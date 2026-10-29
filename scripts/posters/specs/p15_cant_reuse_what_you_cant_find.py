"""Poster 15: You Can't Reuse What You Can't Find (Chapter 9, grid, 3 zones)."""
from svgkit import *

CH = '09-modularity-metadata'

META = dict(
    slug='cant-reuse-what-you-cant-find',
    title='You Can\'t Reuse What You Can\'t Find',
    chapter=CH,
    overlay='grid',
    topic='Why metadata decides whether a resource is found and trusted',
    desc='A mock search for "watershed grade 6 reading open license" shows three resource records: one found and clear, one not found, and one found but unclear.',
    intro=('The principle behind the metadata metric is that you cannot reuse what you cannot find. This poster is a mock search results page for the query from Chapter 9, "watershed grade 6 reading open license", '
           'with the chapter\'s three records as result cards. Resource A has a full record and ranks high. Resource B has only the title "Reading 4", and the search cannot find it. '
           'Resource C has a title and an author but no subject, grade, or license, so it may be found, yet the teacher cannot tell the grade or whether she may reuse it. '
           'Empty fields show as dashed placeholders. The search page is generic and is not any real search engine.'),
    alt=('A generic search page with the query "watershed grade 6 reading open license" and three result cards, each with six fields: title, author, subject, grade level, license, and description. '
         'Resource A is complete: title Watershed Basics, author Maria Lopez, subject Earth science, grade 6 to 7, license CC BY 4.0, and a clear description. The search finds it and it ranks high. '
         'Resource B has only the title "Reading 4"; the other five fields are dashed placeholders, and no field mentions a watershed, so it is not found. '
         'Resource C has the title Watershed Basics and an author, but no subject, grade level, license, or description. It is possibly found, but the teacher cannot tell the grade or whether she may reuse it.'),
    bloom='Analyze',
    objective='**explain** why a record with missing metadata is found, not found, or found but unclear for the same search.',
    objective_plain='explain why a record with missing metadata is found, not found, or found but unclear for the same search.',
    prereq=['The six core metadata fields from [Chapter 9](../../chapters/09-modularity-metadata/index.md).'],
    activities=[
        '**Explore (3 min).** Press each card and read which fields are filled. What does the teacher still not know about card C?',
        '**Quiz (3 min).** Press **Quiz Me** and match three outcomes to the three cards.',
        '**Fix (4 min).** Choose one resource of yours and fill in all six fields. How long did it take?',
    ],
    assessment=[
        ('Why is resource B not found by the search?', 'No field mentions a watershed.'),
        ('Why is resource C found but unclear?', 'It has no subject, grade level, or license, so the teacher cannot tell the grade or whether she may reuse it.'),
        ('Which six fields make up a core record?', 'Title, author, subject, grade level, license, and description.'),
    ],
    connection='Metadata is metric 8. It is also the cheapest fix in Chapter 15, where adding the missing fields takes half an hour in the chapter\'s example.',
    ref_nums=[(CH, [1, 2, 6, 9])],
    key_questions=['Which fields does the search read?', 'What would a teacher still need to know?'],
    misconceptions=['A good resource will be found by its title alone', 'Metadata is part of the content'],
    good=['The three records come from the Chapter 9 worked example and are illustrative.'],
    verify=[(CH, 'A teacher searches a repository for "watershed grade 6 reading open license"'),
            (CH, '| B | Title "Reading 4" and nothing else | No: no field mentions a watershed |'),
            (CH, 'Possibly, but the teacher cannot tell the grade or whether she may reuse it'),
            (CH, 'title, author, subject, grade level, license, and description'),
            ('02-open-licenses-attribution', 'Maria Lopez')],
)

FIELDS = ['Title', 'Author', 'Subject', 'Grade level', 'License', 'Description']
RECS = [
    ('a', 'Resource A', ['Watershed Basics', 'Maria Lopez', 'Earth science', '6 to 7', 'CC BY 4.0', 'A clear description'],
     'Found, ranks high', 'ok', GREEN, '#e5f2e6', 'Yes, and it ranks high.'),
    ('b', 'Resource B', ['Reading 4', None, None, None, None, None], 'Not found', 'no', RED, '#fde8e8', 'No: no field mentions a watershed.'),
    ('c', 'Resource C', ['Watershed Basics', 'Maria Lopez', None, None, None, None], 'Found, but unclear', 'warn', '#8a5a00', '#fdf1d6',
     'Possibly, but the teacher cannot tell the grade or whether she may reuse it.'),
]


