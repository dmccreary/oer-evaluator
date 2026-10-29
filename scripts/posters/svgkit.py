"""Small SVG drawing kit for the OER Evaluator overlay posters.

Everything is drawn in code, so numbers and wording stay exact. Text is measured
with real font metrics so wrapped lines fit their boxes, and every text call
records a warning when it cannot fit.
"""
import html
import math

from PIL import ImageFont

# ---- book palette (matches the Ten-Metric Rubric Map sim) ------------------
INK = '#1b2a41'
MUTED = '#4a5666'
Q, QD, QL = '#2c6fb7', '#1d4f86', '#d6e6f7'      # quality metrics
R, RD, RL = '#7b4aa5', '#573379', '#e8dcf3'      # reusability metrics
ORANGE, ORANGED, ORANGEL = '#e69500', '#8a5a00', '#fff3b0'
GREEN, GREEND, GREENL = '#2e7d32', '#1b5e20', '#c8e6c9'
RED, REDD, REDL = '#b71c1c', '#7f1313', '#ffcdd2'
TEAL, TEALD, TEALL = '#00796b', '#004d40', '#d2efe9'
GRAY, GRAYL, GRAYM = '#6b7785', '#eef1f5', '#c9d1db'
PAPER = '#f7f9fc'
WHITE = '#ffffff'

FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "Menlo, Consolas, Courier New, monospace"

_REG = '/System/Library/Fonts/Supplemental/Arial.ttf'
_BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
_fonts = {}


def tw(s, size, weight='normal', mono=False):
    """Estimated rendered width of s at the given size (6% safety margin)."""
    if mono:
        return len(s) * size * 0.62
    key = 'b' if weight in ('bold', '600', '700', '800') else 'r'
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(_BOLD if key == 'b' else _REG, 100)
    return _fonts[key].getlength(s) * size / 100.0 * 1.06


def esc(s):
    return html.escape(str(s), quote=True)


def _f(v):
    return ('%.1f' % v).rstrip('0').rstrip('.')


