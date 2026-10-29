"""Poster 14: Woven or Modular? The Lift-Out Test (Chapter 9, grid, 2 zones)."""
from svgkit import *

CH = '09-modularity-metadata'

META = dict(
    slug='woven-or-modular',
    title='Woven or Modular? The Lift-Out Test',
    chapter=CH,
    overlay='grid',
    topic='Woven versus modular design and the lift-out test',
    desc='A woven cloth beside three separate building blocks shows why a quiz that is woven into one page cannot be lifted out, while a modular one can.',
    intro=('Modularity is the seventh metric, and the lift-out test is the practical way to score it. This poster shows the same three pieces, a reading, a quiz, and a simulation, built two ways. '
           'On the left they are threads of one cloth, so pulling out the quiz unravels the rest. On the right they are separate blocks, each in its own folder, and the quiz lifts away cleanly. '
           'Four rows come from the chapter\'s table, and a strip along the bottom shows that modularity is a matter of degree.'),
    alt=('Two zones. Woven design: one long page in which a reading, a quiz, and a simulation are interlaced threads of one cloth, with sticky notes "as we saw in the last section" and "the diagram above". '
         'Modular design: a reading, a quiz, and a simulation as three separate blocks in separate folders, with the quiz block lifted away. '
         'Four comparison rows. Structure: one long page that mixes explanation, a quiz, and a simulation, against separate pieces. '
         'Taking out the quiz: copy it from the middle of the page and repair the links, against link or embed the quiz\'s own page. '
         'Revising the simulation: edit the whole page and risk breaking the reading, against edit the simulation\'s folder. '
         'Reuse by another teacher: take everything or nothing, against take any piece. A strip shows degrees of modularity from a single page, to a page with sections, to one file per part, to each part packaged with its own license and metadata.'),
    bloom='Analyze',
    objective='**apply** the lift-out test to decide whether a resource is woven or modular, and **place** it on the degrees of modularity.',
    objective_plain='apply the lift-out test to decide whether a resource is woven or modular, and place it on the degrees of modularity.',
    prereq=['The modularity metric and the standalone component from [Chapter 9](../../chapters/09-modularity-metadata/index.md).'],
    activities=[
        '**Explore (3 min).** Press each side and read its four rows. What changes about reuse?',
        '**Quiz (3 min).** Press **Quiz Me** and decide which design each statement describes.',
        '**Apply (4 min).** Pick one resource of yours. Copy one component into an empty file and read it cold. Does it still make sense?',
    ],
    assessment=[
        ('A quiz refers to "the diagram above". Does it pass the lift-out test?', 'No. A component that depends on its surroundings is not standalone.'),
        ('How does another teacher reuse a woven page?', 'Take everything or nothing.'),
        ('What is the far end of the degrees of modularity?', 'Each part packaged with its own license and metadata.'),
    ],
    connection='Modularity is metric 7 in the ten-metric rubric. It prepares Chapter 18, where components are packaged with a license and metadata.',
    ref_nums=[(CH, [3, 1, 2])],
    key_questions=['Can I lift this out and have it still make sense?', 'What breaks if I change this part?'],
    misconceptions=['Modular means short', 'A long page with headings is already modular'],
    good=['The same three pieces use the same three colors on both sides, so the eye sees that only the construction differs.'],
    verify=[(CH, '| Structure | One long page that mixes explanation, a quiz, and a simulation | Separate pieces: a reading, a quiz, and a simulation |'),
            (CH, '| Taking out the quiz | Copy it from the middle of the page and repair the links | Link or embed the quiz\'s own page |'),
            (CH, '| Revising the simulation | Edit the whole page and risk breaking the reading | Edit the simulation\'s folder |'),
            (CH, '| Reuse by another teacher | Take everything or nothing | Take any piece |'),
            (CH, 'as we saw in the last section'), (CH, 'the diagram above')],
)

READ_C, QUIZ_C, SIM_C = '#2c6fb7', '#e69500', '#00796b'
WOVEN, WOVEND = '#8a5a00', '#5c3c00'
MOD, MODD = '#1a6559', '#0e4a41'
ROWS = [
    ('Structure', 'One long page that mixes explanation, a quiz, and a simulation', 'Separate pieces: a reading, a quiz, and a simulation'),
    ('Taking out the quiz', 'Copy it from the middle of the page and repair the links', 'Link or embed the quiz\'s own page'),
    ('Revising the simulation', 'Edit the whole page and risk breaking the reading', 'Edit the simulation\'s folder'),
    ('Reuse by another teacher', 'Take everything or nothing', 'Take any piece'),
]
COLS = [READ_C, QUIZ_C, SIM_C]


