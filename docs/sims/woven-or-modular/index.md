---
title: "Woven or Modular? The Lift-Out Test"
description: "A woven cloth beside three separate building blocks shows why a quiz that is woven into one page cannot be lifted out, while a modular one can."
image: /sims/woven-or-modular/woven-or-modular.png
og:image: /sims/woven-or-modular/woven-or-modular.png
twitter:image: /sims/woven-or-modular/woven-or-modular.png
social:
   cards: false
status: built
hide:
  - toc
---

# Woven or Modular? The Lift-Out Test

<iframe src="main.html" height="811px" width="100%" scrolling="no"></iframe>

[Run the Woven or Modular? The Lift-Out Test MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 9: Modularity and Metadata](../../chapters/09-modularity-metadata/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `woven-or-modular.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/woven-or-modular/main.html"
        height="811px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Modularity is the seventh metric, and the lift-out test is the practical way to score it. This poster shows the same three pieces, a reading, a quiz, and a simulation, built two ways. On the left they are threads of one cloth, so pulling out the quiz unravels the rest. On the right they are separate blocks, each in its own folder, and the quiz lifts away cleanly. Four rows come from the chapter's table, and a strip along the bottom shows that modularity is a matter of degree.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Woven design | One long page where explanation, quiz, and simulation are threads of one cloth. |
| Modular design | A reading, a quiz, and a simulation as separate pieces, each in its own folder. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The same three pieces use the same three colors on both sides, so the eye sees that only the construction differs.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **apply** the lift-out test to decide whether a resource is woven or modular, and **place** it on the degrees of modularity. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The modularity metric and the standalone component from [Chapter 9](../../chapters/09-modularity-metadata/index.md).

### Activities

1. **Explore (3 min).** Press each side and read its four rows. What changes about reuse?
2. **Quiz (3 min).** Press **Quiz Me** and decide which design each statement describes.
3. **Apply (4 min).** Pick one resource of yours. Copy one component into an empty file and read it cold. Does it still make sense?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. A quiz refers to "the diagram above". Does it pass the lift-out test? *(No. A component that depends on its surroundings is not standalone.)*
2. How does another teacher reuse a woven page? *(Take everything or nothing.)*
3. What is the far end of the degrees of modularity? *(Each part packaged with its own license and metadata.)*

### Connection to the OER Evaluator rubric

Modularity is metric 7 in the ten-metric rubric. It prepares Chapter 18, where components are packaged with a license and metadata.

## References

1. [Learning object](https://en.wikipedia.org/wiki/Learning_object) - Wikipedia - Explains the learning object idea of small, self-contained, reusable units of instruction and the standards built around it. Supports the chapter's modularity metric.
2. [Dublin Core](https://en.wikipedia.org/wiki/Dublin_Core) - Wikipedia - Describes the fifteen-element Dublin Core metadata set, its history, and its use in libraries and repositories. The basis of the metadata record taught in this chapter.
3. [Metadata](https://en.wikipedia.org/wiki/Metadata) - Wikipedia - Surveys kinds of metadata, standards, and uses, from library catalogs to web pages. Background for scoring whether a resource carries complete, useful metadata.
