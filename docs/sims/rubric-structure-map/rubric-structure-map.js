// Ten-Metric Rubric Map MicroSim (vis-network)
// CANVAS_HEIGHT: 560
// A tree of the Ten-Metric Rubric: the root splits into a Quality dimension and a Reusability
// dimension, and each dimension holds five metrics. Each edge means "is a part of" and points from the
// child to its parent.
// Explore mode: click a node to highlight its parent and children and read its definition, the question
// it answers, and the chapter that teaches it. Clicking nodes is exploration, not evidence.
// Quiz mode: ten teacher complaints. The learner clicks the metric node that the complaint tests, with
// two attempts each. Clicking the root or a dimension node counts as a wrong attempt. Only a correct
// first click counts as evidence of mastery, and only on the first completed run.
// The map does not zoom with the mouse wheel, so it never captures page scrolling. Zoom buttons are
// provided, and the map can be dragged only after it has been zoomed in.
// The MicroSim opens in explore mode with all 13 nodes visible and nothing selected.
// To change the nodes or the complaints, edit the NODES and COMPLAINTS tables below.

const CHAPTER_DIRS = {
  3: '03-ten-metric-rubric-scoring', 4: '04-open-formats-version-control', 5: '05-accuracy-currency',
  6: '06-alignment-readability', 7: '07-accessibility', 8: '08-practice-feedback',
  9: '09-modularity-metadata', 10: '10-portability-reuse'
};

// Positions are fixed (left to right: root, dimensions, metrics) so the map never moves on its own
const NODES = [
  { id: 'root', label: 'Ten-Metric Rubric', kind: 'root', parent: null, x: -255, y: 0,
    definition: 'The scoring guide that rates an OER on ten metrics worth 10 points each.', question: 'How good and how reusable is this resource?', chapter: 3 },
  { id: 'quality', label: 'Quality dimension\n(50 points)', kind: 'dimension', parent: 'root', x: -50, y: -125,
    definition: 'The five metrics that measure how well the resource helps learners.', question: 'Does it help learners reach the outcomes?', chapter: 3 },
  { id: 'reusability', label: 'Reusability dimension\n(50 points)', kind: 'dimension', parent: 'root', x: -50, y: 125,
    definition: 'The five metrics that measure how easily others can find, change, and reuse it.', question: 'Can others reuse it?', chapter: 3 },
  { id: 'accuracy', label: 'Accuracy and currency', kind: 'metric', parent: 'quality', x: 135, y: -225,
    definition: 'Facts are correct, and content, sources, and links are up to date.', question: 'Are the facts correct and up to date?', chapter: 5 },
  { id: 'alignment', label: 'Alignment', kind: 'metric', parent: 'quality', x: 135, y: -175,
    definition: 'Activities and assessments match the stated learning outcomes.', question: 'Do the activities and tests match the outcomes?', chapter: 6 },
  { id: 'readability', label: 'Readability', kind: 'metric', parent: 'quality', x: 135, y: -125,
    definition: 'The reading level and wording fit the audience.', question: 'Do the words fit the audience?', chapter: 6 },
  { id: 'accessibility', label: 'Accessibility', kind: 'metric', parent: 'quality', x: 135, y: -75,
    definition: 'Learners with disabilities can use the resource.', question: 'Can learners with disabilities use it?', chapter: 7 },
  { id: 'practice', label: 'Practice with feedback', kind: 'metric', parent: 'quality', x: 135, y: -25,
    definition: 'Learners can practice and learn how they did.', question: 'Can learners try things and get feedback?', chapter: 8 },
  { id: 'license', label: 'Open license', kind: 'metric', parent: 'reusability', x: 135, y: 25,
    definition: 'A clear open license is stated, and attribution is complete.', question: 'Does a clear license say what others may do?', chapter: 9 },
  { id: 'modularity', label: 'Modularity', kind: 'metric', parent: 'reusability', x: 135, y: 75,
    definition: 'Each part stands alone and can be embedded elsewhere.', question: 'Can each part stand alone?', chapter: 9 },
  { id: 'metadata', label: 'Metadata', kind: 'metric', parent: 'reusability', x: 135, y: 125,
    definition: 'Title, author, subject, grade level, license, and description are recorded.', question: 'Can others find it and tell what it is?', chapter: 9 },
  { id: 'source', label: 'Editable source', kind: 'metric', parent: 'reusability', x: 135, y: 175,
    definition: 'The source is in an editable open format, not only PDF.', question: 'Can others change it?', chapter: 4 },
  { id: 'portability', label: 'Portability', kind: 'metric', parent: 'reusability', x: 135, y: 225,
    definition: 'The resource runs in a browser without a login and embeds elsewhere.', question: 'Does it work in other places without a login?', chapter: 10 }
];

