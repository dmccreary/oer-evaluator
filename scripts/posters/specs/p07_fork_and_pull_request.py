"""Poster 7: Fork and Pull Request: Two Lanes, Seven Steps (Chapter 4, callout, 7 markers). No text in the artwork."""
from svgkit import *

CH = '04-open-formats-version-control'

META = dict(
    slug='fork-and-pull-request',
    title='Fork and Pull Request: Two Lanes, Seven Steps',
    chapter=CH,
    overlay='callout',
    layout='top-bottom',
    topic='The fork and pull request workflow for improving someone else\'s resource',
    desc='A two-lane diagram of the seven steps for improving a resource you do not own: find it, fork it, change your copy, propose the change, review, respond, and merge.',
    intro=('Git vocabulary is the hardest part of Chapter 4, and this poster shows what a list cannot: whose copy each step happens in. '
           'The top lane is the original repository and its maintainer. The bottom lane is your own copy. The seven steps run left to right, and the arrows cross between the lanes at the fork, the pull request, and the merge. '
           'A faint dotted branch shows the other ending, a declined pull request. The pictures are physical: a photocopied binder for the fork, a sticky note for the pull request, and a rubber stamp for the merge.'),
    alt=('Two horizontal lanes. The top lane is the original repository and its maintainer. The bottom lane is your own copy. Seven numbered steps run from left to right. '
         '1 Find the repository of the resource you want to improve, in the top lane. 2 Fork it to make your own copy: an arrow crosses down to a photocopied binder in the bottom lane. '
         '3 Make your change in your copy and save it with a message. 4 Open a pull request, a sticky note on an arrow that crosses up to the top lane. '
         '5 The maintainer reads the pull request and leaves comments. 6 You answer the comments with more changes in your copy. '
         '7 The maintainer merges the pull request, shown as a rubber stamp. A faint dotted branch from step 5 ends in a cross, the declined pull request.'),
    bloom='Understand',
    objective='**order** the seven steps of the fork and pull request workflow and **say** in which copy each step happens.',
    objective_plain='order the seven steps of the fork and pull request workflow and say in which copy each step happens.',
    prereq=['The meaning of a repository, a fork, and a pull request from [Chapter 4](../../chapters/04-open-formats-version-control/index.md).'],
    activities=[
        '**Explore (3 min).** Hover over markers 1 to 7 in order. Which steps happen in the top lane and which in the bottom lane?',
        '**Quiz (3 min).** Press **Quiz** and find each step from its description.',
        '**Discuss (4 min).** What does the faint dotted branch show, and what would you do after a declined pull request?',
    ],
    assessment=[
        ('Where do you make your change?', 'In your own copy, the fork, never in the original.'),
        ('Can a pull request be sent before the change is made?', 'No. A pull request needs a change to propose.'),
        ('Must the maintainer accept every pull request?', 'No. A maintainer may decline it.'),
    ],
    connection='This is how an improved resource finds its way back to its author, which matters again in Chapter 15 (improving a resource) and Chapter 18 (publishing components).',
    ref_nums=[(CH, [3, 8, 9])],
    key_questions=['Whose copy is this step in?', 'What does the maintainer see?'],
    misconceptions=['You edit the original repository directly', 'A pull request is sent before the change is made', 'The maintainer must accept every pull request'],
    good=['The drawing is a generic interface with no screenshots or logos of a real code-hosting site.',
          'The sequence shows the successful path. The faint branch is the other ending.'],
    verify=[(CH, '| 2 | Fork the repository to make your own copy. | You change your copy, not the original. |'),
            (CH, '| 4 | Open a pull request that proposes your change to the original repository. |'),
            (CH, '| 7 | The maintainer merges the pull request into the original. |'),
            (CH, 'a maintainer may also decline a pull request')],
)

TOP, TOPD, TOPT = '#1d4f86', '#143a63', '#e6eef8'
BOT, BOTD, BOTT = '#a85d00', '#6e3d00', '#fdf1d6'
LY1, LY2 = (62, 262), (338, 538)
XS = [200, 350, 520, 700, 840, 990, 1110]
YT, YB = 162, 438


