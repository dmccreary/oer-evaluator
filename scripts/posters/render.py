#!/usr/bin/env python3
"""Render poster SVGs to PNG with headless Chromium.

    render.py review OUT_DIR [slug ...]   full-size 1200x700 PNGs for visual review
    render.py thumbs [slug ...]           800 px wide gallery thumbnails into docs/sims/<slug>/<slug>.png
                                          (docs/posters/<slug>/ for specs whose META sets home='posters')
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
DOCS = HERE.parents[1] / 'docs'
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / 'specs'))


def slugs(wanted):
    """(slug, poster directory) for each spec, optionally limited to the wanted slugs."""
    import importlib
    out = []
    for p in sorted((HERE / 'specs').glob('p[0-9][0-9]_*.py')):
        meta = importlib.import_module(p.stem).META
        s = meta['slug']
        if not wanted or s in wanted:
            out.append((s, DOCS / meta.get('home', 'sims') / s))
    return out


def main():
    mode = sys.argv[1]
    if mode == 'review':
        out = pathlib.Path(sys.argv[2])
        out.mkdir(parents=True, exist_ok=True)
        wanted = set(sys.argv[3:])
        width = 1200
    else:
        wanted = set(sys.argv[2:])
        width = 800
    with sync_playwright() as p:
        b = p.chromium.launch()
        for s, home in slugs(wanted):
            svg = home / (s + '.svg')
            pg = b.new_page(viewport={'width': width, 'height': round(700 * width / 1200)})
            html = '<body style="margin:0"><img src="file://%s" style="width:%dpx;display:block"></body>' % (svg, width)
            tmp = HERE / '.render.html'
            tmp.write_text(html)
            pg.goto('file://' + str(tmp))
            pg.wait_for_timeout(150)
            target = (out / (s + '.png')) if mode == 'review' else (home / (s + '.png'))
            pg.screenshot(path=str(target))
            pg.close()
            print('rendered', target)
        b.close()
        (HERE / '.render.html').unlink(missing_ok=True)


if __name__ == '__main__':
    main()
