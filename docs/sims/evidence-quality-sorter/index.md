---
title: Evidence or Opinion Sorter
description: Judge ten review notes as checkable evidence or not evidence yet by looking for a location, an observation, and a rule.
image: /sims/evidence-quality-sorter/evidence-quality-sorter.png
og:image: /sims/evidence-quality-sorter/evidence-quality-sorter.png
twitter:image: /sims/evidence-quality-sorter/evidence-quality-sorter.png
social:
   cards: false
status: built
quality_score: 100
---

# Evidence or Opinion Sorter

<iframe src="main.html" height="654px" width="100%" scrolling="no"></iframe>

[Run the Evidence or Opinion Sorter MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To edit the sketch, paste the contents of `evidence-quality-sorter.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/evidence-quality-sorter/main.html"
        height="654px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

A score needs evidence another reviewer could check. A note is **checkable evidence** when it gives (1) where the reviewer looked, (2) what the reviewer saw, as a quote, count, or measurement, and (3) the rule it was compared with. This MicroSim shows ten review notes and you place each in one of two bins.

An unchecked claim by an AI agent is always **Not evidence yet**, because nobody has checked it. Each bin holds five notes.

| Bin | Meaning |
|---|---|
| Checkable evidence | All three parts are present: where, what, and the rule. |
| Not evidence yet | One or more parts are missing, so no other reviewer could repeat the check. |

### Controls

- **Two bin buttons:** place the note. The placement is final.
- **Next:** moves to the next note.
- **Show definitions:** on a narrow screen the test and bin definitions move behind this button.
- **Play again** and the missed-note review on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The notes are illustrative examples in a shuffled order.
- A note counts as evidence only when all three parts are present.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **judge** whether each of ten review notes is checkable evidence or not yet evidence, by looking for a location, an observation, and a rule, with at least 9 of 10 correct on the first attempt. (Bloom level: Evaluate.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The ideas of *evidence for a score* and *evidence citation* from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Learn the test (2 min).** Read the three-part test and say which part is missing from "The text seems accurate."
2. **Sort the notes (6 min).** Place all ten notes and read each reason.
3. **Repair (4 min).** Rewrite two "Not evidence yet" notes so that they pass the test.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. "The alt text is probably fine." Evidence? *(Not evidence yet. "Probably" shows no one looked.)*
2. "Page 7 link returns an error, tested on 2026-10-12." Evidence? *(Checkable evidence. It gives the location, the observation, the rule, and the date.)*
3. "The AI agent said the license is CC BY." Evidence? *(Not evidence yet. An agent's claim is a statement to check.)*
4. Why does a count help? *(Another reviewer can repeat a count and compare it with yours.)*

### Connection to the OER Evaluator rubric

Evidence is how a reviewer defends a score, and how a team spots a biased one. [Chapter 14](../../chapters/14-checking-agent-output/index.md) treats an AI agent's claims the same way: as statements to verify before they count.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
2. [Creating and Using Rubrics](https://www.cmu.edu/teaching/assessment/assesslearning/rubrics.html). Carnegie Mellon Eberly Center. The parts of a rubric and how to use it.
3. [Inter-rater reliability](https://en.wikipedia.org/wiki/Inter-rater_reliability). Wikipedia. How agreement between independent raters is measured.
4. [VALUE Rubrics](https://www.aacu.org/value/rubrics). AAC&U. Level-by-level descriptors that different reviewers can apply consistently.
