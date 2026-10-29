// Six Creative Commons Licenses Poster MicroSim (SVG and JavaScript)
// CANVAS_HEIGHT: 700
// A flat poster with six equal panels, one per Creative Commons license. The poster prints only the
// six license names, so the sim adds no labels over it. Every other word comes from the DATA block.
// Explore mode: hover, focus, or click a panel to read its summary and facts.
// Quiz mode: six questions. The learner clicks the panel that matches, one attempt each. Only the
// first completed run counts as evidence of mastery; hovering in explore mode is exploration.
// The poster is a drawing made for this book (SVG), not a photograph, and it carries no statistics.
// The MicroSim opens in explore mode with no panel selected, and nothing moves until the learner acts.
// To change the facts or the questions, edit the DATA block below.

const DATA = {
  title: 'Six Creative Commons Licenses Poster',
  itemNoun: 'Question',
  shuffle: false,
  attempts: 1,
  passMark: 5,
  passMessage: 'You can tell the six licenses apart.',
  prompts: {
    explore: 'Hover a panel to learn what the license allows.',
    quiz: 'Click the panel on the poster that matches.'
  },
  zones: [
    { id: 'cc-by', label: 'CC BY', summary: 'Credit is the only condition.',
      facts: ['Credit the creator and link to the license.', 'Share, adapt, and sell, including for profit.', 'All five R permissions remain.', 'The most open of the six.'] },
    { id: 'cc-by-sa', label: 'CC BY-SA', summary: 'Credit, and keep adaptations open the same way.',
      facts: ['Credit the creator.', 'Commercial use is allowed.', 'Every adaptation must carry CC BY-SA.', 'Wikipedia text uses it.'] },
    { id: 'cc-by-nc', label: 'CC BY-NC', summary: 'Credit, and no commercial use.',
      facts: ['Credit the creator.', 'Adaptations are allowed.', 'Use must be noncommercial.', 'Adaptations must stay noncommercial.'] },
    { id: 'cc-by-nc-sa', label: 'CC BY-NC-SA', summary: 'Credit, noncommercial, and the same license on adaptations.',
      facts: ['Credit the creator.', 'Use must be noncommercial.', 'Every adaptation must carry CC BY-NC-SA.'] },
    { id: 'cc-by-nd', label: 'CC BY-ND', summary: 'Credit, and share the work unchanged only.',
      facts: ['Credit the creator.', 'Commercial use is allowed.', 'You may not share a changed version.', 'Private changes are allowed.'] },
    { id: 'cc-by-nc-nd', label: 'CC BY-NC-ND', summary: 'Credit, noncommercial, unchanged only.',
      facts: ['Credit the creator.', 'Use must be noncommercial.', 'You may not share a changed version.', 'The most restrictive of the six.'] }
  ],
  quiz: [
    { prompt: 'Which license allows commercial use and requires every adaptation to carry the same license?', answer: 'cc-by-sa', why: 'SA keeps adaptations open, and without NC, commercial use stays allowed.' },
    { prompt: 'Which license allows noncommercial use only and forbids sharing changed versions?', answer: 'cc-by-nc-nd', why: 'It combines NC and ND.' },
    { prompt: 'Which license allows commercial use but forbids sharing changed versions?', answer: 'cc-by-nd', why: 'ND blocks changed versions, and there is no NC element.' },
    { prompt: 'Which license requires noncommercial use and the same license on every adaptation?', answer: 'cc-by-nc-sa', why: 'It combines NC and SA.' },
    { prompt: 'Which license places no condition on the work beyond credit?', answer: 'cc-by', why: 'BY is the only element.' },
    { prompt: 'Which license allows noncommercial adaptations and does not dictate the adaptation’s license?', answer: 'cc-by-nc', why: 'NC without SA lets adapters choose, as long as use stays noncommercial.' }
  ],
  correctText: (q, z) => 'Correct: ' + z.label + '. ' + q.why,
  hintText: (q, z) => 'Not quite. Try the next panel.',
  revealText: (q, z) => 'Not quite. The answer is ' + z.label + '. ' + q.why,
  missedText: (q, z) => z.label + ': ' + q.why
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
