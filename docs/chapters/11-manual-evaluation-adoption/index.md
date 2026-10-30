---
title: "Manual Evaluation and Adoption Decisions"
description: "Walks through scoring an OER by hand, recording evidence, calibrating and reaching consensus with other reviewers, and turning the total score into an adopt, revise, or reject decision."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:27:21"
version: 1.11
status: built
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

!!! mascot-welcome "Your First Full Review"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    You now know all ten metrics, and this chapter puts them to work on one resource from start to finish. By the end you will have scored it, settled any disagreement with a second reviewer, and made a decision you can defend. Let's dive in and check the evidence!

Chapters 4 through 10 taught the ten metrics one at a time. A real review does not work that way. A reviewer takes one resource, scores all ten metrics, adds them up, compares notes with someone else, and decides what to do. This chapter is about that whole process, done by hand, with no AI agent involved. Doing it by hand first is deliberate, because you cannot check an agent's work in later chapters unless you know what a correct review looks like.

## Manual Evaluation

**Manual evaluation** is the scoring of an OER by a human reviewer who applies the rubric directly: reading the resource, running the checks, choosing the ten metric scores, and recording the evidence. It is slower than letting software do it, and it is the reference against which software is measured. A manual evaluation is also where a reviewer learns what a resource is really like, since reading it carefully surfaces things that no automated check will. The product of a manual evaluation is a completed worksheet, a total, a decision, and a report.

**Worked example: the full review of Watershed Basics.** Chapters 4 through 10 each scored one metric of the CC BY reading from Chapter 3. The table collects all ten scores in one place, with the finding that mattered most for each.

| # | Metric | Score | Most important finding | Chapter |
|---|---|---|---|---|
| 1 | Accuracy and currency | 7 | The river-length figure is outdated, and 2 of 14 links are broken | 5 |
| 2 | Alignment | 6 | Outcome 3 has no activity and no quiz item | 6 |
| 3 | Readability | 8 | Grade 6.4 to 7.3 for a grade 6 to 7 audience, and "aquifer" is undefined | 6 |
| 4 | Accessibility | 5 | One image has no alt text, the video has no captions, and contrast is untested | 7 |
| 5 | Practice with feedback | 6 | No worked example, no simulation, and only recall questions | 8 |
| 6 | Open license | 9 | One third-party image carries no notice | 9 |
| 7 | Modularity | 5 | The quiz cannot be separated from the reading | 9 |
| 8 | Metadata | 4 | Only the title and author are recorded | 9 |
| 9 | Editable source | 8 | The images have no source files, and no change list is offered | 4 |
| 10 | Portability | 7 | The embed fails on one of three platforms | 10 |
| | **Quality subtotal** | **32** | | |
| | **Reusability subtotal** | **33** | | |
| | **Total** | **65** | Band: Fair | |

The total is 65 of 100, in the Fair band. The lowest score is metadata, at 4, and it falls below the floor of 5 that the adoption threshold requires. The decision rule gives **Revise**, as a later section shows. Most of the findings are cheap to fix. Filling in the metadata, adding captions, and writing alt text would each take less time than writing the resource did.

### Review Workflow

A **review workflow** is the ordered set of steps a reviewer follows from receiving a resource to delivering a decision. A fixed workflow keeps reviews comparable, and it keeps a reviewer from skipping the dull steps. Nine steps cover a manual review:

1. Save a dated copy of the resource and fill in the resource block of the worksheet.
2. Read the review checklist and gather your tools.
3. Read the whole resource once, without scoring.
4. Score one metric at a time, writing the evidence as you go.
5. Add the subtotals and the total.
6. Give the worksheet to a second reviewer, who has scored alone.
7. Compare the scores, and reconcile every metric that differs by more than 3 points.
8. Apply the adoption threshold to reach a decision.
9. Write the report and the recommendation.

The first MicroSim of the chapter tests whether you know the order. It gives you the nine steps in a scrambled sequence, and you put them in order.

#### Diagram: Review Workflow Sequencer

<details markdown="1">
<summary>Review Workflow Sequencer</summary>
Type: microsim
**sim-id:** review-workflow-sequencer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** list<br/>
**Learning Objective:** The learner will list the nine steps of a manual review in the correct order, with at least 8 of 9 steps in the correct position on the first Check.

**Prerequisites:** Manual Evaluation, Review Workflow (both defined in this chapter above this block).

**Evidence of Mastery:** The learner arranges nine steps and presses Check. A step is correct when it sits in the position given in the Content table. Mastery is at least 8 of 9 steps in the correct position on the first Check. Rearranging steps before pressing Check is exploration, not evidence.

