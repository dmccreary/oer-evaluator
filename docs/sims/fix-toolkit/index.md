---
title: "The Fix Toolkit"
description: "A pegboard of thirteen tools, one for each fix in Chapter 15, hung in eight panels by the metric each mainly raises, each with a human-check badge."
image: /sims/fix-toolkit/fix-toolkit.png
og:image: /sims/fix-toolkit/fix-toolkit.png
twitter:image: /sims/fix-toolkit/fix-toolkit.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="557px" width="100%" scrolling="no"></iframe>

[Run the Fix Toolkit MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 15: Improving a Resource with AI Agents](../../chapters/15-improving-resources-with-ai/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `fix-toolkit.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/fix-toolkit/main.html"
        height="557px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Thirteen fixes in a table are hard to keep in mind, and the improvement plan starts from the lowest metric and asks which fix applies. This poster is that lookup as a pegboard. Eight panels hold the thirteen tools, one panel for each metric a fix mainly raises. Quality metrics hang in blue panels and reusability metrics in purple panels. Each marker's description gives the typical agent mistake and the human check from the chapter, and every tool carries a small person-with-check badge, because nothing is applied without human review. The artwork has no text, so every name comes from the overlay.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | AI alt text generation | Mainly raises accessibility. Typical agent mistake: generic text or invented details. The human check: look at each image beside its draft. |
| 2 | Caption generation | Mainly raises accessibility. Typical agent mistake: mis-heard technical terms. The human check: watch the video while reading the captions. |
| 3 | Heading repair | Mainly raises accessibility. Typical agent mistake: renamed or merged sections. The human check: compare the outline before and after. |
| 4 | Reading level rewrite | Mainly raises readability. Typical agent mistake: lost precision or meaning. The human check: run the readability tool and the meaning checks. |
| 5 | Glossary generation | Mainly raises readability. Typical agent mistake: a definition that differs from the resource's use. The human check: compare with the resource and a trusted source. |
| 6 | Link repair | Mainly raises accuracy and currency. Typical agent mistake: an invented address. The human check: open every new link. |
| 7 | Content update | Mainly raises accuracy and currency. Typical agent mistake: a figure from memory. The human check: open the source and confirm the figure. |
| 8 | Metadata generation | Mainly raises metadata. Typical agent mistake: a guessed author or license. The human check: verify each field against the page. |
| 9 | License statement repair | Mainly raises open license. Typical agent mistake: a license assigned to someone else's work. The human check: find the owner's terms or replace the item. |
| 10 | Chapter splitting | Mainly raises modularity. Typical agent mistake: a module that still depends on another. The human check: open each module alone. |
| 11 | PDF-to-Markdown conversion | Mainly raises editable source. Typical agent mistake: lost tables, headings, or pictures. The human check: compare the output with the pdf. |
| 12 | Practice question generation | Mainly raises practice with feedback. Typical agent mistake: a wrong key or a leading stem. The human check: answer each question without the key. |
| 13 | MicroSim building | Mainly raises practice with feedback. Typical agent mistake: wrong science or a failed embed. The human check: use every control and embed it on each platform. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- Thirteen markers are near the readable limit, so some leader lines cross the board. Use the labels in the side panels to follow them.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **match** each of the thirteen fixes to the metric it mainly raises, and **state** the human check for one of them. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The ten metrics from [Chapter 3](../../chapters/03-ten-metric-rubric-scoring/index.md) and the improvement plan from [Chapter 15](../../chapters/15-improving-resources-with-ai/index.md).

### Activities

1. **Explore (4 min).** Hover over the markers 1 to 13. Which panel holds the most tools?
2. **Quiz (3 min).** Press **Quiz** and find each tool from its description.
3. **Plan (3 min).** Take the lowest metric of a resource you have scored. Which tool on the pegboard would you reach for, and what is its human check?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Which metric does PDF-to-Markdown conversion mainly raise? *(Editable source.)*
2. What is the human check for link repair? *(Open every new link.)*
3. What is the typical agent mistake in metadata generation? *(A guessed author or license.)*

### Connection to the OER Evaluator rubric

The improvement plan starts from the lowest metric and asks which fix applies. The poster is that lookup, and every tool carries the reminder that nothing is applied without human review.

## References

1. [Derivative work](https://en.wikipedia.org/wiki/Derivative_work) - Wikipedia - Explains how a work based on another is treated in copyright law. Background for the chapter's check of what a license allows before an agent changes a resource.
2. [Alt Decision Tree](https://www.w3.org/WAI/tutorials/images/decision-tree/) - W3C Web Accessibility Initiative - A decision tree for choosing the right alt attribute for each kind of image. Lets a reviewer judge whether an agent's alt text suits the image's purpose.
3. [Marking Your Work with a CC License](https://wiki.creativecommons.org/wiki/Marking_your_work_with_a_CC_license) - CC Public Wiki - Shows how to place a license notice on a work. This is the step needed when a revised version is published.
4. [Pull Requests](https://docs.github.com/en/pull-requests/reference/pull-requests) - GitHub Docs - GitHub's documentation on proposing, reviewing, and merging changes. The standard way to let a person inspect every change an agent made before accepting it.
