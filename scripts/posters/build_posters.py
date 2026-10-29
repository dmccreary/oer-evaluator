#!/usr/bin/env python3
"""Build the overlay infographic posters listed in docs/posters/poster-ideas.md.

Each module in specs/ defines META (text for the lesson page) and draw(), which
returns (canvas, items, quiz). The builder writes, under docs/sims/<slug>/ (or
docs/posters/<slug>/ when META sets home='posters'):

    <slug>.svg   the artwork, drawn in code so numbers and wording stay exact
    data.json    zones (grid) or callouts (callout) for the shared overlay engines
    main.html    iframe-ready page that loads docs/sims/shared-libs
    index.md     lesson page
    metadata.json

Usage:
    python3 scripts/posters/build_posters.py              # build every poster
    python3 scripts/posters/build_posters.py price-and-permission loop ...
"""
import importlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SIMS = ROOT / 'docs' / 'sims'
POSTERS = ROOT / 'docs' / 'posters'
HOMES = {'sims': SIMS, 'posters': POSTERS}
CHAPTERS = ROOT / 'docs' / 'chapters'
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / 'specs'))

SITE = 'https://dmccreary.github.io/oer-evaluator'
TODAY = '2026-10-29'

CHAPTER_TITLES = {
    '01-foundations-of-oer': 'Chapter 1: Foundations of Open Educational Resources',
    '02-open-licenses-attribution': 'Chapter 2: Open Licenses and Attribution',
    '03-ten-metric-rubric-scoring': 'Chapter 3: The Ten-Metric Rubric and Scoring',
    '04-open-formats-version-control': 'Chapter 4: Open File Formats and Version Control',
    '05-accuracy-currency': 'Chapter 5: Accuracy and Currency',
    '06-alignment-readability': 'Chapter 6: Alignment and Readability',
    '07-accessibility': 'Chapter 7: Accessibility',
    '08-practice-feedback': 'Chapter 8: Practice and Feedback',
    '09-modularity-metadata': 'Chapter 9: Modularity and Metadata',
    '10-portability-reuse': 'Chapter 10: Portability and Reuse Across Platforms',
    '11-manual-evaluation-adoption': 'Chapter 11: Manual Evaluation and Adoption Decisions',
    '12-ai-agents-prompts-scoring': 'Chapter 12: AI Agents, Prompts, and Rubric Scoring',
    '13-automated-checks-cost-privacy': 'Chapter 13: Automated Checks, Cost, and Student Privacy',
    '14-checking-agent-output': 'Chapter 14: Checking and Calibrating AI Agent Output',
    '15-improving-resources-with-ai': 'Chapter 15: Improving a Resource with AI Agents',
    '16-ab-testing-design': 'Chapter 16: Designing an A/B Test with Students',
    '17-ab-testing-analysis': 'Chapter 17: Analyzing A/B Test Results',
    '18-components-publishing-oer': 'Chapter 18: Reusable Components and Publishing OER',
    '19-training-certifying-reviewers': 'Chapter 19: Training Teachers and Certifying Reviewers',
}

HEIGHTS = {}
hp = HERE / 'heights.json'
if hp.exists():
    HEIGHTS = json.loads(hp.read_text())


def spec_modules():
    return sorted(p.stem for p in (HERE / 'specs').glob('p[0-9][0-9]_*.py'))


def home_of(meta):
    """Where a poster lives under docs/: 'sims' (the default) or 'posters'."""
    return meta.get('home', 'sims')


def lib_prefix(meta):
    """Relative path from the poster's main.html to docs/sims/shared-libs/."""
    return '../shared-libs/' if home_of(meta) == 'sims' else '../../sims/shared-libs/'


def yq(text):
    """Escape text for a double-quoted YAML scalar."""
    return text.replace('\\', '\\\\').replace('"', '\\"')


def jdump(obj):
    return json.dumps(obj, indent=2, ensure_ascii=False) + '\n'


