"""Poster 18: Weak Prompt, Strong Prompt (Chapter 12, grid, 2 zones)."""
from svgkit import *

CH = '12-ai-agents-prompts-scoring'

META = dict(
    slug='weak-and-strong-prompt',
    title='Weak Prompt, Strong Prompt',
    chapter=CH,
    overlay='grid',
    topic='The five parts of a rubric prompt: role, task, input, rules, and output format',
    desc='Two prompt cards side by side, each divided into the five parts of a prompt; the weak card fills one band and leaves four empty, and the strong card fills all five.',
    intro=('Writing a rubric prompt is the first hands-on AI skill, and its five parts form a checklist. This poster sets two paper cards side by side, each divided into the same five bands: role, task, input, rules, and output format. '
           'The weak card says only "Check accessibility." and the other four bands are empty and hatched. The strong card fills all five. '
           'The wording comes from the Chapter 12 worked example. A good prompt does not guarantee a good answer, so Chapters 13 and 14 exist to check what comes back. '
           'The prompts are drawn as paper cards and not as a chat window, so the poster shows no brand interface.'),
    alt=('Two prompt cards, each with five bands: role, task, input, rules, and output format. The weak prompt has only the task, "Check accessibility.", and the other four bands are empty and hatched. '
         'The strong prompt has all five. Role: You are a careful reviewer of open educational resources. Task: Apply the ten accessibility checks listed below to the resource. '
         'Input: the full text of the resource, pasted below the checks. Rules: Quote evidence for every result. If a check cannot be verified from the text, write "not checkable". '
         'Output format: a table with the columns check, result, and evidence. An arrow from the evidence column points to Chapter 14, where the evidence gets verified. '
         'A footer says a good prompt does not guarantee a good answer.'),
    bloom='Evaluate',
    objective='**evaluate** a prompt against the five parts of a rubric prompt and **name** the part that is missing.',
    objective_plain='evaluate a prompt against the five parts of a rubric prompt and name the part that is missing.',
    prereq=['Prompts and the parts of a rubric prompt from [Chapter 12](../../chapters/12-ai-agents-prompts-scoring/index.md).'],
    activities=[
        '**Explore (3 min).** Press each card. Which empty band of the weak prompt would cause the worst answer, and why?',
        '**Quiz (3 min).** Press **Quiz Me** and match four descriptions to the two cards.',
        '**Rewrite (4 min).** Take a prompt you have used. Fill in the five bands. Which one was missing?',
    ],
    assessment=[
        ('Which part tells the model what to do when it cannot tell?', 'Rules: write "not checkable".'),
        ('Why does the strong prompt include the full text of the resource?', 'The input band supplies the material, so the model does not assume it knows it.'),
        ('Does a strong prompt guarantee a correct answer?', 'No. Answers still need checking, which is why Chapters 13 and 14 exist.'),
    ],
    connection='A rubric prompt is how an agent is told to apply the ten metrics and return evidence. The evidence column is what Chapter 14 checks.',
    ref_nums=[(CH, [2, 6, 7, 9])],
    key_questions=['Which of the five bands is empty?', 'What should the model write when it cannot tell?'],
    misconceptions=['A short prompt is a good prompt', 'A good prompt guarantees a good answer'],
    good=['The prompt text is drawn as live text so its wording is exact.'],
    verify=[(CH, '| Role | None | You are a careful reviewer of open educational resources. |'),
            (CH, '| Task | "Check accessibility." | Apply the ten accessibility checks listed below to the resource. |'),
            (CH, '| Input | The resource is not included | The full text of the resource, pasted below the checks |'),
            (CH, '| Rules | None | Quote evidence for every result. If a check cannot be verified from the text, write "not checkable". |'),
            (CH, '| Output format | None | A table with the columns check, result, and evidence |')],
)

BANDS = [
    ('Role', '#1d4f86', None, 'You are a careful reviewer of open educational resources.'),
    ('Task', '#00796b', 'Check accessibility.', 'Apply the ten accessibility checks listed below to the resource.'),
    ('Input', '#8a5a00', None, 'The full text of the resource, pasted below the checks.'),
    ('Rules', '#573379', None, 'Quote evidence for every result. If a check cannot be verified from the text, write "not checkable".'),
    ('Output format', '#1b5e20', None, 'A table with the columns check, result, and evidence.'),
]


