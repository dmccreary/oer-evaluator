---
title: "Accessibility"
description: "Explains how to score accessibility against WCAG 2.1 AA, covering alt text, headings, color contrast, captions, keyboard use, screen readers, accessible math, and automated checkers."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:14:36"
version: 1.11
status: built
---

# Accessibility

## Summary

Explains how to score accessibility against WCAG 2.1 AA, covering alt text, headings, color contrast, captions, keyboard use, screen readers, accessible math, and automated checkers. It applies the accessibility metric and builds on HTML and the rubric from earlier chapters. After this chapter you can check a resource against WCAG 2.1 AA, write useful alt text, and run an accessibility checker.

## Concepts Covered

This chapter covers the following 23 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Accessibility | 33 |
| Accessibility Metric | 1 |
| WCAG | 21 |
| WCAG 2.1 AA | 20 |
| Alt Text | 4 |
| Decorative Image | 1 |
| Complex Image Description | 1 |
| Heading Structure | 2 |
| Color Contrast | 3 |
| Contrast Ratio | 1 |
| Color Independence | 1 |
| Captions | 4 |
| Transcript | 1 |
| Audio Description | 1 |
| Keyboard Navigation | 1 |
| Screen Reader | 8 |
| Link Text | 1 |
| Table Accessibility | 1 |
| Document Language | 1 |
| Accessible Math | 1 |
| Universal Design for Learning | 2 |
| Accessibility Checker | 2 |
| ARIA Labels | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)
- [Chapter 4: Open File Formats and Version Control](../04-open-formats-version-control/index.md)
- [Chapter 6: Alignment and Readability](../06-alignment-readability/index.md)

---

!!! mascot-welcome "Can Every Learner Get Through It?"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A resource that some learners cannot see, hear, or operate is unfinished, however well it teaches. This chapter gives you the checks that decide whether a blind learner, a deaf learner, or a learner who cannot use a mouse can get all the way through. Let's dive in and check the evidence!

Every other quality metric assumes that the learner can reach the content. The accessibility metric tests that assumption. A beautifully accurate, well-aligned, readable chapter fails a learner who cannot see its diagrams, hear its video, or reach its quiz with a keyboard. Accessibility is also where a reviewer finds the problems that authors see least, since an author who can see and hear and use a mouse rarely notices what a different learner meets.

This chapter explains what accessibility is, introduces the standard that the rubric uses, and then works through the practical checks: images, headings, color, media, keyboard use, screen readers, links, tables, language, math, and the tools that test them. The last section combines them into a score.

## Accessibility

**Accessibility** is the degree to which people with disabilities can perceive, understand, navigate, and use a resource. Disabilities include differences in vision, hearing, movement, and thinking, and they can be permanent, temporary, or situational. A learner with a broken arm, a learner in a noisy room, and a learner who is blind all benefit from a resource built so that information is available more than one way. Accessibility is a property of how the resource is designed. It is not a trait of the learner, and it is the author's responsibility to build it in.

In the United States, laws such as Section 504 of the Rehabilitation Act and the Americans with Disabilities Act apply to many schools and colleges, and the technical standard that policies most often cite is the one in the next section. Your institution's policy tells you what applies to you. The practical case is stronger than the legal one, because accessible design helps every learner.

Several of these supports depend on *assistive technology*, the tools that people with disabilities use to read and operate a page. The most common is a *screen reader*, software that reads a page aloud or sends it to a braille display, which a later section covers in detail.

**Worked example: five learners, five supports.** The table pairs learners with the feature that lets each one use the resource.

| Learner | What gets in the way | The feature that helps |
|---|---|---|
| A blind learner | Cannot see images or the layout | Text descriptions of images, and a clear heading structure for a screen reader |
| A deaf learner | Cannot hear a video | Captions |
| A learner who cannot use a mouse | Cannot point and click | Keyboard navigation |
| A learner with low vision | Faint text on a pale background | Strong color contrast and text that enlarges |
| A learner with a reading disability | Dense text | Clear structure, short paragraphs, and alternative formats |

## Accessibility Metric

The **accessibility metric** is the fourth quality metric of the rubric. It asks whether learners with disabilities can use the resource, judged against WCAG 2.1 at level AA. It is scored with ten checks, listed in the scoring section at the end of this chapter, and the checks follow the topics in between.

## WCAG

**WCAG**, the Web Content Accessibility Guidelines, is the international standard for accessible web content. The World Wide Web Consortium (W3C) publishes it through its Web Accessibility Initiative. WCAG is a long list of *success criteria*, each of which is a testable statement, such as "images have text alternatives" or "text has enough contrast". A reviewer can answer each one with pass or fail.

The criteria are grouped under four principles, often abbreviated POUR. Content must be **Perceivable**: users can see or hear it, through some sense. It must be **Operable**: users can control it, including without a mouse. It must be **Understandable**: users can follow what it says and how it works. And it must be **Robust**: it works with a range of browsers and with assistive technology, the tools that people with disabilities use to read and operate a page.

Each criterion has a conformance level. Level A is the most basic, level AA is the middle level that most policies require, and level AAA is the highest and is not required for whole sites. The standard has appeared in versions: 2.0 in 2008, 2.1 in 2018, and 2.2 in 2023.

**Worked example: one criterion under each principle.**

| Principle | The question it asks | An example criterion |
|---|---|---|
| Perceivable | Can users perceive the content? | Non-text content has a text alternative |
| Operable | Can users operate the controls? | All functions work with a keyboard |
| Understandable | Can users follow it? | The language of the page is identified |
| Robust | Does it work with assistive technology? | Custom controls expose a name and role |

The first MicroSim sorts requirements under the four principles. It shows twelve requirements, and for each one you choose the principle it belongs to.

#### Diagram: WCAG Principles Sorter

<details markdown="1">
<summary>WCAG Principles Sorter</summary>
Type: microsim
**sim-id:** wcag-principles-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of twelve accessibility requirements under the WCAG principle it belongs to (perceivable, operable, understandable, or robust), with at least 10 of 12 correct on the first attempt.

**Prerequisites:** Accessibility, WCAG (both defined in this chapter above this block).

**Evidence of Mastery:** For each requirement the learner commits one of four principles. A placement is correct when it matches the Correct principle column in Content. Mastery is at least 10 of 12 correct on the first attempt. Reading the principle definitions is exploration, not evidence.

**Misconceptions:** (1) Captions belong under Understandable because they explain speech. (2) Contrast is Operable because users act on the page. (3) All requirements about HTML are Robust.

**Instructional Rationale:** Classifying requirements under the four principles is an Understand-level action that shows the learner how the long list of criteria is organized. Three requirements per principle, each tied to a different need, teach the learner to ask which kind of barrier a requirement removes.

