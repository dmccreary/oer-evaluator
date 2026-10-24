---
title: "Alignment and Readability"
description: "Shows how to score alignment to learning outcomes, standards, and Bloom's levels, and readability through reading level, vocabulary, plain language, and how well the text fits its audience."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:09:25"
version: 1.11
---

# Alignment and Readability

## Summary

Shows how to score alignment to learning outcomes, standards, and Bloom's levels, and readability through reading level, vocabulary, plain language, and how well the text fits its audience. It continues the quality metrics by asking whether a resource teaches what it claims to teach, in words its audience can read. After this chapter you can map a resource to learning outcomes and standards, and rate its reading level and fit to its audience.

## Concepts Covered

This chapter covers the following 25 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Learning Outcome | 83 |
| Alignment Metric | 16 |
| Learning Objective | 26 |
| Measurable Verb | 3 |
| Standards Alignment | 15 |
| Curriculum Map | 14 |
| Bloom's Taxonomy | 3 |
| Bloom Cognitive Levels | 2 |
| Outcome Coverage | 3 |
| Assessment Alignment | 1 |
| Content Gap | 1 |
| Scope and Sequence | 10 |
| Prerequisite Knowledge | 9 |
| Readability Metric | 23 |
| Reading Level | 16 |
| Readability Formula | 3 |
| Flesch-Kincaid Grade Level | 1 |
| Vocabulary Level | 7 |
| Defined Terms | 4 |
| Glossary | 3 |
| Plain Language | 1 |
| Jargon | 1 |
| Text Structure | 6 |
| Headings and Subheadings | 3 |
| Audience Fit | 3 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)

---

!!! mascot-welcome "Teach What You Test, and Say It Plainly"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A resource can be accurate and still miss the point: it teaches one thing and tests another, or it speaks far above its readers. This chapter gives you two checks for those problems, one for whether the parts line up and one for whether the words fit. Let's dive in and check the evidence!

Chapter 5 checked whether a resource's facts are right. Two more quality questions remain before we reach accessibility and practice. The first is alignment: does the resource teach and test what it says learners will achieve? The second is readability: can its intended readers read it? Both ask whether the resource fits the learners and the course, and both reward the same habit, which is to compare what a resource says it will do with what it actually does.

The chapter takes the metrics in turn. The alignment half introduces learning outcomes, objectives, Bloom's taxonomy, standards, and the maps that show what is taught and what is tested. The readability half covers reading level, vocabulary, plain language, and text structure. Each half ends with a scoring section built on ten checks.

## Learning Outcome

A **learning outcome** is a statement of what a learner will be able to do after finishing a course, unit, or resource. Two features matter. An outcome describes the learner and not the teacher: "students will explain" and not "the teacher will cover". And it names a capability and not a topic. "Photosynthesis" is a topic, and "Explain how plants make food from light, water, and carbon dioxide" is an outcome. A reviewer needs outcomes because alignment can only be judged against something, and a resource that states none gives the reviewer nothing to compare with.

Outcomes work at different scales. A course has a few broad outcomes, and a unit narrows them. This book's course description, for example, lists its outcomes under the six levels of Bloom's taxonomy, which a later section explains.

**Worked example: from topic to outcome.** Each row takes a topic that a resource might list and rewrites it as an outcome.

| Topic (not an outcome) | Outcome |
|---|---|
| Watersheds | Describe what a watershed is and name its parts. |
| Runoff | Explain how water moves over land and into streams. |
| Paving and flooding | Predict how paving a field changes the amount of runoff. |

These three outcomes are the ones the resource *Watershed Basics* from Chapter 3 states. The rest of this section keeps using them.

## Learning Objective

A **learning objective** is a narrow, specific statement of what a learner will do in one lesson, written so that someone can see whether it happened. Where an outcome describes the end of a unit, an objective describes one step toward it. A well-formed objective has three parts, which come from the educator Robert Mager's classic model:

- **Performance:** what the learner will do, written with a measurable verb.
- **Condition:** the situation or help the learner has, such as "given a map" or "without notes".
- **Criterion:** how well the learner must do it, such as "with no more than one error".

Compare "Students will learn about runoff" with "Given a diagram of a hillside, the student will explain in two sentences where runoff flows". The second states what the learner does, under what condition, and to what standard. A teacher can assess it.

**Worked example: one outcome, two objectives.** The outcome is "Explain how water moves over land and into streams."

| Part | Objective 1 | Objective 2 |
|---|---|---|
| Performance | Label the path of a raindrop | Explain in writing where runoff goes |
| Condition | On a diagram of a hillside | After reading section 2, without notes |
| Criterion | All four stages correct | Two complete sentences |

### Measurable Verb

A **measurable verb** is a verb that names something a teacher could observe a learner doing. *List*, *describe*, *calculate*, *compare*, and *design* are measurable, since you can watch someone do each one. *Know*, *understand*, *learn*, *appreciate*, and *be familiar with* are not, because no one can see them happen. A quick test is to ask, "How would I know the learner did this?" If the answer is "I couldn't tell", the verb is vague.

!!! mascot-tip "Swap the Vague Verb"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    When an outcome says "understand", ask what a learner would do to show it, and write that verb instead. "Understand the water cycle" becomes "explain the water cycle in four steps".

The first MicroSim of the chapter trains the test. It shows ten outcome statements, and for each one you decide whether its verb is measurable.

#### Diagram: Outcome Verb Checker

<details markdown="1">
<summary>Outcome Verb Checker</summary>
Type: microsim
**sim-id:** outcome-verb-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether the verb in each of ten outcome statements is measurable, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Learning Outcome, Learning Objective, Measurable Verb (all defined in this chapter above this block).

**Evidence of Mastery:** For each statement the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the test question is exploration, not evidence.

**Misconceptions:** (1) "Understand" is measurable because teachers use it all the time. (2) A longer statement is more measurable. (3) A measurable verb makes an outcome a good one.

**Instructional Rationale:** Judging a verb against the test "could I observe this?" is an Evaluate-level action. Ten statements that mix vague and measurable verbs in similar sentences make the learner apply the test to the verb itself and not to the topic.

**Content:**

The test, shown at all times: could a teacher watch a learner do this and tell whether it happened?

The two bins: Measurable, and Not measurable.

The ten statements:

| # | Statement shown to the learner | Correct bin | Why (shown as feedback) | Better wording (for Not measurable) |
|---|---|---|---|---|
| 1 | Students will understand the water cycle. | Not measurable | "Understand" cannot be observed. | Students will explain the water cycle in four steps. |
| 2 | Students will list the four main stages of the water cycle. | Measurable | A list can be seen and checked. | Not needed. |
| 3 | Students will know the parts of a cell. | Not measurable | "Know" cannot be observed. | Students will label the parts of a cell on a diagram. |
| 4 | Students will calculate the area of a rectangle from its length and width. | Measurable | A calculation produces a result that can be checked. | Not needed. |
| 5 | Students will appreciate the importance of clean water. | Not measurable | "Appreciate" is a feeling that cannot be observed directly. | Students will describe two ways clean water affects health. |
| 6 | Students will compare a primary source and a secondary source. | Measurable | A comparison can be written or spoken and then checked. | Not needed. |
| 7 | Students will learn about fractions. | Not measurable | "Learn about" names no action. | Students will add two fractions with like denominators. |
| 8 | Students will design a fair test to compare two fertilizers. | Measurable | A design is a product that can be reviewed. | Not needed. |
| 9 | Students will be familiar with the causes of the war. | Not measurable | "Be familiar with" cannot be observed. | Students will name three causes of the war and explain one. |
| 10 | Students will judge which of two websites is more reliable and give two reasons. | Measurable | The judgment and the reasons can be checked. | Not needed. |

**Provenance:** The statements are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The list of measurable and vague verbs follows the chapter section "Measurable Verb".

**Rules:** Each statement has exactly one correct bin, five per bin. A statement is Measurable when its main verb names an observable action.

**Learner Activity:**

