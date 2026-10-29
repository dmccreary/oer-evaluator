---
title: Total Score Calculator
description: Explore how ten metric scores add up to subtotals, a total, a band, and an adoption decision, then calculate the total and decision for five resources.
image: /sims/total-score-calculator/total-score-calculator.png
og:image: /sims/total-score-calculator/total-score-calculator.png
twitter:image: /sims/total-score-calculator/total-score-calculator.png
social:
   cards: false
status: built
quality_score: 100
---

# Total Score Calculator

<iframe src="main.html" height="862px" width="100%" scrolling="no"></iframe>

[Run the Total Score Calculator MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To edit the sketch, paste the contents of `total-score-calculator.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/total-score-calculator/main.html"
        height="862px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Ten metric scores, each a whole number from 0 to 10, add up to a **quality subtotal** (metrics 1 to 5), a **reusability subtotal** (metrics 6 to 10), and a **total** out of 100. The total falls in a band, and a decision rule turns the scores into **Adopt**, **Revise**, or **Reject**.

In explore mode ten sliders show the subtotals, total, band, and decision at once, and name any metric below the floor of 5. In practice mode you type the total for five scored resources, choose the decision, and press **Check**. A resource is correct only when both the total and the decision match.

| Band | Total |
|---|---|
| Excellent | 90 to 100 |
| Good | 75 to 89 |
| Fair | 50 to 74 |
| Weak | 25 to 49 |
| Poor | 0 to 24 |

### Controls

- **Ten sliders:** in explore mode, set each metric score from 0 to 10 in whole points. The start position is 5 for every metric.
- **Start practice:** leaves explore mode.
- **Total score box:** type a whole number from 0 to 100.
- **Adopt, Revise, Reject buttons:** choose the decision.
- **Check:** commits the answer. **Back to explore** is on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The decision rule: Adopt when the total is 75 or more and every metric is 5 or more. Reject when the total is below 50. Otherwise Revise.
- The five resources are illustrative examples. The explanation names the rule that decided each outcome.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **calculate** the quality subtotal, reusability subtotal, total score, band, and adoption decision for each of five scored resources, with the total and the decision both correct on at least 4 of 5. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

15-20 minutes.

### Prerequisites

- The terms *quality subtotal*, *reusability subtotal*, *total score*, *score band*, and *adoption threshold* from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Explore (4 min).** Set every slider to 8, then lower one slider to 4. What happens to the decision, and why?
2. **Calculate (8 min).** Work through the five resources. Add the scores on paper before you type the total.
3. **Explain (3 min).** For the resource whose total is 85, explain why the decision is not Adopt.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. A resource totals 85 and one metric is 4. What is the decision? *(Revise. The metric is below the floor of 5, even though the total is high.)*
2. A resource totals 37. What is the decision? *(Reject. The total is below 50.)*
3. Does a total of 75 always mean Adopt? *(No. Every metric must also be 5 or more.)*
4. Does the floor apply only to the license metric? *(No. It applies to every metric.)*

### Connection to the OER Evaluator rubric

This is the arithmetic behind every total on the rubric worksheet. [Chapter 11](../../chapters/11-manual-evaluation-adoption/index.md) uses the decision in a full manual evaluation.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
2. [Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html). Carnegie Mellon Eberly Center. The parts of a rubric and how to use it.
3. [Not All Rubrics Are Equal: A Review of Rubrics for Evaluating the Quality of Open Educational Resources](https://www.irrodl.org/index.php/irrodl/article/view/2389). IRRODL. Compares fourteen OER quality rubrics.
4. [Achieve OER Rubrics](https://www.achieve.org/node/496). Achieve. Rubrics that score an OER criterion by criterion.
