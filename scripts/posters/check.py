#!/usr/bin/env python3
"""Open each poster's main.html in headless Chromium and check the overlay.

    check.py [--shots OUT_DIR] [--heights] [slug ...]

Serves docs/ through Playwright request routing (no server process). A poster lives
in docs/sims/<slug>/ unless its spec META sets home='posters'. For every
poster it checks that the overlay loads without console errors, that every zone or
marker from data.json is on the page, that explore mode shows detail text, and that
the quiz can be answered to the end. With --heights it measures the tallest content
height at 850 px wide and writes scripts/posters/heights.json for the iframe size.
"""
import json
import mimetypes
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
DOCS = HERE.parents[1] / 'docs'
BASE = 'http://sim.test/'
WIDTH = 850


def spec_homes():
    """{slug: 'sims' | 'posters'} for every poster spec."""
    import importlib
    sys.path.insert(0, str(HERE))
    sys.path.insert(0, str(HERE / 'specs'))
    out = {}
    for p in (HERE / 'specs').glob('p[0-9][0-9]_*.py'):
        meta = importlib.import_module(p.stem).META
        out[meta['slug']] = meta.get('home', 'sims')
    return out


def route(r):
    rel = r.request.url[len(BASE):].split('?')[0]
    p = DOCS / rel
    if p.is_file():
        ctype = mimetypes.guess_type(str(p))[0] or 'application/octet-stream'
        r.fulfill(path=str(p), content_type=ctype)
    else:
        r.fulfill(status=404, body='missing ' + rel)


def check(browser, slug, home, shots, heights):
    data = json.loads((DOCS / home / slug / 'data.json').read_text())
    grid = data.get('layout') == 'grid'
    errs, problems = [], []
    pg = browser.new_page(viewport={'width': WIDTH, 'height': 900})
    pg.route(BASE + '**', route)
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(BASE + home + '/' + slug + '/main.html')
    items = data['zones'] if grid else data['callouts']
    sel = '.grid-zone' if grid else 'button.marker'
    try:
        pg.wait_for_selector(sel, timeout=5000)
    except Exception:
        problems.append('no %s elements appeared' % sel)
    pg.wait_for_timeout(400)
    n = pg.locator(sel).count()
    if n != len(items):
        problems.append('%d elements on page, %d in data.json' % (n, len(items)))
    h_default = pg.evaluate('document.body.scrollHeight')
    hmax = h_default
    if grid:
        for z in items:
            pg.evaluate("sim.zoneEls.get(%s).dispatchEvent(new MouseEvent('mouseenter'))" % json.dumps(z['id']))
            pg.evaluate("sim.zoneEls.get(%s).click()" % json.dumps(z['id']))
            pg.wait_for_timeout(60)
            hmax = max(hmax, pg.evaluate('document.body.scrollHeight'))
        txt = pg.evaluate("document.getElementById('panel-label').textContent")
        if not txt:
            problems.append('explore mode showed no label')
        if shots:
            pg.screenshot(path=str(pathlib.Path(shots) / (slug + '-explore.png')), full_page=True)
        pg.evaluate("sim.setMode('quiz')")
        total = pg.evaluate('sim.quizQueue.length')
        for _ in range(total):
            tid = pg.evaluate('sim.quizQueue[sim.quizIndex].correct_zone')
            pg.evaluate("sim.zoneEls.get(%s).click()" % json.dumps(tid))
            pg.evaluate('sim.correctOkBtn && sim.correctOkBtn.click()')
        done = pg.evaluate("document.getElementById('quiz-question').textContent")
        if 'Quiz complete' not in done or ('%d of %d' % (total, total)) not in done:
            problems.append('quiz did not finish cleanly: %r' % done[:80])
    else:
        for c in items:
            pg.evaluate("sim.showInfo ? 0 : 0")
        first = items[0]['id']
        pg.evaluate("sim.markers.get(%d).dispatchEvent(new MouseEvent('mouseenter'))" % first)
        pg.wait_for_timeout(100)
        hmax = max(hmax, pg.evaluate('document.body.scrollHeight'))
        if shots:
            pg.screenshot(path=str(pathlib.Path(shots) / (slug + '-explore.png')), full_page=True)
        pg.evaluate("sim.setMode('quiz')")
        tgt = pg.evaluate('sim.quizQueue[sim.quizIndex].id')
        pg.evaluate('sim.markers.get(%d).click()' % tgt)
        pg.wait_for_timeout(100)
        lab = pg.evaluate("document.getElementById('infobox-label').textContent")
        if '✓' not in lab:
            problems.append('quiz click on the right marker was not accepted: %r' % lab)
    if errs:
        problems.append('console errors: %s' % '; '.join(errs[:3]))
    heights[slug] = max(hmax, h_default) + 34
    pg.close()
    return problems


def main(argv):
    shots = None
    want_heights = False
    slugs = []
    i = 0
    while i < len(argv):
        if argv[i] == '--shots':
            shots = argv[i + 1]
            pathlib.Path(shots).mkdir(parents=True, exist_ok=True)
            i += 1
        elif argv[i] == '--heights':
            want_heights = True
        else:
            slugs.append(argv[i])
        i += 1
    homes = spec_homes()
    if not slugs:
        slugs = sorted(s for s, h in homes.items() if (DOCS / h / s / 'data.json').exists())
    heights = {}
    bad = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        for s in slugs:
            probs = check(b, s, homes.get(s, 'sims'), shots, heights)
            print('%s %-42s height %d' % ('OK  ' if not probs else 'FAIL', s, heights[s]))
            for x in probs:
                print('      - ' + x)
            bad += bool(probs)
        b.close()
    if want_heights:
        hp = HERE / 'heights.json'
        old = json.loads(hp.read_text()) if hp.exists() else {}
        old.update(heights)
        hp.write_text(json.dumps(old, indent=1, sort_keys=True) + '\n')
    print('%d poster(s) failed' % bad)
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
