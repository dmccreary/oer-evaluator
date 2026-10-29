"""Poster 31: The Sixth R: Regenerate (Chapter 1, grid, 6 zones). Lives in docs/posters/."""
from svgkit import *

CH = '01-foundations-of-oer'
CH18 = '18-components-publishing-oer'

META = dict(
    slug='sixth-r',
    home='posters',
    title='The Sixth R: Regenerate',
    chapter=CH,
    overlay='grid',
    topic='The proposed sixth R, regenerate, and the source behind an AI-built textbook',
    desc='A source-to-book picture that shows what the proposed sixth R, regenerate, adds to the 5Rs: the right to rebuild an intelligent textbook from its course description, learning graph, and agentic skills.',
    intro=('This poster shows what the proposed sixth R adds to the 5Rs. David Wiley\'s five permissions describe what you may do with '
           'a finished book: retain it, reuse it, revise it, remix it, and redistribute it. An intelligent textbook is built by AI agents from a '
           'source: a course description, a learning graph, and agentic skills. A license that covers only the rendered book gives you a copy of '
           'the output but not the means to produce it. The Intelligent Textbooks site proposes regenerate as the sixth R, the right to recreate, '
           'update, or produce new versions of the textbook from that source. The picture reads left to right: the source on the left, the '
           'regenerate arrow in the middle, and the book on the right, with the five Rs listed where they act.'),
    alt=('A picture that reads left to right. On the left, a panel titled The source, the means of production, holds three stacked cards: '
         'course description, which is where the book starts and from which agents build chapters, simulations, and quizzes; learning graph, a map of '
         'the concepts and what each depends on; and agentic skills, reusable documented steps an AI agent follows to build the book. '
         'In the middle, a thick arrow points from the source to the book and is labeled Regenerate, the sixth R, proposed. '
         'On the right, a panel titled The book, the output, shows a rendered page of chapters, MicroSims, and quizzes. Under it, five rows labeled '
         'Wiley\'s 5Rs act here list Retain, Reuse, Revise, Remix, and Redistribute with their test questions, joined by small down arrows to show that each '
         'builds on the one before. A bar along the bottom reads: a license on the output alone gives you a copy, not the means of production; '
         'regenerate closes that gap.'),
    bloom='Understand',
    objective='**explain** how the proposed sixth R, regenerate, differs from the 5Rs, using the source and the book on the poster.',
    objective_plain='explain how the proposed sixth R, regenerate, differs from the 5Rs, using the source and the book on the poster.',
    prereq=['The 5R permissions from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).',
            'The meaning of an intelligent textbook and a learning graph from [Chapter 18](../../chapters/18-components-publishing-oer/index.md).'],
    activities=[
        '**Explore (3 min).** Press each of the six zones. Which of the three source pieces would be hardest for another author to recreate, and why?',
        '**Quiz (3 min).** Press **Quiz Me** and place six descriptions on the poster.',
        '**Apply (4 min).** Pick an AI-built textbook you know. Can you find its course description, its learning graph, and its skills? Could you rebuild it for a different course?',
    ],
    assessment=[
        ('An author posts a textbook under an open license but keeps the learning graph and skills private. Which right is missing?',
         'Regenerate. You have a copy of the output but not the means of production.'),
        ('A teacher translates one chapter of an open textbook by hand. Is that regenerate?',
         'No. Changing the finished book is revise. Regenerate means producing a new version from the source.'),
        ('Is regenerate one of David Wiley\'s original 5Rs?',
         'No. It is a proposal on the Intelligent Textbooks site that extends the 5Rs to the source of a textbook.'),
    ],
    connection=('The rubric\'s open license metric asks whether the 5R permissions are granted, and its editable source metric asks whether others can change the resource. '
                'Regenerate asks a further question about AI-built books: is the source that produced the book published too? '
                'None of the ten metrics scores that today, so treat it as a question to ask during a manual review, not as a rubric score.'),
    ref_nums=[(CH, [6])],
    refs=['[The 6th "R" of Intelligent Textbooks](https://dmccreary.github.io/intelligent-textbooks/appendices/five-rs-of-intelligent-textbooks/) - Dan McCreary, Intelligent Textbooks - '
          'Extends David Wiley\'s 5Rs of open content with a sixth right, regenerate, for rebuilding a textbook from its learning graph, course description, and skills. '
          'The source of the proposal this poster illustrates.'],
    key_questions=['Can I recreate it from its source?', 'Which parts of the source are published with the book?'],
    misconceptions=['An open license on the rendered book is enough to rebuild the book',
                    'Regenerate is one of Wiley\'s original 5Rs',
                    'Regenerate means hand-editing the text again'],
    good=['Regenerate is a proposal from the Intelligent Textbooks site. It is not part of David Wiley\'s 5Rs, so the poster labels it "proposed".',
          'The five test questions are the ones in Chapter 1. The test question for regenerate is written for this poster, in the same form.'],
    verify=[(CH, 'Can I make and keep my own copy?'), (CH, 'Can I use it as it is?'), (CH, 'Can I change it?'),
            (CH, 'Can I combine it with other open work?'), (CH, 'Can I share copies with others?'),
            (CH18, 'A **learning graph** is a map of the concepts of a subject')],
)

