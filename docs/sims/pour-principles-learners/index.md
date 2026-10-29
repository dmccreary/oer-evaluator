---
title: "Four Principles, Five Learners"
description: "Four zones for the WCAG principles Perceivable, Operable, Understandable, and Robust, each pairing an example criterion with the learners it protects."
image: /sims/pour-principles-learners/pour-principles-learners.png
og:image: /sims/pour-principles-learners/pour-principles-learners.png
twitter:image: /sims/pour-principles-learners/pour-principles-learners.png
social:
   cards: false
status: built
hide:
  - toc
---

# Four Principles, Five Learners

<iframe src="main.html" height="789px" width="100%" scrolling="no"></iframe>

[Run the Four Principles, Five Learners MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 7: Accessibility](../../chapters/07-accessibility/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `pour-principles-learners.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/pour-principles-learners/main.html"
        height="789px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Accessibility is full of standards language, and teachers need the human reason first. This poster joins two tables from Chapter 7: the four WCAG principles with an example criterion each, and five learners with the feature that lets each one use a resource. Perceivable covers the blind learner, the deaf learner, and the learner with low vision. Operable covers the learner who cannot use a mouse. Understandable covers the learner with a reading disability. Robust covers assistive technology. Some features serve more than one principle, so the pairing is an editorial choice for teaching.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Perceivable (P) | Perceivable: Can users perceive the content? |
| Operable (O) | Operable: Can users operate the controls? |
| Understandable (U) | Understandable: Can users follow it? |
| Robust (R) | Robust: Does it work with assistive technology? |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The learner pairing is an editorial choice. Some features serve more than one principle, and the author confirms the mapping.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **match** each learner support to the WCAG principle it serves, and **state** one example criterion for each principle. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The accessibility metric from [Chapter 7](../../chapters/07-accessibility/index.md).

### Activities

1. **Explore (3 min).** Press each letter. Which learners does it protect, and what gets in their way?
2. **Quiz (3 min).** Press **Quiz Me** and place five learner supports under the right principle.
3. **Check (4 min).** Open a page you teach from. Pick one support from each zone and test whether the page offers it.

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Which principle do captions for a deaf learner belong to? *(Perceivable.)*
2. Which principle asks that all functions work with a keyboard? *(Operable.)*
3. What does Robust ask about a custom control? *(That it exposes a name and role to assistive technology.)*

### Connection to the OER Evaluator rubric

Accessibility is metric 4 in the ten-metric rubric. The rubric starts from the people, so a reviewer knows why each criterion matters.

## References

1. [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) - Wikipedia - Explains the WCAG versions, their four principles, and the A, AA, and AAA conformance levels. The standard behind this book's accessibility metric, which targets WCAG 2.1 AA.
2. [WCAG 2 Overview](https://www.w3.org/WAI/standards-guidelines/wcag/) - W3C Web Accessibility Initiative - The W3C's overview of the Web Content Accessibility Guidelines covering versions 2.0, 2.1, and 2.2, with links to the full standard and quick references. The official starting point for the accessibility metric.
3. [Alternative Text](https://webaim.org/techniques/alttext/) - WebAIM - Explains when and how to write alt text for informative, decorative, functional, and complex images, with examples. Directly supports the chapter's section on images.
4. [Keyboard Accessibility](https://webaim.org/techniques/keyboard/) - WebAIM - Explains how people use a page without a mouse, including tab order, visible focus, and skip links. Gives a simple procedure for the chapter's keyboard test.
