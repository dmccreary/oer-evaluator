---
title: "Open File Formats and Version Control"
description: "Covers the editable source metric: open file formats, Markdown and HTML, and version control with Git and GitHub, which make a resource easy to revise and remix."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 21:58:07"
version: 1.11
status: built
---

# Open File Formats and Version Control

## Summary

Covers the editable source metric: open file formats, Markdown and HTML, and version control with Git and GitHub, which make a resource easy to revise and remix. It comes early because later chapters on accessibility, practice, and metadata all rely on HTML and open formats. After this chapter you can tell an editable source from a locked file, and explain how Git and GitHub let others revise and remix a resource.

## Concepts Covered

This chapter covers the following 13 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Editable Source Metric | 44 |
| Source Format | 43 |
| Open File Format | 27 |
| Markdown | 6 |
| HTML | 15 |
| Word Processing File | 1 |
| PDF-Only Distribution | 3 |
| Version Control | 11 |
| Git | 7 |
| GitHub Repository | 6 |
| Fork | 1 |
| Pull Request | 2 |
| Changelog | 3 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Foundations of Open Educational Resources](../01-foundations-of-oer/index.md)
- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)

---

!!! mascot-welcome "Having the Right Is Not Having the Means"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A license can give you the right to revise a resource, and a locked file can still make it impossible. This chapter shows you how to tell a source you can edit from a file you can only read, and how teachers keep track when many people improve the same resource. Let's dive in and check the evidence!

Chapter 2 told you whether you may change a resource. This chapter asks a different question: can you? A teacher who finds a CC BY textbook that exists only as a PDF has the legal right to revise it and no practical way to do so. The permission is real, but the file takes it back.

The ten-metric rubric has one metric for this problem, editable source, and this chapter teaches it. You will learn what a source file is, which formats are open, why Markdown and HTML suit open resources, and how version control records every change so that many people can improve one resource without losing track.

## The Editable Source Metric

The **editable source metric** asks whether others can change the resource: whether its source is offered in a format that people can open and edit with free tools, and not only in a locked form such as a PDF. It is a reusability metric, scored from 0 to 10 like every other, and it protects the revise and remix permissions from Chapter 1. A license grants those permissions, and the editable source decides whether they are usable.

This book scores the metric with ten checks. A failed check *blocks revision* when a reviser cannot change the content without it. The scoring rules from Chapter 3 then apply: count the passed checks, find the band that holds that share, and choose the lower number in the band when a failed check blocks revision.

| # | Check | Blocks revision if it fails? |
|---|---|---|
| 1 | An editable source file is offered, not only a PDF | Yes |
| 2 | The source is in an open format | Yes |
| 3 | The source holds all of the content: text, headings, tables, and equations | Yes |
| 4 | The source can be downloaded with no login or payment | Yes |
| 5 | Images have their original or vector source files | No |
| 6 | Interactive parts supply their code | Yes |
| 7 | A short note explains how the pieces fit together | No |
| 8 | A record of changes is available | No |
| 9 | The reviewer opened the source in a free tool and it displayed correctly | Yes |
| 10 | Editing needs no paid software or special template | Yes |

A check that does not apply, such as the interactive-parts check for a resource with no simulations, counts as passed. The check list is this book's starting list, and a team may adjust it.

**Worked example: Watershed Basics.** The reviewer applies the ten checks to the reading from Chapter 3.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | HTML and Markdown source files are linked from the page. |
| 2 | Pass | Both formats are open. |
| 3 | Pass | The source holds all text, headings, and the quiz. |
| 4 | Pass | The files download with no login. |
| 5 | **Fail** | The five images are PNG files, and no source files are offered. |
| 6 | Pass | The quiz script is included in the HTML source. |
| 7 | Pass | A short note lists the files and how they connect. |
| 8 | **Fail** | No list of changes is offered. |
| 9 | Pass | The reviewer opened both files in a free editor, and they displayed correctly. |
| 10 | Pass | No paid software is needed. |

Eight of ten checks pass, a share of 80 percent, which falls in the 7 to 8 band. Neither failed check blocks revision, because a reviser can still change every word and replace any picture. The reviewer therefore chooses the higher number, **8**. The Chapter 3 worksheet recorded the image gap only. A fuller check also finds that no change record is offered, and that second gap is why the score is not higher.

## Source Format

A **source format** is the file format in which a resource is authored and can be edited. It differs from a *delivery format*, which is the form meant for reading, printing, or showing, and which is usually hard to change. A recipe and a cake make a useful comparison. The recipe is the source: you can change an ingredient and bake again. The cake is the delivered result: you can eat it, but you cannot take the sugar out. A source format keeps the structure of the content, such as headings, lists, links, and images, so a reviser can change it. A delivery format often keeps only the appearance.

| Kind | Purpose | Typical files |
|---|---|---|
| Source | Authoring and editing | Markdown, HTML, word processing files, vector drawings, spreadsheets |
| Delivery | Reading, printing, projecting | PDF, scanned pages, flattened images, exported slides |

A resource often exists in several files at once. The same lesson can be a Markdown file, a web page built from it, and a PDF made for printing.

**Worked example: one lesson, four files.**

| File | Source or delivery? | Can a reviser change the content? | Why |
|---|---|---|---|
| lesson.md | Source | Yes | Plain text that any editor can open |
| lesson.html | Source and delivery | Yes | The web page is readable and editable text |
| lesson.docx | Source | Yes | An editable word processing file |
| lesson.pdf | Delivery | Only with difficulty | The file records how pages look, not how the content is built |

A reviewer scores the editable source metric on the source files and does not count the delivery file. A resource that offers four formats but only a PDF as source has one useful file.

