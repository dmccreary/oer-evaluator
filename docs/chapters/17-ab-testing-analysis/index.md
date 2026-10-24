---
title: "Analyzing A/B Test Results"
description: "Shows how to collect and anonymize data, compare group means, read effect size, combine surveys with qualitative feedback, check rubric scores against outcomes, and consider equity."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 23:05:46"
version: 1.11
---

# Analyzing A/B Test Results

## Summary

Shows how to collect and anonymize data, compare group means, read effect size, combine surveys with qualitative feedback, check rubric scores against outcomes, and consider equity. It follows the A/B test design chapter and closes the loop between rubric scores and learning outcomes. After this chapter you can collect and anonymize data, compare two groups, read an effect size, and check whether rubric scores predict learning.

## Concepts Covered

This chapter covers the following 13 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Data Collection | 23 |
| Anonymized Data | 1 |
| Mean Score | 11 |
| Difference of Means | 10 |
| Effect Size | 5 |
| Student Survey | 8 |
| Completion Rate | 1 |
| Time on Task | 1 |
| Qualitative Feedback | 5 |
| Results Summary | 4 |
| Rubric-Outcome Correlation | 1 |
| Pilot Test | 1 |
| Equity Consideration | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)
- [Chapter 7: Accessibility](../07-accessibility/index.md)
- [Chapter 14: Checking and Calibrating AI Agent Output](../14-checking-agent-output/index.md)
- [Chapter 16: Designing an A/B Test with Students](../16-ab-testing-design/index.md)

---

!!! mascot-welcome "Now Let the Data Speak"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    The test is run and the scores are in. This chapter shows you how to look after the data, compare the two groups fairly, and say what the numbers do and do not show. Let's dive in and check the evidence!

The last chapter designed a test, and this chapter reads its results. The test is the *Watershed Basics* pilot: one class of 24 students, split by blocked random assignment into a control group of 12 who used the original version and a treatment group of 12 who used the improved version. Everyone took the same 20-question pre-test and post-test. The hypothesis, written in advance, was that the treatment group's mean learning gain would be at least 5 percentage points larger.

The analysis is deliberately simple. It needs a calculator or a spreadsheet and a few ideas: what to collect, how to compare averages, how big a difference is, what students say, and how far to trust a small test. At the end, the results close a loop. They show whether the rubric scores of Chapters 3 through 10 predict what students learn, which is how the automated scoring in this book is checked against reality.

## Data Collection

**Data collection** is the careful gathering of the measurements the test needs, in the same way for both groups. Chapter 16 chose the measures. This step gets them into a table where they can be trusted. A plan covers four things: what is collected, when, by whom, and where it is kept.

For the pilot, the schedule follows the design.

| Week | What happens | Data collected |
|---|---|---|
| 1 | Pre-test, then assignment | Pre-test score for each student |
| 2 and 3 | Students use their assigned version | Completion of the quiz and minutes on task, logged by the platform |
| 4 | Post-test and survey | Post-test score, survey ratings, and written comments |

Everything goes into one spreadsheet with one row per student. The table gives the columns, which together are the *data dictionary*.

| Column | Meaning |
|---|---|
| Code | The student's code, such as S07, and nothing else that identifies them |
| Version | C for the original, T for the improved version |
| Pre-test | Score from 0 to 100 |
| Post-test | Score from 0 to 100 |
| Gain | Post-test minus pre-test, computed by formula |
| Completed quiz | Yes or No |
| Minutes on task | Whole minutes |
| Survey items 1 to 3 | Ratings from 1 to 5 |
| Comment | Written text with names removed |

Four habits protect the quality of the data. Use the same procedure, script, and timing for both groups. Keep a short log of anything unusual, such as a fire drill during the post-test or a device that failed. Check the table for errors before analyzing it: missing values, scores outside 0 to 100, repeated codes, and labels typed two ways. And keep a backup in an approved location. A calculation on a mistyped table gives a confident wrong answer.

The MicroSim below practices the check. It shows a table of ten rows with five planted errors, and you find them.

#### Diagram: Data Quality Detective

<details markdown="1">
<summary>Data Quality Detective</summary>
Type: microsim
**sim-id:** data-quality-detective<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine a ten-row test data table and identify the five rows with errors and the kind of error in each, with at least 4 of 5 error rows named correctly on the first attempt.

**Prerequisites:** Data Collection, Pre-Test, Post-Test, Learning Gain (all defined in this chapter above this block or in Chapter 16).

**Evidence of Mastery:** The learner marks each row Clean or Error, and for each Error row picks the kind of error. An error row is correct when both the marking and the kind match the Content table. Clean rows marked Error count against the learner. Mastery is at least 4 of the 5 error rows correct and no more than 1 clean row marked as an error, on the first attempt. Reading the error kinds is exploration, not evidence.

**Misconceptions:** (1) A table that opens without a warning is correct. (2) A score of 120 belongs to a high-performing student. (3) A blank cell can be treated as zero.

**Instructional Rationale:** Examining a data table for errors is an Analyze-level action that comes before any calculation. A table with five different kinds of error and five clean rows teaches the learner to check each column against its meaning.

**Content:**

The data dictionary, shown at all times: Code (unique), Version (C or T), Pre-test (0 to 100), Post-test (0 to 100).

The five kinds of error: Missing value, Out of range, Repeated code, Inconsistent label, Wrong unit.

The ten rows (all made up):

| Row | Code | Version | Pre-test | Post-test | Correct marking | Kind of error | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|
| 1 | S01 | T | 28 | 59 | Clean | None | The values are in range and the label is valid. |
| 2 | S02 | C | 22 | 42 | Clean | None | The values are in range and the label is valid. |
| 3 | S03 | T | 31 | (blank) | Error | Missing value | The post-test is blank, and a blank must not be treated as zero. |
| 4 | S04 | C | 35 | 50 | Clean | None | The values are in range and the label is valid. |
| 5 | S05 | T | 41 | 120 | Error | Out of range | A score of 120 is outside 0 to 100. |
| 6 | S06 | C | 0.38 | 46 | Error | Wrong unit | The pre-test is a fraction and the column holds percentages. |
| 7 | S07 | Treatment | 43 | 76 | Error | Inconsistent label | The column uses C and T, and this row uses a word. |
| 8 | S08 | C | 45 | 64 | Clean | None | The values are in range and the label is valid. |
| 9 | S08 | T | 47 | 70 | Error | Repeated code | Code S08 appears twice, so two students share a code. |
| 10 | S10 | C | 48 | 66 | Clean | None | The values are in range and the label is valid. |

