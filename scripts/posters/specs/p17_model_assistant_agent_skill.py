"""Poster 17: Model, Assistant, Agent, Skill (Chapter 12, grid, 4 zones as stacked layers)."""
from svgkit import *

CH = '12-ai-agents-prompts-scoring'

META = dict(
    slug='model-assistant-agent-skill',
    title='Model, Assistant, Agent, Skill',
    chapter=CH,
    overlay='grid',
    topic='The four layers of AI vocabulary: model, assistant, agent, and skill',
    desc='Four stacked layers, each built on the one below it: a language model, an AI assistant, an AI agent, and an agent skill, with the book\'s own example for each.',
    intro=('The vocabulary is the first barrier in the AI half of the book, and mixing the terms leads to wrong decisions about what to trust. This poster stacks four layers, each built on the one below. '
           'A large language model predicts the next piece of text and does not look facts up. An AI assistant is a program you talk to in ordinary language that answers and waits. '
           'An AI agent adds tools, files, and a loop of observe, decide, act, and observe the result. An agent skill is a packaged set of instructions that is the durable, shareable form of a rubric prompt. '
           'The poster leaves out product and model names, which date quickly.'),
    alt=('Four horizontal layers stacked from the bottom. Bottom, Large language model: predicts the next piece of text, one piece at a time; it does not look facts up, and it can sound sure when it is wrong. Example: filling in the next word. '
         'Above it, AI assistant: a program you talk to in ordinary language that answers and waits, powered by a model. Example: pasting in a resource and asking for problems. '
         'Above that, AI agent: adds tools, files, and a loop of observe, decide, act, and observe the result. Example: listing 14 links and testing each. '
         'Top, Agent skill: a packaged set of instructions in a folder, with a short description that tells the agent when to use it. Example: the ten-metric rubric packaged as a skill. '
         'The step from model to assistant adds a conversation; from assistant to agent adds tools and a loop; from agent to skill adds a saved procedure.'),
    bloom='Understand',
    objective='**distinguish** a language model, an assistant, an agent, and a skill, and **say** which layer adds tools and a loop.',
    objective_plain='distinguish a language model, an assistant, an agent, and a skill, and say which layer adds tools and a loop.',
    prereq=['The vocabulary of [Chapter 12](../../chapters/12-ai-agents-prompts-scoring/index.md).'],
    activities=[
        '**Explore (3 min).** Press each layer from the bottom up. What does each step add?',
        '**Quiz (3 min).** Press **Quiz Me** and match four descriptions to the layers.',
        '**Sort (4 min).** Write down three AI tools you have used. Which layer is each one, and what would you need to check?',
    ],
    assessment=[
        ('Which layer answers and waits?', 'The AI assistant.'),
        ('Which layer plans, acts, looks at what happened, and acts again?', 'The AI agent.'),
        ('What does a language model not do?', 'It does not look facts up, and it can sound sure when it is wrong.'),
    ],
    connection='The difference between an assistant that answers and an agent that acts across steps decides what a reviewer must check in Chapters 13 and 14.',
    ref_nums=[(CH, [1, 3, 6, 8])],
    key_questions=['Does it answer and wait, or act across steps?', 'Does it look facts up?'],
    misconceptions=['A language model looks facts up', 'An assistant and an agent are the same thing'],
    good=['The poster leaves out product and model names, which date quickly, and uses no robot or glowing-brain pictures.'],
    verify=[(CH, 'An assistant answers and waits. An agent plans, acts, looks at what happened, and acts again'),
            (CH, 'observe the situation, decide the next step, act, and observe the result'),
            (CH, 'It does not look facts up, and it can sound sure when it is wrong.'),
            (CH, 'The skill is the durable form of a rubric prompt'),
            (CH, 'Read the resource\'s source and list 14 links')],
)

