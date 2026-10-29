---
title: "Source Files and Delivery Files"
description: "Three zones sort common file formats into good source, usually acceptable, and poor source, with two badges that separate \"is the format open?\" from \"is it a good source for editing?\"."
image: /sims/source-and-delivery-files/source-and-delivery-files.png
og:image: /sims/source-and-delivery-files/source-and-delivery-files.png
twitter:image: /sims/source-and-delivery-files/source-and-delivery-files.png
social:
   cards: false
status: built
hide:
  - toc
---

# Source Files and Delivery Files

<iframe src="main.html" height="789px" width="100%" scrolling="no"></iframe>

[Run the Source Files and Delivery Files MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 4: Open File Formats and Version Control](../../chapters/04-open-formats-version-control/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `source-and-delivery-files.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/source-and-delivery-files/main.html"
        height="789px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Editable source is a reusability metric, and the most common failure is a resource distributed only as a PDF. This poster sorts the formats from Chapter 4 into three zones. Every file is a document tile with its extension printed large and two badges: a round badge for "is the format open?" and a square badge for "is it a good source for editing?". The PDF is the instructive tile. Its format is open, and it is still a poor source because it is built for reading.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Good source | Five formats that are open and good sources for editing. |
| Usually acceptable | The Word document is a published standard, but fidelity depends on software. |
| Poor source | A PDF is open but built for reading; a design-program file is closed. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The page layout or design-program file is drawn as a generic tile with no program name or logo.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **explain** why an open file format is not always a good source for editing, using the PDF as the example. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The editable source metric from [Chapter 4](../../chapters/04-open-formats-version-control/index.md).

### Activities

1. **Explore (3 min).** Press each zone. Which tile has a round check badge and a square cross badge?
2. **Quiz (3 min).** Press **Quiz Me** and place four formats.
3. **Apply (4 min).** List the files you hand out to colleagues. Which zone does each belong in? What would you add so that others can edit them?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Is a PDF an open format? Is it a good source? *(Open, yes. Good source, no, because it is built for reading.)*
2. Why is a Word document only usually acceptable? *(It is a published standard, but full fidelity depends on particular software.)*
3. Which formats are good sources for data and for diagrams? *(CSV for data and SVG for diagrams.)*

### Connection to the OER Evaluator rubric

Editable source is metric 9 in the ten-metric rubric. A resource that ships only a PDF loses points here even if its license is fully open.

## References

1. [Open file format](https://en.wikipedia.org/wiki/Open_format) - Wikipedia - Defines file formats whose specifications are published so anyone can implement them without fees, with examples. Background for deciding whether a resource's source files count as open and editable.
2. [Markdown](https://en.wikipedia.org/wiki/Markdown) - Wikipedia - Describes the lightweight plain-text syntax, its history, and variants such as CommonMark. Shows why Markdown is this book's recommended editable source format for text.
3. [Markdown Guide: Basic Syntax](https://www.markdownguide.org/basic-syntax/) - Markdown Guide - A clear reference for headings, emphasis, lists, links, and images in Markdown, with side-by-side examples. Enough to read and edit the Markdown source of an OER and to try the chapter's exercises.
4. [Basic HTML Syntax](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax) - MDN Web Docs - Introduces elements, tags, and attributes in HTML. Helps teachers recognize HTML as an open, editable source format and read the pages they will adapt.
