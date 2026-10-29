---
title: "Component in a Box"
description: "An exploded view of a cardboard box holding the six parts of the Chapter 18 quiz package, with a broken link outside the box and three finished boxes for Watershed Basics v1.1."
image: /sims/component-in-a-box/component-in-a-box.png
og:image: /sims/component-in-a-box/component-in-a-box.png
twitter:image: /sims/component-in-a-box/component-in-a-box.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="552px" width="100%" scrolling="no"></iframe>

[Run the Component in a Box MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 18: Reusable Components and Publishing OER](../../chapters/18-components-publishing-oer/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `component-in-a-box.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/component-in-a-box/main.html"
        height="552px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Chapter 18 turns improved resources into reusable components, and packaging is the concrete step that makes the lift-out test from Chapter 9 and the portability checks from Chapter 10 pass. This poster is an exploded view of the quiz package watershed-quiz. Six parts float above the box: the page itself (index.html), the script it needs kept inside the folder (quiz.js), a README that says what the component is and how to use it, a license file, a metadata file, and an image folder. Everything the component needs travels with it. Outside the box a dotted line runs from the page to a folder elsewhere, with a cross on it: the broken link that packaging prevents. The seventh marker sits on the three finished boxes of Watershed Basics v1.1, the reading, the quiz, and the simulation. The artwork has no text, and the file names come from the overlay.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | index.html | The quiz page itself. A reuser opens this file to see and use the component. All links in it must be complete addresses or point to files inside the folder. |
| 2 | quiz.js | The script the page needs, kept inside the folder. If it lived in a sibling folder, it would not travel with the component. |
| 3 | README.md | What the component is, how to embed it, and how to credit it. |
| 4 | LICENSE.txt | The license text or a link to it, so a reuser knows what they may do. |
| 5 | metadata.json | The metadata record of Chapter 9 in a form a program can read, so a catalog can find and describe the component. |
| 6 | img/ | The images the component uses, kept inside the package with complete addresses or paths inside the folder. |
| 7 | Three finished boxes for Watershed Basics v1.1 | After splitting, Watershed Basics v1.1 has three components: the reading, the quiz, and the simulation. Each is packaged in its own box with its own license and metadata. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- This book's own MicroSim folders follow the same idea: each has a main.html, an index.md, and its own script, but they also load the shared overlay libraries from docs/sims/shared-libs.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **list** the files in a packaged component, **say** what each is for, and **explain** why a link that leaves the folder breaks the package. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Standalone components from [Chapter 9](../../chapters/09-modularity-metadata/index.md) and packaging from [Chapter 18](../../chapters/18-components-publishing-oer/index.md).

### Activities

1. **Explore (4 min).** Hover over markers 1 to 7. Which part would stop a reuser from knowing what they may do if it were missing?
2. **Quiz (3 min).** Press **Quiz** and find each part from its description.
3. **Inspect (3 min).** Open a folder of yours. Which of the six parts are missing, and where do its links point?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Where must the script a page needs be kept? *(Inside the folder, so it travels with the component.)*
2. Why does the box include a license file and a metadata file? *(So a reuser knows what they may do and a catalog can find and describe it.)*
3. What should links inside a package be? *(Complete addresses, or point to files inside the package.)*

### Connection to the OER Evaluator rubric

Packaging ties together license, metadata, and portability. A component with every part passes the lift-out test and embeds without edits.

## References

1. [Material for MkDocs: Getting Started](https://squidfunk.github.io/mkdocs-material/getting-started/) - Material for MkDocs - Official instructions for installing and configuring the Material theme used by this book. Supports the chapter's steps for building a textbook site.
2. [Creating a GitHub Pages Site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) - GitHub Docs - Step-by-step instructions for publishing a site from a repository for free. Supports the chapter's walkthrough of publishing an improved OER.
3. [Semantic Versioning 2.0.0](https://semver.org/) - semver.org - A simple scheme for numbering releases so users can tell a small fix from a breaking change. Useful for keeping a component library's versions clear.
4. [Zenodo](https://zenodo.org/) - CERN - An open repository that gives uploaded files a DOI and reports views and downloads. One way to publish an OER permanently and begin tracking its reuse.
