---
title: "How Fast Does Content Spoil?"
description: "A three-shelf market stall that sorts six kinds of content by how quickly they go out of date, with a date stamp telling a reviewer how often to check each one."
image: /sims/content-shelf-life/content-shelf-life.png
og:image: /sims/content-shelf-life/content-shelf-life.png
twitter:image: /sims/content-shelf-life/content-shelf-life.png
social:
   cards: false
status: built
hide:
  - toc
---

# How Fast Does Content Spoil?

<iframe src="main.html" height="717px" width="100%" scrolling="no"></iframe>

[Run the How Fast Does Content Spoil? MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 5: Accuracy and Currency](../../chapters/05-accuracy-currency/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `content-shelf-life.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/content-shelf-life/main.html"
        height="717px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Currency is half of the accuracy and currency metric, and reviewers often apply one rule to every page. This poster is a market stall with three shelves, taken from the Chapter 5 table of how quickly six kinds of content go out of date. The slow shelf holds content that is checked at each major review. The middle shelf is checked every few years. The fast shelf is checked every year or more often. Every item wears a date stamp with the wording from the chapter.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Slow shelf | Slow shelf: ages very slowly to slowly. |
| Middle shelf | Middle shelf: ages moderately. |
| Fast shelf | Fast shelf: ages quickly. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The poster keeps the chapter's own wording for how often to check. It does not turn "every few years" into a number.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **match** each of six kinds of content to how fast it ages and how often a reviewer should check it. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The currency half of the accuracy and currency metric from [Chapter 5](../../chapters/05-accuracy-currency/index.md).

### Activities

1. **Explore (3 min).** Press each shelf and read its two items and their stamps.
2. **Quiz (3 min).** Press **Quiz Me** and place four kinds of content on the right shelf.
3. **Apply (4 min).** Pick a page you teach from. Which shelf does most of it sit on? When should you next check it?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Which shelf holds software screenshots? *(The fast shelf, checked every year or more often.)*
2. How often do you check standards, curricula, and guidelines? *(Every few years, and when a standard is revised.)*
3. Why not use one currency rule for every page? *(The multiplication table does not change, while a software screenshot can change within a year.)*

### Connection to the OER Evaluator rubric

Currency is half of metric 1. A quick triage by shelf tells a reviewer where to spend checking time, and supports the link rot and revision history ideas in the same chapter.

## References

1. [Link rot](https://en.wikipedia.org/wiki/Link_rot) - Wikipedia - Explains how links stop working over time, how common the problem is, and what can be done about it. Background for the currency checks that test a resource's links.
2. [Fact-checking](https://en.wikipedia.org/wiki/Fact-checking) - Wikipedia - Describes how claims are checked before and after publication and the methods professional fact-checkers use. Supports this chapter's procedure for sampling and verifying the facts in a resource.
3. [Wayback Machine](https://web.archive.org/) - Internet Archive - Lets reviewers retrieve archived copies of pages that have moved or vanished and see what a page said on an earlier date. A practical tool for the broken-link and currency checks in this chapter.