!!! mascot-thinking "Recipe, Not Cake"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A source is the recipe and a delivery file is the cake. Ask whether you could change the recipe, and a PDF alone will fail that test.

## Open File Format

An **open file format** is a file format whose specification is public and can be used without paying a fee or asking permission, so that anyone can write software that reads and writes it. Three questions test a format. Is the specification published? Can anyone implement it without paying? Does free software exist that opens it? A format that passes all three will still be readable when a company changes its products or closes. Files in a closed format may become unreadable, or readable only with software you must buy.

The table lists common formats. "Open" here means the specification is public. The last column says whether the format is a good source for editing.

| Format | Open? | A good source? |
|---|---|---|
| Markdown (.md) and plain text (.txt) | Yes, plain text | Yes |
| HTML (.html) | Yes, public web standards | Yes |
| OpenDocument text (.odt) | Yes, an international standard | Yes |
| Word document (.docx) | A published standard, but full fidelity depends on particular software | Usually acceptable |
| CSV (.csv) | Yes, plain text table | Yes, for data |
| SVG (.svg) | Yes, a web standard for drawings | Yes, for diagrams |
| PDF (.pdf) | An open international standard | Poor, because it is built for reading |
| A page layout or design-program file | Closed | Poor, unless you own the program |

**Worked example: choosing a format.** A teacher wants to share a worksheet so that colleagues can change it. She weighs three options. Saving it as a design-program file would keep her layout, but only people with that program could edit it. Saving it as a PDF would look identical everywhere, but no one could easily change a question. Saving it as an OpenDocument or Word document, with a Markdown or HTML copy beside it, lets nearly everyone open and change it. She picks the last option and keeps the PDF only as a printing copy.

## Common Source Formats

Four kinds of file account for most editable sources in OER. Two of them, Markdown and HTML, are open formats designed for the web. A third, the word processing file, is the format most teachers already use. The fourth, the PDF used alone, is the one that causes the problem.

### Markdown

**Markdown** is a way of writing structured text using plain keyboard symbols, such as a pound sign for a heading and a hyphen for a list item. A Markdown file is plain text, so any editor can open it, and a program converts it into a formatted web page. This book is written in Markdown. Markdown files are small, they work well with version control, and a reviewer can read the source and understand it. The trade-off is limited layout control, which helps accessibility and portability because the structure stays simple.

Before the example, here is what the symbols do. A line that starts with `##` becomes a second-level heading. A line that starts with a hyphen and a space becomes a bullet. Text in square brackets followed by an address in parentheses becomes a link. The same pattern with an exclamation mark in front becomes an image, and the square brackets then hold the *alt text*, the text description of the picture.

```markdown
## Water Cycle

Water moves between the sea, the air, and the land.

- evaporation
- condensation
- precipitation

Read more in [Watershed Basics](https://example.org/watershed-basics).

![A river flowing through a valley](https://example.org/images/river.png)
```

**Worked example: reading the Markdown.** The first line is a heading. The sentence below it is an ordinary paragraph, set off by a blank line. The three hyphen lines are a bulleted list. The sentence with square brackets and parentheses contains a link whose visible text is "Watershed Basics". The last line is an image, and its alt text is "A river flowing through a valley". Every piece of structure is visible in the text, which is exactly what a reviser needs.

Many tools read Markdown. GitHub shows a Markdown file as a formatted page, MkDocs (the tool that builds this book) turns Markdown files into a website, and free converters change Markdown into Word, HTML, or PDF files. That makes Markdown a good first-draft format: write once, and produce the other formats from the same source.

!!! mascot-tip "Write Once, Export Many"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Draft your own materials in Markdown or HTML first. Then export the PDF or Word copies you need, so that the editable source always exists.

The MicroSim below lets you practice. It shows a plain-text editor next to a live preview, and it sets four small tasks. Each task asks for one piece of structure: a heading, a list, a link, and an image with alt text.

#### Diagram: Markdown Practice Lab

<details markdown="1">
<summary>Markdown Practice Lab</summary>
Type: microsim
**sim-id:** markdown-practice-lab<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** practice<br/>
**Learning Objective:** The learner will practice writing Markdown for four structures (a heading, a list, a link, and an image with alt text), with at least 3 of 4 tasks passing on the first Check.

**Prerequisites:** Markdown, Source Format, Open File Format (all defined in this chapter above this block).

**Evidence of Mastery:** For each task the learner edits the text and presses Check. A task passes when the live preview contains the required structure exactly as described in the Requirement column of Content. Mastery is at least 3 of 4 tasks passing on the first Check. Using the hint is allowed and is shown in the score.

**Misconceptions:** (1) Markdown needs special software to write. (2) The square brackets in an image hold the file name. (3) Alt text is optional because the image is already on the page.

**Instructional Rationale:** Practice with immediate feedback is the right pattern for an Apply-level skill. A live preview shows each symbol's effect as the learner types, so the learner links the symbol to the structure instead of memorizing a list.

**Content:**

The four tasks, in this order:

| # | Task | Starting text | Requirement | Hint (shown on request) | Message when it fails |
|---|---|---|---|---|---|
| 1 | Make a heading | Water Cycle | The preview contains a level-2 heading whose text is exactly "Water Cycle". | Start the line with two pound signs and a space. | "The heading needs two pound signs, a space, and the text Water Cycle." |
| 2 | Make a list | evaporation, condensation, and precipitation, one per line | The preview contains a bulleted list of exactly three items, in the order evaporation, condensation, precipitation. | Start each line with a hyphen and a space. | "Each item needs a hyphen and a space at the start of its own line." |
| 3 | Add a link | The words Watershed Basics and the address https://example.org/watershed-basics | The preview contains a link whose visible text is exactly "Watershed Basics" and whose address is https://example.org/watershed-basics. | Put the visible text in square brackets and the address in parentheses right after it. | "The link needs square brackets around the words and parentheses around the address." |
| 4 | Add an image with alt text | The address https://example.org/images/river.png and the words A river flowing through a valley | The preview contains an image whose address is https://example.org/images/river.png and whose alt text is exactly "A river flowing through a valley". | Write an exclamation mark, then square brackets holding the alt text, then the address in parentheses. | "The image needs an exclamation mark first, then the alt text in brackets, then the address in parentheses." |

The Markdown symbols the lab teaches: two pound signs and a space for a level-2 heading, a hyphen and a space for a bullet, square brackets then parentheses for a link, and an exclamation mark before that pattern for an image.

**Provenance:** The tasks are illustrative cases written for this chapter, and the sim labels the addresses "example addresses". The symbols follow the chapter section "Markdown".

**Rules:** A task passes only when the preview shows the required structure with the exact text or address. Extra text elsewhere in the editor does not fail a task. The learner may press Check as many times as they like. Only a pass on the first Check counts toward mastery, and later passes are shown as passed with hint or retry.

**Learner Activity:**

1. The sim shows task 1, with the starting text in the editor and the live preview beside it.
2. The learner edits the text and watches the preview change.
3. The learner presses Check. The sim shows pass or fail with the message.
4. The learner may open the hint at any time.
5. After a pass the sim shows task 2, and so on through task 4.

**Feedback:** 4 tasks in the fixed order. Pass: "Task passed: the preview shows [requirement]". Fail: the message in the table for that task. The summary shows "[n] of 4 tasks passed on the first Check, and [m] needed a retry or a hint". At 3 or more first-Check passes it adds "You can write the four Markdown structures." Below 3 it lists the tasks that needed a retry.

**Starting State:** Task 1 with the text Water Cycle in the editor and an empty-structure preview. The question shown is "Make this line a level-2 heading."

**Chapter Anchors:** The chapter's Markdown example uses the heading "Water Cycle", a list of evaporation, condensation, and precipitation, the link text "Watershed Basics" with the address https://example.org/watershed-basics, and an image with the alt text "A river flowing through a valley".
</details>

### HTML

**HTML**, short for HyperText Markup Language, is the language of web pages. An HTML file is plain text in which *tags*, written in angle brackets, mark the parts of a page: a heading, a paragraph, a picture, a link. Every web page you read is HTML. Because browsers have to read it, HTML is an open standard, and a web resource in HTML needs no special software to open or edit. The accessibility chapter and the portability chapter both depend on HTML, since a screen reader reads HTML tags and an embed runs HTML.

Before the example, here is what the tags do. The heading tag marks a title, and the digit says how important the heading is. The paragraph tag marks a block of text. The image tag shows a picture, and its `alt` attribute holds the alt text. The link tag turns text into a link, and its `href` attribute holds the address.

```html
<h1>Watershed Basics</h1>
<p>Water moves between the sea, the air, and the land.</p>
<img src="river.png" alt="A river flowing through a valley">
<p>Read more in <a href="https://example.org/watershed-basics">Watershed Basics</a>.</p>
```

**Worked example: view the source.** Any browser can show the HTML of a page. Open a web page, right-click, and choose the option to view the page source. The page you read is built from the text you now see. A reviewer who wants to know whether the images have alt text, or whether the headings are in order, can look at the source and check each tag. That inspection is the basis of the accessibility checks in Chapter 7.

The next MicroSim shows the parts of a web page with an illustration. Each of its eight numbered markers points at one part and names the HTML tag that makes it.

#### Diagram: Anatomy of a Web Page

<details markdown="1">
<summary>Anatomy of a Web Page</summary>
Type: infographic
**sim-id:** html-page-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the HTML tag behind each of eight parts of a web page from a description of how the part looks, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** HTML, Markdown, Source Format (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 7 of 8 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) The picture's alt text is shown on the page. (2) Any large text is a heading tag. (3) A link needs no address.

**Instructional Rationale:** Identifying the parts of a page is a Remember-level task, and an illustration links each visible part to the tag that creates it. The quiz asks the learner to go from the look to the tag, which is the direction a reviewer works when inspecting a source.

**Content:**

The illustration is a text-free flat drawing of a simple lesson web page inside a browser frame. A small tab sits at the upper left of the frame. On the page, from top to bottom, are a large bar of heading text, a block of several thin text lines, a landscape picture box with a thin strip beneath it, a short list of three lines each with a dot at its left, an underlined bar of link text, and a small grid of two columns and three rows. The eight markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Page title (title tag) | A small tab at the upper left of the browser frame. | The title tag holds the text that appears in the browser tab and in search results. | Give each page its own title. |
| 2 | Main heading (h1 tag) | The largest bar of text at the top of the page. | The h1 tag marks the page's main heading. A page usually has one. | Use heading tags in order, with no skipped levels. |
| 3 | Paragraph (p tag) | A block of several thin lines under the heading. | The p tag marks a paragraph of text. | Keep one idea in each paragraph. |
| 4 | Image (img tag) | The landscape picture box in the middle of the page. | The img tag shows a picture. Its alt attribute holds the text description for people who cannot see it. | Write alt text for every image that carries meaning. |
| 5 | Caption (figcaption tag) | The thin strip directly beneath the picture. | The figcaption tag holds the caption for a figure, which is a good place to credit the image. | Put the image credit in the caption. |
| 6 | Bulleted list (ul and li tags) | Three short lines, each with a dot at its left. | The ul tag marks a bulleted list, and each li tag is one item. | Use a real list tag, not dots typed by hand. |
| 7 | Link (a tag) | An underlined bar of text. | The a tag makes a link, and its href attribute holds the address. | Write link text that says where the link goes. |
| 8 | Table (table tag) | A small grid with two columns and three rows. | The table tag marks a table, and header cells use the th tag. | Mark header cells so screen readers can read the table. |

