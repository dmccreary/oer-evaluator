---
title: "Improving a Resource with AI Agents"
description: "Guides teachers through an improvement plan that uses agents to fix alt text, headings, reading level, metadata, and links, then re-scores the resource and reviews every change."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:54:40"
version: 1.11
---

# Improving a Resource with AI Agents

## Summary

Guides teachers through an improvement plan that uses agents to fix alt text, headings, reading level, metadata, and links, then re-scores the resource and reviews every change. It turns scores into action and relies on every metric chapter and on checked agent output. After this chapter you can write an improvement plan, use agents to fix the lowest-scoring metrics, and re-score the result to show the gain.

## Concepts Covered

This chapter covers the following 22 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Improvement Plan | 151 |
| Lowest Metric First | 1 |
| Improvement Challenge | 25 |
| AI Alt Text Generation | 1 |
| Caption Generation | 1 |
| Heading Repair | 1 |
| Chapter Splitting | 1 |
| Metadata Generation | 1 |
| License Statement Repair | 1 |
| PDF-to-Markdown Conversion | 1 |
| Practice Question Generation | 1 |
| Glossary Generation | 1 |
| MicroSim Building | 1 |
| Link Repair | 1 |
| Content Update | 1 |
| Re-Scoring | 107 |
| Score Gain | 103 |
| Change Log Entry | 1 |
| Human Review of Changes | 3 |
| Derivative Work | 7 |
| Preserving Original Meaning | 2 |
| Reading Level Rewrite | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Foundations of Open Educational Resources](../01-foundations-of-oer/index.md)
- [Chapter 2: Open Licenses and Attribution](../02-open-licenses-attribution/index.md)
- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)
- [Chapter 4: Open File Formats and Version Control](../04-open-formats-version-control/index.md)
- [Chapter 5: Accuracy and Currency](../05-accuracy-currency/index.md)
- [Chapter 6: Alignment and Readability](../06-alignment-readability/index.md)
- [Chapter 7: Accessibility](../07-accessibility/index.md)
- [Chapter 8: Practice and Feedback](../08-practice-feedback/index.md)
- [Chapter 9: Modularity and Metadata](../09-modularity-metadata/index.md)
- [Chapter 12: AI Agents, Prompts, and Rubric Scoring](../12-ai-agents-prompts-scoring/index.md)
- [Chapter 13: Automated Checks, Cost, and Student Privacy](../13-automated-checks-cost-privacy/index.md)
- [Chapter 14: Checking and Calibrating AI Agent Output](../14-checking-agent-output/index.md)

---

!!! mascot-welcome "From Scores to Better Resources"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A score is only useful if it leads to a better resource, and this chapter shows you how to get there with an agent as your helper. You will plan the work, make each fix, keep a record, and prove the gain. Let's dive in and check the evidence!

The earlier chapters taught you to measure a resource. This chapter uses the measurements to improve one. An agent is a good helper for this work, because many fixes are repetitive drafting tasks: describe five images, write a summary, split a long page. An agent is also a risky helper, because it may change a meaning, invent a source, or damage something that worked. So the method has a fixed shape. You plan the work, check that the license allows it, make each fix with an agent, review every change as a person, keep a log, and score the result again.

Throughout the chapter the example is *Watershed Basics*, the reading and quiz that scored 65 in Chapter 3 and earned the decision *Revise* because Metadata sat at 4. By the end of the chapter the improved version scores 78 and earns *Adopt*, and the gap between the plan and the result teaches a lesson of its own.

## Improvement Plan

An **improvement plan** is a written list of the fixes to make to a resource, in the order to make them, with the score each fix is expected to raise and the time it will take. It is the bridge between the scores and the work. A score says where a resource is weak. A plan says what to do about it, who does it, and how you will know it worked.

The evidence from the first scoring is the raw material. Every check that failed in Chapters 5 through 10 is a possible task. Chapter 3 asked reviewers to record evidence for each score, and this is where that habit pays back: a reviewer who wrote "4 of 5 images have alt text, and 2 of the 4 are one word" has already written most of an alt text task.

A useful plan has five parts:

1. **The baseline:** the ten scores, the total, and the decision before any change.
2. **The gaps:** the failed checks that hold each low score down.
3. **The fixes:** one task per gap, in plain words, with the tool or agent that will do the drafting.
4. **The order and the budget:** which fix comes first, and the human hours each one needs.
5. **The target:** the score the plan aims for, and the decision it should earn.

**Worked example: the plan for *Watershed Basics*.** The gaps come from the evidence recorded in Chapters 5 through 10. The hours are the time a person needs, including review, and are estimates for this book's example.

| Order | Metric | Now | Target | Fix, in plain words | Hours | Projected gain |
|---|---|---|---|---|---|---|
| 1 | Metadata | 4 | 8 | Draft the missing subject, grade level, and description, and add the license to the file properties | 0.5 | +4 |
| 2 | Accessibility | 5 | 8 | Write fuller alt text for three images, add captions to the video, repair the heading jump, and test contrast | 2.0 | +3 |
| 3 | Modularity | 5 | 8 | Split the quiz from the reading so each stands alone | 1.5 | +3 |
| 4 | Practice with feedback | 6 | 8 | Add explanations to the two questions that lack them, a worked example, and a short simulation | 2.5 | +2 |
| 5 | Accuracy and currency | 7 | 9 | Repair the 2 broken links and update the outdated river-length figure | 1.0 | +2 |
| | **Total** | **65** | **79** | | **7.5** | **+14** |

The projected gain is the number of total points a fix is expected to add. The plan expects 65 plus 14, which is 79, and the decision *Adopt*, since 79 is at least 75 and the lowest metric would be 6. Alignment, at 6, is left for a second round, because raising it means adding a question for the third learning outcome, and that choice belongs to the author.

A plan is a forecast, so write it before the work and compare it with the result afterward. The comparison is the subject of the last sections of the chapter.

### Lowest Metric First

**Lowest metric first** is the rule that a plan starts with the lowest-scoring metric. Three reasons support it. The adoption rule of Chapter 11 sets a floor, so a metric under 5 blocks adoption however high the total is. The lowest scores often have the cheapest large gains, since a record with two of six fields filled can reach six in minutes. And a total hides the weakest metric, which Chapter 3 warned about.

The rule has one exception. If the fix for the lowest metric is expensive or needs a decision from the author, do the cheaper fixes first and flag the expensive one. For *Watershed Basics* the rule works cleanly. Metadata, at 4, blocks adoption by itself, and its fix takes half an hour. After it, Accessibility and Modularity tie at 5. The plan puts Accessibility first, because a barrier that keeps some learners out matters more than a reuse problem, even though Modularity is cheaper at 1.5 hours against 2.0.

## Derivative Work

A **derivative work** is a new work based on an existing one: a translation, an adaptation, a remix, or an improved edition. When an agent edits a resource, the edited version is a derivative work of the original. Copyright gives an owner the right to control derivative works, and an open license is the owner's advance permission, with conditions. So the first step before any edit is to read the license and check that it allows the edit you plan.

The table shows what each license allows for an improved version that you want to publish.

| License | May you publish an improved version? | What you must do |
|---|---|---|
| CC0 | Yes | Nothing is required, and giving credit is good practice |
| CC BY | Yes | Credit the author, link to the license, and say that you changed the work |
| CC BY-SA | Yes | The same as CC BY, and release your version under CC BY-SA |
| CC BY-NC | Yes, without commercial use | The same as CC BY, and do not sell or use it for commercial gain |
| CC BY-NC-SA | Yes, without commercial use | The same as CC BY, release under CC BY-NC-SA, and do not use it commercially |
| CC BY-ND | No, you may not share a changed version | You may make changes for your own private use only |
| No license, all rights reserved | No | Ask the owner for permission first |

!!! mascot-warning "Read the License Before the First Edit"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A NoDerivatives license or a missing license stops the work before it starts. Check the license first, and save your effort for resources you may legally improve.

*Watershed Basics* carries CC BY 4.0, so its improved version may be published with credit to Maria Lopez, a link to the license, and a note that the text was changed. Two cautions remain. The license on the text does not cover the third-party images, which carry their own terms, so an image whose terms forbid changes must be replaced and not edited. And the agent service you use has its own terms, which Chapter 13 asked you to read before sending any resource to it.

