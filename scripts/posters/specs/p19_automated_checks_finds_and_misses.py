"""Poster 19: What Each Automated Check Can and Cannot Find (Chapter 13, grid, 4 zones)."""
from svgkit import *

CH = '13-automated-checks-cost-privacy'

META = dict(
    slug='automated-checks-finds-and-misses',
    title='What Each Automated Check Can and Cannot Find',
    chapter=CH,
    overlay='grid',
    topic='What automated checks find and what they miss',
    desc='Four automated tools, each split into what it finds and what it cannot find, with a reminder to keep a human in the loop.',
    intro=('Teachers over-trust a clean scan, and "the scan passed" does not mean "the resource is accessible". This poster pairs what each tool finds with what it misses, taken from the Chapter 13 table. '
           'Every tool is drawn with a beam of light that lights some items and leaves others dark. The "cannot find" half has the same visual weight as the "finds" half, shaded and dotted. '
           'A footer reminds the reader to keep a human in the loop.'),
    alt=('Four tools, each with a finds half and a cannot-find half. Link checker: finds links that return errors or have moved; cannot find a working link that leads to the wrong content. '
         'Accessibility scan: finds missing alt attributes, weak contrast, and missing labels; cannot find whether alt text is useful or captions are accurate. '
         'License detection: finds missing, mismatched, or unrecognized license statements; cannot find whether the license claim is true. '
         'Readability scan: gives a reading level for each passage; cannot find undefined terms, dense ideas, or audience fit. A footer says keep a human in the loop.'),
    bloom='Analyze',
    objective='**state** what each of four automated checks can find and what it cannot, and **explain** why a clean scan is not a finished review.',
    objective_plain='state what each of four automated checks can find and what it cannot, and explain why a clean scan is not a finished review.',
    prereq=['Automated checks and the human in the loop from [Chapter 13](../../chapters/13-automated-checks-cost-privacy/index.md).'],
    activities=[
        '**Explore (3 min).** Press each tool. What is the one thing it cannot find?',
        '**Quiz (3 min).** Press **Quiz Me** and match four findings to the tools.',
        '**Plan (4 min).** For a resource of yours, list one check you would automate and the human check that must follow it.',
    ],
    assessment=[
        ('A link checker reports no broken links. What can it not tell you?', 'Whether a working link leads to the wrong content.'),
        ('Can an accessibility scan tell you whether alt text is useful?', 'No. It finds missing alt attributes, not whether the text is useful.'),
        ('What can a readability scan not find?', 'Undefined terms, dense ideas, and audience fit.'),
    ],
    connection='Pairing what each tool finds with what it misses motivates the human check that Chapter 14 formalizes.',
    ref_nums=[(CH, [2, 8, 6])],
    key_questions=['What did this tool actually look at?', 'What would a person still need to check?'],
    misconceptions=['A clean scan means the resource is accessible', 'Automated checks replace the human reviewer'],
    good=['The poster keeps the chapter\'s wording and shows only the checks the book already uses.'],
    verify=[(CH, '| Link checker | Links that return errors or have moved | A working link that leads to the wrong content |'),
            (CH, '| Accessibility scan | Missing alt attributes, weak contrast, missing labels | Whether alt text is useful, or captions are accurate |'),
            (CH, '| License detection | Missing, mismatched, or unrecognized license statements | Whether the license claim is true |'),
            (CH, '| Readability scan | A reading level for each passage | Undefined terms, dense ideas, audience fit |')],
)

TOOLS = [
    ('link-checker', 'Link checker', ['Links that return errors', 'Links that have moved'], ['A working link that leads to the wrong content'], '#1d4f86', '#e6eef8'),
    ('accessibility-scan', 'Accessibility scan', ['Missing alt attributes', 'Weak contrast', 'Missing labels'], ['Whether alt text is useful', 'Whether captions are accurate'], '#00796b', '#e3f4f1'),
    ('license-detection', 'License detection', ['Missing license statements', 'Mismatched license statements', 'Unrecognized license statements'], ['Whether the license claim is true'], '#8a5a00', '#fdf1d6'),
    ('readability-scan', 'Readability scan', ['A reading level for each passage'], ['Undefined terms', 'Dense ideas', 'Audience fit'], '#573379', '#efe6f6'),
]


