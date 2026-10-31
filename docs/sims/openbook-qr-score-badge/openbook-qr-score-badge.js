// OpenBook QR Score Badge MicroSim (p5.js)
// CANVAS_HEIGHT: 750
// The OpenBook QR Score is the 100-point total of the ten-metric rubric, reported with its quality
// subtotal (Q, metrics 1 to 5) and its reusability subtotal (R, metrics 6 to 10), written
//   QR 65 (Q 32 / R 33)
// The badge draws the ten metric scores as ten modules in a QR-code-like grid: the top row is quality,
// the bottom row is reusability, and each module fills from the bottom in proportion to its score.
// A dashed module with a "!" is below the floor of 5. The corner squares and the dotted line are
// decoration only; the badge is not a scannable code.
// Explore mode: ten sliders, six example resources, and a button that saves the badge as a PNG.
// Build mode: three target badges. The learner sets the sliders until the badge reads the target and
// presses Check. Only the first Check of each target counts as evidence. The targets are illustrative.
// To change the examples or the targets, edit the PRESETS and TARGETS blocks below.

const METRICS = ['Accuracy and currency', 'Alignment', 'Readability', 'Accessibility', 'Practice with feedback',
                 'Open license', 'Modularity', 'Metadata', 'Editable source', 'Portability'];
const FLOOR = 5; // every metric must be at least this for Adopt
const INK = '#1f2430';
const Q_COLOR = '#3b3f9e'; // quality row (indigo)
const R_COLOR = '#0f766e'; // reusability row (teal)
const BAND_COLORS = { Excellent: '#17603a', Good: '#2f6f1f', Fair: '#8a5a00', Weak: '#a8420f', Poor: '#a02323' };

const PRESETS = [
  { name: 'Watershed Basics (before)', scores: [7, 6, 8, 5, 6, 9, 5, 4, 8, 7] },
  { name: 'Watershed Basics (after)', scores: [9, 6, 8, 8, 8, 9, 8, 8, 8, 6] },
  { name: 'Open Algebra', scores: [9, 8, 8, 9, 9, 10, 9, 9, 10, 9] },
  { name: 'Locked Chemistry E-book', scores: [9, 9, 9, 8, 9, 1, 5, 6, 2, 7] },
  { name: 'One Gap', scores: [9, 9, 9, 9, 9, 9, 9, 9, 9, 4] },
  { name: 'Thin Material', scores: [3, 2, 4, 3, 2, 5, 4, 3, 6, 5] }
];
const CUSTOM = 'My own scores';

const TARGETS = [
  { q: 32, r: 33, hint: 'Any ten scores whose halves add to these two subtotals will work.',
    why: 'The two subtotals add to the total, 32 + 33 = 65, and the badge reports all three numbers.' },
  { q: 50, r: 30, hint: 'Quality can be at most 50. What does that make each quality metric?',
    why: 'Q 50 needs all five quality metrics at 10, and R 30 is the sum of the five reusability metrics.' },
  { q: 47, r: 32, metric: { index: 5, value: 1 }, hint: 'Set Open license to exactly 1, then reach the two subtotals.',
    why: 'The total is 79, which is 75 or more, but Open license is 1, below the floor of 5, so the decision is Revise. A bare total would hide that.' }
];

let containerWidth = 400;
let canvasWidth = 400;
const CANVAS_HEIGHT = 750;
const pad = 16;
const BADGE_W = 600;
const BADGE_H = 660;

let sliders = [];
let presetSelect, numbersCheckbox, saveButton, modeButton, checkButton, nextButton, retryButton;
let badgeG;
let badgeKey = '';
let liveRegion;

let mode = 'explore'; // explore | build | summary
let exploreScores = [7, 6, 8, 5, 6, 9, 5, 4, 8, 7];
let buildIndex = 0;
let buildResults = [];
let buildChecked = false;
let buildFeedback = '';
let buildFeedbackOk = false;