def chapter_link(meta):
    if meta['chapter'] == 'all':
        return 'Chapters', '../../chapters/index.md'
    return CHAPTER_TITLES[meta['chapter']], '../../chapters/%s/index.md' % meta['chapter']


def chapter_refs(chapter, nums):
    """Pull numbered entries from a chapter's references.md (kept as written there)."""
    lines = {}
    for ln in (CHAPTERS / chapter / 'references.md').read_text().splitlines():
        head, _, rest = ln.partition('. ')
        if head.isdigit():
            lines[int(head)] = rest.strip()
    return [lines[n] for n in nums]


def ref_lines(meta):
    return '\n'.join('%d. %s' % (i + 1, r) for i, r in enumerate(meta['refs']))


# ---- data.json -------------------------------------------------------------

def grid_data(meta, c, items, quiz):
    palette = []
    zones = []
    for it in items:
        x1, y1, x2, y2 = it['box']
        z = {'id': it['id'], 'label': it['label'], 'color': it['color']}
        z.update(c.pct(x1, y1, x2, y2))
        z['summary'] = it['summary']
        z['facts'] = it['facts']
        zones.append(z)
        if it['color'] not in palette:
            palette.append(it['color'])
    return {'title': meta['title'], 'image': meta['slug'] + '.svg', 'layout': 'grid',
            'showLabels': False, 'palette': palette[:6], 'zones': zones, 'quiz': quiz}


def callout_data(meta, c, items):
    layout = meta.get('layout', 'top-bottom')
    callouts = []
    for it in items:
        x, y = c.pt(*it['at'])
        d = {'id': it['id'], 'label': it['label'], 'x': x, 'y': y, 'radius': it.get('radius', 3.2),
             'color': it['color']}
        d['hint'] = it['hint']
        d['description'] = it['description']
        if it.get('tip'):
            d['tip'] = it['tip']
        callouts.append(d)
    explicit = [it.get('panel') for it in items]
    if all(explicit):
        for d, pn in zip(callouts, explicit):
            d['panel'] = pn
        axis = 'x' if layout == 'top-bottom' else 'y'
        first = 'top' if layout == 'top-bottom' else 'left'
        callouts = (sorted([d for d in callouts if d['panel'] == first], key=lambda d: d[axis]) +
                    sorted([d for d in callouts if d['panel'] != first], key=lambda d: d[axis]))
    elif layout == 'top-bottom':
        # Proximity rule from the overlay guide: upper half of markers -> top strip,
        # each strip ordered left to right.
        order = sorted(callouts, key=lambda d: (d['y'], d['x']))
        n_top = (len(order) + 1) // 2
        for i, d in enumerate(order):
            d['panel'] = 'top' if i < n_top else 'bottom'
        callouts = (sorted([d for d in callouts if d['panel'] == 'top'], key=lambda d: d['x']) +
                    sorted([d for d in callouts if d['panel'] == 'bottom'], key=lambda d: d['x']))
    elif layout == 'dual-panel':
        order = sorted(callouts, key=lambda d: (d['x'], d['y']))
        n_left = (len(order) + 1) // 2
        for i, d in enumerate(order):
            d['panel'] = 'left' if i < n_left else 'right'
        callouts = (sorted([d for d in callouts if d['panel'] == 'left'], key=lambda d: d['y']) +
                    sorted([d for d in callouts if d['panel'] == 'right'], key=lambda d: d['y']))
    out = {'title': meta['title'], 'orientation': 'landscape', 'image': meta['slug'] + '.svg',
           'layout': layout, 'showNumbers': True, 'callouts': callouts}
    return out


# ---- main.html -------------------------------------------------------------

GRID_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="schema" content="https://dmccreary.github.io/intelligent-textbooks/ns/microsim/v1">
  <title>{title} — Interactive Infographic</title>
  <link rel="stylesheet" href="{lib}grid-overlay.css">
