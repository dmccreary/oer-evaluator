# Learning Graph Generator Session Log

- **Skill:** learning-graph-generator version 1.07
- **Date:** 2026-10-20
- **Input:** `docs/course-description.md` (quality score 98, so Step 1 was skipped)

## Programs used

| Program | Version | Command |
| --- | --- | --- |
| `analyze-graph.py` | no version string in the file (skill v1.07 copy) | `python3 analyze-graph.py learning-graph.csv quality-metrics.md` |
| `csv-to-json.py` | 1.05 | `python3 csv-to-json.py learning-graph.csv learning-graph.json color-config.json metadata.json taxonomy-names.json` |
| `taxonomy-distribution.py` | no version string in the file (skill v1.07 copy) | `python3 taxonomy-distribution.py learning-graph.csv taxonomy-distribution.md taxonomy-names.json` |
| `validate-learning-graph.sh` | no version string in the file (skill v1.07 copy) | `./validate-learning-graph.sh learning-graph.json` |

`add-taxonomy.py` was copied but not used; taxonomy IDs were assigned by concept ID range in a one-off script.

## Steps and decisions

1. **Step 2, concept list:** 351 concepts, checked for duplicates, labels over 32 characters, and commas. The author reviewed and approved the list before Step 3.
2. **Step 3, dependencies:** written as a concept-ID to prerequisite-ID map, joined to the exact labels by script, and checked for cycles before writing `learning-graph.csv`.
3. **Step 4, quality analysis:** valid DAG, one connected component, no orphans, 35.3% terminal nodes. The first run showed "Improvement Challenge" (a workshop activity) as the most depended-on concept, with indegree 19. The 13 improvement techniques and three related concepts were repointed to "Improvement Plan", and the graph was regenerated. The longest chain went from 25 to 24.
4. **Step 5 and 6, taxonomy:** 14 categories, none over 11.4%.
5. **Step 9, JSON:** 351 nodes, 586 edges, 14 groups. The top concepts by CIS are Educational Resource, Open Educational Resource, OER Quality, AI Assistant, and Copyright, so edge direction is correct.
6. **Step 10 and 11:** distribution report generated; `index.md` rebuilt from the template.
7. `mkdocs build --strict` passes.

## Open items

- Reviewer-judged quality score is 84/100 (see `quality-metrics.md`). The weakest areas are the number of foundational concepts (6) and the share of concepts with a single dependency (45.6%).
- The ten metrics in the rubric are drafted from the grant proposal, not from a published standard.
