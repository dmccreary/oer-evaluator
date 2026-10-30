---
title: "A One-Day Workshop Timeline"
description: "A horizontal timeline from 8:30 to 3:30 built from the chapter's sample agenda, with block widths in proportion to time and a token for what teachers leave with."
image: /sims/one-day-workshop-timeline/one-day-workshop-timeline.png
og:image: /sims/one-day-workshop-timeline/one-day-workshop-timeline.png
twitter:image: /sims/one-day-workshop-timeline/one-day-workshop-timeline.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="640px" width="100%" scrolling="no"></iframe>

[Run the A One-Day Workshop Timeline MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 19: Training Teachers and Certifying Reviewers](../../chapters/19-training-certifying-reviewers/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `one-day-workshop-timeline.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/one-day-workshop-timeline/main.html"
        height="640px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

A facilitator can print this poster for the room, and participants can see the logic of the day and what they carry out of it. It is built from the sample agenda in Chapter 19: check-in and setup, the ten metrics, calibration by hand and then with the agent, checking the agent, lunch, the improvement challenge, peer review and publishing, and next steps. Block widths are in proportion to time, so the long improvement challenge looks long and the breaks look short. A token under each block shows what teachers leave with. Two arcs show why the order matters: the rubric comes before calibration, and checking comes before improving. The times live in the overlay data and not in the artwork, so a facilitator can adapt the agenda without redrawing.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | Check-in and setup | 8:30 to 9:00. Teachers leave with: a working agent session. |
| 2 | The ten metrics | 9:00 to 9:45. Teachers leave with: a rubric card. |
| 3 | Calibration by hand, then with the agent | 9:45 to 10:45. Teachers leave with: hand and agent scores, with gaps explained. |
| 4 | Checking the agent | 11:00 to 12:00. Teachers leave with: a verified evaluation of the sample. |
| 5 | Lunch | 12:00 to 12:45. Teachers leave with: no deliverable, just a rest. |
| 6 | The improvement challenge | 12:45 to 2:15. Teachers leave with: an improved component and its new score. |
| 7 | Peer review and publishing | 2:30 to 3:15. Teachers leave with: a published, openly licensed component. |
| 8 | Next steps | 3:15 to 3:30. Teachers leave with: a certificate checklist. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- The times are in the overlay data. Edit the descriptions in data.json to adapt the agenda for your own day.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **order** the blocks of the one-day workshop and **explain** why the rubric comes before calibration and checking comes before improving. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The sample agenda from [Chapter 19](../../chapters/19-training-certifying-reviewers/index.md) and the [Sample One-Day Schedule](../../workshops/sample-one-day-schedule.md).

### Activities

1. **Explore (4 min).** Hover over markers 1 to 8. Which block takes the longest, and what do teachers leave with from it?
2. **Quiz (3 min).** Press **Quiz** and find each block from its description.
3. **Adapt (3 min).** If your day were two hours shorter, which block would you shorten, and which two blocks must stay in order?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Which block comes right after calibration and the break? *(Checking the agent.)*
2. What do teachers leave with from the improvement challenge? *(An improved component and its new score.)*
3. Why does the rubric come before calibration? *(You score by hand against the rubric first, so there is a human score to compare the agent with.)*

### Connection to the OER Evaluator rubric

This poster pairs with the Sample One-Day Schedule workshop page and gives a facilitator the logic of the day at a glance.

## References

1. Evaluating Professional Development - Thomas R. Guskey - Corwin Press (2000) - Guskey's five levels (participants' reactions, learning, organization support, use of new knowledge, and student outcomes) test whether a workshop changed practice, not only whether people enjoyed it.
2. [Quality Matters](https://www.qualitymatters.org/) - Quality Matters - A nonprofit that trains peer reviewers and certifies courses against a published rubric. A mature model for training and certifying reviewers, like the local reviewer role in this chapter.
3. [Open Badges](https://www.1edtech.org/standards/open-badges) - 1EdTech - The standard for verifiable digital credentials that can carry evidence of what the earner did. A model for a certificate that links to a learner's reviewed work.
