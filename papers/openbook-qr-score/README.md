# The Case for an Objective Score for Open Educational Resources

Position paper proposing the **OpenBook QR Score** (Quality + Reusability, out of 100).
Version 0.01, 31 October 2026. Written in arXiv format; **not submitted to arXiv**.

| File | What it is |
|------|-----------|
| `main.pdf` | The built paper (23 pages) |
| `main.tex`, `sections/` | LaTeX source, one file per section; `sections/references.bib` has 40 verified references |
| `figures/` | Figure scripts, TikZ source, PNGs, and the data behind them (`public-oer-scores.csv` three-chapter pass, `public-oer-scores-onechapter.csv`, `public-oer-chapters.csv`, `census-book-checks.csv`, `census-book-versions.csv` with each census book's git commit and dirty state, `census-pull-log.csv`) |
| `brief.md` | Interview answers, assumptions, outline, run log (time, tokens, disk) |
| `quality-report.md` | Rubric score, gaps, and what only the author can supply |
| `arxiv-metadata.md` | Form fields, kept in case the paper is posted to a preprint server later |

```bash
./build.sh            # build main.pdf (needs: brew install tectonic)
python3 figures/make_figures.py   # regenerate the three PNG figures
```

Scores in the paper are single-reviewer (one AI agent per title), one sampled chapter, and
unvalidated (AI agents of one model family, two passes). See the Limitations section before quoting any number.
