---
title: "Designing an A/B Test with Students"
description: "Explains how to compare an original and an improved resource with students, covering hypotheses, control and treatment groups, pre-tests and post-tests, sampling, consent, and student privacy."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 23:00:09"
version: 1.11
status: built
---

# Designing an A/B Test with Students

## Summary

Explains how to compare an original and an improved resource with students, covering hypotheses, control and treatment groups, before-and-after comparison, pre-tests and post-tests, sampling, consent, and student privacy. It tests whether the improvements help students, and relies on the improvement work in the previous chapter. After this chapter you can write a hypothesis, set up control and treatment groups, and plan a student test that respects consent and privacy.

## Concepts Covered

This chapter covers the following 17 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| A/B Test | 99 |
| Control Group | 19 |
| Treatment Group | 19 |
| Original Version | 1 |
| Improved Version | 2 |
| Before-and-After Comparison | 1 |
| Test Hypothesis | 29 |
| Outcome Measure | 28 |
| Pre-Test | 2 |
| Post-Test | 2 |
| Learning Gain | 1 |
| Random Assignment | 8 |
| Sample Size | 4 |
| Confounding Variable | 1 |
| Sampling Bias | 2 |
| Informed Consent | 26 |
| Student Privacy in Testing | 25 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Foundations of Open Educational Resources](../01-foundations-of-oer/index.md)
- [Chapter 8: Practice and Feedback](../08-practice-feedback/index.md)
- [Chapter 13: Automated Checks, Cost, and Student Privacy](../13-automated-checks-cost-privacy/index.md)
- [Chapter 15: Improving a Resource with AI Agents](../15-improving-resources-with-ai/index.md)

---

!!! mascot-welcome "Does the Better Score Mean Better Learning?"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    The last chapter raised a resource's score, and a score is only a reviewer's judgment. In this chapter you will plan a fair test with real students to find out whether the improved version helps them learn. Let's dive in and check the evidence!

Chapter 15 ended with a warning: a score gain is not a learning gain. The rubric measures the properties of a resource, such as whether it has alt text or a clear license. It cannot tell you whether a student who uses the resource learns more. Only students can tell you that, and a fair test is how you ask them.

This chapter is about *designing* the test, which is where most of the quality of a test is decided. A well-designed test on 24 students can teach you something real. A badly designed test on 240 students teaches you nothing, however carefully the numbers are added up afterward. The next chapter covers the data and the analysis. The running example is the test of *Watershed Basics*: the original, which scored 65, against the improved version, which scored 78.

## A/B Test

An **A/B test** is a comparison of two versions of something, A and B, in which different people use each version at the same time and the results are compared. The idea comes from product design, where companies show two versions of a page to different visitors and count which one works better. In education the same idea compares an original resource with an improved one, using student learning as the result. The formal research cousin of the A/B test is the randomized controlled trial. In this book the test is *manual*: you set it up, run it, and tally it yourself, with no special software.

An A/B test answers a different question from the rubric. The rubric asks, "Does this resource have the properties that make a resource good?" The A/B test asks, "Do students who use this version learn more than students who use that one?" The two questions can have different answers. A resource can gain 13 rubric points from better metadata, which no student ever sees, and teach no better. The test is how you find out.

The method has eight steps.

1. **State a hypothesis** that predicts what the improved version will do.
2. **Freeze both versions** so that they do not change during the test.
3. **Choose the outcome measure**, and a pre-test and a post-test.
4. **Get consent** and plan how student data will be protected.
5. **Assign students to the two versions by chance.**
6. **Run both groups under the same conditions.**
7. **Collect the data** with care for privacy.
8. **Compare the groups**, which is the subject of Chapter 17.

Steps 1 through 5 are design, and they fill this chapter. A test can show that, for these students and these conditions, one version did better. It cannot prove that the improved version works for all students everywhere, and a good report says so.

### Original Version

The **original version** is the resource exactly as it was before the improvements. For the test it must be frozen: the same files, saved in the version history of Chapter 4 under a label such as *v1*, and the same one that received the baseline score. If the original is quietly fixed during the test, the control group no longer uses what you said it did. Keep it available at its own address so that every student assigned to it reaches the same thing.

### Improved Version

The **improved version** is the resource after the improvement plan, frozen in the same way and labeled, for example, *v1.1*. Its change log from Chapter 15 is the list of differences between the two versions, and it should be written down before the test. *Watershed Basics v1.1* differs from *v1* in five ways: richer metadata, fuller alt text with captions, a separated quiz, explanations with a worked example and a simulation, and corrected facts and links.

Because five fixes arrive together, a test of these two versions can tell you whether the *bundle* helps students. It cannot say which fix did the work. If you need to know that, test one fix at a time, which takes more students and more time. Both versions carry CC BY 4.0, so you may give both to students and share both afterward.

| | Original version | Improved version |
|---|---|---|
| Label | v1 | v1.1 |
| Rubric total | 65 | 78 |
| Decision | Revise | Adopt |
| What changed | Nothing | Five fixes from the change log |
| License | CC BY 4.0 | CC BY 4.0 |

## Control Group

The **control group** is the group of students who use the original version. It is the yardstick for the test. Without it you could say how well students did with the improved version, and you could not say how well they would have done without the improvement. The control group answers the question, "Compared with what?"

A control group is *not* a group that receives no teaching. It is a group that receives the ordinary teaching with the original resource, which is a fully acceptable lesson. That matters for fairness. No student should be given a version that you believe will harm their learning, and a control group that uses the original is not harmed. Many teachers also offer the improved version to the control group after the test ends, so that every student benefits from the work.

For the comparison to mean anything, the control group must differ from the treatment group in one way only: the version. The same teacher, the same instructions, the same time allowed, the same outcome measure, and the same week. The rest of this chapter is largely about protecting that one-difference rule.

## Treatment Group

The **treatment group** is the group of students who use the improved version. The word *treatment* comes from medicine, where it names the thing being tested. Here the treatment is the set of improvements. The group should be about the same size as the control group, because equal groups give the most information from a given number of students.

The treatment group gets nothing extra beyond the improved resource. It gets no longer time, no additional help from the teacher, and no review session, since any of those would be a second difference between the groups. In the *Watershed Basics* pilot, a class of 24 students is split into a control group of 12 and a treatment group of 12.