**Provenance:** The rows are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The error kinds follow the chapter section "Data Collection".

**Rules:** Exactly five rows are errors and five are clean. Each of the five kinds of error appears once.

**Learner Activity:**

1. The learner sees the table and the data dictionary.
2. The learner marks each row Clean or Error, and for each Error row picks the kind of error.
3. The learner presses Check.
4. The sim shows which markings were correct, the kind of each error, and the Why text.

**Feedback:** One check, after all ten rows are marked. Correct: "Correct: row [n], [kind]. [Why]". Incorrect: "Not quite. Row [n] is [marking], [kind]. [Why]". The summary shows "[n] of 5 error rows correct, [m] clean rows marked as errors". When mastery is met it adds "You can check a table before you use it." Otherwise it lists the Why text of each missed row.

**Starting State:** The table with all rows unmarked, and the data dictionary.

**Chapter Anchors:** The chapter says to check for missing values, scores outside 0 to 100, repeated codes, and labels typed two ways. The sim adds a wrong-unit error.
</details>

### Anonymized Data

**Anonymized data** is data from which every link to a particular person has been removed, so that no one, including the teacher, can tell whose scores they are. It differs from *coded* data. Coded data replaces names with codes and keeps a key somewhere, so the link can be rebuilt. Anonymizing happens when the key is destroyed on the deletion date promised in the consent letter, and when nothing else in the table points to a person.

Codes alone are not always enough. In a class of 24, a column that records gender, class period, and the teacher's name can single out a student, and a written comment such as "the girl who sits by the window" can name one. The steps are to drop columns the analysis does not need, to generalize others (grade level, not birthdate), to hide results for any group under the size your district sets, and to remove identifying detail from comments. A good test is to ask whether someone who knows the class could pick out a single student from what you plan to share. If yes, remove more.

The MicroSim below practices the test. It describes eight tables or notes, and for each you decide whether it is safe to share.

#### Diagram: Re-identification Risk Checker

<details markdown="1">
<summary>Re-identification Risk Checker</summary>
Type: microsim
**sim-id:** reidentification-risk-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight data items from a class test is safe to share or a re-identification risk, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Anonymized Data, Student Privacy in Testing (defined in this chapter above this block or in Chapter 16).

**Evidence of Mastery:** For each item the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the four steps is exploration, not evidence.

**Misconceptions:** (1) Replacing names with codes makes data anonymous. (2) A group average is always safe. (3) A quotation is harmless if the name is removed.

**Instructional Rationale:** Judging whether data can point to a person is an Evaluate-level action. Items that look harmless but identify a student in a class of 24 teach the learner to ask who could pick out a student.

**Content:**

The two bins: Safe to share, Re-identification risk.

The eight items (all made up, for the Watershed Basics pilot of 24 students in one class):

| # | Item | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | A table with the columns code, version, pre-test, and post-test. | Safe to share | It holds codes and scores only. |
| 2 | A table with code, version, pre-test, post-test, class period, teacher name, and gender. | Re-identification risk | In a class of 24 these columns can single out a student. |
| 3 | A table with student name, version, pre-test, and post-test. | Re-identification risk | The names identify each student. |
| 4 | Comments with names removed and details about seat and appearance removed. | Safe to share | Nothing in them points to one student. |
| 5 | A comment that reads "The girl who sits by the window said the video was too fast." | Re-identification risk | The detail points to one student. |
| 6 | The average gain for the control group and the average gain for the treatment group. | Safe to share | Each average covers 12 students. |
| 7 | The average gain for the 3 students who use captions. | Re-identification risk | A group of 3 is below the size most districts allow to be reported. |
| 8 | A file of codes and scores after the key file has been deleted on the stated date. | Safe to share | No link to a person remains. |

**Provenance:** The items are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The sim adds the note "your school's rules decide the smallest group you may report".

**Rules:** Each item has exactly one correct bin, four per bin.

**Learner Activity:**

1. The learner sees one item and the two bins.
2. The learner places the item in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After item 8 the sim shows the summary.

**Feedback:** 8 items in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can tell safe data from risky data." Below 7 it lists the Why text of each missed item.

**Starting State:** The first item in the shuffled order and the two bins. The question shown is "Could someone who knows the class pick out a student?"

**Chapter Anchors:** The chapter says that codes alone are not always enough and lists the steps of dropping columns, generalizing, hiding small groups, and cleaning comments.
</details>

## Mean Score

A **mean score** is the average of a set of scores: add them all and divide by how many there are. It is the most common way to summarize a group with one number. For the pilot, the number to summarize is each student's learning gain, the post-test minus the pre-test.

The control group's 12 gains add to 180, so their mean gain is 180 divided by 12, which is **15.0** points. The treatment group's 12 gains add to 264, so their mean gain is 264 divided by 12, which is **22.0** points.

A mean hides how scores are spread out, so report the spread too. The *standard deviation* is the typical distance of a score from the mean: the larger it is, the more the scores vary. The *median* is the middle score when they are sorted, and it is a useful check against one very high or very low score. The table gives all three for the pilot.

| | Control group | Treatment group |
|---|---|---|
| Students | 12 | 12 |
| Mean pre-test score | 51.5 | 52.25 |
| Mean post-test score | 66.5 | 74.25 |
| Mean gain | 15.0 | 22.0 |
| Median gain | 17.5 | 21.5 |
| Standard deviation of the gains | 6.0 | 7.4 |

The two groups began almost level, with mean pre-test scores of 51.5 and 52.25, which is what blocked random assignment was meant to do.

## Difference of Means

The **difference of means** is the mean of the treatment group minus the mean of the control group. It is the single number that answers the hypothesis: how much more did students gain with the improved version?

