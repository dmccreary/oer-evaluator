---
title: "Portability and Reuse Across Platforms"
description: "Explains how to score portability: browser compatibility, no-login access, iframe embedding, LMS import, Common Cartridge, and the platform lock-in that stops a resource from moving."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:25:16"
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

!!! mascot-welcome "Can It Travel?"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A resource that is open, well made, and easy to find still fails a teacher if it will not open on her laptop, asks her for an account, or breaks inside her course page. This chapter gives you the tests that tell you whether a resource can travel. Let's dive in and check the evidence!

Chapter 9 asked whether a reuser can find a resource and lift out the part she needs. This chapter asks the last reusability question: once she has it, will it work where she wants to use it? A resource that runs only in one company's system, needs a login, or falls apart on a phone is not portable, however good its license. The tenth and last metric of the rubric measures that, and it finishes the ten-metric rubric.

## The Portability Metric

The **portability metric** is the tenth metric of the rubric. It asks whether a resource runs in a browser with no login and can be shared or embedded elsewhere. A portable resource goes with the reuser to wherever she teaches: a course page, a learning management system, a phone, a classroom with a weak internet connection. The metric is scored with ten checks, listed at the end of this chapter. The sections between them take each idea in turn.

**Worked example: five questions a reuser asks.** A teacher who finds an open simulation asks five questions before she commits to it, and each one is a portability check.

| The question | What it tests |
|---|---|
| Will it open on my computer and my students' devices? | Browser compatibility and responsive layout |
| Do my students need an account? | No-login access |
| Can I put it on my course page? | Iframe embedding and link sharing |
| Can I take a copy, or bring it into my LMS? | Export format and LMS import |
| Will I be stuck if the host disappears? | Platform lock-in and offline access |

### Browser Compatibility

**Browser compatibility** is a resource's ability to work correctly in the main web browsers, such as Chrome, Firefox, Safari, and Edge, and in recent versions of each. Resources built from open web standards, which means plain HTML, CSS, and JavaScript, usually work everywhere. Resources that depend on browser plug-ins do not. Adobe Flash is the cautionary example: it powered many educational animations and was discontinued at the end of 2020, and the content that depended on it stopped working. A reviewer opens a resource in at least three browsers and notes any that fail.

### No-Login Access

**No-login access** means a learner or teacher can open and use a resource without creating an account or signing in. A login is a barrier in three ways. It stops a resource from embedding in someone else's page, because the frame would show a sign-in form. It blocks sharing by link, since the person who receives the link cannot open it. And it adds a privacy burden, because an account holds personal data. Some content, such as an answer key for teachers, may reasonably need a login. A resource that claims to be open should offer its learner-facing content without one.

### Iframe Embedding

**Iframe embedding** is the placing of a resource inside another page, as Chapter 9 introduced. A component may pass the test on its own and still fail on a particular platform, for three common reasons. The server may tell browsers not to show the page inside a frame, which some sites do for security. The page may be served over an insecure connection, which a secure page's browser refuses to mix in. Or the platform may strip the frame out of the pages its users write. So a reviewer tests the embed on more than one platform, and records which worked.

### Link Sharing

**Link sharing** is the ability to send a person a web address that opens the resource, or a specific part of it, directly. A good link is permanent, goes straight to the content, and works for the person who receives it. Links fail when the address changes with every visit, when it opens a home page instead of the component, or when the link only works for someone already signed in. For a resource made of components, each component should have its own address, as the modularity metric asked.

## Moving Content Between Systems

### Export Format

An **export format** is a form in which a resource or a copy of it can be downloaded and kept, ideally in an open format from Chapter 4, such as HTML, Markdown, or a standard package. Export is the exit door. A resource that can be exported can be backed up, moved to a new host, and worked on offline. A resource whose only copy lives inside a web service, with no download, is exactly as portable as the service is permanent.

### LMS Import

