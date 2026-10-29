#!/usr/bin/env python3
"""Check text contrast in the poster SVGs.

For every <text> element it renders the SVG, finds the most common color behind the text box, and compares it
with the text fill. Normal text must reach 4.5:1 and large text (24 px, or 18.7 px and bold) must reach 3:1.

    python3 scripts/posters/contrast.py [slug ...]      # default: every poster that has an SVG under docs/sims
"""
import io
import pathlib
import re
import sys
from collections import Counter

from PIL import Image
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
SIMS = HERE.parents[1] / 'docs' / 'sims'


def lum(rgb):
    def ch(v):
        v /= 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def hex_rgb(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def check(page, svg_path):
    page.goto('file://' + str(svg_path))
    vb = page.evaluate("(() => { const s = document.documentElement; return [s.viewBox.baseVal.width, s.viewBox.baseVal.height]; })()")
    page.set_viewport_size({'width': int(vb[0]), 'height': int(vb[1])})
    png = Image.open(io.BytesIO(page.screenshot())).convert('RGB')
    texts = page.evaluate("""Array.from(document.querySelectorAll('text')).map(t => {
        const b = t.getBBox();
        return {s: t.textContent, x: b.x, y: b.y, w: b.width, h: b.height, fill: t.getAttribute('fill'),
                size: parseFloat(t.getAttribute('font-size')), bold: (t.getAttribute('font-weight') || '') === 'bold'};
    })""")
    bad = []
    for t in texts:
        if not t['s'].strip() or not t['fill'] or not t['fill'].startswith('#'):
            continue
        box = (max(0, int(t['x'])), max(0, int(t['y'])), min(png.width, int(t['x'] + t['w']) + 1), min(png.height, int(t['y'] + t['h']) + 1))
        if box[2] <= box[0] or box[3] <= box[1]:
            continue
        px = Counter(png.crop(box).getdata())
        fg = hex_rgb(t['fill'])
        # background: the most common color that is not close to the text color
        bg = next((c for c, _ in px.most_common() if sum(abs(c[i] - fg[i]) for i in range(3)) > 90), None)
        if bg is None:
            continue
        need = 3.0 if (t['size'] >= 24 or (t['bold'] and t['size'] >= 18.66)) else 4.5
        r = ratio(fg, bg)
        if r < need:
            bad.append('%.1f:1 (need %.1f) %r on #%02x%02x%02x, text %s' % (r, need, t['s'][:40], bg[0], bg[1], bg[2], t['fill']))
    return bad


def main(argv):
    svgs = sorted(SIMS.glob('*/*.svg'))
    if argv:
        svgs = [p for p in svgs if p.parent.name in argv]
    total = 0
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        for svg in svgs:
            bad = check(page, svg)
            print('%s %s' % ('OK  ' if not bad else 'LOW ', svg.parent.name))
            for x in bad:
                print('      - ' + x)
            total += len(bad)
        b.close()
    print('%d low-contrast text element(s)' % total)
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main(sys.argv[1:])