For the pilot, the difference of mean gains is 22.0 minus 15.0, which is **+7.0** points. The hypothesis set a bar of at least 5 points, and 7.0 is above it, so in this pilot the result supports the hypothesis. Compare gains and not post-test means alone. The post-test means differ by 7.75 points, but the groups started 0.75 points apart, and the gain removes that head start.

A difference of means has to be read with care, especially in a small test. With 12 students per group, a few unusually strong or weak students can move an average. The gains of the two groups overlap: the control group's run from 3 to 22 and the treatment group's from 9 to 33. The difference is a real finding about these 24 students, and it may partly be luck. The effect size, next, puts the difference in context, and the pilot section later in the chapter says what to do about the uncertainty.

The MicroSim below puts the data in your hands. It gives the twelve gains for each group, and you calculate the means, the medians, and the difference.

#### Diagram: Mean and Difference Calculator

<details markdown="1">
<summary>Mean and Difference Calculator</summary>
Type: microsim
**sim-id:** mean-difference-calculator<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the mean gain of each group, the difference of means, and the median gain of each group from a table of 24 gains, and decide whether the difference meets the 5-point threshold, with at least 5 of 6 answers correct on the first attempt.

**Prerequisites:** Mean Score, Difference of Means, Learning Gain (defined in this chapter above this block or in Chapter 16).

**Evidence of Mastery:** The learner answers six questions. An answer is correct when it matches the Correct answer column in Content. Numeric answers are correct to one decimal place. Mastery is at least 5 of 6 correct on the first attempt. Sorting the gains or using a calculator inside the sim is exploration, not evidence.

**Misconceptions:** (1) The mean and the median are the same number. (2) A positive difference always meets the hypothesis. (3) The mean of post-test scores can replace the mean of gains.

**Instructional Rationale:** Calculating means and a difference from raw data is an Apply-level action that the learner will repeat on a real test. Twelve values per group are few enough to calculate by hand and enough to need a method.

**Content:**

The data, shown at all times (learning gains in percentage points, made up for the Watershed Basics pilot):

| Group | The twelve gains, in the order of student code |
|---|---|
| Control (original version) | 20, 15, 8, 19, 18, 17, 21, 10, 18, 9, 3, 22 |
| Treatment (improved version) | 31, 11, 20, 33, 23, 26, 18, 28, 9, 18, 27, 20 |

The hypothesis, shown at all times: the treatment group's mean gain will be at least 5 percentage points larger than the control group's.

The six questions:

| # | Question | Answer type | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | What is the mean gain of the control group? | Number to one decimal place | 15.0 | The gains add to 180, and 180 divided by 12 is 15.0. |
| 2 | What is the mean gain of the treatment group? | Number to one decimal place | 22.0 | The gains add to 264, and 264 divided by 12 is 22.0. |
| 3 | What is the difference of means, treatment minus control? | Number with a sign | +7.0 | 22.0 minus 15.0 is 7.0. |
| 4 | Does the difference meet the hypothesis? | Yes or No | Yes | 7.0 >= 5. |
| 5 | What is the median gain of the control group? | Number to one decimal place | 17.5 | Sorted, the sixth and seventh gains are 17 and 18, and their middle is 17.5. |
| 6 | What is the median gain of the treatment group? | Number to one decimal place | 21.5 | Sorted, the sixth and seventh gains are 20 and 23, and their middle is 21.5. |

**Provenance:** The gains are illustrative examples made up for this chapter, and the sim labels them "illustrative examples". The calculations follow the chapter sections "Mean Score" and "Difference of Means".

**Rules:** The mean is the sum divided by 12. The median of twelve values is the mean of the sixth and seventh values after sorting. The difference is treatment minus control.

**Learner Activity:**

1. The learner sees the data and the first question.
2. The learner enters an answer, and the answer is committed.
3. The sim shows whether it was correct and the Why text.
4. After question 6 the sim shows the summary.

**Feedback:** 6 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can compare two groups." Below 5 it lists the Why text of each missed question.

**Starting State:** The data table, the hypothesis, and question 1.

**Chapter Anchors:** The chapter's table of group statistics and its difference of means use the same gains.
</details>

## Effect Size

An **effect size** is a measure of how big a difference is, in units that do not depend on the test, so that studies can be compared. The most widely used is Cohen's *d*:

d = (mean of treatment - mean of control) / pooled standard deviation

The pooled standard deviation combines the spread of the two groups: for equal sizes it is the square root of the average of the two squared standard deviations. In the pilot, 6.05 squared is about 36.5 and 7.45 squared is about 55.5. They average 46.0, whose square root is 6.78. So *d* is 7.0 divided by 6.78, about **1.03**.

By convention, a *d* of 0.2 is called small, 0.5 medium, and 0.8 large. These are rules of thumb, and what counts as important depends on the cost of the change and the setting. By the convention 1.03 is large, but a small pilot gives a noisy estimate, and impressive estimates from small tests tend to shrink when repeated with more students.

!!! mascot-thinking "A Big Number From a Small Test Deserves a Second Look"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Twelve students per group can produce a lovely effect size by luck. Treat a pilot's result as a reason to test again, and do not treat it as the final answer.

The MicroSim below lets you see how the difference and the spread combine into an effect size.

#### Diagram: Effect Size Explorer

<details markdown="1">
<summary>Effect Size Explorer</summary>
Type: microsim
**sim-id:** effect-size-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate Cohen's d from a difference of means and a pooled standard deviation for six cases and name its conventional size, with at least 5 of 6 cases fully correct on the first attempt.

**Prerequisites:** Effect Size, Difference of Means, Mean Score (all defined in this chapter above this block).

**Evidence of Mastery:** For each case the learner enters d to two decimal places and chooses a size label. A case is fully correct when both match the Content table. Mastery is at least 5 of 6 cases fully correct on the first attempt. Moving the two sliders in free play is exploration, not evidence.

**Misconceptions:** (1) A bigger difference of means always means a bigger effect size. (2) An effect size of 0.2 is worthless. (3) The same difference means the same thing whatever the spread.

**Instructional Rationale:** Calculating d from a difference and a spread is an Apply-level action. Cases that hold the difference fixed while the spread changes teach the learner that the spread is part of the answer.

**Content:**

The formula, shown at all times: d = difference of means / pooled standard deviation.