| | Control group | Treatment group |
|---|---|---|
| Students | 12 | 12 |
| Version | Original, v1 | Improved, v1.1 |
| Teacher | The same teacher | The same teacher |
| Time allowed | The same two class periods | The same two class periods |
| Instructions | The same script | The same script |
| Pre-test and post-test | The same | The same |

## Test Hypothesis

A **test hypothesis** is a prediction, written down before the test, about what the improved version will do for students compared with the original. It turns a hope, such as "the new version is better", into a statement that data can support or fail to support. Writing it first protects you from the common trap of looking at the results and then deciding what you were trying to show.

A good hypothesis has five properties.

- **Specific:** it names the students, the versions, and the measure.
- **Measurable:** the measure is something you can count or score.
- **Directional:** it says which version should do better.
- **Sized:** it says how large a difference would matter.
- **Falsifiable:** some result would show it to be wrong.

The hypothesis for the *Watershed Basics* pilot is: "Grade 6 students who use the improved version will have a mean learning gain at least 5 percentage points larger than students who use the original." The size, 5 points, is a teaching choice that marks the smallest difference a teacher would care about. The statement that the two versions do not differ is the *null hypothesis*, and Chapter 17 shows how data are weighed against it.

| Weak hypothesis | Why it is weak | Strong hypothesis |
|---|---|---|
| The improved version is better. | "Better" has no measure | Students on the improved version will score higher on the post-test |
| Students will like it. | No comparison and no measure | More students will rate the improved version 4 or 5 on a 5-point scale |
| Every student will learn more. | Cannot be shown for every student | The mean gain will be larger in the treatment group |

The MicroSim below practices the skill. It shows eight statements, and for each one you decide whether it can be tested as written.

#### Diagram: Hypothesis Sharpener

<details markdown="1">
<summary>Hypothesis Sharpener</summary>
Type: microsim
**sim-id:** hypothesis-sharpener<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight statements is a testable hypothesis for a student A/B test or is not testable as written, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Test Hypothesis, A/B Test, Original Version, Improved Version (all defined in this chapter above this block).

**Evidence of Mastery:** For each statement the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the five properties is exploration, not evidence.

**Misconceptions:** (1) A hypothesis only needs to state what you hope. (2) A statement about the rubric score is a statement about students. (3) A hypothesis can claim that every student will benefit.

**Instructional Rationale:** Judging a hypothesis against the five properties is an Evaluate-level action that every test design needs. Four testable and four untestable statements, each failing in a different way, teach the learner to look for the measure, the comparison, and the claim of every.

**Content:**

The two bins: Testable as written, and Not testable as written.

The five properties, available on demand: specific, measurable, directional, sized, falsifiable.

The eight statements (all made up, for the Watershed Basics pilot):

| # | Statement | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | Students will like the improved version. | Not testable as written | It has no comparison and no measure of liking. |
| 2 | Grade 6 students who use the improved version will score at least 5 points higher on the 20-question post-test than students who use the original. | Testable as written | It names the students, the measure, the direction, and the size. |
| 3 | The improved version is better. | Not testable as written | "Better" has no measure. |
| 4 | A larger share of students will finish the improved version's quiz than the original's, measured by the count of completed quizzes. | Testable as written | The measure is a count, and the direction is stated. |
| 5 | The improved version will raise the rubric score. | Not testable as written | The rubric score is set by reviewers, so the statement does not test an effect on students. |
| 6 | Students who use the improved version will have a larger learning gain, post-test minus pre-test, than students who use the original. | Testable as written | Learning gain is defined, and the direction is stated. |
| 7 | Every student will learn more from the improved version. | Not testable as written | A claim about every student cannot be shown. |
| 8 | Students who use the improved version will spend less time on the task and score the same or higher on the post-test. | Testable as written | Time on task and post-test score are both measures, and the direction is stated. |

**Provenance:** The statements are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The five properties follow the chapter section "Test Hypothesis".

**Rules:** Each statement has exactly one correct bin, four per bin.

**Learner Activity:**

1. The learner sees one statement and the two bins, and may open the five properties. Opening them does not change the score.
2. The learner places the statement in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After statement 8 the sim shows the summary.

**Feedback:** 8 statements in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can tell a testable hypothesis from a hope." Below 7 it lists the Why text of each missed statement.

**Starting State:** The first statement in the shuffled order and the two bins. The question shown is "Can this be tested as written?"

**Chapter Anchors:** The chapter lists five properties of a good hypothesis, shows a table of weak and strong hypotheses, and states the hypothesis for the Watershed Basics pilot.
</details>

## Outcome Measure

An **outcome measure** is the thing you measure to decide which version did better. It is the answer to the question, "What would I see in the students if the improved version worked?" For a test of learning, the main outcome measure is a score on a test of the skills the resource teaches. Others, such as how many students finish and how long they take, add detail, and Chapter 17 uses them.

Choose one *primary* outcome in advance, and name it in the hypothesis. A test that measures twenty things and then reports whichever came out well is a test that has found noise.

A good outcome measure has five properties.

| Property | What it means | In the *Watershed Basics* pilot |
|---|---|---|
| Aligned | It measures the learning outcomes the resource targets, as in Chapter 6 | The test covers all three outcomes |
| Fair to both versions | It is not built from one version's own quiz | A separate 20-question test, not the resource's quiz |
| Reliable | It has enough questions to give a steady score | 20 questions |
| Right difficulty | Not so easy that everyone scores high, nor so hard that everyone scores low | Trial questions were tried before the test |
| Scored the same way | The same key and, if possible, a scorer who does not know the group | An answer key, with names hidden |

The second property deserves attention. The improved version of *Watershed Basics* has extra explanations and a worked example. If the post-test were the resource's own quiz, the treatment group would have practiced exactly the questions on the test. That would measure rehearsal and not learning.

### Pre-Test

A **pre-test** is a test given before students use the resource, to find out what they already know. It does two jobs. It shows whether the two groups started at the same level, and it provides the starting score from which learning is measured. Without it, a group that scores higher at the end may simply have known more at the start. Use a pre-test that covers the same outcomes as the post-test, and tell students that it is for learning about the resource and not for a grade.

### Post-Test

