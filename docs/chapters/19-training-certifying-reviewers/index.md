---
title: "Training Teachers and Certifying Reviewers"
description: "Describes how to run a teacher training workshop, set certificate requirements, review submissions, train local reviewers, and finish with a capstone project that improves a real OER."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 23:15:44"
version: 1.11
status: built
---

# Training Teachers and Certifying Reviewers

## Summary

Describes how to run a teacher training workshop, set certificate requirements, review submissions, train local reviewers, and finish with a capstone project that improves a real OER. It is the capstone chapter and draws on nearly every earlier chapter. After this chapter you can run a teacher training workshop, set certificate requirements, review submissions, and complete a capstone that improves a real OER.

## Concepts Covered

This chapter covers the following 16 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Teacher Training Workshop | 20 |
| Workshop Agenda | 5 |
| Facilitator Guide | 3 |
| Calibration Exercise | 4 |
| Peer Review | 1 |
| Certificate | 6 |
| Certificate Requirements | 3 |
| Certificate Submission | 2 |
| Submission Review | 1 |
| Exit Survey | 2 |
| Training Evaluation | 1 |
| Local Reviewer Role | 2 |
| Train-the-Trainer | 1 |
| Training Kit | 1 |
| Capstone Project | 1 |
| Professional Development | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)
- [Chapter 11: Manual Evaluation and Adoption Decisions](../11-manual-evaluation-adoption/index.md)
- [Chapter 12: AI Agents, Prompts, and Rubric Scoring](../12-ai-agents-prompts-scoring/index.md)
- [Chapter 14: Checking and Calibrating AI Agent Output](../14-checking-agent-output/index.md)
- [Chapter 15: Improving a Resource with AI Agents](../15-improving-resources-with-ai/index.md)
- [Chapter 16: Designing an A/B Test with Students](../16-ab-testing-design/index.md)
- [Chapter 17: Analyzing A/B Test Results](../17-ab-testing-analysis/index.md)
- [Chapter 18: Reusable Components and Publishing OER](../18-components-publishing-oer/index.md)

---

!!! mascot-welcome "From Learner to Teacher of Others"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    You can now evaluate a resource, check an agent, improve the resource, test the change, and publish it. This last chapter is about passing those skills to colleagues and recognizing the people who have them. Let's dive in and check the evidence!

A skill that only one teacher has helps one classroom. This chapter is about spreading it: running a workshop that teaches colleagues to evaluate and improve open educational resources with AI agents, setting a fair standard for a certificate, reviewing what people submit, and growing a group of local reviewers who keep the work going. It closes with the capstone project, which uses every skill in the book on a resource of your own.

The chapter builds on the sample materials in the book's [workshop section](../../workshops/index.md): the [Sample One-Day Workshop Schedule](../../workshops/sample-one-day-schedule.md), the [Sample Rubric Worksheet](../../workshops/sample-rubric-worksheet.md), and the [Grant-Period Timeline](../../workshops/grant-period-timeline.md). The chapter explains the reasons behind them.

## Teacher Training Workshop

A **teacher training workshop** is a planned session in which teachers learn a skill by practicing it on their own material. This book's workshop teaches teachers to evaluate OER for quality and reusability with AI agents and then to use the agents to improve one resource they already teach with. It is designed for about 20 teachers and fits in one day. Teachers arrive with a resource from their own subject, a laptop, and access to an agent tool, and they leave with an improved, openly licensed component and a checklist for earning a certificate.

Preparation decides much of the outcome. Before the day, each teacher chooses a resource they already use, checks that its license allows an improved version, and tests the agent tool. The facilitator prepares a sample resource with consensus scores, tests the prompts, and seats teachers in pairs, since pairs can compare scores and swap work. By the end of the day a teacher should be able to do four things: score a resource on all ten metrics with an agent, find an invented citation or a misread license in an agent's report, raise a metric with an agent and re-score it, and say what a reviewer needs to see to certify the work.

Three ideas shape the design. Teachers learn by doing, so most of the day is practice on a real resource and not lecture. The order of the skills follows the order of the book: score a resource, check the agent, improve the resource, then review each other's work. And the day ends with something real, a published component, because a workshop that ends with notes is forgotten faster than one that ends with a finished product.

### Workshop Agenda

A **workshop agenda** is the schedule of a workshop: each session, its length, and what participants take away. A good agenda puts the sessions in an order where each one prepares the next. The sample one-day agenda runs from 8:30 a.m. to 3:30 p.m.

| Time | Session | What teachers leave with |
|---|---|---|
| 8:30 to 9:00 | Check-in and setup | A working agent session |
| 9:00 to 9:45 | Why quality and reusability matter: the 10 metrics | A rubric card |
| 9:45 to 10:45 | Calibration: score a sample by hand, then with the agent | Hand and agent scores, with gaps explained |
| 10:45 to 11:00 | Break | |
| 11:00 to 12:00 | Checking the agent: invented citations, misread licenses, overconfident scores | A verified evaluation of the sample |
| 12:00 to 12:45 | Lunch | |
| 12:45 to 2:15 | Improvement challenge: raise one component's score with agents | An improved component and its new score |
| 2:15 to 2:30 | Break | |
| 2:30 to 3:15 | Peer review and publishing | A published, openly licensed component |
| 3:15 to 3:30 | Next steps: certificate requirements and the exit survey | A certificate checklist |

The order matters. Setup comes first because nothing works without a running agent. The rubric comes before calibration, because teachers cannot score what they have not learned. Calibration comes before checking the agent, because you need your own scores to judge the agent's. Checking comes before improving, because Chapter 14 showed that an unchecked agent should not be trusted to change anything. Peer review and publishing come last because they need a finished component.

The MicroSim below practices the sequence. It gives seven sessions in a scrambled order, and you put them in the right one.

#### Diagram: Workshop Agenda Sorter

<details markdown="1">
<summary>Workshop Agenda Sorter</summary>
Type: microsim
**sim-id:** workshop-agenda-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the logic of the workshop agenda by placing seven sessions in the correct order and naming what each session depends on, with at least 6 of 7 sessions in the correct position on the first commit.

