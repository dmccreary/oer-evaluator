---
title: Instructor's Guide for OER Evaluator
description: How teachers, instructional designers, and librarians can use, teach from, and customize the OER Evaluator intelligent textbook, with classroom tips, licensing, analytics, and privacy guidance.
---

# OER Evaluator Instructor's Guide

Welcome to the instructor's guide for *OER Evaluator: Evaluating and Improving
Open Educational Resources with AI Agents*. This guide explains every feature
of the textbook, how to use it in a course or workshop, and how to make your
own customized copy. No technical background is assumed. Every technical term
is defined before it is used.

## About This Intelligent Textbook

### What Is an Intelligent Textbook?

An **intelligent textbook** is a digital textbook that goes beyond static text
and images. It adds interactive simulations, self-check quizzes, a searchable
glossary, and a structured map of how concepts depend on each other. The goal is
a richer experience than a printed book can give.

### The Five Levels of Intelligent Textbooks

Intelligent textbooks fall into five levels, based on how interactive and
adaptive they are:

| Level | Name | Description | Example Features |
|-------|------|-------------|------------------|
| **Level 1** | Static Digital | A PDF or basic web version of a print textbook | Text and images only |
| **Level 2** | Interactive | Adds simulations, quizzes, and searchable glossaries | MicroSims, self-check quizzes, concept search |
| **Level 3** | Adaptive | Adjusts content to student performance | Personalized learning paths |
| **Level 4** | AI-Assisted | Includes an AI tutor that answers student questions | Chatbot integration, automated feedback |
| **Level 5** | Fully Adaptive AI | Learns from student interactions and optimizes itself | Real-time content generation |

**This textbook is a Level 2 Interactive Intelligent Textbook.** It has 51
MicroSims, a quiz for every chapter, a glossary, a FAQ, and a learning graph.
It does not track individual students or adapt to them.

### What Makes This Textbook Different

- **A repeatable method.** The book teaches one 10-metric rubric (five
  *quality* metrics and five *reusability* metrics, 10 points each) and applies
  it by hand, then with AI agents.
- **Evidence over opinion.** Every chapter asks learners to name the evidence
  behind a score. The skill matters most when checking an AI agent's confident
  answer.
- **Improvement, not just judgment.** Later chapters use AI agents to raise a
  resource's score, then test whether the change helped with a manual A/B test
  with students.
- **Interactive MicroSims.** Learners manipulate small models in the browser
  with no software to install.
- **A learning graph.** A visual map of all 351 concepts and their
  prerequisites.
- **A mascot.** Echo the Loon, a friendly guide who appears in the student
  chapters.
- **Free and open.** The book is licensed CC BY-NC-SA 4.0, so you may copy and
  adapt it for non-commercial teaching.

## Who Should Use This Book

The target audience is teachers (K-12 and college), instructional designers,
librarians, and OER coordinators who select, adapt, or create open educational
resources. There are no prerequisites. Readers should be comfortable with a web
browser and a word processor. Experience with an AI chat assistant helps but is
not required, because the book teaches the AI-agent skills it uses.

The [Course Description](../course-description.md) lists the learning outcomes,
organized by the six levels of the 2001 Bloom taxonomy, and the topics the
book deliberately does not cover.

## Using the Chapters

### Chapter Structure

The book has **19 chapters** in a deliberate sequence. Each chapter builds on
earlier ones, so learners should work through them in order.

| Chapters | Topic Area |
|----------|-----------|
| 1 | Foundations: what OER are, the 5R permissions, adopt/adapt/create |
| 2 | Open licenses and attribution |
| 3 | The 10-metric rubric and scoring |
| 4 | Open file formats and version control |
| 5-8 | Quality metrics: accuracy and currency, alignment and readability, accessibility, practice and feedback |
| 9-10 | Reusability metrics: modularity and metadata, portability and reuse |
| 11 | Manual evaluation and adoption decisions |
| 12-14 | AI agents: prompts and rubric scoring, automated checks, cost and privacy, checking and calibrating agent output |
| 15 | Improving a resource with AI agents |
| 16-17 | Designing and analyzing an A/B test with students |
| 18 | Reusable components and publishing OER |
| 19 | Training teachers and certifying reviewers |

The [List of Chapters](../chapters/index.md) shows every chapter with its
summary.

### What Each Chapter Contains

1. **Front matter.** Metadata at the top of the file (title, description,
   version). Students do not see it. Search engines and the site builder do.
2. **Summary.** A short overview of what the chapter covers.
3. **Concepts covered.** The specific concepts from the learning graph that
   the chapter addresses.
