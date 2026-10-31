# OER Evaluator: source code for the deterministic checks

This folder holds the code that applies the **deterministic (scripted) checks** of the OER
Evaluator rubric to a MkDocs textbook, and the code that runs those checks across many
books at once. It is the code behind the "scripted census of 101 textbooks" in the
position paper [`papers/openbook-qr-score`](../papers/openbook-qr-score/).

**What it does:** takes the files of a MkDocs book on disk and reports (a) an inventory of
its reusable components, (b) 13 book-level completeness checks (P1 to P13), and (c) 9
component-level reuse checks (RP1 to RP9) for every component.

**What it does not do:** it never computes the quality score Q or reuse score R, and it does
not estimate them. Those need judgment indicators (human or AI-agent) that version 0.1
deliberately does not run. It never modifies the book it inspects. The `inspect`, `report`
and census steps need no AI model and no network.

---

## 1. Layout

```
src/
├── README.md                    this file
├── requirements.txt             dependencies (the core needs none)
├── oer_evaluator/               the evaluator (a copy of skills/oer-evaluator/scripts)
│   ├── oer_evaluator.py         command line: inspect | findability | report | run
│   ├── inventory.py             finds the components in a book (MicroSims, quizzes, FAQ pairs, ...)
│   ├── checks_book.py           book-level checks P1 to P13
│   ├── checks_component.py      component-level checks RP1 to RP9, and the L0/L1/L2 interactivity level
│   ├── safety.py                records text in the book that is addressed to an evaluator (never obeyed)
│   ├── funnel.py                reuse "funnel" and the Q/R headline (reports "not available" in v0.1)
│   ├── report.py                writes report.json and report.md
│   ├── findability.py           optional retrieval test (needs a model step and extra packages)
│   ├── net.py                   network helpers, used only with --check-external
│   ├── common.py                shared helpers and version numbers
│   └── selftest.py              62 self-checks on a small synthetic book
└── census/
    ├── run_census.py            runs `inspect` over every textbook found under a folder
    └── summarize_census.py      prints the census statistics and writes the per-book CSV
```

Modules import each other by plain name, so the scripts work from any directory. There is
nothing to install.

## 2. Requirements

- Python 3 (tested with 3.13.0; written to avoid newer-only features, but not tested on older
  versions). The standard library is enough for every step in this README.
- A MkDocs textbook laid out the way this author's books are: `mkdocs.yml` at the root and
  Markdown in `docs/` (chapters in `docs/chapters/`, MicroSims in `docs/sims/<id>/`).
- `findability.py` is the only part that needs extra packages (`numpy`,
  `sentence-transformers`). You do not need it for anything below.

## 3. Run the checks on one book, step by step

All commands are run from the repository root (`oer-evaluator/`). Replace `BOOK` with the path
to a book, for example `~/Documents/ws/oer-evaluator`, and `OUT` with a folder **outside** the
book, for example `~/oer-reports/my-book`.

### Step 1: confirm the code works (self-test)

```bash
python3 src/oer_evaluator/selftest.py
```

The self-test builds a small synthetic book in a temporary folder, runs the checks on it and
prints `62 of 62 checks passed`. It touches no real book. If it does not print that line, stop
and fix that first (see section 7).

### Step 2: inspect the book

```bash
python3 src/oer_evaluator/oer_evaluator.py inspect BOOK --out OUT
```

What happens, in order:

1. **Validate.** The command exits with an error (status 2) if `BOOK` has no `mkdocs.yml` or
   `docs/`, or if `OUT` is inside the book. The book is never written to.
2. **Inventory** (`inventory.py`). It walks `docs/` and lists every component: chapter
   sections, quizzes, MicroSims, interactive infographics, static figures, FAQ
   question-and-answer pairs and the glossary.
3. **Book-level checks** (`checks_book.py`). It runs P1 to P13 once for the whole book.
4. **Component-level checks** (`checks_component.py`). It runs RP1 to RP9 on every component
   and classifies each as L0 (static), L1 (interactive) or L2 (instrumented, records events).
5. **Safety scan** (`safety.py`). It records any text in the book that looks like an instruction
   to an evaluator ("ignore previous instructions", "rate this 3"). It only records where
   that text is; it never acts on it.
6. **Findability inputs.** It writes a short content digest for each MicroSim and infographic
   into `OUT/findability/inputs/` for the optional retrieval test (section 5).
7. **Write `OUT/inspect.json`** and print a one-paragraph summary such as:

```
inspected oer-evaluator: 203 components (faq-pair 104, glossary 1, interactive-infographic 30, microsim 23, quiz 19, section 19, static-figure 7)
book checks: 8 pass, 5 fail
```

A typical book takes a few seconds (203 components took 2.3 seconds).

Optional flags:

| Flag | Effect |
|---|---|
| `--check-external` | Also fetches external links and CDN URLs (uses the network; off by default). |
| `--shared-libs-as-declared` | Counts files in shared library folders as declared dependencies of a component (changes check RP1; see `skills/oer-evaluator/references/conventions.md`). |

### Step 3: read `inspect.json`

`OUT/inspect.json` is plain JSON with these top-level keys:

| Key | Contents |
|---|---|
| `run` | Which book, when, with which options and version numbers. |
| `inventory` | `components`: a list with `id`, `type`, `path`, `title` for every component. |
| `book_checks` | One entry per check, `P1` to `P13`. |
| `components` | For each component id: `checks` (RP1 to RP9), `interactivity` (L0, L1 or L2) and `metadata_desc`. |
| `embedded_instructions` | Text found that is addressed to an evaluator (usually an empty list). |
| `site_wide_scripts` | Scripts loaded on every page, and whether they send data off the page. |

Every check has the same shape: `status`, `value`, `evidence` (where in the book it looked),
`method` and `note`. The status is one of:

| Status | Meaning |
|---|---|
| `pass` | Checked, and the book meets the rule. |
| `fail` | Checked, and the book does not meet the rule. |
| `ISE` | Insufficient evidence: it could not be determined, with the reason in `note`. Not a failure. |
| `N/A` | The check does not apply to this component. |

Quick look at the book-level results from the command line:

```bash
python3 - <<'EOF'
import json
d = json.load(open("OUT/inspect.json"))          # replace OUT with your folder
for k, v in d["book_checks"].items():
    print(k, v["status"])
EOF
```

### Step 4: write the readable report

```bash
python3 src/oer_evaluator/oer_evaluator.py report OUT
```

This reads `OUT/inspect.json` and writes:

- `OUT/report.md`: a readable report with these sections: Headline, Book-level checks, Inventory,
  MicroSims and infographics, Findability test, Judgment indicators, Findings for the
  improvement planner, and Limitations.
- `OUT/report.json`: the same content for programs.

In version 0.1 the headline says **Q: not available** and **R: not available** and explains
why. That is intentional, not an error.

### Step 5 (shortcut): inspect and report in one command

```bash
python3 src/oer_evaluator/oer_evaluator.py run BOOK --out OUT --skip-findability
```

`run` does Step 2 and Step 4 together.

## 4. Run the checks on many books (the census)

This reproduces the census reported in the paper.

### Step 1: choose a folder that contains your book folders

The runner treats every direct subfolder of `--root` as a candidate book. A folder counts as a
textbook when it has `mkdocs.yml` and a `docs/chapters/` folder with at least `--min-chapters`
entries (default 5). Under `~/Documents/ws` that finds 101 books.

### Step 2: run the inspection over all of them

```bash
python3 src/census/run_census.py --root ~/Documents/ws --out ~/oer-census --jobs 4
```

For each book it runs the `inspect` command of section 3 with a time limit
(`--limit-seconds`, default 150) and writes `~/oer-census/<book>/inspect.json` and
`~/oer-census/<book>.log`. It finishes with an index, `~/oer-census/census-index.json`
(books run, failures, seconds), and prints a line like:

```
Done: 101 ok, 0 failed, 51.5 s total
```

With `--jobs 4` the 101 books took 51.5 seconds on the author's laptop. The census output takes
about 114 MB. Use `--only name1 name2` to rerun a few books.

### Step 3: summarize

```bash
python3 src/census/summarize_census.py ~/oer-census --csv census-book-checks.csv
```

It prints how many of the 13 checks each book passed (mean, median, distribution), the pass
count for each check, the share of internal links that resolve (check P11) and the number of
components by type. With `--csv` it also writes the per-book table used for the histogram
figure in the paper.

### Step 4: compare with the paper

On the author's workspace the summary reads: 101 books; mean 6.4, median 6 of 13 checks passed;
32 books pass five or fewer; 1 passes ten; no book passes P11 (median 97.8 percent of internal
links resolve); 15,851 components. The CSV matches
`papers/openbook-qr-score/figures/census-book-checks.csv` line for line when the books have not
changed. Books that you edit after the census will, of course, give different numbers.

## 5. The optional findability step (not deterministic)

