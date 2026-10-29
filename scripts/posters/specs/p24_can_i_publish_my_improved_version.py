"""Poster 24: Can I Publish My Improved Version? (Chapter 15, grid, 6 license cards plus a footer band)."""
from svgkit import *

CH = '15-improving-resources-with-ai'

META = dict(
    slug='can-i-publish-my-improved-version',
    title='Can I Publish My Improved Version?',
    chapter=CH,
    overlay='grid',
    topic='What each license allows when you publish an improved version',
    desc='A traffic-light card for each license that answers one question: may you publish an improved version, and what must you do?',
    intro=('An agent\'s edited copy is a derivative work, so the license must be read before the first edit. This poster answers one practical question for each license in the Chapter 15 table: may you publish an improved version, and what must you do? '
           'The cards run from most to least permissive. Each has the same rows: the license name, a verdict, and the duties. The verdict has three states, shown with a symbol and a word as well as color: yes, yes with conditions, and no. '
           'A footer band covers the last row of the table: with no license, all rights are reserved, so ask the owner first. '
           'The poster prints the license names as text and does not redraw the official Creative Commons icons.'),
    alt=('Six license cards from most to least permissive, and a footer band. CC0: yes, nothing is required, and giving credit is good practice. '
         'CC BY: yes with conditions: credit the author, link to the license, and say that you changed the work. '
         'CC BY-SA: yes with conditions: the same as CC BY, and release your version under CC BY-SA. '
         'CC BY-NC: yes without commercial use: the same as CC BY, and do not sell or use it for commercial gain. '
         'CC BY-NC-SA: yes without commercial use: the same as CC BY, release under CC BY-NC-SA, and do not use it commercially. '
         'CC BY-ND: no, you may not share a changed version; you may make changes for your own private use only. '
         'Footer: with no license, all rights reserved: no; ask the owner for permission first.'),
    bloom='Apply',
    objective='**decide** whether an improved version of a resource may be published under its license, and **state** what you must do.',
    objective_plain='decide whether an improved version of a resource may be published under its license, and state what you must do.',
    prereq=['The six Creative Commons licenses from [Chapter 2](../../chapters/02-open-licenses-attribution/index.md) and derivative works from [Chapter 15](../../chapters/15-improving-resources-with-ai/index.md).'],
    activities=[
        '**Explore (3 min).** Press each card from left to right. Where does the answer change from yes to no?',
        '**Quiz (3 min).** Press **Quiz Me** and match four situations to the cards.',
        '**Apply (4 min).** Find the license on a resource you want to improve. Read its card and write the notice you would add to your version.',
    ],
    assessment=[
        ('A resource is CC BY-ND. May you publish your improved version?', 'No. You may make changes for your own private use only.'),
        ('A resource is CC BY-SA. What must you do?', 'The same as CC BY, and release your version under CC BY-SA.'),
        ('A resource has no license. May you publish an improved version?', 'No. All rights are reserved, so ask the owner for permission first.'),
    ],
    connection='This poster saves effort by stopping work on a resource that cannot be legally shared once improved. Read the license before the first edit.',
    ref_nums=[(CH, [1, 9]), ('02-open-licenses-attribution', [6, 8, 9])],
    key_questions=['What does the license say about derivatives?', 'What must I add to my version?'],
    misconceptions=['An AI edit removes the original license', 'Any open license lets you publish a changed version'],
    good=['The chapter\'s table has no row for CC BY-NC-ND, so the poster has none either. The author decides whether to add that row to the chapter and the poster together.',
          'Add the official Creative Commons icons only by following Creative Commons\' guidance on its marks. This poster uses text.'],
    verify=[(CH, '| CC0 | Yes | Nothing is required, and giving credit is good practice |'),
            (CH, '| CC BY | Yes | Credit the author, link to the license, and say that you changed the work |'),
            (CH, '| CC BY-SA | Yes | The same as CC BY, and release your version under CC BY-SA |'),
            (CH, '| CC BY-NC | Yes, without commercial use | The same as CC BY, and do not sell or use it for commercial gain |'),
            (CH, '| CC BY-NC-SA | Yes, without commercial use | The same as CC BY, release under CC BY-NC-SA, and do not use it commercially |'),
            (CH, '| CC BY-ND | No, you may not share a changed version | You may make changes for your own private use only |'),
            (CH, '| No license, all rights reserved | No | Ask the owner for permission first |')],
)

YES, YESD, YEST = '#1b5e20', '#14471a', '#e5f2e6'
COND, CONDD, CONDT = '#8a5a00', '#5c3c00', '#fdf1d6'
NO, NOD, NOT_ = '#b71c1c', '#7f1313', '#fde8e8'

