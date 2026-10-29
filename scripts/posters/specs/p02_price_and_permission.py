"""Poster 2: Free Is Not Open: Price and Permission (Chapter 1, grid, 4 zones)."""
import math

from svgkit import *

CH = '01-foundations-of-oer'

META = dict(
    slug='price-and-permission',
    title='Free Is Not Open: Price and Permission',
    chapter=CH,
    overlay='grid',
    topic='Free versus open: price and permission are independent',
    desc='A two-by-two matrix that shows price and permission are separate dials, so a free resource can be closed and a paid copy of an open resource can still be open.',
    intro=('This poster is a two-by-two matrix. The columns ask what the resource costs the user. The rows ask '
           'whether the user may edit and share it. The four cells use the four examples from Chapter 1. '
           'The point is that the two questions are independent: a zero on the price dial says nothing about the '
           'permission dial. A resource is OER because of what its license permits, not because of what it costs.'),
    alt=('A two-by-two matrix. Columns: costs the user nothing, and costs money. Rows: may edit and share (open), '
         'and may not edit or share (closed). Top left: a lesson plan licensed CC BY 4.0 is free and open. Top right: '
         'an open textbook that a print shop sells at cost is open, and only the printed copy costs money. Bottom left: '
         'a publisher sample chapter marked all rights reserved is free but closed. Bottom right: a commercial textbook '
         'from the campus store costs money and is closed. A bracket around the top row says OER is defined by '
         'permission, not price. Two dials, price and permission, point to different settings.'),
    bloom='Understand',
    objective='**explain** why a resource that costs nothing is not necessarily open, using the four cells of the price and permission matrix.',
    objective_plain='explain why a resource that costs nothing is not necessarily open, using the four cells of the price and permission matrix.',
    prereq=['The definition of an open educational resource from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).'],
    activities=[
        '**Explore (3 min).** Press each of the four zones and read the facts. Which zone surprises you most?',
        '**Quiz (3 min).** Press **Quiz Me** and place all four examples.',
        '**Apply (4 min).** Pick three resources you used this month and say which zone each belongs in. What would you need to check to be sure?',
    ],
    assessment=[
        ('A library e-book costs the reader nothing but forbids copying. Which zone is it in?', 'Free but closed.'),
        ('A lesson plan licensed CC BY 4.0 is posted on a teacher blog. Is it OER?', 'Yes. It is open, and the price does not matter.'),
        ('A print shop sells an open textbook at cost. Is the printed copy still OER?', 'Yes. The license grants the permissions even though the paper copy costs money.'),
    ],
    connection=('Open license is the first reusability metric in the ten-metric rubric. The rubric scores what you may do with a resource, '
                'never what it costs, which is why this matrix comes before any scoring.'),
    ref_nums=[(CH, [1, 3, 6, 7])],
    key_questions=['What does this cost the user?', 'What may the user do with it?'],
    misconceptions=['OER must cost nothing', 'Anything free to read is open', 'A resource that is sold in print cannot be OER'],
    good=['The dollar amounts in the chapter, such as the $15 printed copy, are illustrative and are left off the poster.'],
    verify=[(CH, 'A publisher\'s sample chapter marked "All rights reserved"'),
            (CH, 'An open textbook that a print shop sells at cost'),
            (CH, 'A commercial textbook from the campus store'),
            (CH, 'two separate dials')],
)

OPEN, OPEND = '#00796b', '#004d40'
CLOSED, CLOSEDD = '#6b7785', '#3d4856'


def dial(c, cx, cy, r, value, label, color):
    """Half-circle dial with a needle; value 0 (left) to 1 (right)."""
    c.path('M%s,%s A%s,%s 0 0 1 %s,%s' % (cx - r, cy, r, r, cx + r, cy), stroke=GRAYM, sw=10, cap='butt')
    c.path('M%s,%s A%s,%s 0 0 1 %s,%s' % (cx - r, cy, r, r, cx + r * math.cos(math.pi * (1 - value)),
                                           cy - r * math.sin(math.pi * (1 - value))), stroke=color, sw=10, cap='butt')
    a = math.pi * (1 - value)
    c.line(cx, cy, cx + (r - 10) * math.cos(a), cy - (r - 10) * math.sin(a), INK, 4)
    c.circle(cx, cy, 7, fill=INK)
    c.text(cx, cy + 28, label, 17, 'bold', INK, 'middle')


