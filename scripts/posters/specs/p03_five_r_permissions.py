"""Poster 3: The 5R Permissions: Five Things You May Do (Chapter 1, grid, 5 zones)."""
from svgkit import *

CH = '01-foundations-of-oer'

META = dict(
    slug='five-r-permissions',
    title='The 5R Permissions: Five Things You May Do',
    chapter=CH,
    overlay='grid',
    topic='The 5R permissions: retain, reuse, revise, remix, redistribute',
    desc='Five panels, one for each of the 5R permissions, each with the plain meaning, the test question to ask, and a classroom scene.',
    intro=('This poster shows the five permissions that an open license grants, in the order Chapter 1 teaches them: '
           'retain, reuse, revise, remix, and redistribute. Every panel has the same structure: a scene, a plain-language meaning, '
           'the test question to ask of any resource, and one classroom example. A strip under the panels shows that the permissions build on one another.'),
    alt=('Five equal panels in a row, numbered 1 to 5. Retain: make and keep your own copy; the question is can I make and keep my own copy. '
         'Reuse: use the work as it is; can I use it as it is. Revise: change the work; can I change it. Remix: combine the work with other open work; '
         'can I combine it with other open work. Redistribute: share copies with others; can I share copies with others. '
         'An arrow under the panels reads: have a copy, use it, change it, combine it, share it.'),
    bloom='Remember',
    objective='**identify** which of the 5R permissions a classroom action uses, with at least 4 of 5 correct on the first attempt.',
    objective_plain='identify which of the 5R permissions a classroom action uses, with at least 4 of 5 correct on the first attempt.',
    prereq=['The meaning of an open license from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).'],
    activities=[
        '**Explore (3 min).** Press each panel. Which two permissions are easiest to confuse, and what separates them?',
        '**Quiz (3 min).** Press **Quiz Me** and match five classroom actions to their permissions.',
        '**Practice (4 min).** Write one action of your own for each permission. Swap with a partner and check each other.',
    ],
    assessment=[
        ('You fix a typo in an open worksheet. Which permission is that?', 'Revise. Reuse stops where change begins.'),
        ('You email an unchanged open worksheet to a colleague. Which permission?', 'Redistribute.'),
        ('Which permission lets you build one unit from chapters of two open textbooks?', 'Remix, and the licenses must be compatible.'),
    ],
    connection=('Revise leads to the editable source metric, remix leads to license compatibility, and redistribute leads to ShareAlike. '
                'The 5Rs are the vocabulary of every later chapter.'),
    ref_nums=[(CH, [6, 1, 8])],
    key_questions=['Can I make and keep my own copy?', 'Can I use it as it is?', 'Can I change it?',
                   'Can I combine it with other open work?', 'Can I share copies with others?'],
    misconceptions=['Reuse covers any use, including after changes', 'Retain means keeping a link to a resource online',
                    'Revise and remix are the same permission', 'Sharing an unchanged copy is reuse'],
    good=['The five panels run in sequence, not in rank. No permission is more important than another.'],
    verify=[(CH, 'Can I make and keep my own copy?'), (CH, 'Can I use it as it is?'), (CH, 'Can I change it?'),
            (CH, 'Can I combine it with other open work?'), (CH, 'Can I share copies with others?'),
            (CH, 'Revise is the permission that separates an open resource from a merely free one.'),
            (CH, 'Reuse stops where change begins.')],
)

HUES = [('#00796b', '#e3f4f1'), ('#1d4f86', '#e6eef8'), ('#8a5a00', '#fdf1d6'), ('#573379', '#efe6f6'), ('#1b5e20', '#e5f2e6')]

