---
title: "You Can't Reuse What You Can't Find"
description: "A mock search for \"watershed grade 6 reading open license\" shows three resource records: one found and clear, one not found, and one found but unclear."
image: /sims/cant-reuse-what-you-cant-find/cant-reuse-what-you-cant-find.png
og:image: /sims/cant-reuse-what-you-cant-find/cant-reuse-what-you-cant-find.png
twitter:image: /sims/cant-reuse-what-you-cant-find/cant-reuse-what-you-cant-find.png
social:
   cards: false
status: built
hide:
  - toc
---

# You Can't Reuse What You Can't Find

<iframe src="main.html" height="741px" width="100%" scrolling="no"></iframe>

[Run the You Can't Reuse What You Can't Find MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 9: Modularity and Metadata](../../chapters/09-modularity-metadata/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `cant-reuse-what-you-cant-find.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/cant-reuse-what-you-cant-find/main.html"
        height="741px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

The principle behind the metadata metric is that you cannot reuse what you cannot find. This poster is a mock search results page for the query from Chapter 9, "watershed grade 6 reading open license", with the chapter's three records as result cards. Resource A has a full record and ranks high. Resource B has only the title "Reading 4", and the search cannot find it. Resource C has a title and an author but no subject, grade, or license, so it may be found, yet the teacher cannot tell the grade or whether she may reuse it. Empty fields show as dashed placeholders. The search page is generic and is not any real search engine.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Resource A: found, ranks high | Yes, and it ranks high. |
| Resource B: not found | No: no field mentions a watershed. |
| Resource C: found, but unclear | Possibly, but the teacher cannot tell the grade or whether she may reuse it. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The three records come from the Chapter 9 worked example and are illustrative.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **explain** why a record with missing metadata is found, not found, or found but unclear for the same search. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The six core metadata fields from [Chapter 9](../../chapters/09-modularity-metadata/index.md).

### Activities

1. **Explore (3 min).** Press each card and read which fields are filled. What does the teacher still not know about card C?
2. **Quiz (3 min).** Press **Quiz Me** and match three outcomes to the three cards.
3. **Fix (4 min).** Choose one resource of yours and fill in all six fields. How long did it take?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Why is resource B not found by the search? *(No field mentions a watershed.)*
2. Why is resource C found but unclear? *(It has no subject, grade level, or license, so the teacher cannot tell the grade or whether she may reuse it.)*
3. Which six fields make up a core record? *(Title, author, subject, grade level, license, and description.)*

### Connection to the OER Evaluator rubric

Metadata is metric 8. It is also the cheapest fix in Chapter 15, where adding the missing fields takes half an hour in the chapter's example.

## References

1. [Dublin Core](https://en.wikipedia.org/wiki/Dublin_Core) - Wikipedia - Describes the fifteen-element Dublin Core metadata set, its history, and its use in libraries and repositories. The basis of the metadata record taught in this chapter.
2. [Metadata](https://en.wikipedia.org/wiki/Metadata) - Wikipedia - Surveys kinds of metadata, standards, and uses, from library catalogs to web pages. Background for scoring whether a resource carries complete, useful metadata.
3. [Metadata Basics](https://www.dublincore.org/resources/metadata-basics/) - Dublin Core Metadata Initiative - The DCMI introduction to metadata and the Dublin Core style, listing the fifteen core elements such as title, creator, subject, and description. The primary reference for the chapter's core fields.
4. [Learning Resource Metadata Initiative (LRMI)](https://www.dublincore.org/specifications/lrmi/) - Dublin Core Metadata Initiative - Describes the vocabulary, maintained by DCMI, that adds educational properties such as alignment to standards and typical age range to resource descriptions. Supports scoring education-specific metadata.
