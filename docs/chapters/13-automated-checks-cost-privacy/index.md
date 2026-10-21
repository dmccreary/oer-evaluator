---
title: "Automated Checks, Cost, and Student Privacy"
description: "Covers automated link, accessibility, license, and readability checks, multi-agent review, keeping a human in the loop, AI cost, student data privacy, and FERPA."
generated_by: claude skill chapter-content-generator
date: "2026-10-20 21:06:32"
version: 1.11
---

# Automated Checks, Cost, and Student Privacy

## Summary

Covers multi-agent review, keeping a human in the loop, automated link, accessibility, license, and readability checks, AI cost, and protecting student data under FERPA. It extends AI-agent scoring with the automated checks teachers can run and the limits they must respect. After this chapter you can choose which checks to automate, keep a human in the loop, estimate agent cost, and protect student data.

## Concepts Covered

This chapter covers the following 9 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Multi-Agent Review | 22 |
| Human in the Loop | 160 |
| Automated Link Checker | 1 |
| Automated Accessibility Scan | 1 |
| Automated License Detection | 1 |
| Automated Readability Scan | 1 |
| AI Cost | 1 |
| Student Data Privacy | 27 |
| FERPA | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 2: Open Licenses and Attribution](../02-open-licenses-attribution/index.md)
- [Chapter 5: Accuracy and Currency](../05-accuracy-currency/index.md)
- [Chapter 6: Alignment and Readability](../06-alignment-readability/index.md)
- [Chapter 7: Accessibility](../07-accessibility/index.md)
- [Chapter 11: Manual Evaluation and Adoption Decisions](../11-manual-evaluation-adoption/index.md)
- [Chapter 12: AI Agents, Prompts, and Rubric Scoring](../12-ai-agents-prompts-scoring/index.md)

---