**LMS import** is the ability to bring a resource into a learning management system, the software that schools use to run courses, such as Canvas, Moodle, Blackboard, or Brightspace. A teacher can bring an OER into an LMS in four ways: she can link to it, embed it, upload its files, or import it as a package. The more of these a resource supports, the more teachers can use it where they already work. A reviewer tests at least the link and the embed in a real LMS, or a test site, and notes what happened.

### Common Cartridge

**Common Cartridge** is a standard from 1EdTech, the education technology standards group, for packaging course content so that it can be imported into different learning management systems. A cartridge is a single compressed file that holds the content together with a manifest, a list that says what is inside and how it is organized. A unit exported as a Common Cartridge from one LMS can be imported into another, which is why it is the common exchange form for course material. Not every resource offers one, but those that do travel farther.

### LTI Integration

**LTI integration** uses Learning Tools Interoperability, a 1EdTech standard that lets an external tool open inside an LMS and exchange information with it, such as sending a learner's score back to the gradebook. An LTI tool looks like part of the course and runs on another company's server. It is more powerful than a link and more demanding, because it passes information about learners from one system to another, which raises the privacy questions of [Chapter 13](../13-automated-checks-cost-privacy/index.md). For the portability metric, LTI counts as a plus where a resource claims an LMS integration, and not as a requirement.

## Reaching Every Learner and Every Setting

### Responsive Layout

A **responsive layout** is a page design that adapts to the size of the screen, so that the same page is readable on a phone, a tablet, and a large monitor. A page with a fixed width forces a phone user to scroll sideways and pinch, and a resource inside an iframe on a narrow page overflows. Responsive pages use flexible widths and text that wraps. A reviewer tests by narrowing the browser window to the width of a phone and checking that nothing is cut off or overlaps.

### Offline Access

**Offline access** is the ability to use a resource without an internet connection, by downloading it or saving it first. It matters for classrooms and homes with unreliable connections, for field trips, and for learners who pay for data. A single web page with its files can often be saved and opened from a folder, as long as it does not load code or images from elsewhere on the web. A resource that offers a download, or that works from a saved folder, gains here.

### Platform Lock-In

**Platform lock-in** is the dependence of a resource on one platform in a way that makes leaving costly or impossible. Signs include content stored only in a vendor's proprietary format, no export, features that exist only inside the vendor's system, and accounts that would be lost on leaving. Lock-in is a risk to the author and to every reuser, because the resource lives only as long as the platform's business model. The test is simple: could you move the resource to another host in an afternoon, with nothing lost?

!!! mascot-warning "A Free Platform Can Still Be a Cage"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A resource can be free to read and open-licensed and still live only inside one vendor's system, with no export and no copy. Look for a way out before you rely on it, and score the metric on whether you could actually leave.

The first MicroSim of the chapter sorts barriers. It shows ten problems that a reuser might meet, and for each one you name the portability idea it breaks.

#### Diagram: Portability Barrier Sorter

<details markdown="1">
<summary>Portability Barrier Sorter</summary>
Type: microsim
**sim-id:** portability-barrier-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of ten reuse problems by the portability idea it breaks, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** The Portability Metric and the ten portability sections of this chapter (all defined above this block).

**Evidence of Mastery:** For each problem the learner commits one of ten ideas. A choice is correct when it matches the Correct idea column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the idea list is exploration, not evidence.

**Misconceptions:** (1) A login problem and a lock-in problem are the same. (2) A link that fails is an embedding problem. (3) Offline access means no internet is ever needed.

**Instructional Rationale:** Classifying a problem by the idea it breaks is an Understand-level action that connects a symptom to a check. Ten problems, one per idea, teach the learner to name what is actually wrong.

**Content:**

The ten ideas: Browser compatibility, No-login access, Iframe embedding, Link sharing, Export format, LMS import, LTI integration, Responsive layout, Offline access, Platform lock-in.

The ten problems:

| # | Problem shown to the learner | Correct idea | Why (shown as feedback) |
|---|---|---|---|
| 1 | The page works in one browser and shows an error in the others. | Browser compatibility | The page does not work across the main browsers. |
| 2 | Visitors must create an account before they can see the first page. | No-login access | An account is a barrier to use. |
| 3 | A teacher's course page shows a blank frame where the simulation should be. | Iframe embedding | The page cannot be shown inside another page. |
| 4 | The address changes every time the page is opened, so a saved link fails. | Link sharing | There is no stable address to send. |
| 5 | The only download is a file that opens in one company's program. | Export format | There is no open copy to keep. |
| 6 | A teacher cannot bring the unit into her LMS as a package. | LMS import | The resource offers no way to import it. |
| 7 | A quiz tool opened from the LMS cannot send scores back to the gradebook. | LTI integration | The tool and the LMS do not exchange information. |
| 8 | On a phone the text is tiny and the right half of the page is cut off. | Responsive layout | The page does not adapt to the screen width. |
| 9 | A field trip has no internet, and the resource offers no download. | Offline access | The resource cannot be used without a connection. |
| 10 | The author's content exists only inside one company's service, with no export. | Platform lock-in | Leaving the platform would lose the content. |

**Provenance:** The problems are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The ideas follow the chapter sections on each concept.

**Rules:** Each problem has exactly one correct idea, and the ten ideas are all different.

**Learner Activity:**

1. The learner sees one problem and the ten ideas.
2. The learner may open the idea list. Opening it does not change the score.
3. The learner chooses an idea, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After problem 10 the sim shows the summary.

**Feedback:** 10 problems in a shuffled order, one attempt each. Correct: "Correct: [idea]. [Why]". Incorrect: "Not quite. This breaks [idea]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can name what stops a resource from traveling." Below 9 it lists the Why text of each missed problem.

**Starting State:** The first problem and the ten ideas. The question shown is "Which portability idea does this break?"

**Chapter Anchors:** The chapter's ten ideas are browser compatibility, no-login access, iframe embedding, link sharing, export format, LMS import, LTI integration, responsive layout, offline access, and platform lock-in.
</details>

The second MicroSim practices diagnosis. It shows six reports from embed tests, and for each one you name the cause.

#### Diagram: Embed Failure Diagnoser

<details markdown="1">
<summary>Embed Failure Diagnoser</summary>
Type: microsim
**sim-id:** embed-failure-diagnoser<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** differentiate<br/>
**Learning Objective:** The learner will differentiate six causes of an embedding result by choosing the cause that each of six test reports describes, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Iframe Embedding, No-Login Access, Responsive Layout, Embeddable Component (defined in Chapter 9) (all defined above this block or in Chapter 9).

**Evidence of Mastery:** For each report the learner commits one of six causes. A choice is correct when it matches the Correct cause column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the cause list is exploration, not evidence.

**Misconceptions:** (1) A blank frame always means the file is missing. (2) If the page works on its own, it will embed. (3) A sign-in form in the frame is a platform error.

**Instructional Rationale:** Differentiating among causes is an Analyze-level action, because the learner must read the evidence in a report and decide which cause fits it. Six reports that look alike on the surface teach the learner to read the details.

**Content:**

The six causes: Frame blocked by the host, Insecure address in a secure page, Needs a login, Script path broken, Layout not responsive, Works.

The six reports:

| # | Test report shown to the learner | Correct cause | Why (shown as feedback) |
|---|---|---|---|
| 1 | The frame stays blank, and the browser's message says the page refused to be displayed in a frame. | Frame blocked by the host | The server told browsers not to show the page inside a frame. |
| 2 | The frame is blank on a secure page, and the simulation's address begins with http and not https. | Insecure address in a secure page | A browser refuses to mix an insecure frame into a secure page. |
| 3 | The frame shows a sign-in form. | Needs a login | The resource requires an account, so it cannot embed for visitors. |
| 4 | The page loads, the buttons do nothing, and the browser's message says a script file was not found. | Script path broken | The page loads a script by a path that does not exist at the new location. |
| 5 | The frame shows the simulation, and every control responds. | Works | The embed passed. |
| 6 | The simulation appears, and on a phone the right side is cut off. | Layout not responsive | The page has a fixed width and does not adapt to the frame. |

