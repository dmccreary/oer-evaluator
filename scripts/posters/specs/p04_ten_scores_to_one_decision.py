"""Poster 4: From Ten Scores to One Decision (Chapter 3, callout, 6 markers). The artwork carries no text."""
from svgkit import *

CH = '03-ten-metric-rubric-scoring'

META = dict(
    slug='ten-scores-to-one-decision',
    title='From Ten Scores to One Decision',
    chapter=CH,
    overlay='callout',
    layout='top-bottom',
    topic='How ten metric scores combine into subtotals, a total, a band, and a decision',
    desc='A funnel that narrows ten metric scores to two subtotals, a total out of 100, a score band, and one decision, with the floor shown as a gate.',
    intro=('This poster follows the layers of Chapter 3 from left to right. Ten metric scores, each 0 to 10, combine into two subtotals of 50 points, '
           'which add to a total out of 100. The total falls into a band, and the band plus a floor of 5 produces a decision: Adopt, Revise, or Reject. '
           'The example is Watershed Basics, total 65, Fair, Revise. The inset in the lower right shows the One Gap resource caught at the floor: nine metrics of 9 and one of 4 '
           'give a total of 85, which is Good, and the decision is still Revise.'),
    alt=('A funnel from left to right in five stages. Stage 1: ten vertical bars for the ten metric scores of Watershed Basics, five blue quality bars and five purple reusability bars, with a dashed floor line at 5. '
         'Stage 2: two subtotal bars, quality 32 of 50 and reusability 33 of 50. Stage 3: one total bar, 65 of 100. Stage 4: a band scale with five bands, Poor 0 to 24, Weak 25 to 49, Fair 50 to 74, Good 75 to 89, '
         'Excellent 90 to 100, with a pointer in Fair. Stage 5: three decision icons, a check for Adopt, a pencil for Revise, and a cross for Reject, with Revise highlighted. '
         'An inset in the lower right shows One Gap: nine tall bars and one short bar below the dashed floor line, so a total of 85 still ends in Revise.'),
    bloom='Understand',
    objective='**trace** ten metric scores through subtotals, a total, a band, and a decision, and **explain** why the floor can override a high total.',
    objective_plain='trace ten metric scores through subtotals, a total, a band, and a decision, and explain why the floor can override a high total.',
    prereq=['The ten metrics from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).'],
    activities=[
        '**Explore (3 min).** Hover over markers 1 to 6 in order and watch what each layer keeps and what it loses.',
        '**Quiz (3 min).** Press **Quiz** and find each layer from its description.',
        '**Apply (4 min).** A resource totals 80 with one metric at 3. Which decision does the rule give, and why?',
    ],
    assessment=[
        ('What is the Adopt rule?', 'A total of at least 75 and every metric at least 5.'),
        ('What band is a total of 65?', 'Fair, which runs from 50 to 74.'),
        ('A resource totals 85. Is it always Adopt?', 'No. If any metric is below 5 the decision is Revise.'),
    ],
    connection=('Chapter 11 applies this same decision rule to real adoption decisions. The thresholds are this book\'s starting rule, a teaching choice and not a standard.'),
    ref_nums=[(CH, [1, 7, 6])],
    key_questions=['What does each layer keep, and what does it lose?', 'Which metric is below the floor?'],
    misconceptions=['A total of 75 or more always means Adopt', 'The total is the most informative number in a report'],
    good=['The thresholds are this book\'s starting rule, not a standard.', 'Watershed Basics and One Gap are illustrative examples from Chapter 3.'],
    verify=[(CH, 'Excellent 90 to 100, Good 75 to 89, Fair 50 to 74, Weak 25 to 49, and Poor 0 to 24'),
            (CH, 'Adopt when the total >= 75 and every metric >= 5'),
            (CH, '| 4 | One Gap | 9, 9, 9, 9, 9 | 9, 9, 9, 9, 4 | 45 | 40 | 85 | Good | Revise |'),
            (CH, '| 1 | Watershed Basics | 7, 6, 8, 5, 6 | 9, 5, 4, 8, 7 | 32 | 33 | 65 | Fair | Revise |')],
)