**Prerequisites:** Teacher Training Workshop, Workshop Agenda, and the calibration and improvement chapters (Chapters 14 and 15).

**Evidence of Mastery:** The learner arranges the seven sessions and commits the order once. A session is correct when it is in its position in the Content table. Mastery is at least 6 of 7 sessions in the correct position on the first commit. Rearranging before the commit is exploration, not evidence.

**Misconceptions:** (1) The order of sessions is a matter of taste. (2) Improving a resource can come before checking the agent. (3) Peer review can come before the improvement.

**Instructional Rationale:** Ordering sessions by what each one needs is an Apply-level action that tests why the sequence works. Each session depends on a product of an earlier one, so a wrong order shows a missing prerequisite.

**Content:**

The seven sessions in their correct order:

| Position | Session | Depends on (shown as feedback) |
|---|---|---|
| 1 | Check-in and setup | Nothing, and it gives every teacher a working agent session. |
| 2 | Why quality and reusability matter: the 10 metrics | The agent session is ready, and the metrics are needed to score. |
| 3 | Calibration | The metrics, to score a sample by hand and with the agent. |
| 4 | Checking the agent | The hand and agent scores from calibration. |
| 5 | Improvement challenge | A verified evaluation, so the agent's output can be trusted. |
| 6 | Peer review and publishing | A finished component to swap and re-score. |
| 7 | Next steps: certificate requirements and the exit survey | Everything that came before. |

**Provenance:** The order follows the sample one-day schedule in the book's workshop section. The sim leaves out the breaks and lunch, and says so.

**Rules:** The sim presents the seven sessions in a shuffled order. Each position has exactly one correct session.

**Learner Activity:**

1. The learner sees the seven sessions in a scrambled order.
2. The learner drags the sessions into the order they think is right, and may rearrange them freely.
3. The learner presses Commit.
4. The sim marks each session correct or misplaced, and shows what each misplaced session depends on.

**Feedback:** One commit counts as evidence. The sim shows "[n] of 7 sessions in the correct position". At 6 or more it adds "You can plan a workshop day." Below 6 it lists the correct order with the dependency of each misplaced session.

**Starting State:** The seven sessions in a shuffled order and the Commit button.

**Chapter Anchors:** The chapter's agenda table and its explanation of why the order matters are the basis of this sim.
</details>

### Facilitator Guide

A **facilitator guide** is the document that tells the person running a workshop exactly what to do in each session. A facilitator who wrote the workshop can run it from memory. A colleague who did not write it needs a guide. For each session the guide gives the time, the goal, the materials, the steps, the key points to say, the questions to ask, the common problems, and the answers to any exercise.

The most useful part of a guide is the list of common problems with their fixes, because that is where an unprepared facilitator loses time. The MicroSim below practices handling them. It describes six problems from a workshop day, and for each one you choose the best response.

#### Diagram: Workshop Problem Solver

<details markdown="1">
<summary>Workshop Problem Solver</summary>
Type: microsim
**sim-id:** workshop-problem-solver<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** recommend<br/>
**Learning Objective:** The learner will recommend the best response to each of six problems that arise during a workshop day, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Facilitator Guide, Workshop Agenda, Teacher Training Workshop (all defined in this chapter above this block), and the privacy and licensing chapters (Chapters 2 and 13).

**Evidence of Mastery:** For each problem the learner chooses one of three responses. A choice is correct when it matches the Best response column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the guide excerpt is exploration, not evidence.

**Misconceptions:** (1) The schedule must be kept at any cost. (2) A real resource from a teacher can be pasted into any tool. (3) A participant's licensing question can wait until after the workshop.

**Instructional Rationale:** Recommending a response to a live problem is an Evaluate-level action. Problems that involve time, tools, privacy, and licensing teach the learner what a facilitator guide must anticipate.

**Content:**

The six problems (all made up), each with three responses:

| # | Problem | Responses | Best response | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Three teachers cannot log in to the agent tool at 8:45. | A: Pause the whole room until all three are fixed. B: Pair each of the three with a neighbor who is logged in, and fix the logins during the first break. C: Tell them to try again at home. | B | Pairing keeps the room moving and the fix happens in parallel. |
| 2 | A teacher wants to paste a class roster with student names into the agent to score a quiz. | A: Allow it, since the teacher owns the data. B: Stop it, remind the room that student data stays out of prompts, and use the sample quiz. C: Ask the teacher to remove only the last names. | B | Student information stays out of the prompt, as Chapter 13 taught. |
| 3 | The calibration session runs 20 minutes over. | A: Cut the checking-the-agent session in half. B: Shorten the break and move one calibration comparison to a take-home task. C: Skip lunch. | B | It protects the sessions that depend on each other without cutting a core skill. |
| 4 | A teacher's resource turns out to have no license. | A: Improve it anyway and publish it as CC BY. B: Switch that teacher to the sample resource for the improvement challenge, and have them ask the owner for permission later. C: Tell them to add a CC BY license themselves. | B | Without a license, only the owner can allow an improved version. |
| 5 | Two teachers and the agent disagree by 5 points on Accessibility. | A: Average the three scores. B: Ask each to show their evidence and decide which one the evidence supports. C: Use the agent's score because it is faster. | B | Disagreements are settled by the evidence, as Chapters 11 and 14 taught. |
| 6 | A participant says the agent's score is obviously wrong but cannot say why. | A: Ask them to find the check that the agent passed and that they believe fails, and test it. B: Agree and move on. C: Tell them the agent is usually right. | A | Turning a hunch into a specific check is how the finding gets verified. |

**Provenance:** The problems are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The responses follow Chapters 11, 13, 14, and 15.

**Rules:** Each problem has exactly one best response. The sim shuffles the order of the three responses for each problem, so that the letter shown does not give away the answer.

**Learner Activity:**

1. The learner sees one problem and its three responses.
2. The learner chooses a response, and the choice is committed.
3. The sim shows whether it was best and the Why text.
4. After problem 6 the sim shows the summary.

