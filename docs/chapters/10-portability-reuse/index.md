---
title: "Portability and Reuse Across Platforms"
description: "Explains the portability metric: browser compatibility, no-login access, responsive layout, iframe embedding, export formats, LMS import, Common Cartridge, LTI, offline access, and platform lock-in."
generated_by: claude skill chapter-content-generator
date: "2026-10-20 20:57:21"
version: 1.11
---

# Portability and Reuse Across Platforms

## Summary

Explains how to score portability: browser compatibility, no-login access, iframe embedding, LMS import, Common Cartridge, and the platform lock-in that stops a resource from moving. It finishes the reusability metrics and builds on the components and metadata of the previous chapter. After this chapter you can test whether a resource runs in a browser without a login, embeds in another page, and moves between platforms.

## Concepts Covered

This chapter covers the following 12 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Portability Metric | 15 |
| Browser Compatibility | 2 |
| No-Login Access | 3 |
| Iframe Embedding | 2 |
| Link Sharing | 1 |
| Export Format | 5 |
| LMS Import | 3 |
| Common Cartridge | 1 |
| LTI Integration | 1 |
| Responsive Layout | 1 |
| Offline Access | 1 |
| Platform Lock-In | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)
- [Chapter 4: Open File Formats and Version Control](../04-open-formats-version-control/index.md)
- [Chapter 9: Modularity and Metadata](../09-modularity-metadata/index.md)

---