1. The learner sees one statement and the two bins.
2. The learner places the statement in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. For a Not measurable statement the sim also shows the better wording.
5. After statement 10 the sim shows the summary.

**Feedback:** 10 statements in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can spot a vague verb." Below 9 it lists the Why text of each missed statement.

**Starting State:** The first statement, the test question, and two empty bins. The question shown is "Could a teacher observe this?"

**Chapter Anchors:** The chapter says know, understand, learn, appreciate, and be familiar with are not measurable, and that list, describe, calculate, compare, and design are measurable.
</details>

## Bloom's Taxonomy

**Bloom's taxonomy** is a classification of the thinking that learning goals ask for, from simple recall to creating something new. Benjamin Bloom and colleagues published the first version in 1956, and Lorin Anderson and David Krathwohl revised it in 2001. This book uses the 2001 revision. The taxonomy helps with alignment because it gives reviewers a shared way to say how demanding an outcome or an activity is.

### Bloom Cognitive Levels

The **Bloom cognitive levels** are the six steps of the revised taxonomy, each of which asks more of the learner than the one before. Each level has verbs that signal it, and the table gives the level, a typical verb, and an example objective.

| Level | What it asks | Typical verbs | Example |
|---|---|---|---|
| Remember | Recall facts and terms | list, name, define | List the five parts of a lesson plan. |
| Understand | Explain ideas in your own words | explain, summarize, interpret | Explain why the seasons change. |
| Apply | Use knowledge in a new situation | calculate, use, solve | Calculate the perimeter of a garden. |
| Analyze | Break material into parts and see how they relate | distinguish, differentiate, examine | Differentiate a cause from an effect in a historical event. |
| Evaluate | Judge using criteria | judge, critique, justify | Judge which of two designs is fairer, and justify the choice. |
| Create | Put parts together into something new | design, compose, construct | Design an experiment to test how light affects plant growth. |

The levels matter to a reviewer because an outcome and the activities that teach it should sit at the same level. If an outcome says "predict" and every activity asks only for recall, learners practice a skill that the outcome does not ask for, and they never practice the skill it does.

The second MicroSim practices the levels. It shows twelve objectives, and for each one you choose the Bloom level its verb signals.

#### Diagram: Bloom Level Sorter

<details markdown="1">
<summary>Bloom Level Sorter</summary>
Type: microsim
**sim-id:** bloom-level-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of twelve learning objectives under the Bloom cognitive level its verb signals, with at least 10 of 12 correct on the first attempt.

**Prerequisites:** Bloom's Taxonomy, Bloom Cognitive Levels, Learning Objective, Measurable Verb (all defined in this chapter above this block).

**Evidence of Mastery:** For each objective the learner commits one of six levels. A choice is correct when it matches the Correct level column in Content. Mastery is at least 10 of 12 correct on the first attempt. Reading the level table is exploration, not evidence.

**Misconceptions:** (1) The level depends on the topic. (2) "Identify" and "explain" are the same level. (3) A harder-sounding verb is always a higher level.

**Instructional Rationale:** Classifying objectives by level is an Understand-level action that builds the skill reviewers need when they compare an outcome with its activities. Two objectives per level, each with an unambiguous verb, teach the learner to read the verb first.

**Content:**

The six levels: Remember, Understand, Apply, Analyze, Evaluate, Create.

The twelve objectives:

| # | Objective shown to the learner | Correct level | Why (shown as feedback) |
|---|---|---|---|
| 1 | List the five parts of a lesson plan. | Remember | "List" asks for recall. |
| 2 | Name the three main types of rock. | Remember | "Name" asks for recall. |
| 3 | Explain in your own words why the seasons change. | Understand | "Explain" asks for meaning in your own words. |
| 4 | Summarize the main idea of a news article. | Understand | "Summarize" asks for a restatement of meaning. |
| 5 | Calculate the perimeter of a garden from its side lengths. | Apply | "Calculate" uses a procedure on a new case. |
| 6 | Use a map scale to find the distance between two towns. | Apply | "Use" applies a rule in a new situation. |
| 7 | Distinguish a fact from an opinion in a short article. | Analyze | "Distinguish" separates parts and sees how they differ. |
| 8 | Differentiate a cause from an effect in a historical event. | Analyze | "Differentiate" separates parts and relates them. |
| 9 | Judge which of two experiment designs is fairer, and justify the choice. | Evaluate | "Judge" and "justify" use criteria to decide. |
| 10 | Critique a persuasive essay using a checklist of criteria. | Evaluate | "Critique" judges against criteria. |
| 11 | Design an experiment to test how light affects plant growth. | Create | "Design" produces something new. |
| 12 | Compose a short story that uses three given vocabulary words. | Create | "Compose" produces something new. |

**Provenance:** The objectives are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The levels and their verbs follow the chapter section "Bloom Cognitive Levels", which follows the 2001 revision of the taxonomy.

**Rules:** Each objective has exactly one correct level, two per level. The level is determined by the main verb.

**Learner Activity:**

1. The learner sees one objective and the six levels.
2. The learner may open the level table. Opening it does not change the score.
3. The learner chooses a level, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After objective 12 the sim shows the summary.

**Feedback:** 12 objectives in a shuffled order, one attempt each. Correct: "Correct: [level]. [Why]". Incorrect: "Not quite. This is [level]. [Why]". The summary shows "[n] of 12 correct on the first attempt". At 10 or more it adds "You can read the level in a verb." Below 10 it lists the Why text of each missed objective.

**Starting State:** The first objective, the six levels, and the level table closed. The question shown is "Which Bloom level does this objective ask for?"

**Chapter Anchors:** The chapter lists six levels in the order remember, understand, apply, analyze, evaluate, and create, and says this book uses the 2001 revision.
</details>

## Alignment Metric

The **alignment metric** asks whether a resource's activities, assessments, and content match its stated learning outcomes. Educators call a design with all three in agreement *constructively aligned*: the outcomes say what learners should be able to do, the activities give practice at doing it, and the assessments check that they can. A resource can fail the metric in several ways. It can state no outcomes. It can teach something and never test it, or test something it never taught. It can ask for recall when the outcome asks for judgment.

Alignment is a matching problem among three lists, and the reviewer's tool is a table that puts the three side by side. The worked example below builds that table for *Watershed Basics*, using the three outcomes from the start of this chapter.

**Worked example: matching the three lists.** The resource has two reading sections and a quiz. The table shows which section teaches each outcome and which quiz items check it.

| Outcome | Taught by | Checked by | Result |
|---|---|---|---|
| 1. Describe what a watershed is and name its parts | Section 1 | Quiz items 1 to 4 | Aligned |
| 2. Explain how water moves over land and into streams | Section 2 | Quiz items 5 to 8 | Aligned |
| 3. Predict how paving a field changes the amount of runoff | No section | No quiz item | **Gap: neither taught nor checked** |

Two outcomes are covered, and the third is not. Chapter 3's evidence for this resource noted exactly that: "Outcome 3 has no activity", and quiz items map to two of the three outcomes. A reviewer who reads only the outcome list would think the resource covers prediction. The table shows that it does not.

### Standards Alignment

A **standard** is a public statement of what learners should know or be able to do at a given grade or in a given subject, written by a state, a national body, or a professional group. **Standards alignment** is the match between a resource and the standards it claims to meet. Resources often list standard codes, and listing is not matching. A reviewer reads the standard and checks that the resource asks learners to do what the standard asks, at the level it asks. Three results are possible. A *strong* match has learners doing what the standard names. A *partial* match touches the topic without asking for the performance. *No match* means that only a topic word is shared.

Standards differ from place to place. This book uses two made-up standards so that no claim here concerns a real state or country. The first is S-W1: "Explain how water moves through a watershed, including runoff, infiltration, and flow to a river or lake."

**Worked example: three claims against S-W1.**

