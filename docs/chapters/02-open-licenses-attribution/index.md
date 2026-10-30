---
title: "Open Licenses and Attribution"
description: "Explains the Creative Commons license family, its elements, attribution, and compatibility, so teachers can read a license, give correct credit, and choose a license for their own work."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 21:41:53"
version: 1.11
status: built
---

# Open Licenses and Attribution

## Summary

Explains the Creative Commons license family, its elements, attribution, and compatibility, so teachers can read a license, give correct credit, and choose a license for their own work. It builds on the 5R permissions and is needed before any chapter scores reusability. After this chapter you can read a Creative Commons license, write a correct attribution statement, and spot a license conflict that blocks reuse.

## Concepts Covered

This chapter covers the following 23 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Open License | 295 |
| License Statement | 189 |
| Creative Commons | 65 |
| CC0 Dedication | 1 |
| Attribution Requirement | 21 |
| CC BY | 18 |
| ShareAlike Requirement | 10 |
| CC BY-SA | 5 |
| NonCommercial Requirement | 8 |
| CC BY-NC | 7 |
| CC BY-NC-SA | 4 |
| NoDerivatives Requirement | 6 |
| CC BY-ND | 4 |
| CC BY-NC-ND | 1 |
| License Compatibility | 3 |
| License Conflict | 1 |
| Attribution Statement | 2 |
| TASL Attribution Format | 1 |
| Third-Party Content | 1 |
| Fair Use | 1 |
| Proprietary License | 2 |
| All Rights Reserved | 1 |
| License Selection | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Foundations of Open Educational Resources](../01-foundations-of-oer/index.md)

---

!!! mascot-welcome "Read the Fine Print Without Fear"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A license is only a few lines long, but it decides whether the lesson you love can travel to your classroom. By the end of this chapter you will read any Creative Commons license in under a minute, credit it correctly, and spot a conflict before it costs you a week of work. Let's dive in and check the evidence!

Chapter 1 gave you the five permissions and the idea that an open license grants them in advance. This chapter looks at the licenses themselves. Open licenses do not all grant the same freedoms, and the differences decide whether you can translate a reading, sell a printed copy, or combine two resources into one packet.

You will learn the Creative Commons family of licenses, how to read a license statement, how to credit a creator correctly, how to tell when two licenses cannot be combined, and how to choose a license for your own work. Later chapters score how reusable a resource is, and every one of those scores starts from the vocabulary in this chapter.

## What an Open License Grants

An **open license** is a license in which the owner of a work gives everyone permission, in advance and at no charge, to do things that copyright would otherwise reserve to the owner. Chapter 1 defined a license as a statement of what others may do. An open license is one that grants the five R permissions (retain, reuse, revise, remix, and redistribute) to the whole public instead of to one person who asked.

Three features separate an open license from a one-time permission:

- **Public:** the owner offers it to everyone, not to a named person.
- **In advance:** the owner grants it before anyone asks, usually by posting a notice on the work.
- **Standing:** people who received the work under the license keep their rights, even if the owner later stops offering the work.

Open licenses attach conditions. Every Creative Commons license except the public domain dedication, for example, requires credit to the creator. Conditions differ from license to license, and they decide how much you can do with a resource. A condition that asks something of you, such as giving credit, costs little. A condition that takes a freedom away, such as banning commercial use or banning changes, makes a license less open, and people disagree about how much less.

Some definitions of openness are strict. The Open Definition published by the Open Knowledge Foundation, for example, accepts only licenses that allow commercial use and changes. Many OER programs accept licenses that restrict commercial use, and fewer accept licenses that forbid changes. This book treats openness as a spectrum, and [Chapter 9](../09-modularity-metadata/index.md) shows how the rubric scores a resource's license along it.

Standard licenses also beat homemade ones. Anyone can write "free to use for education" on a page, but the sentence leaves open whether it covers translation, sale, or sharing with a colleague. A standard license answers those questions in advance, it has been tested in courts, and search tools recognize it.

**Worked example: three notices.** Read each notice below and decide what kind of license it is.

| Text found on a page | What it is | Why |
|---|---|---|
| "This lesson plan is licensed under CC BY 4.0." | Open license | It grants permissions to everyone, with one stated condition: credit. |
| "You may view this document for personal use. Copying, editing, or sharing requires written permission." | Proprietary license | Permission is narrow, and every other use needs a request. |
| "© 2025 Example Press. All rights reserved." | All rights reserved | No license is granted, and every right is kept. |

!!! mascot-tip "Look in Three Places"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Look for a license in the page footer or "about" page, on the first or last page of the file, and in the file's properties. If all three are silent, treat the work as all rights reserved.

### Proprietary License

A **proprietary license** is a license that an owner writes to keep control of a work. It grants narrow permission, usually to view or use the work under stated terms, and reserves everything else. Common examples are a publisher's terms of use for a digital textbook, a software end-user license agreement, and a streaming site's terms of service. Proprietary does not mean unfair, and a publisher may have good reasons for its terms. For evaluation the point is practical: a proprietary license permits only the uses it lists, so read it before you assume anything else.

### All Rights Reserved

**All rights reserved** is a notice that the owner keeps every right that copyright gives and has granted no license. In most countries a work is protected whether or not the notice appears, so a work with no notice at all is treated the same way. A work marked all rights reserved is the opposite of an open resource, because it grants none of the five R permissions in advance. You may still link to it, read it, and ask the owner for permission.

## Creative Commons

**Creative Commons** (CC) is a nonprofit organization, founded in 2001, that publishes a standard set of open licenses anyone may apply to their own work. Before CC, an owner who wanted to share generously had to write a custom license and hope it held up. Now the owner picks one of the standard licenses and adds a notice. CC licenses work for text, images, audio, and video.

Every CC license has three layers, so that people, lawyers, and software can each read it:

- **Commons Deed:** a short plain-language summary that people can read in a minute.
- **Legal code:** the full license text that a court would read.
- **Machine-readable code:** metadata that lets search engines and software recognize the license.

CC licenses also have versions, and the current one is 4.0. Terms differ slightly between versions, so a careful credit names the version.

**Worked example: finding the three layers.** A teacher opens a lesson page whose footer says "CC BY 4.0".

1. She clicks the footer link and reaches the Commons Deed, the plain-language summary.
2. At the bottom of the Deed she finds a link to the legal code, the full text.
3. She views the page source and finds a link marked `rel="license"`, which is the machine-readable layer that search tools use to filter by license.

## The Four License Elements

Every CC license is built from four elements. **Attribution (BY)** appears in six of the seven CC tools, and the other three, **ShareAlike (SA)**, **NonCommercial (NC)**, and **NoDerivatives (ND)**, can be added to it. To read a CC license, read which elements it has. The sections below take the elements one at a time and then show how they combine into six licenses.

!!! mascot-thinking "Think of Switches"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Picture the elements as switches on a panel. BY is always on, and each other switch you turn on takes a freedom away from the person who receives the work.

The MicroSim below puts three of these switches in your hands: flip ShareAlike and NonCommercial to watch the license name change and see which freedom each one takes away, and try to turn Attribution off.

#### Diagram: Creative Commons License Switches

<iframe src="../../sims/cc-license-switches/main.html" height="562px" width="100%" scrolling="no"></iframe>

