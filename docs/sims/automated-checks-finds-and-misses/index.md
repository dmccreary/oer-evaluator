---
title: "What Each Automated Check Can and Cannot Find"
description: "Four automated tools, each split into what it finds and what it cannot find, with a reminder to keep a human in the loop."
image: /sims/automated-checks-finds-and-misses/automated-checks-finds-and-misses.png
og:image: /sims/automated-checks-finds-and-misses/automated-checks-finds-and-misses.png
twitter:image: /sims/automated-checks-finds-and-misses/automated-checks-finds-and-misses.png
social:
   cards: false
status: built
hide:
  - toc
---

# What Each Automated Check Can and Cannot Find

<iframe src="main.html" height="789px" width="100%" scrolling="no"></iframe>

[Run the What Each Automated Check Can and Cannot Find MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 13: Automated Checks, Cost, and Student Privacy](../../chapters/13-automated-checks-cost-privacy/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `automated-checks-finds-and-misses.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/automated-checks-finds-and-misses/main.html"
        height="789px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Teachers over-trust a clean scan, and "the scan passed" does not mean "the resource is accessible". This poster pairs what each tool finds with what it misses, taken from the Chapter 13 table. Every tool is drawn with a beam of light that lights some items and leaves others dark. The "cannot find" half has the same visual weight as the "finds" half, shaded and dotted. A footer reminds the reader to keep a human in the loop.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Link checker | Finds: links that return errors; links that have moved. Cannot find: a working link that leads to the wrong content. |
| Accessibility scan | Finds: missing alt attributes; weak contrast; missing labels. Cannot find: whether alt text is useful; whether captions are accurate. |
| License detection | Finds: missing license statements; mismatched license statements; unrecognized license statements. Cannot find: whether the license claim is true. |
| Readability scan | Finds: a reading level for each passage. Cannot find: undefined terms; dense ideas; audience fit. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The poster keeps the chapter's wording and shows only the checks the book already uses.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **state** what each of four automated checks can find and what it cannot, and **explain** why a clean scan is not a finished review. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Automated checks and the human in the loop from [Chapter 13](../../chapters/13-automated-checks-cost-privacy/index.md).

### Activities

1. **Explore (3 min).** Press each tool. What is the one thing it cannot find?
2. **Quiz (3 min).** Press **Quiz Me** and match four findings to the tools.
3. **Plan (4 min).** For a resource of yours, list one check you would automate and the human check that must follow it.

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. A link checker reports no broken links. What can it not tell you? *(Whether a working link leads to the wrong content.)*
2. Can an accessibility scan tell you whether alt text is useful? *(No. It finds missing alt attributes, not whether the text is useful.)*
3. What can a readability scan not find? *(Undefined terms, dense ideas, and audience fit.)*

### Connection to the OER Evaluator rubric

Pairing what each tool finds with what it misses motivates the human check that Chapter 14 formalizes.

## References

1. [Human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop) - Wikipedia - Describes systems in which a person reviews or corrects an automated process. Background for the chapter's rule that a human checks the agent's evidence before any score is accepted.
2. [Web Accessibility Evaluation Tools List](https://www.w3.org/WAI/test-evaluate/tools/list/) - W3C Web Accessibility Initiative - A filterable directory of accessibility checkers by purpose, platform, price, and standard. Helps readers choose the automated accessibility checks this chapter recommends.
3. [Family Educational Rights and Privacy Act (FERPA)](https://studentprivacy.ed.gov/ferpa) - U.S. Department of Education - The Student Privacy Policy Office's official FERPA page, with guidance for schools and teachers on education records and disclosure. The primary source for the chapter's privacy rules.
