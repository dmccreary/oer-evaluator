# Packaging conventions and detection

These come from the documentation of the author's `microsim-generator`, `faq-generator`, `quiz-generator` and `book-chapter-generator` skills. They were read from that documentation and checked against several real books, but a book that departs from them will be under-inventoried, not mis-scored.

| Component | Where | Notes |
|---|---|---|
| MicroSim | `docs/sims/<id>/` with `main.html` and usually `index.md`, `metadata.json`, `<id>.js` | Directories without `main.html` (shared libraries, assets) are skipped. |
| Interactive infographic | a sim with `data.json`, or `diagram_type` containing "overlay" | Type only; the interactivity level comes from code. |
| Placeholder sims | ids `template`, `sample-arch`, `sim-template`, `template-*`; titles containing "a title under", "template" | Excluded and listed in the inventory notes. Same list as the search-microsims duplicate finder. |
| Static figure | `docs/posters/<slug>/`, or an image referenced from a chapter | Images under `docs/sims/` belong to their sim. |
| FAQ pair | `docs/faq.md`, one `###` heading per question | The category `##` is not a component. |
| Chapter quiz | `docs/chapters/<dir>/quiz.md` | One component per chapter, not per MicroSim. |
| Glossary | `docs/glossary.md` | One component. |
| Chapter | `docs/chapters/<dir>/index.md` | Weight comes from its "Concepts Covered" section: a table or a numbered list. |

**Not detected:** worked examples and instructor materials have no convention, and a quiz written for one specific MicroSim has no file convention. The report lists these under `not_detected_types`; finding them needs LLM enumeration with human confirmation.

## Chapter weights

Concept count when every chapter has a "Concepts Covered" section; otherwise word count for every chapter (never mixed). A chapter that lists no concepts carries no weight. The Concept Impact Score is not used in v0.1 (decision D12).

## The instrumentation signature (RP8, RP9)

A component is **L2** when its package loads the LRS runtime (`<script src="…lrs-sim.js">`) **and** calls `LRSSim.create(...)` (the call may live in a separate file such as `xapi.js`). The `status: instrumented` flag in a lesson page is a hint and is not trusted. Concept mapping (RP9) is a `concept` option on `LRSSim.create`, `lrs.item` or `lrs.question`, or a `CONCEPT` map of string values.

## Site-wide scripts and the learning graph

`mkdocs.yml` `extra_javascript` entries load on every page, so a quiz can be instrumented without any code of its own (the author's `quiz-xapi.js` reads the rendered `??? question` blocks and emits `answered`). The inspect step classifies each such script as an xAPI runtime or a quiz emitter by what its code does, not by its filename.

The learning graph is read from `docs/learning-graph/learning-graph.json` (`nodes` with `id` and `label`) or `learning-graph.csv` (`ConceptID`, `ConceptLabel`). An emitted concept id joins it when it equals a `ConceptID`, ends in `-<ConceptID>`, or slugs to a label.

## The RP1 shared-library policy

RP1 follows the spec literally: a required file outside the component directory is a failure. In this author's books that fails nearly every MicroSim, because they load `../../js/lrs-sim.js`, `../../css/…` or `../shared-libs/…`. The report marks such failures `shared_library_only: true`. This is a policy question for the author, not a bug: iframe reuse of the hosted page still works, but copying the folder does not. Use `--shared-libs-as-declared` to see the result under the other reading.
