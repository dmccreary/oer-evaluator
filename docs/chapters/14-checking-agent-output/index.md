---
title: "Checking and Calibrating AI Agent Output"
description: "Teaches teachers to catch hallucinations, invented citations, license misreadings, and overconfident scores, and to measure agreement with human reviewers using simple statistics."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:45:07"
version: 1.11
---

# Checking and Calibrating AI Agent Output

## Summary

Teaches teachers to catch hallucinations, invented citations, license misreadings, and overconfident scores, and to measure agreement with human reviewers using simple statistics. It is the chapter that makes AI scoring trustworthy, and it relies on the prompts and checks from the previous two chapters. After this chapter you can catch common agent errors, log your findings, and measure how closely an agent agrees with human reviewers.

## Concepts Covered

This chapter covers the following 22 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Hallucination | 735 |
| Invented Citation | 184 |
| License Misreading | 184 |
| Overconfident Score | 184 |
| Score Inflation | 1 |
| Agent Error Type | 182 |
| Verification Step | 180 |
| Spot Check | 1 |
| Source Verification | 1 |
| Second-Agent Cross-Check | 21 |
| Agent Disagreement | 20 |
| Accept Correct or Reject | 156 |
| Findings Log | 2 |
| Agent Error Rate | 1 |
| Agreement Rate | 19 |
| Score Difference Threshold | 7 |
| Mean Absolute Difference | 10 |
| Cohen's Kappa | 1 |
| Score Correlation | 2 |
| Calibration Against Humans | 6 |
| Prompt Refinement | 1 |
| Run-to-Run Variance | 1 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 2: Open Licenses and Attribution](../02-open-licenses-attribution/index.md)
- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)
- [Chapter 5: Accuracy and Currency](../05-accuracy-currency/index.md)
- [Chapter 11: Manual Evaluation and Adoption Decisions](../11-manual-evaluation-adoption/index.md)
- [Chapter 12: AI Agents, Prompts, and Rubric Scoring](../12-ai-agents-prompts-scoring/index.md)
- [Chapter 13: Automated Checks, Cost, and Student Privacy](../13-automated-checks-cost-privacy/index.md)

---

!!! mascot-welcome "Trust, But Check the Evidence"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    This is the chapter I have been waiting for, because it turns an agent's confident first pass into something you can rely on. You will learn the mistakes agents make, how to catch each one, and how to measure how closely an agent agrees with careful human reviewers. Let's dive in and check the evidence!

An agent's report looks finished. It has ten scores, a table of evidence, a total, and a recommendation, all in a tidy form. The earlier chapters warned that this polish can hide errors, and this chapter shows you what the errors look like and how to find them. It has two parts. The first part is about *checking*: the kinds of mistake an agent makes, the steps that catch each one, and the habit of accepting, correcting, or rejecting every claim. The second part is about *measuring*: the simple statistics that tell you, across many resources, how closely an agent agrees with human reviewers, and whether it is safe to use as a first pass.

## Hallucination

A **hallucination** is a statement by a language model that is fluent and confident and not true: a fact it made up, a quotation that does not appear in the source, a feature of the resource that is not there, or a reference to something that does not exist. Chapter 12 explained why this happens. A model writes what is likely to come next, and a plausible continuation is not always a true one. In a review the danger is sharper than usual, because the agent is asked to report what it found in a resource, and a hallucination is a report of something it did not find.

Hallucinations take four common forms in an evaluation report:

- **An invented feature:** the report says the video has captions, and it has none.
- **An invented quotation:** the report quotes a sentence as evidence, and the sentence is not in the resource.
- **An invented measurement:** the report gives a contrast ratio or a reading level, and no tool produced it.
- **An invented source:** the report cites a paper or a page that does not exist, which the next section treats separately.

The defense is the rule that every claim must carry evidence a person can find. A quotation can be searched for in the resource. A measurement can be traced to a tool log. A claim with neither is a claim to reject.

**Worked example: four hallucinations in one draft.** An agent's draft for *Watershed Basics* contains four invented claims. The table shows each one and how a reviewer finds it.

| Kind | What the agent wrote | How the reviewer found it |
|---|---|---|
| Invented feature | "The video has English captions." | Played the video, and found no caption control |
| Invented quotation | Evidence: "Alt text: A detailed map of the river and nearby towns" | Searched the page for the sentence, and found different alt text: "A map showing the river and its tributaries" |
| Invented measurement | "Contrast ratio tested: 5.2 to 1" | Asked for the tool log, and found that no tool had run |
| Invented count | "All 14 links work" | Ran a link checker, and found that 2 links fail |

!!! mascot-warning "The Smoothest Sentence May Be the Invented One"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A hallucination does not look different from a true statement, because the model writes both in the same confident voice. Search for every quotation, trace every number to a tool, and treat any claim you cannot find as false until you do.

The first MicroSim of the chapter trains the search for invented quotations. It shows a short excerpt of a resource and eight quotations that an agent offered as evidence, and for each one you decide whether it is exact, altered, or not in the text.

#### Diagram: Quote Verifier

<details markdown="1">
<summary>Quote Verifier</summary>
Type: microsim
**sim-id:** quote-verifier<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight quotations offered by an agent is an exact quote, an altered quote, or not in the text, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Hallucination, Evidence for a Score (defined in Chapter 3), Agent Evaluation Report (defined in Chapter 12) (all defined in this chapter above this block or in earlier chapters).

**Evidence of Mastery:** For each quotation the learner commits one of three verdicts. A verdict is correct when it matches the Correct verdict column in Content. Mastery is at least 7 of 8 correct on the first attempt. Rereading the excerpt is exploration, not evidence.

**Misconceptions:** (1) A quotation that sounds right is exact. (2) A small change to a quotation does not matter. (3) A quotation that is plausible must be somewhere in the text.

**Instructional Rationale:** Judging a quotation against its source is an Evaluate-level action that every review of an agent's evidence needs. Altered quotations, which differ in one detail, teach the learner to compare word for word, and invented ones teach the learner to search the whole text.

**Content:**

The excerpt, shown at all times (made up): "Watershed Basics by Maria Lopez. Licensed under CC BY 4.0. A watershed is an area of land where all the water drains to the same place. Section 2: The Clearwater River drains about 6,000 square miles and flows into Lake Marlow. Figure 1: A map of the Clearwater watershed. Alt text: A map showing the river and its tributaries. Quiz: Question 1 asks the learner to choose the definition of a watershed."

The three verdicts: Exact quote, Altered quote, Not in the text.

The eight quotations:

| # | Quotation offered by the agent | Correct verdict | Why (shown as feedback) |
|---|---|---|---|
| 1 | "Licensed under CC BY 4.0" | Exact quote | The words appear exactly. |
| 2 | "A watershed is an area of land where all the water drains to the same place." | Exact quote | The sentence appears exactly. |
| 3 | "The Clearwater River drains about 6,000 square miles and flows into the sea." | Altered quote | The excerpt says it flows into Lake Marlow, so "the sea" is a change. |
| 4 | "Captions are available in English and Spanish." | Not in the text | Nothing in the excerpt mentions captions. |
| 5 | "Figure 1: A map of the Clearwater watershed." | Exact quote | The caption appears exactly. |
| 6 | "Alt text: A detailed map of the river, its tributaries, and nearby towns." | Altered quote | The excerpt says "A map showing the river and its tributaries", so details were added. |
| 7 | "Licensed under CC BY-SA 4.0" | Altered quote | The excerpt says CC BY, so the license was changed. |
| 8 | "An answer key is included for all quiz questions." | Not in the text | Nothing in the excerpt mentions an answer key. |

**Provenance:** The excerpt and quotations are made up for this chapter, and the sim labels them "illustrative examples". The verdicts follow the chapter section "Hallucination".

**Rules:** Each quotation has exactly one correct verdict. Three are Exact quote, three are Altered quote, and two are Not in the text. A quotation is exact only when it matches the excerpt word for word.

**Learner Activity:**

1. The learner sees the excerpt and one quotation.
2. The learner chooses a verdict, and the choice is committed.
3. The sim shows whether it was correct and the Why text, and highlights the matching or conflicting part of the excerpt.
4. After quotation 8 the sim shows the summary.

**Feedback:** 8 quotations in a shuffled order, one attempt each. Correct: "Correct: [verdict]. [Why]". Incorrect: "Not quite. This is [verdict]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can check an agent's quotations." Below 7 it lists the Why text of each missed quotation.

**Starting State:** The excerpt and quotation 1 or the first quotation in the shuffled order. The question shown is "Does this quotation appear in the text?"

**Chapter Anchors:** The chapter lists four forms of hallucination: an invented feature, quotation, measurement, and source. The chapter's worked example includes an altered alt text for a map.
</details>

## Invented Citation

An **invented citation** is a reference to a source that does not exist, or that exists and does not say what the agent claims. Agents produce these readily, because a citation has a predictable shape, with authors, a title, a journal, a year, and pages, and a model can write that shape without any real source behind it. The result looks scholarly. It is also useless, because no one can find the paper, and it is misleading, because it lends a claim an authority it has not earned.