function sum(a) { return a.reduce((x, y) => x + y, 0); }
function bandOf(total) {
  if (total >= 90) return 'Excellent';
  if (total >= 75) return 'Good';
  if (total >= 50) return 'Fair';
  if (total >= 25) return 'Weak';
  return 'Poor';
}
function decisionOf(scores) {
  const total = sum(scores);
  if (total >= 75 && scores.every(s => s >= FLOOR)) return 'Adopt';
  if (total < 50) return 'Reject';
  return 'Revise';
}
function qrText(scores) {
  const q = sum(scores.slice(0, 5));
  const r = sum(scores.slice(5));
  return 'QR ' + (q + r) + ' (Q ' + q + ' / R ' + r + ')';
}
function currentScores() { return sliders.map(s => Number(s.value())); }
function setScores(scores) { scores.forEach((v, i) => sliders[i].value(v)); }

function setup() {
  updateCanvasSize(); // must be first: get the container width before creating the canvas
  const canvas = createCanvas(containerWidth, CANVAS_HEIGHT);
  canvas.parent(document.querySelector('main'));
  textFont('Arial');

  badgeG = createGraphics(BADGE_W, BADGE_H);
  badgeG.pixelDensity(2);

  createControls(); // all controls exist before anything is positioned

  liveRegion = createDiv('');
  liveRegion.attribute('aria-live', 'polite');
  liveRegion.style('position', 'absolute');
  liveRegion.style('left', '-10000px');
  liveRegion.style('width', '1px');
  liveRegion.style('height', '1px');
  liveRegion.style('overflow', 'hidden');

  describe('An OpenBook QR Score badge. Ten modules in two rows show the ten rubric metric scores: quality on top, ' +
           'reusability below. Sliders change the scores, and the badge text reads the total with its two subtotals.');
  applyPreset(PRESETS[0].name);
  refreshControls();
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(containerWidth, CANVAS_HEIGHT);
}

function updateCanvasSize() {
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width); // avoid fractional pixels
  canvasWidth = containerWidth;
}

function createControls() {
  for (let i = 0; i < 10; i++) {
    const sl = createSlider(0, 10, 5, 1); // built-in p5.js slider, whole points
    sl.attribute('aria-label', METRICS[i] + ' score, 0 to 10');
    sl.input(() => onSliderInput());
    sliders.push(sl);
  }
  presetSelect = createSelect();
  presetSelect.option(CUSTOM);
  PRESETS.forEach(p => presetSelect.option(p.name));
  presetSelect.attribute('aria-label', 'Example resource');
  presetSelect.changed(() => applyPreset(presetSelect.value()));

  numbersCheckbox = createCheckbox(' Show scores on badge', true);
  numbersCheckbox.changed(() => announce(numbersCheckbox.checked() ? 'Scores shown on the badge.' : 'Scores hidden on the badge.'));

  saveButton = createButton('Save badge PNG');
  saveButton.mousePressed(saveBadge);

  modeButton = createButton('Build challenge');
  modeButton.mousePressed(toggleMode);

  checkButton = createButton('Check');
  checkButton.mousePressed(checkBuild);
  nextButton = createButton('Next');
  nextButton.mousePressed(nextBuild);
  retryButton = createButton('Try again');
  retryButton.mousePressed(startBuild);
}

function onSliderInput() {
  if (mode === 'explore') presetSelect.selected(CUSTOM);
  announce(qrText(currentScores()));
}

function applyPreset(name) {
  const p = PRESETS.find(x => x.name === name);
  if (!p) return;
  setScores(p.scores);
  presetSelect.selected(name);
  announce(name + ': ' + qrText(p.scores));
}

function announce(text) { if (liveRegion) liveRegion.html(text); }

function toggleMode() {
  if (mode === 'explore') {
    exploreScores = currentScores();
    startBuild();
  } else {
    setScores(exploreScores);
    mode = 'explore';
    presetSelect.selected(CUSTOM);
    refreshControls();
  }
}

function startBuild() {
  mode = 'build';
  buildIndex = 0;
  buildResults = [];
  prepareTarget();
}

function prepareTarget() {
  setScores([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]);
  buildChecked = false;
  buildFeedback = '';
  announce('Build the badge ' + targetText(TARGETS[buildIndex]));
  refreshControls();
}