[Run the Creative Commons License Switches MicroSim Fullscreen](../../sims/cc-license-switches/main.html){ .md-button .md-button--primary }

### Attribution Requirement

The **attribution requirement** means that anyone who shares the work must give credit to its creator. Under the 4.0 licenses, credit includes the creator's name, any copyright notice the creator supplied, a statement of which license applies and a link to it, a link to the work where practical, and a note of any changes you made. You may give credit in any reasonable way for your medium, such as a caption under an image, a credits slide, or a references page. Credit must not suggest that the creator endorses you or your use.

Credit works in both directions. A creator may ask you to remove their name from a work you have adapted, and the license requires you to do so as far as is reasonably practicable. Credit also does not require the creator's approval. The license grants permission in advance, so you do not need to email the author before you reuse the work.

**Worked example: crediting a diagram.** A teacher puts an openly licensed diagram of the water cycle on a slide.

1. She keeps the creator's name, the title, and the link to the original.
2. She writes the license name and version, with a link to the license.
3. She places all of this in a small caption under the diagram, because that is where a viewer looks for it.

### CC BY

**CC BY**, the Attribution license, has one element: BY. It lets anyone retain, reuse, revise, remix, and redistribute the work, including for money, as long as they credit the creator. It is the most open of the six licenses. Many open textbooks and publicly funded projects choose it, and some funders require it. Choose it when you want your work to travel as far as possible and you accept that others will profit from it and change it. Anyone who adapts the work must note their changes, so readers can tell your words from theirs.

**Worked example: commercial reuse of a CC BY worksheet.** A district posts a revised CC BY worksheet, and a for-profit tutoring company puts it into a paid course. The license allows this. The company must credit the district and note its changes, but the district cannot stop the sale or demand payment. A creator who is uncomfortable with that outcome should pick a different license before sharing, because the choice cannot be reversed later for copies already out in the world.

### ShareAlike Requirement

The **ShareAlike requirement** means that if you share an adaptation, you must license it under the same license, or under one that the license lists as compatible. The aim is to keep improvements open: each new version carries the same freedoms as the one before it. The requirement applies only when you adapt the work. Sharing an unchanged copy brings no extra burden beyond credit. People call this approach *copyleft*, a play on the word copyright: the license uses copyright law to keep a work free instead of to restrict it. The trade-off is that a ShareAlike work cannot move to a less restrictive license, even to another open license that lacks the ShareAlike condition.

**Worked example: translating a ShareAlike reading.** A teacher translates a CC BY-SA reading into Spanish and posts it.

1. She credits the original creator and notes that she translated it.
2. She marks the translation CC BY-SA, because ShareAlike requires the same license.
3. She cannot relabel the translation as CC BY, since that would remove the ShareAlike condition from the original.

### CC BY-SA

**CC BY-SA** combines BY and SA. It allows all five R permissions, including commercial use, and requires every adaptation to carry CC BY-SA too. The text of Wikipedia uses this license, which is why many remixes of Wikipedia text must also be CC BY-SA. The trade-off is compatibility: a ShareAlike work cannot be blended with works whose licenses demand something different, as the section on combining works shows.

### NonCommercial Requirement

The **NonCommercial requirement** means that you may not use the work in a way that is primarily intended for commercial advantage or monetary compensation. The words sound clear, but their edges are not. Creative Commons itself has found that people disagree about whether a use is commercial. The table below gives a likely reading for four uses of a CC BY-NC worksheet, and it is a guide rather than legal advice.

| Use of the worksheet | Likely reading | Reason |
|---|---|---|
| A teacher hands it out in a public school class | Allowed | No one earns money from it. |
| A blog with paid advertising posts it | Not allowed | The advertising income makes the use commercial. |
| A tutoring company uses it in paid sessions | Not allowed | The company earns money from the use. |
| A nonprofit workshop charges $20 to cover room and printing costs | Unclear | Cost recovery is a gray area, so ask the owner. |

!!! mascot-warning "NonCommercial Is Blurrier Than It Sounds"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Advertising, cost recovery, and paid workshops are gray areas that even experts argue about. If your use touches money in any way, ask the owner in writing before you rely on the work, or choose a resource under a more open license.

### CC BY-NC

**CC BY-NC** combines BY and NC. It allows all five R permissions for noncommercial use and requires credit. Teachers like it because it feels protective, but it limits reuse in ways that surprise people. A paid course, a publisher, and a school that sells materials to families may all fall outside it, and a work under CC BY-NC cannot be blended into a resource that allows commercial use. NC can exclude more than people expect: a private school that charges tuition, or a district vendor that bundles materials, may fall outside the license. When you cannot tell whether your setting counts as noncommercial, ask the owner.

**Worked example: adapting a CC BY-NC reading.** A teacher wants to rewrite a CC BY-NC reading and publish the result as a CC BY resource.

1. She checks the original license and finds NC.
2. She sees that releasing her version as CC BY would let anyone sell it, which the original forbids.
3. She decides to publish her version under CC BY-NC, or CC BY-NC-SA, so that the noncommercial limit stays in place.

The MicroSim below tests your judgment on ten uses of a CC BY-NC worksheet. For each use you decide whether it is clearly allowed, unclear, or likely not allowed. The goal is to learn where the clear cases end and the gray area begins, so that you know when to ask the owner.

#### Diagram: NonCommercial Gray Area Sorter

<iframe src="../../sims/noncommercial-gray-area-sorter/main.html" height="710px" width="100%" scrolling="no"></iframe>

[Run the NonCommercial Gray Area Sorter MicroSim Fullscreen](../../sims/noncommercial-gray-area-sorter/main.html){ .md-button .md-button--primary }

<details markdown="1">
<summary>NonCommercial Gray Area Sorter</summary>
Type: microsim
**sim-id:** noncommercial-gray-area-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of ten uses of a CC BY-NC resource is clearly allowed, unclear, or likely not allowed, with at least 8 of 10 correct on the first attempt.

**Prerequisites:** NonCommercial Requirement, CC BY-NC, Attribution Requirement (all defined in this chapter above this block).

**Evidence of Mastery:** For each use the learner commits one of three bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 8 of 10 correct on the first attempt. Reading the bin definitions is exploration, not evidence.

**Misconceptions:** (1) NonCommercial means free of charge. (2) A nonprofit is always noncommercial. (3) Selling at cost is always noncommercial. (4) Advertising on a free page does not count as commercial.

**Instructional Rationale:** Judging a use against a criterion is an Evaluate-level action, and the NonCommercial criterion is vague enough to need judgment. Three bins, including an explicit "unclear" bin, teach the learner that ask-the-owner is a valid answer and not a failure to decide.

**Content:**

The criterion, shown at all times: a use is noncommercial when it is not primarily intended for or directed toward commercial advantage or monetary compensation.

The three bins:

- Clearly allowed: no one earns money from the use.
- Unclear: ask the owner: the use touches money in a way reasonable people disagree about.
- Likely not allowed: the use earns money or is directed toward earning it.

The ten uses of a CC BY-NC worksheet:

