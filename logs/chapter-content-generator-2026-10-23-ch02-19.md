# Chapter Content Generator Session Log: Chapters 2 to 19

**Skill Version:** 1.11
**Date:** 2026-10-23
**Execution Mode:** Sequential (one chapter at a time, each logged before the next began)
**Reading level applied:** College / professional development, in plain language, as in the Chapter 1 session
(`logs/chapter-content-generator-2026-10-23.md`).
**Request:** "continue to generate the chapter content using the /chapter-content-generator skill for chapters 2 to 19.
Be aware of the rich types of overlay infographic posters that can be added to the chapter content. Be aggressive at
looking for opportunities to insert MicroSims in the text."

## Timing

Per-chapter start and end times are in `logs/ch-NN-content-generation.md`.

| Metric | Value |
|--------|-------|
| Start Time (Chapter 2) | 2026-10-23 21:34:27 |
| End Time (Chapter 19) | 2026-10-23 23:16:07 |
| Elapsed Time | 1 hour 41 minutes 40 seconds (wall clock) |
| Sum of per-chapter times | 1 hour 40 minutes 17 seconds |

The Chapter 18 start time was not recorded when that chapter began. The value in `logs/ch-18-content-generation.md`
(23:06:36) is the end time of Chapter 17, which is when Chapter 18 work started, so it is approximate. Token usage was
not measured.

## Setup checks (Steps 1.3a and 1.3b)

- Edge direction validated with `prereqs[edge['from']].add(edge['to'])`: six foundational concepts, all introductory.
- Dependency order re-checked at the end of the session from each chapter's "Concepts Covered" table: 351 of 351
  concepts mapped to a chapter, 586 dependencies, 0 violations.
- `cis_max` = 10324, global.
- MicroSim reuse search: NOT AVAILABLE on this machine, so no existing sims were reused. Reused: 0. From template: 0.
  Newly specified: 146 in Chapters 2 to 19 (149 with Chapter 1). Every specification has `Status: Specified`; none is
  built.

## Results

| Chapter | Directory | Prose words | Budget | Specs | Mascots | Concepts in range / under / over | Elapsed |
|---|---|---|---|---|---|---|---|
| 2 | open-licenses-attribution | 5,215 | 4,430-7,100 | 7 | 9 | 2 / 17 / 4 | 8m 43s |
| 3 | ten-metric-rubric-scoring | 8,171 | 8,200-12,550 | 9 | 10 | 5 / 17 / 3 | 10m 21s |
| 4 | open-formats-version-control | 4,092 | 2,600-4,200 | 7 | 7 | 9 / 1 / 3 | 4m 59s |
| 5 | accuracy-currency | 4,030 | 2,830-4,500 | 8 | 6 | 6 / 6 / 2 | 5m 07s |
| 6 | alignment-readability | 5,484 | 4,430-7,200 | 10 | 9 | 6 / 17 / 2 | 6m 07s |
| 7 | accessibility | 4,588 | 3,280-5,400 | 9 | 7 | 9 / 12 / 2 | 5m 03s |
| 8 | practice-feedback | 3,385 | 2,680-4,400 | 8 | 6 | 7 / 11 / 0 | 3m 53s |
| 9 | modularity-metadata | 5,489 | 4,580-7,400 | 7 | 7 | 5 / 16 / 2 | 4m 46s |
| 10 | portability-reuse | 2,184 | 1,570-2,600 | 4 | 4 | 1 / 11 / 0 | 2m 04s |
| 11 | manual-evaluation-adoption | 2,257 | 1,830-2,950 | 3 | 4 | 4 / 6 / 1 | 2m 13s |
| 12 | ai-agents-prompts-scoring | 7,129 | 7,080-10,850 | 11 | 9 | 3 / 17 / 2 | 6m 17s |
| 13 | automated-checks-cost-privacy | 2,506 | 1,720-2,750 | 5 | 5 | 4 / 4 / 1 | 2m 27s |
| 14 | checking-agent-output | 7,138 | 6,080-9,450 | 11 | 7 | 3 / 14 / 5 | 10m 00s |
| 15 | improving-resources-with-ai | 6,053 | 4,040-6,450 | 9 | 5 | 13 / 4 / 5 | 8m 06s |
| 16 | ab-testing-design | 4,631 | 3,080-5,000 | 9 | 5 | 7 / 5 / 5 | 5m 27s |
| 17 | ab-testing-analysis | 3,676 | 2,080-3,400 | 10 | 4 | 4 / 2 / 7 | 5m 28s |
| 18 | components-publishing-oer | 3,784 | 2,770-4,600 | 10 | 5 | 15 / 6 / 1 | 5m 06s |
| 19 | training-certifying-reviewers | 3,748 | 2,180-3,600 | 9 | 5 | 9 / 2 / 5 | 4m 10s |

- Totals for Chapters 2 to 19: about 83,560 prose words (specification blocks excluded; they add about 109,800 more),
  146 specifications, 114 mascot admonitions.
- Concepts covered: all concepts in every chapter's "Concepts Covered" table appear in the body (verified by script).
- Across the 18 chapters, 112 concept sections were within their word range, 168 were under, and 50 were over. Most
  shortfalls are Tier A and Tier B concepts written without filler, as the anti-padding rules ask. Overages are mostly
  Tier C concepts that carry a worked example the chapter needs (for example Cohen's kappa in Chapter 14, rubric-outcome
  correlation in Chapter 17, the calibration exercise in Chapter 19). Chapter 3 sits 29 words under its chapter budget
  and Chapter 17 sits about 8 percent over.
- Whole-book specification mix (149): 123 `microsim` (p5.js), 21 `infographic` overlay posters (html), 3 `graph-model`
  (vis-network), 2 `chart` (Chart.js). Bloom levels: Evaluate 41, Apply 37, Analyze 24, Understand 23, Remember 23,
  Create 1.