const COMPLAINTS = [
  { text: 'The page gives a river’s length that does not match its own cited source.', answer: 'accuracy', why: 'A fact that disagrees with its source is an accuracy problem.' },
  { text: 'The quiz asks about topics the unit never teaches.', answer: 'alignment', why: 'Assessment that does not match the outcomes is an alignment problem.' },
  { text: 'My students stop at the second paragraph because the words are too hard.', answer: 'readability', why: 'Wording that does not fit the audience is a readability problem.' },
  { text: 'A screen reader reads the picture names as “image1.png”.', answer: 'accessibility', why: 'Missing text descriptions block learners who use screen readers.' },
  { text: 'Students read it, but have nothing to try and no way to know if they are right.', answer: 'practice', why: 'The resource offers no practice and no feedback.' },
  { text: 'I cannot tell whether I may translate this.', answer: 'license', why: 'The reuse permissions are not stated.' },
  { text: 'I want just the quiz, but it is built into the middle of the chapter.', answer: 'modularity', why: 'The quiz cannot stand alone.' },
  { text: 'Search cannot tell me the subject or grade level.', answer: 'metadata', why: 'The descriptive fields are missing.' },
  { text: 'I only have a PDF, and I need to change one sentence.', answer: 'source', why: 'There is no editable file.' },
  { text: 'It needs a login before it will open.', answer: 'portability', why: 'A login blocks use in other places.' }
];

const ATTEMPTS = 2;
const PASS_MARK = 9;
const PASS_MESSAGE = 'You can match a problem to its metric.';
const HINT_TEXT = 'Not quite. Think about what the complaint says is broken.';

// Node colors by kind; states override them
const KIND_COLORS = {
  root: { background: '#1b2a41', border: '#1b2a41', font: 'white' },
  qualityDimension: { background: '#2c6fb7', border: '#1d4f86', font: 'white' },
  reusabilityDimension: { background: '#7b4aa5', border: '#573379', font: 'white' },
  qualityMetric: { background: '#d6e6f7', border: '#2c6fb7', font: '#1b2a41' },
  reusabilityMetric: { background: '#e8dcf3', border: '#7b4aa5', font: '#1b2a41' }
};
const STATE_COLORS = {
  selected: { background: '#fff3b0', border: '#e69500', font: '#1b2a41' },
  related: { border: '#e69500' },
  correct: { background: '#c8e6c9', border: '#2e7d32', font: '#1b2a41' },
  wrong: { background: '#ffcdd2', border: '#b71c1c', font: '#1b2a41' }
};

let nodes, edges, network;
let mode = 'explore'; // 'explore' | 'quiz'
let selectedId = null; // explore mode: the clicked node
let firstRunDone = false; // the first completed quiz run is the one that counts as evidence
let run = null; // { order, pos, tries, phase, results, wrong, feedback, practice }
let zoomedIn = false;

const byId = {};
NODES.forEach(n => { byId[n.id] = n; });

function kindKey(n) {
  const group = n.id === 'root' ? null : (n.kind === 'dimension' ? n.id : n.parent);
  if (n.kind === 'root') return 'root';
  return (group === 'quality' ? 'quality' : 'reusability') + (n.kind === 'dimension' ? 'Dimension' : 'Metric');
}