**Content:**

The four principles: Perceivable (users can sense the content), Operable (users can control it), Understandable (users can follow it), Robust (it works with assistive technology).

The twelve requirements:

| # | Requirement shown to the learner | Correct principle | Why (shown as feedback) |
|---|---|---|---|
| 1 | Images have text alternatives. | Perceivable | A user who cannot see needs another way to perceive it. |
| 2 | Video with sound has captions. | Perceivable | A user who cannot hear needs another way to perceive it. |
| 3 | Text has enough contrast with its background. | Perceivable | A user with low vision must be able to see it. |
| 4 | Every function can be used with a keyboard. | Operable | A user who cannot use a mouse must be able to control it. |
| 5 | Users can pause or stop moving content. | Operable | Users must be able to control content that moves. |
| 6 | Users can see which element has keyboard focus. | Operable | A keyboard user must see where they are in order to operate the page. |
| 7 | The language of the page is identified. | Understandable | Tools and users need to know which language the text is in. |
| 8 | Navigation is consistent from page to page. | Understandable | Users can follow a page when its navigation behaves as before. |
| 9 | Form errors are described in text. | Understandable | Users must be able to understand what went wrong and how to fix it. |
| 10 | Custom buttons expose a name and a role to assistive technology. | Robust | Assistive technology must be able to read and operate them. |
| 11 | Status messages can be announced without moving focus. | Robust | Assistive technology must be able to report them. |
| 12 | The content works with a range of browsers and assistive technologies. | Robust | The content must not depend on one tool. |

**Provenance:** The principles and the requirements follow the chapter section "WCAG", and each requirement paraphrases a criterion of WCAG 2.1. The sim states that the wording is simplified and names the WCAG documents as the authority.

**Rules:** Each requirement has exactly one correct principle, three per principle.

**Learner Activity:**

1. The learner sees one requirement and the four principles.
2. The learner may open the principle definitions. Opening them does not change the score.
3. The learner places the requirement under a principle, and the placement is committed.
4. The sim shows whether it was correct and the Why text.
5. After requirement 12 the sim shows the summary.

**Feedback:** 12 requirements in a shuffled order, one attempt each. Correct: "Correct: [principle]. [Why]". Incorrect: "Not quite. This is [principle]. [Why]". The summary shows "[n] of 12 correct on the first attempt". At 10 or more it adds "You can sort the WCAG requirements." Below 10 it lists the Why text of each missed requirement.

**Starting State:** The first requirement, the four principles, and the definitions closed. The question shown is "Which principle does this requirement serve?"

**Chapter Anchors:** The chapter says the four principles are perceivable, operable, understandable, and robust, abbreviated POUR, and that the levels are A, AA, and AAA.
</details>

## WCAG 2.1 AA

**WCAG 2.1 AA** is version 2.1 of the guidelines at conformance level AA, which means a resource meets every level A criterion and every level AA criterion. It is the target of this book's rubric because policies at many schools and colleges cite it, and because it is demanding enough to protect the main groups of learners and practical enough for a teacher to check. Version 2.1 added criteria to 2.0 for people who use mobile devices, who have low vision, or who have cognitive differences. Version 2.2 adds further criteria to 2.1, so a resource that does well on 2.2 is in good shape for 2.1.

**Worked example: six criteria and their levels.** The criteria below are among those that this chapter's checks draw on.

| Criterion | Level | What it asks | Covered in this chapter under |
|---|---|---|---|
| 1.1.1 Non-text Content | A | Images and other non-text content have text alternatives | Alt Text |
| 1.2.2 Captions (Prerecorded) | A | Prerecorded video with sound has captions | Captions |
| 2.1.1 Keyboard | A | All functions work from a keyboard | Keyboard Navigation |
| 1.4.3 Contrast (Minimum) | AA | Text has a contrast ratio of at least 4.5 to 1, or 3 to 1 for large text | Contrast Ratio |
| 1.2.5 Audio Description (Prerecorded) | AA | Prerecorded video has audio description | Audio Description |
| 1.4.6 Contrast (Enhanced) | AAA | Text has a contrast ratio of at least 7 to 1 | Not required at AA |

## Images

### Alt Text

**Alt text** is a short text description attached to an image, so that a person who cannot see the image still gets what it is for. It is stored in the image's `alt` attribute in HTML, and a screen reader reads it aloud. Good alt text answers the question "what does this image do here?" and not "what does this image look like?". A photo of a river in a lesson about meanders needs alt text that mentions the bends. The same photo used as a mood image needs none.

Four habits make alt text useful. Say what matters in the context, in a sentence or two. Do not begin with "image of" or "picture of", because the screen reader already announces that it is an image. Do not repeat a caption that sits right beside the image. And never leave a filename or a single word such as "photo".

!!! mascot-tip "Describe the Purpose, Not the Picture"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Ask what the image is doing in this sentence, and write alt text that does the same job for a reader who cannot see it. If the lesson is about river bends, the alt text should mention the bends.

**Worked example: three alt texts for one photo.** The photo shows a school garden's rain barrel under a roof downspout, in a lesson on reducing runoff.

| Alt text | Verdict | Why |
|---|---|---|
| "photo" | Poor | One word that says nothing. |
| "A rain barrel at the end of a roof downspout holds runoff from the school roof" | Good | It names the object and the point it makes in the lesson. |
| "Image of a picture of the school garden taken on a sunny day with flowers, a bench, and the principal's car in the background" | Poor | It starts with "image of" and lists details that do not serve the lesson. |

### Decorative Image

A **decorative image** is an image that adds appearance only and carries no information, such as a border line or a mood photo beside a heading. A screen reader should skip it, and the way to say so in HTML is an empty alt attribute, `alt=""`. An image with no alt attribute at all is a different case, because many screen readers then read out the file name. When an image looks decorative but a learner might wonder what it is, the safer choice is a short description.

### Complex Image Description

A **complex image description** is a longer text that conveys the content of an image that is too detailed for a sentence, such as a chart, a map, or a labeled diagram. The pattern has two parts. A short alt text names the image and what it shows, and a longer description or a data table nearby gives the full content. For a bar chart of monthly rainfall, the short alt text says "Bar chart of monthly rainfall" and a table below lists every month and its value. The long description should let a reader who never sees the image answer the same questions a sighted reader could.

The next two MicroSims practice images. The first sorts nine images into three types, and the second judges nine alt texts for one photo.

#### Diagram: Image Type Sorter

<details markdown="1">
<summary>Image Type Sorter</summary>
Type: microsim
**sim-id:** image-type-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of nine images as informative, decorative, or complex, with at least 8 of 9 correct on the first attempt.

