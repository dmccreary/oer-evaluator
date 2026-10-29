"""Poster 6: Source Files and Delivery Files (Chapter 4, grid, 3 zones)."""
from svgkit import *

CH = '04-open-formats-version-control'

META = dict(
    slug='source-and-delivery-files',
    title='Source Files and Delivery Files',
    chapter=CH,
    overlay='grid',
    topic='Open file formats versus good editable source formats',
    desc='Three zones sort common file formats into good source, usually acceptable, and poor source, with two badges that separate "is the format open?" from "is it a good source for editing?".',
    intro=('Editable source is a reusability metric, and the most common failure is a resource distributed only as a PDF. This poster sorts the formats from Chapter 4 into three zones. '
           'Every file is a document tile with its extension printed large and two badges: a round badge for "is the format open?" and a square badge for "is it a good source for editing?". '
           'The PDF is the instructive tile. Its format is open, and it is still a poor source because it is built for reading.'),
    alt=('Three zones under an arrow from source, change this, to delivery, read this. Good source: Markdown and plain text, HTML, OpenDocument text, CSV for data, and SVG for diagrams. '
         'All five are open formats and good sources. Usually acceptable: a Word document, whose format is a published standard but whose full fidelity depends on particular software. '
         'Poor source: a PDF, which is an open international standard but is built for reading, and a page layout or design-program file, which is closed and poor unless you own the program. '
         'Each tile has a round badge for open and a square badge for good source.'),
    bloom='Understand',
    objective='**explain** why an open file format is not always a good source for editing, using the PDF as the example.',
    objective_plain='explain why an open file format is not always a good source for editing, using the PDF as the example.',
    prereq=['The editable source metric from [Chapter 4](../../chapters/04-open-formats-version-control/index.md).'],
    activities=[
        '**Explore (3 min).** Press each zone. Which tile has a round check badge and a square cross badge?',
        '**Quiz (3 min).** Press **Quiz Me** and place four formats.',
        '**Apply (4 min).** List the files you hand out to colleagues. Which zone does each belong in? What would you add so that others can edit them?',
    ],
    assessment=[
        ('Is a PDF an open format? Is it a good source?', 'Open, yes. Good source, no, because it is built for reading.'),
        ('Why is a Word document only usually acceptable?', 'It is a published standard, but full fidelity depends on particular software.'),
        ('Which formats are good sources for data and for diagrams?', 'CSV for data and SVG for diagrams.'),
    ],
    connection='Editable source is metric 9 in the ten-metric rubric. A resource that ships only a PDF loses points here even if its license is fully open.',
    ref_nums=[(CH, [1, 2, 6, 10])],
    key_questions=['Is the format open?', 'Could someone edit this file and keep its structure?'],
    misconceptions=['An open format is an editable format', 'A PDF is a good way to share something others will change'],
    good=['The page layout or design-program file is drawn as a generic tile with no program name or logo.'],
    verify=[(CH, '| Markdown (.md) and plain text (.txt) | Yes, plain text | Yes |'),
            (CH, '| Word document (.docx) | A published standard, but full fidelity depends on particular software | Usually acceptable |'),
            (CH, '| PDF (.pdf) | An open international standard | Poor, because it is built for reading |'),
            (CH, '| A page layout or design-program file | Closed | Poor, unless you own the program |'),
            (CH, '| CSV (.csv) | Yes, plain text table | Yes, for data |'),
            (CH, '| SVG (.svg) | Yes, a web standard for drawings | Yes, for diagrams |')],
)

GOOD, GOODD, GOODT = '#00796b', '#004d40', '#e3f4f1'
OKAY, OKAYD, OKAYT = '#8a5a00', '#5c3c00', '#fdf1d6'
POOR, POORD, POORT = '#b71c1c', '#7f1313', '#fde8e8'

# (extension, name, open?, open note, source?, source note)  state: 'y', 'p', 'n'
GOOD_FILES = [
    ('.md', 'Markdown and plain text', 'y', 'plain text', 'y', 'good source'),
    ('.html', 'HTML', 'y', 'public web standards', 'y', 'good source'),
    ('.odt', 'OpenDocument text', 'y', 'international standard', 'y', 'good source'),
    ('.csv', 'CSV', 'y', 'plain text table', 'y', 'good for data'),
    ('.svg', 'SVG', 'y', 'web standard for drawings', 'y', 'good for diagrams'),
]


