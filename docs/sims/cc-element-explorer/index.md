---
title: Creative Commons Element Explorer
description: Switch the ShareAlike, NonCommercial, and NoDerivatives elements on and off, then predict what each resulting license allows.
image: /sims/cc-element-explorer/cc-element-explorer.png
og:image: /sims/cc-element-explorer/cc-element-explorer.png
twitter:image: /sims/cc-element-explorer/cc-element-explorer.png
social:
   cards: false
status: built
quality_score: 100
---

# Creative Commons Element Explorer

<iframe src="main.html" height="690px" width="100%" scrolling="no"></iframe>

[Run the Creative Commons Element Explorer MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 2: Open Licenses and Attribution](../../chapters/02-open-licenses-attribution/index.md){ .md-button }

To edit the sketch, paste the contents of `cc-element-explorer.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/cc-element-explorer/main.html"
        height="690px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

A Creative Commons license is a set of elements. **BY** (Attribution) is always on. You can add **SA** (ShareAlike), **NC** (NonCommercial), and **ND** (NoDerivatives). SA and ND never appear together, because ShareAlike governs adaptations that NoDerivatives forbids anyone to share.

In explore mode, three switches build a license and the screen shows Yes or No for five actions, with the reason for each No. When you are ready, prediction mode asks eight "Allowed?" questions and makes you commit an answer before it is shown.

| Action | What it asks |
|---|---|
| A1 | Post an unchanged copy on your website, with credit. |
| A2 | Post a translated version. |
| A3 | Sell printed copies for profit. |
| A4 | Publish a remix of it under CC BY. |
| A5 | Change it privately for your own use and do not share it. |

### Controls

- **SA, NC, and ND switches:** turn each element on or off. Turning on SA while ND is on, or the reverse, shows an explanation instead of changing the license.
- **Start the predictions:** leaves explore mode.
- **Yes and No buttons:** commit a prediction.
- **Back to explore:** on the results screen, returns to the switches.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The actions are illustrative examples. The results follow the 4.0 licenses and are a study aid, not legal advice.
- A1 is Yes for every license, and A5 is Yes for every license, because no license forbids private changes.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **infer** whether each of five actions is allowed under a given Creative Commons license by reasoning from its elements, with at least 7 of 8 predictions correct on the first attempt. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The four elements *Attribution*, *ShareAlike*, *NonCommercial*, and *NoDerivatives*, and the six licenses they form, from [Chapter 2](../../chapters/02-open-licenses-attribution/index.md).

### Activities

1. **Explore (5 min).** Build all six licenses with the switches. For each, say which actions are No and why.
2. **Find the rule (2 min).** Find the two licenses where A2 (a translation) is No, and say what they share.
3. **Predict (5 min).** Press **Start the predictions** and answer all eight questions.
4. **Review (2 min).** For each miss, go back to explore mode and rebuild that license.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. A translation of a CC BY-ND work: allowed to post? *(No. ND forbids sharing a changed version, and a translation is a change.)*
2. Can you sell printed copies of a CC BY-NC work? *(No. NC forbids use directed toward monetary compensation.)*
3. Can you privately change a CC BY-NC-ND work? *(Yes. ND blocks sharing changed versions, not private changes.)*
4. Why can SA and ND not both be on? *(SA governs adaptations that ND forbids anyone to share.)*

### Connection to the OER Evaluator rubric

The more elements are on, the lower the license sits on the openness spectrum. [Chapter 9](../../chapters/09-modularity-metadata/index.md) shows how the rubric scores a license along that spectrum.

## References

1. [About CC Licenses](https://creativecommons.org/cc-licenses). Creative Commons. Plain-language summaries of what each license permits and requires.
2. [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license). Wikipedia. The six main licenses and the BY, SA, NC, and ND conditions.
3. [Compatible Licenses](https://creativecommons.org/compatible-licenses). Creative Commons. Which licenses may be combined in an adaptation.
4. [License Chooser](https://creativecommons.org/chooser). Creative Commons. A questionnaire that leads a creator to a license.
