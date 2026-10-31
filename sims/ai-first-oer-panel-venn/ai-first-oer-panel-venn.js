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

// Glossary: each label maps to a term in docs/glossary.md (definition copied from there).
const GLOSSARY_URL = '../../glossary/';
const TERMS = {
  "AI-first OER": {
    "term": "AI-First OER",
    "def": "An open educational resource whose source files, metadata, and structure are designed from the start so that AI tools can generate, adapt, evaluate, and personalize it.",
    "anchor": "ai-first-oer"
  },
  "Open textbooks": {
    "term": "Open Textbook",
    "def": "A full-length textbook released under a license that lets anyone read it online, adapt it, and share it without paying the publisher.",
    "anchor": "open-textbook"
  },
  "Generative AI for learning": {
    "term": "Generative AI",
    "def": "A type of AI model that produces new text, images, code, or other content in response to a prompt, based on patterns learned from training data.",
    "anchor": "generative-ai"
  },
  "OER infrastructure": {
    "term": "OER Infrastructure",
    "def": "The shared platforms, tools, standards, and services used to write, store, find, adapt, deliver, and evaluate open educational resources.",
    "anchor": "oer-infrastructure"
  },
  "Open pedagogy": {
    "term": "Open Pedagogy",
    "def": "A teaching approach in which students help create, revise, or share openly licensed materials as a regular part of their coursework, and do not only consume them.",
    "anchor": "open-pedagogy"
  },
  "LibreTexts authoring": {
    "term": "LibreTexts",
    "def": "A nonprofit open education project, founded by Delmar Larsen at the University of California, Davis, that hosts openly licensed textbooks and the tools to write and remix them.",
    "anchor": "libretexts"
  },
  "AI literacy": {
    "term": "AI Literacy",
    "def": "The knowledge and skills a person needs to understand what AI tools can and cannot do, to use them well, and to judge their outputs and risks.",
    "anchor": "ai-literacy"
  },
  "Lowering textbook costs": {
    "term": "Course Material Affordability",
    "def": "The extent to which the total price of textbooks and other course materials is low enough that students can obtain every item they need.",
    "anchor": "course-material-affordability"
  },
  "Intelligent textbooks": {
    "term": "Intelligent Textbook",
    "def": "A textbook built as a website from a learning graph, chapters in dependency order, a glossary, quizzes, and interactive simulations called MicroSims.",
    "anchor": "intelligent-textbook"
  },
  "MicroSims": {
    "term": "MicroSim",
    "def": "A small, interactive, browser-based educational simulation that can be embedded in a web page with an iframe, usually built with p5.js, and published under an open license.",
    "anchor": "microsim"
  },
  "Knowledge graphs": {
    "term": "Knowledge Graph",
    "def": "A data structure that represents entities as nodes and the relationships between them as labeled edges, so that both can be queried.",
    "anchor": "knowledge-graph"
  },
  "OER Evaluator rubric": {
    "term": "Ten-Metric Rubric",
    "def": "A scoring guide that rates an open educational resource on ten metrics, five for quality and five for reusability, each worth 10 points, for a total of 100.",
    "anchor": "ten-metric-rubric"
  },
  "5R permissions": {
    "term": "The 5R Permissions",
    "def": "A framework, described by David Wiley, of five permissions that together define an open resource: retain, reuse, revise, remix, and redistribute.",
    "anchor": "the-5r-permissions"
  },
  "Lumen Learning": {
    "term": "Lumen Learning",
    "def": "A company, co-founded by David Wiley, that builds courseware for college courses from open educational resources.",
    "anchor": "lumen-learning"
  },
  "OER efficacy research": {
    "term": "OER Efficacy Research",
    "def": "Research that measures whether using open educational resources changes student outcomes, such as grades, course completion, or cost, compared with commercial materials.",
    "anchor": "oer-efficacy-research"
  },
  "Writing & rhetoric": {
    "term": "Writing and Rhetoric",
    "def": "The academic field that studies and teaches how writers compose texts for a particular audience and purpose.",
    "anchor": "writing-and-rhetoric"
  },
  "Community college teaching": {
    "term": "Community College",
    "def": "A public two-year college that offers associate degrees, certificates, and courses that transfer to four-year schools, usually with open admission.",
    "anchor": "community-college"
  },
  "LibreTexts founder": {
    "term": "LibreTexts",
    "def": "A nonprofit open education project, founded by Delmar Larsen at the University of California, Davis, that hosts openly licensed textbooks and the tools to write and remix them.",
    "anchor": "libretexts"
  },
  "Chemistry": {
    "term": "Chemistry",
    "def": "The science of the composition, structure, properties, and reactions of matter.",
    "anchor": "chemistry"
  },
  "ADAPT homework": {
    "term": "ADAPT Homework System",
    "def": "The open online homework and assessment system run by LibreTexts, in which instructors build, share, and automatically grade problem sets.",
    "anchor": "adapt-homework-system"
  }
};