function baseColor(n) {
  const c = KIND_COLORS[kindKey(n)];
  return { background: c.background, border: c.border, highlight: { background: c.background, border: c.border }, hover: { background: c.background, border: c.border } };
}

// --- DOM helpers (text goes in with textContent) ---------------------------------------------
function el(tag, cls, text) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text !== undefined) e.textContent = text;
  return e;
}

// --- Network ----------------------------------------------------------------------------------
function buildNetwork() {
  const visNodes = NODES.map(n => {
    const c = KIND_COLORS[kindKey(n)];
    return {
      id: n.id, label: n.label, x: n.x, y: n.y, shape: 'box', margin: 8,
      widthConstraint: { minimum: n.kind === 'root' ? 130 : 150, maximum: n.kind === 'root' ? 130 : 150 },
      color: baseColor(n), font: { color: c.font, size: 15, face: 'Arial', bold: n.kind !== 'metric' },
      borderWidth: 2, borderWidthSelected: 2, shapeProperties: { borderRadius: 6 }
    };
  });
  const visEdges = NODES.filter(n => n.parent).map(n => ({
    id: 'e-' + n.id, from: n.id, to: n.parent, arrows: { to: { enabled: true, scaleFactor: 0.8 } },
    color: { color: '#6b7785', highlight: '#e69500' }, width: 2,
    smooth: { type: 'cubicBezier', forceDirection: 'horizontal', roundness: 0.5 }
  }));
  nodes = new vis.DataSet(visNodes);
  edges = new vis.DataSet(visEdges);
  network = new vis.Network(document.getElementById('network'), { nodes: nodes, edges: edges }, {
    layout: { improvedLayout: false },
    physics: { enabled: false },
    interaction: { hover: false, zoomView: false, dragView: false, dragNodes: false, selectConnectedEdges: false, navigationButtons: false, keyboard: false }
  });
  network.on('click', params => {
    if (params.nodes.length > 0) onNode(params.nodes[0]);
  });
  window.addEventListener('resize', () => { network.redraw(); if (!zoomedIn) fitMap(); });
  setTimeout(fitMap, 50);
}

let fitScaleValue = 1; // the scale that shows the whole map

function fitMap() {
  network.fit({ animation: false });
  fitScaleValue = network.getScale();
}

function zoomBy(factor) {
  const scale = Math.min(2.5, Math.max(fitScaleValue, network.getScale() * factor));
  network.moveTo({ scale: scale, animation: false });
  zoomedIn = scale > fitScaleValue * 1.05;
  network.setOptions({ interaction: { dragView: zoomedIn } });
}

function resetZoom() {
  zoomedIn = false;
  network.setOptions({ interaction: { dragView: false } });
  fitMap();
}

// Colors for the nodes depend on the mode and state
function paint() {
  const updates = NODES.map(n => {
    let col = Object.assign({}, baseColor(n));
    let font = { color: KIND_COLORS[kindKey(n)].font };
    let label = n.label;
    let borderWidth = 2;
    if (mode === 'explore' && selectedId) {
      const sel = byId[selectedId];
      const related = n.id === sel.parent || n.parent === sel.id;
      if (n.id === selectedId) { col = Object.assign({}, STATE_COLORS.selected); font = { color: STATE_COLORS.selected.font }; borderWidth = 4; }
      else if (related) { col = Object.assign({}, col, { border: STATE_COLORS.related.border }); borderWidth = 4; }
    }
    if (mode === 'quiz' && run) {
      const item = run.phase === 'summary' ? null : COMPLAINTS[run.order[run.pos]];
      if (run.wrong.includes(n.id)) { col = Object.assign({}, STATE_COLORS.wrong); font = { color: STATE_COLORS.wrong.font }; borderWidth = 4; label = '✗ ' + n.label; }
      if (item && run.phase === 'feedback' && n.id === item.answer) { col = Object.assign({}, STATE_COLORS.correct); font = { color: STATE_COLORS.correct.font }; borderWidth = 4; label = '✓ ' + n.label; }
    }
    return { id: n.id, color: Object.assign({ highlight: { background: col.background, border: col.border }, hover: { background: col.background, border: col.border } }, col), font: font, label: label, borderWidth: borderWidth };
  });
  nodes.update(updates);
  // edges: highlight the ones that touch the selected node
  const eu = NODES.filter(n => n.parent).map(n => {
    const hot = mode === 'explore' && selectedId && (n.id === selectedId || n.parent === selectedId);
    return { id: 'e-' + n.id, color: { color: hot ? '#e69500' : '#6b7785' }, width: hot ? 4 : 2 };
  });
  edges.update(eu);
}

