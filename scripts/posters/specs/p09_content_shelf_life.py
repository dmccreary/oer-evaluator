"""Poster 9: How Fast Does Content Spoil? (Chapter 5, grid, 3 zones)."""
from svgkit import *

CH = '05-accuracy-currency'

META = dict(
    slug='content-shelf-life',
    title='How Fast Does Content Spoil?',
    chapter=CH,
    overlay='grid',
    topic='Matching the checking schedule to how fast content ages',
    desc='A three-shelf market stall that sorts six kinds of content by how quickly they go out of date, with a date stamp telling a reviewer how often to check each one.',
    intro=('Currency is half of the accuracy and currency metric, and reviewers often apply one rule to every page. This poster is a market stall with three shelves, '
           'taken from the Chapter 5 table of how quickly six kinds of content go out of date. The slow shelf holds content that is checked at each major review. '
           'The middle shelf is checked every few years. The fast shelf is checked every year or more often. Every item wears a date stamp with the wording from the chapter.'),
    alt=('Three shelves of a market stall, from slow to fast. Slow shelf: basic mathematics and definitions, which age very slowly, checked at each major review; '
         'and the sequence of historical events, which ages slowly, checked at each major review. Middle shelf: statistics and survey results, which age moderately, '
         'checked every few years or whenever new data appear; and standards, curricula, and guidelines, which age moderately, checked every few years and when a standard is revised. '
         'Fast shelf: software screenshots, prices, and web addresses, and laws, policies, and contact details, which age quickly, checked every year or more often.'),
    bloom='Understand',
    objective='**match** each of six kinds of content to how fast it ages and how often a reviewer should check it.',
    objective_plain='match each of six kinds of content to how fast it ages and how often a reviewer should check it.',
    prereq=['The currency half of the accuracy and currency metric from [Chapter 5](../../chapters/05-accuracy-currency/index.md).'],
    activities=[
        '**Explore (3 min).** Press each shelf and read its two items and their stamps.',
        '**Quiz (3 min).** Press **Quiz Me** and place four kinds of content on the right shelf.',
        '**Apply (4 min).** Pick a page you teach from. Which shelf does most of it sit on? When should you next check it?',
    ],
    assessment=[
        ('Which shelf holds software screenshots?', 'The fast shelf, checked every year or more often.'),
        ('How often do you check standards, curricula, and guidelines?', 'Every few years, and when a standard is revised.'),
        ('Why not use one currency rule for every page?', 'The multiplication table does not change, while a software screenshot can change within a year.'),
    ],
    connection='Currency is half of metric 1. A quick triage by shelf tells a reviewer where to spend checking time, and supports the link rot and revision history ideas in the same chapter.',
    ref_nums=[(CH, [2, 1, 10])],
    key_questions=['How fast does this kind of content age?', 'When was it last checked?'],
    misconceptions=['Every page needs the same checking schedule', 'Old content is always outdated'],
    good=['The poster keeps the chapter\'s own wording for how often to check. It does not turn "every few years" into a number.'],
    verify=[(CH, '| Basic mathematics and definitions | Very slowly | At each major review |'),
            (CH, '| The sequence of historical events | Slowly | At each major review |'),
            (CH, '| Statistics and survey results | Moderately | Every few years, or whenever new data appear |'),
            (CH, '| Standards, curricula, and guidelines | Moderately | Every few years, and when a standard is revised |'),
            (CH, '| Software screenshots, prices, and web addresses | Quickly | Every year or more often |'),
            (CH, '| Laws, policies, and contact details | Quickly | Every year or more often |')],
)

