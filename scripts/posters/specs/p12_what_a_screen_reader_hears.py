"""Poster 12: What a Screen Reader Hears (Chapter 7, grid, 2 zones)."""
from svgkit import *

CH = '07-accessibility'

META = dict(
    slug='what-a-screen-reader-hears',
    title='What a Screen Reader Hears',
    chapter=CH,
    overlay='grid',
    topic='How headings and alt text are announced by a screen reader',
    desc='A page on the left and speech bubbles on the right show what a screen reader announces for a heading, an image with good alt text, an image with no alt attribute, and an image with an empty alt attribute.',
    intro=('Hearing the result is more persuasive than reading a rule. This poster shows four rows from the Chapter 7 worked example. On the left is what a sighted reader sees. On the right is what a screen reader typically announces. '
           'The same photograph appears in every image row, so the only difference is the markup. A real heading is announced with its level. Good alt text is read as the image\'s description. '
           'No alt attribute makes the reader announce the file name, which is useless. An empty alt attribute is announced as nothing, which is correct only for a decorative image. '
           'Wording varies between screen reader programs, and the poster shows no real program.'),
    alt=('Two columns, what is seen and what is heard, in four rows. Row 1: a heading "How water moves" at level 2; the screen reader says "Heading level 2, How water moves". '
         'Row 2: a photograph of a river with alt text "A river meandering through a valley"; it says "Image, A river meandering through a valley". '
         'Row 3: the same photograph with no alt attribute; it says "Image, river.png", reading the file name. '
         'Row 4: the same photograph with an empty alt attribute; it says nothing, because the image is skipped, which is correct only for a decorative image.'),
    bloom='Understand',
    objective='**predict** what a screen reader announces for a heading and for images with good, missing, and empty alt text.',
    objective_plain='predict what a screen reader announces for a heading and for images with good, missing, and empty alt text.',
    prereq=['Alt text, decorative images, and heading structure from [Chapter 7](../../chapters/07-accessibility/index.md).'],
    activities=[
        '**Explore (3 min).** Press the seen column, then the heard column. Which row would frustrate a blind learner most?',
        '**Quiz (3 min).** Press **Quiz Me** and answer which zone shows what is seen and what is heard.',
        '**Listen (4 min).** Turn on a screen reader on your computer for five minutes and visit a page you teach from. Which row from this poster did you meet?',
    ],
    assessment=[
        ('What does a screen reader say for an image with no alt attribute?', 'Often the file name, such as "Image, river.png", which is useless.'),
        ('When is an empty alt attribute correct?', 'Only for a decorative image.'),
        ('How does a screen reader announce a real heading?', 'With its level, such as "Heading level 2, How water moves".'),
    ],
    connection='Five minutes with a screen reader changes how you write alt text. This poster gives a taste of that without any software, and supports the accessibility metric.',
    ref_nums=[(CH, [3, 7, 10])],
    key_questions=['What would I hear?', 'Is anything missing?'],
    misconceptions=['An image with no alt attribute is the same as an image with an empty one', 'Every image needs a long alt text'],
    good=['Announcement wording varies between screen reader programs. The poster shows typical announcements and no real program.'],
    verify=[(CH, '"Heading level 2, How water moves"'),
            (CH, '"Image, A river meandering through a valley"'),
            (CH, '"Image, river.png"'),
            (CH, 'The image is skipped, which is correct only for a decorative image')],
)

SEE, SEED = '#1d4f86', '#e6eef8'
HEAR, HEARD = '#573379', '#efe6f6'


def river(c, x, y, w=120, h=76):
    c.rect(x, y, w, h, fill='#bfe3f5', stroke=INK, sw=2.5)
    c.poly([(x, y + h * .62), (x + w * .3, y + h * .32), (x + w * .55, y + h * .58), (x + w * .8, y + h * .28), (x + w, y + h * .5), (x + w, y + h), (x, y + h)],
           fill='#7fb87a')
    c.path('M%s,%s Q%s,%s %s,%s T%s,%s' % (x + w * .35, y + h, x + w * .6, y + h * .82, x + w * .45, y + h * .66, x + w * .7, y + h * .54),
           stroke='#2f7fc1', sw=7, cap='round')
    c.rect(x, y, w, h, fill='none', stroke=INK, sw=2.5)


ROWS = [
    ('heading', 'A heading that reads "How water moves"', 'Heading level 2, How water moves', 'Real headings are announced with their level.'),
    ('alt', 'An image with alt text "A river meandering through a valley"', 'Image, A river meandering through a valley', 'The alt text does its job.'),
    ('none', 'An image with no alt attribute (the file is river.png)', 'Image, river.png', 'The file name is read, which is useless.'),
    ('empty', 'An image with an empty alt attribute', None, 'The image is skipped, which is correct only for a decorative image.'),
]