SCORES = [7, 6, 8, 5, 6, 9, 5, 4, 8, 7]   # Watershed Basics
GAP = [9, 9, 9, 9, 9, 9, 9, 9, 9, 4]       # One Gap
BANDS = [(25, '#d9dde3'), (25, '#b9c1cc'), (25, '#8d99a8'), (15, '#5f6c7c'), (11, '#364152')]
MID = 290   # vertical center of the funnel


def bars(c, x, base, scores, w, gap, unit):
    for i, s in enumerate(scores):
        bx = x + i * (w + gap)
        quality = i < 5
        h = s * unit
        if quality:
            c.rect(bx, base - h, w, h, fill=Q, rx=3)
        else:
            c.rect(bx, base - h, w, h, fill=R, rx=3)
            c.rect(bx, base - h, w, h, fill='url(#dots)', rx=3)
    return x + len(scores) * (w + gap) - gap


def draw():
    c = Canvas(1200, 700)
    c.raw('<defs><pattern id="dots" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.6" fill="#ffffff" opacity=".55"/></pattern></defs>')
    # funnel body: heights narrow stage by stage
    stages = [(40, 330, 410), (380, 560, 310), (620, 770, 220), (810, 1010, 150), (1050, 1160, 104)]
    prev = None
    for (xa, xb, h) in stages:
        if prev:
            c.poly([(prev[1], MID - prev[2] / 2), (xa, MID - h / 2), (xa, MID + h / 2), (prev[1], MID + prev[2] / 2)], fill=GRAYL)
        prev = (xa, xb, h)
    for (xa, xb, h) in stages:
        c.rect(xa, MID - h / 2, xb - xa, h, fill=WHITE, stroke=GRAYM, sw=3, rx=14)
    # stage 1: ten bars with the floor of 5
    base = MID + 176
    unit = 31
    bars(c, 58, base, SCORES, 20, 7, unit)
    c.line(48, base - 5 * unit, 322, base - 5 * unit, ORANGE, 3.5, '8 6')
    c.line(48, base, 322, base, INK, 2.5)
    # stage 2: two subtotal bars (max 50 -> 170 px)
    base2 = MID + 118
    u2 = 200 / 50
    c.rect(405, base2 - 32 * u2, 62, 32 * u2, fill=Q, rx=4)
    c.rect(473, base2 - 33 * u2, 62, 33 * u2, fill=R, rx=4)
    c.rect(473, base2 - 33 * u2, 62, 33 * u2, fill='url(#dots)', rx=4)
    for bx in (405, 473):
        c.rect(bx, base2 - 50 * u2, 62, 50 * u2, fill='none', stroke=GRAYM, sw=2, rx=4, dash='5 4')
    c.line(395, base2, 545, base2, INK, 2.5)
    # stage 3: one total bar (max 100 -> 150 px), quality below, reusability on top
    base3 = MID + 92
    u3 = 170 / 100
    c.rect(668, base3 - 100 * u3, 74, 100 * u3, fill='none', stroke=GRAYM, sw=2, rx=4, dash='5 4')
    c.rect(668, base3 - 32 * u3, 74, 32 * u3, fill=Q, rx=3)
    c.rect(668, base3 - 65 * u3, 74, 33 * u3, fill=R, rx=3)
    c.rect(668, base3 - 65 * u3, 74, 33 * u3, fill='url(#dots)', rx=3)
    c.line(640, base3, 750, base3, INK, 2.5)
    # stage 4: band scale, proportional widths, pointer in Fair
    bx = 826
    scale = 168 / 101.0
    band_y = MID - 12
    pos_x = {}
    x = bx
    for (n, col) in BANDS:
        c.rect(x, band_y, n * scale, 36, fill=col, stroke=WHITE, sw=1.5)
        pos_x[n] = x
        x += n * scale
    px = bx + 65 * scale
    c.poly([(px, band_y - 4), (px - 10, band_y - 24), (px + 10, band_y - 24)], fill=ORANGE, stroke=INK, sw=2.5)
    for k in range(5):
        c.circle(bx + 14 + k * 36, band_y + 62, 6, fill=BANDS[k][1], stroke=INK, sw=1.5)
    # stage 5: three decision icons, Revise highlighted
    for j, (fn, col) in enumerate(((ic_check, GREEN), (ic_pencil, ORANGE), (ic_cross, RED))):
        y = MID - 30 + j * 30
        fn(c, 1105, y, 11, col)
    c.rect(1076, MID - 17, 58, 34, fill='none', stroke=INK, sw=3.5, rx=17)
    # inset: One Gap at the floor gate
    c.rect(810, 512, 350, 168, fill='#fff7e6', stroke=ORANGE, sw=3, rx=14)
    ib = 656
    u4 = 12
    bars(c, 836, ib, GAP, 18, 7, u4)
    c.line(826, ib - 5 * u4, 1148, ib - 5 * u4, ORANGE, 3.5, '8 6')
    c.line(826, ib, 1148, ib, INK, 2.5)
    c.rect(836 + 9 * 25 - 4, ib - 4 * u4 - 4, 26, 4 * u4 + 8, fill='none', stroke=RED, sw=3, rx=4)
    ic_lock(c, 1128, 548, 14, open_=False, fill=INK)
        # connector from stage 4 down toward the inset
    c.arrow(1100, MID + 66, 1100, 504, GRAY, 4, 12)

    def at(x, y):
        return (x, y)

    items = [
        dict(id=1, label='Ten metric scores', color=Q, at=(58, MID - 185),
             hint='Ten vertical bars, five in one color and five in a patterned second color, with a dashed line across them.',
             description='Each metric is scored as a whole number from 0 to 10. Metrics 1 to 5 are quality and metrics 6 to 10 are reusability. The dashed line is the floor of 5. The example is Watershed Basics: 7, 6, 8, 5, 6 and 9, 5, 4, 8, 7.',
             tip='Report the lowest metrics beside every subtotal. The subtotal alone hides them.'),
        dict(id=2, label='Two subtotals of 50 points', color=R, at=(398, MID - 140),
             hint='Two tall bars side by side, each with a dashed outline showing how full it could be.',
             description='The quality subtotal is the sum of metrics 1 to 5 and the reusability subtotal is the sum of metrics 6 to 10. Each is out of 50. Watershed Basics has 32 and 33.',
             tip='Two resources can share a subtotal and need very different fixes.'),
        dict(id=3, label='The total out of 100', color=INK, at=(638, MID - 100),
             hint='A single stacked bar, shorter than the stage before it.',
             description='The total is the quality subtotal plus the reusability subtotal, from 0 to 100. Watershed Basics totals 65. It is the number people ask for and the least informative number in a report.',
             tip='Three resources can each total 65 and need three different actions.'),
        dict(id=4, label='The score band', color=GRAY, at=(828, MID + 76),
             hint='A strip of five segments from light to dark, with a pointer above one of them.',
             description='The total falls into a band: Excellent 90 to 100, Good 75 to 89, Fair 50 to 74, Weak 25 to 49, and Poor 0 to 24. A total of 65 is Fair.',
             tip='The bands are this book\'s starting values, not a standard.'),
        dict(id=5, label='The decision', color=GREEN, at=(1066, MID + 54),
             hint='Three small icons stacked in a column, one of them circled.',
             description='Adopt when the total is at least 75 and every metric is at least 5. Reject when the total is below 50. Otherwise Revise. Watershed Basics is Revise, shown by the pencil.',
             tip='Color alone never carries the decision: a check, a pencil, and a cross do too.'),
        dict(id=6, label='The floor gate and the One Gap example', color=RED, at=(838, 532),
             hint='A small inset with nine tall bars and one short bar that dips below the dashed line, beside a padlock.',
             description='One Gap has nine metrics of 9 and one of 4. The total is 85, which is Good, yet the decision is still Revise because one metric is below the floor of 5.',
             tip='A total of 75 or more does not always mean Adopt. The floor is why.'),
    ]
    return c, items, []
