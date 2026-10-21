# Checks: what each one inspects and where it stops

Every check is static analysis of files on disk. Nothing renders a page, runs a script, or follows a link unless `--check-external` is passed.

## Book level (P1–P13)

| Check | Looks at | Passes when | Known limits |
|---|---|---|---|
| P1 license | `mkdocs.yml` copyright, `docs/license.md`, `LICENSE` | a recognizable CC, MIT or Apache id is found | Notes when a NonCommercial or NoDerivatives term restricts reuse. Does not judge whether a license is "open" enough. |
| P2 creators | `site_author`, an Author section in `about.md` | a name is found | Scaffold text is ignored. |
| P3 sponsor | "sponsored/funded/supported by", "publisher:" wording | a statement is found | Recorded as a signal. Prestige is never scored (D3). |
| P4 objectives | `course-description.md` outcomes, per-chapter Learning Objectives headings or "By the end of this chapter you will…" phrases | the course states outcomes, or every chapter states its own | Phrase detection is deliberately narrow, so an implicit goal reads as not stated. |
| P5 learners | Audience section in `course-description.md` or `about.md` | a non-scaffold audience statement exists | |
| P6 prerequisites | Prerequisites sections | stated for the course or any chapter | |
| P7 instructions | "How to use", "Getting started" sections | present | |
| P8 accessibility | any mention of "accessib…" in front matter pages or `mkdocs.yml` | present | Presence only. J8 would judge whether it works, and is not run. |
| P9 technical requirements | "system/technical requirements", "supported browsers" wording | present | |
| P10 references | list items in `references.md` files | at least one | Counts entries, not their quality. |
| P11 links | internal Markdown, image and HTML links | every internal link resolves | External links are counted but not fetched offline. Links to unbuilt MicroSims are real findings. |
| P12 practice | `#### N.` questions in each chapter's `quiz.md` | every chapter has at least one | |
| P13 alt text | Markdown images and `<img>` tags | every image has non-empty alt text | Checks presence, not whether the text is meaningful. |

## Component level (RP1–RP9)

| Check | Applies to | Passes when |
|---|---|---|
| RP1 self-contained | all | no required file lives outside the component and none inside is missing. For Markdown, only embedded assets count. Iframes of other components are recorded as dependencies, not failures. |
| RP2 renders standalone | HTML components | `main.html` is a complete document and every local reference resolves. Static only; a render would confirm it. |
| RP3 dependencies stable | HTML components | every external library URL carries a version. Font services are exempt. Whether URLs resolve is checked only with `--check-external`. |
| RP4 license | all | declared on the component (`license`, `rights`, …) or inherited from P1. |
| RP5 metadata | all | all four required search fields are present: title, description, subject, learning objectives. Also reports generic fields (a short or iframe-only description, a placeholder title, objectives that are at least half template boilerplate, or any field that is itself text addressed to an evaluator), the recommended level field, and attribution fields (creators, version). |
| RP6 editable source | all | readable (non-minified) source exists. Raster-only images fail. |
| RP7 companions | MicroSims, quizzes | the component links to its quiz or MicroSim. A candidate inferred from chapter embedding but not recorded is a fail with the candidate named. |
| RP8 interactivity | all | classification: L2 when the code loads the LRS runtime and calls `LRSSim.create` (or uses an xAPI client library); L1 when it has interaction handlers; otherwise L0. A quiz is L2 when a script that `mkdocs.yml` loads on every page reads the quiz markup and emits an `answered` statement. For every L2 component the result also carries `extra.delivery`: whether any code that sends events off the page (`sendBeacon`, `XMLHttpRequest`, a `POST` fetch) was found in the files that run it. "Emits" and "delivers" are different claims. |
| RP9 events tied to concepts | L2 only | a `concept` option reaches the LRS runtime (sims) or every question carries a `Concept Tested` label (quizzes). String and numeric ids are resolved through simple variables and maps; computed values are noted, not guessed. When the book has a learning graph, each id is joined to it and `learning_graph.unmatched` lists those that match nothing. |

## Why some outcomes look harsh

RP1 fails for almost every MicroSim in this author's books, because they load shared libraries from outside their folder (`../../js/lrs-sim.js`, `../shared-libs/…`). That is the spec's rule applied as written: copying the folder alone breaks the sim, though embedding the hosted page by iframe still works. The report says when a failure is shared-library-only. Whether such files should count as declared is a decision for the author; `--shared-libs-as-declared` shows the other reading.
