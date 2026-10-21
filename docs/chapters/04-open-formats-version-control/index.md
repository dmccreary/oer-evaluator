---
title: "Open File Formats and Version Control"
description: "Explains the editable source metric, source and open file formats, Markdown, HTML, version control, Git, GitHub, forks, pull requests, and changelogs."
generated_by: claude skill chapter-content-generator
date: "2026-10-20 20:38:05"
version: 1.11
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

!!! mascot-welcome "Can You Actually Change It?"
    ![Echo the Loon waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    An open license promises you the right to revise a resource, but the file you receive decides whether you really can. In this chapter you'll learn to tell an editable source from a locked file and to read the history of a resource's changes. Let's dive in and check the evidence!

Chapter 3 gave you ten metrics, and this chapter takes the one that checks whether a resource can be revised in practice. The Revise and Remix permissions from Chapter 1 mean little if the only copy you can get is a locked file. Sam hit this when adopting the open chapter on cell structure: the license said Sam could rewrite the examples, but the first download was a PDF. The chapter covers file formats, two formats worth knowing, Markdown and HTML, and the tools that track changes, Git and GitHub.

## The Editable Source Metric

The **editable source metric** is the rubric metric that asks whether a resource's source can be edited in an open format. It is metric 9 of the ten, and it protects the Revise and Remix permissions. A resource can carry the friendliest license in the world and still score poorly here, because the permission to revise is worth little without a file that you can revise.

Scores follow descriptors, as Chapter 3 explained. The descriptors below are illustrative and give the shape of the metric.

| Score range | Editable Source descriptor |
|-------------|----------------------------|
| 9 to 10 | All source files, including image sources, are in open, editable formats and come with a version history |
| 5 to 6 | The source is editable but tied to specific software, or no history is kept |
| 1 to 3 | Only locked formats, such as a PDF, are available |
| 0 | No downloadable version exists |

Sam's open chapter shows how a real score arises. The page offers three versions: a web page, a PDF, and a link to the chapter's Markdown source files in a public repository with its full change history. That is strong evidence. But the diagrams in the repository are only exported pictures, with no original drawing files, so Sam cannot change a label inside a diagram without redrawing it. That gap is why Sam scored the metric 8 and not 10. The evidence citations for the score read:

| Where | What | How checked |
|-------|------|-------------|
| Chapter page, download links | Web page, PDF, and a link to the source repository | Read the page on the review date |
| Repository, folder "chapter" | Text is in Markdown files, with history | Opened the repository |
| Repository, folder "images" | Diagrams are exported images only; no original drawing files | Listed the folder contents |

## Source Formats and Open File Formats

A **source format** is the file format in which a resource is created and edited, and from which other versions are produced. It is different from an output format, the finished version made for readers. Picture a recipe and a meal: the source is the recipe, and the outputs are the dishes you can make from it. If you have the recipe, you can make a new dish or change the seasoning. If you have only a dish, you can eat it but you cannot reliably work backward.

Sam's chapter makes the difference concrete. The table lists four forms of the same chapter and says which is the source.

| Form of the chapter | Source or output? | What you can do with it |
|---------------------|-------------------|--------------------------|
| Markdown files in the repository | Source | Edit the text, then regenerate the other forms |
| The web page | Output | Read it, link to it, copy small parts |
| The PDF | Output | Read and print it; changing it is hard and lossy |
| Exported diagram images | Output | View them; labels cannot be edited |

Images follow the same rule. A diagram exported as a PNG picture is an output: its labels are only colored dots on the screen. The same diagram saved as an SVG file is a source, because the labels are real text that Sam could change, for example into another language. When you evaluate a resource, ask for the source of its images as well as its text.

An **open file format** is a format whose specification is published and can be used by anyone without payment or permission. Plain text, Markdown, HTML, OpenDocument (.odt), EPUB, and SVG for drawings are open formats. A format being open matters because anyone can write software that reads it, so the file will still open in the future and on any platform. Two properties are easy to confuse. Open means the format is documented for everyone. Editable means a person can change the content with reasonable effort. The two do not always go together. PDF is a published standard, so it is open, but it is hard to edit, because it describes how a page looks and not how the text is structured. Chapters 5 to 10 use the combination: a good source is open and editable.

| Format | Open? | Editable? | Note |
|--------|-------|-----------|------|
| Plain text (.txt) | Yes | Yes | Simple but has no formatting |
| Markdown (.md) | Yes | Yes | Plain text with simple formatting marks |
| HTML (.html) | Yes | Yes | The format of web pages |
| OpenDocument text (.odt) | Yes | Yes | Word-processor format, open specification |
| EPUB (.epub) | Yes | With effort | A packaged e-book built from HTML |
| SVG (.svg) | Yes | Yes | Drawings that can be edited as text or in a drawing program |
| Word (.docx) | Published standard | Yes, in compatible software | Layout can shift outside the software that made it |
| PDF (.pdf) | Published standard | Rarely | Designed for fixed pages, not for editing |

A quick practical test helps when a format is unfamiliar. Try to open the file in three places: a plain text editor, a free word processor, and a web browser. If any of them shows the content and lets you change it, the format is probably editable. If none can, or if the content appears as strings of symbols, you are likely looking at a locked or specialized format. Sam used this test on a worksheet that arrived with an unfamiliar file ending and found that it opened as readable text in a plain text editor, which showed that it was an editable source.

!!! mascot-thinking "Source Is the Recipe, Output Is the Meal"
    ![Echo the Loon thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    When you can get the source, you can make any output you need. When you can get only an output, you are stuck with someone else's choices. Always ask whether the recipe is available.

Two common ways of sharing deserve their own names. A **word processing file** is a document made with word-processing software, such as a .docx or .odt file. It is editable by many people, which makes it practical for teachers, who already know the tools. Its weakness is that a layout can shift when the file is opened in other software, and a .docx depends on programs that support it. A resource offered as an editable word processing file scores higher on this metric than one offered only as a PDF, and one offered as .odt scores higher still, because the format is open.

**PDF-only distribution** is the practice of offering a resource only as a PDF. PDF is good at what it was designed for: a page looks the same on every screen and prints the same on every printer. But it is a poor source. Copying text out of a PDF can lose headings and lists, the images are fixed, and a PDF that is only a scan of paper has no editable text at all. A resource with PDF-only distribution usually lands in the 1 to 3 range. The remedy is cheap: publish the source beside the PDF.

!!! mascot-warning "A PDF Is Open but Rarely Editable"
    ![Echo the Loon warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    PDF follows a public standard, so it can look "open," yet you still can't revise it comfortably. When a resource offers only a PDF, look for a source link or a repository, and if you find neither, ask the creator for the source files.

## Markdown and HTML

Two formats show up constantly in open resources, and a teacher does not need to master either to benefit from knowing what they are.

**Markdown** is a lightweight format for text, written in a plain text file with a few simple marks that say how it should look. The marks are easy to read even before they are converted. Before the example, here are the marks it uses: a line that starts with `#` is a heading, with more `#` signs for smaller headings. A line that starts with `-` is a bullet point. Text between two asterisks, as in `*cell wall*`, is shown in italics, and text in square brackets followed by an address in parentheses is a link.

```markdown
## The Cell Membrane

The *cell membrane* controls what enters and leaves the cell.

- It is made mostly of lipids and proteins.
- It is selectively permeable.

[Read more about membranes](https://example.org/membranes)
```

A tool turns that file into a web page, a PDF, or a slide deck, with a heading, a sentence with italic words, two bullets, and a link. Markdown works well for OER because any text editor can open it, the text is easy to compare between versions, and one source can produce many outputs. This book itself is written in Markdown. Sam could correct the mitochondria error by changing one line in a Markdown file, and the change would be easy to see.

Teachers who already have material in a word processor do not have to retype it. A free converter such as Pandoc can turn a Word or OpenDocument file into Markdown. Sam converted a one-page handout this way and then read the result to check for lost formatting, because tables sometimes have to be rebuilt by hand.

**HTML**, short for HyperText Markup Language, is the language of web pages. It uses tags in angle brackets that wrap content and say what it is. A tag named `h2` marks a heading, `p` marks a paragraph, and `img` places an image. A tag can carry extra information. The `alt` attribute on an image holds a short text description for people who cannot see the picture, which Chapter 7 covers in detail. Read the example with those parts in mind.

```html
<h2>The Cell Membrane</h2>
<p>The cell membrane controls what enters and leaves the cell.</p>
<img src="membrane.png" alt="Diagram of a cell membrane with proteins crossing a double layer of lipids">
```

HTML is both an output and a source. A web page is the output a reader sees, and the HTML behind it is a source that can be edited in any text editor. Because it is open and editable, HTML scores well on this metric. It is also the foundation for several later chapters: accessibility checks, embedding a resource in another page, and machine-readable descriptions all work through HTML.

You can see the HTML behind any web page yourself. In most browsers, right-clicking the page and choosing the option to view the page source opens it. That is how a reviewer checks whether an image has alt text, the check Sam made in Chapter 3. Reading HTML is much easier than writing it, and a reviewer needs only to recognize a few tags.

## Version Control, Git, and GitHub

A resource that is improved over time raises a question: how do you keep track of what changed? **Version control** is a system that records every change made to a set of files so that you can see earlier versions, compare them, undo mistakes, and learn who changed what and why. It is "track changes" for a whole folder of files, with a permanent history.

Sam's chapter might have three saved versions over a year. The table shows how a history makes the story clear.

| Version | Who | When | What changed |
|---------|-----|------|--------------|
| 1 | Ana Rivera | January | The original chapter |
| 2 | Sam | March | Replaced three examples with a local pond |
| 3 | Sam | April | Added a Spanish vocabulary list |

Without version control, Sam would have three files named something like "chapter-final," "chapter-final-2," and "chapter-final-really." With it, every version is kept under one name, and a reviewer can ask what changed between versions 1 and 3.

Version control gives four practical benefits:

- **Undo:** a mistake can be reversed by returning to an earlier version.
- **Comparison:** you can see exactly which lines changed between two versions.
- **Collaboration:** several people can work on the same files without overwriting each other.
- **Credit:** each change is tied to a person and a date, which supports the attribution you learned about in Chapter 2.

**Git** is the most widely used version control software. It runs on your own computer and keeps a **repository**, a project folder together with its complete history. Each time you save a snapshot of your work, Git records a **commit**, which is a saved version with a short message describing the change. Before the example, here is what the four commands do. `git clone` copies a repository from the web to your computer. `git add` chooses which changed files go in the next snapshot. `git commit` saves the snapshot with a message, and `git log` lists the history.

```bash
git clone https://example.org/open-biology.git
git add chapter/cell-structure.md
git commit -m "Replace three examples with a local pond"
git log --oneline
```

The last command prints one line for each commit, so Sam would see a list like the table above, with the newest commit at the top. You do not need to type commands to benefit from Git. Many teachers use only the website described next, which shows the same history in a browser.

Two habits make a history useful. Each commit message should say what changed and, when it is not obvious, why. "Correct the statement about mitochondria" tells the next reader what happened, while "fixed stuff" tells them nothing. And because everyone who copies a repository receives the whole history, Git keeps working without an internet connection, and the record of changes is hard to lose.

!!! mascot-encourage "Git Feels Strange at First"
    ![Echo the Loon encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If Git's vocabulary feels like another language, that's normal, because it is a tool built for programmers. You've already used the idea when you saved a draft and a final copy, and you can start by just reading a repository's history in your browser.

A **GitHub repository** is a Git repository stored on GitHub, a website that hosts repositories and adds tools for viewing and discussing them. Git and GitHub are not the same thing: Git is the software that tracks changes, and GitHub is one place where repositories live. Many open resources, including this book, are published in GitHub repositories, which makes it a natural place to look for editable sources.

A repository page shows several things at a glance. The table lists what to look for when Sam opens the repository of the open chapter.

| Item | What it tells you |
|------|-------------------|
| README file | What the resource is, and how to use it |
| LICENSE file | The license, in full, which should match the page |
| Folders such as "chapter" and "images" | Where the source files are, and whether image sources are included |
| Date of the latest commit | Whether the resource is maintained, which supports the currency check in Chapter 5 |
| Commit history | Who has changed the resource, when, and why |
| Issues list | Problems that other users have reported |

Suppose Sam opens the chapter's repository and finds that the latest commit is three years old and that several issues about errors are still open. That is a currency finding, not a reason to reject the chapter, but it tells Sam that the resource is probably not being maintained, so any errors will have to be fixed by Sam or another adopter. The same page also shows how to reach the creators, which Sam will need if a pull request is to be accepted.

## Fork, Pull Request, and Changelog

A reviewer who improves an open resource wants to share the improvement. Two features of GitHub make that routine. A **fork** is a personal copy of someone else's repository, kept on GitHub and linked to the original. Because it is yours, you can change it freely without touching the original. A fork is the practical form of the Revise permission: it lets Sam work on a corrected chapter while the original stays as the creators published it. The license still applies, so a fork carries the credit and any ShareAlike conditions from Chapter 2.

A **pull request** is a request to the owner of the original repository to include your changes. It shows exactly what you changed, lets the owner discuss it with you, and lets the owner accept it, which is called merging, or decline it. When Sam finds the mitochondria error, Sam can fork the repository, correct the line, and open a pull request saying why. If the owners agree, every teacher who uses the chapter gets the fix.

The steps are easier to see in order. The step-through below shows which copy changes at each stage, and it asks you to predict before the answer is shown.

#### Diagram: Fork and Pull Request Step-Through

<details markdown="1">
<summary>Fork and Pull Request Step-Through</summary>
Type: microsim
**sim-id:** fork-pull-request-step-through<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Template:** https://github.com/dmccreary/information-systems/tree/main/docs/sims/git-feature-branch-workflow<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** infer<br/>
**Learning Objective:** The learner will infer which of three copies of a resource changes at each of the 6 steps of a fork-and-pull-request workflow.

**Prerequisites:** version control, Git, GitHub repository, commit, fork, pull request (all defined in the chapter above this block).

**Evidence of Mastery:** At each of the 6 steps, the learner predicts which copy's files change, choosing one of four options, and presses Check before the sim reveals the result. A prediction is correct when it matches the Correct answer column in Content. Mastery is 5 or more of 6 correct on the first attempt. Stepping through after the answer is shown is exploration and does not count as evidence.

**Misconceptions:** (1) Forking changes the original repository. (2) Opening a pull request changes the original's files immediately. (3) Saving a commit on your computer changes your fork on GitHub. (4) Copying a repository to your computer changes the fork.

**Instructional Rationale:** Understanding a workflow means being able to say what each step does to each part. Asking the learner to predict before the result is revealed makes the learner use the definitions of fork, commit, and pull request instead of only watching the steps.

**Content:**

The three copies are: the original repository (owned by the chapter's creators), Sam's fork (on GitHub), and Sam's computer (a local copy). The four answer options are: Original repository files, Sam's fork files, Sam's computer files, and No files change.

| Step | What happens | Correct answer | Why (shown as feedback) |
|------|--------------|----------------|-------------------------|
| 1 | Sam forks the original repository on GitHub. | Sam's fork files | A new copy is created in Sam's GitHub account. The original is untouched. |
| 2 | Sam copies the fork to their computer. | Sam's computer files | The files now exist on Sam's computer. The fork and the original do not change. |
| 3 | Sam corrects the mitochondria sentence on their computer and saves a commit with the message "Correct the mitochondria DNA statement". | Sam's computer files | The change and the commit exist only on Sam's computer so far. |
| 4 | Sam sends the commit to their fork on GitHub. | Sam's fork files | The fork now has the correction. The original still has the old sentence. |
| 5 | Sam opens a pull request asking the original owners to include the correction. | No files change | A request appears in the original repository's list of requests, but no copy's files change yet. |
| 6 | The original owners review the pull request and merge it. | Original repository files | Accepting the request puts the correction into the original, so every adopter can get the fix. |

**Provenance:** The six steps and the example correction are illustrative, written for this chapter, and describe no real repository. The workflow follows the chapter section "Fork, Pull Request, and Changelog." The sim labels the repository and names "illustrative."

**Rules:** Forking creates a new copy and changes no other copy. Cloning copies files to the computer and changes only the computer. A commit changes only the copy where it is saved. Sending a commit changes only the destination copy. A pull request creates a request and changes no copy's files. Merging changes only the repository that receives the merge.

**Learner Activity:**

1. The learner reads the description of step 1 and sees the three copies, all showing the original sentence about mitochondria.
2. The learner predicts which copy's files change, chooses an option, and presses Check.
3. The sim shows whether the prediction is correct, shows the Why text, and updates the three copies to show their contents after the step.
4. The learner moves to the next step. After step 6, the sim shows the first-attempt score and the final state of all three copies.

**Feedback:** Six steps, always in the order of the table, two attempts each. Correct: "Correct: [answer]. [Why text]." Incorrect on the first attempt: "Not quite. Think about which copy the step acts on," followed by a hint. If the learner chose Original repository files for steps 1 to 5, the hint is "The original changes only when its owners accept a change." If the learner chose No files change for a step that creates or changes files, the hint is "Check whether a copy is created or edited at this step." If the learner chose a copy that the step does not act on, the hint is "That copy is not touched at this step." After a second wrong prediction the correct answer and Why text are revealed and the step counts as missed. The score "Correct on first attempt: n of 6" is shown at the end, and the sim states whether mastery was reached.

**Starting State:** The three copies are shown, each with the original sentence about mitochondria, and step 1 is described. The question on screen is "Which copy's files change when Sam forks the repository?"

**Chapter Anchors:** The chapter states that a fork is a personal copy that leaves the original untouched, that a pull request asks the original owner to include changes, that merging is accepting a pull request, and that the step-through has 6 steps.
</details>

A **changelog** is a human-readable list of the notable changes to a resource, organized by version or date. The commit history records every change, down to a corrected comma. A changelog gives the headline version, written for readers who want to know what is different without reading each commit. A changelog for Sam's revised chapter might read:

```text
Version 3 (April): Added a Spanish vocabulary list.
Version 2 (March): Replaced three examples with a local pond. Corrected the statement about mitochondria.
Version 1 (January): Original chapter by Ana Rivera, CC BY 4.0.
```

Changelogs matter for OER for a second reason. Chapter 2 explained that a CC license asks users to say what they changed. A changelog is the natural place to record that, and it lets the next teacher see at once what has been adapted and by whom.

Putting the chapter's parts to work, the sorter below lets you practice the central skill: looking at how a resource is distributed and judging how well it supports revision.

#### Diagram: Editable Source Sorter

<details markdown="1">
<summary>Editable Source Sorter</summary>
Type: microsim
**sim-id:** editable-source-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify 8 described ways of distributing an OER into open and editable, editable but tied to specific software, or locked, according to how well each supports revising the resource.

**Prerequisites:** editable source metric, source format, open file format, word processing file, PDF-only distribution, Markdown, HTML (all defined in the chapter above this block).

**Evidence of Mastery:** For each of the 8 distributions, the learner chooses one of three categories and presses Check. A choice is correct when it matches the Correct category column in Content. Mastery is 7 or more of 8 correct on the first attempt. Changing a choice before pressing Check is exploration and does not count as evidence.

**Misconceptions:** (1) A resource available as a PDF can be edited easily. (2) A format with a published standard is always easy to edit. (3) Any file that opens on a computer counts as an editable source. (4) A finished video is an editable source.

**Instructional Rationale:** Classifying requires the learner to apply the two properties from the chapter, open and editable, to a described case. Distributions that look similar on the surface but differ in editability make the learner reason about the format instead of the file's name.

**Content:**

The three categories are: Open and editable, Editable but tied to specific software, and Locked.

| # | Distribution shown to the learner | Correct category | Why (shown as feedback) |
|---|-----------------------------------|------------------|-------------------------|
| 1 | A chapter published as a web page, with its Markdown source and history in a public repository. | Open and editable | Markdown is an open, editable format and the history shows every change. |
| 2 | A lesson set published as OpenDocument (.odt) files that anyone can download. | Open and editable | OpenDocument is an open format that word processors can edit. |
| 3 | A worksheet packet distributed as Word (.docx) files. | Editable but tied to specific software | It can be edited, but the layout and features depend on word-processing software. |
| 4 | A textbook distributed only as a PDF. | Locked | PDF describes fixed pages, so the text and images are hard to edit. |
| 5 | A slide deck distributed as a PowerPoint (.pptx) file. | Editable but tied to specific software | It can be edited, but it depends on presentation software. |
| 6 | A set of diagrams distributed as SVG files. | Open and editable | SVG is an open format and a drawing program or text editor can edit it. |
| 7 | A video lesson distributed only as a finished MP4 file, with no project files or transcript. | Locked | The finished video cannot be revised in any practical way without the project files. |
| 8 | A web page whose text is an image of a scanned book page, with no text version. | Locked | The words are in a picture, so the text cannot be edited without retyping it. |

**Provenance:** The 8 distributions are illustrative scenarios written for this chapter and describe no real resources. The categories come from the chapter sections "The Editable Source Metric" and "Source Formats and Open File Formats." The sim labels the scenarios "illustrative."

**Rules:** A distribution is Open and editable when its source is in a format with a published open specification and a person can change its content with ordinary tools. It is Editable but tied to specific software when it can be edited but depends on particular software. It is Locked when a person cannot reasonably change its content. Each of the 8 distributions fits exactly one category. Mastery is correct first attempts >= 7 of 8.

**Learner Activity:**

1. The learner reads the first distribution.
2. The learner chooses one of the three categories and presses Check.
3. The sim shows whether the choice is correct and shows the Why text, then moves to the next distribution.
4. After distribution 8, the sim shows the first-attempt score, lists any distribution the learner missed with its Why text, and offers the learner a chance to retry the missed distributions.

**Feedback:** Eight distributions, shown in the order of the table, two attempts each. Correct: "Correct: [category]. [Why text]." Incorrect on the first attempt: "Not quite," followed by a hint. If the learner chose Open and editable for a locked or software-tied distribution, the hint is "Ask whether the format is open, and whether a person can change the content with ordinary tools." If the learner chose Locked for an editable distribution, the hint is "Check whether the content can be changed without retyping it." If the learner chose Editable but tied to specific software for an open format, the hint is "A format with a published open specification does not depend on one program." After a second wrong choice the correct category and Why text are revealed and the distribution counts as missed. The score "Correct on first attempt: n of 8" is shown at the end, and the sim states whether mastery was reached.

**Starting State:** The first distribution is shown with the three category names and no choice made. The question on screen is "How well does this support revising the resource?"

**Chapter Anchors:** The chapter states that open and editable are separate properties, that PDF is open but rarely editable, that Markdown, HTML, OpenDocument, and SVG are open and editable, and that the sorter has 8 distributions.
</details>

!!! mascot-tip "Look for the Source Link"
    ![Echo the Loon giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    When a page offers only a PDF, scroll to the footer and look for words like "source," "edit," or "repository." A link to a GitHub page is a good sign, and if you find nothing, a short email asking for the source files is usually answered.

## Summary

This chapter showed how to judge whether a resource can really be revised. The key points are:

- The editable source metric asks whether the source can be edited in an open format, and it protects the Revise and Remix permissions.
- A source format is the recipe from which outputs such as web pages and PDFs are made, and an open file format is documented for anyone to use.
- Open and editable are different properties: PDF is open but rarely editable.
- Word processing files are editable but tied to software, and PDF-only distribution usually scores in the 1 to 3 range.
- Markdown and HTML are open, editable formats that suit OER, and one source can produce many outputs.
- Version control records every change, Git is the common tool, and a GitHub repository shows the files and history in a browser.
- A fork is your own copy, a pull request asks the original owner to include your changes, and a changelog summarizes the changes for readers.

!!! mascot-celebration "You Can Check a Source"
    ![Echo the Loon celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now open a resource's distribution and say whether you could revise it, read a repository's history, and explain how a fork and a pull request carry a correction back to the original. Chapter 5 turns to the first quality metric: whether the facts are right and up to date.
