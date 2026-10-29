"""Poster 1: The OER Evaluator Loop (all chapters, callout, 8 markers). The artwork carries no text."""
import math

from svgkit import *

META = dict(
    slug='oer-evaluator-loop',
    title='The OER Evaluator Loop',
    chapter='all',
    overlay='callout',
    layout='dual-panel',
    topic='The whole book as one closed loop of evaluation, improvement, testing, and publishing',
    desc='A closed loop with eight numbered stations that shows how the chapters fit together, and why test results are used to calibrate the AI agent.',
    intro=('This poster is a map of the whole book. Eight stations sit on one closed loop. A reader first learns what OER and licenses are, '
           'scores a resource by hand with the ten-metric rubric, directs an AI agent to make a first pass, and checks the agent\'s evidence. '
           'The reader then improves the lowest metrics with agents, tests the change with students, calibrates the agent against the test results, '
           'and publishes and trains others. The thick arrow that returns from calibration to the agent\'s first pass is the one that matters: it is how automated scores earn trust.'),
    alt=('A closed loop of eight numbered stations. 1 Understand OER and licenses, Chapters 1 and 2. 2 Score a resource by hand with the ten-metric rubric, Chapters 3 to 11. '
         '3 Direct an AI agent to make a first pass, Chapters 12 and 13. 4 Check the agent\'s evidence, Chapter 14. 5 Improve the lowest metrics with agents, Chapter 15. '
         '6 Test the change with students in an A/B test, Chapters 16 and 17. 7 Calibrate the agent against the test results, Chapters 14 and 17. '
         '8 Publish and train others, Chapters 18 and 19. A thick return arrow runs from station 7 back to station 3. Stations 1 to 4 are one color, station 5 another, and stations 6 to 8 a third.'),
    bloom='Understand',
    objective='**describe** the eight stations of the OER Evaluator loop in order and **explain** why test results are used to calibrate the AI agent.',
    objective_plain='describe the eight stations of the OER Evaluator loop in order and explain why test results are used to calibrate the AI agent.',
    prereq=['None. This poster is the overview, so it works before or after any chapter.'],
    activities=[
        '**Explore (3 min).** Hover over each marker in order, 1 to 8. Which station would your team start at?',
        '**Quiz (3 min).** Press **Quiz** and find each station from its description.',
        '**Discuss (4 min).** Marker 7 returns to marker 3. In your own words, what changes in the agent\'s next pass after calibration?',
    ],
    assessment=[
        ('Which station comes right after "check the agent"?', 'Improve the lowest metrics with agents (Chapter 15).'),
        ('What does the return arrow from station 7 to station 3 mean?', 'Test results calibrate the agent, so its next first pass can be trusted more.'),
        ('Which chapters teach scoring by hand?', 'Chapters 3 to 11.'),
    ],
    connection=('The course description lays out a path from evaluation to improvement to testing, with test results used to check and calibrate the automated scores. '
                'This poster is that path in one picture.'),
    refs=['[Open educational resources](https://en.wikipedia.org/wiki/Open_educational_resources). Wikipedia. Background for station 1.',
          '[Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Background for station 2.',
          '[Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)). Wikipedia. Why station 4 checks the agent\'s evidence.',
          '[A/B testing](https://en.wikipedia.org/wiki/A/B_testing). Wikipedia. Background for station 6.',
          '[Calibration (statistics)](https://en.wikipedia.org/wiki/Calibration_(statistics)). Wikipedia. Background for station 7.'],
    key_questions=['Where am I on the loop?', 'What evidence lets me trust an automated score?'],
    misconceptions=['An AI agent can replace the human review', 'The loop ends when a resource is published'],
    good=['Chapter numbers come from the chapter list. If chapters move, update the marker descriptions in `data.json`.'],
    verify=[],
)

TEAL_, TEALD_ = '#00796b', '#004d40'
AMBER, AMBERD = '#c77700', '#8a5a00'
PLUM, PLUMD = '#ad1457', '#7b0e3d'

