"""Poster 28: Component in a Box (Chapter 18, callout, 7 markers). The artwork carries no text."""
from svgkit import *

CH = '18-components-publishing-oer'

META = dict(
    slug='component-in-a-box',
    title='Component in a Box',
    chapter=CH,
    overlay='callout',
    layout='dual-panel',
    topic='What goes into a packaged, reusable component',
    desc='An exploded view of a cardboard box holding the six parts of the Chapter 18 quiz package, with a broken link outside the box and three finished boxes for Watershed Basics v1.1.',
    intro=('Chapter 18 turns improved resources into reusable components, and packaging is the concrete step that makes the lift-out test from Chapter 9 and the portability checks from Chapter 10 pass. '
           'This poster is an exploded view of the quiz package watershed-quiz. Six parts float above the box: the page itself (index.html), the script it needs kept inside the folder (quiz.js), '
           'a README that says what the component is and how to use it, a license file, a metadata file, and an image folder. Everything the component needs travels with it. '
           'Outside the box a dotted line runs from the page to a folder elsewhere, with a cross on it: the broken link that packaging prevents. '
           'The seventh marker sits on the three finished boxes of Watershed Basics v1.1, the reading, the quiz, and the simulation. The artwork has no text, and the file names come from the overlay.'),
    alt=('An exploded view. A cardboard box labelled with a folder shape; six parts float above it with dotted lines into the box: a page (index.html), a script (quiz.js) that stays inside the folder, '
         'a README, a license file, a metadata file, and an image folder (img). Outside the box, a dotted line runs from the page to a separate folder far away with a cross on it, showing the broken link that packaging prevents. '
         'At the lower right, three finished boxes stand for the reading, the quiz, and the simulation of Watershed Basics v1.1.'),
    bloom='Understand',
    objective='**list** the files in a packaged component, **say** what each is for, and **explain** why a link that leaves the folder breaks the package.',
    objective_plain='list the files in a packaged component, say what each is for, and explain why a link that leaves the folder breaks the package.',
    prereq=['Standalone components from [Chapter 9](../../chapters/09-modularity-metadata/index.md) and packaging from [Chapter 18](../../chapters/18-components-publishing-oer/index.md).'],
    activities=[
        '**Explore (4 min).** Hover over markers 1 to 7. Which part would stop a reuser from knowing what they may do if it were missing?',
        '**Quiz (3 min).** Press **Quiz** and find each part from its description.',
        '**Inspect (3 min).** Open a folder of yours. Which of the six parts are missing, and where do its links point?',
    ],
    assessment=[
        ('Where must the script a page needs be kept?', 'Inside the folder, so it travels with the component.'),
        ('Why does the box include a license file and a metadata file?', 'So a reuser knows what they may do and a catalog can find and describe it.'),
        ('What should links inside a package be?', 'Complete addresses, or point to files inside the package.'),
    ],
    connection='Packaging ties together license, metadata, and portability. A component with every part passes the lift-out test and embeds without edits.',
    ref_nums=[(CH, [6, 7, 9, 10])],
    key_questions=['Does everything it needs travel with it?', 'Do all links stay inside the folder or use complete addresses?'],
    misconceptions=['A link to a shared folder is fine', 'A license can be added later'],
    good=['This book\'s own MicroSim folders follow the same idea: each has a main.html, an index.md, and its own script, but they also load the shared overlay libraries from docs/sims/shared-libs.'],
    verify=[(CH, 'index.html'), (CH, 'quiz.js'), (CH, 'README.md'), (CH, 'LICENSE.txt'), (CH, 'metadata.json'),
            (CH, 'The script the page needs, kept inside the folder'),
            (CH, '*Watershed Basics v1.1* has three components')],
)

BOXC, BOXD = '#c8a06a', '#8d6e4b'


