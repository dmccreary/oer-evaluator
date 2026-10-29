---
title: License Selection Advisor
description: Apply three questions to choose the license that serves each of seven stated creator goals.
image: /sims/license-selection-advisor/license-selection-advisor.png
og:image: /sims/license-selection-advisor/license-selection-advisor.png
twitter:image: /sims/license-selection-advisor/license-selection-advisor.png
social:
   cards: false
status: built
quality_score: 100
---

# License Selection Advisor

<iframe src="main.html" height="686px" width="100%" scrolling="no"></iframe>

[Run the License Selection Advisor MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 2: Open Licenses and Attribution](../../chapters/02-open-licenses-attribution/index.md){ .md-button }

To edit the sketch, paste the contents of `license-selection-advisor.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/license-selection-advisor/main.html"
        height="686px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Choosing a license means choosing which freedoms to give away. Three questions drive the choice: **Will you allow commercial reuse? Will you allow others to share changed versions? Must changed versions carry the same license?** CC0 applies only when a creator wants no conditions at all.

This MicroSim states seven goals, one for each of seven licenses. For each goal you choose the license that serves it. The three questions are available on request, and opening them is exploration, not evidence.

| Commercial reuse? / Shared changes? / Same license? | License |
|---|---|
| Yes / Yes / No | CC BY |
| Yes / Yes / Yes | CC BY-SA |
| No / Yes / No | CC BY-NC |
| No / Yes / Yes | CC BY-NC-SA |
| Yes / No / not applicable | CC BY-ND |
| No / No / not applicable | CC BY-NC-ND |
| No conditions at all | CC0 |

### Controls

- **Seven license buttons:** CC0, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND.
- **Show the three questions:** opens the table above.
- **Next:** moves to the next goal.
- **Play again** and the missed-goal review on the results screen.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The goals are illustrative examples and appear in a shuffled order.
- Each goal has exactly one correct license, one per license.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **apply** the three license-selection questions to choose the license that serves each of seven stated goals, with at least 6 of 7 correct on the first attempt. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The idea of *license selection* and the licenses *CC0*, *CC BY*, *CC BY-SA*, *CC BY-NC*, *CC BY-NC-SA*, *CC BY-ND*, and *CC BY-NC-ND* from [Chapter 2](../../chapters/02-open-licenses-attribution/index.md).

### Activities

1. **Answer the questions (3 min).** Read the first goal and answer the three questions for it before you choose.
2. **Choose licenses (6 min).** Work through all seven goals. Open the table only if you are stuck.
3. **Create (4 min).** Write a goal of your own for a resource you own, answer the three questions, and name the license.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. Others may change my lesson noncommercially, and every changed version must carry my license. Which license? *(CC BY-NC-SA. NC blocks commercial use, and SA requires the same license on changes.)*
2. Anyone may share my finished report, even for sale, but nobody may share a changed version. Which license? *(CC BY-ND. ND forbids changed versions, and there is no NC element.)*
3. When is CC0 the right choice? *(Only when the goal asks for no conditions at all, not even credit.)*
4. Name two checks to make before you pick any license. *(Check who owns the work, and read any grant terms that require a specific license.)*

### Connection to the OER Evaluator rubric

The license a creator picks becomes the license a reviewer scores. [Chapter 18](../../chapters/18-components-publishing-oer/index.md) returns to licensing the components you publish.

## References

1. [License Chooser](https://creativecommons.org/chooser). Creative Commons. A questionnaire that leads a creator to a license.
2. [About CC Licenses](https://creativecommons.org/cc-licenses). Creative Commons. Plain-language summaries of what each license permits and requires.
3. [Creative Commons license](https://en.wikipedia.org/wiki/Creative_Commons_license). Wikipedia. The six main licenses and the BY, SA, NC, and ND conditions.
4. [Compatible Licenses](https://creativecommons.org/compatible-licenses). Creative Commons. Which licenses may be combined in an adaptation.