**Prerequisites:** Alt Text, Decorative Image, Complex Image Description (all defined in this chapter above this block).

**Evidence of Mastery:** For each image the learner commits one of three bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 8 of 9 correct on the first attempt. Reading the definitions is exploration, not evidence.

**Misconceptions:** (1) Every image needs a long description. (2) A logo needs no alt text. (3) A decorative image should have alt text that says "decoration".

**Instructional Rationale:** Classifying an image by its role is an Understand-level action that decides what kind of text it needs. Three images per type, each in a different setting, teach the learner to ask what the image does and not what it shows.

**Content:**

The three bins: Informative (needs short alt text), Decorative (needs empty alt text), Complex (needs short alt text and a long description or data table).

The nine images:

| # | Image shown to the learner (described in words) | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | A photo of a river with sharp bends, used to show how a river meanders. | Informative | It carries information the lesson uses, and a sentence can convey it. |
| 2 | A thin decorative line between two sections. | Decorative | It adds no information. |
| 3 | A bar chart of monthly rainfall with twelve bars. | Complex | The values need a table or a long description. |
| 4 | A school logo in the page header that links to the home page. | Informative | Its alt text should state where the link goes. |
| 5 | A stock photo of smiling students beside a heading, adding mood only. | Decorative | It carries no information. |
| 6 | A labeled diagram of the water cycle with six labels and arrows. | Complex | The parts and the order of the arrows need a longer description. |
| 7 | A screenshot showing which button to click in a software tool. | Informative | It shows where to click, and a sentence can say so. |
| 8 | A map of a river and its tributaries with several labeled towns. | Complex | The places and their relations need a longer description. |
| 9 | A small lightbulb icon beside the word "Tip" that the text already states. | Decorative | The adjacent text carries the meaning. |

**Provenance:** The images are described in words for this chapter, and the sim labels them "illustrative examples". The bins follow the chapter sections "Alt Text", "Decorative Image", and "Complex Image Description".

**Rules:** Each image has exactly one correct bin, three per bin.

**Learner Activity:**

1. The learner sees a description of one image and the three bins.
2. The learner places the image in a bin, and the placement is committed.
3. The sim shows whether it was correct, the Why text, and the kind of text the image needs.
4. After image 9 the sim shows the summary.

**Feedback:** 9 images in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 9 correct on the first attempt". At 8 or more it adds "You can tell which images need which text." Below 8 it lists the Why text of each missed image.

**Starting State:** The first image description and the three bins. The question shown is "What does this image need?"

**Chapter Anchors:** The chapter says a decorative image takes an empty alt attribute, a complex image takes short alt text plus a longer description or table, and an informative image takes a short alt text.
</details>

#### Diagram: Alt Text Evaluator

<details markdown="1">
<summary>Alt Text Evaluator</summary>
Type: microsim
**sim-id:** alt-text-evaluator<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of nine alt texts for one photo is useful or needs work, with at least 8 of 9 correct on the first attempt.

**Prerequisites:** Alt Text, Decorative Image (both defined in this chapter above this block).

**Evidence of Mastery:** For each alt text the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 8 of 9 correct on the first attempt. Reading the four habits is exploration, not evidence.

**Misconceptions:** (1) Longer alt text is always better. (2) "Image of" helps the reader. (3) Empty alt text is safe for any image.

**Instructional Rationale:** Judging alt text against stated habits is an Evaluate-level action. Nine alternatives for one photo isolate the differences that matter, so the learner learns what separates a useful description from a poor one.

**Content:**

The photo, described in words and shown at all times: a school garden's rain barrel under a roof downspout, used in a lesson on reducing runoff.

The four habits, shown on request: say what matters in the context; do not begin with "image of"; do not repeat an adjacent caption; never use a filename or a single word.

The nine alt texts:

| # | Alt text shown to the learner | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | image1.png | Needs work | A filename says nothing about the image. |
| 2 | photo | Needs work | One word that says nothing. |
| 3 | A rain barrel under a roof downspout collects water from the roof | Useful | It names the object and what it does. |
| 4 | Image of a photograph of a barrel | Needs work | It begins with "image of" and does not say what matters. |
| 5 | A rain barrel in a school garden collects roof runoff, one way to keep water from flowing onto pavement | Useful | It connects the object to the lesson. |
| 6 | A rain barrel at the end of a roof downspout | Useful | It is short and names what is shown and where. |
| 7 | A picture of the school garden taken by Ms. Lee on a sunny day with many flowers, a bench, and the principal's car in the background | Needs work | It is long and lists details that do not serve the lesson. |
| 8 | (empty alt text) | Needs work | The photo carries information the lesson uses, so it is not decorative. |
| 9 | Rain barrel connected to a downspout, holding runoff from the school roof | Useful | It is plain and says what the picture shows and why it matters. |

**Provenance:** The photo and the alt texts are written for this chapter, and the sim labels them "illustrative examples". The habits follow the chapter section "Alt Text".

**Rules:** Each alt text has exactly one correct bin. Four are Useful and five Need work. A screen reader reads alt text aloud and announces that the element is an image, so the sim treats "image of" as redundant.

**Learner Activity:**

1. The learner sees the photo description, the four habits on request, and one alt text.
2. The learner places the alt text in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After alt text 9 the sim shows the summary.

**Feedback:** 9 alt texts in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 9 correct on the first attempt". At 8 or more it adds "You can judge alt text." Below 8 it lists the Why text of each missed alt text.

**Starting State:** The photo description and alt text 1 or the first in the shuffled order. The question shown is "Is this alt text useful?"

**Chapter Anchors:** The chapter's worked example of three alt texts for the rain barrel photo agrees with this sim: "photo" needs work and the rain barrel at the end of a roof downspout is useful.
</details>

## Structure

### Heading Structure

**Heading structure** is the order and nesting of a page's headings. A page should have one main heading, with subheadings nested beneath it in order, and no level skipped: an h2 contains h3 headings, and an h3 never sits directly under an h1. Real headings, made with heading tags and not bold text, matter because assistive technology builds a map of the page from them, and a screen reader user can jump from heading to heading to skim a page the way a sighted reader scans one.

A reviewer checks three things. Are the headings real heading tags? Is the order logical, with no skipped level? And does each heading describe its section, as Chapter 6 asked? The accessibility check adds the first two to the readability check from that chapter.

The MicroSim below practices the check. It shows two outlines of ten heading lines in all, and for each line you decide whether it is fine or has one of three defects.

#### Diagram: Heading Outline Checker

<details markdown="1">
<summary>Heading Outline Checker</summary>
Type: microsim
**sim-id:** heading-outline-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine ten heading lines from two page outlines and mark each as fine or as having a skipped level, a second main heading, or a vague heading, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Heading Structure (defined in this chapter above this block) and Headings and Subheadings (defined in Chapter 6).