class Canvas:
    def __init__(self, w=1200, h=700, title='', desc='', bg=PAPER):
        self.w, self.h = w, h
        self.title, self.desc, self.bg = title, desc, bg
        self.parts = []
        self.warnings = []

    # ---- raw ---------------------------------------------------------------
    def raw(self, s):
        self.parts.append(s)

    def _attrs(self, fill, stroke, sw, dash, opacity, extra):
        a = ' fill="%s"' % fill
        if stroke:
            a += ' stroke="%s" stroke-width="%s"' % (stroke, _f(sw))
        if dash:
            a += ' stroke-dasharray="%s"' % dash
        if opacity is not None:
            a += ' opacity="%s"' % opacity
        return a + (' ' + extra if extra else '')

    # ---- shapes ------------------------------------------------------------
    def rect(self, x, y, w, h, fill='none', stroke=None, sw=2, rx=0, dash=None, opacity=None, extra=''):
        self.raw('<rect x="%s" y="%s" width="%s" height="%s" rx="%s"%s/>' % (
            _f(x), _f(y), _f(w), _f(h), _f(rx), self._attrs(fill, stroke, sw, dash, opacity, extra)))

    def circle(self, cx, cy, r, fill='none', stroke=None, sw=2, dash=None, opacity=None, extra=''):
        self.raw('<circle cx="%s" cy="%s" r="%s"%s/>' % (
            _f(cx), _f(cy), _f(r), self._attrs(fill, stroke, sw, dash, opacity, extra)))

    def ellipse(self, cx, cy, rx, ry, fill='none', stroke=None, sw=2, dash=None, opacity=None, extra=''):
        self.raw('<ellipse cx="%s" cy="%s" rx="%s" ry="%s"%s/>' % (
            _f(cx), _f(cy), _f(rx), _f(ry), self._attrs(fill, stroke, sw, dash, opacity, extra)))

    def line(self, x1, y1, x2, y2, stroke=INK, sw=2, dash=None, cap='round', opacity=None):
        a = ' stroke="%s" stroke-width="%s" stroke-linecap="%s"' % (stroke, _f(sw), cap)
        if dash:
            a += ' stroke-dasharray="%s"' % dash
        if opacity is not None:
            a += ' opacity="%s"' % opacity
        self.raw('<line x1="%s" y1="%s" x2="%s" y2="%s"%s/>' % (_f(x1), _f(y1), _f(x2), _f(y2), a))

    def poly(self, pts, fill='none', stroke=None, sw=2, dash=None, opacity=None, join='round'):
        p = ' '.join('%s,%s' % (_f(x), _f(y)) for x, y in pts)
        a = self._attrs(fill, stroke, sw, dash, opacity, 'stroke-linejoin="%s"' % join)
        self.raw('<polygon points="%s"%s/>' % (p, a))

    def path(self, d, fill='none', stroke=None, sw=2, dash=None, opacity=None, cap='round', join='round'):
        a = self._attrs(fill, stroke, sw, dash, opacity,
                        'stroke-linecap="%s" stroke-linejoin="%s"' % (cap, join))
        self.raw('<path d="%s"%s/>' % (d, a))

    def arrow(self, x1, y1, x2, y2, stroke=INK, sw=3, head=12, dash=None, both=False):
        ang = math.atan2(y2 - y1, x2 - x1)
        bx, by = x2 - head * 0.8 * math.cos(ang), y2 - head * 0.8 * math.sin(ang)
        sx, sy = x1, y1
        if both:
            sx, sy = x1 + head * 0.8 * math.cos(ang), y1 + head * 0.8 * math.sin(ang)
        self.line(sx, sy, bx, by, stroke, sw, dash, cap='butt')
        self._head(x2, y2, ang, head, stroke)
        if both:
            self._head(x1, y1, ang + math.pi, head, stroke)

    def _head(self, x, y, ang, head, fill):
        a1, a2 = ang + math.radians(150), ang - math.radians(150)
        self.poly([(x, y), (x + head * math.cos(a1), y + head * math.sin(a1)),
                   (x + head * math.cos(a2), y + head * math.sin(a2))], fill=fill, join='miter')

    def curve_arrow(self, x1, y1, cx, cy, x2, y2, stroke=INK, sw=3, head=12, dash=None):
        """Quadratic curve with a head at the end."""
        ang = math.atan2(y2 - cy, x2 - cx)
        bx, by = x2 - head * 0.8 * math.cos(ang), y2 - head * 0.8 * math.sin(ang)
        self.path('M%s,%s Q%s,%s %s,%s' % (_f(x1), _f(y1), _f(cx), _f(cy), _f(bx), _f(by)),
                  stroke=stroke, sw=sw, dash=dash, cap='butt')
        self._head(x2, y2, ang, head, stroke)

    # ---- text --------------------------------------------------------------
    def text(self, x, y, s, size=18, weight='normal', fill=INK, anchor='start', italic=False,
             maxw=None, mono=False, minsize=None, spacing=None):
        """Draw one line. With maxw the size shrinks (down to minsize) to fit; else warns."""
        if maxw:
            ms = minsize or max(12, size * 0.8)
            while tw(s, size, weight, mono) > maxw and size > ms:
                size -= 0.5
            if tw(s, size, weight, mono) > maxw:
                self.warnings.append('overflow %.0f>%.0f: %r' % (tw(s, size, weight, mono), maxw, s))
        a = 'x="%s" y="%s" font-size="%s" fill="%s"' % (_f(x), _f(y), _f(size), fill)
        if weight != 'normal':
            a += ' font-weight="%s"' % weight
        if anchor != 'start':
            a += ' text-anchor="%s"' % anchor
        if italic:
            a += ' font-style="italic"'
        if mono:
            a += ' font-family="%s"' % MONO
        if spacing:
            a += ' letter-spacing="%s"' % spacing
        self.raw('<text %s>%s</text>' % (a, esc(s)))
        return size

    def wrap(self, s, width, size, weight='normal', mono=False):
        words, lines, cur = str(s).split(), [], ''
        for w in words:
            t = (cur + ' ' + w).strip()
            if tw(t, size, weight, mono) <= width or not cur:
                cur = t
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def para(self, x, y, s, width, size=18, lh=1.28, weight='normal', fill=INK, anchor='start',
             italic=False, maxlines=None, mono=False, maxh=None):
        """Wrapped paragraph; y is the first baseline. Returns the next baseline."""
        lines = self.wrap(s, width, size, weight, mono)
        if maxlines and len(lines) > maxlines:
            self.warnings.append('too many lines (%d>%d): %r' % (len(lines), maxlines, s[:40]))
        if maxh and y + (len(lines) - 1) * size * lh > y + maxh:
            self.warnings.append('para taller than %d: %r' % (maxh, s[:40]))
        for ln in lines:
            self.text(x, y, ln, size, weight, fill, anchor, italic, mono=mono)
            y += size * lh
        return y

    def lines_h(self, s, width, size, lh=1.28, weight='normal'):
        return len(self.wrap(s, width, size, weight)) * size * lh

    def bullets(self, x, y, items, width, size=17, lh=1.25, gap=6, fill=INK, dot=None, weight='normal'):
        for it in items:
            self.circle(x + 5, y - size * 0.32, 3.2, fill=dot or fill)
            y = self.para(x + 18, y, it, width - 18, size, lh, weight, fill) + gap
        return y

    def chip(self, x, y, s, fill=Q, color=WHITE, size=15, weight='bold', padx=10, h=None,
             anchor='start', rx=None, stroke=None):
        w = tw(s, size, weight) + 2 * padx
        h = h or size + 12
        x0 = x - w / 2 if anchor == 'middle' else (x - w if anchor == 'end' else x)
        self.rect(x0, y, w, h, fill=fill, stroke=stroke, sw=1.5, rx=rx if rx is not None else h / 2)
        self.text(x0 + w / 2, y + h / 2 + size * 0.34, s, size, weight, color, 'middle')
        return x0, w

    # ---- coordinates for overlay data -------------------------------------
    def pct(self, x1, y1, x2, y2):
        return {'x1': round(x1 / self.w * 100, 1), 'y1': round(y1 / self.h * 100, 1),
                'x2': round(x2 / self.w * 100, 1), 'y2': round(y2 / self.h * 100, 1)}

    def pt(self, x, y):
        return round(x / self.w * 100, 1), round(y / self.h * 100, 1)

    # ---- output ------------------------------------------------------------
    def svg(self):
        head = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" '
                'font-family="%s" role="img">\n' % (self.w, self.h, self.w, self.h, FONT))
        head += '<title>%s</title>\n<desc>%s</desc>\n' % (esc(self.title), esc(self.desc))
        head += '<rect width="%d" height="%d" fill="%s"/>\n' % (self.w, self.h, self.bg)
        return head + '\n'.join(self.parts) + '\n</svg>\n'


