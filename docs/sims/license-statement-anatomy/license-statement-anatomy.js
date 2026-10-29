// Anatomy of a License Statement MicroSim (SVG and JavaScript)
// CANVAS_HEIGHT: 700
// A text-free flat drawing of the bottom of a lesson web page: a picture with a caption strip above
// a footer bar. Seven numbered markers point at the parts of a complete license statement. Every
// label comes from the DATA block, not from the drawing.
// Explore mode: hover, focus, or click a marker to read its label, description, and tip.
// Quiz mode: seven hints that describe how a part looks. The learner clicks the marker that matches,
// with two attempts each. Only a correct first click counts as evidence of mastery, and only on the
// first completed run. Hovering markers in explore mode is exploration.
// The drawing is made for this book (SVG). It carries no statistics.
// The MicroSim opens in explore mode with nothing selected, and nothing moves until the learner acts.
// To change the parts or the hints, edit the DATA block below.

const PARTS = [
  { id: '1', label: 'License badge icons', hint: 'A row of four small round icons at the left of the footer.',
    description: 'The icons show at a glance which license elements apply. They are a hint, not the license itself.',
    tip: 'Icons are easy to copy onto a page with no license, so always confirm the written statement.' },
  { id: '2', label: 'License name and version', hint: 'Two short stacked lines of text beside the icons.',
    description: 'The exact license name, for instance Creative Commons Attribution 4.0 International. The version matters because terms differ between versions.',
    tip: '“CC BY” alone leaves the version open. Write the full name or the version number.' },
  { id: '3', label: 'Link to the license', hint: 'An underlined bar that looks like a hyperlink.',
    description: 'A link to the license page, so readers can check the real terms.',
    tip: 'Check that the link goes to the Creative Commons site and not to a copy.' },
  { id: '4', label: 'Copyright holder and year', hint: 'A copyright symbol beside a short name line.',
    description: 'Names who holds the copyright and when. This is the person to credit and the person to ask for permission.',
    tip: 'The work of a school employee may belong to the school, so the named holder is the one to ask.' },
  { id: '5', label: 'Scope of the license', hint: 'A thin line directly under the license name.',
    description: 'States what the license covers: this page, the whole book, or only the text.',
    tip: 'A missing scope is a question to ask the owner, not an assumption.' },
  { id: '6', label: 'Notice for third-party content', hint: 'The thin caption strip beneath the picture thumbnail.',
    description: 'Marks material that someone else owns or that carries a different license, for instance a photo used with permission.',
    tip: 'Treat each image as separately licensed until its caption says otherwise.' },
  { id: '7', label: 'Machine-readable license marking', hint: 'The small code-bracket icon at the far right of the footer.',
    description: 'Hidden markup, like a link marked rel="license", lets search tools filter by license. Readers cannot see it on the page.',
    tip: 'Look in the page source, or use a search tool’s license filter.' }
];

const DATA = {
  title: 'Anatomy of a License Statement',
  itemNoun: 'Hint',
  shuffle: true,
  attempts: 2,
  passMark: 6,
  passMessage: 'You can find every part of a license statement.',
  prompts: {
    explore: 'Hover a marker to see what it is.',
    quiz: 'Click the numbered marker that matches the hint.'
  },
  zones: PARTS.map(p => ({ id: p.id, label: p.label, summary: p.description, facts: [], tip: p.tip,
                           ariaLabel: 'Marker ' + p.id + ': ' + p.label + '. ' + p.description, quizLabel: 'Marker ' + p.id })),
  quiz: PARTS.map(p => ({ prompt: 'Hint: ' + p.hint, answer: p.id, hint: p.hint, description: p.description })),
  correctText: (q, z) => 'Correct: ' + z.label + '. ' + q.description,
  hintText: (q, z) => 'Not quite. Look again at the hint: ' + q.hint,
  revealText: (q, z) => 'This is ' + z.label + '. ' + q.description,
  missedText: (q, z) => z.label
};