**Misconceptions:** (1) The first reading of a resource should include scoring. (2) Reviewers should compare scores before they finish their own. (3) The decision comes before the reconciliation.

**Instructional Rationale:** Ordering the steps of a process is a Remember-level task that checks whether the learner holds the sequence. Each step depends on the one before it, so a wrong position can be explained by a dependency.

**Content:**

The nine steps, with their positions and the reason each follows its predecessor:

| Position | Step | Why it comes here |
|---|---|---|
| 1 | Save a dated copy of the resource and fill in the resource block. | The evidence must refer to a fixed version. |
| 2 | Read the review checklist and gather the tools. | The tools are needed for the checks. |
| 3 | Read the whole resource once, without scoring. | A first read gives the whole picture before any score. |
| 4 | Score one metric at a time, writing the evidence as you go. | Scoring needs the checklist, the tools, and the first read. |
| 5 | Add the subtotals and the total. | The sums need all ten scores. |
| 6 | Give the worksheet to a second reviewer who has scored alone. | Comparison needs two independent sets of scores. |
| 7 | Compare the scores and reconcile every metric that differs by more than 3 points. | Reconciliation needs the comparison. |
| 8 | Apply the adoption threshold to reach a decision. | The decision needs the reconciled scores. |
| 9 | Write the report and the recommendation. | The report records the decision and the reasons. |

**Provenance:** The steps follow the chapter section "Review Workflow". The sim states that a review with one reviewer skips steps 6 and 7.

**Rules:** Each step has exactly one correct position, and the nine positions are distinct. The learner may move steps freely before pressing Check. After a Check, steps in the correct position are marked correct and the rest are marked out of place.

**Learner Activity:**

1. The sim shows the nine steps in a shuffled order.
2. The learner moves steps up or down to put them in the order they think is correct.
3. The learner presses Check.
4. The sim shows which steps are in the correct position and, for each out-of-place step, the reason it belongs where it does.
5. The learner may rearrange and Check again.

**Feedback:** The learner may press Check as many times as they like, and only the first Check counts as evidence. After each Check the sim shows "[n] of 9 steps in the correct position". For each out-of-place step the sim shows its Why text. At 8 or more on the first Check it adds "You know the order of a review." Below 8 it reports the count and invites another try.

**Starting State:** The nine steps in a shuffled order that is not the correct order, and the prompt "Put the steps in the order a review happens."

**Chapter Anchors:** The chapter lists nine steps, starting with saving a dated copy and ending with writing the report and the recommendation. Comparison and reconciliation are steps 6 and 7.
</details>

### Evidence Recording

**Evidence recording** is the habit of writing down, for every score, the evidence that supports it, as Chapter 3 required. In a manual review it takes concrete forms: the evidence column of the worksheet, screenshots with dates, saved tool reports, and copies of the quotes and figures that decided a score. Record failures and passes alike, because a reviewer who writes down only the problems cannot show what was checked. Keep the evidence with the report, so that anyone who disputes a score can see what it rested on.

### Reviewer Notes

**Reviewer notes** are the informal jottings a reviewer makes during a review: questions, hunches, things to check later, and thoughts about what the author meant. They differ from evidence. Evidence is a checked observation that supports a score. A note is a lead that may turn into evidence once it is checked, or may turn out to be wrong. Keeping notes in their own place, apart from the evidence column, stops an unchecked hunch from posing as a finding. Many reviewers keep a short "to check" list that they clear before they finish.

## Calibration Session

A **calibration session** is a meeting in which reviewers score the same sample resources, compare their scores, and discuss the differences until they apply the rubric in the same way. Calibration is what turns a written rubric into a shared one. Two reviewers who read the same descriptor can mean different things by "adequate", and the only way to find that out is to score something together. A calibration session usually follows this plan: each reviewer scores the sample alone, the group compares scores metric by metric using the agreement rule from Chapter 3, the group discusses each flagged metric with its evidence, and the group notes how it will score similar cases in future.

**Worked example: a calibration session with two sample resources.** Four reviewers each score two sample resources alone and then meet.

| Step | What happens | Output |
|---|---|---|
| 1 | Each reviewer scores sample A alone, with evidence | Four worksheets |
| 2 | The group compares the four scores for each metric | A list of flagged metrics, where scores differ by more than 3 points |
| 3 | The group discusses each flagged metric, showing evidence | A shared reading of the check and a written note |
| 4 | Each reviewer scores sample B alone, applying the shared readings | Four more worksheets |
| 5 | The group compares again | Fewer flagged metrics, ideally two or fewer |

