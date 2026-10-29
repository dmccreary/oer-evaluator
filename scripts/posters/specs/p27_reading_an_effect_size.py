"""Poster 27: Reading an Effect Size (Chapter 17, grid, 3 curve panels plus a caution strip). Curves drawn from the normal density."""
import math

from svgkit import *

CH = '17-ab-testing-analysis'

META = dict(
    slug='reading-an-effect-size',
    title='Reading an Effect Size',
    chapter=CH,
    overlay='grid',
    topic='What Cohen\'s d of 0.2, 0.5, and 0.8 look like',
    desc='Three pairs of overlapping bell curves show d of 0.2 (small), 0.5 (medium), and 0.8 (large), with a caution about a pilot whose d was about 1.03.',
    intro=('Effect size is the hardest idea in the second half of the book for readers without statistics. Overlapping curves give the intuition without algebra. '
           'Each panel shows the control group as one curve and the treatment group as the other, with the two means marked and the overlap shaded. The more the curves separate, the larger d. '
           'All three panels use the same axes, and the curves are drawn from the normal density. The sizes are rules of thumb, and what counts as important depends on the cost of the change and the setting. '
           'The caution strip carries the Watershed Basics pilot: a difference of 7.0 over a pooled standard deviation of about 6.78 gives d of about 1.03, and a big number from a small test deserves a second look.'),
    alt=('Three pairs of overlapping bell curves on the same axes. Small: d = 0.2, the treatment curve sits just to the right of the control curve and almost all of it overlaps. '
         'Medium: d = 0.5, the curves are clearly offset with a large overlap. Large: d = 0.8, the curves are further apart with less overlap. '
         'Under the curves the formula reads d = (mean of treatment minus mean of control) / pooled standard deviation. '
         'A caution strip says the pilot difference of 7.0 over a pooled standard deviation of about 6.78 gives d of about 1.03, from only 12 students per group, which deserves a second look.'),
    bloom='Understand',
    objective='**interpret** d values of 0.2, 0.5, and 0.8 as the overlap between two groups, and **explain** why a large d from a small test deserves caution.',
    objective_plain='interpret d values of 0.2, 0.5, and 0.8 as the overlap between two groups, and explain why a large d from a small test deserves caution.',
    prereq=['Means, spread, and effect size from [Chapter 17](../../chapters/17-ab-testing-analysis/index.md).'],
    activities=[
        '**Explore (3 min).** Press each panel. How much of the control curve is still overlapped at d = 0.8?',
        '**Quiz (3 min).** Press **Quiz Me** and match four descriptions to the panels.',
        '**Compute (4 min).** Use the formula for a difference of 4.0 and a pooled standard deviation of 8.0. Which panel is closest?',
    ],
    assessment=[
        ('What does d measure?', 'The difference of the two group means in units of the pooled standard deviation.'),
        ('What size is d = 0.5 by convention?', 'Medium, a rule of thumb.'),
        ('Why is the pilot\'s d of about 1.03 not the number to plan the next test on?', 'A small pilot gives a noisy estimate, and impressive estimates from small tests tend to shrink when repeated.'),
    ],
    connection='Effect size is how Chapter 17 puts a difference on a common ruler. A teacher can compare tests with different spreads.',
    ref_nums=[(CH, [1, 6, 7, 4])],
    key_questions=['How far apart are the group means, in units of spread?', 'How many students are behind this number?'],
    misconceptions=['A bigger difference always means a bigger effect', 'A large d from a small test is a sure thing'],
    good=['The curves are normal densities with equal spread, drawn in code. The d labels are rules of thumb and not cutoffs.'],
    verify=[(CH, 'd = (mean of treatment - mean of control) / pooled standard deviation'),
            (CH, 'By convention, a *d* of 0.2 is called small, 0.5 medium, and 0.8 large.'),
            (CH, 'their square root is 6.78'.replace('their', 'whose')),
            (CH, 'about **1.03**'),
            (CH, 'impressive estimates from small tests tend to shrink when repeated with more students')],
)

CTRL, TREAT = '#6b7785', '#00796b'


def pdf(x, mu):
    return math.exp(-0.5 * (x - mu) ** 2) / math.sqrt(2 * math.pi)


def curve_pts(x0, base, sx, sy, mu, lo=-3.2, hi=4.2, n=120):
    return [(x0 + (lo + (hi - lo) * i / n - lo) * sx, base - pdf(lo + (hi - lo) * i / n, mu) * sy) for i in range(n + 1)]