4. **Prerequisites.** Links to earlier chapters.
5. **Main content.** The core material, with tables, worked examples, and
   embedded MicroSims.
6. **Mascot admonitions.** Short callout boxes from Echo (see
   [Meet Echo](#echo-the-loon-the-pedagogical-agent) below).
7. **Key takeaways.** A numbered summary of the most important ideas.
8. **Quiz and references.** Separate pages linked under each chapter in the
   left navigation.

### Suggested Classroom Use

- **Before class.** Assign the chapter as reading. The MicroSims keep
  independent reading active.
- **During class.** Project a MicroSim and ask learners to predict what
  happens when you move a slider, then test the prediction.
- **After class.** Assign the chapter quiz as a self-check, then have learners
  apply the rubric to a real resource.
- **Pacing.** Plan roughly two to three class periods (90 to 135 minutes) per
  chapter. Chapters with more MicroSims take longer. For a short course, see
  the formats below.

### Course Formats

| Format | Suggested Path |
|--------|---------------|
| One-day workshop | Chapters 1-3, 11, 15 and a hands-on scoring practice. See the [workshop materials](../workshops/index.md) and the [Sample One-Day Schedule](../workshops/sample-one-day-schedule.md). |
| Manual-evaluation unit | Chapters 1-11 with the [Sample Rubric Worksheet](../workshops/sample-rubric-worksheet.md) |
| AI-agent unit | Chapters 12-15 after learners can score by hand |
| Research or capstone project | Chapters 16-17, designing and analyzing an A/B test |
| Reviewer training | Chapter 19, built on the earlier chapters |

!!! note "Teach the manual rubric first"
    Learners who score by hand before using an AI agent can tell when the agent
    is wrong. Chapter 14 depends on that skill.

## Using the MicroSims

### What Is a MicroSim?

A **MicroSim** (micro-simulation) is a small interactive model that runs in a
web browser. Learners change one or more variables with sliders, buttons, or
drag-and-drop and see the result immediately. No software installation is
needed. MicroSims work in any modern browser (Chrome, Firefox, Safari, Edge) on
a computer, tablet, or phone.

### How MicroSims Are Embedded

MicroSims appear in the chapter text as rectangular interactive areas. They are
embedded with an **iframe**, a web feature that shows one web page inside
another. You do not need to understand iframes. The MicroSim loads
automatically when a learner opens the page.

The book has **51 MicroSims**. Browse them all on the
[MicroSims list](../sims/index.md). A few examples:

| MicroSim | What It Teaches |
|----------|-----------------|
| [Creative Commons License Switches](../sims/cc-license-switches/index.md) | How each license element changes what you may do |
| [Total Score Calculator](../sims/total-score-calculator/index.md) | How ten metric scores combine into one 100-point total |
| [Weak and Strong Prompt](../sims/weak-and-strong-prompt/index.md) | Why specific prompts produce better agent scoring |
| [Inter-Rater Agreement Explorer](../sims/inter-rater-agreement-explorer/index.md) | How to measure whether two reviewers agree |
| [Five Confounders](../sims/five-confounders/index.md) | What can spoil an A/B test |

### Tips for Using MicroSims in Class

1. **Project them.** Ask learners to call out a prediction before you change a
   control.
2. **Let learners explore.** After a demonstration, give them five to ten
   minutes to experiment on their own devices.
3. **Reset and retry.** Encourage learners to reset a MicroSim and try a
   different scenario.
4. **Return to the text.** Each MicroSim sits near the concept it illustrates.
   After exploring, have learners re-read the surrounding text.
5. **Internet required.** MicroSims load from the website. For offline use,
   build the site locally (see "Customizing Your Own Textbook" below).

### Embedding a MicroSim in Your Own Page

You can add any MicroSim to a Google Site, a WordPress blog, a learning
management system (LMS) such as Canvas or Schoology, or a plain HTML file.
Paste one line of HTML:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/YOUR-MICROSIM-NAME/main.html"
    width="100%" height="450px"
    scrolling="no">
</iframe>
```

Replace `YOUR-MICROSIM-NAME` with the folder name of any MicroSim, for example
`cc-license-switches`. Some LMS platforms block iframes. If yours does, link to
the MicroSim page instead.

### MicroSim Specifications

Each MicroSim has its own lesson page with a description, the learning
objective, the controls, and lesson-plan ideas. Use these pages for planning
and to see the teaching intent behind each simulation.

## Using the Glossary

The **glossary** is an alphabetical list of the book's 351 key terms, each with a
short, precise definition. Learners reach it from the **Glossary** link in the left
navigation or from the search bar at the top of any page. The browser's find
command (Ctrl+F or Cmd+F) finds a term on the glossary page.

Ways to use it in class:

- **Vocabulary preview.** Before a chapter, have learners look up its key terms.
- **Definition matching.** Run a warm-up where learners match definitions to
  terms.
- **Student-written definitions.** Learners write their own definitions after
  reading, then compare them with the glossary.
- **Quick quizzes.** Use terms for flash cards or short formative checks.

## Using the FAQ

The **FAQ** (Frequently Asked Questions) holds 100 questions that learners and
reviewers commonly ask about evaluating OER, grouped by topic. Answers are
written at the same reading level as the chapters.

- **Discussion starters.** Pick two or three questions, have learners discuss,
  then reveal the answer.
- **Homework support.** Point learners to the FAQ for questions outside class.
- **Extension reading.** The FAQ covers angles that the chapter text skips.
- **Test review.** Learners can use it as a study guide.

## Using the Quizzes

Every chapter has a quiz page with ten multiple-choice questions, 190 in all.
Open the **Quiz** link under a chapter in the left navigation. Learners click a
question to reveal the answer and explanation after trying it.

Quizzes are **not graded automatically**. They are formative self-checks, not
summative tests.

- **Exit tickets.** Have learners take the quiz at the end of a session.
- **Pre-reading check.** Assign it before the chapter to see what learners
  already know.
- **Post-reading review.** Use it to find concepts that need re-teaching.
- **Pair discussion.** Learners discuss each question before revealing the
  answer.
- **Question bank.** Reuse the questions in your own assessments. The license
  permits it, with attribution and under the same license.

### Bloom's Taxonomy Levels

Each quiz question is tagged with a **Bloom's Taxonomy** level. Bloom's
Taxonomy classifies thinking skills from simple to complex:

| Level | Name | What It Means | Example Verbs |
|-------|------|--------------|---------------|
| L1 | Remember | Recall facts and definitions | Define, list, name |
| L2 | Understand | Explain concepts in your own words | Explain, describe, compare |
| L3 | Apply | Use concepts to solve problems | Calculate, demonstrate, solve |
| L4 | Analyze | Break down and examine relationships | Differentiate, organize |
| L5 | Evaluate | Make judgments based on criteria | Assess, justify, critique |
| L6 | Create | Produce original work | Design, construct, propose |

The quizzes target mostly levels L1 to L4. Rubric scoring practice, agent-output
checks, and the A/B test design in the later chapters reach L5 and L6.

## Using the References

Each chapter has an **Annotated References** page with about ten sources for
further reading. Each entry gives the title, a link, and a note on why the
source is useful. Wikipedia articles come first for stability and access,
followed by authoritative books and papers.

### A Note About Link Rot

**Link rot** happens when a web link stops working because the page moved or
was deleted. Wikipedia links are stable, but some others may age. If a link is
broken:

1. Search for the article title on the source's website.
2. Look for an archived copy in the [Wayback Machine](https://web.archive.org/).
3. Report it as a GitHub Issue (see "Feedback" below).

!!! tip "A good exercise"
    Checking whether a link still works is itself an OER evaluation skill
    (accuracy and currency, Chapter 5). Ask learners to audit a reference page.

## Using the Learning Graph

### What Is a Learning Graph?

A **learning graph** is a map showing how the concepts in a textbook depend on
each other. It is a **DAG** (Directed Acyclic Graph): a diagram of nodes joined
by one-way arrows, with no loops. An arrow from concept A to concept B means
"understand A before B."

This book's graph has 351 concepts in 14 categories. Open the
[Learning Graph](index.md) section of the left navigation to explore it and to
see the quality reports.

### How Teachers Can Use the Learning Graph

- **Prerequisite checking.** Before teaching a concept, confirm that learners
  have covered what it depends on.
- **Remediation.** When a learner struggles, trace back through the
  prerequisites to find the gap.
- **Curriculum mapping.** Compare the graph with your syllabus to find
  coverage gaps.
- **Enrichment.** Advanced learners can follow the graph forward to concepts
  beyond the current chapter.

### Reports in This Section

| Report | What It Tells You |
|--------|-------------------|
| [Course Description Assessment](course-description-assessment.md) | How complete the course description is |
| [Concept Enumeration](concept-list.md) | The full list of 351 concepts |
| [Graph Quality Analysis](quality-metrics.md) | Whether the graph is a valid DAG and how well connected it is |
| [Concept Taxonomy](concept-taxonomy.md) | The 14 concept categories |
| [Taxonomy Distribution Report](taxonomy-distribution.md) | How concepts spread across categories |
| [Book Metrics](book-metrics.md) | Chapters, words, MicroSims, quizzes, and other totals |
| [Chapter Metrics](chapter-metrics.md) | The same measures chapter by chapter |
| [Glossary Quality Report](glossary-quality-report.md), [FAQ Quality Report](faq-quality-report.md), [Quiz Generation Report](quiz-generation-report.md) | Quality checks on the supporting content |

## Echo the Loon: The Pedagogical Agent

A **pedagogical agent** is a character who appears in a textbook to guide
learners. Research on the **persona effect** suggests that such characters
improve engagement and learners' perception of the material.

This book's agent is **Echo the Loon**, who carries a magnifying glass and
asks, "What is the evidence?" Echo's catchphrase is "Let's dive in and check
the evidence!" See [Meet Echo](../img/mascot/character-sheet.md) for the full
character sheet.

Echo appears as colored callout boxes (called **admonitions**) in student
chapters. There are seven types:

| Type | Purpose | Where It Appears |
|------|---------|------------------|
| Welcome | Introduces the chapter | Chapter opening |
| Thinking | Highlights a key insight | Occasionally |
| Tip | Shares practical advice | As the material warrants |
| Warning | Alerts to a common mistake | As the material warrants |
| Encourage | Supports learners on harder concepts | Where learners may struggle |
| Celebration | Marks progress | Chapter ending |
| Neutral | General note | Rarely |

Echo is used sparingly and never twice in a row. This instructor-facing guide
does not use Echo.

Tips for teachers:

- **Read Echo's tips aloud.** They are written in a calm, conversational voice.
- **Use "thinking" boxes as discussion prompts.** They mark the most
  important insights.
- **Point frustrated learners to "encourage" boxes.**

The [Mascot Rendering Test](mascot-test.md) page shows all seven styles.

## Feedback

### Reporting Issues and Suggestions

This book is an open-source project on **GitHub**, a website where projects are
built collaboratively. You do not need to program to report a problem.

A **GitHub Issue** works like a support ticket. Each issue has a number and can
be discussed by the author and the community.

1. Go to the [GitHub repository](https://github.com/dmccreary/oer-evaluator).
2. Click the **Issues** tab.
3. Click the green **New issue** button.
4. Give a clear title, such as "Broken link in Chapter 5 references".
5. In the description, say which page has the problem, what you expected, what
   you saw, and your browser and device if relevant.
6. Click **Submit new issue**.

A free GitHub account is required. If you prefer not to make one, use the
[Contact](../contact.md) page.

Welcome feedback includes typos and factual errors, broken links, MicroSim bugs,
content suggestions, and accessibility problems.

## Understanding the License

### What Is a Creative Commons License?

A **license** is a legal document that says what others may do with a work. A
**Creative Commons (CC) license** is a standard, plain-language license used
for educational and creative content. This is the same kind of license that the
book teaches learners to read.

### This Textbook's License

The book uses **CC BY-NC-SA 4.0**:

| Code | Full Name | What It Means |
|------|-----------|---------------|
| **CC** | Creative Commons | A standard open license |
| **BY** | Attribution | You must credit the author |
| **NC** | NonCommercial | You may not use the material to make money |
| **SA** | ShareAlike | If you modify it, you must share it under the same license |
| **4.0** | Version 4.0 | The current version of the license |

### What You Can Do

- **Copy** the book or single chapters for your learners.
- **Share** the link with colleagues, learners, or parents.
- **Print** chapters for classroom use.
- **Modify** the content: add examples, remove sections, reorder chapters.
- **Translate** it into other languages.
- **Build a derivative** version based on this one.

### What You Cannot Do

- **Sell** the book or charge learners for access.
- **Remove attribution.** You must credit the original author, Dan McCreary.
- **Use a different license.** A modified version must stay CC BY-NC-SA 4.0.
- **Claim it as your own work.**

!!! warning "Check the NonCommercial line before a paid workshop"
    "NonCommercial" has gray areas, and Chapter 2 covers them. If you charge a
    fee for a workshop that uses this book, read the license and the
    NonCommercial chapter material first, or ask the author.

See the [Creative Commons License](../license.md) page for the full legal text.

## Customizing Your Own Textbook

You can make your own customized copy. This section explains how, step by
step.

### Key Technical Terms

- **Repository (repo).** A folder on GitHub that holds all of a project's
  files.
- **Git.** A tool that tracks changes to files and who made them.
- **Clone.** A complete copy of a repository on your own computer.
- **Fork.** A complete copy of a repository in your own GitHub account.
- **MkDocs.** The software that turns the book's Markdown files into a
  website.
- **Markdown.** A simple text format. `**bold**` makes **bold**, `# Heading`
  makes a heading, and `-` makes a bullet point.
- **mkdocs.yml.** The main settings file for the site. It controls the title,
  navigation, colors, and enabled features.

### Step 1: Create a GitHub Account

If you do not have one, create a free account at [github.com](https://github.com).

### Step 2: Fork or Clone the Repository

**Option A: Fork (easier, stays on GitHub)**

1. Go to the [repository](https://github.com/dmccreary/oer-evaluator).
2. Click **Fork** in the upper right.
3. You now have a copy in your own account that you can edit.

**Option B: Clone (more control, works on your computer)**

1. Install Git from [git-scm.com](https://git-scm.com/).
2. Open a terminal (Command Prompt on Windows, Terminal on Mac).
3. Run:

```bash
git clone https://github.com/dmccreary/oer-evaluator.git
```

### Step 3: Make Changes

All content lives in the `docs/` folder as Markdown (`.md`) files. Edit them
with any text editor.

#### Change the Title and Description

Edit these lines in `mkdocs.yml`:

```yaml
site_name: "Your Custom Textbook Title"
site_description: "Your description here"
site_author: "Your Name"
```

#### Change the Colors

Find the `palette` section in `mkdocs.yml`:

```yaml
theme:
  palette:
    primary: indigo    # try blue, red, purple, teal, green, and others
    accent: orange     # the accent color
```

#### Change the Logo

Replace the logo file under `docs/img/` with your own PNG image, about 128 by
128 pixels.

!!! note "Keep the license notice"
    If you share your customized version, keep the CC BY-NC-SA 4.0 notice and
    credit the original author.

### Step 4: Preview Your Changes

1. Install Python (3.8 or newer) from [python.org](https://python.org).
2. Install MkDocs and the Material theme:

    ```bash
    pip install mkdocs mkdocs-material
    ```

3. In the project folder, start the preview server:

    ```bash
    cd oer-evaluator
    mkdocs serve
    ```

4. Open `http://127.0.0.1:8000/oer-evaluator/` in your browser.

The preview refreshes each time you save a file.

### Step 5: Publish Your Version

To publish as a free website with GitHub Pages:

```bash
mkdocs gh-deploy
```

This publishes to `https://YOUR-USERNAME.github.io/oer-evaluator/` in about one
to two minutes.

## Customizing Your Analytics

### What Is Web Analytics?

**Web analytics** measures how visitors use a website: which pages they visit,
how long they stay, and where they come from. For a textbook, it shows which
chapters are read and which MicroSims are used.

### Google Analytics

This book uses **Google Analytics**, a free Google service. The author's
property is already set up. If you make your own copy, create your own so that
your learners' visits are not mixed in with the author's.

1. Go to [analytics.google.com](https://analytics.google.com/) and sign in.
2. Create a **property** (Google's word for a tracked website).
3. Google gives you a **Measurement ID** that looks like `G-XXXXXXXXXX`.
4. Put it in `mkdocs.yml`:

    ```yaml
    extra:
      analytics:
        provider: google
        property: G-YOUR-MEASUREMENT-ID
    ```

5. Rebuild and deploy. Data appears within 24 to 48 hours.

What you can learn: most and least visited chapters, time on page, phone versus
computer use, and where visitors are located.

### xAPI Monitoring (Advanced)

**xAPI** (Experience API) is a standard for recording detailed learning
activity, such as "the learner answered question 3 correctly." An **LRS**
(Learning Record Store) is the database that holds those records.

!!! warning "Student privacy laws apply"
    Before collecting data that can identify individual learners, know the
    rules that apply to you:

    - **FERPA** (Family Educational Rights and Privacy Act), a U.S. law that
      protects student education records.
    - **COPPA** (Children's Online Privacy Protection Act), a U.S. law with
      extra limits for children under 13.
    - **State laws.** Many U.S. states add their own student privacy rules.
    - **GDPR** (General Data Protection Regulation), a European Union law that
      applies if any learner is in the EU.

The Google Analytics setup above is anonymous by default: it counts page views,
not individual people. That is the safest choice. If you want per-learner
tracking, talk to your school or district data privacy officer first.

## Related Pages

- [Course Description](../course-description.md): audience, topics, and Bloom-level outcomes
- [Rubric Specification](../rubric-spec.md): the full 10-metric rubric
- [Workshop materials](../workshops/index.md): sample schedules and worksheets
- [Glossary](../glossary.md) and [FAQ](../faq.md)
- [About This Book](../about.md)