def card(c, x, y, w, h, strong):
    c.rect(x + 5, y + 6, w, h, fill=GRAYM, rx=10)
    c.rect(x, y, w, h, fill=WHITE, stroke=INK, sw=3, rx=10)
    bh = (h - 16) / 5
    for i, (name, hue, weak_txt, strong_txt) in enumerate(BANDS):
        by = y + 8 + i * bh
        c.rect(x + 8, by, 116, bh - 6, fill=hue, rx=6)
        c.text(x + 66, by + bh / 2 + 4, name, 16, 'bold', WHITE, 'middle', maxw=106, minsize=12)
        filled = strong or weak_txt
        if filled:
            c.rect(x + 130, by, w - 138, bh - 6, fill=WHITE, stroke=hue, sw=2.5, rx=6)
            txt = strong_txt if strong else weak_txt
            c.para(x + 142, by + 24, txt, w - 162, 16 if strong else 21, 1.18, 'bold' if not strong else 'normal', INK, maxlines=3)
        else:
            c.rect(x + 130, by, w - 138, bh - 6, fill='url(#hatch)', stroke=GRAY, sw=2, rx=6, dash='6 5')
            c.text(x + 142 + (w - 162) / 2, by + bh / 2 + 4, 'empty', 15, 'normal', MUTED, 'middle', italic=True)
    return bh


def draw():
    c = Canvas(1200, 700)
    stripe_defs(c, 'hatch', '#d3d9e0', '#f7f9fc')
    title_block(c, 'Weak Prompt, Strong Prompt', 'Every rubric prompt has the same five parts. How many does yours have?')
    y0, y1 = 112, 626
    lx, lw, rx, rw = 30, 450, 510, 660
    items = []
    for (x, w, name, strong, hue, verdict, chip_c) in ((lx, lw, 'Weak prompt', False, '#b71c1c', 'One of five parts', '#fde8e8'),
                                                        (rx, rw, 'Strong prompt', True, '#1b5e20', 'All five parts', '#e5f2e6')):
        c.rect(x, y0 - 6, w, y1 - y0 + 12, fill=chip_c, stroke=hue, sw=3, rx=14)
        c.text(x + 18, y0 + 28, name, 26, 'bold', hue)
        c.chip(x + w - 16, y0 + 8, verdict, fill=hue, size=15, h=28, anchor='end')
        card(c, x + 16, y0 + 48, w - 32, y1 - y0 - 66, strong)
        items.append(dict(id='strong' if strong else 'weak', label=name, color=hue, box=(x, y0 - 6, x + w, y1 + 6),
                          summary=('The strong prompt fills all five bands.' if strong else 'The weak prompt fills only the task band.'),
                          facts=(['Role: %s' % BANDS[0][3], 'Task: %s' % BANDS[1][3], 'Input: %s' % BANDS[2][3], 'Rules: %s' % BANDS[3][3], 'Output format: %s' % BANDS[4][3]]
                                 if strong else ['Task: "Check accessibility."', 'Role: none.', 'Input: the resource is not included.', 'Rules: none.', 'Output format: none.',
                                                 'With no role, input, rules, or format, the model has to guess what to check and how to answer.'])))
    # arrow from the evidence column to chapter 14
    c.chip(rx + rw - 22, y1 - 6, 'Chapter 14 verifies this evidence', fill=INK, size=14, h=26, anchor='end')
    c.text(40, 670, 'A good prompt does not guarantee a good answer. Chapters 13 and 14 exist because answers still need checking.', 17, 'bold', INK, maxw=1120)
    quiz = [
        dict(question='Which card has a role, a task, input, rules, and an output format?', correct_zone='strong', explanation='The strong prompt fills all five bands.'),
        dict(question='Which card says only "Check accessibility." and leaves four bands empty?', correct_zone='weak', explanation='The weak prompt has only a task.'),
        dict(question='Which card tells the model to write "not checkable" when it cannot verify a check?', correct_zone='strong', explanation='That is in the rules band of the strong prompt.'),
        dict(question='Which card gives the model no resource text to check?', correct_zone='weak', explanation='The input band is empty, so the resource is not included.'),
    ]
    return c, items, quiz
