---
title: "Reusable Components and Publishing OER"
description: "Shows how to package components, build a library, publish improved OER with MkDocs and GitHub Pages, share through a clearinghouse, track reuse, and report impact."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 23:11:09"
version: 1.11
---

# Reusable Components and Publishing OER

## Summary

Shows how to package components, build a library, publish improved OER with MkDocs and GitHub Pages, share through a clearinghouse, track reuse, and report impact. It covers what happens after improvement and testing, and builds on the components, metadata, and results from earlier chapters. After this chapter you can package a reusable component, publish it openly, and track how others reuse it.

## Concepts Covered

This chapter covers the following 22 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Reusable Component | 5 |
| Component Library | 2 |
| Component Packaging | 1 |
| Component Licensing | 1 |
| Component Discoverability | 1 |
| Learning Graph | 5 |
| Concept Dependency | 1 |
| Chapter Structure | 2 |
| Intelligent Textbook | 1 |
| Publishing OER | 11 |
| Static Site Generator | 3 |
| MkDocs | 1 |
| GitHub Pages | 1 |
| OER Clearinghouse | 1 |
| Release Notes | 1 |
| Maintenance Plan | 1 |
| Issue Tracking | 1 |
| Feedback Channel | 2 |
| Community Contribution | 1 |
| Reuse Tracking | 2 |
| Usage Analytics | 2 |
| Impact Reporting | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Foundations of Open Educational Resources](../01-foundations-of-oer/index.md)
- [Chapter 2: Open Licenses and Attribution](../02-open-licenses-attribution/index.md)
- [Chapter 4: Open File Formats and Version Control](../04-open-formats-version-control/index.md)
- [Chapter 5: Accuracy and Currency](../05-accuracy-currency/index.md)
- [Chapter 6: Alignment and Readability](../06-alignment-readability/index.md)
- [Chapter 8: Practice and Feedback](../08-practice-feedback/index.md)
- [Chapter 9: Modularity and Metadata](../09-modularity-metadata/index.md)
- [Chapter 10: Portability and Reuse Across Platforms](../10-portability-reuse/index.md)
- [Chapter 15: Improving a Resource with AI Agents](../15-improving-resources-with-ai/index.md)
- [Chapter 17: Analyzing A/B Test Results](../17-ab-testing-analysis/index.md)

---

!!! mascot-welcome "An Improved Resource Is Only Useful When Others Can Use It"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    You improved a resource and tested it with students. Now you will package it so other teachers can reuse it, publish it so they can find it, and keep it healthy once it is out. Let's dive in and check the evidence!

A resource that sits on your computer helps one class. The point of an open educational resource is that it can help many, and that only happens if others can find it, understand what they may do with it, and use it without rebuilding it. This chapter covers the work after the improvement and the test: packaging the parts, publishing the whole, and learning what happened next.

The example is the improved *Watershed Basics v1.1*. After the test of Chapter 17 the teacher decides to release it, so the chapter follows that release from a folder of files to a public site and a report on its use.

## Reusable Component

A **reusable component** is a part of a resource that a stranger can lift out and use in a different course without asking for help. Chapter 9 gave the tests: the part stands alone, it embeds without edits, and it carries its own license and metadata. This chapter adds the work of making components available to others.

After the splitting of Chapter 15, *Watershed Basics v1.1* has three components.

| Component | What it is | Stands alone because |
|---|---|---|
| watershed-reading | The reading with its images and captions | It defines its terms and refers to nothing outside itself |
| watershed-quiz | The 8-question quiz with explanations | It repeats what it needs and loads its own script |
| watershed-sim | The "Where does the rain go?" simulation | It has its own page and instructions |

### Component Packaging

**Component packaging** is the gathering of everything a component needs into one folder that can be copied, downloaded, or embedded as a unit. A package contains the content, a short README that says what the component is and how to use it, a license file, a metadata file, and any images or scripts. All links inside the package should be complete addresses or point to files inside the package, so that nothing breaks when the folder moves, which was the portability problem of Chapter 10.

A package is easiest to understand as a folder with a fixed shape. The listing below shows the quiz package, with the purpose of each file in the table that follows it.

```text
watershed-quiz/
  index.html
  quiz.js
  README.md
  LICENSE.txt
  metadata.json
  img/
```

| File | Purpose |
|---|---|
| index.html | The quiz page itself |
| quiz.js | The script the page needs, kept inside the folder |
| README.md | What the component is, how to embed it, and how to credit it |
| LICENSE.txt | The license text or a link to it |
| metadata.json | The metadata record of Chapter 9 in a form a program can read |
| img/ | The images the page uses |

### Component Licensing

**Component licensing** is the practice of giving each component its own license statement and credit lines, so that a component keeps its terms when it travels alone. A reuser who copies only the quiz must still see that it is CC BY 4.0, who wrote it, and what it adapted. The statement appears in three places: the visible footer of the page, the license file, and the metadata record.

Licenses can interact inside a component. If the quiz includes an image under CC BY-SA, the component as a whole must be shared in a way that satisfies that condition, as Chapter 2 taught. List every third-party item with its title, author, source, and license, and check that the licenses are compatible with the one you choose.

### Component Discoverability

**Component discoverability** is how easily the people who need a component can find it. A component that no one can find is not reused. Discoverability comes from a clear descriptive name, a complete metadata record with subject, grade level, and keywords, a short description in plain words, and a place where it is listed: an index page of your own site and a catalog that others search. A name like `watershed-quiz` tells a visitor what the component is, and a name like `final-v2` tells them nothing. A description of one or two sentences that begins with what the component does, such as "An 8-question quiz on how water drains from land", lets a search match it to a teacher's need.

The MicroSim below practices the checks of this section. It shows seven packages, and for each one you decide whether it is ready to publish.

#### Diagram: Component Package Inspector

<details markdown="1">
<summary>Component Package Inspector</summary>
Type: microsim
**sim-id:** component-package-inspector<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of seven component packages is ready to publish and name the gap in each package that is not, with at least 6 of 7 verdicts correct on the first attempt.

**Prerequisites:** Reusable Component, Component Packaging, Component Licensing, Component Discoverability (all defined in this chapter above this block).

