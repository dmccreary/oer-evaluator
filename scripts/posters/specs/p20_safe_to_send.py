"""Poster 20: Safe to Send? Student Data and AI Services (Chapter 13, grid, 3 zones)."""
from svgkit import *

CH = '13-automated-checks-cost-privacy'

META = dict(
    slug='safe-to-send',
    title='Safe to Send? Student Data and AI Services',
    chapter=CH,
    overlay='grid',
    topic='Which materials are safe to send to an AI service',
    desc='Three chutes sort six items into send it, fix it first, and never send it, with a warning that text sent to an AI service cannot be pulled back.',
    intro=('A privacy mistake cannot be undone, and a teacher new to AI may paste a gradebook without thinking. This poster sorts the items from the Chapter 13 worked example into three chutes. '
           'The published text of an open textbook chapter and a rubric prompt template are safe to send. A class\'s quiz scores with student names need fixing first, because names make the scores personal data. '
           'A spreadsheet of grades with student ID numbers, a student\'s photograph, and an email thread with a parent about a student must never be sent. '
           'Shapes and icons carry the meaning as well as color, and a silhouette stands in for the photograph. The poster gives no legal advice.'),
    alt=('Three chutes. Send it, marked with a check in a circle: the published text of an open textbook chapter, and a rubric prompt template. They are public or hold no student data. '
         'Fix it first, marked with a wrench in a triangle: a class\'s quiz scores with student names. The names make the scores personal data, so anonymize or get approval first. '
         'Never send it, marked with a stop sign: a spreadsheet of grades with student ID numbers, a student\'s photograph shown as a silhouette, and an email thread with a parent about a student. '
         'A footer says that once text is sent to an AI service you cannot pull it back, names FERPA, and says if you are not sure, ask before you send.'),
    bloom='Apply',
    objective='**sort** six items into send it, fix it first, and never send it, and **state** why the sorting matters.',
    objective_plain='sort six items into send it, fix it first, and never send it, and state why the sorting matters.',
    prereq=['Student data privacy and FERPA from [Chapter 13](../../chapters/13-automated-checks-cost-privacy/index.md).'],
    activities=[
        '**Explore (3 min).** Press each chute and read why each item belongs in it.',
        '**Quiz (3 min).** Press **Quiz Me** and place six items in the right chute.',
        '**Apply (4 min).** List three files you would like an AI service to help with. Which chute is each in? Who would you ask if you are not sure?',
    ],
    assessment=[
        ('Why are quiz scores with names not safe as they are?', 'Names make the scores personal data, so anonymize or get approval first.'),
        ('Can you take back text you pasted into an AI service?', 'No. It has left your computer, and a deletion request may not undo it.'),
        ('What do you do if you are not sure an item is safe?', 'Ask before you send it.'),
    ],
    connection='The same care applies to the student-privacy rules for A/B tests in Chapter 16. Your school\'s policy decides what you may send.',
    ref_nums=[(CH, [6, 1, 7, 10])],
    key_questions=['Does it name or identify a student?', 'Can I take it back once it is sent?'],
    misconceptions=['Deleting a chat removes what was sent', 'Removing the name from a gradebook is always enough'],
    good=['The poster gives no legal advice. Your school\'s policy decides what you may send, and FERPA is the U.S. law that protects student education records.'],
    verify=[(CH, '| The published text of an open textbook chapter | Yes | It is public and holds no student data |'),
            (CH, '| A class\'s quiz scores with student names | Not as it is | Names make the scores personal data, so anonymize or get approval first |'),
            (CH, '| A spreadsheet of grades with student ID numbers | No | It is identifiable and sensitive |'),
            (CH, '| An email thread with a parent about a student | No | It is private and identifies a student |'),
            (CH, 'Once It Is Sent, You Cannot Pull It Back'),
            (CH, 'if you are not sure an item is safe, ask before you send it')],
)

CHUTES = [
    ('send-it', 'Send it', 'Safe to send', '#1b5e20', '#e5f2e6', ic_check,
     [('The published text of an open textbook chapter', 'It is public and holds no student data.', 'doc'),
      ('A rubric prompt template', 'It holds no student data.', 'doc')]),
    ('fix-it-first', 'Fix it first', 'Anonymize or get approval', '#8a5a00', '#fdf1d6', ic_warn,
     [('A class\'s quiz scores with student names', 'Names make the scores personal data, so anonymize or get approval first.', 'names')]),
    ('never-send', 'Never send it', 'Do not send', '#b71c1c', '#fde8e8', ic_stop,
     [('A spreadsheet of grades with student ID numbers', 'It is identifiable and sensitive.', 'grid'),
      ('A student\'s photograph', 'It identifies a person.', 'photo'),
      ('An email thread with a parent about a student', 'It is private and identifies a student.', 'mail')]),
]