The MicroSim below practices the check. It gives eight planned improvements, each with the license of the original, and for each one you decide whether the plan is allowed.

#### Diagram: Derivative Permission Checker

<details markdown="1">
<summary>Derivative Permission Checker</summary>
Type: microsim
**sim-id:** derivative-permission-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the license rules to eight planned improvements and decide whether each plan is allowed as planned or not allowed as planned, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Derivative Work, and the license elements of Chapter 2 (BY, SA, NC, ND, and CC0) (all defined in this chapter above this block or in Chapter 2).

**Evidence of Mastery:** For each plan the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the license table is exploration, not evidence.

**Misconceptions:** (1) Any open license lets you publish a changed version. (2) NoDerivatives forbids all changes, including private ones. (3) A free license means you owe nothing in return.

**Instructional Rationale:** Applying a license rule to a planned action is an Apply-level task that every improvement starts with. Eight plans that differ in license and in intended use teach the learner to read both parts before deciding.

**Content:**

The two bins: Allowed as planned, and Not allowed as planned.

The license table, available on demand: CC0 allows publishing a changed version with nothing required. CC BY allows it with credit, a link to the license, and a note that changes were made. CC BY-SA adds that the new version must carry CC BY-SA. CC BY-NC allows it without commercial use. CC BY-ND does not allow sharing a changed version, and allows private changes. A resource with no license and all rights reserved allows nothing without the owner's permission.

The eight plans (all made up):

| # | Plan | Correct bin | What the learner is told afterward |
|---|---|---|---|
| 1 | The original is CC BY. The plan is to add alt text and post the improved version free for anyone. | Allowed as planned | Credit the author, link the license, and say that you changed the work. |
| 2 | The original is CC BY-SA. The plan is to split it into modules and post them free for anyone. | Allowed as planned | Credit the author, link the license, say that you changed the work, and release the modules under CC BY-SA. |
| 3 | The original is CC BY-ND. The plan is to rewrite it for a lower reading level and post the rewrite free. | Not allowed as planned | NoDerivatives does not allow sharing a changed version. Ask the owner, or keep the rewrite private. |
| 4 | The original is CC BY-NC. The plan is to improve it and sell it in a paid course. | Not allowed as planned | NonCommercial does not allow selling it. Ask the owner for permission. |
| 5 | The original is CC BY-NC. The plan is to improve it and post it free for other teachers. | Allowed as planned | Credit the author, link the license, say that you changed the work, and do not use it commercially. |
| 6 | The original has no license and says all rights reserved. The plan is to fix its links and post the fixed version. | Not allowed as planned | No permission has been given. Ask the owner first. |
| 7 | The original is CC0. The plan is to improve and publish it with no credit line. | Allowed as planned | Nothing is required, and giving credit is good practice. |
| 8 | The original is CC BY-ND. The plan is to improve a copy for the learner's own use and share it with no one. | Allowed as planned | NoDerivatives allows private changes that are not shared. |

**Provenance:** The plans are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The license rules follow Chapter 2 and the chapter section "Derivative Work". The sim adds the note "check the legal text of your license".

**Rules:** Each plan has exactly one correct bin. Five plans are Allowed as planned and three are Not allowed as planned.

**Learner Activity:**

1. The learner sees one plan and may open the license table. Opening it does not change the score.
2. The learner places the plan in a bin, and the placement is committed.
3. The sim shows whether it was correct and the text in the last column of the table.
4. After plan 8 the sim shows the summary.

**Feedback:** 8 plans in a shuffled order, one attempt each. Correct: "Correct: [bin]. [afterward text]". Incorrect: "Not quite. This plan is [bin]. [afterward text]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can check a license before you edit." Below 7 it lists the afterward text of each missed plan.

**Starting State:** The first plan in the shuffled order and the two bins. The question shown is "May you do this with the original?"

**Chapter Anchors:** The chapter's license table lists the same seven cases. The sim adds the private-copy case for NoDerivatives and the free-versus-paid case for NonCommercial.
</details>

### Preserving Original Meaning

**Preserving original meaning** is the rule that an improvement changes the form of a resource and not what it says. An agent rewriting a sentence for clarity may quietly drop a qualifier, turn a possibility into a certainty, or add a claim that sounds helpful. Each of these changes the author's meaning, and a reader who trusts the source is misled.

Five kinds of edit change meaning without looking like it:

- **A changed quantity:** "about 6,000" becomes "more than 6,000".
- **A changed strength:** "can carry pollutants" becomes "always carries pollutants".
- **A dropped qualifier:** "most rain soaks in" becomes "rain soaks in".
- **An added claim:** a sentence about wetlands gains the clause "and remove all pollutants".
- **A dropped item:** "the river and its tributaries" becomes "the river".

The checks are plain. Compare the before and after side by side in a difference view, one claim at a time. Ask the agent to list every claim it changed, added, or removed, and treat any added claim as rejected unless a source supports it, as Chapter 14 taught. Keep corrections separate from rewrites: when you fix an error, as in Content Update later in this chapter, log it as a correction so that a reader of the log can see that meaning changed on purpose.

The MicroSim below practices the comparison. It shows ten sentences before and after an agent's edit, and for each pair you decide whether the meaning was preserved.

#### Diagram: Meaning Preservation Checker

<details markdown="1">
<summary>Meaning Preservation Checker</summary>
Type: microsim
**sim-id:** meaning-preservation-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of ten edited sentences keeps the meaning of the original, and name the kind of change when it does not, with at least 9 of 10 verdicts correct on the first attempt.

**Prerequisites:** Preserving Original Meaning, Hallucination (both defined in this chapter above this block or in Chapter 14).

**Evidence of Mastery:** For each pair the learner commits Meaning preserved or Meaning changed. A verdict is correct when it matches the Correct verdict column in Content. When the verdict is Meaning changed, the learner also names the kind of change from the five listed, and the kind is checked in the feedback. Mastery is at least 9 of 10 verdicts correct on the first attempt. Reading the five kinds is exploration, not evidence.

**Misconceptions:** (1) A shorter sentence keeps the same meaning. (2) A small word change is harmless. (3) An edit that adds a true-sounding claim is an improvement.

**Instructional Rationale:** Judging whether an edit keeps the author's meaning is an Evaluate-level action that every reviewer of an agent's edits performs. Pairs that include a harmless rewrite and a subtle one teach the learner to compare each qualifier.

**Content:**

The two verdicts: Meaning preserved, Meaning changed. The five kinds of change: Changed quantity, Changed strength, Dropped qualifier, Added claim, Dropped item.

The ten pairs (all made up):

| # | Before | After | Correct verdict | Kind of change | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | A watershed is an area of land where all the water drains to the same place. | A watershed is land whose water all drains to one place. | Meaning preserved | None | The claim is the same in fewer words. |
| 2 | The Clearwater River drains about 6,000 square miles. | The Clearwater River drains more than 6,000 square miles. | Meaning changed | Changed quantity | "About" became "more than". |
| 3 | Most rain soaks into the ground. | Rain soaks into the ground. | Meaning changed | Dropped qualifier | "Most" was dropped, so the claim now covers all rain. |
| 4 | Infiltration is the process by which water enters soil. | Infiltration is how water moves into soil. | Meaning preserved | None | The claim is the same in plainer words. |
| 5 | Runoff can carry pollutants into the river. | Runoff always carries pollutants into the river. | Meaning changed | Changed strength | "Can" became "always". |
| 6 | Wetlands slow the flow of water. | Wetlands slow the flow of water and remove all pollutants. | Meaning changed | Added claim | A new claim was added. |
| 7 | Students should record the water level every day for one week. | Students should record the water level daily for a week. | Meaning preserved | None | The instruction is the same. |
| 8 | The map shows the river and its tributaries. | The map shows the river. | Meaning changed | Dropped item | The tributaries were dropped. |
| 9 | Plants along the bank hold the soil in place. | Plants on the riverbank keep the soil from washing away. | Meaning preserved | None | The claim is the same in other words. |
| 10 | Lake Marlow is the largest lake in the watershed. | Lake Marlow is the biggest lake in the watershed. | Meaning preserved | None | "Biggest" and "largest" mean the same here. |

