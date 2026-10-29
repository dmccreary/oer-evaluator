"""Poster 26: Five Ways a Test Can Lie to You (Chapter 16, grid, 5 zones)."""
from svgkit import *

CH = '16-ab-testing-design'

META = dict(
    slug='five-confounders',
    title='Five Ways a Test Can Lie to You',
    chapter=CH,
    overlay='grid',
    topic='Five confounding variables in a classroom A/B test and their defenses',
    desc='Five paired panels, one per confounder, each showing a tilted balance scale for how it misleads and a level scale for the defense.',
    intro=('Small classroom tests fail on confounds far more often than on statistics. This poster is a pre-flight checklist for a test plan. '
           'Each of the five panels from the Chapter 16 table has a pair of balance scales. The top scale is tilted by a hidden weight, which is how the confounder misleads. '
           'The bottom scale is level, which is the defense. The weights are neutral: a confounder is hidden and is not villainous. '
           'Before you trust any difference between groups, ask what else is different besides the version.'),
    alt=('Five panels, each with a tilted scale above a level scale. Different teachers: one teacher\'s enthusiasm lifts one group; use one teacher for both groups. '
         'Different times of day: students are more alert at one time; run both groups at the same time. '
         'Extra help: one group gets a review or hints; use the same script and help for both. '
         'Different tests: the versions are measured in different ways; use the same test and key for both. '
         'Student choice: motivated students choose one version; assign at random.'),
    bloom='Analyze',
    objective='**identify** the confounder in a test setup and **name** its defense.',
    objective_plain='identify the confounder in a test setup and name its defense.',
    prereq=['The control group and the one-difference rule from [Chapter 16](../../chapters/16-ab-testing-design/index.md).'],
    activities=[
        '**Explore (3 min).** Press each panel. What is the hidden weight in each tilted scale?',
        '**Quiz (3 min).** Press **Quiz Me** and match four test setups to their confounders.',
        '**Preflight (4 min).** Take a test plan of your own. Go through the five panels and say which defense you use for each.',
    ],
    assessment=[
        ('Students choose which version to use. What is the confounder, and what is the defense?', 'Student choice, because motivated students choose one version. Defense: random assignment.'),
        ('One group takes the test in the morning and the other after lunch. Which confounder?', 'Different times of day. Run both groups at the same time.'),
        ('What question should you ask before trusting a difference between groups?', 'What else was different besides the version?'),
    ],
    connection='This is the one-difference rule: arrange everything except the version to be the same, and let random assignment handle what you cannot arrange.',
    ref_nums=[(CH, [1, 2, 7, 8])],
    key_questions=['What else is different between the groups?', 'Which defense removes it?'],
    misconceptions=['A big difference proves the version caused it', 'Volunteers make a fair comparison'],
    good=['The weights are drawn as neutral gray blocks, since a confounder is hidden and is not a villain.'],
    verify=[(CH, '| Different teachers | One teacher\'s enthusiasm lifts one group | One teacher for both groups |'),
            (CH, '| Different times of day | Students are more alert at one time | Both groups at the same time |'),
            (CH, '| Extra help | One group gets a review or hints | The same script and help for both |'),
            (CH, '| Different tests | The versions are measured in different ways | The same test and key for both |'),
            (CH, '| Student choice | Motivated students choose one version | Random assignment |')],
)

HUES = [('#1d4f86', '#e6eef8'), ('#00796b', '#e3f4f1'), ('#8a5a00', '#fdf1d6'), ('#573379', '#efe6f6'), ('#b71c1c', '#fde8e8')]
ROWS = [
    ('different-teachers', 'Different teachers', 'One teacher\'s enthusiasm lifts one group.', 'One teacher for both groups.', 'teacher'),
    ('different-times', 'Different times of day', 'Students are more alert at one time.', 'Both groups at the same time.', 'clock'),
    ('extra-help', 'Extra help', 'One group gets a review or hints.', 'The same script and help for both.', 'help'),
    ('different-tests', 'Different tests', 'The versions are measured in different ways.', 'The same test and key for both.', 'test'),
    ('student-choice', 'Student choice', 'Motivated students choose one version.', 'Random assignment.', 'hand'),
]


