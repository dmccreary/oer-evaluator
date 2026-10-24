---
title: "Automated Checks, Cost, and Student Privacy"
description: "Covers multi-agent review, keeping a human in the loop, automated link, accessibility, license, and readability checks, AI cost, and protecting student data under FERPA."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:36:18"
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

!!! mascot-welcome "Automate the Counting, Keep the Judgment"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    An agent can run a hundred checks while you drink your coffee, and it can also make a hundred confident mistakes. This chapter shows you what to automate, where a person must stay, what it costs, and how to keep student information out of harm's way. Let's dive in and check the evidence!

Chapter 12 gave you an agent that can read a resource and return scores. Before you let it loose on a collection, four questions deserve answers. Which checks are safe to automate, and which can fool you? Where does a person have to stay in the process? What will a large run cost? And what information must never go into an AI service at all? This chapter answers them, in that order, and the answers shape how the rest of the book uses agents.

## Human in the Loop

**Human in the loop** is a way of working in which a person reviews, approves, or corrects an automated system's output at the points where errors matter. It does not mean that a person redoes the work. It means that the machine's draft passes through a person before it becomes a decision. The idea fits this book's whole method: an agent produces a fast first pass with evidence, and a human checks the evidence, settles disagreements, and makes the adoption decision.

There are three reasons to keep a person in the loop. Agents make confident mistakes, as Chapter 12 showed, and Chapter 14 teaches you to find them. Accountability cannot be delegated: when a district adopts a resource, a person answers for the choice, and "the agent said so" is not an answer. And some checks depend on knowledge or context that an agent lacks, such as what a particular class needs. The cost is time, so the practical question is where a person's attention buys the most.

A useful way to spend that attention is to match the level of checking to the risk. A report that follows the rules, carries tool logs, and shows exact evidence needs only a spot check. A report whose claims rest on the agent's own memory needs every claim checked. A report that breaks the rubric's own rules, for example a total that does not equal the sum of its scores, goes back for another run.

**Worked example: three levels of oversight.** The table compares three ways of using the same agent on the same collection.

| Approach | What happens | Likely outcome |
|---|---|---|
| No oversight | The agent's totals go straight into the adoption list | A resource with an invented caption claim is adopted, and a blind learner meets a video with no captions |
| Check everything | A person redoes every score by hand | The review is accurate, and the agent saved no time |
| Risk-matched oversight | Rule-breaking reports go back, claims with no source are checked in full, and well-evidenced reports are spot-checked | Errors are caught where they occur, and most of the agent's time saving remains |

!!! mascot-thinking "The Answer Still Belongs to a Person"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    An agent can supply scores and evidence, and it cannot take responsibility for the decision. Plan the loop so that a named person looks at each report before it is used.

The first MicroSim of the chapter practices matching the check to the risk. It shows eight features of agent reports, and for each one you choose how much checking it needs.

#### Diagram: Human Check Planner

<details markdown="1">
<summary>Human Check Planner</summary>
Type: microsim
**sim-id:** human-check-planner<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply risk-matched oversight to choose send back, check every claim, or spot-check for each of eight features of agent reports, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Human in the Loop, and the sections on agent scoring and agent evaluation reports in Chapter 12 (all defined in this chapter above this block or in Chapter 12).

**Evidence of Mastery:** For each feature the learner commits one of three responses. A response is correct when it matches the Correct response column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the oversight levels is exploration, not evidence.

**Misconceptions:** (1) A report with numbers is trustworthy. (2) A person must redo every score. (3) A rule-breaking report can be fixed by hand.

**Instructional Rationale:** Choosing a response from a risk rule is an Apply-level action. Eight report features that map to three responses teach the learner to read a report for the signs that need attention.

**Content:**

