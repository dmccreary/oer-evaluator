"""Poster 5: Five Resources, Five Shapes (Chapter 3, grid, 5 zones). Radar charts drawn from the chapter's scores."""
import math

from svgkit import *

CH = '03-ten-metric-rubric-scoring'

METRICS = ['Accuracy and currency', 'Alignment', 'Readability', 'Accessibility', 'Practice with feedback',
           'Open license', 'Modularity', 'Metadata', 'Editable source', 'Portability']

# Chapter 3 worked example, ordered here from lowest total to highest.
RES = [
    ('Thin Material', [3, 2, 4, 3, 2], [5, 4, 3, 6, 5], 14, 23, 37, 'Weak', 'Reject'),
    ('Watershed Basics', [7, 6, 8, 5, 6], [9, 5, 4, 8, 7], 32, 33, 65, 'Fair', 'Revise'),
    ('Locked Chemistry E-book', [9, 9, 9, 8, 9], [1, 5, 6, 2, 7], 44, 21, 65, 'Fair', 'Revise'),
    ('One Gap', [9, 9, 9, 9, 9], [9, 9, 9, 9, 4], 45, 40, 85, 'Good', 'Revise'),
    ('Open Algebra', [9, 8, 8, 9, 9], [10, 9, 9, 10, 9], 43, 47, 90, 'Excellent', 'Adopt'),
]

META = dict(
    slug='five-resources-five-shapes',
    title='Five Resources, Five Shapes',
    chapter=CH,
    overlay='grid',
    topic='The shape of ten metric scores behind one total',
    desc='Five radar charts, one for each resource in the Chapter 3 total score example, showing that equal totals can hide very different shapes.',
    intro=('This poster draws the five resources from the Chapter 3 total score example as radar charts, from the lowest total to the highest. '
           'Each chart has ten spokes. The five spokes on the right are the quality metrics, drawn as blue circles. The five on the left are the reusability metrics, '
           'drawn as purple squares. A dashed ring marks the floor of 5. Watershed Basics and Locked Chemistry E-book both total 65, yet their shapes look nothing alike. '
           'All five resources are illustrative examples written for the chapter.'),
    alt=('Five radar charts side by side, ordered from the lowest total to the highest. Thin Material: quality 14, reusability 23, total 37, Weak, Reject. '
         'Watershed Basics: 32 and 33, total 65, Fair, Revise; a balanced, middling shape. Locked Chemistry E-book: 44 and 21, total 65, Fair, Revise; '
         'strong on the quality side and collapsed on the reusability side. One Gap: 45 and 40, total 85, Good, Revise; round except for one dent at portability. '
         'Open Algebra: 43 and 47, total 90, Excellent, Adopt; a large, even shape. A bracket joins the two charts with total 65 and reads same total, different shape.'),
    bloom='Analyze',
    objective='**distinguish** resources with the same total score by the shape of their ten metric scores, and name the metric to fix first.',
    objective_plain='distinguish resources with the same total score by the shape of their ten metric scores, and name the metric to fix first.',
    prereq=['The ten metrics and the 0 to 10 scale from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).'],
    activities=[
        '**Explore (3 min).** Press Watershed Basics, then Locked Chemistry E-book. Both total 65. What does each need first?',
        '**Quiz (3 min).** Press **Quiz Me** and find each resource from a description of its shape.',
        '**Plan (4 min).** For each resource, name the one metric you would raise first and say why.',
    ],
    assessment=[
        ('Two resources total 65. Can you say how they differ from the total alone?', 'No. A total hides the split between quality and reusability and the weakest metric.'),
        ('Which resource has nine metrics of 9 and one of 4, and what is its decision?', 'One Gap, total 85, Good, and Revise because one metric is below 5.'),
        ('What does the dashed ring on each chart mark?', 'The floor of 5. Any spoke that dips inside it is a metric below the floor.'),
    ],
    connection=('A shape is learned faster than a table, and the notch in a shape is the first thing to fix. This prepares the improvement rule of Chapter 15: raise the lowest metric first.'),
    ref_nums=[(CH, [1, 7, 6])],
    key_questions=['Which half of the chart is bigger?', 'Which spoke dips inside the floor ring?'],
    misconceptions=['A total of 75 or more always means Adopt', 'Equal totals mean equal resources'],
    good=['The five resources, their scores, and their decisions are illustrative examples from Chapter 3.',
          'The bands and the decision rule are this book\'s starting values, not a standard.'],
    verify=[(CH, '| 1 | Watershed Basics | 7, 6, 8, 5, 6 | 9, 5, 4, 8, 7 | 32 | 33 | 65 | Fair | Revise |'),
            (CH, '| 2 | Open Algebra | 9, 8, 8, 9, 9 | 10, 9, 9, 10, 9 | 43 | 47 | 90 | Excellent | Adopt |'),
            (CH, '| 3 | Locked Chemistry E-book | 9, 9, 9, 8, 9 | 1, 5, 6, 2, 7 | 44 | 21 | 65 | Fair | Revise |'),
            (CH, '| 4 | One Gap | 9, 9, 9, 9, 9 | 9, 9, 9, 9, 4 | 45 | 40 | 85 | Good | Revise |'),
            (CH, '| 5 | Thin Material | 3, 2, 4, 3, 2 | 5, 4, 3, 6, 5 | 14 | 23 | 37 | Weak | Reject |')],
)


