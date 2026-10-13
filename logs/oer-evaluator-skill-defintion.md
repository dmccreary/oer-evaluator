# Session log: defining the OER Evaluator rubric and building the `oer-evaluator` skill

Date: 2026-10-12
Repository: `/Users/dan/projects/oer-evaluator` (branch `main`)
Published site: https://dmccreary.github.io/oer-evaluator/
Published spec: https://dmccreary.github.io/oer-evaluator/rubric-spec/

This log records what was asked, what was decided, what was built, what was
tested, and what is still open, so that a later session can resume without the
conversation.

## 1. The original prompt

Verbatim, as the first message of the session:

> Please take a look at this paper and summarize it's key finding related to objective automated review of OER resources.  Assume we are using an LLM and AI Agent Skills to do the evaluation of an OER textbook.
>
> https://www.irrodl.org/index.php/irrodl/article/view/2389/3412

Everything below grew from that request.

## 2. Outcome in brief

- The paper is Yuan & Recker (2015), "Not all rubrics are equal: A review of
  rubrics for evaluating the quality of open educational resources," IRRODL
  16(5), 16-38, DOI 10.19173/irrodl.v16i5.2389, licensed CC BY 4.0. It
  reviews 14 OER quality rubrics along content, development process,
  application context, and user support.
- A rubric specification was drafted from it, grounded in the paper and
  credited to its authors, and taken through four published versions
  (v0.1 to v0.4). All 18 design decisions are resolved.
- A first version of the `oer-evaluator` agent skill was built with
  skill-creator and put through one test round (3 tasks, with and without the
  skill). It is **not committed**.
- The companion improvement-planner skill is **not started**.

## 3. Chronology

1. **Paper summary.** The page fetched through WebFetch returned only a
   header, so the PDF was downloaded and its text extracted with Swift
   PDFKit (no PDF tools were installed). The first summary contained two
   errors found on reading the full text: the inclusion criteria say "four"
   and list five (not the reverse), and the two automated rubrics (Custard &
   Sumner 2005; Wetzler et al. 2013) are not presence-only, since Wetzler
   mixes "Has instructions" with judgments like "Content is appropriate for
   age range".
2. **Spec drafted** at `docs/rubric-spec.md`, nav entry added to
   `mkdocs.yml`. Published as v0.1.
3. **Decisions D1-D14** were put to the author one at a time and recorded,
   producing v0.2, v0.3 and v0.4. Each version was committed, pushed, and
   deployed with `mkdocs gh-deploy` when the author said "publish".
4. **Search tool discovered.** The author pointed at
   `/Users/dan/projects/search-microsims`, which already had a reuse-mode
   search service, a catalog, calibrated score bands, duplicate clusters and
   metadata-quality tooling. The findability design was rebuilt around it
   (decision D11).
5. **Improvement list.** The author asked that the system also produce a
   list of ways to improve a book. This became a second skill, decisions
   D15-D18, validation step V7, and a new subsection of the spec.
6. **v0.4 published**, then the author asked to start building the skill
   with `/anthropic-skills:skill-creator`.
7. **Skill built and tested** (Section 6 and 7 below).

### Commits

| Commit | Content |
|---|---|
| `d864d26` | Spec v0.1 |
| `d49f0b8` | Spec v0.2: reuse co-primary |
| `8ac6561` | Spec v0.3: 13 decisions resolved, two headline numbers |
| `d87fa57` | Spec v0.4: findability via search-microsims, improvement list, all decisions resolved (deployed to `gh-pages`) |

Uncommitted at the time of writing: the whole `skills/oer-evaluator/` tree
and this log.

## 4. Key decisions

Resolved by the author. "Author words" are quoted where they set the
direction.