A **post-test** is a test given after students use the resource, to find out what they learned. It should cover the same outcomes as the pre-test, and it should be given under the same conditions to both groups, at the same time after the lesson. A test given the same day shows immediate learning. A test given a week later shows what students kept. The choice belongs in the plan, and the same choice applies to both groups. Using the same questions on the pre-test and the post-test can inflate scores through memory, so many tests use two equivalent forms of the same length.

### Learning Gain

**Learning gain** is the amount a student's score rose from the pre-test to the post-test. The simplest form is the *raw gain*: the post-test score minus the pre-test score, in percentage points. A student who scores 40 and then 70 has a raw gain of 30 points.

Raw gain has a weakness. A student who starts at 90 can gain at most 10 points, while a student who starts at 20 can gain 80. The *normalized gain* fixes this by comparing the gain to the room available:

normalized gain = (post - pre) / (100 - pre)

The student who goes from 40 to 70 has a normalized gain of 30 divided by 60, which is 0.50. A student who goes from 90 to 95 has a raw gain of only 5 points, and a normalized gain of 5 divided by 10, which is also 0.50. Both students closed half of the gap that was open to them. When the pre-test is 100, the normalized gain is undefined, since there was no room to gain.

The MicroSim below practices both forms.

#### Diagram: Learning Gain Calculator

<details markdown="1">
<summary>Learning Gain Calculator</summary>
Type: microsim
**sim-id:** learning-gain-calculator<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the raw gain and the normalized gain for six students from their pre-test and post-test scores, with at least 5 of 6 cases fully correct on the first attempt.

**Prerequisites:** Pre-Test, Post-Test, Learning Gain (all defined in this chapter above this block).

**Evidence of Mastery:** For each case the learner enters the raw gain and the normalized gain. A case is fully correct when both match the Content table. Normalized gain is rounded to two decimal places, and the learner enters Undefined when the pre-test is 100. Mastery is at least 5 of 6 cases fully correct on the first attempt. Reading the formulas is exploration, not evidence.

**Misconceptions:** (1) A larger raw gain always means more learning. (2) A negative gain cannot happen. (3) The normalized gain is always defined.

**Instructional Rationale:** Calculating a gain from two scores is an Apply-level action. Cases with different starting points, a loss, and a perfect pre-test show why the normalized gain exists and where it fails.

**Content:**

The formulas, shown at all times: raw gain = post - pre. Normalized gain = (post - pre) / (100 - pre). The normalized gain is undefined when pre = 100.

The six cases (all made up, scores out of 100):

| # | Pre-test | Post-test | Raw gain | Normalized gain | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | 40 | 70 | 30 | 0.50 | 30 divided by 60 is 0.50. |
| 2 | 60 | 80 | 20 | 0.50 | 20 divided by 40 is 0.50. |
| 3 | 20 | 50 | 30 | 0.38 | 30 divided by 80 is 0.375, which rounds to 0.38. |
| 4 | 90 | 95 | 5 | 0.50 | 5 divided by 10 is 0.50, the same share of the room as case 1. |
| 5 | 80 | 70 | -10 | -0.50 | The score fell, so both gains are negative. |
| 6 | 100 | 100 | 0 | Undefined | There was no room to gain. |

**Provenance:** The scores are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The normalized gain follows the chapter section "Learning Gain".

**Rules:** Raw gain is an integer and may be negative. Normalized gain is rounded to two decimal places with 0.375 rounded to 0.38. A case is fully correct only when both entries match.

**Learner Activity:**

1. The learner sees one pre-test and post-test pair and the formulas.
2. The learner enters the raw gain and the normalized gain, and presses Check.
3. The sim shows which entries were correct and the Why text.
4. After case 6 the sim shows the summary.

**Feedback:** 6 cases in a shuffled order, one attempt each. Correct: "Correct: raw gain [raw], normalized gain [normalized]. [Why]". Incorrect: "Not quite. The raw gain is [raw] and the normalized gain is [normalized]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can calculate a learning gain." Below 5 it lists the Why text of each missed case.

**Starting State:** The first case in the shuffled order, the formulas, and empty fields.

**Chapter Anchors:** The chapter's worked examples are cases 1 and 4, which both give a normalized gain of 0.50.
</details>

### Before-and-After Comparison

A **before-and-after comparison** looks at one group's scores before and after using a single version. It has no second group. A teacher gives a pre-test, teaches the improved lesson, gives a post-test, and sees a gain of 18 points. It is tempting to call this evidence that the lesson works.

It is weak evidence, because anything that happened between the two tests can explain the gain: the students were also learning in other classes, they had seen the test questions before, and they simply got older. Without a control group you cannot separate the effect of the lesson from the effect of time. A before-and-after comparison is useful when no second group is possible, and a report should name that limit. The A/B test is stronger because both groups have the same time, the same other classes, and the same test, so those effects cancel when you compare the groups' gains.

## Random Assignment

**Random assignment** is the use of chance to decide which version each student receives. Flip a coin, draw a slip, or sort a column of random numbers: the point is that neither the teacher nor the student chooses. Chance matters because students differ in ways you cannot see and cannot measure, such as motivation, home support, and sleep. Chance spreads those differences across the two groups, so that on average the groups are alike before the lesson begins.

The alternatives are worse. If students pick their version, the keenest ones may pick the new one. If the teacher picks, the choice may favor the students the teacher expects to succeed. If the two classes in different periods get different versions, the periods differ in many ways.

The simplest method uses a spreadsheet. List the student codes in a column, put a random number from the RAND function beside each, sort by the random column, and give the top half the improved version. A better method for small classes is *blocked* random assignment. Give the pre-test first, sort the students by their scores, pair up neighbors, and flip a coin within each pair to decide who gets which version. Each pair then contributes one student to each group, which keeps the groups close in starting level.

Random assignment balances the groups *on average*, and a small class can still be unlucky. Take the class of 24 students in the pilot, with made-up pre-test scores that range from 22 to 78 and average 51.9. The table compares three ways of forming two groups of 12. The simulated figures come from 20,000 random assignments of this class, computed for this chapter.