!!! mascot-welcome "Will It Travel?"
    ![Echo the Loon waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    An open resource is only reusable if it still works when it lands in someone else's school, device, and learning system. This chapter finishes the reusability metrics with portability, and gives you a handful of quick tests you can run in minutes. Let's dive in and check the evidence!

Chapter 9 asked whether a resource is licensed clearly, built in pieces, and described well enough to be found. The last reusability metric asks whether the resource still works once it leaves home. A teacher in another district has a different browser, a different learning management system, a phone-bound class, and sometimes a weak internet connection. Portability is the metric that scores how well a resource copes with all of that. Sam's open chapter scored 7, and the chapter shows what holds it back.

## The Portability Metric

The **portability metric** is metric 10 of the ten, and the last. It asks whether a resource works on other platforms and devices without special accounts, software, or workarounds. Portability protects the Reuse and Redistribute permissions from Chapter 1, because a resource that only works in one place cannot be reused or redistributed elsewhere, whatever its license says. The descriptors below are illustrative.

| Score range | Portability descriptor |
|-------------|------------------------|
| 9 to 10 | Works in major browsers and on phones, needs no login, embeds and imports into learning systems, exports in open formats, and has an offline version |
| 7 to 8 | Works broadly, with one or two limits, such as one component that depends on a particular service |
| 5 to 6 | Works in a limited range of settings, or needs a login or a special tool |
| 3 to 4 | Works only on one platform or device |
| 0 to 2 | Cannot be used outside its original setting |

A reviewer scores the metric by running a handful of tests. Sam ran six on the open chapter, and the table lists the results. The chapter opens in the major browsers and needs no login, which are strong points. Its embedded video depends on a streaming site, wide tables run off the edge of a phone screen, and there is no package for a learning system. That mix puts the chapter at 7.

| Test | Result for Sam's chapter |
|------|--------------------------|
| Opens in at least two major browsers | Pass |
| Opens without a login | Pass |
| Embeds in another page | Partial: the text embeds, but the video depends on a streaming site |
| Reads well on a phone | Partial: wide tables run off the screen |
| Works offline | Partial: the PDF does, but the video does not |
| Imports into a learning system | Not offered |

!!! mascot-thinking "Portable Means It Survives the Move"
    ![Echo the Loon thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Think of portability as a moving-day test. A resource that works only in its original home hasn't really been shared, because it can't live anywhere else.

## Opening It Anywhere

**Browser compatibility** is the ability of a resource to work in the major web browsers, which today include Chrome, Firefox, Safari, and Edge. A resource built on open web standards, such as ordinary HTML and JavaScript, tends to work everywhere. One built on a plug-in, a small add-on that a browser must install, tends to break when browsers stop supporting it. The Flash plug-in is the standard cautionary tale: Adobe ended support at the end of 2020, and the browsers removed it, and teaching resources built on it simply stopped working. A quick test is to open the resource in two different browsers and see whether everything displays and responds.

**No-login access** is the ability to open a resource without creating an account or signing in. A login barrier stops adoption in several ways. A teacher cannot paste a link into a class page if each student must register, and creating accounts raises student privacy questions that Chapter 13 takes up. An open resource should normally be viewable by anyone with its link. The test is to open the address in a private browser window, where no one is signed in, and see whether the content loads.

**Link sharing** is the ability to point others to a resource, or to a specific part of it, with a stable web address. A good address leads to the same place every time and does not depend on who is signed in or on a session that expires. Links to a specific section are especially useful. Sam can send students a link straight to the membrane section instead of the whole chapter. Addresses that change when a site is reorganized break every link that points to them, which is the link rot from Chapter 5.

**Responsive layout** is a page design that adapts to the width of the screen, so that text, images, and tables fit on a phone as well as a desktop. Many learners use phones as their main device, so a page that only works at desktop width excludes them. The test is to make the browser window narrow, or open the page on a phone, and check that text wraps instead of running off the edge and that nothing needs sideways scrolling. A related accessibility rule, WCAG 2.1's reflow criterion, asks for content to fit a narrow screen without scrolling in two directions. Sam's chapter fails on its wide tables.

## Embedding and Learning Systems

**Iframe embedding** is showing a resource inside another page by pointing an iframe at its address, as Chapters 8 and 9 introduced. It is the simplest way for a teacher to put an interactive piece into a course page, and a resource has to cooperate for it to work. Some websites tell browsers not to display them inside other pages, which produces a blank box or a refusal message. The test is to put the address in an iframe on a test page. Before the example, here are the parts: `src` is the address, `width` and `height` are the size, and `title` is a short description that screen readers announce.

```html
<iframe src="https://example.org/sims/cell-size/main.html" title="Cell Size Explorer" width="100%" height="500px"></iframe>
```

An **export format** is a file format in which a resource can be downloaded or exported for use elsewhere. Common choices are HTML for the web, PDF for printing, EPUB for e-readers, Markdown and word processing files for editing, and packages for learning systems. The more formats a resource offers, and the more of them are open, the more places it can go. The table lists common formats and what each is good for.

| Export format | Good for |
|---------------|----------|
| HTML | Putting the resource on a web site or in a course page |
| PDF | Printing and offline reading |
| EPUB | Reading on phones and e-readers |
| Markdown or word processing file | Editing and adapting |
| Common Cartridge package | Importing into a learning system |

**LMS import** is the ability to bring a resource into a learning management system, such as Canvas, Moodle, Blackboard, or D2L Brightspace, so that students reach it from their course page. There are three ways to do it: link to the resource, embed it, or import it as a file. Importing is the most convenient, because the content arrives inside the course, ready to arrange. **Common Cartridge** is a packaging standard, maintained by the 1EdTech consortium, that bundles course content into a single file that many learning systems can import. A resource that offers a Common Cartridge file can be moved into a course in one step.

**LTI integration** is a way for an external tool to run inside a learning system, using the 1EdTech standard called Learning Tools Interoperability. The learning system tells the tool who the student is and which course they are in, so students do not create another account, and the tool can send results, such as a grade, back to the gradebook. It looks like a login, but for the learner it is not one, so it can sit beside the no-login goal for open content. A teacher who wants a MicroSim as a graded activity inside their course will want it to offer LTI.

## Working When Things Go Wrong

**Offline access** is the ability to use a resource without an internet connection. Learners with limited or unreliable connections, whether at home, on a bus, or in a school with weak coverage, rely on it. A downloadable PDF or a packaged copy of the pages is the usual way to offer it. Sam's chapter is partly offline: the text is in the PDF, but the video needs the internet, so a student on a poor connection can read the chapter but not watch the video. A fix is to offer the video as a downloadable file as well.

**Platform lock-in** is a situation in which a resource depends so heavily on one platform or vendor that moving it elsewhere is hard or impossible. It shows up as content that exists only inside one system, as formats that only one program can open, as login walls, and as platforms that offer no way to export. Lock-in is the opposite of what open licensing promises. A license that grants the right to revise and redistribute is empty if the only copy is trapped in a service that will not release it. The table lists signs of lock-in and the questions that reveal them.

| Sign of lock-in | Question to ask |
|-----------------|-----------------|
| Content is created and stored inside a vendor's platform | Can I download all of it, in an editable open format? |
| Only one program opens the files | Can another program read them? |
| The content needs an account to view | Can I view it without signing in? |
| The platform offers no export | If the vendor closed tomorrow, what would remain? |

!!! mascot-warning "If You Can't Export It, You Don't Really Own It"
    ![Echo the Loon warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A friendly platform that hosts your open resource can still lock it in if there's no export. Before you commit, download a copy and check that you can open and edit it somewhere else.

The matcher below gives you eight symptoms that a teacher might meet. Each points to one portability problem.

#### Diagram: Portability Problem Matcher

<details markdown="1">
<summary>Portability Problem Matcher</summary>
Type: microsim
**sim-id:** portability-problem-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** distinguish<br/>
**Learning Objective:** The learner will distinguish which of 8 portability problems each of 8 described symptoms shows, by matching the symptom to its cause.

**Prerequisites:** browser compatibility, no-login access, iframe embedding, responsive layout, offline access, platform lock-in, LMS import, LTI integration (all defined in the chapter above this block).

**Evidence of Mastery:** For each of the 8 symptoms, the learner chooses one of eight problems and presses Check. A choice is correct when it matches the Correct problem column in Content. Mastery is 7 or more of 8 correct on the first attempt. Reading a symptom and changing a choice before pressing Check is exploration and does not count as evidence.

**Misconceptions:** (1) All portability problems are caused by the learner's device. (2) A login is the same as LTI integration. (3) A resource that can be linked can always be embedded. (4) Exporting a PDF solves lock-in.

**Instructional Rationale:** Distinguishing means separating things that look alike by their causes. Each symptom is a different way for a resource to fail to travel, so the learner must link what the teacher sees to the property that is missing.

**Content:**

The eight problems are: Browser compatibility, No-login access, Iframe embedding, Responsive layout, Offline access, Platform lock-in, LMS import, and LTI integration. Each problem is the correct answer for exactly one symptom.

| # | Symptom shown to the learner | Correct problem | Why (shown as feedback) |
|---|------------------------------|-----------------|-------------------------|
| 1 | A teacher pastes a resource's embed code into a course page and sees a blank box with a message that the page refused to connect. | Iframe embedding | The site does not allow its pages to be shown inside other pages. |
| 2 | A student on an older tablet sees a gray square where an interactive should appear, because the resource needs a browser add-on that the tablet does not have. | Browser compatibility | The resource depends on a plug-in that the device's browser does not support. |
| 3 | A link emailed to students opens a sign-in page that asks each student to create an account. | No-login access | The resource cannot be opened without an account. |
| 4 | On a phone, a wide table runs off the right edge of the screen and the reader must scroll sideways. | Responsive layout | The page does not adapt to a narrow screen. |
| 5 | A teacher in a school with an unreliable connection cannot open the resource at home. | Offline access | There is no downloadable version that works without the internet. |
| 6 | A vendor's platform hosts a whole course and offers no way to download the content in any editable form. | Platform lock-in | The content is trapped in one platform with no export. |
| 7 | A teacher wants the resource inside their course as a graded activity that signs students in automatically, but only a plain link is offered. | LTI integration | The resource lacks the standard that passes the student's identity and returns a grade. |
| 8 | A teacher wants to bring a whole unit into the course in one step, but the resource offers only separate web pages. | LMS import | There is no package that a learning system can import. |

**Provenance:** The 8 symptoms are illustrative and written for this chapter, and they describe no real resource or vendor. The problems come from the chapter sections "Opening It Anywhere," "Embedding and Learning Systems," and "Working When Things Go Wrong." The sim labels the symptoms "illustrative."

**Rules:** Each symptom has exactly one correct problem, and each problem is the correct answer for exactly one symptom. A symptom about a page that refuses to display inside another page is Iframe embedding, about a missing add-on is Browser compatibility, about a required account is No-login access, about a page that does not fit a narrow screen is Responsive layout, about no internet is Offline access, about content that cannot be exported is Platform lock-in, about automatic sign-in and grades is LTI integration, and about bringing a unit in one step is LMS import. Mastery is correct first attempts >= 7 of 8.

**Learner Activity:**

1. The learner reads the first symptom.
2. The learner chooses one of the eight problems and presses Check.
3. The sim shows whether the choice is correct and shows the Why text, then moves to the next symptom.
4. After symptom 8, the sim shows the first-attempt score, lists any missed symptom with its Why text, and offers a retry of the missed symptoms.

**Feedback:** Eight symptoms, shown in the order of the table, two attempts each. Correct: "Correct: [problem]. [Why text]." Incorrect on the first attempt: "Not quite," followed by a hint. If the learner chose a problem the symptom does not mention, the hint is "Ask what is missing: a connection, an account, a screen size, an export, or a standard." If the learner chose LTI integration for an account problem, the hint is "LTI passes the student's identity from the learning system, so students do not make new accounts." After a second wrong choice the correct problem and Why text are revealed and the symptom counts as missed. The score "Correct on first attempt: n of 8" is shown at the end, and the sim states whether mastery was reached.

**Starting State:** The first symptom is shown with the eight problems listed and no choice made. The question on screen is "Which portability problem does this symptom show?"

**Chapter Anchors:** The chapter states that Flash support ended at the end of 2020, that Common Cartridge is maintained by 1EdTech, that LTI passes a student's identity and returns grades, and that the matcher has 8 symptoms.
</details>

!!! mascot-tip "Test Like a Stranger"
    ![Echo the Loon giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Open the resource in a private window, on a phone, and in a second browser. In five minutes you'll have run most of the portability test, using nothing but what any other teacher would have.

## Summary

This chapter covered the last reusability metric and what evidence supports it. The key points are:

- The portability metric asks whether a resource works on other platforms and devices without special accounts, software, or workarounds.
- Browser compatibility, no-login access, link sharing, and responsive layout decide whether a resource opens everywhere.
- Iframe embedding, export formats, LMS import, Common Cartridge, and LTI integration decide whether it fits into learning systems.
- Offline access matters for learners with weak connections, and platform lock-in empties an open license.
- A reviewer runs a handful of quick tests: two browsers, a private window, a phone-width window, and an embed on a test page.

!!! mascot-celebration "You've Finished the Ten Metrics"
    ![Echo the Loon celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now run the portability tests, and with Chapters 4 to 9 you've met every one of the ten metrics, five for quality and five for reusability. Chapter 11 puts them together in a manual review, from scoring by hand to an adopt, revise, or reject decision.