function targetText(t) { return 'QR ' + (t.q + t.r) + ' (Q ' + t.q + ' / R ' + t.r + ')'; }

function checkBuild() {
  if (mode !== 'build') return;
  const t = TARGETS[buildIndex];
  const sc = currentScores();
  const q = sum(sc.slice(0, 5));
  const r = sum(sc.slice(5));
  const okMetric = !t.metric || sc[t.metric.index] === t.metric.value;
  const ok = q === t.q && r === t.r && okMetric;
  if (buildResults[buildIndex] === undefined) buildResults[buildIndex] = ok; // first check counts
  buildChecked = true;
  buildFeedbackOk = ok;
  if (ok) {
    buildFeedback = 'Correct: ' + targetText(t) + '. ' + t.why;
  } else {
    const parts = [];
    if (q !== t.q) parts.push('Q is ' + q + ', not ' + t.q);
    if (r !== t.r) parts.push('R is ' + r + ', not ' + t.r);
    if (!okMetric) parts.push(METRICS[t.metric.index] + ' is ' + sc[t.metric.index] + ', not ' + t.metric.value);
    buildFeedback = 'Not quite. ' + parts.join('; ') + '. Adjust the sliders and check again.';
  }
  announce(buildFeedback);
  refreshControls();
}

function nextBuild() {
  if (buildResults[buildIndex] === undefined) return;
  if (buildIndex < TARGETS.length - 1) {
    buildIndex++;
    prepareTarget();
  } else {
    mode = 'summary';
    announce('You built ' + buildResults.filter(Boolean).length + ' of ' + TARGETS.length + ' badges correctly on the first check.');
    refreshControls();
  }
}

function saveBadge() {
  renderBadge(true);
  const cv = badgeG.elt || badgeG.canvas;
  const name = 'openbook-qr-score-' + sum(currentScores()) + '.png';
  cv.toBlob(blob => {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = name;
    a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 1000);
  });
}

// ---------------------------------------------------------------------------
// Layout. One column of drawing, then a two-column block of sliders: quality left, reusability right.
// ---------------------------------------------------------------------------
function geom() {
  const W = canvasWidth;
  const bh = 300;
  const bw = bh * BADGE_W / BADGE_H;
  const colGap = 20;
  const colW = Math.floor((W - 2 * pad - colGap) / 2);
  return { W: W, bx: (W - bw) / 2, by: 80, bw: bw, bh: bh, panelY: 386, panelH: 72, headY: 464, slY: 484,
           rowH: 46, colW: colW, colGap: colGap, botY: 716, modeY: 40 };
}

function refreshControls() {
  const inExplore = mode === 'explore';
  const inBuild = mode === 'build';
  const inSummary = mode === 'summary';
  toggle(presetSelect, inExplore);
  toggle(numbersCheckbox, inExplore || inBuild);
  toggle(saveButton, inExplore);
  toggle(modeButton, true);
  toggle(checkButton, inBuild);
  toggle(nextButton, inBuild && buildResults[buildIndex] !== undefined);
  toggle(retryButton, inSummary);
  sliders.forEach(s => toggle(s, !inSummary));
  modeButton.html(inExplore ? 'Build challenge' : 'Back to explore');
}

function toggle(el, on) { if (on) el.show(); else el.hide(); }

function positionControls(L) {
  presetSelect.position(pad, L.modeY);
  presetSelect.size(Math.min(210, L.W - 2 * pad - 140));
  modeButton.position(mode === 'explore' ? pad + Math.min(210, L.W - 2 * pad - 140) + 10 : pad, L.modeY);
  sliders.forEach((s, i) => {
    const col = i < 5 ? 0 : 1;
    const row = i % 5;
    s.position(pad + col * (L.colW + L.colGap), L.slY + row * L.rowH + 18);
    s.size(L.colW);
  });
  numbersCheckbox.position(pad, L.botY);
  saveButton.position(pad + 200, L.botY - 2);
  checkButton.position(pad, L.botY - 2);
  nextButton.position(pad + 78, L.botY - 2);
  retryButton.position(pad + 14, 352);
  if (mode === 'build') numbersCheckbox.position(pad + 150, L.botY);
}

