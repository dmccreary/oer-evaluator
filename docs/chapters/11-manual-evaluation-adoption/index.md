---
title: "Manual Evaluation and Adoption Decisions"
description: "Explains how to run a manual review: the review workflow, evidence recording, calibration sessions, score reconciliation, reviewer training, and the adopt, revise, or reject decision."
generated_by: claude skill chapter-content-generator
date: "2026-10-20 20:59:33"
version: 1.11
---

# Manual Evaluation and Adoption Decisions

## Summary

Walks through scoring an OER by hand, recording evidence, calibrating and reaching consensus with other reviewers, and turning the total score into an adopt, revise, or reject decision. It brings the ten metrics together into a human review before any AI agent is used. After this chapter you can score a resource by hand, record evidence, reconcile scores with another reviewer, and reach an adopt, revise, or reject decision.

## Concepts Covered

This chapter covers the following 11 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Manual Evaluation | 198 |
| Evidence Recording | 2 |
| Reviewer Notes | 1 |
| Calibration Session | 14 |
| Consensus Scoring | 2 |
| Score Reconciliation | 1 |
| Adopt Revise or Reject | 3 |
| Adoption Decision | 2 |
| Adoption Recommendation | 1 |
| Review Workflow | 1 |
| Reviewer Training | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Foundations of Open Educational Resources](../01-foundations-of-oer/index.md)
- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)

---