STATIONS = [
    dict(id=1, fam='eval', label='Understand OER and licenses',
         hint='A book with an open lock on its cover, at the start of the loop.',
         description='Learn what makes a resource open and how the six Creative Commons licenses work. Chapters 1 and 2.',
         tip='Open means permission, not price. Everything later in the loop depends on reading a license correctly.'),
    dict(id=2, fam='eval', label='Score a resource by hand with the ten-metric rubric',
         hint='A worksheet with a column of check boxes.',
         description='Score ten metrics, five for quality and five for reusability, and add them up to a total out of 100. Chapters 3 to 11.',
         tip='Scoring by hand first gives you the human judgment that the agent will later be compared with.'),
    dict(id=3, fam='eval', label='Direct an AI agent to make a first pass',
         hint='A window with a prompt arrow, where the return arrow ends.',
         description='Write a rubric prompt, run the agent, and collect its scores with evidence. Chapters 12 and 13.',
         tip='The return arrow from station 7 ends here: each pass should be better calibrated than the last.'),
    dict(id=4, fam='eval', label='Check the agent\'s evidence',
         hint='A magnifying glass over a page.',
         description='Open each quoted source and recompute each score. Look for factual, license, citation, and scoring errors. Chapter 14.',
         tip='A fluent report is not a correct report. Agreement with a human can also come from chance.'),
    dict(id=5, fam='improve', label='Improve the lowest metrics with agents',
         hint='A wrench beside an upward arrow, the only marker in its color.',
         description='Fix the lowest-scoring metric first, using agents for alt text, readability, metadata, and more, with a human check on every change. Chapter 15.',
         tip='An agent\'s edited copy is a derivative work, so read the license before the first edit.'),
    dict(id=6, fam='test', label='Test the change with students in an A/B test',
         hint='Two groups of people separated by a vertical divider.',
         description='Randomly assign students to the original or the improved version, and compare learning gain. Chapters 16 and 17.',
         tip='Change one thing at a time, and say that a small test is evidence, not proof.'),
    dict(id=7, fam='test', label='Calibrate the agent against the test results',
         hint='A dial with a needle, at the start of the thick return arrow.',
         description='Compare the agent\'s scores with what the students actually learned, then adjust the prompt. Chapters 14 and 17.',
         tip='This is the thick return arrow to station 3. It is how automated scores earn trust.'),
    dict(id=8, fam='test', label='Publish and train others',
         hint='A ribbon badge with a star, just before the loop closes.',
         description='Package improved components with a license and metadata, publish them openly, and train other teachers. Chapters 18 and 19.',
         tip='Published work and trained reviewers bring new resources back to station 1.'),
]
FAM = {'eval': (TEAL_, TEALD_), 'improve': (AMBER, AMBERD), 'test': (PLUM, PLUMD)}


def ring_pt(cx, cy, rx, ry, deg):
    a = math.radians(deg)
    return cx + rx * math.cos(a), cy + ry * math.sin(a)