// --- Behavior ---------------------------------------------------------------------------------
function onNode(id) {
  if (mode === 'explore') {
    selectedId = selectedId === id ? null : id;
    render();
    return;
  }
  if (!run || run.phase !== 'question' || run.wrong.includes(id)) return;
  const item = COMPLAINTS[run.order[run.pos]];
  run.tries++;
  const answer = byId[item.answer];
  if (id === item.answer) {
    run.results[run.pos] = { item: item, firstTry: run.tries === 1 };
    run.feedback = { kind: 'good', text: 'Correct: ' + answer.label.replace('\n', ' ') + '. ' + item.why };
    run.phase = 'feedback';
  } else if (run.tries < ATTEMPTS) {
    run.wrong.push(id);
    run.feedback = { kind: 'hint', text: HINT_TEXT };
  } else {
    run.wrong.push(id);
    run.results[run.pos] = { item: item, firstTry: false };
    run.feedback = { kind: 'bad', text: 'This is ' + answer.label.replace('\n', ' ') + '. ' + item.why };
    run.phase = 'feedback';
  }
  render();
}

function startRun() {
  mode = 'quiz';
  const order = COMPLAINTS.map((_, i) => i);
  for (let i = order.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [order[i], order[j]] = [order[j], order[i]];
  }
  run = { order: order, pos: 0, tries: 0, phase: 'question', results: [], wrong: [], feedback: null, practice: firstRunDone };
  render();
}

function nextQuestion() {
  if (!run || run.phase !== 'feedback') return;
  run.pos++;
  run.tries = 0;
  run.wrong = [];
  run.feedback = null;
  if (run.pos >= run.order.length) {
    run.phase = 'summary';
    if (!run.practice) firstRunDone = true;
  } else {
    run.phase = 'question';
  }
  render();
}