A reasonable goal, which a team may change, is that reviewers agree within 3 points on at least 8 of the 10 metrics before they score real resources. If they do not, the group repeats the session with a new sample.

!!! mascot-tip "Bring a Second Reviewer to the First Review"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Your first review is the one where a second pair of eyes helps most. Score alone, then compare, and the metrics where you differ show you which descriptors you read differently.

### Reviewer Training

**Reviewer training** is the preparation that new reviewers go through before they score real resources. It covers the rubric, the checks, the tools, and the habits that keep scores honest, and it ends with practice on sample resources and a calibration session. A new reviewer reads Chapters 3 through 10, scores two sample resources with evidence, and compares the results with an experienced reviewer's scores. [Chapter 19](../19-training-certifying-reviewers/index.md) shows how to run a training workshop and certify reviewers.

## Reaching Agreement

### Consensus Scoring

**Consensus scoring** is the process by which two or more reviewers agree on one final score for each metric. Each reviewer scores alone first. Then they compare, and for each metric where they differ, they discuss until they agree on a single score. The rule that makes consensus work is to decide by evidence. The final score is not an average of the two. Averaging hides a disagreement and produces a number that neither reviewer would defend. When the reviewers cannot agree, they record both scores and the reason, and the report says the metric is disputed.

### Score Reconciliation

**Score reconciliation** is the step-by-step handling of a metric where two reviewers' scores differ by more than 3 points. Three steps resolve it. First, each reviewer states the evidence behind their score. Second, the reviewers repeat the check that the evidence rests on, to see whether it holds. Third, they choose the score that the checked evidence supports, or, if the evidence is incomplete, they gather more and decide again. A score backed by specific, repeatable evidence outweighs one backed by a vague impression. A vague report of a failure still deserves a re-check, because it may point at a real problem that the other reviewer missed.

!!! mascot-warning "Do Not Split the Difference"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Averaging two scores feels fair and tells you nothing, because a 5 and a 9 average to a 7 that neither reviewer found. Compare the evidence, repeat the check, and keep the score that the evidence supports.

The second MicroSim practices reconciliation. It shows five metrics on which two reviewers disagreed, with each reviewer's score and evidence, and for each one you decide how to resolve it.

#### Diagram: Score Reconciliation Judge

<details markdown="1">
<summary>Score Reconciliation Judge</summary>
Type: microsim
**sim-id:** score-reconciliation-judge<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge how to resolve each of five disagreements between two reviewers by choosing the resolution that their evidence supports, with at least 4 of 5 correct on the first attempt.

**Prerequisites:** Consensus Scoring, Score Reconciliation, Evidence Recording, Inter-Rater Agreement (defined in Chapter 3) (all defined in this chapter or in Chapter 3 above this block).

**Evidence of Mastery:** For each case the learner commits one of four resolutions. A resolution is correct when it matches the Correct resolution column in Content. Mastery is at least 4 of 5 correct on the first attempt. Reading the three-step procedure is exploration, not evidence.

**Misconceptions:** (1) Average the two scores. (2) The more senior reviewer's score wins. (3) A tool report settles any score.

**Instructional Rationale:** Judging between two reviewers' evidence is an Evaluate-level action. Five cases in which different kinds of evidence meet teach the learner to ask which evidence is specific, which is repeatable, and which belongs to the check.

**Content:**

The four resolutions: Reviewer A's score stands, Reviewer B's score stands, Re-check and decide, Record the disagreement.

The three-step procedure, shown on request: each reviewer states their evidence; the reviewers repeat the check the evidence rests on; they choose the score the checked evidence supports.

The five cases (all made up, for Watershed Basics):