| Lesson activity | Claims S-W1 | Result | Why |
|---|---|---|---|
| Students sketch a hillside, draw arrows to show where runoff flows, and explain the path in two sentences. | Yes | Strong | Learners explain how water moves, which is what the standard asks. |
| Students read a paragraph that mentions runoff. | Yes | Partial | The topic appears, and learners are not asked to explain anything. |
| Students color a picture of a river. | Yes | No match | Only the word river is shared with the standard. |

!!! mascot-warning "A Standard Code Is a Claim, Not Evidence"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A code printed beside an activity tells you what the author hopes, not what learners do. Read the standard, find the verb it asks for, and look for an activity that asks for it; if only the topic matches, mark the match partial.

The MicroSim below practices the judgment. It shows six lesson activities that each claim to meet one of two made-up standards, and for each one you rate the match.

#### Diagram: Standards Claim Checker

<details markdown="1">
<summary>Standards Claim Checker</summary>
Type: microsim
**sim-id:** standards-claim-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** assess<br/>
**Learning Objective:** The learner will assess whether each of six lesson activities is a strong match, a partial match, or no match for the standard it claims, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Standards Alignment, Learning Outcome, Bloom Cognitive Levels (all defined in this chapter above this block).

**Evidence of Mastery:** For each claim the learner commits one of three ratings. A rating is correct when it matches the Correct rating column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the standards is exploration, not evidence.

**Misconceptions:** (1) A shared topic is a match. (2) A listed code proves alignment. (3) A match must be exact in wording.

**Instructional Rationale:** Assessing a claim against a standard is an Evaluate-level action that requires reading what the standard asks learners to do. Pairing near-matches with strong matches teaches the learner to compare the verb and the content, and not only the topic.

**Content:**

The two made-up standards, shown at all times:

- S-W1: Explain how water moves through a watershed, including runoff, infiltration, and flow to a river or lake.
- S-W2: Predict how changes in land use affect runoff.

The three ratings: Strong match (learners do what the standard names), Partial match (the topic appears and the performance is missing or weaker), No match (only a topic word is shared).

The six claims:

| # | Lesson activity shown to the learner | Standard claimed | Correct rating | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Students read about runoff, infiltration, and river flow, then explain the path of a raindrop in a written paragraph. | S-W1 | Strong match | Learners explain how water moves, which is the standard's verb and content. |
| 2 | Students label the parts of a watershed diagram. | S-W1 | Partial match | Labeling names parts and does not explain movement. |
| 3 | Students watch a video about a famous river. | S-W1 | No match | The topic word river is shared, and no explanation is asked for. |
| 4 | Students compare runoff from a grass plot and a paved plot in a model, then predict what happens when more land is paved. | S-W2 | Strong match | Learners predict the effect of a land-use change on runoff. |
| 5 | Students list ways people use land near rivers. | S-W2 | Partial match | Listing land uses touches the topic and asks for no prediction. |
| 6 | Students memorize the names of five rivers. | S-W2 | No match | Nothing in the activity concerns land use or runoff. |

**Provenance:** The standards and activities are made up for this chapter, and the sim labels them "illustrative examples". The three ratings follow the chapter section "Standards Alignment".

**Rules:** Each claim has exactly one correct rating, two per rating. The rating depends on the standard's verb and content together.

**Learner Activity:**

1. The learner sees the two standards and one claim.
2. The learner chooses a rating, and the choice is committed.
3. The sim shows whether it was correct and the Why text, and highlights the standard's verb.
4. After claim 6 the sim shows the summary.

**Feedback:** 6 claims in a shuffled order, one attempt each. Correct: "Correct: [rating]. [Why]". Incorrect: "Not quite. This is [rating]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can check a standards claim." Below 5 it lists the Why text of each missed claim.

**Starting State:** The two standards and claim 1 or the first claim in the shuffled order. The question shown is "How well does this activity match the standard?"

**Chapter Anchors:** The chapter's example standard S-W1 reads "Explain how water moves through a watershed, including runoff, infiltration, and flow to a river or lake." The chapter says a strong match has learners doing what the standard names.
</details>

### Curriculum Map

A **curriculum map** is a table that shows how a course's outcomes, activities, and assessments connect. Each row is an outcome. The columns show the activities that teach it and the assessment items that check it. A map makes gaps visible that a list of outcomes hides. Teachers build full maps for courses, and a reviewer builds a quick one for a resource, as in the Watershed Basics table earlier in this chapter.

**Worked example: a small map for a fraction unit.** The unit has three outcomes, three sections, and five quiz items.

| Outcome | Taught by | Checked by | Result |
|---|---|---|---|
| F1. Name the numerator and denominator of a fraction | Section 1 | Items 1 and 2 | Aligned |
| F2. Compare two fractions with the same denominator | Section 2 | Items 3, 4, and 5 | Aligned |
| F3. Add two fractions with the same denominator | Section 3 | None | **Gap: taught but not checked** |

!!! mascot-thinking "Three Lists, One Story"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Outcomes, activities, and assessments are one story told three ways. Wherever the three disagree, a learner is practicing one thing and being tested on another.

### Outcome Coverage

**Outcome coverage** is the share of a resource's stated outcomes that are both taught and assessed. To compute it, count the outcomes that have at least one activity and at least one assessment item, and divide by the number of outcomes. Watershed Basics covers 2 of its 3 outcomes, a coverage of 67 percent. A coverage below 100 percent means the resource makes a promise that it does not keep.

### Assessment Alignment

**Assessment alignment** is the match between an assessment item and the outcome it claims to check. An item is aligned when it checks that outcome, at the level the outcome asks. An item can fail in two ways. It can check something other than the outcome, as when a quiz on rivers asks about river lengths while the outcome is to explain runoff. Or it can check the right topic at the wrong level, as when an outcome says "explain" and every item asks the learner to choose a vocabulary word. The second failure is easy to miss, because the topic matches.

### Content Gap

A **content gap** is an outcome that is not taught, not assessed, or not assessed at the level it asks. The gap may be in the teaching, in the checking, or in both, and the fix differs: add an activity, add a question, or raise the level of the question. The reverse problem is content with no outcome, such as a video that supports nothing the resource promises. That is not a gap, but it adds length and may distract, so a reviewer notes it.

The MicroSim below puts all of this together. It shows a curriculum map for a watershed unit, with four outcomes, five activities, and five quiz items. Your job is to find six problems in the map.

#### Diagram: Curriculum Map Gap Finder

<details markdown="1">
<summary>Curriculum Map Gap Finder</summary>
Type: microsim
**sim-id:** curriculum-map-gap-finder<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine a curriculum map and find all six gaps and mismatches in it, with no more than one incorrect mark.

**Prerequisites:** Curriculum Map, Outcome Coverage, Assessment Alignment, Content Gap, Bloom Cognitive Levels (all defined in this chapter above this block).

**Evidence of Mastery:** The learner marks the problems they find on the map and presses Check. The learner passes when all six problems in the Content table are marked and at most one other mark is wrong. Only the first Check counts as evidence. Opening the problem types is exploration, not evidence.

**Misconceptions:** (1) An outcome with a matching topic is covered. (2) Content with no outcome is always harmless. (3) A quiz item at any level checks any outcome on its topic.

**Instructional Rationale:** Finding gaps in a map is an Analyze-level action, because the learner must examine each connection and decide which is missing, extra, or at the wrong level. A map with several kinds of problem teaches the learner to look in every direction.

**Content:**

The four outcomes, with the Bloom level of each verb:

- O1: Describe what a watershed is. (Remember)
- O2: Explain how water moves through a watershed. (Understand)
- O3: Predict how paving changes runoff. (Analyze)
- O4: Compare two ways to reduce flooding. (Analyze)

The five activities and what each supports:

- A1: Reading, "What is a watershed?" supports O1.
- A2: Reading, "How water moves" supports O2.
- A3: Label a watershed diagram supports O1.
- A4: Video of famous rivers supports no outcome.
- A5: Group discussion on ways to reduce flooding supports O4.

The five quiz items and what each checks:

- Q1: Choose the definition of a watershed checks O1.
- Q2: Name the parts of a watershed checks O1.
- Q3: Choose the word for water flowing over land checks O2, and asks only for recall.
- Q4: Choose the term for water soaking into the ground checks O2, and asks only for recall.
- Q5: Choose the longest river in the region checks no outcome.

The six problems to find:

| # | Problem | Type | Why it is a problem |
|---|---|---|---|
| 1 | O3 has no activity. | Not taught | No activity gives practice at predicting. |
| 2 | O3 has no quiz item. | Not checked | Nothing checks whether learners can predict. |
| 3 | O4 has no quiz item. | Not checked | The discussion is never checked. |
| 4 | A4 supports no outcome. | Content with no outcome | The video adds length and supports no promise. |
| 5 | Q5 checks no outcome. | Item with no outcome | The question tests something the resource never promised. |
| 6 | O2 is checked only at the recall level. | Level mismatch | O2 asks learners to explain, and both items ask only for recall. |

**Provenance:** The outcomes, activities, and quiz items are made up for this chapter, and the sim labels them "illustrative example". The problem types follow the chapter sections "Outcome Coverage", "Assessment Alignment", and "Content Gap".

**Rules:** The map has exactly six problems, one per row of the table. A mark is correct when it identifies one of the six, by the outcome, activity, or item and the problem type. The learner may mark an outcome as unchecked or untaught, an activity or item as having no outcome, and an outcome as checked at the wrong level.

**Learner Activity:**

1. The sim shows the map as a grid of outcomes against activities and quiz items, with the Bloom level of each outcome.
2. The learner clicks a cell, an activity, an item, or an outcome and chooses the problem type from a short list.
3. The learner may remove a mark.
4. The learner presses Check.
5. The sim shows which of the six were found, which marks were wrong, and the Why text for each missed problem.

**Feedback:** One Check counts as evidence, and the learner may try again afterward. Pass: "You found all six problems with [n] wrong marks." Not yet: "You found [n] of 6. Missing: [problems with their Why text]." Wrong marks are named with the reason they are not problems. At a pass it adds "You can find the gaps in a map."

**Starting State:** The map with no marks and the prompt "Find six problems in this map."

**Chapter Anchors:** The chapter's Watershed Basics table has three outcomes with outcome 3 neither taught nor checked, and the chapter says outcome coverage is the number of taught and assessed outcomes divided by the number of outcomes. This sim's map is a larger unit with four outcomes.
</details>

### Scope and Sequence

**Scope and sequence** is the plan for what a course covers and in what order. *Scope* is the content included, and *sequence* is the order in which it arrives. Sequence matters because ideas build on each other. A section that uses a term or an idea before the resource has introduced it leaves learners guessing, and a section that is introduced and never used may not belong. A reviewer checks sequence by listing, for each section, what it introduces and what it uses, and looking for a section that uses what comes later.

**Worked example: a forward reference.** A resource on water has four sections.

| Section | Introduces | Uses |
|---|---|---|
| 1. Parts of a watershed | Watershed, tributary | None |
| 2. Where rain goes | Runoff | Watershed |
| 3. Flooding | Flood | Runoff, infiltration |
| 4. Soaking in | Infiltration | Runoff |

Section 3 uses *infiltration*, and section 4 is where it is introduced. The sequence is broken. The fix is to introduce infiltration before section 3, by moving section 4 up.

### Prerequisite Knowledge

**Prerequisite knowledge** is what a learner must already know or be able to do to use a resource. A resource should state its prerequisites, so that teachers can judge whether their learners are ready and can teach what is missing first. A good statement names concepts and skills and does not name only a grade. "Students should be able to count to 100 and tell when two groups have the same size" is more useful than "grade 1".

**Worked example: prerequisites for adding fractions.** The table lists three prerequisites for a unit on adding fractions, how a teacher could check each one, and where the resource addresses it.

| Prerequisite | How to check | Where the resource addresses it |
|---|---|---|
| Count and compare whole numbers | Ask learners to order four numbers | Assumed, not taught |
| Understand a fraction as part of a whole | Ask learners to shade three of four parts | Section 1 |
| Find equivalent fractions | Ask learners to write two fractions equal to one half | Section 4 |

The MicroSim below practices the sequence check. It shows the six sections of a fraction unit, with what each introduces and what each uses. For each section you decide whether the sequence works.

#### Diagram: Scope and Sequence Order Checker

<details markdown="1">
<summary>Scope and Sequence Order Checker</summary>
Type: microsim
**sim-id:** scope-sequence-order-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine a six-section unit and judge for each section whether its sequence is sound, uses an idea before it is introduced, or uses an idea that is never introduced, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Scope and Sequence, Prerequisite Knowledge, Curriculum Map (all defined in this chapter above this block).

**Evidence of Mastery:** For each section the learner commits one of three judgments. A judgment is correct when it matches the Correct judgment column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the section list is exploration, not evidence.

**Misconceptions:** (1) A term used in the section title counts as introduced. (2) Every used idea is introduced somewhere. (3) A section is fine if the idea appears later in the unit.

**Instructional Rationale:** Examining a sequence is an Analyze-level action, because the learner must follow what each part introduces and uses and trace the dependencies. A unit with one forward reference and one missing introduction teaches the learner that the two errors differ and need different fixes.

**Content:**

The three judgments: Sound, Uses an idea before it is introduced, Uses an idea that is never introduced.

The six sections, in order:

| # | Section | Introduces | Uses | Correct judgment | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | Parts of a whole | fraction, numerator, denominator | none | Sound | It uses nothing that is not already given. |
| 2 | Comparing fractions | comparing fractions | numerator, denominator, equivalent fractions | Uses an idea before it is introduced | Equivalent fractions are introduced in section 4. |
| 3 | Adding fractions with like denominators | adding like fractions | numerator, denominator | Sound | Both terms were introduced in section 1. |
| 4 | Equivalent fractions | equivalent fractions | fraction | Sound | Fraction was introduced in section 1. |
| 5 | Adding fractions with unlike denominators | common denominator | equivalent fractions, adding like fractions | Sound | Both ideas were introduced earlier, in sections 4 and 3. |
| 6 | Fractions on a number line | number line | fraction, comparing fractions, mixed numbers | Uses an idea that is never introduced | Mixed numbers appear in no section. |

**Provenance:** The unit is made up for this chapter, and the sim labels it "illustrative example". The judgments follow the chapter section "Scope and Sequence".

**Rules:** Each section has exactly one correct judgment. Four sections are Sound, one is Uses an idea before it is introduced, and one is Uses an idea that is never introduced. An idea counts as introduced only in a section numbered before the section that uses it.

**Learner Activity:**

1. The learner sees the six sections in a table with what each introduces and uses.
2. The learner chooses a judgment for section 1, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. The learner continues through sections 2 to 6.
5. After section 6 the sim shows the summary, and the learner may suggest the fix for each unsound section, which the sim then compares with the Why text.

**Feedback:** 6 sections in the fixed order, one attempt each. Correct: "Correct: [judgment]. [Why]". Incorrect: "Not quite. This section is [judgment]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can check a sequence." Below 5 it lists the Why text of each missed section.

**Starting State:** The six sections with their introduces and uses columns, and no judgments chosen. The question shown is "Is the sequence sound for section 1?"

**Chapter Anchors:** The chapter's sequence example has four sections about water with a forward reference to infiltration, and the chapter says a section that uses an idea before it is introduced is a sequence problem.
</details>

## Scoring Alignment

Alignment is scored with ten checks. A failed check is **serious** when it leaves the reviewer unable to judge alignment at all, which happens when the resource states no outcomes or states ones that cannot be observed. When a serious check fails, choose the lower number in a two-number band. Otherwise choose the higher number.