- Overlay infographic posters (21, all specified as callout overlays except the four grid overlays marked G). No
  verified-infographic was used, because it needs web-checked sources and an author approval checkpoint.

- Ch2: `six-cc-licenses-poster`
- Ch2: `license-statement-anatomy`
- Ch3: `rubric-worksheet-anatomy`
- Ch3: `reliability-validity-targets`
- Ch4: `html-page-anatomy`
- Ch4: `github-repository-anatomy`
- Ch5: `citation-anatomy`
- Ch6: `readable-page-anatomy`
- Ch7: `accessibility-page-anatomy`
- Ch8: `quiz-question-anatomy`
- Ch9: `metadata-record-anatomy`
- Ch12: `prompt-anatomy`
- Ch12: `agent-report-anatomy`
- Ch14: `agent-report-checkpoints`
- Ch15: `pdf-conversion-error-poster`
- Ch15: `improvement-workflow-poster`
- Ch16: `ab-test-anatomy`
- Ch17: `results-summary-anatomy`
- Ch18: `publishing-pipeline-poster`
- Ch19: `training-kit-poster`
- Ch19: `capstone-roadmap-poster`

  Grid overlays (G): `six-cc-licenses-poster`, `reliability-validity-targets`, `improvement-workflow-poster`,
  `capstone-roadmap-poster`.

## Running example and numbers

Chapters 3 to 19 share one fictional running example, *Watershed Basics* by Maria Lopez (CC BY 4.0, at
`example.org`), which scores 65 (Revise) at baseline and 78 (Adopt) after the Chapter 15 improvement plan. All
statistics in the examples (agreement rates, kappa, effect size, correlations, costs, sample sizes) were computed
exactly in Python. Anything labeled "illustrative" in a specification is made up for teaching. Details are in the
scratchpad notes and in the chapters.

## Verification

| Check | Result |
|-------|--------|
| Frontmatter parses as YAML; `date` is a string; TODO placeholder removed | Pass for all 18 chapters |
| `validate-chapter-mascots.py` on every chapter 1 to 19 | Pass: no placement rule violations |
| Specification block structure, Bloom verb in level list, forbidden phrases, threshold wording | Pass for Chapters 3 to 19 |
| Unique kebab-case sim-ids | Pass: 149 unique, none collide with a folder in `docs/sims/` |
| Dependency order across all chapters | Pass: 0 violations |
| `mkdocs build --strict` after each chapter and at the end | Pass: exit 0, no warnings |
| Chapter 2 specification check | Two flags caused by the author's embed of the built `cc-license-switches` sim (a `Diagram` header with an `iframe`); the chapter's own seven specifications are well formed |

## Needs the author's attention

1. **Rubric design conflict.** `docs/rubric-spec.md` (draft v0.4, 0 to 3 scale with P/J/RP/RJ indicators) describes a
   different rubric from the ten-metric, 0 to 10 design in the course description and the sample worksheet, which the
   chapters follow.
2. **Values invented for this book** (labeled provisional or illustrative in the text): the scoring bands used to turn
   checks into scores, the adoption rule (total >= 75 and every metric >= 5), the ten checks listed for each metric,
   the agent first-pass standard (agreement >= 80 percent at a threshold of 1, absolute bias <= 0.5, mean absolute
   difference <= 1.0, kappa >= 0.61, run-to-run range <= 1), the 5-point hypothesis threshold, and the hour estimates in
   the Chapter 15 plan.
3. **Claims written from memory that need a citation check.** Chapters 1 to 13: the facts listed in the Chapter 1 log,
   WCAG 2.1 AA criteria and contrast ratios, the Flesch-Kincaid formula, Dublin Core and Schema.org terms, Creative
   Commons license terms, FERPA. Chapters 14 to 19: Landis and Koch kappa labels; Cohen's d conventions (0.2, 0.5, 0.8);
   the sample-size rule of thumb (about 16 divided by d squared, giving 25, 64, and 400 students per group); COPPA,
   consent and assent, and small-group reporting thresholds (hedged in the text); Kirkpatrick's four levels; OER Commons,
   MERLOT, Jekyll, Hugo, the Internet Archive's Wayback Machine, and the `mkdocs build --strict` and `mkdocs gh-deploy`
   commands.
4. **Missing infrastructure.** KaTeX or MathJax is not installed (`arithmatex` is configured only), so formulas are
   plain text. The overlay shared libraries under `docs/sims/shared-libs` are not installed, which the 21 poster
   specifications need. `textstat` is not installed, so the reading-level report was not run.
5. **Overlap with your new sim.** `docs/sims/cc-license-switches` covers ideas that the Chapter 2 specification
   `cc-element-explorer` also covers; consider dropping one of them.
6. **Light spots.** Only one specification is at the Create level. Chapter 1 has three specifications and no overlay
   poster; Chapters 10, 11, and 13 have no overlay poster either.
7. **Nothing built.** All 149 specifications await `microsim-generator`; none has a `docs/sims/<sim-id>/` folder yet,
   apart from your `cc-license-switches`.
8. **Deploy check.** After the earlier `mkdocs gh-deploy`, the live site still showed the old placeholder 17 seconds
   later. Propagation was not re-checked.

## Files Created/Updated

- `docs/chapters/02-*` to `docs/chapters/19-*/index.md` (content generated; Chapters 2 to 13 were committed in
  `3b52a52`, Chapters 14 to 19 are not yet committed)
- `logs/ch-02-content-generation.md` to `logs/ch-19-content-generation.md` (start and end times)
- `logs/chapter-content-generator-2026-10-23-ch02-19.md` (this file)