function draw() {
  updateCanvasSize();
  if (containerWidth !== width) resizeCanvas(containerWidth, CANVAS_HEIGHT);
  const L = geom();
  positionControls(L);

  // Drawing region (aliceblue) and control region (white), both with a silver border
  fill('aliceblue');
  stroke('silver');
  strokeWeight(1);
  rect(0, 0, L.W, L.headY - 4);
  fill('white');
  rect(0, L.headY - 4, L.W, CANVAS_HEIGHT - L.headY + 4);

  noStroke();
  fill('black');
  textStyle(BOLD);
  textSize(fitSize('OpenBook QR Score Badge', L.W - 2 * pad, 24, 16));
  textAlign(CENTER, TOP);
  text('OpenBook QR Score Badge', L.W / 2, 8);
  textStyle(NORMAL);

  if (mode === 'summary') {
    drawSummary(L);
  } else {
    const scores = currentScores();
    renderBadge(false);
    image(badgeG, L.bx, L.by, L.bw, L.bh);
    if (mode === 'explore') drawExploreReadout(L, scores); else drawBuildReadout(L);
    drawSliderLabels(L, scores);
    if (mode === 'build') drawProgress(L);
  }
}

function fitSize(str, maxW, maxSize, minSize) {
  let s = maxSize;
  textSize(s);
  while (s > minSize && textWidth(str) > maxW) { s--; textSize(s); }
  return s;
}

function drawPanel(L) {
  fill('white');
  stroke('silver');
  strokeWeight(1);
  rect(pad, L.panelY, L.W - 2 * pad, L.panelH, 6);
  noStroke();
  fill(INK);
  textAlign(LEFT, TOP);
}

function drawExploreReadout(L, scores) {
  drawPanel(L);
  const q = sum(scores.slice(0, 5));
  const total = sum(scores);
  const w = L.W - 2 * pad - 16;
  textStyle(BOLD);
  textSize(fitSize('OpenBook QR Score: ' + qrText(scores), w, 18, 12));
  text('OpenBook QR Score: ' + qrText(scores), pad + 8, L.panelY + 7);
  textStyle(NORMAL);
  const bandText = 'Band: ' + bandOf(total) + '. Decision: ' + decisionOf(scores) + ' (starting rule).';
  textSize(fitSize(bandText, w, 14, 11));
  text(bandText, pad + 8, L.panelY + 29);
  const low = lowestMetric(scores);
  const lowText = 'Lowest metric: ' + METRICS[low.i] + ', ' + low.s + (low.s < FLOOR ? ', below the floor of 5.' : '. Every metric is at least 5.');
  textSize(fitSize(lowText, w, 14, 11));
  text(lowText, pad + 8, L.panelY + 48, w);
}

function lowestMetric(scores) {
  let i = 0;
  scores.forEach((s, k) => { if (s < scores[i]) i = k; });
  return { i: i, s: scores[i] };
}

function drawBuildReadout(L) {
  drawPanel(L);
  const t = TARGETS[buildIndex];
  const w = L.W - 2 * pad - 16;
  textStyle(BOLD);
  textSize(fitSize('Build this badge: ' + targetText(t), w, 18, 12));
  text('Build this badge: ' + targetText(t), pad + 8, L.panelY + 7);
  textStyle(NORMAL);
  textSize(13);
  if (!buildChecked) {
    fill(INK);
    text(t.hint, pad + 8, L.panelY + 30, w, L.panelH - 32);
  } else {
    fill(buildFeedbackOk ? '#17603a' : '#a02323');
    text(buildFeedback, pad + 8, L.panelY + 30, w, L.panelH - 32);
  }
}

function drawProgress(L) {
  fill(INK);
  noStroke();
  textSize(14);
  textAlign(RIGHT, CENTER);
  text('Target ' + (buildIndex + 1) + ' of ' + TARGETS.length, L.W - pad, L.modeY + 12);
}

