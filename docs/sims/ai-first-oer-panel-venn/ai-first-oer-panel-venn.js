// AI-First OER Panel Interest Venn MicroSim (p5.js)
// CANVAS_HEIGHT: 690
// Four translucent circles, one per panelist plus the host. Gold labels mark interests
// all four share. Hover any label to see who shares it. Interests come from public pages
// and email; see index.md Sources. Edit the PEOPLE and REGIONS blocks to update.

const PEOPLE = [
  { key: 'D', name: 'Dan McCreary', role: 'Panelist', col: [65, 105, 225] },
  { key: 'W', name: 'David Wiley', role: 'Panelist', col: [46, 139, 87] },
  { key: 'J', name: 'Joel Gladd', role: 'Panelist', col: [255, 140, 0] },
  { key: 'L', name: 'Delmar Larsen', role: 'Host / moderator', col: [153, 50, 204] }
];
// Layout: D top-left, W top-right, L bottom-left, J bottom-right.
// Diagonal pairs: D+J and W+L.
const REGIONS = [
  { who: 'DWJL', labels: ['AI-first OER', 'Open textbooks'] },
  { who: 'DW', labels: ['Generative AI for learning'] },
  { who: 'DL', labels: ['OER infrastructure'] },
  { who: 'WJ', labels: ['Open pedagogy'] },
  { who: 'JL', labels: ['LibreTexts authoring'] },
  { who: 'DJ', labels: ['AI literacy'] },
  { who: 'WL', labels: ['Lowering textbook costs'] },
  { who: 'D', labels: ['Intelligent textbooks', 'MicroSims', 'Knowledge graphs', 'OER Evaluator rubric'] },
  { who: 'W', labels: ['5R permissions', 'Lumen Learning', 'OER efficacy research'] },
  { who: 'J', labels: ['Writing & rhetoric', 'Community college teaching'] },
  { who: 'L', labels: ['LibreTexts founder', 'Chemistry', 'ADAPT homework'] }
];

const DRAW_H = 630, CTRL_H = 60;
let W = 800, items = [], hovered = null;

function setup() {
  updateCanvasSize();
  const c = createCanvas(W, DRAW_H + CTRL_H);
  c.parent(document.querySelector('main'));
  textFont('Arial');
  describe('Venn diagram of interests shared by the four people on the AI-first OER infrastructure panel.');
}

function geom() {
  const cx = W / 2, cy = 70 + (DRAW_H - 70) / 2;
  const s = min(W / 800, 1);
  const d = 92 * s, r = 158 * s;
  const ctr = { D: [cx - d, cy - d], W: [cx + d, cy - d], L: [cx - d, cy + d], J: [cx + d, cy + d] };
  return { cx, cy, d, r, s, ctr };
}

function regionPos(who, g) {
  const { cx, cy, d, s } = g;
  const k = 1.95 * d;
  const map = {
    DWJL: [cx, cy],
    DW: [cx, cy - 1.55 * d], JL: [cx, cy + 1.55 * d],
    DL: [cx - 1.55 * d, cy], WJ: [cx + 1.55 * d, cy],
    DJ: [cx - 0.55 * d, cy - 0.62 * d], WL: [cx + 0.55 * d, cy + 0.62 * d],
    D: [cx - k, cy - k], W: [cx + k, cy - k],
    L: [cx - k, cy + k], J: [cx + k, cy + k]
  };
  return map[who];
}

function draw() {
  background(250);
  const g = geom();
  noStroke(); fill(30); textAlign(CENTER, TOP); textSize(20 * max(g.s, 0.8));
  text('What would an AI-first OER infrastructure look like?', W / 2, 10);
  textSize(13); fill(90);
  text('Shared interests of the panelists and host. Hover a label to see who shares it.', W / 2, 36);
  for (const p of PEOPLE) {
    const [x, y] = g.ctr[p.key];
    fill(p.col[0], p.col[1], p.col[2], 50); stroke(p.col[0], p.col[1], p.col[2]); strokeWeight(2);
    circle(x, y, 2 * g.r);
  }
  // names on the outer edge of each circle
  textStyle(BOLD); textSize(16 * max(g.s, 0.8)); noStroke();
  for (const p of PEOPLE) {
    const [x, y] = g.ctr[p.key];
    const top = p.key === 'D' || p.key === 'W';
    const left = p.key === 'D' || p.key === 'L';
    const t = p.name + (p.key === 'L' ? ' (host)' : '');
    const tw = textWidth(t);
    let nx = x + (left ? -1 : 1) * g.r * 0.45;
    nx = constrain(nx, tw / 2 + 6, W - tw / 2 - 6);
    const ny = y + (top ? -1 : 1) * (g.r + 14 * max(g.s, 0.8));
    fill(p.col[0] * 0.75, p.col[1] * 0.75, p.col[2] * 0.75);
    textAlign(CENTER, CENTER); text(t, nx, ny);
  }
  textStyle(NORMAL);
  items = []; hovered = null;
  const ts = 12.5 * max(g.s, 0.75);
  textSize(ts);
  for (const rg of REGIONS) {
    const [x, y] = regionPos(rg.who, g);
    const n = rg.labels.length, lh = ts + 9;
    rg.labels.forEach((lab, i) => {
      const yy = y + (i - (n - 1) / 2) * lh;
      const tw = textWidth(lab) + 10;
      const it = { lab, who: rg.who, x, y: yy, w: tw, h: ts + 6 };
      items.push(it);
      if (abs(mouseX - x) < tw / 2 && abs(mouseY - yy) < it.h / 2) hovered = it;
    });
  }
  for (const it of items) {
    const gold = it.who.length === 4;
    fill(gold ? color(255, 215, 0) : color(255, 255, 255, 220));
    stroke(it === hovered ? 0 : (gold ? color(184, 134, 11) : 180)); strokeWeight(it === hovered ? 2 : 1);
    rectMode(CENTER); rect(it.x, it.y, it.w, it.h, 5);
    noStroke(); fill(20); textAlign(CENTER, CENTER); text(it.lab, it.x, it.y);
  }
  // control/info area
  fill(240); noStroke(); rectMode(CORNER); rect(0, DRAW_H, W, CTRL_H);
  fill(30); textAlign(LEFT, CENTER); textSize(14);
  if (hovered) {
    const names = PEOPLE.filter(p => hovered.who.includes(p.key)).map(p => p.name);
    text('"' + hovered.lab + '" is shared by: ' + names.join(', '), 12, DRAW_H + CTRL_H / 2);
  } else {
    fill(255, 215, 0); rect(12, DRAW_H + 23, 14, 14, 3);
    fill(30); text('Gold = shared by all four. Hover any label to see who shares it.', 32, DRAW_H + 30);
  }
}

function windowResized() { updateCanvasSize(); resizeCanvas(W, DRAW_H + CTRL_H); }
function updateCanvasSize() {
  const m = document.querySelector('main');
  W = max(480, m ? m.getBoundingClientRect().width : windowWidth);
}