**Evidence of Mastery:** For each heading line the learner commits one of four options. A choice is correct when it matches the Correct option column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the defect definitions is exploration, not evidence.

**Misconceptions:** (1) A heading level is chosen for how large it looks. (2) A page may have several main headings. (3) A short heading is a good heading.

**Instructional Rationale:** Examining an outline is an Analyze-level action, because the learner must compare each line with the line before it and with the page's structure. Ten lines with three different defects teach the learner to look for each defect separately.

**Content:**

The four options: Fine, Skipped level, Second main heading, Vague heading.

The two outlines (each line shows the heading level and text):

| Outline | Line | Level | Text | Correct option | Why (shown as feedback) |
|---|---|---|---|---|---|
| A | A1 | h1 | Watershed Basics | Fine | The one main heading names the page. |
| A | A2 | h2 | What a watershed is | Fine | It sits directly under the main heading and says what follows. |
| A | A3 | h4 | Parts of a watershed | Skipped level | It jumps from h2 to h4 and skips h3. |
| A | A4 | h2 | How water moves | Fine | It returns to the section level and says what follows. |
| A | A5 | h3 | Runoff | Fine | It sits directly under an h2 and names its topic. |
| B | B1 | h1 | Rivers | Fine | The one main heading names the page. |
| B | B2 | h2 | Where rivers start | Fine | It sits directly under the main heading and says what follows. |
| B | B3 | h1 | River safety | Second main heading | A page should have one main heading, and this line starts a second. |
| B | B4 | h2 | Stuff | Vague heading | The word does not tell the reader what the section holds. |
| B | B5 | h3 | Cold water | Fine | It sits under an h2 and says what follows. |

**Provenance:** The outlines are made up for this chapter, and the sim labels them "illustrative examples". The defects follow the chapter section "Heading Structure".

**Rules:** Each line has exactly one correct option. Seven lines are Fine, and the three defects each occur once. A line is a Skipped level when its level is more than one deeper than the previous line's level.

**Learner Activity:**

1. The learner sees outline A as an indented list with levels shown.
2. The learner chooses an option for each line, and the choice is committed.
3. The sim shows whether each choice was correct and the Why text.
4. The learner repeats for outline B.
5. After line B5 the sim shows the summary.

**Feedback:** 10 lines in outline order, one attempt each. Correct: "Correct: [option]. [Why]". Incorrect: "Not quite. This line is [option]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can read a page's outline." Below 9 it lists the Why text of each missed line.

**Starting State:** Outline A with no choices made. The question shown is "Is this heading fine?"

**Chapter Anchors:** The chapter says a page should have one main heading with subheadings nested in order and no skipped level, and that headings should describe their sections.
</details>

## Color

### Color Contrast

**Color contrast** is the difference in brightness between text, or another meaningful element, and the background behind it. Strong contrast makes text easy to read for everyone and essential for people with low vision, for aging eyes, and for anyone reading in bright light. Weak contrast, such as pale gray text on white, is one of the most common accessibility failures. The requirement covers text, the parts of controls that identify them, and the lines and shapes that carry meaning in a chart. It does not cover a logo or a purely decorative element.

### Contrast Ratio

A **contrast ratio** is a number that measures color contrast, from 1 to 1 for no difference to 21 to 1 for black on white. WCAG 2.1 AA sets three minimums. Normal text needs a ratio of at least 4.5 to 1. Large text, which means text of at least 18 points, or at least 14 points if bold, needs at least 3 to 1. And the parts of controls and graphics that convey meaning need at least 3 to 1.

The ratio comes from the *relative luminance* of the two colors, a number from 0 for black to 1 for white that measures how bright a color appears to the eye. The formula is:

```text
contrast ratio = (L1 + 0.05) / (L2 + 0.05)
```

Here L1 is the relative luminance of the lighter color and L2 is that of the darker one. You never compute luminance by hand, because free tools do it, but the formula shows why black on white scores the maximum: white has a luminance of 1, black has 0, and the ratio is (1 + 0.05) divided by (0 + 0.05), which is 21.

**Worked example: a difference you cannot see.** Two grays on a white background look almost the same. A tool gives #767676 on white a ratio of 4.54 to 1, which passes the 4.5 minimum for normal text. It gives the slightly lighter #777777 on white a ratio of 4.48 to 1, which fails. The tests use the unrounded ratio, so 4.499 fails even though a tool may display it as 4.50. A pass or fail can hinge on a difference no one can see, and that is why reviewers measure instead of judging by eye.

### Color Independence

**Color independence** means that color is never the only way a resource conveys information. A chart that marks the winner in green and the loser in red, with no other cue, fails a learner who is color blind and a learner who prints the page in gray. The fix is a second cue: a label, a pattern, a shape, an icon, or underlined text. Links inside a paragraph are a common case. A link marked only by a slightly different color needs an underline or another cue.

The MicroSim below practices contrast. In explore mode you enter two colors and read the ratio, and in practice mode you decide whether nine color pairs pass for normal text, for large text only, or not at all.

#### Diagram: Contrast Ratio Checker

<details markdown="1">
<summary>Contrast Ratio Checker</summary>
Type: microsim
**sim-id:** contrast-ratio-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** use<br/>
**Learning Objective:** The learner will use the contrast ratio and the 4.5 and 3 minimums to decide whether each of nine color pairs passes for normal text, passes for large text only, or fails, with at least 8 of 9 correct on the first attempt.

**Prerequisites:** Color Contrast, Contrast Ratio, Color Independence (all defined in this chapter above this block).

**Evidence of Mastery:** For each pair the learner commits one of three verdicts after seeing the colors and before the ratio is shown. A verdict is correct when it matches the Correct verdict column in Content. Mastery is at least 8 of 9 correct on the first attempt. Using the explore mode is exploration, not evidence.

**Misconceptions:** (1) If two colors look different, they pass. (2) Rounding 4.499 up to 4.5 makes it pass. (3) Large text needs the same ratio as normal text.

**Instructional Rationale:** Using a numeric threshold on measured values is an Apply-level action. Predicting from sight first, and then seeing the measured ratio, shows the learner that sight is unreliable near the threshold, which is the reason the check exists.

**Content:**

The thresholds, shown at all times: normal text needs a ratio >= 4.5; large text (18 points or larger, or 14 points or larger if bold) needs a ratio >= 3.0. The three verdicts: Passes for normal text (ratio >= 4.5), Passes for large text only (ratio >= 3.0 and < 4.5), Fails (ratio < 3.0).

