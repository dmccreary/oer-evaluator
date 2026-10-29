"""Poster 29: A One-Day Workshop Timeline (Chapter 19, callout, 8 markers). The artwork carries no text; block widths are proportional to time."""
from svgkit import *

CH = '19-training-certifying-reviewers'

META = dict(
    slug='one-day-workshop-timeline',
    title='A One-Day Workshop Timeline',
    chapter=CH,
    overlay='callout',
    layout='top-bottom',
    topic='The order of a one-day OER reviewer workshop and what teachers leave with',
    desc='A horizontal timeline from 8:30 to 3:30 built from the chapter\'s sample agenda, with block widths in proportion to time and a token for what teachers leave with.',
    intro=('A facilitator can print this poster for the room, and participants can see the logic of the day and what they carry out of it. It is built from the sample agenda in Chapter 19: check-in and setup, the ten metrics, '
           'calibration by hand and then with the agent, checking the agent, lunch, the improvement challenge, peer review and publishing, and next steps. '
           'Block widths are in proportion to time, so the long improvement challenge looks long and the breaks look short. A token under each block shows what teachers leave with. '
           'Two arcs show why the order matters: the rubric comes before calibration, and checking comes before improving. The times live in the overlay data and not in the artwork, so a facilitator can adapt the agenda without redrawing.'),
    alt=('A timeline from 8:30 to 3:30 with block widths in proportion to time. 1 Check-in and setup, 8:30 to 9:00, leaves teachers with a working agent session. '
         '2 The ten metrics, 9:00 to 9:45, a rubric card. 3 Calibration, 9:45 to 10:45, hand and agent scores with gaps explained; a 15-minute break follows. '
         '4 Checking the agent, 11:00 to 12:00, a verified evaluation of the sample. 5 Lunch, 12:00 to 12:45. 6 The improvement challenge, 12:45 to 2:15, an improved component and its new score; a 15-minute break follows. '
         '7 Peer review and publishing, 2:30 to 3:15, a published, openly licensed component. 8 Next steps, 3:15 to 3:30, a certificate checklist. '
         'An arc from block 2 to block 3 shows the rubric before calibration, and an arc from block 4 to block 6 shows checking before improving.'),
    bloom='Understand',
    objective='**order** the blocks of the one-day workshop and **explain** why the rubric comes before calibration and checking comes before improving.',
    objective_plain='order the blocks of the one-day workshop and explain why the rubric comes before calibration and checking comes before improving.',
    prereq=['The sample agenda from [Chapter 19](../../chapters/19-training-certifying-reviewers/index.md) and the [Sample One-Day Schedule](../../workshops/sample-one-day-schedule.md).'],
    activities=[
        '**Explore (4 min).** Hover over markers 1 to 8. Which block takes the longest, and what do teachers leave with from it?',
        '**Quiz (3 min).** Press **Quiz** and find each block from its description.',
        '**Adapt (3 min).** If your day were two hours shorter, which block would you shorten, and which two blocks must stay in order?',
    ],
    assessment=[
        ('Which block comes right after calibration and the break?', 'Checking the agent.'),
        ('What do teachers leave with from the improvement challenge?', 'An improved component and its new score.'),
        ('Why does the rubric come before calibration?', 'You score by hand against the rubric first, so there is a human score to compare the agent with.'),
    ],
    connection='This poster pairs with the Sample One-Day Schedule workshop page and gives a facilitator the logic of the day at a glance.',
    ref_nums=[(CH, [5, 7, 10])],
    key_questions=['What do teachers leave with from this block?', 'What must come before it?'],
    misconceptions=['A workshop is a lecture followed by a survey', 'The order of the blocks does not matter'],
    good=['The times are in the overlay data. Edit the descriptions in data.json to adapt the agenda for your own day.'],
    verify=[(CH, '| 8:30 to 9:00 | Check-in and setup | A working agent session |'),
            (CH, '| 9:45 to 10:45 | Calibration: score a sample by hand, then with the agent | Hand and agent scores, with gaps explained |'),
            (CH, '| 12:45 to 2:15 | Improvement challenge: raise one component\'s score with agents | An improved component and its new score |'),
            (CH, '| 3:15 to 3:30 | Next steps: certificate requirements and the exit survey | A certificate checklist |')],
)

AGENDA = [  # (kind, minutes)
    ('check-in', 30), ('metrics', 45), ('calibration', 60), ('break', 15), ('checking', 60), ('lunch', 45),
    ('improve', 90), ('break', 15), ('peer', 45), ('next', 15),
]
X0, SC = 40, 1120 / 420.0
BY, BH = 250, 100
HUE = {'check-in': '#00796b', 'metrics': '#1d4f86', 'calibration': '#1d4f86', 'checking': '#00796b', 'improve': '#8a5a00',
       'peer': '#573379', 'next': '#573379'}