The size labels, shown at all times: d < 0.2 is Less than small. 0.2 <= d < 0.5 is Small. 0.5 <= d < 0.8 is Medium. d >= 0.8 is Large. These are conventional rules of thumb, labeled "rule of thumb" in the sim.

The six cases (all made up, in test-score points):

| # | Difference of means | Pooled standard deviation | d | Size label | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | 7.0 | 6.8 | 1.03 | Large | 7.0 divided by 6.8 is about 1.03, the Watershed Basics pilot. |
| 2 | 5.0 | 10.0 | 0.50 | Medium | 5.0 divided by 10.0 is 0.50. |
| 3 | 2.0 | 10.0 | 0.20 | Small | 2.0 divided by 10.0 is 0.20. |
| 4 | 8.0 | 10.0 | 0.80 | Large | 8.0 divided by 10.0 is 0.80. |
| 5 | 3.0 | 15.0 | 0.20 | Small | A 3-point difference is small when scores vary by 15. |
| 6 | 1.0 | 10.0 | 0.10 | Less than small | 1.0 divided by 10.0 is 0.10. |

Free play: two sliders set the difference of means from 0 to 15 and the pooled standard deviation from 3 to 15, and the sim shows d and its label. Free play is labeled "not scored".

**Provenance:** The cases are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The size labels are Cohen's conventions and are marked "rule of thumb".

**Rules:** d is rounded to two decimal places. A case is fully correct only when d and the label both match.

**Learner Activity:**

1. The learner sees one case with its difference and spread.
2. The learner enters d and chooses a size label, and presses Check.
3. The sim shows which entries were correct and the Why text.
4. After case 6 the sim shows the summary and opens free play.

**Feedback:** 6 cases in a shuffled order, one attempt each. Correct: "Correct: d is [d], which is [label]. [Why]". Incorrect: "Not quite. d is [d], which is [label]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read an effect size." Below 5 it lists the Why text of each missed case.

**Starting State:** The first case in the shuffled order, the formula, and the size labels.

**Chapter Anchors:** The chapter's worked calculation gives d = 1.03 for the pilot, and the sim's case 1 is the same calculation.
</details>

## Student Survey

A **student survey** is a short set of questions that asks students what they thought of the lesson. The test scores say what students learned. The survey says what they experienced: whether they could follow it, whether they met barriers, and whether they would want more. The two kinds of evidence answer different questions, and a version can do well on one and not on the other.

Good survey questions follow five rules.

- **Same for both groups:** the same wording and scale, so ratings can be compared.
- **Neutral:** a question must not hint at the answer. "Did you enjoy the great new simulation?" pushes students to say yes.
- **One idea each:** "The lesson was clear and the quiz was fair" asks two things, and a student who thinks one is true and the other false cannot answer.
- **Specific:** "The lesson was good" says nothing about what to fix.
- **Anonymous:** answers are tied to a code and not a name, so students can be honest.

A common format is a rating from 1 (strongly disagree) to 5 (strongly agree). The pilot's survey had three such questions, and all 24 students answered. The table gives the mean rating in each group.

| Survey question | Control mean | Treatment mean |
|---|---|---|
| The lesson helped me understand what a watershed is. | 3.5 | 4.3 |
| I could read or hear every part of the lesson without help. | 3.3 | 4.4 |
| I would like more lessons like this one. | 3.4 | 4.3 |

The treatment group rated all three questions about one point higher, and the largest gap is on the accessibility question, which fits the added captions and image descriptions. Read ratings with care. They report opinion and not learning, and students given something new may rate it higher partly because it is new. They are a useful companion to the scores and a poor substitute for them.

The MicroSim below practices writing questions. It shows eight draft questions, and for each one you decide whether it is good or has a problem.

#### Diagram: Survey Question Reviewer

<details markdown="1">
<summary>Survey Question Reviewer</summary>
Type: microsim
**sim-id:** survey-question-reviewer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** critique<br/>
**Learning Objective:** The learner will critique eight draft survey questions as good or problematic and name the problem in each problematic question, with at least 7 of 8 verdicts correct on the first attempt.

**Prerequisites:** Student Survey (defined in this chapter above this block).

**Evidence of Mastery:** For each question the learner commits Good or Problem, and for a Problem picks its kind from Leading, Double-barreled, or Vague. A verdict is correct when it matches the Correct verdict column in Content, and the kind is checked in the feedback. Mastery is at least 7 of 8 verdicts correct on the first attempt. Reading the five rules is exploration, not evidence.

**Misconceptions:** (1) A longer question gets a better answer. (2) A positive question is a neutral question. (3) Asking two things at once saves time.

**Instructional Rationale:** Critiquing a question against the survey rules is an Evaluate-level action. Questions that fail in different ways, and four sound ones, teach the learner to read each question as a student would.

**Content:**

The two verdicts: Good, Problem. The kinds of problem: Leading, Double-barreled, Vague.

The eight draft questions (all made up):

| # | Draft question | Correct verdict | Kind of problem | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | The lesson helped me understand what a watershed is. (1 to 5, disagree to agree) | Good | None | It is neutral, specific, and about one idea. |
| 2 | Did you enjoy the great new simulation? | Problem | Leading | The word "great" pushes students toward yes. |
| 3 | The lesson was clear and the quiz was fair. | Problem | Double-barreled | It asks two things at once. |
| 4 | The lesson was good. | Problem | Vague | It does not say what to fix. |
| 5 | I could read or hear every part of the lesson without help. (1 to 5, disagree to agree) | Good | None | It is neutral and specific, and it asks about access. |
| 6 | Which parts of the lesson, if any, were hard to use? (open answer) | Good | None | It is neutral and invites specific answers. |
| 7 | Don't you agree that the explanations were helpful? | Problem | Leading | It asks the student to agree. |
| 8 | I would like more lessons like this one. (1 to 5, disagree to agree) | Good | None | It is neutral and about one idea. |

**Provenance:** The questions are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The rules follow the chapter section "Student Survey".

**Rules:** Each question has exactly one correct verdict, four per verdict. The four problems are two Leading, one Double-barreled, and one Vague.

**Learner Activity:**