| # | Use shown to the learner | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | A public-school teacher hands the worksheet out in class. | Clearly allowed | No one earns money from the use. |
| 2 | A teacher posts the worksheet on a free class website with no advertising. | Clearly allowed | No payment or advertising income is involved. |
| 3 | A blog with paid advertising posts the worksheet. | Likely not allowed | The advertising income makes the use commercial. |
| 4 | A tutoring company uses the worksheet in sessions that parents pay for. | Likely not allowed | The company earns money from sessions that use the worksheet. |
| 5 | A nonprofit workshop charges $20 to cover room and printing costs. | Unclear: ask the owner | Cost recovery is a gray area, because the charge is not profit but is still payment. |
| 6 | A university department prints copies and sells them at cost in its bookstore. | Unclear: ask the owner | Selling at cost is a gray area, because the sale is not for profit but is still a sale. |
| 7 | A publisher sells a printed edition for profit. | Likely not allowed | Sale for profit is commercial advantage. |
| 8 | A teacher places the worksheet in a paid online course on a marketplace. | Likely not allowed | The course earns money from learners who pay for it. |
| 9 | Teachers exchange the worksheet through a free file-sharing group, with no payment. | Clearly allowed | An exchange with no payment is noncommercial. |
| 10 | A school district uses the worksheet in free training for its own teachers. | Clearly allowed | No one is charged, and the use is not directed toward earning money. |

**Provenance:** The criterion is the Creative Commons definition of NonCommercial, paraphrased in the chapter section "NonCommercial Requirement". The ten uses are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The sim states that the bins are a likely reading and not legal advice.

**Rules:** Each use has exactly one correct bin. Only the "Clearly allowed" bin means no permission is needed. The "Unclear" bin is a valid answer, and it is correct for exactly the uses marked Unclear in the table.

**Learner Activity:**

1. The learner sees one use at a time, with the criterion and the three bins.
2. The learner places the use in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After the 10th use the sim shows the summary.

**Feedback:** 10 uses in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 8 or more it adds "You can spot when to ask the owner." Below 8 it lists the Why text of each missed use.

**Starting State:** The first use, the criterion, and the three empty bins. The question shown is "Is this use allowed under CC BY-NC?"

**Chapter Anchors:** The chapter's table of four uses agrees with this sim: the classroom handout is allowed (use 1), the advertising blog is not allowed (use 3), the tutoring company is not allowed (use 4), and the $20 nonprofit workshop is unclear (use 5).
</details>

### CC BY-NC-SA

**CC BY-NC-SA** adds ShareAlike to CC BY-NC. Credit is required, use must be noncommercial, and every adaptation must carry CC BY-NC-SA. It is a common choice for course materials from universities. It is also easy to get stuck with, because it cannot be combined with a CC BY-SA work: one requires noncommercial use and the other requires that commercial use remain possible.

### NoDerivatives Requirement

The **NoDerivatives requirement** means that you may share the work only as it is. You may not share a version that you have changed. The license does not forbid private changes, so you may adjust a copy for your own study, but sharing that adjusted copy is not allowed. In an OER setting this limit is severe, because it blocks the revise and remix permissions for anyone who wants to share the result.

**Worked example: alt text on an ND chapter.** A teacher finds a CC BY-ND chapter whose images lack alt text.

1. She may add alt text to a copy for her own reading.
2. Giving that changed copy to students or colleagues counts as sharing, and the license does not allow it.
3. She can ask the owner for permission to share the improved version, or she can choose a resource that allows changes.

!!! mascot-warning "ND Blocks the Fixes This Book Teaches"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Adding alt text, lowering a reading level, and fixing an error all change the work, so an ND license stops you from sharing any of them. If sharing the improved version matters to you, ask the owner for written permission or pick a different resource.

### CC BY-ND

**CC BY-ND** combines BY and ND. You may share the unchanged work, including commercially, with credit. You may not share any changed version, whether it is a translation, a summary, or a remix. It suits a creator who wants wide distribution of a finished piece, such as a report, and no variations.

### CC BY-NC-ND

**CC BY-NC-ND** combines all three restrictions. You may share the unchanged work, for noncommercial purposes only, with credit. It is the most restrictive of the six licenses and the one that gives teachers the least to work with. A resource under it can be read, assigned, and passed along, but it cannot be improved and shared.

### CC0 Dedication

The **CC0 dedication**, written CC0 1.0 Universal, is a Creative Commons tool for placing a work in the public domain. It is not a license that adds conditions. The creator gives up copyright and related rights as far as the law of their country allows, and where the law does not allow giving them up, CC0 acts as a license with no conditions. Credit is not legally required for CC0 work, though giving credit is good practice and helps readers find the source. Creators use CC0 for data sets, quiz banks, and other material where they want no friction at all.

## The Six Licenses Together

The four elements combine into six licenses. ShareAlike and NoDerivatives never appear together, because ShareAlike governs adaptations that NoDerivatives forbids you to share. The table summarizes what each license allows, with CC0 added for comparison.

| License | Elements | Share unchanged | Share a changed version | Commercial use | Rule for changed versions |
|---|---|---|---|---|---|
| CC0 | None | Yes | Yes | Yes | None |
| CC BY | BY | Yes | Yes | Yes | Keep the credit and note changes |
| CC BY-SA | BY, SA | Yes | Yes | Yes | Same license, CC BY-SA |
| CC BY-NC | BY, NC | Yes | Yes | No | Stay noncommercial |
| CC BY-NC-SA | BY, NC, SA | Yes | Yes | No | Same license, CC BY-NC-SA |
| CC BY-ND | BY, ND | Yes | No | Yes | Sharing a changed version is not allowed |
| CC BY-NC-ND | BY, NC, ND | Yes | No | No | Sharing a changed version is not allowed |

Creative Commons orders the licenses from most to least permissive: CC0, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, and CC BY-NC-ND. Each step down takes away a freedom from the person receiving the work. The first MicroSim below makes this concrete. You switch elements on and off, predict what a license allows, and check your prediction against the license's actual terms.

#### Diagram: Creative Commons Element Explorer

<iframe src="../../sims/cc-element-explorer/main.html" height="690px" width="100%" scrolling="no"></iframe>

[Run the Creative Commons Element Explorer MicroSim Fullscreen](../../sims/cc-element-explorer/main.html){ .md-button .md-button--primary }

<details markdown="1">
<summary>Creative Commons Element Explorer</summary>
Type: microsim
**sim-id:** cc-element-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** infer<br/>
**Learning Objective:** The learner will infer whether each of five actions is allowed under a given Creative Commons license by reasoning from its elements, with at least 7 of 8 predictions correct on the first attempt.

**Prerequisites:** Attribution Requirement, ShareAlike Requirement, NonCommercial Requirement, NoDerivatives Requirement, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND (all defined in this chapter above this block).

**Evidence of Mastery:** The learner commits a Yes or No for each of 8 prompts before the answer is shown. A prediction is correct when it matches the Correct answer column in Content. Mastery is at least 7 of 8 correct on the first attempt. Switching elements on and off in explore mode is exploration, not evidence.

**Misconceptions:** (1) NoDerivatives forbids all changes, including private ones. (2) NonCommercial only forbids selling the exact file. (3) ShareAlike applies to unchanged copies. (4) Any element can be combined with any other.

