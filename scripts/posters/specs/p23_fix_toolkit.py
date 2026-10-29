"""Poster 23: The Fix Toolkit (Chapter 15, callout, 13 markers). The artwork carries no text."""
from svgkit import *

CH = '15-improving-resources-with-ai'

META = dict(
    slug='fix-toolkit',
    title='The Fix Toolkit',
    chapter=CH,
    overlay='callout',
    layout='dual-panel',
    topic='The thirteen fixes an agent can help with, grouped by the metric each raises',
    desc='A pegboard of thirteen tools, one for each fix in Chapter 15, hung in eight panels by the metric each mainly raises, each with a human-check badge.',
    intro=('Thirteen fixes in a table are hard to keep in mind, and the improvement plan starts from the lowest metric and asks which fix applies. This poster is that lookup as a pegboard. '
           'Eight panels hold the thirteen tools, one panel for each metric a fix mainly raises. Quality metrics hang in blue panels and reusability metrics in purple panels. '
           'Each marker\'s description gives the typical agent mistake and the human check from the chapter, and every tool carries a small person-with-check badge, because nothing is applied without human review. '
           'The artwork has no text, so every name comes from the overlay.'),
    alt=('A pegboard with eight panels holding thirteen tools. Accessibility panel, blue: AI alt text generation, caption generation, heading repair. Readability panel, blue: reading level rewrite, glossary generation. '
         'Accuracy and currency panel, blue: link repair, content update. Practice with feedback panel, blue: practice question generation, MicroSim building. '
         'Metadata panel, purple: metadata generation. Open license panel, purple: license statement repair. Modularity panel, purple: chapter splitting. Editable source panel, purple: PDF-to-Markdown conversion. '
         'Every tool has a small person-with-check badge for the human check.'),
    bloom='Apply',
    objective='**match** each of the thirteen fixes to the metric it mainly raises, and **state** the human check for one of them.',
    objective_plain='match each of the thirteen fixes to the metric it mainly raises, and state the human check for one of them.',
    prereq=['The ten metrics from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md) and the improvement plan from [Chapter 15](../../chapters/15-improving-resources-with-ai/index.md).'],
    activities=[
        '**Explore (4 min).** Hover over the markers 1 to 13. Which panel holds the most tools?',
        '**Quiz (3 min).** Press **Quiz** and find each tool from its description.',
        '**Plan (3 min).** Take the lowest metric of a resource you have scored. Which tool on the pegboard would you reach for, and what is its human check?',
    ],
    assessment=[
        ('Which metric does PDF-to-Markdown conversion mainly raise?', 'Editable source.'),
        ('What is the human check for link repair?', 'Open every new link.'),
        ('What is the typical agent mistake in metadata generation?', 'A guessed author or license.'),
    ],
    connection='The improvement plan starts from the lowest metric and asks which fix applies. The poster is that lookup, and every tool carries the reminder that nothing is applied without human review.',
    ref_nums=[(CH, [1, 6, 9, 7])],
    key_questions=['Which metric is lowest?', 'What mistake should I expect, and how do I check it?'],
    misconceptions=['An agent\'s fix can be applied without review', 'A fix for one metric has no side effects on the others'],
    good=['Thirteen markers are near the readable limit, so some leader lines cross the board. Use the labels in the side panels to follow them.'],
    verify=[(CH, 'The table summarizes the thirteen fixes. Each row names the metric the fix mainly raises, the mistake to expect, and the human check.'),
            (CH, '| AI alt text generation | Accessibility | Generic text or invented details | Look at each image beside its draft |'),
            (CH, '| Link repair | Accuracy and currency | An invented address | Open every new link |'),
            (CH, '| Metadata generation | Metadata | A guessed author or license | Verify each field against the page |'),
            (CH, '| MicroSim building | Practice with feedback | Wrong science or a failed embed | Use every control and embed it on each platform |')],
)