| # | Metric | Reviewer A | Reviewer B | Correct resolution | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | Accessibility | Score 5. Evidence: "4 of 5 images have alt text, and 2 of those 4 are one word. The video has no captions. One heading skips a level." | Score 9. Evidence: "An automated checker reported no errors." | Reviewer A's score stands | A's evidence is specific and repeatable. A checker cannot judge alt text quality or the absence of captions, so B's evidence does not address A's findings. |
| 2 | Portability | Score 7. Evidence: "The embed worked on 2 of 3 test platforms and failed on the third, tested 2026-10-12." | Score 3. Evidence: "It did not work in my LMS." | Re-check and decide | B's evidence names no platform, no date, and no cause, and it may point at the same failure A found or at a new one. Repeat the test on B's platform. |
| 3 | Open license | Score 3. Evidence: "I found no license." | Score 9. Evidence: "CC BY 4.0 appears in the footer of pages 1 to 6, with a link to the license." | Reviewer B's score stands | B's evidence is specific and shows that A missed the footer. |
| 4 | Modularity | Score 5. Evidence: "The quiz cannot be opened apart from the reading, and it has no address of its own." | Score 9. Evidence: "The reading is divided into sections with clear headings." | Reviewer A's score stands | Headings divide a page and do not make the parts separable, so B's evidence answers a different question. |
| 5 | Practice with feedback | Score 8. Evidence: "All 8 items give feedback after the learner clicks Show answer." | Score 4. Evidence: "The feedback appears only after the click on Show answer, so it is not immediate." | Record the disagreement | Both readings are defensible, because the rubric does not say whether click-to-reveal counts as feedback after the learner responds. Record the disagreement and ask the rubric's owner to clarify the check. |

**Provenance:** The cases are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The procedure follows the chapter section "Score Reconciliation".

**Rules:** Each case has exactly one correct resolution. Two cases are Reviewer A's score stands, one is Reviewer B's score stands, one is Re-check and decide, and one is Record the disagreement. The sim never offers averaging as a resolution, and states that averaging is not a resolution.

**Learner Activity:**

1. The learner sees the metric, both reviewers' scores, and both reviewers' evidence.
2. The learner may open the three-step procedure. Opening it does not change the score.
3. The learner chooses a resolution, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After case 5 the sim shows the summary.

**Feedback:** 5 cases in a shuffled order, one attempt each. Correct: "Correct: [resolution]. [Why]". Incorrect: "Not quite. The best resolution is [resolution]. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can settle a disagreement with evidence." Below 4 it lists the Why text of each missed case.

**Starting State:** Case 1 with both reviewers' scores and evidence shown. The question shown is "How should these two reviewers resolve this metric?"

**Chapter Anchors:** The chapter says reconciliation applies when scores differ by more than 3 points, that the reviewers decide by evidence and never average, and that unresolved metrics are recorded as disputed.
</details>

## Adopt, Revise, or Reject

**Adopt, revise, or reject** names the three decisions a review can lead to. The adoption threshold from Chapter 3 maps scores to them. A resource is ready to **adopt** when its total is at least 75 and every metric is at least 5. It should be **revised** when its total is at least 50 and the adopt rule is not met, which means the resource is promising and needs work. It should be **rejected** when its total is below 50. These values are this book's starting rule, and a department may set stricter ones.

| Decision | Rule | What it means for the teacher |
|---|---|---|
| Adopt | Total >= 75, and every metric >= 5 | Use the resource as it is, and record the weak metrics |
| Revise | Total >= 50, and the Adopt rule is not met | Improve the resource, or use it with the known gaps, then review again |
| Reject | Total < 50 | Look for another resource |

The rule has sharp edges, and a reviewer should know them. A total of exactly 75 with every metric at 5 or above is an Adopt. A total of 74 is a Revise, however close it looks. A total of 88 with one metric at 4 is a Revise, because the floor catches a failed metric that a high total hides. A total of exactly 50 is a Revise, and 49 is a Reject.

The third MicroSim practices the edges. It shows six scored resources, and for each one you apply the rule to choose the decision.

#### Diagram: Adoption Boundary Cases

<details markdown="1">
<summary>Adoption Boundary Cases</summary>
Type: microsim
**sim-id:** adoption-boundary-cases<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the adoption threshold to choose adopt, revise, or reject for each of six resources, including cases at the boundaries, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Adopt Revise or Reject, Manual Evaluation (both defined in this chapter above this block), and the Total Score and Adoption Threshold sections of Chapter 3.

**Evidence of Mastery:** For each resource the learner commits one of three decisions. A decision is correct when it matches the Correct decision column in Content. Mastery is at least 5 of 6 correct on the first attempt. Using the explore mode is exploration, not evidence.

**Misconceptions:** (1) A total of 75 or more is always an Adopt. (2) A total of 50 is a Reject. (3) The floor applies only to the lowest-scoring chapter.

**Instructional Rationale:** Applying a rule at its edges is an Apply-level action that exposes misreadings of the rule. Six cases at the exact boundaries and with a hidden low metric teach the learner to check both parts of the Adopt rule.

**Content:**

The rule, shown at all times: Adopt when the total >= 75 and every metric >= 5. Reject when the total < 50. Otherwise Revise.

The six resources (all made up):