**Instructional Rationale:** Inferring is an Understand-level action, so the learner must reason from the elements to a result instead of reading it from a chart. Explore mode lets the learner build the mental model first, and committed predictions afterward make them test it before the answer appears.

**Content:**

The four elements: BY (Attribution), SA (ShareAlike), NC (NonCommercial), ND (NoDerivatives). BY is always on. SA and ND cannot both be on, and the sim explains why: ShareAlike governs adaptations that NoDerivatives forbids anyone to share.

The five actions:

- A1: Post an unchanged copy on your website, with credit.
- A2: Post a translated version.
- A3: Sell printed copies for profit.
- A4: Publish a remix of it under CC BY.
- A5: Change it privately for your own use and do not share it.

The result for each license and action:

| License | A1 | A2 | A3 | A4 | A5 |
|---|---|---|---|---|---|
| CC BY | Yes | Yes | Yes | Yes | Yes |
| CC BY-SA | Yes | Yes (translation must be CC BY-SA) | Yes | No (remix must be CC BY-SA) | Yes |
| CC BY-NC | Yes | Yes (noncommercial only) | No | No (CC BY would allow commercial use) | Yes |
| CC BY-NC-SA | Yes | Yes (must be CC BY-NC-SA) | No | No | Yes |
| CC BY-ND | Yes | No (ND forbids sharing changes) | Yes | No | Yes |
| CC BY-NC-ND | Yes | No | No | No | Yes |

The eight predictions, in this order:

| # | License | Action | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | CC BY-SA | A2 | Yes | Translations are allowed, and the translation must carry CC BY-SA. |
| 2 | CC BY-ND | A2 | No | ND forbids sharing a changed version, and a translation is a change. |
| 3 | CC BY-NC | A3 | No | NC forbids use directed toward monetary compensation. |
| 4 | CC BY | A3 | Yes | BY allows commercial use with credit. |
| 5 | CC BY-NC-ND | A5 | Yes | ND blocks sharing changed versions, not private changes. |
| 6 | CC BY-SA | A4 | No | SA requires the remix to carry CC BY-SA, not CC BY. |
| 7 | CC BY-NC-SA | A2 | Yes | A translation is allowed if it is noncommercial and carries CC BY-NC-SA. |
| 8 | CC BY-ND | A1 | Yes | ND allows sharing the unchanged work with credit. |

**Provenance:** The result table applies the element definitions in the chapter sections "The Four License Elements" and "The Six Licenses Together". The actions are illustrative cases written for this chapter, and the sim labels them "illustrative examples".

**Rules:** A license is the set of elements switched on, and only the six valid combinations exist. A1 is Yes for every license because every license allows sharing the unchanged work with credit. A5 is Yes for every license because no license forbids private changes. For every other cell, apply the result table. The sim states that the table follows the 4.0 licenses and is a study aid, not legal advice.

**Learner Activity:**

1. In explore mode the learner switches NC, SA, and ND on or off. BY stays on, and turning on SA while ND is on, or the reverse, shows the explanation instead of a change.
2. After each switch the sim shows the license name and the Yes or No result for all five actions, with the reason for each No.
3. When the learner is ready, prediction mode starts. The sim shows prediction 1 and asks "Allowed?" with Yes and No.
4. The learner commits an answer, and the sim shows the correct answer with the Why text.
5. After prediction 8 the sim shows the summary.

**Feedback:** 8 predictions in the fixed order, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can read a license from its elements." Below 7 it lists the Why text of each missed prediction.

**Starting State:** The BY element on, the other three off, the license shown as "CC BY", and the question "What does this license allow?"

**Chapter Anchors:** The chapter says the elements combine into six licenses and that SA and ND never appear together. The chapter's table "The Six Licenses Together" agrees with this result table for sharing unchanged copies, sharing changed versions, and commercial use.
</details>

The second MicroSim is a comparison poster. A poster suits the six licenses because the reader's question is "which license is which?", and a labeled picture with hover zones answers it faster than a paragraph.

#### Diagram: Six Creative Commons Licenses Poster

<iframe src="../../sims/six-cc-licenses-poster/main.html" height="702px" width="100%" scrolling="no"></iframe>

[Run the Six Creative Commons Licenses Poster MicroSim Fullscreen](../../sims/six-cc-licenses-poster/main.html){ .md-button .md-button--primary }

<details markdown="1">
<summary>Six Creative Commons Licenses Poster</summary>
Type: infographic
**sim-id:** six-cc-licenses-poster<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify which of the six Creative Commons licenses matches each of six descriptions, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the poster zone that matches each description. A click is correct when the zone's id equals the Correct zone column in Content. Mastery is at least 5 of 6 correct on the first attempt. Hovering a zone in explore mode is exploration, not evidence.

**Misconceptions:** (1) CC BY-NC allows no adaptations. (2) CC BY-ND forbids commercial use. (3) CC BY-SA forbids commercial use.

**Instructional Rationale:** Identifying six near-identical license names is a Remember-level task, and a poster with six labeled regions lets the learner hold them side by side. The quiz forces recall of each license's distinguishing rule rather than recognition of its name.

**Content:**

The poster is a flat comparison illustration with six equal panels in two rows of three. Each panel prints the license's short name and shows the license's icons, and each carries a simple pictogram that suggests its main rule. The printed text is limited to the six license names. All other words come from the explore and quiz data. The six zones, one per panel:

| Zone id | Label | Summary | Facts shown on hover or click |
|---|---|---|---|
| cc-by | CC BY | Credit is the only condition. | Credit the creator and link to the license. Share, adapt, and sell, including for profit. All five R permissions remain. The most open of the six. |
| cc-by-sa | CC BY-SA | Credit, and keep adaptations open the same way. | Credit the creator. Commercial use is allowed. Every adaptation must carry CC BY-SA. Wikipedia text uses it. |
| cc-by-nc | CC BY-NC | Credit, and no commercial use. | Credit the creator. Adaptations are allowed. Use must be noncommercial. Adaptations must stay noncommercial. |
| cc-by-nc-sa | CC BY-NC-SA | Credit, noncommercial, and the same license on adaptations. | Credit the creator. Use must be noncommercial. Every adaptation must carry CC BY-NC-SA. |
| cc-by-nd | CC BY-ND | Credit, and share the work unchanged only. | Credit the creator. Commercial use is allowed. You may not share a changed version. Private changes are allowed. |
| cc-by-nc-nd | CC BY-NC-ND | Credit, noncommercial, unchanged only. | Credit the creator. Use must be noncommercial. You may not share a changed version. The most restrictive of the six. |

The six quiz questions, in this order:

| # | Question | Correct zone | Why (shown as feedback) |
|---|---|---|---|
| 1 | Which license allows commercial use and requires every adaptation to carry the same license? | cc-by-sa | SA keeps adaptations open, and without NC, commercial use stays allowed. |
| 2 | Which license allows noncommercial use only and forbids sharing changed versions? | cc-by-nc-nd | It combines NC and ND. |
| 3 | Which license allows commercial use but forbids sharing changed versions? | cc-by-nd | ND blocks changed versions, and there is no NC element. |
| 4 | Which license requires noncommercial use and the same license on every adaptation? | cc-by-nc-sa | It combines NC and SA. |
| 5 | Which license places no condition on the work beyond credit? | cc-by | BY is the only element. |
| 6 | Which license allows noncommercial adaptations and does not dictate the adaptation's license? | cc-by-nc | NC without SA lets adapters choose, as long as use stays noncommercial. |

