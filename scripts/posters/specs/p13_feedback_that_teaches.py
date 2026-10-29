"""Poster 13: Feedback That Teaches (Chapter 8, grid, 4 zones)."""
from svgkit import *

CH = '08-practice-feedback'

META = dict(
    slug='feedback-that-teaches',
    title='Feedback That Teaches',
    chapter=CH,
    overlay='grid',
    topic='What makes a feedback message teach',
    desc='One question and one wrong answer, answered four ways, with each message rated against four criteria; only the last one passes all four.',
    intro=('Feedback is the part of practice that does the teaching. This poster holds the situation constant: the question "Which describes infiltration?" and a learner who chose "water flowing over the ground". '
           'It answers the same wrong answer four ways, ordered from least to most helpful, and rates each message against the criteria in Chapter 8: it says the answer was wrong, it explains why, '
           'it points toward the right idea, and it does not blame. Only the last message passes all four. Chapter 15 has agents write practice questions, so the same yardstick applies to what they produce.'),
    alt=('The question "Which describes infiltration?" and the learner\'s choice, B, water flowing over the ground. Four messages in order of helpfulness. '
         '"Wrong." says the answer failed, explains nothing, points nowhere, and does not blame; the learner is puzzled; weak. '
         '"Good try!" does not say whether the answer was right, explains nothing, points nowhere, and does not blame; the learner is still puzzled; weak. '
         '"Incorrect. The answer is A." says the answer was wrong and gives the answer but no reason; weak. '
         '"Not quite. Water flowing over the ground is runoff. Infiltration is water soaking into the ground, so the answer is A." says it was wrong, explains why, points toward the right idea, and does not blame; the learner understands; strong.'),
    bloom='Evaluate',
    objective='**rate** a feedback message against four criteria and **explain** why only one of four messages for the same wrong answer is strong.',
    objective_plain='rate a feedback message against four criteria and explain why only one of four messages for the same wrong answer is strong.',
    prereq=['The feedback metric from [Chapter 8](../../chapters/08-practice-feedback/index.md).'],
    activities=[
        '**Explore (3 min).** Press each message and read what it does. Which criterion does each weak message miss?',
        '**Quiz (3 min).** Press **Quiz Me** and find the message that matches each description.',
        '**Rewrite (4 min).** Take one wrong answer from a quiz you use. Write a message that names the likely mix-up and points to what to review.',
    ],
    assessment=[
        ('A message says "Incorrect. The answer is A." Is it strong?', 'No. It gives the answer and no reason.'),
        ('What does "Good try!" fail to do?', 'It does not say whether the answer was right.'),
        ('What four things does a helpful message do?', 'Says the answer was wrong, explains why, points toward the right idea, and does not blame.'),
    ],
    connection='Feedback is part of the practice and feedback metric. Because agents write practice questions in Chapter 15, reviewers use the same four criteria on what they produce.',
    ref_nums=[(CH, [1, 2, 8])],
    key_questions=['Does the message name the likely mix-up?', 'Does it point to what to do next?'],
    misconceptions=['Telling the learner the right answer is enough', 'Encouragement alone is helpful feedback'],
    good=['The wording of the messages is exact and not paraphrased. The check and cross marks are rated against the four criteria in the chapter.'],
    verify=[(CH, 'A learner chooses "water flowing over the ground" for the question "Which describes infiltration?"'),
            (CH, '"Not quite. Water flowing over the ground is runoff. Infiltration is water soaking into the ground, so the answer is A."'),
            (CH, '| 4 | "Good try!" | Not helpful | It does not say whether the answer was right. |'),
            (CH, 'says the answer was wrong, explains why, and points toward the right idea or the next step, without blaming the learner')],
)

CRIT = ['Says the answer was wrong', 'Explains why', 'Points toward the right idea', 'Does not blame']
MSGS = [
    ('wrong', 'Wrong.', [1, 0, 0, 1], 'Weak', 'puzzled', '#b71c1c', 'Says the answer failed and says nothing else.'),
    ('good-try', 'Good try!', [0, 0, 0, 1], 'Weak', 'puzzled2', '#8a5a00', 'Does not say whether the answer was right.'),
    ('incorrect-a', 'Incorrect. The answer is A.', [1, 0, 0, 1], 'Weak', 'flat', '#8a5a00', 'Gives the answer and no reason.'),
    ('not-quite', 'Not quite. Water flowing over the ground is runoff. Infiltration is water soaking into the ground, so the answer is A.',
     [1, 1, 1, 1], 'Strong', 'happy', '#1b5e20', 'Corrects, explains, and names the mix-up.'),
]


