"""Poster 25: The A/B Test on One Page (Chapter 16, callout, 7 markers). The artwork carries no text."""
from svgkit import *

CH = '16-ab-testing-design'

META = dict(
    slug='ab-test-on-one-page',
    title='The A/B Test on One Page',
    chapter=CH,
    overlay='callout',
    layout='top-bottom',
    topic='The whole design of a classroom A/B test on one page',
    desc='A left-to-right flow of the whole A/B test: a pool of students is randomly assigned to the original or the improved version, both groups take the same pre-test and post-test, and learning gain is compared.',
    intro=('The A/B test is the book\'s main method for checking whether an improvement helped, and its concepts are introduced in separate sections. This poster is the "design on one page" from Chapter 16. '
           'A pool of students is randomly assigned to two groups. The control group uses the original version (v1, rubric total 65, Revise) and the treatment group uses the improved version (v1.1, total 78, Adopt). '
           'Both take the same pre-test before and the same post-test after, and the comparison is the learning gain. The two groups are drawn as mirror images so the only visible difference is the version. '
           'A time strip along the bottom follows the schedule of Chapter 17: pre-test and assignment in week 1, use of the assigned version in weeks 2 and 3, and post-test and survey in week 4. '
           'The artwork has no text, so the numbers can follow the chapter if it changes.'),
    alt=('A flow from left to right. Consent and privacy: a form and a shield protect a pool of student silhouettes. Random assignment: the pool is shuffled into two groups by tokens. '
         'Two mirror-image lanes. Top lane, the control group, uses the original version, v1, rubric total 65, Revise. Bottom lane, the treatment group, uses the improved version, v1.1, total 78, Adopt. '
         'Both lanes take the same pre-test before and the same post-test after. At the right, two gain bars are compared. A hypothesis lightbulb sits at the top. '
         'A time strip of four weeks runs along the bottom: week 1 pre-test and assignment, weeks 2 and 3 use the assigned version, week 4 post-test and survey.'),
    bloom='Understand',
    objective='**describe** the parts of a classroom A/B test and **explain** why the two groups must differ only in the version.',
    objective_plain='describe the parts of a classroom A/B test and explain why the two groups must differ only in the version.',
    prereq=['Control group, treatment group, and random assignment from [Chapter 16](../../chapters/16-ab-testing-design/index.md).'],
    activities=[
        '**Explore (4 min).** Hover over markers 1 to 7. Which two parts must be identical for both groups?',
        '**Quiz (3 min).** Press **Quiz** and find each part from its description.',
        '**Draft (3 min).** Write one sentence for your hypothesis. Which of the seven parts will be hardest to arrange in your class?',
    ],
    assessment=[
        ('What does the control group receive?', 'Ordinary teaching with the original version, not no teaching.'),
        ('Why is assignment random?', 'So that motivated or stronger students do not end up in one group by choice.'),
        ('What is the comparison at the end?', 'The learning gain of each group, from the pre-test to the post-test.'),
    ],
    connection='Chapter 17 analyzes the results. A reviewer can use this poster to check a test plan, and a teacher can use it to draft one.',
    ref_nums=[(CH, [1, 2, 3, 6])],
    key_questions=['What is the one difference between the groups?', 'Did both groups take the same tests?'],
    misconceptions=['The control group gets no teaching', 'Volunteers make a fair treatment group'],
    good=['The rubric totals 65 and 78 and the version labels follow the chapter and are shown in the marker descriptions, not in the artwork.',
          'Students are drawn as plain silhouettes with no identifying features.'],
    verify=[(CH, 'v1.1'),
            (CH, 'the lesson is in weeks 2 and 3, and the post-test is in week 4'),
            ('17-ab-testing-analysis', 'above the 5-point threshold in the hypothesis'),
            (CH, 'The Design on One Page'),
            ('17-ab-testing-analysis', 'survey')],
)

GC, GT = '#1d4f86', '#00796b'    # control lane, treatment lane hues


def crowd(c, x, y, n, cols, hue, step=24, r=10):
    for k in range(n):
        r_, c_ = divmod(k, cols)
        ic_person(c, x + c_ * step, y + r_ * (step + 4), r, hue)