**Provenance:** The facts follow the chapter sections "The Four License Elements" and "The Six Licenses Together". The statement that Wikipedia text uses CC BY-SA follows the chapter section "CC BY-SA". The illustration is synthetic, and it carries no statistics.

**Rules:** Each question has exactly one correct zone. Zones are distinct regions of the poster, so a click belongs to at most one zone. Because the poster prints its own panel titles, the sim does not add its own zone labels over the image.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a panel and reads its summary and facts.
2. In quiz mode the sim shows question 1 above the poster.
3. The learner clicks the panel they think matches.
4. The sim shows the Why text and moves to the next question, until question 6 is done.

**Feedback:** 6 questions in the fixed order, one attempt each. Correct: "Correct: [label]. [Why]". Incorrect: "Not quite. The answer is [label]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can tell the six licenses apart." Below 5 it lists the Why text of each missed question.

**Starting State:** The poster with no zone selected, explore mode active, and the prompt "Hover a panel to learn what the license allows."

**Chapter Anchors:** The chapter says there are six licenses, lists them as CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, and CC BY-NC-ND, and states that Wikipedia text uses CC BY-SA.
</details>

## License Statement

A **license statement** is the notice that tells readers which license applies to a work. A complete statement does four things. It names the license and its version, it links to the license text, it identifies the owner, and it says what the statement covers. The standard Creative Commons wording is short, such as "This work is licensed under a Creative Commons Attribution 4.0 International License", followed by a link to the license page.

Place the statement where readers will meet it: the footer of every page, the title page of a book, the last slide of a deck, or the description of a video. A statement that sits only on the home page leaves a reader on page 40 guessing. For readers who use search tools, add machine-readable marking as well, such as a link marked `rel="license"` in the page's code, so that a filter for "reusable" resources can find the work.

A statement is a claim, and claims need checking. A page can show a license icon that its owner never intended, or a site can copy a work and add a license that the original never carried. The reliable check is to follow the link back to the original source and confirm the license there. When the statement and the source disagree, the source wins.

Only an owner can grant a license. Suppose a teacher-sharing site marks a worksheet CC BY, but the worksheet's own pages say the uploader copied it from a publisher's book. The marking is worthless, because the uploader never held the rights to give away. This is why you trace a resource to its original creator before you rely on its statement, and why [Chapter 14](../14-checking-agent-output/index.md) asks you to check an AI agent's reading of a license the same way.

Before you look at an annotated example, three terms need defining. The **scope** is what the statement covers: this page, the whole book, or only the text. The **version** is the release of the license, such as 4.0. The **holder** is the person or organization that owns the copyright. The table below applies the four-part test to four statements.

**Worked example: grading four statements.** The statements are made-up examples.

| Statement | Verdict | What to do |
|---|---|---|
| "Licensed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. © 2025 Maria Lopez. Applies to all text on this page." | Complete | License, version, link, holder, and scope are all present. |
| "Some rights reserved." | Incomplete | No license is named. Look for the source or ask the owner. |
| "Free to use." | Not a license | The words do not say which uses are allowed. Ask, or treat the work as all rights reserved. |
| "Licensed under Creative Commons." | Incomplete | Which of the six, and which version? Check the source before you reuse it. |

### Third-Party Content

**Third-party content** is material inside a resource that someone other than the resource's owner created, such as a photograph, a chart, or a quotation. A page's license statement usually covers only what the page's owner made. Phrases like "except where otherwise noted" warn you that some items carry other licenses. Before you reuse a page, check the caption or credit line of each image and figure.

For example, suppose a CC BY textbook includes a photo credited "Used with permission of Example Agency." The textbook's license covers the author's own text and diagrams. The photo is not covered, so you may not copy it into your remix without the agency's permission.

!!! mascot-tip "Follow the Link Back"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    If you find a license statement on a copy, follow its link back to the original and read the license there. Copies can lose a statement or change it, and the original is the evidence.

The MicroSim below puts a license statement under a magnifying glass. The illustration shows the footer of an open lesson page, and its seven numbered markers point to the parts of a complete statement. In explore mode you read what each part does. In quiz mode you match a visual clue to its marker.

#### Diagram: Anatomy of a License Statement

<iframe src="../../sims/license-statement-anatomy/main.html" height="702px" width="100%" scrolling="no"></iframe>

[Run the Anatomy of a License Statement MicroSim Fullscreen](../../sims/license-statement-anatomy/main.html){ .md-button .md-button--primary }

<details markdown="1">
<summary>Anatomy of a License Statement</summary>
Type: infographic
**sim-id:** license-statement-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the seven parts of a complete license statement on an annotated page footer from a description of each part, with at least 6 of 7 correct on the first attempt.

**Prerequisites:** License Statement, Open License, Creative Commons, Third-Party Content (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 6 of 7 correct on the first attempt. Hovering markers in explore mode is exploration, not evidence.

**Misconceptions:** (1) The license icons alone are the license. (2) "CC BY" without a version is a complete statement. (3) A license statement on a page covers every image on it.

**Instructional Rationale:** Identifying the parts of a statement is a Remember-level task, and an annotated illustration places each part where it appears on a real page. The quiz asks the learner to recognize a part from how it looks, which is how they will find it on real pages.

**Content:**

The illustration is a text-free flat drawing of the bottom of a lesson web page inside a simple browser frame. Across the footer bar, left to right, are a row of four small round badge icons, two short stacked lines of text, an underlined link-shaped bar, and a copyright symbol beside a short name line. Above the footer is a framed picture thumbnail with a thin caption strip beneath it. At the far right of the footer is a small code-bracket icon, drawn as a shape. The seven markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | License badge icons | A row of four small round icons at the left of the footer. | The icons show at a glance which license elements apply. They are a hint, not the license itself. | Icons are easy to copy onto a page with no license, so always confirm the written statement. |
| 2 | License name and version | Two short stacked lines of text beside the icons. | The exact license name, for instance Creative Commons Attribution 4.0 International. The version matters because terms differ between versions. | "CC BY" alone leaves the version open. Write the full name or the version number. |
| 3 | Link to the license | An underlined bar that looks like a hyperlink. | A link to the license page, so readers can check the real terms. | Check that the link goes to the Creative Commons site and not to a copy. |
| 4 | Copyright holder and year | A copyright symbol beside a short name line. | Names who holds the copyright and when. This is the person to credit and the person to ask for permission. | The work of a school employee may belong to the school, so the named holder is the one to ask. |
| 5 | Scope of the license | A thin line directly under the license name. | States what the license covers: this page, the whole book, or only the text. | A missing scope is a question to ask the owner, not an assumption. |
| 6 | Notice for third-party content | The thin caption strip beneath the picture thumbnail. | Marks material that someone else owns or that carries a different license, for instance a photo used with permission. | Treat each image as separately licensed until its caption says otherwise. |
| 7 | Machine-readable license marking | The small code-bracket icon at the far right of the footer. | Hidden markup, like a link marked rel="license", lets search tools filter by license. Readers cannot see it on the page. | Look in the page source, or use a search tool's license filter. |

**Provenance:** The seven parts follow the chapter section "License Statement" and its example statements. The illustration is synthetic, and the sim labels the page "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 7 in the order of the table.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint, for instance "A row of four small round icons at the left of the footer".
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says the click was wrong and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 7 hints the sim shows the summary.

**Feedback:** 7 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 7 correct on the first attempt". At 6 or more it adds "You can find every part of a license statement." Below 6 it lists the labels of the missed parts.

**Starting State:** The illustration with seven numbered markers, explore mode active, and the prompt "Hover a marker to see what it is."

**Chapter Anchors:** The chapter says a complete license statement names the license and its version, links to the license text, identifies the owner, and says what the statement covers. The illustration shows seven parts, and the chapter's text mentions the scope, version, and holder.
</details>

## Giving Credit

### Attribution Statement

An **attribution statement** is the credit line that meets the attribution requirement. It tells readers who made the work, where it came from, and under which license it may be used. A good attribution statement is short, sits next to the item it credits, and gives the reader enough to find the original in a minute. If you changed the work, the statement also says what you changed, such as "translated into Spanish" or "reading level lowered." A statement that only says "image from the internet" gives no usable credit.

### TASL Attribution Format

The **TASL attribution format** is a four-part pattern that Creative Commons recommends for credit lines. TASL stands for Title, Author, Source, and License. Writing the four parts in order makes a statement hard to get wrong. The table shows what each part contains, using a made-up resource.

| Part | What to write | Example |
|---|---|---|
| Title | The work's name, in quotation marks | "Watershed Basics" |
| Author | The creator, and the organization if one is named | Maria Lopez |
| Source | A link to the work | https://example.org/watershed-basics |
| License | The license name and version, linked to the license | CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) |

