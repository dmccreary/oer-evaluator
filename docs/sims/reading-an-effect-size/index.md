---
title: "Reading an Effect Size"
description: "Three pairs of overlapping bell curves show d of 0.2 (small), 0.5 (medium), and 0.8 (large), with a caution about a pilot whose d was about 1.03."
image: /sims/reading-an-effect-size/reading-an-effect-size.png
og:image: /sims/reading-an-effect-size/reading-an-effect-size.png
twitter:image: /sims/reading-an-effect-size/reading-an-effect-size.png
social:
   cards: false
status: built
hide:
  - toc
---

# Reading an Effect Size

<iframe src="main.html" height="765px" width="100%" scrolling="no"></iframe>

[Run the Reading an Effect Size MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 17: Analyzing A/B Test Results](../../chapters/17-ab-testing-analysis/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `reading-an-effect-size.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/reading-an-effect-size/main.html"
        height="765px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Effect size is the hardest idea in the second half of the book for readers without statistics. Overlapping curves give the intuition without algebra. Each panel shows the control group as one curve and the treatment group as the other, with the two means marked and the overlap shaded. The more the curves separate, the larger d. All three panels use the same axes, and the curves are drawn from the normal density. The sizes are rules of thumb, and what counts as important depends on the cost of the change and the setting. The caution strip carries the Watershed Basics pilot: a difference of 7.0 over a pooled standard deviation of about 6.78 gives d of about 1.03, and a big number from a small test deserves a second look.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Small: d = 0.2 | d = 0.2 is called small by convention, a rule of thumb. |
| Medium: d = 0.5 | d = 0.5 is called medium by convention, a rule of thumb. |
| Large: d = 0.8 | d = 0.8 is called large by convention, a rule of thumb. |
| Caution: a pilot with d about 1.03 | A d of about 1.03 from 12 students per group deserves a second look. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The curves are normal densities with equal spread, drawn in code. The d labels are rules of thumb and not cutoffs.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **interpret** d values of 0.2, 0.5, and 0.8 as the overlap between two groups, and **explain** why a large d from a small test deserves caution. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Means, spread, and effect size from [Chapter 17](../../chapters/17-ab-testing-analysis/index.md).

### Activities

1. **Explore (3 min).** Press each panel. How much of the control curve is still overlapped at d = 0.8?
2. **Quiz (3 min).** Press **Quiz Me** and match four descriptions to the panels.
3. **Compute (4 min).** Use the formula for a difference of 4.0 and a pooled standard deviation of 8.0. Which panel is closest?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. What does d measure? *(The difference of the two group means in units of the pooled standard deviation.)*
2. What size is d = 0.5 by convention? *(Medium, a rule of thumb.)*
3. Why is the pilot's d of about 1.03 not the number to plan the next test on? *(A small pilot gives a noisy estimate, and impressive estimates from small tests tend to shrink when repeated.)*

### Connection to the OER Evaluator rubric

Effect size is how Chapter 17 puts a difference on a common ruler. A teacher can compare tests with different spreads.

## References

1. [Effect size](https://en.wikipedia.org/wiki/Effect_size) - Wikipedia - Explains effect sizes such as Cohen's d, how they are computed, and how to interpret them. Supports the chapter's section on reading the size of a difference, not only whether it exists.
2. [Using Effect Size—or Why the P Value Is Not Enough](https://pmc.ncbi.nlm.nih.gov/articles/PMC3444174/) - Journal of Graduate Medical Education - Sullivan and Feinn explain why a significant p value says little about how large or useful a difference is. A short, readable argument for reporting effect size.
3. [Interpreting Cohen's d](https://rpsychologist.com/cohend/) - R Psychologist (Kristoffer Magnusson) - An interactive visualization showing how two overlapping distributions change as Cohen's d grows. Helps teachers picture what a small or medium effect looks like.
4. Statistical Power Analysis for the Behavioral Sciences (2nd ed.) - Jacob Cohen - Lawrence Erlbaum Associates (1988) - Cohen introduced the standardized difference d and offered 0.2, 0.5, and 0.8 as rough small, medium, and large conventions. He also showed how to plan sample size for them. The source of this chapter's effect size convention.
