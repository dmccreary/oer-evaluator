---
title: The Sixth R: Regenerate
description: A source-to-book picture that shows what the proposed sixth R, regenerate, adds to the 5Rs: the right to rebuild an intelligent textbook from its course description, learning graph, and agentic skills.
image: /posters/sixth-r/sixth-r.png
og:image: /posters/sixth-r/sixth-r.png
twitter:image: /posters/sixth-r/sixth-r.png
social:
   cards: false
status: built
hide:
  - toc
---

# The Sixth R: Regenerate

<iframe src="main.html" height="811px" width="100%" scrolling="no"></iframe>

[Run the Sixth R: Regenerate MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 1: Foundations of Open Educational Resources](../../chapters/01-foundations-of-oer/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `sixth-r.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/posters/sixth-r/main.html"
        height="811px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

This poster shows what the proposed sixth R adds to the 5Rs. David Wiley's five permissions describe what you may do with a finished book: retain it, reuse it, revise it, remix it, and redistribute it. An intelligent textbook is built by AI agents from a source: a course description, a learning graph, and agentic skills. A license that covers only the rendered book gives you a copy of the output but not the means to produce it. The Intelligent Textbooks site proposes regenerate as the sixth R, the right to recreate, update, or produce new versions of the textbook from that source. The picture reads left to right: the source on the left, the regenerate arrow in the middle, and the book on the right, with the five Rs listed where they act.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Course description | Course description: where the book starts. Agents build the chapters from it. |
| Learning graph | Learning graph: a map of the book's concepts and what each one depends on. |
| Agentic skills | Agentic skills: reusable, documented steps an AI agent follows to build the book. |
| Regenerate | Regenerate, the proposed sixth R: the right to recreate, update, or produce new versions of an intelligent textbook. |
| The book | The book: the rendered output that readers see and the 5Rs act on. |
| The 5Rs | The 5Rs: five permissions that an open license grants on the finished book. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- Regenerate is a proposal from the Intelligent Textbooks site. It is not part of David Wiley's 5Rs, so the poster labels it "proposed".
- The five test questions are the ones in Chapter 1. The test question for regenerate is written for this poster, in the same form.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **explain** how the proposed sixth R, regenerate, differs from the 5Rs, using the source and the book on the poster. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The 5R permissions from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).
- The meaning of an intelligent textbook and a learning graph from [Chapter 18](../../chapters/18-components-publishing-oer/index.md).

### Activities

1. **Explore (3 min).** Press each of the six zones. Which of the three source pieces would be hardest for another author to recreate, and why?
2. **Quiz (3 min).** Press **Quiz Me** and place six descriptions on the poster.
3. **Apply (4 min).** Pick an AI-built textbook you know. Can you find its course description, its learning graph, and its skills? Could you rebuild it for a different course?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. An author posts a textbook under an open license but keeps the learning graph and skills private. Which right is missing? *(Regenerate. You have a copy of the output but not the means of production.)*
2. A teacher translates one chapter of an open textbook by hand. Is that regenerate? *(No. Changing the finished book is revise. Regenerate means producing a new version from the source.)*
3. Is regenerate one of David Wiley's original 5Rs? *(No. It is a proposal on the Intelligent Textbooks site that extends the 5Rs to the source of a textbook.)*

### Connection to the OER Evaluator rubric

The rubric's open license metric asks whether the 5R permissions are granted, and its editable source metric asks whether others can change the resource. Regenerate asks a further question about AI-built books: is the source that produced the book published too? None of the ten metrics scores that today, so treat it as a question to ask during a manual review, not as a rubric score.

## References

1. [Definition of Open](https://opencontent.org/definition/) - opencontent.org - David Wiley's own statement of the 5R permissions (retain, reuse, revise, remix, redistribute) and why a license must grant all five. This is the source of the 5R framework used throughout the book.
2. [The 6th "R" of Intelligent Textbooks](https://dmccreary.github.io/intelligent-textbooks/appendices/five-rs-of-intelligent-textbooks/) - Dan McCreary, Intelligent Textbooks - Extends David Wiley's 5Rs of open content with a sixth right, regenerate, for rebuilding a textbook from its learning graph, course description, and skills. The source of the proposal this poster illustrates.