# bottom to top
LAYERS = [
    ('model', 'Large language model', 'Predicts the next piece of text, one piece at a time.',
     'Filling in the next word.', 'Limits: it does not look facts up, and it can sound sure when it is wrong.', '#8a5a00', '#fdf1d6'),
    ('assistant', 'AI assistant', 'A program you talk to in ordinary language. It answers and waits.',
     'Paste in a resource and ask for problems.', 'Powered by a model.', '#1d4f86', '#e6eef8'),
    ('agent', 'AI agent', 'Works toward a goal over several steps, using tools and files.',
     'List 14 links and test each one.', 'Loop: observe, decide, act, observe the result.', '#00796b', '#e3f4f1'),
    ('skill', 'Agent skill', 'A saved set of instructions that an agent loads when a task matches.',
     'The ten-metric rubric packaged as a skill.', 'The durable, shareable form of a rubric prompt.', '#573379', '#efe6f6'),
]
STEPS = ['', 'adds a conversation', 'adds tools and a loop', 'adds a saved procedure']


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Model, Assistant, Agent, Skill', 'Four layers, each built on the one below. What does each step add?')
    y_top, bh, gap = 100, 118, 32
    items = []
    n = len(LAYERS)
    for k, (zid, name, diff, ex, extra, hue, tint) in enumerate(LAYERS):
        i = n - 1 - k   # top is the last layer
        y = y_top + i * (bh + gap)
        x, w = 30, 1140
        c.rect(x, y, w, bh, fill=tint, stroke=hue, sw=3, rx=14)
        c.rect(x, y, 230, bh, fill=hue, rx=14)
        c.rect(x + 200, y, 30, bh, fill=hue)
        c.text(x + 20, y + 40, str(k + 1), 36, 'bold', WHITE)
        c.para(x + 62, y + 46, name, 160, 20, 1.15, 'bold', WHITE, maxlines=2)
        # icon
        icx, icy = x + 190, y + 98
        if zid == 'model':
            for k in range(3):
                c.circle(x + 70 + k * 18, y + 92, 5, fill=WHITE)
        elif zid == 'assistant':
            ic_bubble(c, x + 66, y + 78, 62, 26, fill=WHITE, stroke=WHITE, tail='left')
        elif zid == 'agent':
            ic_gear(c, x + 84, y + 90, 15, WHITE)
        else:
            ic_folder(c, x + 62, y + 78, 48, 34, fill='#fff3b0', stroke=INK)
        c.para(x + 250, y + 44, diff, 520, 24, 1.15, 'bold', INK, maxlines=3)
        c.text(x + 250, y + bh - 20, extra, 16, 'normal', hue, maxw=520, minsize=13)
        c.rect(x + 800, y + 14, 326, bh - 28, fill=WHITE, stroke=hue, sw=2, rx=10)
        c.text(x + 816, y + 38, 'THE BOOK\'S EXAMPLE', 12, 'bold', hue, spacing='1')
        c.para(x + 816, y + 66, ex, 296, 19, 1.2, 'bold', INK, maxlines=3)
        if zid == 'model':
            ic_warn(c, x + 1100, y + bh - 30, 14, ORANGE)
        if k > 0:
            ay = y + bh + 4
            c.arrow(600, ay + gap - 4, 600, ay + 2, GRAY, 5, 14)
            c.chip(630, ay + 3, STEPS[k], fill=INK, size=15, h=26)
        items.append(dict(id=zid, label=name, color=hue, box=(x, y, x + w, y + bh),
                          summary=diff, facts=[diff, extra, 'The book\'s example: %s' % ex]))
    quiz = [
        dict(question='Which layer works toward a goal over several steps, using tools and files?', correct_zone='agent', explanation='An agent plans, acts, looks at what happened, and acts again.'),
        dict(question='Which layer is a program you talk to that answers and waits?', correct_zone='assistant', explanation='An assistant answers and waits.'),
        dict(question='Which layer does not look facts up and can sound sure when it is wrong?', correct_zone='model', explanation='A model completes likely text.'),
        dict(question='Which layer is a saved procedure in a folder that is the durable form of a rubric prompt?', correct_zone='skill', explanation='A skill packages instructions for reuse.'),
    ]
    return c, items, quiz
