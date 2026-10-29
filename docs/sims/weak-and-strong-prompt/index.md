---
title: "Weak Prompt, Strong Prompt"
description: "Two prompt cards side by side, each divided into the five parts of a prompt; the weak card fills one band and leaves four empty, and the strong card fills all five."
image: /sims/weak-and-strong-prompt/weak-and-strong-prompt.png
og:image: /sims/weak-and-strong-prompt/weak-and-strong-prompt.png
twitter:image: /sims/weak-and-strong-prompt/weak-and-strong-prompt.png
social:
   cards: false
status: built
hide:
  - toc
---

# Weak Prompt, Strong Prompt

<iframe src="main.html" height="813px" width="100%" scrolling="no"></iframe>

[Run the Weak Prompt, Strong Prompt MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 12: AI Agents, Prompts, and Rubric Scoring](../../chapters/12-ai-agents-prompts-scoring/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `weak-and-strong-prompt.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/weak-and-strong-prompt/main.html"
        height="813px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Writing a rubric prompt is the first hands-on AI skill, and its five parts form a checklist. This poster sets two paper cards side by side, each divided into the same five bands: role, task, input, rules, and output format. The weak card says only "Check accessibility." and the other four bands are empty and hatched. The strong card fills all five. The wording comes from the Chapter 12 worked example. A good prompt does not guarantee a good answer, so Chapters 13 and 14 exist to check what comes back. The prompts are drawn as paper cards and not as a chat window, so the poster shows no brand interface.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Weak prompt | The weak prompt fills only the task band. |
| Strong prompt | The strong prompt fills all five bands. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The prompt text is drawn as live text so its wording is exact.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **evaluate** a prompt against the five parts of a rubric prompt and **name** the part that is missing. (Bloom level: Evaluate.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Prompts and the parts of a rubric prompt from [Chapter 12](../../chapters/12-ai-agents-prompts-scoring/index.md).

### Activities

1. **Explore (3 min).** Press each card. Which empty band of the weak prompt would cause the worst answer, and why?
2. **Quiz (3 min).** Press **Quiz Me** and match four descriptions to the two cards.
3. **Rewrite (4 min).** Take a prompt you have used. Fill in the five bands. Which one was missing?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Which part tells the model what to do when it cannot tell? *(Rules: write "not checkable".)*
2. Why does the strong prompt include the full text of the resource? *(The input band supplies the material, so the model does not assume it knows it.)*
3. Does a strong prompt guarantee a correct answer? *(No. Answers still need checking, which is why Chapters 13 and 14 exist.)*

### Connection to the OER Evaluator rubric

A rubric prompt is how an agent is told to apply the ten metrics and return evidence. The evidence column is what Chapter 14 checks.

## References

1. [Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering) - Wikipedia - Surveys techniques such as few-shot examples and chain-of-thought prompting for steering a model's output. Supports the chapter's guidance on writing prompts and prompt templates.
2. [Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) - Anthropic - Separates workflows from agents and describes patterns such as prompt chaining, routing, and evaluator-optimizer. Helps teachers understand the agent workflow this chapter uses for rubric scoring.
3. [Prompt Engineering Overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) - Claude Platform Docs - Official guidance on writing clear prompts, giving examples, and iterating with tests. Supports the chapter's section on prompt iteration, where a rubric prompt is refined after checking the agent's first results.
4. [Prompt Engineering Guide](https://www.promptingguide.ai/) - DAIR.AI - A free catalog of prompting techniques with examples, including zero-shot, few-shot, and chain-of-thought prompts. A handy reference while building a rubric prompt.