# ---- icons (drawn around a center point; r is the half-size) ---------------

def ic_check(c, cx, cy, r=14, fill=GREEN):
    c.circle(cx, cy, r, fill=fill)
    c.path('M%s,%s L%s,%s L%s,%s' % (_f(cx - r * .45), _f(cy), _f(cx - r * .1), _f(cy + r * .38),
                                      _f(cx + r * .5), _f(cy - r * .38)), stroke=WHITE, sw=max(2, r * .22))


def ic_cross(c, cx, cy, r=14, fill=RED):
    c.circle(cx, cy, r, fill=fill)
    d = r * .4
    c.line(cx - d, cy - d, cx + d, cy + d, WHITE, max(2, r * .22))
    c.line(cx - d, cy + d, cx + d, cy - d, WHITE, max(2, r * .22))


def ic_stop(c, cx, cy, r=14, fill=RED):
    pts = [(cx + r * math.cos(math.radians(22.5 + 45 * i)), cy + r * math.sin(math.radians(22.5 + 45 * i)))
           for i in range(8)]
    c.poly(pts, fill=fill)
    c.rect(cx - r * .5, cy - r * .12, r, r * .24, fill=WHITE, rx=2)


def ic_warn(c, cx, cy, r=14, fill=ORANGE, ink=INK):
    c.poly([(cx, cy - r), (cx + r * 1.05, cy + r * .8), (cx - r * 1.05, cy + r * .8)], fill=fill)
    c.line(cx, cy - r * .3, cx, cy + r * .25, ink, max(2, r * .2))
    c.circle(cx, cy + r * .55, r * .09 + 1, fill=ink)