**Provenance:** The reports are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The causes follow the chapter sections "Iframe Embedding", "No-Login Access", and "Responsive Layout".

**Rules:** Each report has exactly one correct cause, and the six causes are all different.

**Learner Activity:**

1. The learner reads one test report and sees the six causes.
2. The learner chooses a cause, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After report 6 the sim shows the summary.

**Feedback:** 6 reports in a shuffled order, one attempt each. Correct: "Correct: [cause]. [Why]". Incorrect: "Not quite. The cause is [cause]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read an embed test." Below 5 it lists the Why text of each missed report.

**Starting State:** The first report and the six causes. The question shown is "What explains this result?"

**Chapter Anchors:** The chapter says an embed can fail because the host blocks frames, because an insecure address is shown in a secure page, because a login is required, or because the layout is fixed, and the sim adds a broken script path.
</details>

The third MicroSim is a decision exercise. For each of six teacher needs you choose how best to bring an open resource into a learning management system.

#### Diagram: LMS Integration Chooser

<details markdown="1">
<summary>LMS Integration Chooser</summary>
Type: microsim
**sim-id:** lms-integration-chooser<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the differences among a link, an embed, a Common Cartridge import, and an LTI tool to choose the best way to bring a resource into an LMS for each of six teacher needs, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** LMS Import, Common Cartridge, LTI Integration, Iframe Embedding, Link Sharing (all defined in this chapter above this block).

**Evidence of Mastery:** For each need the learner commits one of four methods. A choice is correct when it matches the Correct method column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the method list is exploration, not evidence.

**Misconceptions:** (1) An embed copies the resource into the LMS. (2) A Common Cartridge only works inside one LMS. (3) LTI is just a fancy link.

**Instructional Rationale:** Choosing a method for a need is an Apply-level action. Six needs that map to four methods teach the learner what each method does and does not give a teacher.

**Content:**

The four methods: Link (students open the resource at its own address), Embed (the resource appears on the course page through a frame), Common Cartridge import (a whole unit is copied into the LMS as a package), LTI tool (an external tool opens inside the LMS and can send results back).

The six needs:

| # | Teacher need shown to the learner | Correct method | Why (shown as feedback) |
|---|---|---|---|
| 1 | "I want students to open one reading in a new tab." | Link | A link opens the resource at its own address. |
| 2 | "I want a simulation to appear on my course page." | Embed | A frame shows the simulation inside the page. |
| 3 | "I want to copy a whole unit, with pages, quizzes, and files, into my course." | Common Cartridge import | A package carries the whole unit into the LMS. |
| 4 | "I want an external quiz tool to send each student's score to the LMS gradebook." | LTI tool | LTI lets the tool exchange information with the LMS. |
| 5 | "I want colleagues in another school, with a different LMS, to receive the same unit." | Common Cartridge import | A cartridge is the common exchange form between LMSs. |
| 6 | "I want students to read chapter 4 of an open textbook." | Link | A link to the chapter is enough. |

**Provenance:** The needs are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The methods follow the chapter sections "LMS Import", "Common Cartridge", "LTI Integration", "Iframe Embedding", and "Link Sharing".

**Rules:** Each need has exactly one correct method. Two needs call for a Link, one for an Embed, two for a Common Cartridge import, and one for an LTI tool.

**Learner Activity:**

1. The learner sees one need and the four methods.
2. The learner may open the method descriptions. Opening them does not change the score.
3. The learner chooses a method, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After need 6 the sim shows the summary.

