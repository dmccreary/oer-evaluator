"""Poster 22: Agreement Is Not Skill (Chapter 14, grid, 3 zones). Numbers computed from the count table."""
from svgkit import *

CH = '14-checking-agent-output'

# Chapter 14 worked example: agent and human on 20 resources, "ready to adopt?"
BOTH_READY, AGENT_ONLY, HUMAN_ONLY, BOTH_NOT = 1, 1, 1, 17
N = BOTH_READY + AGENT_ONLY + HUMAN_ONLY + BOTH_NOT
PO = (BOTH_READY + BOTH_NOT) / N
PA, PH = (BOTH_READY + AGENT_ONLY) / N, (BOTH_READY + HUMAN_ONLY) / N
PE = PA * PH + (1 - PA) * (1 - PH)
KAPPA = (PO - PE) / (1 - PE)
assert (N, round(PO, 2), round(PE, 2), round(KAPPA, 2)) == (20, 0.90, 0.82, 0.44)

META = dict(
    slug='agreement-is-not-skill',
    title='Agreement Is Not Skill',
    chapter=CH,
    overlay='grid',
    topic='Why a high agreement rate can hide a low kappa',
    desc='Three panels walk through the Chapter 14 example: 18 of 20 agree, most of that agreement is expected by chance, and kappa is only 0.44.',
    intro=('This is the most counterintuitive statistic in the book, and teachers often report only the agreement rate. The poster follows the worked example from Chapter 14: an agent and a human judge 20 resources as ready to adopt or not. '
           'Panel 1 is the count table, with the diagonal of agreements highlighted. Panel 2 shows the chance baseline as a filled bar: most of the 90 percent agreement is expected by luck. '
           'Panel 3 shows kappa as (0.90 − 0.82) / (1 − 0.82), which is 0.44. The agent found only one of the two resources the human judged ready. '
           'The poster gives no numeric cutoffs for kappa, because the chapter says to check cutoffs against the source before quoting them.'),
    alt=('Three panels. Panel 1, the count table for 20 resources: agent ready and human ready, 1; agent ready and human not ready, 1; agent not ready and human ready, 1; agent not ready and human not ready, 17. '
         'The two agreements, 1 and 17, are highlighted, so they agree on 18 of 20, which is 0.90. '
         'Panel 2, chance agreement: a bar from 0 to 1 shows 0.01 from both saying ready plus 0.81 from both saying not ready, which is 0.82, so most of the 0.90 is expected by luck; only 0.08 is beyond chance. '
         'Panel 3: kappa equals (0.90 minus 0.82) divided by (1 minus 0.82), which is 0.08 divided by 0.18, about 0.44. The agent found only one of the two resources the human judged ready.'),
    bloom='Analyze',
    objective='**compute** Cohen\'s kappa from a count table and **explain** why 90 percent agreement can be a kappa of only 0.44.',
    objective_plain='compute Cohen\'s kappa from a count table and explain why 90 percent agreement can be a kappa of only 0.44.',
    prereq=['Inter-rater agreement and Cohen\'s kappa from [Chapter 14](../../chapters/14-checking-agent-output/index.md).'],
    activities=[
        '**Explore (3 min).** Press each panel in order, 1 to 3. Where does the chance baseline come from?',
        '**Quiz (3 min).** Press **Quiz Me** and match four statements to the panels.',
        '**Compute (4 min).** Change one cell of the table in your head (for example, 2 both ready and 16 both not ready). Does kappa rise or fall?',
    ],
    assessment=[
        ('Why is a 90 percent agreement not impressive in this example?', 'Almost everything is "not ready", so two raters would agree 82 percent of the time by chance.'),
        ('What is the formula for kappa?', '(po − pe) / (1 − pe).'),
        ('What should you always show beside kappa?', 'The count table.'),
    ],
    connection='Calibration compares the agent with trained humans. Reporting kappa with the count table keeps the comparison honest.',
    ref_nums=[(CH, [2, 8, 5])],
    key_questions=['How much agreement would chance alone give?', 'Which resources did the agent miss?'],
    misconceptions=['High agreement means high skill', 'Kappa and percent agreement are the same number'],
    good=['The numbers are from the Chapter 14 worked example. The poster prints no numeric kappa cutoffs.'],
    verify=[(CH, 'the agent says "ready" 2 of 20 times and the human says "ready" 2 of 20 times'),
            (CH, 'so the chance of both saying ready is 0.10 times 0.10 = 0.01'),
            (CH, 'The two add to 0.82.'),
            (CH, 'kappa = (po - pe) / (1 - pe)'),
            (CH, 'And the agent found only one of the two resources that the human judged ready.')],
)