def file_icon(c, k, cx, cy):
    """Small file pictures, about 70 px across."""
    c.circle(cx, cy, 44, fill=WHITE, stroke=INK, sw=3)
    if k == 0:   # page
        ic_doc(c, cx - 20, cy - 26, 40, 52, label=None, fold=10)
        c.rect(cx - 12, cy - 6, 24, 14, fill='#d6e6f7')
        ic_lines(c, cx - 12, cy + 14, 24, 2, gap=6)
    elif k == 1:  # script with braces
        ic_doc(c, cx - 20, cy - 26, 40, 52, label=None, fold=10)
        c.path('M%s,%s q-6,0 -6,6 v4 q0,4 -4,4 q4,0 4,4 v4 q0,6 6,6' % (cx - 4, cy - 12), stroke=ORANGE, sw=3.5)
        c.path('M%s,%s q6,0 6,6 v4 q0,4 4,4 q-4,0 -4,4 v4 q0,6 -6,6' % (cx + 6, cy - 12), stroke=ORANGE, sw=3.5)
    elif k == 2:  # readme: page with an info mark
        ic_doc(c, cx - 20, cy - 26, 40, 52, label=None, fold=10)
        c.circle(cx, cy - 4, 10, fill=Q)
        c.circle(cx, cy - 10, 2, fill=WHITE)
        c.line(cx, cy - 6, cx, cy + 2, WHITE, 3)
        ic_lines(c, cx - 12, cy + 14, 24, 2, gap=6)
    elif k == 3:  # license: page with seal
        ic_doc(c, cx - 20, cy - 26, 40, 52, label=None, fold=10)
        ic_star(c, cx, cy + 2, 12, ORANGE)
        c.circle(cx, cy + 2, 14, fill='none', stroke=INK, sw=2)
    elif k == 4:  # metadata: tag
        c.poly([(cx - 26, cy - 4), (cx - 8, cy - 22), (cx + 26, cy - 22), (cx + 26, cy + 22), (cx - 8, cy + 22)], fill='#e8dcf3', stroke=INK, sw=2.5)
        c.circle(cx - 8, cy, 5, fill=INK)
        ic_lines(c, cx + 2, cy - 8, 18, 3, gap=7)
    else:  # picture folder
        ic_folder(c, cx - 28, cy - 18, 56, 40, fill='#fff3b0')
        c.poly([(cx - 16, cy + 14), (cx - 4, cy), (cx + 4, cy + 8), (cx + 12, cy - 2), (cx + 20, cy + 14)], fill=GREEN)


