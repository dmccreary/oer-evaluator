# Quiz: Improving a Resource with AI Agents

Test your understanding of improvement plans, derivative works, the fix toolkit, human review, change logs, and re-scoring with these review questions.

---

#### 1. Which list gives the five parts of a useful improvement plan?

<div class="upper-alpha" markdown>
1. Title, author, subject, grade level, license, description, and keywords
2. The baseline, the gaps, the fixes, the order and the budget, and the target
3. Role, task, input, rules, output format, and a worked example
4. Stem, key, distractors, feedback message, outcome tag, difficulty tag, and retry control
</div>

??? question "Show Answer"
    The correct answer is **B**. An improvement plan is the bridge between the scores and the work. The baseline holds the ten scores, the total, and the decision before any change. The gaps are the failed checks that hold each low score down, the fixes are one task per gap, the order and budget say what comes first and how many human hours each needs, and the target names the score and decision the plan aims for. Write it before the work and compare it with the result afterward.

    **Concept Tested:** Improvement Plan

    **See:** [Improvement Plan](index.md#improvement-plan)

---

#### 2. What does the lowest-metric-first rule say?

<div class="upper-alpha" markdown>
1. Start with the metric whose fix costs the most hours, because it will be the hardest to finish
2. Start with the highest-scoring metric to build momentum, because it needs the fewest changes
3. Start the plan with the lowest-scoring metric, because a metric under 5 blocks adoption and is often cheap
4. Start with whichever metric the agent finds easiest to improve, whatever its current score
</div>

??? question "Show Answer"
    The correct answer is **C**. Three reasons support the rule. The adoption rule sets a floor, so a metric under 5 blocks adoption however high the total is. The lowest scores often have the cheapest large gains, since a record with two of six fields filled can reach six in minutes. And a total hides the weakest metric. The exception is a lowest-metric fix that is expensive or needs the author's decision, in which case do cheaper fixes first and flag it.

    **Concept Tested:** Lowest Metric First

    **See:** [Lowest Metric First](index.md#lowest-metric-first)

---

#### 3. Why should a reviewer read a resource's license before an agent makes the first edit?

<div class="upper-alpha" markdown>
1. Agents are unable to edit any resource that carries an open license of any kind, so the license must be removed first
2. An edited version is a derivative work, and a NoDerivatives or missing license does not allow sharing it
3. The license decides which agent and which model to use, since each model has its own license
4. The license determines the reading level of the improved version, so it limits the rewrite
</div>

??? question "Show Answer"
    The correct answer is **B**. A derivative work is a new work based on an existing one, such as a translation, an adaptation, a remix, or an improved edition. An open license is the owner's advance permission with conditions. CC BY allows an improved version with credit, a link, and a note of changes, while CC BY-ND allows changes only for private use, and a resource with no license needs the owner's permission. Check this first, before any effort goes in.

    **Concept Tested:** Derivative Work

    **See:** [Derivative Work](index.md#derivative-work)

---

#### 4. Why does the chapter require a re-score of all ten metrics and not only the ones that were fixed?

<div class="upper-alpha" markdown>
1. The rubric states that every metric must be re-scored once a year, whether or not it changed
2. Fixes have side effects, such as a simulation lowering portability, and only a full re-score finds them
3. Metrics that were not fixed always improve as a side effect, so they must all be confirmed
4. Agents refuse to score fewer than ten metrics, so a partial re-score cannot be run
</div>

??? question "Show Answer"
    The correct answer is **B**. A simulation added to raise Practice can lower Portability if its script is blocked on a platform, a split can break a link, and a rewrite can drop a fact. Only a full re-score gives the true total and the true decision. Use the same rubric, evidence rules, and calibrated prompt as the first scoring, and use a fresh scorer, since an agent that edited a resource tends to score it generously. A person verifies every changed score.

    **Concept Tested:** Re-Scoring

    **See:** [Re-Scoring](index.md#re-scoring)

---

#### 5. An agent rewrites "Most rain soaks into the ground" as "Rain soaks into the ground." Which kind of meaning change is this?

<div class="upper-alpha" markdown>
1. A dropped qualifier
2. A changed strength
3. A changed quantity
4. An added claim
</div>

??? question "Show Answer"
    The correct answer is **A**. Preserving original meaning means an improvement changes the form of a resource and not what it says. The word "most" limits the claim to a share of the rain, and dropping it makes the claim cover all rain. The five quiet changes are a changed quantity, a changed strength, a dropped qualifier, an added claim, and a dropped item. Compare before and after in a difference view, and ask the agent to list every claim it changed, added, or removed.

    **Concept Tested:** Preserving Original Meaning

    **See:** [Preserving Original Meaning](index.md#preserving-original-meaning)

---

#### 6. A teacher plans to improve a CC BY-NC resource and post the improved version for free for other teachers. What must she do?

<div class="upper-alpha" markdown>
1. Nothing, because an open license requires nothing in return from the person who adapts the work
2. Ask the owner for permission first, because NonCommercial forbids any change
3. Release the new version under CC BY so that others may also sell it and change it freely
4. Credit the author, link to the license, say that she changed the work, and keep the use noncommercial
</div>

??? question "Show Answer"
    The correct answer is **D**. CC BY-NC allows an improved version to be published without commercial use. The conditions are the same as for CC BY: credit the author, link to the license, and say that the work was changed. NonCommercial limits selling or commercial gain, and it does not forbid changes, so permission is not needed (B). Releasing the version under CC BY (C) would let others sell it, which the original forbids. Sharing free with other teachers is allowed.

    **Concept Tested:** Derivative Work

    **See:** [Derivative Work](index.md#derivative-work)

---

#### 7. In the chapter's re-score of Watershed Basics, Practice rose from 6 to 8 and Portability fell from 7 to 6, and the total rose by 13 against a projected 14. Which analysis is correct?

<div class="upper-alpha" markdown>
1. A gain of 13 shows that every metric improved, so no individual metric needs a closer look
2. The projection was exact to within a point, so no side effect occurred in any of the ten metrics
3. Portability fell because the agent edited the portability checks while it was re-scoring the resource
4. The new simulation raised Practice but is blocked on one platform, a side effect only a full re-score catches
</div>

??? question "Show Answer"
    The correct answer is **D**. The simulation that earned the Practice gain cost a point of Portability because its script is blocked on one of the three test platforms. The plan forecast 79 and the re-score found 78. A total can rise while one metric gets worse, which is why a report names any metric that fell and the reason. The Practice fix returned a net gain of 1, because its +2 was offset by the −1 on Portability.

    **Concept Tested:** Re-Scoring

    **See:** [Re-Scoring](index.md#re-scoring)

---

#### 8. The chapter's gain-per-hour table shows Metadata returning 8.0 points per hour and Practice with its simulation returning 0.4. Which conclusion do the figures support?

<div class="upper-alpha" markdown>
1. Cheap fixes to the lowest metric return the most per hour, and the slowest fix returned the least
2. The simulation was the best investment of time, because it took the longest to build
3. Accessibility fixes are not worth doing, because they take 2.0 hours for only 3 points
4. Gain per hour is nearly identical across all fixes, so the order in which the work is done does not matter
</div>

??? question "Show Answer"
    The correct answer is **A**. Metadata took half an hour and returned +4, which is 8.0 points per hour. The Practice fix took 2.5 hours and returned a net +1, which is 0.4 per hour. The whole set returned about 1.7 points per hour. The figures argue for starting with the lowest metric. Two warnings apply: a small change may be noise, and a score gain is not a learning gain, since it shows that the resource meets more checks and not that students learn more.

    **Concept Tested:** Score Gain

    **See:** [Score Gain](index.md#score-gain)

---

#### 9. An agent's summary says it changed 12 items, but a reviewer's difference view shows 15 changes. What is the best judgment?

<div class="upper-alpha" markdown>
1. Rely on the difference view and review every change, because an agent's summary can omit a change
2. Trust the agent's summary, because the agent made the changes and so knows what it did
3. Reject all of the agent's changes without reading them, since the summary is unreliable
4. Ignore the three extra changes, because they were probably low risk and can safely be checked later on
</div>

??? question "Show Answer"
    The correct answer is **A**. Human review of changes means a named person examines each change before it is kept, using a difference view that shows every change, and decides accept, correct, or reject. The agent's own summary is not enough. Match the depth of review to risk: facts, numbers, quotations, citations, captions, license statements, and anything touching meaning get a full check, while heading levels and formatting get a spot check. In the chapter's example, one change in three needed a correction or a rejection.

    **Concept Tested:** Human Review of Changes

    **See:** [Human Review of Changes](index.md#human-review-of-changes)

---

#### 10. A resource totals 65, with Metadata at 4 and Accessibility and Modularity at 5. You have 5.0 hours. The candidate fixes are: A, Metadata (+4, 0.5 hours); B, Accessibility (+3, 2.0 hours); C, Modularity (+3, 1.5 hours); D, Accuracy (+2, 1.0 hour); E, Practice (+2, 2.5 hours); and H, Editable source (+1, 2.0 hours). Which plan best meets the chapter's guidance and earns the Adopt decision?

<div class="upper-alpha" markdown>
1. B, C, and E, which raise the most metrics that sit at 5 or 6 but leave metadata at 4
2. A, E, and H, which use exactly 5.0 hours but reach a total of only 72, below the Adopt bar
3. A, B, C, and D, which start with the lowest metric, use 5.0 hours, and reach a total of 77
4. A, B, C, D, and E, which raise the most points but use 7.5 hours, over the budget
</div>

??? question "Show Answer"
    The correct answer is **C**. The plan starts with the lowest metric. Fixes A, B, C, and D take 0.5 + 2.0 + 1.5 + 1.0 = 5.0 hours and add 4 + 3 + 3 + 2 = 12 points, for a total of 77. Every metric then sits at 6 or above, so the Adopt rule is met. Option A leaves Metadata at 4 and runs to 6.0 hours. Option B reaches only 72. Option D needs 7.5 hours, over the budget.

    **Concept Tested:** Improvement Plan

    **See:** [Improvement Plan](index.md#improvement-plan)
