"""Poster 21: Four Ways an Agent Gets It Wrong (Chapter 14, grid, 4 error cards plus an inset)."""
from svgkit import *

CH = '14-checking-agent-output'

META = dict(
    slug='four-agent-error-types',
    title='Four Ways an Agent Gets It Wrong',
    chapter=CH,
    overlay='grid',
    topic='The four types of AI agent error: factual, license, citation, and scoring',
    desc='Four field-guide cards for the agent error types, each with what it looks like, how a reviewer catches it, and how a prompt prevents it, plus the worked example "A 9 that should be a 5".',
    intro=('Classifying errors by type is a stated course outcome, because the type tells the reviewer how to catch the error and the prompt writer how to prevent it. '
           'This poster is a field guide for the review desk. Each card has the same three parts: what the error looks like, how to catch it, and how to prevent it. '
           'The inset at the bottom is the Chapter 14 worked example, "A 9 that should be a 5": the agent reported a 9, and its own evidence supports five passing checks. '
           'The tone is gently skeptical and not mocking.'),
    alt=('Four cards and an inset. Factual error: a wrong claim about the resource, such as a feature that is absent or a count that is off; catch it by opening the resource and checking the claim; prevent it by requiring a quotation or a location for every claim and a tool log for every measurement. '
         'License error: a wrong reading of the resource\'s license, or a missed or mismatched license; compare the claim with the statement itself; require the license statement quoted word for word, and "not stated" for anything it does not mention. '
         'Citation error: a reference that does not exist or does not support its claim; look up the source and read the passage; allow only sources found in the resource or supplied by the reviewer. '
         'Scoring error: a score that does not follow from the agent\'s own checks, or arithmetic that does not add up; recount the passes, recompute the band, and re-add the total; ask for the list of checks with a pass or fail on each, and have a spreadsheet or script add the total. '
         'Inset: the agent reported accessibility 9; the evidence supports five passing checks, which gives a 5.'),
    bloom='Analyze',
    objective='**classify** an agent error as factual, license, citation, or scoring, and **name** the reviewer check and the prompt fix for it.',
    objective_plain='classify an agent error as factual, license, citation, or scoring, and name the reviewer check and the prompt fix for it.',
    prereq=['Hallucination and agent error types from [Chapter 14](../../chapters/14-checking-agent-output/index.md).'],
    activities=[
        '**Explore (3 min).** Press each card and read the three parts. Which check needs the least outside information?',
        '**Quiz (3 min).** Press **Quiz Me** and match four reviewer checks to the error types.',
        '**Apply (4 min).** Find an agent report you have. Pick one claim and say which error type it could be, and which check would expose it.',
    ],
    assessment=[
        ('A reference does not exist. Which error type is it?', 'A citation error.'),
        ('What do you do to catch a scoring error?', 'Recount the passes, recompute the band, and re-add the total.'),
        ('How can a prompt prevent a license error?', 'Require the license statement quoted word for word, and "not stated" for anything it does not mention.'),
    ],
    connection='Agent output is a draft that a person must check. The error type tells the reviewer where to look first.',
    ref_nums=[(CH, [1, 7, 6])],
    key_questions=['What kind of mistake could this be?', 'What would expose it?'],
    misconceptions=['A fluent report is a correct report', 'An agent\'s evidence is always real'],
    good=['The "9 that should be a 5" example is from the chapter. The chapter\'s sources are invented, so the poster prints no real names.'],
    verify=[(CH, '| Factual error | A wrong claim about the resource, such as a feature that is absent or a count that is off | Open the resource and check the claim |'),
            (CH, '| License error | A wrong reading of the resource\'s license, or a missed or mismatched license | Compare the claim with the statement itself |'),
            (CH, '| Citation error | A reference that does not exist or does not support its claim | Look up the source and read the passage |'),
            (CH, '| Scoring error | A score that does not follow from the agent\'s own checks, or arithmetic that does not add up | Recount the passes, recompute the band, and re-add the total |'),
            (CH, '| Score: 9 | Five checks pass, which gives a score of 5 |')],
)