def binder(c, x, y, hue, copy=False):
    """A ring binder, about 70 wide by 84 high, centered at (x, y)."""
    c.rect(x - 34, y - 42, 68, 84, fill=hue, stroke=INK, sw=2.5, rx=5)
    c.rect(x - 24, y - 24, 44, 30, fill=WHITE, rx=2)
    c.line(x - 18, y - 15, x + 14, y - 15, GRAYM, 3)
    c.line(x - 18, y - 6, x + 8, y - 6, GRAYM, 3)
    for k in range(3):
        c.circle(x - 34, y - 24 + k * 24, 4.5, fill=WHITE, stroke=INK, sw=1.5)
    if copy:
        c.rect(x - 28, y - 48, 68, 84, fill='none', stroke=INK, sw=2, rx=5, dash='5 4')


def draw():
    c = Canvas(1200, 600)
    # lanes
    c.rect(20, LY1[0], 1160, 200, fill=TOPT, stroke=TOP, sw=3, rx=16)
    c.rect(20, LY2[0], 1160, 200, fill=BOTT, stroke=BOT, sw=3, rx=16)
    # lane owners at the left edge
    ic_person(c, 70, YT - 20, 24, TOPD)
    binder(c, 70, YT + 44, TOP)
    ic_person(c, 70, YB - 20, 24, BOTD)
    binder(c, 70, YB + 44, BOT)
    # lane guide lines
    c.line(130, YT, 1160, YT, TOP, 2.5, '3 8', opacity=0.5)
    c.line(130, YB, 1160, YB, BOT, 2.5, '3 8', opacity=0.5)
    # crossing arrows: fork (down), pull request (up), merge (up); comments (down, thin)
    c.arrow(262, YT + 34, 330, YB - 40, INK, 6, 16)
    c.arrow(740, YB - 40, 700, YT + 44, INK, 6, 16)
    c.arrow(1030, YB - 40, 1084, YT + 44, INK, 6, 16)
    c.arrow(870, YT + 44, 962, YB - 40, GRAY, 2.5, 11, dash='5 5')
    # along-lane arrows
    c.arrow(404, YB, 470, YB, BOT, 4, 12)
    c.arrow(782, YT, 812, YT, TOP, 4, 12)
    # declined branch (faint)
    c.path('M880,%s Q930,%s 985,%s' % (YT - 40, YT - 70, YT - 60), stroke=GRAY, sw=2.5, dash='3 6', opacity=0.8)
    c.circle(1005, YT - 60, 14, fill=WHITE, stroke=GRAY, sw=2.5, opacity=0.9)
    c.line(998, YT - 67, 1012, YT - 53, GRAY, 2.5)
    c.line(998, YT - 53, 1012, YT - 67, GRAY, 2.5)
    # step 1: find the repository (binder and magnifier)
    binder(c, XS[0], YT, TOP)
    ic_magnifier(c, XS[0] + 38, YT + 24, 20, INK)
    # step 2: fork = photocopied binder in the bottom lane
    binder(c, XS[1], YB, BOT, copy=True)
    # step 3: change and save with a message
    ic_doc(c, XS[2] - 28, YB - 46, 56, 74, label=None)
    ic_lines(c, XS[2] - 18, YB - 20, 36, 3)
    c.poly([(XS[2] + 6, YB + 22), (XS[2] + 40, YB - 12), (XS[2] + 50, YB - 2), (XS[2] + 16, YB + 32)], fill=ORANGE, stroke=INK, sw=2.5)
    c.rect(XS[2] - 38, YB + 26, 34, 24, fill='#fff3b0', stroke=INK, sw=2, rx=3)
    c.line(XS[2] - 32, YB + 34, XS[2] - 10, YB + 34, INK, 2)
    c.line(XS[2] - 32, YB + 42, XS[2] - 16, YB + 42, INK, 2)
    # step 4: sticky note on the upward arrow
    nx, ny = XS[3], 300
    c.poly([(nx - 28, ny - 28), (nx + 28, ny - 28), (nx + 28, ny + 14), (nx + 14, ny + 28), (nx - 28, ny + 28)], fill='#ffe66d', stroke=INK, sw=2.5)
    c.poly([(nx + 28, ny + 14), (nx + 14, ny + 14), (nx + 14, ny + 28)], fill='#e0c93c', stroke=INK, sw=2)
    for k in range(3):
        c.line(nx - 18, ny - 14 + k * 12, nx + 18 - (8 if k == 2 else 0), ny - 14 + k * 12, INK, 2.5)
    # step 5: maintainer reads and comments
    ic_person(c, XS[4] - 26, YT - 6, 22, TOPD)
    ic_bubble(c, XS[4] + 6, YT - 42, 64, 44, fill=WHITE, stroke=INK, tail='left')
    c.line(XS[4] + 18, YT - 28, XS[4] + 58, YT - 28, GRAYM, 3)
    c.line(XS[4] + 18, YT - 16, XS[4] + 46, YT - 16, GRAYM, 3)
    # step 6: answer with more changes (in your copy)
    ic_doc(c, XS[5] - 28, YB - 46, 56, 74, label=None)
    ic_lines(c, XS[5] - 18, YB - 20, 36, 3)
    c.poly([(XS[5] + 6, YB + 22), (XS[5] + 40, YB - 12), (XS[5] + 50, YB - 2), (XS[5] + 16, YB + 32)], fill=ORANGE, stroke=INK, sw=2.5)
    ic_bubble(c, XS[5] + 18, YB - 62, 44, 28, fill=WHITE, stroke=GRAY, tail='left', sw=2)
    # step 7: merge stamp on the original
    ic_doc(c, XS[6] - 30, YT - 20, 60, 78, label=None)
    ic_lines(c, XS[6] - 20, YT + 14, 38, 3)
    c.rect(XS[6] - 18, YT - 74, 36, 36, fill=INK, rx=8)
    c.rect(XS[6] - 8, YT - 40, 16, 22, fill=INK)
    c.rect(XS[6] - 30, YT - 20, 60, 8, fill=GREEN, rx=4)
    ic_check(c, XS[6] + 30, YT + 30, 16, GREEN)

    steps = [
        (1, 'Find the repository', 'top', (XS[0] - 46, YT - 30), TOP,
         'A binder with a magnifying glass, in the top lane.',
         'Find the repository of the resource you want to improve. You cannot copy what you have not found.',
         'The repository is the original, and the maintainer owns it.'),
        (2, 'Fork it to make your own copy', 'bottom', (XS[1] - 40, YB - 36), BOT,
         'A binder with a dotted copy of itself, in the bottom lane, at the end of the first crossing arrow.',
         'Fork the repository to make your own copy. You change your copy, not the original.',
         'A fork keeps a link back to the source. It is the repository version of the revise and remix permissions.'),
        (3, 'Make your change and save it with a message', 'bottom', (XS[2] - 44, YB - 52), BOT,
         'A page with a pencil and a small note, in the bottom lane.',
         'Make your change in your copy and save it with a message that says what you did. A pull request needs a change to propose.',
         'Write the message for the maintainer who will read it.'),
        (4, 'Open a pull request', 'bottom', (XS[3] - 34, 270), INK,
         'A yellow sticky note on the arrow that crosses up to the top lane.',
         'Open a pull request that proposes your change to the original repository. The maintainer can only review a change that has been proposed.',
         'A pull request is a proposal. It does not change the original until it is merged.'),
        (5, 'The maintainer reads and comments', 'top', (XS[4] - 46, YT - 38), TOP,
         'A person beside a speech bubble, in the top lane, with a faint dotted branch ending in a cross.',
         'The maintainer reads your pull request and leaves comments. The review follows the proposal.',
         'The faint dotted branch is the other ending: a maintainer may also decline a pull request.'),
        (6, 'You answer with more changes', 'bottom', (XS[5] - 44, YB - 52), BOT,
         'A page with a pencil and a small grey speech bubble, in the bottom lane.',
         'You answer any comments by adding more changes to your copy. You respond to what the review found.',
         'The thin dashed arrow carries the comments back to your copy.'),
        (7, 'The maintainer merges', 'top', (XS[6] - 46, YT - 80), GREEN,
         'A rubber stamp pressing a page with a green check, at the right end of the top lane.',
         'The maintainer merges the pull request into the original. Merging is the last step, after the review is satisfied.',
         'Only now does the original change. The sequence shows the successful path.'),
    ]
    items = []
    for (i, label, panel, at, col, hint, desc, tip) in steps:
        items.append(dict(id=i, label=label, panel=panel, at=at, color=col, hint=hint, description=desc, tip=tip, radius=2.8))
    return c, items, []
