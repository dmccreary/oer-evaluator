---
title: "Following a Claim Back to Its Source"
description: "A chain of four links that follows the claim \"Wetlands filter pollutants\" from a footnote to a textbook, a review article, and the study where the measurement was made."
image: /sims/claim-source-chain/claim-source-chain.png
og:image: /sims/claim-source-chain/claim-source-chain.png
twitter:image: /sims/claim-source-chain/claim-source-chain.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="670px" width="100%" scrolling="no"></iframe>

[Run the Following a Claim Back to Its Source MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 5: Accuracy and Currency](../../chapters/05-accuracy-currency/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `claim-source-chain.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/claim-source-chain/main.html"
        height="670px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Confirming that a citation exists is not the same as tracing the claim. This poster shows the worked example from Chapter 5. The claim "Wetlands filter pollutants" appears in a resource's footnote 4, which cites a textbook, which cites a review article, which summarizes several studies. One of those studies reports measurements of pollutant levels before and after water passed through a wetland. The first three links are other people's summaries. The fourth is where the measurement was made. A red flag at the second link marks the early stop that the poster exists to prevent. The sources are invented for the chapter and are illustrative, so there is nothing to look up.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | Footnote 4 of the resource | The claim "Wetlands filter pollutants" appears in the resource. Footnote 4 cites a textbook. This link is someone's summary and is not the original. |
| 2 | The textbook | The textbook says wetlands filter pollutants and cites a review. A reviewer who stops here, at the red flag, has found only that a textbook agrees with the resource. |
| 3 | The review article | The review article summarizes several studies of wetland filtering. It is another summary, so it is not the original either. |
| 4 | The original study | One of those studies reports measurements of pollutant levels before and after water passed through a wetland. This is the original, and the claim is supported by it. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- The chapter's sources are invented for illustration. The poster prints no journal names or citations.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **trace** a claim through a chain of citations to its original source and **explain** why stopping at the first link is not enough. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Primary and secondary sources from [Chapter 5](../../chapters/05-accuracy-currency/index.md).

### Activities

1. **Explore (3 min).** Hover over markers 1 to 4. Which links are other people's summaries?
2. **Quiz (3 min).** Press **Quiz** and find each link from its description.
3. **Trace (4 min).** Pick a claim from a resource you use. How many links can you follow before you reach a primary source?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. A reviewer stops at link 2. What has the reviewer found? *(Only that a textbook agrees with the resource.)*
2. Which link is the original source? *(Link 4, the study that reports the measurements.)*
3. The further back you trace a claim, what happens to the check? *(You can trust the check more.)*

### Connection to the OER Evaluator rubric

Chapter 14 warns about invented citations. A reader needs to see that confirming a citation exists is not the same as tracing the claim.

## References

1. [Fact-checking](https://en.wikipedia.org/wiki/Fact-checking) - Wikipedia - Describes how claims are checked before and after publication and the methods professional fact-checkers use. Supports this chapter's procedure for sampling and verifying the facts in a resource.
2. [SIFT (The Four Moves)](https://hapgood.us/2019/06/19/sift-the-four-moves/) - Hapgood - Mike Caulfield's own post explaining Stop, Investigate the source, Find better coverage, and Trace claims. A short, usable routine for tracing a citation back to its origin.
3. [Evaluating Sources of Information](https://owl.purdue.edu/owl/research_and_citation/conducting_research/evaluating_sources_of_information/index.html) - Purdue OWL - Explains how to judge a source's author, publisher, date, and evidence. A plain companion for deciding whether a resource's citations are reliable and recent enough.
