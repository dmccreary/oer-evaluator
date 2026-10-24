// Creative Commons License Switches MicroSim (p5.js)
// CANVAS_HEIGHT: 560
// Three switches on a panel: Attribution (BY, always on), ShareAlike (SA) and NonCommercial (NC).
// Flipping SA or NC changes the license name and takes a freedom away from the person who
// receives the work. BY stays on because every Creative Commons license requires credit.
// NoDerivatives (ND) is left out on purpose: this panel covers the three elements that still
// allow adaptation. Text follows the 4.0 licenses and is a study aid, not legal advice.
// The MicroSim opens in its default state (CC BY) and nothing moves until the learner clicks.

// Canvas dimensions: a drawing region above a control region that holds the three switches
let containerWidth; // calculated from the <main> element on init and on resize
let canvasWidth = 400;
let drawHeight = 460; // the drawing region has no controls
let controlHeight = 100; // one row of switches: toggle (34) + two-line label (41) + padding
let canvasHeight = drawHeight + controlHeight;
let containerHeight = canvasHeight;

let pad = 16; // space around the panels in the drawing region
let defaultTextSize = 16;

// Switch state. BY is not a variable because it can never be off.
let shareAlike = false;
let nonCommercial = false;

// Each switch has its own color so the license name can echo it
const BY_COLOR = 'darkgreen';
const SA_COLOR = 'mediumblue';
const NC_COLOR = 'darkmagenta';

// The four licenses reachable with these switches, keyed by the optional elements that are on
const LICENSES = {
  '': {
    official: 'Attribution 4.0 International',
    summary: 'Anyone may copy, adapt, and sell this work if they credit the creator.'
  },
  'SA': {
    official: 'Attribution-ShareAlike 4.0 International',
    summary: 'Anyone may copy, adapt, and sell this work if they credit the creator and share adaptations under this same license.'
  },
  'NC': {
    official: 'Attribution-NonCommercial 4.0 International',
    summary: 'Anyone may copy and adapt this work if they credit the creator, but not for commercial use.'
  },
  'NCSA': {
    official: 'Attribution-NonCommercial-ShareAlike 4.0 International',
    summary: 'Anyone may copy and adapt this work noncommercially if they credit the creator and share adaptations under this same license.'
  }
};

// The freedoms of the person who receives the work. Two are always kept; each remaining
// freedom is taken away by exactly one switch.
const FREEDOMS = [
  {
    label: 'Share the unchanged work',
    takenBy: null,
    note: () => nonCommercial ? 'Allowed for noncommercial use, with credit.'
                              : 'Allowed for any purpose, with credit.'
  },
  {
    label: 'Adapt, translate, remix',
    takenBy: null,
    note: () => nonCommercial ? 'Allowed for noncommercial use, with credit and a note of your changes.'
                              : 'Allowed for any purpose, with credit and a note of your changes.'
  },
  {
    label: 'Use it commercially',
    takenBy: 'NC',
    note: () => nonCommercial ? 'NonCommercial rules out sales, ads, and paid courses.'
                              : 'Sell it, run ads on it, or use it in a paid course.'
  },
  {
    label: "Pick your remix's license",
    takenBy: 'SA',
    note: () => shareAlike ? 'ShareAlike requires your remix to carry this same license.'
                           : 'Release your remix under any license you like.'
  }
];

// Feedback line shown above the license summary
let message = 'Flip a switch below to see which freedom it takes away.';
let messageColor = 'black';

// Flash on a freedom row after the learner changes it (0 = idle). Starts at 0, so nothing moves on load.
let pulse = [0, 0, 0, 0];
let prevKept = [true, true, true, true];

// Switch objects and screen reader helpers
let bySwitch, saSwitch, ncSwitch;
let liveRegion;

let layout = {};

function setup() {
  updateCanvasSize(); // must be first: get the container width before creating the canvas
  const canvas = createCanvas(containerWidth, containerHeight);
  canvas.parent(document.querySelector('main'));
  textSize(defaultTextSize);

  // Native p5.js checkboxes, restyled with CSS so they look like panel switches
  injectSwitchStyles();
  bySwitch = createLicenseSwitch('BY', 'Attribution', BY_COLOR, true);
  saSwitch = createLicenseSwitch('SA', 'ShareAlike', SA_COLOR, false);
  ncSwitch = createLicenseSwitch('NC', 'NonCommercial', NC_COLOR, false);
  bySwitch.input.addEventListener('change', onAttributionClicked);
  saSwitch.input.addEventListener('change', onShareAlikeChanged);
  ncSwitch.input.addEventListener('change', onNonCommercialChanged);
  positionSwitches();

  // Visually hidden live region so screen readers hear the result of each switch
  liveRegion = createDiv('');
  liveRegion.attribute('aria-live', 'polite');
  liveRegion.style('position', 'absolute');
  liveRegion.style('left', '-10000px');
  liveRegion.style('width', '1px');
  liveRegion.style('height', '1px');
  liveRegion.style('overflow', 'hidden');
  announce();
}