PANELS = [
    ('Retain', 'Make and keep your own copy', 'Can I make and keep my own copy?',
     'Copy the source files of an open lab manual to an external drive.', 'retain'),
    ('Reuse', 'Use the work as it is', 'Can I use it as it is?',
     'Show an open diagram, unchanged, on the projector.', 'reuse'),
    ('Revise', 'Change the work', 'Can I change it?',
     'Add alt text to every image in an open chapter.', 'revise'),
    ('Remix', 'Combine the work with other open work', 'Can I combine it with other open work?',
     'Combine chapters from two open textbooks and a public-domain map.', 'remix'),
    ('Redistribute', 'Share copies with others', 'Can I share copies with others?',
     'Email an unchanged open worksheet to a colleague.', 'redistribute'),
]


def scene(c, kind, cx, cy, hue):
    """Small classroom scene, about 160 wide by 100 high around (cx, cy)."""
    if kind == 'retain':
        ic_doc(c, cx - 70, cy - 40, 48, 62, label=None)
        ic_lines(c, cx - 62, cy - 14, 30, 3)
        c.arrow(cx - 14, cy - 8, cx + 24, cy - 8, hue, 4, 11)
        ic_folder(c, cx + 28, cy - 28, 56, 44, fill='#fff3b0')
        ic_doc(c, cx + 40, cy - 38, 30, 38, label=None, fold=8)
        ic_person(c, cx + 56, cy + 38, 14, hue)
    elif kind == 'reuse':
        c.rect(cx - 76, cy - 44, 152, 80, fill=WHITE, stroke=hue, sw=3, rx=4)
        ic_doc(c, cx - 22, cy - 36, 44, 58, label=None)
        ic_lines(c, cx - 14, cy - 8, 28, 3)
        c.line(cx, cy + 36, cx, cy + 46, hue, 4)
        c.line(cx - 22, cy + 46, cx + 22, cy + 46, hue, 4)
    elif kind == 'revise':
        ic_doc(c, cx - 50, cy - 46, 70, 90, label=None)
        ic_lines(c, cx - 40, cy - 14, 44, 3)
        c.rect(cx - 40, cy - 28, 30, 7, fill=hue, rx=2)
        c.poly([(cx + 8, cy + 18), (cx + 58, cy - 32), (cx + 70, cy - 20), (cx + 20, cy + 30), (cx + 6, cy + 32)],
               fill=ORANGE, stroke=INK, sw=2.5)
    elif kind == 'remix':
        ic_doc(c, cx - 78, cy - 44, 44, 56, label=None, fill='#e6eef8')
        ic_doc(c, cx - 78, cy + 8, 44, 40, label=None, fill='#fdf1d6')
        c.arrow(cx - 28, cy - 16, cx + 6, cy, hue, 4, 11)
        c.arrow(cx - 28, cy + 28, cx + 6, cy + 6, hue, 4, 11)
        ic_doc(c, cx + 12, cy - 40, 62, 80, label=None, fill='#efe6f6')
        c.rect(cx + 20, cy - 16, 20, 20, fill='#e6eef8', stroke=INK, sw=1.5)
        c.rect(cx + 44, cy - 16, 20, 20, fill='#fdf1d6', stroke=INK, sw=1.5)
        ic_lines(c, cx + 22, cy + 16, 36, 2)
    else:
        ic_doc(c, cx - 22, cy - 46, 44, 58, label=None)
        ic_lines(c, cx - 14, cy - 18, 28, 3)
        for dx in (-62, 0, 62):
            c.arrow(cx + dx * .35, cy + 18, cx + dx, cy + 26, hue, 3, 9)
            ic_person(c, cx + dx, cy + 40, 15, hue)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'The 5R Permissions: Five Things You May Do',
                'An open license grants five permissions. Ask the test question of any resource.')
    n, gap = 5, 14
    x0, x1, y0, y1 = 30, 1170, 116, 612
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (verb, meaning, question, example, kind) in enumerate(PANELS):
        hue, tint = HUES[i]
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 52, fill=hue, rx=14)
        c.rect(x, y0 + 30, w, 22, fill=hue)
        c.circle(x + 28, y0 + 26, 15, fill=WHITE)
        c.text(x + 28, y0 + 32, str(i + 1), 18, 'bold', hue, 'middle')
        c.text(x + 52, y0 + 34, verb, 24, 'bold', WHITE, maxw=w - 62)
        # scene
        c.rect(x + 10, y0 + 62, w - 20, 118, fill=tint, rx=10)
        scene(c, kind, x + w / 2, y0 + 121, hue)
        # meaning
        yy = c.para(x + 14, y0 + 208, meaning, w - 28, 17, 1.25, 'bold', INK)
        # test question (largest text)
        c.rect(x + 10, y0 + 252, w - 20, 118, fill=tint, rx=10)
        c.text(x + 18, y0 + 272, 'TEST QUESTION', 12, 'bold', hue, spacing='1')
        c.para(x + 18, y0 + 302, question, w - 36, 22, 1.18, 'bold', hue, maxlines=4)
        # example
        c.text(x + 14, y0 + 396, 'EXAMPLE', 12, 'bold', MUTED, spacing='1')
        c.para(x + 14, y0 + 420, example, w - 28, 16, 1.28, 'normal', INK, maxlines=5)
        items.append(dict(id=kind, label=verb, color=hue, box=(x, y0, x + w, y1)))
    # build-on-each-other strip
    ys = 650
    c.line(x0 + 30, ys - 16, x1 - 30, ys - 16, GRAY, 4)
    c._head(x1 - 20, ys - 16, 0, 16, GRAY)
    words = ['have a copy', 'use it', 'change it', 'combine it', 'share it']
    for i, wd in enumerate(words):
        cx = x0 + i * (w + gap) + w / 2
        c.circle(cx, ys - 16, 8, fill=HUES[i][0])
        c.text(cx, ys + 20, wd, 17, 'bold', INK, 'middle')

    facts = {
        'retain': ('Make, own, and control copies of the resource.',
                   ['Download it, duplicate it, store it, and manage your own copy.',
                    'Keep the file, not just a link. A bookmark is not a copy.',
                    'Retain matters because websites change and disappear.']),
        'reuse': ('Use the resource in its original, unaltered form.',
                  ['In a class, a study group, a workshop, a website, or a video.',
                   'Reuse stops where change begins.',
                   'The moment you alter it, even to fix a typo, you have moved to revise.']),
        'revise': ('Adapt, adjust, modify, or alter the resource itself.',
                   ['Fix an error, update a statistic, translate, lower the reading level, or add local examples.',
                    'Adding captions or alt text is also a revision.',
                    'Revise is the permission that separates an open resource from a merely free one.']),
        'remix': ('Combine the work with other open material to create something new.',
                  ['Revise changes one work; remix joins two or more.',
                   'Remixing requires that the licenses of the parts are compatible. Chapter 2 explains how.']),
        'redistribute': ('Share copies of the original, revised, or remixed work with others.',
                         ['Post it on a website, email it to colleagues, or upload it to a repository.',
                          'Redistribution is what lets one teacher\'s improvement reach every other teacher.',
                          'Keep a credit note and the license notice with the file when you pass it on.']),
    }
    for it in items:
        it['summary'], it['facts'] = facts[it['id']]

    quiz = [
        dict(question='You add alt text to every image in an openly licensed chapter. Which permission is that?', correct_zone='revise',
             explanation='Adding alt text changes the work, and changing a work is revising it.'),
        dict(question='You show an openly licensed diagram, unchanged, on the projector. Which permission is that?', correct_zone='reuse',
             explanation='Using a work as it is, in your class, is reuse.'),
        dict(question='You copy the full set of source files of an open lab manual to an external drive. Which permission is that?', correct_zone='retain',
             explanation='Keeping your own copy for safekeeping is retaining.'),
        dict(question='You combine two chapters from different open textbooks and a public-domain map into one unit packet. Which permission is that?', correct_zone='remix',
             explanation='Combining two or more works into something new is remixing.'),
        dict(question='A colleague asks for the open worksheet you use, and you email them an unchanged copy. Which permission is that?', correct_zone='redistribute',
             explanation='Sharing copies with others is redistributing.'),
    ]
    return c, items, quiz