def block_icon(c, kind, cx, cy, hue):
    if kind == 'check-in':
        c.rect(cx - 22, cy - 18, 44, 28, fill=WHITE, stroke=WHITE, sw=1, rx=3)
        c.rect(cx - 30, cy + 12, 60, 6, fill=WHITE, rx=2)
        c.path('M%s,%s l7,5 l-7,5' % (cx - 12, cy - 12), stroke=hue, sw=3)
    elif kind == 'metrics':
        for j in range(10):
            r_, c_ = divmod(j, 5)
            col = Q if j < 5 else R
            c.rect(cx - 40 + c_ * 17, cy - 14 + r_ * 18, 12, 12, fill=WHITE if j < 5 else WHITE, stroke=WHITE, sw=1, rx=2)
    elif kind == 'calibration':
        c.rect(cx - 42, cy - 4, 26, 24, fill=WHITE, rx=2)
        c.rect(cx - 8, cy - 14, 26, 34, fill=WHITE, rx=2)
        c.rect(cx + 26, cy - 4, 20, 24, fill=WHITE, rx=2, opacity=0.7)
        c.line(cx - 46, cy - 12, cx + 50, cy - 12, WHITE, 3, '4 4')
    elif kind == 'checking':
        ic_doc(c, cx - 30, cy - 26, 36, 48, label=None, fold=9)
        ic_magnifier(c, cx + 12, cy + 4, 22, WHITE)
    elif kind == 'lunch':
        c.circle(cx, cy, 24, fill='none', stroke=INK, sw=4)
        c.circle(cx, cy, 12, fill='none', stroke=INK, sw=3)
        c.line(cx - 40, cy - 16, cx - 40, cy + 18, INK, 4)
        c.line(cx + 40, cy - 16, cx + 40, cy + 18, INK, 4)
    elif kind == 'improve':
        ic_wrench(c, cx - 30, cy + 4, 28, WHITE)
        for j in range(3):
            c.rect(cx + 8 + j * 22, cy + 18 - (j + 1) * 14, 16, (j + 1) * 14, fill=WHITE)
        c.arrow(cx + 6, cy - 24, cx + 60, cy - 34, WHITE, 4, 11)
    elif kind == 'peer':
        ic_person(c, cx - 26, cy + 6, 16, WHITE)
        ic_person(c, cx + 10, cy + 6, 16, WHITE)
        c.arrow(cx + 40, cy - 10, cx + 40, cy - 30, WHITE, 3, 8)
    elif kind == 'next':
        c.rect(cx - 10, cy - 16, 20, 30, fill=WHITE, rx=2)
        c.circle(cx, cy - 4, 4, fill=hue)


def token(c, kind, cx, cy):
    c.rect(cx - 50, cy - 34, 100, 68, fill=WHITE, stroke=INK, sw=2.5, rx=14)
    c.circle(cx - 50, cy, 6, fill=GRAYM, stroke=INK, sw=1.5)
    if kind == 'check-in':      # working agent session
        c.rect(cx - 22, cy - 18, 44, 30, fill=WHITE, stroke=INK, sw=2.5, rx=3)
        c.rect(cx - 22, cy - 18, 44, 8, fill=Q, rx=3)
        c.path('M%s,%s l6,4 l-6,4' % (cx - 14, cy - 4), stroke=INK, sw=2.5)
    elif kind == 'metrics':     # rubric card
        for j in range(10):
            r_, c_ = divmod(j, 5)
            if j < 5:
                c.circle(cx - 28 + c_ * 14, cy - 8 + r_ * 18, 5, fill=Q)
            else:
                c.rect(cx - 33 + c_ * 14, cy - 3 + (r_ - 1) * 18, 10, 10, fill=R)
    elif kind == 'calibration':  # hand and agent scores with a gap
        c.rect(cx - 34, cy - 6, 20, 24, fill=Q, rx=2)
        c.rect(cx - 8, cy - 14, 20, 32, fill=GRAY, rx=2)
        c.rect(cx + 18, cy - 2, 20, 20, fill=ORANGE, rx=2)
        c.line(cx - 34, cy - 14, cx + 38, cy - 14, INK, 2, '3 3')
    elif kind == 'checking':     # verified evaluation
        ic_doc(c, cx - 14, cy - 26, 28, 38, label=None, fold=8)
        ic_check(c, cx + 14, cy + 12, 12, GREEN)
    elif kind == 'improve':      # improved component and new score
        c.rect(cx - 34, cy - 16, 34, 32, fill='#fdf1d6', stroke=INK, sw=2.5, rx=4)
        c.arrow(cx - 6, cy + 8, cx + 14, cy - 12, GREEN, 4, 10)
        c.rect(cx + 18, cy - 20, 26, 40, fill=WHITE, stroke=INK, sw=2.5, rx=3)
        c.rect(cx + 24, cy - 12, 14, 8, fill=GREEN)
    elif kind == 'peer':         # published openly licensed
        ic_doc(c, cx - 30, cy - 26, 32, 42, label=None, fold=8)
        ic_lock(c, cx + 18, cy + 2, 14, True, GREEN)
    elif kind == 'next':         # certificate checklist
        c.rect(cx - 22, cy - 26, 44, 52, fill=WHITE, stroke=INK, sw=2.5, rx=4)
        for j in range(3):
            ic_check(c, cx - 11, cy - 14 + j * 14, 5, GREEN)
            c.line(cx, cy - 14 + j * 14, cx + 14, cy - 14 + j * 14, GRAYM, 3)


