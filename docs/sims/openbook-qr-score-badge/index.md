---
title: OpenBook QR Score Badge
description: Build and read an OpenBook QR Score badge, the total out of 100 reported with its quality and reusability halves, and save the badge as a PNG.
image: /sims/openbook-qr-score-badge/openbook-qr-score-badge.png
og:image: /sims/openbook-qr-score-badge/openbook-qr-score-badge.png
twitter:image: /sims/openbook-qr-score-badge/openbook-qr-score-badge.png
social:
   cards: false
status: built
---

# OpenBook QR Score Badge

<iframe src="main.html" height="752px" width="100%" scrolling="no"></iframe>

[Run the OpenBook QR Score Badge MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 3: The Ten-Metric Rubric and Scoring](../../chapters/03-ten-metric-rubric-scoring/index.md){ .md-button }

To edit the sketch, paste the contents of `openbook-qr-score-badge.js` into the [p5.js editor](https://editor.p5js.org/). The six example resources and the three build targets are in the `PRESETS` and `TARGETS` blocks near the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/openbook-qr-score-badge/main.html"
        height="752px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

The **OpenBook QR Score** is the total of the ten-metric rubric, reported with its two halves: **Q** for the quality subtotal and **R** for the reusability subtotal. It is always written the same way, for example **QR 65 (Q 32 / R 33)**. The badge turns that result into a picture.

The badge is a small grid, a little like a QR code. The top row of five modules is quality, and the bottom row of five is reusability. Each module fills from the bottom in proportion to its score, so a score of 10 is a full module and a score of 0 is empty. A module below the floor of 5 gets a dashed outline and a "!" mark, so the warning does not depend on color alone. The text under the grid gives the OpenBook QR Score and the band.

The corner squares and the dotted line are decoration. The badge is not a scannable code, and nothing is encoded in it.

### Controls

- **Example resource menu:** loads one of six illustrative resources. Moving a slider switches the menu to *My own scores*.
- **Ten sliders:** set each metric score from 0 to 10 in whole points. Quality is on the left and reusability is on the right.
- **Show scores on badge:** shows or hides the number on each module.
- **Save badge PNG:** downloads the badge as an image with a transparent background, to put in a review report or a README.
- **Build challenge:** switches to three target badges. Set the sliders until the badge reads the target, then press **Check**, and **Next** for the following target. **Back to explore** returns to the example resources.

### Good to Know

Only the first **Check** of each target counts as evidence. You can keep adjusting and check again, and the feedback names which half is off.

- The band and decision shown in explore mode use the book's starting rule: Adopt when the total is 75 or more and every metric is 5 or more, and Reject when the total is below 50. These are starting values, not a standard.
- The six resources are illustrative examples. *Watershed Basics* is the worked example from Chapters 3 and 15.
- The MicroSim does not store anything you do.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **write** the OpenBook QR Score for a resource, in the form QR *total* (Q *quality* / R *reusability*), from ten metric scores, and can name which half and which metric hold the total down. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The terms *quality subtotal*, *reusability subtotal*, *total score*, and *OpenBook QR Score* from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md).

### Activities

1. **Explore (4 min).** Load *Locked Chemistry E-book* and then *Watershed Basics (before)*. Both total 65. Compare the two badges and their QR strings. What does each one tell you that the total alone does not?
2. **Improve (3 min).** Load *Watershed Basics (before)*, then raise Metadata, Accessibility, Modularity, Practice, and Accuracy as in the Chapter 15 plan and watch the string change. Which row changed most?
3. **Build (5 min).** Press **Build challenge** and build all three targets. For the third, explain why the decision is Revise even though the total is 79.
4. **Share (2 min).** Save a badge PNG for a resource you have scored by hand.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. Quality is 32 and reusability is 33. How is the OpenBook QR Score written? *(QR 65 (Q 32 / R 33).)*
2. Two resources both have QR 65. One is Q 44 / R 21 and the other is Q 32 / R 33. Which is held back by reuse? *(The first one: its reusability half is only 21 of 50.)*
3. A badge has a module with a dashed outline and a "!". What does it mean? *(That metric scored below the floor of 5.)*
4. A resource reads QR 79 (Q 47 / R 32) and its Open license score is 1. Is it ready to adopt? *(No. The floor catches the failed metric, so the decision is Revise.)*

### Connection to the OER Evaluator rubric

This is how every review report in the book states its result. [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md) defines the OpenBook QR Score, [Chapter 11](../../chapters/11-manual-evaluation-adoption/index.md) uses it in a full manual evaluation, and [Chapter 15](../../chapters/15-improving-resources-with-ai/index.md) reports a score gain as a move from one QR string to another.

## References

1. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Criteria, performance levels, and analytic versus holistic rubrics.
2. [QR code](https://en.wikipedia.org/wiki/QR_code). Wikipedia. The matrix layout and corner finder patterns that the badge imitates for looks only.
3. [Not All Rubrics Are Equal: A Review of Rubrics for Evaluating the Quality of Open Educational Resources](https://www.irrodl.org/index.php/irrodl/article/view/2389). IRRODL. Compares fourteen OER quality rubrics.