The nine pairs, with each ratio computed from relative luminance as the chapter states:

| # | Text color | Background color | Ratio | Correct verdict | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | #000000 | #FFFFFF | 21.00 | Passes for normal text | The largest possible ratio. |
| 2 | #757575 | #FFFFFF | 4.61 | Passes for normal text | The ratio is at least 4.5. |
| 3 | #949494 | #FFFFFF | 3.03 | Passes for large text only | The ratio is at least 3.0 and less than 4.5. |
| 4 | #FFFFFF | #1A5FB4 | 6.29 | Passes for normal text | White text on a deep blue has a high ratio. |
| 5 | #FFFFFF | #FF8C00 | 2.33 | Fails | White on orange is less than 3.0, so no text size passes. |
| 6 | #FF0000 | #FFFFFF | 4.00 | Passes for large text only | Red on white is at least 3.0 and less than 4.5. |
| 7 | #767676 | #F0F0F0 | 3.99 | Passes for large text only | The same gray that passes on white is less than 4.5 on a light gray background. |
| 8 | #DDDDDD | #FFFFFF | 1.36 | Fails | Pale gray on white has almost no contrast. |
| 9 | #FFFFFF | #2E7D32 | 5.13 | Passes for normal text | White on a dark green has a ratio of at least 4.5. |

**Provenance:** The ratios are computed from the WCAG definition of relative luminance and are shown to two decimals. The color pairs are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The thresholds follow the chapter section "Contrast Ratio".

**Rules:** The ratio is (L1 + 0.05) / (L2 + 0.05) with L1 the luminance of the lighter color and L2 that of the darker. Tests use the unrounded ratio. Each pair has exactly one correct verdict. In explore mode the learner enters a text color and a background color as hex codes, and the sim shows the ratio to two decimals and the three verdicts for normal text, for large text, and for graphics. Four pairs are Passes for normal text, three are Passes for large text only, and two are Fails.

**Learner Activity:**

1. In explore mode the learner enters two colors and reads the ratio and the verdicts.
2. In practice mode the sim shows pair 1 as a sample of text on its background, without the ratio.
3. The learner chooses a verdict, and the choice is committed.
4. The sim shows the ratio, whether the verdict was correct, and the Why text.
5. After pair 9 the sim shows the summary.

**Feedback:** 9 pairs in a shuffled order, one attempt each. Correct: "Correct: [verdict]. The ratio is [ratio]. [Why]". Incorrect: "Not quite. The ratio is [ratio], so this is [verdict]. [Why]". The summary shows "[n] of 9 correct on the first attempt". At 8 or more it adds "You can read a contrast ratio." Below 8 it lists the Why text of each missed pair.

**Starting State:** Explore mode with black text on a white background and a ratio of 21.00. The prompt is "Enter two colors to see the ratio."

**Chapter Anchors:** The chapter says normal text needs a ratio of at least 4.5 to 1, large text at least 3 to 1, black on white is 21 to 1, #767676 on white is 4.54 to 1, and #777777 on white is 4.48 to 1.
</details>

## Audio and Video

### Captions

**Captions** are a text version of the speech and important sounds in a video, shown in time with the video. They serve learners who are deaf or hard of hearing, and they also help learners who watch with the sound off, learners who are still learning the language, and anyone in a noisy room. Good captions include who is speaking when that is not obvious, and sounds that matter, such as "[a door slams]". Automatic captions are a start. A reviewer checks them for errors, because a wrong word in a technical term can change the meaning.

### Transcript

A **transcript** is a text version of the audio and, when there is video, of the important visual information too, given as a separate document. A transcript serves learners who prefer to read, learners who use a braille display, and anyone who wants to search for a quotation. It does not replace captions for video, since captions are timed and a transcript is not, and the two work well together.

### Audio Description

**Audio description** is spoken narration of the important visual information in a video that the soundtrack does not already give: actions, scene changes, on-screen text, and charts. It serves learners who are blind or have low vision. A video in which an instructor says "as you can see here" and points to a chart, with no description of the chart, leaves a blind learner out. The simplest fix is to say what the chart shows. At level AA, prerecorded video with sound needs captions and audio description.

The MicroSim below matches eight situations to the alternative each one calls for.

#### Diagram: Media Alternative Matcher

<details markdown="1">
<summary>Media Alternative Matcher</summary>
Type: microsim
**sim-id:** media-alternative-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of eight situations by the media alternative it calls for (captions, transcript, or audio description), with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Captions, Transcript, Audio Description (all defined in this chapter above this block).

**Evidence of Mastery:** For each situation the learner commits one of three alternatives. A choice is correct when it matches the Correct alternative column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the definitions is exploration, not evidence.

**Misconceptions:** (1) A transcript replaces captions. (2) Audio description is only for blind learners watching films. (3) Captions help only deaf learners.

**Instructional Rationale:** Classifying a need by its alternative is an Understand-level action. Eight situations that vary the learner and the barrier teach the learner to ask what is missing: the sound, the sight, or a readable text.

**Content:**

The three alternatives: Captions (timed text of speech and sounds), Transcript (a separate text document of the audio and the key visual information), Audio description (narration of important visual information).

The eight situations:

| # | Situation shown to the learner | Correct alternative | Why (shown as feedback) |
|---|---|---|---|
| 1 | A deaf learner watches a lecture video. | Captions | The learner needs the speech as timed text. |
| 2 | A blind learner watches a science demonstration in which the steps appear only on screen. | Audio description | The visual steps are not in the audio. |
| 3 | A learner wants to search a podcast for a quotation. | Transcript | Text can be searched, and audio alone cannot. |
| 4 | A learner watches a video in a noisy cafeteria with the sound off. | Captions | Timed text lets the learner follow without sound. |
| 5 | A learner who is deaf and blind reads a video's content on a braille display. | Transcript | A text document can be read in braille. |
| 6 | A video shows a chart that the narrator never describes. | Audio description | The chart is visual information that the audio leaves out. |
| 7 | A learner with a reading difference prefers to read at their own pace instead of watching. | Transcript | A document lets the learner set the pace. |
| 8 | A learner still learning the language wants to follow the words on screen as they are spoken. | Captions | Timed text matches the speech as it is said. |

**Provenance:** The situations are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The definitions follow the chapter sections "Captions", "Transcript", and "Audio Description".

**Rules:** Each situation has exactly one correct alternative. Three situations call for Captions, three for Transcript, and two for Audio description.

**Learner Activity:**

1. The learner sees one situation and the three alternatives.
2. The learner chooses an alternative, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After situation 8 the sim shows the summary.

**Feedback:** 8 situations in a shuffled order, one attempt each. Correct: "Correct: [alternative]. [Why]". Incorrect: "Not quite. This calls for [alternative]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can match the need to the alternative." Below 7 it lists the Why text of each missed situation.