CARDS = [
    ('cc0', 'CC0', 'yes', 'Yes', 'Nothing is required, and giving credit is good practice.'),
    ('cc-by', 'CC BY', 'cond', 'Yes, with conditions', 'Credit the author, link to the license, and say that you changed the work.'),
    ('cc-by-sa', 'CC BY-SA', 'cond', 'Yes, with conditions', 'The same as CC BY, and release your version under CC BY-SA.'),
    ('cc-by-nc', 'CC BY-NC', 'cond', 'Yes, without commercial use', 'The same as CC BY, and do not sell or use it for commercial gain.'),
    ('cc-by-nc-sa', 'CC BY-NC-SA', 'cond', 'Yes, without commercial use', 'The same as CC BY, release under CC BY-NC-SA, and do not use it commercially.'),
    ('cc-by-nd', 'CC BY-ND', 'no', 'No', 'You may not share a changed version. You may make changes for your own private use only.'),
]


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Can I Publish My Improved Version?', 'An agent\'s edited copy is a derivative work. Read the license before the first edit.')
    # legend
    lx = 700
    for (k, (fn, col, txt)) in enumerate(((ic_check, GREEN, 'Yes'), (ic_warn, ORANGE, 'Yes, with conditions'), (ic_cross, RED, 'No'))):
        x = lx + (0, 80, 280)[k]
        fn(c, x, 34, 12)
        c.text(x + 18, 40, txt, 15, 'bold', INK)
    n, gap = 6, 10
    x0, x1, y0, y1 = 30, 1170, 110, 552
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, name, kind, verdict, duty) in enumerate(CARDS):
        hue, hued, tint = {'yes': (YES, YESD, YEST), 'cond': (COND, CONDD, CONDT), 'no': (NO, NOD, NOT_)}[kind]
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=tint, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 56, fill=hue, rx=14)
        c.rect(x, y0 + 30, w, 26, fill=hue)
        c.text(x + w / 2, y0 + 37, name, 22, 'bold', WHITE, 'middle', maxw=w - 16)
        # verdict
        c.circle(x + w / 2, y0 + 108, 30, fill=WHITE, stroke=hue, sw=3)
        {'yes': ic_check, 'cond': ic_warn, 'no': ic_cross}[kind](c, x + w / 2, y0 + 108, 20)
        c.para(x + w / 2, y0 + 166, verdict, w - 20, 18, 1.2, 'bold', hued, 'middle', maxlines=3)
        c.text(x + 14, y0 + 242, 'WHAT YOU MUST DO', 12, 'bold', hued, spacing='1')
        c.para(x + 14, y0 + 268, duty, w - 28, 16, 1.25, 'normal', INK, maxlines=8)
        items.append(dict(id=zid, label=name, color=hue, box=(x, y0, x + w, y1),
                          summary='%s: %s' % (verdict, duty), facts=['May you publish an improved version? %s.' % verdict, 'What you must do: %s' % duty]))
    # footer band: no license
    fy0, fy1 = 566, 664
    c.rect(30, fy0, 1140, fy1 - fy0, fill=NOT_, stroke=NO, sw=3, rx=14)
    c.circle(78, fy0 + 49, 30, fill=WHITE, stroke=NO, sw=3)
    ic_stop(c, 78, fy0 + 49, 20)
    c.text(126, fy0 + 38, 'No license: all rights reserved', 24, 'bold', NOD)
    c.text(126, fy0 + 64, 'No. You may not publish an improved version.', 19, 'bold', INK)
    c.text(126, fy0 + 88, 'Ask the owner for permission first.', 18, 'normal', INK)
    c.text(1160, fy0 + 88, 'Cards run from most to least permissive.', 14, 'normal', MUTED, 'end')
    items.append(dict(id='no-license', label='No license, all rights reserved', color=NO, box=(30, fy0, 1170, fy1),
                      summary='No. Ask the owner for permission first.',
                      facts=['With no license, the default is all rights reserved.', 'An improved version is a derivative work, which the owner controls.',
                             'Ask the owner for permission before you edit or share it.']))
    quiz = [
        dict(question='Which card says you may not share a changed version, only change it for private use?', correct_zone='cc-by-nd', explanation='ND means no derivatives to share.'),
        dict(question='Which card says nothing is required, though credit is good practice?', correct_zone='cc0', explanation='CC0 puts the work in the public domain.'),
        dict(question='Which card says release your version under the same license and credit the author?', correct_zone='cc-by-sa', explanation='ShareAlike keeps adaptations open the same way.'),
        dict(question='Which zone says ask the owner for permission first?', correct_zone='no-license', explanation='All rights are reserved by default.'),
        dict(question='Which card allows publishing an improved version only without commercial use, under the same license?', correct_zone='cc-by-nc-sa', explanation='NC plus SA.'),
    ]
    return c, items, quiz
