"""Poster 8: Following a Claim Back to Its Source (Chapter 5, callout, 4 markers). No text in the artwork."""
from svgkit import *

CH = '05-accuracy-currency'

META = dict(
    slug='claim-source-chain',
    title='Following a Claim Back to Its Source',
    chapter=CH,
    overlay='callout',
    layout='top-bottom',
    topic='Tracing a claim through a citation chain to the original source',
    desc='A chain of four links that follows the claim "Wetlands filter pollutants" from a footnote to a textbook, a review article, and the study where the measurement was made.',
    intro=('Confirming that a citation exists is not the same as tracing the claim. This poster shows the worked example from Chapter 5. '
           'The claim "Wetlands filter pollutants" appears in a resource\'s footnote 4, which cites a textbook, which cites a review article, which summarizes several studies. '
           'One of those studies reports measurements of pollutant levels before and after water passed through a wetland. The first three links are other people\'s summaries. '
           'The fourth is where the measurement was made. A red flag at the second link marks the early stop that the poster exists to prevent. '
           'The sources are invented for the chapter and are illustrative, so there is nothing to look up.'),
    alt=('A chain of four links from left to right, each a different object. Link 1: a page with a footnote mark, the resource\'s footnote 4, which cites a textbook. '
         'Link 2: a closed textbook, which says wetlands filter pollutants and cites a review. A red stop flag stands on it, meaning a reviewer who stops here has only found that a textbook agrees. '
         'Link 3: a review article, which summarizes several studies of wetland filtering. Link 4: a laboratory bench with a flask and a gauge, one of those studies, '
         'which reports pollutant measurements before and after water passed through a wetland. It is the only link drawn as a place where something was measured, and it is the original source.'),
    bloom='Analyze',
    objective='**trace** a claim through a chain of citations to its original source and **explain** why stopping at the first link is not enough.',
    objective_plain='trace a claim through a chain of citations to its original source and explain why stopping at the first link is not enough.',
    prereq=['Primary and secondary sources from [Chapter 5](../../chapters/05-accuracy-currency/index.md).'],
    activities=[
        '**Explore (3 min).** Hover over markers 1 to 4. Which links are other people\'s summaries?',
        '**Quiz (3 min).** Press **Quiz** and find each link from its description.',
        '**Trace (4 min).** Pick a claim from a resource you use. How many links can you follow before you reach a primary source?',
    ],
    assessment=[
        ('A reviewer stops at link 2. What has the reviewer found?', 'Only that a textbook agrees with the resource.'),
        ('Which link is the original source?', 'Link 4, the study that reports the measurements.'),
        ('The further back you trace a claim, what happens to the check?', 'You can trust the check more.'),
    ],
    connection='Chapter 14 warns about invented citations. A reader needs to see that confirming a citation exists is not the same as tracing the claim.',
    ref_nums=[(CH, [1, 7, 9])],
    key_questions=['Is this link the original?', 'Who made the measurement?'],
    misconceptions=['A citation that exists proves the claim', 'A textbook agreeing with a resource is evidence'],
    good=['The chapter\'s sources are invented for illustration. The poster prints no journal names or citations.'],
    verify=[(CH, '| 1 | The resource\'s footnote 4 | Cites a textbook | No |'),
            (CH, '| 4 | One of those studies | Reports measurements of pollutant levels before and after water passed through a wetland | Yes |'),
            (CH, 'A reviewer who stopped at step 2 would have found only that a textbook agreed with the resource.'),
            (CH, 'The further back you trace a claim, the more you can trust the check.')],
)

GREYBOX, SRC = '#6b7785', '#2e7d32'
XS = [170, 430, 690, 950]
Y = 235


def bubble_box(c, x, y, w=190, h=210, hue=GREYBOX):
    c.rect(x - w / 2, y - h / 2, w, h, fill='#eef1f5', stroke=hue, sw=4, rx=16)
    c.poly([(x - 20, y + h / 2), (x - 4, y + h / 2 + 22), (x + 12, y + h / 2)], fill='#eef1f5', stroke=hue, sw=4)
    c.line(x - 19, y + h / 2 - 1, x + 11, y + h / 2 - 1, '#eef1f5', 6, cap='butt')