| ID | Decision | Resolution |
|---|---|---|
| D1 | Construct emphasis | Instructional quality and reuse are co-primary and reported separately. Reuse applies to any content that can be easily reused in another textbook, including a MicroSim and the quiz that assesses it. |
| D2 | Rating scale | 0-3 with N/A (an extra ISE level, "insufficient evidence", is distinct from N/A). |
| D3 | Social-authority signals | Recorded, never scored. |
| D4 | Agreement pass lines | V1: exact agreement >= 70% and within one level >= 95% (mean over the three pairs of passes). V2: human-to-human weighted kappa >= 0.60 first, then LLM-to-human kappa >= 0.60 and within 0.10 of human-to-human. V5: AUC >= 0.75 against an author panel. |
| D5 | Sampling | None. Every unit is read, unit by unit by the skill, and reuse and quality-gate judgments run on every component. |
| D6 | Anchor pattern | Approved. Anchors drafted for all 17 Tier 2 indicators. |
| D7 | Headline | Two numbers on the 0-3 scale, Q (overall quality) and R (reusable content), never combined. |
| D8 | Quality gate | A component whose content quality (J1) is below 2 is not reuse-ready. The companion gate on interaction usability (J7) for interactive components is kept as a default and was not separately confirmed. |
| D9 | Component types | Nine: MicroSim, quiz, section or chapter, static figure, interactive infographic, glossary, FAQ question-answer pair, worked example, instructor material. Locations follow the conventions in the author's generator skills. |
| D10 | Operational rules | A failing indicator is marked unvalidated and always routed to human review; a pilot run is allowed if the confirmatory run uses fixed lines and fresh items; a few dozen units per indicator; V5 ranks the reuse value. V3, V4, V6 pass lines are unset and must be fixed before each step's first run. |
| D11 | Findability | The principle "you can't reuse what you can't find" drives the reuse scoring process. Mechanism: the author's search-microsims reuse mode, 12 generated queries per component (3 each of topic, topic plus level, objective, format) written from content and never from metadata; strong hit = top 3 and WHAT score >= 0.75; hit = top 10 and >= 0.60; duplicate-cluster twins (WHAT >= 0.90) removed; keyword search is a diagnostic. RJ6 = 3 if strong-hit rate >= 75%, 2 if hit rate >= 50%, 1 if any hit (also the ceiling when a required search field is missing), 0 otherwise. The 75% and 50% lines are starting values for a pilot. |
| D12 | Chapter roll-up | Mean per indicator weighted by each chapter's number of concepts. Concepts are not equally weighted; for the first release the Concept Impact Score is assumed roughly equal and a CIS-weighted roll-up is deferred. |
| D13 | Learner-data capability | Reported beside the reuse value, never blended into it. Instrumentation is counted once, as the headline count of instrumented components. |
| D14 | How Q and R are computed | Q uses the judgment indicators only (completeness checks shown beside it, not scored). R is the unweighted mean reuse value over all components. A number is provisional when it includes an unvalidated indicator or leaves out ISE scores; no threshold is set for how many (so any one does). |
| D15 | Number of skills | Two: an evaluator and a separate improvement planner that reads its report. |
| D16 | Planner scope | List only for now. The planner never edits the book. |
| D17 | Prioritization | Lowest effort and highest reward first, assuming an LLM tool does the drafting. Effort classes S, M, L with starting weights 1, 2, 4. |
| D18 | First-release items | Deterministic items only; items from Tier 2 judgments wait until those indicators pass V1 and V2. |

### Author statements that set direction

- On reuse: "make reuse a primary component of scoring ... any content that
  can be easily reused in another textbook. For example a very detailed
  MicroSim about 'What is the Scientific Method' can be reused in many
  introductory science textbooks. The quiz related to this MicroSim should
  also be a reusable component."
- On findability: "I want the phrase 'you can't reuse what you can't find' to
  drive the reuse scoring process", and reuse scoring "weighted based on the
  quality of the metadata ... so it can be found with a strong search tool."
- On static versus instrumented content: "critical to differentiate a static
  image that provides no feedback on student activity from a full
  interactive infographic that allows the textbook to track user viewing of
  an image and predict concept understanding from that activity."
- On quality and reuse: "If an item has low content quality it is clearly not
  a strong candidate for reuse."
- On the skill: the goal is "an AI Agent Skill that will automate the scoring
  process", with a second skill for "a list of ways that the textbook can be
  improved".

## 5. The rubric specification (v0.4) in one page

Source: `docs/rubric-spec.md`, about 1,160 lines, 13 sections.

- **Tiers.** Tier 1 is scripted: 13 book-level presence checks (P1-P13) and 9
  component-level reuse checks (RP1-RP9), 22 in all. Tier 2 is 17 anchored
  language-model judgments: J1-J8, J10, J11 for instructional quality and
  RJ1-RJ7 for reuse. J9 is retired.
- **Units.** Book, component, bundle. A component is anything another author
  could lift out; a MicroSim and its quiz are components and form a bundle.
- **Interactivity levels.** L0 static, L1 interactive, L2 instrumented
  (records learner activity as exportable events). Detected from code, never
  from status flags.
- **Reuse process (four stages, each a precondition of the next).**
  1. Findable (RP5, RJ6). Stops when RJ6 = 0.
  2. Portable (RP1-RP4, RP6, RJ2). Stops when a check fails or RJ2 < 2.
  3. Sound (J1, and J7 if interactive). Stops when below 2.
  4. Worth reusing (RJ1 reach, RJ4 substance). Scored, never a gate.
