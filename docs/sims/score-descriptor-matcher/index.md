---
title: Score Descriptor Matcher
description: Apply the scoring descriptors to choose the score band for each of nine observations about a rubric metric.
image: /sims/score-descriptor-matcher/score-descriptor-matcher.png
og:image: /sims/score-descriptor-matcher/score-descriptor-matcher.png
twitter:image: /sims/score-descriptor-matcher/score-descriptor-matcher.png
social:
   cards: false
status: built
quality_score: 100
---

# Score Descriptor Matcher

<iframe src="main.html" height="614px" width="100%" scrolling="no"></iframe>

[Run the Score Descriptor Matcher MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To edit the sketch, paste the contents of `score-descriptor-matcher.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/score-descriptor-matcher/main.html"
        height="614px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Every rubric metric uses the same 0 to 10 scale, and each band has a descriptor. The share of the check that is met decides the band: checks passed divided by checks, times 100. This MicroSim states nine observations, such as "Accessibility: 13 of 24 checks pass", and you choose the band that fits.

The six bands are 0 Absent, 1 to 2 Very poor, 3 to 4 Weak, 5 to 6 Adequate, 7 to 8 Good, and 9 to 10 Excellent. A boundary belongs to the higher band, so 25% is Weak, 50% is Adequate, and 75% is Good.

| Score | Share of the check met |
|---|---|
| 0 Absent | 0% |
| 1 to 2 Very poor | 1% to 24% |
| 3 to 4 Weak | 25% to 49% |
| 5 to 6 Adequate | 50% to 74% |
| 7 to 8 Good | 75% to 89% |
| 9 to 10 Excellent | 90% to 100% |

### Controls

- **Six band buttons:** choose the band. The choice is final.
- **Show descriptor table:** opens the table above. Opening it is exploration, not evidence.
- **Next:** moves to the next observation.
- **Play again** and the missed-observation review on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The observations are illustrative examples in a shuffled order.
- A share that falls between two whole percentages belongs to the band that contains it, so 12.5% is in the 1% to 24% band.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **apply** the scoring descriptors to choose the correct score band for each of nine observations about a metric, with at least 8 of 9 correct on the first attempt. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The terms *score scale*, *scoring descriptor*, and *metric score* from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Calculate (3 min).** Work out the share for "9 of 12 checks pass" by hand. Which band is it?
2. **Match the bands (6 min).** Choose a band for all nine observations.
3. **Edge cases (3 min).** Find the three observations that sit exactly on a boundary and explain why the higher band wins.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. 3 of 12 components stand alone. Which band? *(3 to 4 Weak. 25% is the bottom of the Weak band.)*
2. 18 of 22 checked facts match their sources. Which band? *(7 to 8 Good. About 82% is in the 75% to 89% band.)*
3. 0 of 6 required metadata fields are recorded. Which band? *(0 Absent. Nothing in the check is met.)*
4. Why does a boundary belong to the higher band? *(The rule avoids ties, and a check that is exactly half met earns Adequate.)*

### Connection to the OER Evaluator rubric

Descriptors are what make one reviewer's 7 equal another reviewer's 7. [Chapter 14](../../chapters/14-checking-agent-output/index.md) checks whether an AI agent applies them the same way.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
2. [Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html). Carnegie Mellon Eberly Center. The parts of a rubric and how to use it.
3. [VALUE Rubrics](https://www.aacu.org/value/rubrics). AAC&U. Level-by-level descriptors that different reviewers can apply consistently.
4. [Achieve OER Rubrics](https://www.achieve.org/node/496). Achieve. Rubrics that score an OER criterion by criterion.
