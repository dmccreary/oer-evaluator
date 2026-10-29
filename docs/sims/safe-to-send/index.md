---
title: "Safe to Send? Student Data and AI Services"
description: "Three chutes sort six items into send it, fix it first, and never send it, with a warning that text sent to an AI service cannot be pulled back."
image: /sims/safe-to-send/safe-to-send.png
og:image: /sims/safe-to-send/safe-to-send.png
twitter:image: /sims/safe-to-send/safe-to-send.png
social:
   cards: false
status: built
hide:
  - toc
---

# Safe to Send? Student Data and AI Services

<iframe src="main.html" height="741px" width="100%" scrolling="no"></iframe>

[Run the Safe to Send? Student Data and AI Services MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 13: Automated Checks, Cost, and Student Privacy](../../chapters/13-automated-checks-cost-privacy/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `safe-to-send.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/safe-to-send/main.html"
        height="741px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

A privacy mistake cannot be undone, and a teacher new to AI may paste a gradebook without thinking. This poster sorts the items from the Chapter 13 worked example into three chutes. The published text of an open textbook chapter and a rubric prompt template are safe to send. A class's quiz scores with student names need fixing first, because names make the scores personal data. A spreadsheet of grades with student ID numbers, a student's photograph, and an email thread with a parent about a student must never be sent. Shapes and icons carry the meaning as well as color, and a silhouette stands in for the photograph. The poster gives no legal advice.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Send it | Safe to send. |
| Fix it first | Anonymize or get approval. |
| Never send it | Do not send. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.

- The poster gives no legal advice. Your school's policy decides what you may send, and FERPA is the U.S. law that protects student education records.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **sort** six items into send it, fix it first, and never send it, and **state** why the sorting matters. (Bloom level: Apply.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- Student data privacy and FERPA from [Chapter 13](../../chapters/13-automated-checks-cost-privacy/index.md).

### Activities

1. **Explore (3 min).** Press each chute and read why each item belongs in it.
2. **Quiz (3 min).** Press **Quiz Me** and place six items in the right chute.
3. **Apply (4 min).** List three files you would like an AI service to help with. Which chute is each in? Who would you ask if you are not sure?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Why are quiz scores with names not safe as they are? *(Names make the scores personal data, so anonymize or get approval first.)*
2. Can you take back text you pasted into an AI service? *(No. It has left your computer, and a deletion request may not undo it.)*
3. What do you do if you are not sure an item is safe? *(Ask before you send it.)*

### Connection to the OER Evaluator rubric

The same care applies to the student-privacy rules for A/B tests in Chapter 16. Your school's policy decides what you may send.

## References

1. [Family Educational Rights and Privacy Act (FERPA)](https://studentprivacy.ed.gov/ferpa) - U.S. Department of Education - The Student Privacy Policy Office's official FERPA page, with guidance for schools and teachers on education records and disclosure. The primary source for the chapter's privacy rules.
2. [Family Educational Rights and Privacy Act](https://en.wikipedia.org/wiki/Family_Educational_Rights_and_Privacy_Act) - Wikipedia - Explains the U.S. law that protects the privacy of student education records and when schools may disclose them. The legal basis for the chapter's student data privacy guidance.
3. [Common Sense Privacy Program](https://privacy.commonsense.org/) - Common Sense Media - Evaluates the privacy policies of educational apps and tools and rates them. Helps teachers check an AI service's data practices before sending it any student material.
4. [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - NIST - A voluntary framework for governing, mapping, measuring, and managing the risks of AI systems. Supports decisions about which checks to automate and which need human oversight.