def tool_icon(c, zid, cx, cy, hue):
    c.circle(cx, cy, 30, fill=WHITE, stroke=hue, sw=4)
    if zid == 'link-checker':
        ic_link(c, cx, cy, 14, hue)
    elif zid == 'accessibility-scan':
        c.circle(cx, cy - 12, 5, fill=hue)
        c.line(cx - 12, cy - 4, cx + 12, cy - 4, hue, 4)
        c.line(cx, cy - 4, cx, cy + 6, hue, 4)
        c.line(cx, cy + 6, cx - 8, cy + 16, hue, 4)
        c.line(cx, cy + 6, cx + 8, cy + 16, hue, 4)
    elif zid == 'license-detection':
        c.circle(cx, cy, 14, fill='none', stroke=hue, sw=3.5)
        c.text(cx, cy + 7, 'c', 20, 'bold', hue, 'middle')
    else:
        c.rect(cx - 16, cy - 8, 32, 16, fill='none', stroke=hue, sw=3, rx=2)
        for k in range(5):
            c.line(cx - 12 + k * 6, cy - 8, cx - 12 + k * 6, cy - (1 if k % 2 else 3), hue, 2.5)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'What Each Automated Check Can and Cannot Find', 'A clean scan is not a finished review. Every tool has a lit half and a dark half.')
    n, gap = 4, 14
    x0, x1, y0, y1 = 30, 1170, 106, 616
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, name, finds, misses, hue, tint) in enumerate(TOOLS):
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 52, fill=hue, rx=14)
        c.rect(x, y0 + 28, w, 24, fill=hue)
        c.text(x + 16, y0 + 34, name, 22, 'bold', WHITE, maxw=w - 30)
        tool_icon(c, zid, x + w / 2, y0 + 88, hue)
        # beam
        c.poly([(x + w / 2 - 10, y0 + 116), (x + w / 2 + 10, y0 + 116), (x + w - 30, y0 + 178), (x + 30, y0 + 178)], fill='#fff3b0', opacity=0.9)
        # finds half
        c.rect(x + 12, y0 + 184, w - 24, 184, fill=tint, stroke=hue, sw=2.5, rx=10)
        ic_check(c, x + 34, y0 + 208, 11, GREEN)
        c.text(x + 54, y0 + 214, 'FINDS', 15, 'bold', GREEND)
        yy = y0 + 244
        for f in finds:
            c.circle(x + 28, yy - 5, 3.5, fill=hue)
            yy = c.para(x + 38, yy, f, w - 56, 14.5, 1.2, 'normal', INK) + 4
        # cannot find half
        c.rect(x + 12, y0 + 380, w - 24, 122, fill='#e1e5ea', stroke=INK, sw=2.5, rx=10, dash='2 6')
        ic_cross(c, x + 34, y0 + 404, 11, RED)
        c.text(x + 54, y0 + 410, 'CANNOT FIND', 15, 'bold', REDD)
        yy = y0 + 438
        for m in misses:
            c.circle(x + 28, yy - 5, 3.5, fill=INK)
            yy = c.para(x + 38, yy, m, w - 56, 14.5, 1.2, 'normal', INK) + 4
        items.append(dict(id=zid, label=name, color=hue, box=(x, y0, x + w, y1),
                          summary='Finds: %s. Cannot find: %s.' % ('; '.join(f.lower() for f in finds), '; '.join(m.lower() for m in misses)),
                          facts=['Finds: ' + f for f in finds] + ['Cannot find: ' + m for m in misses]))
    c.rect(30, 630, 1140, 52, fill=GRAYL, stroke=GRAY, sw=2.5, rx=12)
    ic_person(c, 62, 656, 15, INK)
    ic_magnifier(c, 100, 656, 14, INK)
    c.text(132, 663, 'Keep a human in the loop. Automated checks find what they can measure and miss what needs judgment.', 18, 'bold', INK, maxw=1020)
    quiz = [
        dict(question='Which tool cannot find a working link that leads to the wrong content?', correct_zone='link-checker', explanation='It finds links that error or have moved.'),
        dict(question='Which tool finds missing alt attributes and weak contrast but not whether alt text is useful?', correct_zone='accessibility-scan', explanation='Usefulness takes a human.'),
        dict(question='Which tool finds missing or mismatched license statements but cannot say whether the claim is true?', correct_zone='license-detection', explanation='It checks the statement, not the truth.'),
        dict(question='Which tool gives a reading level for each passage but cannot find undefined terms or audience fit?', correct_zone='readability-scan', explanation='A reading level is not the same as fit.'),
    ]
    return c, items, quiz
