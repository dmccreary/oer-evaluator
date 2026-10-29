---
title: "Link, Embed, Import, or LTI: Four Ways Into an LMS"
description: "The same resource moving four ways toward the same generic learning management system: a link, an embed, a Common Cartridge import, and an LTI tool."
image: /sims/four-ways-into-an-lms/four-ways-into-an-lms.png
og:image: /sims/four-ways-into-an-lms/four-ways-into-an-lms.png
twitter:image: /sims/four-ways-into-an-lms/four-ways-into-an-lms.png
social:
   cards: false
status: built
hide:
  - toc
---

# Link, Embed, Import, or LTI: Four Ways Into an LMS

<iframe src="main.html" height="765px" width="100%" scrolling="no"></iframe>

[Run the Link, Embed, Import, or LTI: Four Ways Into an LMS MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 10: Portability and Reuse Across Platforms](../../chapters/10-portability-reuse/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `four-ways-into-an-lms.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/four-ways-into-an-lms/main.html"
        height="765px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Teachers constantly ask how to put a resource into their course, and the wrong method means a broken embed or a gradebook that never updates. This poster shows the same resource and the same generic learning management system (LMS) in four zones. A link opens the resource at its own address. An embed shows it inside your course page. A Common Cartridge import brings a single compressed file with a manifest into the LMS. An LTI tool opens inside the course but runs on another company's server and can send a score back to the gradebook. The arrows show the difference: one-way for the first three, two-way for LTI. The LTI zone carries a small shield because passing learner information raises the privacy questions of Chapter 13. A footer names the barrier that stops all four, platform lock-in.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Link | Students open the resource at its own address. |
| Embed | The resource appears on your course page through a frame. |
| Common Cartridge import | A whole unit is copied into the LMS as a package. |
| LTI tool | An external tool opens inside the LMS and can send results back. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The poster draws a generic LMS and no vendor logos. 1EdTech is named as the standards group.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **choose** the right way to bring a resource into an LMS for each of four teacher needs. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- LMS import, Common Cartridge, and LTI from [Chapter 10](../../chapters/10-portability-reuse/index.md).

### Activities

1. **Explore (3 min).** Press each zone. Which arrows are one-way, and which is two-way?
2. **Quiz (3 min).** Press **Quiz Me** and match four teacher needs to the zones.
3. **Plan (4 min).** Think of a resource you use. Which method would you choose, and what would you test in a real LMS first?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. You want an external quiz tool to send each student's score to the gradebook. Which method? *(An LTI tool.)*
2. You want a simulation to appear on your course page. Which method? *(Embed.)*
3. You want colleagues with a different LMS to receive the same unit. Which method? *(Common Cartridge import.)*

### Connection to the OER Evaluator rubric

Portability is metric 10. The chapter's own objective is to choose among exactly these four methods for a given need.

## References

1. [Learning management system](https://en.wikipedia.org/wiki/Learning_management_system) - Wikipedia - Describes what learning management systems do, the major products, and how course content is delivered through them. Background for testing whether a resource can be imported into an LMS.
2. [Common Cartridge](https://www.1edtech.org/standards/cc) - 1EdTech - The official page for Common Cartridge, the open package format that lets learning management systems import and exchange course content. The standard behind the chapter's LMS import test.
3. [Learning Tools Interoperability (LTI)](https://www.1edtech.org/standards/lti) - 1EdTech - The official page for the LTI standard, which connects external tools to learning platforms. Useful for understanding how an interactive resource can be launched from many systems.
4. [<iframe>: The Inline Frame Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe) - MDN Web Docs - Reference for the HTML element that embeds one page inside another, including attributes and security notes. Directly supports the chapter's iframe embedding test.