</head>
<body>
<main>

<div id="image-wrapper">
  <!-- image and zone overlay injected by grid-diagram.js -->
</div>

<div id="controls">
  <button class="mode-btn active" id="btn-explore">Explore</button>
  <button class="mode-btn"        id="btn-quiz">Quiz Me</button>
  <span id="quiz-score" style="display:none">
    Score: <strong id="score-val">0</strong> / <strong id="score-total">0</strong>
  </span>
  <span id="edit-badge">EDIT MODE</span>
</div>

<div id="detail-panel">
  <div id="panel-prompt">{prompt}</div>
  <div id="panel-content">
    <div id="panel-label"></div>
    <div id="panel-summary"></div>
    <ul id="panel-facts"></ul>
  </div>
</div>

<div id="quiz-question"></div>

<div id="edit-panel">
  <h3>Edit Mode — drag corner handles to calibrate zone boundaries</h3>
  <div id="coord-display">Drag a corner handle to see live coordinates.</div>
  <textarea id="json-output" readonly spellcheck="false"></textarea>
  <div id="edit-actions">
    <button id="copy-json-btn" onclick="sim.copyJSON()">Copy JSON</button>
    <span id="copy-confirm"></span>
  </div>
</div>

</main>

<script src="{lib}grid-diagram.js"></script>
</body>
</html>
'''

CALLOUT_HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Interactive Diagram</title>
  <meta name="schema" content="https://dmccreary.github.io/intelligent-textbooks/ns/microsim/v1">
  <link rel="stylesheet" href="{lib}style.css">
</head>
<body>
<main>

<div id="layout">
  <svg id="leaders-svg"></svg>

  <div id="diagram-wrapper">
    <img id="diagram-img" src="{image}" alt="{alt}" draggable="false">
    <div id="markers-layer"></div>
  </div>

  <div id="label-panel">
    <!-- label rows injected by diagram.js -->
  </div>
</div>

<div id="controls">
  <button class="mode-btn active" id="btn-explore" onclick="sim.setMode('explore')">Explore</button>
  <button class="mode-btn"        id="btn-quiz"    onclick="sim.setMode('quiz')">Quiz</button>
  <span id="quiz-score" style="display:none">
    Score: <strong id="score-val">0</strong> / <strong id="score-total">0</strong>
  </span>
</div>

<div id="infobox">
  <div id="infobox-prompt">Hover over a numbered marker or a label to learn about that part of the poster.</div>
  <div id="infobox-content">
    <div id="infobox-label"></div>
    <div id="infobox-desc"></div>
    <div id="infobox-ap-tip"></div>
    <button id="quiz-restart" onclick="sim.restartQuiz()">Try Again</button>
  </div>
</div>

<div id="edit-panel">
  <h3>Edit Mode — drag markers to calibrate positions</h3>
  <div id="coord-display">Drag a marker to see its live coordinates.</div>
  <textarea id="json-output" readonly spellcheck="false"></textarea>
  <div id="edit-actions">
    <button id="copy-json-btn" onclick="sim.copyJSON()">Copy JSON</button>
    <span id="copy-confirm"></span>
  </div>
</div>

</main>

<script src="{lib}diagram.js"></script>
</body>
</html>
'''


def main_html(meta, engine):
    if engine == 'grid':
        return GRID_HTML.format(title=meta['title'], lib=lib_prefix(meta),
                                prompt='Hover over or click a part of the poster to read about it.')
    return CALLOUT_HTML.format(title=meta['title'], image=meta['slug'] + '.svg', alt=meta['title'],
                               lib=lib_prefix(meta))


# ---- index.md --------------------------------------------------------------