BLUE, GREY = '#1d4f86', '#6b7785'


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Agreement Is Not Skill', '20 resources, one question: is each one ready to adopt? An agent and a human answer.')
    y0, y1 = 106, 640
    xs = [(30, 380), (424, 380), (818, 352)]
    items = []
    # panel 1: count table
    x, w = xs[0]
    c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=BLUE, sw=3, rx=14)
    c.rect(x, y0, w, 46, fill=BLUE, rx=14)
    c.rect(x, y0 + 24, w, 22, fill=BLUE)
    c.text(x + 16, y0 + 31, '1  Count the agreements', 21, 'bold', WHITE)
    tx, ty, cw, rh = x + 110, y0 + 124, 124, 78
    c.text(tx + cw, ty - 52, 'Human', 17, 'bold', INK, 'middle')
    c.text(tx + cw / 2, ty - 20, 'ready', 16, 'bold', INK, 'middle')
    c.text(tx + cw * 1.5, ty - 20, 'not ready', 16, 'bold', INK, 'middle')
    c.text(x + 56, ty + rh, 'Agent', 17, 'bold', INK, 'middle')
    c.text(x + 100, ty + rh / 2 + 6, 'ready', 16, 'bold', INK, 'end')
    c.text(x + 100, ty + rh * 1.5 + 6, 'not ready', 16, 'bold', INK, 'end')
    cells = [(0, 0, BOTH_READY, True), (0, 1, AGENT_ONLY, False), (1, 0, HUMAN_ONLY, False), (1, 1, BOTH_NOT, True)]
    for (r, k, v, diag) in cells:
        cx, cy = tx + k * cw, ty + r * rh
        c.rect(cx, cy, cw, rh, fill='#c8e6c9' if diag else '#f3f4f6', stroke=GREEN if diag else GRAYM, sw=4 if diag else 2, rx=6)
        c.text(cx + cw / 2, cy + rh / 2 + 15, str(v), 42, 'bold', GREEND if diag else INK, 'middle')
    c.text(x + w / 2, ty + rh * 2 + 44, 'Agree on 1 + 17 = 18 of 20', 20, 'bold', GREEND, 'middle')
    c.text(x + w / 2, ty + rh * 2 + 82, 'observed agreement  po = 0.90', 22, 'bold', INK, 'middle')
    c.para(x + w / 2, ty + rh * 2 + 120, 'The green diagonal holds the agreements. Always show this table beside kappa.', w - 40, 16, 1.25, 'normal', MUTED, 'middle')
    items.append(dict(id='count-table', label='1: Count the agreements', color=BLUE, box=(x, y0, x + w, y1),
                      summary='The agent and the human agree on 18 of 20 resources, an agreement rate of 0.90.',
                      facts=['Both say ready: 1. Both say not ready: 17. They disagree on 2, one each way.', 'Agreement rate po = (1 + 17) / 20 = 0.90.',
                             'The agent says ready 2 of 20 times and the human says ready 2 of 20 times.']))
    # panel 2: chance bar
    x, w = xs[1]
    c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke='#8a5a00', sw=3, rx=14)
    c.rect(x, y0, w, 46, fill='#8a5a00', rx=14)
    c.rect(x, y0 + 24, w, 22, fill='#8a5a00')
    c.text(x + 16, y0 + 31, '2  Subtract what luck gives', 21, 'bold', WHITE, maxw=w - 30)
    stripe_defs(c, 'chance', '#c9a45f', '#fdf1d6')
    bx, bw, by, bh = x + 30, w - 60, y0 + 150, 64
    c.rect(bx, by, bw, bh, fill='#f3f4f6', stroke=INK, sw=2.5)
    c.rect(bx, by, bw * 0.82, bh, fill='url(#chance)', stroke=INK, sw=2.5)
    c.rect(bx + bw * 0.01, by, bw * 0.81, bh, fill='none')
    c.rect(bx + bw * PE, by, bw * (PO - PE), bh, fill=GREEN, stroke=INK, sw=2.5)
    c.rect(bx + bw * PO, by, bw * (1 - PO), bh, fill='#e57373', stroke=INK, sw=2.5)
    c.line(bx + bw * PE, by - 22, bx + bw * PE, by + bh + 10, INK, 2.5)
    c.line(bx + bw * PO, by - 48, bx + bw * PO, by + bh + 10, INK, 2.5)
    c.text(bx + bw * PE - 6, by - 10, 'pe = 0.82', 17, 'bold', '#5c3c00', 'end')
    c.text(bx + bw, by - 54, 'po = 0.90', 17, 'bold', GREEND, 'end')
    c.text(bx, by + bh + 28, '0', 15, 'normal', MUTED, 'middle')
    c.text(bx + bw, by + bh + 28, '1', 15, 'normal', MUTED, 'middle')
    ly = by + bh + 44
    for (col, fillp, txt) in (('url(#chance)', True, 'expected by chance: 0.01 + 0.81 = 0.82'), (GREEN, False, 'beyond chance: 0.90 − 0.82 = 0.08'), ('#e57373', False, 'disagreements: 0.10')):
        ly += 30
        c.rect(bx, ly - 16, 22, 22, fill=col, stroke=INK, sw=2)
        c.text(bx + 32, ly + 1, txt, 16.5, 'normal', INK, maxw=w - 100)
    c.para(x + w / 2, ly + 62, 'Both say ready: 0.10 × 0.10 = 0.01. Both say not ready: 0.90 × 0.90 = 0.81. Most of the 90 percent is not skill.', w - 40, 16, 1.25, 'bold', INK, 'middle')
    items.append(dict(id='chance-baseline', label='2: Subtract what luck gives', color='#8a5a00', box=(x, y0, x + w, y1),
                      summary='Chance agreement is 0.82, so most of the 0.90 agreement is expected by luck.',
                      facts=['Chance of both saying ready: 0.10 × 0.10 = 0.01.', 'Chance of both saying not ready: 0.90 × 0.90 = 0.81.',
                             'The two add to pe = 0.82.', 'Two raters who answered "not ready" at random 90 percent of the time would agree 82 percent of the time.']))
    # panel 3: kappa
    x, w = xs[2]
    c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke='#573379', sw=3, rx=14)
    c.rect(x, y0, w, 46, fill='#573379', rx=14)
    c.rect(x, y0 + 24, w, 22, fill='#573379')
    c.text(x + 16, y0 + 31, '3  Kappa', 21, 'bold', WHITE)
    c.text(x + w / 2, y0 + 92, 'κ = (po − pe) / (1 − pe)', 30, 'bold', INK, 'middle', maxw=w - 30)
    c.text(x + w / 2, y0 + 142, '= (0.90 − 0.82) / (1 − 0.82)', 24, 'normal', INK, 'middle', maxw=w - 30)
    c.text(x + w / 2, y0 + 184, '= 0.08 / 0.18', 24, 'normal', INK, 'middle')
    c.rect(x + 50, y0 + 210, w - 100, 92, fill='#efe6f6', stroke='#573379', sw=3, rx=14)
    c.text(x + w / 2, y0 + 275, '0.44', 62, 'bold', '#573379', 'middle')
    c.text(x + w / 2, y0 + 338, '90 percent agreement sounds excellent.', 17, 'bold', INK, 'middle', maxw=w - 30)
    c.text(x + w / 2, y0 + 362, 'Kappa tells a more honest story.', 17, 'bold', INK, 'middle', maxw=w - 30)
    ic_warn(c, x + 46, y0 + 424, 20, ORANGE)
    c.para(x + 78, y0 + 420, 'The agent found only one of the two resources the human judged ready.', w - 104, 17, 1.25, 'bold', INK)
    items.append(dict(id='kappa', label='3: Kappa', color='#573379', box=(x, y0, x + w, y1),
                      summary='Kappa = (0.90 − 0.82) / (1 − 0.82) = 0.08 / 0.18, about 0.44.',
                      facts=['Kappa corrects agreement for chance.', 'It is the observed agreement beyond chance, divided by the most agreement chance leaves room for.',
                             'The agent found only one of the two resources that the human judged ready.', 'Always show the count table beside kappa.']))
    c.text(40, 672, 'Worked example from Chapter 14, rounded to two decimal places. Kappa cutoffs are rules of thumb: check them against the source before quoting them.',
           14, 'normal', MUTED, maxw=1120, minsize=12)
    quiz = [
        dict(question='Which panel shows that the agent and human agree on 18 of 20 resources?', correct_zone='count-table', explanation='1 + 17 = 18 of 20 is 0.90.'),
        dict(question='Which panel shows that most of the 0.90 agreement is expected by chance?', correct_zone='chance-baseline', explanation='Chance agreement is 0.82.'),
        dict(question='Which panel gives the number 0.44?', correct_zone='kappa', explanation='(0.90 − 0.82) / (1 − 0.82) is about 0.44.'),
        dict(question='Which panel adds 0.10 × 0.10 and 0.90 × 0.90 to get 0.82?', correct_zone='chance-baseline', explanation='Both say ready, plus both say not ready.'),
    ]
    return c, items, quiz