def band(t):
    return 'Excellent' if t >= 90 else 'Good' if t >= 75 else 'Fair' if t >= 50 else 'Weak' if t >= 25 else 'Poor'


def decision(t, scores):
    return 'Adopt' if t >= 75 and min(scores) >= 5 else 'Reject' if t < 50 else 'Revise'


def radar(c, cx, cy, rad, scores):
    for ring, dash in ((10, None), (5, '6 5')):
        pts = [(cx + rad * ring / 10 * math.cos(math.radians(-90 + 36 * i)),
                cy + rad * ring / 10 * math.sin(math.radians(-90 + 36 * i))) for i in range(10)]
        c.poly(pts, fill='none', stroke=ORANGE if ring == 5 else GRAYM, sw=2.5 if ring == 5 else 1.5, dash=dash)
    for i in range(10):
        a = math.radians(-90 + 36 * i)
        c.line(cx, cy, cx + rad * math.cos(a), cy + rad * math.sin(a), GRAYM, 1)
    pts = [(cx + rad * s / 10 * math.cos(math.radians(-90 + 36 * i)),
            cy + rad * s / 10 * math.sin(math.radians(-90 + 36 * i))) for i, s in enumerate(scores)]
    c.poly(pts, fill=INK, stroke=INK, sw=2.5, opacity=0.13)
    c.poly(pts, fill='none', stroke=INK, sw=2.5)
    for i, (x, y) in enumerate(pts):
        a = math.radians(-90 + 36 * i)
        quality = i < 5
        c.line(cx, cy, x, y, Q if quality else R, 4.5)
        if quality:
            c.circle(x, y, 6.5, fill=Q, stroke=WHITE, sw=2)
        else:
            c.rect(x - 6, y - 6, 12, 12, fill=R, stroke=WHITE, sw=2)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Five Resources, Five Shapes', 'Ten metric scores per resource, from the lowest total to the highest. Illustrative examples from Chapter 3.')
    n, gap = 5, 12
    x0, x1, y0, y1 = 30, 1170, 124, 618
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    deco = {'Adopt': ('#e5f2e6', GREEN, 'check'), 'Revise': ('#fdf1d6', ORANGED, 'pencil'), 'Reject': ('#fde3e3', RED, 'cross')}
    for i, (name, q, r, qs, rs, tot, bnd, dec) in enumerate(RES):
        assert sum(q) == qs and sum(r) == rs and qs + rs == tot and band(tot) == bnd and decision(tot, q + r) == dec, name
        x = x0 + i * (w + gap)
        cx = x + w / 2
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=GRAYM, sw=2.5, rx=14)
        c.para(cx, y0 + 30, name, w - 20, 19, 1.15, 'bold', INK, 'middle', maxlines=2)
        radar(c, cx, y0 + 222, 96, q + r)
        c.text(cx, y0 + 355, 'Total %d' % tot, 30, 'bold', INK, 'middle')
        c.text(cx, y0 + 383, '%s band' % bnd, 18, 'normal', INK, 'middle')
        fill, ink, kind = deco[dec]
        c.rect(x + 14, y0 + 400, w - 28, 36, fill=fill, stroke=ink, sw=2.5, rx=18)
        {'check': ic_check, 'pencil': ic_pencil, 'cross': ic_cross}[kind](c, x + 36, y0 + 418, 12, ink)
        c.text(x + 58, y0 + 425, dec, 20, 'bold', ink)
        c.text(cx, y0 + 466, 'Quality %d · Reusability %d' % (qs, rs), 15, 'normal', MUTED, 'middle', maxw=w - 16)
        low = min(q + r)
        lows = [METRICS[j] for j, s in enumerate(q + r) if s == low]
        summary = 'Total %d, %s band, decision %s. Quality %d, reusability %d.' % (tot, bnd, dec, qs, rs)
        facts = ['Quality scores %s: %s.' % (', '.join(map(str, q)), 'accuracy and currency, alignment, readability, accessibility, practice with feedback'),
                 'Reusability scores %s: %s.' % (', '.join(map(str, r)), 'open license, modularity, metadata, editable source, portability'),
                 'Lowest metric: %s, at %d.' % (' and '.join(lows), low)]
        items.append(dict(id=name.lower().replace(' ', '-').replace('e-book', 'ebook'), label=name, color=ink if dec != 'Adopt' else GREEN,
                          box=(x, y0, x + w, y1), summary=summary, facts=facts))
    # bracket over the two charts that total 65
    xa = x0 + 1 * (w + gap) + 14
    xb = x0 + 2 * (w + gap) + w - 14
    c.path('M%s,%s v-12 H%s v12' % (xa, y0 - 4, xb), stroke=ORANGED, sw=3)
    c.chip((xa + xb) / 2, y0 - 36, 'Same total, different shape', fill=ORANGE, color=INK, size=16, anchor='middle', h=26)
    # legend
    ly = 648
    c.circle(48, ly, 7, fill=Q)
    c.text(62, ly + 6, 'Quality metrics 1 to 5 (right half)', 15, 'normal', INK)
    c.rect(330, ly - 6, 12, 12, fill=R)
    c.text(350, ly + 6, 'Reusability metrics 6 to 10 (left half)', 15, 'normal', INK)
    c.line(660, ly, 700, ly, ORANGE, 3, '6 5')
    c.text(708, ly + 6, 'Floor: a score of 5', 15, 'normal', INK)
    c.text(40, 684, 'Each spoke runs from 0 at the center to 10 at the outer ring. Bands and decisions use the chapter\'s starting values.',
           14, 'normal', MUTED, maxw=1120)

    quiz = [
        dict(question='Which resource has nine metrics of 9 and one of 4, so it is Good but still Revise?', correct_zone='one-gap',
             explanation='Total 85 is Good, but one metric is below the floor of 5.'),
        dict(question='Which resource has strong quality metrics but a collapsed reusability side, and a total of 65?', correct_zone='locked-chemistry-ebook',
             explanation='Quality 44, reusability 21: strong on one side and locked down on the other.'),
        dict(question='Which resource is balanced and middling, with a total of 65 and metadata as its lowest metric?', correct_zone='watershed-basics',
             explanation='Quality 32 and reusability 33, with metadata at 4.'),
        dict(question='Which resource has the largest, most even shape and the decision Adopt?', correct_zone='open-algebra',
             explanation='Total 90, Excellent, with every metric at 8 or higher.'),
        dict(question='Which resource has the smallest shape and the decision Reject?', correct_zone='thin-material',
             explanation='Total 37 is below 50, so the decision is Reject.'),
    ]
    return c, items, quiz
