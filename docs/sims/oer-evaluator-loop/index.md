---
title: "The OER Evaluator Loop"
description: "A closed loop with eight numbered stations that shows how the chapters fit together, and why test results are used to calibrate the AI agent."
image: /sims/oer-evaluator-loop/oer-evaluator-loop.png
og:image: /sims/oer-evaluator-loop/oer-evaluator-loop.png
twitter:image: /sims/oer-evaluator-loop/oer-evaluator-loop.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="575px" width="100%" scrolling="no"></iframe>

[Run the OER Evaluator Loop MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapters](../../chapters/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `oer-evaluator-loop.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/oer-evaluator-loop/main.html"
        height="575px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

This poster is a map of the whole book. Eight stations sit on one closed loop. A reader first learns what OER and licenses are, scores a resource by hand with the ten-metric rubric, directs an AI agent to make a first pass, and checks the agent's evidence. The reader then improves the lowest metrics with agents, tests the change with students, calibrates the agent against the test results, and publishes and trains others. The thick arrow that returns from calibration to the agent's first pass is the one that matters: it is how automated scores earn trust.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | Understand OER and licenses | Learn what makes a resource open and how the six Creative Commons licenses work. Chapters 1 and 2. |
| 2 | Score a resource by hand with the ten-metric rubric | Score ten metrics, five for quality and five for reusability, and add them up to a total out of 100. Chapters 3 to 11. |
| 3 | Direct an AI agent to make a first pass | Write a rubric prompt, run the agent, and collect its scores with evidence. Chapters 12 and 13. |
| 4 | Check the agent's evidence | Open each quoted source and recompute each score. Look for factual, license, citation, and scoring errors. Chapter 14. |
| 5 | Improve the lowest metrics with agents | Fix the lowest-scoring metric first, using agents for alt text, readability, metadata, and more, with a human check on every change. Chapter 15. |
| 6 | Test the change with students in an A/B test | Randomly assign students to the original or the improved version, and compare learning gain. Chapters 16 and 17. |
| 7 | Calibrate the agent against the test results | Compare the agent's scores with what the students actually learned, then adjust the prompt. Chapters 14 and 17. |
| 8 | Publish and train others | Package improved components with a license and metadata, publish them openly, and train other teachers. Chapters 18 and 19. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- Chapter numbers come from the chapter list. If chapters move, update the marker descriptions in `data.json`.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **describe** the eight stations of the OER Evaluator loop in order and **explain** why test results are used to calibrate the AI agent. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- None. This poster is the overview, so it works before or after any chapter.

### Activities

1. **Explore (3 min).** Hover over each marker in order, 1 to 8. Which station would your team start at?
2. **Quiz (3 min).** Press **Quiz** and find each station from its description.
3. **Discuss (4 min).** Marker 7 returns to marker 3. In your own words, what changes in the agent's next pass after calibration?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Which station comes right after "check the agent"? *(Improve the lowest metrics with agents (Chapter 15).)*
2. What does the return arrow from station 7 to station 3 mean? *(Test results calibrate the agent, so its next first pass can be trusted more.)*
3. Which chapters teach scoring by hand? *(Chapters 3 to 11.)*

### Connection to the OER Evaluator rubric

The course description lays out a path from evaluation to improvement to testing, with test results used to check and calibrate the automated scores. This poster is that path in one picture.

## References

1. [Open educational resources](https://en.wikipedia.org/wiki/Open_educational_resources). Wikipedia. Background for station 1.
2. [Rubric (academic)](https://en.wikipedia.org/wiki/Rubric_(academic)). Wikipedia. Background for station 2.
3. [Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)). Wikipedia. Why station 4 checks the agent's evidence.
4. [A/B testing](https://en.wikipedia.org/wiki/A/B_testing). Wikipedia. Background for station 6.
5. [Calibration (statistics)](https://en.wikipedia.org/wiki/Calibration_(statistics)). Wikipedia. Background for station 7.
