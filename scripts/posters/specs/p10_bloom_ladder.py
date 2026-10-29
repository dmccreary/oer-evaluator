"""Poster 10: Bloom's Ladder: Six Levels, Measurable Verbs (Chapter 6, grid, 6 zones plus a mismatch panel)."""
from svgkit import *

CH = '06-alignment-readability'

META = dict(
    slug='bloom-ladder',
    title='Bloom\'s Ladder: Six Levels, Measurable Verbs',
    chapter=CH,
    overlay='grid',
    topic='The six levels of the revised Bloom taxonomy and their measurable verbs',
    desc='A six-step staircase of the revised Bloom taxonomy with measurable verbs and an example objective for each level, plus a panel on matching outcomes to activities.',
    intro=('The alignment metric, the outcome verb checks, the quiz bank, and this book\'s own learning outcomes all use Bloom\'s levels, so this poster is a reference to come back to. '
           'It uses the 2001 revised names. The verbs are the largest text on each step because they are what a writer or auditor actually uses. '
           'A side panel shows the mismatch the chapter warns about: an outcome that says "predict" taught by activities that ask only for recall.'),
    alt=('A staircase of six steps rising from left to right. 1 Remember: list, name, define. Example: list the five parts of a lesson plan. '
         '2 Understand: explain, summarize, interpret. Example: explain why the seasons change. 3 Apply: calculate, use, solve. Example: calculate the perimeter of a garden. '
         '4 Analyze: distinguish, differentiate, examine. Example: differentiate a cause from an effect in a historical event. '
         '5 Evaluate: judge, critique, justify. Example: judge which of two designs is fairer, and justify the choice. '
         '6 Create: design, compose, construct. Example: design an experiment to test how light affects plant growth. '
         'A side panel shows a level mismatch: the outcome says predict, but every activity asks only for recall.'),
    bloom='Remember',
    objective='**name** the six levels of the revised Bloom taxonomy in order and **match** measurable verbs to their levels.',
    objective_plain='name the six levels of the revised Bloom taxonomy in order and match measurable verbs to their levels.',
    prereq=['The alignment metric from [Chapter 6](../../chapters/06-alignment-readability/index.md).'],
    activities=[
        '**Explore (3 min).** Press each step and read its verbs and example objective.',
        '**Quiz (3 min).** Press **Quiz Me** and find the level for six verbs or examples.',
        '**Audit (4 min).** Take one outcome from a resource you use. Circle its verb. Which level is it, and do the activities sit at the same level?',
    ],
    assessment=[
        ('Which level are "explain", "summarize", and "interpret"?', 'Understand.'),
        ('Which level asks learners to put parts together into something new?', 'Create.'),
        ('An outcome says "predict" and every activity asks only for recall. What is wrong?', 'The outcome and its activities sit at different levels, so learners never practice the skill the outcome asks for.'),
    ],
    connection='An outcome and the activities that teach it should sit at the same level. That is the core of the alignment metric.',
    ref_nums=[(CH, [1, 3, 7])],
    key_questions=['What verb does this outcome use?', 'Do the activities ask for the same level?'],
    misconceptions=['Higher levels matter more than lower ones', 'Bloom\'s taxonomy is a pyramid with fewer outcomes at the top'],
    good=['The poster is a staircase and not a pyramid. The chapter does not claim that fewer outcomes belong at the top.'],
    verify=[(CH, '| Remember | Recall facts and terms | list, name, define | List the five parts of a lesson plan. |'),
            (CH, '| Understand | Explain ideas in your own words | explain, summarize, interpret | Explain why the seasons change. |'),
            (CH, '| Apply | Use knowledge in a new situation | calculate, use, solve | Calculate the perimeter of a garden. |'),
            (CH, '| Analyze | Break material into parts and see how they relate | distinguish, differentiate, examine | Differentiate a cause from an effect in a historical event. |'),
            (CH, '| Evaluate | Judge using criteria | judge, critique, justify | Judge which of two designs is fairer, and justify the choice. |'),
            (CH, '| Create | Put parts together into something new | design, compose, construct | Design an experiment to test how light affects plant growth. |'),
            (CH, 'If an outcome says "predict" and every activity asks only for recall')],
)