function drawSliderLabels(L, scores) {
  noStroke();
  textAlign(LEFT, TOP);
  const q = sum(scores.slice(0, 5));
  const r = sum(scores.slice(5));
  textStyle(BOLD);
  textSize(14);
  fill(Q_COLOR);
  text('Quality (Q) = ' + q + ' of 50', pad, L.headY);
  fill(R_COLOR);
  text('Reusability (R) = ' + r + ' of 50', pad + L.colW + L.colGap, L.headY);
  textStyle(NORMAL);
  scores.forEach((s, i) => {
    const col = i < 5 ? 0 : 1;
    const row = i % 5;
    const x = pad + col * (L.colW + L.colGap);
    const y = L.slY + row * L.rowH;
    fill(INK);
    textSize(fitSize((i + 1) + '. ' + METRICS[i], L.colW - 34, 13, 10));
    textAlign(LEFT, TOP);
    text((i + 1) + '. ' + METRICS[i], x, y);
    textAlign(RIGHT, TOP);
    textStyle(BOLD);
    fill(s < FLOOR ? '#a8420f' : INK);
    textSize(14);
    text(String(s), x + L.colW, y);
    textStyle(NORMAL);
  });
}

function drawSummary(L) {
  const n = buildResults.filter(Boolean).length;
  fill('white');
  stroke('silver');
  strokeWeight(1);
  rect(pad, 60, L.W - 2 * pad, 330, 8);
  noStroke();
  fill(INK);
  textAlign(LEFT, TOP);
  textStyle(BOLD);
  textSize(20);
  text('Build challenge results', pad + 14, 76, L.W - 2 * pad - 28);
  textStyle(NORMAL);
  textSize(15);
  let y = 112;
  TARGETS.forEach((t, i) => {
    fill(buildResults[i] ? '#17603a' : '#a02323');
    text((buildResults[i] ? 'Correct on the first check: ' : 'Needed another try: ') + targetText(t), pad + 14, y, L.W - 2 * pad - 28);
    y += 26;
  });
  fill(INK);
  textStyle(BOLD);
  text(n + ' of ' + TARGETS.length + ' correct on the first check.', pad + 14, y + 8, L.W - 2 * pad - 28);
  textStyle(NORMAL);
  const msg = n >= 2
    ? 'You can write a resource’s result as an OpenBook QR Score, with the total and both halves.'
    : 'Try again: the total is just Q plus R, and the badge always reports all three numbers.';
  text(msg, pad + 14, y + 38, L.W - 2 * pad - 28);
  text('Press Try again to rebuild the badges, or Back to explore to keep experimenting.', pad + 14, y + 112, L.W - 2 * pad - 28);
}

// ---------------------------------------------------------------------------
// The badge. It is drawn into an off-screen buffer so the same picture is shown on the canvas and saved.
// ---------------------------------------------------------------------------
function renderBadge(force) {
  const scores = currentScores();
  const showNums = numbersCheckbox.checked();
  const key = scores.join(',') + '|' + showNums;
  if (!force && key === badgeKey) return;
  badgeKey = key;

  const g = badgeG;
  const q = sum(scores.slice(0, 5));
  const total = sum(scores);
  g.clear();
  g.noStroke();

  // Card
  g.stroke(Q_COLOR);
  g.strokeWeight(8);
  g.fill(255);
  g.rect(8, 8, BADGE_W - 16, BADGE_H - 16, 44);
  g.noStroke();

  // Title: open-book icon and the two-line name
  drawBookIcon(g, 150, 68, 42);
  g.fill(INK);
  g.textAlign(CENTER, CENTER);
  g.textStyle(BOLD);
  g.textSize(54);
  g.text('OpenBook', 340, 62);
  g.textSize(28);
  g.fill(Q_COLOR);
  g.text('QR Score', 340, 106);

  // QR-style matrix
  const x0 = 100;
  const y0 = 140;
  const M = 400;
  drawFinder(g, x0, y0);
  drawFinder(g, x0 + M - 84, y0);
  drawFinder(g, x0, y0 + M - 84);
  g.fill(INK);
  for (let i = 0; i < 13; i += 2) g.rect(x0 + 96 + i * 16, y0 + 34, 16, 16);

  for (let i = 0; i < 10; i++) {
    const col = i % 5;
    const row = i < 5 ? 0 : 1;
    drawModule(g, x0 + 4 + col * 80, y0 + 104 + row * 88, scores[i], row === 0 ? Q_COLOR : R_COLOR, showNums);
  }

  // Legend in the bottom-right of the matrix
  g.textAlign(LEFT, CENTER);
  g.textStyle(NORMAL);
  g.textSize(20);
  g.fill(Q_COLOR);
  g.rect(x0 + 108, y0 + M - 70, 22, 22, 4);
  g.fill(INK);
  g.text('Top row: quality (Q)', x0 + 140, y0 + M - 59);
  g.fill(R_COLOR);
  g.rect(x0 + 108, y0 + M - 34, 22, 22, 4);
  g.fill(INK);
  g.text('Bottom row: reusability (R)', x0 + 140, y0 + M - 23);

  // Score text and band
  g.textAlign(CENTER, CENTER);
  g.textStyle(BOLD);
  g.fill(INK);
  g.textSize(qrFontSize(g, qrText(scores)));
  g.text(qrText(scores), BADGE_W / 2, 574);
  const band = bandOf(total);
  g.fill(BAND_COLORS[band]);
  g.rect(BADGE_W / 2 - 90, 606, 180, 38, 19);
  g.fill(255);
  g.textSize(24);
  g.text(band, BADGE_W / 2, 626);
}