| # | Check | Serious if it fails? |
|---|---|---|
| 1 | Learning outcomes are stated | Yes |
| 2 | Each outcome uses a measurable verb | Yes |
| 3 | Every outcome is taught by at least one section or activity | No |
| 4 | Every outcome is checked by at least one assessment item | No |
| 5 | Every activity and assessment item maps to a stated outcome | No |
| 6 | The Bloom levels of activities and items match the levels of the outcomes | No |
| 7 | Standards alignment is shown where a standard applies | No |
| 8 | Prerequisite knowledge is stated | No |
| 9 | The sections follow a sound sequence | No |
| 10 | The intended course, grade, or audience is named | No |

A check that does not apply, such as standards alignment for a resource that claims no standard, counts as passed.

**Worked example: Watershed Basics.** The reviewer builds the map shown earlier in this chapter and applies the ten checks.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | The page states three outcomes. |
| 2 | Pass | The verbs are describe, explain, and predict. |
| 3 | **Fail** | Outcome 3 has no section or activity. |
| 4 | **Fail** | Quiz items check outcomes 1 and 2, and none checks outcome 3. |
| 5 | Pass | Every section and quiz item maps to an outcome. |
| 6 | **Fail** | Outcome 3 asks learners to predict, and only the remember and understand levels appear anywhere. |
| 7 | Pass | The resource claims no standard, so the check does not apply. |
| 8 | **Fail** | No note says what students should know first. |
| 9 | Pass | The two sections follow a sound order. |
| 10 | Pass | The page names its audience as grade 6 to 7. |

Six of ten checks pass, a share of 60 percent, in the 5 to 6 band. None of the four failures is serious, because the outcomes exist and can be observed. The reviewer therefore chooses the higher number, **6**, the score on the Chapter 3 worksheet. That worksheet recorded the three main gaps. The full check also finds that no prerequisite knowledge is stated.

## Readability Metric

The **readability metric** asks whether a resource's intended readers can read it with understanding. It is the second half of this chapter's pair, and it looks at the words and the layout instead of at what the resource covers. A resource can be aligned to its outcomes and still fail the metric, because a learner who cannot read the text cannot reach the outcomes. Five things feed the metric: the reading level of the text, the difficulty of its vocabulary, how plainly it is written, how it is organized, and how well all of that fits the people who will use it.

**Worked example: four readers, four barriers.** A grade 6 class uses a resource, and each reader meets a different barrier that the metric is designed to catch.

| Reader | Barrier | What the metric looks at |
|---|---|---|
| A student who reads at grade level | Sentences of 40 words and more | Reading level |
| A student who is learning English | Words such as "aquifer" with no definition | Vocabulary and defined terms |
| A student who skims | A wall of text with no headings | Text structure |
| A teacher choosing a reading | Cannot tell who the text is for | Audience fit |

## Reading Level

A **reading level** is the school grade, or age, at which a typical reader can read a text with understanding. A text written at grade 6 level is one that a typical grade 6 reader can handle. Reading level can be measured with a formula, which counts features of the words and sentences, or judged by a reader who knows the audience. The two methods answer slightly different questions, so a careful reviewer uses both.

A mismatch between the reading level and the audience is a barrier either way. A text far above the audience is hard to follow and can make a reader stop. A text far below it can feel childish and can leave out the ideas that older learners need. A good fit usually falls within about one grade of the audience's level.

**Worked example: three passages for a grade 6 audience.** The reading levels come from a readability tool.

| Passage | Measured level | Distance from grade 6 | Fit |
|---|---|---|---|
| A | 6.4 | 0.4 grades above | Good fit |
| B | 9.8 | 3.8 grades above | Too hard |
| C | 3.1 | 2.9 grades below | Too easy for this audience |

### Readability Formula

A **readability formula** is a calculation that estimates how hard a text is from features that a computer can count, usually the length of sentences and the length of words. Several are in common use, including the Flesch Reading Ease score, the Flesch-Kincaid Grade Level, the Gunning Fog index, and the SMOG index. They are quick and repeatable, which is why reviewers use them. They are also limited. A formula counts the surface of the text and cannot see how difficult the ideas are, how familiar the words are to a particular reader, or whether the passage is well organized.

### Flesch-Kincaid Grade Level

The **Flesch-Kincaid Grade Level** is a readability formula that gives a U.S. school grade. It uses three counts from a passage: the number of sentences, the number of words, and the number of syllables. Longer sentences and longer words raise the grade. For a stable result, use passages of at least 100 words, because a short sample can swing wildly. The formula is:

```text
grade = 0.39 x (words / sentences) + 11.8 x (syllables / words) - 15.59
```

The first part of the formula measures sentence length, as the average number of words per sentence. The second part measures word length, as the average number of syllables per word. The last number only adjusts the result so that it lines up with school grades. You never need to work it out by hand, because free tools do the counting, but seeing the arithmetic once shows what the number is made of.

**Worked example: a 120-word passage.** The passage has 6 sentences, 120 words, and 168 syllables.

1. Words per sentence: 120 divided by 6 is 20.
2. Syllables per word: 168 divided by 120 is 1.4.
3. Sentence part: 0.39 times 20 is 7.8.
4. Word part: 11.8 times 1.4 is 16.52.
5. Add the two parts: 7.8 plus 16.52 is 24.32.
6. Subtract 15.59: 24.32 minus 15.59 is 8.73, which rounds to a grade level of 8.7.

!!! mascot-encourage "The Tool Does the Counting"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If counting syllables by hand sounds tedious, it is, and that is why tools do it. You already read other formulas by asking what they measure, and the question here is what a grade number is made of. Once you know that, you can judge when to trust it.

The formula has a blind spot that is worth naming before you rely on it.

!!! mascot-thinking "The Formula Measures the Sentence, Not the Idea"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A passage of short words and short sentences can score as easy and still be hard, if its ideas are dense or its terms are never defined. Treat the number as one piece of evidence and read the passage yourself.

The MicroSim below lets you work the formula. In explore mode you change the three counts and watch the grade move. In practice mode you compute the grade for four passages.

#### Diagram: Flesch-Kincaid Calculator

<details markdown="1">
<summary>Flesch-Kincaid Calculator</summary>
Type: microsim
**sim-id:** flesch-kincaid-calculator<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the Flesch-Kincaid grade level of each of four passages from its counts of sentences, words, and syllables, to within 0.1 of the correct value, with at least 3 of 4 correct on the first attempt.

**Prerequisites:** Reading Level, Readability Formula, Flesch-Kincaid Grade Level (all defined in this chapter above this block).

**Evidence of Mastery:** For each passage the learner enters a grade level before the answer is shown. An answer is correct when it is within 0.1 of the Grade level column in Content. Mastery is at least 3 of 4 correct on the first attempt. Moving the explore-mode inputs is exploration, not evidence.

**Misconceptions:** (1) More syllables per word has little effect. (2) A shorter passage always gives a lower grade. (3) The grade is a score out of 10.

**Instructional Rationale:** Calculating with a formula is an Apply-level task. Exploration first shows how each count moves the grade, and committed calculations afterward test whether the learner can apply all three steps without help.

**Content:**

The formula, shown at all times: grade = 0.39 x (words / sentences) + 11.8 x (syllables / words) - 15.59.

The four passages:

| # | Sentences | Words | Syllables | Words per sentence | Syllables per word | Grade level (to one decimal) |
|---|---|---|---|---|---|---|
| 1 | 8 | 110 | 143 | 13.75 | 1.30 | 5.1 |
| 2 | 5 | 100 | 150 | 20.00 | 1.50 | 9.9 |
| 3 | 10 | 150 | 195 | 15.00 | 1.30 | 5.6 |
| 4 | 4 | 100 | 160 | 25.00 | 1.60 | 13.0 |

**Provenance:** The counts are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The formula is the Flesch-Kincaid Grade Level as stated in the chapter section "Flesch-Kincaid Grade Level".

**Rules:** In explore mode the sentences input has minimum 1, maximum 30, step 1, default 6, unit sentences. The words input has minimum 50, maximum 400, step 1, default 120, unit words. The syllables input has minimum equal to the number of words, maximum equal to 3 times the number of words, step 1, default 168, unit syllables. The grade is computed with the formula, rounded to one decimal place, and shown even when it is less than 0. In practice mode the learner enters the grade to one decimal place. An answer is correct when it differs from the Grade level column by <= 0.1.