def cloth(c, x, y, w, h):
    n = 12
    cw = w / n
    rh = h / 9
    for r in range(9):
        c.rect(x, y + r * rh + 2, w, rh - 4, fill=COLS[r // 3], opacity=0.95)
    for k in range(n):
        for r in range(9):
            if (k + r) % 2 == 0:
                c.rect(x + k * cw + 2, y + r * rh - 1, cw - 4, rh + 2, fill=COLS[k % 3], stroke=WHITE, sw=1.5, rx=3)
    c.rect(x, y, w, h, fill='none', stroke=INK, sw=3)


def note(c, x, y, w, text):
    c.poly([(x, y), (x + w, y - 4), (x + w + 2, y + 56), (x + 2, y + 58)], fill='#ffe66d', stroke=INK, sw=2)
    c.para(x + w / 2, y + 22, text, w - 14, 14, 1.2, 'bold', INK, 'middle', maxlines=3)


def block(c, x, y, w, h, col, kind):
    c.rect(x, y, w, h, fill=col, stroke=INK, sw=2.5, rx=8)
    c.rect(x + 8, y + 8, w - 16, 14, fill=WHITE, opacity=0.9, rx=3)
    if kind == 'quiz':
        for k in range(3):
            c.circle(x + 20, y + 40 + k * 20, 5, fill=WHITE)
            c.line(x + 32, y + 40 + k * 20, x + w - 14, y + 40 + k * 20, WHITE, 3)
    elif kind == 'sim':
        c.path('M%s,%s l16,-22 l16,10 l16,-26' % (x + 14, y + h - 14), stroke=WHITE, sw=3.5)
    else:
        for k in range(4):
            c.line(x + 14, y + 40 + k * 14, x + w - 14 - (16 if k == 3 else 0), y + 40 + k * 14, WHITE, 3)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Woven or Modular? The Lift-Out Test', 'The same three pieces, built two ways. Try to lift the quiz out.')
    y0, y1 = 100, 642
    lx, lw, rx, rw = 30, 560, 610, 560
    items = []
    # woven
    c.rect(lx, y0, lw, y1 - y0, fill=WHITE, stroke=WOVEN, sw=3, rx=14)
    c.rect(lx, y0, lw, 46, fill=WOVEN, rx=14)
    c.rect(lx, y0 + 24, lw, 22, fill=WOVEN)
    c.text(lx + 18, y0 + 32, 'Woven design', 24, 'bold', WHITE)
    c.text(lx + lw - 18, y0 + 32, 'one cloth', 18, 'normal', WHITE, 'end')
    cloth(c, lx + 30, y0 + 66, 250, 190)
    note(c, lx + 238, y0 + 80, 150, '"as we saw in the last section"')
    note(c, lx + 330, y0 + 160, 150, '"the diagram above"')
    c.arrow(lx + 400, y0 + 262, lx + 330, y0 + 226, RED, 4, 12)
    for (cx, col, t) in ((lx + 360, READ_C, 'reading'), (lx + 420, QUIZ_C, 'quiz'), (lx + 480, SIM_C, 'simulation')):
        pass
    # legend of threads
    for k, (col, t) in enumerate(((READ_C, 'reading'), (QUIZ_C, 'quiz'), (SIM_C, 'simulation'))):
        c.rect(lx + 30 + k * 130, y0 + 268, 18, 18, fill=col, rx=3)
        c.text(lx + 54 + k * 130, y0 + 283, t, 16, 'normal', INK)
    # modular
    c.rect(rx, y0, rw, y1 - y0, fill=WHITE, stroke=MOD, sw=3, rx=14)
    c.rect(rx, y0, rw, 46, fill=MOD, rx=14)
    c.rect(rx, y0 + 24, rw, 22, fill=MOD)
    c.text(rx + 18, y0 + 32, 'Modular design', 24, 'bold', WHITE)
    c.text(rx + rw - 18, y0 + 32, 'separate blocks', 18, 'normal', WHITE, 'end')
    for k, (col, kind) in enumerate(((READ_C, 'read'), (QUIZ_C, 'quiz'), (SIM_C, 'sim'))):
        bx = rx + 30 + k * 170
        ic_folder(c, bx - 2, y0 + 190, 144, 78, fill='#fff3b0')
        if kind == 'quiz':
            c.rect(bx + 10, y0 + 54, 120, 100, fill='none', stroke=GRAY, sw=2.5, rx=8, dash='6 5')
            block(c, bx + 10, y0 + 62, 120, 100, col, kind)
            c.rect(bx + 10, y0 + 54, 120, 100, fill='none')
        else:
            block(c, bx + 10, y0 + 100, 120, 92, col, kind)
    c.arrow(rx + 30 + 170 + 150, y0 + 150, rx + 30 + 170 + 150, y0 + 78, INK, 5, 14)
    # four rows
    c.text(lx + 18, y0 + 322, 'FOUR ROWS FROM THE CHAPTER', 12, 'bold', MUTED, spacing='1')
    c.text(rx + 18, y0 + 322, 'FOUR ROWS FROM THE CHAPTER', 12, 'bold', MUTED, spacing='1')
    for i, (feat, wv, md) in enumerate(ROWS):
        y = y0 + 336 + i * 50
        c.rect(lx + 10, y, lw - 20, 44, fill='#fdf1d6', rx=8)
        c.rect(rx + 10, y, rw - 20, 44, fill='#e3f4f1', rx=8)
        c.text(lx + 20, y + 17, feat, 13.5, 'bold', WOVEND, maxw=lw - 40)
        c.text(lx + 20, y + 37, wv, 14.5, 'normal', INK, maxw=lw - 40, minsize=12)
        c.text(rx + 20, y + 17, feat, 13.5, 'bold', MODD, maxw=rw - 40)
        c.text(rx + 20, y + 37, md, 14.5, 'normal', INK, maxw=rw - 40, minsize=12)
    # degrees strip
    ys = 674
    c.text(30, ys - 8, 'DEGREES OF MODULARITY', 12, 'bold', MUTED, spacing='1')
    steps = ['A single page', 'A page with sections', 'One file per part', 'Each part with its own license and metadata']
    sx = 250
    for k, t in enumerate(steps):
        wd = [140, 190, 160, 330][k]
        c.rect(sx, ys - 24, wd, 30, fill=[GRAYM, '#a8d5cc', '#5fb3a4', MOD][k], rx=6)
        c.text(sx + wd / 2, ys - 4, t, 14, 'bold', INK if k < 3 else WHITE, 'middle', maxw=wd - 8)
        if k < 3:
            c._head(sx + wd + 8, ys - 9, 0, 11, GRAY)
        sx += wd + 16
    items = [
        dict(id='woven', label='Woven design', color=WOVEN, box=(lx, y0, lx + lw, y1),
             summary='One long page where explanation, quiz, and simulation are threads of one cloth.',
             facts=[' | '.join(('Structure: %s' % ROWS[0][1],)), 'Taking out the quiz: %s.' % ROWS[1][1], 'Revising the simulation: %s.' % ROWS[2][1],
                    'Reuse by another teacher: %s.' % ROWS[3][1], 'Failure phrases: "as we saw in the last section" and "the diagram above".']),
        dict(id='modular', label='Modular design', color=MOD, box=(rx, y0, rx + rw, y1),
             summary='A reading, a quiz, and a simulation as separate pieces, each in its own folder.',
             facts=['Structure: %s.' % ROWS[0][2], 'Taking out the quiz: %s.' % ROWS[1][2], 'Revising the simulation: %s.' % ROWS[2][2],
                    'Reuse by another teacher: %s.' % ROWS[3][2],
                    'Modularity is a matter of degree: a single page, a page with sections, one file per part, each part with its own license and metadata.']),
    ]
    quiz = [
        dict(question='Which design makes another teacher take everything or nothing?', correct_zone='woven', explanation='Woven pages cannot be taken apart.'),
        dict(question='Which design lets you link or embed the quiz\'s own page?', correct_zone='modular', explanation='Each piece has its own page.'),
        dict(question='Which design risks breaking the reading when you revise the simulation?', correct_zone='woven', explanation='You edit the whole page.'),
        dict(question='Which design lets you edit the simulation\'s folder and leave the rest alone?', correct_zone='modular', explanation='Each part is in its own folder.'),
    ]
    return c, items, quiz