ORG, ORGD, ORGL = '#c77700', '#8a5a00', '#fff6d6'   # the source and the sixth R
TL, TLD = '#00796b', '#004d40'                      # the book and the 5Rs


def icon_course_description(c, cx, cy):
    ic_doc(c, cx - 17, cy - 22, 34, 44, fill=WHITE, stroke=ORGD)
    ic_lines(c, cx - 11, cy - 2, 22, n=3, gap=8, stroke=ORG, sw=3)


def icon_learning_graph(c, cx, cy):
    pts = [(cx, cy - 17), (cx - 17, cy + 1), (cx + 17, cy + 1), (cx - 9, cy + 19), (cx + 9, cy + 19)]
    for a, b in ((0, 1), (0, 2), (1, 3), (2, 4), (1, 2)):
        c.line(pts[a][0], pts[a][1], pts[b][0], pts[b][1], ORGD, 2.5)
    for x, y in pts:
        c.circle(x, y, 5.5, fill=ORGD)


def icon_skills(c, cx, cy):
    ic_gear(c, cx, cy, 21, fill=ORGD)


def source_card(c, x, y, w, h, icon, name, text):
    c.rect(x, y, w, h, fill=WHITE, stroke=ORG, sw=3, rx=14)
    cx, cy = x + 46, y + h / 2
    c.circle(cx, cy, 33, fill=ORGL, stroke=ORG, sw=3)
    icon(c, cx, cy)
    tx, tw_ = x + 94, w - 94 - 14
    c.text(tx, y + 42, name, 24, 'bold', ORGD, maxw=tw_)
    c.para(tx, y + 72, text, tw_, 18, 1.25, 'normal', INK, maxlines=3, maxh=h - 80)