**Learner Activity:**

1. In explore mode the learner changes sentences, words, and syllables and watches the two averages and the grade update.
2. The learner should notice that adding words without adding sentences raises the grade quickly.
3. In practice mode the sim shows passage 1 with its three counts.
4. The learner enters the grade and presses Check.
5. The sim shows the two averages, the grade, and the three steps of the arithmetic, then shows the next passage, until passage 4 is done.

**Feedback:** 4 passages in the fixed order, one attempt each. Correct: "Correct: grade [grade]. [Words per sentence] words per sentence and [syllables per word] syllables per word." Incorrect: "Not quite. The grade is [grade]. Step through: [three steps]". The summary shows "[n] of 4 correct on the first attempt". At 3 or more it adds "You can work the formula." Below 3 it shows the steps for each missed passage.

**Starting State:** Explore mode with 6 sentences, 120 words, and 168 syllables, so the grade is 8.7. The prompt is "Change a count to see the grade move."

**Chapter Anchors:** The chapter states the formula as grade = 0.39 x (words / sentences) + 11.8 x (syllables / words) - 15.59, and its worked example of 6 sentences, 120 words, and 168 syllables gives a grade of 8.7. The chapter advises passages of at least 100 words.
</details>

## Vocabulary Level

**Vocabulary level** is how difficult a text's words are for its readers. The educators Isabel Beck, Margaret McKeown, and Linda Kucan describe three tiers of words that help a reviewer decide what to do. *Tier 1* words are everyday words that most readers know, such as *because* and *river*. *Tier 2* words are general academic words that appear across subjects, such as *analyze*, *however*, and *evidence*. *Tier 3* words belong to one field, such as *aquifer* and *runoff*. The tiers call for different treatment: Tier 1 words need nothing, Tier 2 words are worth teaching and using consistently, and Tier 3 words must be defined where they first appear.

**Worked example: sorting six words from a reading.**

| Word | Tier | What the author should do |
|---|---|---|
| because | Tier 1 | Nothing |
| river | Tier 1 | Nothing |
| however | Tier 2 | Use it consistently, and make sure the audience knows it |
| analyze | Tier 2 | Use it consistently, and teach it if learners will meet it often |
| aquifer | Tier 3 | Define it where it first appears, and list it in a glossary |
| runoff | Tier 3 | Define it where it first appears, and list it in a glossary |

### Defined Terms

**Defined terms** are the specialized words that a resource explains in the text, and the practice of explaining each one where it first appears. The test is simple: when a reader meets a term for the first time, is its meaning in the same sentence or the next? A term defined three pages later, or never, forces the reader to guess. A good definition says what the term means in plain words, without using the term itself.

!!! mascot-tip "Define It Where It First Appears"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Put the definition in the same sentence as the term's first use, or in the sentence right after. A reader should never have to scroll or flip pages to learn what a word means.

### Glossary

A **glossary** is an alphabetical list of a resource's specialized terms with a definition for each. It supports defined terms in the text. A reader who forgets a term can look it up without hunting through earlier pages. A good glossary entry is short, precise, and written in terms simpler than the term itself. Many resources also link each term in the text to its glossary entry, so the definition is one click away.

The MicroSim below practices the check for defined terms. It shows a passage of eight sentences with five specialized terms, and for each term you decide whether it is defined at first use, defined later, or never defined.

#### Diagram: Term Before Definition Finder

<details markdown="1">
<summary>Term Before Definition Finder</summary>
Type: microsim
**sim-id:** term-before-definition-finder<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine a passage and judge for each of five specialized terms whether it is defined at first use, defined later, or never defined, with at least 4 of 5 correct on the first attempt.

**Prerequisites:** Vocabulary Level, Defined Terms, Glossary (all defined in this chapter above this block).

**Evidence of Mastery:** For each term the learner commits one of three judgments. A judgment is correct when it matches the Correct judgment column in Content. Mastery is at least 4 of 5 correct on the first attempt. Rereading the passage is exploration, not evidence.

**Misconceptions:** (1) A term defined anywhere in the passage is fine. (2) A word the reader probably knows needs no definition. (3) A glossary makes in-text definitions unnecessary.

**Instructional Rationale:** Examining a passage for the position of each definition is an Analyze-level action, because the learner must locate the first use and the definition and compare their order. Five terms with three different outcomes teach the learner to check each one separately.

**Content:**

The passage, shown at all times, with its sentences numbered:

1. A watershed is an area of land where all the water drains to the same place.
2. When rain falls, some of it becomes runoff and flows over the land.
3. The rest soaks in by infiltration, which means water seeping into the ground.
4. Water that collects underground fills an aquifer.
5. Runoff is the water that flows over the ground instead of soaking in.
6. Pavement increases runoff because water cannot seep through it.
7. A tributary is a smaller river that flows into a larger one.
8. Many tributaries join to form the main river.

The three judgments: Defined at first use, Defined later, Never defined.

The five terms:

| # | Term | First used in sentence | Defined in sentence | Correct judgment | Why (shown as feedback) |
|---|---|---|---|---|---|
| 1 | watershed | 1 | 1 | Defined at first use | The definition is in the same sentence as the term. |
| 2 | runoff | 2 | 5 | Defined later | The term is used in sentence 2, and its definition arrives in sentence 5. |
| 3 | infiltration | 3 | 3 | Defined at first use | The sentence says what it means right after the term. |
| 4 | aquifer | 4 | none | Never defined | No sentence says what an aquifer is. |
| 5 | tributary | 7 | 7 | Defined at first use | The definition is in the same sentence as the term. |

**Provenance:** The passage is written for this chapter and states general facts about watersheds, and the sim labels it "illustrative example". The judgments follow the chapter section "Defined Terms".

**Rules:** Each term has exactly one correct judgment. A term is Defined at first use when its definition is in the same sentence as its first use or the sentence immediately after. A term is Defined later when its definition appears more than one sentence after its first use. A term is Never defined when no sentence defines it.

**Learner Activity:**

1. The learner reads the passage with its numbered sentences.
2. The learner chooses a judgment for the first term, and the choice is committed.
3. The sim shows whether it was correct and the Why text, and highlights the first use and the definition in the passage.
4. The learner continues through the five terms.
5. After the fifth term the sim shows the summary.

**Feedback:** 5 terms in the fixed order, one attempt each. Correct: "Correct: [judgment]. [Why]". Incorrect: "Not quite. This term is [judgment]. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can find a missing definition." Below 4 it lists the Why text of each missed term.

**Starting State:** The passage and the first term, watershed, with the three judgments. The question shown is "Is this term defined where it first appears?"

**Chapter Anchors:** The chapter says a term should be defined in the same sentence as its first use or the sentence right after, and its Watershed Basics example uses the word aquifer before it is defined.
</details>

### Plain Language

**Plain language** is writing that readers can understand the first time they read it. It does not mean simple ideas or small words only. It means choosing the clearest way to say what you mean. Its habits are easy to list: short sentences with one idea each, the active voice, common words where a common word is as accurate, the reader's own terms, and examples. Plain language is not "dumbing down", because the ideas stay the same and the clutter goes away.

The MicroSim below practices the choice. For each of six sentences you pick the best of three rewrites.

#### Diagram: Plain Language Chooser

<details markdown="1">
<summary>Plain Language Chooser</summary>
Type: microsim
**sim-id:** plain-language-chooser<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply plain-language habits to choose the best rewrite of each of six sentences from three options, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Plain Language, Reading Level, Vocabulary Level (all defined in this chapter above this block).

**Evidence of Mastery:** For each sentence the learner chooses one of three rewrites. A choice is correct when it matches the Best rewrite column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the habit list is exploration, not evidence.

**Misconceptions:** (1) The shortest rewrite is always the plainest. (2) Plain language drops technical accuracy. (3) Passive voice is always wrong.