**Feedback:** 6 problems in a shuffled order, one attempt each. Correct: "Correct: [response]. [Why]". Incorrect: "Not quite. The best response is [response]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can handle a workshop day." Below 5 it lists the Why text of each missed problem.

**Starting State:** The first problem in the shuffled order and its three responses. The question shown is "What is the best response?"

**Chapter Anchors:** The chapter says a facilitator guide includes the common problems with their fixes.
</details>

### Calibration Exercise

A **calibration exercise** is the workshop session in which each teacher scores a sample resource by hand, runs the agent on the same resource, and compares the two sets of scores. It is the teaching version of the calibration of Chapter 14. The facilitator keeps a set of consensus scores for the sample, agreed in advance by careful reviewers. Teachers compare their own scores with the agent's and with the consensus, and the worksheet asks them to list every metric on which their score and the agent's differ by more than 3 points and to explain which score they trust.

That flagging threshold of 3 is the one from Chapter 11, which suits a conversation between a person and an agent who have both read the evidence. A facilitator who wants a closer look can also compute the measures of Chapter 14 for the whole group: the agreement rate at a threshold of 1, the mean absolute difference, and the bias.

**Worked example: one teacher and the agent on *Watershed Basics*.** The teacher scored the sample, and the agent's scores follow.

| Metric | Teacher | Agent | Difference (agent minus teacher) |
|---|---|---|---|
| Accuracy and currency | 7 | 9 | +2 |
| Alignment | 6 | 6 | 0 |
| Readability | 8 | 8 | 0 |
| Accessibility | 5 | 9 | **+4** |
| Practice with feedback | 6 | 6 | 0 |
| Open license | 9 | 10 | +1 |
| Modularity | 5 | 5 | 0 |
| Metadata | 4 | 5 | +1 |
| Editable source | 8 | 8 | 0 |
| Portability | 7 | 7 | 0 |
| **Total** | **65** | **73** | **+8** |

One metric differs by more than 3: Accessibility, where the agent gave 9 and the teacher gave 5. The teacher traces it to the evidence. The agent reported that contrast was fine but attached no tool log, and the video has no captions. The teacher trusts the 5 and writes the reason on the worksheet. The group measures also show a pattern: the agent agrees within 1 point on 8 of the 10 metrics, a rate of 80 percent, and its bias is +0.8, a mild generosity.

!!! mascot-thinking "The Gap Is the Lesson"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Do not hurry past the metrics where you and the agent disagree. Explaining one disagreement from the evidence teaches more than agreeing on nine.

The MicroSim below puts the exercise in your hands. It gives the table above, and you read it.

#### Diagram: Calibration Exercise Reviewer

<details markdown="1">
<summary>Calibration Exercise Reviewer</summary>
Type: microsim
**sim-id:** calibration-exercise-reviewer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the totals, the flagged metrics, the agreement rate, and the bias from a teacher and agent score table, and judge whether the agent meets the first-pass standard, with at least 5 of 6 answers correct on the first attempt.

**Prerequisites:** Calibration Exercise, and the agreement measures of Chapter 14 (Agreement Rate, Bias, Mean Absolute Difference).

**Evidence of Mastery:** The learner answers six questions. An answer is correct when it matches the Correct answer column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the standard is exploration, not evidence.

**Misconceptions:** (1) Only the total matters. (2) A flag means the agent is wrong. (3) An agent that agrees on most metrics can be trusted as a first pass.

**Instructional Rationale:** Calculating the comparison measures from a score table is an Apply-level action that joins the workshop exercise to the measures of Chapter 14. A table with one flagged metric and a mild bias shows that an agent can pass one test and fail another.

**Content:**

The data, shown at all times (made up, for the Watershed Basics sample):

| Metric | Teacher | Agent |
|---|---|---|
| Accuracy and currency | 7 | 9 |
| Alignment | 6 | 6 |
| Readability | 8 | 8 |
| Accessibility | 5 | 9 |
| Practice with feedback | 6 | 6 |
| Open license | 9 | 10 |
| Modularity | 5 | 5 |
| Metadata | 4 | 5 |
| Editable source | 8 | 8 |
| Portability | 7 | 7 |

The flag rule, shown at all times: flag a metric when the absolute difference is > 3. The adoption rule: Adopt when the total >= 75 and every metric >= 5; Revise when the total >= 50 and the resource is not Adopt; Reject when the total < 50. The illustrative first-pass standard: agreement rate at a threshold of 1 >= 80 percent, absolute bias <= 0.5, mean absolute difference <= 1.0, and the adoption decision matches the teacher's.

The six questions:

| # | Question | Answer type | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | What are the two totals? | Two whole numbers | 65 and 73 | The teacher's scores add to 65 and the agent's to 73. |
| 2 | Which metric is flagged by the rule > 3? | Choice among the ten metrics | Accessibility | The difference is 4. |
| 3 | What is the agreement rate at a threshold of 1? | Percent | 80 percent | Eight of ten metrics differ by 1 or less. |
| 4 | What is the bias, agent minus teacher, per metric? | Number with a sign | +0.8 | The differences add to +8, and 8 divided by 10 is 0.8. |
| 5 | What is the agent's adoption decision? | Choice among Adopt, Revise, Reject | Revise | The total 73 is < 75. |
| 6 | Does the agent meet the first-pass standard? | Yes or No | No | The bias of 0.8 is > 0.5. |

**Provenance:** The scores are illustrative examples made up for this chapter, and the sim labels them "illustrative examples". The flag rule follows the worksheet and Chapter 11, and the standard follows Chapter 14 and is labeled "illustrative standard".

**Rules:** Total = sum of the ten scores. Difference = agent minus teacher. Agreement rate = metrics with an absolute difference <= 1 divided by 10. Bias = sum of the differences divided by 10.

**Learner Activity:**

1. The learner sees the data table and the first question.
2. The learner enters or chooses an answer, and the answer is committed.
3. The sim shows whether it was correct and the Why text.
4. After question 6 the sim shows the summary.

**Feedback:** 6 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read a calibration exercise." Below 5 it lists the Why text of each missed question.

