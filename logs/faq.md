# FAQ Generator Session Log

**Skill:** faq-generator, version 1.0
**Date:** 2026-10-24
**Request:** `/faq-generator`
**Result:** `docs/faq.md` with 103 questions in 6 categories, plus a chatbot JSON export, a quality report, and a coverage gaps report. `mkdocs build --strict` exits 0.

Timing was not recorded for this session.

## Step 1: Content completeness

| Input | Finding | Points |
|---|---|---|
| Course description | Quality score 98/100, Bloom outcomes at all six levels, prerequisites stated | 25/25 |
| Learning graph | Valid DAG, 351 concepts, 586 dependencies, 0 cycles. The file is `docs/learning-graph/learning-graph.csv`, not the `03-concept-dependencies.csv` the skill names | 25/25 |
| Glossary | 351 terms, about 21,900 words. **It did not exist when the session started.** See "Decision" below | 15/15 |
| Word count | More than 240,000 words across 19 chapters, the glossary, and the rubric specification | 20/20 |
| Concept coverage | All 351 concepts placed in a chapter (checked in the Chapter Content Generator log) | 15/15 |
| **Total** | | **100/100** |

The first measurement, taken before the glossary existed, was about 85/100.

## Decision: no glossary at the start

The skill says to ask when there is no glossary. I asked whether to generate the FAQ without one or to create the glossary first. The answer was to generate the FAQ now. While I was reading chapters, the glossary was finished in another session, so I read it in full and used it for terminology. The FAQ links to `glossary.md` as a file, never to an entry.

## How the FAQ was built

- Read the course description, learning graph (JSON, with Concept Impact Scores), concept taxonomy, glossary, the workshop pages, and the Bloom's Taxonomy reference at `$BK_HOME/skills/chapter-content-generator/references/blooms-taxonomy.md`.
- Read `CONTENT-GENERATION-GUIDE.md`, because the repo applies the mascot rules to FAQs.
- Five reading agents covered the 19 chapters and `docs/rubric-spec.md` and returned structured digests of facts, pitfalls, worked examples, and inconsistencies. The first attempt, three agents, failed to start with an empty error and was retried with five. I wrote every answer myself from those digests and the glossary.
- I re-checked about 35 specific figures against the chapter text with `grep` (thresholds, formulas, worked-example numbers, counts). A few greps came back empty on the first try. Each turned out to be a wording difference or the wrong chapter in my search, not an error in the answer, and I confirmed the facts against the text.
- The FAQ page, the JSON, and both reports come from one script that parses `docs/faq.md`. The Bloom's levels, difficulty ratings, concept lists, and keywords are author-assigned labels. That script and the label file live in the session scratchpad, not in the repo. The labels are preserved in `faq-chatbot-training.json`.

## Results

| Category | Questions | Skill target |
|---|---|---|
| Getting Started | 15 | 10-15 |
| Core Concepts | 28 | 20-30 |
| Technical Details | 25 | 15-25 |
| Common Challenges | 12 | 10-15 |
| Best Practices | 15 | 10-15 |
| Advanced Topics | 8 | 5-10 |
| **Total** | **103** | 70-110 |

| Measure | Result |
|---|---|
| Overall quality score (scripted) | 95/100: coverage 30, Bloom's 20, answer quality 25, organization 20 |
| Concept coverage | 88.3% (310 of 351). All 41 uncovered concepts are low priority (CIS under 30) |
| Bloom's distribution | Remember 19%, Understand 30%, Apply 30%, Analyze 12%, Evaluate 6%, Create 3% (total deviation 10 points) |
| Answers with an example | 83% |
| Answers linking to a chapter, reference, or page | 100% |
| Average answer length | 158 words (all between 100 and 300) |
| Estimated reading grade | 7.8 (Flesch-Kincaid) |
| Broken links, anchor links, duplicate questions | 0, 0, 0 |

Apply is 5 points above the overall target, and Best Practices leans toward Apply. Both are noted in the quality report.

## Mascot

Four admonitions: one `mascot-welcome` at the top, one `mascot-thinking` (quality and reusability as two scoreboards), one `mascot-warning` (a clean accessibility scan is not a pass), and one `mascot-tip` (check the claims that decide a band first). `validate-chapter-mascots.py` reports no violations, and the built page renders all four with working images. I did not use `mascot-celebration` because an FAQ has no milestone to close on.

## Validation

