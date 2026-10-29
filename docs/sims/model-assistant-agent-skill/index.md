---
title: "Model, Assistant, Agent, Skill"
description: "Four stacked layers, each built on the one below it: a language model, an AI assistant, an AI agent, and an agent skill, with the book's own example for each."
image: /sims/model-assistant-agent-skill/model-assistant-agent-skill.png
og:image: /sims/model-assistant-agent-skill/model-assistant-agent-skill.png
twitter:image: /sims/model-assistant-agent-skill/model-assistant-agent-skill.png
social:
   cards: false
status: built
hide:
  - toc
---

# Model, Assistant, Agent, Skill

<iframe src="main.html" height="741px" width="100%" scrolling="no"></iframe>

[Run the Model, Assistant, Agent, Skill MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 12: AI Agents, Prompts, and Rubric Scoring](../../chapters/12-ai-agents-prompts-scoring/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `model-assistant-agent-skill.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/model-assistant-agent-skill/main.html"
        height="741px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

The vocabulary is the first barrier in the AI half of the book, and mixing the terms leads to wrong decisions about what to trust. This poster stacks four layers, each built on the one below. A large language model predicts the next piece of text and does not look facts up. An AI assistant is a program you talk to in ordinary language that answers and waits. An AI agent adds tools, files, and a loop of observe, decide, act, and observe the result. An agent skill is a packaged set of instructions that is the durable, shareable form of a rubric prompt. The poster leaves out product and model names, which date quickly.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Large language model | Predicts the next piece of text, one piece at a time. |
| AI assistant | A program you talk to in ordinary language. It answers and waits. |
| AI agent | Works toward a goal over several steps, using tools and files. |
| Agent skill | A saved set of instructions that an agent loads when a task matches. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The poster leaves out product and model names, which date quickly, and uses no robot or glowing-brain pictures.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **distinguish** a language model, an assistant, an agent, and a skill, and **say** which layer adds tools and a loop. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The vocabulary of [Chapter 12](../../chapters/12-ai-agents-prompts-scoring/index.md).

### Activities

1. **Explore (3 min).** Press each layer from the bottom up. What does each step add?
2. **Quiz (3 min).** Press **Quiz Me** and match four descriptions to the layers.
3. **Sort (4 min).** Write down three AI tools you have used. Which layer is each one, and what would you need to check?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Which layer answers and waits? *(The AI assistant.)*
2. Which layer plans, acts, looks at what happened, and acts again? *(The AI agent.)*
3. What does a language model not do? *(It does not look facts up, and it can sound sure when it is wrong.)*

### Connection to the OER Evaluator rubric

The difference between an assistant that answers and an agent that acts across steps decides what a reviewer must check in Chapters 13 and 14.

## References

1. [Large language model](https://en.wikipedia.org/wiki/Large_language_model) - Wikipedia - Explains how large language models are trained, how they use tokens and context, and what they can and cannot do. Background for the chapter's sections on models and the context window.
2. [Intelligent agent](https://en.wikipedia.org/wiki/Intelligent_agent) - Wikipedia - Defines an agent as a system that perceives its environment and acts toward goals, with common agent types. The foundation for the chapter's distinction between an assistant and an agent.
3. [Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents) - Anthropic - Separates workflows from agents and describes patterns such as prompt chaining, routing, and evaluator-optimizer. Helps teachers understand the agent workflow this chapter uses for rubric scoring.
4. [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) - Claude Platform Docs - Explains skills as packaged instructions and resources that an agent loads when relevant. Shows the format behind the reusable evaluator skills this book teaches readers to build.