**Provenance:** The sentences are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The five kinds of change follow the chapter section "Preserving Original Meaning".

**Rules:** Each pair has exactly one correct verdict. Five pairs are Meaning preserved and five are Meaning changed, one for each kind of change. A verdict counts as correct on the verdict alone, and the kind of change is shown as feedback.

**Learner Activity:**

1. The learner sees one pair, with the changed words not marked.
2. The learner chooses a verdict. If the verdict is Meaning changed, the learner also picks the kind of change.
3. The sim shows whether the verdict was correct, the kind of change, and the Why text, and marks the changed words.
4. After pair 10 the sim shows the summary.

**Feedback:** 10 pairs in a shuffled order, one attempt each. Correct: "Correct: [verdict]. [Why]". Incorrect: "Not quite. The meaning was [verdict]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can check an edit against the original." Below 9 it lists the Why text of each missed pair.

**Starting State:** The first pair in the shuffled order and the two verdicts. The question shown is "Does the second sentence say the same thing?"

**Chapter Anchors:** The chapter lists five kinds of edit that change meaning: a changed quantity, a changed strength, a dropped qualifier, an added claim, and a dropped item. Each kind appears once in the pairs.
</details>

---

## The Fix Toolkit

Thirteen fixes cover most of what the metric chapters found. They fall into five groups by the metric they raise: accessibility, readability, accuracy, the reusability metrics, and practice. Every fix follows the same loop. The agent drafts the change, the agent's likely mistake is known in advance, and a person runs a specific check before the change is kept. Each fix below names the mistake to expect and the check to run.

### AI Alt Text Generation

**AI alt text generation** is the use of an agent that can see images to draft alt text for them. Chapter 7 taught that good alt text says what an image does in its context, and an agent sees pixels and not purpose. To get purpose, give the agent the paragraph around each image and the lesson goal, and ask for one or two sentences.

Expect four mistakes: text that is too generic, details that are not in the image, a wrong count or label on a map or chart, and a missing role for a decorative image, which should get an empty alt attribute. The check is to look at each image beside its draft and apply the Chapter 14 decisions: accept it, correct it, or reject it. For *Watershed Basics*, three images need new text: one has none and two have a single word. The other two already pass.

!!! mascot-tip "Give the Agent the Sentence Around the Image"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    The same photo needs different alt text in a lesson about river bends and in a lesson about bridges. Paste the surrounding paragraph into the prompt so that the agent can tell which job the image is doing.

#### Diagram: AI Alt Text Reviewer

<details markdown="1">
<summary>AI Alt Text Reviewer</summary>
Type: microsim
**sim-id:** ai-alt-text-reviewer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge each of six AI-drafted alt texts as accept, correct, or reject, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** AI Alt Text Generation, Accept Correct or Reject, Hallucination, and the alt text sections of Chapter 7 (all defined in this chapter above this block or in earlier chapters).

**Evidence of Mastery:** For each draft the learner commits one of three decisions. A decision is correct when it matches the Correct decision column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the decision definitions is exploration, not evidence.

**Misconceptions:** (1) A fluent description is a correct one. (2) Every image needs alt text with words. (3) A draft that is almost right should be thrown away.

**Instructional Rationale:** Judging a draft against the image and its lesson context is an Evaluate-level action. Drafts that are accurate, generic, wrongly detailed, and invented teach the learner to compare each draft with what the image shows and what the lesson needs.

**Content:**

The three decisions: Accept (accurate and useful as written), Correct (right in substance, with a detail or purpose to fix), Reject (describes something that is not in the image).

The six items (all made up). Each shows a plain description of what the image contains, the lesson sentence beside it, and the agent's draft:

| # | What the image contains | Lesson sentence | Agent draft | Correct decision | Corrected text shown after | Why (shown as feedback) |
|---|---|---|---|---|---|---|
| 1 | A photo of the Clearwater River in a wide bend, seen from a bridge. | Rivers on flat land bend back and forth in curves called meanders. | A photo of a river. | Correct | The Clearwater River curving in a wide bend, seen from a bridge. | The draft is generic and misses the bend that the lesson is about. |
| 2 | A bar chart of monthly river flow, highest in April and lowest in September. | River flow is highest in spring. | Bar chart of monthly river flow, highest in April and lowest in September. | Accept | None | The draft is accurate and short. The chart still needs a data table nearby. |
| 3 | A thin decorative wave line between two sections. | None | Blue wave line separating two sections. | Correct | Empty alt text | A decorative image should have empty alt text so that a screen reader skips it. |
| 4 | A diagram of the water cycle with arrows from the ocean to a cloud to a mountain to a river. | Water moves in a cycle between the sea, the air, and the land. | A satellite photo of a city at night. | Reject | A diagram of the water cycle, with arrows from the ocean to a cloud, to a mountain, and to a river. | The draft describes something that is not in the image. |
| 5 | A photo of two students measuring the depth of a stream with a ruler. | Students measure the depth of the stream. | Two students use a ruler to measure the depth of a stream. | Accept | None | The draft matches the image and the lesson. |
| 6 | A map of the river with two tributaries. | The map shows how the tributaries join the river. | Map showing the river and its three tributaries. | Correct | Map showing the river and its two tributaries. | The draft is right in substance and the count is wrong. |

**Provenance:** The images and drafts are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The decisions follow Chapter 14 and the alt text rules of Chapter 7.

**Rules:** Each item has exactly one correct decision. Two are Accept, three are Correct, and one is Reject. The sim shows each image as a plain description of its contents.

**Learner Activity:**

1. The learner sees the image description, the lesson sentence, and the agent's draft.
2. The learner chooses a decision, and the choice is committed.
3. The sim shows whether it was correct, the corrected text when there is one, and the Why text.
4. After item 6 the sim shows the summary.

**Feedback:** 6 items in a shuffled order, one attempt each. Correct: "Correct: [decision]. [Why]". Incorrect: "Not quite. The decision is [decision]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can review an agent's alt text." Below 5 it lists the Why text of each missed item.

**Starting State:** The first item in the shuffled order and the three decisions. The question shown is "What should the reviewer do with this draft?"

**Chapter Anchors:** The chapter lists four mistakes in agent alt text: generic text, details not in the image, wrong counts or labels, and a missing decorative role. Items 1, 4, 6, and 3 show them in that order.
</details>

### Caption Generation

**Caption generation** is the use of a speech-to-text tool, with an agent to tidy the output, to draft timed captions for a video. The draft includes the words and the times at which they appear. An agent can also fix punctuation, split lines at natural pauses, and add a sound cue where one matters.

The expected mistakes are mis-heard technical words, wrong names, missing speaker changes, and drifting time codes. In a watershed lesson, "aquifer" can become "a quiver" and change what a learner reads. The check is for a person to watch the video once from start to finish while reading the captions, so plan at least the length of the video for review. Offer a separate transcript as well, as Chapter 7 advised. For *Watershed Basics*, the video has no captions, and Chapter 7 treated that as a serious failure. Adding captions is the largest part of the Accessibility fix.

### Heading Repair

**Heading repair** is the correction of a resource's heading levels so that they form a clean outline. Screen reader users jump between headings, and a skipped level makes the outline confusing. An agent can read the page, list the headings, and propose levels with no skips, one top-level heading, and wording that describes each section.

The mistake to expect is an agent that renames or merges headings to make them tidy, which changes the structure the author chose. The check is to list the outline before and after as an indented list and confirm that the sections stay in the same order with the same names. For *Watershed Basics*, a heading jumps from level 2 to level 4, and the repair is one change.

| Outline | Before | After |
|---|---|---|
| Level 1 | Watershed Basics | Watershed Basics |
| Level 2 | What is a watershed? | What is a watershed? |
| Level 3 | (missing) | Rivers and tributaries |
| Level 4 | Rivers and tributaries | (none) |

### Reading Level Rewrite

A **reading level rewrite** is the revision of a passage to bring it closer to the grade level of its audience. It is the right fix only when readability is a low metric or when one passage sits well above the audience. An agent can shorten sentences, choose plainer words, and add a definition for a hard term.