// ---------------------------------------------------------------------------
// Poster engine. Everything above this line is content (DATA); everything below is code.
// Explore mode: hover, focus, or click a zone to read about it. Quiz mode: the learner clicks the
// zone that matches a prompt. Only the first click on each question, on the first completed run,
// counts as evidence of mastery. Nothing moves or changes until the learner acts.
// ---------------------------------------------------------------------------
(function () {
  const svg = document.getElementById('poster');
  const panel = document.getElementById('panel');
  const progress = document.getElementById('progress');
  const btnExplore = document.getElementById('btn-explore');
  const btnQuiz = document.getElementById('btn-quiz');
  const btnNext = document.getElementById('btn-next');
  const btnAgain = document.getElementById('btn-again');
  const zoneEls = Array.from(svg.querySelectorAll('.zone'));
  const byId = {};
  DATA.zones.forEach(z => {
    z.ariaLabel = z.ariaLabel || (z.label + '. ' + z.summary);
    z.quizLabel = z.quizLabel || z.label;
    byId[z.id] = z;
  });

  let mode = 'explore'; // 'explore' | 'quiz'
  let hoverId = null; // zone under the pointer or focus (explore mode)
  let pinnedId = null; // zone the learner clicked (explore mode)
  let firstRunDone = false; // the first completed quiz run is the one that counts as evidence
  let run = null; // { order, pos, tries, phase, results, wrong, feedback, practice }

  // --- small DOM helpers (text goes in with textContent) -----------------------------------
  function el(tag, cls, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }
  function zoneEl(id) { return zoneEls.find(z => z.dataset.zone === id); }

  // --- zones: make each one a keyboard-reachable button -------------------------------------
  zoneEls.forEach(ze => {
    const z = byId[ze.dataset.zone];
    ze.setAttribute('tabindex', '0');
    ze.setAttribute('role', 'button');
    ze.addEventListener('mouseenter', () => { if (mode === 'explore') { hoverId = z.id; render(); } });
    ze.addEventListener('mouseleave', () => { if (mode === 'explore') { hoverId = null; render(); } });
    ze.addEventListener('focus', () => { if (mode === 'explore') { hoverId = z.id; render(); } });
    ze.addEventListener('blur', () => { if (mode === 'explore') { hoverId = null; render(); } });
    ze.addEventListener('click', () => onZone(z.id));
    ze.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onZone(z.id); } });
  });

  btnExplore.addEventListener('click', () => { mode = 'explore'; hoverId = null; render(); });
  btnQuiz.addEventListener('click', () => { startRun(); });
  btnNext.addEventListener('click', () => { next(); });
  btnAgain.addEventListener('click', () => { startRun(); });

  // --- quiz logic ---------------------------------------------------------------------------
  function startRun() {
    mode = 'quiz';
    const order = DATA.quiz.map((_, i) => i);
    if (DATA.shuffle) {
      for (let i = order.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [order[i], order[j]] = [order[j], order[i]];
      }
    }
    run = { order: order, pos: 0, tries: 0, phase: 'question', results: [], wrong: [], feedback: null, practice: firstRunDone };
    render();
  }

  function current() { return DATA.quiz[run.order[run.pos]]; }

  function onZone(id) {
    if (mode === 'explore') { pinnedId = pinnedId === id ? null : id; render(); return; }
    if (!run || run.phase !== 'question' || run.wrong.includes(id)) return;
    const item = current();
    run.tries++;
    if (id === item.answer) {
      run.results[run.pos] = { item: item, firstTry: run.tries === 1 };
      run.feedback = { kind: 'good', text: DATA.correctText(item, byId[item.answer]) };
      run.phase = 'feedback';
      run.clicked = id;
    } else if (run.tries < DATA.attempts) {
      run.wrong.push(id);
      run.feedback = { kind: 'hint', text: DATA.hintText(item, byId[item.answer], byId[id]) };
    } else {
      run.wrong.push(id);
      run.results[run.pos] = { item: item, firstTry: false };
      run.feedback = { kind: 'bad', text: DATA.revealText(item, byId[item.answer], byId[id]) };
      run.phase = 'feedback';
      run.clicked = id;
    }
    render();
  }

  function next() {
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

  function score() { return run.results.filter(r => r.firstTry).length; }

  // --- rendering ----------------------------------------------------------------------------
  function render() {
    // mode buttons
    btnExplore.setAttribute('aria-pressed', mode === 'explore' ? 'true' : 'false');
    btnQuiz.setAttribute('aria-pressed', mode === 'quiz' ? 'true' : 'false');
    btnExplore.classList.toggle('on', mode === 'explore');
    btnQuiz.classList.toggle('on', mode === 'quiz');

    // zone state classes and accessible names
    const shown = mode === 'explore' ? (hoverId || pinnedId) : null;
    zoneEls.forEach(ze => {
      const id = ze.dataset.zone;
      const z = byId[id];
      ze.classList.toggle('active', id === shown);
      ze.classList.remove('correct', 'wrong');
      if (mode === 'quiz' && run) {
        if (run.phase === 'feedback' || run.phase === 'summary') {
          if (run.phase === 'feedback' && id === current().answer) ze.classList.add('correct');
        }
        if (run.wrong.includes(id)) ze.classList.add('wrong');
      }
      ze.setAttribute('aria-label', mode === 'explore' ? z.ariaLabel : z.quizLabel);
    });

    // progress segments
    progress.textContent = '';
    if (mode === 'quiz' && run) {
      DATA.quiz.forEach((_, i) => {
        const s = el('span', 'seg');
        const r = run.results[i];
        if (r) s.classList.add(r.firstTry ? 'ok' : 'miss');
        if (i === run.pos && run.phase !== 'summary') s.classList.add('cur');
        progress.appendChild(s);
      });
    }

    // buttons in the action row
    const inQuiz = mode === 'quiz' && run;
    btnNext.hidden = !(inQuiz && (run.phase === 'feedback' || run.phase === 'question'));
    btnNext.disabled = !(inQuiz && run.phase === 'feedback');
    btnNext.textContent = inQuiz && run.pos >= run.order.length - 1 ? 'See results' : 'Next →';
    btnAgain.hidden = !(inQuiz && run.phase === 'summary');

    // panel
    panel.textContent = '';
    if (mode === 'explore') {
      const z = shown ? byId[shown] : null;
      if (!z) {
        panel.appendChild(el('p', 'prompt', DATA.prompts.explore));
      } else {
        panel.appendChild(el('h2', '', z.label));
        panel.appendChild(el('p', 'summary', z.summary));
        if (z.facts && z.facts.length) {
          const ul = el('ul');
          z.facts.forEach(f => ul.appendChild(el('li', '', f)));
          panel.appendChild(ul);
        }
        if (z.tip) panel.appendChild(el('p', 'tip', 'Tip: ' + z.tip));
      }
      return;
    }
    if (run.phase === 'summary') { renderSummary(); return; }
    const item = current();
    panel.appendChild(el('p', 'qhead', (run.practice ? 'Practice ' : DATA.itemNoun + ' ') + (run.pos + 1) + ' of ' + run.order.length));
    panel.appendChild(el('p', 'question', item.prompt));
    if (run.feedback) {
      const fb = el('p', 'feedback ' + run.feedback.kind);
      fb.textContent = run.feedback.text;
      panel.appendChild(fb);
    } else {
      panel.appendChild(el('p', 'prompt', DATA.prompts.quiz));
    }
  }

  function renderSummary() {
    const total = run.results.length;
    const n = score();
    const passed = n >= DATA.passMark;
    panel.appendChild(el('h2', passed ? 'pass' : '', run.practice
      ? n + ' of ' + total + ' correct on this practice run'
      : n + ' of ' + total + ' correct on the first attempt'));
    if (run.practice) {
      panel.appendChild(el('p', '', 'Practice runs do not change your first-run score.'));
    } else {
      panel.appendChild(el('p', '', passed ? DATA.passMessage : 'Mastery is ' + DATA.passMark + ' of ' + total + ' on the first attempt. Review the misses below, then play again.'));
    }
    const missed = run.results.filter(r => !r.firstTry);
    if (missed.length) {
      panel.appendChild(el('p', 'qhead', 'Missed:'));
      const ul = el('ul');
      missed.forEach(r => ul.appendChild(el('li', '', DATA.missedText(r.item, byId[r.item.answer]))));
      panel.appendChild(ul);
    }
  }

  render();
})();