def ic_pencil(c, cx, cy, r=14, fill=ORANGE):
    c.circle(cx, cy, r, fill=fill)
    c.poly([(cx - r * .45, cy + r * .45), (cx - r * .4, cy + r * .1), (cx + r * .25, cy - r * .55),
            (cx + r * .55, cy - r * .25), (cx - r * .1, cy + r * .4)], fill=INK)


def ic_lock(c, cx, cy, r=14, open_=False, fill=INK):
    c.rect(cx - r * .7, cy - r * .1, r * 1.4, r * 1.0, fill=fill, rx=r * .15)
    if open_:
        c.path('M%s,%s v%s a%s,%s 0 0 1 %s,0 v%s' % (_f(cx + r * .35), _f(cy - r * .1), _f(-r * .25),
                                                     _f(r * .35), _f(r * .35), _f(r * .7), _f(r * .15)),
               stroke=fill, sw=max(2.5, r * .2))
    else:
        c.path('M%s,%s v%s a%s,%s 0 0 1 %s,0 v%s' % (_f(cx - r * .35), _f(cy - r * .1), _f(-r * .3),
                                                     _f(r * .35), _f(r * .35), _f(r * .7), _f(r * .3)),
               stroke=fill, sw=max(2.5, r * .2))
    c.circle(cx, cy + r * .35, r * .12, fill=WHITE)


def ic_person(c, cx, cy, r=14, fill=INK):
    c.circle(cx, cy - r * .45, r * .38, fill=fill)
    c.path('M%s,%s a%s,%s 0 0 1 %s,0 z' % (_f(cx - r * .7), _f(cy + r * .85), _f(r * .7), _f(r * .85), _f(r * 1.4)),
           fill=fill)


def ic_doc(c, x, y, w=60, h=76, fill=WHITE, stroke=INK, label=None, lsize=None, lfill=INK, fold=None):
    f = fold or w * .28
    c.poly([(x, y), (x + w - f, y), (x + w, y + f), (x + w, y + h), (x, y + h)], fill=fill, stroke=stroke, sw=2.5)
    c.poly([(x + w - f, y), (x + w - f, y + f), (x + w, y + f)], fill=GRAYM, stroke=stroke, sw=2)
    if label:
        s = lsize or min(22, w * .3)
        c.text(x + w / 2, y + h * .66, label, s, 'bold', lfill, 'middle', maxw=w - 8)


def ic_lines(c, x, y, w, n=3, gap=9, stroke=GRAYM, sw=3):
    for i in range(n):
        c.line(x, y + i * gap, x + (w if i < n - 1 else w * .6), y + i * gap, stroke, sw)


def ic_magnifier(c, cx, cy, r=16, stroke=INK):
    c.circle(cx - r * .15, cy - r * .15, r * .6, fill=WHITE, stroke=stroke, sw=max(2.5, r * .18))
    c.line(cx + r * .3, cy + r * .3, cx + r * .85, cy + r * .85, stroke, max(3, r * .24))