# (panel name, quality?, [(fix, mistake, human check, hint)])
PANELS = [
    ('Accessibility', True, [('AI alt text generation', 'Generic text or invented details', 'Look at each image beside its draft', 'A picture frame with lines of text under it.'),
                              ('Caption generation', 'Mis-heard technical terms', 'Watch the video while reading the captions', 'A screen with two subtitle bars.'),
                              ('Heading repair', 'Renamed or merged sections', 'Compare the outline before and after', 'Bars at three indent levels, like an outline.')]),
    ('Readability', True, [('Reading level rewrite', 'Lost precision or meaning', 'Run the readability tool and the meaning checks', 'A staircase with a downward arrow.'),
                           ('Glossary generation', 'A definition that differs from the resource\'s use', 'Compare with the resource and a trusted source', 'A book with a list and a bookmark.')]),
    ('Accuracy and currency', True, [('Link repair', 'An invented address', 'Open every new link', 'Two chain links with a gap and a bridge.'),
                                      ('Content update', 'A figure from memory', 'Open the source and confirm the figure', 'A calendar with a circular arrow.')]),
    ('Metadata', False, [('Metadata generation', 'A guessed author or license', 'Verify each field against the page', 'A price-tag shape with a hole.')]),
    ('Open license', False, [('License statement repair', 'A license assigned to someone else\'s work', 'Find the owner\'s terms or replace the item', 'A page with a round seal.')]),
    ('Modularity', False, [('Chapter splitting', 'A module that still depends on another', 'Open each module alone', 'Scissors cutting a page in two.')]),
    ('Editable source', False, [('PDF-to-Markdown conversion', 'Lost tables, headings, or pictures', 'Compare the output with the PDF', 'A locked page with an arrow to an open page of hash marks.')]),
    ('Practice with feedback', True, [('Practice question generation', 'A wrong key or a leading stem', 'Answer each question without the key', 'A sheet with check boxes.'),
                                       ('MicroSim building', 'Wrong science or a failed embed', 'Use every control and embed it on each platform', 'A window with a slider and a play triangle.')]),
]


def tool(c, k, cx, cy, hue):
    """Tool picture k (0-based chapter order), about 60 px across."""
    if k == 0:
        c.rect(cx - 26, cy - 24, 52, 34, fill=WHITE, stroke=INK, sw=2.5, rx=3)
        c.poly([(cx - 22, cy + 6), (cx - 8, cy - 10), (cx + 2, cy), (cx + 10, cy - 6), (cx + 22, cy + 6)], fill=hue)
        c.line(cx - 22, cy + 18, cx + 22, cy + 18, GRAYM, 3)
        c.line(cx - 22, cy + 26, cx + 8, cy + 26, GRAYM, 3)
    elif k == 1:
        c.rect(cx - 28, cy - 22, 56, 40, fill=INK, rx=4)
        c.rect(cx - 20, cy + 2, 40, 6, fill=WHITE, rx=2)
        c.rect(cx - 14, cy + 11, 28, 5, fill=WHITE, rx=2)
    elif k == 2:
        c.rect(cx - 24, cy - 22, 30, 7, fill=INK, rx=2)
        c.rect(cx - 12, cy - 8, 32, 7, fill=hue, rx=2)
        c.rect(cx - 12, cy + 6, 26, 7, fill=hue, rx=2)
        c.rect(cx - 24, cy + 20, 34, 7, fill=INK, rx=2)
    elif k == 3:
        for j in range(3):
            c.rect(cx - 26 + j * 17, cy + 14 - j * 14, 17, 12 + j * 14, fill=hue)
        c.arrow(cx - 22, cy - 22, cx + 22, cy - 22, INK, 4, 10)
    elif k == 4:
        c.poly([(cx - 28, cy - 18), (cx, cy - 12), (cx, cy + 22), (cx - 28, cy + 16)], fill=WHITE, stroke=INK, sw=2.5)
        c.poly([(cx + 28, cy - 18), (cx, cy - 12), (cx, cy + 22), (cx + 28, cy + 16)], fill=WHITE, stroke=INK, sw=2.5)
        c.rect(cx + 10, cy - 20, 8, 20, fill=ORANGE)
    elif k == 5:
        c.rect(cx - 30, cy - 8, 26, 16, fill='none', stroke=INK, sw=4, rx=8)
        c.rect(cx + 8, cy - 8, 26, 16, fill='none', stroke=INK, sw=4, rx=8)
        c.line(cx - 4, cy, cx + 8, cy, RED, 4, '3 4')
    elif k == 6:
        ic_calendar(c, cx - 4, cy, 22, INK, WHITE, hue)
        c.path('M%s,%s a12,12 0 1 1 -4,-10' % (cx + 26, cy + 14), stroke=ORANGE, sw=4)
    elif k == 7:
        c.poly([(cx - 26, cy - 4), (cx - 8, cy - 22), (cx + 26, cy - 22), (cx + 26, cy + 22), (cx - 8, cy + 22)], fill=WHITE, stroke=INK, sw=2.5)
        c.circle(cx - 6, cy, 5, fill=INK)
    elif k == 8:
        ic_doc(c, cx - 22, cy - 28, 44, 56, label=None, fold=10)
        ic_star(c, cx + 14, cy + 16, 13, ORANGE)
    elif k == 9:
        ic_scissors(c, cx, cy, 26, INK)
        c.line(cx + 12, cy - 22, cx + 12, cy + 22, GRAY, 2.5, '3 4')
    elif k == 10:
        ic_lock(c, cx - 14, cy - 2, 14, False, INK)
        c.arrow(cx + 4, cy, cx + 18, cy, INK, 3.5, 9)
        c.rect(cx + 18, cy - 20, 24, 36, fill=WHITE, stroke=INK, sw=2.5)
        for j in range(3):
            c.line(cx + 22, cy - 10 + j * 9, cx + 38, cy - 10 + j * 9, hue, 3)
    elif k == 11:
        c.rect(cx - 24, cy - 26, 48, 52, fill=WHITE, stroke=INK, sw=2.5, rx=3)
        for j in range(3):
            c.rect(cx - 16, cy - 16 + j * 14, 9, 9, fill=WHITE, stroke=INK, sw=2)
            c.line(cx - 2, cy - 11 + j * 14, cx + 16, cy - 11 + j * 14, GRAYM, 3)
    else:
        c.rect(cx - 30, cy - 24, 60, 48, fill=WHITE, stroke=INK, sw=2.5, rx=4)
        c.rect(cx - 30, cy - 24, 60, 11, fill=hue, rx=4)
        c.line(cx - 20, cy + 6, cx + 4, cy + 6, GRAYM, 4)
        c.circle(cx - 6, cy + 6, 6, fill=ORANGE, stroke=INK, sw=2)
        c.poly([(cx + 12, cy - 4), (cx + 12, cy + 16), (cx + 26, cy + 6)], fill=INK)