| Method | How groups are formed | Gap between the groups' pre-test averages |
|---|---|---|
| Students choose | The 12 highest scorers choose the improved version | 23.8 points, built in |
| Simple random assignment | Each student is placed by chance | Median about 4 points; 95 percent of splits within 12 points; 42 percent of splits more than 5 points apart |
| Blocked random assignment | Pairs matched on the pre-test, coin flip within each pair | Median about 0.6 points; 95 percent of splits within 1.6 points; the largest gap 2.6 points |

Choice builds a large imbalance into the test before the lesson starts. Simple random assignment usually gives a small gap and sometimes gives a large one. Blocked assignment keeps the gap small every time, and it needs the pre-test scores before assigning. Whichever method you use, record the pre-test averages of the two groups, and compare gains and not only post-test scores.

!!! mascot-tip "Pre-Test, Pair, Then Flip"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    When a class is small, give the pre-test first, sort the scores, pair neighbors, and flip a coin inside each pair. It takes ten minutes and keeps luck from stacking the groups.

The MicroSim below lets you see the difference for yourself by forming the groups again and again.

#### Diagram: Group Assignment Lab

<details markdown="1">
<summary>Group Assignment Lab</summary>
Type: microsim
**sim-id:** group-assignment-lab<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** compare<br/>
**Learning Objective:** The learner will compare how three assignment methods balance two groups of 12 students on their pre-test averages, and answer 4 of 4 questions about the methods, with at least 3 of 4 correct on the first attempt.

**Prerequisites:** Random Assignment, Pre-Test, Control Group, Treatment Group (all defined in this chapter above this block).

**Evidence of Mastery:** The learner answers four questions after running the methods. An answer is correct when it matches the Correct answer column in Content. Mastery is at least 3 of 4 correct on the first attempt. Running the methods is exploration, not evidence.

**Misconceptions:** (1) Random assignment always gives equal groups. (2) Letting students choose is fair because it respects their preferences. (3) Blocked assignment can be done before the pre-test.

**Instructional Rationale:** Comparing methods on the same class is an Analyze-level action. Running each method many times shows that random assignment works on average, varies from run to run, and is improved by blocking.

**Content:**

The class: 24 students with these made-up pre-test scores, out of 100: 22, 28, 31, 35, 38, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 58, 60, 62, 64, 66, 68, 70, 74, 78. The average of all 24 is 51.875.

The three methods:

| Method | What the sim does |
|---|---|
| Students choose | The 12 highest scores form the improved group and the 12 lowest form the original group. Every press gives the same result. |
| Simple random assignment | Each press forms two groups of 12 by a fresh random shuffle of the 24 students. |
| Blocked random assignment | The sim sorts the scores, pairs neighbors (22 with 28, 31 with 35, and so on up to 74 with 78), and decides by a fresh coin flip within each pair which student goes to each group. |

For every press the sim shows the two group averages and the absolute difference between them, and keeps a running list of the differences for each method.

Facts shown after at least 20 presses of a method, from 20,000 simulated assignments of this class:

| Method | Difference between group averages |
|---|---|
| Students choose | 23.75 points: group averages of 63.75 and 40.0 |
| Simple random assignment | Median 4.25; 95 percent of splits are <= 11.9; 42 percent of splits are > 5 |
| Blocked random assignment | Median 0.58; 95 percent of splits are <= 1.6; the largest is 2.6 |

The four questions:

| # | Question | Choices | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Which method builds the largest imbalance into the groups? | Students choose; Simple random assignment; Blocked random assignment | Students choose | The 12 highest scorers form one group, so the averages differ by 23.75. |
| 2 | Does simple random assignment guarantee equal pre-test averages? | Yes; No | No | Some splits differ by more than 5 points. |
| 3 | What must you know before you can use blocked random assignment? | The post-test scores; Each student's pre-test score; The teacher's preference | Each student's pre-test score | The scores are needed to sort and pair the students. |
| 4 | Which method gave the smallest typical difference? | Students choose; Simple random assignment; Blocked random assignment | Blocked random assignment | Its median difference is 0.58. |

**Provenance:** The scores are made up for this chapter, and the sim labels them "illustrative examples". The simulated figures were computed for this class from 20,000 random assignments with a fixed seed, and the sim labels them "simulation results for this class".

**Rules:** The group sizes are always 12 and 12. A press never changes the class. The facts appear only after at least 20 presses of the method, so that the learner sees the spread before reading the summary.

**Learner Activity:**

1. The learner picks a method and presses Form groups at least 20 times for each random method.
2. After each press the learner sees the two averages and their difference.
3. The learner presses Quiz and answers the four questions.
4. After question 4 the sim shows the summary.

**Feedback:** 4 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 4 correct on the first attempt". At 3 or more it adds "You can compare ways to form groups." Below 3 it lists the Why text of each missed question.

**Starting State:** The class table, the Students choose method selected, and no presses yet.

**Chapter Anchors:** The chapter's table of three methods uses the same class and the same figures as this sim.
</details>

## Sample Size

**Sample size** is the number of students in the test. A larger sample gives a steadier answer, because chance fluctuations in who is in each group average out. A small sample gives a noisy one: a few unusually strong or weak students can swing the result.

The practical rule is that the smaller the difference you hope to find, the more students you need. The table gives rough guidance for comparing the averages of two groups under the usual research standards. The sizes are rules of thumb, and a real study should confirm them with a statistician. Chapter 17 defines large, medium, and small differences more exactly.

| Students in each group | What the test can tell you |
|---|---|
| 5 to 10 | A pilot only: it checks the procedure and the measure |
| About 25 | A large difference, and it may miss a medium one |
| About 65 | A medium difference |
| About 400 | A small difference |

The *Watershed Basics* test is a pilot with 12 students in each group. That is enough to find out whether the test runs smoothly, whether the post-test is too easy or too hard, and how widely scores vary. It is not enough to prove that the improved version works. A pilot's purpose is to decide whether a larger test is worth running, and to say honestly that its own result is suggestive and not conclusive.

## Confounding Variable

A **confounding variable** is a factor other than the version that differs between the groups and could explain the result. If the treatment group did better and also had a different teacher, you cannot tell whether the improved version or the teacher made the difference. The two are tangled together, or confounded.

The cure is the one-difference rule from the section on the control group: arrange everything except the version to be the same, and let random assignment handle what you cannot arrange. The table lists the usual confounders and the defense against each.

