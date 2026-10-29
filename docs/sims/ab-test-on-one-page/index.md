---
title: "The A/B Test on One Page"
description: "A left-to-right flow of the whole A/B test: a pool of students is randomly assigned to the original or the improved version, both groups take the same pre-test and post-test, and learning gain is compared."
image: /sims/ab-test-on-one-page/ab-test-on-one-page.png
og:image: /sims/ab-test-on-one-page/ab-test-on-one-page.png
twitter:image: /sims/ab-test-on-one-page/ab-test-on-one-page.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="753px" width="100%" scrolling="no"></iframe>

[Run the A/B Test on One Page MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 16: Designing an A/B Test with Students](../../chapters/16-ab-testing-design/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `ab-test-on-one-page.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/ab-test-on-one-page/main.html"
        height="753px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

The A/B test is the book's main method for checking whether an improvement helped, and its concepts are introduced in separate sections. This poster is the "design on one page" from Chapter 16. A pool of students is randomly assigned to two groups. The control group uses the original version (v1, rubric total 65, Revise) and the treatment group uses the improved version (v1.1, total 78, Adopt). Both take the same pre-test before and the same post-test after, and the comparison is the learning gain. The two groups are drawn as mirror images so the only visible difference is the version. A time strip along the bottom follows the schedule of Chapter 17: pre-test and assignment in week 1, use of the assigned version in weeks 2 and 3, and post-test and survey in week 4. The artwork has no text, so the numbers can follow the chapter if it changes.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | The hypothesis | The hypothesis states what you expect, such as that the improved version gives a larger learning gain than the original. In the pilot it set a threshold of 5 points. |
| 2 | Random assignment | Students are assigned to the two groups at random, like shuffled tokens. Random assignment spreads motivation and ability evenly, so students do not choose their group. |
| 3 | The control group | The control group uses the original version, v1, with a rubric total of 65 (Revise). It receives ordinary teaching with the original, not no teaching. |
| 4 | The treatment group | The treatment group uses the improved version, v1.1, with a rubric total of 78 (Adopt). Everything else is the same as for the control group. |
| 5 | The pre-test | Both groups take the same pre-test before the lesson, in week 1. It shows where each student starts, so the gain can be measured. |
| 6 | The post-test and the learning gain | Both groups take the same post-test in week 4. The comparison is the learning gain of each group, the post-test score minus the pre-test score. |
| 7 | Consent and privacy | Students and families are informed, and student data is protected. The pool is drawn as plain silhouettes with no identifying features. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- The rubric totals 65 and 78 and the version labels follow the chapter and are shown in the marker descriptions, not in the artwork.
- Students are drawn as plain silhouettes with no identifying features.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **describe** the parts of a classroom A/B test and **explain** why the two groups must differ only in the version. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Control group, treatment group, and random assignment from [Chapter 16](../../chapters/16-ab-testing-design/index.md).

### Activities

1. **Explore (4 min).** Hover over markers 1 to 7. Which two parts must be identical for both groups?
2. **Quiz (3 min).** Press **Quiz** and find each part from its description.
3. **Draft (3 min).** Write one sentence for your hypothesis. Which of the seven parts will be hardest to arrange in your class?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. What does the control group receive? *(Ordinary teaching with the original version, not no teaching.)*
2. Why is assignment random? *(So that motivated or stronger students do not end up in one group by choice.)*
3. What is the comparison at the end? *(The learning gain of each group, from the pre-test to the post-test.)*

### Connection to the OER Evaluator rubric

Chapter 17 analyzes the results. A reviewer can use this poster to check a test plan, and a teacher can use it to draft one.

## References

1. [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) - Wikipedia - Defines A/B testing, how users are split between versions, and how results are compared. The core idea behind comparing an original resource with its improved version.
2. [Randomized controlled trial](https://en.wikipedia.org/wiki/Randomized_controlled_trial) - Wikipedia - Explains random assignment to treatment and control groups and why it supports causal claims. Background for the chapter's sections on random assignment and control and treatment groups.
3. [Informed consent](https://en.wikipedia.org/wiki/Informed_consent) - Wikipedia - Describes what people must be told and agree to before taking part in research, and the special rules for minors. Supports the chapter's guidance on consent and student privacy.
4. [Sample Size Calculator](https://www.evanmiller.org/ab-testing/sample-size.html) - Evan Miller - A free calculator that estimates how many participants a two-group test needs for a chosen effect and confidence. Supports the chapter's sample size planning.