**Starting State:** The data table, the rules, and question 1.

**Chapter Anchors:** The chapter's worked example uses the same scores and the same measures.
</details>

### Peer Review

**Peer review** is the practice in which teachers examine each other's work. In the workshop, participants swap their improved components, re-score them with the same rubric, and compare the new scores with the author's. A second reviewer catches what the author is too close to see, and reading someone else's work shows the reader new ways to solve the same problem.

Peer review works only when the feedback is useful. Three rules help. Tie every comment to evidence in the resource and to a check in the rubric. Say what to do, not only what is wrong. And review the work and not the person.

The MicroSim below practices the skill. It shows eight pieces of feedback, and for each one you decide whether it is useful.

#### Diagram: Peer Feedback Judge

<details markdown="1">
<summary>Peer Feedback Judge</summary>
Type: microsim
**sim-id:** peer-feedback-judge<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight peer review comments is useful or not useful, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Peer Review, Evidence for a Score (defined in this chapter above this block or in Chapter 3).

**Evidence of Mastery:** For each comment the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the three rules is exploration, not evidence.

**Misconceptions:** (1) Praise is useful feedback. (2) A harsh comment is an honest one. (3) A comment needs no evidence if the reviewer is experienced.

**Instructional Rationale:** Judging feedback against the three rules is an Evaluate-level action that improves the comments the learner writes. Pairs of comments about the same flaw, one useful and one not, teach the learner what the difference looks like.

**Content:**

The two bins: Useful, and Not useful.

The eight comments (all made up, about an improved Watershed Basics component):

| # | Comment | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | Image 3 has the alt text "map". Describe what the map shows: the river and its two tributaries. | Useful | It cites the evidence and says what to do. |
| 2 | The accessibility is bad. | Not useful | It has no evidence and no action. |
| 3 | The quiz explanations are clear, and question 4 says why the wrong choices are wrong. | Useful | It names specific strengths that the author should keep. |
| 4 | Nice work! | Not useful | It says nothing that the author can use. |
| 5 | The license footer is missing on page 3, so check 6 of the open-license metric fails. Add the footer. | Useful | It ties the comment to a rubric check and an action. |
| 6 | Whoever wrote this clearly does not understand watersheds. | Not useful | It attacks the person and gives no evidence. |
| 7 | The reading level is grade 9 in section 3 and the audience is grade 6 to 7. Shorten the sentences there. | Useful | It cites a measurement and says what to do. |
| 8 | I would have done it differently. | Not useful | It gives no reason and no direction. |

**Provenance:** The comments are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The three rules follow the chapter section "Peer Review".

**Rules:** Each comment has exactly one correct bin, four per bin.

**Learner Activity:**

1. The learner sees one comment and the two bins.
2. The learner places the comment in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After comment 8 the sim shows the summary.

