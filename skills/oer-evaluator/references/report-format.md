# report.json (schema `oer-evaluator-report/v1`)

This file is the contract between the evaluator and the improvement planner. The planner reads it and never rescans the book, so everything it needs is here.

## Top level

| Field | Meaning |
|---|---|
| `schema`, `spec_version`, `skill_version`, `generated_at` | Provenance. Scores are only comparable within one spec version. |
| `run` | `book_path`, `book_name`, `site_url`, `out_dir`, `options` (`check_external`, `shared_libs_as_declared`), `scope`. |
| `headline` | `Q`, `R`, `beside_Q`, `beside_R`, `provisional`, `provisional_because`. |
| `book.checks` | P1–P13, each `{status, value, evidence[], method, note}`. |
| `book.chapters` | Per chapter: `concept_count`, `weight`, `has_quiz`, `word_count`. `chapter_weight_scale` is `concepts`, `words`, or `none`. |
| `inventory` | `counts_by_type`, `not_detected_types`, `notes`. |
| `components` | Keyed by component id. See below. |
| `judgments` | Each Tier 2 indicator as `not_run` (v0.1) or `supplied`. |
| `signals` | Recorded and never scored (decision D3): `sponsor`, `embedded_instructions` (text addressed to an evaluator, with location and quote), `site_wide_scripts` (scripts `mkdocs.yml` loads on every page, with their roles). |
| `findability` | Catalog identity (`count`, `model`, `generated_at`, bands) or the reason the test did not run. |
| `findings` | Flat list of deterministic findings for the planner. |
| `limitations` | Plain statements of what this run did not do. |

## Status vocabulary

- `pass`, `fail`: the check ran and decided.
- `ISE`: insufficient evidence. It could not be determined. Always has a reason in `note` or `evidence`.
- `N/A`: the check cannot apply to this component type.
- `recorded`: a classification, not a test (RP8's interactivity level).
- `not_available` (headline only): the number cannot be computed from what ran.

## Component record

`type`, `path`, `title`, `interactivity` (L0, L1, L2), `checks` (RP1–RP9; RP8 carries `extra.delivery` for L2 components), `RJ6` (`score`, `status`, `reason`, `rates`, `by_query_type`, `twins_removed`, `queries[]`), and `reuse`:

```json
"reuse": {
  "stages": {"1": {"status": "pass|fail|ISE", "detail": "..."},
             "2": {"status": "pass|fail|ISE|pending"},
             "3": {"status": "pass|fail|pending"},
             "4": {"status": "scored|pending"}},
  "stage_reached": 1,
  "stopped_at": 2,
  "reuse_ready": true | false | null,
  "reuse_value": 0.0 | number | null,
  "value_without_findability": null,
  "pending": ["J1", "RJ2", "..."]
}
```

`reuse_ready: false` is definitive (a stage failed). `null` means a stage is still pending a judgment that did not run. `reuse_value` is `0.0` for definitely-not-ready components and `null` while undetermined.

## Findings

Each finding: `check`, `level` (`book` or `component`), `unit {kind, type, id}`, `status`, `value`, `evidence[]`, `note`. Kinds beyond failed checks:

- `duplicate-cluster`: `value` is the number of catalog entries that teach the same concept (WHAT similarity of 0.90 or more).
- `RP8` with `kind: opportunity`: a static figure that could be made interactive. Never a defect (decision D13).
- `RJ6` with `status: partial`: findability scored 1 (found, but weakly).
- `embedded-instructions`: text addressed to an evaluator, with `unit`, `location` and `quote`. Treated as data and not followed.
- `events-delivery`: an L2 component for which no code that sends events off the page was found. `status: info`, because absence from the files checked is not proof that nothing is delivered.

## How Tier 2 judgments will plug in

`report --judgments FILE` accepts `{"components": {"<id>": {"J1": 3, "J7": 2, "RJ1": 3, "RJ2": 2, "RJ4": 2}}, "chapters": {"<dir>": {"J1": 3, ...}}}`. When supplied, the funnel computes stages, reuse value and Q, and labels them provisional and unvalidated. v0.1 does not produce this file.