def ic_clock(c, cx, cy, r=16, stroke=INK, fill=WHITE):
    c.circle(cx, cy, r, fill=fill, stroke=stroke, sw=2.5)
    c.line(cx, cy, cx, cy - r * .6, stroke, 2.5)
    c.line(cx, cy, cx + r * .45, cy + r * .2, stroke, 2.5)


def ic_calendar(c, cx, cy, r=16, stroke=INK, fill=WHITE, head=RED):
    c.rect(cx - r, cy - r * .85, r * 2, r * 1.8, fill=fill, stroke=stroke, sw=2.5, rx=3)
    c.rect(cx - r, cy - r * .85, r * 2, r * .5, fill=head, stroke=stroke, sw=2.5, rx=3)
    for i in range(3):
        for j in range(2):
            c.rect(cx - r * .7 + i * r * .55, cy - r * .1 + j * r * .5, r * .3, r * .3, fill=stroke)


def ic_link(c, cx, cy, r=16, stroke=INK):
    c.rect(cx - r * 1.0, cy - r * .35, r * 1.2, r * .7, fill='none', stroke=stroke, sw=max(2.5, r * .2), rx=r * .35)
    c.rect(cx - r * .2, cy - r * .35, r * 1.2, r * .7, fill='none', stroke=stroke, sw=max(2.5, r * .2), rx=r * .35)


def ic_eye(c, cx, cy, r=16, stroke=INK):
    c.path('M%s,%s Q%s,%s %s,%s Q%s,%s %s,%s z' % (_f(cx - r), _f(cy), _f(cx), _f(cy - r * .9), _f(cx + r), _f(cy),
                                                   _f(cx), _f(cy + r * .9), _f(cx - r), _f(cy)),
           fill=WHITE, stroke=stroke, sw=2.5)
    c.circle(cx, cy, r * .3, fill=stroke)


def ic_speaker(c, cx, cy, r=16, stroke=INK):
    c.poly([(cx - r * .8, cy - r * .3), (cx - r * .35, cy - r * .3), (cx + r * .1, cy - r * .7),
            (cx + r * .1, cy + r * .7), (cx - r * .35, cy + r * .3), (cx - r * .8, cy + r * .3)], fill=stroke)
    c.path('M%s,%s q%s,%s 0,%s' % (_f(cx + r * .4), _f(cy - r * .35), _f(r * .3), _f(r * .35), _f(r * .7)), stroke=stroke, sw=2.5)
    c.path('M%s,%s q%s,%s 0,%s' % (_f(cx + r * .65), _f(cy - r * .65), _f(r * .55), _f(r * .65), _f(r * 1.3)), stroke=stroke, sw=2.5)


def ic_shield(c, cx, cy, r=16, fill=TEAL):
    c.path('M%s,%s L%s,%s L%s,%s Q%s,%s %s,%s Q%s,%s %s,%s z' % (
        _f(cx - r * .8), _f(cy - r * .7), _f(cx), _f(cy - r), _f(cx + r * .8), _f(cy - r * .7),
        _f(cx + r * .8), _f(cy + r * .5), _f(cx), _f(cy + r),
        _f(cx - r * .8), _f(cy + r * .5), _f(cx - r * .8), _f(cy - r * .7)), fill=fill)
    c.path('M%s,%s L%s,%s L%s,%s' % (_f(cx - r * .3), _f(cy), _f(cx - r * .05), _f(cy + r * .28), _f(cx + r * .35), _f(cy - r * .22)),
           stroke=WHITE, sw=max(2.5, r * .18))


def ic_bubble(c, x, y, w, h, fill=WHITE, stroke=INK, tail='left', sw=2.5):
    c.rect(x, y, w, h, fill=fill, stroke=stroke, sw=sw, rx=10)
    if tail == 'left':
        c.poly([(x + 2, y + h * .35), (x - 14, y + h * .5), (x + 2, y + h * .65)], fill=fill, stroke=stroke, sw=sw)
        c.line(x + sw / 2, y + h * .38, x + sw / 2, y + h * .62, fill, sw + 1, cap='butt')


