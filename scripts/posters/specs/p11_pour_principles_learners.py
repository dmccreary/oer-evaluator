"""Poster 11: Four Principles, Five Learners (Chapter 7, grid, 4 zones)."""
from svgkit import *

CH = '07-accessibility'

META = dict(
    slug='pour-principles-learners',
    title='Four Principles, Five Learners',
    chapter=CH,
    overlay='grid',
    topic='The four WCAG principles and the learners each one protects',
    desc='Four zones for the WCAG principles Perceivable, Operable, Understandable, and Robust, each pairing an example criterion with the learners it protects.',
    intro=('Accessibility is full of standards language, and teachers need the human reason first. This poster joins two tables from Chapter 7: the four WCAG principles with an example criterion each, '
           'and five learners with the feature that lets each one use a resource. Perceivable covers the blind learner, the deaf learner, and the learner with low vision. Operable covers the learner who cannot use a mouse. '
           'Understandable covers the learner with a reading disability. Robust covers assistive technology. Some features serve more than one principle, so the pairing is an editorial choice for teaching.'),
    alt=('Four equal zones headed P, O, U, and R. Perceivable asks can users perceive the content; its example criterion is that non-text content has a text alternative; '
         'it protects a blind learner who needs text descriptions and a clear heading structure, a deaf learner who needs captions, and a learner with low vision who needs strong color contrast. '
         'Operable asks can users operate the controls; its example criterion is that all functions work with a keyboard; it protects a learner who cannot use a mouse and needs keyboard navigation. '
         'Understandable asks can users follow it; its example criterion is that the language of the page is identified; it protects a learner with a reading disability who needs clear structure and short paragraphs. '
         'Robust asks does it work with assistive technology; its example criterion is that custom controls expose a name and role.'),
    bloom='Understand',
    objective='**match** each learner support to the WCAG principle it serves, and **state** one example criterion for each principle.',
    objective_plain='match each learner support to the WCAG principle it serves, and state one example criterion for each principle.',
    prereq=['The accessibility metric from [Chapter 7](../../chapters/07-accessibility/index.md).'],
    activities=[
        '**Explore (3 min).** Press each letter. Which learners does it protect, and what gets in their way?',
        '**Quiz (3 min).** Press **Quiz Me** and place five learner supports under the right principle.',
        '**Check (4 min).** Open a page you teach from. Pick one support from each zone and test whether the page offers it.',
    ],
    assessment=[
        ('Which principle do captions for a deaf learner belong to?', 'Perceivable.'),
        ('Which principle asks that all functions work with a keyboard?', 'Operable.'),
        ('What does Robust ask about a custom control?', 'That it exposes a name and role to assistive technology.'),
    ],
    connection='Accessibility is metric 4 in the ten-metric rubric. The rubric starts from the people, so a reviewer knows why each criterion matters.',
    ref_nums=[(CH, [1, 6, 7, 9])],
    key_questions=['Who cannot use this yet?', 'Which principle does the missing support belong to?'],
    misconceptions=['Accessibility only matters for a few learners', 'Captions are only for deaf learners', 'A support belongs to exactly one principle'],
    good=['The learner pairing is an editorial choice. Some features serve more than one principle, and the author confirms the mapping.'],
    verify=[(CH, '| Perceivable | Can users perceive the content? | Non-text content has a text alternative |'),
            (CH, '| Operable | Can users operate the controls? | All functions work with a keyboard |'),
            (CH, '| Understandable | Can users follow it? | The language of the page is identified |'),
            (CH, '| Robust | Does it work with assistive technology? | Custom controls expose a name and role |'),
            (CH, '| A learner with low vision | Faint text on a pale background | Strong color contrast and text that enlarges |'),
            (CH, '| A learner with a reading disability | Dense text | Clear structure, short paragraphs, and alternative formats |')],
)

PRIN = [
    ('P', 'Perceivable', 'Can users perceive the content?', 'Non-text content has a text alternative', '#1d4f86', '#e6eef8',
     [('blind', 'Blind learner', 'Text descriptions of images and a clear heading structure'),
      ('deaf', 'Deaf learner', 'Captions on video'),
      ('lowvision', 'Low-vision learner', 'Strong color contrast and text that enlarges')]),
    ('O', 'Operable', 'Can users operate the controls?', 'All functions work with a keyboard', '#1a6559', '#e3f4f1',
     [('keyboard', 'Learner who cannot use a mouse', 'Keyboard navigation')]),
    ('U', 'Understandable', 'Can users follow it?', 'The language of the page is identified', '#8a5a00', '#fdf1d6',
     [('reading', 'Learner with a reading disability', 'Clear structure, short paragraphs, and alternative formats')]),
    ('R', 'Robust', 'Does it work with assistive technology?', 'Custom controls expose a name and role', '#573379', '#efe6f6',
     [('tech', 'Assistive technology', 'A name and a role it can read and operate')]),
]