function draw() {
  updateCanvasSize();
  computeLayout();

  // Drawing region (aliceblue) and control region (white), both with a silver border
  fill('aliceblue');
  stroke('silver');
  strokeWeight(1);
  rect(0, 0, canvasWidth, drawHeight);
  fill('white');
  rect(0, drawHeight, canvasWidth, controlHeight);

  // Title, shrunk if needed so it fits a narrow container
  fill('black');
  noStroke();
  textStyle(BOLD);
  textSize(fitTextSize('Creative Commons License Switches', canvasWidth - 2 * pad, 24, 18));
  textAlign(CENTER, TOP);
  text('Creative Commons License Switches', canvasWidth / 2, 10);

  drawLicensePlate(layout.plate);
  drawFreedoms(layout.freedoms);
  drawNote(layout.note);
  drawControlDecor();

  // Let the row flashes fade out
  for (let i = 0; i < pulse.length; i++) {
    pulse[i] = max(0, pulse[i] - 0.03);
  }
}

// ---------------------------------------------------------------------------
// Layout: two columns when the container is wide, one stacked column when narrow
// ---------------------------------------------------------------------------
function computeLayout() {
  const top = 44;
  if (canvasWidth >= 800) {
    const gap = 16;
    const leftW = Math.floor((canvasWidth - 2 * pad - gap) / 2);
    layout = {
      wide: true,
      plate: { x: pad, y: top + 2, w: leftW, h: 124 },
      note: { x: pad, y: top + 2 + 124 + 8, w: leftW, h: drawHeight - (top + 2 + 124 + 8) - 14 },
      freedoms: { x: pad + leftW + gap, y: top + 2, w: canvasWidth - 2 * pad - leftW - gap, h: drawHeight - (top + 2) - 14 }
    };
  } else {
    const w = canvasWidth - 2 * pad;
    layout = {
      wide: false,
      plate: { x: pad, y: top, w: w, h: 94 },
      freedoms: { x: pad, y: top + 94 + 8, w: w, h: 166 },
      note: { x: pad, y: top + 94 + 8 + 166 + 8, w: w, h: drawHeight - (top + 94 + 8 + 166 + 8) - 8 }
    };
  }
}

// ---------------------------------------------------------------------------
// Drawing helpers
// ---------------------------------------------------------------------------

// The license "plate": the license name with each element colored like its switch
function drawLicensePlate(r) {
  const lic = currentLicense();
  fill('white');
  stroke('darkslategray');
  strokeWeight(3);
  rect(r.x, r.y, r.w, r.h, 14);
  noStroke();

  const parts = [{ t: 'CC', c: 'black' }, { t: 'BY', c: BY_COLOR }];
  if (nonCommercial) parts.push({ t: '-NC', c: NC_COLOR });
  if (shareAlike) parts.push({ t: '-SA', c: SA_COLOR });
  const full = licenseName();

  textStyle(BOLD);
  const size = fitTextSize(full, r.w - 28, layout.wide ? 48 : 38, 22);
  textSize(size);
  // The name is drawn in pieces so each element can take its switch's color.
  // A space-sized gap separates CC from BY and the elements from the version number.
  const spaceW = textWidth('n') * 0.6;
  const widths = parts.map(p => textWidth(p.t));
  const totalW = widths.reduce((a, b) => a + b, 0) + spaceW * 2 + textWidth('4.0');
  let x = r.x + (r.w - totalW) / 2;
  const nameY = r.y + (layout.wide ? 14 : 8);
  textAlign(LEFT, TOP);
  for (let i = 0; i < parts.length; i++) {
    fill(parts[i].c);
    text(parts[i].t, x, nameY);
    x += widths[i];
    if (i === 0) x += spaceW; // gap between CC and BY
  }
  x += spaceW; // gap before the version
  fill('black');
  text('4.0', x, nameY);

  // Official name under the plate title
  textStyle(NORMAL);
  textSize(defaultTextSize);
  fill('dimgray');
  textAlign(CENTER, TOP);
  const lines = wrapLines(lic.official, r.w - 28);
  for (let i = 0; i < lines.length; i++) {
    text(lines[i], r.x + r.w / 2, nameY + size + 8 + i * 20);
  }
}