**Feedback:** 8 comments in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This comment is [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can give useful peer feedback." Below 7 it lists the Why text of each missed comment.

**Starting State:** The first comment in the shuffled order and the two bins. The question shown is "Could the author act on this?"

**Chapter Anchors:** The chapter gives three rules for peer review: tie comments to evidence, say what to do, and review the work and not the person.
</details>

## Certificate

A **certificate** is a record, issued by a program, that a person has done defined work to a defined standard. In this book it is the **Certificate of OER Quality Evaluation Using AI Agents**. Earning it shows that a teacher attended the training, calibrated against an agent, evaluated a real resource with evidence, checked the agent's output, and improved and published a component that gained on four metrics.

A certificate is only as good as the standard behind it. It is not a legal license, an accreditation by a government body, or a promise that every later evaluation by the holder will be correct. Its value comes from design. The requirements are public, so anyone can check what the certificate means. The decision rests on evidence in the submission and not on effort or attendance alone. The reviewers are calibrated against each other, so a certificate from one reviewer means what it means from another. And there is a path for a near miss, so that a teacher who falls short on one requirement can fix it and try again.

A certificate is also a record, so keep one. For each decision the program stores the date, the reviewer, the outcome, and the reasons, and it publishes the list of certified teachers only with their consent. If a teacher later disputes a decision, the record shows what the reviewer saw. If a requirement changes, the record shows which standard applied to whom.

### Certificate Requirements

The **certificate requirements** are the conditions a teacher must meet to earn the certificate. The sample worksheet sets five, and the table says what evidence shows each one.

| # | Requirement | Evidence | Checked by |
|---|---|---|---|
| 1 | Attend the full training day | The attendance record | The program |
| 2 | Complete the calibration exercise, and explain every metric where the teacher's score and the agent's differ by more than 3 points | The worksheet's calibration table | The reviewer |
| 3 | Submit an evaluation of one resource from the teacher's own subject, scored on all 10 metrics, with evidence for each score and a note on every agent finding accepted, corrected, or rejected | The worksheet and the findings log | The reviewer |
| 4 | Publish one improved component under a CC BY license, with metadata, that gains on at least two quality and two reusability metrics | The published component, its change log, and the re-score | The reviewer |
| 5 | Submit both within 30 days of the workshop | The date stamps | The program |

### Certificate Submission

A **certificate submission** is the package of evidence a teacher sends to earn the certificate. It contains the worksheet with the baseline scores and evidence, the agent's scores beside them, and the calibration explanation; the findings log; a link to the published improved component, with its metadata and license; the change log; and the re-score of all ten metrics with the gains.

The 30-day clock starts at the workshop. For a training day on February 20, 2027, the sample timeline sets the deadline at March 22, 2027. Submit early enough to leave time for a revision, since a reviewer may ask for one.

### Submission Review

A **submission review** is the examination of a certificate submission against the requirements by a reviewer who did not take part in the work. It has five steps.

1. **Check completeness.** Compare the package with the requirements list.
2. **Check the published component.** Open its address and confirm the license, the metadata, and the change log.
3. **Verify the gains.** Re-check a sample of the claimed gains, beginning with the largest, using the verification steps of Chapter 14. A claim of "alt text added" is checked by looking at the images.
4. **Read the findings log.** A log in which every agent finding was accepted, with no reasons, suggests the agent's output was not checked.
5. **Decide.** The decisions are *Certify*, *Revise and resubmit* with the specific gaps named, or *Not eligible* when a requirement cannot be met by revision, such as missing the training day.

Borderline cases go to a second reviewer. The decisions and reasons are recorded, so that the standard stays steady.

!!! mascot-tip "Start With the Biggest Claimed Gain"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    If a metric's score jumped by four points, check that one first. A large gain with thin evidence is the most likely place for a mistake.

The MicroSim below practices the review. It shows eight submissions, and for each one you decide the outcome.

#### Diagram: Certificate Submission Reviewer

<details markdown="1">
<summary>Certificate Submission Reviewer</summary>
Type: microsim
**sim-id:** certificate-submission-reviewer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight certificate submissions should be certified, revised and resubmitted, or declared not eligible, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Certificate, Certificate Requirements, Certificate Submission, Submission Review (all defined in this chapter above this block).

**Evidence of Mastery:** For each submission the learner commits one of three outcomes. An outcome is correct when it matches the Correct outcome column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the five requirements is exploration, not evidence.

**Misconceptions:** (1) Attendance and effort earn the certificate. (2) A submission with one gap is declined for good. (3) A claimed gain needs no checking.

**Instructional Rationale:** Judging a submission against the requirements is an Evaluate-level action. Submissions that meet all requirements, miss one that can be fixed, or miss one that cannot teach the learner to apply the standard evenly.

**Content:**

The three outcomes: Certify, Revise and resubmit, Not eligible.

The five requirements, available on demand: attend the full day; complete the calibration exercise and explain each flagged metric; submit an evaluation on all 10 metrics with evidence and a note on every agent finding; publish an improved component under CC BY with metadata that gains on at least two quality and two reusability metrics; submit within 30 days.

The eight submissions (all made up):

| # | Submission | Correct outcome | Why (shown as feedback) |
|---|---|---|---|
| 1 | Complete worksheet with evidence for all 10 metrics and a findings log of 5 entries (3 accepted, 1 corrected, 1 rejected). The component is published under CC BY with metadata. Gains: Accessibility +3 and Practice +2 on quality, Modularity +3 and Metadata +4 on reusability. Submitted on day 28. | Certify | It meets every requirement. |
| 2 | Gains on two quality metrics and one reusability metric. Everything else is complete. | Revise and resubmit | It needs a gain on a second reusability metric. |
| 3 | The improved component is published under CC BY-NC. Everything else is complete. | Revise and resubmit | The requirement is a CC BY license. |
| 4 | The findings log lists 6 agent findings, all marked accepted with no reasons. | Revise and resubmit | There is no sign that the agent's output was checked. |
| 5 | Evidence is missing for 4 of the 10 scores. | Revise and resubmit | Each score needs evidence. |
| 6 | The re-score claims that all five images now have alt text, and the published component shows two images with none. | Revise and resubmit | The claimed gain is not supported by the component. |
| 7 | The teacher did not attend the training day and watched a recording. | Not eligible | Attendance cannot be made up by revision. |
| 8 | Complete worksheet; the two flagged metrics are explained; gains on three quality and three reusability metrics; CC BY with metadata; submitted on day 21. | Certify | It meets every requirement. |

**Provenance:** The submissions are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The requirements follow the sample rubric worksheet in the book's workshop section.

**Rules:** Each submission has exactly one correct outcome. Two are Certify, five are Revise and resubmit, and one is Not eligible.

**Learner Activity:**

1. The learner sees one submission and the three outcomes, and may open the five requirements. Opening them does not change the score.
2. The learner chooses an outcome, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After submission 8 the sim shows the summary.

**Feedback:** 8 submissions in a shuffled order, one attempt each. Correct: "Correct: [outcome]. [Why]". Incorrect: "Not quite. The outcome is [outcome]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can review a submission fairly." Below 7 it lists the Why text of each missed submission.

**Starting State:** The first submission in the shuffled order and the three outcomes. The question shown is "What should the reviewer decide?"

**Chapter Anchors:** The chapter's table of five requirements and its five review steps are the basis of this sim.
</details>

### Exit Survey

An **exit survey** is a short survey given at the end of a workshop, while the experience is fresh. It has two jobs: to learn how participants experienced the day, and to take a quick reading of what they feel able to do. Keep it to a few minutes. Apply the rules of Chapter 17: neutral wording, one idea per question, a rating scale, one open question, and anonymity so people answer honestly.

| Item | Type |
|---|---|
| The day gave me skills I can use with my own resources. | Rating from 1 to 5 |
| I am confident that I can score a resource with an agent. | Rating from 1 to 5 |
| I am confident that I can check an agent's output. | Rating from 1 to 5 |
| Which session was the most useful? | Choice from the agenda |
| What should change for the next workshop? | Open answer |

### Training Evaluation

A **training evaluation** is the assessment of whether a training worked. The widely used model of Donald Kirkpatrick asks four questions: how participants *reacted*, what they *learned*, whether their *behavior* changed afterward, and what *results* followed. The exit survey measures only the first. Judging a program needs evidence at every level, and the later levels take more time to collect.

| Level | The question | Illustrative evidence for a workshop of 20 teachers |
|---|---|---|
| Reaction | Did participants find the day useful? | 19 of 20 returned the exit survey, and 18 rated the day 4 or 5 |
| Learning | Did they gain the skills? | 17 of 20 earned the certificate, and their calibration scores differed from the consensus by 1.1 points on average |
| Behavior | Do they use the skills afterward? | 12 of the 17 certified teachers scored another resource within three months |
| Results | Did it change outcomes? | 20 improved components were published, and 9 were reused by another teacher within three months |

These numbers are made up to show the form. Real evaluation faces the cautions of Chapters 16 and 17: without a comparison group a change may have other causes, and counts of reuse are weaker than evidence of learning.

The MicroSim below practices placing evidence at the right level.

#### Diagram: Training Evaluation Matcher

<details markdown="1">
<summary>Training Evaluation Matcher</summary>
Type: microsim
**sim-id:** training-evaluation-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of eight pieces of evidence under Reaction, Learning, Behavior, or Results, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Exit Survey, Training Evaluation (both defined in this chapter above this block).

**Evidence of Mastery:** For each item the learner commits one of four levels. A placement is correct when it matches the Correct level column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the four levels is exploration, not evidence.

**Misconceptions:** (1) An exit survey shows that the training worked. (2) A certificate count shows changed behavior. (3) Reuse by others is a measure of satisfaction.

**Instructional Rationale:** Classifying evidence by level is an Understand-level action that shows how far each piece of evidence reaches. Two items per level teach the learner to see what an exit survey cannot show.

**Content:**

The four levels and their meanings: Reaction (how participants felt about the training), Learning (what they learned), Behavior (what they do differently afterward), Results (what changed because of it).

The eight items (all made up):

| # | Evidence | Correct level | Why (shown as feedback) |
|---|---|---|---|
| 1 | 18 of 19 respondents rated the day 4 or 5. | Reaction | It records how participants felt. |
| 2 | Participants wrote that the pace was too fast. | Reaction | It is an opinion about the training. |
| 3 | Teachers' calibration scores differed from the consensus by 1.1 points on average. | Learning | It measures a skill gained. |
| 4 | 17 of 20 teachers earned the certificate. | Learning | It shows the skills were demonstrated. |
| 5 | 12 of 17 certified teachers scored another resource within three months. | Behavior | It shows use of the skill afterward. |
| 6 | Teachers kept a findings log on their own reviews. | Behavior | It shows a practice carried over. |
| 7 | 20 improved components were published. | Results | They are products of the training. |
| 8 | 9 components were reused by another teacher within three months. | Results | Reuse is an outcome beyond the participants. |

**Provenance:** The items are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The four levels follow the model of Donald Kirkpatrick, as described in the chapter section "Training Evaluation".

**Rules:** Each item has exactly one correct level, two per level.

**Learner Activity:**

1. The learner sees one item and the four levels.
2. The learner places the item under a level, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After item 8 the sim shows the summary.

**Feedback:** 8 items in a shuffled order, one attempt each. Correct: "Correct: [level]. [Why]". Incorrect: "Not quite. This is [level]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can place evidence at the right level." Below 7 it lists the Why text of each missed item.

**Starting State:** The first item in the shuffled order and the four levels. The question shown is "What does this evidence show?"

**Chapter Anchors:** The chapter's table of four levels gives two examples of evidence for each level.
</details>

## Local Reviewer Role

A **local reviewer role** is a position, held by a trained and certified teacher, in which they act as the first reviewer of resources for their school or district. Colleagues bring a resource, and the local reviewer scores it with the rubric and an agent, verifies the agent's claims, keeps a findings log, and tells the colleague which metric to fix first.

The role has limits. A local reviewer reads a license statement and flags problems, and does not rule on what is legally safe: that is a question for the school's counsel or privacy officer. A local reviewer never sends student information to an agent. A local reviewer advises on an adoption, and the decision goes through the school's own process. And a local reviewer does not certify other teachers, which belongs to the program's reviewers. To stay accurate, a local reviewer repeats a calibration exercise on a reference set at least once a year and compares the result with the first-pass standard of Chapter 14.

The MicroSim below practices the boundary of the role.

#### Diagram: Local Reviewer Scope Sorter

<details markdown="1">
<summary>Local Reviewer Scope Sorter</summary>
Type: microsim
**sim-id:** local-reviewer-scope-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight tasks belongs to the local reviewer role or must be referred to someone else, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Local Reviewer Role, Certificate, Submission Review (all defined in this chapter above this block), and the privacy section of Chapter 13.

**Evidence of Mastery:** For each task the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the role description is exploration, not evidence.

**Misconceptions:** (1) A certified teacher can rule on what is legal. (2) A local reviewer approves adoptions alone. (3) Certifying others is part of the role.

**Instructional Rationale:** Judging the boundary of a role is an Evaluate-level action that protects both the reviewer and the colleagues who rely on them. Tasks that look similar to in-role tasks but fall outside teach the learner where to refer.

**Content:**

The two bins: In the role, and Refer or do not do.

The eight tasks (all made up):

| # | Task | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | Score a colleague's quiz with the rubric and an agent, and verify the agent's claims. | In the role | It is the core of the role. |
| 2 | Keep a findings log for each review. | In the role | The log is part of the method. |
| 3 | Tell a colleague which metric to fix first. | In the role | It applies the lowest-metric-first rule. |
| 4 | Decide that a resource's license is legally safe to publish. | Refer or do not do | Legal questions go to the school's counsel or privacy officer. |
| 5 | Send a class roster with student names to the agent. | Refer or do not do | Student information stays out of prompts. |
| 6 | Approve a district-wide adoption on their own. | Refer or do not do | Adoption follows the school's own process. |
| 7 | Repeat the calibration exercise on a reference set once a year. | In the role | It keeps the reviewer accurate. |
| 8 | Certify another teacher. | Refer or do not do | Certification belongs to the program's reviewers. |

**Provenance:** The tasks are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The scope follows the chapter section "Local Reviewer Role" and Chapters 11, 13, and 14.

**Rules:** Each task has exactly one correct bin, four per bin.

**Learner Activity:**

1. The learner sees one task and the two bins.
2. The learner places the task in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After task 8 the sim shows the summary.

**Feedback:** 8 tasks in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This task is [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You know where the role ends." Below 7 it lists the Why text of each missed task.

**Starting State:** The first task in the shuffled order and the two bins. The question shown is "Is this part of the local reviewer's job?"

**Chapter Anchors:** The chapter lists four limits of the role: no legal rulings, no student information in prompts, no solo adoption decisions, and no certifying of others.
</details>

### Train-the-Trainer

**Train-the-trainer** is a model in which people who have learned a skill are trained to teach it to others. It lets a program grow without relying on its original founders. A certified teacher joins as a co-facilitator at a workshop, then leads one with a more experienced facilitator watching, and then leads on their own, using the training kit and the facilitator guide.

The arithmetic is encouraging. If 17 teachers earn the certificate and each trains 10 colleagues, the next round reaches 170 teachers. The risk is that quality thins as the skill passes along. Three habits protect it: trainers use the same kit and the same reference set, a new trainer is observed on the first session, and trainers repeat the calibration exercise so that their scores stay close to the consensus.

!!! mascot-encourage "Teaching It Is the Best Way to Learn It"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If you feel unsure about leading a workshop, co-facilitate one first. Explaining the rubric to a colleague will show you exactly which parts you understand best.

### Training Kit

A **training kit** is the bundle of materials that lets someone run the workshop without the original team. It is itself an open educational resource, so it should be packaged, licensed, and published by the methods of Chapter 18: under CC BY, with metadata, a version number, and release notes.

| Item | What it is for |
|---|---|
| Agenda | The one-page schedule of the day |
| Facilitator guide | Step-by-step directions, key points, and fixes for common problems |
| Slides | Visual support for the short talks |
| Rubric worksheet | The form teachers fill in during the day |
| Sample resource with consensus scores | The material for the calibration exercise |
| Agent prompts and setup notes | The prompts of Chapter 12 and instructions for getting an agent running |
| Certificate checklist and submission template | What to submit and how it is reviewed |
| Exit survey and follow-up survey | The instruments for the training evaluation |

The poster below shows the kit as a box of eight items.

#### Diagram: Training Kit Contents

<details markdown="1">
<summary>Training Kit Contents</summary>
Type: infographic
**sim-id:** training-kit-poster<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the eight items of the training kit from a description of how each looks, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Training Kit, Facilitator Guide, Workshop Agenda, Exit Survey, Certificate Submission (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 7 of 8 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) A kit is only slides. (2) The kit needs no license. (3) The sample resource can be any resource.

**Instructional Rationale:** Identifying the items of a kit is a Remember-level task, and a picture of an open box with its contents gives each item a place. The quiz asks the learner to recognize an item by its look.

**Content:**

The illustration is a text-free flat drawing of an open box seen from above, with eight items inside. One is a sheet with a grid of eight rows and two columns. One is a thick booklet with a bookmark ribbon. One is a short stack of rectangles with a play-button shape on the top one. One is a printed form with boxes and a pencil. One is a document with a ribbon and a row of ten small squares. One is a speech bubble containing short lines and a gear. One is a clipboard with a check mark. One is a card with five stars and a blank line. The eight markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Agenda | The sheet with a grid of eight rows and two columns. | The one-page schedule of the day. | Show the time and what teachers leave with. |
| 2 | Facilitator guide | The thick booklet with a bookmark ribbon. | Step-by-step directions and fixes for common problems. | Include the answers to every exercise. |
| 3 | Slides | The short stack of rectangles with a play-button shape. | Visual support for the short talks. | Keep talks short and practice long. |
| 4 | Rubric worksheet | The printed form with boxes and a pencil. | The form teachers fill in during the day. | Use the ten metrics and the evidence column. |
| 5 | Sample resource | The document with a ribbon and a row of ten small squares. | The material for the calibration exercise, with consensus scores. | Agree the consensus scores before the day. |
| 6 | Agent prompts | The speech bubble with short lines and a gear. | The prompts and setup notes for the agent. | Test the prompts before the day. |
| 7 | Certificate checklist | The clipboard with a check mark. | What to submit and how it is reviewed. | Show the 30-day deadline. |
| 8 | Surveys | The card with five stars and a blank line. | The exit survey and the follow-up survey. | Keep them short and anonymous. |

**Provenance:** The eight items follow the chapter section "Training Kit". The illustration is synthetic, and the sim labels it "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 8 in the order of the table.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 8 hints the sim shows the summary.

**Feedback:** 8 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You know what goes in the kit." Below 7 it lists the labels of the missed items.

**Starting State:** The illustration with eight numbered markers, explore mode active, and the prompt "Hover an item to see what it is for."

**Chapter Anchors:** The chapter's table of eight kit items lists the same items.
</details>

## Capstone Project

The **capstone project** is the culminating work of the book: you evaluate one open educational resource from your own subject, use AI agents to improve it on at least two quality and two reusability metrics, test the change with students, and publish the result under a CC BY license. It uses every skill in the book on a resource that matters to you. The table maps its steps to the chapters.

| Step | What you do | Chapters |
|---|---|---|
| 1. Choose and check | Pick a resource, and confirm its license allows an improved version | 1, 2, 15 |
| 2. Evaluate | Score it on all ten metrics with evidence, using the rubric and an agent | 3 to 11 |
| 3. Check the agent | Verify its claims, log your findings, and compare with your own scores | 12 to 14 |
| 4. Improve | Plan lowest-metric-first, fix with agents, review and log every change, and re-score | 15 |
| 5. Test | Design and run an A/B test with consent and privacy, and write the results summary | 16 and 17 |
| 6. Publish | Package the components, publish under CC BY, and set up feedback and maintenance | 18 |
| 7. Share | Report what you found, and offer to train a colleague | 19 |

A capstone succeeds when it meets four tests: it improves at least two quality and two reusability metrics with evidence, it includes a test with students that follows the consent and privacy rules, it is published under CC BY with metadata, and its report states the gain, the limits of the test, and any side effect honestly.

The poster below lays the roadmap out as six panels. Hover over a panel to see what it asks of you.

#### Diagram: Capstone Roadmap

<details markdown="1">
<summary>Capstone Roadmap</summary>
Type: infographic
**sim-id:** capstone-roadmap-poster<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify which of the six capstone stages matches each of six descriptions, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Capstone Project, Improvement Challenge, A/B Test, Publishing OER, Certificate Submission (defined in this chapter above this block or in Chapters 15, 16, and 18).

**Evidence of Mastery:** In quiz mode the learner clicks the poster zone that matches each description. A click is correct when the zone's id equals the Correct zone column in Content. Mastery is at least 5 of 6 correct on the first attempt. Hovering a zone in explore mode is exploration, not evidence.

**Misconceptions:** (1) The capstone ends with the improved resource. (2) Testing with students is optional. (3) Sharing means only posting a link.

**Instructional Rationale:** Remembering the stages of the capstone and what each asks is a Remember-level task, and a poster with six panels in order lets the learner hold the whole project at once. The quiz asks for the stage by its purpose.

**Content:**

The poster is a flat illustration of six equal panels in two rows of three, read left to right and top to bottom. Each panel shows one simple pictogram and a stage number, and the printed text is limited to the six stage numbers. The first panel shows a magnifying glass over a page with ten bars. The second shows a robot head with a check mark. The third shows a wrench over a page. The fourth shows two groups of figures joined by an arrow. The fifth shows a globe with a branching line. The sixth shows a speech bubble between two figures. All other words come from the explore and quiz data. The six zones:

| Zone id | Label | Summary | Facts shown on hover or click |
|---|---|---|---|
| stage-1-evaluate | 1. Evaluate | Score your resource on all ten metrics with evidence. | Use the rubric and an agent. Record evidence for each score. Check the license first. |
| stage-2-check | 2. Check the agent | Verify the agent's claims and log your findings. | Look for invented citations, misread licenses, and overconfident scores. Accept, correct, or reject each claim. |
| stage-3-improve | 3. Improve | Raise at least two quality and two reusability metrics. | Plan lowest first. Review and log every change. Re-score all ten metrics. |
| stage-4-test | 4. Test with students | Compare the original and improved versions. | State a hypothesis. Assign by chance. Get consent and protect privacy. Report the effect size and the limits. |
| stage-5-publish | 5. Publish | Release the improved resource under CC BY. | Package the components. Include metadata. Build and deploy. Open a feedback channel. |
| stage-6-share | 6. Share | Report what you found and help others. | Write the results summary. Track reuse. Offer to train a colleague. |

The six quiz questions, in this order:

| # | Question | Correct zone | Why (shown as feedback) |
|---|---|---|---|
| 1 | Which stage asks you to compare an original and an improved version with students? | stage-4-test | The test is the stage with groups and consent. |
| 2 | Which stage checks for invented citations and misread licenses? | stage-2-check | Verifying the agent's claims is stage 2. |
| 3 | Which stage ends with the resource at a public address under CC BY? | stage-5-publish | Publishing releases the resource. |
| 4 | Which stage plans fixes lowest metric first? | stage-3-improve | The plan and the re-score belong to stage 3. |
| 5 | Which stage begins with scoring all ten metrics? | stage-1-evaluate | The baseline comes first. |
| 6 | Which stage includes offering to train a colleague? | stage-6-share | Sharing includes teaching others. |

**Provenance:** The six stages follow the chapter section "Capstone Project" and the course description's capstone. The illustration is synthetic, and it carries no statistics.

**Rules:** Each question has exactly one correct zone. Zones are distinct regions of the poster, so a click belongs to at most one zone. Because the poster prints only stage numbers, the sim shows the zone labels on hover.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a panel and reads its summary and facts.
2. In quiz mode the sim shows question 1 above the poster.
3. The learner clicks the panel they think matches.
4. The sim shows the Why text and moves to the next question, until question 6 is done.

**Feedback:** 6 questions in the fixed order, one attempt each. Correct: "Correct: [label]. [Why]". Incorrect: "Not quite. The answer is [label]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You know the road to the capstone." Below 5 it lists the Why text of each missed question.

**Starting State:** The poster with no zone selected, explore mode active, and the prompt "Hover a panel to learn about the stage."

**Chapter Anchors:** The chapter's table of seven capstone steps groups into these six stages, with the last step combining the report and the offer to train.
</details>

## Professional Development

**Professional development** is the continuing learning that teachers do to improve their practice. A workshop and a capstone project are good examples: they are hands-on, they use the teacher's own material, and they end in a product that others can use. Whether they count toward required hours or credits depends on your school or district, so ask before you promise anything.

The most useful professional development is a cycle and not an event. A teacher learns a skill, practices it on real work, applies it in class, shares the result, and helps the next teacher learn. That cycle is also the loop of this whole book. You *evaluate* a resource, *check* the agent that helped, *improve* the resource, *test* the change with students, *publish* the result, and *train* others. Each pass produces evidence that feeds the next one. The rubric-outcome correlation of Chapter 17 shows whether the rubric still predicts learning, the calibration of Chapter 14 shows whether the agent still agrees with careful people, and the reuse tracking of Chapter 18 shows whether the work travels. Each check makes the next evaluation more trustworthy.

---

## Key Takeaways

- A **teacher training workshop** teaches by practice on the teacher's own resource, and its **workshop agenda** puts each session after the one it depends on. A **facilitator guide** lets someone else run it and lists the common problems with their fixes.
- The **calibration exercise** compares a teacher's scores with the agent's and the consensus, and asks for an evidence-based explanation of every large gap. **Peer review** needs comments that cite evidence, say what to do, and review the work and not the person.
- The **certificate** is only as good as its standard. The **certificate requirements** are public and evidence-based, a **certificate submission** gathers the evidence, and a **submission review** verifies the gains, reads the findings log, and decides to certify, to ask for revision, or to find the teacher not eligible.
- An **exit survey** measures reaction. A **training evaluation** also looks for evidence of learning, behavior, and results.
- A **local reviewer role** scores resources, verifies agents, and advises colleagues, and it refers legal, privacy, adoption, and certification questions to others. **Train-the-trainer** spreads the skill while guarding quality, and a **training kit** is an open resource packaged like any other.
- The **capstone project** applies every skill in the book to one real resource. **Professional development** is a cycle of learning, practicing, applying, and sharing, and the cycle of this book makes each pass more trustworthy than the last.

!!! mascot-celebration "You Finished the Whole Loop"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now evaluate an open resource, check the agent that helped, improve the resource, test it with students, publish it, and teach others to do the same. Pick one resource you use this week, and start the loop.

[See Annotated References](./references.md)