!!! mascot-welcome "Faster, Cheaper, and Still Accountable"
    ![Echo the Loon waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Automation can run a dozen checks in the time it takes to run one by hand, but speed raises three questions: who is checking the checker, what does it cost, and whose information is flowing through it? This chapter answers all three. Let's dive in and check the evidence!

Chapter 12 introduced AI agents and showed how to brief one with a rubric prompt. This chapter covers what a responsible team does around that agent. It starts with the automated checks that do the measuring, then asks how several agents can cross-check each other, why a person must stay in the loop, what the work costs, and how to protect student information. The last topic matters most. A review of an open resource involves no student data, but the work that follows it often does, including the student tests of Chapters 16 and 17, so privacy habits have to be in place before the data arrives.

## Automated Checks

Chapter 12 explained that an agent should call tools for anything that is a measurement. Four automated checks cover the measurements this rubric depends on most. Each automates a manual check from an earlier chapter, and each is only as good as what it can see.

An **automated link checker** is a tool that requests each web address in a resource and records whether it works. It automates the broken link check from Chapter 5, and it can run on hundreds of links in the time it takes a person to open ten. It reports which links return errors, which have moved, and which are slow. It cannot tell whether a working link still supports the claim it is attached to, so a clean report says only that the links open. Run on Sam's chapter, it finds what Sam found by hand: two of the nine references return "page not found."

An **automated accessibility scan** is a tool that tests a page against accessibility rules, such as missing alt text, low contrast, skipped headings, and unlabeled controls. It automates much of the accessibility checker work from Chapter 7. A scan of Sam's chapter flags the four diagrams with no alt text, the pale gray labels, and the jump from heading level 2 to level 4. It cannot judge whether alt text is any good, whether captions are accurate, or whether the page is usable with a keyboard alone, so a clean scan is a start and not a finish.

**Automated license detection** is a tool or script that finds the license statement in a resource and reports which license it names. It reads the footer, the repository's license file, and the metadata, and it compares them. Many tools report the license as a short standard code, such as CC-BY-4.0, drawn from a public list of license identifiers, which makes reports easy to compare. An agent can also read a statement and explain it, but a script is safer for the identification itself, because a script reads the real text and does not recall a typical one. Run on Sam's chapter, the check finds CC BY 4.0 in the footer and in the license file, and they agree. It cannot tell whether an image inside the chapter has a different license, so third-party content still needs a human check.

An **automated readability scan** is a tool that estimates a text's reading level with a readability formula, such as the Flesch-Kincaid grade level from Chapter 6. It takes seconds, and it can scan every section of a long resource and show which are hardest. Run on three passages of Sam's chapter, it reports 10.3, 10.6, and 10.7, which Sam had calculated by hand. It measures length of sentences and words only, so it cannot say whether the ideas are clear, and it can mislead on tables and lists.

The table gathers the four checks, with what each can and cannot judge. A reviewer can use it to decide which checks to automate and which findings still need a person.

| Automated check | Automates | Reports on Sam's chapter | Cannot judge |
|-----------------|-----------|--------------------------|--------------|
| Link checker | Broken link check, Chapter 5 | 2 of 9 links broken | Whether a working link supports the claim |
| Accessibility scan | Accessibility checker, Chapter 7 | 4 images without alt text, low-contrast labels, a heading-level skip | Quality of alt text, caption accuracy, keyboard use |
| License detection | License statement check, Chapter 2 | CC BY 4.0 in the footer and the license file | Licenses of material inside the resource |
| Readability scan | Readability formula, Chapter 6 | Grade levels of about 10.5 | Whether the ideas are clear |

## Multi-Agent Review

**Multi-agent review** is a review in which more than one agent takes part, each with its own task or its own view. Two patterns are common. In the first, specialist agents each handle one group of metrics, such as one for accuracy and sources, one for accessibility, and one for reusability, and a coordinating step combines their results. Each specialist gets a shorter, sharper prompt and only the tools it needs. In the second pattern, a second agent checks the first. It reads the first agent's scores and evidence and looks for scores that the evidence does not support.

Sam sets up three specialists and a coordinator. The table shows who does what.

| Agent | Task | Tools |
|-------|------|-------|
| Accuracy agent | Check claims and citations | Link checker, search |
| Accessibility agent | Check accessibility | Accessibility scan, contrast calculator |
| Reusability agent | Check license, modularity, metadata, source, portability | License detection, file access |
| Coordinator | Merge the three results into one report and flag disagreements | None |

Multi-agent review has an attraction and a trap. The attraction is that disagreement is informative. Suppose two agents review Alignment independently and one gives 6 while the other gives 4. That gap tells the team where to look, much as a gap between two human reviewers does. The trap is that agents built on the same model can share the same blind spots. If both miss the error in the ribosome statement, their agreement looks like confirmation and is not. Using different prompts, different models, or a different kind of check, such as a tool that looks up facts, makes the agreement more meaningful. Either way, more agents mean more cost, and they do not remove the need for a person.

## Keeping a Person in the Loop

**Human in the loop** is a way of designing automated work so that a person reviews, approves, or corrects the automated output at defined points. Three levels are commonly distinguished. With a human *in* the loop, a person approves each important output before anything happens. With a human *on* the loop, the system runs and a person monitors it and can step in. With a human *out* of the loop, nobody checks. This book recommends the first for anything that affects a decision, because a review's recommendation can decide what students are given to learn from.

There are three reasons for keeping a person in. The first is accountability: a person, not a program, is answerable for a decision about learners. The second is error catching, because models make mistakes that sound right, as Chapter 12 showed. The third is judgment, since fit with a particular classroom is something a teacher knows and an agent does not.

A person in the loop is only useful if the person really checks. **Automation bias** is the tendency to trust an automated answer more than it deserves, and it affects careful people too. A reviewer who sees an agent's score of 8 tends to settle near 8. Three habits reduce it. Score first, then look at the agent's scores, as the workflow in Chapter 12 does. Check the evidence before the score. And audit a sample: periodically re-check a few items the agent marked as fine, to see how often it is wrong.

The checkpoints belong at fixed places. The table shows the plan for Sam's agent-assisted review.

| Checkpoint | What the human does | Why |
|------------|---------------------|-----|
| Before the run | Fills in the context card and chooses the prompt version | The agent's judgment is only as good as the context |
| After scoring | Reviews every item the agent marked "cannot determine," and any score more than 3 points from the human's own | These are the places most likely to be wrong |
| Before the report | Reads the evidence for each metric, not just the scores | Evidence, not confidence, is what justifies a score |
| Before any change to a resource | Approves each edit | An agent that edits can introduce new errors |
| Before the decision | Makes the adopt, revise, or reject decision | The decision belongs to the team |

!!! mascot-thinking "The Loop Is the Point"
    ![Echo the Loon thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    The human step is where the quality comes from. An agent that does the reading, measuring, and drafting frees you to spend your attention on the judgments only you can make.

## What It Costs

**AI cost** is what it takes, in money and in time, to run a model or agent on a task. Hosted models usually charge by the token, with separate prices for the text sent in and the text produced, and the text produced often costs more. A rough cost for a task is the tokens in times the price per token in, plus the tokens out times the price per token out. Prices change often, and they differ from service to service, so check the current figures before budgeting.

Here is an illustrative estimate, using invented prices of $3 per million input tokens and $15 per million output tokens. Suppose one metric run on Sam's chapter sends about 10,000 tokens in, which is the chapter at about 8,000 tokens plus a prompt of about 2,000, and gets about 1,500 tokens back. The input costs 10,000 ÷ 1,000,000 × $3 = $0.03. The output costs 1,500 ÷ 1,000,000 × $15 = $0.0225. One run costs $0.0525. A full review of ten metrics, one run each, costs about $0.53 for the chapter, and nineteen chapters of similar size cost about $10.

| Item | Tokens in | Tokens out | Cost at the illustrative prices |
|------|-----------|------------|---------------------------------|
| One metric run | 10,000 | 1,500 | $0.0525 |
| Ten metrics for one chapter | 100,000 | 15,000 | $0.525 |
| Nineteen chapters of that size | 1,900,000 | 285,000 | $9.975 |

Machine cost is small next to human cost. Checking an agent's work takes a reviewer's time, which is worth more than the tokens, so a cheap agent that produces unreliable results can cost more overall than a careful manual review. Some services discount repeated input, which helps when the same chapter is sent for ten metrics, and local models run on your own computer for no per-token charge but need capable hardware.

## Protecting Student Information

**Student data privacy** is the protection of personal information about students, including names, ID numbers, grades, test scores, work that carries a name, photos, and records about health, disability, or discipline. It matters here because most AI tools run on a company's servers. Typing or pasting text into them sends that text to a third party. Some services keep what you send, some may use it to improve their products unless you change a setting or have a contract that says otherwise, and the terms differ from one service to the next. A teacher who pastes a student's essay into an unapproved tool may have disclosed the student's work without permission.

A review of an open textbook involves no student data, and it should stay that way: keep student information out of resource reviews entirely. The risk comes later, in the activities this book recommends next. A student A/B test, which Chapters 16 and 17 cover, collects scores and survey answers. Open pedagogy, from Chapter 1, publishes student work. Both need care. Four habits protect students:

- **Collect only what you need.** If you do not need names, do not collect them.
- **Remove identifiers before using any outside tool.** Replace names with codes, and strip emails, ID numbers, and details that could identify someone.
- **Use only tools your school has approved.** An approved tool is covered by an agreement about how the data is handled.
- **Know where the data goes.** Read the tool's terms on retention and training, and when you cannot tell, do not use it.

Take Sam wanting an agent to summarize the end-of-unit survey answers from students. The table shows how the data changes before it goes anywhere near a tool.

| Original | Safer version |
|----------|---------------|
| "Maria Lopez (maria.l@example.org): The video had no captions and I missed half of it." | "Student 14: The video had no captions and I missed half of it." |
| A spreadsheet with a column of student ID numbers | The ID column removed, and a row number kept |
| Results listed by class period, with five students in one period | Results combined across periods, so no small group can single anyone out |

!!! mascot-warning "Don't Paste Student Work Into a Chat Box"
    ![Echo the Loon warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A consumer chat tool isn't covered by your school's privacy agreements, and what you paste may be stored. Strip the names and identifiers first, and use only a tool your school or district has approved.

**FERPA**, the Family Educational Rights and Privacy Act of 1974, is the U.S. federal law that protects the privacy of student education records at schools that receive funds from the U.S. Department of Education. It gives parents, and students who are 18 or older or attend college, the right to inspect and request corrections to their records. It also restricts schools from disclosing personally identifiable information from those records without written consent, with several exceptions. One exception lets a school share records with a service provider that performs a function for the school and is under the school's direct control over how the data is used. For a teacher, the practical point is this: sending identifiable student information to an AI tool may count as a disclosure, so use de-identified data or an approved service, and follow your district's policy. Other rules also apply in some settings, such as laws on online services for children under 13 and state privacy laws, and rules differ outside the United States. This book explains concepts and is not legal advice.

The exercise below gives you eight pieces of information and asks what to do with each before it goes near an AI tool.

#### Diagram: Student Data Safety Sorter

<details markdown="1">
<summary>Student Data Safety Sorter</summary>
Type: microsim
**sim-id:** student-data-safety-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Template:** https://github.com/dmccreary/ai-persona-testing/tree/main/docs/sims/persona-data-privacy-flow<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of 8 pieces of information is fine to use with an AI tool, needs de-identifying first, or must not be used, assuming the tool has not been approved by the school.

**Prerequisites:** student data privacy, FERPA, human in the loop (all defined in the chapter above this block).

**Evidence of Mastery:** For each of the 8 pieces of information, the learner chooses one of three categories and presses Check. A choice is correct when it matches the Correct category column in Content. Mastery is 7 or more of 8 correct on the first attempt. Reading an item and changing a choice before pressing Check is exploration and does not count as evidence.

**Misconceptions:** (1) Removing a student's name is always enough to make information safe. (2) Anything about a student can be shared if the tool is popular. (3) Information about a resource and information about a student are handled the same way. (4) De-identifying is needed only for grades.

**Instructional Rationale:** Judging means applying criteria to a case. Items that differ in whether they identify a person, and in how sensitive they are, make the learner decide by the content of the information and not by how it is packaged.

**Content:**

The three categories are: Fine to use, De-identify first, and Do not use. The assumption throughout is that the AI tool is not covered by an agreement with the school or district. Where the school has approved a tool and permits it, some items in De-identify first may be allowed, and the sim says so in its note.

| # | Information shown to the learner | Correct category | Why (shown as feedback) |
|---|----------------------------------|------------------|-------------------------|
| 1 | The text of an open textbook chapter | Fine to use | It is public and contains no student information. |
| 2 | Your own completed rubric scorecard for an open resource | Fine to use | It describes a resource, not students. |
| 3 | A spreadsheet of end-of-unit survey answers, with each student's name and email | De-identify first | Names and emails identify the students. Replace them with codes before use. |
| 4 | A student's essay with the student's name at the top, shared to get ideas for feedback | De-identify first | The name identifies the student, and the work is part of the student's record. Remove the name and other identifying details. |
| 5 | A list of students who have disability accommodations | Do not use | It is sensitive information about individuals, and de-identifying it is not enough to make it appropriate for an unapproved tool. |
| 6 | A photo of a student's face taken during a class activity | Do not use | A face identifies the student and cannot be de-identified. |
| 7 | Survey answers with no names or codes, combined across four classes of 120 students in total | Fine to use | There is no identifying information, and the group is large enough that no student stands out. |
| 8 | An excerpt from a student's discipline record | Do not use | It is sensitive information about an individual and is protected as an education record. |

**Provenance:** The 8 pieces of information are illustrative and describe no real students. The categories follow the chapter section "Protecting Student Information." The sim labels the items "illustrative" and displays the note that it gives general guidance and not legal advice.

**Rules:** Information about a resource, with no student information, is Fine to use. Information that identifies a student but can be made non-identifying by removing names, contact details, and other identifiers is De-identify first. Information that is highly sensitive (disability, discipline, or health information) or that cannot be de-identified (a photo of a face) is Do not use. Information already stripped of identifiers and combined across a group large enough that no individual stands out is Fine to use. Each of the 8 items fits exactly one category. Mastery is correct first attempts >= 7 of 8.

**Learner Activity:**

1. The learner reads the first piece of information.
2. The learner chooses one of the three categories and presses Check.
3. The sim shows whether the choice is correct and shows the Why text, then moves to the next piece.
4. After item 8, the sim shows the first-attempt score, lists any missed item with its Why text, and offers a retry of the missed items. The sim also shows the note that the guidance is general and that the school's own policy applies.

**Feedback:** Eight items, shown in the order of the table, two attempts each. Correct: "Correct: [category]. [Why text]." Incorrect on the first attempt: "Not quite," followed by a hint. If the learner chose Fine to use for an item that identifies a student, the hint is "Ask whether anyone could tell which student this is about." If the learner chose De-identify first for a highly sensitive item, the hint is "Some information is too sensitive to share even without a name." If the learner chose Do not use for an item that can be made anonymous, the hint is "Ask whether removing the identifiers leaves something safe to use." After a second wrong choice the correct category and Why text are revealed and the item counts as missed. The score "Correct on first attempt: n of 8" is shown at the end, and the sim states whether mastery was reached.

**Starting State:** The first piece of information is shown with the three categories listed and no choice made. The question on screen is "What should you do with this before using an AI tool?"

**Chapter Anchors:** The chapter states that names, IDs, photos, and records about health, disability, or discipline count as student information, that identifiers should be removed before using an outside tool, that FERPA protects student education records, and that the sorter has 8 items.
</details>

!!! mascot-tip "Strip, Then Share"
    ![Echo the Loon giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Before any student text goes into a tool, replace names with codes and delete emails, ID numbers, and any detail that points to one child. If you can't tell whether something identifies a student, treat it as if it does.

## Summary

This chapter covered the checks, the cost, and the care that surround an AI-assisted review. The key points are:

- Automated link checking, accessibility scanning, license detection, and readability scanning measure what an agent should not guess, and each has limits a person must cover.
- Multi-agent review uses specialist agents or a second-opinion agent, and agreement is more meaningful when the agents differ in model, prompt, or method.
- Human in the loop keeps a person responsible at set checkpoints, and automation bias is countered by scoring first, checking evidence, and auditing samples.
- AI cost is mostly tokens, so it is small next to the cost of a human reviewer's time, and an unreliable cheap agent can cost more than it saves.
- Student data privacy means collecting only what you need, removing identifiers, using approved tools, and knowing where the data goes.
- FERPA protects student education records at U.S. schools that receive federal funds, and sending identifiable records to an AI tool may be a disclosure.

!!! mascot-celebration "You Can Run an Agent Responsibly"
    ![Echo the Loon celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now choose which checks to automate, set up checkpoints where a person decides, estimate what a run will cost, and keep student information out of harm's way. Chapter 14 turns to the hardest part: catching the mistakes an agent makes with confidence.