1. The learner sees one draft question.
2. The learner chooses Good or Problem. For a Problem the learner also picks its kind.
3. The sim shows whether the verdict was correct, the kind of problem, and the Why text.
4. After question 8 the sim shows the summary.

**Feedback:** 8 questions in a shuffled order, one attempt each. Correct: "Correct: [verdict]. [Why]". Incorrect: "Not quite. This question is [verdict]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can write fair survey questions." Below 7 it lists the Why text of each missed question.

**Starting State:** The first question in the shuffled order and the two verdicts. The question shown is "Would this question get an honest answer?"

**Chapter Anchors:** The chapter lists five rules for survey questions, and its examples of a leading question, a double-barreled question, and a vague question appear in the sim.
</details>

### Completion Rate

The **completion rate** is the share of students who finished an activity out of those who started it. Divide the number who finished by the number who started and write the answer as a percentage. In the pilot, 10 of the 12 control students finished the quiz, a rate of 83 percent, and all 12 treatment students did, a rate of 100 percent.

A low completion rate is a signal to look for the reason. Here the two control students who did not finish could not make the original quiz load on the school's tablets. That is the portability failure that Chapter 10 found: the quiz script failed on one platform. It is a barrier and not a lack of interest. Because the post-test was separate from the resource's quiz, those two students still took it, and their gains stayed in the analysis.

### Time on Task

**Time on task** is the number of minutes a student spends working on the activity. A platform log or a teacher's timer records it. The pilot's mean was 38 minutes for the control group and 47 for the treatment group, a difference of 9 minutes.

Read the number with care, because more time is not automatically better or worse. The improved version contains a worked example and a simulation, so 9 more minutes is about what they would add. If a change cut time on task and left the gain unchanged, that would suggest a more efficient resource. If it cut time and the gain fell, students may have lost interest. Always read time on task together with the learning gain.

## Qualitative Feedback

**Qualitative feedback** is what students say in their own words: written comments, answers to open questions, or short interviews. It tells you the *why* behind the numbers. A rating tells you a student was unhappy. A comment tells you that the quiz would not open on a tablet.

To use comments, code them. Read all the comments, list the themes that recur, and count how many comments mention each. Have two people code independently and compare, as with the human raters of Chapter 14, and resolve differences by discussion. Remove names and identifying detail before you quote anyone. The table gives the themes of the pilot's comments from the 24 students, counted by the number of students who raised each one.

| Theme | Control (of 12) | Treatment (of 12) |
|---|---|---|
| Unfamiliar words, such as "aquifer" | 4 | 1 |
| The quiz would not load | 2 | 0 |
| Wanted a worked example or more practice | 5 | 1 |
| The simulation helped me see it | 0 | 7 |
| Captions or image descriptions helped | 0 | 4 |
| The quiz explanations helped | 1 | 6 |

The themes agree with the numbers: the control group's comments cluster around problems the plan fixed, and the treatment group's around the features it added. Comments hint at causes without proving them.

!!! mascot-tip "Quote the Comment That Surprised You"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Counts show the pattern, and one well-chosen comment makes it real for a reader. Pick a comment that explains a number, and take out anything that could identify the student.

The MicroSim below practices coding. It shows ten comments, and for each one you choose the theme it belongs to.

#### Diagram: Feedback Theme Coder

<details markdown="1">
<summary>Feedback Theme Coder</summary>
Type: microsim
**sim-id:** feedback-theme-coder<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of ten student comments under one of seven themes, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Qualitative Feedback, Student Survey (both defined in this chapter above this block).

**Evidence of Mastery:** For each comment the learner commits one of seven themes. A placement is correct when it matches the Correct theme column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the theme list is exploration, not evidence.

**Misconceptions:** (1) Comments are too subjective to code. (2) A comment can belong to only one study. (3) The most vivid comment is the most common theme.

**Instructional Rationale:** Classifying comments under themes is an Understand-level action that turns words into counts. Ten comments over seven themes teach the learner to read for the main point of each.

**Content:**

The seven themes: Unfamiliar words, Technical problem, Wanted more practice, Simulation helped, Captions or descriptions helped, Explanations helped, Other.

The ten comments (all made up, names removed):

| # | Comment | Correct theme | Why (shown as feedback) |
|---|---|---|---|
| 1 | I did not know what "aquifer" meant. | Unfamiliar words | The student names a word they did not know. |
| 2 | The quiz would not open on my tablet. | Technical problem | It describes a failure to load. |
| 3 | The slider that changes the ground cover showed me where the rain goes. | Simulation helped | It credits the simulation. |
| 4 | I could follow the video because of the captions. | Captions or descriptions helped | It credits the captions. |
| 5 | I wanted more questions to practice before the test. | Wanted more practice | It asks for more practice. |
| 6 | When I got a question wrong, the explanation told me why. | Explanations helped | It credits the explanations. |
| 7 | There were too many hard words in section 3. | Unfamiliar words | It names hard words. |
| 8 | I liked the pictures. | Other | It fits none of the six named themes. |
| 9 | The page was slow to load. | Technical problem | It describes a loading problem. |
| 10 | A worked example would have helped. | Wanted more practice | It asks for more support to practice. |

**Provenance:** The comments are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The themes follow the chapter section "Qualitative Feedback".

**Rules:** Each comment has exactly one correct theme. Unfamiliar words, Technical problem, and Wanted more practice have two comments each. Simulation helped, Captions or descriptions helped, Explanations helped, and Other have one each.

**Learner Activity:**

1. The learner sees one comment and the seven themes.
2. The learner places the comment under a theme, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After comment 10 the sim shows the summary with the count for each theme.

**Feedback:** 10 comments in a shuffled order, one attempt each. Correct: "Correct: [theme]. [Why]". Incorrect: "Not quite. This comment is [theme]. [Why]". The summary shows "[n] of 10 correct on the first attempt" and the counts per theme. At 9 or more it adds "You can turn comments into counts." Below 9 it lists the Why text of each missed comment.

**Starting State:** The first comment in the shuffled order and the seven themes. The question shown is "What is this student mainly saying?"

**Chapter Anchors:** The chapter's table of themes for the pilot uses the same six named themes.
</details>

## Results Summary

