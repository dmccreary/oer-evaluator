---
title: Adopt, Adapt, or Create Pathway Chooser
description: Use a three-fact rule of thumb to choose adopt, adapt, create, or keep searching for four teacher cases, then explore which facts change the answer.
image: /sims/adopt-adapt-create-pathway-chooser/adopt-adapt-create-pathway-chooser.png
og:image: /sims/adopt-adapt-create-pathway-chooser/adopt-adapt-create-pathway-chooser.png
twitter:image: /sims/adopt-adapt-create-pathway-chooser/adopt-adapt-create-pathway-chooser.png
social:
   cards: false
status: built
quality_score: 100
---

# Adopt, Adapt, or Create Pathway Chooser

<iframe src="main.html" height="690px" width="100%" scrolling="no"></iframe>

[Run the Adopt, Adapt, or Create Pathway Chooser MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 1: Foundations of Open Educational Resources](../../chapters/01-foundations-of-oer/index.md){ .md-button }

To edit the sketch, paste the contents of `adopt-adapt-create-pathway-chooser.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/adopt-adapt-create-pathway-chooser/main.html"
        height="690px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Teachers put OER to work in three ways: adopt it as it is, adapt it by changing it, or create something new. Sometimes the right move is to keep searching. This MicroSim gives you four teacher cases. Each case states three facts: **fit to the course outcomes** (Full, Partial, or None), whether **revision is permitted** (Yes or No), and the **time available** (Little or Much).

You predict the pathway before the rule is shown. Then an explore screen lets you set the three facts yourself and watch the pathway and the rule number change. The rule is a simple rule of thumb, not a standard, and the 40-hour threshold for time is illustrative.

| Rule | Pathway |
|---|---|
| 1. Fit is Full | Adopt, whatever the other two facts are |
| 2. Fit is Partial and revision is permitted | Adapt |
| 3. Fit is Partial and revision is not permitted | Keep searching, because a partial fit that may not be changed cannot be fixed |
| 4. Fit is None and time is Much | Create |
| 5. Fit is None and time is Little | Keep searching |

### Controls

- **Four pathway buttons:** choose Adopt, Adapt, Create, or Keep searching for the case.
- **Next:** moves to the next case.
- **Explore the rule:** on the results screen, opens three drop-down lists (fit, revision permitted, time available) that show the pathway, the rule number, and which facts matter.
- **Back to results:** returns from the explore screen.
- **Play again:** repeats the four cases.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The cases are illustrative examples written for Chapter 1, and they always appear in the order A, B, C, D.
- Revision permission has no effect when fit is Full or None, and time matters only when fit is None.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **use** a three-fact decision rule (fit to the course, whether revision is permitted, and time available) to choose adopt, adapt, create, or keep searching for four teacher cases, with at least 3 of 4 correct on the first attempt. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The terms *OER adoption*, *OER adaptation*, *OER creation*, and *revise permission* from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).

### Activities

1. **Predict (4 min).** For each of the four cases, choose a pathway before you see the rule. Notice which fact you relied on.
2. **Read the rule (2 min).** After each answer, read which rule applied and why.
3. **Explore (4 min).** Open **Explore the rule**. Find the three fact settings that give each of the four pathways. Then find a fact that never changes the answer for Full fit.
4. **Reflect (2 min).** Explain in one sentence why a partial fit with no revision permission is "keep searching" and not "adapt".

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. Fit is Full, revision is not permitted, time is Little. Which pathway? *(Adopt (rule 1). Revision permission does not matter when the fit is Full.)*
2. Fit is None, revision is permitted, time is Little. Which pathway? *(Keep searching (rule 5). Without time, creating is not realistic.)*
3. Which one fact changes the answer only when fit is None? *(Time available.)*
4. Why is "create" not always the best choice? *(Creating takes the most time, and a good fit already in hand makes adopting cheaper.)*

### Connection to the OER Evaluator rubric

A teacher who keeps searching still needs a way to compare candidates. [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md) introduces the ten-metric rubric that scores each candidate, and [Chapter 11](../../chapters/11-manual-evaluation-adoption/index.md) uses the scores for adoption decisions.

## References

1. [Open educational resources](https://en.wikipedia.org/wiki/Open_educational_resources). Wikipedia. Defines OER and lists the 5R permissions.
2. [OER Resources for Educators](https://creativecommons.org/about/education/education-oer-resources). Creative Commons. A teacher's guide to finding openly licensed materials.
3. [OpenStax](https://openstax.org/). Rice University. A well-known collection of adoptable open textbooks.
4. [Definition of Open](https://opencontent.org/definition/). opencontent.org. David Wiley's statement of the 5R permissions.
