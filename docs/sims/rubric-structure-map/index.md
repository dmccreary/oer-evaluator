---
title: Ten-Metric Rubric Map
description: Explore the structure of the ten-metric rubric as a tree, then click the metric that each of ten teacher complaints tests.
image: /sims/rubric-structure-map/rubric-structure-map.png
og:image: /sims/rubric-structure-map/rubric-structure-map.png
twitter:image: /sims/rubric-structure-map/rubric-structure-map.png
social:
   cards: false
status: built
quality_score: 100
---

# Ten-Metric Rubric Map

<iframe src="main.html" height="562px" width="100%" scrolling="no"></iframe>

[Run the Ten-Metric Rubric Map MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To change the nodes or the complaints, edit the `NODES` and `COMPLAINTS` tables at the top of `rubric-structure-map.js`.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/rubric-structure-map/main.html"
        height="562px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

The Ten-Metric Rubric rates an OER on ten metrics worth 10 points each. This map shows 13 nodes: the root, two dimensions (**Quality**, 50 points, and **Reusability**, 50 points), and five metrics under each dimension. Each edge means "is a part of" and points from the child to its parent.

In **Explore** mode you click a node to highlight its parent and children and to read its definition, the question it answers, and the chapter that teaches it. In **Quiz me** mode you read a teacher complaint, such as "I only have a PDF, and I need to change one sentence", and click the metric it tests. You get two tries.

| Dimension | Metrics |
|---|---|
| Quality (50 points) | Accuracy and currency, Alignment, Readability, Accessibility, Practice with feedback |
| Reusability (50 points) | Open license, Modularity, Metadata, Editable source, Portability |

### Controls

- **Explore and Quiz me buttons:** switch modes. Quiz me starts a new run.
- **Nodes:** click a node. The same nodes are reachable by keyboard through a hidden list of buttons, and a screen reader announces each node.
- **+, minus, and Fit:** zoom the map. The map does not zoom with the mouse wheel, so it never captures page scrolling. Once zoomed in, drag to pan.
- **Next:** moves to the next complaint. **Play again** repeats the quiz.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- Clicking the root or a dimension node during the quiz counts as a wrong attempt.
- Each complaint has exactly one correct metric, and each metric is the answer to exactly one complaint.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **attribute** each of ten teacher complaints to the one rubric metric it tests, with at least 9 of 10 correct on the first attempt. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The ten rubric metrics and the *quality* and *reusability* dimensions from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Explore (4 min).** Click each of the ten metrics and read the question it answers. Which two metrics sound most alike?
2. **Quiz (5 min).** Press **Quiz me** and match all ten complaints to metrics.
3. **Distinguish (3 min).** For each metric pair you confused, write one complaint that belongs to only one of them.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. "A screen reader reads the picture names as image1.png." Which metric? *(Accessibility. Missing text descriptions block learners who use screen readers.)*
2. "I cannot tell whether I may translate this." Which metric? *(Open license. The reuse permissions are not stated.)*
3. Which dimension holds Editable source? *(Reusability.)*
4. Are readability and accessibility the same metric? *(No. Readability is about wording for the audience, and accessibility is about learners with disabilities.)*

### Connection to the OER Evaluator rubric

Chapters 4 to 10 teach the checks behind these ten metrics, and each node in the map names the chapter that teaches it.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
2. [Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html). Carnegie Mellon Eberly Center. The parts of a rubric and how to use it.
3. [Not All Rubrics Are Equal: A Review of Rubrics for Evaluating the Quality of Open Educational Resources](https://www.irrodl.org/index.php/irrodl/article/view/2389). IRRODL. Compares fourteen OER quality rubrics.
4. [Achieve OER Rubrics](https://www.achieve.org/node/496). Achieve. Rubrics that score an OER criterion by criterion.
