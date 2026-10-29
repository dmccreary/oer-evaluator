---
title: Attribution Statement Checker
description: Assess eight attribution statements by marking exactly which of five parts (title, author, source, license, change note) are missing.
image: /sims/attribution-statement-checker/attribution-statement-checker.png
og:image: /sims/attribution-statement-checker/attribution-statement-checker.png
twitter:image: /sims/attribution-statement-checker/attribution-statement-checker.png
social:
   cards: false
status: built
quality_score: 100
---

# Attribution Statement Checker

<iframe src="main.html" height="814px" width="100%" scrolling="no"></iframe>

[Run the Attribution Statement Checker MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 2: Open Licenses and Attribution](../../chapters/02-open-licenses-attribution/index.md){ .md-button }

To edit the sketch, paste the contents of `attribution-statement-checker.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/attribution-statement-checker/main.html"
        height="814px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

A good credit line names the title, the author, the source, and the license (TASL), and adds a change note when the work was changed. This MicroSim shows one made-up resource, "Watershed Basics", and eight statements that credit it. For each statement you mark exactly which parts are missing, or choose **None missing**, and press **Check**.

A judgment is correct only when your marked set equals the true set of missing parts. The Change note button is offered only for the three statements whose use changed the work.

| Part | Counts as present when |
|---|---|
| Title | The work's name appears. |
| Author | The creator's name appears. |
| Source | A link to the work appears. A site name alone does not count. |
| License | A specific license with its version, or a link to it, appears. "Creative Commons" alone, or "CC BY" with no version or link, does not count. |
| Change note | A sentence says what was changed. Required only when the use changed the work. |

### Controls

- **Title, Author, Source, License, Change note:** mark each part that is missing. A mark is a toggle, and a check badge shows it is on.
- **None missing:** marks the statement as complete and clears the other marks.
- **Check:** commits your answer and shows the correct set.
- **Show definitions:** on a narrow screen the part definitions move behind this button.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The statements are illustrative examples. This is a study aid, not legal advice.
- The five parts are checked as a set, so marking a part that is present is as much a mistake as missing one that is not.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **assess** whether each of eight attribution statements is complete by identifying exactly which of the five checked parts are missing, with at least 7 of 8 judged correctly on the first attempt. (Bloom level: Evaluate.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The terms *attribution requirement*, *title, author, source, and license (TASL)*, and *change note* from [Chapter 2](../../chapters/02-open-licenses-attribution/index.md).

### Activities

1. **Read the rules (2 min).** Read the five parts and when each counts as present.
2. **Check the statements (8 min).** Mark and check all eight statements. After each, compare the correct set with your marks.
3. **Rewrite (3 min).** Choose one statement you got wrong and rewrite it so that all four TASL parts are present.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. "Watershed Basics", link, licensed CC BY. What is missing? *(Author and License. The creator is not named, and "CC BY" has no version or link.)*
2. Image courtesy of Maria Lopez. What is missing? *(Title, Source, and License.)*
3. Is a change note needed for an unchanged copy? *(No. It is required only when the use changed the work.)*
4. Does a copyright line with no license count as credit? *(No. It leaves the license missing, and "All rights reserved" contradicts a CC BY license.)*

### Connection to the OER Evaluator rubric

Complete attribution is part of what the open license metric checks. [Chapter 9](../../chapters/09-modularity-metadata/index.md) scores whether attribution is complete.

## References

1. [Recommended Practices for Attribution](https://wiki.creativecommons.org/wiki/Best_practices_for_attribution). CC Public Wiki. Good and weak credit lines for CC-licensed work.
2. [About CC Licenses](https://creativecommons.org/cc-licenses). Creative Commons. Plain-language summaries of what each license permits and requires.
3. [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license). Wikipedia. The six main licenses and the BY, SA, NC, and ND conditions.
4. [Copyright](https://en.wikipedia.org/wiki/Copyright). Wikipedia. Explains why all rights are reserved by default.