**Starting State:** The first situation and the three alternatives. The question shown is "What does this learner need?"

**Chapter Anchors:** The chapter says captions are timed text, a transcript is a separate text document, and audio description narrates visual information the audio omits.
</details>

## Operating the Page

### Keyboard Navigation

**Keyboard navigation** is the ability to use every function of a resource with a keyboard alone. Many learners cannot use a mouse, including learners with motor disabilities, learners who use a screen reader, and learners who use a device that sends keyboard signals. The Tab key moves from one control to the next, Shift and Tab together move back, and Enter or Space activates a control. A resource passes when every link, button, and quiz can be reached and used this way, the focus is visible as an outline or highlight, the order of focus follows the order of the page, and the keyboard never gets stuck in one place.

!!! mascot-tip "Put the Mouse Aside for Two Minutes"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Open the page, set the mouse out of reach, and press Tab through the whole thing. If you lose track of where you are, or you cannot reach a control, you have found a keyboard failure.

### Screen Reader

A **screen reader** is software that reads a page aloud, or sends it to a braille display, for people who cannot see the screen. Examples include NVDA, which is free for Windows, VoiceOver, which is built into Apple devices, and JAWS, a commercial program. A screen reader does not read the page as it looks. It reads the page's underlying structure: headings, links, buttons, image descriptions, and table cells. A user typically moves through a page by jumping from heading to heading or by pulling up a list of all the links, so structure and good text are everything.

A reviewer who has never heard a screen reader read a page learns a great deal from five minutes of listening. Missing alt text becomes a file name read aloud, a link that says only "click here" is useless in a list of links, and a heading structure that looked fine shows its gaps.

**Worked example: what four snippets sound like.** The table gives each snippet of HTML and what a screen reader typically says. Wording varies between programs.

| What the page contains | What a screen reader typically says | What it tells the reviewer |
|---|---|---|
| A heading that reads "How water moves" | "Heading level 2, How water moves" | Real headings are announced with their level |
| An image with alt text "A river meandering through a valley" | "Image, A river meandering through a valley" | The alt text does its job |
| An image with no alt attribute | "Image, river.png" | The file name is read, which is useless |
| An image with an empty alt attribute | Nothing | The image is skipped, which is correct only for a decorative image |

!!! mascot-encourage "Listen Once and You Will Hear It Forever"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    The first time you hear a screen reader read a page aloud it can feel fast and strange, and that is normal for every new listener. You already skim a page by its headings, and a screen reader user does the same by ear. Five minutes with one will change how you write alt text.

The MicroSim below practices the connection. It shows six snippets, and for each one you choose what a screen reader typically says.

#### Diagram: Screen Reader Announcement Matcher

<details markdown="1">
<summary>Screen Reader Announcement Matcher</summary>
Type: microsim
**sim-id:** screen-reader-announcement-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** infer<br/>
**Learning Objective:** The learner will infer what a screen reader typically announces for each of six snippets of page markup, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Screen Reader, Alt Text, Decorative Image, Heading Structure (all defined in this chapter above this block).

**Evidence of Mastery:** For each snippet the learner commits one of three announcements before the answer is shown. A choice is correct when it matches the Correct announcement column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the worked-example table is exploration, not evidence.

**Misconceptions:** (1) A screen reader describes what an image looks like by itself. (2) An image with no alt attribute is skipped. (3) A heading is read as ordinary text.

**Instructional Rationale:** Inferring the announcement from the markup is an Understand-level action that connects what an author writes to what a listener hears. Six snippets that differ in one detail each teach the learner to read markup as a listener would.

**Content:**

The sim states that announcements are typical and simplified, and that wording differs between screen readers.

The six snippets:

| # | Snippet shown to the learner | Option A | Option B | Option C | Correct | Why (shown as feedback) |
|---|---|---|---|---|---|---|
| 1 | A heading "How water moves" at level 2 | Heading level 2, How water moves | How water moves | Link, How water moves | A | A heading is announced with its level. |
| 2 | An image with alt text "A river meandering through a valley" | Image, river dot png | Image, A river meandering through a valley | Nothing | B | The alt text is read as the image's description. |
| 3 | An image with no alt attribute and the file name river.png | Image, river dot png | Image, a river | Nothing | A | Without alt text, the file name is often read. |
| 4 | An image with an empty alt attribute | Image, no description | Image, decorative | Nothing | C | An empty alt attribute tells the reader to skip the image. |
| 5 | A link whose text is "click here" | Link, click here | Link, goes to the runoff page | Button, click here | A | The reader announces only the link text, which says nothing about the destination. |
| 6 | A button that contains only an image with no alt text, file name close.png | Button, close dot png | Button, close | Nothing | A | The file name becomes the button's name, which is useless. |

**Provenance:** The snippets are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The announcements are typical and simplified, and the sim states that they vary between programs.

**Rules:** Each snippet has exactly one correct option, in the position shown in the Correct column.

**Learner Activity:**

1. The learner sees one snippet and three options.
2. The learner chooses an option, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After snippet 6 the sim shows the summary.

**Feedback:** 6 snippets in a shuffled order, one attempt each. Correct: "Correct: [announcement]. [Why]". Incorrect: "Not quite. A screen reader typically says: [announcement]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can hear the markup." Below 5 it lists the Why text of each missed snippet.

**Starting State:** The first snippet and its three options. The question shown is "What does a screen reader typically say?"

**Chapter Anchors:** The chapter's worked example lists four snippets and what a screen reader typically says: a heading with its level, an image with alt text, an image with no alt attribute read as its file name, and an image with empty alt text skipped.
</details>

## Links, Tables, Language, and Math

### Link Text

**Link text** is the visible words of a link. Good link text says where the link goes, such as "Chapter 5: Accuracy and Currency" or "the state water agency's river data". Screen reader users often pull up a list of all the links on a page, and a list that reads "click here, click here, read more" is useless. A link inside a sentence should still make sense out of context. Avoid raw web addresses as link text, and avoid the same text for links that go to different places.

### Table Accessibility

**Table accessibility** is the practice of building tables so that a screen reader can read the cells in relation to their headings. A data table has a header row, and sometimes a header column, marked as headers in HTML with the `th` tag, so that a reader hearing a cell also hears its column heading. A table needs a short caption or title, and a simple structure without merged cells where possible. Tables are for data. Using a table to lay out a page confuses screen readers, so layout should be done another way.

### Document Language

**Document language** is the human language of the page's text, set in HTML with the `lang` attribute on the page, such as `lang="en"` for English. A screen reader uses it to choose the right pronunciation, and a translation tool uses it to know what to translate. When a passage in another language appears, such as a Spanish quotation, it can carry its own language setting.