A **results summary** is a short written account of what the test showed. It is the document a colleague, a principal, or an adopter will read, so it has to be clear, honest, and complete in one or two pages. A good summary has seven parts.

| Part | What it says |
|---|---|
| Question | What the test set out to find out, and the hypothesis |
| Design | The two versions, the groups, the assignment, and the measures |
| Participants | How many students, from where, and how many finished |
| Results | The means, the difference, and the other measures |
| Effect size | How big the difference is, with the convention noted |
| Limitations | The small sample, the bundle of fixes, and anything unusual |
| Decision | What follows, such as adopt, revise, or run a larger test |

For the pilot, the Results part would read: "The treatment group's mean gain was 22.0 points and the control group's was 15.0, a difference of 7.0, above the 5-point threshold in the hypothesis. The effect size was 1.03." The Limitations part would say that this was one class of 24 students, that five fixes were tested as a bundle, and that a pilot's effect size often shrinks in a larger test. The Decision would be to run a larger test.

The poster below shows the seven parts on a picture of a one-page summary.

#### Diagram: Results Summary Anatomy

<details markdown="1">
<summary>Results Summary Anatomy</summary>
Type: infographic
**sim-id:** results-summary-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the seven parts of a results summary from a description of how each looks, with at least 6 of 7 correct on the first attempt.

**Prerequisites:** Results Summary, Effect Size, Difference of Means (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 6 of 7 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) A results summary lists only the good news. (2) The limitations belong in a footnote. (3) The decision is separate from the results.

**Instructional Rationale:** Identifying the parts of a report is a Remember-level task, and a picture of a one-page summary with its parts marked gives each a place. The quiz asks the learner to recognize a part by its look.

**Content:**

The illustration is a text-free flat drawing of a one-page report. At the top is a banner with a question-mark icon. Below it is a small drawing of two groups of figures joined by an arrow. Next is a grid of 24 small dots. Next is a pair of bars of different heights. Beside the bars is a ruler with one marker on it. Below is a triangle with an exclamation mark. At the bottom is a signpost with two arrows. The seven markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Question | The banner with the question-mark icon. | What the test set out to find out, and the hypothesis. | State the hypothesis as it was written before the test. |
| 2 | Design | The two groups of figures joined by an arrow. | The versions, the groups, and the measures. | Name the one difference between the groups. |
| 3 | Participants | The grid of 24 small dots. | How many students took part and finished. | Report how many were invited, agreed, and finished. |
| 4 | Results | The pair of bars of different heights. | The means and the difference. | Report the gain and not only the post-test. |
| 5 | Effect size | The ruler with one marker on it. | How big the difference is. | Say which convention you used. |
| 6 | Limitations | The triangle with an exclamation mark. | What the test cannot show. | Name the small sample and the bundle of fixes. |
| 7 | Decision | The signpost with two arrows. | What follows from the results. | Tie the decision to the hypothesis. |

**Provenance:** The seven parts follow the chapter section "Results Summary". The illustration is synthetic, and the sim labels it "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 7 from the top of the page to its bottom.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 7 hints the sim shows the summary.

**Feedback:** 7 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 7 correct on the first attempt". At 6 or more it adds "You can read a results summary." Below 6 it lists the labels of the missed parts.

**Starting State:** The illustration with seven numbered markers, explore mode active, and the prompt "Hover a marker to see a part of the summary."

**Chapter Anchors:** The chapter's table of seven parts lists the same parts in the same order.
</details>

The MicroSim below tests the most important habit of a results summary: claiming no more than the data allow. It shows eight statements about the pilot, and for each one you decide whether the data support it.

#### Diagram: Claim and Data Judge

<details markdown="1">
<summary>Claim and Data Judge</summary>
Type: microsim
**sim-id:** claim-data-judge<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight statements about the pilot is supported by the data, is an overclaim, or is not shown by this test, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Results Summary, Difference of Means, Effect Size, Completion Rate (all defined in this chapter above this block).

**Evidence of Mastery:** For each statement the learner commits one of three bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the pilot's facts is exploration, not evidence.

**Misconceptions:** (1) A large effect size proves the improved version works everywhere. (2) A test of a bundle shows which fix worked. (3) A test with 24 students can report on subgroups.

**Instructional Rationale:** Judging a claim against the data is an Evaluate-level action that every results summary needs. Statements that are supported, overreach, or go beyond what was measured teach the learner to tie each claim to a number.

**Content:**

The three bins: Supported by the data, Overclaim, Not shown by this test. An Overclaim says more than the data allow, usually by generalizing past the students or the conditions tested. A statement that is Not shown by this test concerns something that the test did not measure or could not separate.

The pilot facts, available on demand: 24 students in one class, 12 per group. Mean gains 15.0 (control) and 22.0 (treatment), difference 7.0, effect size 1.03. The hypothesis threshold was 5. Quiz completion was 10 of 12 (control) and 12 of 12 (treatment). Five fixes were tested as a bundle. No subgroup results were collected, and the largest subgroup had 3 students.

The eight statements (all about the made-up Watershed Basics pilot):

| # | Statement | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | The treatment group's mean learning gain was 7.0 points larger than the control group's. | Supported by the data | It restates the difference of means. |
| 2 | The improved version works for all Grade 6 students. | Overclaim | The test used 24 students in one class. |
| 3 | The result met the 5-point threshold set in the hypothesis. | Supported by the data | 7.0 >= 5. |
| 4 | The simulation caused the larger gain. | Not shown by this test | Five fixes were tested together, so the test cannot say which one mattered. |
| 5 | The effect size was 1.03, which is large by the usual convention. | Supported by the data | It restates the calculation and the convention. |
| 6 | More students finished the quiz with the improved version: 12 of 12 against 10 of 12. | Supported by the data | It restates the completion counts. |
| 7 | Students who use captions benefited most from the improved version. | Not shown by this test | No subgroup results were collected, and the subgroup had 3 students. |
| 8 | A higher rubric score always means more learning. | Overclaim | One pilot cannot show an "always". |

**Provenance:** The facts and statements are illustrative examples written for this chapter, and the sim labels them "illustrative examples".

**Rules:** Each statement has exactly one correct bin. Four statements are Supported by the data, two are Overclaim, and two are Not shown by this test.