The mistakes to expect are lost precision and lost meaning, since a simpler sentence can say less or say something different. Keep the technical terms and define them, and never swap a term for a vaguer word. Check the result with the readability tool of Chapter 6 and with the five meaning checks above. A sentence like "Precipitation infiltrates permeable strata and recharges the aquifer" becomes "Rain soaks into the ground and refills the aquifer, an underground layer of rock or sand that holds water." The second version adds a definition that the author should approve. For *Watershed Basics*, Readability is already 8 and only one section sits above the audience, so the plan leaves this fix out.

### Glossary Generation

**Glossary generation** is the use of an agent to list the terms in a resource that a learner may not know and to draft a definition for each. Good definitions are precise, short, and not circular, and they do not begin with "is when". The agent should list only terms that the resource uses, and write each definition for the way the resource uses it.

The mistake to expect is a definition from the model's general knowledge that differs from the resource's use of the term. The check is to compare each definition with the resource and with a trusted source, and to define each term where it first appears as well as in the glossary. For *Watershed Basics*, "aquifer" is used and never defined. One glossary entry and one sentence at first use close the gap, and both raise Readability.

### Link Repair

**Link repair** is the replacement of broken links with working ones. A link checker, which is a tool and not an agent, finds the links that fail. An agent can then propose a replacement: a new address for the same page, an archived copy such as one from the Internet Archive's Wayback Machine, or another source that supports the same claim.

The mistake to expect is an invented address, or a real page that says something different. The check is to open every new link and read the sentence it supports. Then record the date of the test, since links fail again. For *Watershed Basics*, 2 of 14 links failed on 2026-10-12, and the repair replaces both.

### Content Update

**Content update** is the replacement of an outdated fact with a current one. An agent drafts the new wording from a source that you supply or approve. It must not draft it from memory, because a figure from memory is the commonest hallucination in a repair.

The check is to open the source, confirm the figure and the date, and cite the source in the text. Log the change as a correction and not as a rewrite, since the meaning changes on purpose. For *Watershed Basics*, Section 2 says the Clearwater River is 410 miles long and the State Water Agency now gives 398. The update replaces the figure, cites the agency's page with the date it was read, and adds a log entry that names the old and new values.

### Metadata Generation

**Metadata generation** is the use of an agent to draft the descriptive fields of a metadata record from the resource itself. Chapter 9 named six core fields: title, author, subject, grade level, license, and description. The agent reads the resource and proposes each missing field, and it can add keywords.

The mistakes to expect are a guessed author, a license that the agent assumes and does not read, and a description that promises more than the resource delivers. The check is to verify every field against the page: the author from the byline, the license from the license statement, and the grade level against the readability evidence. For *Watershed Basics*, only title and author were present. The fix fills the other four fields and adds keywords.

| Field | Before | After (drafted by the agent and verified) |
|---|---|---|
| Title | Watershed Basics | Watershed Basics |
| Author | Maria Lopez | Maria Lopez |
| Subject | None | Earth science |
| Grade level | None | Grades 6 and 7 |
| License | None in the file properties | CC BY 4.0, with a link to the license |
| Description | None | A short reading and quiz that explain what a watershed is. |
| Keywords | None | watershed, river, runoff, groundwater |

All six core fields are now present, and Metadata rises from 4 to 8. It does not reach 10, because the record has no machine-readable markup.

### License Statement Repair

**License statement repair** is the completion of missing or partial license statements. It adds the license to every page or component and to the file properties, and it adds a credit line for each third-party item in the title, author, source, and license form of Chapter 2. An agent can draft the lines from information you provide.

The mistake to expect is an agent that fills a gap by assigning a license to something it does not own. An agent must never choose a license for someone else's work or guess the owner's terms. If the terms of a third-party item cannot be found, replace the item. For *Watershed Basics*, one of the three third-party images has no notice. The repair finds its source and records the notice, or replaces the image if the source cannot be found.

### Chapter Splitting

**Chapter splitting** is the division of a long page or file into modules that each cover one idea or objective and stand alone. Chapter 9 gave the checks: each module has its own address, its own title, its own license, and its own metadata, and it makes no reference to "the section above". An agent can propose the split points, copy the license and metadata into each module, and rewrite cross-references so that they work.

The mistake to expect is a module that still depends on another, such as a quiz that says "use the diagram from the reading". The check is to open each module alone and read it as a stranger would. For *Watershed Basics*, the quiz is inseparable from the reading. The split makes two modules, each with its own address and metadata, and changes the quiz script's relative path to a complete address so that the quiz can be embedded alone. Modularity rises from 5 to 8.

### PDF-to-Markdown Conversion

**PDF-to-Markdown conversion** is the change of a resource from a PDF, which is hard to edit, into Markdown, which is plain text that anyone can revise. It raises the editable source metric of Chapter 4, and it helps portability. A conversion tool or an agent extracts the text and rebuilds the structure.

PDFs store where things sit on a page and not what they mean, so conversion makes predictable errors. The table lists the common ones and the check for each.

| Error | What goes wrong | The check |
|---|---|---|
| Column order | Two columns are read across the page, mixing their lines | Read a paragraph from each column in the output |
| Flattened table | A table becomes a run of separate lines | Compare each table with the original |
| Lost heading | A large heading becomes plain text | List the headings in the output |
| Garbled equation | A formula turns into scrambled symbols | Compare each formula with the original |
| Lost image | A picture is dropped, with no note | Count the pictures before and after |
| Split word | A word hyphenated at a line end stays broken | Search for stray hyphens inside words |

The poster below places each error on a picture of a converted page.

#### Diagram: PDF Conversion Error Poster

<details markdown="1">
<summary>PDF Conversion Error Poster</summary>
Type: infographic
**sim-id:** pdf-conversion-error-poster<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the six common errors of a PDF-to-Markdown conversion from a description of how each looks, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** PDF-to-Markdown Conversion (defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 5 of 6 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) A conversion that opens without an error is correct. (2) A tool converts every element equally well. (3) Only text can be lost.

**Instructional Rationale:** Identifying conversion errors is a Remember-level task, and a picture of a converted page with the errors marked gives each one a place and a look. The quiz asks the learner to recognize an error by its appearance.

**Content:**

The illustration is a text-free flat drawing of a converted page. The page has a large heading bar at the top. Below it are two columns of thin lines, with lines from the left column running into lines from the right column. Under the columns is a grid of cells whose lines have collapsed into one stack. To the right is a row of scrambled small symbols where a formula should be. Below that is an empty frame with a dashed outline where a picture should be. At the bottom is a thin line with a short hyphen inside one word. The six markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Lost heading | The large bar at the top that has shrunk to the same weight as plain lines. | A heading that has become plain text. | List the headings in the output and compare with the original. |
| 2 | Column order | The two columns whose lines run into each other. | Lines from two columns are mixed together. | Read one paragraph from each column in the output. |
| 3 | Flattened table | The grid of cells whose lines have collapsed into one stack. | A table whose rows and columns are lost. | Compare each table with the original. |
| 4 | Garbled equation | The row of scrambled small symbols. | A formula that no longer reads correctly. | Compare each formula with the original. |
| 5 | Lost image | The empty frame with a dashed outline. | A picture that is missing, with no note. | Count the pictures before and after. |
| 6 | Split word | The thin line with a short hyphen inside one word. | A word broken at a line end that stayed broken. | Search for stray hyphens inside words. |

**Provenance:** The six errors follow the chapter section "PDF-to-Markdown Conversion". The illustration is synthetic, and the sim labels the page "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 6 from the top of the page to its bottom.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 6 hints the sim shows the summary.

**Feedback:** 6 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can spot a conversion error." Below 5 it lists the labels of the missed errors.

**Starting State:** The illustration with six numbered markers, explore mode active, and the prompt "Hover a marker to see what went wrong."

**Chapter Anchors:** The chapter's table of conversion errors lists the same six errors, in a different order, with a check for each.
</details>

### Practice Question Generation

