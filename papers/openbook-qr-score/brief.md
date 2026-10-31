# Paper Brief: The Case for an Objective Score for OER (OpenBook QR Score)

**Slug:** openbook-qr-score · **Created:** 2026-10-31 · **Status:** built, scored, not submitted
**Readiness score:** about 82/100 at drafting time (evidence was the weak point; see below)

## Thesis
Deciding which OER to adopt needs a shared, objective score that is anchored, two-part (quality and reusability), reproducible by humans and AI agents, and validated before use; the OpenBook QR Score is a candidate.

## Paper type and audience
- **Type:** position paper (framework plus an illustrative application)
- **Audience:** OER coordinators, instructional designers, librarians, OER researchers
- **Venue:** none for now. The author decided NOT to submit to arXiv but to keep the arXiv format.
- **Eligibility note:** arXiv's CS categories reject unreviewed position papers (since 31 Oct 2025); EdArXiv/OSF would fit if it is posted later.

## Authors
| Order | Full name | Affiliation | Contact | ORCID |
|------:|-----------|-------------|---------|-------|
| 1 | Dan McCreary | Independent Researcher (assumed) | https://github.com/dmccreary | none given |

## Problem and gap
Review of 14 OER rubrics (Yuan and Recker 2015): 5 no scale, 3 detailed scoring guide, 6 tested, 3 revised, 2 automated; rubrics emphasize different constructs. AI makes scoring cheap but unvalidated.

## Contributions
1. Four requirements for an objective OER score (anchored, two-part, reproducible, validated).
2. The OpenBook QR Score specification (10 metrics, descriptors, equations, decision rule).
3. An illustration: ten widely used textbooks scored by one AI agent each, plus a 101-book scripted census.
4. Under-specifications exposed (NonCommercial licenses).
5. A six-study validation agenda.

## Evidence
| Evidence | Kind | Source |
|----------|------|--------|
| Yuan and Recker counts | cited data | irrodl article text (verified in the article, not only the book's spec) |
| 10 textbook scores | AI-agent case studies, two passes | `figures/public-oer-scores.csv` (three chapters), `public-oer-scores-onechapter.csv`, `public-oer-chapters.csv`; agents' evidence recorded per metric |
| 101-book census | scripted checks | `figures/census-book-checks.csv`; oer-evaluator skill v0.1 |
| Cost: tokens, seconds | measured | agent harness usage reports |

## Run log (time, tokens, disk) -- requested by the author
- **Pass 1 (one chapter, fifth in TOC):** launched 2026-10-31 19:05:49 UTC, last report about 19:08:14 UTC (about 2 min 25 s wall clock, 10 agents in parallel). 827,549 tokens, 135 tool calls, 944 agent-seconds. Mean 82,755 tokens and 94.4 s per title (71,761 to 102,022 tokens; 47.0 to 144.4 s).
- **Pass 2 (three chapters: first, middle, last numbered; each agent in its own folder):** launched 19:35:41 UTC, last report about 19:39:18 UTC (about 3 min 37 s wall clock). 860,984 tokens, 176 tool calls, 1,205.7 agent-seconds. Mean 86,098 tokens and 120.6 s per title (74,385 to 97,170 tokens; 51.7 to 217.0 s).
- Both passes: default subagent model (inherits the session model, Claude Sonnet 5.5); Haiku was not used so all twenty runs are comparable. Combined 1,688,533 tokens.
- Scripted census: 101 books, 2.3 s for the 203-component reference book; the whole census finished in a few minutes.
- Disk: `~/tmp/oer-books` held 308 KB after pass 1 (the Yuan and Recker article only; agents read pages and APIs). After pass 2 it held 111,212 KB (about 109 MB), of which 96,888 KB is the `openintro-statistics` folder and the rest is the other agents' scripts and fetched pages. Census reports in the session scratchpad: about 114 MB. Free space fell from 670.63 GB-equivalent (670,625,448 KB) to 670,566,376 KB, i.e. about 60 MB, and stayed near 640 GiB.
- Tokens used by the main session for drafting are not included above.

## Assumptions (made without the author; confirm each)
- Author is Dan McCreary, Independent Researcher; no email or ORCID printed.
- License CC BY 4.0.
- "Widely used" titles are a judgment sample (no ranking source found), 6 of 10 from OpenStax.
- Pass 1 scored the fifth chapter for metrics 1 to 5; after the author asked whether one chapter is enough, pass 2 scored the first, middle and last numbered chapters (mean, rounded half up). Pass 2 is the headline result; pass 1 is the comparison.
- The paper presents 100-point QR totals even though the companion rubric spec v0.4 never blends Q and R; flagged as an open question in the paper.

## Open questions
- Name collision search for "OpenBook" was never done.
- Should a NonCommercial clause cap the license metric?
- Human second-reviewer scores for at least three titles would raise the evidence criterion substantially. Pass-to-pass agreement: totals differ by 3.5 points on average, rank correlation 0.75, 9 of 10 decisions unchanged (Calculus Vol 1 Revise to Adopt), metric scores exact 46% and within one point 88%, pooled quadratic-weighted kappa 0.80 (0.86 for whole-work metrics 6 to 10, 0.71 for metrics 1 to 5).

## Outline (author did not review it; they asked for evidence and then the draft)
1 Abstract; 2 Introduction; 3 Background and related work (4 strands); 4 Why OER need an objective score (4 requirements); 5 The OpenBook QR Score; 6 Illustration (method, scores, findings, cost, census); 7 Validation agenda (6 studies); 8 Discussion and limitations; 9 Conclusion. Figures: workflow (TikZ), Q-versus-R scatter, metric profile, census histogram. Tables: requirements, metrics, descriptors, scores, cost.
