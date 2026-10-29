---
title: "Five Resources, Five Shapes"
description: "Five radar charts, one for each resource in the Chapter 3 total score example, showing that equal totals can hide very different shapes."
image: /sims/five-resources-five-shapes/five-resources-five-shapes.png
og:image: /sims/five-resources-five-shapes/five-resources-five-shapes.png
twitter:image: /sims/five-resources-five-shapes/five-resources-five-shapes.png
social:
   cards: false
status: built
hide:
  - toc
---

# Five Resources, Five Shapes

<iframe src="main.html" height="741px" width="100%" scrolling="no"></iframe>

[Run the Five Resources, Five Shapes MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `five-resources-five-shapes.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/five-resources-five-shapes/main.html"
        height="741px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

This poster draws the five resources from the Chapter 3 total score example as radar charts, from the lowest total to the highest. Each chart has ten spokes. The five spokes on the right are the quality metrics, drawn as blue circles. The five on the left are the reusability metrics, drawn as purple squares. A dashed ring marks the floor of 5. Watershed Basics and Locked Chemistry E-book both total 65, yet their shapes look nothing alike. All five resources are illustrative examples written for the chapter.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Thin Material | Total 37, Weak band, decision Reject. Quality 14, reusability 23. |
| Watershed Basics | Total 65, Fair band, decision Revise. Quality 32, reusability 33. |
| Locked Chemistry E-book | Total 65, Fair band, decision Revise. Quality 44, reusability 21. |
| One Gap | Total 85, Good band, decision Revise. Quality 45, reusability 40. |
| Open Algebra | Total 90, Excellent band, decision Adopt. Quality 43, reusability 47. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The five resources, their scores, and their decisions are illustrative examples from Chapter 3.
- The bands and the decision rule are this book's starting values, not a standard.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **distinguish** resources with the same total score by the shape of their ten metric scores, and name the metric to fix first. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The ten metrics and the 0 to 10 scale from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Explore (3 min).** Press Watershed Basics, then Locked Chemistry E-book. Both total 65. What does each need first?
2. **Quiz (3 min).** Press **Quiz Me** and find each resource from a description of its shape.
3. **Plan (4 min).** For each resource, name the one metric you would raise first and say why.

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Two resources total 65. Can you say how they differ from the total alone? *(No. A total hides the split between quality and reusability and the weakest metric.)*
2. Which resource has nine metrics of 9 and one of 4, and what is its decision? *(One Gap, total 85, Good, and Revise because one metric is below 5.)*
3. What does the dashed ring on each chart mark? *(The floor of 5. Any spoke that dips inside it is a metric below the floor.)*

### Connection to the OER Evaluator rubric

A shape is learned faster than a table, and the notch in a shape is the first thing to fix. This prepares the improvement rule of Chapter 15: raise the lowest metric first.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)) - Wikipedia - Defines rubrics, their criteria and performance levels, and the difference between analytic and holistic forms. Background for the ten-metric rubric and for how its scoring scales are built.
2. [Not All Rubrics Are Equal: A Review of Rubrics for Evaluating the Quality of Open Educational Resources](https://www.irrodl.org/index.php/irrodl/article/view/2389) - IRRODL - Yuan and Recker's peer-reviewed comparison of fourteen OER quality rubrics shows what each one emphasizes. Useful for seeing where this book's ten metrics overlap with, and differ from, earlier tools.
3. [Achieve OER Rubrics](https://www.achieve.org/node/496) - Achieve - Describes eight rubrics for judging how well an OER aligns to standards and meets other quality criteria, delivered through an online evaluation tool on OER Commons. An earlier example of scoring an OER criterion by criterion.