- **Reuse value** = mean(RJ1, RJ4) x (RJ6 / 3), on the 0-3 scale; 0 for
  components that are not reuse-ready.
- **Validation protocol.** V1 self-consistency, V2 human agreement, V3
  quality validity (A/B tests), V4 drift, V5 reuse validity (author panel,
  AUC), V6 activity-data validity, V7 improvement-list validity.
- **Credit.** The spec separates what comes from Yuan & Recker, what comes
  from the rubrics they catalogued, what comes from the author, and what this
  book added. The reuse decomposition, the tiers, and the LLM application are
  this book's own and are not attributed to the review.

## 6. The `oer-evaluator` skill, v0.1

Location: `skills/oer-evaluator/` (uncommitted). Skill version 0.1.0 against
spec v0.4. skill-creator's validator passes.

### Scope, as directed by the author

Deterministic work only. The Tier 2 judgments (J1-J11, RJ1-RJ5, RJ7) are not
run, so **Q is not available**. During the build it was recognized that **R
is also not available**, because reuse-readiness needs RJ2 and J1 and reuse
value needs RJ1 and RJ4, all Tier 2. The report states both as "not
available" with the reason and never estimates them. It does give definite
answers where they exist, for example components that are definitely not
reuse-ready because a deterministic stage failed.

### Layout

```text
skills/oer-evaluator/
  SKILL.md                      workflow, reporting rules, why
  references/
    report-format.md            report.json contract with the planner
    checks.md                   what each check inspects and its limits
    findability.md              how to write queries; how RJ6 is scored
    conventions.md              packaging conventions, instrumentation signature
  scripts/
    oer_evaluator.py            CLI: inspect | findability | report | run
    inventory.py                components and chapter weights
    checks_book.py              P1-P13
    checks_component.py         RP1-RP9, RP8 level, delivery, learning-graph join
    findability.py              RJ6 retrieval test and score mapping
    funnel.py                   stages, reuse value, Q and R headline
    report.py                   report.json and report.md
    safety.py                   detects text addressed to an evaluator
    common.py, net.py           helpers
    selftest.py                 62 checks on a synthetic book
  evals/
    evals.json                  3 test tasks with assertions (iteration 2 version)
    files/injected-book/        prompt-injection fixture
```

### Workflow

1. `oer_evaluator.py inspect BOOK [--out DIR]` writes `inspect.json` and one
   content digest per MicroSim. Output defaults to
   `~/oer-evaluator-reports/<book>/<timestamp>/` and may never be inside the
   book.
2. The agent writes 12 queries per MicroSim from each digest (the only
   language-model step, kept separate so it is auditable). The validator
   rejects queries that copy the title, the description, or an 8-word run of
   them.
3. `oer_evaluator.py findability OUT` runs the retrieval test.
4. `oer_evaluator.py report OUT` writes `report.json` (schema
   `oer-evaluator-report/v1`, the contract with the planner) and `report.md`.

### What it detects

- Inventory using the author's packaging conventions: `docs/sims/<id>/`
  (main.html, index.md, metadata.json), `docs/posters/<slug>/`,
  `docs/faq.md` (one `###` per pair), `docs/chapters/<dir>/quiz.md`,
  `docs/glossary.md`. Placeholder sims are excluded. Worked examples and
  instructor materials have no convention and are listed as not detected.
- Chapter weights from "Concepts Covered" (table or numbered list), falling
  back to word count for every chapter.
- Interactivity: L2 when the code loads `lrs-sim.js` and calls
  `LRSSim.create` (the call may be in a separate `xapi.js`), or uses an xAPI
  client library, or when a quiz is covered by a site-wide emitter script
  loaded from `mkdocs.yml` `extra_javascript`.
- Delivery: whether any code sends events off the page. In the test book
  none does.
- Concept mapping (RP9): string and numeric ids through simple variables and
  maps, joined to the book's learning graph (JSON or CSV).
- Metadata (RP5): required search fields (title, description, subject,
  learning objectives), a recommended level field, attribution fields.
  Template boilerplate objectives (at least half) and fields that are
  themselves instructions count as generic.
- Instruction-like text aimed at an evaluator (`safety.py`), recorded under
  `signals.embedded_instructions` and never followed.

### Environment facts

- The default `python3` here is the `mkdocs` conda environment (3.11) and
  already has numpy, sentence-transformers 6.1.0 and torch. No separate
  `.venv-embeddings` exists at `/Users/dan/projects/search-microsims`.