def draw():
    c = Canvas(1200, 520)
    x = X0
    blocks = []
    for kind, mins in AGENDA:
        w = mins * SC
        blocks.append((kind, x, w))
        x += w
    # time axis
    c.line(X0, BY + BH + 14, X0 + 420 * SC, BY + BH + 14, GRAY, 3)
    for kind, bx, w in blocks:
        if kind in ('break', 'lunch'):
            c.rect(bx + 2, BY + 10, w - 4, BH - 20, fill=GRAYL, stroke=GRAY, sw=2.5, rx=8, dash='5 4')
            if kind == 'lunch':
                block_icon(c, 'lunch', bx + w / 2, BY + BH / 2, GRAY)
            else:
                c.rect(bx + w / 2 - 9, BY + BH / 2 - 10, 18, 20, fill='none', stroke=GRAY, sw=3, rx=3)
                c.path('M%s,%s q8,0 8,8 q0,6 -8,6' % (bx + w / 2 + 9, BY + BH / 2 - 4), stroke=GRAY, sw=3)
            continue
        hue = HUE[kind]
        c.rect(bx + 2, BY, w - 4, BH, fill=hue, stroke=INK, sw=2.5, rx=10)
        block_icon(c, kind, bx + w / 2, BY + BH / 2 + 4, hue)
    # tokens under the blocks
    tok_x = {'check-in': 94, 'metrics': 204, 'calibration': 324, 'checking': 520, 'improve': 840, 'peer': 1020, 'next': 1132}
    for kind, bx, w in blocks:
        if kind in tok_x:
            cx = tok_x[kind]
            c.line(bx + w / 2, BY + BH + 14, cx, BY + BH + 66, GRAY, 2.5, '3 4')
            token(c, kind, cx, BY + BH + 100)
    # order arcs above: rubric -> calibration ; checking -> improving
    def mid(i):
        return blocks[i][1] + blocks[i][2] / 2
    c.curve_arrow(mid(1) + 10, BY - 4, (mid(1) + mid(2)) / 2, BY - 90, mid(2) - 10, BY - 4, ORANGE, 6, 16)
    c.curve_arrow(mid(4) + 10, BY - 4, (mid(4) + mid(6)) / 2, BY - 110, mid(6) - 10, BY - 4, ORANGE, 6, 16)
    # markers
    names = {'check-in': ('Check-in and setup', '8:30 to 9:00', 'A working agent session.', 'A laptop with a prompt, in the shortest session block at the start.'),
             'metrics': ('The ten metrics', '9:00 to 9:45', 'A rubric card.', 'A sheet of ten small boxes in two rows, the first arc starts here.'),
             'calibration': ('Calibration by hand, then with the agent', '9:45 to 10:45', 'Hand and agent scores, with gaps explained.', 'Bars of unequal heights under a dashed line, where the first arc lands.'),
             'checking': ('Checking the agent', '11:00 to 12:00', 'A verified evaluation of the sample.', 'A page under a magnifying glass, where the second arc starts.'),
             'lunch': ('Lunch', '12:00 to 12:45', 'No deliverable.', 'A plate with a knife and fork in a dashed block.'),
             'improve': ('The improvement challenge', '12:45 to 2:15', 'An improved component and its new score.', 'The longest block, with a wrench and a staircase of bars, where the second arc lands.'),
             'peer': ('Peer review and publishing', '2:30 to 3:15', 'A published, openly licensed component.', 'Two people and an upward arrow.'),
             'next': ('Next steps', '3:15 to 3:30', 'A certificate checklist.', 'The smallest block at the right end, with a small certificate.')}
    tips = {'metrics': 'Arc 1: the rubric comes before calibration, so teachers have a human score to compare the agent with.',
            'calibration': 'Teachers score a sample by hand first, then with the agent, and explain the gaps.',
            'checking': 'Arc 2: checking comes before improving, so teachers fix a resource only after they trust the evidence.',
            'improve': 'The longest block, because teachers do the real work here.',
            'lunch': 'Breaks and lunch are drawn short on purpose so the blocks stay in proportion to time.',
            'check-in': 'Everyone leaves this block with a working session, so nothing later is blocked by setup.',
            'peer': 'Peer review comes after the improvement challenge, so reviewers have something to review.',
            'next': 'The exit survey measures only the first level of training evaluation.'}
    items = []
    n = 0
    for kind, bx, w in blocks:
        if kind == 'break':
            continue
        n += 1
        title, when, leave, hint = names[kind]
        items.append(dict(id=n, label=title, panel='top', at=(bx + 14, BY + 14) if w > 60 else (bx + w / 2, BY + 14), color=HUE.get(kind, GRAY), radius=2.3,
                          hint=hint, description='%s. Teachers leave with: %s' % (when, leave[0].lower() + leave[1:] if leave != 'No deliverable.' else 'no deliverable, just a rest.'),
                          tip=tips.get(kind)))
    return c, items, []