**Instructional Rationale:** Applying plain-language habits to new sentences is an Apply-level task. Options that include a wordy rewrite, an over-trimmed rewrite, and a plain and accurate rewrite make the learner weigh clarity against meaning.

**Content:**

The habits, shown on request: one idea per sentence; active voice; common words where they are as accurate; keep the meaning.

The six sentences:

| # | Original sentence | Option A | Option B | Option C | Best rewrite | Why (shown as feedback) |
|---|---|---|---|---|---|---|
| 1 | Individuals should endeavor to utilize the water conservation methodology. | People should try to use ways to save water. | Individuals ought to make an attempt to employ water-saving measures. | Water should be saved. | A | A keeps the meaning in common words. B keeps the long words, and C loses who should act. |
| 2 | The experiment was conducted by the students, and the results were recorded. | The students ran the experiment and recorded the results. | The experiment was done by students and results were put down. | Students conducted experimentation and recorded results. | A | A uses the active voice and plain verbs. B stays passive, and C uses stiffer words. |
| 3 | Photosynthetic organisms synthesize carbohydrates using solar radiation. | Plants make sugar from sunlight. | Plants and algae make sugar from sunlight. | Organisms that photosynthesize synthesize sugars from light. | B | B is plain and keeps the meaning, since algae also photosynthesize. A leaves them out, and C repeats the specialist words. |
| 4 | In the event that precipitation occurs, the field trip will be postponed. | If it rains, we will move the field trip to another day. | Should precipitation take place, the field trip is postponed. | If it rains, no trip. | A | A is plain and complete. B keeps the formal wording, and C drops the plan. |
| 5 | The aforementioned data indicates a significant increase. | The data in the table above show a large increase. | The data shows it went up. | The aforementioned figures reveal a major rise. | A | A replaces the stiff words and says where the data are. B is vague, and C keeps "aforementioned". |
| 6 | Utilize the glossary for the purpose of locating unfamiliar terms. | Use the glossary to find words you do not know. | Utilize the glossary to locate terms. | Look at the glossary. | A | A is plain and complete. B keeps "utilize", and C loses the purpose. |

**Provenance:** The sentences and rewrites are written for this chapter, and the sim labels them "illustrative examples". The habits follow the chapter section "Plain Language".

**Rules:** Each sentence has exactly one best rewrite. Options are shown in a fixed order for each sentence. A rewrite is best when it uses plain words and keeps the meaning of the original.

**Learner Activity:**

1. The learner sees one original sentence and three rewrites.
2. The learner chooses one rewrite, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After sentence 6 the sim shows the summary.

**Feedback:** 6 sentences in a shuffled order, one attempt each. Correct: "Correct: [option]. [Why]". Incorrect: "Not quite. The best rewrite is [option]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can write plainly and keep the meaning." Below 5 it lists the Why text of each missed sentence.

**Starting State:** The first sentence with its three rewrites. The question shown is "Which rewrite is the plainest and keeps the meaning?"

**Chapter Anchors:** The chapter says plain language uses short sentences with one idea each, the active voice, and common words where they are as accurate, and that it does not change the ideas.
</details>

### Jargon

**Jargon** is specialized language that a person outside a field would not know, and that the author uses without need or without explaining. Some specialized words are necessary: *aquifer* is the right word for an aquifer, and the fix is to define it. Jargon is the extra: an insider phrase where a common one would do, such as "utilize" for "use" or "operationalize" for "put into practice". A reviewer's test has two parts. If a common word says the same thing, ask for it. If the specialized word is necessary, ask for a definition.

!!! mascot-warning "Do Not Trade Accuracy for a Lower Grade"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Stripping out technical terms to lower a reading score can make a resource vague or wrong. Keep the term that is needed, define it where it first appears, and cut only the words that add nothing.

## Text Structure

**Text structure** is how a resource's text is organized: its headings, paragraph length, lists, signposts, examples, and summaries. Good structure lets a reader see the shape of the content, find a section again, and skip what they already know. Structure also affects readability for learners who struggle with long blocks of text, and it is the foundation for accessibility, because screen readers use headings to navigate.

**Worked example: before and after.** The table contrasts two versions of the same page.

| Feature | Before | After |
|---|---|---|
| Headings | None | A heading for each of five sections |
| Paragraphs | One block of 600 words | Paragraphs of three to five sentences, each with one idea |
| Lists | Steps buried in a paragraph | A numbered list of four steps |
| Signposts | None | A sentence that says what the section will do |
| Ending | The text stops | A short summary of key points |

The next MicroSim shows the parts of a readable page. Its illustration shows a page with seven features, each marked with a numbered marker.

#### Diagram: Anatomy of a Readable Page

<details markdown="1">
<summary>Anatomy of a Readable Page</summary>
Type: infographic
**sim-id:** readable-page-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify seven features of a readable page from a description of how each looks, with at least 6 of 7 correct on the first attempt.

**Prerequisites:** Text Structure, Defined Terms, Plain Language (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 6 of 7 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) A heading is just larger text. (2) A summary repeats the whole page. (3) Examples make a page longer without helping.

**Instructional Rationale:** Identifying features of a page is a Remember-level task, and an illustration of a readable page shows how the features sit together on one page. The quiz asks the learner to recognize each by its look.

**Content:**

The illustration is a text-free flat drawing of one lesson page. At the top is a wide bar of heading text. Under it is a short block of three thin lines. Further down a single word in the block is highlighted with a small dot beside it. A box with a small lightbulb icon holds two thin lines. A short list of three lines, each with a dot at its left, follows. Next is a framed picture with a thin strip beneath it. At the bottom is a shaded box with two thin lines and a small checkmark icon. The seven markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Descriptive heading | The wide bar of text at the top of the page. | A heading that tells the reader what the section is about, in words that match its content. | Write headings as short phrases that say what is inside. |
| 2 | Short paragraph | A block of three thin lines under the heading. | A paragraph of three to five sentences with one idea. | Break a paragraph when the idea changes. |
| 3 | Defined term | A single highlighted word with a small dot beside it. | A specialized word whose meaning is given where it first appears. | Put the definition in the same sentence. |
| 4 | Example box | A box with a small lightbulb icon holding two thin lines. | A concrete example that shows the idea at work. | Use an example whenever an idea is abstract. |
| 5 | List | A short list of three lines, each with a dot at its left. | Steps or items set apart, so the reader can scan them. | Use a numbered list when order matters. |
| 6 | Figure with caption | A framed picture with a thin strip beneath it. | A picture that supports the text, with a caption that says what to notice. | Describe the figure in the caption and credit its source. |
| 7 | Summary box | A shaded box at the bottom with a small checkmark icon. | A short recap of the key points at the end of the section. | Name the two or three ideas a reader should keep. |

**Provenance:** The seven features follow the chapter sections "Text Structure", "Defined Terms", and "Plain Language". The illustration is synthetic, and the sim labels the page "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 7 in the order of the table.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 7 hints the sim shows the summary.

**Feedback:** 7 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 7 correct on the first attempt". At 6 or more it adds "You can read a page's structure." Below 6 it lists the labels of the missed features.

**Starting State:** The illustration with seven numbered markers, explore mode active, and the prompt "Hover a marker to see what it is."

**Chapter Anchors:** The chapter's text-structure example lists headings, short paragraphs, lists, signposts, and a summary, and its page features include a defined term, an example box, and a figure with a caption.
</details>

### Headings and Subheadings

**Headings and subheadings** are the titles that label a resource's sections, with the main heading at the top and subheadings nested beneath it. A good heading is descriptive: "How runoff reaches a river" tells the reader more than "More information". Headings should follow a hierarchy, so that a section heading contains its subheadings and no level is skipped. A page that jumps from a main heading straight to a sub-sub-heading confuses readers and breaks screen readers, which is why the accessibility chapter checks it.

### Audience Fit