**Learner Activity:**

1. The learner sees one statement and the three bins, and may open the pilot facts. Opening them does not change the score.
2. The learner places the statement in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After statement 8 the sim shows the summary.

**Feedback:** 8 statements in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can tie a claim to the data." Below 7 it lists the Why text of each missed statement.

**Starting State:** The first statement in the shuffled order and the three bins. The question shown is "Does the data support this?"

**Chapter Anchors:** The chapter's Limitations part names the small sample, the bundle of fixes, and the lack of subgroup data, and its results come from the same pilot.
</details>

## Rubric-Outcome Correlation

The **rubric-outcome correlation** is the strength of the relationship between resources' rubric scores and how much students learn from them. This check closes the loop of the whole book. If resources with higher rubric scores tend to produce larger gains, the rubric measures something that matters. If not, the rubric and the automated scores built on it need rethinking.

Compute it across several resources, each tested in a pilot like this one. Because pilots use different tests, compare the *normalized* gain of Chapter 16. The table pairs seven resources' rubric totals with their mean normalized gains. Two are the original and improved *Watershed Basics*, taken from the pilot, and five are made-up pilots of resources from earlier chapters.

| Resource | Rubric total | Mean normalized gain |
|---|---|---|
| Thin Material | 37 | 0.12 |
| Open Unit With Errors | 65 | 0.22 |
| Locked Chemistry E-book | 65 | 0.28 |
| Watershed Basics, original | 65 | 0.33 |
| Watershed Basics, improved | 78 | 0.50 |
| One Gap | 85 | 0.46 |
| Open Algebra | 90 | 0.55 |

The Pearson correlation of these seven pairs, which is the same statistic as in Chapter 14, is about **0.93**. A value close to 1 means that higher totals go with higher gains. The squared value, 0.87, says that a straight line through the totals accounts for about 87 percent of the differences among these seven gains.

Read the result with care. Seven resources are few, so a correlation from them can swing widely. Different teachers taught different classes, and a correlation does not show that raising a rubric score causes more learning. Look also at the three resources that share a total of 65: their gains are 0.22, 0.28, and 0.33. Equal totals do not guarantee equal learning, and the lowest gain belongs to the resource with an Accuracy score of 3, which supports reading the lowest metric before the total. A serious check of the rubric needs 20 or more resources.

The MicroSim below lets you explore the scatter plot of these seven resources.

#### Diagram: Rubric-Outcome Scatter

<details markdown="1">
<summary>Rubric-Outcome Scatter</summary>
Type: chart
**sim-id:** rubric-outcome-scatter<br/>
**Library:** Chart.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine a scatter plot of rubric totals against mean normalized gains for seven resources and answer five questions about the correlation and its limits, with at least 4 of 5 correct on the first attempt.

**Prerequisites:** Rubric-Outcome Correlation, Learning Gain, Score Correlation (defined in this chapter above this block, in Chapter 16, or in Chapter 14).

**Evidence of Mastery:** The learner answers five questions about the plot. An answer is correct when it matches the Correct answer column in Content. Mastery is at least 4 of 5 correct on the first attempt. Hovering over points and toggling a point off are exploration, not evidence.

**Misconceptions:** (1) A correlation near 1 shows that raising the rubric score causes learning. (2) Resources with the same rubric total have the same gain. (3) Seven points are enough to settle the question.

**Instructional Rationale:** Examining a scatter plot against a number is an Analyze-level action that links a picture to a statistic. Points that share a total but differ in gain, and a toggle that removes a point, teach the learner what a correlation can and cannot say.

**Content:**

The plot, with the rubric total on the horizontal axis and the mean normalized gain on the vertical axis, shows the seven points:

| Resource | Rubric total | Mean normalized gain |
|---|---|---|
| Thin Material | 37 | 0.12 |
| Open Unit With Errors | 65 | 0.22 |
| Locked Chemistry E-book | 65 | 0.28 |
| Watershed Basics, original | 65 | 0.33 |
| Watershed Basics, improved | 78 | 0.50 |
| One Gap | 85 | 0.46 |
| Open Algebra | 90 | 0.55 |

The correlation is shown as r and updates when a point is toggled off. With all seven points r is 0.93. With Thin Material toggled off r is 0.92.

The five questions:

| # | Question | Choices | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | What is the correlation r for all seven points? | 0.43; 0.93; 1.00 | 0.93 | The plot's statistic is 0.93. |
| 2 | Which resource has the lowest gain among the three with a total of 65? | Open Unit With Errors; Locked Chemistry E-book; Watershed Basics, original | Open Unit With Errors | Its gain of 0.22 is the lowest of the three. |
| 3 | Does r = 0.93 show that raising a rubric score causes more learning? | Yes; No | No | A correlation does not show cause. |
| 4 | With Thin Material toggled off, is r still > 0.9? | Yes; No | Yes | r is 0.92. |
| 5 | Are seven resources enough to settle whether the rubric predicts learning? | Yes; No | No | Seven points can swing widely, and 20 or more are needed. |

**Provenance:** The two Watershed Basics values come from the chapter's pilot. The other five values are illustrative examples made up for this chapter, and the sim labels them "illustrative examples". The correlation is the Pearson correlation of the seven pairs as displayed.

**Rules:** r is rounded to two decimal places. Toggling a point off recomputes r from the remaining points. The sim labels the plot "illustrative data".

**Learner Activity:**

1. The learner hovers over points to see the resource names and values.
2. The learner may toggle any point off and see r change. Toggling is not scored.
3. The learner presses Quiz and answers the five questions.
4. After question 5 the sim shows the summary.

**Feedback:** 5 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can read a scatter plot and its limits." Below 4 it lists the Why text of each missed question.

**Starting State:** The scatter plot with all seven points shown, r displayed as 0.93, and the Quiz button.

**Chapter Anchors:** The chapter's table of seven resources and its correlation of 0.93 are the data and the statistic of this sim.
</details>

## Pilot Test

A **pilot test** is a small first run of a test, done to check the procedure and to learn what a larger test would need. The *Watershed Basics* test was a pilot: one class, 24 students. A pilot is not a weak version of the real test. It has its own jobs:

