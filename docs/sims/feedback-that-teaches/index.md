---
title: "Feedback That Teaches"
description: "One question and one wrong answer, answered four ways, with each message rated against four criteria; only the last one passes all four."
image: /sims/feedback-that-teaches/feedback-that-teaches.png
og:image: /sims/feedback-that-teaches/feedback-that-teaches.png
twitter:image: /sims/feedback-that-teaches/feedback-that-teaches.png
social:
   cards: false
status: built
hide:
  - toc
---

# Feedback That Teaches

<iframe src="main.html" height="789px" width="100%" scrolling="no"></iframe>

[Run the Feedback That Teaches MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 8: Practice and Feedback](../../chapters/08-practice-feedback/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `feedback-that-teaches.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/feedback-that-teaches/main.html"
        height="789px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Feedback is the part of practice that does the teaching. This poster holds the situation constant: the question "Which describes infiltration?" and a learner who chose "water flowing over the ground". It answers the same wrong answer four ways, ordered from least to most helpful, and rates each message against the criteria in Chapter 8: it says the answer was wrong, it explains why, it points toward the right idea, and it does not blame. Only the last message passes all four. Chapter 15 has agents write practice questions, so the same yardstick applies to what they produce.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Message 1: Wrong. | Says the answer failed and says nothing else. Rated weak. |
| Message 2: Good try! | Does not say whether the answer was right. Rated weak. |
| Message 3: Incorrect. The answer is A. | Gives the answer and no reason. Rated weak. |
| Message 4: Not quite... | Corrects, explains, and names the mix-up. Rated strong. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The wording of the messages is exact and not paraphrased. The check and cross marks are rated against the four criteria in the chapter.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **rate** a feedback message against four criteria and **explain** why only one of four messages for the same wrong answer is strong. (Bloom level: Evaluate.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The feedback metric from [Chapter 8](../../chapters/08-practice-feedback/index.md).

### Activities

1. **Explore (3 min).** Press each message and read what it does. Which criterion does each weak message miss?
2. **Quiz (3 min).** Press **Quiz Me** and find the message that matches each description.
3. **Rewrite (4 min).** Take one wrong answer from a quiz you use. Write a message that names the likely mix-up and points to what to review.

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. A message says "Incorrect. The answer is A." Is it strong? *(No. It gives the answer and no reason.)*
2. What does "Good try!" fail to do? *(It does not say whether the answer was right.)*
3. What four things does a helpful message do? *(Says the answer was wrong, explains why, points toward the right idea, and does not blame.)*

### Connection to the OER Evaluator rubric

Feedback is part of the practice and feedback metric. Because agents write practice questions in Chapter 15, reviewers use the same four criteria on what they produce.

## References

1. [Formative assessment](https://en.wikipedia.org/wiki/Formative_assessment) - Wikipedia - Describes assessment used during learning to guide teaching and give feedback, as opposed to grading at the end. Background for judging whether a resource's questions help learners improve.
2. [Testing effect](https://en.wikipedia.org/wiki/Testing_effect) - Wikipedia - Summarizes research showing that retrieving information from memory strengthens it more than rereading. Supports the chapter's sections on quizzes and retrieval practice.
3. [Formative vs Summative Assessment](https://www.cmu.edu/teaching/assessment/basics/formative-summative.html) - Carnegie Mellon Eberly Center - Contrasts assessment that guides learning with assessment that measures it, with examples of each. Helps reviewers decide whether a resource's quizzes give feedback or only a grade.
