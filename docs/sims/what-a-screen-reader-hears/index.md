---
title: "What a Screen Reader Hears"
description: "A page on the left and speech bubbles on the right show what a screen reader announces for a heading, an image with good alt text, an image with no alt attribute, and an image with an empty alt attribute."
image: /sims/what-a-screen-reader-hears/what-a-screen-reader-hears.png
og:image: /sims/what-a-screen-reader-hears/what-a-screen-reader-hears.png
twitter:image: /sims/what-a-screen-reader-hears/what-a-screen-reader-hears.png
social:
   cards: false
status: built
hide:
  - toc
---

# What a Screen Reader Hears

<iframe src="main.html" height="789px" width="100%" scrolling="no"></iframe>

[Run the What a Screen Reader Hears MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 7: Accessibility](../../chapters/07-accessibility/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `what-a-screen-reader-hears.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/what-a-screen-reader-hears/main.html"
        height="789px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Hearing the result is more persuasive than reading a rule. This poster shows four rows from the Chapter 7 worked example. On the left is what a sighted reader sees. On the right is what a screen reader typically announces. The same photograph appears in every image row, so the only difference is the markup. A real heading is announced with its level. Good alt text is read as the image's description. No alt attribute makes the reader announce the file name, which is useless. An empty alt attribute is announced as nothing, which is correct only for a decorative image. Wording varies between screen reader programs, and the poster shows no real program.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| What is seen | Four rows a sighted reader sees: a heading and the same photograph with three kinds of alt markup. |
| What is heard | What a screen reader typically announces for each of the four rows. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- Announcement wording varies between screen reader programs. The poster shows typical announcements and no real program.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **predict** what a screen reader announces for a heading and for images with good, missing, and empty alt text. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Alt text, decorative images, and heading structure from [Chapter 7](../../chapters/07-accessibility/index.md).

### Activities

1. **Explore (3 min).** Press the seen column, then the heard column. Which row would frustrate a blind learner most?
2. **Quiz (3 min).** Press **Quiz Me** and answer which zone shows what is seen and what is heard.
3. **Listen (4 min).** Turn on a screen reader on your computer for five minutes and visit a page you teach from. Which row from this poster did you meet?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. What does a screen reader say for an image with no alt attribute? *(Often the file name, such as "Image, river.png", which is useless.)*
2. When is an empty alt attribute correct? *(Only for a decorative image.)*
3. How does a screen reader announce a real heading? *(With its level, such as "Heading level 2, How water moves".)*

### Connection to the OER Evaluator rubric

Five minutes with a screen reader changes how you write alt text. This poster gives a taste of that without any software, and supports the accessibility metric.

## References

1. [Screen reader](https://en.wikipedia.org/wiki/Screen_reader) - Wikipedia - Describes how screen readers turn on-screen content into speech or braille and what they need from a page's structure. Helps reviewers understand why headings and alt text are scored.
2. [Alternative Text](https://webaim.org/techniques/alttext/) - WebAIM - Explains when and how to write alt text for informative, decorative, functional, and complex images, with examples. Directly supports the chapter's section on images.
3. [WAVE Web Accessibility Evaluation Tools](https://wave.webaim.org/) - WebAIM - A free tool that marks errors and alerts directly on a web page. Shows which accessibility problems automated checks can find and which still need a human reviewer.
