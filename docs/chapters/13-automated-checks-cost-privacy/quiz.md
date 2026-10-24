# Quiz: Automated Checks, Cost, and Student Privacy

Test your understanding of human oversight, multi-agent review, automated checks, AI cost, and student data privacy with these review questions.

---

#### 1. What does FERPA protect?

<div class="upper-alpha" markdown>
1. The copyright of teachers' lesson plans
2. The accessibility of web content for learners with disabilities
3. The licensing terms of open textbooks
4. The privacy of student education records in the United States
</div>

??? question "Show Answer"
    The correct answer is **D**. FERPA, the Family Educational Rights and Privacy Act of 1974, is a U.S. federal law that protects the privacy of student education records. It applies to schools and colleges that receive funds from the U.S. Department of Education, and it generally requires written consent before a school discloses personally identifiable information from a record. Sending identifiable student records to an AI company is a disclosure that FERPA may restrict. Ask your school's privacy officer which rules cover you.

    **Concept Tested:** FERPA

    **See:** [FERPA](index.md#ferpa)

---

#### 2. In multi-agent review, what spread between the highest and lowest agent scores flags a metric for a person to examine first?

<div class="upper-alpha" markdown>
1. More than 1 point
2. More than 3 points
3. More than 5 points
4. Any spread at all
</div>

??? question "Show Answer"
    The correct answer is **B**. Multi-agent review has two or more agents, or several runs with different prompts or models, score the same resource independently. It copies the two-reviewer method of Chapter 11, so it uses the same rule: a metric is flagged when the scores differ by more than 3 points. The spread is a cheap signal that points to metrics where the evidence is unclear or an agent has gone astray. Agreement within 3 points still needs a check if no evidence was quoted.

    **Concept Tested:** Multi-Agent Review

    **See:** [Multi-Agent Review](index.md#multi-agent-review)

---

#### 3. Why does the chapter recommend matching the level of checking to the risk instead of redoing every score by hand?

<div class="upper-alpha" markdown>
1. Risk-matched oversight catches errors where they occur and keeps most of the agent's time saving
2. Agents are always accurate on low-risk metrics, so no one needs to read their reports at all
3. A person is not responsible for decisions that an agent's report supports, because the agent made them
4. Reports with exact evidence should be accepted without any human check, because the evidence is exact
</div>

??? question "Show Answer"
    The correct answer is **A**. Human in the loop means a person reviews the agent's output where errors matter. The cost is time, so the practical question is where attention buys the most. A report that follows the rules, carries tool logs, and shows exact evidence needs a spot check, a report built on the agent's memory needs every claim checked, and a report that breaks the rubric's rules goes back. Accountability cannot be delegated, so a person always answers for the decision.

    **Concept Tested:** Human in the Loop

    **See:** [Human in the Loop](index.md#human-in-the-loop)

---

#### 4. Why is a clean automated accessibility scan a starting point and not a pass?

<div class="upper-alpha" markdown>
1. Automated scans are never accurate about missing alt attributes, so every image must be checked by hand
2. A scan can examine only the first page of a resource, so most pages are never checked
3. A scan checks only the color of text and nothing else, so most problems are never found
4. A scan finds machine-detectable problems but cannot judge whether alt text is useful or captions are accurate
</div>

??? question "Show Answer"
    The correct answer is **D**. An automated scan finds images with no alt attribute, text with weak contrast, missing form labels, and some heading problems. Those are real findings, and they are quick to get. It cannot judge quality: alt text that says "photo" exists, so the scan passes it. The accessibility metric still needs the human checks, which means reading the alt text, listening with a screen reader, and tabbing through the page.

    **Concept Tested:** Automated Accessibility Scan

    **See:** [Automated Accessibility Scan](index.md#automated-accessibility-scan)

---

#### 5. Which approach does the chapter recommend for reducing AI cost without cutting quality?

<div class="upper-alpha" markdown>
1. Run every resource three times and keep the cheapest result, whatever the quality of the answer
2. Skip the human check on every report that comes from a larger model, to save the reviewer's time
3. Use the largest and most expensive model for every check, so that no check needs to be repeated
4. Give exact checks to free tools, send only what a check needs, use a cheaper model first, and pilot
</div>

??? question "Show Answer"
    The correct answer is **D**. Cost is tokens times price, times resources, times runs, so each lever matters. Free tools cost nothing per token, shorter instructions and trimmed inputs cut the tokens, and a smaller model suffices for a first screen. A pilot of three resources shows the price and whether the prompt works, so a flaw costs three runs and not three hundred. Prices change often, so look up current ones and never rely on a figure in a book.

    **Concept Tested:** AI Cost

    **See:** [AI Cost](index.md#ai-cost)

---

#### 6. A run reads 6,000 input tokens and writes 1,000 output tokens, at $2.00 per million input tokens and $8.00 per million output tokens. What does a batch of 500 resources cost if three agents each score every resource once?

<div class="upper-alpha" markdown>
1. $30.00
2. $10.00
3. $90.00
4. $0.06
</div>

??? question "Show Answer"
    The correct answer is **A**. One run costs (6,000 × 2.00 + 1,000 × 8.00) ÷ 1,000,000, which is 0.012 + 0.008, or $0.02. Five hundred resources at one run each cost $10.00, and three agents triple the number of runs, so the batch costs $30.00. Option B forgets the extra agents, and option D is the cost of one resource scored by three agents. The prices here are illustrative, and a retry after an invalid answer adds another run.

    **Concept Tested:** AI Cost

    **See:** [AI Cost](index.md#ai-cost)

---

#### 7. A teacher wants an agent to review a published open textbook chapter. She also has a spreadsheet of her class's quiz scores listed with student names. What should she send?

<div class="upper-alpha" markdown>
1. Only the published chapter, because the scores with names need approval or anonymizing first
2. Both files, because anything a teacher already holds is safe to send to an AI service
3. Neither file, because every file is private once it is on a teacher's computer and cannot leave it
4. Only the spreadsheet, because the chapter is already public and so needs no review by the agent
</div>

??? question "Show Answer"
    The correct answer is **A**. An agent that reviews a resource needs only the resource, which is published or ready to publish and holds no student data. Names make quiz scores personal data, so the spreadsheet needs anonymizing or approval first, and even coded scores from a very small class may still identify students. Text pasted into an AI service leaves your control, and a deletion request may not undo it. If unsure, ask the school's privacy officer or technology office.

    **Concept Tested:** Student Data Privacy

    **See:** [Student Data Privacy](index.md#student-data-privacy)

---

#### 8. A page footer says CC BY-NC, while the license recorded in the page's metadata says CC BY. Which automated check would find this mismatch?

<div class="upper-alpha" markdown>
1. An automated link checker
2. An automated readability scan
3. Automated license detection
4. An automated accessibility scan
</div>

??? question "Show Answer"
    The correct answer is **C**. Automated license detection finds license statements in a resource, reads their names, versions, and links, and compares them with the license recorded in the metadata. It catches a missing license, a mismatch between page and metadata, and an unrecognized license text. It cannot tell whether the statement is true: a work copied from someone else with a license label added still passes. The check supports the open license metric.

    **Concept Tested:** Automated License Detection

    **See:** [Automated License Detection](index.md#automated-license-detection)

---

#### 9. Three agents score two metrics. For accessibility they give 5, 9, and 6, and all three quote evidence. For open license they all give 9, and none quotes any evidence. Which analysis is correct?

<div class="upper-alpha" markdown>
1. Accessibility needs a check, but open license can be accepted because all three agents agree on it
2. Both metrics should be accepted, using the average of the three scores for each metric
3. Accessibility is flagged by its spread of 4, and open license needs a check because agreement alone proves little
4. Open license is flagged because the agents agree, and accessibility can be accepted because its evidence was quoted
</div>

??? question "Show Answer"
    The correct answer is **C**. The spread for accessibility is 9 minus 5, which is 4, and that is more than 3, so the metric is flagged. For open license the spread is 0, but no agent quoted evidence. Agreement among agents is not truth, because agents built on similar models can share the same blind spots. Agreement with no evidence is especially suspect, so a person checks it anyway. The average of three scores is not the right score.

    **Concept Tested:** Multi-Agent Review

    **See:** [Multi-Agent Review](index.md#multi-agent-review)

---

#### 10. An agent's report recommends Adopt for a resource with a total of 76, but one metric scores 4. Which analysis is correct?

<div class="upper-alpha" markdown>
1. Adopt is correct, because the total is at least 75 and that is what the rule requires
2. The decision breaks the adoption rule, which needs every metric at 5 or more, so the report goes back
3. The report needs only a spot check, because its numbers look exact and complete
4. A person should check every claim, because the report has no evidence for its decision
</div>

??? question "Show Answer"
    The correct answer is **B**. The Adopt rule has two parts: a total of at least 75 and every metric at least 5. The report meets the first and fails the second, so its own decision breaks the rubric's rule. A report that breaks the rules goes back to the agent for another run, which is the highest level of oversight, ahead of checking every claim or spot-checking. The details of the report do not make it trustworthy, since the error lies in the logic and not in a missing source.

    **Concept Tested:** Human in the Loop

    **See:** [Human in the Loop](index.md#human-in-the-loop)