**Practice question generation** is the use of an agent to draft questions, answer keys, wrong choices, and explanations at a chosen cognitive level for a stated learning outcome. Chapter 8 taught that practice needs feedback, so the explanation matters as much as the question.

The mistakes to expect are a wrong answer key, two correct choices, a stem that gives the answer away, and questions that stay at the remember level. The check is to answer every question yourself without looking at the key, to confirm that each wrong choice is plausible and wrong, and to confirm that each explanation says why. For *Watershed Basics*, 6 of 8 quiz questions have explanations. The plan asks the agent to draft the two missing explanations, and a person to verify them.

### MicroSim Building

**MicroSim building** is the use of an agent to build a small interactive simulation from a written specification. A good specification states the learning objective, the evidence that proves learning, the complete content, the rules, and the feedback. The agent builds from it, and a person tests the result.

The mistakes to expect are wrong science, a control that does nothing, a simulation that works on one page and fails when embedded elsewhere, and a missing keyboard path. The check is to use every control, check each number against a hand calculation, tab through the page with the keyboard, and embed the simulation on each platform you care about. For *Watershed Basics*, the plan adds a short simulation, "Where does the rain go?", in which a slider changes ground cover. Its script is blocked on one of the three platforms, and the re-score below finds the cost.

### The Fixes Together

The table summarizes the thirteen fixes. Each row names the metric the fix mainly raises, the mistake to expect, and the human check.

| Fix | Mainly raises | A typical agent mistake | The human check |
|---|---|---|---|
| AI alt text generation | Accessibility | Generic text or invented details | Look at each image beside its draft |
| Caption generation | Accessibility | Mis-heard technical terms | Watch the video while reading the captions |
| Heading repair | Accessibility | Renamed or merged sections | Compare the outline before and after |
| Reading level rewrite | Readability | Lost precision or meaning | Run the readability tool and the meaning checks |
| Glossary generation | Readability | A definition that differs from the resource's use | Compare with the resource and a trusted source |
| Link repair | Accuracy and currency | An invented address | Open every new link |
| Content update | Accuracy and currency | A figure from memory | Open the source and confirm the figure |
| Metadata generation | Metadata | A guessed author or license | Verify each field against the page |
| License statement repair | Open license | A license assigned to someone else's work | Find the owner's terms or replace the item |
| Chapter splitting | Modularity | A module that still depends on another | Open each module alone |
| PDF-to-Markdown conversion | Editable source | Lost tables, headings, or pictures | Compare the output with the PDF |
| Practice question generation | Practice with feedback | A wrong key or a leading stem | Answer each question without the key |
| MicroSim building | Practice with feedback | Wrong science or a failed embed | Use every control and embed it on each platform |

The MicroSim below practices the link between fix and metric. It gives each fix, and you name the metric that it mainly raises.

#### Diagram: Fix and Metric Matcher

<details markdown="1">
<summary>Fix and Metric Matcher</summary>
Type: microsim
**sim-id:** fix-metric-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of thirteen fixes under the rubric metric it mainly raises, with at least 11 of 13 correct on the first attempt.

**Prerequisites:** All thirteen fixes of the chapter section "The Fix Toolkit", and the ten metrics of Chapter 3 (all defined in this chapter above this block or in earlier chapters).

**Evidence of Mastery:** For each fix the learner commits one of eight metrics. A placement is correct when it matches the Correct metric column in Content. Mastery is at least 11 of 13 correct on the first attempt. Reading the fix summary table is exploration, not evidence.

**Misconceptions:** (1) Every fix raises the accessibility metric. (2) One fix raises only one metric and never affects another. (3) Practice questions raise the readability metric.

**Instructional Rationale:** Classifying fixes by the metric they mainly raise is an Understand-level action that lets the learner choose a fix from a low score. Thirteen fixes spread over eight metrics teach the learner which fix belongs to which gap.

**Content:**

The eight metric bins: Accessibility, Readability, Accuracy and currency, Open license, Modularity, Metadata, Editable source, Practice with feedback.

The thirteen fixes:

| # | Fix | Correct metric | Why (shown as feedback) |
|---|---|---|---|
| 1 | AI alt text generation | Accessibility | Alt text is a WCAG text alternative. |
| 2 | Caption generation | Accessibility | Captions serve learners who cannot hear the video. |
| 3 | Heading repair | Accessibility | A clean outline serves screen reader users. |
| 4 | Reading level rewrite | Readability | It moves the text toward the audience's grade. |
| 5 | Glossary generation | Readability | It defines terms the audience may not know. |
| 6 | Link repair | Accuracy and currency | A working link is part of a current resource. |
| 7 | Content update | Accuracy and currency | It replaces an outdated fact. |
| 8 | Metadata generation | Metadata | It fills the record's descriptive fields. |
| 9 | License statement repair | Open license | It completes the license and credit statements. |
| 10 | Chapter splitting | Modularity | It makes modules that stand alone. |
| 11 | PDF-to-Markdown conversion | Editable source | It turns a locked file into one that anyone can revise. |
| 12 | Practice question generation | Practice with feedback | It adds questions with answers and explanations. |
| 13 | MicroSim building | Practice with feedback | It adds an interactive activity with feedback. |

**Provenance:** The pairs follow the chapter section "The Fix Toolkit" and the metric definitions of Chapters 4 through 10. The sim notes that a fix can affect more than one metric and that each pair shows the main metric.

**Rules:** Each fix has exactly one correct metric. Accessibility holds three fixes. Readability, Accuracy and currency, and Practice with feedback hold two each. Open license, Modularity, Metadata, and Editable source hold one each.

**Learner Activity:**

1. The learner sees one fix and the eight metric bins.
2. The learner may open the fix summary table. Opening it does not change the score.
3. The learner places the fix in a bin, and the placement is committed.
4. The sim shows whether it was correct and the Why text.
5. After fix 13 the sim shows the summary.

**Feedback:** 13 fixes in a shuffled order, one attempt each. Correct: "Correct: [metric]. [Why]". Incorrect: "Not quite. This fix mainly raises [metric]. [Why]". The summary shows "[n] of 13 correct on the first attempt". At 11 or more it adds "You can pick the fix for a low metric." Below 11 it lists the Why text of each missed fix.

**Starting State:** The first fix in the shuffled order and the eight bins. The question shown is "Which metric does this fix mainly raise?"

**Chapter Anchors:** The chapter's table of thirteen fixes names the same metric for each fix.
</details>

---

## Controlling the Changes

An agent can make dozens of changes in minutes, and that speed is the danger. A change that nobody reviews can be wrong, and a change that nobody records cannot be explained later. Two practices keep the work under control: a person reviews every change, and every change goes in a log.

### Human Review of Changes

**Human review of changes** is the step in which a named person examines each change an agent made before it is kept. Nothing goes live on the agent's say-so. The agent's own summary of what it changed is not enough, because an agent can leave a change out of its summary. Use a difference view that shows every change, and decide on each one: accept, correct, or reject, as Chapter 14 taught.

Match the depth of review to the risk. High-risk changes get a full check against the source: facts, numbers, quotations, citations, captions, license statements, and anything that touches meaning. Low-risk changes, such as heading levels and formatting, get a spot check by the sampling rule of Chapter 14.

**Worked example: reviewing 15 text changes to *Watershed Basics*.**

| Change type | Changes | Review depth | Accepted | Corrected | Rejected |
|---|---|---|---|---|---|
| Alt text | 3 | Full | 2 | 1 | 0 |
| Caption file | 1 | Full, the whole video watched | 0 | 1 | 0 |
| Heading level | 1 | Spot check | 1 | 0 | 0 |
| Metadata fields | 5 | Full | 4 | 1 | 0 |
| Link replacements | 2 | Full | 1 | 0 | 1 |
| Figure update | 1 | Full | 1 | 0 | 0 |
| Quiz explanations | 2 | Full | 1 | 1 | 0 |
| **Total** | **15** | | **10** | **4** | **1** |

Five of the 15 changes, or 33 percent, needed a correction or a rejection. That is the agent error rate of Chapter 14, and it is the best argument for the review: one change in three would have gone live with a defect.

### Change Log Entry

