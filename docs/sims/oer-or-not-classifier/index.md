---
title: OER or Not Classifier
description: Place eleven resource cards in three bins (Open OER, Free but not open, Not free and not open) to see that openness comes from the license, not the price.
image: /sims/oer-or-not-classifier/oer-or-not-classifier.png
og:image: /sims/oer-or-not-classifier/oer-or-not-classifier.png
twitter:image: /sims/oer-or-not-classifier/oer-or-not-classifier.png
social:
   cards: false
status: built
quality_score: 100
---

# OER or Not Classifier

<iframe src="main.html" height="690px" width="100%" scrolling="no"></iframe>

[Run the OER or Not Classifier MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 1: Foundations of Open Educational Resources](../../chapters/01-foundations-of-oer/index.md){ .md-button }

To edit the sketch, paste the contents of `oer-or-not-classifier.js` into the [p5.js editor](https://editor.p5js.org/). The learning content (the items, answers, and reasons) is in the `CONFIG` block at the top of the file.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/oer-or-not-classifier/main.html"
        height="690px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

A resource can cost nothing and still be closed, and it can cost money and still be open. This MicroSim shows eleven described resources, one at a time. You decide whether each is **Open (OER)**, **Free but not open**, or **Not free and not open** by checking its license and public-domain status instead of its price.

After each placement the card flies into its correct bin, and you read the reason. The bins stay on screen the whole time, so you can compare a new card with the cards you have already placed.

| Bin | What it holds |
|---|---|
| Open (OER) | The resource is in the public domain or carries an open license, whatever its price. |
| Free but not open | The resource costs nothing but is neither in the public domain nor under an open license. |
| Not free and not open | The resource costs money and is neither in the public domain nor under an open license. |

### Controls

- **Three bin buttons:** place the current card. The placement is final.
- **Next:** moves to the next card after you read the feedback.
- **Show definitions:** on a narrow screen the bin definitions move behind this button.
- **Previous missed / Next missed:** on the results screen, page through the cards you missed.
- **Play again:** shuffles the cards for a practice run.

### Good to Know

Only your first committed answer on the first completed run counts as evidence of mastery. Practice runs give the same feedback but do not change that first-run score. Nothing moves until you act, and the MicroSim does not store your answers.

- The eleven cards are illustrative examples written for Chapter 1.
- A card with no license statement counts as all rights reserved, and a price never moves a resource out of the Open bin.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **classify** each of 11 described resources as open (OER), free but not open, or not free and not open, by checking its license and public-domain status rather than its price. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

10-15 minutes.

### Prerequisites

- The terms *educational resource*, *copyright*, *license*, *public domain*, *open license*, *free resource*, and *open educational resource* from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).

### Activities

1. **Predict (2 min).** Read the three bin definitions. Before placing any card, write down which bin you think a free online course with the terms "personal use only" belongs in.
2. **Place the cards (5 min).** Place all 11 cards. Read the reason after each one, especially the ones you got wrong.
3. **Review (3 min).** On the results screen, page through the missed cards and say aloud what you checked the first time and what you should have checked.
4. **Replay (2 min).** Press **Play again** and aim for a perfect run. Practice runs do not change the first-run score.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by using it.

1. A quiz bank under CC0 is sold on a marketplace for $5. Which bin? *(Open (OER). CC0 grants the permissions, and the price does not change that.)*
2. A video streams free of charge and shows no license. Which bin? *(Free but not open. With no license the default is all rights reserved.)*
3. Why is a photograph taken by a NASA employee as part of their job an open resource? *(Works made by U.S. federal employees as part of their duties are in the public domain.)*
4. What single question separates the Open bin from the other two? *(Does a license or the public domain grant permission to retain, reuse, revise, remix, and redistribute?)*

### Connection to the OER Evaluator rubric

The first question a reviewer asks about any resource is whether it is open. [Chapter 9](../../chapters/09-modularity-metadata/index.md) scores the license metric on how clearly a resource states what others may do.

## References

1. [Open educational resources](https://en.wikipedia.org/wiki/Open_educational_resources). Wikipedia. Defines OER and lists the 5R permissions.
2. [Free content](https://en.wikipedia.org/wiki/Free_content). Wikipedia. Separates works that merely cost nothing from works that grant freedoms.
3. [Copyright](https://en.wikipedia.org/wiki/Copyright). Wikipedia. Explains why all rights are reserved by default.
4. [Definition of Open](https://opencontent.org/definition/). opencontent.org. David Wiley's statement of the 5R permissions.