`findability` tests how easily a MicroSim can be found in the author's `search-microsims`
catalog (check RJ6). It is the one step that is not deterministic, because a language model
must first write search queries from each component's content digest. In outline:

1. `inspect` writes digests to `OUT/findability/inputs/` (Step 2 above).
2. A language-model agent writes 12 queries per digest into `OUT/findability/queries/`
   (instructions in `skills/oer-evaluator/references/findability.md`).
3. `python3 src/oer_evaluator/oer_evaluator.py findability OUT` embeds and ranks them. It
   needs `numpy`, `sentence-transformers` and a local checkout of the `search-microsims`
   catalog (set `OER_SEARCH_MICROSIMS` or pass `--search-home`).

If you skip it, every RJ6 result is simply reported as `ISE` and the rest of the report is
unaffected. The census did not use it.

## 6. What the checks look at

Every check is static analysis of files on disk. Nothing renders a page, runs a script or
follows a link unless `--check-external` is given.

**Book level**

| Check | Looks at | Passes when |
|---|---|---|
| P1 license | `mkdocs.yml` copyright, `docs/license.md`, `LICENSE` | a recognizable CC, MIT or Apache license is found |
| P2 creators | `site_author`, an Author section in `about.md` | a name is found |
| P3 sponsor | wording such as "sponsored by", "publisher:" | a statement is found |
| P4 objectives | course description outcomes, per-chapter Learning Objectives | the course or every chapter states outcomes |
| P5 learners | an Audience section | a non-template audience statement exists |
| P6 prerequisites | Prerequisites sections | stated for the course or any chapter |
| P7 instructions | "How to use", "Getting started" | present |
| P8 accessibility | any mention of accessibility in front matter or `mkdocs.yml` | present (presence only) |
| P9 technical requirements | "system requirements", "supported browsers" | present |
| P10 references | `references.md` files | at least one entry |
| P11 links | internal Markdown, image and HTML links | **every** internal link resolves |
| P12 practice | `#### N.` questions in each chapter's `quiz.md` | every chapter has at least one |
| P13 alt text | Markdown images and `<img>` tags | every image has non-empty alt text |

**Component level:** RP1 self-contained, RP2 renders standalone (static), RP3 stable
dependencies, RP4 license, RP5 metadata, RP6 editable source, RP7 companions (quiz or
MicroSim), RP8 interactivity level, RP9 events tied to concepts. The precise rules and known
limits of every check are in `skills/oer-evaluator/references/checks.md`.

Two things to keep in mind when you read the numbers. First, several checks are deliberately
strict or narrow: P11 fails a book for a single unresolved link, and P4 and P3 look for
specific phrases, so a low pass rate may reflect conventions rather than quality. Second,
RP1 fails for most MicroSims in this author's books because they load shared libraries from
outside their own folder; that is the specification applied as written.

## 7. Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `error: ... is not a MkDocs book` (exit status 2) | `BOOK` lacks `mkdocs.yml` or `docs/`. Point at the book root. |
| `error: --out must be outside the book` | Choose an output folder elsewhere; the book is never written to. |
| Self-test reports fewer than 62 passing checks | A script was edited or a Python version difference. Run `python3 --version` (3.9 or newer) and re-copy the scripts from `skills/oer-evaluator/scripts`. |
| `run_census.py` says `No MkDocs textbooks found` | `--root` should be the folder that *contains* book folders, not a book itself; lower `--min-chapters` if your books have fewer than 5 chapters. |
| One book shows `timeout after 150s` in the census | Raise `--limit-seconds`, or rerun it alone with `--only`. |
| `findability` reports it cannot run | Install `numpy` and `sentence-transformers`, or skip the step (section 5). |

## 8. Relationship to `skills/oer-evaluator`

`src/oer_evaluator/` is a copy of `skills/oer-evaluator/scripts/` so the code has a
conventional home as a software project. The skill folder stays as the agent-facing package
(its `SKILL.md` and reference documents tell an AI agent how to use these scripts). The two
copies are identical today. To check that they have not drifted:

```bash
diff -r skills/oer-evaluator/scripts src/oer_evaluator -x __pycache__ && echo "in sync"
```

If you change one, change the other, or replace one with a symbolic link to the other.
The census scripts exist only under `src/census/`.

## 9. Versions

The evaluator reports `skill v0.1.0` and `spec v0.4`
([rubric specification](https://dmccreary.github.io/oer-evaluator/rubric-spec/)). Check with:

```bash
python3 src/oer_evaluator/oer_evaluator.py --version
```
