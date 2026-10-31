# Quality Report: The Case for an Objective Score for OER (OpenBook QR Score)

**Version:** 0.01 · **Date:** 2026-10-31 · **Score:** 90/100 (Excellent), self-scored by the drafting agent
**Caution:** the 70 judgment points are the drafting agent's own, which is a generous grader of its own work; treat 90 as borderline Good/Excellent and expect an outside reader to score lower.
**Submission-ready:** not applicable (the author is not submitting to arXiv). All six hard gates pass as far as the agent could check; gate 3 and 4 need the author's spot check (below).

## Score breakdown
| # | Criterion | Points | Max | Notes |
|---|-----------|-------:|----:|-------|
| 1 | Title | 4 | 5 | 15 words, specific; "QR" is not defined until the abstract |
| 2 | Authors | 3 | 3 | Full name, "Independent Researcher", URL; no ORCID |
| 3 | Abstract | 6 | 7 | 236 words, 1,416 chars, five moves; "OER" is not expanded inside it |
| 4 | Introduction | 8 | 8 | Motivation, gap, enumerated contributions, roadmap |
| 5 | Related work | 7 | 7 | 4 strands, each ending in how this paper differs |
| 6 | Core contribution | 7 | 10 | Metrics, scale, equations, rationale; the per-metric sub-checks are summarized, not listed |
| 7 | Evidence | 6 | 8 | 10 real scored cases in two independent passes (three chapters per book in the headline pass), a pass-to-pass agreement analysis and a 101-book census; still one model family and no human baseline |
| 8 | Discussion and limitations | 4 | 4 | 8 explicit limitations |
| 9 | Conclusion | 3 | 3 | |
| 10 | References | 10 | 10 | 40 entries, all cited, 100% DOI or URL, 35% from 2021+ |
| 11 | Figures | 8 | 8 | 5 figures, all referenced, 327 to 369 DPI or vector, Okabe-Ito palette |
| 12 | Tables and formal elements | 4 | 4 | 5 booktabs tables, 2 equations |
| 13 | Claim support | 2 | 3 | Per-title facts come from agent reports (license facts spot-checked, see below) |
| 14 | Clean build | 4 | 4 | 21 pages, 0 errors, 0 overfull, 0 missing characters |
| 15 | Package | 4 | 4 | `arxiv-upload.zip` test-compiles |
| 16 | Metadata and disclosure | 4 | 4 | AI disclosure in Acknowledgments |
| 17 | Writing quality | 6 | 8 | Some repetition between abstract, intro and conclusion |
| | **Total** | **90** | **100** | |

## Hard gates
- [x] Compiles without errors
- [x] No undefined citations or references
- [x] Every DOI resolves to the cited work (31 verified by Crossref); 6 URL entries checked by HTTP 200, and the two arXiv entries by title and authors
- [x] Abstract at most 1,920 characters
- [x] No TODO or placeholder text
- [ ] No fabricated data: all numbers trace to logged data, but the per-title evidence is the agents' claims

## Gaps, ordered by points recoverable
1. **Evidence (up to +2):** add a second, human reviewer on at least three titles and report agreement with the agents.
2. **Core contribution (up to +3):** list the per-metric sub-checks as an appendix table.
3. **Writing (+2):** trim repetition.
4. **Title/abstract (+2):** define QR and OER in the abstract.

## Needs the author
- Confirm authorship, affiliation, contact, ORCID and the CC BY 4.0 license.
- Spot-check at least two agent reports against the live books. The agent already confirmed the license of Eloquent JavaScript, OpenIntro, Think Python, Beezer and OpenStax Physics directly. It did not re-verify accessibility, metadata or portability findings.
- References whose claims rest on titles or Crossref abstracts only (not full text): Hilton 2016 and 2020, Wiley et al. 2014, Mullens and Hoffman 2023, Shareefa et al. 2023, Bliss et al. 2013, Bozkurt 2023, Moore et al. 2024. Read these and check that the sentences citing them are fair.
- A name-collision search for "OpenBook".
- The physics agent reported its shared scratch folder was overwritten by another agent; consider re-running that title in isolation.