Joined together, the credit reads: "Watershed Basics" by Maria Lopez, https://example.org/watershed-basics, licensed under CC BY 4.0. If you adapted it, add a sentence such as "Adapted: reading level lowered and two examples localized."

The MicroSim below gives you eight credit lines to inspect. For each one you decide which TASL parts are missing, and whether a change note is also needed.

#### Diagram: Attribution Statement Checker

<iframe src="../../sims/attribution-statement-checker/main.html" height="814px" width="100%" scrolling="no"></iframe>

[Run the Attribution Statement Checker MicroSim Fullscreen](../../sims/attribution-statement-checker/main.html){ .md-button .md-button--primary }

<details markdown="1">
<summary>Attribution Statement Checker</summary>
Type: microsim
**sim-id:** attribution-statement-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** assess<br/>
**Learning Objective:** The learner will assess whether each of eight attribution statements is complete by identifying exactly which of the five checked parts are missing, with at least 7 of 8 judged correctly on the first attempt.

**Prerequisites:** Attribution Requirement, Attribution Statement, TASL Attribution Format, CC BY (all defined in this chapter above this block).

**Evidence of Mastery:** For each statement the learner marks which of five parts are missing, or marks none. A judgment is correct when the marked set equals the Missing parts column in Content exactly. Mastery is at least 7 of 8 correct on the first attempt. Reading the checklist definitions is exploration, not evidence.

**Misconceptions:** (1) "CC BY" without a version is a complete license part. (2) A copyright line with no license counts as credit. (3) A change note is needed even when the work is unchanged. (4) A site name is a source link.

**Instructional Rationale:** Assessing a credit line against a criterion list is an Evaluate-level action, and the checklist makes the criteria explicit so the learner judges against standards, not impressions. Eight statements with different mixes of gaps force the learner to apply each criterion separately.

**Content:**

The resource record that every statement refers to (a made-up resource): Title "Watershed Basics", Author Maria Lopez, Source https://example.org/watershed-basics, License CC BY 4.0, license link https://creativecommons.org/licenses/by/4.0/.

The five checked parts and when each counts as present:

| Part | Counts as present when |
|---|---|
| Title | The work's name appears. |
| Author | The creator's name appears. |
| Source | A link to the work appears. A site name alone does not count. |
| License | A specific license with its version, or a link to it, appears. "Creative Commons" alone or "CC BY" with no version or link does not count. |
| Change note | A sentence says what was changed. Required only when the use changed the work. |

The eight statements:

| # | Use | Statement shown | Missing parts | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Unchanged | "Watershed Basics" by Maria Lopez, https://example.org/watershed-basics, licensed under CC BY 4.0. | None | All four TASL parts are present, and no change note is needed. |
| 2 | Unchanged | Maria Lopez, Watershed Basics. | Source, License | The link and the license are missing. |
| 3 | Unchanged | "Watershed Basics", https://example.org/watershed-basics, licensed CC BY. | Author, License | The creator is not named, and "CC BY" has no version or link. |
| 4 | Unchanged | "Watershed Basics" by Maria Lopez, https://example.org/watershed-basics, licensed under a Creative Commons license. | License | The statement does not say which license or version. |
| 5 | Unchanged | Image courtesy of Maria Lopez. | Title, Source, License | The work is not named, linked, or licensed. |
| 6 | Changed: reading level lowered, two examples localized | "Watershed Basics" by Maria Lopez, https://example.org/watershed-basics, licensed under CC BY 4.0. Adapted: reading level lowered and two examples localized. | None | The four TASL parts and the change note are all present. |
| 7 | Changed: translated into Spanish | "Watershed Basics" by Maria Lopez, https://example.org/watershed-basics, licensed under CC BY 4.0. | Change note | The work was translated, and the statement does not say so. |
| 8 | Changed: shortened | © Maria Lopez. All rights reserved. | Title, Source, License, Change note | The statement claims all rights reserved, which contradicts the CC BY license, and it omits the title, link, and change note. |

**Provenance:** The resource, creator, and URL are made up, and the sim labels them "illustrative example". The checked parts follow the chapter sections "Attribution Requirement", "Attribution Statement", and "TASL Attribution Format".

**Rules:** Each statement has a fixed set of missing parts, and the empty set is valid. A part is present only when it meets the "Counts as present when" rule. Change note is checked only for statements 6, 7, and 8, where the use column says the work was changed. For statements 1 to 5, Change note is not offered as a choice.

**Learner Activity:**

1. The learner sees the resource record, the use, and the statement.
2. The learner marks each missing part, or marks "None missing".
3. The learner presses Check. The sim shows the correct set and the Why text.
4. The learner moves to the next statement, until statement 8 is done.

**Feedback:** 8 statements in the fixed order, one attempt each. Correct: "Correct. [Why]". Incorrect: "Not quite. Missing: [missing parts, or none]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can check a credit line." Below 7 it lists the Why text of each missed statement.

**Starting State:** The resource record, the five parts and their rules, and statement 1 with all five parts unmarked. The question shown is "Which parts are missing?"

**Chapter Anchors:** The chapter says TASL stands for Title, Author, Source, and License, and its example credit line matches statement 1. The chapter says that a statement for an adapted work adds a change note.
</details>

## Combining Works

### License Compatibility

**License compatibility** is whether the licenses of two or more sources can all be satisfied at once by a single license on the combined work. You need it whenever you remix: a unit built from a CC BY chapter and a CC BY-SA chapter must carry one license, and that license must honor both sources. A simple method works for the six licenses. For each source, write what it requires of the combined work, then look for a license that meets every requirement. If more than one qualifies, use the first in the order CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA.