def badge(c, cx, cy, state, shape):
    col = {'y': GREEN, 'p': ORANGE, 'n': RED}[state]
    if shape == 'round':
        c.circle(cx, cy, 15, fill=WHITE, stroke=col, sw=3)
    else:
        c.rect(cx - 15, cy - 15, 30, 30, fill=WHITE, stroke=col, sw=3, rx=5)
    if state == 'y':
        c.path('M%s,%s l5,6 l9,-12' % (cx - 7, cy + 1), stroke=col, sw=3.5)
    elif state == 'n':
        c.line(cx - 6, cy - 6, cx + 6, cy + 6, col, 3.5)
        c.line(cx - 6, cy + 6, cx + 6, cy - 6, col, 3.5)
    else:
        c.line(cx, cy - 7, cx, cy + 2, INK, 3.5)
        c.circle(cx, cy + 8, 2.2, fill=INK)


def tile(c, x, y, w, ext, name, o, onote, s, snote, hue, generic=False):
    """A file tile in a cell of width w; returns nothing. Height used is about 196."""
    cx = x + w / 2
    if generic:
        ic_doc(c, cx - 31, y, 62, 78, label=None)
        c.rect(cx - 21, y + 14, 18, 22, fill=GRAYM)
        c.rect(cx + 3, y + 14, 18, 10, fill=GRAYM)
        c.rect(cx + 3, y + 28, 18, 8, fill=GRAYM)
        c.line(cx - 21, y + 48, cx + 21, y + 48, GRAYM, 3)
        c.line(cx - 21, y + 58, cx + 6, y + 58, GRAYM, 3)
    else:
        ic_doc(c, cx - 31, y, 62, 78, label=ext, lsize=19 if len(ext) < 5 else 17, lfill=hue)
    c.para(cx, y + 104, name, w - 10, 16, 1.18, 'bold', INK, 'middle', maxlines=3)
    by = y + 148
    badge(c, cx - w * .2, by, o, 'round')
    badge(c, cx + w * .2, by, s, 'square')
    c.text(cx - w * .2, by + 30, 'Open?', 14, 'bold', INK, 'middle')
    c.text(cx + w * .2, by + 30, 'Source?', 14, 'bold', INK, 'middle')


def ico_good(c, a, b, r, f):
    c.circle(a, b, r, fill=WHITE)
    c.path('M%s,%s l5,6 l9,-12' % (a - 7, b + 1), stroke=GREEND, sw=3.5)


def ico_ok(c, a, b, r, f):
    ic_warn(c, a, b, r, WHITE, OKAYD)


def ico_poor(c, a, b, r, f):
    c.circle(a, b, r, fill=WHITE)
    c.line(a - r * .4, b - r * .4, a + r * .4, b + r * .4, POOR, 3.5)
    c.line(a - r * .4, b + r * .4, a + r * .4, b - r * .4, POOR, 3.5)