// The panel listing the four freedoms of the receiver
function drawFreedoms(r) {
  const wide = layout.wide;
  fill('white');
  stroke('silver');
  strokeWeight(1);
  rect(r.x, r.y, r.w, r.h, 10);

  noStroke();
  fill('black');
  textStyle(BOLD);
  textSize(17);
  textAlign(LEFT, TOP);
  text('Freedoms the receiver keeps', r.x + 14, r.y + 8);

  const headerH = wide ? 38 : 34;
  const meterH = wide ? 46 : 30;
  const rowH = Math.min(80, Math.floor((r.h - headerH - meterH) / FREEDOMS.length));

  for (let i = 0; i < FREEDOMS.length; i++) {
    const f = FREEDOMS[i];
    const kept = freedomKept(i);
    const y = r.y + headerH + i * rowH;
    const cy = wide ? y + 20 : y + rowH / 2;

    // Soft highlight on a row whose state just changed
    if (pulse[i] > 0.01) {
      const flash = color('gold');
      flash.setAlpha(pulse[i] * 130);
      noStroke();
      fill(flash);
      rect(r.x + 4, y, r.w - 8, rowH - 2, 6);
    }

    drawLamp(r.x + 14 + 11, cy, 11 + 3 * pulse[i], kept);
    noStroke(); // the lamp leaves a stroke on; clear it before any text

    // Row label, shrunk a little if the status text needs the room
    const statusText = kept ? 'Kept' : 'Taken by ' + f.takenBy;
    textStyle(BOLD);
    textSize(defaultTextSize);
    const statusW = textWidth(statusText);
    const labelX = r.x + 14 + 22 + 10;
    const labelMaxW = r.x + r.w - 14 - statusW - 10 - labelX;
    textStyle(NORMAL);
    textSize(fitTextSize(f.label, labelMaxW, defaultTextSize, 14));
    fill('black');
    textAlign(LEFT, CENTER);
    text(f.label, labelX, cy);

    textStyle(BOLD);
    textSize(defaultTextSize);
    fill(kept ? 'darkgreen' : 'firebrick');
    textAlign(RIGHT, CENTER);
    text(statusText, r.x + r.w - 14, cy);

    // Detail line, only when the rows are tall enough for it
    if (wide) {
      textStyle(NORMAL);
      textSize(defaultTextSize);
      fill('dimgray');
      textAlign(LEFT, TOP);
      drawWrapped(f.note(), labelX, cy + 14, r.x + r.w - 14 - labelX, 19);
    }
  }

  // Freedom meter: one segment per freedom
  const meterY = r.y + headerH + rowH * FREEDOMS.length + (wide ? 12 : 6);
  const n = keptCount();
  const segW = 30;
  const segGap = 6;
  for (let i = 0; i < FREEDOMS.length; i++) {
    fill(i < n ? 'darkgreen' : 'gainsboro');
    stroke('silver');
    strokeWeight(1);
    rect(r.x + 14 + i * (segW + segGap), meterY, segW, 16, 3);
  }
  noStroke();
  fill('black');
  textStyle(BOLD);
  textSize(defaultTextSize);
  textAlign(LEFT, CENTER);
  text('Freedoms kept: ' + n + ' of ' + FREEDOMS.length,
       r.x + 14 + FREEDOMS.length * (segW + segGap) + 6, meterY + 8);
}

// Round indicator lamp: green with a check when kept, red-outlined with an X when taken
function drawLamp(cx, cy, radius, kept) {
  if (kept) {
    noStroke();
    fill('darkgreen');
    circle(cx, cy, radius * 2);
    stroke('white');
    strokeWeight(3);
    line(cx - 5, cy, cx - 1, cy + 4);
    line(cx - 1, cy + 4, cx + 6, cy - 4);
  } else {
    fill('white');
    stroke('firebrick');
    strokeWeight(3);
    circle(cx, cy, radius * 2 - 3);
    line(cx - 4, cy - 4, cx + 4, cy + 4);
    line(cx + 4, cy - 4, cx - 4, cy + 4);
  }
}