CARDS = [
    ('factual-error', 'Factual error', 'A wrong claim about the resource, such as a feature that is absent or a count that is off.',
     'Open the resource and check the claim.', 'Require a quotation or a location for every claim, and a tool log for every measurement.', '#1d4f86', '#e6eef8'),
    ('license-error', 'License error', 'A wrong reading of the resource\'s license, or a missed or mismatched license.',
     'Compare the claim with the statement itself.', 'Require the license statement quoted word for word, and "not stated" for anything it does not mention.', '#8a5a00', '#fdf1d6'),
    ('citation-error', 'Citation error', 'A reference that does not exist or does not support its claim.',
     'Look up the source and read the passage.', 'Allow only sources found in the resource or supplied by the reviewer.', '#573379', '#efe6f6'),
    ('scoring-error', 'Scoring error', 'A score that does not follow from the agent\'s own checks, or arithmetic that does not add up.',
     'Recount the passes, recompute the band, and re-add the total.', 'Ask for the list of checks with a pass or fail on each, and have a spreadsheet or script add the total.', '#b71c1c', '#fde8e8'),
]


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Four Ways an Agent Gets It Wrong', 'A field guide for the review desk. The type of error tells you how to catch it and how to prevent it.')
    n, gap = 4, 14
    x0, x1, y0, y1 = 30, 1170, 104, 500
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, name, looks, catch, prevent, hue, tint) in enumerate(CARDS):
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 48, fill=hue, rx=14)
        c.rect(x, y0 + 26, w, 22, fill=hue)
        c.circle(x + 28, y0 + 24, 14, fill=WHITE)
        ic_magnifier(c, x + 28, y0 + 24, 12, hue)
        c.text(x + 52, y0 + 32, name, 21, 'bold', WHITE, maxw=w - 62)
        yy = y0 + 70
        for (lab, txt, sz) in (('WHAT IT LOOKS LIKE', looks, 15.5), ('HOW TO CATCH IT', catch, 15.5), ('HOW TO PREVENT IT', prevent, 15.5)):
            c.text(x + 16, yy, lab, 12, 'bold', hue, spacing='1')
            yy = c.para(x + 16, yy + 22, txt, w - 32, sz, 1.22, 'normal', INK, maxlines=6) + 12
        items.append(dict(id=zid, label=name, color=hue, box=(x, y0, x + w, y1),
                          summary=looks, facts=['How to catch it: %s' % catch, 'How to prevent it: %s' % prevent]))
    # inset: a 9 that should be a 5
    iy0, iy1 = 516, 684
    c.rect(30, iy0, 1140, iy1 - iy0, fill='#fff7e6', stroke=ORANGE, sw=3, rx=14)
    c.text(48, iy0 + 30, 'Worked example: a 9 that should be a 5', 21, 'bold', INK)
    c.text(48, iy0 + 54, 'The agent gave accessibility a 9. The human reviewer scored it 5.', 16, 'normal', MUTED)
    rows = [('"Images have alt text" with no count', 'The count is 4 of 5, and 2 of the 4 are one word'),
            ('"Video is accessible" with no quote', 'The video has no captions'),
            ('"Contrast is fine" with no tool log', 'The contrast was never tested, so the check counts as failed')]
    c.text(48, iy0 + 84, 'WHAT THE AGENT REPORTED', 12, 'bold', MUTED, spacing='1')
    c.text(470, iy0 + 84, 'WHAT THE EVIDENCE SUPPORTS', 12, 'bold', MUTED, spacing='1')
    for k, (a, b) in enumerate(rows):
        yy = iy0 + 108 + k * 24
        c.text(48, yy, a, 15.5, 'normal', INK, maxw=400)
        c.arrow(432, yy - 5, 458, yy - 5, GRAY, 2.5, 8)
        c.text(470, yy, b, 15.5, 'normal', INK, maxw=480)
    # score tiles
    c.rect(990, iy0 + 22, 80, 70, fill=WHITE, stroke=RED, sw=3, rx=10)
    c.text(1030, iy0 + 70, '9', 44, 'bold', RED, 'middle')
    c.text(1030, iy0 + 108, 'reported', 14, 'normal', INK, 'middle')
    c.arrow(1076, iy0 + 57, 1098, iy0 + 57, INK, 3.5, 11)
    c.rect(1104, iy0 + 22, 56, 70, fill=WHITE, stroke=GREEN, sw=3, rx=10)
    c.text(1132, iy0 + 70, '5', 44, 'bold', GREEN, 'middle')
    c.text(1132, iy0 + 108, 'supported', 14, 'normal', INK, 'middle')
    items.append(dict(id='nine-that-should-be-five', label='A 9 that should be a 5', color=ORANGE, box=(30, iy0, 1170, iy1),
                      summary='The agent reported accessibility 9. Its evidence supports five passing checks, so the score is 5.',
                      facts=['"Images have alt text" with no count: the count is 4 of 5, and 2 of the 4 are one word.', '"Video is accessible" with no quote: the video has no captions.',
                             '"Contrast is fine" with no tool log: the contrast was never tested, so the check counts as failed.',
                             'Checks not verified: an empty list, but several checks were never verified.', 'Five checks pass, which gives a score of 5.']))
    quiz = [
        dict(question='Which card is a reference that does not exist or does not support its claim?', correct_zone='citation-error', explanation='Look up the source and read the passage.'),
        dict(question='Which card is a wrong claim such as a feature that is absent or a count that is off?', correct_zone='factual-error', explanation='Open the resource and check the claim.'),
        dict(question='Which card is caught by comparing the claim with the license statement itself?', correct_zone='license-error', explanation='Quote the statement word for word.'),
        dict(question='Which card is caught by recounting the passes and re-adding the total?', correct_zone='scoring-error', explanation='A score must follow from the agent\'s own checks.'),
        dict(question='Which zone shows an agent score of 9 that its own evidence supports as a 5?', correct_zone='nine-that-should-be-five', explanation='Five checks pass, so the score is 5.'),
    ]
    return c, items, quiz