!!! mascot-welcome "From Ten Scores to One Decision"
    ![Echo the Loon waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    You now know all ten metrics, so the next question is how to use them well: how to run a review, make two reviewers agree, and turn a scorecard into a decision you can defend. This chapter walks through the whole process by hand, before any AI agent enters the picture. Let's dive in and check the evidence!

Chapters 4 to 10 introduced the ten metrics one by one. This chapter puts them together into a complete review that a teacher or a small team can carry out by hand. That order is deliberate. Chapters 12 to 14 bring in AI agents to do the first pass, and you can only judge an agent's work if you know what a careful manual review looks like and have scores of your own to compare against. Sam, who has scored the open chapter on cell structure metric by metric, now follows the review through to a decision.

## Manual Evaluation

**Manual evaluation** is scoring a resource by hand, following the rubric, with a human reviewer reading the resource, running the checks, recording evidence, and assigning each score. It is the method this book teaches first, for three reasons. It builds your understanding of the metrics, because you cannot supervise a tool that applies a rubric you have never applied yourself. It produces reference scores that later chapters compare agent output against. And for a single resource that matters, it is often the right amount of effort. Its limit is time, which is why Chapters 12 to 14 explore how agents can help.

A **review workflow** is the sequence of steps from the request to review a resource to the decision about it, with who does each step and what it produces. A good workflow is short and the same every time, so that no step gets skipped. The table gives the workflow for a review by a small team. It uses pieces from earlier chapters: the review context card, the checklist, the worksheet, and the report from Chapter 3.

| Step | Who | What happens | Output |
|------|-----|--------------|--------|
| 1. Set the context | Lead reviewer | Fill in the review context card: audience, outcomes, use, constraints | Completed context card |
| 2. Check readiness | Lead reviewer | Complete the review checklist: whole resource available, audience known, license present | Checklist |
| 3. First read | Each reviewer | Read the whole resource once without scoring | Impressions, noted separately |
| 4. Score independently | Each reviewer | Score each metric on the worksheet, with evidence | Two or more worksheets |
| 5. Compare | Reviewers | Compute subtotals and totals, and find the gaps | Agreement figures |
| 6. Reconcile | Reviewers | Discuss gaps and agree on final scores | One reconciled scorecard |
| 7. Report | Lead reviewer | Write the review report with a recommendation | Review report |
| 8. Decide | The team | Make the adoption decision | Recorded decision |

Sam's review followed those eight steps. Sam and a biology colleague each scored the open chapter independently in step 4. Their scores, which Chapter 3 compared, agreed exactly on 4 of 10 metrics and differed by more than 3 points on Readability. In step 6 they sat down with the evidence, and the differences resolved once both looked at the same pages. The colleague had read only the first page and not the later sections with the undefined terms, had missed the broken links, and had not run the lift-out test or the phone test. After checking, they agreed on Sam's original scores, so the reconciled scorecard is the one from Chapter 3: a quality subtotal of 22, a reusability subtotal of 34, and a total of 56.

A long resource cannot be read closely word by word, so a reviewer samples. Read the whole resource once, then read closely the sections that tie to your outcomes, check every image and every link, and run each metric's checks on a few components. Say in the report what you sampled, as Chapter 5 recommended for fact checking, so that the next reviewer knows what the scores rest on.

Two small habits make the process smoother. **Evidence recording** is writing down each piece of evidence as you find it, in the where, what, and how-checked form from Chapter 3, instead of reconstructing it from memory afterward. Recording as you go is faster in total, and it prevents the common problem of a score you can no longer justify. Because a web page can change after you have reviewed it, it also helps to save a dated copy of what you reviewed, using the Retain permission from Chapter 1.

**Reviewer notes** are the observations that do not belong in the evidence for a score: questions, ideas for improvement, and context that might help the next person. A note might say, "The video looks like it was made for college students; check whether there is a simpler one," or "Ask the author whether the image sources exist." Keep notes separate from evidence, so that the scores rest only on checkable facts, and date them. Good notes often turn into the improvement list in the review report.

!!! mascot-thinking "Manual First, So You Know What the Machine Should Say"
    ![Echo the Loon thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    When you've scored a resource yourself, you have a reference point. Later, when an AI agent gives its scores, you can compare them with yours and see where it's right and where it's overconfident.

## Calibrating and Reconciling

If two reviewers read the same descriptor differently, their scores will drift apart no matter how careful each is. A **calibration session** is a meeting in which reviewers each score the same sample resource on their own, compare their scores, and discuss the differences until they share an understanding of what the descriptors mean. It is the best single way to raise agreement, and it takes about an hour. The workshop schedule in this book gives it a full hour for that reason, and the [Sample One-Day Workshop Schedule](../../workshops/sample-one-day-schedule.md) shows where it fits in the day.

Here is how a calibration session goes. Sam and two colleagues each score the college-level chapter from Chapter 3 on three of the metrics, and then they compare. The table shows a first-round result and what the discussion produced.

| Metric | Reviewer 1 | Reviewer 2 | Reviewer 3 | Spread | After discussion |
|--------|------------|------------|------------|--------|------------------|
| Accuracy and Currency | 9 | 9 | 8 | 1 | No change; all found no errors in their samples |
| Readability | 5 | 8 | 9 | 4 | Agreed the chapter's reading level is above the audience's, and that the descriptor depends on the audience, not on the text alone |
| Practice with Feedback | 4 | 4 | 5 | 1 | No change; one reviewer had missed the answer key |

The big gap is on Readability, and the discussion turns up the cause. Reviewer 1 scored the chapter against the ninth-grade audience on the context card. The others scored it as a text for any reader. Once all three work from the same context card, their scores converge. Calibration also exposes descriptors that need rewording. When three careful reviewers disagree, the descriptor is probably ambiguous, and fixing it helps every later review.

!!! mascot-tip "Calibrate on a Borderline Resource"
    ![Echo the Loon giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Choose a sample that's neither excellent nor terrible, because very good and very bad resources get similar scores from everyone. A middling one is where reviewers' readings of the descriptors really differ.


**Consensus scoring** is a method in which reviewers agree on a single final score for each metric by discussing the evidence, instead of averaging separate scores. The aim is a score that every reviewer can defend with evidence. **Score reconciliation** is the step that resolves differences between independent scores. Differences of a point or two are normal and need only a short note. A difference of more than 3 points on a metric means the reviewers are probably looking at different evidence, so each shows what they found and they agree on a score together. If they still cannot agree, a third reviewer examines the evidence and decides. Record the independent scores, the final score, and the reason, so that anyone can see how it was reached.

!!! mascot-warning "Don't Settle by Splitting the Difference"
    ![Echo the Loon warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Averaging a 5 and a 9 gives a 7 that neither reviewer believes, and it hides the disagreement. Look at the evidence together, and agree on a score one of you can defend, or bring in a third reviewer.

**Reviewer training** is the preparation that gets a person ready to score reliably. It has four parts: reading the rubric and its descriptors, practicing on sample resources whose scores are already known, comparing one's scores with those references and discussing the gaps, and learning about the common biases from Chapter 3. A calibration session is the core of the training. Refresher sessions help when the rubric changes or when new reviewers join. The certificate program described in Chapter 19 builds on the same training.

## From Scores to a Decision

A scorecard is not yet a decision. **Adopt, revise, or reject** is the three-way choice that a review leads to. To adopt means to use the resource as it stands. To revise means to adapt it before use, and to reject means to choose another resource. The score band from Chapter 3 gives a starting point, but two reusability scores decide whether revising is practical. An open license is needed to adapt a resource legally, and an editable source is needed to adapt it in practice. A weak but open and editable resource can be improved. A strong but locked one cannot.

The rules below are illustrative, and your team may set its own. Apply them in order.

1. If the Open License score is 2 or lower, reject: the resource is not open enough to adapt or share.
2. Otherwise, if the total is 80 or higher, adopt.
3. Otherwise, if the total is 40 or higher and the Editable Source score is 5 or higher, revise.
4. Otherwise, reject.

Sam's chapter scored a total of 56, with an Open License score of 10 and an Editable Source score of 8. The first rule does not apply, the total is below 80, and the third rule fits, so the decision is revise. The table walks through the three outcomes with the four resources from Chapter 3's calculator.

| Resource | Total | Open License | Editable Source | Decision | Reason |
|----------|-------|--------------|-----------------|----------|--------|
| Sam's open chapter | 56 | 10 | 8 | Revise | Open and editable, with scope to improve |
| A polished publisher PDF | 50 | 1 | 1 | Reject | Not open, so it cannot be adapted |
| An openly licensed worksheet set | 67 | 10 | 9 | Revise | Open and editable, with improvements needed |
| A strong open textbook | 84 | 10 | 9 | Adopt | Meets the adopt band |

An **adoption decision** is the recorded choice about a resource, made by the people responsible for the course. The reviewer advises, and the team decides. A good record has four parts: the decision, the reasons, taken from the evidence, any conditions that must be met before use, and a date to review the decision again, since resources and courses change. For Sam, the record says: revise; reasons, two factual errors, no practice answers, and missing alt text; conditions, fix the errors and add alt text and answers before students use it; review again next June.

An **adoption recommendation** is the reviewer's written advice about what the team should decide, placed at the top of the review report so that a busy reader meets it first. It gives the recommended decision, the two or three reasons that matter most, and the conditions. Sam's recommendation reads: "Recommend revising before adoption. The chapter is open and editable, but two factual errors, missing alt text, and the absence of practice answers must be fixed first. Estimated improvement: from 56 to the 70s with these fixes." Ending with the next action, here an improvement plan, turns a review into work that can start.

Practice applying the rules on six scorecards in the exercise below.

#### Diagram: Adoption Decision Practice

<details markdown="1">
<summary>Adoption Decision Practice</summary>
Type: microsim
**sim-id:** adoption-decision-practice<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Template:** https://github.com/dmccreary/search-microsims/tree/main/docs/sims/rubric-scorer<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** recommend<br/>
**Learning Objective:** The learner will recommend adopt, revise, or reject for each of 6 resources by applying the four decision rules to its total score, Open License score, and Editable Source score.

**Prerequisites:** total score, score band, adoption threshold, Adopt revise or reject, adoption decision (all defined in the chapter section "From Scores to a Decision" above this block).

**Evidence of Mastery:** For each of the 6 resources, the learner chooses Adopt, Revise, or Reject and presses Check. A recommendation is correct when it matches the Correct decision column in Content. Mastery is 5 or more of 6 correct on the first attempt. Reading the scores and changing a choice before pressing Check is exploration and does not count as evidence.

**Misconceptions:** (1) A high quality score alone justifies adopting a resource. (2) A total in the revise range always means the resource can be revised. (3) A locked resource can be revised if its quality is good. (4) Any total below 80 means reject.

**Instructional Rationale:** Recommending means choosing a course of action and justifying it against criteria. Scorecards chosen so that each rule decides at least one outcome force the learner to apply the rules in order instead of looking only at the total.

**Content:**

The decision rules, applied in order, are shown at all times: (1) if the Open License score is <= 2, Reject; (2) otherwise, if the total is >= 80, Adopt; (3) otherwise, if the total is >= 40 and the Editable Source score is >= 5, Revise; (4) otherwise, Reject. Every metric score is a whole number from 0 to 10.

| # | Resource shown | Quality subtotal | Reusability subtotal | Total | Open License | Editable Source | Correct decision | Why (shown as feedback) |
|---|----------------|------------------|----------------------|-------|--------------|-----------------|------------------|-------------------------|
| 1 | Sam's open chapter | 22 | 34 | 56 | 10 | 8 | Revise | Rule 1 does not apply, 56 is below 80, and 56 >= 40 with Editable Source 8 >= 5. |
| 2 | A polished publisher PDF | 39 | 11 | 50 | 1 | 1 | Reject | Rule 1 applies: Open License 1 is <= 2, so it cannot be adapted. |
| 3 | An openly licensed worksheet set | 25 | 42 | 67 | 10 | 9 | Revise | 67 is below 80, and 67 >= 40 with Editable Source 9 >= 5. |
| 4 | A strong open textbook | 41 | 43 | 84 | 10 | 9 | Adopt | Rule 1 does not apply, and 84 >= 80. |
| 5 | An open booklet distributed only as a PDF | 35 | 31 | 66 | 10 | 2 | Reject | 66 >= 40, but Editable Source 2 is below 5, so rule 3 fails and rule 4 applies. The creator could be asked for the source files. |
| 6 | A weak open resource | 12 | 25 | 37 | 10 | 6 | Reject | Rule 1 does not apply, 37 is below 80, and 37 is below 40, so rule 3 fails and rule 4 applies. |

**Provenance:** The scores for resources 1 to 4 repeat those in the chapter 3 calculator and this chapter's table. Resources 5 and 6 are illustrative and written for this chapter. All six are labeled "illustrative" in the sim. The decision rules come from the chapter section "From Scores to a Decision" and are the chapter's illustrative rules.

**Rules:** Apply the four rules in order and stop at the first that decides. Rule 1 decides Reject when the Open License score <= 2. Rule 2 decides Adopt when the total >= 80. Rule 3 decides Revise when the total >= 40 and the Editable Source score >= 5. Rule 4 decides Reject in every other case. Each resource has exactly one correct decision. Mastery is correct first attempts >= 5 of 6.

**Learner Activity:**

1. The learner reads the scores for the first resource.
2. The learner chooses Adopt, Revise, or Reject and presses Check.
3. The sim shows whether the choice is correct and shows the Why text, then moves to the next resource.
4. After resource 6, the sim shows the first-attempt score, lists any missed resource with its Why text, and offers a retry of the missed resources.

**Feedback:** Six resources, shown in the order of the table, two attempts each. Correct: "Correct: [decision]. [Why text]." Incorrect on the first attempt: "Not quite. Apply the rules in order, starting with the Open License score," followed by a hint. If the learner chose Adopt or Revise for a resource with Open License <= 2, the hint is "Rule 1 comes first: a resource that is not open cannot be adapted." If the learner chose Revise for a resource whose Editable Source score is below 5, the hint is "Check whether the source can actually be edited." If the learner chose Reject for a resource that passes rule 3, the hint is "The total is high enough and the resource is open and editable." After a second wrong choice the correct decision and Why text are revealed and the resource counts as missed. The score "Correct on first attempt: n of 6" is shown at the end, and the sim states whether mastery was reached.

**Starting State:** The first resource's three scores are shown with the four rules and no choice made. The question on screen is "Adopt, revise, or reject?"

**Chapter Anchors:** The chapter states four decision rules in order (Open License <= 2 rejects; total >= 80 adopts; total >= 40 with Editable Source >= 5 revises; otherwise reject), that Sam's chapter scored 56 with Open License 10 and Editable Source 8 and is a revise, and that the exercise has 6 resources.
</details>

## Summary

This chapter turned the rubric into a complete manual review and a decision. The key points are:

- Manual evaluation is scoring by hand, and it comes first because it builds understanding and creates reference scores for later chapters.
- A review workflow of eight steps, from setting the context to recording the decision, keeps every review the same.
- Evidence recording and reviewer notes capture findings as you go, and a dated copy of the resource protects the evidence.
- A calibration session raises agreement by having reviewers score the same sample and discuss the differences.
- Consensus scoring and score reconciliation resolve differences by looking at the evidence together, not by averaging.
- Reviewer training combines rubric study, practice on known samples, and attention to bias.
- Adopt, revise, or reject is the choice a review leads to, and the Open License and Editable Source scores decide whether revising is possible.
- An adoption decision records the choice, reasons, conditions, and a review date, and an adoption recommendation puts the advice at the top of the report.

!!! mascot-celebration "You Can Run a Review From Start to Finish"
    ![Echo the Loon celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now run an eight-step manual review, calibrate with a colleague, reconcile scores with evidence, and turn a scorecard into an adopt, revise, or reject decision you can defend. Chapter 12 introduces AI agents and shows how a rubric prompt can make one do a first pass.