def cell(c, x, y, w, h, hue, hued, tint, icon, head, example, note, open_row):
    c.rect(x, y, w, h, fill=tint, stroke=hue, sw=3, rx=14)
    # icon column
    cx, cy = x + 52, y + 62
    c.circle(cx, cy, 36, fill=WHITE, stroke=hue, sw=3)
    ic_lock(c, cx, cy - 2, 20, open_=open_row, fill=hued)
    if open_row:
        ic_check(c, cx + 26, cy + 26, 13, GREEN)
    else:
        ic_cross(c, cx + 26, cy + 26, 13, RED)
    tx, tw_ = x + 106, w - 124
    c.text(tx, y + 42, head, 24, 'bold', hued, maxw=tw_)
    yy = c.para(tx, y + 76, example, tw_, 18, 1.25, 'bold', INK)
    c.para(tx, yy + 8, note, tw_, 18, 1.28, 'normal', INK)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Free Is Not Open', 'Price and permission are two separate dials. OER is defined by permission.')
    # dials, top right
    dial(c, 930, 78, 52, 0.08, 'Price', ORANGE)
    dial(c, 1100, 78, 52, 0.92, 'Permission', OPEN)

    x0, x1 = 250, 1160
    colw = (x1 - x0 - 16) / 2
    # column headers
    for i, (txt, ic) in enumerate((('Costs the user nothing', 0), ('Costs money', 1))):
        cx = x0 + i * (colw + 16)
        c.rect(cx, 138, colw, 40, fill=INK, rx=8)
        c.text(cx + colw / 2, 165, txt, 20, 'bold', WHITE, 'middle', maxw=colw - 20)
    # row headers
    rows = [(212, 'May edit and share', 'open license', True), (444, 'May not edit or share', 'all rights reserved', False)]
    for (ry, t, sub, op) in rows:
        hue = OPEN if op else CLOSED
        c.rect(30, ry, 200, 208, fill=hue, rx=14)
        ic_lock(c, 130, ry + 62, 30, open_=op, fill=WHITE)
        c.para(130, ry + 128, t, 170, 21, 1.2, 'bold', WHITE, 'middle')
        c.text(130, ry + 188, sub, 17, 'normal', WHITE, 'middle', maxw=180)
    # cells
    ch = 208
    ys = (212, 444)
    cw = colw
    cells = [
        (x0, ys[0], OPEN, OPEND, '#e3f4f1', 'Free and open', 'A lesson plan with a CC BY 4.0 license',
         'Costs nothing. You may edit and share it, with credit to the author.', True, 'free-open'),
        (x0 + colw + 16, ys[0], OPEN, OPEND, '#e3f4f1', 'Open, with a paid print copy', 'An open textbook that a print shop sells at cost',
         'The digital copy is free. Only the printed copy costs money, and you may still edit and share it.', True, 'open-paid-print'),
        (x0, ys[1], CLOSED, CLOSEDD, GRAYL, 'Free but closed', 'A publisher\'s sample chapter marked "All rights reserved"',
         'Costs nothing, but you may not edit or share it.', False, 'free-closed'),
        (x0 + colw + 16, ys[1], CLOSED, CLOSEDD, GRAYL, 'Paid and closed', 'A commercial textbook from the campus store',
         'Costs money and grants no permission to edit or share.', False, 'paid-closed'),
    ]
    items = []
    for (x, y, hue, hued, tint, head, ex, note, op, zid) in cells:
        cell(c, x, y, cw, ch, hue, hued, tint, None, head, ex, note, op)
        items.append(dict(id=zid, label=head, color=hue, box=(x, y, x + cw, y + ch)))
    # OER bracket around the top row
    c.rect(x0 - 8, 196, x1 - x0 + 16, 240, fill='none', stroke=OPEN, sw=3, rx=18, dash='10 7')
    c.chip(x0 + (x1 - x0) / 2, 184, 'OER: open, whatever the price', fill=OPEN, size=17, anchor='middle', h=28)
    c.text(40, 686, 'Illustrative examples drawn from Chapter 1. Open means the license grants permissions; it says nothing about quality.',
           15, 'normal', MUTED, maxw=1120)

    facts = {
        'free-open': ('Free and open: costs nothing and grants permissions.',
                      ['Chapter 1 example: a lesson plan with a CC BY license.',
                       'The user pays nothing and may edit and share it, with credit to the author.',
                       'It passes both OER tests: an educational resource, under an open license.']),
        'open-paid-print': ('Open, with a paid print copy: the license, not the price, makes it OER.',
                            ['Chapter 1 example: an open textbook that a print shop sells at cost.',
                             'The digital copy is free; the printed copy costs money.',
                             'The license still lets a campus print shop make copies without asking the publisher.',
                             'It is OER. "OER must cost nothing" is a common misunderstanding.']),
        'free-closed': ('Free but closed: no price, but no permission to edit or share.',
                        ['Chapter 1 example: a publisher\'s sample chapter marked "All rights reserved".',
                         'You may read it, but copyright\'s default of all rights reserved still applies.',
                         'It is not OER because it has no open license.']),
        'paid-closed': ('Paid and closed: costs money and grants no permissions.',
                        ['Chapter 1 example: a commercial textbook from the campus store.',
                         'The student pays and still may not edit or share it.',
                         'Many resources you meet in school sit in this zone.']),
    }
    for it in items:
        it['summary'], it['facts'] = facts[it['id']]

    quiz = [
        dict(question='Which zone holds a publisher\'s sample chapter marked "All rights reserved"?', correct_zone='free-closed',
             explanation='It costs nothing, but all rights are reserved.'),
        dict(question='Which zone holds a lesson plan licensed CC BY 4.0 that costs the user nothing?', correct_zone='free-open',
             explanation='It is free and open.'),
        dict(question='Which zone shows an open resource where only the printed copy costs money?', correct_zone='open-paid-print',
             explanation='The license grants the permissions, so the paid print copy is still OER.'),
        dict(question='Which zone holds a commercial textbook from the campus store?', correct_zone='paid-closed',
             explanation='It costs money and grants no permissions.'),
    ]
    return c, items, quiz