| # | Resource | Total | Lowest metric | Correct decision | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | Boundary Adopt | 75 | 5 | Adopt | The total is exactly 75 and the lowest metric is exactly 5, so both conditions hold. |
| 2 | Just Short | 74 | 6 | Revise | The total is 74, which is less than 75, and 74 is at least 50. |
| 3 | High Total, One Gap | 88 | 4 | Revise | The total passes, but one metric is less than 5, so the Adopt rule is not met. |
| 4 | Boundary Revise | 50 | 3 | Revise | The total is exactly 50, which is not less than 50, and the Adopt rule is not met. |
| 5 | Just Below | 49 | 4 | Reject | The total is less than 50. |
| 6 | Strong All Round | 93 | 9 | Adopt | The total is greater than 75 and the lowest metric is greater than 5. |

**Provenance:** The resources are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The rule is the chapter's starting rule, and the sim labels it "starting values, not a standard".

**Rules:** Each resource has exactly one correct decision. Two are Adopt, three are Revise, and one is Reject. In explore mode the learner sets the total (minimum 0, maximum 100, step 1, default 70, unit points) and the lowest metric (minimum 0, maximum 10, step 1, default 5, unit points), and the sim shows the decision and the rule that produced it. Ten scores cannot have a lowest value greater than their average, so the lowest metric cannot exceed the total divided by 10 rounded down, and it cannot be less than the total minus 90. The sim disables impossible combinations.

**Learner Activity:**

1. In explore mode the learner moves the two sliders and watches the decision change.
2. In practice mode the sim shows resource 1 with its total and lowest metric.
3. The learner chooses Adopt, Revise, or Reject, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After resource 6 the sim shows the summary.

**Feedback:** 6 resources in a shuffled order, one attempt each. Correct: "Correct: [decision]. [Why]". Incorrect: "Not quite. The decision is [decision]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can apply the threshold at its edges." Below 5 it lists the Why text of each missed resource.

**Starting State:** Explore mode with a total of 70 and a lowest metric of 5, so the decision is Revise. The prompt is "Move a slider to see the decision change."

**Chapter Anchors:** The chapter says Adopt needs a total >= 75 and every metric >= 5, Revise needs a total >= 50 without meeting the Adopt rule, and Reject is a total < 50. The chapter's worked examples are a total of 75, 74, 88 with one metric at 4, 50, and 49, and the sim's case with a total of 49 has a lowest metric of 4.
</details>

### Adoption Decision

An **adoption decision** is the formal choice, by a person or group with authority, of whether to use a resource in a course or a school. A review informs the decision and does not make it. The group that decides may be a department, a district committee, or a single teacher, and it weighs the review against things the rubric does not measure, such as cost, fit with the course, and training needs. A good decision is recorded with the date, the decision-makers, the review it relied on, and a time to look again, since a resource that scores well today may be out of date in a few years.

### Adoption Recommendation

An **adoption recommendation** is the reviewer's written advice to the decision-makers. It states the decision the scores support, gives the reasons in plain words, names the strongest and weakest metrics, and lists the improvements that would raise the score most. It is the part of the review that busy readers will actually read, so it comes first in the report and fits on a page.

**Worked example: the recommendation for Watershed Basics.** The reviewer writes three sentences for the department.

"Revise before adopting. *Watershed Basics* scores 65 of 100, in the Fair band, and the adoption rule is not met because its metadata scores 4, below the floor of 5. The three changes that would help most are filling in the metadata, adding captions and alt text, and separating the quiz from the reading, and each is small."

## Key Takeaways

- **Manual evaluation** is a full human review: ten scores, evidence, subtotals, a total, and a decision. Doing it by hand first gives you the standard for checking an AI agent later.
- A **review workflow** of nine steps keeps reviews comparable. **Evidence recording** keeps every score checkable, and **reviewer notes** hold leads that are not yet evidence.
- A **calibration session** has reviewers score the same samples and discuss the differences. **Reviewer training** prepares a new reviewer for real reviews.
- **Consensus scoring** settles on one score per metric by evidence, never by averaging. **Score reconciliation** repeats the check behind each flagged metric and chooses the score the evidence supports.
- **Adopt, revise, or reject** follows the adoption threshold. An **adoption decision** is made by people with authority, and an **adoption recommendation** gives them the reviewer's advice in a page.

!!! mascot-celebration "You Can Review a Resource From Start to Finish"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now run a full manual review, record the evidence, reconcile scores with a second reviewer, and turn the total into an adopt, revise, or reject recommendation you can defend. That is the human standard that every AI agent in the coming chapters will be measured against.

[See Annotated References](./references.md)