// --- Rendering --------------------------------------------------------------------------------
function render() {
  const btnExplore = document.getElementById('btn-explore');
  const btnQuiz = document.getElementById('btn-quiz');
  btnExplore.classList.toggle('on', mode === 'explore');
  btnQuiz.classList.toggle('on', mode === 'quiz');
  btnExplore.setAttribute('aria-pressed', mode === 'explore' ? 'true' : 'false');
  btnQuiz.setAttribute('aria-pressed', mode === 'quiz' ? 'true' : 'false');

  const progress = document.getElementById('progress');
  progress.textContent = '';
  if (mode === 'quiz' && run) {
    COMPLAINTS.forEach((_, i) => {
      const s = el('span', 'seg');
      const r = run.results[i];
      if (r) s.classList.add(r.firstTry ? 'ok' : 'miss');
      if (i === run.pos && run.phase !== 'summary') s.classList.add('cur');
      progress.appendChild(s);
    });
  }

  const inQuiz = mode === 'quiz' && run;
  const btnNext = document.getElementById('btn-next');
  btnNext.hidden = !(inQuiz && run.phase !== 'summary');
  btnNext.disabled = !(inQuiz && run.phase === 'feedback');
  btnNext.textContent = inQuiz && run.pos >= run.order.length - 1 ? 'See results' : 'Next →';
  document.getElementById('btn-again').hidden = !(inQuiz && run.phase === 'summary');

  const panel = document.getElementById('panel');
  panel.textContent = '';
  if (mode === 'explore') {
    if (!selectedId) {
      panel.appendChild(el('p', 'prompt', 'Click a node to see what it means.'));
    } else {
      const n = byId[selectedId];
      panel.appendChild(el('h2', '', n.label.replace('\n', ' ')));
      const dl = el('dl');
      dl.appendChild(el('dt', '', 'Definition'));
      dl.appendChild(el('dd', '', n.definition));
      dl.appendChild(el('dt', '', 'Question it answers'));
      dl.appendChild(el('dd', '', n.question));
      dl.appendChild(el('dt', '', 'Taught in'));
      const dd = el('dd');
      const a = el('a', '', 'Chapter ' + n.chapter);
      a.href = '../../chapters/' + CHAPTER_DIRS[n.chapter] + '/';
      a.target = '_top';
      dd.appendChild(a);
      dl.appendChild(dd);
      const parent = n.parent ? byId[n.parent].label.replace('\n', ' ') : 'none (this is the root)';
      dl.appendChild(el('dt', '', 'Part of'));
      dl.appendChild(el('dd', '', parent));
      const kids = NODES.filter(c => c.parent === n.id).map(c => c.label.replace('\n', ' '));
      if (kids.length) {
        dl.appendChild(el('dt', '', 'Contains'));
        dl.appendChild(el('dd', '', kids.join(', ')));
      }
      panel.appendChild(dl);
    }
  } else if (run.phase === 'summary') {
    renderSummary(panel);
  } else {
    const item = COMPLAINTS[run.order[run.pos]];
    panel.appendChild(el('p', 'qhead', (run.practice ? 'Practice ' : 'Complaint ') + (run.pos + 1) + ' of ' + run.order.length));
    panel.appendChild(el('p', 'question', '“' + item.text.replace(/^“|”$/g, '') + '”'));
    if (run.feedback) panel.appendChild(el('p', 'feedback ' + run.feedback.kind, run.feedback.text));
    else panel.appendChild(el('p', 'prompt', 'Click the metric node that this complaint tests.'));
  }
  paint();
}

function renderSummary(panel) {
  const total = run.results.length;
  const n = run.results.filter(r => r.firstTry).length;
  const passed = n >= PASS_MARK;
  panel.appendChild(el('h2', passed ? 'pass' : '', run.practice
    ? n + ' of ' + total + ' correct on this practice run'
    : n + ' of ' + total + ' correct on the first attempt'));
  panel.appendChild(el('p', '', run.practice ? 'Practice runs do not change your first-run score.'
    : (passed ? PASS_MESSAGE : 'Mastery is ' + PASS_MARK + ' of ' + total + ' on the first attempt. Review the misses below, then play again.')));
  const missed = run.results.filter(r => !r.firstTry);
  if (missed.length) {
    panel.appendChild(el('p', 'qhead', 'Metrics you missed:'));
    const ul = el('ul');
    missed.forEach(r => ul.appendChild(el('li', '', byId[r.item.answer].label.replace('\n', ' '))));
    panel.appendChild(ul);
  }
}

// --- Start ------------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function () {
  buildNetwork();

  // Visually hidden buttons so keyboard and screen reader users can reach every node
  const list = document.getElementById('node-list');
  NODES.forEach(n => {
    const b = el('button', '', n.label.replace('\n', ' '));
    b.type = 'button';
    b.addEventListener('click', () => onNode(n.id));
    list.appendChild(b);
  });

  document.getElementById('btn-explore').addEventListener('click', () => { mode = 'explore'; render(); });
  document.getElementById('btn-quiz').addEventListener('click', startRun);
  document.getElementById('btn-next').addEventListener('click', nextQuestion);
  document.getElementById('btn-again').addEventListener('click', startRun);
  document.getElementById('btn-zoom-in').addEventListener('click', () => zoomBy(1.25));
  document.getElementById('btn-zoom-out').addEventListener('click', () => zoomBy(0.8));
  document.getElementById('btn-fit').addEventListener('click', resetZoom);
  render();
});