**Audience fit** is how well the whole of a resource matches the people who will use it: their reading level, prior knowledge, language, culture, and purpose. It is the summary question that the other readability features serve. A grade number cannot capture it. A passage at the right grade level can still be a poor fit if it assumes background the audience lacks, uses examples from an unfamiliar setting, or serves a purpose different from the audience's. A reviewer judges fit by asking a person from the audience to read a section aloud, and by noting where they stumble.

## Scoring Readability

Readability is scored with ten checks. A failed check is **serious** when it can stop the intended audience from reading the resource at all, which happens when the audience is not stated or the measured reading level is far from it. When a serious check fails, choose the lower number in a two-number band. Otherwise choose the higher number.

| # | Check | Serious if it fails? |
|---|---|---|
| 1 | The intended audience, a grade or level, is stated | Yes |
| 2 | The measured reading level of sampled passages is within one grade of the audience level | Yes |
| 3 | At least three passages from different sections were sampled | No |
| 4 | Technical terms are defined at first use | No |
| 5 | A glossary or term list is provided | No |
| 6 | Sentences are plain: mostly one idea each, in the active voice | No |
| 7 | Jargon is replaced or explained | No |
| 8 | Headings describe the content of their sections | No |
| 9 | Paragraphs are short and focused | No |
| 10 | Examples and visuals fit the audience's experience | No |

**Worked example: Watershed Basics.** The reviewer samples three passages and applies the ten checks.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | The page names its audience as grade 6 to 7. |
| 2 | Pass | A readability tool gave grade 6.4, 6.9, and 7.3 for the three samples. |
| 3 | Pass | The samples come from sections 1, 2, and 3. |
| 4 | **Fail** | The word "aquifer" is used in section 3 before any definition. |
| 5 | **Fail** | The resource has no glossary. |
| 6 | Pass | The sampled sentences are mostly one idea each. |
| 7 | Pass | No unexplained jargon appears in the samples. |
| 8 | Pass | Every heading says what its section contains. |
| 9 | Pass | Paragraphs run three to five sentences. |
| 10 | Pass | The examples use local rivers that a grade 6 reader would know. |

Eight of ten checks pass, a share of 80 percent, in the 7 to 8 band. Neither failed check is serious, because the audience is stated and the reading level fits it. The reviewer therefore chooses the higher number, **8**, the score on the Chapter 3 worksheet.

The last MicroSim of the chapter is a scoring practice for both halves. It shows three resources scored on alignment and three scored on readability, with each one's ten check results, and for each you choose the metric score.

#### Diagram: Alignment and Readability Scorer

<details markdown="1">
<summary>Alignment and Readability Scorer</summary>
Type: microsim
**sim-id:** alignment-readability-scorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the ten alignment checks and the ten readability checks, with the Chapter 3 scoring rules, to choose the metric score for each of six cases, with at least 5 of 6 scores exactly correct on the first attempt.

**Prerequisites:** The Alignment Metric, The Readability Metric, Scoring Alignment, Scoring Readability, Metric Score, Scoring Descriptor (all defined in this chapter or in Chapter 3 above this block).

**Evidence of Mastery:** For each case the learner chooses a whole-number score from 0 to 10 after seeing the ten check results. A score is correct when it equals the Correct score column in Content. Mastery is at least 5 of 6 scores correct on the first attempt. Opening the check lists and the descriptor table is exploration, not evidence.

**Misconceptions:** (1) Every failed check lowers the score equally. (2) A serious failure always drops a full band. (3) The two metrics use different scoring rules.

**Instructional Rationale:** Applying a scoring procedure to new cases is an Apply-level task. Three cases for each metric, with different counts and different serious failures, make the learner repeat the same procedure on two sets of checks.

**Content:**

The two ten-check lists are those in the chapter sections "Scoring Alignment" and "Scoring Readability", each marked serious or not. The descriptor bands applied to the share of checks passed: 0% is 0; 1% to 24% is 1 to 2; 25% to 49% is 3 to 4; 50% to 74% is 5 to 6; 75% to 89% is 7 to 8; 90% to 100% is 9 to 10. Within a two-number band, choose the lower number when a serious check failed and the higher number otherwise. A score of 10 requires every check to pass. A check that does not apply counts as passed.

The six cases:

| # | Metric | Resource | Checks failed | Checks passed | Share | Band | Serious failure? | Correct score | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Alignment | Open Algebra Unit | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed. |
| 2 | Alignment | Watershed Basics | 3, 4, 6, 8 | 6 | 60% | 5 to 6 | No | 6 | None of the failures is serious, so the higher number applies. |
| 3 | Alignment | Unit Without Outcomes | 1, 2, 3, 4, 5, 6, 8 | 3 (checks 7, 9, 10) | 30% | 3 to 4 | Yes, checks 1 and 2 | 3 | The unit states no outcomes, which is serious, so the lower number applies. |
| 4 | Readability | Open Algebra Unit | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed. |
| 5 | Readability | Watershed Basics | 4 and 5 | 8 | 80% | 7 to 8 | No | 8 | Neither failure is serious, so the higher number applies. |
| 6 | Readability | College Text Used in Grade 7 | 2, 4, 5, 6, 7 | 5 (checks 1, 3, 8, 9, 10) | 50% | 5 to 6 | Yes, check 2 | 5 | The reading level is far above the audience, which is serious, so the lower number applies. |

**Provenance:** The ten checks and the bands follow the chapter sections "Scoring Alignment" and "Scoring Readability" and Chapter 3. The six cases are illustrative cases written for this chapter, and the sim labels them "illustrative examples". Cases 2 and 5 are the chapter's worked examples.

**Rules:** A score is the band chosen from the share passed, then the number chosen within the band by the serious-failure rule. Each case has exactly one correct score. For a band that holds a single number, that number is the score.

**Learner Activity:**

1. The sim shows case 1 with its ten check results and the name of the metric.
2. The learner may open the check list and the descriptor table.
3. The learner chooses a score from 0 to 10, and the choice is committed.
4. The sim shows the count of passes, the band, whether a serious check failed, and the correct score with the Why text.
5. After case 6 the sim shows the summary.

**Feedback:** 6 cases in the fixed order, one attempt each. Correct: "Correct: [score]. [Why]". Incorrect: "Not quite. [passes] checks passed, which is [share] and the [band] band. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can score both metrics." Below 5 it lists the Why text of each missed case.

**Starting State:** Case 1 with all ten results shown and no score chosen. The question shown is "What alignment score does this resource earn?"

**Chapter Anchors:** The chapter's worked examples score Watershed Basics 6 on alignment, with failures of checks 3, 4, 6, and 8, and 8 on readability, with failures of checks 4 and 5. The chapter says a serious failure puts the score at the lower number in the band.
</details>

## Key Takeaways

- A **learning outcome** says what a learner will be able to do. A **learning objective** is one lesson's narrower, measurable step toward it, built with a **measurable verb**. **Bloom's taxonomy** and its six **cognitive levels** describe how demanding an outcome or an activity is.
- The **alignment metric** asks whether outcomes, activities, and assessments match. **Standards alignment** needs more than a code, a **curriculum map** shows what is taught and checked, **outcome coverage** measures the share covered, and **assessment alignment** and **content gaps** mark where the match breaks.
- **Scope and sequence** and **prerequisite knowledge** decide whether ideas arrive in an order a learner can follow.
- The **readability metric** asks whether intended readers can read the text. **Reading level** can be estimated with a **readability formula** such as the **Flesch-Kincaid Grade Level**, which counts the surface of the text and not the difficulty of its ideas.
- **Vocabulary level**, **defined terms**, a **glossary**, **plain language**, and the avoidance of **jargon** make a text easier to read. **Text structure**, with clear **headings and subheadings**, makes it easier to navigate, and **audience fit** is the overall judgment.

!!! mascot-celebration "You Can Check the Match and the Words"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now map a resource to its outcomes and find the gaps, rate its reading level, check its terms and structure, and score both alignment and readability with evidence. These two scores tell you whether a resource teaches what it promises in words its readers can use.