| Source license | What it requires of the combined work |
|---|---|
| CC0 | Nothing. |
| CC BY | Credit, and any CC license that keeps the credit. |
| CC BY-SA | The combined work must be CC BY-SA. |
| CC BY-NC | The combined work must be noncommercial. |
| CC BY-NC-SA | The combined work must be CC BY-NC-SA. |
| Any ND license | The source cannot be changed or blended and then shared. |

**Worked example: three combinations.** Apply the table to three pairs of sources.

1. CC BY with CC BY-SA: the second source requires CC BY-SA, and CC BY accepts it, so the result is CC BY-SA.
2. CC BY-NC with CC BY-NC-SA: the first needs noncommercial use, the second requires CC BY-NC-SA, and that satisfies both, so the result is CC BY-NC-SA.
3. CC BY-ND with any other source: the ND source cannot be changed or blended and then shared, so the combination cannot be shared at all.

This is a rule of thumb for study. Creative Commons publishes its own compatibility chart, and you should check it for any real combination.

### License Conflict

A **license conflict** is a case where no single license satisfies all the sources, so the combined work cannot legally be shared. CC BY-SA and CC BY-NC conflict: one requires the whole work to be CC BY-SA, which allows commercial use, and the other requires noncommercial use. CC BY-SA and CC BY-NC-SA also conflict, because each demands that the work carry its own license. When you face a conflict you have three choices. You can pick a different resource for one of the parts. You can ask an owner in writing to permit different terms. Or you can keep the works separate, each with its own license notice, so that you are not blending them into one work. Whether a packet counts as blended can be a judgment call, so ask the owners if you are unsure.

!!! mascot-encourage "Compatibility Trips Up Almost Everyone"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If license compatibility feels slippery, that is normal, because even experienced reviewers check a chart. You already solve problems like this when you match two schedules, and the same method works here. List what each source requires, then look for one license that meets all of it.

The MicroSim below gives you ten pairs of sources to combine. For each pair you choose the license the combined work may carry, or you recognize a conflict or a blocked combination.

#### Diagram: License Compatibility Checker

<iframe src="../../sims/license-compatibility-checker/main.html" height="614px" width="100%" scrolling="no"></iframe>

[Run the License Compatibility Checker MicroSim Fullscreen](../../sims/license-compatibility-checker/main.html){ .md-button .md-button--primary }

<details markdown="1">
<summary>License Compatibility Checker</summary>
Type: microsim
**sim-id:** license-compatibility-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** solve<br/>
**Learning Objective:** The learner will solve ten license-combination problems by finding the license a combined work may carry, or by recognizing a conflict or a blocked combination, with at least 8 of 10 correct on the first attempt.

**Prerequisites:** License Compatibility, License Conflict, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND, CC0 Dedication (all defined in this chapter above this block).

**Evidence of Mastery:** For each pair the learner chooses one of six outcomes. A choice is correct when it matches the Correct outcome column in Content. Mastery is at least 8 of 10 correct on the first attempt. Viewing the requirements table is exploration, not evidence.

**Misconceptions:** (1) Any two Creative Commons licenses can be combined. (2) The more restrictive license always wins. (3) CC BY-SA and CC BY-NC can be combined if the author gives credit. (4) An ND source can be remixed if the remix is credited.

**Instructional Rationale:** Solving combination problems is an Apply-level task, and ten pairs of increasing difficulty make the learner execute the same procedure repeatedly: write each source's requirement, intersect them, and choose the first qualifying license. Immediate feedback with the worked reasoning builds the habit.

**Content:**

The six outcomes the learner can choose: CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, Conflict (no license satisfies both), Blocked (an ND source cannot be shared in a combined work).

What each source requires of the combined work, written as the set of licenses it allows:

| Source | Licenses the combined work may carry |
|---|---|
| CC0 | CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA |
| CC BY | CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA |
| CC BY-SA | CC BY-SA |
| CC BY-NC | CC BY-NC, CC BY-NC-SA |
| CC BY-NC-SA | CC BY-NC-SA |
| CC BY-ND, CC BY-NC-ND | None: the combination is Blocked |

The ten pairs:

| # | Source A | Source B | Correct outcome | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | CC BY | CC BY | CC BY | Both allow any of the four licenses, and CC BY is first in the order. |
| 2 | CC BY | CC BY-SA | CC BY-SA | Only CC BY-SA satisfies the second source, and CC BY accepts it. |
| 3 | CC BY | CC BY-NC | CC BY-NC | The second source needs a noncommercial license, and CC BY-NC comes first among those. |
| 4 | CC BY-SA | CC BY-NC | Conflict | CC BY-SA allows only CC BY-SA, and CC BY-NC allows only noncommercial licenses, so there is no overlap. |
| 5 | CC BY-NC | CC BY-NC-SA | CC BY-NC-SA | CC BY-NC-SA is the only license that satisfies both. |
| 6 | CC BY-SA | CC BY-NC-SA | Conflict | Each requires its own license, and the two are different. |
| 7 | CC BY | CC BY-ND | Blocked | The ND source cannot be changed or blended and then shared. |
| 8 | CC0 | CC BY-SA | CC BY-SA | CC0 allows any of the four, and CC BY-SA is the only one that satisfies the other source. |
| 9 | CC0 | CC BY | CC BY | Both allow any of the four, and CC BY is first. |
| 10 | CC BY-NC | CC BY-NC-ND | Blocked | The ND source cannot be changed or blended and then shared. |

**Provenance:** The requirements table is this chapter's rule of thumb, written for study and consistent with the chapter sections "License Compatibility" and "License Conflict". The sim labels it "a study aid, not a legal chart" and links to the Creative Commons compatibility chart as the authority.

**Rules:** The correct outcome for a pair is the first license, in the order CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, that appears in the allowed set of both sources. If the two allowed sets share no license the outcome is Conflict. If either source is an ND license the outcome is Blocked, whatever the other source is. Each pair has exactly one correct outcome.

**Learner Activity:**

1. The learner sees a pair of sources and the six outcomes.
2. The learner may open the requirements table. Opening it does not change the score.
3. The learner chooses an outcome.
4. The sim shows whether it was correct and the Why text, then presents the next pair.
5. After pair 10 the sim shows the summary.

**Feedback:** 10 pairs in the fixed order, one attempt each. Correct: "Correct: [outcome]. [Why]". Incorrect: "Not quite. The answer is [outcome]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 8 or more it adds "You can combine licenses." Below 8 it lists the Why text of each missed pair.

**Starting State:** Pair 1 with the six outcomes and the requirements table closed. The question shown is "Which license may the combined work carry?"

**Chapter Anchors:** The chapter says CC BY-SA and CC BY-NC conflict, CC BY-SA and CC BY-NC-SA conflict, CC BY with CC BY-SA gives CC BY-SA, CC BY-NC with CC BY-NC-SA gives CC BY-NC-SA, and any ND source blocks sharing the combination. The chapter's first-in-order rule uses the order CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA.
</details>

## Fair Use

**Fair use** is a U.S. legal doctrine that lets people use copyrighted work without permission in some situations, such as teaching, criticism, and news reporting. A court weighs four factors:

- **Purpose and character:** whether the use is educational and transformative or commercial.
- **Nature of the work:** whether the work is factual or creative.
- **Amount used:** how much of the work is used, and whether it is the heart of the work.
- **Market effect:** whether the use harms the owner's ability to sell the work.

Fair use is decided case by case, usually after a dispute has begun, so you cannot know in advance how a court would rule. It is a defense, not a license. For OER work, that has two consequences. Fair use does not let you share a changed copy of a whole resource, and it does not replace a license that already covers your use. If a license covers what you want to do, rely on the license. Keep fair use in reserve for small excerpts, such as quoting a paragraph in a review, and note that other countries have different rules. This is general information, not legal advice.

## License Selection

**License selection** is the choice of which license to put on a work you own. Three questions drive the choice: will you allow commercial reuse, will you allow others to share changed versions, and must changed versions carry the same license? The table maps the answers to a license.

| Allow commercial reuse? | Allow shared changes? | Same license on changes? | License |
|---|---|---|---|
| Yes | Yes | No | CC BY |
| Yes | Yes | Yes | CC BY-SA |
| No | Yes | No | CC BY-NC |
| No | Yes | Yes | CC BY-NC-SA |
| Yes | No | Not applicable | CC BY-ND |
| No | No | Not applicable | CC BY-NC-ND |

If you want no conditions at all, CC0 does that. Five practical points apply before you decide:

- **Ownership:** check who owns the work. A school's policy or your employment contract may give the school the right to choose.
- **Funders:** some grants require a specific license, so read the grant terms first.
- **Third-party content:** you can license only what you own, so replace or credit any item that belongs to someone else.
- **Permanence:** you can stop offering a work, but people who already received it keep their rights.
- **Software:** Creative Commons recommends licenses designed for software when you share code, not CC licenses.

!!! mascot-thinking "Choosing Is Giving"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Choosing a license is choosing which freedoms to give away. Each condition you add protects something you care about and removes a use someone else could have made.

The default advice in OER work is CC BY for the widest reuse, or CC BY-SA when you want improvements to stay open. NC and ND licenses reduce reuse, so choose them for a reason you can state. [Chapter 9](../09-modularity-metadata/index.md) shows how the rubric scores that choice. The last MicroSim of the chapter is a practice round. You read a teacher's goal and choose the license that serves it.

#### Diagram: License Selection Advisor

<iframe src="../../sims/license-selection-advisor/main.html" height="686px" width="100%" scrolling="no"></iframe>

[Run the License Selection Advisor MicroSim Fullscreen](../../sims/license-selection-advisor/main.html){ .md-button .md-button--primary }

<details markdown="1">
<summary>License Selection Advisor</summary>
Type: microsim
**sim-id:** license-selection-advisor<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the three license-selection questions to choose the license that serves each of seven stated goals, with at least 6 of 7 correct on the first attempt.

**Prerequisites:** License Selection, CC0 Dedication, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND (all defined in this chapter above this block).

**Evidence of Mastery:** For each goal the learner chooses one of seven licenses. A choice is correct when it matches the Correct license column in Content. Mastery is at least 6 of 7 correct on the first attempt. Opening the question table is exploration, not evidence.

**Misconceptions:** (1) NonCommercial protects a creator without limiting reuse much. (2) NoDerivatives and ShareAlike can be combined. (3) CC BY is the only open choice.

**Instructional Rationale:** Choosing a license for a goal is an Apply-level task that uses the three questions as a procedure. One goal per license makes the learner discriminate between neighboring options.

**Content:**

The seven license choices: CC0, CC BY, CC BY-SA, CC BY-NC, CC BY-NC-SA, CC BY-ND, CC BY-NC-ND.

The three questions, shown on request: Will you allow commercial reuse? Will you allow others to share changed versions? Must changed versions carry the same license?

The seven goals:

| # | Goal shown to the learner | Correct license | Why (shown as feedback) |
|---|---|---|---|
| 1 | "I want no friction at all. Anyone may do anything." | CC0 | CC0 gives up all conditions, including credit. |
| 2 | "Anyone may use, change, and sell my worksheet. I only need credit." | CC BY | BY is the only condition, and commercial reuse and changes are allowed. |
| 3 | "Anyone may use and sell my unit, but every changed version must stay open under the same terms." | CC BY-SA | SA keeps changed versions under the same license, and commercial use stays allowed. |
| 4 | "Others may change my lesson, but they may not make money from it, and I do not mind which license their changes use." | CC BY-NC | NC blocks commercial use, and without SA, adapters choose their license. |
| 5 | "Others may change my lesson noncommercially, and every changed version must carry my license." | CC BY-NC-SA | NC blocks commercial use, and SA requires the same license on changes. |
| 6 | "Anyone may share my finished report, even for sale, but nobody may share a changed version." | CC BY-ND | ND forbids changed versions, and there is no NC element. |
| 7 | "Anyone may share my unchanged handout, but not for money, and nobody may share a changed version." | CC BY-NC-ND | It combines NC and ND. |

**Provenance:** The goals are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The mapping follows the chapter's license-selection table.

**Rules:** Each goal has exactly one correct license, one per license. The three questions determine the choice as shown in the chapter's table. CC0 applies only when the goal asks for no conditions.

**Learner Activity:**

1. The learner reads a goal.
2. The learner may open the three questions.
3. The learner chooses one of the seven licenses.
4. The sim shows whether it was correct and the Why text, then presents the next goal.
5. After goal 7 the sim shows the summary.

**Feedback:** 7 goals in a shuffled order, one attempt each. Correct: "Correct: [license]. [Why]". Incorrect: "Not quite. The answer is [license]. [Why]". The summary shows "[n] of 7 correct on the first attempt". At 6 or more it adds "You can pick a license for a goal." Below 6 it lists the Why text of each missed goal.

**Starting State:** Goal 1 or the first goal in the shuffled order, with the seven licenses and the question "Which license fits this goal?"

**Chapter Anchors:** The chapter's table maps three yes-or-no answers to six licenses, and says CC0 applies when you want no conditions at all.
</details>

## Key Takeaways

- An **open license** gives everyone permission in advance. A **proprietary license** and **all rights reserved** grant little or nothing, so read them before you assume.
- **Creative Commons** offers six licenses built from four elements: attribution (BY), ShareAlike (SA), NonCommercial (NC), and NoDerivatives (ND). SA and ND never appear together, and **CC0** is a dedication with no conditions.
- NC is blurrier than it sounds, and ND blocks the improvements this book teaches you to make.
- A complete **license statement** names the license and version, links to it, names the owner, and says what it covers. **Third-party content** may be licensed separately.
- Credit with **TASL**: Title, Author, Source, License, plus a note of any change.
- **License compatibility** asks whether one license satisfies every source. A **license conflict** means none does, and an ND source blocks sharing entirely.
- **Fair use** is a case-by-case defense and not a license. **License selection** is a choice of which freedoms to give.

!!! mascot-celebration "You Can Read a License"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now tell the six Creative Commons licenses apart, write a TASL credit line, and check whether two licenses can be combined. That is the reading skill every reusability score in this book depends on.

[See Annotated References](./references.md)