Two kinds of invented citation need different checks. A *nonexistent* source is one that cannot be found at all: the journal, the article, or the author is made up. A *misattributed* source exists and does not support the claim: a real paper on urban runoff cited for a claim about wetlands. A reviewer needs four checks to tell them apart. Search for the exact title. Check that the journal exists and has the issue cited. Resolve the identifier or the link. And open the source and read the passage that is supposed to support the claim.

An identifier helps. A DOI (digital object identifier) is a permanent code that should lead to the article's page, so a DOI that leads nowhere, or leads to a different article, is a strong sign of an invented or misattributed citation. A missing identifier is a weaker sign, since many real sources, such as a school's own pages, have none. The best defense sits in the prompt: tell the agent to cite only sources that appear in the resource or that you supplied, and to write "no source found" in place of supplying one from memory.

**Worked example: three citations from an agent's report.** The table shows the checks and the verdicts.

| Citation | What the checks found | Verdict |
|---|---|---|
| State Water Agency, "Lake Marlow Fact Sheet", 2025, with a link | The link opens a fact sheet that gives the lake's depth, which supports the claim | Real and supports the claim |
| Lopez, M. (2024), "Rivers of the Plain", *Journal of Water Education*, 12(3), 44 to 59 | No journal by that name appears in any index, and no article has that title | Invented |
| Okafor, S. (2022), "Runoff and Land Use", *Earth Science Review* | The article exists and studies urban runoff, and it does not mention wetlands | Real and does not support the claim |

The MicroSim below practices the checks. It shows six citations, each with the result of a lookup, and for each one you decide what the lookup shows.

#### Diagram: Citation Existence Checker

<details markdown="1">
<summary>Citation Existence Checker</summary>
Type: microsim
**sim-id:** citation-existence-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine the lookup result for each of six citations and decide whether the source exists and supports the claim, exists and does not support it, or does not exist, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Invented Citation, Hallucination, Citation Quality (defined in Chapter 5) (all defined in this chapter above this block or in Chapter 5).

**Evidence of Mastery:** For each citation the learner commits one of three verdicts. A verdict is correct when it matches the Correct verdict column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the four checks is exploration, not evidence.

**Misconceptions:** (1) A citation that looks complete is real. (2) A source that exists supports the claim. (3) A working link means the claim is supported.

**Instructional Rationale:** Examining a lookup result against a claim is an Analyze-level action, because the learner must relate what was found to what the agent claimed. Six citations that mix real, misattributed, and invented ones teach the learner to ask two questions each time: does it exist, and does it say that.

**Content:**

The three verdicts: Exists and supports the claim, Exists but does not support the claim, Does not exist.

The six citations (all made up), each with the claim the agent attached to it and the result of a lookup:

| # | Agent's claim and citation | Lookup result shown to the learner | Correct verdict | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Claim: the deepest point of Lake Marlow is 31 meters. Citation: State Water Agency, "Lake Marlow Fact Sheet", 2025, https://example.gov/lake-marlow | The page loads and gives the lake's area and its deepest point of 31 meters. | Exists and supports the claim | The source is real and states the figure. |
| 2 | Claim: rivers on plains meander more. Citation: Lopez, M. (2024), "Rivers of the Plain", Journal of Water Education, 12(3), 44 to 59. | No journal named Journal of Water Education appears in any index, and no article has this title. | Does not exist | Neither the journal nor the article can be found. |
| 3 | Claim: wetlands filter pollutants. Citation: Okafor, S. (2022), "Runoff and Land Use", Earth Science Review. | The article exists and studies urban runoff, and it does not discuss wetlands. | Exists but does not support the claim | The source is real and says nothing about the claim. |
| 4 | Claim: the reading is licensed CC BY 4.0. Citation: https://example.org/watershed-basics | The page loads, and its footer says CC BY 4.0. | Exists and supports the claim | The source is real and states the license. |
| 5 | Claim: soil infiltration varies with grain size. Citation: Reyes, D. (2021), "Soil Infiltration Rates", Geology Quarterly, 5(2), 10 to 19. | The journal exists, and volume 5 issue 2 has no article with this title or author. | Does not exist | The journal is real and the article is not in the issue cited. |
| 6 | Claim: aquifers store groundwater. Citation: National Water Atlas (2019), entry on aquifers. | The atlas exists, and its aquifer entry says aquifers store groundwater. | Exists and supports the claim | The source is real and states the claim. |

**Provenance:** The claims, citations, and lookup results are made up for this chapter, and the sim labels them "illustrative examples". The checks follow the chapter section "Invented Citation".

**Rules:** Each citation has exactly one correct verdict. Three are Exists and supports the claim, one is Exists but does not support the claim, and two are Does not exist.

**Learner Activity:**

1. The learner sees the claim, the citation, and the lookup result.
2. The learner chooses a verdict, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After citation 6 the sim shows the summary.

**Feedback:** 6 citations in a shuffled order, one attempt each. Correct: "Correct: [verdict]. [Why]". Incorrect: "Not quite. The verdict is [verdict]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can tell a real citation from an invented one." Below 5 it lists the Why text of each missed citation.

**Starting State:** The first citation with its claim and lookup result. The question shown is "Does this source exist, and does it support the claim?"

**Chapter Anchors:** The chapter says an invented citation is either nonexistent or misattributed, and lists four checks: search the title, check the journal and issue, resolve the identifier, and read the supporting passage.
</details>

## License Misreading

A **license misreading** is an agent's wrong statement about what a resource's license says or what it allows. Agents misread licenses in a handful of predictable ways. They treat a page's single license as covering every item on it, when the images carry other rights. They confuse neighboring licenses, so CC BY-NC reads as CC BY. They ignore a restriction, such as ND, when summarizing what a reuser may do. They read the license of the site's template and not of the content. And they conclude that a public page is free to copy because it is on the web. Because a misreading can send a teacher into a legal problem, a reviewer checks every license claim against the statement itself, the way Chapter 2 taught.

The prompt can lower the risk. Ask the agent to quote the license statement word for word, to name each item the statement covers, and to write "not stated" for any item the statement does not mention. A report that quotes the statement can be checked in seconds, and a report that paraphrases it cannot.

**Worked example: five misreadings.** The page states: "Text: CC BY-SA 4.0. Images: © their owners, used with permission, except where marked CC BY."

| What the agent said | What the page says | The misreading |
|---|---|---|
| "Everything on the page is CC BY-SA 4.0." | The license covers the text, and the images are separate | Treating one license as covering all items |
| "The license is CC BY-NC-SA." | The text is CC BY-SA, with no NC element | Confusing neighboring licenses |
| "The images may be reused freely with credit." | The images are © their owners unless marked | Ignoring a restriction |
| "The page is public, so it can be copied." | A public page is still protected by copyright, and the license sets the permissions | Equating public with free |
| "Adaptations may be shared under any license." | CC BY-SA requires adaptations to carry CC BY-SA | Missing the ShareAlike condition |

The next MicroSim practices the check. It shows one page statement and eight license claims that an agent made about it, and for each one you decide whether the agent read it correctly.

#### Diagram: License Misreading Checker

<details markdown="1">
<summary>License Misreading Checker</summary>
Type: microsim
**sim-id:** license-misreading-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight agent claims about a page's license is correct or a misreading, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** License Misreading, Hallucination, and the license sections of Chapter 2 (all defined in this chapter above this block or in Chapter 2).

**Evidence of Mastery:** For each claim the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Rereading the statement is exploration, not evidence.

**Misconceptions:** (1) One license on a page covers every item. (2) A public page may be copied. (3) CC BY-SA and CC BY-NC-SA are the same.

**Instructional Rationale:** Judging a license claim against a statement applies the Chapter 2 skill to an agent's output. Eight claims that fail in the five ways named in the chapter teach the learner to check each claim against the exact words.

**Content:**

The page statement, shown at all times (made up): "Text: CC BY-SA 4.0. Images: © their owners, used with permission, except where marked CC BY."

The two bins: Correct reading, and Misreading.

The eight claims:

| # | Claim made by the agent | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | The text is licensed CC BY-SA 4.0. | Correct reading | It matches the statement. |
| 2 | Everything on the page is CC BY-SA 4.0. | Misreading | The images carry other rights. |
| 3 | Adaptations of the text must be shared under CC BY-SA. | Correct reading | ShareAlike requires it. |
| 4 | The images may be reused freely with credit. | Misreading | The images are © their owners unless marked CC BY. |
| 5 | The license allows commercial use of the text. | Correct reading | CC BY-SA has no NonCommercial element. |
| 6 | The license is CC BY-NC-SA. | Misreading | The statement names CC BY-SA, with no NC element. |
| 7 | The images marked CC BY may be reused with credit. | Correct reading | CC BY allows reuse with credit. |
| 8 | Because the page is public, it can be copied without a license. | Misreading | A public page is still protected, and the license sets the permissions. |

**Provenance:** The statement and claims are made up for this chapter, and the sim labels them "illustrative examples". The license rules follow Chapter 2.

**Rules:** Each claim has exactly one correct bin, four per bin.

**Learner Activity:**

1. The learner sees the page statement and one claim.
2. The learner places the claim in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After claim 8 the sim shows the summary.