**Evidence of Mastery:** For each package the learner commits Ready or Not ready, and for a Not ready package picks the gap from five. A verdict is correct when it matches the Correct verdict column in Content, and the gap is checked in the feedback. Mastery is at least 6 of 7 verdicts correct on the first attempt. Reading the package table is exploration, not evidence.

**Misconceptions:** (1) A package with a page and images is complete. (2) The license can be added when someone asks. (3) A package that works on the author's computer works everywhere.

**Instructional Rationale:** Judging a package against the checks is an Evaluate-level action that precedes every release. Packages that each lack one thing, and two that lack nothing, teach the learner to inspect a package item by item.

**Content:**

The two verdicts: Ready, Not ready. The five gaps: No license, No metadata, No README, Link outside the folder, Not standalone.

The seven packages (all made up, for Watershed Basics v1.1):

| # | Package | Files and notes | Correct verdict | Gap | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | watershed-reading | index.html, README.md, LICENSE.txt, metadata.json, img/ with complete image addresses | Ready | None | It has every file and its links work from anywhere. |
| 2 | watershed-quiz | index.html, README.md, LICENSE.txt, metadata.json, and a script loaded from ../shared/quiz.js | Not ready | Link outside the folder | The script lives outside the folder and will not travel with it. |
| 3 | watershed-sim | index.html, sim.js, README.md, metadata.json, and no license file or statement | Not ready | No license | A reuser cannot tell what they may do. |
| 4 | watershed-glossary | index.html, README.md, LICENSE.txt, and no metadata file | Not ready | No metadata | The component cannot be found or described by a catalog. |
| 5 | watershed-map | map.png, LICENSE.txt, metadata.json, and no README or page | Not ready | No README | Nothing explains what the map is or how to credit it. |
| 6 | watershed-unit | index.html, README.md, LICENSE.txt, metadata.json, and a page that says "use the quiz in watershed-quiz" | Not ready | Not standalone | It depends on another component. |
| 7 | watershed-video | index.html, captions.vtt, transcript.md, README.md, LICENSE.txt, metadata.json | Ready | None | It has every file, including captions and a transcript. |

**Provenance:** The packages are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The gaps follow the chapter sections on packaging, licensing, and discoverability.

**Rules:** Each package has exactly one correct verdict. Two are Ready and five are Not ready, one for each gap.

**Learner Activity:**

1. The learner sees one package as a file listing with notes.
2. The learner chooses Ready or Not ready. If Not ready, the learner also picks the gap.
3. The sim shows whether the verdict was correct, the gap, and the Why text.
4. After package 7 the sim shows the summary.

**Feedback:** 7 packages in a shuffled order, one attempt each. Correct: "Correct: [verdict]. [Why]". Incorrect: "Not quite. This package is [verdict]. [Why]". The summary shows "[n] of 7 correct on the first attempt". At 6 or more it adds "You can inspect a package." Below 6 it lists the Why text of each missed package.

**Starting State:** The first package in the shuffled order and the two verdicts. The question shown is "Could a stranger use this package as it is?"

**Chapter Anchors:** The chapter's file table lists the README, the license file, and the metadata file, and it says links must stay inside the package.
</details>

## Component Library

A **component library** is an organized collection of reusable components, with an index that lets a visitor see what is there and pick what they need. A library turns a pile of packages into something a teacher can browse. It works best with consistent names, one folder per component, a catalog page, and a release version for the library as a whole.

The catalog is a table with one row per component. The *Watershed Basics* library lists its three components and a glossary.

| Component | Description | Grade | License | Version |
|---|---|---|---|---|
| watershed-reading | A short reading that explains what a watershed is | 6 and 7 | CC BY 4.0 | 1.1 |
| watershed-quiz | An 8-question quiz with explanations | 6 and 7 | CC BY 4.0 | 1.1 |
| watershed-sim | A simulation of rain and ground cover | 6 and 7 | CC BY 4.0 | 1.1 |
| watershed-glossary | Eleven terms with definitions | 6 and 7 | CC BY 4.0 | 1.1 |

A library also makes upkeep easier, since one maintenance plan and one feedback channel serve every component.

## Learning Graph

A **learning graph** is a map of the concepts of a subject in which each concept is linked to the concepts it depends on. It answers the question, "What must a learner know before this?" A learning graph helps reuse because a teacher can place a component in a sequence by checking what it assumes and what it teaches, and an author can order a textbook so that nothing is used before it is explained.

This book has a learning graph of its own, with 351 concepts joined by 586 dependencies. Its longest chain of prerequisites is 24 concepts deep, and it ends at the concept of Rubric-Outcome Correlation from Chapter 17.

### Concept Dependency

A **concept dependency** is a link that says one concept needs another first. If a learner cannot understand *Re-Scoring* without understanding an *Improvement Plan*, then Re-Scoring depends on Improvement Plan. In this book's graph, each link points from the concept to the concept it depends on, so the arrow reads "needs".