| Confounder | How it misleads | The defense |
|---|---|---|
| Different teachers | One teacher's enthusiasm lifts one group | One teacher for both groups |
| Different times of day | Students are more alert at one time | Both groups at the same time |
| Extra help | One group gets a review or hints | The same script and help for both |
| Different tests | The versions are measured in different ways | The same test and key for both |
| Student choice | Motivated students choose one version | Random assignment |

!!! mascot-thinking "Ask What Else Is Different"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Before you trust any difference between groups, list everything that was different besides the version. If the list is not empty, one of those things may be the real cause.

The MicroSim below practices the hunt. It describes eight test setups, and for each one you decide whether a confounder is present and name it.

#### Diagram: Confounder Finder

<details markdown="1">
<summary>Confounder Finder</summary>
Type: microsim
**sim-id:** confounder-finder<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine eight test setups and decide whether a confounding variable is present and, if so, name its source, with at least 7 of 8 setups fully correct on the first attempt.

**Prerequisites:** Confounding Variable, Control Group, Treatment Group, Random Assignment (all defined in this chapter above this block).

**Evidence of Mastery:** For each setup the learner chooses Confounder present or No confounder, and when a confounder is present picks its source from the list. A setup is fully correct when the choice and the source both match the Content table. Mastery is at least 7 of 8 setups fully correct on the first attempt. Reading the confounder table is exploration, not evidence.

**Misconceptions:** (1) A large sample removes a confounder. (2) Random assignment is unnecessary when the groups look alike. (3) A confounder always makes the improved version look better.

**Instructional Rationale:** Examining a setup for a second difference between groups is an Analyze-level action. Setups that differ in one way each, and two with no confounder, teach the learner to name the difference and to know when to stop looking.

**Content:**

The two choices: Confounder present, No confounder. The sources: Teacher, Time of day, Extra help, Different tests, Student choice, Different period of the year.

The eight setups (all made up):

| # | Setup | Correct choice | Source | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | The morning section uses the original, and the afternoon section uses the improved version. | Confounder present | Time of day | Alertness and the students in each section differ, so the version is not the only difference. |
| 2 | One teacher teaches both groups with the same script in the same week, students are assigned by random number, and both groups take the same test. | No confounder | None | The groups differ only in version. |
| 3 | The treatment group also gets a 10-minute review before the post-test. | Confounder present | Extra help | The review is a second difference. |
| 4 | The control group is tested in September and the treatment group in March. | Confounder present | Different period of the year | Students learn more in the intervening months. |
| 5 | Students choose which version to use. | Confounder present | Student choice | Motivated students may choose the new version. |
| 6 | The improved version is taught by a teacher who is excited about it, and the original by a teacher who is not. | Confounder present | Teacher | The teacher's attitude is a second difference. |
| 7 | The treatment group takes the resource's own quiz as the post-test, and the control group takes a separate test. | Confounder present | Different tests | The groups are measured differently. |
| 8 | Both groups use their version for the same time, in the same room, with the same instructions, and a coin flip assigns each student. | No confounder | None | The groups differ only in version. |

**Provenance:** The setups are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The sources follow the chapter section "Confounding Variable".

**Rules:** Each setup has exactly one correct choice. Six have a confounder and two do not. Each of the six sources appears once.

**Learner Activity:**

1. The learner sees one setup.
2. The learner chooses Confounder present or No confounder. If a confounder is present, the learner also picks the source.
3. The sim shows whether the choice and the source were correct, and the Why text.
4. After setup 8 the sim shows the summary.

**Feedback:** 8 setups in a shuffled order, one attempt each. Correct: "Correct: [choice], [source]. [Why]". Incorrect: "Not quite. The answer is [choice], [source]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can find what else is different." Below 7 it lists the Why text of each missed setup.

**Starting State:** The first setup in the shuffled order and the two choices. The question shown is "Is anything besides the version different between the groups?"

**Chapter Anchors:** The chapter's table of confounders lists teacher, time of day, extra help, different tests, and student choice. The sim adds a different period of the year.
</details>

## Sampling Bias

**Sampling bias** is a distortion that arises when the students in the test are not like the students you want to learn about, or when the students who finish are not like the ones who started. The result is true for the group that was tested and misleading about everyone else.

Four forms are common.

- **Volunteer bias:** only students who volunteer or return a form take part, and volunteers tend to be more motivated.
- **Convenience sampling:** you test the class that is easiest to reach and then speak as if it represented all students.
- **Attrition:** students drop out unevenly, so the scores that remain come from the students who stayed.
- **Exclusion:** some students cannot take part, for instance because the online version needs a device that they do not have.

Exclusion is also an equity problem. If students who use assistive technology, or who lack a home computer, cannot use one of the versions, the test measures only the students that the version suits. Chapter 17 comes back to this under equity.

The defenses are practical. Invite every student in the class, and do not select. Record how many were invited, how many agreed, and how many finished each group. Offer both versions in forms that every student can use. And report who took part, so that readers can decide how far the result applies to their students.

The MicroSim below practices naming the bias.

#### Diagram: Sampling Bias Spotter

<details markdown="1">
<summary>Sampling Bias Spotter</summary>
Type: microsim
**sim-id:** sampling-bias-spotter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** differentiate<br/>
**Learning Objective:** The learner will differentiate volunteer bias, convenience sampling, attrition, exclusion, and no concern by sorting each of six recruitment scenarios, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Sampling Bias, Sample Size, Treatment Group, Control Group (all defined in this chapter above this block).

**Evidence of Mastery:** For each scenario the learner commits one of five bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the four forms is exploration, not evidence.

**Misconceptions:** (1) Bias only occurs when the researcher is dishonest. (2) A volunteer is as good as a randomly chosen student. (3) Dropping students who did not finish is harmless.

**Instructional Rationale:** Differentiating the forms of sampling bias is an Analyze-level action. Scenarios that each fail in one way, and two that are sound, teach the learner to ask who is missing and why.

**Content:**

The five bins: Volunteer bias, Convenience sampling, Attrition, Exclusion, No concern.

The six scenarios (all made up):