def face(c, cx, cy, r, kind, hue):
    c.circle(cx, cy, r, fill='#fff3b0', stroke=INK, sw=2.5)
    c.circle(cx - r * .35, cy - r * .15, r * .1, fill=INK)
    c.circle(cx + r * .35, cy - r * .15, r * .1, fill=INK)
    if kind == 'happy':
        c.path('M%s,%s q%s,%s %s,0' % (cx - r * .4, cy + r * .3, r * .4, r * .4, r * .8), stroke=INK, sw=2.5)
    elif kind == 'flat':
        c.line(cx - r * .35, cy + r * .4, cx + r * .35, cy + r * .4, INK, 2.5)
        c.line(cx - r * .55, cy - r * .45, cx - r * .15, cy - r * .35, INK, 2.5)
    else:
        c.path('M%s,%s q%s,%s %s,0 t%s,0' % (cx - r * .45, cy + r * .42, r * .22, -r * .2, r * .45, r * .45), stroke=INK, sw=2.5)
        c.line(cx - r * .55, cy - r * .35, cx - r * .15, cy - r * .5, INK, 2.5)
        c.line(cx + r * .15, cy - r * .5, cx + r * .55, cy - r * .35, INK, 2.5)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Feedback That Teaches', 'One wrong answer, four messages, from least to most helpful.')
    # situation banner
    c.rect(30, 98, 1140, 62, fill=WHITE, stroke=GRAYM, sw=2.5, rx=12)
    c.text(46, 125, 'Question: "Which describes infiltration?"', 20, 'bold', INK)
    c.text(46, 150, 'The learner chose B: "Water flowing over the ground." The right answer is A: "Water soaking into the ground."', 17, 'normal', INK, maxw=1100)
    n, gap = 4, 14
    x0, x1, y0, y1 = 30, 1170, 176, 650
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, msg, marks, verdict, mood, hue, does) in enumerate(MSGS):
        x = x0 + i * (w + gap)
        strong = verdict == 'Strong'
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 46, fill=hue, rx=14)
        c.rect(x, y0 + 24, w, 22, fill=hue)
        c.text(x + 16, y0 + 31, 'Message %d' % (i + 1), 20, 'bold', WHITE)
        c.chip(x + w - 14, y0 + 9, verdict.upper(), fill=WHITE, color=hue, size=14, h=28, anchor='end')
        face(c, x + 36, y0 + 90, 24, mood, hue)
        c.text(x + 72, y0 + 84, 'Learner feels', 13, 'normal', MUTED)
        c.text(x + 72, y0 + 102, {'puzzled': 'puzzled', 'puzzled2': 'still puzzled', 'flat': 'knows what, not why', 'happy': 'understanding'}[mood], 17, 'bold', INK, maxw=w - 80)
        # message
        c.rect(x + 12, y0 + 128, w - 24, 140, fill=GRAYL if not strong else '#e5f2e6', rx=10)
        c.text(x + 22, y0 + 150, 'MESSAGE', 12, 'bold', MUTED, spacing='1')
        c.para(x + 22, y0 + 178, '“%s”' % msg, w - 44, 18 if len(msg) < 40 else 16.5, 1.25, 'bold', INK, maxlines=6)
        # criteria
        yy = y0 + 304
        for k, name in enumerate(CRIT):
            ok = marks[k]
            (ic_check if ok else ic_cross)(c, x + 30, yy - 6, 12, GREEN if ok else RED)
            c.text(x + 52, yy, name, 16, 'normal', INK, maxw=w - 62)
            yy += 38
        c.para(x + 16, y1 - 36, does, w - 30, 14, 1.2, 'normal', MUTED, maxlines=2)
        items.append(dict(id=zid, label='Message %d: %s' % (i + 1, msg if len(msg) < 30 else 'Not quite...'), color=hue, box=(x, y0, x + w, y1),
                          summary='%s Rated %s.' % (does, verdict.lower()),
                          facts=['Message: "%s"' % msg] + ['%s: %s.' % (name, 'yes' if marks[k] else 'no') for k, name in enumerate(CRIT)]))
    c.text(40, 678, 'Messages and ratings follow the Chapter 8 worked example. A check means the message meets the criterion.', 14, 'normal', MUTED, maxw=1120)
    quiz = [
        dict(question='Which message says only that the answer failed and nothing else?', correct_zone='wrong', explanation='"Wrong." is weak.'),
        dict(question='Which message does not say whether the answer was right?', correct_zone='good-try', explanation='"Good try!" is weak.'),
        dict(question='Which message gives the answer and no reason?', correct_zone='incorrect-a', explanation='"Incorrect. The answer is A." is weak.'),
        dict(question='Which message passes all four criteria?', correct_zone='not-quite', explanation='It corrects, explains, and names the mix-up.'),
    ]
    return c, items, quiz