- **Check the procedure.** Did the assignment, the timing, and the data collection work? The pilot found that the original's quiz failed to load for two students.
- **Check the measures.** Was the post-test too easy? Three students reached 95 to 98, so the test had little room above them, and harder questions would measure the strongest students better.
- **Estimate the spread and the effect.** These guide the size of the larger test.

The estimate leads to a planning rule. Under the usual research standards, the students needed in each group is about 16 divided by *d* squared, where *d* is the effect size you want to detect. The rule is an approximation that a statistician should confirm for a real study, and it gives the figures of the Chapter 16 table.

| Effect size to detect | Students per group |
|---|---|
| 0.8, large | 25 |
| 0.5, medium | 64 |
| 0.4 | 100 |
| 0.2, small | 400 |

Do not plan on the pilot's own effect size. Its *d* of 1.03 would suggest 16 students per group (16 divided by 1.06 is about 15.1, rounded up), which is too optimistic, since pilot estimates tend to be inflated. A safer habit is to plan for about half the pilot's effect, close to 0.5, which calls for about 64 students per group.

The MicroSim below practices the planning rule.

#### Diagram: Pilot Sample Planner

<details markdown="1">
<summary>Pilot Sample Planner</summary>
Type: microsim
**sim-id:** pilot-sample-planner<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the number of students needed in each group for six effect sizes by the rule of 16 divided by d squared, rounded up, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Pilot Test, Effect Size, and Sample Size (defined in this chapter above this block or in Chapter 16).

**Evidence of Mastery:** For each effect size the learner enters the students needed per group. An answer is correct when it matches the Content table. Mastery is at least 5 of 6 correct on the first attempt. Reading the rule is exploration, not evidence.

**Misconceptions:** (1) A larger effect needs a larger sample. (2) The pilot's effect size is the right one to plan on. (3) Rounding down is acceptable.

**Instructional Rationale:** Calculating a sample size from an effect size is an Apply-level action. Six effect sizes show that the number grows quickly as the effect shrinks, and the pilot's own value shows why it is a poor planning value.

**Content:**

The rule, shown at all times: students per group = 16 / d squared, rounded up to a whole number. The rule is labeled "rule of thumb for comparing two group means under the usual research standards".

The six cases:

| # | Effect size d | Students per group | Why (shown as feedback) |
|---|---|---|---|
| 1 | 0.80 | 25 | 16 divided by 0.64 is 25. |
| 2 | 0.50 | 64 | 16 divided by 0.25 is 64. |
| 3 | 0.40 | 100 | 16 divided by 0.16 is 100. |
| 4 | 0.20 | 400 | 16 divided by 0.04 is 400. |
| 5 | 0.60 | 45 | 16 divided by 0.36 is about 44.4, which rounds up to 45. |
| 6 | 1.03 | 16 | 16 divided by 1.0609 is about 15.1, which rounds up to 16. The sim adds: "Do not plan on a pilot's own effect size." |

**Provenance:** The rule of thumb is labeled as an approximation that a statistician should confirm. The cases are illustrative examples, and the sim labels them "illustrative examples". Case 6 is the pilot's effect size.

**Rules:** The answer is the smallest whole number >= 16 divided by d squared.

**Learner Activity:**

1. The learner sees one effect size and the rule.
2. The learner enters the students per group, and the answer is committed.
3. The sim shows whether it was correct and the Why text.
4. After case 6 the sim shows the summary.

**Feedback:** 6 cases in a shuffled order, one attempt each. Correct: "Correct: [answer] students per group. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can size a larger test." Below 5 it lists the Why text of each missed case.

**Starting State:** The first case in the shuffled order, the rule, and an empty field.

**Chapter Anchors:** The chapter's table of effect sizes and group sizes contains cases 1, 2, 3, and 4, and the chapter's planning advice discusses case 6.
</details>

## Equity Consideration

An **equity consideration** is a check that a resource, and the test of it, work fairly for all the students who might use them. A result that says a version helps "students" on average can hide the fact that it helps some and leaves others out. Equity here includes students who use assistive technology, students learning English, and students without a home device or a fast connection.

Build the check into the test. Confirm before the test that every student can use both versions: captions, readable text, devices that load the content. Include a survey question about barriers, such as the second question in the pilot. Record what the teacher observes. And report with care. Chapter 16 and the section on anonymized data explain why results for groups of fewer than about ten students should not be published. In the pilot, 2 students used captions and 3 were learning English. Those groups are too small to report, so their experience comes from comments and observation and not from subgroup averages.

The pilot found equity differences of a different kind. The original version had no captions and an inaccessible quiz script, and both are barriers for some students. The improvement removed them. A fair summary says so, and it also says that the test could not measure how much those students benefited.

---

## Key Takeaways

- **Data collection** uses one procedure for both groups and a data dictionary with one row per student. Check the table for missing, out-of-range, repeated, and mislabeled values before analyzing.
- **Anonymized data** has no link to a person. Codes are not enough in a small class, so drop columns, generalize, hide small groups, and clean comments.
- A **mean score** summarizes a group, and the **difference of means** answers the hypothesis. Compare gains, report the spread, and remember that a small test can mislead.
- An **effect size** puts a difference on a common ruler. Cohen's d is the difference divided by the pooled standard deviation, with 0.2, 0.5, and 0.8 as conventional markers. Small pilots tend to overstate it.
- A **student survey** needs neutral, specific, one-idea questions. **Completion rate** and **time on task** are read with the learning gain. **Qualitative feedback** is coded into themes and counted.
- A **results summary** has seven parts and claims no more than the data allow.
- The **rubric-outcome correlation** checks whether rubric scores predict learning, using normalized gains across many resources. It shows association and not cause, and it needs far more than seven resources.
- A **pilot test** checks the procedure and the measures and estimates the size of a larger test. Plan on a smaller effect than the pilot found.
- An **equity consideration** checks that both versions work for every student and reports small groups with care.

!!! mascot-celebration "You Can Read the Evidence"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now collect and protect test data, compare two groups, size an effect, weigh what students say, and check whether the rubric predicts learning. Next comes the work of packaging and publishing an improved resource, and of training the reviewers who will keep the loop going.

[See Annotated References](./references.md)
