---
title: Five R Scenario Matcher
description: Match ten everyday teacher actions to the one of the five R permissions (retain, reuse, revise, remix, redistribute) that each action uses.
image: /sims/five-r-scenario-matcher/five-r-scenario-matcher.png
og:image: /sims/five-r-scenario-matcher/five-r-scenario-matcher.png
twitter:image: /sims/five-r-scenario-matcher/five-r-scenario-matcher.png
social:
   cards: false
status: built
quality_score: 100
---

# Five R Scenario Matcher

<iframe src="main.html" height="634px" width="100%" scrolling="no"></iframe>

[Run the Five R Scenario Matcher MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 1: Foundations of Open Educational Resources](../../chapters/01-foundations-of-oer/index.md){ .md-button }

To edit the sketch, paste the contents of `five-r-scenario-matcher.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/five-r-scenario-matcher/main.html"
        height="634px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

An open license grants five permissions: **retain**, **reuse**, **revise**, **remix**, and **redistribute**. This MicroSim gives you ten everyday teacher actions, one at a time, and you name the one permission that each action uses.

You get two tries on each action. If your first answer is wrong, the sim shows the test question for the right permission without naming it. Only a correct first answer counts as evidence of mastery.

| Permission | Test question |
|---|---|
| Retain | Can I make and keep my own copy? |
| Reuse | Can I use it as it is? |
| Revise | Can I change it? |
| Remix | Can I combine it with other open work? |
| Redistribute | Can I share copies with others? |

### Controls

- **Five permission buttons:** choose the permission the action uses.
- **Next:** moves on after you read the feedback.
- **Previous missed / Next missed:** on the results screen, page through the actions you missed.
- **Play again:** reshuffles the ten actions for a practice run.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The scenarios are illustrative examples written for Chapter 1.
- Where a scenario says a step is already done, only the action happening now counts. The MicroSim does not test license conditions such as credit or share-alike.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **apply** the definitions of the five R permissions to name the one permission that each of 10 classroom actions exercises, with at least 8 correct on the first attempt. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The terms *open license* and the five permissions *retain*, *reuse*, *revise*, *remix*, and *redistribute* from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).

### Activities

1. **Recall (2 min).** Write the five test questions from memory, then check them against the table above.
2. **Match the actions (6 min).** Work through the ten actions. When a hint appears, answer the test question before you choose again.
3. **Explain (3 min).** For each action you needed a hint on, explain in one sentence why the permission you first chose was wrong.
4. **Replay (2 min).** Press **Play again** and try to answer every action correctly on the first try.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. You email a colleague an unchanged copy of an open worksheet. Which permission? *(Redistribute. Sharing copies with others is redistributing.)*
2. You add alt text to every image in an open chapter. Which permission? *(Revise. Adding alt text changes the work.)*
3. You download the editable source files of an open lab manual for safekeeping. Which permission? *(Retain. Making and keeping your own copy is retaining.)*
4. What is the difference between revise and remix? *(Revise changes one work. Remix combines two or more works into something new.)*

### Connection to the OER Evaluator rubric

The five permissions are the vocabulary behind the open license and editable source metrics. [Chapter 4](../../chapters/04-open-formats-version-control/index.md) shows why editable source files make revise and remix possible.

## References

1. [Definition of Open](https://opencontent.org/definition/). opencontent.org. David Wiley's statement of the 5R permissions.
2. [Open educational resources](https://en.wikipedia.org/wiki/Open_educational_resources). Wikipedia. Defines OER and lists the 5R permissions.
3. [Open Educational Resources](https://www.unesco.org/en/open-educational-resources). UNESCO. The international Recommendation on OER.
4. [OER Resources for Educators](https://creativecommons.org/about/education/education-oer-resources). Creative Commons. A teacher's guide to finding openly licensed materials.