def draw():
    c = Canvas(1000, 650)
    # exploded parts above the box
    xs = [170, 290, 410, 530, 650, 770]
    ys = [200, 150, 122, 122, 150, 200]
    bx0, bx1, by0, by1 = 120, 840, 340, 530
    # box body, with the lid flaps open
    c.poly([(bx0, by0 + 20), (bx0 + 40, by0 - 24), (bx1 - 40, by0 - 24), (bx1, by0 + 20)], fill='#d9b987', stroke=BOXD, sw=3)
    c.rect(bx0, by0 + 20, bx1 - bx0, by1 - by0 - 20, fill=BOXC, stroke=BOXD, sw=4, rx=6)
    c.rect(bx0 + 20, by0 + 40, 140, 40, fill='#e8d3a8', stroke=BOXD, sw=2, rx=3)
    ic_folder(c, bx1 - 120, by0 + 52, 70, 50, fill='#fff3b0')
    c.line(bx0 + 20, by0 + 20, bx1 - 20, by0 + 20, BOXD, 3)
    c.rect(480 - 22, by0 + 20, 44, by1 - by0 - 20, fill='#e6cf9d', opacity=0.9)
    c.rect(bx0 + 20, by1 - 54, 110, 32, fill='#e8d3a8', stroke=BOXD, sw=2, rx=3)
    c.arrow(bx0 + 40, by1 - 38, bx0 + 110, by1 - 38, BOXD, 4, 10)
    for k, (x, y) in enumerate(zip(xs, ys)):
        c.line(x, y + 44, x, by0 - 8, GRAY, 2.5, '4 5')
        c.arrow(x, by0 - 22, x, by0 - 4, GRAY, 3, 9)
        file_icon(c, k, x, y)
    # broken link: dotted line from the page to a folder outside the box, with a cross
    c.path('M%s,%s C%s,%s %s,%s %s,%s' % (xs[0] - 40, ys[0] + 30, 120, 230, 80, 250, 66, 292), stroke=INK, sw=3.5, dash='3 8')
    ic_folder(c, 24, 296, 84, 58, fill=GRAYL, stroke=GRAY)
    ic_cross(c, 30, 322, 16, RED)
    # finished boxes, below
    for k, (bxk, kind) in enumerate(((120, 'read'), (390, 'quiz'), (660, 'sim'))):
        x, y, w, h = bxk, 576, 220, 60
        c.rect(x, y, w, h, fill=BOXC, stroke=BOXD, sw=3, rx=6)
        c.rect(x, y, w, 12, fill='#d9b987', stroke=BOXD, sw=2)
        c.rect(x + w / 2 - 14, y, 28, h, fill='#e6cf9d')
        ic_check(c, x + w - 24, y + 36, 11, GREEN)
        cx_ = x + 54
        if kind == 'read':
            ic_doc(c, cx_ - 14, y + 14, 28, 40, label=None, fold=8)
        elif kind == 'quiz':
            ic_doc(c, cx_ - 14, y + 14, 28, 40, label=None, fold=8)
            c.rect(cx_ - 8, y + 28, 6, 6, fill=WHITE, stroke=INK, sw=1.5)
            c.rect(cx_ - 8, y + 38, 6, 6, fill=WHITE, stroke=INK, sw=1.5)
        else:
            c.rect(cx_ - 20, y + 14, 40, 34, fill=WHITE, stroke=INK, sw=2, rx=3)
            c.path('M%s,%s l8,-12 l8,6 l8,-14' % (cx_ - 14, y + 42), stroke=Q, sw=3)
    items = [
        dict(id=1, label='index.html', at=(xs[0] - 56, ys[0] - 36), color=Q, radius=2.8, panel='left',
             hint='A page with a blue picture box and lines, the first of the six floating parts.',
             description='The quiz page itself. A reuser opens this file to see and use the component. All links in it must be complete addresses or point to files inside the folder.',
             tip='The dotted line leaving this page is the broken link that packaging prevents.'),
        dict(id=2, label='quiz.js', at=(xs[1] - 56, ys[1] - 36), color=ORANGE, radius=2.8, panel='left',
             hint='A page with two orange curly braces.',
             description='The script the page needs, kept inside the folder. If it lived in a sibling folder, it would not travel with the component.',
             tip='A script path that points outside the folder is the classic broken package.'),
        dict(id=3, label='README.md', at=(xs[2] - 56, ys[2] - 36), color=Q, radius=2.8, panel='left',
             hint='A page with a round information mark.',
             description='What the component is, how to embed it, and how to credit it.',
             tip='Nothing explains a component without a README.'),
        dict(id=4, label='LICENSE.txt', at=(xs[3] + 56, ys[3] - 36), color=R, radius=2.8, panel='right',
             hint='A page with an orange seal.',
             description='The license text or a link to it, so a reuser knows what they may do.',
             tip='A resource with no license cannot be reused with confidence.'),
        dict(id=5, label='metadata.json', at=(xs[4] + 56, ys[4] - 36), color=R, radius=2.8, panel='right',
             hint='A purple tag with a hole and short lines.',
             description='The metadata record of Chapter 9 in a form a program can read, so a catalog can find and describe the component.',
             tip='Metadata is for people and for machines.'),
        dict(id=6, label='img/', at=(xs[5] + 56, ys[5] - 36), color=GREEN, radius=2.8, panel='right',
             hint='A yellow folder with a green hill picture.',
             description='The images the component uses, kept inside the package with complete addresses or paths inside the folder.',
             tip='Each image should have its own caption and alt text.'),
        dict(id=7, label='Three finished boxes for Watershed Basics v1.1', at=(560, 572), color=GREEN, radius=2.8, panel='right',
             hint='Three closed boxes in a row at the bottom, each with a green check.',
             description='After splitting, Watershed Basics v1.1 has three components: the reading, the quiz, and the simulation. Each is packaged in its own box with its own license and metadata.',
             tip='Ready means every file is present and every link works from anywhere.'),
    ]
    return c, items, []
