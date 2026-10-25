# Quiz: Designing an A/B Test with Students

Test your understanding of control and treatment groups, hypotheses, learning gain, random assignment, confounders, sampling bias, consent, and student privacy in testing with these review questions.

---

#### 1. In an A/B test of an original resource and an improved resource, what is the control group?

<div class="upper-alpha" markdown>
1. The students who use the original version and receive ordinary teaching with it
2. The students who receive no lesson at all while the others use the improved version
3. The students who use the improved version of the resource and are tested the same way
4. The students who choose their own version of the resource after seeing both of them
</div>

??? question "Show Answer"
    The correct answer is **A**. The control group is the yardstick for the test. It answers the question "Compared with what?" It is not a group that receives no teaching: it gets the ordinary lesson with the original resource, which is a fully acceptable lesson, so no student is harmed. Many teachers offer the improved version to the control group after the test ends. The control group must differ from the treatment group in the version and in nothing else.

    **Concept Tested:** Control Group

    **See:** [Control Group](index.md#control-group)

---

#### 2. Which formula gives a student's normalized learning gain?

<div class="upper-alpha" markdown>
1. The gain divided by the room available: (post − pre) ÷ (100 − pre)
2. The raw difference between the two scores: post − pre
3. The gain divided by the starting score: (post − pre) ÷ pre
4. The ratio of the final score to the starting score on the same test: post ÷ pre
</div>

??? question "Show Answer"
    The correct answer is **A**. The normalized gain compares the gain with the room available to gain. A student who goes from 40 to 70 has a gain of 30 out of a possible 60, which is 0.50. A student who goes from 90 to 95 gains only 5 points but also closes half the available gap, 5 out of 10. The raw gain, post minus pre (B), cannot compare these students fairly. When the pre-test score is 100, the normalized gain is undefined.

    **Concept Tested:** Learning Gain

    **See:** [Learning Gain](index.md#learning-gain)

---

#### 3. Why does an A/B test use a control group instead of only comparing one group's scores before and after the lesson?

<div class="upper-alpha" markdown>
1. A single group cannot take both a pre-test and a post-test on the same set of questions in the same school week
2. Anything that happened between the tests can explain the gain, and a control group shares that time
3. A control group makes the sample size larger, which makes every result more reliable
4. A report is never allowed to include a before-and-after result from a single group
</div>

??? question "Show Answer"
    The correct answer is **B**. A gain of 18 points after a lesson is weak evidence on its own, because students were also learning in other classes, may have seen the test questions before, and simply got older. Without a second group you cannot separate the effect of the lesson from the effect of time. In an A/B test those effects cancel when you compare the two groups' gains. A before-and-after comparison is acceptable when no second group is possible, if the report names the limit.

    **Concept Tested:** Before-and-After Comparison

    **See:** [Before-and-After Comparison](index.md#before-and-after-comparison)

---

#### 4. Why does the chapter prefer assigning students to versions by chance instead of letting them choose?

<div class="upper-alpha" markdown>
1. Chance always produces two groups with exactly equal pre-test averages, however small the class
2. Letting students choose is against the law in most schools and so cannot be used in a test
3. Chance increases the number of students who can take part in the test at the same time
4. Chance spreads unseen differences, such as motivation, across the groups, while choice clusters keen students
</div>

??? question "Show Answer"
    The correct answer is **D**. Students differ in ways you cannot see or measure, such as motivation, home support, and sleep. Random assignment spreads those differences across the groups so that, on average, the groups are alike before the lesson. It balances groups only on average, so a small class can still be unlucky, and the chapter recommends pairing students by pre-test score and flipping a coin inside each pair. When the 12 highest scorers chose the improved version, the group averages differed by 23.75 points.

    **Concept Tested:** Random Assignment

    **See:** [Random Assignment](index.md#random-assignment)

---

#### 5. A student scores 40 on the pre-test and 70 on the post-test. What are the raw gain and the normalized gain?

<div class="upper-alpha" markdown>
1. 30 points and 0.30
2. 70 points and 0.70
3. 30 points and 0.50
4. 30 points and 0.75
</div>

??? question "Show Answer"
    The correct answer is **C**. The raw gain is the post-test score minus the pre-test score, which is 70 minus 40, or 30 percentage points. The normalized gain divides that by the room available, which is 100 minus 40, or 60. Thirty divided by 60 is 0.50, so the student closed half of the gap that was open. Option A divides by 100, which ignores the starting score. Compare gains, and not only post-test scores, because the groups may not start at the same level.

    **Concept Tested:** Learning Gain

    **See:** [Learning Gain](index.md#learning-gain)

---

#### 6. Which statement is a testable hypothesis for the Watershed Basics pilot?

<div class="upper-alpha" markdown>
1. The improved version is better than the original version for the students who use it in class
2. Students will like the improved version more than they like the original version of the lesson
3. Every student will learn more from the improved version than from the original version of the lesson
4. Grade 6 students on the improved version will have a larger mean learning gain than those on the original
</div>

??? question "Show Answer"
    The correct answer is **D**. A good hypothesis is specific, measurable, directional, sized, and falsifiable. Option D names the students and the measure and states the direction, and the chapter's own version adds a size of at least 5 percentage points. "Better" (A) has no measure. "Like" (B) has no comparison or measure. A claim about every student (C) cannot be shown, because some result would have to show it wrong. Write the hypothesis before the test, not after the results.

    **Concept Tested:** Test Hypothesis

    **See:** [Test Hypothesis](index.md#test-hypothesis)

---

#### 7. For the pilot, which set of items should the teacher keep in the data file?

<div class="upper-alpha" markdown>
1. The student's name, birthdate, home address, and scores, so each student can be contacted
2. The version label, pre-test score, post-test score, and grade level, with a code in place of the name
3. The scores, the email addresses, and a photograph of each student working on the lesson
4. The scores and the school student ID number, so that each score can be traced back
</div>

??? question "Show Answer"
    The correct answer is **B**. Collect only what the question needs. To compare gains you need the version, the pre-test, the post-test, and a grade level, which describes the sample without identifying anyone. Give each student a code such as S01, and keep the key that links codes to names in a separate, locked file. Names, ID numbers, birthdates, addresses, emails, and photographs are not needed, and each adds risk. Keep identifiable data away from AI agents too.

    **Concept Tested:** Student Privacy in Testing

    **See:** [Student Privacy in Testing](index.md#student-privacy-in-testing)

---

#### 8. In a test, the morning section uses the original version and the afternoon section uses the improved version, and the afternoon group scores higher. Which analysis is best?

<div class="upper-alpha" markdown>
1. The improved version is proven better, because its group scored higher than the other group
2. The sample is too large to trust, because larger samples contain more unusual students
3. Time of day and the students in each section also differ, so the version cannot be separated from them
4. The result is valid, because the same teacher taught both sections and so removed every other difference
</div>

??? question "Show Answer"
    The correct answer is **C**. A confounding variable is a factor other than the version that differs between the groups and could explain the result. Alertness changes through the day, and the two sections differ in other ways, so the version is tangled with them. The cure is the one-difference rule: arrange everything but the version to be the same, and let random assignment handle what you cannot arrange. A single teacher (D) removes one confounder and leaves the others in place.

    **Concept Tested:** Confounding Variable

    **See:** [Confounding Variable](index.md#confounding-variable)

---

#### 9. Nine students in the treatment group leave the test because the simulation would not load on their devices, and their scores are dropped. What problem does this show?

<div class="upper-alpha" markdown>
1. Volunteer bias, because the students chose to leave the test of their own accord
2. Convenience sampling, because the class was easy for the teacher to reach and test
3. Attrition, because the students who remain are those whose devices worked, so the result is biased
4. No concern, because the remaining students still took the test and their scores count
</div>

??? question "Show Answer"
    The correct answer is **C**. Sampling bias is a distortion when the students in the test are not like the students you want to learn about, or when the students who finish are not like those who started. Attrition is uneven dropout, so the scores that remain come from students who stayed. Record how many were invited, how many agreed, and how many finished each group, and report who took part. Offer both versions in forms that every student can use.

    **Concept Tested:** Sampling Bias

    **See:** [Sampling Bias](index.md#sampling-bias)

---

#### 10. A draft test plan says, "Students take part as a class activity, and a note will be sent home afterward." What is the best judgment?

<div class="upper-alpha" markdown>
1. It is sound, because a class activity does not need consent from the parents or the students
2. It is flawed, because consent must come before any data is collected, and declining must cost nothing
3. It is sound if the note is sent within a week, because the test is a normal class activity
4. It is flawed only because the note is too short to explain the test to the parents
</div>

??? question "Show Answer"
    The correct answer is **B**. Informed consent is agreement given freely after a person understands what taking part involves. For students under 18, a parent or guardian gives permission and the student gives assent. Consent comes before any data is collected, and anything collected earlier may not be usable. Declining must cost nothing, with an equally good alternative activity. The test also needs approval from the school or district before it starts.

    **Concept Tested:** Informed Consent

    **See:** [Informed Consent](index.md#informed-consent)