A **change log entry** is the record of one change to a resource. It answers seven questions: when the change was made, where in the resource, what changed, why, who or what made it, who reviewed it, and what was decided. The log serves four readers. A reuser needs it, since CC BY asks you to indicate that you changed the work. A future reviewer needs it, to know what has already been fixed. The re-score uses it, to tie each change to the check it was meant to fix. And the version history of Chapter 4 reads best when each saved version has one clear log entry.

**Worked example: three entries for *Watershed Basics*.**

| When | Where | What changed | Why | Made by | Reviewed by | Decision |
|---|---|---|---|---|---|---|
| 2026-10-24 | Section 2, paragraph 1 | "410 miles" became "398 miles", with the State Water Agency page cited | Accuracy: outdated figure | Agent, from a supplied source | Reviewer A | Accepted |
| 2026-10-24 | Image 3 | Alt text "map" became "Map showing the river and its two tributaries" | Accessibility: one-word alt text | Agent, corrected because the draft said three tributaries | Reviewer A | Corrected |
| 2026-10-24 | Link 9 | A broken address was replaced by an archived copy of the same page | Accuracy: broken link | Person, because the agent's suggested address did not exist | Reviewer A | Agent suggestion rejected |

The MicroSim below practices reading a log. It shows seven entries, each missing one of the seven answers, and you name what is missing.

#### Diagram: Change Log Gap Finder

<details markdown="1">
<summary>Change Log Gap Finder</summary>
Type: microsim
**sim-id:** change-log-gap-finder<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine seven change log entries and name the one field that is missing from each, with at least 6 of 7 correct on the first attempt.

**Prerequisites:** Change Log Entry, Human Review of Changes, Accept Correct or Reject (all defined in this chapter above this block or in Chapter 14).

**Evidence of Mastery:** For each entry the learner commits the missing field from a list of seven. A choice is correct when it matches the Missing field column in Content. Mastery is at least 6 of 7 correct on the first attempt. Reading the field list is exploration, not evidence.

**Misconceptions:** (1) A log needs only what changed. (2) Naming the reviewer is optional. (3) The reason for a change can be guessed later.

**Instructional Rationale:** Examining an entry for a missing part is an Analyze-level action. Seven entries that each lack a different field teach the learner what each field contributes.

**Content:**

The seven fields: When, Where, What changed, Why, Made by, Reviewed by, Decision.

The seven entries (all made up for Watershed Basics). A dash marks the missing field:

| # | When | Where | What changed | Why | Made by | Reviewed by | Decision | Missing field | Why it matters (shown as feedback) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | - | Section 2, paragraph 1 | "410 miles" became "398 miles" | Outdated figure | Agent | Reviewer A | Accepted | When | Without a date, no one can tell which version was scored. |
| 2 | 2026-10-24 | - | "410 miles" became "398 miles" | Outdated figure | Agent | Reviewer A | Accepted | Where | A reuser cannot find the change. |
| 3 | 2026-10-24 | Image 3 | - | One-word alt text | Agent | Reviewer A | Corrected | What changed | A reuser must be able to indicate what was changed. |
| 4 | 2026-10-24 | Link 9 | Address replaced | - | Person | Reviewer A | Accepted | Why | The change cannot be tied to the check it fixes. |
| 5 | 2026-10-24 | Heading 4 | Level 4 became level 3 | Skipped heading level | - | Reviewer A | Accepted | Made by | The log cannot show how often agents are right. |
| 6 | 2026-10-24 | Question 3 | Explanation added | No explanation | Agent | - | Accepted | Reviewed by | Nothing shows that a person checked the change. |
| 7 | 2026-10-24 | Section 3 | Sentence shortened | Reading level | Agent | Reviewer A | - | Decision | No one can tell whether the change was kept. |

**Provenance:** The entries are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The seven fields follow the chapter section "Change Log Entry".

**Rules:** Each entry lacks exactly one field, and each of the seven fields is missing from exactly one entry.

**Learner Activity:**

1. The learner sees one entry as a row with one empty cell.
2. The learner chooses which of the seven fields is missing, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After entry 7 the sim shows the summary.

**Feedback:** 7 entries in a shuffled order, one attempt each. Correct: "Correct: [field]. [Why]". Incorrect: "Not quite. The missing field is [field]. [Why]". The summary shows "[n] of 7 correct on the first attempt". At 6 or more it adds "You can read a change log." Below 6 it lists the Why text of each missed entry.

**Starting State:** The first entry in the shuffled order and the list of seven fields. The question shown is "Which field is missing?"

**Chapter Anchors:** The chapter lists seven questions that a log entry answers, and gives three complete entries for the running example.
</details>

## Measuring the Result

### Re-Scoring

**Re-scoring** is scoring the improved resource again, on all ten metrics, with the same rubric, the same evidence rules, and the same prompt and tools as the first scoring. Two choices matter most.

The first choice is to score *all ten* metrics and not only the ones you worked on. Fixes have side effects. A simulation added to raise Practice can lower Portability if its script is blocked somewhere. A split can break a link. A rewrite can drop a fact. Only a full re-score finds these, and only a full re-score gives the true total and decision.

The second choice is who scores. An agent that edited a resource tends to score it generously, and a reviewer who approved the changes is anchored on them. Use a fresh agent session with the same calibrated prompt, so that the two scorings are comparable, and have a person verify every metric whose score changed and sample the rest, as Chapter 14 taught. Changing the scoring prompt between the two scorings would make the comparison meaningless.

The steps are short:

1. Freeze the improved version and save it in the version history.
2. Run the same checks and the same scoring prompt on it.
3. Verify every changed score against its evidence, and sample the unchanged ones.
4. Record the evidence for each score in the same form as before.
5. Put the old and new scores side by side.

**Worked example: the re-score of *Watershed Basics*.**

| Metric | Before | After | Change | Evidence for the new score |
|---|---|---|---|---|
| Accuracy and currency | 7 | 9 | +2 | 14 of 14 links work, tested 2026-10-24, and the river length cites the agency page |
| Alignment | 6 | 6 | 0 | Unchanged: the quiz still maps to 2 of 3 outcomes |
| Readability | 8 | 8 | 0 | Unchanged |
| Accessibility | 5 | 8 | +3 | 5 of 5 images have descriptive alt text, the video has captions, heading order is correct, and contrast was tested |
| Practice with feedback | 6 | 8 | +2 | 8 of 8 questions have explanations, and there is a worked example and a simulation |
| Open license | 9 | 9 | 0 | Unchanged |
| Modularity | 5 | 8 | +3 | The reading and the quiz are separate modules, each with its own address |
| Metadata | 4 | 8 | +4 | All six core fields are present, plus keywords |
| Editable source | 8 | 8 | 0 | Unchanged |
| Portability | 7 | 6 | -1 | The new simulation's script is blocked on one of the three platforms |
| **Total** | **65** | **78** | **+13** | |

The decision rule of Chapter 11 gives *Adopt*, since 78 is at least 75 and the lowest metric is 6. The surprise is the last row. The simulation that raised Practice also cost a point of Portability, and no one planned for that. The plan forecast 79, and the re-score found 78 because the full re-score caught a side effect that a targeted check would have missed.

### Score Gain

**Score gain** is the difference between the total after an improvement and the total before it. A positive gain means the resource now passes more of the rubric's checks. Report three numbers: the gain in the total, the gain on each metric, and the gap between the projected gain in the plan and the actual gain. For *Watershed Basics* the total rose from 65 to 78, a gain of +13 against a projection of +14, a shortfall of 1.

Divide the gain by the human hours to see where the effort paid off. The table compares the plan with the result.

| Fix | Hours | Projected gain | Actual gain | Actual gain per hour |
|---|---|---|---|---|
| Metadata | 0.5 | +4 | +4 | 8.0 |
| Accessibility | 2.0 | +3 | +3 | 1.5 |
| Modularity | 1.5 | +3 | +3 | 2.0 |
| Practice, with the simulation | 2.5 | +2 | +1 | 0.4 |
| Accuracy | 1.0 | +2 | +2 | 2.0 |
| **Total** | **7.5** | **+14** | **+13** | **1.7** |