def icon(c, k, x, y, col):
    if k == 1:  # open book with an open lock
        c.poly([(x - 28, y - 14), (x, y - 8), (x, y + 24), (x - 28, y + 18)], fill=WHITE, stroke=INK, sw=2.5)
        c.poly([(x + 28, y - 14), (x, y - 8), (x, y + 24), (x + 28, y + 18)], fill=WHITE, stroke=INK, sw=2.5)
        ic_lock(c, x, y - 12, 12, open_=True, fill=col)
    elif k == 2:  # rubric sheet
        ic_doc(c, x - 20, y - 28, 40, 56, label=None, fold=9)
        for j in range(3):
            c.rect(x - 12, y - 8 + j * 12, 7, 7, fill=WHITE, stroke=INK, sw=1.5)
            c.line(x - 1, y - 4 + j * 12, x + 11, y - 4 + j * 12, GRAYM, 2.5)
    elif k == 3:  # agent window with prompt
        c.rect(x - 30, y - 22, 60, 44, fill=WHITE, stroke=INK, sw=2.5, rx=5)
        c.rect(x - 30, y - 22, 60, 11, fill=col, rx=5)
        c.path('M%s,%s l8,6 l-8,6' % (x - 20, y - 2), stroke=INK, sw=3)
        c.line(x - 6, y + 12, x + 12, y + 12, INK, 3)
    elif k == 4:  # magnifier over page
        ic_doc(c, x - 26, y - 28, 38, 50, label=None, fold=8)
        ic_magnifier(c, x + 8, y + 6, 22, INK)
    elif k == 5:  # wrench and up arrow
        ic_wrench(c, x - 8, y + 4, 24, INK)
        c.arrow(x + 22, y + 22, x + 22, y - 18, INK, 4, 11)
    elif k == 6:  # two groups and divider
        c.line(x, y - 28, x, y + 28, INK, 3, '5 4')
        for dx, cc in ((-17, Q), (17, R)):
            ic_person(c, x + dx, y - 6, 12, cc)
            ic_person(c, x + dx, y + 16, 8, cc)
    elif k == 7:  # dial
        c.path('M%s,%s A28,28 0 0 1 %s,%s' % (x - 28, y + 12, x + 28, y + 12), stroke=INK, sw=5, cap='butt')
        for t in range(5):
            a = math.radians(180 + 45 * t)
            c.line(x + 20 * math.cos(a), y + 12 + 20 * math.sin(a), x + 25 * math.cos(a), y + 12 + 25 * math.sin(a), INK, 2.5)
        c.line(x, y + 12, x + 15, y - 8, ORANGE, 4)
        c.circle(x, y + 12, 5, fill=INK)
    else:  # badge
        c.poly([(x - 14, y + 10), (x - 22, y + 32), (x - 8, y + 26), (x, y + 34), (x + 4, y + 12)], fill=col, stroke=INK, sw=2)
        c.poly([(x + 14, y + 10), (x + 22, y + 32), (x + 8, y + 26), (x, y + 34), (x - 4, y + 12)], fill=col, stroke=INK, sw=2)
        c.circle(x, y - 6, 22, fill='#fff3b0', stroke=INK, sw=2.5)
        ic_star(c, x, y - 6, 12, ORANGE)


def draw():
    c = Canvas(1000, 700)
    cx, cy, rx, ry = 500, 350, 360, 250
    degs = [-112.5 + 45 * i for i in range(8)]
    pos = [ring_pt(cx, cy, rx, ry, d) for d in degs]
    # ring and direction chevrons
    c.ellipse(cx, cy, rx, ry, fill='none', stroke=GRAYM, sw=12)
    for i, d in enumerate(degs):
        m = math.radians(d + 22.5)
        x, y = cx + rx * math.cos(m), cy + ry * math.sin(m)
        tx, ty = -rx * math.sin(m), ry * math.cos(m)
        ang = math.atan2(ty, tx)
        c._head(x + 10 * math.cos(ang), y + 10 * math.sin(ang), ang, 26, GRAY)
    # ten-metric dots in the middle, quality and reusability in the book's two colors
    for j in range(10):
        row, col = divmod(j, 5)
        x, y = 440 + col * 30, 225 + row * 30
        if j < 5:
            c.circle(x, y, 10, fill=Q)
        else:
            c.rect(x - 10, y - 10, 20, 20, fill=R, rx=2)
    # return arrow: station 7 -> station 3, the strongest line on the poster
    p7, p3 = pos[6], pos[2]
    c.curve_arrow(p7[0] + 40, p7[1] + 18, 500, 505, p3[0] - 42, p3[1] + 16, ORANGE, 12, 30)
    c.curve_arrow(p7[0] + 40, p7[1] + 18, 500, 505, p3[0] - 42, p3[1] + 16, INK, 2, 1)
    # stations
    items = []
    for s, (x, y) in zip(STATIONS, pos):
        col, cold = FAM[s['fam']]
        c.circle(x, y, 52, fill=WHITE, stroke=col, sw=7)
        c.circle(x, y, 44, fill='#f3f6fa')
        icon(c, s['id'], x, y, col)
        item = dict(s)
        item['color'] = col
        item['at'] = (x - 52, y) if x < cx else (x + 52, y)
        item['radius'] = 3.0
        items.append(item)
    return c, items, []