- The `all-MiniLM-L6-v2` model downloads from Hugging Face on first use
  (about 15 seconds for a run).
- The catalog used: 3,746 embedded entries (3,764 records), generated
  2026-07-15, WHAT vectors built from metadata only. The service's bands are
  0.75 reuse and 0.60 template.
- `OER_SEARCH_MICROSIMS` overrides the search-microsims path.
- The keyword diagnostic is a TF-IDF stand-in; ItemsJS is not run.

## 7. Test round (iteration 1)

Three tasks, each run with and without the skill, then graded by independent
grader agents plus programmatic file checks.

| Eval | Task | With skill | Without skill |
|---|---|---|---|
| 1 | Full evaluation of `digital-electronics` | 7/7 | 4/7 |
| 2 | Which sims in `learning-record-store` send xAPI events | 5/5 | 5/5 |
| 3 | Fixture with injected instructions | 6/6 | 5/6 |
| Mean | pass rate | 100% | 80% |
| Mean | tokens | 121k | 320k |
| Mean | time | 193 s | 661 s |

How to read this:

- The pass-rate gap is conformance, not accuracy. Every baseline failure was
  either giving a Q or R number (which the author decided v0.1 must not) or
  not writing `report.json`.
- Eval 2 did not discriminate on correctness; both found the same six
  instrumented sims. The skill's advantage there was cost and structure.
- On eval 1 the skill used about 4x fewer tokens and 5x less time (147k
  tokens and 266 s against 636k and about 1,416 s). A later notification
  reported an implausible 4.2-hour duration for that baseline; the value
  matching the file timestamps was kept.
