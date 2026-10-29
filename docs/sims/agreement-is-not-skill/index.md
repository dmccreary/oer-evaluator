---
title: "Agreement Is Not Skill"
description: "Three panels walk through the Chapter 14 example: 18 of 20 agree, most of that agreement is expected by chance, and kappa is only 0.44."
image: /sims/agreement-is-not-skill/agreement-is-not-skill.png
og:image: /sims/agreement-is-not-skill/agreement-is-not-skill.png
twitter:image: /sims/agreement-is-not-skill/agreement-is-not-skill.png
social:
   cards: false
status: built
hide:
  - toc
---

# Agreement Is Not Skill

<iframe src="main.html" height="765px" width="100%" scrolling="no"></iframe>

[Run the Agreement Is Not Skill MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 14: Checking and Calibrating AI Agent Output](../../chapters/14-checking-agent-output/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `agreement-is-not-skill.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/agreement-is-not-skill/main.html"
        height="765px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

This is the most counterintuitive statistic in the book, and teachers often report only the agreement rate. The poster follows the worked example from Chapter 14: an agent and a human judge 20 resources as ready to adopt or not. Panel 1 is the count table, with the diagonal of agreements highlighted. Panel 2 shows the chance baseline as a filled bar: most of the 90 percent agreement is expected by luck. Panel 3 shows kappa as (0.90 − 0.82) / (1 − 0.82), which is 0.44. The agent found only one of the two resources the human judged ready. The poster gives no numeric cutoffs for kappa, because the chapter says to check cutoffs against the source before quoting them.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| 1: Count the agreements | The agent and the human agree on 18 of 20 resources, an agreement rate of 0.90. |
| 2: Subtract what luck gives | Chance agreement is 0.82, so most of the 0.90 agreement is expected by luck. |
| 3: Kappa | Kappa = (0.90 − 0.82) / (1 − 0.82) = 0.08 / 0.18, about 0.44. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The numbers are from the Chapter 14 worked example. The poster prints no numeric kappa cutoffs.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **compute** Cohen's kappa from a count table and **explain** why 90 percent agreement can be a kappa of only 0.44. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Inter-rater agreement and Cohen's kappa from [Chapter 14](../../chapters/14-checking-agent-output/index.md).

### Activities

1. **Explore (3 min).** Press each panel in order, 1 to 3. Where does the chance baseline come from?
2. **Quiz (3 min).** Press **Quiz Me** and match four statements to the panels.
3. **Compute (4 min).** Change one cell of the table in your head (for example, 2 both ready and 16 both not ready). Does kappa rise or fall?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Why is a 90 percent agreement not impressive in this example? *(Almost everything is "not ready", so two raters would agree 82 percent of the time by chance.)*
2. What is the formula for kappa? *((po − pe) / (1 − pe).)*
3. What should you always show beside kappa? *(The count table.)*

### Connection to the OER Evaluator rubric

Calibration compares the agent with trained humans. Reporting kappa with the count table keeps the comparison honest.

## References

1. [Cohen's kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa) - Wikipedia - Defines Cohen's kappa, which measures agreement between two raters beyond chance, with a worked example. Supports the chapter's measures of agreement between an agent and human reviewers.
2. [Interrater Reliability: The Kappa Statistic](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/) - Biochemia Medica - McHugh explains kappa in plain terms, how to interpret its values, and where it misleads. A readable companion to the chapter's section on measuring agreement.
3. Handbook of Inter-Rater Reliability (4th ed.) - Kilem L. Gwet - Advanced Analytics (2014) - Gwet devised the AC1 statistic to fix the kappa paradox, in which high raw agreement can still yield a low kappa. The handbook explains agreement measures with worked examples.