// The box holding the feedback line and the plain-language summary of the license
function drawNote(r) {
  const lic = currentLicense();
  fill('white');
  stroke('silver');
  strokeWeight(1);
  rect(r.x, r.y, r.w, r.h, 10);
  noStroke();

  const size = layout.wide ? 20 : defaultTextSize;
  const lineH = layout.wide ? 28 : 21;
  textSize(size);
  textAlign(LEFT, TOP);
  textStyle(BOLD);
  fill(messageColor);
  let y = drawWrapped(message, r.x + 12, r.y + 8, r.w - 24, lineH);
  textStyle(NORMAL);
  fill('black');
  drawWrapped(lic.summary, r.x + 12, y + 6, r.w - 24, lineH);
}

// Dividers between the three switch cells and a padlock on the locked BY switch
function drawControlDecor() {
  const cellW = canvasWidth / 3;
  stroke('gainsboro');
  strokeWeight(1);
  line(cellW, drawHeight + 10, cellW, canvasHeight - 10);
  line(2 * cellW, drawHeight + 10, 2 * cellW, canvasHeight - 10);

  const lx = cellW / 2 + 34 + 10;
  const ly = drawHeight + 8 + 17;
  noFill();
  stroke('dimgray');
  strokeWeight(2);
  arc(lx + 7, ly - 2, 10, 12, PI, TWO_PI);
  noStroke();
  fill('dimgray');
  rect(lx, ly - 2, 14, 11, 2);
}

// ---------------------------------------------------------------------------
// Text helpers (own word wrap so the layout is the same in every p5.js version)
// ---------------------------------------------------------------------------
function wrapLines(str, maxW) {
  const words = str.split(' ');
  const lines = [];
  let line = '';
  for (const w of words) {
    const test = line ? line + ' ' + w : w;
    if (line && textWidth(test) > maxW) {
      lines.push(line);
      line = w;
    } else {
      line = test;
    }
  }
  if (line) lines.push(line);
  return lines;
}

// Draws left-aligned wrapped text starting at (x, y) and returns the y below the last line
function drawWrapped(str, x, y, maxW, lineH) {
  const lines = wrapLines(str, maxW);
  textAlign(LEFT, TOP);
  for (let i = 0; i < lines.length; i++) {
    text(lines[i], x, y + i * lineH);
  }
  return y + lines.length * lineH;
}

// Largest text size (between minSize and maxSize) at which str fits in maxW
function fitTextSize(str, maxW, maxSize, minSize) {
  let s = maxSize;
  textSize(s);
  while (s > minSize && textWidth(str) > maxW) {
    s -= 1;
    textSize(s);
  }
  return s;
}

// ---------------------------------------------------------------------------
// License model
// ---------------------------------------------------------------------------
function currentLicense() {
  return LICENSES[(nonCommercial ? 'NC' : '') + (shareAlike ? 'SA' : '')];
}

function freedomKept(i) {
  const takenBy = FREEDOMS[i].takenBy;
  if (takenBy === 'NC') return !nonCommercial;
  if (takenBy === 'SA') return !shareAlike;
  return true;
}

function keptCount() {
  let n = 0;
  for (let i = 0; i < FREEDOMS.length; i++) {
    if (freedomKept(i)) n++;
  }
  return n;
}

function licenseName() {
  return 'CC BY' + (nonCommercial ? '-NC' : '') + (shareAlike ? '-SA' : '') + ' 4.0';
}

// ---------------------------------------------------------------------------
// Switch events
// ---------------------------------------------------------------------------
function onAttributionClicked() {
  // BY is locked on: put the switch back and explain why
  bySwitch.input.checked = true;
  message = 'Attribution is locked on. Every Creative Commons license requires credit.';
  messageColor = 'black';
  announce();
}

function onShareAlikeChanged() {
  shareAlike = saSwitch.input.checked;
  message = shareAlike
    ? "ShareAlike is on: picking your remix's license is taken away."
    : "ShareAlike is off: picking your remix's license is given back.";
  messageColor = shareAlike ? 'firebrick' : 'darkgreen';
  flashChangedFreedoms();
  announce();
}

function onNonCommercialChanged() {
  nonCommercial = ncSwitch.input.checked;
  message = nonCommercial
    ? 'NonCommercial is on: using the work commercially is taken away.'
    : 'NonCommercial is off: using the work commercially is given back.';
  messageColor = nonCommercial ? 'firebrick' : 'darkgreen';
  flashChangedFreedoms();
  announce();
}

