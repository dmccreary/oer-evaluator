---
title: "Four Ways an Agent Gets It Wrong"
description: "Four field-guide cards for the agent error types, each with what it looks like, how a reviewer catches it, and how a prompt prevents it, plus the worked example \"A 9 that should be a 5\"."
image: /sims/four-agent-error-types/four-agent-error-types.png
og:image: /sims/four-agent-error-types/four-agent-error-types.png
twitter:image: /sims/four-agent-error-types/four-agent-error-types.png
social:
   cards: false
status: built
hide:
  - toc
---

# Four Ways an Agent Gets It Wrong

<iframe src="main.html" height="789px" width="100%" scrolling="no"></iframe>

[Run the Four Ways an Agent Gets It Wrong MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 14: Checking and Calibrating AI Agent Output](../../chapters/14-checking-agent-output/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `four-agent-error-types.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/four-agent-error-types/main.html"
        height="789px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Classifying errors by type is a stated course outcome, because the type tells the reviewer how to catch the error and the prompt writer how to prevent it. This poster is a field guide for the review desk. Each card has the same three parts: what the error looks like, how to catch it, and how to prevent it. The inset at the bottom is the Chapter 14 worked example, "A 9 that should be a 5": the agent reported a 9, and its own evidence supports five passing checks. The tone is gently skeptical and not mocking.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Factual error | A wrong claim about the resource, such as a feature that is absent or a count that is off. |
| License error | A wrong reading of the resource's license, or a missed or mismatched license. |
| Citation error | A reference that does not exist or does not support its claim. |
| Scoring error | A score that does not follow from the agent's own checks, or arithmetic that does not add up. |
| A 9 that should be a 5 | The agent reported accessibility 9. Its evidence supports five passing checks, so the score is 5. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The "9 that should be a 5" example is from the chapter. The chapter's sources are invented, so the poster prints no real names.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **classify** an agent error as factual, license, citation, or scoring, and **name** the reviewer check and the prompt fix for it. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Hallucination and agent error types from [Chapter 14](../../chapters/14-checking-agent-output/index.md).

### Activities

1. **Explore (3 min).** Press each card and read the three parts. Which check needs the least outside information?
2. **Quiz (3 min).** Press **Quiz Me** and match four reviewer checks to the error types.
3. **Apply (4 min).** Find an agent report you have. Pick one claim and say which error type it could be, and which check would expose it.

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. A reference does not exist. Which error type is it? *(A citation error.)*
2. What do you do to catch a scoring error? *(Recount the passes, recompute the band, and re-add the total.)*
3. How can a prompt prevent a license error? *(Require the license statement quoted word for word, and "not stated" for anything it does not mention.)*

### Connection to the OER Evaluator rubric

Agent output is a draft that a person must check. The error type tells the reviewer where to look first.

## References

1. [Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)) - Wikipedia - Explains how AI systems produce confident but false output, including invented citations, and why it happens. Background for the chapter's sections on hallucination and invented citation.
2. [Reduce Hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) - Claude Platform Docs - Practical prompt techniques such as letting the model say it does not know, asking for direct quotes, and verifying claims. Supports the chapter's verification steps.
3. [Survey of Hallucination in Natural Language Generation](https://arxiv.org/abs/2202.03629) - arXiv - Ji and colleagues' survey sorts hallucinations into types and reviews how they are measured and reduced. Gives vocabulary for classifying an agent's errors.