def draw():
    c = Canvas(1200, 700)
    title_block(c, 'What a Screen Reader Hears', 'The same page, four ways. What you see on the left is not what a screen reader announces on the right.')
    y0, y1 = 108, 642
    lx, lw = 30, 560
    rx, rw = 610, 560
    for (x, w, hue, tint, head, ic) in ((lx, lw, SEE, SEED, 'What is seen', ic_eye), (rx, rw, HEAR, HEARD, 'What is heard', ic_speaker)):
        c.rect(x, y0, w, y1 - y0, fill=WHITE, stroke=hue, sw=3, rx=14)
        c.rect(x, y0, w, 48, fill=hue, rx=14)
        c.rect(x, y0 + 26, w, 22, fill=hue)
        c.circle(x + 30, y0 + 24, 17, fill=WHITE)
        ic(c, x + 30, y0 + 24, 12, hue)
        c.text(x + 58, y0 + 32, head, 23, 'bold', WHITE)
    rh = 118
    for i, (kind, seen, heard, why) in enumerate(ROWS):
        y = y0 + 62 + i * (rh + 3)
        c.rect(lx + 10, y, lw - 20, rh - 8, fill=SEED, rx=10)
        c.rect(rx + 10, y, rw - 20, rh - 8, fill=HEARD, rx=10)
        c.circle(lx + 28, y + 22, 13, fill=SEE)
        c.text(lx + 28, y + 28, str(i + 1), 15, 'bold', WHITE, 'middle')
        c.circle(rx + 28, y + 22, 13, fill=HEAR)
        c.text(rx + 28, y + 28, str(i + 1), 15, 'bold', WHITE, 'middle')
        # seen side
        if kind == 'heading':
            c.text(lx + 56, y + 62, 'How water moves', 32, 'bold', INK, maxw=lw - 80)
            c.line(lx + 56, y + 74, lx + 330, y + 74, GRAYM, 3)
        else:
            river(c, lx + 56, y + 14, 130, 82)
            c.para(lx + 204, y + 36, seen, lw - 230, 16, 1.25, 'bold', INK, maxlines=4)
        # heard side
        if heard:
            ic_bubble(c, rx + 64, y + 12, rw - 100, 54, fill=WHITE, stroke=HEAR)
            c.text(rx + 84, y + 47, '“%s”' % heard, 20, 'bold', INK, maxw=rw - 140, minsize=14)
        else:
            c.rect(rx + 64, y + 12, rw - 100, 54, fill=WHITE, stroke=GRAY, sw=2.5, rx=10, dash='7 6')
            c.text(rx + 84, y + 47, '(nothing is announced)', 20, 'bold', MUTED, maxw=rw - 140)
        c.para(rx + 64, y + 86, why, rw - 100, 15, 1.2, 'normal', MUTED, maxlines=2)
    c.text(40, 672, 'Typical announcements. Wording varies between screen reader programs, and some read the file name in other ways.', 15, 'normal', MUTED, maxw=1120)

    items = [
        dict(id='seen', label='What is seen', color=SEE, box=(lx, y0, lx + lw, y1),
             summary='Four rows a sighted reader sees: a heading and the same photograph with three kinds of alt markup.',
             facts=['Row 1: a heading that reads "How water moves".', 'Row 2: the photograph with alt text "A river meandering through a valley".',
                    'Row 3: the same photograph with no alt attribute; the file is river.png.', 'Row 4: the same photograph with an empty alt attribute.',
                    'The picture looks identical in rows 2 to 4. Only the markup differs.']),
        dict(id='heard', label='What is heard', color=HEAR, box=(rx, y0, rx + rw, y1),
             summary='What a screen reader typically announces for each of the four rows.',
             facts=['Row 1: "Heading level 2, How water moves". Real headings are announced with their level.',
                    'Row 2: "Image, A river meandering through a valley". The alt text does its job.',
                    'Row 3: "Image, river.png". The file name is read, which is useless.',
                    'Row 4: nothing. The image is skipped, which is correct only for a decorative image.']),
    ]
    quiz = [
        dict(question='Which zone shows what a screen reader announces, such as "Heading level 2, How water moves"?', correct_zone='heard', explanation='The right-hand column is what is heard.'),
        dict(question='Which zone shows the page as a sighted reader sees it, with the same river photograph in three rows?', correct_zone='seen', explanation='The left-hand column is what is seen.'),
        dict(question='Which zone shows the useless announcement "Image, river.png" for an image with no alt attribute?', correct_zone='heard', explanation='The file name is read, which is useless.'),
        dict(question='Which zone shows an image with an empty alt attribute that looks exactly like the others?', correct_zone='seen', explanation='Only the markup differs, so the picture looks the same.'),
    ]
    return c, items, quiz
