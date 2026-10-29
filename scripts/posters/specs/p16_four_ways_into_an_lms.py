"""Poster 16: Link, Embed, Import, or LTI: Four Ways Into an LMS (Chapter 10, grid, 4 zones)."""
from svgkit import *

CH = '10-portability-reuse'

META = dict(
    slug='four-ways-into-an-lms',
    title='Link, Embed, Import, or LTI: Four Ways Into an LMS',
    chapter=CH,
    overlay='grid',
    topic='Four ways to bring an OER into a learning management system',
    desc='The same resource moving four ways toward the same generic learning management system: a link, an embed, a Common Cartridge import, and an LTI tool.',
    intro=('Teachers constantly ask how to put a resource into their course, and the wrong method means a broken embed or a gradebook that never updates. This poster shows the same resource and the same generic learning management system (LMS) in four zones. '
           'A link opens the resource at its own address. An embed shows it inside your course page. A Common Cartridge import brings a single compressed file with a manifest into the LMS. '
           'An LTI tool opens inside the course but runs on another company\'s server and can send a score back to the gradebook. The arrows show the difference: one-way for the first three, two-way for LTI. '
           'The LTI zone carries a small shield because passing learner information raises the privacy questions of Chapter 13. A footer names the barrier that stops all four, platform lock-in.'),
    alt=('Four zones, each showing a resource and a generic learning management system. Link: students open the resource at its own address; one arrow runs from the course page to the resource, which stays on its own host. '
         'Embed: the resource appears on the course page through a frame; the arrow runs from the resource into the page; it needs a host that allows framing. '
         'Common Cartridge import: a whole unit is copied into the LMS as one compressed file with a manifest; one arrow into the LMS. '
         'LTI tool: an external tool opens inside the LMS and can send results back to the gradebook; a two-way arrow and a shield for learner privacy; the tool runs on another company\'s server. '
         'A footer says platform lock-in stops all four.'),
    bloom='Apply',
    objective='**choose** the right way to bring a resource into an LMS for each of four teacher needs.',
    objective_plain='choose the right way to bring a resource into an LMS for each of four teacher needs.',
    prereq=['LMS import, Common Cartridge, and LTI from [Chapter 10](../../chapters/10-portability-reuse/index.md).'],
    activities=[
        '**Explore (3 min).** Press each zone. Which arrows are one-way, and which is two-way?',
        '**Quiz (3 min).** Press **Quiz Me** and match four teacher needs to the zones.',
        '**Plan (4 min).** Think of a resource you use. Which method would you choose, and what would you test in a real LMS first?',
    ],
    assessment=[
        ('You want an external quiz tool to send each student\'s score to the gradebook. Which method?', 'An LTI tool.'),
        ('You want a simulation to appear on your course page. Which method?', 'Embed.'),
        ('You want colleagues with a different LMS to receive the same unit. Which method?', 'Common Cartridge import.'),
    ],
    connection='Portability is metric 10. The chapter\'s own objective is to choose among exactly these four methods for a given need.',
    ref_nums=[(CH, [1, 6, 7, 8])],
    key_questions=['Where does the resource live afterward?', 'Does anything need to come back to the gradebook?'],
    misconceptions=['A link that fails is an embedding problem', 'LTI and a link do the same thing'],
    good=['The poster draws a generic LMS and no vendor logos. 1EdTech is named as the standards group.'],
    verify=[(CH, 'Link (students open the resource at its own address)'),
            (CH, 'Embed (the resource appears on the course page through a frame)'),
            (CH, 'Common Cartridge import (a whole unit is copied into the LMS as a package)'),
            (CH, 'LTI tool (an external tool opens inside the LMS and can send results back)'),
            (CH, 'An LTI tool looks like part of the course and runs on another company\'s server'),
            (CH, 'a single compressed file that holds the content together with a manifest')],
)

HUES = [('#1d4f86', '#e6eef8'), ('#00796b', '#e3f4f1'), ('#8a5a00', '#fdf1d6'), ('#573379', '#efe6f6')]
COLS = [
    ('link', 'Link', 'Students open the resource at its own address.', 'One-way', 'The resource stays on its own host.',
     'Needs a good link: permanent, direct, and working for the person who receives it.'),
    ('embed', 'Embed', 'The resource appears on your course page through a frame.', 'One-way', 'The page shows it without leaving your course.',
     'Needs a host that allows framing, and no login.'),
    ('cartridge', 'Common Cartridge import', 'A whole unit is copied into the LMS as a package.', 'One-way', 'A single compressed file with a manifest.',
     'The common exchange form between LMSs. Not every resource offers one.'),
    ('lti', 'LTI tool', 'An external tool opens inside the LMS and can send results back.', 'Two-way', 'It runs on another company\'s server.',
     'Passes learner information, which raises the privacy questions of Chapter 13.'),
]


def lms(c, x, y, w, h, hue, inner=None):
    c.rect(x, y, w, h, fill=WHITE, stroke=INK, sw=3, rx=8)
    c.rect(x, y, w, 20, fill=INK, rx=8)
    c.rect(x, y + 10, w, 10, fill=INK)
    for k in range(3):
        c.circle(x + 12 + k * 12, y + 10, 3, fill=WHITE)
    c.line(x + 12, y + 34, x + w - 12, y + 34, GRAYM, 3)
    c.line(x + 12, y + 46, x + w - 40, y + 46, GRAYM, 3)


def res(c, x, y, w, h, hue):
    c.rect(x, y, w, h, fill=WHITE, stroke=hue, sw=3, rx=6)
    c.rect(x, y, w, 16, fill=hue, rx=6)
    c.rect(x, y + 8, w, 8, fill=hue)
    c.line(x + 8, y + 28, x + w - 8, y + 28, GRAYM, 3)
    c.line(x + 8, y + 38, x + w - 20, y + 38, GRAYM, 3)