| Concept | Depends on (examples from this book's graph) |
|---|---|
| Score Gain | Re-Scoring |
| Re-Scoring | Improvement Plan, Agent Scoring, Total Score |
| Improvement Plan | Total Score, Accept Correct or Reject |
| Impact Reporting | Reuse Tracking, Usage Analytics, Results Summary |

A valid graph has no loops. If A needs B and B needs A, neither can be learned first. Checking for loops, and for concepts used before their prerequisites, is how a graph earns trust.

!!! mascot-thinking "Read an Arrow as the Word Needs"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    When an arrow runs from Score Gain to Re-Scoring, it says Score Gain needs Re-Scoring. Learn the concept at the arrow's tip first.

### Chapter Structure

A **chapter structure** is the division of a textbook's concepts into chapters in an order that respects the dependencies: every concept's prerequisites must appear in the same chapter or an earlier one. A structure that breaks this rule forces the reader to use a term before it is defined. Suppose Chapter 4 needed *Re-Scoring*, which this book teaches in Chapter 15: the reader would meet the term eleven chapters early. The fix is to move the concept later or to move its prerequisites earlier. A short script can test every dependency against the chapter order, and for this book it checked all 586 dependencies of the 351 concepts and found none placed before a prerequisite.

### Intelligent Textbook

An **intelligent textbook** is a textbook built as a website from a learning graph, chapters in dependency order, a glossary, quizzes, and interactive simulations called MicroSims. The learning graph gives it a map of its own contents, and the MicroSims let readers practice. This book is one: its chapters follow the learning graph, its terms are defined before they are used, and its practice activities are specified as MicroSims. The improved *Watershed Basics* library can be published inside such a book or on its own.

The MicroSim below makes the dependency idea concrete. It shows a piece of this book's graph, and you explore it.

#### Diagram: Learning Graph Explorer

<details markdown="1">
<summary>Learning Graph Explorer</summary>
Type: graph-model
**sim-id:** learning-graph-explorer<br/>
**Library:** vis-network<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine an excerpt of a learning graph and answer five questions about direct and indirect prerequisites and a valid study order, with at least 4 of 5 correct on the first attempt.

**Prerequisites:** Learning Graph, Concept Dependency, Chapter Structure, Intelligent Textbook (all defined in this chapter above this block).

**Evidence of Mastery:** The learner answers five questions about the graph. An answer is correct when it matches the Correct answer column in Content. Mastery is at least 4 of 5 correct on the first attempt. Clicking nodes to highlight prerequisites is exploration, not evidence.

**Misconceptions:** (1) An arrow points from a prerequisite to the concept that needs it. (2) Only direct prerequisites matter. (3) Any order that lists all the concepts is a valid study order.

**Instructional Rationale:** Examining a graph for direct and indirect dependencies is an Analyze-level action. A small graph whose arrows read "needs" lets the learner trace a chain and test a study order.

**Content:**

The graph is an excerpt of this book's learning graph with ten concepts and ten dependencies. Each dependency is written as concept, then the concept it needs:

| Concept | Needs |
|---|---|
| Intelligent Textbook | Chapter Structure |
| Intelligent Textbook | MicroSim |
| Intelligent Textbook | Learning Graph |
| Intelligent Textbook | Glossary |
| Chapter Structure | Learning Graph |
| Chapter Structure | Modular Content |
| Learning Graph | Learning Outcome |
| Learning Graph | Prerequisite Knowledge |
| Glossary | Defined Terms |
| Prerequisite Knowledge | Scope and Sequence |

The reading of an arrow: it points from a concept to the concept it needs.

The five questions:

| # | Question | Choices | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Which concept needs the most other concepts directly? | Learning Graph; Chapter Structure; Intelligent Textbook | Intelligent Textbook | It needs four concepts directly. |
| 2 | Which two concepts does Learning Graph need directly? | Learning Outcome and Prerequisite Knowledge; Glossary and MicroSim; Modular Content and Defined Terms | Learning Outcome and Prerequisite Knowledge | Those are its two outgoing arrows. |
| 3 | Does Chapter Structure need Glossary, directly or through a chain? | Yes; No | No | No chain leads from Chapter Structure to Glossary. |
| 4 | Which concept is the deepest prerequisite of Learning Graph? | Learning Outcome; Prerequisite Knowledge; Scope and Sequence | Scope and Sequence | Learning Graph needs Prerequisite Knowledge, which needs Scope and Sequence. |
| 5 | Which study order respects every dependency? | Scope and Sequence, Prerequisite Knowledge, Learning Outcome, Learning Graph; Learning Graph, Learning Outcome, Prerequisite Knowledge, Scope and Sequence; Prerequisite Knowledge, Scope and Sequence, Learning Outcome, Learning Graph | Scope and Sequence, Prerequisite Knowledge, Learning Outcome, Learning Graph | Each concept comes after everything it needs. |

**Provenance:** The ten concepts and ten dependencies are an excerpt of this book's learning graph, with some of the concepts' other dependencies left out. The sim labels the graph "excerpt of this book's learning graph".

**Rules:** Each question has exactly one correct answer. Arrows are directed from a concept to the concept it needs. The graph has no loops.

**Learner Activity:**

1. The learner explores the graph and may click a node to highlight everything that node needs, directly or through a chain. Clicking is not scored.
2. The learner presses Quiz and answers the five questions.
3. After question 5 the sim shows the summary.

**Feedback:** 5 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can read a learning graph." Below 4 it lists the Why text of each missed question.

**Starting State:** The graph with no node selected and the Quiz button.

**Chapter Anchors:** The chapter says each link points from a concept to the concept it depends on, and that a valid structure puts every prerequisite in the same chapter or an earlier one.
</details>

## Publishing OER

**Publishing OER** is the act of making a resource openly available: placed at a stable public address, under an open license, with complete metadata, so that anyone can find it, use it, copy it, and adapt it within the license. Publishing is different from posting a file. A file on a shared drive may be visible and still not be open, because no one knows the license and no one can find it.

Publishing has eight steps, in this order.

1. **Confirm the license.** Check that the license of the original allows you to publish the improved version, as Chapter 15 taught.
2. **Finish the metadata** for the resource and for each component.
3. **Freeze the tested version.** Save it, label it, and write its release notes.
4. **Package each component** with its README, license, and metadata.
5. **Build the site** from the source files.
6. **Deploy the site** to a host that serves it publicly.
7. **Open the feedback channel and publish the maintenance plan**, so that readers know where to send problems and what to expect.
8. **List the resource in a clearinghouse** and tell colleagues.

Several of these terms are defined in the sections that follow. The first page of a published resource should carry the title, the license with a link, a way to cite it, the version, a link to the source files, and a way to contact the author. A reuser who finds only the page needs all of these without hunting.

### Static Site Generator

A **static site generator** is a program that turns plain source files, usually Markdown and a few settings, into a folder of finished web pages. The pages are fixed files, not built on demand, so they are fast, cheap to host, and easy to copy. That fits open resources well: the source is plain text that anyone can edit and keep in version control, as Chapter 4 explained, and the built pages work on almost any web host. Well-known generators include MkDocs, Jekyll, and Hugo. The flow is short: you write Markdown pages, the generator applies a theme and a menu from a settings file, and it writes HTML, CSS, and script files that any web server can send as they are. There is no database and no program running on the server, which is why the result is cheap to host and hard to break.

### MkDocs

**MkDocs** is a static site generator written in Python and designed for documentation and textbooks. It reads Markdown files and a settings file called `mkdocs.yml`, which holds the site title, the menu, and the theme, and it writes a complete website. This book is built with MkDocs using the Material theme. Two commands cover most of the work.

| Command | What it does |
|---|---|
| `mkdocs build --strict` | Builds the site and stops with an error on a broken link or a page missing from the menu |
| `mkdocs gh-deploy` | Builds the site and pushes the finished pages to a branch that GitHub Pages serves |

The strict option matters because a published resource with a broken internal link fails the accuracy and portability checks that the rubric applies to everyone else's resources.

### GitHub Pages

**GitHub Pages** is a free hosting service of GitHub that serves a static site straight from a repository. After the site is deployed, it appears at an address of the form `https://username.github.io/repository/`, so the *Watershed Basics* library might sit at a site such as `https://example.github.io/watershed-basics/`. The repository that holds the source is public too, which lets anyone read, copy, and propose changes to the files, as Chapter 4's version control allows. GitHub Pages has usage limits and terms that change, so check them for your case.

The two commands in the table are all it takes to publish an update. The first line checks the build, and the second sends it live.

```bash
mkdocs build --strict
mkdocs gh-deploy
```

!!! mascot-tip "Run the Strict Build Before Every Deploy"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    A strict build catches the broken link before your readers do. Make it a habit to run it first, and deploy only when it passes.

### OER Clearinghouse

An **OER clearinghouse** is a catalog that lists open resources from many sources and links to each, so that teachers can search in one place. Two well-known examples are OER Commons and MERLOT, and each has its own submission rules and review process. A listing makes a resource more discoverable, and it does not move the resource: your repository stays the source of truth, and the listing points to it. Good metadata is what makes a listing useful, since the catalog searches the subject, grade level, and description you supply.

The poster below shows the path from source files to a reader and to a listing.

#### Diagram: Publishing Pipeline

<details markdown="1">
<summary>Publishing Pipeline</summary>
Type: infographic
**sim-id:** publishing-pipeline-poster<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the six parts of the publishing pipeline from a description of how each looks, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Publishing OER, Static Site Generator, MkDocs, GitHub Pages, OER Clearinghouse (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 5 of 6 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) The source files and the built site are the same thing. (2) A clearinghouse stores the resource. (3) Deploying and building are the same step.

**Instructional Rationale:** Identifying the parts of a pipeline is a Remember-level task, and a left-to-right picture of the whole path gives each part a place. The quiz asks the learner to recognize a part by its look.

**Content:**

The illustration is a text-free flat drawing read from left to right. At the left is a folder of plain text pages. An arrow leads to a gear. Another arrow leads from the gear to a folder of web pages with a frame around each. Next is a box with a branching line inside it. Beyond it is a globe on a stand. Above the globe, a separate card in a filing drawer points down to the globe with a thin line. The six markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Source files | The folder of plain text pages at the left. | The Markdown pages and settings that you write and edit. | Keep the source in version control. |
| 2 | Build | The gear between the two folders. | A static site generator, like MkDocs, turns the source into web pages. | Run the strict build first. |
| 3 | Built site | The folder of web pages with a frame around each. | The finished pages that a browser can show. | Do not edit these by hand. |
| 4 | Repository | The box with the branching line inside it. | The public home of the files, with their history. | Make the repository public and add the license. |
| 5 | Hosting | The globe on a stand. | A hosting service like GitHub Pages serves the built site at a public address. | Share the stable address. |
| 6 | Clearinghouse listing | The card in the filing drawer with a thin line to the globe. | A catalog entry that points to the published site. | The listing links to your site, and your site stays the source. |

**Provenance:** The six parts follow the chapter sections "Publishing OER", "Static Site Generator", "MkDocs", "GitHub Pages", and "OER Clearinghouse". The illustration is synthetic, and the sim labels it "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 6 from left to right.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 6 hints the sim shows the summary.

**Feedback:** 6 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can follow the path to publication." Below 5 it lists the labels of the missed parts.

**Starting State:** The illustration with six numbered markers, explore mode active, and the prompt "Hover a marker to see a part of the pipeline."

**Chapter Anchors:** The chapter's eight publishing steps and its sections on the generator, MkDocs, GitHub Pages, and the clearinghouse describe these six parts.
</details>

### Release Notes

**Release notes** are a short, readable summary of what changed in each released version. They tell reusers whether to update and what to expect. Group the changes under four headings: *Added*, *Changed*, *Fixed*, and *Removed*. The change log of Chapter 4 and the change log entries of Chapter 15 are the raw material: the release notes are the condensed version for readers who will not read every entry.

Number each release so that people can refer to it. *Watershed Basics v1.1* follows *v1*, and a later correction might be *v1.1.1*.

The MicroSim below practices the grouping. It shows ten changes, and for each one you choose the heading.

#### Diagram: Release Note Sorter

<details markdown="1">
<summary>Release Note Sorter</summary>
Type: microsim
**sim-id:** release-note-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of ten changes under Added, Changed, Fixed, or Removed, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Release Notes (defined in this chapter above this block).

**Evidence of Mastery:** For each change the learner commits one of four headings. A placement is correct when it matches the Correct heading column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the four headings is exploration, not evidence.

**Misconceptions:** (1) Every edit is a fix. (2) A change that improves a feature is an addition. (3) Removing outdated content is not worth mentioning.

**Instructional Rationale:** Classifying changes under headings is an Understand-level action that turns a log into readable notes. Ten changes spread over four headings teach the learner the dividing lines.

**Content:**

The four headings and their meanings: Added (something new), Changed (something that existed now works or reads differently), Fixed (an error or a defect was corrected), Removed (something was taken out).

The ten changes (all made up, for Watershed Basics v1.1):

| # | Change | Correct heading | Why (shown as feedback) |
|---|---|---|---|
| 1 | Added captions to the lesson video. | Added | Captions are new. |
| 2 | Added a simulation of rain and ground cover. | Added | The simulation is new. |
| 3 | Updated the river length from 410 to 398 miles. | Changed | An existing fact now reads differently. |
| 4 | Replaced two broken links. | Fixed | The links were defects. |
| 5 | Split the quiz into its own component. | Changed | An existing part is organized differently. |
| 6 | Corrected the heading that skipped from level 2 to level 4. | Fixed | The heading order was a defect. |
| 7 | Removed the outdated 2019 rainfall chart. | Removed | Something was taken out. |
| 8 | Added a glossary entry for "aquifer". | Added | The entry is new. |
| 9 | Corrected the quiz script path so the quiz loads on tablets. | Fixed | The path was a defect. |
| 10 | Rewrote the introduction at a lower reading level. | Changed | An existing paragraph now reads differently. |

**Provenance:** The changes are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The headings follow the chapter section "Release Notes".

**Rules:** Each change has exactly one correct heading. Added, Changed, and Fixed hold three changes each, and Removed holds one.

**Learner Activity:**

1. The learner sees one change and the four headings.
2. The learner places the change under a heading, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After change 10 the sim shows the summary and the finished release notes.

**Feedback:** 10 changes in a shuffled order, one attempt each. Correct: "Correct: [heading]. [Why]". Incorrect: "Not quite. This change is [heading]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can write release notes." Below 9 it lists the Why text of each missed change.

**Starting State:** The first change in the shuffled order and the four headings. The question shown is "Under which heading does this change belong?"

**Chapter Anchors:** The chapter names the four headings Added, Changed, Fixed, and Removed, and its example release is Watershed Basics v1.1.
</details>

### Maintenance Plan

A **maintenance plan** is a written commitment about how a published resource will be kept in good condition: who is responsible, what is checked, how often, and when the resource will be retired. Without one, a resource drifts out of date, and a reuser cannot tell whether it is still safe to trust. The outdated content and broken links of Chapter 5 are exactly the problems a plan prevents.

| Task | How often | Owner |
|---|---|---|
| Run the link checker | Every three months | The author |
| Check facts that can change, such as figures and dates | Once a year | The author |
| Run the accessibility scan | Once a year and after any large change | The author |
| Review open issues and decide what goes in the next release | Every release | The author |
| Decide whether to retire the resource and post a notice | Once a year | The author |

Retiring is part of maintaining. A resource that nobody can keep accurate is better marked as archived, with a note on its first page, than left to mislead.

### Issue Tracking

**Issue tracking** is the practice of recording every reported problem or request in one list, with a status, so that none is lost and each is decided. GitHub provides this with Issues, attached to the repository. Each issue has a title, a description, a label such as *bug*, *content error*, *accessibility*, or *request*, and a status of open or closed. The list tells you what to fix, what to schedule, and what to decline, and the closed issues form a record of how the resource improved.

The MicroSim below practices the decision. It shows eight reports, and for each one you decide what to do.

#### Diagram: Issue Triage Sorter

<details markdown="1">
<summary>Issue Triage Sorter</summary>
Type: microsim
**sim-id:** issue-triage-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** prioritize<br/>
**Learning Objective:** The learner will prioritize eight incoming reports by sorting each into Fix in the next patch, Schedule for a later release, Answer and close, or Decline politely, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Issue Tracking, Maintenance Plan, Release Notes, Accept Correct or Reject (all defined in this chapter above this block or in Chapter 14).

**Evidence of Mastery:** For each report the learner commits one of four decisions. A placement is correct when it matches the Correct decision column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the four decisions is exploration, not evidence.

**Misconceptions:** (1) Every request must be done. (2) A reader can ask the author to remove a required credit. (3) A question needs a code change.

**Instructional Rationale:** Prioritizing incoming reports is an Evaluate-level action that maintainers repeat. Reports that range from an urgent defect to a request that conflicts with the license teach the learner to match the response to the kind of report.

**Content:**

The four decisions and their meanings: Fix in the next patch (a defect that harms accuracy, access, or function, to be verified and corrected soon), Schedule for a later release (a worthwhile improvement), Answer and close (a question that the documentation or license already answers), Decline politely (a request that conflicts with the license, the purpose, or the evidence).

The eight reports (all made up, for Watershed Basics v1.1):

| # | Report | Correct decision | Why (shown as feedback) |
|---|---|---|---|
| 1 | The quiz does not load on my school's tablets. | Fix in the next patch | It stops learners from using the quiz. |
| 2 | Section 2 says the river is 398 miles but my atlas says 392. | Fix in the next patch | An accuracy report should be verified at the source and corrected if right. |
| 3 | Can I use this in my paid online course? | Answer and close | CC BY 4.0 allows it with credit. |
| 4 | Please add a Spanish version. | Schedule for a later release | It is a worthwhile improvement and a larger piece of work. |
| 5 | Please remove the credit line; it looks cluttered. | Decline politely | The license requires credit. |
| 6 | The captions say "a quiver" where the video says "aquifer". | Fix in the next patch | A caption error changes meaning. |
| 7 | How do I embed the simulation in my learning platform? | Answer and close | The README explains embedding. |
| 8 | Please add a section on desert watersheds. | Schedule for a later release | It is a worthwhile addition for a later release. |

**Provenance:** The reports are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The decisions follow the chapter sections "Issue Tracking" and "Maintenance Plan".

**Rules:** Each report has exactly one correct decision. Three are Fix in the next patch, two are Schedule for a later release, two are Answer and close, and one is Decline politely.

**Learner Activity:**

1. The learner sees one report and the four decisions.
2. The learner places the report under a decision, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After report 8 the sim shows the summary.

**Feedback:** 8 reports in a shuffled order, one attempt each. Correct: "Correct: [decision]. [Why]". Incorrect: "Not quite. The decision is [decision]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can triage reports." Below 7 it lists the Why text of each missed report.

**Starting State:** The first report in the shuffled order and the four decisions. The question shown is "What should the maintainer do with this report?"

**Chapter Anchors:** The chapter says an issue list tells the maintainer what to fix, what to schedule, and what to decline. The sim adds a category for questions that the documentation already answers.
</details>

### Feedback Channel

A **feedback channel** is the way readers tell you about problems and ideas. Provide at least one that is easy to find, put the link on every page, and say what response to expect. Good options are the repository's issue tracker for people who use GitHub, and a plain email address or a short form for those who do not. Offer more than one, since a channel that needs an account excludes teachers who have none. Ask only for what you need, never for student information, and say how long you take to reply. A channel that is promised and then ignored is worse than none.

!!! mascot-warning "Never Ask for Student Information in a Feedback Form"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A teacher or a student may mention a name or a score in a message. Tell people not to, and delete any that arrive.

### Community Contribution

A **community contribution** is a change that someone else proposes to your resource. On GitHub this is a pull request: the contributor copies the repository, makes a change, and asks you to adopt it. Contributions are one of the great benefits of open resources, since readers fix errors, translate, and adapt for new settings. They also carry risk, so apply the same review as your own agent's changes. Check that the change keeps the meaning or is a labeled correction, that it carries a compatible license, that third-party material is credited, and that it does not collect personal data. A short contribution guide on your site, saying that contributors agree to share under the same license, keeps the exchange clear. Credit contributors in the release notes.

The MicroSim below practices the review. It shows eight proposed contributions, and for each one you decide what to do.

#### Diagram: Contribution Checker

<details markdown="1">
<summary>Contribution Checker</summary>
Type: microsim
**sim-id:** contribution-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight proposed contributions should be accepted, sent back for changes, or declined, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Community Contribution, Preserving Original Meaning, Human Review of Changes, Component Licensing (defined in this chapter above this block or in Chapter 15).

**Evidence of Mastery:** For each contribution the learner commits one of three decisions. A decision is correct when it matches the Correct decision column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the review checks is exploration, not evidence.

**Misconceptions:** (1) Any free contribution should be accepted. (2) A contribution that is almost right is declined. (3) A contributor can keep all rights in a change to an open resource.

**Instructional Rationale:** Judging a contribution against the review checks is an Evaluate-level action. Contributions that are sound, need a fix, or cannot be accepted teach the learner to check meaning, license, credit, and privacy.

**Content:**

The three decisions: Accept, Ask for changes first, Decline.

The review checks, available on demand: the meaning is kept or the change is a labeled correction; the license is compatible; third-party material is credited; no personal data is collected.

The eight contributions (all made up, for Watershed Basics v1.1):

| # | Proposed contribution | Correct decision | Why (shown as feedback) |
|---|---|---|---|
| 1 | Fixes a typo in section 3. | Accept | It is a small correction that keeps the meaning. |
| 2 | Adds a Spanish translation, credits the original, uses CC BY 4.0, and includes a note from a bilingual teacher who checked it. | Accept | The meaning is checked and the license and credit are right. |
| 3 | Replaces a figure with an image copied from a website, with no license information. | Ask for changes first | The contributor must show the license or use another image. |
| 4 | Changes "about 6,000" to "more than 6,000" with no source. | Ask for changes first | It changes the meaning, so it needs a source. |
| 5 | Adds tracking code that sends each student's name to an outside service. | Decline | It collects personal student data. |
| 6 | Rewrites the quiz and removes all the explanations to make it shorter. | Decline | It removes a feature the test found helpful. |
| 7 | Offers a change that the contributor says is "all rights reserved". | Decline | It is not compatible with the resource's open license. |
| 8 | Adds alt text to two images that had none, checked against the images. | Accept | It improves access and keeps the meaning. |

**Provenance:** The contributions are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The checks follow the chapter section "Community Contribution" and Chapter 15.

**Rules:** Each contribution has exactly one correct decision. Three are Accept, two are Ask for changes first, and three are Decline.

**Learner Activity:**

1. The learner sees one contribution and the three decisions, and may open the review checks. Opening them does not change the score.
2. The learner places the contribution under a decision, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After contribution 8 the sim shows the summary.

**Feedback:** 8 contributions in a shuffled order, one attempt each. Correct: "Correct: [decision]. [Why]". Incorrect: "Not quite. The decision is [decision]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can review a contribution." Below 7 it lists the Why text of each missed contribution.

**Starting State:** The first contribution in the shuffled order and the three decisions. The question shown is "Should this be adopted?"

**Chapter Anchors:** The chapter lists four review checks for a contribution: meaning, license, credit, and personal data.
</details>

The MicroSim below ties the publishing steps together. It gives eight steps in a scrambled order, and you put them in sequence.

#### Diagram: Publishing Steps Sorter

<details markdown="1">
<summary>Publishing Steps Sorter</summary>
Type: microsim
**sim-id:** publishing-steps-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the publishing workflow by placing eight steps in the correct order, with at least 7 of 8 steps in the correct position on the first commit.

**Prerequisites:** Publishing OER, Component Packaging, Static Site Generator, GitHub Pages, OER Clearinghouse, Release Notes, Maintenance Plan, Feedback Channel (all defined in this chapter above this block).

**Evidence of Mastery:** The learner arranges the eight steps and commits the order once. A step is correct when it is in its position in the Content table. Mastery is at least 7 of 8 steps in the correct position on the first commit. Rearranging before the commit is exploration, not evidence.

**Misconceptions:** (1) Listing in a clearinghouse comes first because it brings visitors. (2) The license check can wait until the site is built. (3) The feedback channel can open after the announcement.

**Instructional Rationale:** Ordering the steps of a workflow is an Apply-level action that tests whether the learner understands why each step comes where it does. Dependencies between steps, like license before building and feedback before announcing, make the order matter.

**Content:**

The eight steps in their correct order:

| Position | Step | Why it comes here (shown as feedback) |
|---|---|---|
| 1 | Confirm that the license allows publishing the improved version | Nothing else matters if the license forbids it. |
| 2 | Finish the metadata for the resource and each component | The build and the listing use it. |
| 3 | Freeze the tested version, tag it, and write its release notes | The released version must not change after testing. |
| 4 | Package each component | Packages are built from the frozen version. |
| 5 | Build the site with the static site generator | The build uses the packages and the metadata. |
| 6 | Deploy the site to the host | Only a built site can be deployed. |
| 7 | Open the feedback channel and publish the maintenance plan | Readers need a way to report problems before they arrive. |
| 8 | List the resource in a clearinghouse and announce it | Announce only when everything else is ready. |

**Provenance:** The order follows the chapter section "Publishing OER". The steps are labeled "recommended order" in the sim.

**Rules:** The sim presents the eight steps in a shuffled order and the learner arranges them. Each position has exactly one correct step.

**Learner Activity:**

1. The learner sees the eight steps in a scrambled order.
2. The learner drags the steps into the order they think is right, and may rearrange them freely.
3. The learner presses Commit.
4. The sim marks each step correct or misplaced, and shows the Why text for the misplaced ones.

**Feedback:** One commit counts as evidence. The sim shows "[n] of 8 steps in the correct position". At 7 or more it adds "You can plan a release." Below 7 it lists the correct order with the Why text of each misplaced step.

**Starting State:** The eight steps in a shuffled order and the Commit button.

**Chapter Anchors:** The chapter's eight numbered publishing steps are the order used in this sim.
</details>

## Reuse Tracking

**Reuse tracking** is the effort to learn who is using your resource, and how. An open license lets people reuse without asking or telling you, so you will see only part of the picture. Several signals help, and they differ in strength.

- **Strong:** a course page that links to your component and credits you, a copy (a *fork*) of your repository with changes, and a message from a teacher who describes using it.
- **Weak:** downloads, page views, and a star on your repository show interest and not use.
- **Not evidence:** your own visits, and automated crawlers that load pages without a reader.

Search for the title of your resource and the text of your attribution line, since a reuser who followed the license will have written them. Keep a simple table of reuses you learn about, with the date, who, and how. Respect privacy: track the reuse of the resource, not the identity of students.

The MicroSim below practices judging signals.

#### Diagram: Reuse Evidence Sorter

<details markdown="1">
<summary>Reuse Evidence Sorter</summary>
Type: microsim
**sim-id:** reuse-evidence-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** assess<br/>
**Learning Objective:** The learner will assess eight signals as strong evidence of reuse, weak evidence, or not evidence of reuse, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Reuse Tracking, Derivative Work, Component Licensing (defined in this chapter above this block or in Chapter 15).

**Evidence of Mastery:** For each signal the learner commits one of three bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the three strengths is exploration, not evidence.

**Misconceptions:** (1) Page views measure reuse. (2) A star on a repository is a use. (3) All visits come from readers.

**Instructional Rationale:** Assessing the strength of evidence is an Evaluate-level action. Signals that show use, interest, and nothing at all teach the learner not to count every number as impact.

**Content:**

The three bins: Strong evidence of reuse, Weak evidence, Not evidence of reuse.

The eight signals (all made up, for Watershed Basics v1.1):

| # | Signal | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | A teacher's course page embeds your simulation and credits you. | Strong evidence of reuse | Someone is using it and has credited it. |
| 2 | Someone copied your repository and changed the quiz. | Strong evidence of reuse | A copy with changes is an adaptation. |
| 3 | An email says, "I used your reading with my class and added two questions." | Strong evidence of reuse | A user describes using and adapting it. |
| 4 | The clearinghouse listing shows 300 downloads. | Weak evidence | A download shows interest and not use. |
| 5 | The site had 1,200 page views last month. | Weak evidence | A view shows a visit and not reuse. |
| 6 | Three people starred your repository. | Weak evidence | A star shows interest. |
| 7 | Your own computer opened the site 40 times while you tested it. | Not evidence of reuse | The visits are yours. |
| 8 | Traffic spiked when automated crawlers scanned the site. | Not evidence of reuse | No reader was involved. |

**Provenance:** The signals are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The strengths follow the chapter section "Reuse Tracking".

**Rules:** Each signal has exactly one correct bin. Three signals are Strong evidence of reuse, three are Weak evidence, and two are Not evidence of reuse.

**Learner Activity:**

1. The learner sees one signal and the three bins.
2. The learner places the signal in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After signal 8 the sim shows the summary.

**Feedback:** 8 signals in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can weigh signs of reuse." Below 7 it lists the Why text of each missed signal.

**Starting State:** The first signal in the shuffled order and the three bins. The question shown is "Does this show that someone reused the resource?"

**Chapter Anchors:** The chapter lists strong signals, weak signals, and non-evidence.
</details>

### Usage Analytics

**Usage analytics** are counts of how a site is used: visits, pages viewed, where visitors come from, and which components are opened most. They show reach and patterns, and they help plan: a component that no one opens may need to be easier to find. Choose a tool that records counts and not individuals, and tell visitors what you collect. For a site used by students, do not collect personal data, as Chapter 16 advised.

Analytics also mislead easily. A page view is not a reader, a reader is not a learner, and a drop in visits in the school holidays reflects the calendar and not the quality of the resource. Always read the counts alongside the calendar and next to the learning evidence of Chapter 17.

The chart below shows six months of page views for the three components, with each month's total. Use it to practice reading analytics with care.

#### Diagram: Usage Analytics Reader

<details markdown="1">
<summary>Usage Analytics Reader</summary>
Type: chart
**sim-id:** usage-analytics-reader<br/>
**Library:** Chart.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine a chart of monthly page views for three components and answer five questions about totals, trends, and what the counts do and do not show, with at least 4 of 5 correct on the first attempt.

**Prerequisites:** Usage Analytics, Reuse Tracking (defined in this chapter above this block).

**Evidence of Mastery:** The learner answers five questions about the chart. An answer is correct when it matches the Correct answer column in Content. Mastery is at least 4 of 5 correct on the first attempt. Hovering over bars and toggling a component are exploration, not evidence.

**Misconceptions:** (1) Page views show that students learned. (2) A drop in views means the resource got worse. (3) The most viewed component is the best one.

**Instructional Rationale:** Examining a chart with a calendar effect is an Analyze-level action. A chart with a holiday dip and one dominant component teaches the learner to separate the pattern from its causes.

**Content:**

The data, shown as a grouped bar chart with months on the horizontal axis and page views on the vertical axis (made up, for the Watershed Basics components over six school months):

| Month | Reading | Quiz | Simulation | Month total |
|---|---|---|---|---|
| September | 180 | 120 | 60 | 360 |
| October | 420 | 300 | 210 | 930 |
| November | 380 | 290 | 270 | 940 |
| December | 150 | 100 | 90 | 340 |
| January | 90 | 60 | 40 | 190 |
| February | 310 | 240 | 190 | 740 |
| Six-month total | 1,530 | 1,110 | 860 | 3,500 |

The five questions:

| # | Question | Choices | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Which component had the most page views over the six months? | Reading; Quiz; Simulation | Reading | It had 1,530 views. |
| 2 | Which month had the highest total? | October; November; February | November | Its total is 940. |
| 3 | What most likely explains the low December and January totals? | The resource got worse; The school calendar; A broken link | The school calendar | Holidays reduce visits for every component. |
| 4 | Do these page views show that students learned? | Yes; No | No | A view is not a reader, and a reader is not a learner. |
| 5 | What share of all views went to the simulation, to the nearest percent? | 25 percent; 33 percent; 45 percent | 25 percent | 860 divided by 3,500 is about 24.6 percent, which rounds to 25. |

**Provenance:** The page views are illustrative examples made up for this chapter, and the sim labels them "illustrative data".

**Rules:** Month totals and the six-month totals are the sums of the values shown. Percentages are rounded to the nearest whole percent.

**Learner Activity:**

1. The learner hovers over bars to see exact values, and may toggle a component on or off. Toggling is not scored.
2. The learner presses Quiz and answers the five questions.
3. After question 5 the sim shows the summary.

**Feedback:** 5 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can read analytics with care." Below 4 it lists the Why text of each missed question.

**Starting State:** The chart with all three components shown and the Quiz button.

**Chapter Anchors:** The chapter says a page view is not a reader, a reader is not a learner, and holiday drops reflect the calendar.
</details>

### Impact Reporting

**Impact reporting** is the honest account, to the people who care, of what a published resource has done. It draws on four kinds of evidence from this book: the *reach* from usage analytics, the *reuse* from reuse tracking, the *learning* from the A/B test of Chapters 16 and 17, and the *experience* from surveys, comments, and the issue list. A good report keeps the kinds apart, says how strong each is, and does not claim learning on the strength of page views.

A short report has the same bones as the results summary of Chapter 17: a question, the evidence, the limits, and the decision. For *Watershed Basics v1.1* it might say that the library was viewed about 3,500 times in six months, was reused by at least three teachers, produced a learning gain of 22.0 points against 15.0 for the original in a pilot of 24 students, and received 11 issues, of which 7 were fixed. The report would add that the pilot was small, that page views do not measure learning, and that a larger test is planned.

The MicroSim below practices the key skill, which is matching each question to the evidence that can answer it.

#### Diagram: Impact Evidence Matcher

<details markdown="1">
<summary>Impact Evidence Matcher</summary>
Type: microsim
**sim-id:** impact-evidence-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of eight impact questions under the source of evidence that can answer it, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Impact Reporting, Usage Analytics, Reuse Tracking, Issue Tracking, Feedback Channel (all defined in this chapter above this block), and the A/B test of Chapter 16.

**Evidence of Mastery:** For each question the learner commits one of five sources. A placement is correct when it matches the Correct source column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the source descriptions is exploration, not evidence.

**Misconceptions:** (1) Page views can answer a question about learning. (2) One source answers every question. (3) The issue list only records complaints.

**Instructional Rationale:** Matching a question to its evidence source is an Understand-level action that stops a report from answering a question with the wrong data. Eight questions across five sources teach the learner what each source can and cannot say.

**Content:**

The five sources: Usage analytics, Reuse tracking, A/B test, Survey and feedback, Issue tracker.

The eight questions (all about Watershed Basics v1.1):

| # | Question | Correct source | Why (shown as feedback) |
|---|---|---|---|
| 1 | How many people visited the quiz page last month? | Usage analytics | Visits are counted by analytics. |
| 2 | Did another teacher adapt the simulation for their class? | Reuse tracking | Adaptation is a sign of reuse. |
| 3 | Did students who used the improved version learn more? | A/B test | Only a comparison of groups can answer it. |
| 4 | What do students say about the captions? | Survey and feedback | It asks for opinions in students' own words. |
| 5 | How many accuracy errors were reported and fixed this year? | Issue tracker | Reports and their status are recorded there. |
| 6 | Which component is opened most? | Usage analytics | Page views by component come from analytics. |
| 7 | Which other course sites link to the reading? | Reuse tracking | Links with credit are a sign of reuse. |
| 8 | By how much did mean learning gain differ between the versions? | A/B test | The difference of means comes from the test. |

**Provenance:** The questions are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The sources follow the chapter sections "Usage Analytics", "Reuse Tracking", "Issue Tracking", and "Impact Reporting" and Chapters 16 and 17.

**Rules:** Each question has exactly one correct source. Usage analytics, Reuse tracking, and A/B test hold two questions each. Survey and feedback and Issue tracker hold one each.

**Learner Activity:**

1. The learner sees one question and the five sources, and may open the source descriptions. Opening them does not change the score.
2. The learner places the question under a source, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After question 8 the sim shows the summary.

**Feedback:** 8 questions in a shuffled order, one attempt each. Correct: "Correct: [source]. [Why]". Incorrect: "Not quite. This question is answered by [source]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can match a question to its evidence." Below 7 it lists the Why text of each missed question.

**Starting State:** The first question in the shuffled order and the five sources. The question shown is "Which source can answer this?"

**Chapter Anchors:** The chapter names four kinds of evidence for an impact report: reach, reuse, learning, and experience.
</details>

---

## Key Takeaways

- A **reusable component** stands alone, embeds without edits, and carries its own license and metadata. **Component packaging** gathers its content, README, license file, and metadata in one folder with links that stay inside it.
- **Component licensing** keeps each component's terms with it, and **component discoverability** depends on a clear name, complete metadata, and a listing. A **component library** organizes components with a catalog.
- A **learning graph** links each concept to the concepts it needs, and a **concept dependency** reads as "needs". A **chapter structure** puts every prerequisite in the same chapter or an earlier one, and an **intelligent textbook** is built on that structure.
- **Publishing OER** puts a resource at a stable public address under an open license with complete metadata. Confirm the license, finish the metadata, freeze the tested version, package, build, deploy, open the feedback channel, then list and announce.
- A **static site generator** such as **MkDocs** turns Markdown into pages, and **GitHub Pages** hosts them. Run `mkdocs build --strict` before `mkdocs gh-deploy`. An **OER clearinghouse** lists your resource and points to your site.
- **Release notes** group changes as added, changed, fixed, and removed. A **maintenance plan** says who checks what and when. **Issue tracking** records each report and decision, a **feedback channel** invites reports, and a **community contribution** gets the same review as any change.
- **Reuse tracking** weighs strong signals above weak ones, and **usage analytics** show reach and not learning. **Impact reporting** keeps reach, reuse, learning, and experience apart and claims no more than the evidence shows.

!!! mascot-celebration "You Can Share What You Built"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now package a component, publish it with MkDocs and GitHub Pages, keep it healthy, and report honestly on what it does. The last chapter turns to the people: how to train and certify the reviewers who keep the whole loop running.