**Feedback:** 8 claims in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is a [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can check an agent's license reading." Below 7 it lists the Why text of each missed claim.

**Starting State:** The page statement and claim 1 or the first claim in the shuffled order. The question shown is "Did the agent read the license correctly?"

**Chapter Anchors:** The chapter lists five license misreadings: treating one license as covering all items, confusing neighboring licenses, ignoring a restriction, equating public with free, and missing ShareAlike.
</details>

## Overconfident Score

An **overconfident score** is a score that is higher or more certain than its evidence supports. It is the quietest error, because nothing in the report is invented. The agent simply gives a 9 for a metric it did not fully check, or a 10 where a careful reviewer would find a gap. Signs include a high score with no quoted evidence, a pass on a check that needs a tool when no tool log is attached, an empty list of checks not verified when some checks could not have been verified from the text, and round scores of 9 and 10 across many metrics.

The rubric's own rules offer the remedy, and Chapter 12's prompt built it in. A check that was not tested counts as failed. A check that cannot be verified is marked "not checkable", and it is listed. A score of 10 requires every check to pass. When a report follows those rules, a high score is earned and shows its evidence. When it does not, a reviewer lowers the score to what the evidence supports.

**Worked example: a 9 that should be a 5.** The agent gave accessibility a 9. The human reviewer scored it 5.

| What the agent reported | What the evidence supports |
|---|---|
| "Images have alt text" with no count | The count is 4 of 5, and 2 of the 4 are one word |
| "Video is accessible" with no quote | The video has no captions, which is a serious failure |
| "Contrast is fine" with no tool log | The contrast was never tested, so the check counts as failed |
| Checks not verified: an empty list | Several checks were never verified |
| Score: 9 | Five checks pass, which gives a score of 5 |

A quick test works on any report: recompute the band from the agent's own checks. The agent lists its ten checks, the number that pass is divided by ten, and the share sets the band by the rule of Chapter 3. If 6 of 10 checks pass, the share is 60 percent, which is the Adequate band of 5 to 6, and a reported 8 is overconfident by at least two points. The test needs no outside source, only the report itself, and it catches a mismatch between the agent's evidence and its own score.

### Score Inflation

**Score inflation** is a systematic tendency of an agent to score higher than careful human reviewers, across many metrics and many resources. It differs from a single overconfident score, since inflation is a pattern. An agent that is a little generous on every metric produces totals that are too high, which can lift a resource across the adoption threshold that a human would not cross. It shows up as a positive average difference between agent and human scores, which the section on mean absolute difference later calls the bias. The fix is a stricter prompt, the "untested counts as failed" rule, and calibration against human scores, as the second half of the chapter explains.

The MicroSim below practices the detection. It shows six metric results from agents, and for each one you decide whether the score is plausible or overconfident.

#### Diagram: Overconfident Score Detector

<details markdown="1">
<summary>Overconfident Score Detector</summary>
Type: microsim
**sim-id:** overconfident-score-detector<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** examine<br/>
**Learning Objective:** The learner will examine the score, evidence, tool log, and unverified list of each of six agent results and decide whether the score is plausible or overconfident, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Overconfident Score, Score Inflation, Agent Scoring (defined in Chapter 12) (all defined in this chapter above this block or in Chapter 12).

**Evidence of Mastery:** For each result the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the rule is exploration, not evidence.

**Misconceptions:** (1) A high score is always suspect. (2) A detailed paragraph is evidence. (3) An empty unverified list means everything was verified.

**Instructional Rationale:** Examining a result for the match between score and evidence is an Analyze-level action. Results with high scores and strong evidence teach the learner that a high score is not itself a warning, and results with weak evidence teach them what is.

**Content:**

The rule, shown at all times: a result is Overconfident when its score is >= 9 and at least one of these holds: no specific evidence is quoted; a check that needs a tool was marked passed with no tool log; or the unverified list is empty although some checks cannot be verified from the text. Otherwise it is Plausible.

The two bins: Plausible, and Overconfident.

The six results (all made up, for Watershed Basics):

| # | Metric and score | What the result shows | Correct bin | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Open license, 9 | Evidence names the footer on 6 of 6 pages and an image with no notice. A license scan log is attached. The unverified list is empty. | Plausible | The score has exact evidence and a tool log. |
| 2 | Accessibility, 9 | Evidence says "looks accessible". No tool log. The unverified list is empty. | Overconfident | The score has no specific evidence, and the contrast and caption checks were never run. |
| 3 | Readability, 8 | A readability tool log with three grade levels is attached. The unverified list is empty. | Plausible | The score is < 9, and it rests on a tool log. |
| 4 | Portability, 10 | Evidence says "works everywhere". No test log. | Overconfident | A 10 with no test evidence cannot be earned. |
| 5 | Accuracy and currency, 6 | Evidence quotes 10 facts checked with 2 mismatches. The unverified list names the link checks. | Plausible | The score is < 9, and the report lists what it could not verify. |
| 6 | Editable source, 9 | The evidence lists the source files and all ten check results. The unverified list is empty. | Plausible | The score has exact evidence and a complete check list. |

**Provenance:** The results are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The rule follows the chapter section "Overconfident Score".

**Rules:** Each result has exactly one correct bin. Two results are Overconfident and four are Plausible.

**Learner Activity:**

1. The learner sees one result and the rule.
2. The learner places the result in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After result 6 the sim shows the summary.

**Feedback:** 6 results in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can spot a score that outruns its evidence." Below 5 it lists the Why text of each missed result.

**Starting State:** The first result and the rule. The question shown is "Does the evidence support this score?"

**Chapter Anchors:** The chapter says an overconfident score is higher than its evidence supports, and that a check not tested counts as failed and a score of 10 requires every check to pass.
</details>

## Agent Error Type

An **agent error type** is a category of mistake that an agent makes, used to organize what a reviewer finds. Naming the type tells the reviewer how to catch it and tells the prompt writer how to fix it. This book uses four types, which match the errors a reviewer meets most often.

| Type | What it looks like | How to catch it |
|---|---|---|
| Factual error | A wrong claim about the resource, such as a feature that is absent or a count that is off | Open the resource and check the claim |
| License error | A wrong reading of the resource's license, or a missed or mismatched license | Compare the claim with the statement itself |
| Citation error | A reference that does not exist or does not support its claim | Look up the source and read the passage |
| Scoring error | A score that does not follow from the agent's own checks, or arithmetic that does not add up | Recount the passes, recompute the band, and re-add the total |

Each type also points to a fix in the prompt, which is why the type is worth naming. The log of a calibration run, described later in this chapter, shows which type is most common, and that tells the prompt writer where to spend effort.

| Type | Typical fix in the prompt |
|---|---|
| Factual error | Require a quotation or a location for every claim, and a tool log for every measurement |
| License error | Require the license statement quoted word for word, and "not stated" for anything it does not mention |
| Citation error | Allow only sources found in the resource or supplied by the reviewer |
| Scoring error | Ask for the list of checks with a pass or fail on each, and have a spreadsheet or script add the total |

A fifth case is useful to name: a claim by the agent that turns out to be correct is *not an error*. Reviewers who see only mistakes become suspicious of everything, and an accurate record of what the agent got right is as useful as a list of what it got wrong.

The next MicroSim practices the naming. It shows ten findings from reviews of agent reports, and for each one you choose its type or decide that it is not an error.

#### Diagram: Agent Error Type Sorter

<details markdown="1">
<summary>Agent Error Type Sorter</summary>
Type: microsim
**sim-id:** agent-error-type-sorter<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** differentiate<br/>
**Learning Objective:** The learner will differentiate four agent error types and the no-error case by sorting each of ten findings, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Agent Error Type, Hallucination, Invented Citation, License Misreading, Overconfident Score (all defined in this chapter above this block).

**Evidence of Mastery:** For each finding the learner commits one of five bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the type table is exploration, not evidence.

**Misconceptions:** (1) A wrong score is always a scoring error. (2) A hallucinated feature is a citation error. (3) Every finding is an error.

**Instructional Rationale:** Differentiating among categories is an Analyze-level action. Ten findings that include two no-error cases and look alike on the surface teach the learner to name the specific kind of failure.

**Content:**

The five bins: Factual error, License error, Citation error, Scoring error, Not an error.

The ten findings:

| # | Finding shown to the learner | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | The agent says the video has captions, and it has none. | Factual error | It is a wrong claim about the resource. |
| 2 | The agent says the footer license is CC BY-NC, and it is CC BY. | License error | It misreads the license. |
| 3 | The agent cites a paper that does not exist. | Citation error | The reference is invented. |
| 4 | The agent's table lists five passes and it reports a score of 8, where the bands give 5 or 6. | Scoring error | The score does not follow from its own checks. |
| 5 | The agent says 4 of 5 images have alt text, and the true count is 4 of 5. | Not an error | The claim is correct. |
| 6 | The agent attributes the lake depth to a fact sheet that gives a different figure. | Citation error | The source does not support the claim. |
| 7 | The agent reports a total of 71, and the ten scores add to 68. | Scoring error | The arithmetic is wrong. |
| 8 | The agent says the resource has no license, and a footer states CC BY 4.0. | License error | It misses a license that is there. |
| 9 | The agent says the reading states three outcomes, and it states three. | Not an error | The claim is correct. |
| 10 | The agent says the quiz has 12 questions, and it has 8. | Factual error | It is a wrong claim about the resource. |

**Provenance:** The findings are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The types follow the chapter section "Agent Error Type".

**Rules:** Each finding has exactly one correct bin, two per bin.

**Learner Activity:**

1. The learner sees one finding and the five bins.
2. The learner may open the type table. Opening it does not change the score.
3. The learner places the finding in a bin, and the placement is committed.
4. The sim shows whether it was correct and the Why text.
5. After finding 10 the sim shows the summary.

**Feedback:** 10 findings in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This is [bin]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can name an agent's mistake." Below 9 it lists the Why text of each missed finding.

**Starting State:** The first finding and the five bins. The question shown is "What type of error is this, if any?"

**Chapter Anchors:** The chapter lists four error types: factual, license, citation, and scoring, and names a fifth case, a correct claim, as not an error.
</details>

The poster below pulls the error types together on one picture. It shows an agent's report with five places where a reviewer checks first, and each marker names the check and the error it catches.

#### Diagram: Agent Report Checkpoints

<details markdown="1">
<summary>Agent Report Checkpoints</summary>
Type: infographic
**sim-id:** agent-report-checkpoints<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the five places in an agent's report where a reviewer checks for errors, and the error each place catches, with at least 4 of 5 correct on the first attempt.

**Prerequisites:** Hallucination, Invented Citation, License Misreading, Overconfident Score, Agent Error Type (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 4 of 5 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) A report needs checking only at its score. (2) One check catches every kind of error. (3) A report with a tool log needs no checking.

**Instructional Rationale:** Identifying where each error type hides is a Remember-level task, and a picture of one report with five marked places gives each check a location. The quiz asks the learner to recognize a place by its look.

**Content:**

The illustration is a text-free flat drawing of a one-page report. The top of the page has a row of ten small boxes with a bar chart icon above them. Below it is a block of three thin lines, the first with a magnifying glass icon at its left. Below that is a line with a small book icon and a chain-link icon. Next is a line with a circled copyright symbol. Next is a large box holding one big digit, with a small empty tray beside it. At the bottom is a line of ten small boxes joined by plus signs and ending in an equals sign and a wider box. The five markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Quoted evidence | The block of three thin lines with a magnifying glass icon at its left. | A quotation or fact that the agent says it found in the resource. It can hide a hallucination. | Search the resource for the exact words. |
| 2 | Citation | The line with a small book icon and a chain-link icon. | A reference that the agent offers as support. It can hide an invented citation. | Look up the source and read the supporting passage. |
| 3 | License claim | The line with a circled copyright symbol. | What the agent says the license is and allows. It can hide a license misreading. | Compare the claim with the license statement on the page. |
| 4 | Score and tool log | The large box holding one big digit, with a small empty tray beside it. | A score and the tool log behind it. An empty tray beside a high score can mean an overconfident score. | Ask for the tool log, and lower any score the evidence does not support. |
| 5 | Total | The bottom line of ten small boxes joined by plus signs. | The ten scores and their sum. A wrong sum is a scoring error. | Add the ten scores yourself. |

**Provenance:** The five checkpoints follow the chapter sections "Hallucination", "Invented Citation", "License Misreading", "Overconfident Score", and "Agent Error Type". The illustration is synthetic, and the sim labels the report "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 5 in the order of the table, from the middle of the page to its bottom.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 5 hints the sim shows the summary.

**Feedback:** 5 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You know where to look in an agent's report." Below 4 it lists the labels of the missed checkpoints.

**Starting State:** The illustration with five numbered markers, explore mode active, and the prompt "Hover a marker to see what it checks."

**Chapter Anchors:** The chapter names four error types and the checks that catch them. The poster places a check for each one on the page of a report: quotations, citations, license claims, scores, and the total.
</details>

## Verification Step

A **verification step** is a defined action a person takes to confirm or refute one claim in an agent's report. A step names the claim, the way to test it, and what result would confirm it. Verification steps get stronger as they move away from the agent's own words. The weakest is to ask the agent whether it is sure, which proves nothing. Better is to recompute arithmetic from the table. Better still is to run a tool and read its log. The strongest is to open the actual source, such as the resource's page or a cited paper, and see for yourself. The ladder ranks the common steps by how much each one proves.

| Step | What it proves | Strength |
|---|---|---|
| Ask the agent whether it is sure | Nothing, since the same model answers again | Weakest |
| Recompute the arithmetic from the report's own table | The totals follow from the scores | Weak |
| Run a tool and read its log | A measurement is real and can be repeated | Strong |
| Open the resource and find the quoted text | The evidence exists where the agent says | Strong |
| Open the cited source and read the passage | The source exists and supports the claim | Strongest |

A good verification step has four parts. State the claim in its exact words. Say how to test it, such as the tool to run or the page to open. Record what you found, with a date. And mark the result: confirmed, or not confirmed.

**Worked example: three verification steps.**

| Claim | How to test it | Result recorded |
|---|---|---|
| "4 of 5 images have alt text" | Open the page source and count the images and their alt attributes | Confirmed: 4 of 5 |
| "The total is 65" | Add the ten scores in the table | Confirmed: 65 |
| "The footer states CC BY 4.0 on all six pages" | Open each page and read the footer | Not confirmed: the footer is missing on page 4 |

### Spot Check

A **spot check** is the verification of a sample of an agent's claims and not all of them. It saves effort where the agent's work is well evidenced and the risk is low. A good sample is not random alone. It includes at least one claim from each metric, every claim that carries a lot of weight, such as one that decides a band or a floor, and a few chosen at random. If the sample turns up an error, widen it: an error in a sample suggests more errors outside it. Record which claims were checked, so that the report says what was and was not verified.

### Source Verification

**Source verification** is the verification of a claim by going to the original source and not to the agent's summary of it. It is the strongest verification step. For a license claim, the original source is the license statement on the page. For a fact, it is the cited reference, opened and read. For a measurement, it is the tool's own log. Source verification is the antidote to invented citations and hallucinated quotations, because an invented source cannot be opened. It takes longer than a spot check, so a reviewer reserves it for the claims that decide the outcome.

!!! mascot-tip "Check the Claims That Decide the Outcome First"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    If you only have time to verify five claims, verify the ones that would change the band or the decision, such as the lowest metric and any score that sits at the edge of a band. A mistake there costs the most.

## Second-Agent Cross-Check

A **second-agent cross-check** is the use of a second agent to review the first agent's report, looking for unsupported claims, missing evidence, and arithmetic that does not add up. The second agent gets the resource, the first agent's report, and a prompt that asks for faults, not for a fresh score. It is a cheap first filter. It catches many errors that a person would otherwise find by hand, such as a quotation that is not in the text, and it can run on every report.

It has the limit that Chapter 13 noted. A second agent built on the same kind of model can share the first one's blind spots, so it may miss the same errors, and it may also raise false alarms that waste a person's time. A cross-check narrows the list of things to verify and does not replace verification.

**Worked example: a cross-check on five known errors.** A reviewer planted five known errors in a draft report and asked a second agent to find faults.

| Result | Count |
|---|---|
| Real errors the second agent flagged | 3 of 5 |
| Real errors the second agent missed | 2 of 5 |
| Flags that were false alarms | 1 |

The cross-check found 60 percent of the real errors and raised one false alarm. A person would still need to check the other two errors and the alarm, and the cross-check cut the list down.

## Agent Disagreement

**Agent disagreement** is a difference in the scores or findings of two agents, or of an agent and a human, on the same metric. It is information. A disagreement shows where the evidence is unclear, where an agent may have erred, or where a check in the rubric is ambiguous. Handle it the way Chapter 11 handled disagreement between human reviewers: ask for the evidence on each side, repeat the check, and decide by what the evidence supports. The agent's score does not win because it came from a machine, and it does not lose for the same reason. A disagreement that traces to an unclear check is also a finding about the rubric, and it belongs in the notes for the rubric's owner. The next section gives the three outcomes that a disagreement, or any other checked claim, can end in.

## Accept, Correct, or Reject

**Accept, correct, or reject** names the three outcomes of checking one claim from an agent's report. A claim is **accepted** when verification shows it is true as stated. It is **corrected** when it is right in substance and a detail is wrong, as when a count is off by one: the reviewer fixes the detail and notes the change. It is **rejected** when it is false, invented, or impossible to verify. A rejected claim is removed, and the score is recomputed without it, treating any check that rested on it as failed or not checkable.

**Worked example: six claims triaged.** The table shows what verification found and the decision.

| Agent claim | What verification found | Decision |
|---|---|---|
| "4 of 5 images have alt text" | The count is exactly 4 of 5 | Accept |
| "Reading level is grade 6.9" | The tool reports 7.1 | Correct to 7.1 |
| "The footer states CC BY 4.0 on all six pages" | The footer is on five of the six pages | Correct to five pages |
| "The video has captions" | The video has none | Reject |
| "Contrast tested at 5.2 to 1" | No tool was run | Reject |
| "Citation: Reyes (2021)" | No such article exists | Reject |

Two rules cover the hard cases. A claim that cannot be verified in the time available is not accepted: mark it "not verified", and treat the check that rests on it as failed or not checkable, as the rubric says. And a rejection changes the score, so recompute the score from the checks that remain.

**Worked example: rescoring after four rejections.** The agent gave Accessibility a 9 and reported 9 of its 10 checks as passed. Verification rejected four claims: the captions, the contrast test, the heading order, and alt text on every image. Each rejected claim turns a passed check into a failed one.

| Step | Value |
|---|---|
| Checks the agent reported as passed | 9 of 10 |
| Checks whose claims were rejected | 4 |
| Checks that still pass | 5 of 10 |
| Share of the check met | 50 percent, the Adequate band of 5 to 6 |
| Serious failure present | Yes, the video has no captions |
| Corrected score | 5, the lower number |

The corrected score of 5 matches the human reviewers' score for Accessibility, and the log records the four rejections as the reason for the change.

### Findings Log

A **findings log** is the record of every agent claim a reviewer checked and what was decided. Its columns are the agent's finding, the decision (accepted, corrected, or rejected), and the reason, as in the findings log of this book's sample rubric worksheet. The log serves three purposes. It makes the review auditable: anyone can see what was checked. It feeds the measurement in the next sections, since the share of rejected claims is the agent's error rate. And it feeds prompt refinement, because the rejected claims show which instructions the prompt needs.

### Agent Error Rate

The **agent error rate** is the share of the agent's checked claims that were corrected or rejected. To compute it, count the claims verified and the number that were not accepted as stated, and divide. If a reviewer verified 40 claims and 6 were corrected or rejected, the error rate is 6 divided by 40, which is 15 percent. A breakdown by error type is more useful than the total, since it shows where the agent fails: perhaps two citation errors, one license error, two overconfident scores, and one miscount. The rate is only as honest as the sample behind it. A rate from claims chosen because they looked suspicious overstates the agent's errors, and a rate from only the easy claims understates them.

The MicroSim below practices the three decisions. It shows eight claims with what verification found, and for each one you decide.

#### Diagram: Claim Triage Judge

<details markdown="1">
<summary>Claim Triage Judge</summary>
Type: microsim
**sim-id:** claim-triage-judge<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight verified agent claims should be accepted, corrected, or rejected, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Accept Correct or Reject, Verification Step, Spot Check, Source Verification, Findings Log (all defined in this chapter above this block).

**Evidence of Mastery:** For each claim the learner commits one of three decisions. A decision is correct when it matches the Correct decision column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the decision definitions is exploration, not evidence.

**Misconceptions:** (1) A claim that is almost right is rejected. (2) A claim that cannot be verified is accepted. (3) A corrected claim needs no note.

**Instructional Rationale:** Judging what to do with a verified claim is an Evaluate-level action that reviewers repeat dozens of times in a review. Eight claims split across the three decisions teach the learner the dividing lines.

**Content:**

The three decisions: Accept (verified as stated), Correct (right in substance with one detail wrong, so fix the detail and log it), Reject (false, invented, or unverifiable, so remove it and rescore without it).

The eight claims (all made up, for Watershed Basics):

| # | Agent claim | What verification found | Correct decision | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | "4 of 5 images have alt text." | The count is exactly 4 of 5. | Accept | It is true as stated. |
| 2 | "Reading level is grade 6.9." | The tool reports 7.1. | Correct | The claim is right in substance and the number is wrong. |
| 3 | "Citation: Reyes (2021), Soil Infiltration Rates." | No such article exists. | Reject | The reference is invented. |
| 4 | "The footer states CC BY 4.0 on 6 of 6 pages." | The footer is on 5 of 6 pages. | Correct | The license is right and the page count is wrong. |
| 5 | "The video has captions." | The video has no captions. | Reject | The claim is false. |
| 6 | "Heading order is correct." | One heading skips from level 2 to level 4. | Reject | The claim is false, and the defect is recorded as a new finding. |
| 7 | "Contrast tested at 5.2 to 1." | No tool was run. | Reject | The measurement is invented. |
| 8 | "The author is named as Maria Lopez." | The page names Maria Lopez. | Accept | It is true as stated. |

**Provenance:** The claims are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The decisions follow the chapter section "Accept, Correct, or Reject".

**Rules:** Each claim has exactly one correct decision. Two are Accept, two are Correct, and four are Reject.

**Learner Activity:**

1. The learner sees one claim with what verification found, and the three decisions.
2. The learner chooses a decision, and the choice is committed.
3. The sim shows whether it was correct and the Why text.
4. After claim 8 the sim shows the summary.

**Feedback:** 8 claims in a shuffled order, one attempt each. Correct: "Correct: [decision]. [Why]". Incorrect: "Not quite. The decision is [decision]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can triage an agent's claims." Below 7 it lists the Why text of each missed claim.

**Starting State:** The first claim, what verification found, and the three decisions. The question shown is "What should the reviewer do with this claim?"

**Chapter Anchors:** The chapter's worked example triages six claims and agrees with this sim: a correct count is accepted, a number that is off is corrected, and an invented citation, a false claim, and an invented measurement are rejected.
</details>

---

## Measuring Agreement With Human Reviewers

Checking claims one by one tells you whether a single report can be trusted. To decide whether an agent can be trusted as a first pass over many resources, you need to measure how closely it agrees with careful human reviewers. The measures in this part are all simple. They use the ten metric scores from Chapter 3, and each one answers a different question, so a reviewer needs more than one.

The running example is *Watershed Basics*. A pair of careful human reviewers reached the consensus scores below, and the table adds three agents that scored the same resource. Agent A1 is a first-draft prompt. Agent A2 is the same prompt after the refinement that the last section describes. Agent A3 is a different tool with a looser prompt.

| Metric | Human consensus | Agent A1 | Agent A2 | Agent A3 |
|---|---|---|---|---|
| Accuracy and currency | 7 | 8 | 7 | 5 |
| Alignment | 6 | 7 | 5 | 6 |
| Readability | 8 | 9 | 8 | 8 |
| Accessibility | 5 | 6 | 5 | 8 |
| Practice with feedback | 6 | 7 | 6 | 3 |
| Open license | 9 | 10 | 10 | 9 |
| Modularity | 5 | 6 | 5 | 7 |
| Metadata | 4 | 5 | 4 | 4 |
| Editable source | 8 | 9 | 8 | 6 |
| Portability | 7 | 8 | 6 | 9 |
| **Total** | **65** | **75** | **64** | **65** |

Under the provisional adoption rule of Chapter 11, a resource is adopted when its total is at least 75 and every metric is at least 5. The humans' total of 65, with Metadata at 4, means *Revise*. Agent A1 reaches 75 with every metric at least 5, so its report says *Adopt*. The other two agents say *Revise*. Keep this table in view, because every measure below describes how these three agents relate to the humans.

### Score Difference Threshold

A **score difference threshold** is the largest gap between an agent's score and the human score that still counts as agreement on a metric. A gap at or below the threshold is agreement. A larger gap is a disagreement. The threshold is a choice, and it should be made before the numbers are seen, because a threshold chosen afterward can make any agent look good.

Chapter 11 used a threshold of 3 to flag a metric on which two human reviewers needed to talk. That is a loose setting, which suits a conversation between two people who both read the evidence. A tighter setting suits the question of whether an agent can replace a first human pass. The descriptor bands give a reason. They are two points wide (1 to 2, 3 to 4, 5 to 6, 7 to 8, 9 to 10), so a difference of 2 or more always moves a score into a different band, and a difference of 1 sometimes does. This book uses a threshold of 1 for calibration, and it labels that number a provisional teaching choice that each team should confirm for its own use.

### Agreement Rate

The **agreement rate** is the share of metrics on which the agent's score is within the threshold of the human score. Count the metrics that agree, divide by the number of metrics, and write the result as a percentage. If 8 of 10 metrics agree, the agreement rate is 80 percent.

The threshold changes the answer, so always report both. The table gives the number of the ten metrics that agree for each agent at four thresholds.

| Threshold | Agent A1 | Agent A2 | Agent A3 |
|---|---|---|---|
| 0 (exact match) | 0 of 10 | 7 of 10 | 4 of 10 |
| 1 | 10 of 10 | 10 of 10 | 4 of 10 |
| 2 | 10 of 10 | 10 of 10 | 8 of 10 |
| 3 | 10 of 10 | 10 of 10 | 10 of 10 |

At the loose threshold of 3, all three agents agree on every metric, and the measure cannot tell them apart. At a threshold of 1, Agent A3 falls to 40 percent while A1 and A2 stay at 100 percent. The agreement rate is easy to read and it has two weaknesses. It says nothing about the direction of the differences, so it cannot tell a generous agent from a harsh one. And it treats a gap of 1 and a gap of 0 as the same, which hides how large the typical difference is. The next two measures fill those gaps.

### Mean Absolute Difference

The **mean absolute difference** is the average size of the gap between agent and human, ignoring direction. For each metric, take the difference between the agent's score and the human score and drop the sign. Then average the ten values. A value near 0 means the agent's scores sit close to the humans'. Because the unit is the score itself, a mean absolute difference of 1.4 reads as "typically 1.4 points away".

A companion measure keeps the sign. The **bias** is the average of the signed differences, agent minus human. A positive bias means the agent is generous and a negative one means it is harsh. This is the number that detects score inflation. The two measures together describe both the size and the direction of the gaps.

**Worked example: three agents against the humans.**

| Agent | Differences, in table order | Mean absolute difference | Bias |
|---|---|---|---|
| A1 | +1, +1, +1, +1, +1, +1, +1, +1, +1, +1 | 1.0 | +1.0 |
| A2 | 0, -1, 0, 0, 0, +1, 0, 0, 0, -1 | 0.3 | -0.1 |
| A3 | -2, 0, 0, +3, -3, 0, +2, 0, -2, +2 | 1.4 | 0.0 |

Agent A1 is off by exactly one point on every metric, always upward, so its bias equals its mean absolute difference. Agent A3 has a bias of zero, because its overshoots and undershoots cancel, and its mean absolute difference of 1.4 shows that the cancelling hides large errors. A bias near zero never proves an agent is accurate.

### Score Correlation

The **score correlation** measures how well the agent's scores rise and fall together with the human scores across the metrics. It is a number from -1 to 1. A value near 1 means that metrics the humans scored high are also scored high by the agent, and metrics the humans scored low are scored low. A value near 0 means the agent's pattern has little to do with the humans'. Spreadsheets compute it with the CORREL function, and this chapter uses the standard Pearson correlation.

Correlation checks the *pattern*, and it ignores the *level*. If an agent adds exactly one point to every human score, the pattern is identical, and the correlation is exactly 1. That is a weakness, since the agent is wrong on every metric. It makes correlation a useful second measure and a poor only measure.

**Worked example: what correlation sees.**

| Agent | Correlation with the humans | What it says |
|---|---|---|
| A1 | 1.00 | The pattern matches exactly, and the level is one point too high |
| A2 | 0.96 | The pattern matches closely |
| A3 | 0.46 | The pattern matches weakly |

The three agents also teach a second lesson about totals. Agent A3's total is 65, the same as the humans', and its metric scores are poor. Matching the total says little about matching the scores that produce it, since high and low errors cancel in a sum.

!!! mascot-thinking "One Number Is Never Enough"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Agent A1 has a perfect correlation and a wrong adoption decision. Agent A3 has a perfect total and large errors on single metrics. Ask each measure what it can and cannot see, and read them together.

The MicroSim below lets you see this directly. You change the threshold and watch the measures for the three agents.

#### Diagram: Agent-Human Agreement Explorer

<details markdown="1">
<summary>Agent-Human Agreement Explorer</summary>
Type: microsim
**sim-id:** agent-human-agreement-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Analyze<br/>
**Bloom Verb:** compare<br/>
**Learning Objective:** The learner will compare agreement rate, mean absolute difference, bias, and correlation for three agents against human scores, and answer 6 of 6 questions on what each measure can and cannot detect, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Score Difference Threshold, Agreement Rate, Mean Absolute Difference, Score Correlation, Score Inflation (all defined in this chapter above this block).

**Evidence of Mastery:** The learner answers six questions after exploring. An answer is correct when it matches the Correct answer column in Content. Mastery is at least 5 of 6 correct on the first attempt. Moving the threshold control is exploration, not evidence.

**Misconceptions:** (1) A perfect correlation means the agent is accurate. (2) A matching total means the metric scores match. (3) A loose threshold shows that agents are equally good.

**Instructional Rationale:** Comparing several measures on the same data is an Analyze-level action. Three agents built so that each measure misses a different failure teach the learner that each measure has a blind spot.

**Content:**

The data, shown as a table at all times (the human consensus and three agents, made up for the book's running example, Watershed Basics):

| Metric | Human | A1 | A2 | A3 |
|---|---|---|---|---|
| Accuracy and currency | 7 | 8 | 7 | 5 |
| Alignment | 6 | 7 | 5 | 6 |
| Readability | 8 | 9 | 8 | 8 |
| Accessibility | 5 | 6 | 5 | 8 |
| Practice with feedback | 6 | 7 | 6 | 3 |
| Open license | 9 | 10 | 10 | 9 |
| Modularity | 5 | 6 | 5 | 7 |
| Metadata | 4 | 5 | 4 | 4 |
| Editable source | 8 | 9 | 8 | 6 |
| Portability | 7 | 8 | 6 | 9 |
| Total | 65 | 75 | 64 | 65 |

The threshold control takes the values 0, 1, 2, and 3. For each agent the sim shows the number of metrics within the threshold of the human score, and these values that do not depend on the threshold:

| Agent | Mean absolute difference | Bias | Correlation | Total | Adoption decision |
|---|---|---|---|---|---|
| A1 | 1.0 | +1.0 | 1.00 | 75 | Adopt |
| A2 | 0.3 | -0.1 | 0.96 | 64 | Revise |
| A3 | 1.4 | 0.0 | 0.46 | 65 | Revise |

The adoption decision rule: Adopt when the total >= 75 and every metric >= 5. Revise when the total >= 50 and the resource is not Adopt. Reject when the total < 50. The human decision is Revise.

Metrics within the threshold, by threshold:

| Threshold | A1 | A2 | A3 |
|---|---|---|---|
| 0 | 0 of 10 | 7 of 10 | 4 of 10 |
| 1 | 10 of 10 | 10 of 10 | 4 of 10 |
| 2 | 10 of 10 | 10 of 10 | 8 of 10 |
| 3 | 10 of 10 | 10 of 10 | 10 of 10 |

The six questions:

| # | Question | Choices | Correct answer | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | At a threshold of 3, which agents agree with the humans on all ten metrics? | A1 only; A2 only; A3 only; All three | All three | Every gap is 3 or less, so a loose threshold cannot separate the agents. |
| 2 | At a threshold of 1, which agent has the lowest agreement rate? | A1; A2; A3 | A3 | A3 agrees on 4 of 10 metrics. |
| 3 | Which measure shows that A1 is generous? | Agreement rate at threshold 1; Correlation; Bias | Bias | The bias is +1.0, while its agreement rate is 100 percent and its correlation is 1.00. |
| 4 | Which agent's total matches the humans' total? | A1; A2; A3 | A3 | A3's total is 65, the same as the humans'. A2's is 64. |
| 5 | Which agent has a bias of zero and still makes large errors? | A1; A2; A3 | A3 | Its overshoots and undershoots cancel, and its mean absolute difference is 1.4. |
| 6 | Which agent changes the adoption decision? | A1; A2; A3 | A1 | A1's total of 75 with every metric at least 5 gives Adopt, and the humans' result is Revise. |

**Provenance:** The scores are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The measures follow the chapter sections "Agreement Rate", "Mean Absolute Difference", and "Score Correlation".

**Rules:** All numbers come from the tables above and are computed from the data table. The correlation is the Pearson correlation of the ten agent scores with the ten human scores.

**Learner Activity:**

1. The learner moves the threshold control and watches the metrics-within-threshold counts change.
2. The learner reads the fixed measures for each agent.
3. The learner presses Quiz and answers the six questions, one at a time.
4. After question 6 the sim shows the summary.

**Feedback:** 6 questions in the order of the table, one attempt each. Correct: "Correct: [answer]. [Why]". Incorrect: "Not quite. The answer is [answer]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read agreement measures together." Below 5 it lists the Why text of each missed question.

**Starting State:** The data table, the threshold control at 1, and the three agents' measures.

**Chapter Anchors:** The chapter's tables for the three agents at four thresholds, their differences and bias, and their correlations use the same numbers as this sim.
</details>

### Cohen's Kappa

Agreement rate has another weakness, which is that some of the agreement happens by chance. If two people each say "not ready" about nearly every resource, they will agree most of the time even if neither one looks at the resource. **Cohen's kappa** corrects for this. It compares the agreement actually seen with the agreement expected by chance, given how often each side uses each answer. Kappa is the standard measure when the answers fall in categories, such as "ready to adopt" or "not ready", and when the categories are not used equally often.

The calculation has three steps. Write the observed agreement, called po, as the share of cases on which agent and human gave the same answer. Write the chance agreement, called pe, as the sum over the categories of the agent's share of that category times the human's share of that category. Then kappa is the difference between the two, divided by the room above chance:

kappa = (po - pe) / (1 - pe)

A kappa of 1 means perfect agreement, 0 means no more agreement than chance, and a negative value means less than chance. Commonly cited labels for the values between are slight, fair, moderate, substantial, and almost perfect. Treat the labels as rules of thumb and not as laws, and check the cutoffs against the source you cite before you quote them in a report.

**Worked example: 90 percent agreement and a kappa of 0.44.** A teacher compares an agent and a human on 20 resources, asking whether each one is ready to adopt. The table gives the counts.

| | Human: ready | Human: not ready | Agent total |
|---|---|---|---|
| **Agent: ready** | 1 | 1 | 2 |
| **Agent: not ready** | 1 | 17 | 18 |
| **Human total** | 2 | 18 | 20 |

1. Observed agreement po: the agent and human agree on 1 + 17 = 18 of 20 resources, which is 0.90.
2. Chance agreement pe: the agent says "ready" 2 of 20 times and the human says "ready" 2 of 20 times, so the chance of both saying ready is 0.10 times 0.10 = 0.01. The agent says "not ready" 18 of 20 times and the human does too, so the chance of both saying "not ready" is 0.90 times 0.90 = 0.81. The two add to 0.82.
3. Kappa: (0.90 - 0.82) / (1 - 0.82) = 0.08 / 0.18, which is 0.44.

The agreement rate of 90 percent sounds excellent, and kappa of 0.44 tells a more honest story. Two raters who answered "not ready" at random 90 percent of the time would agree 82 percent of the time, so most of the 90 percent is not skill. And the agent found only one of the two resources that the human judged ready.

!!! mascot-tip "Report the Counts Behind the Statistic"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Always show the small table of counts next to a kappa, so a reader can see which cell the disagreements fall in. A single number can hide the error that matters most.

The MicroSim below practices the calculation. You get a table of counts and work out the three numbers, then see how kappa moves as the counts change.

#### Diagram: Kappa Calculator

<details markdown="1">
<summary>Kappa Calculator</summary>
Type: microsim
**sim-id:** kappa-calculator<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate observed agreement, chance agreement, and Cohen's kappa from a table of counts for five cases, with at least 4 of 5 kappa values correct to two decimal places on the first attempt.

**Prerequisites:** Cohen's Kappa, Agreement Rate (both defined in this chapter above this block).

**Evidence of Mastery:** For each case the learner enters po, pe, and kappa. A case is correct when kappa matches the Kappa column in Content to two decimal places. Mastery is at least 4 of 5 cases correct on the first attempt. Changing the counts in the free-play table is exploration, not evidence.

**Misconceptions:** (1) A high agreement rate means a high kappa. (2) Kappa cannot be below zero. (3) Chance agreement is always 50 percent.

**Instructional Rationale:** Calculating kappa by hand is an Apply-level action. Five cases that include a skewed table, a perfect table, a chance table, a modest table, and a worse-than-chance table show the whole range of the measure.

**Content:**

The formula, shown at all times: po = (both ready + both not ready) / total. pe = (agent ready share x human ready share) + (agent not ready share x human not ready share). kappa = (po - pe) / (1 - pe).

The question for every case: "An agent and a human each judged whether resources are ready to adopt."

The five cases (the four counts are: both ready, agent ready and human not ready, agent not ready and human ready, both not ready):

| # | Both ready | Agent ready, human not | Agent not, human ready | Both not ready | po | pe | Kappa | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 17 | 0.90 | 0.82 | 0.44 | Most agreement is expected by chance, because almost everything is not ready. |
| 2 | 10 | 0 | 0 | 10 | 1.00 | 0.50 | 1.00 | The two always agree. |
| 3 | 5 | 5 | 5 | 5 | 0.50 | 0.50 | 0.00 | The agreement equals what chance gives. |
| 4 | 8 | 2 | 2 | 8 | 0.80 | 0.50 | 0.60 | The agreement is well above chance. |
| 5 | 2 | 8 | 8 | 2 | 0.20 | 0.50 | -0.60 | They agree less than chance, so they tend to answer in opposite ways. |

The kappa labels used for feedback (commonly cited, labeled "rule of thumb" in the sim): kappa < 0 is Poor, 0 to 0.20 is Slight, 0.21 to 0.40 is Fair, 0.41 to 0.60 is Moderate, 0.61 to 0.80 is Substantial, and 0.81 to 1.00 is Almost perfect.

**Provenance:** The counts are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The labels are the commonly cited descriptions of Landis and Koch (1977), and the sim marks them "rule of thumb, verify before citing".

**Rules:** Each case has 20 resources. po, pe, and kappa follow the formula and are rounded to two decimal places. An answer is correct when it matches the table to two decimal places. Kappa is not defined when pe equals 1, and none of the five cases has that value.

**Learner Activity:**

1. The learner sees one table of counts and the formula.
2. The learner enters po, pe, and kappa in three fields and presses Check.
3. The sim shows which of the three numbers are correct, and the Why text.
4. After case 5 the sim shows the summary.
5. The learner may then open free play, where the four counts can be changed and po, pe, kappa, and the label update. Free play does not count as evidence.

**Feedback:** 5 cases in a shuffled order, one attempt each. Correct: "Correct: kappa is [value], which is [label]. [Why]". Incorrect: "Not quite. po is [po], pe is [pe], and kappa is [value]. [Why]". The summary shows "[n] of 5 correct on the first attempt". At 4 or more it adds "You can calculate kappa." Below 4 it lists the Why text of each missed case.

**Starting State:** Case 1 or the first case in the shuffled order, with the formula and empty fields.

**Chapter Anchors:** The chapter's worked example of 20 resources with 90 percent agreement and a kappa of 0.44 is case 1. The chapter's formula and labels are the same as in this sim.
</details>

## Calibration Against Humans

**Calibration against humans** is the process of testing an agent's scores against careful human scores on a set of resources, then adjusting the prompt until the two agree well enough for the agent's purpose. It is how an agent earns the trust that a teacher is asked to place in it. It follows the logic of any measuring instrument: before you rely on a scale, you weigh something of known weight.

A calibration run has six steps.

1. **Build a calibration set.** Choose 10 to 20 resources that cover the range you expect, from poor to excellent. Have two or more trained humans score each one, and reach a consensus score by the method of Chapter 11. Keep the scores hidden from the agent.
2. **Run the agent** with the prompt under test, and save every report.
3. **Compute the measures.** For each metric and for the adoption decision, compute the agreement rate at the chosen threshold, the mean absolute difference, the bias, the correlation, and kappa for the decision.
4. **Find the largest disagreements** and trace each to a cause, using the error types from earlier in this chapter. Is a metric systematically too high? Does the agent skip a check?
5. **Refine the prompt** and rerun on the *same* set to see whether the measures move.
6. **Confirm on a fresh set.** A prompt tuned on one set can learn that set's quirks. Test the final prompt on resources it has not seen, and report that result.

Before the run, write down the standard the agent must meet. The numbers below are illustrative, and each team should set its own after a pilot.

| Measure | Illustrative standard for use as a first pass |
|---|---|
| Agreement rate at a threshold of 1 | 80 percent or more |
| Absolute value of the bias | 0.5 or less |
| Mean absolute difference | 1.0 or less |
| Kappa on the adoption decision | 0.61 or more |
| Run-to-run range on each metric | 1 or less, or the metric goes to a person |

An agent that meets the standard is used as a first pass, and a person still verifies the claims that decide the outcome. An agent that does not meet it is used only to draft evidence for a person to check.

!!! mascot-encourage "A First Run Rarely Passes"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    Do not be discouraged when the first calibration run shows a gap. The gap is the finding, and it tells you exactly where the prompt needs work.

### Prompt Refinement

**Prompt refinement** is the revision of a prompt in response to the errors found in calibration, followed by a rerun to see whether the errors shrink. Each change targets one observed error, so that its effect can be seen. Changing five things at once leaves you unable to tell which one helped.

**Worked example: from Agent A1 to Agent A2.** The calibration of Agent A1 found a bias of +1.0 and a changed adoption decision. The findings log traced the inflation to three causes, and each got one change to the prompt.

| Error found in the log | Change to the prompt | Effect on the next run |
|---|---|---|
| Contrast and caption checks were marked passed with no tool log | Added the rule "A check that needs a tool counts as failed unless a tool log is attached" | Accessibility fell from 6 to 5 |
| Scores of 9 and 10 given with no check list | Added the rule "A score of 10 requires all ten checks to pass, and list every check" | Alignment fell from 7 to 5, and Portability from 8 to 6 |
| The unverified list was empty on every metric | Added "List every check you could not verify from the text" | Metadata fell from 5 to 4 |

The same stricter rules also lowered Accuracy, Readability, Practice with feedback, Modularity, and Editable source by one point each, and left Open license at 10. After the changes, Agent A2 had a bias of -0.1, a mean absolute difference of 0.3, a total of 64, and the decision *Revise*, which matches the humans. It also now scores License at 10, one point above the humans, and that is a new finding for the next round, since a 10 needs all ten checks to pass.

### Run-to-Run Variance

**Run-to-run variance** is the variation in an agent's scores when it scores the same resource with the same prompt more than once. Language models do not always give the same answer twice. An agent that gives a 5 on one run and a 7 on the next is not measuring anything stable on that metric, however well its average agrees with the humans.

To measure it, run the agent several times on the same resource, five is a practical number, and for each metric record the lowest score, the highest score, and the range, which is the highest minus the lowest. A small range means a stable metric. A large range marks a metric to hand to a person. Taking the **median** of the runs, the middle value when they are sorted, also removes the effect of one odd run.

**Worked example: five runs on Watershed Basics.**

| Metric | Five runs | Range | Median | Human score | Verdict |
|---|---|---|---|---|---|
| Accuracy and currency | 7, 7, 7, 7, 7 | 0 | 7 | 7 | Stable |
| Alignment | 6, 6, 5, 6, 6 | 1 | 6 | 6 | Stable |
| Readability | 8, 8, 8, 9, 8 | 1 | 8 | 8 | Stable |
| Accessibility | 5, 6, 5, 7, 5 | 2 | 5 | 5 | Unstable |
| Practice with feedback | 4, 7, 6, 5, 8 | 4 | 6 | 6 | Unstable |
| Metadata | 4, 4, 4, 4, 4 | 0 | 4 | 4 | Stable |

The illustrative rule here is that a range of 1 or less is stable and a range of 2 or more is unstable. Accessibility and Practice with feedback go to a person, even though their medians happen to equal the human scores. That match, from five runs on one resource, is not a reason to trust a single run on the next one.

#### Diagram: Run Variance Checker

<details markdown="1">
<summary>Run Variance Checker</summary>
Type: microsim
**sim-id:** run-variance-checker<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the range and the median of five runs for each of six metrics and decide whether each metric is stable or unstable, with at least 5 of 6 metrics fully correct on the first attempt.

**Prerequisites:** Run-to-Run Variance, Agent Disagreement (both defined in this chapter above this block).

**Evidence of Mastery:** For each metric the learner enters the range, enters the median, and chooses Stable or Unstable. A metric is fully correct when all three match the Content table. Mastery is at least 5 of 6 metrics fully correct on the first attempt. Viewing the rule is exploration, not evidence.

**Misconceptions:** (1) An average that matches the humans means the agent is reliable. (2) One run is enough. (3) The median is the same as the average.

**Instructional Rationale:** Computing a range and a median is an Apply-level action. Metrics that include a stable one, a one-run outlier, and a wide spread teach the learner to look at the spread and not only the center.

**Content:**

The rule, shown at all times: the range is the highest run minus the lowest run. A metric is Stable when its range is <= 1 and Unstable when its range is >= 2. An unstable metric goes to a human reviewer.

The six metrics (all for the made-up resource Watershed Basics):

| # | Metric | Five runs | Range | Median | Verdict | Why (shown as feedback) |
|---|---|---|---|---|---|---|
| 1 | Accuracy and currency | 7, 7, 7, 7, 7 | 0 | 7 | Stable | All five runs agree. |
| 2 | Alignment | 6, 6, 5, 6, 6 | 1 | 6 | Stable | One run is a point lower, and the range is 1. |
| 3 | Readability | 8, 8, 8, 9, 8 | 1 | 8 | Stable | One run is a point higher, and the range is 1. |
| 4 | Accessibility | 5, 6, 5, 7, 5 | 2 | 5 | Unstable | The range is 2, so a person decides. |
| 5 | Practice with feedback | 4, 7, 6, 5, 8 | 4 | 6 | Unstable | The runs spread across five values. |
| 6 | Metadata | 4, 4, 4, 4, 4 | 0 | 4 | Stable | All five runs agree. |

**Provenance:** The runs are illustrative examples written for this chapter, and the sim labels them "illustrative examples". The stability rule is a teaching choice, and the sim labels it "illustrative threshold".

**Rules:** The median is the third value after the five runs are sorted. The range and median are whole numbers. A metric is fully correct only when the range, the median, and the verdict all match.

**Learner Activity:**

1. The learner sees one metric with its five runs and the rule.
2. The learner enters the range and the median, and chooses Stable or Unstable.
3. The learner presses Check, and the sim shows which of the three answers are correct and the Why text.
4. After metric 6 the sim shows the summary.

**Feedback:** 6 metrics in a shuffled order, one attempt each. Correct: "Correct: range [range], median [median], [verdict]. [Why]". Incorrect: "Not quite. The range is [range], the median is [median], and the metric is [verdict]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can tell a stable metric from an unstable one." Below 5 it lists the Why text of each missed metric.

**Starting State:** Metric 1 or the first metric in the shuffled order, with the rule and empty fields.

**Chapter Anchors:** The chapter's table of five runs on six metrics is the data of this sim. The chapter says an unstable metric goes to a person even if the median matches the human score.
</details>

The last MicroSim of the chapter is a dashboard that brings every measure together. It shows the calibration results for the three agents, and you decide what each result means for how the agent may be used.

#### Diagram: Calibration Dashboard Reader

<details markdown="1">
<summary>Calibration Dashboard Reader</summary>
Type: microsim
**sim-id:** calibration-dashboard-reader<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of three agents may be used as a first pass, may be used only to draft evidence, or should not be used, and name the measure on the calibration dashboard that decided it, with at least 5 of 6 decisions correct on the first attempt.

**Prerequisites:** Calibration Against Humans, Agreement Rate, Mean Absolute Difference, Score Correlation, Cohen's Kappa, Run-to-Run Variance, Prompt Refinement (all defined in this chapter above this block).

**Evidence of Mastery:** For each agent the learner makes two decisions: how the agent may be used, and which measure decided it. A decision is correct when it matches the Content table. Mastery is at least 5 of 6 decisions correct on the first attempt. Reading the standard is exploration, not evidence.

**Misconceptions:** (1) The best single measure decides everything. (2) A high correlation is enough. (3) An agent that fails the standard is useless.

**Instructional Rationale:** Deciding how an agent may be used from a set of measures is an Evaluate-level action. Three agents that each fail, or pass, for a different reason teach the learner to find the measure that matters.

**Content:**

The standard, shown at all times (illustrative, labeled "illustrative standard"): first pass requires all of these: agreement rate at a threshold of 1 >= 80 percent, absolute bias <= 0.5, mean absolute difference <= 1.0, and the adoption decision matches the humans. An agent that fails any one of them may be used only to draft evidence for a person to check. An agent whose adoption decision differs from the humans and whose absolute bias is > 0.5 should not be used until the prompt is refined.

The dashboard covers one resource, so it shows the adoption decision and not kappa or the run-to-run range, which need many resources or many runs. The dashboard, one row per agent (the numbers come from the chapter's running example):

| Agent | Agreement at threshold 1 | Mean absolute difference | Bias | Correlation | Adoption decision (humans: Revise) |
|---|---|---|---|---|---|
| A1 | 100 percent | 1.0 | +1.0 | 1.00 | Adopt |
| A2 | 100 percent | 0.3 | -0.1 | 0.96 | Revise |
| A3 | 40 percent | 1.4 | 0.0 | 0.46 | Revise |

The decisions:

| Agent | Correct use | Deciding measure | Why (shown as feedback) |
|---|---|---|---|
| A1 | Should not be used until the prompt is refined | Bias | The bias is +1.0, which exceeds 0.5, and the adoption decision differs from the humans. |
| A2 | May be used as a first pass | None fails | Every measure is within the standard. |
| A3 | May be used only to draft evidence | Agreement rate | Its agreement rate of 40 percent is < 80 percent, and its decision matches the humans. |

The three uses, offered as choices: May be used as a first pass; May be used only to draft evidence; Should not be used until the prompt is refined. The deciding measures, offered as choices: Agreement rate; Mean absolute difference; Bias; Correlation; Adoption decision; None fails.

**Provenance:** The numbers come from the chapter's running example and are labeled "illustrative examples". The standard is an illustrative choice for the book, and the sim labels it "illustrative standard".

**Rules:** Each agent has exactly one correct use and one correct deciding measure. The deciding measure is the first failing measure in this order: agreement rate, mean absolute difference, bias, adoption decision. Correlation never decides.

**Learner Activity:**

1. The learner sees the dashboard and the standard.
2. For the highlighted agent the learner chooses a use and a deciding measure.
3. The sim shows whether each choice was correct and the Why text.
4. After the third agent the sim shows the summary.

**Feedback:** 3 agents in a shuffled order, two decisions each, one attempt each. Correct: "Correct. [Why]". Incorrect: "Not quite. The correct use is [use], decided by [measure]. [Why]". The summary shows "[n] of 6 decisions correct on the first attempt". At 5 or more it adds "You can read a calibration dashboard." Below 5 it lists the Why text of each missed agent.

**Starting State:** The dashboard, the standard, and the first agent highlighted.

**Chapter Anchors:** The chapter's calibration steps, the illustrative standard, and the refinement from Agent A1 to Agent A2 give the numbers and the standard used in this sim.
</details>

---

## Key Takeaways

- A **hallucination** is a confident statement that is not true. Defend against it by requiring evidence a person can find, searching for every quotation, and tracing every number to a tool log.
- An **invented citation** is nonexistent or misattributed. Search the title, check the journal and issue, resolve the link, and read the supporting passage.
- A **license misreading** has predictable forms: one license assumed for every item, neighboring licenses confused, a restriction ignored, public equated with free, and ShareAlike missed. Compare every license claim with the statement itself.
- An **overconfident score** outruns its evidence, and **score inflation** is the same tendency across many metrics. Untested counts as failed, and a 10 needs every check to pass.
- Name each finding by **agent error type**: factual, license, citation, or scoring. A correct claim is not an error.
- A **verification step** names the claim, the test, and the result. A **spot check** samples the claims, and **source verification** goes to the original source. Verify the claims that decide the outcome first.
- A **second-agent cross-check** narrows the list of things to verify and does not replace verification. **Agent disagreement** is information, and the evidence decides it.
- Every checked claim is **accepted, corrected, or rejected**, and the **findings log** records which. The **agent error rate** is the share corrected or rejected, and it is only as honest as the sample behind it.
- Measure agreement with a **score difference threshold** chosen in advance, then report the **agreement rate**, the **mean absolute difference**, the **bias**, and the **score correlation** together. Each has a blind spot, and matching totals can hide large errors.
- **Cohen's kappa** corrects agreement for chance with kappa = (po - pe) / (1 - pe). A 90 percent agreement can be a kappa of 0.44.
- **Calibration against humans** tests the agent on resources with known scores, uses **prompt refinement** to fix the errors found, and confirms the result on a fresh set. Measure **run-to-run variance**, and send unstable metrics to a person.

!!! mascot-celebration "You Can Check the Checker"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now catch an agent's invented facts, citations, and license readings, log what you decided, and measure whether the agent agrees with careful humans. The next chapter turns from judging resources to improving them.

[See Annotated References](./references.md)