function qrFontSize(g, str) {
  let s = 44;
  g.textSize(s);
  while (s > 24 && g.textWidth(str) > BADGE_W - 90) { s -= 2; g.textSize(s); }
  return s;
}

function drawBookIcon(g, cx, cy, s) {
  g.noStroke();
  g.fill(Q_COLOR);
  g.beginShape();
  g.vertex(cx - s, cy - s * 0.55);
  g.vertex(cx - s * 0.06, cy - s * 0.3);
  g.vertex(cx - s * 0.06, cy + s * 0.65);
  g.vertex(cx - s, cy + s * 0.4);
  g.endShape(CLOSE);
  g.fill(R_COLOR);
  g.beginShape();
  g.vertex(cx + s, cy - s * 0.55);
  g.vertex(cx + s * 0.06, cy - s * 0.3);
  g.vertex(cx + s * 0.06, cy + s * 0.65);
  g.vertex(cx + s, cy + s * 0.4);
  g.endShape(CLOSE);
}

function drawFinder(g, x, y) {
  g.noStroke();
  g.fill(INK);
  g.rect(x, y, 84, 84, 8);
  g.fill(255);
  g.rect(x + 12, y + 12, 60, 60, 4);
  g.fill(INK);
  g.rect(x + 24, y + 24, 36, 36, 3);
}

function drawModule(g, x, y, score, color, showNums) {
  const S = 72;
  g.stroke('#b8bfcc');
  g.strokeWeight(3);
  g.fill('#f4f6fb');
  g.rect(x, y, S, S, 8);
  g.noStroke();
  const h = S * score / 10;
  if (h > 0) {
    g.fill(color);
    g.rect(x, y + S - h, S, h, 0, 0, 8, 8);
  }
  if (showNums) {
    g.fill(255);
    g.rect(x + S / 2 - 18, y + S - 34, 36, 28, 6);
    g.fill(INK);
    g.textAlign(CENTER, CENTER);
    g.textStyle(BOLD);
    g.textSize(24);
    g.text(String(score), x + S / 2, y + S - 19);
  }
  if (score < FLOOR) {
    // Below the floor: dashed outline and a "!" mark, so color is not the only signal
    g.noFill();
    g.stroke('#b45309');
    g.strokeWeight(5);
    g.drawingContext.setLineDash([9, 7]);
    g.rect(x - 2, y - 2, S + 4, S + 4, 10);
    g.drawingContext.setLineDash([]);
    g.noStroke();
    g.fill('#b45309');
    g.circle(x + S - 6, y + 6, 26);
    g.fill(255);
    g.textAlign(CENTER, CENTER);
    g.textStyle(BOLD);
    g.textSize(20);
    g.text('!', x + S - 6, y + 7);
  }
}