def ic_folder(c, x, y, w=70, h=52, fill=ORANGEL, stroke=INK):
    c.poly([(x, y + 8), (x + w * .38, y + 8), (x + w * .46, y), (x + w * .72, y), (x + w * .78, y + 8),
            (x + w, y + 8), (x + w, y + h), (x, y + h)], fill=fill, stroke=stroke, sw=2.5)


def ic_gear(c, cx, cy, r=16, fill=GRAY):
    for i in range(8):
        a = math.radians(i * 45)
        c.circle(cx + r * .82 * math.cos(a), cy + r * .82 * math.sin(a), r * .24, fill=fill)
    c.circle(cx, cy, r * .72, fill=fill)
    c.circle(cx, cy, r * .3, fill=WHITE)


def ic_star(c, cx, cy, r=14, fill=ORANGE):
    pts = []
    for i in range(10):
        rad = r if i % 2 == 0 else r * .45
        a = math.radians(-90 + i * 36)
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    c.poly(pts, fill=fill)


def ic_wrench(c, cx, cy, r=16, fill=INK):
    c.line(cx - r * .7, cy + r * .7, cx + r * .2, cy - r * .2, fill, max(4, r * .35))
    c.circle(cx + r * .4, cy - r * .4, r * .45, fill=fill)
    c.circle(cx + r * .55, cy - r * .55, r * .2, fill=WHITE)


def ic_scissors(c, cx, cy, r=16, stroke=INK):
    c.line(cx - r * .6, cy + r * .6, cx + r * .7, cy - r * .7, stroke, 3)
    c.line(cx - r * .6, cy - r * .6, cx + r * .7, cy + r * .7, stroke, 3)
    c.circle(cx - r * .65, cy + r * .65, r * .25, fill=WHITE, stroke=stroke, sw=2.5)
    c.circle(cx - r * .65, cy - r * .65, r * .25, fill=WHITE, stroke=stroke, sw=2.5)


def ic_scale(c, cx, cy, w=170, tilt=0, left=None, right=None, stroke=INK):
    """Balance scale. tilt in degrees (positive = right pan lower)."""
    c.line(cx, cy + 62, cx, cy - 28, stroke, 5)
    c.rect(cx - 36, cy + 58, 72, 12, fill=stroke, rx=3)
    a = math.radians(tilt)
    dx, dy = (w / 2) * math.cos(a), (w / 2) * math.sin(a)
    lx, ly, rx, ry = cx - dx, cy - 28 - dy, cx + dx, cy - 28 + dy
    c.line(lx, ly, rx, ry, stroke, 5)
    c.circle(cx, cy - 28, 7, fill=stroke)
    for px, py in ((lx, ly), (rx, ry)):
        c.line(px, py, px - 28, py + 40, stroke, 2)
        c.line(px, py, px + 28, py + 40, stroke, 2)
        c.path('M%s,%s h56 a28,18 0 0 1 -56,0 z' % (_f(px - 28), _f(py + 40)), fill=GRAYL, stroke=stroke, sw=2.5)
    return (lx, ly + 40), (rx, ry + 40)


def stripe_defs(c, pid='hatch', color=GRAY, bg=WHITE):
    c.raw('<defs><pattern id="%s" width="8" height="8" patternUnits="userSpaceOnUse" '
          'patternTransform="rotate(45)"><rect width="8" height="8" fill="%s"/>'
          '<line x1="0" y1="0" x2="0" y2="8" stroke="%s" stroke-width="3"/></pattern></defs>' % (pid, bg, color))


def title_block(c, title, sub=None, x=40, y=50, size=32):
    c.text(x, y, title, size, 'bold', INK, maxw=c.w - 2 * x)
    if sub:
        c.text(x, y + 30, sub, 18, 'normal', MUTED, maxw=c.w - 2 * x)