def column(c, x, y0, y1, w, hue, hued, tint, head, sub, icon):
    c.rect(x, y0, w, y1 - y0, fill=tint, stroke=hue, sw=3, rx=14)
    c.rect(x, y0, w, 52, fill=hue, rx=14)
    c.rect(x, y0 + 28, w, 24, fill=hue)
    icon(c, x + 30, y0 + 26, 14, WHITE if icon is not ic_check else WHITE)
    c.text(x + 56, y0 + 33, head, 23, 'bold', WHITE, maxw=w - 70)
    c.text(x + 16, y0 + 78, sub, 16, 'normal', hued, maxw=w - 30)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Source Files and Delivery Files', 'Open is not the same as editable. The round badge asks "is it open?" The square badge asks "is it a good source?"')
    # source -> delivery arrow
    c.arrow(60, 112, 1140, 112, GRAY, 4, 14)
    c.chip(60, 90, 'SOURCE: change this', fill=INK, size=15, h=26)
    c.chip(1140, 90, 'DELIVERY: read this', fill=GRAY, size=15, h=26, anchor='end')
    y0, y1 = 136, 640
    xs = [(30, 510), (556, 250), (822, 348)]
    # zone 1
    x, w = xs[0]
    column(c, x, y0, y1, w, GOOD, GOODD, GOODT, 'Good source', 'Open formats you can edit and reuse', ico_good)
    cell = (w - 20) / 3
    for i, f in enumerate(GOOD_FILES):
        r, k = divmod(i, 3)
        tile(c, x + 10 + k * cell, y0 + 104 + r * 206, cell, f[0], f[1], f[2], f[3], f[4], f[5], GOOD)
    z1 = (x, y0, x + w, y1)
    # zone 2
    x, w = xs[1]
    column(c, x, y0, y1, w, OKAY, OKAYD, OKAYT, 'Usually acceptable', 'Works if you have the right software', ico_ok)
    tile(c, x + 10, y0 + 104, w - 20, '.docx', 'Word document', 'p', 'published standard', 'p', 'usually acceptable', OKAY)
    c.para(x + w / 2, y0 + 340, 'A published standard, but full fidelity depends on particular software.', w - 36, 16, 1.25, 'normal', INK, 'middle')
    z2 = (x, y0, x + w, y1)
    # zone 3
    x, w = xs[2]
    column(c, x, y0, y1, w, POOR, POORD, POORT, 'Poor source', 'Built for reading, or closed', ico_poor)
    cell = (w - 20) / 2
    tile(c, x + 10, y0 + 104, cell, '.pdf', 'PDF', 'y', 'open international standard', 'n', 'poor', POOR)
    tile(c, x + 10 + cell, y0 + 104, cell, '', 'Page layout or design file', 'n', 'closed', 'n', 'poor', POOR, generic=True)
    c.para(x + w / 2, y0 + 340, 'A PDF is an open international standard, and still a poor source because it is built for reading.', w - 36, 16, 1.25, 'normal', INK, 'middle')
    c.para(x + w / 2, y0 + 410, 'A design-program file is poor unless you own the program.', w - 36, 16, 1.25, 'normal', INK, 'middle')
    z3 = (x, y0, x + w, y1)
    c.text(40, 674, 'Open here means the specification is public. The last badge says whether the format is a good source for editing.', 15, 'normal', MUTED, maxw=1120)

    items = [
        dict(id='good-source', label='Good source', color=GOOD, box=z1,
             summary='Five formats that are open and good sources for editing.',
             facts=['Markdown (.md) and plain text (.txt): open, plain text.', 'HTML (.html): open, public web standards.',
                    'OpenDocument text (.odt): open, an international standard.', 'CSV (.csv): open plain text table, good for data.',
                    'SVG (.svg): open web standard for drawings, good for diagrams.']),
        dict(id='usually-acceptable', label='Usually acceptable', color=OKAY, box=z2,
             summary='The Word document is a published standard, but fidelity depends on software.',
             facts=['Word document (.docx): a published standard.', 'Full fidelity depends on particular software.',
                    'A reasonable source format when your colleagues have a word processor.']),
        dict(id='poor-source', label='Poor source', color=POOR, box=z3,
             summary='A PDF is open but built for reading; a design-program file is closed.',
             facts=['PDF (.pdf): an open international standard, poor as a source because it is built for reading.',
                    'A page layout or design-program file: closed, poor unless you own the program.',
                    'A PDF records how each page looks, not the structure, so changing a sentence means copying text out of the page.']),
    ]
    quiz = [
        dict(question='Which zone holds the PDF, a format that is open but a poor source?', correct_zone='poor-source', explanation='A PDF is built for reading.'),
        dict(question='Which zone holds the Word document?', correct_zone='usually-acceptable', explanation='Full fidelity depends on particular software.'),
        dict(question='Which zone holds Markdown, HTML, OpenDocument text, CSV, and SVG?', correct_zone='good-source', explanation='All five are open and good sources.'),
        dict(question='Which zone holds a page layout file that you can edit only if you own the program?', correct_zone='poor-source', explanation='It is closed, so it is a poor source.'),
    ]
    return c, items, quiz