def draw():
    c = Canvas(1200, 440)
    # chain connectors with link rings
    for a, b in zip(XS[:-1], XS[1:]):
        xa, xb = a + 100, b - 100
        c.line(xa, Y, xb, Y, INK, 4)
        for k in range(3):
            cx = xa + (xb - xa) * (k + 1) / 4
            c.ellipse(cx, Y, 17, 10, fill='none', stroke=INK, sw=4)
        c.arrow(xb - 22, Y, xb, Y, INK, 4, 14)
    # link 1: page with a footnote mark
    bubble_box(c, XS[0], Y)
    ic_doc(c, XS[0] - 44, Y - 82, 88, 118, label=None)
    ic_lines(c, XS[0] - 30, Y - 50, 58, 4, gap=13)
    c.line(XS[0] - 32, Y + 6, XS[0] + 20, Y + 6, INK, 2)
    c.rect(XS[0] - 32, Y + 14, 12, 12, fill=ORANGE, stroke=INK, sw=1.5)
    c.line(XS[0] - 14, Y + 20, XS[0] + 26, Y + 20, GRAYM, 3)
    # link 2: textbook with a stop flag
    bubble_box(c, XS[1], Y)
    c.rect(XS[1] - 52, Y - 78, 104, 130, fill='#d6e6f7', stroke=INK, sw=3, rx=5)
    c.rect(XS[1] - 52, Y - 78, 18, 130, fill=Q, stroke=INK, sw=3, rx=3)
    c.rect(XS[1] - 20, Y - 56, 60, 34, fill=WHITE, stroke=INK, sw=2, rx=3)
    c.line(XS[1] - 10, Y - 40, XS[1] + 30, Y - 40, GRAYM, 3)
    c.line(XS[1] - 10, Y - 30, XS[1] + 14, Y - 30, GRAYM, 3)
    c.line(XS[1] + 70, Y - 130, XS[1] + 70, Y - 20, INK, 5)
    ic_stop(c, XS[1] + 70, Y - 142, 22, RED)
    # link 3: review article, two columns, stacked pages
    bubble_box(c, XS[2], Y)
    for k in (2, 1, 0):
        c.rect(XS[2] - 52 + k * 7, Y - 82 + k * 7 - 7, 96, 124, fill=WHITE, stroke=INK, sw=2.5, rx=3)
    for col in (0, 1):
        for k in range(6):
            c.line(XS[2] - 42 + col * 44, Y - 62 + k * 15, XS[2] - 12 + col * 44, Y - 62 + k * 15, GRAYM, 3)
    c.rect(XS[2] - 42, Y - 76, 80, 8, fill=INK)
    # link 4: lab bench, drawn as a hexagon to look different (the original)
    hx, hy, hr = XS[3], Y, 112
    pts = [(hx + hr * math_cos(a), hy + hr * math_sin(a)) for a in (0, 60, 120, 180, 240, 300)]
    c.poly(pts, fill='#e5f2e6', stroke=SRC, sw=5)
    c.rect(hx - 70, hy + 40, 140, 14, fill='#8d6e4b', stroke=INK, sw=2.5, rx=3)
    c.path('M%s,%s h26 l22,46 h-70 z' % (hx - 40, hy - 20), fill='#d6e6f7', stroke=INK, sw=3)
    c.rect(hx - 32, hy - 54, 12, 34, fill='#d6e6f7', stroke=INK, sw=3)
    c.path('M%s,%s h22 l12,26 h-46 z' % (hx - 36, hy + 12), fill=Q, opacity=0.7)
    c.circle(hx + 36, hy - 4, 32, fill=WHITE, stroke=INK, sw=3)
    c.line(hx + 36, hy - 4, hx + 52, hy - 18, RED, 4)
    c.circle(hx + 36, hy - 4, 4, fill=INK)
    ic_check(c, hx + 80, hy - 70, 16, GREEN)

    items = [
        dict(id=1, label='Footnote 4 of the resource', panel='top', at=(XS[0] - 82, Y - 118), color=GREYBOX,
             hint='A page with a small footnote mark at the bottom, inside a speech bubble.',
             description='The claim "Wetlands filter pollutants" appears in the resource. Footnote 4 cites a textbook. This link is someone\'s summary and is not the original.',
             tip='A footnote tells you where to look next. It is not evidence by itself.'),
        dict(id=2, label='The textbook', panel='top', at=(XS[1] - 82, Y - 118), color=RED,
             hint='A closed book with a red stop sign on a flag pole.',
             description='The textbook says wetlands filter pollutants and cites a review. A reviewer who stops here, at the red flag, has found only that a textbook agrees with the resource.',
             tip='This is the early stop the poster exists to prevent.'),
        dict(id=3, label='The review article', panel='top', at=(XS[2] - 82, Y - 118), color=GREYBOX,
             hint='Stacked pages in two columns, inside a speech bubble.',
             description='The review article summarizes several studies of wetland filtering. It is another summary, so it is not the original either.',
             tip='Secondary sources describe, summarize, or interpret primary sources.'),
        dict(id=4, label='The original study', panel='top', at=(XS[3] - 60, Y - 100), color=GREEN,
             hint='A laboratory bench with a flask and a gauge inside a six-sided shape, the only link not in a speech bubble.',
             description='One of those studies reports measurements of pollutant levels before and after water passed through a wetland. This is the original, and the claim is supported by it.',
             tip='The further back you trace a claim, the more you can trust the check. The sources in this example are invented.'),
    ]
    return c, items, []


import math  # noqa: E402


def math_cos(deg):
    return math.cos(math.radians(deg))


def math_sin(deg):
    return math.sin(math.radians(deg))
