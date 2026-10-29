---
title: Anatomy of a Rubric Worksheet
description: Find the eight parts of a rubric worksheet on a drawing of a printed sheet, then identify each part from a description of how it looks.
image: /sims/rubric-worksheet-anatomy/rubric-worksheet-anatomy.png
og:image: /sims/rubric-worksheet-anatomy/rubric-worksheet-anatomy.png
twitter:image: /sims/rubric-worksheet-anatomy/rubric-worksheet-anatomy.png
social:
   cards: false
status: built
quality_score: 100
---

# Anatomy of a Rubric Worksheet

<iframe src="main.html" height="702px" width="100%" scrolling="no"></iframe>

[Run the Anatomy of a Rubric Worksheet MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To change the content, edit the `DATA` block at the top of `rubric-worksheet-anatomy.js`. The drawing is inline SVG in `main.html`.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/rubric-worksheet-anatomy/main.html"
        height="702px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

The rubric worksheet is where a reviewer records scores and evidence. This MicroSim draws a printed worksheet lying on a desk, seen from above. Eight numbered markers point at its parts. The drawing contains no text, so every label comes from the data in the sim.

In **Explore** mode you hover or click a marker to read its label, description, and tip. In **Quiz me** mode you read a hint, such as "A narrow column marked with a person icon", and click the marker that matches. You get two tries.

| Marker | Part |
|---|---|
| 1 | Resource information block |
| 2 | Metric and what-to-check columns |
| 3 | Your score column |
| 4 | Agent score column |
| 5 | Evidence column |
| 6 | Quality half |
| 7 | Reusability half |
| 8 | Totals box |

### Controls

- **Explore and Quiz me buttons:** switch modes. Quiz me starts a new run.
- **The eight numbered markers:** hover, focus with the Tab key, or click.
- **Next:** moves to the next hint.
- **Play again:** repeats the quiz as practice.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- A wrong first click says so and lets you try once more. A second wrong click reveals the marker. Only a correct first click counts as evidence.
- The drawing is made for this book (SVG) and carries no statistics. A blank agent column is correct in a manual review.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **identify** the eight parts of a rubric worksheet from a description of each part's appearance, with at least 7 of 8 correct on the first attempt. (Bloom level: Remember.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The terms *rubric worksheet* and *review checklist* from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md), and the [sample rubric worksheet](../../workshops/sample-rubric-worksheet.md).

### Activities

1. **Explore (3 min).** Hover over every marker. Which column stays blank in a manual review?
2. **Quiz (4 min).** Press **Quiz me** and find all eight parts from their hints.
3. **Apply (3 min).** Open the sample rubric worksheet and point to each of the eight parts.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. Which column holds where you looked, what you saw, and the rule you applied? *(The evidence column.)*
2. Which half of the sheet is worth 50 points and holds Open license? *(The reusability half.)*
3. Is the agent column filled in during a manual review? *(No. Leave it blank.)*
4. Does the total box replace the two subtotals? *(No. Report both subtotals next to the total.)*

### Connection to the OER Evaluator rubric

The worksheet is where the scores and evidence for all ten metrics are recorded. [Chapter 11](../../chapters/11-manual-evaluation-adoption/index.md) shows a full manual review.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
2. [Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html). Carnegie Mellon Eberly Center. The parts of a rubric and how to use it.
3. [Achieve OER Rubrics](https://www.achieve.org/node/496). Achieve. Rubrics that score an OER criterion by criterion.
4. [Not All Rubrics Are Equal: A Review of Rubrics for Evaluating the Quality of Open Educational Resources](https://www.irrodl.org/index.php/irrodl/article/view/2389). IRRODL. Compares fourteen OER quality rubrics.