def icon(c, kind, cx, cy, hue):
    if kind == 'teacher':
        ic_person(c, cx, cy, 14, hue)
        c.line(cx + 10, cy - 8, cx + 24, cy - 18, hue, 3)
    elif kind == 'clock':
        ic_clock(c, cx, cy, 14, hue)
    elif kind == 'help':
        c.circle(cx, cy, 13, fill='none', stroke=hue, sw=6)
        c.circle(cx, cy, 13, fill='none', stroke=WHITE, sw=2, dash='6 9')
    elif kind == 'test':
        ic_doc(c, cx - 11, cy - 14, 22, 28, label=None, fold=6, stroke=hue)
        ic_lines(c, cx - 6, cy - 2, 12, 2, gap=6, stroke=hue, sw=2)
    else:
        c.line(cx, cy + 14, cx, cy - 4, hue, 5)
        c.circle(cx, cy - 10, 6, fill=hue)
        c.line(cx - 7, cy - 6, cx - 7, cy - 18, hue, 4)
        c.line(cx + 7, cy - 6, cx + 7, cy - 18, hue, 4)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Five Ways a Test Can Lie to You', 'Before you trust a difference between groups, ask what else was different besides the version.')
    n, gap = 5, 12
    x0, x1, y0, y1 = 30, 1170, 104, 640
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, name, misleads, defense, kind) in enumerate(ROWS):
        hue, tint = HUES[i]
        x = x0 + i * (w + gap)
        cx = x + w / 2
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 56, fill=hue, rx=14)
        c.rect(x, y0 + 30, w, 26, fill=hue)
        c.circle(x + 30, y0 + 28, 20, fill=WHITE)
        icon(c, kind, x + 30, y0 + 28, hue)
        c.para(x + 58, y0 + 26, name, w - 66, 18, 1.1, 'bold', WHITE, maxlines=2)
        # problem
        c.rect(x + 8, y0 + 66, w - 16, 232, fill=tint, rx=10)
        c.text(x + 18, y0 + 88, 'HOW IT MISLEADS', 12, 'bold', hue, spacing='1')
        (lx, ly), (rx_, ry) = ic_scale(c, cx, y0 + 150, 128, tilt=9)
        c.rect(rx_ - 18, ry - 30, 36, 28, fill=GRAY, stroke=INK, sw=2.5, rx=3)
        c.text(rx_, ry - 10, '?', 20, 'bold', WHITE, 'middle')
        c.rect(lx - 14, ly - 18, 28, 16, fill='#d6e6f7', stroke=INK, sw=2, rx=2)
        c.para(cx, y0 + 252, misleads, w - 30, 15.5, 1.2, 'bold', INK, 'middle', maxlines=3)
        # defense
        c.rect(x + 8, y0 + 308, w - 16, 218, fill='#e5f2e6', rx=10)
        c.text(x + 18, y0 + 330, 'THE DEFENSE', 12, 'bold', GREEND, spacing='1')
        (lx, ly), (rx_, ry) = ic_scale(c, cx, y0 + 384, 128, tilt=0)
        c.rect(rx_ - 14, ry - 18, 28, 16, fill='#fdf1d6', stroke=INK, sw=2, rx=2)
        c.rect(lx - 14, ly - 18, 28, 16, fill='#d6e6f7', stroke=INK, sw=2, rx=2)
        c.para(cx, y0 + 482, defense, w - 30, 15.5, 1.2, 'bold', GREEND, 'middle', maxlines=3)
        items.append(dict(id=zid, label=name, color=hue, box=(x, y0, x + w, y1),
                          summary='How it misleads: %s The defense: %s' % (misleads, defense),
                          facts=['How it misleads: %s' % misleads, 'The defense: %s' % defense,
                                 'Ask: what else is different besides the version?']))
    c.text(40, 672, 'Tilted scale: a hidden weight tips the comparison. Level scale: the defense makes the groups equal except for the version.', 15, 'normal', MUTED, maxw=1120)
    quiz = [
        dict(question='Which confounder do you defend against by using one teacher for both groups?', correct_zone='different-teachers', explanation='One teacher\'s enthusiasm lifts one group.'),
        dict(question='Which confounder do you defend against by running both groups at the same time?', correct_zone='different-times', explanation='Students are more alert at one time.'),
        dict(question='Which confounder is solved by the same script and help for both groups?', correct_zone='extra-help', explanation='One group gets a review or hints.'),
        dict(question='Which confounder is solved by the same test and key for both?', correct_zone='different-tests', explanation='The versions are measured in different ways.'),
        dict(question='Which confounder is solved by random assignment?', correct_zone='student-choice', explanation='Motivated students choose one version.'),
    ]
    return c, items, quiz