**Provenance:** The tags follow the chapter section "HTML". The illustration is synthetic, and the sim labels the page "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 8 in the order of the table.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 8 hints the sim shows the summary.

**Feedback:** 8 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can read the parts of a page." Below 7 it lists the labels of the missed parts.

**Starting State:** The illustration with eight numbered markers, explore mode active, and the prompt "Hover a marker to see which tag makes it."

**Chapter Anchors:** The chapter says the heading tag marks a title, the paragraph tag marks text, the image tag has an alt attribute, and the link tag has an href attribute. The chapter's HTML example uses h1, p, img, and a.
</details>

### Word Processing File

A **word processing file** is a document made in a program such as a word processor, saved as an editable file with a name ending in .docx or .odt. It is the format most teachers already use, and it is a reasonable source format: anyone with a word processor can open it, change it, and save it. Two cautions apply. A .docx file is a published standard but is built around one family of programs, and complex layouts may shift in another program. An .odt file uses an international open standard and opens consistently in free software. When you share a word processing file as a source, keep the layout simple, use real headings and lists, and describe images with alt text.

### PDF-Only Distribution

**PDF-only distribution** means that the only file a resource offers is a PDF. A PDF records how each page looks, so a person can read and print it with confidence. It does not record the structure, so changing a sentence means copying text out of the page, losing headings and tables, and rebuilding the layout by hand. PDF-only distribution fails the editable source checks that matter most, and it usually leaves the metric in the low bands. A PDF alongside editable sources is fine. A PDF in place of them is a locked file.

!!! mascot-warning "A PDF Is Not a Source"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A PDF looks finished, so it is easy to mistake it for a source. If a resource offers only a PDF, you may have the legal right to change it and no practical way to do so. Ask the author for the Markdown, HTML, or word processing file, or score the metric low.

The next MicroSim puts the formats together. It shows ten files you might find with a resource, and for each one you judge whether it is a good source, an acceptable source, or a poor source.

#### Diagram: File Format Triage

<details markdown="1">
<summary>File Format Triage</summary>
Type: microsim
**sim-id:** file-format-triage<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of ten files is a good source, an acceptable source, or a poor source for revising a resource, with at least 8 of 10 correct on the first attempt.

**Prerequisites:** Source Format, Open File Format, Markdown, HTML, Word Processing File, PDF-Only Distribution (all defined in this chapter above this block).

**Evidence of Mastery:** For each file the learner commits one of three bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 8 of 10 correct on the first attempt. Reading the format table is exploration, not evidence.

**Misconceptions:** (1) A PDF is a good source because it is an open standard. (2) A picture of text can be edited. (3) A word processing file is always a poor source.

**Instructional Rationale:** Judging a file against criteria is an Evaluate-level action. Ten files that mix open and closed formats, text and pictures, and editable and locked files make the learner apply the same criteria each time: can the structure be changed with free tools?

**Content:**

The three bins: Good source (open format that keeps structure and opens in free tools), Acceptable source (editable, but depends on particular software or loses some structure), and Poor source (cannot be edited as structured content with free tools).

The ten files:

| # | File shown to the learner | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | lesson.md, a Markdown text file | Good source | Plain text in an open format that any editor opens. |
| 2 | lesson.odt, an OpenDocument text file | Good source | An international open standard that free software opens. |
| 3 | lesson.docx, a Word document | Acceptable source | Editable in many programs, though full fidelity depends on particular software. |
| 4 | slides.pptx, a slide file | Acceptable source | Editable, but it depends on particular software to display exactly. |
| 5 | diagram.svg, a vector drawing | Good source | An open web standard, and shapes and text stay editable. |
| 6 | diagram.png, a picture with no original drawing file | Poor source | A flat picture of a diagram, so its shapes and words cannot be edited. |
| 7 | data.csv, a table saved as plain text | Good source | Plain text that any spreadsheet or editor opens. |
| 8 | sim.html with sim.js, a simulation's web code | Good source | Readable, editable web code in open formats. |
| 9 | lesson.pdf, offered with no other file | Poor source | A PDF records how pages look, not how the content is built. |
| 10 | scan.jpg, a photo of a printed page | Poor source | It is a picture of text and not text, so no structure exists to edit. |

**Provenance:** The files are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The format judgments follow the chapter sections "Open File Format" and "Common Source Formats".

**Rules:** Each file has exactly one correct bin. Five files are Good, two are Acceptable, and three are Poor. A file offered alongside editable sources would be judged differently, and the sim states that these files are offered without other sources.

**Learner Activity:**

1. The learner sees one file at a time, with the three bin definitions.
2. The learner places the file in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After file 10 the sim shows the summary.

**Feedback:** 10 files in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 8 or more it adds "You can judge a source." Below 8 it lists the Why text of each missed file.

**Starting State:** The first file, the three bin definitions, and three empty bins. The question shown is "Is this file a good source for revising the resource?"

**Chapter Anchors:** The chapter's format table lists Markdown, HTML, OpenDocument, Word, CSV, SVG, and PDF, and says a PDF alone is a poor source.
</details>

## Version Control

