---
title: "From Ten Scores to One Decision"
description: "A funnel that narrows ten metric scores to two subtotals, a total out of 100, a score band, and one decision, with the floor shown as a gate."
image: /sims/ten-scores-to-one-decision/ten-scores-to-one-decision.png
og:image: /sims/ten-scores-to-one-decision/ten-scores-to-one-decision.png
twitter:image: /sims/ten-scores-to-one-decision/ten-scores-to-one-decision.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="850px" width="100%" scrolling="no"></iframe>

[Run the From Ten Scores to One Decision MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `ten-scores-to-one-decision.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/ten-scores-to-one-decision/main.html"
        height="850px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

This poster follows the layers of Chapter 3 from left to right. Ten metric scores, each 0 to 10, combine into two subtotals of 50 points, which add to a total out of 100. The total falls into a band, and the band plus a floor of 5 produces a decision: Adopt, Revise, or Reject. The example is Watershed Basics, total 65, Fair, Revise. The inset in the lower right shows the One Gap resource caught at the floor: nine metrics of 9 and one of 4 give a total of 85, which is Good, and the decision is still Revise.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | Ten metric scores | Each metric is scored as a whole number from 0 to 10. Metrics 1 to 5 are quality and metrics 6 to 10 are reusability. The dashed line is the floor of 5. The example is Watershed Basics: 7, 6, 8, 5, 6 and 9, 5, 4, 8, 7. |
| 2 | Two subtotals of 50 points | The quality subtotal is the sum of metrics 1 to 5 and the reusability subtotal is the sum of metrics 6 to 10. Each is out of 50. Watershed Basics has 32 and 33. |
| 3 | The total out of 100 | The total is the quality subtotal plus the reusability subtotal, from 0 to 100. Watershed Basics totals 65. It is the number people ask for and the least informative number in a report. |
| 4 | The score band | The total falls into a band: Excellent 90 to 100, Good 75 to 89, Fair 50 to 74, Weak 25 to 49, and Poor 0 to 24. A total of 65 is Fair. |
| 5 | The decision | Adopt when the total is at least 75 and every metric is at least 5. Reject when the total is below 50. Otherwise Revise. Watershed Basics is Revise, shown by the pencil. |
| 6 | The floor gate and the One Gap example | One Gap has nine metrics of 9 and one of 4. The total is 85, which is Good, yet the decision is still Revise because one metric is below the floor of 5. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- The thresholds are this book's starting rule, not a standard.
- Watershed Basics and One Gap are illustrative examples from Chapter 3.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **trace** ten metric scores through subtotals, a total, a band, and a decision, and **explain** why the floor can override a high total. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The ten metrics from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Explore (3 min).** Hover over markers 1 to 6 in order and watch what each layer keeps and what it loses.
2. **Quiz (3 min).** Press **Quiz** and find each layer from its description.
3. **Apply (4 min).** A resource totals 80 with one metric at 3. Which decision does the rule give, and why?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. What is the Adopt rule? *(A total of at least 75 and every metric at least 5.)*
2. What band is a total of 65? *(Fair, which runs from 50 to 74.)*
3. A resource totals 85. Is it always Adopt? *(No. If any metric is below 5 the decision is Revise.)*

### Connection to the OER Evaluator rubric

Chapter 11 applies this same decision rule to real adoption decisions. The thresholds are this book's starting rule, a teaching choice and not a standard.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)) - Wikipedia - Defines rubrics, their criteria and performance levels, and the difference between analytic and holistic forms. Background for the ten-metric rubric and for how its scoring scales are built.
2. [Not All Rubrics Are Equal: A Review of Rubrics for Evaluating the Quality of Open Educational Resources](https://www.irrodl.org/index.php/irrodl/article/view/2389) - IRRODL - Yuan and Recker's peer-reviewed comparison of fourteen OER quality rubrics shows what each one emphasizes. Useful for seeing where this book's ten metrics overlap with, and differ from, earlier tools.
3. [Achieve OER Rubrics](https://www.achieve.org/node/496) - Achieve - Describes eight rubrics for judging how well an OER aligns to standards and meets other quality criteria, delivered through an online evaluation tool on OER Commons. An earlier example of scoring an OER criterion by criterion.
