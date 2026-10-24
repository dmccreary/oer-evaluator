# Quiz: AI Agents, Prompts, and Rubric Scoring

Test your understanding of language models, prompts, agents, tool use, structured output, and rubric prompts with these review questions.

---

#### 1. What is a token in a language model?

<div class="upper-alpha" markdown>
1. A secret key that lets a user sign in to an AI service and pay for each request
2. The small piece of text a model reads and writes, such as a short word or part of a word
3. A single learning outcome written inside a prompt so the model knows the goal
4. A score the model assigns to its own answer to show how confident it is
</div>

??? question "Show Answer"
    The correct answer is **B**. A model does not see letters or whole sentences. It sees a stream of tokens, and for ordinary English a token averages about three quarters of a word, so 100 words come to about 133 tokens. Tokens matter because every model limits how many it can handle at once, which is its context window, and because many services charge by the token. Numbers, unusual words, and other languages break into more tokens.

    **Concept Tested:** Token

    **See:** [Token](index.md#token)

---

#### 2. Which list names the parts of a good prompt?

<div class="upper-alpha" markdown>
1. Title, author, subject, grade level, license, and description
2. Stem, key, distractors, feedback, tag, and retry control
3. Observe, decide, act, and observe the result
4. Role, task, input, rules, output format, and example
</div>

??? question "Show Answer"
    The correct answer is **D**. A prompt is the text you give a model to tell it what to do, and a good one has up to six parts. The role says who the model should act as, the task says what to do, and the input is the material to work on. The rules say what to do and what not to do, including what to write when unsure. The output format shapes the answer, and an example shows a good answer. Option A lists metadata fields.

    **Concept Tested:** Prompt

    **See:** [Prompt](index.md#prompt)

---

#### 3. Why can an AI assistant write a confident review of a resource it has never seen?

<div class="upper-alpha" markdown>
1. It stores a copy of every web page and checks the copy against the resource
2. It runs a built-in accessibility checker on any resource name that it is given
3. Every open educational resource is part of its training data, so it has read them
4. A language model predicts likely text and does not look facts up, so it answers even without the resource
</div>

??? question "Show Answer"
    The correct answer is **D**. A large language model generates text one piece at a time by predicting what is likely to come next. It does not consult a database, it knows only what it was trained on and what you give it, and it will write an answer even when it cannot do what you asked. A request such as "Score this resource for accessibility" with nothing attached gets an invented number. Supply the text, name the checks, and demand evidence.

    **Concept Tested:** Large Language Model

    **See:** [Large Language Model](index.md#large-language-model)

---

#### 4. How does an AI agent differ from an AI assistant?

<div class="upper-alpha" markdown>
1. An agent is a larger language model, while an assistant is a smaller one of the same kind
2. An assistant answers and waits, while an agent plans, uses tools, observes results, and acts again until done
3. An assistant can use tools and files freely, while an agent can only reply in plain text
4. An agent works only on resources that a human reviewer has already scored by hand first
</div>

??? question "Show Answer"
    The correct answer is **B**. An agent is a system built around a language model that works toward a goal over several steps. The model supplies judgment and language, the tools supply measurements, and the loop lets the agent keep going. An agent asked to check links lists them, tests each with a tool, reads the results, and writes a report. Agents have more ways to go wrong because each step can inherit the error of the one before, so a person stays in the loop.

    **Concept Tested:** AI Agent

    **See:** [AI Agent](index.md#ai-agent)

---

#### 5. Why should exact tasks, such as counting the images that lack alt text, be given to a tool and not to the model?

<div class="upper-alpha" markdown>
1. Language models are weak at exact work and can miscount while sounding sure, whereas a tool is repeatable
2. Tools can judge whether alt text is useful, and language models cannot judge text at all
3. Language models are not allowed to read HTML, so they cannot see which images lack alt text
4. Tools are always free to use, and language models are always too expensive to run on a resource
</div>

??? question "Show Answer"
    The correct answer is **A**. The chapter divides the work three ways. Tools do exact tasks, such as counting, measuring, testing, and comparing. The model does judgment tasks on text, such as whether alt text is useful or a heading describes its section. A person keeps real-world tasks, such as confirming a fact against its source. In the chapter's example, a model counted two images without alt text when the true number was one.

    **Concept Tested:** Tool Use

    **See:** [Tool Use](index.md#tool-use)

---

#### 6. A reviewer wants an agent to score a 6,000-word resource using a 900-word prompt and expects a 1,200-word answer. Using the rule that tokens equal words divided by 0.75, rounded up, will the request fit in a window of 8,000 tokens?

<div class="upper-alpha" markdown>
1. Yes, because the resource alone is only 6,000 words, which is less than the window
2. Yes, because the expected answer does not count against the window of the model
3. No, because it needs about 10,800 tokens, so she needs a larger window or a shorter request
4. No, because it needs about 8,100 tokens, since words and tokens are the same thing
</div>

??? question "Show Answer"
    The correct answer is **C**. Everything the model uses must fit in the window: the instructions, the resource, the conversation, and the answer it writes. The total is 6,000 + 900 + 1,200 = 8,100 words, and dividing by 0.75 gives 10,800 tokens, which is more than 8,000. The three remedies are a larger window, shorter instructions, or splitting the resource, though splitting can miss checks that span the whole resource, such as whether an outcome is ever taught.

    **Concept Tested:** Context Window

    **See:** [Context Window](index.md#context-window)

---

#### 7. The required form for an agent's answer is a JSON object with a text metric, a whole-number score from 0 to 10, and text evidence. An agent returns `{"metric": "Readability", "score": "eight", "evidence": "Grade 6.4"}`. What is the defect?

<div class="upper-alpha" markdown>
1. It is not valid JSON, because a comma is missing between two pairs
2. A field is missing, because the answer has no evidence key
3. A value is wrong, because the score is text and must be a whole number
4. There is no defect, because the answer is valid and meets the required form
</div>

??? question "Show Answer"
    The correct answer is **C**. The snippet is valid JSON: every name and text value is in double quotes, commas separate the pairs, and all three keys are present. The defect is the value of score. A number has no quotes, and "eight" is text, so it does not meet the schema that calls for a whole number from 0 to 10. A program can test every answer against the schema and ask the agent to try again. Validation catches errors of form and cannot tell whether the content is true.

    **Concept Tested:** JSON Output

    **See:** [JSON Output](index.md#json-output)

---

#### 8. A department wants an agent to check the accessibility of a resource that exists as an HTML page, a PDF made from a word processor, and a scan of a printed copy. Which source should it give the agent first, and why?

<div class="upper-alpha" markdown>
1. The PDF, because a PDF preserves every heading and image description exactly
2. The scan, because a scan is the original and so is the most reliable source
3. Any of the three, because an agent receives the same information from each
4. The HTML page, because its headings, links, and alt text stay in the markup
</div>

??? question "Show Answer"
    The correct answer is **D**. Document ingestion decides what an agent can check, because a model reads text and not files. Markdown and HTML hold their structure in the text, so they ingest cleanly. A PDF often ingests with damage: reading order, headings, and tables can come out scrambled, and alt text is lost. A scan is a picture that needs text recognition first. If ingestion strips out the alt text, the agent may report that none exists.

    **Concept Tested:** Document Ingestion

    **See:** [Document Ingestion](index.md#document-ingestion)

---

#### 9. An agent's draft says "Contrast ratio tested: 5.2 to 1." The agent was given no contrast tool, and the reviewer finds no record of a test. What is the best analysis?

<div class="upper-alpha" markdown>
1. The measurement is likely accurate, because language models compute contrast reliably
2. The claim is acceptable, because 5.2 is above the 4.5 minimum for normal text
3. The measurement is invented and has no evidence, so the reviewer should reject it and run a contrast tool
4. The measurement is a harmless rounding difference that can safely be ignored by the reviewer
</div>

??? question "Show Answer"
    The correct answer is **C**. Agent scoring produces a draft that a person must check, because an agent can be wrong in ways that look right: a check marked as passed that was never run, a quotation that is not in the resource, or a measurement from a tool it never called. The reviewer's test is to ask which tool produced the number and to run it. A measurement without a source is not evidence, whatever value it reports.

    **Concept Tested:** Agent Scoring

    **See:** [Agent Scoring](index.md#agent-scoring)

---

#### 10. A reviewer tests a rubric prompt on Watershed Basics, whose human accessibility score is 5. In three rounds the agent's score moves from 8 to 7 to 6 as rules are added that demand evidence and allow "not checkable." What does this pattern show?

<div class="upper-alpha" markdown>
1. Forcing evidence moved the agent toward the human score, but a gap remains that should be measured
2. The prompt is now perfect, because the score went down in every round of testing
3. The agent must be right, because the human score cannot be trusted to be accurate
4. The prompt should be abandoned, because it never matched the human score exactly
</div>

??? question "Show Answer"
    The correct answer is **A**. Prompt iteration improves a prompt in cycles: write it, run it on a resource you have already scored by hand, compare, and change one thing at a time. The rules that required evidence and honest blanks pulled the score down, but the agent still reads 6 against the human 5. A gap that remains is a finding. Chapter 14 shows how to measure it, and the human score is the reference, not the agent's.

    **Concept Tested:** Prompt Iteration

    **See:** [Prompt Iteration](index.md#prompt-iteration)
