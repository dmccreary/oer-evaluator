---
title: Inter-Rater Agreement Explorer
description: Explore how two reviewers' scores agree or disagree, then count the agreeing metrics and name the flagged metrics for three pairs of scores.
image: /sims/inter-rater-agreement-explorer/inter-rater-agreement-explorer.png
og:image: /sims/inter-rater-agreement-explorer/inter-rater-agreement-explorer.png
twitter:image: /sims/inter-rater-agreement-explorer/inter-rater-agreement-explorer.png
social:
   cards: false
status: built
quality_score: 100
---

# Inter-Rater Agreement Explorer

<iframe src="main.html" height="888px" width="100%" scrolling="no"></iframe>

[Run the Inter-Rater Agreement Explorer MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To edit the sketch, paste the contents of `inter-rater-agreement-explorer.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/inter-rater-agreement-explorer/main.html"
        height="888px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Two reviewers can give a resource the same total and still disagree on many metrics. A metric **agrees** when the two scores differ by 3 or fewer, and it is **flagged** when they differ by more than 3. **Percent agreement** is the number of agreeing metrics divided by 10, times 100.

In explore mode, Reviewer 1's ten scores are fixed and ten sliders change Reviewer 2's scores. The differences, flags, percent agreement, and both totals update at once. In practice mode you type the number of agreeing metrics and mark the flagged metrics for three pairs, then press **Check**.

| Term | Rule |
|---|---|
| Agrees | The two scores differ by 3 or fewer |
| Flagged | The two scores differ by more than 3 |
| Percent agreement | Agreeing metrics / 10 x 100 |

### Controls

- **Ten sliders:** in explore mode, set Reviewer 2's scores from 0 to 10 in whole points. They start equal to Reviewer 1's.
- **Start practice:** leaves explore mode.
- **Agreeing metrics box:** type a whole number from 0 to 10.
- **Ten metric buttons and None flagged:** mark every flagged metric, or choose None flagged.
- **Check:** commits the answer. **Back to explore** is on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The three pairs are illustrative examples in the order A, B, C.
- A pair is correct only when both the count and the flagged set match exactly. Equal totals do not mean agreement.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **calculate** the number of agreeing metrics and name the flagged metrics for each of three pairs of reviewer scores, with at least 2 of 3 pairs fully correct on the first attempt. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

15-20 minutes.

### Prerequisites

- The terms *inter-rater agreement*, *agreeing metric*, *flagged metric*, and *percent agreement* from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Explore (5 min).** Move one Reviewer 2 slider until a metric is flagged. Then change two scores so the totals match but five metrics disagree.
2. **Calculate (8 min).** Work through the three pairs. Find the differences on paper before you type the count.
3. **Interpret (3 min).** Explain why case B has 100% agreement even though the totals differ.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. Two scores are 5 and 9. Agree or flagged? *(Flagged. The difference is 4, which is more than 3.)*
2. Two scores are 7 and 4. Agree or flagged? *(Agree. The difference is exactly 3.)*
3. Reviewer totals are both 65. Do the reviewers agree? *(Not necessarily. Totals can match when metric scores disagree.)*
4. Seven of ten metrics agree. What is the percent agreement? *(70%.)*

### Connection to the OER Evaluator rubric

Agreement between reviewers is the first test of whether a rubric is reliable. [Chapter 14](../../chapters/14-checking-agent-output/index.md) measures agreement between an AI agent and human reviewers.

## References

1. [Inter-rater reliability](https://en.wikipedia.org/wiki/Inter-rater_reliability). Wikipedia. How agreement between independent raters is measured.
2. [Reliability (statistics)](https://en.wikipedia.org/wiki/Reliability_(statistics)). Wikipedia. Consistency of a measure across repeated use.
3. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
4. [VALUE Rubrics](https://www.aacu.org/value/rubrics). AAC&U. Level-by-level descriptors that different reviewers can apply consistently.
