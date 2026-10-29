---
title: "Five Ways a Test Can Lie to You"
description: "Five paired panels, one per confounder, each showing a tilted balance scale for how it misleads and a level scale for the defense."
image: /sims/five-confounders/five-confounders.png
og:image: /sims/five-confounders/five-confounders.png
twitter:image: /sims/five-confounders/five-confounders.png
social:
   cards: false
status: built
hide:
  - toc
---

# Five Ways a Test Can Lie to You

<iframe src="main.html" height="741px" width="100%" scrolling="no"></iframe>

[Run the Five Ways a Test Can Lie to You MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 16: Designing an A/B Test with Students](../../chapters/16-ab-testing-design/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `five-confounders.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/five-confounders/main.html"
        height="741px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Small classroom tests fail on confounds far more often than on statistics. This poster is a pre-flight checklist for a test plan. Each of the five panels from the Chapter 16 table has a pair of balance scales. The top scale is tilted by a hidden weight, which is how the confounder misleads. The bottom scale is level, which is the defense. The weights are neutral: a confounder is hidden and is not villainous. Before you trust any difference between groups, ask what else is different besides the version.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Different teachers | How it misleads: One teacher's enthusiasm lifts one group. The defense: One teacher for both groups. |
| Different times of day | How it misleads: Students are more alert at one time. The defense: Both groups at the same time. |
| Extra help | How it misleads: One group gets a review or hints. The defense: The same script and help for both. |
| Different tests | How it misleads: The versions are measured in different ways. The defense: The same test and key for both. |
| Student choice | How it misleads: Motivated students choose one version. The defense: Random assignment. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The weights are drawn as neutral gray blocks, since a confounder is hidden and is not a villain.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **identify** the confounder in a test setup and **name** its defense. (Bloom level: Analyze.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The control group and the one-difference rule from [Chapter 16](../../chapters/16-ab-testing-design/index.md).

### Activities

1. **Explore (3 min).** Press each panel. What is the hidden weight in each tilted scale?
2. **Quiz (3 min).** Press **Quiz Me** and match four test setups to their confounders.
3. **Preflight (4 min).** Take a test plan of your own. Go through the five panels and say which defense you use for each.

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Students choose which version to use. What is the confounder, and what is the defense? *(Student choice, because motivated students choose one version. Defense: random assignment.)*
2. One group takes the test in the morning and the other after lunch. Which confounder? *(Different times of day. Run both groups at the same time.)*
3. What question should you ask before trusting a difference between groups? *(What else was different besides the version?)*

### Connection to the OER Evaluator rubric

This is the one-difference rule: arrange everything except the version to be the same, and let random assignment handle what you cannot arrange.

## References

1. [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) - Wikipedia - Defines A/B testing, how users are split between versions, and how results are compared. The core idea behind comparing an original resource with its improved version.
2. [Randomized controlled trial](https://en.wikipedia.org/wiki/Randomized_controlled_trial) - Wikipedia - Explains random assignment to treatment and control groups and why it supports causal claims. Background for the chapter's sections on random assignment and control and treatment groups.
3. [How Not To Run an A/B Test](https://www.evanmiller.org/how-not-to-run-an-ab-test.html) - Evan Miller - Explains why checking results repeatedly and stopping when they look good inflates false positives. A caution for anyone running a small test with students.
4. [Identifying and Implementing Educational Practices Supported by Rigorous Evidence](https://ies.ed.gov/use-work/resource-library/resource/handbook/identifying-and-implementing-educational-practices) - Institute of Education Sciences - A user-friendly guide to what counts as strong evidence in education, with emphasis on randomized studies. Helps teachers judge what their own small test can and cannot show.
