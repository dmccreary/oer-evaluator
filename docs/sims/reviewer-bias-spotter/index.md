---
title: Reviewer Bias Spotter
description: Distinguish the bias shown in each of eight reviewer notes from six named biases and a no-bias option, and learn the defense for each.
image: /sims/reviewer-bias-spotter/reviewer-bias-spotter.png
og:image: /sims/reviewer-bias-spotter/reviewer-bias-spotter.png
twitter:image: /sims/reviewer-bias-spotter/reviewer-bias-spotter.png
social:
   cards: false
status: built
quality_score: 100
---

# Reviewer Bias Spotter

<iframe src="main.html" height="666px" width="100%" scrolling="no"></iframe>

[Run the Reviewer Bias Spotter MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To edit the sketch, paste the contents of `reviewer-bias-spotter.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/reviewer-bias-spotter/main.html"
        height="666px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Reviewer bias is a systematic tendency in a reviewer's judgment that comes from the reviewer and not from the resource. Biases are not character flaws: everyone has them, and a method works by catching them. This MicroSim shows eight reviewer notes. For each you choose the bias it shows from six named biases or **No bias**.

After each answer the sim names the bias, says why, and gives the defense. Two of the eight notes show the same bias, and one shows none.

| Bias | Defense |
|---|---|
| Halo effect | Score one metric at a time, across the whole resource |
| Anchoring | Score alone, and do not see others' scores first |
| Leniency | Score against the descriptors, not against the effort |
| Author or brand bias | Run every check, whatever the source |
| Confirmation bias | Look for evidence that would change the score |
| Fatigue | Take breaks, and review in two sessions |

### Controls

- **Seven option buttons:** the six biases and No bias. The choice is final.
- **Show bias table:** opens a table of the six biases, what happens, and the defense. Opening it is exploration, not evidence.
- **Next:** moves to the next note.
- **Play again** and the missed-note review on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The notes are illustrative examples in a shuffled order.
- The seven options are always offered.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **distinguish** the bias shown in each of eight reviewer notes from six named biases and a no-bias option, with at least 7 of 8 correct on the first attempt. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The term *reviewer bias* and the six biases listed in [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Study the table (2 min).** Open the bias table. Which two biases involve the order in which you score?
2. **Spot the bias (6 min).** Work through all eight notes and read the defense for each.
3. **Plan (4 min).** Choose the bias you are most likely to show and write the defense you will use in your next review.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. "The graphics are gorgeous, so I gave every metric an 8 or higher." Which bias? *(Halo effect. One strong feature lifted every score.)*
2. "It comes from a famous university press, so I skipped the link check." Which bias? *(Author or brand bias. The source led the reviewer to skip a check.)*
3. How does anchoring differ from the halo effect? *(Anchoring is pulled by a number seen first. The halo effect is pulled by one strong feature.)*
4. What does a note with no bias look like? *(It shows a check, a record, and a score that follows from them.)*

### Connection to the OER Evaluator rubric

Naming a bias is the first step in correcting for it. [Chapter 14](../../chapters/14-checking-agent-output/index.md) shows how an AI agent's scores can drift too, as score inflation, and how to check them against human reviewers.

## References

1. [Halo effect](https://en.wikipedia.org/wiki/Halo_effect). Wikipedia. One striking trait coloring the judgment of every other trait.
2. [Anchoring effect](https://en.wikipedia.org/wiki/Anchoring_effect). Wikipedia. The first number seen pulls later judgments toward it.
3. [Confirmation bias](https://en.wikipedia.org/wiki/Confirmation_bias). Wikipedia. Looking for evidence that fits an expectation.
4. [Inter-rater reliability](https://en.wikipedia.org/wiki/Inter-rater_reliability). Wikipedia. How agreement between independent raters is measured.