The Practice row shows +1 because the +2 on Practice is offset by the -1 on Portability. The whole set returned about 1.7 points per hour, and the cheapest fix, Metadata, returned 8. This is the evidence for the lowest-metric-first rule, and it is also a lesson in pricing: the simulation took the longest and returned the least.

Two warnings keep a score gain honest. First, a small change may be noise. Chapter 14 showed that an unstable metric can move a point or two from run to run, so trust the evidence about which checks changed and not the number alone. Second, a score gain is not a learning gain. It says that the resource meets more of the rubric's checks. It does not say that students learn more. Better metadata may help teachers find the resource and teach students nothing. Whether the improved version helps students is a question to settle with students, and Chapters 16 and 17 show how to design and analyze such a test.

The MicroSim below puts the numbers in your hands. It gives the before and after scores of all ten metrics, and you work out the total, the gain, and the side effect.

#### Diagram: Re-Scoring Ledger

<details markdown="1">
<summary>Re-Scoring Ledger</summary>
Type: microsim
**sim-id:** rescoring-ledger<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the total after, the score gain, the shortfall against the projection, and the gain per hour from a before and after table, and name the metric that fell and the resulting decision, with at least 5 of 6 answers correct on the first attempt.

**Prerequisites:** Re-Scoring, Score Gain, Improvement Plan, Lowest Metric First (all defined in this chapter above this block).

**Evidence of Mastery:** The learner answers six questions. An answer is correct when it matches the Correct answer column in Content. Numeric answers are correct when they match to the precision stated in the table. Mastery is at least 5 of 6 correct on the first attempt. Reading the decision rule is exploration, not evidence.

**Misconceptions:** (1) Only the metrics you worked on can change. (2) A higher total always means every metric improved. (3) The projected gain is the real gain.

**Instructional Rationale:** Calculating a gain from a table is an Apply-level action. A table in which one metric falls teaches the learner that the total can rise while a metric gets worse, and that only a full re-score shows it.

**Content:**

The decision rule, shown at all times: Adopt when the total >= 75 and every metric >= 5. Revise when the total >= 50 and the resource is not Adopt. Reject when the total < 50.

The data (made up for Watershed Basics), shown at all times:

| Metric | Before | After |
|---|---|---|
| Accuracy and currency | 7 | 9 |
| Alignment | 6 | 6 |
| Readability | 8 | 8 |
| Accessibility | 5 | 8 |
| Practice with feedback | 6 | 8 |
| Open license | 9 | 9 |
| Modularity | 5 | 8 |
| Metadata | 4 | 8 |
| Editable source | 8 | 8 |
| Portability | 7 | 6 |
| Total | 65 | 78 |

The plan projected a gain of +14 and took 7.5 hours.

The six questions:

| # | Question | Answer type | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | What is the total after the improvements? | Whole number | 78 | 9 + 6 + 8 + 8 + 8 + 9 + 8 + 8 + 8 + 6 = 78. |
| 2 | What is the score gain? | Whole number with a sign | +13 | 78 minus 65 is 13. |
| 3 | Which metric went down? | Choice among the ten metrics | Portability | It fell from 7 to 6. |
| 4 | What is the decision after the improvements? | Choice among Adopt, Revise, Reject | Adopt | The total is 78 >= 75 and the lowest metric is 6 >= 5. |
| 5 | By how many points did the actual gain fall short of the projected gain? | Whole number | 1 | The projection was +14 and the gain was +13. |
| 6 | What is the gain per hour, rounded to one decimal place? | Number | 1.7 | 13 divided by 7.5 is about 1.7. |

**Provenance:** The scores come from the chapter's re-scoring example and are labeled "illustrative examples". The decision rule follows Chapter 11 and is labeled "provisional adoption rule".

**Rules:** Total = sum of the ten scores. Gain = total after minus total before. The shortfall = projected gain minus actual gain. Gain per hour = gain divided by hours, rounded to one decimal place.

**Learner Activity:**

1. The learner sees the data table and the first question.
2. The learner enters or chooses an answer, and the answer is committed.
3. The sim shows whether it was correct and the Why text.
4. After question 6 the sim shows the summary.

**Feedback:** 6 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read a re-score." Below 5 it lists the Why text of each missed question.

**Starting State:** The data table and question 1.

**Chapter Anchors:** The chapter's re-scoring table and its score gain table use the same numbers as this sim.
</details>

## Improvement Challenge

An **improvement challenge** is a structured exercise in which you take one real resource, improve it on a stated set of metrics with the help of agents, review and log every change, re-score it, and report the gain. It is the working form of everything in this chapter. This book's capstone project is an improvement challenge on a resource from your own subject, and it asks for more than a score: it asks you to improve at least two quality and two reusability metrics, to test the change with students, and to publish the result under a CC BY license.

The challenge has eight deliverables.

| Step | What you deliver |
|---|---|
| 1. Baseline | The ten scores with evidence, the total, and the decision |
| 2. License check | The license, whether it permits a derivative work, and your obligations |
| 3. Plan | The fixes in lowest-metric-first order, with hours and projected gain |
| 4. Fixes | The changes made with agents, and the prompts used |
| 5. Review | An accept, correct, or reject decision for every change |
| 6. Change log | One entry for each change |
| 7. Re-score | All ten metrics, scored the same way as the baseline |
| 8. Report | The gain, any side effect, the hours, and the decision after |

An improvement challenge succeeds when it meets four tests. It raises at least two quality metrics and at least two reusability metrics. Every change was reviewed and logged. No metric fell without a stated reason, and the report names any that did. And the report states the decision before and after. *Watershed Basics* meets all four: it raised three quality metrics (Accessibility, Practice with feedback, and Accuracy and currency) and two reusability metrics (Modularity and Metadata). It also reports honestly that Portability fell by one point and why.

!!! mascot-encourage "A Side Effect Is a Finding, Not a Failure"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    When the re-score shows a metric that fell, you have learned something real about your fix. Write it in the report and plan the next round around it.

The first MicroSim of the challenge lets you plan under a budget. It gives eight fixes with their hours and expected gains, and you build the plan.

#### Diagram: Improvement Planner

<details markdown="1">
<summary>Improvement Planner</summary>
Type: microsim
**sim-id:** improvement-planner<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** prioritize<br/>
**Learning Objective:** The learner will prioritize eight candidate fixes for a resource under a 5.0 hour budget and commit a plan that includes the lowest-metric fix, stays within the budget, reaches the Adopt decision, and gains at least 11 points.

**Prerequisites:** Improvement Plan, Lowest Metric First, Score Gain, Re-Scoring (all defined in this chapter above this block).

**Evidence of Mastery:** The learner commits a plan. The plan is correct when it meets all four conditions in Rules. Mastery is a correct plan on the first commit. Selecting and deselecting fixes before committing is exploration, not evidence.

**Misconceptions:** (1) The plan should use the whole budget. (2) Fixes with the biggest gain per fix are always best. (3) A plan that reaches 75 is always an Adopt.

**Instructional Rationale:** Choosing among competing fixes under a budget is an Evaluate-level action. Eight fixes with different costs, and a decision rule with a floor, teach the learner to weigh gain, cost, and the floor together.

**Content:**

The baseline (made up for Watershed Basics), shown at all times:

| Metric | Score |
|---|---|
| Accuracy and currency | 7 |
| Alignment | 6 |
| Readability | 8 |
| Accessibility | 5 |
| Practice with feedback | 6 |
| Open license | 9 |
| Modularity | 5 |
| Metadata | 4 |
| Editable source | 8 |
| Portability | 7 |
| Total | 65 |

The eight fixes:

| Id | Fix | Metric raised | Gain | Hours |
|---|---|---|---|---|
| A | Metadata generation | Metadata | +4 | 0.5 |
| B | Accessibility repair | Accessibility | +3 | 2.0 |
| C | Chapter splitting | Modularity | +3 | 1.5 |
| D | Link repair and content update | Accuracy and currency | +2 | 1.0 |
| E | Explanations, a worked example, and a simulation | Practice with feedback | +2 | 2.5 |
| F | Reading level rewrite of the one section above the audience | Readability | +1 | 1.0 |
| G | A new question for the third learning outcome | Alignment | +2 | 1.5 |
| H | Source files for the images | Editable source | +1 | 2.0 |