def field_icon(c, k, x, y):
    if k == 0:
        c.rect(x - 7, y - 7, 14, 14, fill=INK, rx=2)
    elif k == 1:
        ic_person(c, x, y, 9, INK)
    elif k == 2:
        c.poly([(x - 8, y + 6), (x, y - 8), (x + 8, y + 6)], fill=INK)
    elif k == 3:
        for j in range(3):
            c.rect(x - 8 + j * 6, y + 6 - (j + 1) * 5, 4, (j + 1) * 5, fill=INK)
    elif k == 4:
        c.circle(x, y, 8, fill='none', stroke=INK, sw=2.5)
        c.circle(x, y, 3, fill=INK)
    else:
        for j in range(3):
            c.line(x - 8, y - 6 + j * 6, x + 8 - (4 if j == 2 else 0), y - 6 + j * 6, INK, 2.5)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'You Can\'t Reuse What You Can\'t Find', 'One search, three records. What the teacher finds depends on the metadata.')
    # search bar
    c.rect(30, 96, 1140, 48, fill=WHITE, stroke=GRAY, sw=3, rx=24)
    ic_magnifier(c, 62, 119, 14, INK)
    c.text(92, 128, 'watershed grade 6 reading open license', 21, 'normal', INK, mono=True, maxw=800)
    c.rect(1050, 104, 104, 32, fill=INK, rx=16)
    c.text(1102, 126, 'Search', 17, 'bold', WHITE, 'middle')
    n, gap = 3, 16
    x0, x1, y0, y1 = 30, 1170, 160, 638
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, name, vals, verdict, kind, hue, tint, found) in enumerate(RECS):
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 46, fill=hue, rx=14)
        c.rect(x, y0 + 24, w, 22, fill=hue)
        c.text(x + 16, y0 + 31, name, 22, 'bold', WHITE)
        for k, (f, v) in enumerate(zip(FIELDS, vals)):
            y = y0 + 64 + k * 58
            c.rect(x + 12, y, w - 24, 50, fill=tint if v else WHITE, stroke=GRAYM if not v else hue, sw=2, rx=8, dash=None if v else '6 5')
            field_icon(c, k, x + 34, y + 25)
            c.text(x + 54, y + 20, f.upper(), 12, 'bold', MUTED, spacing='1')
            if v:
                c.text(x + 54, y + 40, v, 18, 'bold', INK, maxw=w - 80)
            else:
                c.text(x + 54, y + 40, 'missing', 16, 'normal', MUTED, italic=True)
        # result badge
        by = y0 + 64 + 6 * 58 + 8
        c.rect(x + 12, by, w - 24, 44, fill=tint, stroke=hue, sw=3, rx=22)
        {'ok': ic_check, 'no': ic_cross, 'warn': ic_warn}[kind](c, x + 40, by + 22, 14, hue if kind == 'warn' else hue)
        c.text(x + 66, by + 29, verdict, 20, 'bold', hue, maxw=w - 90)
        facts = ['Fields filled: %s.' % (', '.join(f.lower() for f, v in zip(FIELDS, vals) if v) or 'none'),
                 'Fields missing: %s.' % (', '.join(f.lower() for f, v in zip(FIELDS, vals) if not v) or 'none'),
                 'Does the search find it? %s' % found]
        items.append(dict(id=zid, label=name + ': ' + verdict.lower(), color=hue, box=(x, y0, x + w, y1),
                          summary=found, facts=facts))
    c.text(40, 664, 'Six core fields: title, author, subject, grade level, license, and description. A dashed box is an empty field.', 15, 'normal', MUTED, maxw=1120)
    c.text(40, 686, 'Illustrative records from the Chapter 9 worked example, on a generic search page.', 15, 'normal', MUTED, maxw=1120)
    quiz = [
        dict(question='Which record has all six fields and ranks high for the search?', correct_zone='a', explanation='Resource A is complete.'),
        dict(question='Which record has only the title "Reading 4" and cannot be found?', correct_zone='b', explanation='No field mentions a watershed.'),
        dict(question='Which record may be found, but leaves the teacher unable to tell the grade or whether she may reuse it?', correct_zone='c', explanation='It lacks subject, grade level, license, and description.'),
    ]
    return c, items, quiz