| # | Scenario | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | A note is sent home, and only students who return a signed form take part. | Volunteer bias | Students who return forms tend to be more motivated. |
| 2 | Only the teacher's honors class is tested, and the results are reported for all Grade 6 students. | Convenience sampling | One easy-to-reach class does not represent the grade. |
| 3 | Nine students in the treatment group leave the test because the simulation would not load on their devices, and their scores are dropped. | Attrition | The students who remain are the ones whose devices worked. |
| 4 | The improved version needs a laptop, so students without laptops are left out. | Exclusion | The test cannot speak for students who could not use it. |
| 5 | Every student in the grade is invited, 24 of 25 in each section take part, and the reasons for the missing students are recorded. | No concern | Nearly everyone is included and the gaps are recorded. |
| 6 | Three schools of different sizes are invited, and every student with consent takes part. | No concern | Participation does not depend on motivation or access. |

**Provenance:** The scenarios are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The four forms follow the chapter section "Sampling Bias".

**Rules:** Each scenario has exactly one correct bin. Four scenarios have one of the four forms each, and two have no concern.

**Learner Activity:**

1. The learner sees one scenario and the five bins, and may open the four forms. Opening them does not change the score.
2. The learner places the scenario in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After scenario 6 the sim shows the summary.

**Feedback:** 6 scenarios in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can spot who is missing from a test." Below 5 it lists the Why text of each missed scenario.

**Starting State:** The first scenario in the shuffled order and the five bins. The question shown is "Who is missing, and why?"

**Chapter Anchors:** The chapter lists four forms of sampling bias: volunteer bias, convenience sampling, attrition, and exclusion. The sim adds two cases with no concern.
</details>

### The Design on One Page

The poster below pulls the whole design onto one picture. It follows the students from the pool, through random assignment, into the two groups, through the same tests, to the comparison.

#### Diagram: A/B Test Anatomy

<details markdown="1">
<summary>A/B Test Anatomy</summary>
Type: infographic
**sim-id:** ab-test-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the six parts of an A/B test design from a description of how each looks, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** A/B Test, Control Group, Treatment Group, Random Assignment, Pre-Test, Post-Test, Outcome Measure (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 5 of 6 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) The two groups are formed by choice. (2) Only the post-test is needed. (3) The control group gets no lesson.

**Instructional Rationale:** Identifying the parts of a design is a Remember-level task, and a picture of the whole flow from pool to comparison gives each part a place. The quiz asks the learner to recognize a part by its look.

**Content:**

The illustration is a text-free flat drawing read from left to right. At the left is a circle of 24 identical small figures. An arrow leaves the circle and passes through a pair of dice. Beyond the dice the figures split into two equal clusters, an upper cluster of 12 holding a page with one dot and a lower cluster of 12 holding a page with two dots. Each cluster has a pencil-and-paper icon before it and another after it. At the right is a balance scale with a cluster on each pan. The six markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Student pool | The circle of identical figures at the left. | The students invited to take part. | Invite every student in the class, and record who agrees. |
| 2 | Random assignment | The pair of dice on the arrow. | Chance decides who gets which version. | Sort by the pre-test, pair neighbors, and flip a coin inside each pair. |
| 3 | Control group | The upper cluster holding the page with one dot. | The students who use the original version. | Treat them exactly like the other group in every way but the version. |
| 4 | Treatment group | The lower cluster holding the page with two dots. | The students who use the improved version. | Give them nothing extra beyond the improved version. |
| 5 | Pre-test and post-test | The pencil-and-paper icons before and after each cluster. | The same tests, given to both groups. | Use equivalent forms and the same conditions for both groups. |
| 6 | Comparison | The balance scale at the right. | The two groups' learning gains are compared. | Compare the gains and not only the post-test scores. |

**Provenance:** The six parts follow the chapter sections "A/B Test", "Random Assignment", "Control Group", "Treatment Group", "Pre-Test", "Post-Test", and "Outcome Measure". The illustration is synthetic, and the sim labels it "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 6 in the order of the table, from left to right.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 6 hints the sim shows the summary.

**Feedback:** 6 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read the design of an A/B test." Below 5 it lists the labels of the missed parts.

**Starting State:** The illustration with six numbered markers, explore mode active, and the prompt "Hover a marker to see a part of the design."

**Chapter Anchors:** The chapter's eight-step method and its sections on groups, assignment, and tests describe the same six parts.
</details>

## Informed Consent

**Informed consent** is a person's agreement to take part in a test, given freely after they understand what taking part involves. Students in a test are not just data. They are children and young people whose time, learning, and information are being used, and they and their families have a right to decide. For students under 18, a parent or guardian gives permission, and the student gives *assent*, which is agreement in words that the student can understand.

Valid consent has these parts.

| Part | What the letter says |
|---|---|
| Purpose | Why the test is being done, in plain words |
| What students do | Which version, which tests, how long |
| What data is collected | Which scores and which information, and no more than needed |
| Risks and benefits | What could go wrong, and what may be gained, without promises |
| Voluntary | Taking part is a choice, and saying no has no penalty |
| Right to withdraw | A student may stop at any time without penalty |
| Confidentiality | Who sees the data, and how it is kept |
| Keeping and sharing | How long the data is kept, and whether results are shared |
| Contact | A person to ask, with a way to reach them |

Three practical rules follow. Consent comes *before* any data is collected, and not after. Declining must cost the student nothing: no grade penalty, no loss of access, and an equally good alternative activity during the test. And the test needs approval from the school or district before it starts. Rules differ between schools, districts, and countries, and some require review by an ethics board for research with students. This book does not give legal advice, so ask your administrator or privacy officer what applies to you.

!!! mascot-warning "Consent Comes Before the First Score"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Do not run the pre-test and send the form afterward. Anything collected before consent is data you may not be allowed to use. Get the answer first.

The MicroSim below practices reading a consent letter. It shows eight sentences from drafts, and for each one you decide whether it belongs in a good letter.

#### Diagram: Consent Letter Checker

<details markdown="1">
<summary>Consent Letter Checker</summary>
Type: microsim
**sim-id:** consent-letter-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight sentences from draft consent letters is acceptable or a problem, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Informed Consent, Sampling Bias (both defined in this chapter above this block).

**Evidence of Mastery:** For each sentence the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the consent parts is exploration, not evidence.

**Misconceptions:** (1) A promise of a better grade encourages participation. (2) Participation can be required if the activity is part of class. (3) More data is always better.