def zone_table(engine, items):
    if engine == 'grid':
        rows = ['| Zone | What it shows |', '|---|---|']
        for it in items:
            rows.append('| %s | %s |' % (it['label'], it['summary']))
    else:
        rows = ['| # | Part | What it shows |', '|---|---|---|']
        for it in sorted(items, key=lambda d: d['id']):
            rows.append('| %d | %s | %s |' % (it['id'], it['label'], it['summary'] if 'summary' in it else it['description']))
    return '\n'.join(rows)


def index_md(meta, engine, items, height):
    slug, title = meta['slug'], meta['title']
    ch_label, ch_href = chapter_link(meta)
    if engine == 'grid':
        controls = (
            '- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.\n'
            '- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.\n'
            '- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.\n'
            '- **Try Again:** repeats the quiz after the last question.')
        good = ('Quiz mode scores each question as you answer it. The MicroSim does not store your answers. '
                'The poster prints its own headings, so the sim adds no labels on top of it.')
        h1 = '# %s\n\n' % title
        kind = 'a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.'
    else:
        controls = (
            '- **Explore and Quiz buttons:** switch modes.\n'
            '- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.\n'
            '- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.\n'
            '- **Try Again:** repeats the quiz after the last question.')
        good = ('Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. '
                'The artwork carries no text, so every name and number you read comes from the overlay.')
        h1 = ''
        kind = 'a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.'
    # A list needs a blank line before it, or MkDocs folds the bullets into the paragraph above.
    extra_good = ('\n' + ''.join('\n- %s' % g for g in meta['good'])) if meta.get('good') else ''
    acts = '\n'.join('%d. %s' % (i + 1, a) for i, a in enumerate(meta['activities']))
    qa = '\n'.join('%d. %s *(%s)*' % (i + 1, q, a) for i, (q, a) in enumerate(meta['assessment']))
    prereq = '\n'.join('- %s' % p for p in meta['prereq'])
    return '''---
title: "{ytitle}"
description: "{ydesc}"
image: /{home}/{slug}/{slug}.png
og:image: /{home}/{slug}/{slug}.png
twitter:image: /{home}/{slug}/{slug}.png
social:
   cards: false
status: built
hide:
  - toc
---

{h1}<iframe src="main.html" height="{height}px" width="100%" scrolling="no"></iframe>

[Run the {run_title} MicroSim Fullscreen](./main.html){{ .md-button .md-button--primary }}
<br/>
[{ch_label}]({ch_href}){{ .md-button }}

To change the content, edit `data.json` in this folder. The artwork is `{slug}.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="{site}/{home}/{slug}/main.html"
        height="{height}px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

{intro}

This MicroSim is {kind}

{table}

### Controls

{controls}

### Good to Know

{good}{extra_good}

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can {objective} (Bloom level: {bloom}.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

{prereq}

### Activities

{acts}

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

{qa}

### Connection to the OER Evaluator rubric

{connection}

## References

{refs}
'''.format(title=title, run_title=title[4:] if title.startswith('The ') else title,
           ytitle=yq(title), ydesc=yq(meta['desc']),
           desc=meta['desc'], slug=slug, home=home_of(meta), h1=h1, height=height, ch_label=ch_label,
           ch_href=ch_href, site=SITE, intro=meta['intro'], kind=kind, table=zone_table(engine, items),
           controls=controls, good=good, extra_good=extra_good, objective=meta['objective'],
           bloom=meta['bloom'], prereq=prereq, acts=acts, qa=qa, connection=meta['connection'],
           refs=ref_lines(meta))


# ---- metadata.json ---------------------------------------------------------