The three responses: Send back (the report breaks a rule of the rubric or the prompt, so the agent must run again), Check every claim (the report may follow the rules, but its claims rest on the agent's own word), and Spot-check (the report follows the rules and shows exact evidence, so a person verifies a sample).

The eight features:

| # | Feature of an agent report shown to the learner | Correct response | Why (shown as feedback) |
|---|---|---|---|
| 1 | The total is 71, and the ten metric scores add up to 68. | Send back | The arithmetic is wrong, and the report breaks its own rule. |
| 2 | The decision is Adopt for a resource with a total of 76 and one metric at 4. | Send back | The decision breaks the adoption rule, which needs every metric at 5 or more. |
| 3 | An alignment score of 7 with no evidence quoted. | Send back | The prompt required evidence for every score. |
| 4 | A factual accuracy score of 9 that rests on the agent's own knowledge, with no sources. | Check every claim | No source is cited, so each claim must be checked. |
| 5 | A statement that all links work, with no link-checker log attached. | Check every claim | The claim may be invented, and the test must be run again. |
| 6 | An open license score of 9, with footer evidence on 6 of 6 pages and a tool log. | Spot-check | The evidence is exact and checkable, so a sample is enough. |
| 7 | A reading level from a tool, with the grade numbers shown. | Spot-check | The numbers are in the tool log, and a person can recompute one. |
| 8 | An editable source score of 10, with a file list and all ten check results. | Spot-check | The evidence is complete and verifiable. |

**Provenance:** The features are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The responses follow the chapter section "Human in the Loop".

**Rules:** Each feature has exactly one correct response. Three features are Send back, two are Check every claim, and three are Spot-check.

**Learner Activity:**

1. The learner sees one feature and the three responses.
2. The learner may open the oversight levels. Opening them does not change the score.
3. The learner chooses a response, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After feature 8 the sim shows the summary.

**Feedback:** 8 features in a shuffled order, one attempt each. Correct: "Correct: [response]. [Why]". Incorrect: "Not quite. The response is [response]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can match the check to the risk." Below 7 it lists the Why text of each missed feature.

**Starting State:** The first feature and the three responses. The question shown is "How much checking does this report need?"

**Chapter Anchors:** The chapter says rule-breaking reports go back, claims with no source are checked in full, and well-evidenced reports are spot-checked.
</details>

## Multi-Agent Review

**Multi-agent review** is the use of two or more agents, or several runs of one agent with different prompts or models, to score the same resource independently, so that their results can be compared. It copies the logic of the two-reviewer method from Chapter 11. Where the agents agree, a person can look less closely, and where they disagree, a person looks first. The spread between scores is a cheap signal. It points to the metrics where the evidence is unclear or where an agent has gone astray.

Multi-agent review has a limit that a reviewer must remember. Agreement among agents is not truth. Agents built on similar models can share the same blind spots, so three agents can all be wrong in the same way. Agreement with no evidence behind it is especially suspect. A sensible rule flags any metric where the scores spread by more than 3 points, flags any agreement where an agent has quoted no evidence, and leaves the rest for a spot check.

**Worked example: three agents score six metrics.** The table shows the scores and the action each row calls for.

| Metric | Agent 1 | Agent 2 | Agent 3 | Spread | Evidence | Action |
|---|---|---|---|---|---|---|
| Readability | 8 | 8 | 7 | 1 | Quoted by all three | Accept for a spot check |
| Accessibility | 5 | 9 | 6 | 4 | Quoted by all three | Flag: the spread exceeds 3 |
| Open license | 9 | 9 | 9 | 0 | None quoted by any agent | Check anyway: agreement without evidence |
| Metadata | 4 | 4 | 3 | 1 | Quoted by all three | Accept for a spot check |

The next MicroSim practices the triage. It shows six metrics scored by three agents, and for each row you choose the action.

#### Diagram: Multi-Agent Triage

<details markdown="1">
<summary>Multi-Agent Triage</summary>
Type: microsim
**sim-id:** multi-agent-triage<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine the scores and evidence of three agents for each of six metrics and choose accept, flag, or check anyway, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Multi-Agent Review, Human in the Loop, Inter-Rater Agreement (defined in Chapter 3) (all defined in this chapter above this block or in Chapter 3).

**Evidence of Mastery:** For each row the learner commits one of three actions. An action is correct when it matches the Correct action column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the triage rule is exploration, not evidence.

**Misconceptions:** (1) Agreement among agents proves a score is right. (2) Only disagreement needs a person. (3) The average of three scores is the right score.

**Instructional Rationale:** Triaging results from several agents is an Analyze-level action, because the learner must examine each row's spread and evidence together. Rows that agree with no evidence teach the learner that agreement alone proves little.

**Content:**

The triage rule, shown at all times: the spread is the highest score minus the lowest. If the spread is > 3, Flag. Otherwise, if any agent quoted no evidence, Check anyway. Otherwise, Accept for a spot check.

The three actions: Accept for a spot check, Flag, Check anyway.

The six rows (all made up, for Watershed Basics):

| # | Metric | Agent 1 | Agent 2 | Agent 3 | Evidence quoted | Correct action | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|
| 1 | Readability | 8 | 8 | 7 | All three agents | Accept for a spot check | The spread is 1, and all three quoted evidence. |
| 2 | Accessibility | 5 | 9 | 6 | All three agents | Flag | The spread is 4, which is > 3. |
| 3 | Open license | 9 | 9 | 9 | No agent | Check anyway | The agents agree and none quoted any evidence. |
| 4 | Metadata | 4 | 4 | 3 | All three agents | Accept for a spot check | The spread is 1, and all three quoted evidence. |
| 5 | Portability | 7 | 3 | 7 | All three agents | Flag | The spread is 4, which is > 3. |
| 6 | Alignment | 6 | 6 | 6 | Agent 1 only | Check anyway | The agents agree and two of them quoted no evidence. |

**Provenance:** The rows are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The rule follows the chapter section "Multi-Agent Review" and the agreement rule of Chapter 3.

**Rules:** Each row has exactly one correct action, two per action. The spread is computed as the highest minus the lowest of the three scores.

**Learner Activity:**

1. The learner sees one row with the three scores and the evidence note.
2. The learner chooses an action, and the choice is committed.
3. The sim shows the spread, whether the choice was correct, and the Why text.
4. After row 6 the sim shows the summary.

**Feedback:** 6 rows in a shuffled order, one attempt each. Correct: "Correct: [action]. [Why]". Incorrect: "Not quite. The action is [action]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can triage several agents." Below 5 it lists the Why text of each missed row.

**Starting State:** The first row and the three actions. The question shown is "What should a person do with this row?"

**Chapter Anchors:** The chapter says a spread of more than 3 is flagged, agreement with no evidence is checked anyway, and agreement among agents is not truth.
</details>

## Automated Checks

Four kinds of check are worth automating, because each one is exact and repeatable, and each can be run by a free tool that an agent can call. They map onto metrics you have already learned. Each one finds a certain kind of problem and misses another, and a reviewer needs to know both.

### Automated Link Checker

An **automated link checker** is a tool that tests every link in a resource and reports which ones fail, as Chapter 5 described. It is the model automated check: exact, fast, and repeatable. It finds links that return errors or move. It cannot tell whether a working link still leads to the cited content, and it may be refused by sites that block tools. The report supports the accuracy and currency metric, and a person opens a sample of working links to confirm they reach the right page.

### Automated Accessibility Scan

An **automated accessibility scan** is a tool that examines a page for the machine-detectable parts of WCAG, as Chapter 7 described. It finds images with no alt attribute, text with weak contrast, missing form labels, and some heading problems. It cannot judge whether alt text is useful, whether captions are accurate, or whether a page makes sense to a screen reader user. A clean scan is a starting point and never a pass, and the accessibility metric still needs the human checks.

### Automated License Detection

**Automated license detection** is the use of a tool to find license statements in a resource and read their names, versions, and links, and to compare them with the license recorded in the metadata. It catches a missing license, a license that differs between the page and the metadata, and an unrecognized or custom license text. It cannot tell whether the statement is true, so a work copied from someone else with a license label added still passes, and it can miss a license that appears only in an image. The check supports the open license metric.

### Automated Readability Scan

An **automated readability scan** computes a reading level for sampled passages, using a formula such as the Flesch-Kincaid Grade Level from Chapter 6. It gives a repeatable number quickly and can run over every section. It measures the surface of the text and cannot see whether the words are defined or the ideas are dense. Use it for a first screen, and read the passages that surprise you.

The table sums up what each scan is good for and where it stops.

| Automated check | Finds | Cannot find |
|---|---|---|
| Link checker | Links that return errors or have moved | A working link that leads to the wrong content |
| Accessibility scan | Missing alt attributes, weak contrast, missing labels | Whether alt text is useful, or captions are accurate |
| License detection | Missing, mismatched, or unrecognized license statements | Whether the license claim is true |
| Readability scan | A reading level for each passage | Undefined terms, dense ideas, audience fit |

The MicroSim below practices the match. It shows eight problems, and for each one you choose the automated check that would find it, or decide that no scan can.

#### Diagram: Automated Check Matcher

<details markdown="1">
<summary>Automated Check Matcher</summary>
Type: microsim
**sim-id:** automated-check-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of eight problems by the automated check that finds it, or as one that no scan finds, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Automated Link Checker, Automated Accessibility Scan, Automated License Detection, Automated Readability Scan (all defined in this chapter above this block).

**Evidence of Mastery:** For each problem the learner commits one of five options. A choice is correct when it matches the Correct option column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the table of what each scan finds is exploration, not evidence.

**Misconceptions:** (1) A clean accessibility scan means the page is accessible. (2) A license tool can tell whether a license claim is true. (3) A link checker can tell whether the cited content is right.

**Instructional Rationale:** Classifying a problem by the check that finds it is an Understand-level action that teaches the limits of each scan. Two problems that no scan finds teach the learner that automation leaves gaps.

**Content:**

The five options: Link checker, Accessibility scan, License detection, Readability scan, No scan finds it.

The eight problems:

| # | Problem shown to the learner | Correct option | Why (shown as feedback) |
|---|---|---|---|
| 1 | A link in the reference list returns "page not found". | Link checker | A link checker tests exactly this. |
| 2 | An image has no alt attribute at all. | Accessibility scan | A scan detects a missing alt attribute. |
| 3 | The footer says CC BY-NC, and the metadata says CC BY. | License detection | License detection compares the two statements. |
| 4 | A passage measures at grade 11 for a grade 6 audience. | Readability scan | A readability scan computes the grade level. |
| 5 | The alt text says only "photo". | No scan finds it | A scan sees that alt text exists and cannot judge whether it is useful. |
| 6 | White text on a pale yellow background has a contrast ratio of 1.4 to 1. | Accessibility scan | A scan computes contrast ratios. |
| 7 | A statistic in the text is ten years out of date. | No scan finds it | Only a person with a current source can tell. |
| 8 | No license statement appears anywhere in the resource. | License detection | License detection reports that no license was found. |

**Provenance:** The problems are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The matches follow the chapter section "Automated Checks".

**Rules:** Each problem has exactly one correct option. One is Link checker, two are Accessibility scan, two are License detection, one is Readability scan, and two are No scan finds it.

**Learner Activity:**

1. The learner sees one problem and the five options.
2. The learner may open the table of what each scan finds. Opening it does not change the score.
3. The learner chooses an option, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After problem 8 the sim shows the summary.

**Feedback:** 8 problems in a shuffled order, one attempt each. Correct: "Correct: [option]. [Why]". Incorrect: "Not quite. The answer is [option]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You know what each scan can and cannot see." Below 7 it lists the Why text of each missed problem.

**Starting State:** The first problem and the five options. The question shown is "Which automated check would find this?"

**Chapter Anchors:** The chapter's table lists what the link checker, accessibility scan, license detection, and readability scan each find and cannot find.
</details>

## AI Cost

**AI cost** is the money a service charges for the language model's work. Most services bill by the token, with one price for the tokens you send and a higher price for the tokens the model writes. Prices vary widely between models and change often, so a reviewer should look up current prices and never rely on a figure in a book. The arithmetic is stable, and it takes one formula:

```text
cost of one run = (input tokens x input price + output tokens x output price) / 1,000,000
```

The prices are per million tokens, so the division by 1,000,000 turns a price per million into a price for the tokens you used. The total for a batch is the cost of one run, times the number of resources, times the number of runs on each. A multi-agent review that uses three agents multiplies the cost by three, and a retry after an invalid answer adds another run.

**Worked example: the cost of a batch.** The prices are illustrative, at $2.00 per million input tokens and $8.00 per million output tokens. A run reads 6,000 input tokens and writes 1,000 output tokens.

| Step | Calculation | Result |
|---|---|---|
| Input cost | 6,000 x 2.00 / 1,000,000 | $0.012 |
| Output cost | 1,000 x 8.00 / 1,000,000 | $0.008 |
| One run | 0.012 + 0.008 | $0.02 |
| 500 resources, one run each | 500 x 0.02 | $10.00 |
| 500 resources, three agents | 3 x 10.00 | $30.00 |

Cost can be reduced without cutting quality. Give exact checks to free tools, which cost nothing per token. Shorten the instructions and send only the parts of the resource that a check needs. Use a smaller, cheaper model for first screens and a larger one for judgment. Test the prompt on three resources before running it on three hundred, so a flaw costs three runs and not three hundred.

!!! mascot-tip "Run a Pilot Before You Run the Batch"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Score three resources, read the reports, and multiply the cost by the size of the collection. A pilot tells you the price and shows whether the prompt works before you commit to the whole batch.

The MicroSim below practices the arithmetic. It shows five scenarios, and for each one you compute the total cost.

#### Diagram: AI Cost Calculator

<details markdown="1">
<summary>AI Cost Calculator</summary>
Type: microsim
**sim-id:** ai-cost-calculator<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the total cost of each of five scenarios from tokens, prices, resources, and runs, to the nearest cent, with at least 4 of 5 correct on the first attempt.

**Prerequisites:** AI Cost, Token, Context Window (defined in Chapter 12), Batch Evaluation (defined in Chapter 12) (all defined in this chapter above this block or in Chapter 12).

**Evidence of Mastery:** For each scenario the learner enters the total cost in dollars before the answer is shown. An answer is correct when it equals the Total cost column in Content to the nearest cent. Mastery is at least 4 of 5 correct on the first attempt. Using the explore mode is exploration, not evidence.

**Misconceptions:** (1) Input and output tokens cost the same. (2) A multi-agent review costs the same as one agent. (3) Prices in a book stay current.

**Instructional Rationale:** Calculating a cost from a formula is an Apply-level action. Five scenarios that change one quantity at a time teach the learner which quantity drives the total.

**Content:**

The formula, shown at all times: cost of one run = (input tokens x input price + output tokens x output price) / 1,000,000, with prices in dollars per million tokens. Total cost = cost of one run x resources x runs per resource.

The five scenarios (all prices are illustrative and labeled so):

| # | Input tokens | Output tokens | Input price | Output price | Resources | Runs each | Cost of one run | Total cost | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6,000 | 1,000 | $2.00 | $8.00 | 1 | 1 | $0.02 | $0.02 | (12,000 + 8,000) / 1,000,000 = 0.02. |
| 2 | 6,000 | 1,000 | $2.00 | $8.00 | 500 | 1 | $0.02 | $10.00 | 500 runs at $0.02 each. |
| 3 | 6,000 | 1,000 | $2.00 | $8.00 | 500 | 3 | $0.02 | $30.00 | Three agents triple the runs. |
| 4 | 60,000 | 2,000 | $2.00 | $8.00 | 1 | 1 | $0.136 | $0.14 | (120,000 + 16,000) / 1,000,000 = 0.136, which rounds to 0.14. |
| 5 | 6,000 | 1,000 | $10.00 | $30.00 | 500 | 1 | $0.09 | $45.00 | A model with higher prices costs $0.09 a run, and 500 runs cost $45.00. |

**Provenance:** The scenarios and prices are illustrative cases written for this chapter, and the sim labels them "illustrative prices, not a price list". Real prices vary by model and change.

**Rules:** The cost of one run is (input tokens x input price + output tokens x output price) / 1,000,000. The total is that cost x resources x runs, rounded to the nearest cent. In explore mode each input token count has minimum 1,000, maximum 200,000, step 1,000, default 6,000, unit tokens. Each output token count has minimum 500, maximum 10,000, step 500, default 1,000, unit tokens. Each price has minimum 0.10, maximum 50.00, step 0.10, unit dollars per million tokens. Resources have minimum 1, maximum 1,000, step 1, default 500. Runs have minimum 1, maximum 5, step 1, default 1.

**Learner Activity:**

1. In explore mode the learner changes the inputs and watches the cost of one run and the total.
2. The learner should notice that the number of runs multiplies the total in the same way as the number of resources.
3. In practice mode the sim shows scenario 1 with its numbers.
4. The learner enters the total cost in dollars and presses Check.
5. The sim shows the arithmetic and the correct total, then the next scenario, until scenario 5 is done.

**Feedback:** 5 scenarios in the fixed order, one attempt each. Correct: "Correct: $[total]. [Why]". Incorrect: "Not quite. One run costs $[run], so the total is $[total]. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can price a batch." Below 4 it shows the arithmetic for each missed scenario.

**Starting State:** Explore mode with 6,000 input tokens, 1,000 output tokens, $2.00 and $8.00 prices, 500 resources, and 1 run, giving a total of $10.00. The prompt is "Change a number to see the cost move."

**Chapter Anchors:** The chapter's worked example uses illustrative prices of $2.00 and $8.00 per million tokens, 6,000 input tokens and 1,000 output tokens, and arrives at $0.02 per run, $10.00 for 500 resources, and $30.00 for three agents.
</details>

## Student Data Privacy

**Student data privacy** is the protection of information about students from being collected, shared, or used in ways they and their families have not agreed to. Student data includes names, identification numbers, grades, test results, written work, photographs, attendance, and health and disability information, and anything that could identify a student when combined with other details. The duty to protect it applies to every tool you use, and AI services need particular care because text sent to a service leaves your control. The service may store it, a company's staff may read it, and some services use submitted text to improve their models.

For the work in this book, the rule is simple. An AI agent that reviews a *resource* needs only the resource, which is published or ready to publish and holds no student data. Keep student information out of the folder, the prompt, and the reports. The A/B tests in Chapters 16 and 17 do involve student data, and they need consent, anonymizing, and an approved way to handle the data. A teacher who is unsure should ask the school's privacy officer or technology office before sending anything.

**Worked example: sorting what may go to an AI service.** The table sorts six items.

| Item | May it be sent to an AI service? | Why |
|---|---|---|
| The published text of an open textbook chapter | Yes | It is public and holds no student data |
| A rubric prompt template | Yes | It holds no student data |
| A class's quiz scores with student names | Not as it is | Names make the scores personal data, so anonymize or get approval first |
| A spreadsheet of grades with student ID numbers | No | It is identifiable and sensitive |
| A student's photograph | No | It identifies a person |
| An email thread with a parent about a student | No | It is private and identifies a student |

!!! mascot-warning "Once It Is Sent, You Cannot Pull It Back"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Text pasted into an AI service has left your computer, and a deletion request may not undo it. Keep student names, grades, and records out of every prompt, and if you are not sure an item is safe, ask before you send it.

The MicroSim below practices the sort. It shows ten items, and for each one you decide whether it is safe to send, needs approval or anonymizing first, or must not be sent.

#### Diagram: Student Data Sorter

<details markdown="1">
<summary>Student Data Sorter</summary>
Type: microsim
**sim-id:** student-data-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of ten items is safe to send to an AI service, needs approval or anonymizing first, or must not be sent, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Student Data Privacy, FERPA, AI Assistant (defined in Chapter 12) (all defined in this chapter above this block or in Chapter 12).

**Evidence of Mastery:** For each item the learner commits one of three bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the definitions is exploration, not evidence.

**Misconceptions:** (1) Removing names always makes data anonymous. (2) A small class cannot be identified from its scores. (3) Anything a teacher already holds is safe to send.

**Instructional Rationale:** Judging whether an item may be sent is an Evaluate-level action that applies a privacy rule. Ten items that include re-identifiable ones teach the learner that anonymizing takes more than deleting names.

**Content:**

The three bins: Safe to send (public material with no student data), Needs approval or anonymizing first (could identify students, or is sensitive), and Do not send (clearly identifies a student or is private).

The ten items:

| # | Item shown to the learner | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | The published text of an open textbook chapter. | Safe to send | It is public and holds no student data. |
| 2 | A rubric prompt template with placeholders. | Safe to send | It holds no student data. |
| 3 | A class's quiz scores listed with student names. | Needs approval or anonymizing first | The names make the scores personal data. |
| 4 | A spreadsheet of grades with student ID numbers. | Do not send | It is identifiable and sensitive. |
| 5 | A photograph of a student. | Do not send | It identifies a person. |
| 6 | Quiz results with names replaced by codes, from a class of four students. | Needs approval or anonymizing first | In a very small group, the scores may still identify students. |
| 7 | A teacher's own lesson plan with no student information. | Safe to send | It holds no student data. |
| 8 | An email thread with a parent about a student's progress. | Do not send | It is private and identifies a student. |
| 9 | A public district policy document. | Safe to send | It is public and holds no student data. |
| 10 | Unsigned survey comments from a class of 120 students. | Needs approval or anonymizing first | Comments can reveal who wrote them, so check them before sending. |

**Provenance:** The items are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The sim states that it is a study aid and not legal advice, and that a school's own policy decides.

**Rules:** Each item has exactly one correct bin. Four items are Safe to send, three are Needs approval or anonymizing first, and three are Do not send.

**Learner Activity:**

1. The learner sees one item and the three bins.
2. The learner places the item in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After item 10 the sim shows the summary.

**Feedback:** 10 items in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can keep student data out of an AI service." Below 9 it lists the Why text of each missed item.

**Starting State:** The first item and the three bins. The question shown is "May this go to an AI service?"

**Chapter Anchors:** The chapter's worked example sorts a public textbook chapter and a rubric prompt as safe, class scores with names as needing anonymizing first, and a grade spreadsheet, a photograph, and a parent email as not to be sent.
</details>

### FERPA

**FERPA**, the Family Educational Rights and Privacy Act, is a United States federal law of 1974 that protects the privacy of student education records. It applies to schools and colleges that receive funds from the U.S. Department of Education. It gives parents the right to see their children's education records and to ask for corrections, and those rights pass to the student at age 18 or on entering a college. It generally requires written consent before a school discloses personally identifiable information from a student's education record, with exceptions, such as sharing with school officials who have a legitimate educational interest. Sending identifiable student records to an AI company is a disclosure that FERPA may restrict. Other laws also apply in other places or to other data, and this book does not give legal advice, so ask your school's privacy officer which rules cover you.

## Key Takeaways

- **Human in the loop** means a named person reviews the agent's output where errors matter, and matches the level of checking to the risk. The decision stays with a person.
- **Multi-agent review** compares independent runs, and a spread of more than 3 points flags a metric. Agreement among agents is not truth, and agreement with no evidence needs a check.
- An **automated link checker**, **accessibility scan**, **license detection**, and **readability scan** each do an exact job well and miss a kind of problem, so a clean scan is never a pass.
- **AI cost** is tokens times price, times resources, times runs. Give exact checks to free tools, and run a pilot before a batch.
- **Student data privacy** means keeping student information out of every prompt and report. **FERPA** is the U.S. law that protects student education records, and your school's policy decides what you may send.

!!! mascot-celebration "You Can Automate With Care"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now choose which checks to automate, keep a person in the loop, triage several agents, price a batch, and keep student data out of harm's way. The agent can do the counting, and you keep the judgment and the responsibility.
