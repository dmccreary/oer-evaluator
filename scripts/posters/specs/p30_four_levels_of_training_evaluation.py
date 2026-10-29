"""Poster 30: Four Levels of Training Evaluation (Chapter 19, grid, 4 zones)."""
from svgkit import *

CH = '19-training-certifying-reviewers'

META = dict(
    slug='four-levels-of-training-evaluation',
    title='Four Levels of Training Evaluation',
    chapter=CH,
    overlay='grid',
    topic='The four levels of training evaluation and the evidence that belongs at each',
    desc='A four-step staircase of reaction, learning, behavior, and results, with the illustrative evidence for a workshop of 20 teachers at each step.',
    intro=('Most workshops stop at a happy survey, which measures only the first level. This staircase uses the model of Donald Kirkpatrick that Chapter 19 names: reaction, learning, behavior, and results. '
           'Each step asks its question and shows the chapter\'s evidence for a workshop of 20 teachers. All the numbers are illustrative, made up in the chapter to show the form, and the poster marks them that way. '
           'An arrow beneath shows that later levels take longer to collect. Without a comparison group a change may have other causes, and counts of reuse are weaker than evidence of learning.'),
    alt=('A four-step staircase rising from left to right. Reaction: did participants find the day useful? Illustrative evidence: 19 of 20 returned the exit survey, and 18 rated the day 4 or 5. '
         'Learning: did they gain the skills? 17 of 20 earned the certificate, and their calibration scores differed from the consensus by 1.1 points on average. '
         'Behavior: do they use the skills afterward? 12 of the 17 certified teachers scored another resource within three months. '
         'Results: did it change outcomes? 20 improved components were published, and 9 were reused by another teacher within three months. '
         'An arrow beneath says later levels take longer to collect. Every number is marked illustrative.'),
    bloom='Understand',
    objective='**place** a piece of workshop evidence at the right level of training evaluation and **explain** why a happy survey is not enough.',
    objective_plain='place a piece of workshop evidence at the right level of training evaluation and explain why a happy survey is not enough.',
    prereq=['Training evaluation from [Chapter 19](../../chapters/19-training-certifying-reviewers/index.md) and the cautions of Chapters 16 and 17.'],
    activities=[
        '**Explore (3 min).** Press each step. Which level is the easiest to collect, and which is the hardest?',
        '**Quiz (3 min).** Press **Quiz Me** and place four pieces of evidence on the right step.',
        '**Plan (4 min).** For a workshop you run, write one piece of evidence you could collect for each level.',
    ],
    assessment=[
        ('"17 of 20 teachers earned the certificate" belongs to which level?', 'Learning.'),
        ('"9 components were reused by another teacher" belongs to which level?', 'Results.'),
        ('Why is a count of reuse weaker than evidence of learning?', 'Without a comparison group, reuse may have other causes.'),
    ],
    connection='The staircase is a ready frame for a grant report, alongside the Grant Response and Grant-Period Timeline workshop pages.',
    ref_nums=[(CH, [5, 1, 10])],
    key_questions=['Which level does this evidence measure?', 'What would stronger evidence look like?'],
    misconceptions=['A happy exit survey shows the training worked', 'Counts of reuse prove learning'],
    good=['Every number on the poster is illustrative and made up in the chapter to show the form. Replace them with your own in data.json for a real workshop.'],
    verify=[(CH, '| Reaction | Did participants find the day useful? | 19 of 20 returned the exit survey, and 18 rated the day 4 or 5 |'),
            (CH, '| Learning | Did they gain the skills? | 17 of 20 earned the certificate, and their calibration scores differed from the consensus by 1.1 points on average |'),
            (CH, '| Behavior | Do they use the skills afterward? | 12 of the 17 certified teachers scored another resource within three months |'),
            (CH, '| Results | Did it change outcomes? | 20 improved components were published, and 9 were reused by another teacher within three months |'),
            (CH, 'counts of reuse are weaker than evidence of learning')],
)

LEVELS = [
    ('reaction', 'Reaction', 'Did participants find the day useful?', ['19 of 20 returned the exit survey', '18 rated the day 4 or 5'], '#00796b'),
    ('learning', 'Learning', 'Did they gain the skills?', ['17 of 20 earned the certificate', 'Calibration scores differed from the consensus by 1.1 points on average'], '#1d4f86'),
    ('behavior', 'Behavior', 'Do they use the skills afterward?', ['12 of the 17 certified teachers scored another resource within three months'], '#8a5a00'),
    ('results', 'Results', 'Did it change outcomes?', ['20 improved components were published', '9 were reused by another teacher within three months'], '#573379'),
]


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Four Levels of Training Evaluation', 'A happy survey measures only the first level. What would stronger evidence look like?')
    base = 596
    x0, cw, gap = 30, 276, 12
    items = []
    for i, (zid, name, q, evid, hue) in enumerate(LEVELS):
        h = 330 + 46 * i
        x = x0 + i * (cw + gap)
        top = base - h
        c.rect(x, top, cw, h, fill=WHITE, stroke=hue, sw=3, rx=12)
        c.rect(x, top, cw, 50, fill=hue, rx=12)
        c.rect(x, top + 26, cw, 24, fill=hue)
        c.circle(x + 26, top + 25, 15, fill=WHITE)
        c.text(x + 26, top + 31, str(i + 1), 17, 'bold', hue, 'middle')
        c.text(x + 52, top + 33, name, 24, 'bold', WHITE)
        yy = c.para(x + 16, top + 82, q, cw - 32, 21, 1.2, 'bold', INK, maxlines=3)
        c.text(x + 16, yy + 14, 'EVIDENCE FOR 20 TEACHERS', 12, 'bold', hue, spacing='1')
        yy += 38
        for e in evid:
            c.circle(x + 22, yy - 5, 4, fill=hue)
            yy = c.para(x + 34, yy, e, cw - 50, 16.5, 1.22, 'normal', INK, maxlines=4) + 6
        c.chip(x + 16, base - 38, 'illustrative', fill=GRAYL, color=INK, size=14, h=24, stroke=GRAY)
        items.append(dict(id=zid, label='%d. %s' % (i + 1, name), color=hue, box=(x, top, x + cw, base),
                          summary='%s Illustrative evidence for a workshop of 20 teachers.' % q,
                          facts=evid + ['These numbers are made up in the chapter to show the form.']))
    # slower arrow
    c.arrow(60, 628, 1140, 628, GRAY, 5, 16)
    c.text(60, 660, 'EASIER AND FASTER TO COLLECT', 13, 'bold', MUTED, spacing='1')
    c.text(1140, 660, 'HARDER AND SLOWER TO COLLECT', 13, 'bold', MUTED, 'end', spacing='1')
    c.text(600, 690, 'Without a comparison group a change may have other causes, and counts of reuse are weaker than evidence of learning.', 15, 'normal', MUTED, 'middle', maxw=1140)
    quiz = [
        dict(question='Which level does "17 of 20 earned the certificate" belong to?', correct_zone='learning', explanation='It shows the skills were demonstrated.'),
        dict(question='Which level does "19 of 20 returned the exit survey" belong to?', correct_zone='reaction', explanation='The exit survey measures only the first level.'),
        dict(question='Which level does "12 of the 17 certified teachers scored another resource within three months" belong to?', correct_zone='behavior', explanation='It shows the skills are used afterward.'),
        dict(question='Which level does "9 components were reused by another teacher" belong to?', correct_zone='results', explanation='Reuse is an outcome beyond the participants.'),
    ]
    return c, items, quiz