### Accessible Math

**Accessible math** is the practice of writing equations so that a screen reader can read them and a learner can enlarge them. A picture of an equation is not accessible, because it cannot be read aloud or resized without blurring. Better choices are MathML, a web standard for math notation, or LaTeX rendered by a web library that exposes the equation to assistive technology. If an image is unavoidable, give it alt text that states the equation in words. Writing the equation in words beside it is a good habit as well.

### ARIA Labels

**ARIA labels** are attributes from a web standard called WAI-ARIA that add a name or description to an element when the page's ordinary HTML does not provide one. A button that shows only an icon can carry `aria-label="Close"` so that a screen reader announces "Close". The first rule of ARIA is to use ordinary HTML elements first, because a real button already has a name and a role. ARIA used wrongly can make a page worse than no ARIA at all, so add it only where ordinary HTML falls short.

## Design and Tools

### Universal Design for Learning

**Universal Design for Learning** (UDL) is a framework for designing learning so that it works for the widest range of learners from the start, instead of adding fixes later. CAST, an education nonprofit, developed it around three principles: give learners multiple ways to engage with the material, multiple ways to take it in, and multiple ways to show what they know. A resource that offers a text version, a captioned video, and an interactive simulation of the same idea follows UDL. Accessibility removes barriers for learners with disabilities, and UDL plans for variety among all learners, so the two support each other.

!!! mascot-thinking "A Ramp Helps More Than the Wheelchair"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A curb cut built for wheelchairs also helps strollers, carts, and tired travelers. Captions, clear headings, and strong contrast work the same way, and they help learners you never planned for.

### Accessibility Checker

An **accessibility checker** is a tool that scans a page or a document and reports accessibility problems automatically. Free examples include WAVE, axe, and the accessibility audit built into the Chrome browser's Lighthouse tool. Checkers find real problems quickly, such as images with no alt attribute, text with weak contrast, and form fields with no label. They cannot judge everything. A tool can tell that alt text exists and cannot tell whether it is useful, and it cannot tell whether a heading describes its section. Use a checker to find the problems it can see, then check the rest by hand.

!!! mascot-warning "A Clean Report Is Not a Pass"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A checker can pass a page whose alt text says "photo" on every image, because the text exists. Run the tool, then do the human checks it cannot do: read the alt text, listen with a screen reader, and tab through the page.

The next MicroSim is an illustration of a page that follows the checks in this chapter. Its eight numbered markers point to the features that a reviewer looks for.

#### Diagram: Anatomy of an Accessible Page

<details markdown="1">
<summary>Anatomy of an Accessible Page</summary>
Type: infographic
**sim-id:** accessibility-page-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify eight accessibility features on an illustrated page from a description of how each looks, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Alt Text, Captions, Transcript, Link Text, Table Accessibility, Keyboard Navigation, Color Independence, Heading Structure (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 7 of 8 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) A video player with a caption button is captioned. (2) The focus ring is a design flaw. (3) A chart is accessible if its colors are bright.

**Instructional Rationale:** Identifying features on an illustrated page is a Remember-level task that anchors each check to something the learner can look for. The quiz asks the learner to go from the look of a feature to its name.

**Content:**

The illustration is a text-free flat drawing of a lesson page. At the top is a wide bar of heading text. Below it is a picture with a small tag icon at one corner. A video frame follows, with a strip of thin text lines along its bottom edge and a small badge at the lower right. Under the video is an underlined bar with a small document icon. In the paragraph below, one underlined phrase is set apart. A grid with a shaded top row and a shaded left column follows. A button has a thick outline around it. At the bottom is a bar chart whose bars differ by pattern as well as by shading. The eight markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Descriptive heading | The wide bar of text at the top of the page. | A real heading that names the page, the start of a logical heading structure. | Use one main heading and nest the others in order. |
| 2 | Image with alt text | A picture with a small tag icon at one corner. | An image whose purpose is described in its alt text. | Describe the purpose, not just the look. |
| 3 | Captioned video | A video frame with a strip of thin text lines along its bottom edge. | A video whose speech appears as timed captions. | Check automatic captions for errors. |
| 4 | Transcript link | An underlined bar with a small document icon beneath the video. | A link to a text version of the video's audio and key visuals. | Place it right next to the video. |
| 5 | Descriptive link | One underlined phrase set apart inside a paragraph. | A link whose words say where it goes. | Avoid "click here". |
| 6 | Table with headers | A grid with a shaded top row and a shaded left column. | A data table whose header cells are marked, so a screen reader pairs each cell with its headings. | Give the table a short caption. |
| 7 | Visible focus | A button with a thick outline around it. | The outline shows which control a keyboard user is on. | Never remove the focus outline without a replacement. |
| 8 | Chart with patterns | A bar chart whose bars differ by pattern as well as shading. | A chart that does not depend on color alone to tell its bars apart. | Add labels or patterns to any chart that uses color to carry meaning. |

**Provenance:** The features follow the chapter sections on alt text, captions, transcripts, link text, table accessibility, keyboard navigation, color independence, and heading structure. The illustration is synthetic, and the sim labels the page "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 8 in the order of the table.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 8 hints the sim shows the summary.

**Feedback:** 8 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can spot an accessible page." Below 7 it lists the labels of the missed features.

**Starting State:** The illustration with eight numbered markers, explore mode active, and the prompt "Hover a marker to see what it is."

**Chapter Anchors:** The chapter lists these features as checks: headings in order, alt text, captions, a transcript, descriptive link text, table headers, visible keyboard focus, and color independence.
</details>

## Scoring Accessibility

Accessibility is scored with ten checks. A failed check is **serious** when it keeps a group of learners out of the content altogether: images with no alt text, text that cannot be read for lack of contrast, video with no captions, or controls that a keyboard cannot reach. When a serious check fails, choose the lower number in a two-number band. Otherwise choose the higher number.

| # | Check | Serious if it fails? |
|---|---|---|
| 1 | Every meaningful image has alt text | Yes |
| 2 | Alt text is useful, not a filename or a single word | No |
| 3 | Decorative images are marked to be skipped | No |
| 4 | Headings are real headings, in order, with no skipped level | No |
| 5 | Text and background colors meet the contrast minimums | Yes |
| 6 | Color is not the only way information is shown | No |
| 7 | Video has captions | Yes |
| 8 | Audio and video also have transcripts or audio description where needed | No |
| 9 | Every function works with a keyboard alone | Yes |
| 10 | The page language is set, links have descriptive text, and tables have header cells | No |

A check that does not apply, such as captions for a resource with no video, counts as passed. A check that was not tested counts as failed until it is tested.