SHELVES = [
    ('slow', 'Slow shelf', 'Ages very slowly to slowly', '#00796b', '#004d40', '#e3f4f1',
     [('Basic mathematics and definitions', 'Ages very slowly', 'Check at each major review'),
      ('The sequence of historical events', 'Ages slowly', 'Check at each major review')]),
    ('middle', 'Middle shelf', 'Ages moderately', '#8a5a00', '#5c3c00', '#fdf1d6',
     [('Statistics and survey results', 'Ages moderately', 'Check every few years, or whenever new data appear'),
      ('Standards, curricula, and guidelines', 'Ages moderately', 'Check every few years, and when a standard is revised')]),
    ('fast', 'Fast shelf', 'Ages quickly', '#b71c1c', '#7f1313', '#fde8e8',
     [('Software screenshots, prices, and web addresses', 'Ages quickly', 'Check every year or more often'),
      ('Laws, policies, and contact details', 'Ages quickly', 'Check every year or more often')]),
]


def crate(c, x, y, w, h, hue, hued, name, ages, check):
    c.rect(x, y, w, h, fill=WHITE, stroke=hue, sw=3, rx=10)
    c.rect(x, y, w, 8, fill=hue, rx=4)
    c.para(x + 16, y + 40, name, w - 190, 19, 1.2, 'bold', INK, maxlines=3)
    c.text(x + 16, y + h - 18, ages, 15, 'normal', MUTED, maxw=w - 190)
    # date stamp
    sx, sy, sw_, sh = x + w - 166, y + 14, 152, h - 28
    c.rect(sx, sy, sw_, sh, fill=hue, rx=8)
    ic_calendar(c, sx + sw_ / 2, sy + 24, 13, INK, WHITE, hued)
    c.para(sx + sw_ / 2, sy + 60, check, sw_ - 14, 14, 1.2, 'bold', WHITE, 'middle', maxlines=4)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'How Fast Does Content Spoil?', 'Match the amount of checking to how fast the topic moves. Six kinds of content, three shelves.')
    y0 = 108
    sh = 172
    items = []
    for i, (zid, name, sub, hue, hued, tint, goods) in enumerate(SHELVES):
        y = y0 + i * (sh + 12)
        c.rect(30, y, 1140, sh, fill=tint, stroke=hue, sw=3, rx=14)
        # left label
        c.rect(30, y, 200, sh, fill=hue, rx=14)
        c.rect(180, y, 50, sh, fill=hue)
        if i < 2:
            ic_calendar(c, 130, y + 52, 26, INK, WHITE, hued)
        else:
            ic_clock(c, 130, y + 52, 28, INK, WHITE)
        c.text(130, y + 112, name, 22, 'bold', WHITE, 'middle', maxw=180)
        c.para(130, y + 138, sub, 180, 15, 1.2, 'normal', WHITE, 'middle')
        for j, (nm, ag, ck) in enumerate(goods):
            crate(c, 250 + j * 460, y + 16, 440, sh - 32, hue, hued, nm, ag, ck)
        # plank
        c.rect(30, y + sh - 8, 1140, 8, fill='#8d6e4b')
        items.append(dict(id=zid + '-shelf', label=name, color=hue, box=(30, y, 1170, y + sh),
                          summary='%s: %s.' % (name, sub.lower()),
                          facts=['%s. %s. %s.' % (n, a, k) for n, a, k in goods]))
    c.text(40, 690, 'Wording for how often to check is taken from the Chapter 5 table. The multiplication table does not change; a software screenshot can change within a year.',
           14, 'normal', MUTED, maxw=1120)
    quiz = [
        dict(question='Which shelf holds software screenshots, prices, and web addresses?', correct_zone='fast-shelf', explanation='They age quickly, so check every year or more often.'),
        dict(question='Which shelf holds basic mathematics and definitions?', correct_zone='slow-shelf', explanation='They age very slowly, so check at each major review.'),
        dict(question='Which shelf holds statistics and survey results, checked every few years or whenever new data appear?', correct_zone='middle-shelf', explanation='They age moderately.'),
        dict(question='Which shelf holds laws, policies, and contact details?', correct_zone='fast-shelf', explanation='They age quickly.'),
    ]
    return c, items, quiz