- `python3 "$BK_HOME/skills/book-installer/scripts/validate-chapter-mascots.py" docs/faq.md`: OK.
- `mkdocs build --strict` (built into a scratch directory, not `site/`): exit 0, no warnings. One INFO message about `image-prompts.md` being excluded from the site predates this work.
- Every list in `docs/faq.md` has a blank line before it.
- The JSON has all required fields for all 103 questions, unique IDs, and plain-text answers.

## Files

Created:

- `docs/faq.md`
- `docs/learning-graph/faq-chatbot-training.json`
- `docs/learning-graph/faq-quality-report.md`
- `docs/learning-graph/faq-coverage-gaps.md`
- `logs/faq.md`

Changed: `mkdocs.yml`. `FAQ: faq.md` now sits beside Glossary, and the two FAQ reports sit under Learning Graph. Nothing is committed.

## Problems found in the book itself

The FAQ avoids repeating any of these. They are listed so the author can decide what to fix.

### Verified against the files

1. **Two different rubrics.** `docs/rubric-spec.md` is marked "Draft v0.4 — design specification, not yet validated" and describes a 0 to 3 scale, 22 scripted checks, 17 judgment indicators, and two headline numbers "never combined" (decision D7). Chapter 3 teaches ten metrics scored 0 to 10, summed to a total of 100 with an adopt, revise, or reject rule. Nothing reconciles them. The FAQ treats Chapter 3 as the book's rubric and explains the difference in the Advanced Topics category.
2. **"Never merged" versus a merged total.** Chapter 3's mascot box is titled "Two Scoreboards, Never Merged" and warns that a merged number hides what to fix, while the chapter defines the total score as the sum of the ten metrics.
3. **Rubric specification decision count.** Line 11 says "the eighteen decisions, all resolved". Line 949 says "All fourteen decisions are resolved". The decision table runs to D18.
4. **Chapter range for the metric chapters (Chapter 3).** Lines 61 and 234 say Chapters 4 through 10 teach the ten metrics. Line 381 says Chapters 5 through 10 supply the checks. Editable source is in Chapter 4, so the first is right.
5. **Caption users in the pilot (Chapter 17).** Line 833 says 2 students used captions. Lines 185 and 648 say 3. The FAQ states no count.
6. **Chapter 13, Multi-Agent Review.** The worked example's heading says "three agents score six metrics". The digest reported only four rows in its table, and I did not recount them.
7. **Chapter 15 step order.** The introduction lists "plan the work, check that the license allows it". The Derivative Work section says reading the license is "the first step before any edit". The FAQ says to read the license first.
8. **Chapter 14 hallucination forms.** The text says hallucinations take four common forms. The worked example's fourth row is labeled "Invented count".

### Reported by the reading agents, not re-verified

- The "score of 10 requires every check to pass" rule appears in the MicroSim specifications and in Chapter 14, but the body text of Chapters 4 to 10 says only "choose the higher number" when no serious check fails. The FAQ states the 10 rule.
- *Watershed Basics* is described as having two reading sections in Chapter 6's alignment text and three in its readability text and in Chapter 5.
- Chapter 5 gives "Groundwater stored in underground layers is called an aquifer" as a fact, while Chapter 6 says the word is used before it is defined.
- Chapters 9, 10, and 11 differ on whether the quiz and the sections each have their own address, and on whether one image or none lacks alt text.
- Chapter 12 lists three different sets of JSON keys for the agent report. The FAQ uses the schema in the rubric-prompt section.
- Chapter 19's capstone has seven steps in its table but six stages on its poster, and the chapter never says whether the capstone and the certificate submission are the same work. The FAQ keeps them separate.
- Chapter 16's sample-size table says about 65 per group for a medium effect, and Chapter 17's rule gives 64. The FAQ says about 64 to 65.
- `AGENTS.md` and Chapter 18 say `mkdocs build --strict` fails on a page missing from the nav. By default MkDocs reports omitted pages at INFO level, which strict mode does not escalate, unless `validation.nav.omitted_files` is set to warn. `mkdocs.yml` has no such setting. The FAQ does not repeat the claim.

### Other

- `docs/about.md` still holds template text under Audience ("Describe the intended reader"). The FAQ takes the audience from the course description.
- Every MicroSim specified in the chapters has `Status: Specified`. Only the Creative Commons License Switches sim is built, so the FAQ links only to that one.

## Not done

- Nothing was committed, pushed, or deployed. The `publish` sequence is yours to run.
- The FAQ was not exercised with a chatbot or retrieval system.
- The 41 uncovered concepts, mostly accessibility details and the improvement-toolkit fixes, are listed in `docs/learning-graph/faq-coverage-gaps.md`.