**Version control** is a system that records every change made to a set of files, along with who made it, when, and why, so that any earlier state can be viewed or restored. Most people have met the problem it solves: a folder holding `lesson_final.docx`, `lesson_final2.docx`, and `lesson_FINAL_really.docx`, with no way to tell which differs from which. A version control system replaces that folder with one set of files and a recorded history.

The history gives an open resource four things that copies cannot. A reviser can see exactly what changed between two versions. A mistake can be undone by returning to an earlier state. Several people can work on the same resource at once and combine their changes. And a reuser can judge a resource's health by looking at when it was last changed and by whom.

| Without version control | With version control |
|---|---|
| Many copies of the same file with confusing names | One set of files with a recorded history |
| No record of who changed what | Every change carries an author, a date, and a message |
| Two people editing at once overwrite each other | Changes are combined, and conflicts are shown |
| An error cannot be reliably undone | Any earlier version can be restored |

**Worked example: a history instead of a pile of copies.** A teacher fixes a wrong answer in a practice set on 12 September and adds alt text on 13 September. With copies, a colleague must open both files and compare them by eye. With version control, the history lists the two changes, each with a date and a one-line message, and shows the exact lines that differ.

### Git

**Git** is the most widely used version control software. It is free and open source, and its creator, Linus Torvalds, released it in 2005 to manage the Linux kernel project. Git keeps the whole history on your own computer, so you can work without a network connection and share your work later. It uses four ideas, and the table defines them before they appear in any example.

| Term | Meaning |
|---|---|
| Repository | The project folder together with its full recorded history |
| Commit | A saved snapshot of the changes, with an author, a date, and a message |
| Branch | A separate line of work that does not disturb the main line until you are ready |
| Merge | Combining the changes from one branch into another |

You can use Git without typing commands, because GitHub and several desktop programs provide buttons for each step. For readers who want to see the commands, four of them cover most of a teacher's work. The command `git clone` copies a repository from the web to your computer. The command `git add` marks a changed file for the next snapshot. The command `git commit` saves the snapshot, and the text after `-m` is its message. The command `git push` sends your new commits to the shared copy on the web.

```bash
git clone https://github.com/example-school/fraction-practice-set.git
git add problems.md
git commit -m "Add alt text to the two number-line images"
git push
```

**Worked example: one improvement, start to finish.** A teacher wants to add alt text to a practice set. She runs the four commands in order. The clone gives her a working copy. She edits `problems.md` in a text editor. The add command selects that file, the commit command saves the change with a message that says what she did, and the push command publishes it. The history now shows her change, her name, and the date.

!!! mascot-encourage "The Words Are the Hard Part"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    Commit, branch, and merge sound strange at first, and nearly everyone stumbles on them. You already keep a history when you save a document under a new name, and Git does the same with a message attached. Start with the four terms in the table and the rest follows.

The MicroSim below shows a small repository's history as a graph. Each circle is a commit, and the lines show which commit came before which. In explore mode you click a commit to read its message. In quiz mode you answer questions about the history by clicking the right commit.

#### Diagram: Git History Explorer