def sheet(c, x, y, hue):
    ic_doc(c, x - 20, y - 26, 40, 52, label=None, fold=9)
    for j in range(3):
        c.rect(x - 12, y - 8 + j * 11, 7, 7, fill=WHITE, stroke=hue, sw=1.5)
        c.line(x - 1, y - 4 + j * 11, x + 12, y - 4 + j * 11, GRAYM, 2.5)


def draw():
    c = Canvas(1200, 560)
    # lanes
    c.rect(470, 90, 530, 150, fill='#e6eef8', stroke=GC, sw=3, rx=14)
    c.rect(470, 270, 530, 150, fill='#e3f4f1', stroke=GT, sw=3, rx=14)
    # consent and pool
    c.rect(36, 120, 250, 250, fill='#f3f4f6', stroke=GRAY, sw=3, rx=14)
    crowd(c, 70, 186, 12, 4, GRAY, 28, 12)
    ic_shield(c, 62, 92, 20, TEAL)
    ic_doc(c, 96, 68, 40, 50, label=None, fold=9)
    ic_lines(c, 104, 94, 24, 3, gap=8)
    ic_check(c, 134, 112, 10, GREEN)
    # shuffle tokens and arrows into lanes
    for k, col in enumerate((GC, GT, GC, GT)):
        c.circle(326 + (k % 2) * 34, 220 + (k // 2) * 34, 13, fill=col, stroke=WHITE, sw=2)
    c.path('M300,200 q16,-24 40,-10', stroke=INK, sw=3)
    c.path('M300,290 q16,24 40,10', stroke=INK, sw=3)
    c.arrow(364, 214, 462, 160, INK, 4, 12)
    c.arrow(364, 262, 462, 340, INK, 4, 12)
    # lanes content: pre-test, version, post-test; group of students at left of each lane
    for (ly, hue, label_v) in ((165, GC, 'v1'), (345, GT, 'v1.1')):
        crowd(c, 500, ly - 20, 6, 3, hue, 24, 10)
        sheet(c, 610, ly, hue)
        c.arrow(636, ly, 676, ly, hue, 4, 11)
        # version document
        ic_doc(c, 690, ly - 34, 56, 68, label=None, fold=12, fill=WHITE)
        ic_lines(c, 698, ly - 8, 36, 3, gap=9)
        if hue == GT:
            c.poly([(724, ly - 40), (738, ly - 56), (752, ly - 40)], fill=ORANGE, stroke=INK, sw=2)
            c.rect(698, ly - 24, 40, 8, fill=hue, rx=2)
        else:
            c.rect(698, ly - 24, 40, 8, fill=GRAYM, rx=2)
        c.arrow(756, ly, 796, ly, hue, 4, 11)
        sheet(c, 830, ly, hue)
        # gain arrow
        c.arrow(868, ly + 16, 940, ly - 16, hue, 5, 13)
    # comparison at right: two gain bars
    c.rect(1022, 120, 150, 280, fill='#fff7e6', stroke=ORANGE, sw=3, rx=14)
    c.line(1042, 380, 1152, 380, INK, 3)
    c.rect(1056, 380 - 110, 34, 110, fill=GC, rx=3)
    c.rect(1106, 380 - 160, 34, 160, fill=GT, rx=3)
    c.path('M1073,262 L1073,236 L1123,216 L1123,190', stroke=INK, sw=2.5, dash='4 4')
    c.circle(1098, 214, 14, fill=WHITE, stroke=INK, sw=2.5)
    c.line(1090, 211, 1106, 211, INK, 3)
    c.line(1090, 218, 1106, 218, INK, 3)
    # hypothesis lightbulb at top
    c.circle(700, 46, 22, fill='#fff3b0', stroke=INK, sw=3)
    c.rect(692, 66, 16, 10, fill=GRAYM, stroke=INK, sw=2, rx=2)
    for a in (-60, -20, 20, 60):
        import math
        c.line(700 + 28 * math.sin(math.radians(a)), 46 - 28 * math.cos(math.radians(a)), 700 + 38 * math.sin(math.radians(a)), 46 - 38 * math.cos(math.radians(a)), ORANGE, 3)
    c.line(700, 38, 700, 54, INK, 3)
    c.line(692, 46, 708, 46, INK, 3)
    # time strip
    sx, sy, sw, sh = 36, 466, 1128, 68
    for k, (x, w, kind) in enumerate(((sx, 276, 0), (sx + 288, 276, 1), (sx + 576, 276, 1), (sx + 864, 264, 2))):
        c.rect(x, sy, w, sh, fill=['#e3f4f1', '#f3f4f6', '#f3f4f6', '#fdf1d6'][k], stroke=GRAY, sw=2.5, rx=10)
        ic_calendar(c, x + 28, sy + 30, 14, INK, WHITE, [GT, GRAY, GRAY, ORANGE][k])
        if kind == 0:
            sheet(c, x + 120, sy + 34, GT)
            crowd(c, x + 168, sy + 40, 3, 3, GRAY, 24, 9)
        elif kind == 1:
            ic_doc(c, x + 100, sy + 8, 38, 52, label=None, fold=8)
            ic_doc(c, x + 148, sy + 8, 38, 52, label=None, fold=8, fill='#e6f4f1')
        else:
            sheet(c, x + 110, sy + 34, GT)
            c.rect(x + 160, sy + 10, 44, 48, fill=WHITE, stroke=INK, sw=2.5, rx=4)
            for j in range(3):
                c.line(x + 166, sy + 20 + j * 12, x + 198, sy + 20 + j * 12, GRAYM, 3)
    items = [
        dict(id=1, label='The hypothesis', panel='top', at=(670, 30), color=ORANGE,
             hint='A glowing lightbulb above the two lanes.',
             description='The hypothesis states what you expect, such as that the improved version gives a larger learning gain than the original. In the pilot it set a threshold of 5 points.',
             tip='Write the hypothesis before the test, so the result cannot choose it.'),
        dict(id=2, label='Random assignment', panel='top', at=(300, 188), color=INK,
             hint='Four colored tokens being shuffled between a crowd of students and the two lanes.',
             description='Students are assigned to the two groups at random, like shuffled tokens. Random assignment spreads motivation and ability evenly, so students do not choose their group.',
             tip='Never let volunteers pick a version. Student choice is a confounder.'),
        dict(id=3, label='The control group', panel='top', at=(488, 112), color=GC,
             hint='The upper lane, where a group of students uses a plain document, version v1.',
             description='The control group uses the original version, v1, with a rubric total of 65 (Revise). It receives ordinary teaching with the original, not no teaching.',
             tip='The two lanes are mirror images. The only visible difference is the version.'),
        dict(id=4, label='The treatment group', panel='bottom', at=(488, 292), color=GT,
             hint='The lower lane, where a group of students uses a document with a small upward chevron, version v1.1.',
             description='The treatment group uses the improved version, v1.1, with a rubric total of 78 (Adopt). Everything else is the same as for the control group.',
             tip='Change one thing at a time, or say that you tested a bundle.'),
        dict(id=5, label='The pre-test', panel='bottom', at=(588, 360), color=Q,
             hint='A sheet with check boxes, at the start of each lane, before the version document.',
             description='Both groups take the same pre-test before the lesson, in week 1. It shows where each student starts, so the gain can be measured.',
             tip='Use the same test and key for both groups.'),
        dict(id=6, label='The post-test and the learning gain', panel='bottom', at=(808, 360), color=R,
             hint='A second sheet at the end of each lane, with arrows leading up to two bars of different heights.',
             description='Both groups take the same post-test in week 4. The comparison is the learning gain of each group, the post-test score minus the pre-test score.',
             tip='A difference from a small test may partly be luck. Chapter 17 puts it in context with an effect size.'),
        dict(id=7, label='Consent and privacy', panel='top', at=(40, 96), color=TEAL,
             hint='A form with a check mark and a shield above the crowd of students.',
             description='Students and families are informed, and student data is protected. The pool is drawn as plain silhouettes with no identifying features.',
             tip='Keep names and records out of every prompt and report.'),
    ]
    return c, items, []