R_ROWS = [('Retain', 'Can I make and keep my own copy?'),
          ('Reuse', 'Can I use it as it is?'),
          ('Revise', 'Can I change it?'),
          ('Remix', 'Can I combine it with other open work?'),
          ('Redistribute', 'Can I share copies with others?')]


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'The Sixth R: Regenerate',
                'Wiley\'s 5Rs cover the finished book. A proposed sixth R covers the source that builds it.')

    top, bot = 104, 600
    # ---- left: the source ------------------------------------------------
    c.rect(40, top, 410, bot - top, fill=ORGL, stroke=ORG, sw=3, rx=18)
    x0, w0 = c.chip(60, top + 14, 'The source', fill=ORGD, size=21, h=34)
    c.text(x0 + w0 + 12, top + 38, 'the means of production', 19, 'normal', INK)
    cards = [
        (162, icon_course_description, 'Course description', 'Where the book starts. Agents build chapters, simulations, and quizzes from it.'),
        (304, icon_learning_graph, 'Learning graph', 'A map of the book\'s concepts and what each one depends on.'),
        (446, icon_skills, 'Agentic skills', 'Reusable, documented steps an AI agent follows to build the book.'),
    ]
    items = []
    ids = ['course-description', 'learning-graph', 'agentic-skills']
    for (y, ic, name, text), zid in zip(cards, ids):
        source_card(c, 60, y, 370, 132, ic, name, text)
        items.append(dict(id=zid, label=name, color=ORG, box=(60, y, 430, y + 132)))

    # ---- middle: regenerate ----------------------------------------------
    mid_y = (top + bot) / 2
    c.arrow(462, mid_y, 708, mid_y, stroke=ORG, sw=20, head=40)
    c.chip(585, mid_y - 76, 'Regenerate', fill=ORGD, size=25, h=44, padx=16, anchor='middle')
    c.text(585, mid_y + 56, 'the sixth R', 20, 'bold', ORGD, 'middle')
    c.text(585, mid_y + 80, '(proposed)', 18, 'normal', INK, 'middle')
    items.append(dict(id='regenerate', label='Regenerate', color=ORG, box=(456, mid_y - 90, 714, mid_y + 92)))

    # ---- right: the book and the 5Rs -------------------------------------
    c.rect(720, top, 440, bot - top, fill=WHITE, stroke=TL, sw=3, rx=18)
    x1, w1 = c.chip(740, top + 14, 'The book', fill=TLD, size=21, h=34)
    c.text(x1 + w1 + 12, top + 38, 'the output', 19, 'normal', INK)
    ic_doc(c, 748, 160, 78, 100, fill=WHITE, stroke=TLD)
    ic_lines(c, 762, 200, 44, n=4, gap=11, stroke=TL, sw=4)
    c.para(848, 192, 'The rendered site that readers see: chapters, MicroSims, and quizzes.', 290, 19, 1.28, 'normal', INK, maxlines=4)
    items.append(dict(id='the-book', label='The book', color=TL, box=(720, top, 1160, 300)))

    c.line(740, 308, 1140, 308, GRAYM, 2, dash='6 6')
    c.text(740, 336, 'Wiley\'s 5Rs act here', 21, 'bold', TLD)
    for i, (name, q) in enumerate(R_ROWS):
        y = 350 + i * 50
        c.chip(740, y, name, fill=TLD, size=19, h=38, padx=(150 - tw(name, 19, 'bold')) / 2)
        n = len(c.wrap(q, 236, 17))
        c.para(904, y + 25 - (n - 1) * 9, q, 236, 17, 1.07, 'normal', INK, maxlines=2)
        if i < len(R_ROWS) - 1:
            c.poly([(808, y + 40), (822, y + 40), (815, y + 49)], fill=TLD)
    items.append(dict(id='five-rs', label='The 5Rs', color=TL, box=(720, 312, 1160, bot)))

    # ---- bottom strip ----------------------------------------------------
    c.rect(40, 612, 1120, 46, fill=WHITE, stroke=ORG, sw=2.5, rx=12, dash='9 6')
    c.text(600, 642, 'A license on the output alone gives you a copy, not the means of production. Regenerate closes that gap.',
           18, 'bold', INK, 'middle', maxw=1090, minsize=16)
    c.text(40, 686, 'Regenerate is a proposal on the Intelligent Textbooks site, not part of Wiley\'s 5Rs. The five test questions are from Chapter 1.',
           15, 'normal', MUTED, maxw=1120)

    facts = {
        'course-description': (
            'Course description: where the book starts. Agents build the chapters from it.',
            ['Agentic workflows turn a course description into chapters, simulations, quizzes, and a learning graph.',
             'It is part of the source. The rendered book on its own does not include it.',
             'Publishing it lets another author start from the same description, or change it, which supports remix and regenerate.']),
        'learning-graph': (
            'Learning graph: a map of the book\'s concepts and what each one depends on.',
            ['Chapter 18 defines it as a map of the concepts of a subject, each linked to the concepts it depends on.',
             'It is part of the source of an intelligent textbook, so retaining the book means retaining the graph too.',
             'Publishing it supports remix and regenerate.']),
        'agentic-skills': (
            'Agentic skills: reusable, documented steps an AI agent follows to build the book.',
            ['Documented, reusable skills let another author regenerate a textbook from a different course description.',
             'Platform-independent instructions can produce versions of the book across different AI tools.',
             'Without the skills, the book is a finished artifact. With them, it can be rebuilt.']),
        'regenerate': (
            'Regenerate, the proposed sixth R: the right to recreate, update, or produce new versions of an intelligent textbook.',
            ['It applies to the source (the course description, learning graph, and agentic skills), not only to the rendered book.',
             'Test question, written for this poster: Can I recreate it from its source?',
             'An open license on the rendered Markdown gives you the output but not the means of production. Regenerate closes that gap.',
             'It is a proposal on the Intelligent Textbooks site. It is not part of Wiley\'s original framework.',
             'The site weighed three other candidates (reason, respond, reflect) and chose regenerate. Those three describe what an AI does when a learner uses the book. Regenerate is a freedom over the book itself, like the other five.']),
        'the-book': (
            'The book: the rendered output that readers see and the 5Rs act on.',
            ['The rendered Markdown: chapters, MicroSims, and quizzes.',
             'Markdown output is only half the story. Without the source, the book is no more adaptable than a PDF.',
             'David Wiley proposed the 5Rs in 2014 to describe what an open license lets you do with a finished resource like this.']),
        'five-rs': (
            'The 5Rs: five permissions that an open license grants on the finished book.',
            ['Retain, reuse, revise, remix, and redistribute. The Intelligent Textbooks site calls them cumulative: you cannot revise what you cannot retain.',
             'The test question beside each name is the one Chapter 1 teaches.',
             'For an AI-built book, each R gets a wider meaning. Retain, for example, includes the prompts, skills, and learning graph that generated the book.']),
    }
    for it in items:
        it['summary'], it['facts'] = facts[it['id']]

    quiz = [
        dict(question='Which zone is the right to recreate, update, or produce new versions of the textbook?', correct_zone='regenerate',
             explanation='That is the definition of regenerate, the proposed sixth R.'),
        dict(question='Which zone holds the five permissions that David Wiley named?', correct_zone='five-rs',
             explanation='The 5Rs describe what you may do with the finished book.'),
        dict(question='Which zone is the map of the book\'s concepts and what each one depends on?', correct_zone='learning-graph',
             explanation='A learning graph links each concept to the concepts it depends on.'),
        dict(question='Which zone is the starting point that agents turn into chapters, simulations, and quizzes?', correct_zone='course-description',
             explanation='Agentic workflows begin with the course description.'),
        dict(question='Which zone holds the reusable, documented steps an AI agent follows to build the book?', correct_zone='agentic-skills',
             explanation='Those steps are the agentic skills. With them, another author can rebuild the book for a different course.'),
        dict(question='Which zone is the rendered output, the chapters, MicroSims, and quizzes that readers see?', correct_zone='the-book',
             explanation='The book is the output. The source is what produces it.'),
    ]
    return c, items, quiz