**Worked example: Watershed Basics.** The reviewer applies the checks to the reading from Chapter 3.

| # | Result | Evidence |
|---|---|---|
| 1 | **Fail** | 4 of 5 images have alt text, so one meaningful image has none. |
| 2 | **Fail** | Two of the four alt texts are one word long, "photo". |
| 3 | Pass | The reading has no decorative images, so the check does not apply and counts as passed. |
| 4 | **Fail** | One heading jumps from level 2 to level 4. |
| 5 | **Fail** | Color contrast was not tested, so the check counts as failed until it is. |
| 6 | Pass | The chart uses labels as well as color. |
| 7 | **Fail** | The video has no captions. |
| 8 | Pass | The video's visuals are all described in its narration, so no audio description is needed. |
| 9 | Pass | The quiz and every link work with the keyboard. |
| 10 | Pass | The page language is set, links are descriptive, and the data table has header cells. |

Five of ten checks pass, a share of 50 percent, in the 5 to 6 band. Checks 1, 5, and 7 are serious failures. The reviewer therefore chooses the lower number, **5**, the score on the Chapter 3 worksheet. That worksheet recorded the image, video, heading, and contrast findings. The full check also records the one-word alt text.

The last MicroSim of the chapter is a scoring practice. It shows five resources with their ten check results, and for each one you choose the metric score.

#### Diagram: Accessibility Metric Scorer

<details markdown="1">
<summary>Accessibility Metric Scorer</summary>
Type: microsim
**sim-id:** accessibility-metric-scorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the ten accessibility checks and the Chapter 3 scoring rules to choose the metric score for each of five resources, with at least 4 of 5 scores exactly correct on the first attempt.

**Prerequisites:** Accessibility Metric, WCAG 2.1 AA, Metric Score, Scoring Descriptor (all defined in this chapter or in Chapter 3 above this block).

**Evidence of Mastery:** For each resource the learner chooses a whole-number score from 0 to 10 after seeing the ten check results. A score is correct when it equals the Correct score column in Content. Mastery is at least 4 of 5 scores correct on the first attempt. Opening the check list and the descriptor table is exploration, not evidence.

**Misconceptions:** (1) Every failed check lowers the score equally. (2) A clean automated checker report earns a 10. (3) A check not tested can be skipped.

**Instructional Rationale:** Applying a scoring procedure to new cases is an Apply-level task. Five resources that differ in how many checks fail and whether a serious check fails make the learner use every step: count, band, then choose within the band.

**Content:**

The ten checks, each marked serious or not, are those in the chapter's check table. The descriptor bands applied to the share of checks passed: 0% is 0; 1% to 24% is 1 to 2; 25% to 49% is 3 to 4; 50% to 74% is 5 to 6; 75% to 89% is 7 to 8; 90% to 100% is 9 to 10. Within a two-number band, choose the lower number when a serious check failed and the higher number otherwise. A score of 10 requires every check to pass. A check that does not apply counts as passed, and a check that was not tested counts as failed.

The five resources:

| # | Resource | Checks failed | Checks passed | Share | Band | Serious failure? | Correct score | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|---|
| 1 | Open Algebra | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed. |
| 2 | Watershed Basics | 1, 2, 4, 5, 7 | 5 | 50% | 5 to 6 | Yes, checks 1, 5, and 7 | 5 | Missing alt text, untested contrast, and uncaptioned video are serious, so the lower number applies. |
| 3 | Science Lab Page | 6 and 10 | 8 | 80% | 7 to 8 | No | 8 | Neither failed check is serious, so the higher number applies. |
| 4 | Lecture Video Series | 7, 8, and 10 | 7 | 70% | 5 to 6 | Yes, check 7 | 5 | Videos with no captions are a serious failure, so the lower number applies. |
| 5 | Scanned Worksheets | 1, 2, 3, 4, 5, 6, 8, and 10 | 2 (checks 7 and 9) | 20% | 1 to 2 | Yes, checks 1 and 5 | 1 | Scans have no alt text and weak contrast, and the failures are serious, so the lower number applies. |

**Provenance:** The ten checks and the bands follow the chapter section "Scoring Accessibility" and Chapter 3. The five resources are illustrative cases written for this chapter, and the sim labels them "illustrative examples". Resource 2 is the chapter's worked example.

**Rules:** A score is the band chosen from the share passed, and then the number chosen within the band by the serious-failure rule. Each resource has exactly one correct score. For a band that holds a single number, that number is the score.

**Learner Activity:**

1. The sim shows resource 1 with its ten check results.
2. The learner may open the check list and the descriptor table.
3. The learner chooses a score from 0 to 10, and the choice is committed.
4. The sim shows the count of passes, the band, whether a serious check failed, and the correct score with the Why text.
5. After resource 5 the sim shows the summary.

**Feedback:** 5 resources in the fixed order, one attempt each. Correct: "Correct: [score]. [Why]". Incorrect: "Not quite. [passes] checks passed, which is [share] and the [band] band. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can score accessibility." Below 4 it lists the Why text of each missed resource.

**Starting State:** Resource 1 with all ten results shown and no score chosen. The question shown is "What accessibility score does this resource earn?"

**Chapter Anchors:** The chapter's worked example for Watershed Basics fails checks 1, 2, 4, 5, and 7, passes 5 of 10, and scores 5, with the lower number chosen because checks 1, 5, and 7 are serious failures.
</details>

## Key Takeaways

- **Accessibility** means learners with disabilities can use a resource. The **accessibility metric** is scored against **WCAG** at level AA, which means **WCAG 2.1 AA**, organized under four principles: perceivable, operable, understandable, and robust.
- Images need **alt text** that serves their purpose. A **decorative image** takes empty alt text, and a **complex image description** adds a longer text or a table. **Heading structure** must be real and in order.
- **Color contrast** is measured by a **contrast ratio**, with minimums of 4.5 to 1 for normal text and 3 to 1 for large text. **Color independence** means color is never the only cue.
- **Captions**, a **transcript**, and **audio description** open media to learners who cannot hear or see it. **Keyboard navigation** and a **screen reader** test whether a page can be operated without a mouse or a screen.
- **Link text**, **table accessibility**, **document language**, **accessible math**, and **ARIA labels** handle the details. **Universal Design for Learning** plans for variety, and an **accessibility checker** finds only part of the problems, so the human checks remain.

!!! mascot-celebration "You Can Check Who Gets Left Out"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now check a resource against WCAG 2.1 AA, write useful alt text, measure a contrast ratio, test a page with a keyboard, and score accessibility with evidence. Every learner who can get through a resource is a learner your score helped to count.

[See Annotated References](./references.md)