LEVELS = [
    ('Remember', ['list', 'name', 'define'], 'List the five parts of a lesson plan.', 'Recall facts and terms'),
    ('Understand', ['explain', 'summarize', 'interpret'], 'Explain why the seasons change.', 'Explain ideas in your own words'),
    ('Apply', ['calculate', 'use', 'solve'], 'Calculate the perimeter of a garden.', 'Use knowledge in a new situation'),
    ('Analyze', ['distinguish', 'differentiate', 'examine'], 'Differentiate a cause from an effect in a historical event.', 'Break material into parts and see how they relate'),
    ('Evaluate', ['judge', 'critique', 'justify'], 'Judge which of two designs is fairer, and justify the choice.', 'Judge using criteria'),
    ('Create', ['design', 'compose', 'construct'], 'Design an experiment to test how light affects plant growth.', 'Put parts together into something new'),
]
RAMP = [('#d0ece7', INK), ('#a3dad0', INK), ('#74c4b6', INK), ('#2a7f73', WHITE), ('#1a6559', WHITE), ('#0e4a41', WHITE)]


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Bloom\'s Ladder: Six Levels, Measurable Verbs', 'The revised taxonomy. Write outcomes with the verbs, and match the activities to the same level.')
    base = 650
    x0, cw, gap = 30, 150, 6
    items = []
    for i, (name, verbs, ex, mean) in enumerate(LEVELS):
        fill, ink = RAMP[i]
        h = 330 + 46 * i
        x = x0 + i * (cw + gap)
        top = base - h
        c.rect(x, top, cw, h, fill=fill, stroke=INK if i < 3 else fill, sw=2, rx=10)
        c.circle(x + 24, top + 28, 15, fill=INK if i < 3 else WHITE)
        c.text(x + 24, top + 34, str(i + 1), 17, 'bold', WHITE if i < 3 else INK, 'middle')
        c.text(x + 46, top + 34, name, 20, 'bold', ink, maxw=cw - 52)
        yy = top + 74
        for v in verbs:
            c.text(x + 12, yy, v, 22 if len(v) < 11 else 19, 'bold', ink, maxw=cw - 20)
            yy += 28
        c.line(x + 12, yy - 8, x + cw - 12, yy - 8, ink, 1.5, opacity=0.5)
        c.text(x + 12, yy + 14, 'EXAMPLE', 12, 'bold', ink, spacing='1')
        c.para(x + 12, yy + 34, ex, cw - 22, 14.5, 1.22, 'normal', ink, maxlines=6)
        items.append(dict(id=name.lower(), label=name, color=['#00796b', '#00796b', '#00796b', '#1a6559', '#1a6559', '#0e4a41'][i],
                          box=(x, top, x + cw, base),
                          summary='%s: %s.' % (name, mean.lower()),
                          facts=['Measurable verbs: %s.' % ', '.join(verbs), 'Example objective: %s' % ex]))
    # mismatch panel
    mx, mw = 990, 180
    top = 150
    c.rect(mx, top, mw, base - top, fill=WHITE, stroke=ORANGE, sw=3, rx=12)
    c.rect(mx, top, mw, 46, fill=ORANGE, rx=12)
    c.rect(mx, top + 24, mw, 22, fill=ORANGE)
    c.text(mx + mw / 2, top + 31, 'Level mismatch', 19, 'bold', INK, 'middle')
    c.text(mx + 14, top + 78, 'OUTCOME SAYS', 12, 'bold', MUTED, spacing='1')
    c.chip(mx + 14, top + 88, 'predict', fill=INK, size=19, h=32)
    c.text(mx + 14, top + 156, 'ACTIVITIES ASK ONLY', 12, 'bold', MUTED, spacing='1')
    c.chip(mx + 14, top + 166, 'recall', fill=GRAY, size=19, h=32)
    ic_warn(c, mx + mw / 2, top + 244, 24, ORANGE)
    c.para(mx + 14, top + 296, 'Learners practice a skill the outcome does not ask for, and never practice the skill it does.', mw - 28, 15.5, 1.25, 'normal', INK, maxlines=7)
    items.append(dict(id='level-mismatch', label='Level mismatch', color=ORANGE, box=(mx, top, mx + mw, base),
                      summary='An outcome and its activities should sit at the same level.',
                      facts=['If an outcome says "predict" and every activity asks only for recall, learners practice a skill that the outcome does not ask for.',
                             'They never practice the skill the outcome does ask for.']))
    c.text(30, 686, 'Revised (2001) names. A staircase, not a pyramid: the levels are not a ranking of importance.', 14, 'normal', MUTED, maxw=940)
    quiz = [
        dict(question='Which level uses the verbs explain, summarize, and interpret?', correct_zone='understand', explanation='These verbs ask learners to explain ideas in their own words.'),
        dict(question='Which level asks learners to design, compose, or construct something new?', correct_zone='create', explanation='Create puts parts together into something new.'),
        dict(question='Which level has the example "Calculate the perimeter of a garden"?', correct_zone='apply', explanation='Using knowledge in a new situation is Apply.'),
        dict(question='Which level has the verbs judge, critique, and justify?', correct_zone='evaluate', explanation='Evaluate means judging using criteria.'),
        dict(question='Which zone shows an outcome that says "predict" taught by activities that ask only for recall?', correct_zone='level-mismatch', explanation='Outcome and activities sit at different levels.'),
        dict(question='Which level has the verbs list, name, and define?', correct_zone='remember', explanation='Remember recalls facts and terms.'),
    ]
    return c, items, quiz
