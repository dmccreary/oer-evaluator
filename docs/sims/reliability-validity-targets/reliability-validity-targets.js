// Reliability and Validity Targets Poster MicroSim (SVG and JavaScript)
// CANVAS_HEIGHT: 700
// A flat poster with four archery targets, each with a bullseye and six shots. Reliable means the
// shots land close together (reviewers agree). Valid means they land on the bullseye (scores measure
// what matters). The poster prints its own target titles and no numbers, so the sim adds no labels.
// Explore mode: hover, focus, or click a target to read what it means for a rubric.
// Quiz mode: six scenarios. The learner clicks the target that matches, one attempt each. Only the
// first completed run counts as evidence of mastery; hovering in explore mode is exploration.
// The poster is a drawing made for this book (SVG). The shot positions are fixed, not random.
// The MicroSim opens in explore mode with no target selected, and nothing moves until the learner acts.
// To change the facts or the scenarios, edit the DATA block below.

const DATA = {
  title: 'Reliability and Validity Targets Poster',
  itemNoun: 'Scenario',
  shuffle: false,
  attempts: 1,
  passMark: 5,
  passMessage: 'You can tell steady from correct.',
  prompts: {
    explore: 'Hover a target to learn what it means for a rubric.',
    quiz: 'Click the target that matches this scenario.'
  },
  zones: [
    { id: 'reliable-valid', label: 'Reliable and valid', summary: 'Scores are consistent and measure the right thing.',
      facts: ['Reviewers’ scores agree closely.', 'Scores rise with student learning.', 'The ideal rubric.'] },
    { id: 'reliable-not-valid', label: 'Reliable but not valid', summary: 'Scores are consistent but miss what matters.',
      facts: ['Reviewers agree with each other.', 'The rubric may skip something learners need.', 'Agreement alone does not prove the rubric is right.'] },
    { id: 'valid-not-reliable', label: 'Valid on average but not reliable', summary: 'Scores scatter, though their average points the right way.',
      facts: ['Individual scores vary a lot from reviewer to reviewer.', 'The average of many reviewers is close to expert judgment.', 'More reviewers or clearer descriptors would help.'] },
    { id: 'neither', label: 'Neither reliable nor valid', summary: 'Scores scatter and miss what matters.',
      facts: ['Reviewers disagree.', 'The scores do not track learning.', 'The rubric needs redesign.'] }
  ],
  quiz: [
    { prompt: 'Two reviewers always give the same scores, but the scores do not predict whether students learn.', answer: 'reliable-not-valid', why: 'The scores are consistent but do not measure what matters.' },
    { prompt: 'Reviewers’ scores vary widely, but the average across reviewers tracks how students perform.', answer: 'valid-not-reliable', why: 'Individual scores scatter, and the average is on target.' },
    { prompt: 'Scores are consistent across reviewers and rise with student learning gains.', answer: 'reliable-valid', why: 'The scores are both consistent and on target.' },
    { prompt: 'Scores vary from reviewer to reviewer and do not relate to learning.', answer: 'neither', why: 'The scores scatter and miss the target.' },
    { prompt: 'A reviewer re-scores a resource a month later and gets nearly the same numbers, but the rubric never checks accessibility, which blocks many learners.', answer: 'reliable-not-valid', why: 'The scores are steady, and the rubric omits something that matters.' },
    { prompt: 'Reviewers disagree by more than 3 points on half the metrics, yet the group’s average for each metric matches expert judgment.', answer: 'valid-not-reliable', why: 'Individual scores scatter, and the group average is on target.' }
  ],
  correctText: (q, z) => 'Correct: ' + z.label + '. ' + q.why,
  hintText: (q, z) => 'Not quite. Try another target.',
  revealText: (q, z, clicked) => 'Not quite. This is ' + z.label + '. ' + q.why,
  missedText: (q, z) => q.why
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