def learner(c, kind, cx, cy, hue):
    """Person plus one cue, in a 64 by 64 area."""
    ic_person(c, cx - 8, cy, 22, hue)
    if kind == 'blind':
        c.path('M%s,%s q10,-8 20,0 q-10,8 -20,0 z' % (cx + 4, cy - 14), fill=WHITE, stroke=INK, sw=2)
        c.line(cx + 4, cy - 22, cx + 24, cy - 6, RED, 3)
    elif kind == 'deaf':
        c.rect(cx + 6, cy - 26, 30, 20, fill=INK, rx=4)
        c.text(cx + 21, cy - 11, 'CC', 13, 'bold', WHITE, 'middle')
    elif kind == 'lowvision':
        ic_magnifier(c, cx + 20, cy - 8, 18, INK)
    elif kind == 'keyboard':
        c.rect(cx + 4, cy - 18, 32, 20, fill=WHITE, stroke=INK, sw=2.5, rx=4)
        for k in range(3):
            c.rect(cx + 8 + k * 9, cy - 13, 6, 5, fill=INK)
        c.rect(cx + 14, cy - 5, 14, 4, fill=INK)
    elif kind == 'reading':
        for k in range(3):
            c.rect(cx + 4, cy - 26 + k * 10, 34, 7, fill=GRAYM, rx=2)
    else:
        ic_gear(c, cx + 18, cy - 10, 14, hue)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Four Principles, Five Learners', 'WCAG groups its criteria under four principles. Each one exists for real people.')
    n, gap = 4, 14
    x0, x1, y0, y1 = 30, 1170, 108, 640
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (letter, name, q, crit, hue, tint, learners) in enumerate(PRIN):
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 108, fill=hue, rx=14)
        c.rect(x, y0 + 80, w, 28, fill=hue)
        c.text(x + 52, y0 + 78, letter, 72, 'bold', WHITE, 'middle')
        c.text(x + 100, y0 + 48, name, 24, 'bold', WHITE, maxw=w - 110)
        c.para(x + 100, y0 + 76, q, w - 110, 15, 1.2, 'normal', WHITE, maxlines=2)
        # learners
        c.text(x + 16, y0 + 134, 'WHO IT PROTECTS', 12, 'bold', hue, spacing='1')
        yy = y0 + 160
        many = len(learners) > 1
        ch_, step = (84, 92) if many else (110, 120)
        for (kind, who, support) in learners:
            c.rect(x + 10, yy - 12, w - 20, ch_, fill=tint, rx=10)
            learner(c, kind, x + 50, yy + ch_ / 2 - 8, hue)
            c.para(x + 100, yy + 10, who, w - 114, 15.5, 1.15, 'bold', INK, maxlines=2)
            c.para(x + 100, yy + (32 if many else 54), support, w - 114, 14, 1.18, 'normal', INK, maxlines=3)
            yy += step
        # example criterion
        c.rect(x + 10, y1 - 96, w - 20, 84, fill=tint, stroke=hue, sw=2, rx=10)
        c.text(x + 20, y1 - 74, 'EXAMPLE CRITERION', 12, 'bold', hue, spacing='1')
        c.para(x + 20, y1 - 50, crit, w - 40, 17, 1.2, 'bold', INK, maxlines=2)
        facts = ['Question: %s' % q, 'Example criterion: %s.' % crit]
        facts += ['%s: %s.' % (who, support) for (_, who, support) in learners]
        items.append(dict(id=name.lower(), label='%s (%s)' % (name, letter), color=hue, box=(x, y0, x + w, y1),
                          summary='%s: %s' % (name, q), facts=facts))
    c.text(40, 674, 'Principles and the example criteria are from Chapter 7. Pairing learners with principles is an editorial choice for teaching.', 15, 'normal', MUTED, maxw=1120)
    quiz = [
        dict(question='Which principle do captions for a deaf learner serve?', correct_zone='perceivable', explanation='A user who cannot hear needs another way to perceive the content.'),
        dict(question='Which principle asks that all functions work with a keyboard?', correct_zone='operable', explanation='A user who cannot use a mouse must be able to control the page.'),
        dict(question='Which principle includes identifying the language of the page and keeping paragraphs short?', correct_zone='understandable', explanation='Users can follow a page that is clearly structured and identified.'),
        dict(question='Which principle says custom controls must expose a name and a role?', correct_zone='robust', explanation='Assistive technology must be able to read and operate them.'),
        dict(question='Which principle do strong color contrast and enlargeable text for low vision serve?', correct_zone='perceivable', explanation='A user with low vision must be able to see the content.'),
    ]
    return c, items, quiz