def scene(c, kind, x, w, y, hue):
    cx = x + w / 2
    # resource (left or bottom) and LMS (right), 100 wide each
    lx, rx_ = x + 16, x + w - 16 - 112
    if kind == 'link':
        lms(c, rx_, y, 112, 96, hue)
        c.rect(rx_ + 14, y + 58, 52, 20, fill=hue, rx=10)
        c.text(rx_ + 40, y + 73, 'link', 13, 'bold', WHITE, 'middle')
        res(c, lx, y + 10, 92, 76, hue)
        c.rect(lx + 8, y - 6, 76, 14, fill=WHITE, stroke=hue, sw=2, rx=7)
        c.arrow(rx_ + 66, y + 68, lx + 94, y + 54, hue, 4, 12)
    elif kind == 'embed':
        lms(c, rx_ - 22, y, 134, 100, hue)
        res(c, rx_ + 2, y + 40, 82, 54, hue)
        c.rect(rx_ + 2, y + 40, 82, 54, fill='none', stroke=hue, sw=2.5, rx=6, dash='5 4')
        res(c, lx, y + 14, 78, 66, hue)
        c.arrow(lx + 80, y + 48, rx_ - 2, y + 62, hue, 4, 12)
    elif kind == 'cartridge':
        lms(c, rx_, y, 112, 96, hue)
        # compressed package with manifest
        c.rect(lx, y + 14, 84, 70, fill='#ffe8b0', stroke=INK, sw=3, rx=6)
        c.line(lx + 42, y + 14, lx + 42, y + 84, INK, 3, '4 4')
        c.rect(lx + 52, y + 26, 24, 34, fill=WHITE, stroke=INK, sw=2)
        for k in range(3):
            c.line(lx + 56, y + 34 + k * 8, lx + 72, y + 34 + k * 8, GRAYM, 2.5)
        c.arrow(lx + 88, y + 50, rx_ + 6, y + 50, hue, 4, 12)
    else:
        lms(c, rx_, y, 112, 96, hue)
        c.rect(rx_ + 10, y + 58, 40, 28, fill='#efe6f6', stroke=hue, sw=2, rx=4)
        c.path('M%s,%s l8,-10 l8,6 l10,-14' % (rx_ + 16, y + 80), stroke=hue, sw=3)
        c.rect(lx, y + 18, 82, 60, fill=WHITE, stroke=hue, sw=3, rx=6, dash='6 4')
        c.text(lx + 41, y + 52, 'tool', 15, 'bold', hue, 'middle')
        c.arrow(lx + 86, y + 50, rx_ - 4, y + 50, hue, 4, 12, both=True)
        ic_shield(c, cx, y - 2, 13, TEAL)


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'Link, Embed, Import, or LTI: Four Ways Into an LMS', 'The same resource, the same generic LMS, four ways in. The arrows show which way information flows.')
    n, gap = 4, 14
    x0, x1, y0, y1 = 30, 1170, 108, 612
    w = (x1 - x0 - gap * (n - 1)) / n
    items = []
    for i, (zid, name, does, flow, keep, needs) in enumerate(COLS):
        hue, tint = HUES[i]
        x = x0 + i * (w + gap)
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 52, fill=hue, rx=14)
        c.rect(x, y0 + 28, w, 24, fill=hue)
        c.text(x + 16, y0 + 34, name, 22, 'bold', WHITE, maxw=w - 30)
        c.rect(x + 10, y0 + 64, w - 20, 150, fill=tint, rx=10)
        scene(c, zid, x + 10, w - 20, y0 + 92, hue)
        c.chip(x + w / 2, y0 + 214 - 14, flow + ' arrow' if False else flow, fill=hue, size=14, h=24, anchor='middle')
        c.text(x + 16, y0 + 258, 'WHAT IT DOES', 12, 'bold', hue, spacing='1')
        yy = c.para(x + 16, y0 + 282, does, w - 32, 17, 1.22, 'bold', INK, maxlines=4)
        c.text(x + 16, yy + 12, 'WHAT STAYS', 12, 'bold', hue, spacing='1')
        yy = c.para(x + 16, yy + 36, keep, w - 32, 16, 1.22, 'normal', INK, maxlines=3)
        c.text(x + 16, yy + 12, 'WHAT IT NEEDS', 12, 'bold', hue, spacing='1')
        c.para(x + 16, yy + 36, needs, w - 32, 16, 1.22, 'normal', INK, maxlines=4)
        items.append(dict(id=zid, label=name, color=hue, box=(x, y0, x + w, y1),
                          summary=does, facts=[does, 'Information flow: %s.' % flow.lower(), keep, needs]))
    # lock-in footer
    c.rect(30, 626, 1140, 52, fill=GRAYL, stroke=GRAY, sw=2.5, rx=12)
    ic_lock(c, 62, 652, 16, fill=INK)
    c.text(92, 658, 'Platform lock-in is the barrier that stops all four: leaving a platform should not cost you the resource.', 18, 'bold', INK, maxw=1060)
    quiz = [
        dict(question='Which method lets an external quiz tool send each student\'s score to the LMS gradebook?', correct_zone='lti', explanation='LTI lets the tool exchange information with the LMS.'),
        dict(question='Which method makes a simulation appear on your course page through a frame?', correct_zone='embed', explanation='A frame shows the simulation inside the page.'),
        dict(question='Which method copies a whole unit, with pages, quizzes, and files, into your course as one package?', correct_zone='cartridge', explanation='A package carries the whole unit into the LMS.'),
        dict(question='Which method just lets students open one reading in a new tab at its own address?', correct_zone='link', explanation='A link opens the resource at its own address.'),
    ]
    return c, items, quiz