**Instructional Rationale:** Judging a sentence against the parts of valid consent is an Evaluate-level action. Sentences that pressure, over-collect, or over-share, mixed with sound ones, teach the learner what a letter must and must not say.

**Content:**

The two bins: Acceptable, and Problem.

The eight sentences (all made up, for the Watershed Basics pilot):

| # | Sentence from a draft letter | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | Your child will use one of two versions of a lesson on watersheds, and a computer will choose which version by chance. | Acceptable | It states what students do and that assignment is random. |
| 2 | Taking part will raise your child's science grade. | Problem | It promises a benefit that the test cannot promise, and it ties participation to the grade. |
| 3 | Taking part is voluntary. Your child may stop at any time, and nothing will happen to their grade. | Acceptable | It states that participation is voluntary and withdrawal is free. |
| 4 | All students must take part, and those who decline will lose participation points. | Problem | It forces participation and penalizes refusal. |
| 5 | We will collect your child's name, birthdate, home address, and phone number with every test. | Problem | It collects personal information that the test does not need. |
| 6 | Scores are stored under a code number. Names are kept in a separate locked file that only the teacher can open, and the file will be deleted on 2027-06-30. | Acceptable | It states how data is protected and when it is deleted. |
| 7 | Results may be shared with any company that wants them. | Problem | It allows unlimited sharing of student information. |
| 8 | Questions about the test may be sent to the teacher at the school office or to the district research contact. | Acceptable | It gives a way to reach a person. |

**Provenance:** The sentences are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The consent parts follow the chapter section "Informed Consent". The sim adds the note "check your school's rules".

**Rules:** Each sentence has exactly one correct bin, four per bin.

**Learner Activity:**

1. The learner sees one sentence and the two bins, and may open the table of consent parts. Opening it does not change the score.
2. The learner places the sentence in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After sentence 8 the sim shows the summary.

**Feedback:** 8 sentences in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can read a consent letter critically." Below 7 it lists the Why text of each missed sentence.

**Starting State:** The first sentence in the shuffled order and the two bins. The question shown is "Does this sentence belong in a good consent letter?"

**Chapter Anchors:** The chapter's table of consent parts and its three practical rules are the basis of the sentences.
</details>

## Student Privacy in Testing

**Student privacy in testing** is the set of practices that keep information about students safe while a test is run and afterward. Chapter 13 explained that the work of reviewing resources needs no student data, and that an A/B test does. This is where the rules for that data are set.

Six practices cover most of the risk.

1. **Collect only what the question needs.** To compare gains you need a version label, a pre-test score, a post-test score, and a grade level. You do not need a name, a birthdate, or a home address in the data.
2. **Use a code in place of a name.** Give each student a code such as S01. Keep a key that links codes to names in a separate, locked file, and give the data file only the codes.
3. **Store data in an approved place.** Use storage that the school or district approves, with access limited to the people who need it.
4. **Keep it only as long as needed.** Set a deletion date before the test, state it in the consent letter, and delete the data and the key on that date.
5. **Report in groups.** Publish averages, and do not publish an individual's score. Many agencies hide results for groups smaller than a set size, such as 10, so follow your district's rule.
6. **Keep identifiable data away from AI agents.** Do not paste student names, scores tied to names, or free-text answers that name a student into an agent unless the school has approved that agent for that use. Use codes, and remove names from written answers first.

Laws add to these practices. In the United States, FERPA covers student education records, as Chapter 13 explained, and the law known as COPPA can apply to online tools that collect personal information from children under 13. The laws differ by place and by tool, so check with your school's privacy officer before you collect anything.

| Stage | What is held | Where | Who sees it |
|---|---|---|---|
| Collect | Code, version, pre-test, post-test | The approved school system | The teacher |
| Store | The data file, and the key in a separate file | Two locked locations | The teacher and the data owner |
| Analyze | Codes and scores only | The teacher's computer, or an approved tool | The teacher |
| Report | Group averages, with small groups hidden | The published report | The public |
| Delete | Nothing remains | The date stated in the letter | No one |

The MicroSim below practices the first two practices. It shows ten possible data items, and for each one you decide whether to collect it, replace it with a code, or not collect it.

#### Diagram: Privacy Data Sorter

<details markdown="1">
<summary>Privacy Data Sorter</summary>
Type: microsim
**sim-id:** privacy-data-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the data-minimization practices to ten possible data items by sorting each into Collect, Replace with a code, or Do not collect, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Student Privacy in Testing, Informed Consent, Pre-Test, Post-Test (all defined in this chapter above this block).

**Evidence of Mastery:** For each item the learner commits one of three bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the six practices is exploration, not evidence.

**Misconceptions:** (1) More data makes a better test. (2) Replacing a name with a code makes the key unnecessary to protect. (3) A birthdate is needed to know a student's grade level.

**Instructional Rationale:** Sorting data items by what the question needs is an Apply-level use of data minimization. Ten items that cover the scores, the identifiers, and the contact details teach the learner to ask whether each item answers the research question.

**Content:**

The three bins: Collect (keep it in the data file), Replace with a code (keep it only in the separate key file), Do not collect.

The ten items (all for the Watershed Basics pilot):

| # | Data item | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | Pre-test score | Collect | The gain cannot be computed without it. |
| 2 | Post-test score | Collect | The gain cannot be computed without it. |
| 3 | Which version the student used | Collect | The comparison depends on it. |
| 4 | Grade level | Collect | It describes the sample without identifying a student. |
| 5 | Student name | Replace with a code | The name belongs only in the separate key file. |
| 6 | School student ID number | Replace with a code | The ID identifies the student, so only a code goes in the data. |
| 7 | Email address | Do not collect | The test does not need it. |
| 8 | Home address | Do not collect | The test does not need it. |
| 9 | Birthdate | Do not collect | Grade level answers the question without it. |
| 10 | Photograph of the student working | Do not collect | It identifies the student and the test does not need it. |

**Provenance:** The items are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The practices follow the chapter section "Student Privacy in Testing". The sim adds the note "your school's rules decide".

**Rules:** Each item has exactly one correct bin. Four items are Collect, two are Replace with a code, and four are Do not collect.

**Learner Activity:**

