---
title: Quality and Reusability Quadrant Sorter
description: Place eight resource profiles in one of four quadrants, then see each profile plotted by its quality subtotal and reusability subtotal.
image: /sims/quality-reusability-quadrant/quality-reusability-quadrant.png
og:image: /sims/quality-reusability-quadrant/quality-reusability-quadrant.png
twitter:image: /sims/quality-reusability-quadrant/quality-reusability-quadrant.png
social:
   cards: false
status: built
quality_score: 100
---

# Quality and Reusability Quadrant Sorter

<iframe src="main.html" height="750px" width="100%" scrolling="no"></iframe>

[Run the Quality and Reusability Quadrant Sorter MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To edit the sketch, paste the contents of `quality-reusability-quadrant.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/quality-reusability-quadrant/main.html"
        height="750px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

A resource can be good but locked, or open but weak. The rubric separates the two ideas into a **quality subtotal** (metrics 1 to 5) and a **reusability subtotal** (metrics 6 to 10), each out of 50. A subtotal is high at 25 or more and low below 25. The threshold is a study aid.

This MicroSim shows eight resource profiles. You place each one in one of four quadrants. Afterward the sim shows the two subtotals and plots the profile on a two-axis chart. The chart doubles as the legend: each quadrant is named and defined in place.

| Quadrant | Subtotals |
|---|---|
| Strong and open | Quality 25 or more and reusability 25 or more |
| Good but locked | Quality 25 or more and reusability less than 25 |
| Open but weak | Quality less than 25 and reusability 25 or more |
| Weak and locked | Quality less than 25 and reusability less than 25 |

### Controls

- **Four quadrant buttons:** place the profile. The placement is final.
- **Next:** moves to the next profile.
- **Chart:** each answered profile appears as a numbered point, green when right the first time and red when missed. On a wide page the results screen shows all eight points.
- **Play again** and the missed-profile review on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The profiles are illustrative examples in a shuffled order, two per quadrant.
- The subtotals appear only after you answer.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **differentiate** resources that need quality work from resources that need reusability work by placing each of eight profiles in the correct one of four quadrants, with at least 7 of 8 correct on the first attempt. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The ideas of the *quality dimension*, the *reusability dimension*, and *quality versus reusability* from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Predict (2 min).** Read the four definitions. Which quadrant do you expect a commercial e-book to land in?
2. **Place the profiles (6 min).** Place all eight profiles, then study the chart.
3. **Plan (4 min).** Choose one profile in a "locked" quadrant and name the two metrics you would fix first.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. A polished e-book, all rights reserved, PDF only. Which quadrant? *(Good but locked. Quality is high, and the license and source pull reusability below 25.)*
2. A CC BY worksheet set with outdated links and no alt text. Which quadrant? *(Open but weak. Reusability is high, and the errors and missing descriptions pull quality below 25.)*
3. Which quadrant needs work on both subtotals? *(Weak and locked.)*
4. Why report both subtotals and not only the total? *(Two resources can share a total and need very different work.)*

### Connection to the OER Evaluator rubric

Reporting both subtotals next to the total tells a reviewer which half of the rubric to improve. [Chapter 15](../../chapters/15-improving-resources-with-ai/index.md) shows how an AI agent can help improve a resource.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
2. [Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html). Carnegie Mellon Eberly Center. The parts of a rubric and how to use it.
3. [Not All Rubrics Are Equal: A Review of Rubrics for Evaluating the Quality of Open Educational Resources](https://www.irrodl.org/index.php/irrodl/article/view/2389). IRRODL. Compares fourteen OER quality rubrics.
4. [Achieve OER Rubrics](https://www.achieve.org/node/496). Achieve. Rubrics that score an OER criterion by criterion.