**Feedback:** 6 needs in a shuffled order, one attempt each. Correct: "Correct: [method]. [Why]". Incorrect: "Not quite. The best method is [method]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can choose how to bring a resource into an LMS." Below 5 it lists the Why text of each missed need.

**Starting State:** The first need and the four methods. The question shown is "Which method fits this need?"

**Chapter Anchors:** The chapter says a teacher can bring an OER into an LMS by link, embed, file upload, or package import, that a Common Cartridge is a single package that moves between LMSs, and that LTI lets an external tool exchange information with an LMS.
</details>

## Scoring Portability

Portability is scored with ten checks. A failed check is **serious** when it stops a reuser from using the resource at all in a common setting, which covers a resource that does not open in the main browsers, one that needs a login, and one that cannot be embedded. When a serious check fails, choose the lower number in a two-number band. Otherwise choose the higher number.

| # | Check | Serious if it fails? |
|---|---|---|
| 1 | The resource opens without errors in at least three current browsers | Yes |
| 2 | No login or account is needed to view the learner-facing content | Yes |
| 3 | The resource, and each component, has a permanent address that can be shared | No |
| 4 | It embeds by iframe on test platforms without changes | Yes |
| 5 | The layout adapts to a phone-width screen | No |
| 6 | A downloadable copy in an open format is offered | No |
| 7 | It can be brought into an LMS by link, embed, or package | No |
| 8 | Where an LMS integration is claimed, it works | No |
| 9 | The resource can be used offline from a saved copy | No |
| 10 | Nothing is lost by moving it to another host, so there is no lock-in | No |

A check that does not apply, such as the LMS integration check for a resource that claims none, counts as passed.

**Worked example: Watershed Basics.** The reviewer applies the checks to the reading from Chapter 3.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | The page opens without errors in three browsers. |
| 2 | Pass | No login is needed. |
| 3 | Pass | Each section has its own address. |
| 4 | **Fail** | The iframe embed works on 2 of 3 test platforms. On the third the quiz script fails, for the broken relative path that the Chapter 9 modularity review found. |
| 5 | Pass | The layout adapts to a phone-width screen. |
| 6 | Pass | HTML and Markdown downloads are offered. |
| 7 | Pass | The reading links into an LMS and embeds on two platforms. |
| 8 | Pass | The resource claims no LMS integration, so the check does not apply. |
| 9 | **Fail** | The page loads its fonts and a quiz library from other sites, so a saved copy loses its styling and the quiz stops working without an internet connection. |
| 10 | Pass | Nothing is tied to one vendor, and the files move with no loss. |

Eight of ten checks pass, a share of 80 percent, in the 7 to 8 band. Check 4 failed and is serious, so the reviewer chooses the lower number, **7**, the score on the Chapter 3 worksheet. That worksheet recorded the embed result. The full check also finds the offline gap.

!!! mascot-tip "Test in a Private Window"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Open the resource in a private or incognito browser window, which carries none of your sign-ins or saved settings. If it opens there with no login, you have seen what a stranger will see.

The last MicroSim of the chapter is a scoring practice. It shows five resources with their ten check results, and for each one you choose the metric score.

#### Diagram: Portability Metric Scorer

<details markdown="1">
<summary>Portability Metric Scorer</summary>
Type: microsim
**sim-id:** portability-metric-scorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the ten portability checks and the Chapter 3 scoring rules to choose the metric score for each of five resources, with at least 4 of 5 scores exactly correct on the first attempt.

**Prerequisites:** The Portability Metric, Metric Score, Scoring Descriptor (all defined in this chapter or in Chapter 3 above this block).

**Evidence of Mastery:** For each resource the learner chooses a whole-number score from 0 to 10 after seeing the ten check results. A score is correct when it equals the Correct score column in Content. Mastery is at least 4 of 5 scores correct on the first attempt. Opening the check list and the descriptor table is exploration, not evidence.

**Misconceptions:** (1) Every failed check lowers the score equally. (2) A free platform is automatically portable. (3) A check that does not apply counts as failed.