const DRAW_H = 630, CTRL_H = 60;
let W = 800, items = [], hovered = null, pinned = null, box;

function setup() {
  updateCanvasSize();
  const c = createCanvas(W, DRAW_H + CTRL_H);
  c.parent(document.querySelector('main'));
  textFont('Arial');
  const m = document.querySelector('main'); m.style.position = 'relative';
  box = createDiv(''); box.parent(m); box.style('display', 'none');
  box.style('position', 'absolute'); box.style('max-width', '300px'); box.style('background', 'white');
  box.style('border', '2px solid #b8860b'); box.style('border-radius', '8px'); box.style('padding', '10px 12px');
  box.style('font', '14px Arial'); box.style('line-height', '1.35'); box.style('box-shadow', '0 2px 8px rgba(0,0,0,.25)');
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
  text('Shared interests of the panelists and host. Hover or click a label to learn more.', W / 2, 36);
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
  if (frameCount === 2 && location.hash.startsWith('#pin=')) {
    pinned = items.find(i => i.lab === decodeURIComponent(location.hash.slice(5))) || null; // for screenshots
  }
  updateInfo();
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
    fill(30); text('Gold = shared by all four. Hover or click a label for its definition.', 32, DRAW_H + 30);
  }
}

function windowResized() { updateCanvasSize(); resizeCanvas(W, DRAW_H + CTRL_H); }
function updateCanvasSize() {
  const m = document.querySelector('main');
  W = max(480, m ? m.getBoundingClientRect().width : windowWidth);
}

function namesFor(it) { return PEOPLE.filter(p => it.who.includes(p.key)).map(p => p.name); }

// Infobox: hover a label to preview, click to pin (so the glossary link can be clicked).
let shown = null;
function updateInfo() {
  const it = pinned || hovered;
  if (it === shown) return;
  shown = it;
  if (!it) { box.style('display', 'none'); return; }
  const t = TERMS[it.lab];
  box.html('<b>' + it.lab + '</b><br>' + t.def +
    '<br><br><b>Shared by:</b> ' + namesFor(it).join(', ') +
    '<br><a href="' + GLOSSARY_URL + '#' + t.anchor + '" target="_blank">Glossary: ' + t.term + '</a>' +
    (pinned ? '' : '<br><i style="color:#666">Click the label to pin this box.</i>'));
  const bw = 300, left = constrain(it.x - bw / 2, 4, W - bw - 4);
  box.style('display', 'block');
  const bh = box.elt.offsetHeight;
  const top = it.y > DRAW_H / 2 ? it.y - it.h / 2 - bh - 8 : it.y + it.h / 2 + 8;
  box.position(left, max(4, top));
}

function mousePressed() {
  if (mouseY < 0 || mouseY > DRAW_H + CTRL_H || mouseX < 0 || mouseX > W) return;
  pinned = (hovered && hovered !== pinned) ? hovered : null;
  shown = undefined;
}
