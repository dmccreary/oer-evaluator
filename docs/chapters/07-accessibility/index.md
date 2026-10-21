---
title: "Accessibility"
description: "Explains the accessibility metric and WCAG 2.1 AA: alt text, headings, color contrast, captions, keyboard and screen reader use, accessibility checkers, and universal design for learning."
generated_by: claude skill chapter-content-generator
date: "2026-10-20 20:48:47"
version: 1.11
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

!!! mascot-welcome "Can Everyone Use It?"
    ![Echo the Loon waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A resource that some of your students can't read, hear, or navigate isn't finished, however good its content is. In this chapter you'll learn the standard that defines accessible, the checks that matter most, and how to find the barriers before your students do. Let's dive in and check the evidence!

Chapters 5 and 6 asked whether a resource is right and whether it fits. This chapter asks whether every learner can get to it. It covers metric 4, Accessibility, and the standard that gives the metric its checks. Sam's open chapter on cell structure scored 3 here, the lowest of its quality scores, and the chapter shows why and how each problem can be repaired. Because accessibility problems are usually invisible to the people who do not have them, the chapter relies on checks you can run yourself and tools that run them for you.

## What Accessibility Means

**Accessibility** is the practice of designing resources so that people with a wide range of abilities can perceive, understand, navigate, and use them, with or without assistive technology. Assistive technology means tools that people use to work around a barrier, such as screen readers or magnifiers. The abilities involved include vision, hearing, movement, and thinking and learning. A person may be blind or have low vision, be deaf or hard of hearing, be unable to use a mouse, or have dyslexia or a difficulty with attention. Barriers can also be temporary or situational: a broken arm, bright sunlight on a screen, or a noisy room all make a resource harder to use.

Accessibility matters for two reasons. The first is fairness and, in many places, law: in the United States, for example, the Americans with Disabilities Act and Section 504 of the Rehabilitation Act apply to many schools and colleges. The second is that accessible design helps almost everyone. This is sometimes called the curb-cut effect, after the sloped cuts in sidewalks, which were built for wheelchairs and are used by people with strollers, suitcases, and bicycles. Captions built for deaf viewers help someone watching in a noisy room, and clear headings help every reader find a section. This book explains concepts and is not legal advice.

Sam's class makes the idea concrete. One student uses a screen reader, one has low vision and magnifies the screen, one has dyslexia, and one has a hearing loss. The table shows what four features of the open chapter do to them.

| Feature of the open chapter | Who it blocks | What happens |
|-----------------------------|---------------|--------------|
| Four diagrams with no alt text | The screen reader user | The diagrams, which carry the lesson, are simply missing |
| Pale gray text labels on a white background | The student with low vision, and anyone in glare | The labels are too faint to read |
| An eight-minute video with no captions | The student with hearing loss, and anyone with sound off | The video's content is unavailable |
| Headings that jump from level 2 to level 4 | The screen reader user | The chapter's outline is confusing to move through |

The **accessibility metric** is metric 4 of the ten. It scores a resource against the technical standard introduced in the next section, using the checks in this chapter: alt text on images, headings in order, text contrast, captions on video, and the ability to use the page by keyboard and screen reader. Chapter 3's metric card listed the evidence that the metric requires. For Sam's chapter, four of the five checks Sam ran failed and one passed, because the page text itself can be read by a screen reader. That pattern falls in the 1 to 3 range, and Sam scored it 3.

!!! mascot-thinking "Accessibility Helps Everyone"
    ![Echo the Loon thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Notice that every fix for one group turns out to help others too. Captions help in a noisy room, high contrast helps in glare, and clear headings help every reader find their place. Think of accessibility as better design, not extra work for a few.

## WCAG and the AA Standard

How do you decide what counts as accessible? **WCAG**, the Web Content Accessibility Guidelines, is the international technical standard for it. The World Wide Web Consortium publishes it through its Web Accessibility Initiative. WCAG organizes its guidance under four principles, summarized by the acronym POUR. Content must be **perceivable**, which means users can take it in through at least one sense. It must be **operable**, so users can navigate and use it. It must be **understandable**, so users can follow both the content and how the page behaves. And it must be **robust**, so that it works with current and future technologies, including assistive technology. Each principle breaks down into numbered, testable statements called success criteria.

WCAG comes in versions. Version 2.0 appeared in 2008, version 2.1 in 2018, and version 2.2 in 2023, each adding criteria while keeping the earlier ones. Each success criterion has a conformance level of A, AA, or AAA. The table applies the four principles to Sam's chapter.

| Principle | What it asks | Example from Sam's chapter |
|-----------|--------------|----------------------------|
| Perceivable | Can users take it in through some sense? | The diagrams have no text alternative, so blind users cannot perceive them |
| Operable | Can users navigate and operate it? | The page can be moved through, but the heading levels are out of order |
| Understandable | Can users follow it? | The language of the page is not declared, so a screen reader may mispronounce text |
| Robust | Does it work with assistive technology? | The page text is real text, so screen readers can read it |

**WCAG 2.1 AA** is the target this book uses: version 2.1 of the guidelines at conformance level AA. Level A covers the most basic barriers. Level AA adds the criteria that remove the major remaining barriers, and meeting AA means meeting every A and AA criterion. Level AAA is the strictest, and it is not expected for whole resources because some of its criteria cannot be met for all content. Laws and policies often name WCAG 2.1 AA. For example, recent U.S. Department of Justice rules for state and local government websites, which include public schools and colleges, name it as the technical standard. Version 2.2 is a later release that adds a few criteria, and the course description sets 2.1 AA as this book's baseline.

The table lists the checks this chapter covers, with the success criterion each comes from and its level.

| Check | WCAG success criterion | Level |
|-------|------------------------|-------|
| Text alternative for images (alt text) | 1.1.1 Non-text Content | A |
| Captions for prerecorded video | 1.2.2 Captions (Prerecorded) | A |
| Audio description for prerecorded video | 1.2.5 Audio Description (Prerecorded) | AA |
| Headings and tables marked up properly | 1.3.1 Info and Relationships | A |
| Color not the only signal | 1.4.1 Use of Color | A |
| Text contrast | 1.4.3 Contrast (Minimum) | AA |
| Everything works by keyboard | 2.1.1 Keyboard | A |
| Link text makes sense | 2.4.4 Link Purpose (In Context) | A |
| Page language declared | 3.1.1 Language of Page | A |

!!! mascot-encourage "You Don't Have to Memorize the Numbers"
    ![Echo the Loon encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    A list of criteria like that looks heavy, and nobody carries it in their head. Keep the four POUR ideas in mind, and use the table and a checker tool for the rest. Most reviewers learn the handful of checks that catch most problems.

## Images and Alt Text

**Alt text**, short for alternative text, is a brief written description of an image, stored in the image's `alt` attribute in HTML, as Chapter 4 showed. A screen reader reads it aloud in place of the image, so a reader who cannot see the picture still gets what it contributes. Good alt text conveys the image's purpose in its context, not just its appearance. It is short, usually a sentence or two, and it does not begin with "image of" or "picture of," because the screen reader already announces that it is an image. For the membrane diagram in Sam's chapter, which shows a double layer of fat-based molecules with proteins crossing it, good alt text reads, "Diagram of the cell membrane: two layers of lipid molecules with protein channels passing through both layers."

Not every image needs a description. A **decorative image** is an image that adds no information, such as a divider line, a background texture, or an icon that repeats the words beside it. A decorative image should have an empty alt attribute, written `alt=""`, which tells screen readers to skip it. Giving a divider line a description would only make the reader listen to noise, and leaving the attribute off altogether often makes screen readers read the file name instead.

A **complex image description** is a longer text that explains an image carrying more information than a sentence can hold, such as a chart, a map, or a detailed diagram. The usual pattern is two parts. The alt text says what the image is and where to find the full explanation, and a long description gives the details, either in the nearby text or in a data table beside the chart. A chart of yeast growth over five hours, for example, has short alt text, "Bar chart of yeast cell counts rising each hour over five hours; the numbers are in the table below," with the table placed under it.

!!! mascot-warning "Automatic Descriptions Miss the Point"
    ![Echo the Loon warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Tools that write alt text automatically often name what is pictured but miss why it's there. Check every description against one question: what does a reader who can't see this image need to know?

Writing alt text is a judgment, and the exercise below gives you eight images with a proposed alt text each. Decide whether each one works.

#### Diagram: Alt Text Judge

<details markdown="1">
<summary>Alt Text Judge</summary>
Type: microsim
**sim-id:** alt-text-judge<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** critique<br/>
**Learning Objective:** The learner will critique the alt text proposed for each of 8 images as good, too vague, too long, or unnecessary because the image is decorative.

**Prerequisites:** alt text, decorative image, complex image description (all defined in the chapter section "Images and Alt Text" above this block).

**Evidence of Mastery:** For each of the 8 images, the learner reads the image description and the proposed alt text, chooses one of four verdicts, and presses Check. A verdict is correct when it matches the Correct verdict column in Content. Mastery is 7 or more of 8 correct on the first attempt. Changing a verdict before pressing Check is exploration and does not count as evidence.

**Misconceptions:** (1) Longer alt text is always better. (2) Every image needs alt text with words in it. (3) Alt text should start with "image of." (4) One word that names the image is enough.

**Instructional Rationale:** Critiquing means judging a work against criteria. Giving the learner both what the image shows and why it appears, then a proposed alt text, lets the learner apply the purpose-based test instead of checking only whether text is present.

**Content:**

The four verdicts are: Good, Too vague, Too long, and Should be empty (the image is decorative). The rule of thumb used here is that alt text of more than two sentences belongs in a separate long description. Each image has a description of what it shows and why it appears in the resource.

| # | What the image shows and why it is there | Proposed alt text | Correct verdict | Why (shown as feedback) |
|---|------------------------------------------|-------------------|-----------------|-------------------------|
| 1 | A microscope photo of onion skin cells, used to show the cell wall | "Photo" | Too vague | It does not say what the photo shows or why it is there. |
| 2 | The same microscope photo of onion skin cells, used to show the cell wall | "Micrograph of onion skin cells: rectangular cells with thick walls and a visible nucleus in each." | Good | It says what the image is and what it shows about cell walls. |
| 3 | A wavy line used only to separate two sections | "Divider image of a wavy line" | Should be empty | The line adds no information, so the alt text should be empty and screen readers can skip it. |
| 4 | A bar chart of yeast cell counts over five hours, with a data table beside it | "Chart" | Too vague | It does not say what the chart shows or point to the table. |
| 5 | The same bar chart of yeast cell counts over five hours, with a data table beside it | "Bar chart of yeast cell counts rising each hour over five hours; the numbers are in the table below." | Good | It says what the chart shows and where the full data is. |
| 6 | A labeled diagram of the cell membrane, used to explain how substances cross it | "Image of a diagram of the cell membrane. The diagram shows the membrane, which is made of a phospholipid bilayer with embedded proteins. The heads of the phospholipids face the water on both sides and the tails face each other inside, and channel proteins span both layers and let some substances pass through." | Too long | It is far more than two sentences, and it starts with "image of." The details belong in a long description, with a short alt text. |
| 7 | A small lightbulb icon placed next to a heading that already says "Tip" | "Lightbulb" | Should be empty | The icon repeats what the heading says, so describing it adds noise. |
| 8 | A photo of a student at a microscope, used to show the lab setup | "Student looking through a microscope while adjusting the focus knob." | Good | It says who and what is shown and why the photo matters. |

**Provenance:** The 8 images, descriptions, and alt texts are illustrative and describe no real resource. The criteria come from the chapter section "Images and Alt Text." The two-sentence limit is the chapter's rule of thumb and is not a WCAG requirement. The sim labels the scenarios "illustrative."

**Rules:** Alt text is Good when it states what the image is and what it contributes in context, in no more than two sentences. It is Too vague when it names the image type or a single word without its contribution. It is Too long when it exceeds two sentences or repeats details that belong in a long description. An image that adds no information beyond adjacent text, or that is purely visual, should have empty alt text, so any non-empty alt text for it has the verdict Should be empty. Each of the 8 images fits exactly one verdict. Mastery is correct first attempts >= 7 of 8.

**Learner Activity:**

1. The learner reads what the first image shows and why it is there, then reads the proposed alt text.
2. The learner chooses one of the four verdicts and presses Check.
3. The sim shows whether the verdict is correct and shows the Why text, then moves to the next image.
4. After image 8, the sim shows the first-attempt score, lists any missed image with its Why text, and offers a retry of the missed images.

**Feedback:** Eight images, shown in the order of the table, two attempts each. Correct: "Correct: [verdict]. [Why text]." Incorrect on the first attempt: "Not quite," followed by a hint. If the learner chose Good for a flawed alt text, the hint is "Ask whether it says what the image contributes, in a sentence or two." If the learner chose a flaw for a good alt text, the hint is "This one says what the image shows and why it matters." If the learner chose Too vague or Too long for a decorative image, the hint is "Ask whether the image adds any information at all." After a second wrong verdict the correct verdict and Why text are revealed and the image counts as missed. The score "Correct on first attempt: n of 8" is shown at the end, and the sim states whether mastery was reached.

**Starting State:** The first image's description and proposed alt text are shown with the four verdicts and no choice made. The question on screen is "Does this alt text work for a reader who cannot see the image?"

**Chapter Anchors:** The chapter states that good alt text conveys purpose in a sentence or two, that decorative images get empty alt text, that a complex image gets a short alt text plus a long description, and that the judge has 8 images.
</details>

## Headings, Color, and Contrast

**Heading structure** is the order and nesting of a page's headings. In a well-built page the headings are real heading elements, not bold text, with one top-level heading, followed by second-level headings, third-level headings beneath them, and no levels skipped. Screen reader users depend on headings: many move through a page by jumping from heading to heading, much as a sighted reader skims. A page whose headings skip from level 2 to level 4, as Sam's chapter does, gives them a confusing outline. The repair costs a few seconds. Change the level-4 heading to level 3, and the outline makes sense. This builds on the headings and subheadings from Chapter 6, which covered them as a readability aid.

**Color contrast** is the difference in brightness between the text, or other content, and its background. Low contrast makes text hard to read for people with low vision or color vision deficiency, and for everyone in glare. WCAG sets minimum levels for it, measured by a number.

The **contrast ratio** is that number. It compares the brightness of two colors, on a scale from 1:1, no difference, to 21:1, black on white. WCAG 2.1 AA sets two thresholds. Normal text needs a ratio of at least 4.5:1. Large text, which means at least 18 point, or at least 14 point if bold, needs at least 3:1, and so do meaningful graphics and parts of interface controls. You do not calculate the ratio by hand, because a contrast checker tool does it from the two color codes. As an example, this book's mascot boxes put white text on indigo for 7.7:1, and white text on burnt orange for 5.0:1, both comfortably above 4.5. Sam's pale gray labels on white measure about 2.3:1, which fails.

**Color independence** is the principle that color should never be the only way information is conveyed. Imagine a chart whose lines differ only in red and green. Roughly one man in twelve has some difficulty telling those two colors apart, and a chart printed in black and white loses the distinction altogether. The repair is a second signal: direct labels on the lines, different line patterns, or different marker shapes. "Required fields are shown in red" fails the check, while "Required fields are marked with an asterisk and shown in red" passes.

!!! mascot-tip "Measure Contrast, Don't Eyeball It"
    ![Echo the Loon giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Your eyes and your screen both mislead you about contrast. Paste the two color codes into a contrast checker and compare the ratio with 4.5 for normal text and 3 for large text.

The checker below gives you eight color pairs, each with its measured ratio, and asks you to apply the thresholds.

#### Diagram: Contrast Ratio Check

<details markdown="1">
<summary>Contrast Ratio Check</summary>
Type: microsim
**sim-id:** contrast-ratio-check<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Template:** https://github.com/dmccreary/ibook-skills/tree/main/docs/sims/color-accessibility-checker-microsim<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of 8 text and background color pairs meets WCAG 2.1 AA contrast, by comparing the pair's contrast ratio with the threshold for its text size.

**Prerequisites:** color contrast, contrast ratio, WCAG 2.1 AA (all defined in the chapter above this block).

**Evidence of Mastery:** For each of the 8 pairs, the learner chooses Pass or Fail for WCAG 2.1 AA and presses Check. A choice is correct when it matches the Correct result column in Content. Mastery is 7 or more of 8 correct on the first attempt. Changing a choice before pressing Check is exploration and does not count as evidence.

**Misconceptions:** (1) A pair that looks readable on screen passes. (2) The same pair has the same result at any text size. (3) A ratio just below the threshold passes because it is close. (4) Light text on a mid-tone background always has good contrast.

**Instructional Rationale:** Judging means applying a criterion to a case. The ratio is given, so the skill practiced is applying the right threshold to the right text size. Pairs that share a color but differ in size, or that sit just either side of a threshold, force the learner to read the number against the rule.

**Content:**

The thresholds are: normal text passes at a contrast ratio of 4.5 or higher, and large text passes at 3.0 or higher. Large text is at least 18 point, or at least 14 point if bold. Each pair is shown as a sample of text in the foreground color on the background color, with its size, its color codes, and its measured ratio.

| # | Foreground | Background | Text size | Contrast ratio | Correct result | Why (shown as feedback) |
|---|------------|------------|-----------|----------------|----------------|-------------------------|
| 1 | #000000 | #FFFFFF | Normal | 21.00 | Pass | 21.00 is above 4.5. |
| 2 | #767676 | #FFFFFF | Normal | 4.54 | Pass | 4.54 is above 4.5, narrowly. |
| 3 | #777777 | #FFFFFF | Normal | 4.48 | Fail | 4.48 is below 4.5, so it fails even though it looks the same as pair 2. |
| 4 | #AAAAAA | #FFFFFF | Normal | 2.32 | Fail | 2.32 is below 4.5. |
| 5 | #949494 | #FFFFFF | Large | 3.03 | Pass | Large text needs only 3.0, and 3.03 is above it. |
| 6 | #949494 | #FFFFFF | Normal | 3.03 | Fail | Normal text needs 4.5, and 3.03 is below it. |
| 7 | #FFFFFF | #3949AB | Normal | 7.73 | Pass | 7.73 is above 4.5. |
| 8 | #FFFFFF | #FF8800 | Normal | 2.39 | Fail | 2.39 is below 4.5, so white on this orange is too faint. |

**Provenance:** The contrast ratios are computed with the WCAG relative luminance formula from the color codes shown, rounded to two decimal places. The thresholds of 4.5 and 3.0 come from WCAG 2.1 success criterion 1.4.3. The pairs are illustrative selections. The sim labels the pairs "illustrative."

**Rules:** Contrast ratio = (L1 + 0.05) ÷ (L2 + 0.05), where L1 is the relative luminance of the lighter color and L2 of the darker. Normal text passes when ratio >= 4.5. Large text passes when ratio >= 3.0. The ratios shown are fixed and are not computed by the learner. Each pair has exactly one correct result. Mastery is correct first attempts >= 7 of 8.

**Learner Activity:**

1. The learner reads pair 1: the sample text, its size, and its contrast ratio.
2. The learner chooses Pass or Fail and presses Check.
3. The sim shows whether the choice is correct and shows the Why text, then moves to the next pair.
4. After pair 8, the sim shows the first-attempt score, lists any missed pair with its Why text, and offers a retry of the missed pairs.

**Feedback:** Eight pairs, shown in the order of the table, two attempts each. Correct: "Correct: [result]. [Why text]." Incorrect on the first attempt: "Not quite," followed by a hint. If the learner chose Pass for a failing pair, the hint is "Compare the ratio with the threshold for this text size." If the learner chose Fail for a passing pair, the hint is "Check whether this is large text, which needs only 3.0." After a second wrong choice the correct result and Why text are revealed and the pair counts as missed. The score "Correct on first attempt: n of 8" is shown at the end, and the sim states whether mastery was reached.

**Starting State:** The first pair is shown as sample text on its background with its size and ratio, and no choice made. The question on screen is "Does this pair meet WCAG 2.1 AA?"

**Chapter Anchors:** The chapter states that normal text needs a ratio of at least 4.5:1, that large text needs at least 3:1, that white on indigo measures 7.7:1 and white on burnt orange 5.0:1, and that the checker has 8 pairs.
</details>

## Video and Audio

**Captions** are text versions of the speech and important sounds in a video, shown in time with the video. WCAG Level A requires captions for prerecorded video that has sound. They serve people who are deaf or hard of hearing, and also people watching with the sound off, in a noisy place, or in a language they are still learning. Automatic captions are a useful first draft but contain errors, especially with technical words, so someone must read and correct them. Sam's chapter has an eight-minute video with no captions at all, which means a deaf student has no access to it. The fix is to add a caption file, which most video platforms accept.

A **transcript** is a complete text version of the audio in a recording, and of the important visuals too, provided as a separate document. It is the main solution for audio-only content such as a podcast, where captions do not apply. It also helps people who prefer to read, makes content searchable, and can be turned into braille for readers who are both deaf and blind. A transcript is a useful companion to captions but does not replace them.

**Audio description** is narration that tells listeners what is happening visually in a video when the soundtrack does not already say it. Level AA requires it for prerecorded video. It serves people who are blind or have low vision. A video that shows a labeled diagram while a narrator says "as you can see here, this part controls the flow" leaves a blind viewer guessing. Two fixes work. The narrator can say the details aloud, and then no separate description is needed, or a second version of the video can carry added description.

## Keyboards and Screen Readers

**Keyboard navigation** is the ability to use every function of a page with the keyboard alone. People who cannot use a mouse, including people with limited movement and people who use screen readers, rely on it. Keyboard users move between links and controls with the Tab key and activate them with Enter or the space bar, and they need a visible highlight that shows where they are. A page fails this check if a control can only be reached by a mouse, or if the keyboard gets stuck inside one element and cannot leave.

!!! mascot-tip "Put the Mouse Away"
    ![Echo the Loon giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Try using the resource for two minutes with the keyboard only. If you can't reach a link or control, or you can't tell where you are on the page, that's a finding you can write down.

A **screen reader** is software that reads the content of a screen aloud, or sends it to a braille display. Common ones include NVDA and JAWS on Windows, VoiceOver on Apple devices, and TalkBack on Android. A screen reader user moves through a page by headings, links, form controls, and tables rather than line by line, and the reader announces what each element is. Everything a screen reader says comes from the page's underlying markup. That is why alt text, headings, and labels matter, and why a page can look perfect and be unusable.

You can hear the difference yourself. Sam turned on a free screen reader and listened to five minutes of the open chapter. At each diagram, the reader said only "graphic," or read out a file name. When Sam asked it to list the headings, it announced them in an order that jumped from level 2 to level 4. The table sets what Sam heard against what a repaired page should say.

| Element | What Sam heard | What a repaired page says |
|---------|----------------|---------------------------|
| A diagram with no alt text | "Graphic" or the file name | A short description of what the diagram shows |
| The heading list | Levels 1, 2, then 4 | Levels in order, with no gap |
| A link that reads "click here" | "Click here, link" | A link whose words describe the destination |

Several smaller checks follow from how screen readers work. **Link text** is the words of a link, and it has to make sense when heard on its own, because users often list all the links on a page. "Read the Creative Commons license" tells a listener where the link goes. "Click here" tells them nothing, and so does a bare web address read out letter by letter. Two links that go to different places should not share the same words.

**Table accessibility** is the practice of marking up a data table so that a screen reader can announce which row and column each cell belongs to. A table should use proper header cells for its column and row headings, stay simple, and avoid merged cells where possible. A table is for data, never for page layout. The tables in this book follow this rule.

**Document language** is the human language that a page declares in its markup, such as English. A screen reader uses the declaration to choose the right pronunciation. Without it, a reader may pronounce English words with the wrong accent or fail on other languages. Passages in another language should be marked separately: when Sam adds the Spanish vocabulary list, that passage should be marked as Spanish so that the reader switches to Spanish pronunciation.

**Accessible math** means writing equations in a form that assistive technology can read, which means real text or a standard such as MathML, not a picture of an equation. A screenshot of a formula is a closed box to a screen reader. If an image is the only option, its alt text must give the full equation in words. Equation tools such as MathJax and KaTeX turn written equations into rendered math, and many can output readable structure.

**ARIA labels** are attributes from a standard called WAI-ARIA that give a name, role, or description to an element when plain HTML cannot. Before the example, here is the idea: a button whose visible content is only the symbol × has no name a screen reader can say. The `aria-label` attribute supplies one.

```html
<button aria-label="Close the glossary">×</button>
```

A screen reader announces this as "Close the glossary, button." ARIA has a first rule: use a built-in HTML element when one does the job, and add ARIA only to fill a gap. Wrong ARIA can make a page worse than none, because it can tell a screen reader something untrue.

## Checking and Designing for Everyone

An **accessibility checker** is a tool that scans a page or document for accessibility problems. Free browser tools such as WAVE, axe, and the Lighthouse audit in Chrome, and checkers built into Word, PowerPoint, and Acrobat, find missing alt text, low contrast, skipped headings, and unlabeled controls in seconds. They are fast, and they are not enough. A tool can see that alt text exists but not whether it is any good, can see that a link has words but not whether they make sense, and cannot judge whether captions are accurate or the reading order is sensible. A reviewer therefore runs a checker first and then adds the manual checks in this chapter: the keyboard test, a few minutes with a screen reader, and a look at the alt text and links.

!!! mascot-warning "A Clean Report Isn't Proof"
    ![Echo the Loon warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    An accessibility checker can pass a page whose alt text says "image" on every picture. Treat a clean report as the start of your review, and follow it with the keyboard test and a short screen reader listen.

**Universal Design for Learning**, or UDL, is a framework for designing instruction that works for the widest range of learners from the start. Developed by the organization CAST, it rests on three principles: offer multiple means of engagement, so learners have reasons to care; multiple means of representation, so information comes in more than one form; and multiple means of action and expression, so learners can show what they know in more than one way. Accessibility is the floor, and UDL is the design approach built on top of it. For Sam's unit, a UDL approach offers the chapter's text, a captioned video, and a labeled diagram with a description, and lets students show their understanding through a written answer, a drawing, or a spoken explanation.

## Summary

This chapter showed how to score the accessibility metric and what evidence supports it. The key points are:

- Accessibility is designing so that people with a wide range of abilities can use a resource, and it helps almost everyone.
- WCAG organizes its guidance under four principles, perceivable, operable, understandable, and robust, and this book targets WCAG 2.1 AA.
- Alt text describes an image's purpose in a sentence or two, decorative images get empty alt text, and complex images need a long description.
- Headings should follow in order, text needs a contrast ratio of at least 4.5 to 1 (3 to 1 for large text), and color should never be the only signal.
- Captions, transcripts, and audio description make video and audio available to people who cannot hear or see them.
- Keyboard navigation and screen reader use depend on link text, table markup, a declared page language, accessible math, and sometimes ARIA labels.
- An accessibility checker finds many problems but not all, so manual checks are part of every review.
- Universal Design for Learning builds options into instruction from the start.

!!! mascot-celebration "You Can Find the Barriers"
    ![Echo the Loon celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now run the key WCAG 2.1 AA checks on a resource, judge alt text and contrast, and back an accessibility score with evidence. Chapter 8 turns to the last quality metric: whether learners can practice and get feedback.