1. The learner sees one item and the three bins, and may open the six practices. Opening them does not change the score.
2. The learner places the item in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After item 10 the sim shows the summary.

**Feedback:** 10 items in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This item belongs in [bin]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can collect only what the test needs." Below 9 it lists the Why text of each missed item.

**Starting State:** The first item in the shuffled order and the three bins. The question shown is "Does the test need this item, and in what form?"

**Chapter Anchors:** The chapter's first two practices are to collect only what the question needs and to use a code in place of a name. The sim applies both.
</details>

## Reviewing a Test Plan

The last MicroSim puts the whole chapter together. It shows a draft plan for a test, one section at a time, and for each section you decide whether it is sound or has a flaw.

#### Diagram: Test Plan Reviewer

<details markdown="1">
<summary>Test Plan Reviewer</summary>
Type: microsim
**sim-id:** test-plan-reviewer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** critique<br/>
**Learning Objective:** The learner will critique the eight sections of a draft test plan, deciding for each whether it is sound or flawed, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Test Hypothesis, Control Group, Treatment Group, Random Assignment, Outcome Measure, Sample Size, Confounding Variable, Informed Consent, Student Privacy in Testing (all defined in this chapter above this block).

**Evidence of Mastery:** For each section the learner commits Sound or Flawed. A verdict is correct when it matches the Correct verdict column in Content. When the verdict is Flawed, the learner also names the flaw from the list, and the name is checked in the feedback. Mastery is at least 7 of 8 verdicts correct on the first attempt. Reading the chapter summary is exploration, not evidence.

**Misconceptions:** (1) A plan is sound if it has all the section headings. (2) A small test can prove that a version works. (3) A note sent home after the test counts as consent.

**Instructional Rationale:** Critiquing a plan section by section is an Evaluate-level action that brings the chapter's concepts together. Four flawed and four sound sections teach the learner to find the weak point and to leave a sound section alone.

**Content:**

The two verdicts: Sound, Flawed. The flaws: Vague hypothesis, Confounded groups, Overclaim from a small sample, Consent after the test, Privacy gap.

The eight sections of the draft plan (all made up, for a Watershed Basics pilot):

| # | Section | Text of the draft | Correct verdict | Flaw | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | Hypothesis | The improved version will be better. | Flawed | Vague hypothesis | "Better" has no measure, size, or direction. |
| 2 | Groups | The control group is the third-period class using the original. The treatment group is the fifth-period class using the improved version. | Flawed | Confounded groups | The periods differ in students, time of day, and more. |
| 3 | Assignment | Students are paired by pre-test score, and a random number decides which student in each pair gets the improved version. | Sound | None | It is blocked random assignment. |
| 4 | Outcome measure | Both groups take a 20-question test written for the three learning outcomes, with the same key, before and after the lesson. | Sound | None | The measure is aligned, the same for both, and scored alike. |
| 5 | Sample size and claim | All 24 students in one class take part, and the result will be reported as proof that the improved version works for all Grade 6 students. | Flawed | Overclaim from a small sample | A pilot of 24 students cannot prove an effect for all students. |
| 6 | Consent | Students take part as a class activity, and a note will be sent home afterward. | Flawed | Consent after the test | Consent must come before any data is collected. |
| 7 | Privacy | Scores are stored under code numbers, the key is kept in a separate locked file, and no names are sent to any AI agent. | Sound | None | It follows the minimization, code, and agent practices. |
| 8 | Timeline | The pre-test is in week 1, the lesson is in weeks 2 and 3, and the post-test is in week 4, on the same days for both groups. | Sound | None | The conditions are the same for both groups. |

**Provenance:** The sections are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The flaws follow the chapter sections on the hypothesis, the groups, the sample, consent, and privacy.

**Rules:** Each section has exactly one correct verdict. Four are Flawed and four are Sound. The flaw named for each Flawed section is unique.

**Learner Activity:**

1. The learner sees one section of the plan.
2. The learner chooses Sound or Flawed. If Flawed, the learner also names the flaw.
3. The sim shows whether the verdict was correct, the flaw, and the Why text.
4. After section 8 the sim shows the summary.

**Feedback:** 8 sections in the order of the table, one attempt each. Correct: "Correct: [verdict]. [Why]". Incorrect: "Not quite. This section is [verdict]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can review a test plan." Below 7 it lists the Why text of each missed section.

**Starting State:** Section 1 of the draft plan and the two verdicts. The question shown is "Is this section ready to use?"

**Chapter Anchors:** The sections correspond to the chapter's hypothesis, groups, assignment, outcome measure, sample size, consent, privacy, and the timeline of the eight-step method.
</details>

---

## Key Takeaways

- An **A/B test** compares two versions, with different students using each at the same time. It answers a question the rubric cannot: whether students learn more from the improved version.
- Freeze the **original version** and the **improved version** before the test. The change log lists the differences, and a bundle of fixes tests only the bundle.
- The **control group** uses the original and the **treatment group** uses the improved version. They must differ in the version and in nothing else.
- A **test hypothesis** is written first, and it is specific, measurable, directional, sized, and falsifiable.
- An **outcome measure** is chosen in advance, aligned to the outcomes, fair to both versions, and scored alike. A **pre-test** and a **post-test** give the **learning gain**, and the normalized gain accounts for the room to improve. A **before-and-after comparison** without a second group cannot separate the lesson from the passage of time.
- **Random assignment** spreads unseen differences across the groups. It balances groups on average, so small classes should use blocked assignment, which needs the pre-test first.
- **Sample size** limits what a test can show. A pilot of 12 students per group checks the procedure and does not prove an effect.
- A **confounding variable** is a second difference between the groups, and **sampling bias** is a distortion in who takes part. Defend against both with the one-difference rule, random assignment, and a record of who participated.
- **Informed consent** comes before any data, is voluntary and free of penalty, and needs school or district approval. **Student privacy in testing** means collecting only what is needed, using codes, storing and deleting data safely, reporting in groups, and keeping identifiable data away from agents.

!!! mascot-celebration "You Can Design a Fair Test"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now write a testable hypothesis, form two comparable groups, choose fair measures, and plan consent and privacy for a student test. The next chapter turns to the data and shows how to tell whether the improved version helped.

[See Annotated References](./references.md)