<details markdown="1">
<summary>Git History Explorer</summary>
Type: graph-model
**sim-id:** git-history-explorer<br/>
**Library:** vis-network<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine the history of a small repository to find the commit that answers each of six questions, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Version Control, Git (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the commit that answers a question. A click is correct when it matches the Correct commit column in Content. Mastery is at least 5 of 6 correct on the first attempt. Clicking commits in explore mode is exploration, not evidence.

**Misconceptions:** (1) A merge commit is the same as the changes it combines. (2) A branch is a separate copy of the files. (3) The history cannot show who made a change.

**Instructional Rationale:** Examining a history is an Analyze-level action, because the learner must read the parts, the messages and the structure, to find which one answers a question. A graph shows the branch and the merge as shape, so the learner sees what the words describe.

**Content:**

The graph has 8 nodes, one per commit, and 8 edges. Each edge points from a commit to its parent, the commit that came before it. Commit c7 is a merge commit and has two parents, c6 and c5. The repository is a made-up practice set called Fraction Practice Set, and the authors are made up. Clicking a node highlights its parents and children and shows its details.

| Commit | Author | Date | Message | Files changed | Branch | Parents |
|---|---|---|---|---|---|---|
| c1 | Priya Shah | 2026-09-01 | Add first draft of the fraction problems | problems.md | main | none |
| c2 | Priya Shah | 2026-09-03 | Add an answer key | answers.md | main | c1 |
| c3 | Sam Okafor | 2026-09-10 | Fix the answer to problem 7 | answers.md | main | c2 |
| c4 | Dana Reyes | 2026-09-12 | Start alt text work: describe the two number-line images | problems.md | alt-text | c3 |
| c5 | Dana Reyes | 2026-09-13 | Add alt text to two more images | problems.md | alt-text | c4 |
| c6 | Priya Shah | 2026-09-14 | Define denominator where it first appears | problems.md | main | c3 |
| c7 | Priya Shah | 2026-09-15 | Merge the alt-text branch into main | problems.md | main | c6 and c5 |
| c8 | Priya Shah | 2026-09-16 | Add CHANGELOG.md listing the changes | CHANGELOG.md | main | c7 |

The six questions, in this order:

| # | Question shown to the learner | Correct commit | Why (shown as feedback) |
|---|---|---|---|
| 1 | Which commit first added an answer key? | c2 | Its message says it added an answer key, and it changed answers.md. |
| 2 | Which commit corrected a wrong answer? | c3 | Its message says it fixed the answer to problem 7. |
| 3 | Which commit began the alt text work? | c4 | It is the first commit on the alt-text branch and its message names the number-line images. |
| 4 | Which commit brought the alt text work into the main line? | c7 | It is the merge commit, and it has two parents, c6 and c5. |
| 5 | Which commit created the first list of changes? | c8 | It added CHANGELOG.md. |
| 6 | Which commit defined the word denominator? | c6 | Its message says it defined denominator where it first appears. |

**Provenance:** The repository, authors, dates, and messages are made up for this chapter, and the sim labels them "illustrative example". The terms follow the chapter section "Git".

**Rules:** Each question has exactly one correct commit. Clicking a branch label or the background during the quiz counts as a wrong attempt. The sim offers buttons to zoom and does not zoom with the mouse wheel.

**Learner Activity:**

1. In explore mode the learner clicks each commit and reads its author, date, message, and files changed.
2. In quiz mode the sim shows question 1 above the graph.
3. The learner clicks the commit that answers it.
4. If the first click is wrong, the sim says so and the learner tries once more. If the second click is also wrong, the sim reveals the commit and the Why text.
5. After question 6 the sim shows the summary.

**Feedback:** 6 questions in the fixed order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [commit]. [Why]". First wrong click: "Not quite. Read the commit messages again." Second wrong click: "The answer is [commit]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read a history." Below 5 it lists the questions the learner missed.

**Starting State:** The graph with all 8 commits visible, explore mode active, and the prompt "Click a commit to see what changed."

**Chapter Anchors:** The chapter's terms are repository, commit, branch, and merge. The chapter says a history records an author, a date, and a message for every change.
</details>

### GitHub Repository

**GitHub** is a website that hosts Git repositories and adds tools for people to work together. A **GitHub repository** is one project's page on that site, holding the files, the history, and the discussion around them. Many open resources live in GitHub repositories because the site is free for public projects, shows the history, and can publish a repository as a web page. Other hosts do the same job, and a repository can be copied between hosts because Git is open.

A repository page has parts that a reviewer learns to read:

- **The file list:** the source files themselves.
- **The README:** a text file shown below the file list that says what the resource is and how to use it.
- **The license file:** a file, often named LICENSE, that states the license.
- **The commit history:** the record of every change.
- **Issues:** a place where users report problems or ask questions.
- **Pull requests:** a place where people propose changes, explained a few sections ahead.

**Worked example: reading a repository.** A reviewer opens the repository for a practice set and answers four questions in five minutes. Is there a license file, and does it match the resource's license statement? When was the last commit, and so is the resource still maintained? Are the files in open formats such as Markdown? Do the open issues show unresolved problems? Each answer gives evidence for the open license, editable source, and accuracy metrics. Evidence from a repository, such as the date of a commit, can be checked and cited.

The MicroSim below shows an illustration of a repository page. Eight numbered markers point to the parts a reviewer reads.

#### Diagram: Anatomy of a GitHub Repository Page

<details markdown="1">
<summary>Anatomy of a GitHub Repository Page</summary>
Type: infographic
**sim-id:** github-repository-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the eight parts of a repository page that a reviewer reads, from a description of each part's appearance, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** GitHub Repository, Version Control, Git (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 7 of 8 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) The README is the license. (2) The fork button changes the original repository. (3) The file list shows only the final version.

**Instructional Rationale:** Identifying the parts of a page is a Remember-level task, and an illustration of the page places each part where the reviewer will find it. The quiz asks the learner to go from the look of a part to its name, which is how they will navigate a real repository.

**Content:**

The illustration is a text-free flat drawing of a repository page in a browser frame. Under the page header is a row of five small tabs. At the upper right is a small button with a branching-line icon. At the left, above the main area, is a drop-down box. Below it is a thin strip holding a small round avatar and one short line of text, and beside the strip is a small clock icon with a number. Under the strip is a column of rows, each with a folder icon or a file icon. Below the column is a large block of text lines. In a narrow column at the right is a small scales icon beside a short line. The eight markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Tab row | A row of five small tabs under the page header. | The tabs switch between the files, the reported problems (issues), and the proposed changes (pull requests). | Open the issues tab to see problems others have found. |
| 2 | Fork button | A small button with a branching-line icon at the upper right. | Creates your own copy of the repository, which you can change without touching the original. | Fork before you revise, so the original stays as the author left it. |
| 3 | Branch selector | A drop-down box at the left above the main area. | Switches between lines of work, like the main line and a branch for a new feature. | The main branch is the usual place to read the current version. |
| 4 | Latest commit strip | A thin strip with a small round avatar and one short line of text. | Shows who made the most recent change, what they said about it, and when. | A last commit that is years old suggests the resource is no longer maintained. |
| 5 | Commit history link | A small clock icon with a number beside it. | Opens the full list of commits, with authors, dates, and messages. | Use it to date your evidence: cite the commit you reviewed. |
| 6 | File list | A column of rows, each with a folder icon or a file icon. | Lists the source files and folders in the repository. | Check the file types: Markdown or HTML suggest an editable source. |
| 7 | README | A large block of text lines below the file list. | Explains what the resource is, how its files fit together, and how to use it. | A README is the note that the editable source metric's seventh check asks for. |
| 8 | License entry | A small scales icon beside a short line in the narrow column at the right. | Shows the repository's license, taken from its license file. | Compare it with the license statement on the resource itself. |

**Provenance:** The parts follow the chapter section "GitHub Repository". The illustration is synthetic, and the sim labels the page "illustrative example". The sim states that the layout of a real GitHub page can change over time and that the parts, not their positions, are what a reviewer should look for.

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 8 in the order of the table.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 8 hints the sim shows the summary.

**Feedback:** 8 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can read a repository page." Below 7 it lists the labels of the missed parts.

**Starting State:** The illustration with eight numbered markers, explore mode active, and the prompt "Hover a marker to see what it is."

**Chapter Anchors:** The chapter lists the parts of a repository page as the file list, the README, the license file, the commit history, issues, and pull requests. The chapter says a README is the short note that explains how the pieces fit together.
</details>

### Fork

A **fork** is your own copy of someone else's repository, made on the same site. The copy is independent: you can change it freely without affecting the original, and it keeps a link back to the source. Forking is the repository version of the revise and remix permissions. An open license gives you the right to change a resource, and a fork gives you the place to do it. A teacher who wants to adapt an open lesson for her class forks the repository, edits her copy, and keeps the original untouched.

### Pull Request

A **pull request** is a proposal to merge changes from one copy of a repository into another. It lets you offer a correction to the original author instead of keeping it in your fork. You make the change in your fork, open a pull request, and the maintainer reads it, comments, and either merges it or asks for changes. Pull requests are how a small fix, such as a typo or a missing alt text, travels from one teacher to every other teacher who uses the resource. They also keep the original's quality under review, because every change is read before it joins the main line.

The MicroSim below tests whether you know the order of a contribution. It gives you seven steps in a scrambled order, and you put them into the right sequence.

#### Diagram: Fork and Pull Request Sequencer

<details markdown="1">
<summary>Fork and Pull Request Sequencer</summary>
Type: microsim
**sim-id:** fork-pull-request-sequencer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** list<br/>
**Learning Objective:** The learner will list the seven steps of contributing an improvement to an open resource in the correct order, with at least 6 of 7 steps in the correct position on the first Check.

**Prerequisites:** Fork, Pull Request, GitHub Repository, Git (all defined in this chapter above this block).

**Evidence of Mastery:** The learner arranges seven steps and presses Check. A step is correct when it sits in the position given in the Position column of Content. Mastery is at least 6 of 7 steps in the correct position on the first Check. Rearranging steps before pressing Check is exploration, not evidence.

**Misconceptions:** (1) You edit the original repository directly. (2) A pull request is sent before the change is made. (3) The maintainer must accept every pull request.

**Instructional Rationale:** Ordering the steps of a process is a Remember-level task that checks whether the learner holds the sequence. Each step depends on the one before, so a wrong position can be explained by a dependency.

**Content:**

The seven steps, with their correct positions and the reason each follows its predecessor:

| Position | Step | Why it comes here |
|---|---|---|
| 1 | Find the repository of the resource you want to improve. | You cannot copy what you have not found. |
| 2 | Fork the repository to make your own copy. | You change your copy, not the original. |
| 3 | Make your change in your copy and save it with a message that says what you did. | A pull request needs a change to propose. |
| 4 | Open a pull request that proposes your change to the original repository. | The maintainer can only review a change that has been proposed. |
| 5 | The maintainer reads your pull request and leaves comments. | The review follows the proposal. |
| 6 | You answer any comments by adding more changes to your copy. | You respond to what the review found. |
| 7 | The maintainer merges the pull request into the original. | Merging is the last step, after the review is satisfied. |

**Provenance:** The steps follow the chapter sections "Fork" and "Pull Request". The sim states that a maintainer may also decline a pull request, and that the sequence shows the successful path.

**Rules:** Each step has exactly one correct position, and the seven positions are distinct. The learner may move steps freely before pressing Check. After a Check, steps in the correct position are marked correct and the rest are marked out of place.

**Learner Activity:**

1. The sim shows the seven steps in a shuffled order.
2. The learner moves steps up or down to put them in the order they think is correct.
3. The learner presses Check.
4. The sim shows which steps are in the correct position and, for each out-of-place step, the reason it belongs where it does.
5. The learner may rearrange and Check again.

**Feedback:** The learner may press Check as many times as they like, and only the first Check counts as evidence. After each Check the sim shows "[n] of 7 steps in the correct position". Correct steps are marked correct. For each out-of-place step the sim shows its Why text. At 6 or more on the first Check it adds "You know the order of a contribution." Below 6 it reports the count and invites another try.

**Starting State:** The seven steps in a shuffled order that is not the correct order, and the prompt "Put the steps in the order a contribution happens."

**Chapter Anchors:** The chapter says a fork is your own copy, that you make the change in your fork, and that a pull request proposes your change to the original, where the maintainer reads it and may merge it.
</details>

### Changelog

A **changelog** is a file that lists the notable changes to a resource in order, usually with a date or a version number and a line for each change. A reviser can read it to see what changed without comparing files, and a reuser can decide whether to update. A changelog is also the right place to record changes for the attribution requirement from Chapter 2, which asks anyone who adapts a CC BY work to say what they changed. A common convention uses a file named CHANGELOG.md, with the newest entry first.

```markdown
## 2026-09-16

- Added alt text to four images.
- Defined the word denominator where it first appears.
- Fixed the answer to problem 7.
```

The Markdown above shows a changelog entry: a date as a heading, then one bullet per change. Each bullet is short and says what changed, not why.

!!! mascot-tip "One Line, Two Jobs"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Write each change in the changelog as one dated line. The same line later serves as the change note that a CC BY credit requires, so you write it once and use it twice.

## Scoring the Editable Source Metric

You now have what you need to score the metric. The procedure has six steps. List the files the resource offers. Open the source files in a free tool. Run the ten checks from the first section of this chapter. Count the passes and find the band. Choose the number inside the band, using the lower one when a failed check blocks revision. Record the evidence for each failed check.

The last MicroSim of the chapter is a scoring practice. It shows five resources with their ten check results, and for each one you choose the score from 0 to 10.

#### Diagram: Editable Source Metric Scorer

<details markdown="1">
<summary>Editable Source Metric Scorer</summary>
Type: microsim
**sim-id:** editable-source-metric-scorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the ten editable source checks and the Chapter 3 scoring rules to choose the metric score for each of five resources, with at least 4 of 5 scores exactly correct on the first attempt.

**Prerequisites:** The Editable Source Metric, Metric Score, Scoring Descriptor, Source Format, Open File Format, Changelog (all defined in this chapter or in Chapter 3 above this block).

**Evidence of Mastery:** For each resource the learner chooses a whole-number score from 0 to 10 after seeing the ten check results. A score is correct when it equals the Correct score column in Content. Mastery is at least 4 of 5 scores correct on the first attempt. Opening the check list and the descriptor table is exploration, not evidence.

**Misconceptions:** (1) Any failed check lowers the score by the same amount. (2) A resource with some editable files scores at least 5. (3) The higher number in a band is always correct.

**Instructional Rationale:** Applying a scoring procedure to new cases is an Apply-level task. Five resources with different mixes of passes and blocking failures make the learner use every step: count, band, then choose within the band.

**Content:**

The ten checks, each marked as blocking or not:

| # | Check | Blocks revision if it fails? |
|---|---|---|
| 1 | An editable source file is offered, not only a PDF | Yes |
| 2 | The source is in an open format | Yes |
| 3 | The source holds all of the content | Yes |
| 4 | The source can be downloaded with no login or payment | Yes |
| 5 | Images have their original or vector source files | No |
| 6 | Interactive parts supply their code | Yes |
| 7 | A short note explains how the pieces fit together | No |
| 8 | A record of changes is available | No |
| 9 | The reviewer opened the source in a free tool and it displayed correctly | Yes |
| 10 | Editing needs no paid software or special template | Yes |

The descriptor bands, applied to the share of checks passed: 0% is 0; 1% to 24% is 1 to 2; 25% to 49% is 3 to 4; 50% to 74% is 5 to 6; 75% to 89% is 7 to 8; 90% to 100% is 9 to 10. Within a two-number band, choose the lower number when any failed check blocks revision, and the higher number otherwise. A score of 10 requires every check to pass. A check that does not apply counts as passed.

The five resources:

| # | Resource | Checks failed | Checks passed | Share | Band | Blocking failure? | Correct score | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|---|
| 1 | Open Algebra | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed, so the score is 10. |
| 2 | Watershed Basics | 5 and 8 | 8 | 80% | 7 to 8 | No | 8 | Neither failed check blocks revision, so the higher number applies. |
| 3 | District Unit | 3 and 7 | 8 | 80% | 7 to 8 | Yes, check 3 | 7 | The source is missing part of the content, which blocks revision, so the lower number applies. |
| 4 | Handout Scans | 1, 2, 3, 5, 9 | 5 (checks 4, 6, 7, 8, 10) | 50% | 5 to 6 | Yes | 5 | Check 6 does not apply and counts as passed. Several blocking checks failed, so the lower number applies. |
| 5 | PDF-Only Report | 1, 2, 3, 5, 7, 8, 9 | 3 (checks 4, 6, 10) | 30% | 3 to 4 | Yes | 3 | Check 6 does not apply and counts as passed. Blocking checks failed, so the lower number applies. |

**Provenance:** The ten checks and the descriptor bands follow the chapter sections "The Editable Source Metric" and Chapter 3. The five resources are illustrative cases written for this chapter, and the sim labels them "illustrative examples". Resource 2 is the chapter's worked example.

**Rules:** A score is the band chosen from the share passed, and then the number chosen within the band by the blocking rule. Each resource has exactly one correct score. For a band that holds a single number, that number is the score.

**Learner Activity:**

1. The sim shows resource 1 with its ten check results.
2. The learner may open the check list and the descriptor table.
3. The learner chooses a score from 0 to 10, and the choice is committed.
4. The sim shows the count of passes, the band, whether any failure blocks revision, and the correct score with the Why text.
5. After resource 5 the sim shows the summary.

**Feedback:** 5 resources in the fixed order, one attempt each. Correct: "Correct: [score]. [Why]". Incorrect: "Not quite. [passes] checks passed, which is [share] and the [band] band. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can score editable source." Below 4 it lists the Why text of each missed resource.

**Starting State:** Resource 1 with all ten results shown and no score chosen. The question shown is "What editable source score does this resource earn?"

**Chapter Anchors:** The chapter's worked example for Watershed Basics fails checks 5 and 8, passes 8 of 10, and scores 8, with the higher number chosen because neither failure blocks revision.
</details>

## Key Takeaways

- The **editable source metric** asks whether others can change the resource. Ten checks decide the score, and a failed check that blocks revision pulls the score to the lower number in its band.
- A **source format** is the form you edit, and a delivery format is the form you read. An **open file format** has a public specification, can be implemented without a fee, and opens in free software.
- **Markdown** and **HTML** are plain-text open formats. A **word processing file** is a reasonable source. **PDF-only distribution** is a locked file.
- **Version control** records every change with an author, a date, and a message. **Git** is the open-source tool, and a **GitHub repository** is a project's page on a hosting site.
- A **fork** is your own copy, a **pull request** proposes your change to the original, and a **changelog** lists the changes in order.

!!! mascot-celebration "You Can Tell Source From Cake"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now tell an editable source from a locked file, name an open format, read a repository's history, and score the editable source metric with evidence. A resource you can change is a resource you can improve, and this chapter gave you the means to check.

[See Annotated References](./references.md)
