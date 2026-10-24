# Quiz: Checking and Calibrating AI Agent Output

Test your understanding of agent error types, verification, accept-correct-reject decisions, agreement measures, Cohen's kappa, and calibration with these review questions.

---

#### 1. Which list names the four agent error types that this chapter uses?

<div class="upper-alpha" markdown>
1. Factual, license, citation, and scoring
2. Factual, format, citation, and timing
3. Hallucination, inflation, variance, and bias
4. Role, task, input, and output
</div>

??? question "Show Answer"
    The correct answer is **A**. A factual error is a wrong claim about the resource, a license error is a wrong reading of its license, a citation error is a reference that does not exist or does not support its claim, and a scoring error is a score or total that does not follow from the agent's own checks. Naming the type tells the reviewer how to catch the mistake and tells the prompt writer how to fix it. A correct claim is not an error at all.

    **Concept Tested:** Agent Error Type

    **See:** [Agent Error Type](index.md#agent-error-type)

---

#### 2. What does a findings log record?

<div class="upper-alpha" markdown>
1. Only the claims that were rejected, with the agent's own explanation of each rejected claim
2. Every agent claim a reviewer checked, the decision (accepted, corrected, or rejected), and the reason
3. The cost of each run, the name of the model that was used, and the date of the run
4. The reviewer's final adoption decision and nothing else, such as the evidence or the reasons
</div>

??? question "Show Answer"
    The correct answer is **B**. The log makes a review auditable, because anyone can see what was checked. It feeds the measurement of the agent error rate, since the share of rejected or corrected claims comes straight from it. And it feeds prompt refinement, because the rejected claims show which instructions the prompt needs. Recording the accepted claims matters as much as recording the failures, so that the log shows what the agent got right.

    **Concept Tested:** Findings Log

    **See:** [Findings Log](index.md#findings-log)

---

#### 3. Why does the chapter rank "ask the agent whether it is sure" as the weakest verification step?

<div class="upper-alpha" markdown>
1. Agents refuse to answer questions about their own confidence in a claim
2. It takes longer than opening the cited source and reading the passage
3. Agents always reply that they are unsure, so the answer is never useful
4. The same model answers again, so the reply proves nothing about the claim
</div>

??? question "Show Answer"
    The correct answer is **D**. Verification steps get stronger as they move away from the agent's own words. Asking the agent to confirm proves nothing, recomputing arithmetic from the report's table is weak, running a tool and reading its log is strong, and opening the cited source and reading the passage is strongest. A good step states the claim in its exact words, says how to test it, records what was found with a date, and marks the result confirmed or not confirmed.

    **Concept Tested:** Verification Step

    **See:** [Verification Step](index.md#verification-step)

---

#### 4. How does an invented citation differ from a misattributed one?

<div class="upper-alpha" markdown>
1. An invented citation has no identifier, while a misattributed one always has a working DOI
2. An invented citation supports the claim, while a misattributed one does not support it
3. An invented citation cannot be found at all, while a misattributed one exists but does not support the claim
4. An invented citation always names a journal, while a misattributed one always names a website
</div>

??? question "Show Answer"
    The correct answer is **C**. A nonexistent source is one whose journal, article, or author is made up. A misattributed source is real but does not say what the agent claims, such as a paper on urban runoff cited for a claim about wetlands. Four checks tell them apart: search for the exact title, check that the journal has the issue cited, resolve the identifier, and open the source and read the supporting passage. A missing identifier alone is a weaker sign.

    **Concept Tested:** Invented Citation

    **See:** [Invented Citation](index.md#invented-citation)

---

#### 5. A calibration run shows an agent with a bias of 0.0 and a mean absolute difference of 1.4. What does the pair of numbers show?

<div class="upper-alpha" markdown>
1. The agent matches the humans exactly on every metric, since a bias of zero means no error
2. Its overshoots and undershoots cancel in the bias, so it still makes sizable errors on single metrics
3. The agent is consistently too generous on every metric, which is why the bias looks so low
4. The two measures contradict each other, so one of them was miscalculated by the reviewer
</div>

??? question "Show Answer"
    The correct answer is **B**. The bias keeps the sign of each difference, so overshoots and undershoots cancel. The mean absolute difference drops the sign and averages the size of the gaps, so it shows that the typical score is 1.4 points from the human's. In the chapter's running example, Agent A3 has exactly this pattern, with differences from minus 3 to plus 3. A bias near zero never proves an agent is accurate.

    **Concept Tested:** Mean Absolute Difference

    **See:** [Mean Absolute Difference](index.md#mean-absolute-difference)

---

#### 6. A reviewer verified 40 of an agent's claims. Six were corrected or rejected, and 34 were accepted. What is the agent error rate?

<div class="upper-alpha" markdown>
1. 15 percent
2. 85 percent
3. 6 percent
4. 40 percent
</div>

??? question "Show Answer"
    The correct answer is **A**. The agent error rate is the share of the agent's checked claims that were corrected or rejected. Six divided by 40 is 0.15, or 15 percent. Option B is the share that was accepted. A breakdown by error type is more useful than the total, because it shows where the agent fails. The rate is only as honest as the sample behind it: claims chosen because they looked suspicious overstate the errors, and only easy claims understate them.

    **Concept Tested:** Agent Error Rate

    **See:** [Agent Error Rate](index.md#agent-error-rate)

---

#### 7. An agent's report says "Reading level is grade 6.9." The readability tool reports 7.1. What should the reviewer do with the claim?

<div class="upper-alpha" markdown>
1. Accept it, because 6.9 is close to 7.1 and the difference is only a fifth of a grade
2. Reject it, because any wrong number makes a claim false and unusable in the report
3. Accept it, and ask the agent to run again so that the number can be compared
4. Correct it to 7.1 and log the change, since it is right in substance with one detail wrong
</div>

??? question "Show Answer"
    The correct answer is **D**. A claim is accepted when verification shows it is true as stated, corrected when it is right in substance and a detail is wrong, and rejected when it is false, invented, or impossible to verify. Here the agent did measure the reading level, and the number is slightly off, so the reviewer fixes the detail and notes the change in the findings log. Rejecting every inexact claim (B) would overstate the agent's errors, and accepting an inexact figure (A) lets mistakes through.

    **Concept Tested:** Accept Correct or Reject

    **See:** [Accept, Correct, or Reject](index.md#accept-correct-or-reject)

---

#### 8. An agent and a human each judge 20 resources as ready or not ready to adopt. Both say ready for 8, only the agent says ready for 2, only the human says ready for 2, and both say not ready for 8. What is Cohen's kappa?

<div class="upper-alpha" markdown>
1. 0.80
2. 0.50
3. 0.60
4. 0.30
</div>

??? question "Show Answer"
    The correct answer is **C**. Observed agreement po is (8 + 8) ÷ 20, which is 0.80. Each side says "ready" for 10 of 20, so the chance both say ready is 0.5 × 0.5 = 0.25, and the chance both say not ready is also 0.25, giving pe = 0.50. Kappa is (po − pe) ÷ (1 − pe) = 0.30 ÷ 0.50 = 0.60. Option A is the raw agreement, which does not correct for chance, and 0.60 falls in the moderate range of the commonly cited rule-of-thumb labels.

    **Concept Tested:** Cohen's Kappa

    **See:** [Cohen's Kappa](index.md#cohens-kappa)

---

#### 9. Agent A1 is exactly one point higher than the humans on every metric. Its correlation with the human scores is 1.00 and its agreement rate at a threshold of 1 is 100 percent, yet its report says Adopt where the humans say Revise. What explains this?

<div class="upper-alpha" markdown>
1. Correlation ignores the level, so a constant one-point inflation leaves it perfect yet lifts the total to 75
2. A correlation of 1.00 means the agent's scores are identical to the humans' on every metric
3. An agreement rate of 100 percent always guarantees the same adoption decision as the humans
4. The adoption decision is made by correlation, so the humans must have miscalculated the total
</div>

??? question "Show Answer"
    The correct answer is **A**. Correlation checks whether metrics the humans scored high are also high for the agent, and it is blind to a constant offset. Agent A1's bias is +1.0 on every metric, which is score inflation. Ten extra points lift the total from 65 to 75, and with every metric at least 5 the Adopt rule is met. A threshold of 1 treats a gap of 1 as agreement. This is why the measures must be read together and why bias detects what correlation cannot.

    **Concept Tested:** Score Correlation

    **See:** [Score Correlation](index.md#score-correlation)

---

#### 10. A calibration dashboard for one agent shows 100 percent agreement at a threshold of 1, a mean absolute difference of 1.0, a bias of +1.0, a correlation of 1.00, and an Adopt decision where the humans say Revise. The illustrative standard needs an absolute bias of 0.5 or less and a matching decision. Which judgment is best?

<div class="upper-alpha" markdown>
1. It may be used as a first pass, because its correlation with the humans is perfect
2. It should be discarded permanently, because it failed its first calibration run on the set
3. It should not be used until the prompt is refined, because its bias exceeds 0.5 and its decision differs
4. It may be used as a first pass, because its agreement rate at the loose threshold is 100 percent
</div>

??? question "Show Answer"
    The correct answer is **C**. An agent whose adoption decision differs from the humans' and whose absolute bias exceeds 0.5 fails the standard on two counts. Correlation never decides, and a 100 percent agreement rate at a loose threshold hides a consistent one-point inflation. The agent is not useless: refine the prompt against the errors in the findings log, rerun on the same set, then confirm on a fresh set. In the chapter, this refinement turned Agent A1 into Agent A2.

    **Concept Tested:** Calibration Against Humans

    **See:** [Calibration Against Humans](index.md#calibration-against-humans)