// Start a flash on every freedom row whose state differs from the last time we looked
function flashChangedFreedoms() {
  for (let i = 0; i < FREEDOMS.length; i++) {
    const kept = freedomKept(i);
    if (kept !== prevKept[i]) pulse[i] = 1;
    prevKept[i] = kept;
  }
}

// Update the screen reader description and the live region
function announce() {
  const text = message + ' The license is now ' + licenseName() + '. ' + currentLicense().summary +
               ' Freedoms kept: ' + keptCount() + ' of ' + FREEDOMS.length + '.';
  // Screen-reader-only description (no LABEL, so no duplicate text appears under the canvas)
  describe('Panel of three switches for Creative Commons elements. Attribution is locked on. ' +
           'ShareAlike and NonCommercial can be turned on or off. ' + text);
  if (liveRegion) liveRegion.html(text);
}

// ---------------------------------------------------------------------------
// Switch controls: native p5.js checkbox + CSS toggle look
// ---------------------------------------------------------------------------
function createLicenseSwitch(code, name, colorName, startOn) {
  const box = createCheckbox('', startOn); // built-in p5.js control
  const input = box.elt.querySelector('input');
  const label = box.elt.querySelector('label');
  // p5.js versions differ in whether the input sits inside the label or beside it.
  // Make it a direct child, before the label, so the CSS sibling selectors work and
  // rewriting the label text below cannot delete the input.
  box.elt.insertBefore(input, label);
  const id = 'cc-switch-' + code.toLowerCase();
  input.id = id;
  label.htmlFor = id; // clicking the label also flips the switch
  label.innerHTML = '<b>' + code + '</b><br>' + name;

  // Visual track and knob; the real input sits on top of them, invisible, and takes the clicks
  const track = document.createElement('span');
  track.className = 'cc-track';
  track.innerHTML = '<span class="cc-knob"></span>';
  box.elt.insertBefore(track, label);

  box.elt.classList.add('cc-switch');
  box.elt.style.setProperty('--sw-color', colorName);
  return { box: box, input: input };
}

// Place the three switches in equal cells of the control region
function positionSwitches() {
  const cellW = canvasWidth / 3;
  const switches = [bySwitch, saSwitch, ncSwitch];
  for (let i = 0; i < switches.length; i++) {
    switches[i].box.position(Math.round(i * cellW), drawHeight + 8);
    switches[i].box.style('width', Math.round(cellW) + 'px');
  }
}

function injectSwitchStyles() {
  if (document.getElementById('cc-switch-styles')) return;
  const style = document.createElement('style');
  style.id = 'cc-switch-styles';
  style.textContent = `
    .cc-switch { margin: 0; padding: 0; text-align: center; font-family: Arial, Helvetica, sans-serif;
                 font-size: 16px; line-height: 1.25; color: black; }
    .cc-switch input { position: absolute; left: 50%; top: 0; width: 68px; height: 34px;
                       margin: 0 0 0 -34px; opacity: 0; cursor: pointer; z-index: 2; }
    .cc-switch .cc-track { display: block; position: relative; width: 68px; height: 34px;
                           margin: 0 auto 6px auto; border-radius: 17px; background: dimgray;
                           transition: background 0.2s; }
    .cc-switch .cc-track::after { content: 'OFF'; position: absolute; right: 9px; top: 0;
                                  line-height: 34px; font-size: 13px; font-weight: bold; color: white; }
    .cc-switch .cc-knob { position: absolute; top: 3px; left: 3px; width: 28px; height: 28px;
                          border-radius: 50%; background: white; transition: left 0.2s; }
    .cc-switch input:checked + .cc-track { background: var(--sw-color); }
    .cc-switch input:checked + .cc-track .cc-knob { left: 37px; }
    .cc-switch input:checked + .cc-track::after { content: 'ON'; left: 10px; right: auto; }
    .cc-switch input:focus-visible + .cc-track { outline: 3px solid black; outline-offset: 2px; }
    .cc-switch label { display: block; cursor: pointer; }
  `;
  document.head.appendChild(style);
}

// ---------------------------------------------------------------------------
// These two functions make the MicroSim width responsive. Keep them at the end of the file.
// ---------------------------------------------------------------------------
function windowResized() {
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  positionSwitches();
  redraw();
}

function updateCanvasSize() {
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width); // avoid fractional pixels
  canvasWidth = containerWidth;
}