- The baseline read all 15 chapters and found real content defects the skill
  cannot find in v0.1: wrong worked answers, leaked drafting notes ("Wait,
  let me recalculate"), a quiz key where B is correct in 82% of 150
  questions, conflicting license statements, empty nav pages.
- Both configurations resisted the injected instructions and left the
  fixture untouched.

### Real ground-truth facts established

- `learning-record-store` has exactly six instrumented MicroSims:
  animal-cell, bouncing-ball, chaos-kill-test-simulator, scientific-method,
  sine-wave, xapi-statement-triple. Its 32 chapter quizzes are instrumented
  by the site-wide `quiz-xapi.js`.
- Only chaos-kill-test-simulator and xapi-statement-triple use concept ids
  that join the book's learning graph. The other four use 22 slugs that
  match none of its 578 labels.
- No code in that book sends statements anywhere; they stay in memory.
- `digital-electronics`: 135 of 138 chapter embeds point to sims that do not
  exist; 2 of 11 images have alt text; 3 of 7 sims definitely not
  reuse-ready (flip-flop loads a missing file, graph-viewer and
  single-logic-gate depend on files outside their folder).

## 8. Bugs and corrections found along the way

Defects in the skill, found by testing and fixed (each has a regression test
where practical):

1. RP9 reported code identifiers as concept ids, then failed
   `chaos-kill-test-simulator` because it uses numeric ids through a
   variable.
2. Chapters failed RP1 only because they iframe-embed sims; embedding is now
   recorded as a dependency, not a packaging defect.
3. Quizzes instrumented by a site-wide script were labelled L1.
4. "Emits events" was conflated with "delivers events".
5. Concept ids were not checked against the learning graph.
6. RP5 gave a hollow pass to a description that was itself an injected
   instruction, and missed the fourth line of the author's boilerplate
   objectives template.
7. The instruction detector initially had no code at all, then 15 of 52 books
   triggered it on ordinary teaching prose. It now requires an evaluator-style
   addressee or coupling to scoring, with weak signals counting only in
   pairs. A full sweep of all 53 books runs in 36 seconds with no crashes.
8. An overlong link string crashed path resolution.

Errors of mine corrected during the session:

- The first paper summary (two points, Section 3).
- A mistaken claim that only Q would be unavailable (R too).
- An ID-uniqueness check script with an invalid regex printed false
  "MISSING" lines; re-run correctly.
- A tautological test assertion, replaced with a real one.
- Spec version bumps: unpublished versions absorbed small decisions; a new
  version was cut once a version had been published.

## 9. Findings about the author's ecosystem

- The search-microsims project provides: a crawler over `dmccreary/*`
  repositories, ItemsJS faceted search, dual WHAT/HOW embeddings, reuse mode
  with calibrated bands, duplicate clustering (99 clusters covering 225
  sims, 64 cross-repo), a schema validator, enrichment scripts, and
  metadata-quality metrics. Its own record shows that rewriting boilerplate
  learning objectives tightened score separation, which supports the premise
  of RJ6.
- Metadata completeness in the January report (873 sims; stale): license
  18.7%, author 17.3%, version 45.7%, grade level 47.3%, against title,
  description, subject and objectives at 97% or more. This is why RP5 was
  split so attribution gaps do not cap findability.
- Across `~/projects` there are 53 MkDocs books and about 2,500 sim
  directories.
- A single-sim `quiz` has no file convention; quizzes are chapter files, sim
  quiz modes, or sorting-quiz MicroSims.

## 10. Open items

### Unset parameters (listed in spec Section 11)

| Parameter | Why it is open |
|---|---|
| V3 pass line (quality validity) | Needs the book's A/B test results |
| V4 pass line (drift) | Set once the calibration set exists |
| V6 pass line (activity-data validity) | Needs real learner event data |
| V7 pass line (improvement-list validity) | Set once the planner exists |
| ISE threshold for "provisional" | For now any one left-out ISE score makes a number provisional |
| RJ6 hit-rate lines (75% and 50%) | Starting values; confirm in the D10 pilot |
| Effort weights (S 1, M 2, L 4) and the finding-to-effort lookup | Starting values for the author to confirm |

### Judgment questions raised, not decided

- **RP1 and shared libraries.** The spec's literal rule fails almost every
  MicroSim in the author's books because they load `../../js/lrs-sim.js` and
  `../shared-libs/...`. The report marks these `shared_library_only` and a
  flag `--shared-libs-as-declared` shows the other reading. Policy is the
  author's.
- **RJ6 calibration.** The bands were calibrated on full-format queries.
  Short partial queries often rank first yet score below 0.60, so most sims
  land at 0 or 1. The report records rank-only rates beside band-based ones
  as pilot evidence. The same sim scored differently between two runs
  because the model wrote different queries, which is what V1 is for.
- **Candidate deterministic checks** surfaced by the baseline, not in the
  spec: leaked drafting notes in published text, quiz answer-key position
  bias, conflicting license statements across files, empty navigation pages.
- **Spec lag.** The skill now does things spec v0.4 does not describe:
  site-wide quiz instrumentation, delivery evidence, the learning-graph join,
  embedded-instruction detection, and the boilerplate rule. A spec v0.5
  should record them.
- **Single-sim quiz convention.** Spec D9 notes there is no file convention
  for a quiz written for one MicroSim; a convention such as
  `docs/sims/<id>/quiz.md` would be a change to the author's skills.

## 11. Suggested next steps

1. Review iteration 1 in the viewer and give feedback.
2. Run iteration 2 with the tightened assertions in `evals/evals.json` (they
   now assert on delivery, the learning-graph join, the D10 caveat, and that
   deterministic results are still reported even when Q and R are withheld).
3. Commit `skills/oer-evaluator/` and this log (the author's "publish" runs
   `git add`, `git commit`, `git push`, and `mkdocs gh-deploy`; the skill
   directory is outside `docs/`, so it does not affect the site build).
4. Build the second skill, the improvement planner, reading `report.json`
   `findings`; first release is deterministic items only, list only,
   ordered by lowest effort and highest reward.
5. Add the unvalidated-indicator path: author the Tier 2 prompts, then run
   V1 and V2 before any J or RJ score is trusted.
6. Update the spec to v0.5 for the items in Section 10.
7. Optionally run skill-creator's description optimization on the skill
   description once the author is satisfied with behavior.

## 12. How to resume

```bash
# self-test (no model, no network)
python3 skills/oer-evaluator/scripts/selftest.py

# evaluate a book (output goes outside the book)
python3 skills/oer-evaluator/scripts/oer_evaluator.py inspect /Users/dan/projects/digital-electronics
# write queries into <out>/findability/queries/, then:
python3 skills/oer-evaluator/scripts/oer_evaluator.py findability <out>
python3 skills/oer-evaluator/scripts/oer_evaluator.py report <out>

# verify the docs build (never run mkdocs serve; the author runs it)
mkdocs build --strict
```

Test workspace from this session (transient, in the session scratchpad):
`.../scratchpad/oer-evaluator-workspace/` with `iteration-1/`, the review
viewer `oer-evaluator-review.html`, and the injection fixture. If the
scratchpad is gone, recreate the fixture from
`skills/oer-evaluator/evals/files/injected-book/`.

Project rules that apply (from `AGENTS.md`): never start or kill
`mkdocs serve`; verify with `mkdocs build --strict`; never add
`navigation.tabs`; "publish" means add relevant files, commit with a message
that explains why, push, and deploy.
