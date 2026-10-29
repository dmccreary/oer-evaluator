---
title: License Compatibility Checker
description: Solve ten license-combination problems by finding the license a combined work may carry, or by spotting a conflict or a blocked combination.
image: /sims/license-compatibility-checker/license-compatibility-checker.png
og:image: /sims/license-compatibility-checker/license-compatibility-checker.png
twitter:image: /sims/license-compatibility-checker/license-compatibility-checker.png
social:
   cards: false
status: built
quality_score: 100
---

# License Compatibility Checker

<iframe src="main.html" height="614px" width="100%" scrolling="no"></iframe>

[Run the License Compatibility Checker MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 2: Open Licenses and Attribution](../../chapters/02-open-licenses-attribution/index.md){ .md-button }

To edit the sketch, paste the contents of `license-compatibility-checker.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/license-compatibility-checker/main.html"
        height="614px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

When you combine two openly licensed sources into one work, each source sets conditions on the license of the result. This MicroSim shows ten pairs of source licenses. For each pair you choose the license the combined work may carry, or **Conflict** when no license satisfies both sources, or **Blocked** when one source is an ND license.

The rule: the answer is the first license, in the order CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, that both sources allow. If the two allowed sets share no license the answer is Conflict. If either source is an ND license the answer is Blocked.

| Source | Licenses the combined work may carry |
|---|---|
| CC0 and CC BY | CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA |
| CC BY-SA | CC BY-SA |
| CC BY-NC | CC BY-NC, CC BY-NC-SA |
| CC BY-NC-SA | CC BY-NC-SA |
| CC BY-ND and CC BY-NC-ND | None: the combination is Blocked |

### Controls

- **Six outcome buttons:** CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, Conflict, Blocked.
- **Show requirements table:** opens the table above. Opening it is exploration, not evidence. On a narrow screen a long table has page buttons.
- **Next:** moves to the next pair.
- **Play again** and the missed-pair review on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The pairs are illustrative examples, always in the same order. This is a study aid, not legal advice.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **solve** ten license-combination problems by finding the license a combined work may carry, or by recognizing a conflict or a blocked combination, with at least 8 of 10 correct on the first attempt. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The licenses *CC0*, *CC BY*, *CC BY-SA*, *CC BY-NC*, *CC BY-NC-SA*, *CC BY-ND*, and *CC BY-NC-ND* and the idea of *license compatibility* from [Chapter 2](../../chapters/02-open-licenses-attribution/index.md).

### Activities

1. **Study the table (2 min).** Open the requirements table and say why CC BY-SA and CC BY-NC cannot be combined.
2. **Solve the pairs (8 min).** Work through all ten pairs, opening the table only when you need it.
3. **Generalize (3 min).** Write a one-line rule for each of the three outcome types: a license, Conflict, and Blocked.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. CC BY with CC BY-SA. What may the combined work carry? *(CC BY-SA. Only CC BY-SA satisfies the second source, and CC BY accepts it.)*
2. CC BY-SA with CC BY-NC. What is the outcome? *(Conflict. CC BY-SA allows only CC BY-SA, and CC BY-NC allows only noncommercial licenses.)*
3. CC BY with CC BY-ND. What is the outcome? *(Blocked. The ND source cannot be changed or blended and then shared.)*
4. CC0 with CC BY-SA. What may the combined work carry? *(CC BY-SA. CC0 allows any of the four, and CC BY-SA is the only one that satisfies the other source.)*

### Connection to the OER Evaluator rubric

A resource built from open parts is only reusable if its license is consistent. [Chapter 4](../../chapters/04-open-formats-version-control/index.md) explains why editable source files make remixing practical.

## References

1. [Compatible Licenses](https://creativecommons.org/compatible-licenses). Creative Commons. Which licenses may be combined in an adaptation.
2. [License compatibility](https://en.wikipedia.org/wiki/License_compatibility). Wikipedia. Why works under different licenses cannot always be combined.
3. [About CC Licenses](https://creativecommons.org/cc-licenses). Creative Commons. Plain-language summaries of what each license permits and requires.
4. [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license). Wikipedia. The six main licenses and the BY, SA, NC, and ND conditions.