def item_icon(c, kind, x, y, hue):
    if kind == 'doc':
        ic_doc(c, x - 18, y - 24, 36, 48, label=None, fold=9)
        ic_lines(c, x - 10, y - 2, 20, 3, gap=7)
    elif kind == 'names':
        c.rect(x - 24, y - 22, 48, 44, fill=WHITE, stroke=INK, sw=2.5, rx=4)
        for k in range(3):
            c.line(x - 18, y - 12 + k * 12, x + 4, y - 12 + k * 12, GRAYM, 3)
            c.rect(x + 8, y - 16 + k * 12, 12, 8, fill=hue, rx=2)
        c.rect(x - 28, y - 30, 30, 14, fill=hue, rx=7)
        c.text(x - 13, y - 19, 'name', 10.5, 'bold', WHITE, 'middle')
    elif kind == 'grid':
        c.rect(x - 24, y - 22, 48, 44, fill=WHITE, stroke=INK, sw=2.5, rx=4)
        for k in range(1, 4):
            c.line(x - 24, y - 22 + k * 11, x + 24, y - 22 + k * 11, GRAYM, 2)
        c.line(x - 4, y - 22, x - 4, y + 22, GRAYM, 2)
        c.line(x + 12, y - 22, x + 12, y + 22, GRAYM, 2)
        c.rect(x - 22, y - 20, 16, 8, fill=hue)
    elif kind == 'photo':
        c.rect(x - 24, y - 24, 48, 48, fill=WHITE, stroke=INK, sw=2.5, rx=4)
        ic_person(c, x, y + 2, 18, GRAY)
    else:
        c.rect(x - 24, y - 16, 48, 32, fill=WHITE, stroke=INK, sw=2.5, rx=4)
        c.path('M%s,%s L%s,%s L%s,%s' % (x - 24, y - 16, x, y + 4, x + 24, y - 16), stroke=INK, sw=2.5)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Safe to Send? Student Data and AI Services', 'Sort before you paste. Three chutes, six items from Chapter 13.')
    n, gap = 3, 16
    x0, x1, y0, y1 = 30, 1170, 108, 590
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, name, sub, hue, tint, icon, things) in enumerate(CHUTES):
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=tint, stroke=hue, sw=3, rx=14)
        c.poly([(x + 30, y0), (x + w - 30, y0), (x + w - 70, y0 + 66), (x + 70, y0 + 66)], fill=hue)
        c.rect(x, y0, w, 8, fill=hue, rx=4)
        c.circle(x + 50, y0 + 38, 25, fill=WHITE)
        icon(c, x + 50, y0 + 38, 18)
        c.text(x + 88, y0 + 38, name, 26, 'bold', WHITE, maxw=w - 100)
        c.text(x + 88, y0 + 60, sub, 15, 'normal', WHITE, maxw=w - 100)
        yy = y0 + 90
        for (label, why, kind) in things:
            hh = 108 if kind != 'names' else 150
            c.rect(x + 12, yy, w - 24, hh, fill=WHITE, stroke=hue, sw=2.5, rx=10)
            item_icon(c, kind, x + 52, yy + 34, hue)
            c.para(x + 92, yy + 28, label, w - 112, 17, 1.2, 'bold', INK, maxlines=3)
            c.para(x + 22, yy + (86 if kind != 'names' else 92), why, w - 44, 14.5, 1.2, 'normal', MUTED if kind != 'names' else INK, maxlines=3)
            yy += hh + 10
        items.append(dict(id=zid, label=name, color=hue, box=(x, y0, x + w, y1), summary=sub + '.',
                          facts=['%s: %s' % (l, w_) for (l, w_, k) in things]))
    # footer warning
    c.rect(30, 604, 1140, 78, fill=WHITE, stroke=INK, sw=3, rx=12)
    ic_warn(c, 64, 643, 20, ORANGE)
    c.text(100, 634, 'Once it is sent, you cannot pull it back.', 21, 'bold', INK, maxw=1040)
    c.para(100, 660, 'Text pasted into an AI service has left your computer, and a deletion request may not undo it. FERPA protects student education records. If you are not sure, ask before you send.', 1050, 15.5, 1.2, 'normal', INK, maxlines=2)
    quiz = [
        dict(question='Which chute holds the published text of an open textbook chapter and a rubric prompt template?', correct_zone='send-it', explanation='Both are public or hold no student data.'),
        dict(question='Which chute holds a class\'s quiz scores listed with student names?', correct_zone='fix-it-first', explanation='Names make the scores personal data.'),
        dict(question='Which chute holds a spreadsheet of grades with student ID numbers?', correct_zone='never-send', explanation='It is identifiable and sensitive.'),
        dict(question='Which chute holds an email thread with a parent about a student?', correct_zone='never-send', explanation='It is private and identifies a student.'),
    ]
    return c, items, quiz