**Instructional Rationale:** Applying a scoring procedure to new cases is an Apply-level task. Five resources that differ in how many checks fail and whether a serious check fails make the learner use every step: count, band, then choose within the band.

**Content:**

The ten checks, each marked serious or not, are those in the chapter's check table. The descriptor bands applied to the share of checks passed: 0% is 0; 1% to 24% is 1 to 2; 25% to 49% is 3 to 4; 50% to 74% is 5 to 6; 75% to 89% is 7 to 8; 90% to 100% is 9 to 10. Within a two-number band, choose the lower number when a serious check failed and the higher number otherwise. A score of 10 requires every check to pass. A check that does not apply counts as passed.

The five resources:

| # | Resource | Checks failed | Checks passed | Share | Band | Serious failure? | Correct score | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|---|
| 1 | Open Algebra | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed. |
| 2 | Watershed Basics | 4 and 9 | 8 | 80% | 7 to 8 | Yes, check 4 | 7 | Failing to embed on one platform is serious, so the lower number applies. |
| 3 | Login-Only Course | 2, 3, 4, 6, 7, 9, 10 | 3 (checks 1, 5, 8) | 30% | 3 to 4 | Yes, checks 2 and 4 | 3 | A required login and no embedding are serious, so the lower number applies. |
| 4 | Desktop-Only Page | 1 and 5 | 8 | 80% | 7 to 8 | Yes, check 1 | 7 | A page that does not open in the main browsers is serious, so the lower number applies. |
| 5 | Vendor Platform Module | 4, 6, 7, and 10 | 6 (checks 1, 2, 3, 5, 8, 9) | 60% | 5 to 6 | Yes, check 4 | 5 | The module cannot embed, which is serious, so the lower number applies. |

**Provenance:** The ten checks and the bands follow the chapter section "Scoring Portability" and Chapter 3. The five resources are illustrative cases written for this chapter, and the sim labels them "illustrative examples". Resource 2 is the chapter's worked example.

**Rules:** A score is the band chosen from the share passed, and then the number chosen within the band by the serious-failure rule. Each resource has exactly one correct score. For a band that holds a single number, that number is the score.

**Learner Activity:**

1. The sim shows resource 1 with its ten check results.
2. The learner may open the check list and the descriptor table.
3. The learner chooses a score from 0 to 10, and the choice is committed.
4. The sim shows the count of passes, the band, whether a serious check failed, and the correct score with the Why text.
5. After resource 5 the sim shows the summary.

**Feedback:** 5 resources in the fixed order, one attempt each. Correct: "Correct: [score]. [Why]". Incorrect: "Not quite. [passes] checks passed, which is [share] and the [band] band. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can score portability." Below 4 it lists the Why text of each missed resource.

**Starting State:** Resource 1 with all ten results shown and no score chosen. The question shown is "What portability score does this resource earn?"

**Chapter Anchors:** The chapter's worked example for Watershed Basics fails checks 4 and 9, passes 8 of 10, and scores 7, with the lower number chosen because the embed failure is serious.
</details>

## Key Takeaways

- The **portability metric** asks whether a resource runs in a browser with no login and can be shared or embedded elsewhere. It completes the ten-metric rubric.
- A portable resource has **browser compatibility**, offers **no-login access**, supports **iframe embedding** and **link sharing**, and adapts through a **responsive layout**.
- An **export format** is the exit door. **LMS import**, a **Common Cartridge** package, and **LTI integration** bring a resource into the systems schools use.
- **Offline access** keeps a resource usable without a connection, and **platform lock-in** is the dependence on one platform that makes leaving costly.

!!! mascot-celebration "All Ten Metrics Are in Your Hands"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now test whether a resource opens in the main browsers, needs a login, embeds in another page, and moves between platforms, and you can score portability with evidence. With this chapter you have met all ten metrics, and the rest of the book puts them to work.

[See Annotated References](./references.md)