PANELS = [
    ('small', 'Small', 0.2, '#1d4f86'),
    ('medium', 'Medium', 0.5, '#8a5a00'),
    ('large', 'Large', 0.8, '#573379'),
]


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Reading an Effect Size', 'The more the two curves separate, the larger d. Same axes in every panel.')
    stripe_defs(c, 'overlap', '#e6a8a8', '#ffffff')
    n, gap = 3, 14
    x0, x1, y0, y1 = 30, 1170, 104, 490
    w = (x1 - x0 - gap * (n - 1)) / n
    lo, hi = -3.2, 4.2
    sx = (w - 40) / (hi - lo)
    sy = 400
    items = []
    for i, (zid, name, d, hue) in enumerate(PANELS):
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 50, fill=hue, rx=14)
        c.rect(x, y0 + 26, w, 24, fill=hue)
        c.text(x + 16, y0 + 33, '%s: d = %s' % (name, d), 23, 'bold', WHITE)
        base = y0 + 300
        ox = x + 20
        # overlap polygon (minimum of both curves)
        pts = []
        N = 140
        for k in range(N + 1):
            t = lo + (hi - lo) * k / N
            pts.append((ox + (t - lo) * sx, base - min(pdf(t, 0), pdf(t, d)) * sy))
        c.poly([(ox, base)] + pts + [(ox + (hi - lo) * sx, base)], fill='url(#overlap)', stroke=None)
        c.path('M' + ' L'.join('%.1f,%.1f' % p for p in curve_pts(ox, base, sx, sy, 0)), stroke=CTRL, sw=4)
        c.path('M' + ' L'.join('%.1f,%.1f' % p for p in curve_pts(ox, base, sx, sy, d)), stroke=TREAT, sw=4)
        c.line(ox, base, ox + (hi - lo) * sx, base, INK, 2.5)
        for mu, col, lab, dy in ((0, CTRL, 'control mean', -8), (d, TREAT, 'treatment mean', -8)):
            mx = ox + (mu - lo) * sx
            c.line(mx, base - pdf(mu, mu) * sy - 6, mx, base + 8, col, 2.5, '5 4')
        c.chip(ox + (0 - lo) * sx - 8, base + 22, 'control', fill=CTRL, size=14, h=24, anchor='end')
        c.chip(ox + (d - lo) * sx + 8, base + 22, 'treatment', fill=TREAT, size=14, h=24, anchor='start')
        c.text(x + w / 2, y0 + 366, 'Shaded overlap: groups that look alike', 15, 'normal', MUTED, 'middle', maxw=w - 20)
        items.append(dict(id=zid, label='%s: d = %s' % (name, d), color=hue, box=(x, y0, x + w, y1),
                          summary='d = %s is called %s by convention, a rule of thumb.' % (d, name.lower()),
                          facts=['The treatment mean sits %s pooled standard deviations above the control mean.' % d,
                                 'The shaded part is where the two groups overlap.', 'What counts as important depends on the cost of the change and the setting.']))
    # formula
    c.rect(30, 502, 1140, 56, fill=GRAYL, stroke=GRAY, sw=2.5, rx=12)
    c.text(600, 540, 'd = (mean of treatment − mean of control) / pooled standard deviation', 25, 'bold', INK, 'middle', maxw=1100)
    # caution strip
    cy0, cy1 = 572, 680
    c.rect(30, cy0, 1140, cy1 - cy0, fill='#fff7e6', stroke=ORANGE, sw=3, rx=14)
    ic_warn(c, 70, cy0 + 54, 26, ORANGE)
    c.text(116, cy0 + 36, 'Caution: a big number from a small test', 22, 'bold', INK)
    c.para(116, cy0 + 64, 'The Watershed Basics pilot: a difference of 7.0 over a pooled standard deviation of about 6.78 gives d of about 1.03. '
           'With only 12 students per group, an impressive estimate often shrinks when the test is repeated with more students.', 1020, 16.5, 1.25, 'normal', INK, maxlines=3)
    items.append(dict(id='pilot-caution', label='Caution: a pilot with d about 1.03', color=ORANGE, box=(30, 572, 1170, 680),
                      summary='A d of about 1.03 from 12 students per group deserves a second look.',
                      facts=['Mean gains: control 15.0, treatment 22.0, a difference of 7.0.', 'Pooled standard deviation is about 6.78, so d = 7.0 / 6.78, about 1.03.',
                             'By convention 1.03 is large, but a small pilot gives a noisy estimate.',
                             'Plan the next test for about half the pilot\'s effect, not for the pilot\'s own number.']))
    quiz = [
        dict(question='Which panel shows two groups that overlap the most?', correct_zone='small', explanation='d = 0.2 is the smallest separation.'),
        dict(question='Which panel shows the curves furthest apart, with the least overlap?', correct_zone='large', explanation='d = 0.8 is a large effect by convention.'),
        dict(question='Which panel is called medium by the usual rule of thumb?', correct_zone='medium', explanation='d = 0.5.'),
        dict(question='Which zone warns about an impressive estimate from only 12 students per group?', correct_zone='pilot-caution', explanation='Small pilots tend to overstate effect size.'),
    ]
    return c, items, quiz