The decision rule, shown at all times: Adopt when the total >= 75 and every metric >= 5. Revise when the total >= 50 and the resource is not Adopt. Reject when the total < 50.

The four plans that meet every condition:

| Plan | Fixes | Hours | Total after | Gain |
|---|---|---|---|---|
| 1 | A, B, C, D | 5.0 | 77 | +12 |
| 2 | A, B, C, F | 5.0 | 76 | +11 |
| 3 | A, B, D, G | 5.0 | 76 | +11 |
| 4 | A, C, D, G | 4.5 | 76 | +11 |

**Provenance:** The scores and fixes come from the chapter's running example and are labeled "illustrative examples". The sim ignores side effects, and it says so, because the chapter's re-score shows that real results can differ.

**Rules:** The budget is 5.0 hours. The gains are independent and add. A plan is correct when all four hold: it includes fix A, the lowest metric's fix; its hours are <= 5.0; its decision is Adopt; and its gain is >= 11. The sim shows the live total, hours, gain, and decision as fixes are selected. It lets the learner select fixes beyond the budget and marks such a plan over budget.

**Learner Activity:**

1. The learner sees the baseline, the eight fixes, and the budget.
2. The learner selects and deselects fixes and watches the live total, hours, gain, and decision.
3. The learner presses Commit.
4. The sim states which of the four conditions the plan meets, and shows the four plans that meet all four.

**Feedback:** One commit counts as evidence. Correct: "Your plan meets all four conditions: [total], [gain], [hours]." Incorrect: "Your plan misses: [conditions that fail]." In both cases the sim then lists the four plans. The summary shows "Correct plan on the first commit" or "Not yet". When correct it adds "You can plan under a budget."

**Starting State:** The baseline, the eight fixes unselected, the live total of 65, hours of 0.0, and the decision Revise.

**Chapter Anchors:** The chapter's plan for Watershed Basics uses fixes A through E on a larger budget of 7.5 hours. The sim shows that a smaller budget reaches Adopt with fewer fixes.
</details>

The poster below sums up the workflow of the whole chapter in six steps. Hover over a step to see its rules, then use the quiz mode to test yourself.

#### Diagram: Improvement Workflow Poster

<details markdown="1">
<summary>Improvement Workflow Poster</summary>
Type: infographic
**sim-id:** improvement-workflow-poster<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify which of the six workflow steps matches each of six descriptions, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Derivative Work, Improvement Plan, Lowest Metric First, Human Review of Changes, Change Log Entry, Re-Scoring (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the poster zone that matches each description. A click is correct when the zone's id equals the Correct zone column in Content. Mastery is at least 5 of 6 correct on the first attempt. Hovering a zone in explore mode is exploration, not evidence.

**Misconceptions:** (1) Re-scoring covers only the metrics you changed. (2) Logging can wait until the end. (3) The license check is needed only when publishing.

**Instructional Rationale:** Remembering the order and purpose of the six steps is a Remember-level task, and a poster with six panels in order lets the learner hold the whole workflow at once. The quiz asks for the step by its purpose.

**Content:**

The poster is a flat illustration of six equal panels in two rows of three, read left to right and top to bottom. Each panel shows one simple pictogram and a step number, and the printed text is limited to the six step numbers. The first panel shows an open padlock above a document. The second shows a row of bars with the shortest bar highlighted. The third shows a hand holding a wand over a document. The fourth shows a magnifying glass over two stacked pages with a check mark. The fifth shows a notebook with ruled lines. The sixth shows two sets of ten bars side by side. All other words come from the explore and quiz data. The six zones:

| Zone id | Label | Summary | Facts shown on hover or click |
|---|---|---|---|
| step-1-license | 1. Check the license | Confirm you may make and share a derivative work. | Read the license first. NoDerivatives and a missing license stop the work. Note the credit and the statement of changes that the license requires. |
| step-2-plan | 2. Plan lowest first | Write the fixes in order, with hours and projected gain. | Start with the lowest metric. Set a budget. Write the projected gain so you can compare it later. |
| step-3-fix | 3. Fix with an agent | Let the agent draft each fix. | Give the agent the context. Expect the known mistake for each fix. Keep the original meaning. |
| step-4-review | 4. Review every change | A person checks each change against the source. | Use a difference view. Accept, correct, or reject each change. Check high-risk changes in full. |
| step-5-log | 5. Log each change | Record when, where, what, why, who, reviewer, and decision. | One entry per change. The log supports the statement of changes and the re-score. |
| step-6-rescore | 6. Re-score all ten | Score the improved version the same way as the first. | Use the same prompt. Verify the changed scores. Report the gain and any metric that fell. |

The six quiz questions, in this order:

| # | Question | Correct zone | Why (shown as feedback) |
|---|---|---|---|
| 1 | Which step stops the work if the original is NoDerivatives? | step-1-license | The license decides whether a changed version may be shared. |
| 2 | Which step sets a budget and projected gain? | step-2-plan | The plan holds the hours and the forecast. |
| 3 | Which step catches a figure the agent invented? | step-4-review | A person checks each change against the source. |
| 4 | Which step finds that a new simulation lowered portability? | step-6-rescore | Only scoring all ten metrics shows a side effect. |
| 5 | Which step records who reviewed each change? | step-5-log | The log holds the reviewer and the decision. |
| 6 | Which step drafts alt text and metadata? | step-3-fix | The agent drafts the fixes. |

**Provenance:** The six steps follow the chapter sections "Improvement Plan", "Derivative Work", "The Fix Toolkit", "Human Review of Changes", "Change Log Entry", and "Re-Scoring". The illustration is synthetic, and it carries no statistics.

**Rules:** Each question has exactly one correct zone. Zones are distinct regions of the poster, so a click belongs to at most one zone. Because the poster prints only step numbers, the sim shows the zone labels on hover.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a panel and reads its summary and facts.
2. In quiz mode the sim shows question 1 above the poster.
3. The learner clicks the panel they think matches.
4. The sim shows the Why text and moves to the next question, until question 6 is done.

**Feedback:** 6 questions in the fixed order, one attempt each. Correct: "Correct: [label]. [Why]". Incorrect: "Not quite. The answer is [label]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You know the improvement workflow." Below 5 it lists the Why text of each missed question.

**Starting State:** The poster with no zone selected, explore mode active, and the prompt "Hover a panel to learn about the step."

**Chapter Anchors:** The chapter's eight deliverables of the improvement challenge include these six steps. The poster leaves out the baseline and the report, which bracket the workflow.
</details>

---

## Key Takeaways

- An **improvement plan** lists the fixes in order, with hours and the projected gain for each. **Lowest metric first** is the rule for the order, because a low metric blocks adoption and is often the cheapest to raise.
- Improving a resource creates a **derivative work**. Read the license before the first edit, and credit the author and indicate your changes. A NoDerivatives or missing license stops the work.
- **Preserving original meaning** means changing the form and not the claims. Watch for a changed quantity, a changed strength, a dropped qualifier, an added claim, and a dropped item.
- Thirteen fixes cover most gaps: AI alt text generation, caption generation, heading repair, reading level rewrite, glossary generation, link repair, content update, metadata generation, license statement repair, chapter splitting, PDF-to-Markdown conversion, practice question generation, and MicroSim building. Each has a known agent mistake and a human check.
- **Human review of changes** examines every change in a difference view and decides accept, correct, or reject, with the most care for facts, numbers, captions, and licenses.
- A **change log entry** records when, where, what, why, who made it, who reviewed it, and the decision.
- **Re-scoring** scores all ten metrics with the same rubric and prompt, because fixes have side effects. A fresh scorer and a human check keep it honest.
- **Score gain** is the new total minus the old total. Compare it with the projection, divide it by the hours, and remember that a score gain is not a learning gain.
- An **improvement challenge** raises at least two quality and two reusability metrics, reviews and logs every change, and reports the gain and any side effect.

!!! mascot-celebration "You Can Turn a Score Into a Better Resource"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now plan an improvement, check what the license allows, fix a resource with an agent, review and log each change, and prove the gain with a full re-score. The next chapters ask the harder question of whether students learn more from the improved version.