def draw():
    c = Canvas(1000, 660)
    c.rect(14, 14, 972, 632, fill='#efe3d0', stroke='#8d6e4b', sw=6, rx=14)
    # peg holes
    for gx in range(40, 980, 28):
        for gy in range(40, 640, 28):
            c.circle(gx, gy, 2, fill='#c9b79b')
    slot, pad = 118, 14
    rows = [(0, 1, 2), (3, 4, 5, 6, 7)]
    pw = lambda n: n * slot + 2 * pad
    items = []
    k = 0
    # row 1 panels: accessibility (3), readability (2), accuracy (2) ; row 2: metadata, license, modularity, editable source, practice (2)
    placements = []
    y = 42
    row_defs = [([0, 1, 2], 42, 270), ([3, 4, 5, 6, 7], 340, 270)]
    for (idxs, ry, rh) in row_defs:
        total = sum(pw(len(PANELS[i][2])) for i in idxs) + 10 * (len(idxs) - 1)
        x = (1000 - total) / 2
        for i in idxs:
            n = len(PANELS[i][2])
            placements.append((i, x, ry, pw(n), 250))
            x += pw(n) + 10
    tool_index = {}
    kk = 0
    for (i, fixes_unused) in [(i, None) for i in range(len(PANELS))]:
        for j in range(len(PANELS[i][2])):
            tool_index[(i, j)] = kk
            kk += 1
    for (i, x, ry, w, h) in placements:
        name, quality, tools = PANELS[i]
        hue, hued, tint = (Q, QD, QL) if quality else (R, RD, RL)
        c.rect(x, ry, w, h, fill=tint, stroke=hue, sw=4, rx=12)
        c.rect(x, ry, w, 34, fill=hue, rx=12)
        c.rect(x, ry + 18, w, 16, fill=hue)
        # a small rail with hooks (no text)
        for j, (fix, mistake, check, hint) in enumerate(tools):
            kidx = tool_index[(i, j)]
            cx = x + pad + slot * j + slot / 2
            cy = ry + 112
            c.line(cx, ry + 34, cx, cy - 46, GRAY, 3)
            c.circle(cx, ry + 38, 4.5, fill=INK)
            c.circle(cx, cy, 48, fill=WHITE, stroke=hued, sw=3.5)
            tool(c, kidx, cx, cy, hue)
            # human check badge
            c.circle(cx + 38, cy + 40, 15, fill=WHITE, stroke=INK, sw=2.5)
            ic_person(c, cx + 38, cy + 40, 8, INK)
            c.path('M%s,%s l3,4 l6,-8' % (cx + 40, cy + 44), stroke=GREEN, sw=3)
            items.append(dict(id=kidx + 1, label=fix, at=(cx - 40, cy - 40), color=hue, radius=2.2,
                              hint=hint,
                              description='Mainly raises %s. Typical agent mistake: %s. The human check: %s.' % (name.lower(), mistake.lower(), check.lower()),
                              tip='Nothing is applied without human review.'))
    return c, items, []