def metadata(meta, engine, items, height):
    ctrl = [
        {'name': 'Explore and Quiz buttons', 'type': 'button', 'description': 'switch between exploring the poster and answering quiz questions.'},
        {'name': 'Poster zones' if engine == 'grid' else 'Numbered markers',
         'type': 'interactive overlay',
         'description': 'hover or press to read about that part of the poster. In quiz mode a press is your answer.'},
        {'name': 'Try Again', 'type': 'button', 'description': 'repeats the quiz after the last question.'},
    ]
    return {
        'title': meta['title'],
        'creator': 'Dan McCreary',
        'subject': 'Open Educational Resources',
        'description': meta['desc'],
        'date': TODAY,
        'educational': {
            'gradeLevel': ['Adult'],
            'subjectArea': 'Other',
            'topic': meta['topic'],
            'learningObjectives': ['The learner will ' + meta['objective_plain']],
            'bloomsTaxonomy': meta['bloom'],
            'duration': '5-10 minutes',
            'prerequisites': meta['prereq'],
            'standards': [],
        },
        'technical': {
            'framework': 'SVG poster with shared overlay (%s)' % ('grid-diagram.js' if engine == 'grid' else 'diagram.js'),
            'version': 'n/a',
            'canvasDimensions': {'width': 'responsive', 'height': height},
            'canvasHeight': height,
            'responsive': True,
            'dependencies': ['%s%s' % (lib_prefix(meta), 'grid-diagram.js, grid-overlay.css' if engine == 'grid' else 'diagram.js, style.css')],
            'accessibility': {'hasAltText': True, 'keyboardNavigable': True},
        },
        'pedagogical': {
            'teachingStrategy': 'Explore a reference picture, then quiz on the same picture',
            'keyQuestions': meta['key_questions'],
            'commonMisconceptions': meta['misconceptions'],
            'assessmentOpportunities': [q for q, _ in meta['assessment']],
        },
        'controls': ctrl,
        'chapter': meta['chapter'],
    }


# ---- fact check ------------------------------------------------------------

def check_facts(meta):
    bad = []
    for chap, needle in meta.get('verify', []):
        d = CHAPTERS / chap
        text = ''
        if d.is_dir():
            for p in d.glob('*.md'):
                text += p.read_text()
        elif (ROOT / 'docs' / chap).exists():
            text = (ROOT / 'docs' / chap).read_text()
        if needle not in text:
            bad.append('%s: %r not found' % (chap, needle))
    return bad


# ---- driver ----------------------------------------------------------------

def build_one(modname):
    mod = importlib.import_module(modname)
    meta = dict(mod.META)
    meta['refs'] = [r for ch, nums in meta.get('ref_nums', []) for r in chapter_refs(ch, nums)] + meta.get('refs', [])
    c, items, quiz = mod.draw()
    engine = meta['overlay']
    slug = meta['slug']
    out = HOMES[home_of(meta)] / slug
    out.mkdir(parents=True, exist_ok=True)
    c.title = meta['title']
    c.desc = meta['alt']
    (out / (slug + '.svg')).write_text(c.svg())
    if engine == 'grid':
        data = grid_data(meta, c, items, quiz)
    else:
        data = callout_data(meta, c, items)
    (out / 'data.json').write_text(jdump(data))
    (out / 'main.html').write_text(main_html(meta, engine))
    height = HEIGHTS.get(slug, 760)
    md_items = items if engine == 'grid' else [dict(i, summary=i.get('summary') or i['description']) for i in items]
    (out / 'index.md').write_text(index_md(meta, engine, md_items, height))
    (out / 'metadata.json').write_text(jdump(metadata(meta, engine, items, height)))
    problems = list(c.warnings) + check_facts(meta)
    return slug, engine, len(items), problems


def main(argv):
    wanted = set(argv)
    failed = 0
    for modname in spec_modules():
        slug_guess = importlib.import_module(modname).META['slug']
        if wanted and slug_guess not in wanted and modname not in wanted:
            continue
        slug, engine, n, problems = build_one(modname)
        flag = 'OK ' if not problems else 'WARN'
        print('%s %-42s %-7s %2d items' % (flag, slug, engine, n))
        for p in problems:
            print('      - ' + p)
        failed += bool(problems)
    print('done; %d poster(s) with warnings' % failed)


if __name__ == '__main__':
    main(sys.argv[1:])
