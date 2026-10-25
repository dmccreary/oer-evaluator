---
title: Frequently Asked Questions
description: Answers to the most common questions about the OER Evaluator book, the ten-metric rubric, AI-agent scoring, improving a resource, A/B testing with students, and the certificate, grouped by category.
category_count: 6
question_count: 103
---
# OER Evaluator FAQ

!!! mascot-welcome "Ask Away"
    ![Echo waving welcome](img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every teacher who tries the rubric ends up asking a few of the same questions, and the answers here are the ones that save the most time. Skim the headings, jump to the question you have, and follow the links when you want the full story. Let's dive in and check the evidence!

Questions are grouped from first steps to advanced topics. Each answer links to the chapter that teaches the idea in full, and every term is defined in the [glossary](glossary.md).

## Getting Started Questions

### What is this book about?

The OER Evaluator teaches a repeatable method for deciding whether an open educational resource (OER) is good and whether other teachers can actually reuse it. You score a resource on 10 metrics worth 10 points each, five for quality and five for reusability, for a total out of 100. You learn to score by hand first, then to direct an AI agent to make the first pass and check its evidence. The book then moves from evaluation to improvement and shows how to test with students whether a change helped.

**Example:** A department choosing between two open algebra textbooks scores both on the same ten metrics and compares the totals and subtotals instead of relying on first impressions.

The [course description](course-description.md) lays out the full scope, and [Chapter 1](chapters/01-foundations-of-oer/index.md) starts the content.

### Who is this book for?

The book is written for teachers in K-12 and college, instructional designers, librarians, and OER coordinators who select, adapt, or create open educational resources. If you choose course materials, advise people who do, or build lessons that others will reuse, you are the intended reader.

**Example:** A school librarian who maintains a shelf of open textbooks and a high-school science teacher who wants to improve one open unit would both use the same ten-metric rubric, each on their own resources.

The [course description](course-description.md) states the audience, and the [workshop pages](workshops/index.md) show how a group of about 20 teachers uses the book over one day.

### Do I need any background before I start?

No. The course description lists the prerequisites as none. You should be comfortable using a web browser and a word processor. Experience with an AI chat assistant helps but is not required, because the book teaches the AI-agent skills it uses.

A little Markdown and HTML appears when you publish a resource, but the book does not teach programming beyond simple prompts, Markdown, and HTML. If the vocabulary is new, [Chapter 1](chapters/01-foundations-of-oer/index.md) defines educational resource, copyright, public domain, and open educational resource before any later idea depends on them, and the [glossary](glossary.md) covers every term after that.

**Example:** A teacher who has only used a word processor and a search engine can start at Chapter 1 and follow the chapters in order.

### What will I be able to do when I finish?

You will be able to carry out the whole evaluate, improve, and test cycle on a resource from your own subject. The course description states the outcomes at all six levels of Bloom's Taxonomy, from Remember to Create. Among them, you will be able to:

- Define open educational resource and list the 5R permissions.
- Score a sample OER on all 10 metrics by hand and record evidence for each score.
- Write an AI-agent prompt that scores a resource against the rubric and returns evidence.
- Critique an agent's evaluation and decide which findings to accept, correct, or reject.
- Judge whether an OER is ready to adopt, needs revision, or should be rejected, and justify the decision.
- Design and run an A/B test that compares an original resource with its improved version.

The full list is in the [course description](course-description.md).

### What is the capstone project?

The capstone project is the book's culminating work. You evaluate one OER from your own subject, use AI agents to improve it on at least two quality metrics and two reusability metrics, test the change with students, and publish the result under a CC BY license.

[Chapter 19](chapters/19-training-certifying-reviewers/index.md) lays the project out in seven steps that map back to earlier chapters: choose and check the resource, evaluate it, check the agent, improve, test with students, publish, and share.

The chapter sets four tests for success:

- The resource gains on at least two quality and two reusability metrics, with evidence.
- A student test follows the consent and privacy rules.
- The result is published under CC BY with metadata.
- A report states the gain and the limits of the test honestly.

### How is the book organized?

The book has 19 chapters covering 351 concepts. Each chapter lists the concepts it covers, and the [chapter list](chapters/index.md) gives a summary of every one. In outline:

- **Chapters 1 and 2** cover OER foundations and open licensing.
- **Chapter 3** introduces the ten-metric rubric and how scoring works.
- **Chapters 4 to 10** teach how to score the metrics: editable source, accuracy and currency, alignment and readability, accessibility, practice and feedback, open license, modularity and metadata, and portability.
- **Chapter 11** covers scoring by hand and turning scores into an adopt, revise, or reject decision.
- **Chapters 12 to 14** introduce AI agents and prompts, automated checks, and how to check agent output.
- **Chapter 15** shows how to improve a resource with agents.
- **Chapters 16 and 17** teach designing and analyzing an A/B test with students.
- **Chapters 18 and 19** cover publishing OER and training and certifying reviewers.

### Do I have to read the chapters in order?

In general, yes. The chapters introduce concepts in dependency order, so each concept appears after the concepts it relies on. If you already know a topic well, look at the chapter's list of concepts and its prerequisites, then skip ahead.

The one chapter that is unwise to skip is [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md). Every later chapter that scores a resource, checks an agent's score, or measures improvement uses the ten-metric rubric introduced there. If you only need one skill, such as checking AI output, read Chapter 3 first and then go straight to [Chapter 14](chapters/14-checking-agent-output/index.md).

**Example:** A librarian who already knows Creative Commons licensing can skim the concept list of Chapter 2, then continue with Chapter 3.

### What is a learning graph, and how does it help me?

A learning graph is a map of the concepts of a subject in which each concept is linked to the concepts it depends on. It answers the question "What must a learner know before this?" For this book, the graph holds 351 concepts joined by 586 dependencies. It is a valid directed acyclic graph, so no concept depends on itself, even indirectly.

Six concepts have no prerequisites: Educational Resource, Copyright, Learning Outcome, Accessibility, AI Assistant, and Student Data Privacy. The longest chain of prerequisites runs 24 concepts deep. The graph decides the order of the chapters, and you can use it to see how a concept you are studying fits the larger picture.

The [learning graph overview](learning-graph/index.md) explains the files, and the [graph quality report](learning-graph/quality-metrics.md) gives the numbers.

### Where do I look up a term I don't know?

Use the [glossary](glossary.md). It defines all 351 concepts from the learning graph in alphabetical order. Each entry gives a one-sentence definition written to ISO 11179 style (precise, concise, and not circular), a note on why the term matters when you evaluate or improve an OER, an example for many terms, and related terms. The search bar at the top of every page also searches the whole book.

**Example:** Searching for Score Band finds the five named ranges of the total score: Excellent 90 to 100, Good 75 to 89, Fair 50 to 74, Weak 25 to 49, and Poor 0 to 24.

### Is there a workshop or a certificate?

Yes. The book supports a one-day workshop for about 20 teachers, from 8:30 a.m. to 3:30 p.m. Each teacher brings one OER from their own subject and leaves with an improved, openly licensed component and a checklist for the Certificate of OER Quality Evaluation Using AI Agents. The sample day moves from setup and the rubric to calibration against an agent, checking the agent's output, an improvement challenge, and peer review and publishing. After the workshop, teachers have 30 days to finish the certificate work, and a reviewer checks each submission against the rubric.

The [workshop pages](workshops/index.md) hold a sample schedule, a rubric worksheet, and a sample timeline, and [Chapter 19](chapters/19-training-certifying-reviewers/index.md) explains how to run the workshop and the certificate program.

### How much time should I plan to set aside?

The book does not set a study schedule, so plan from the pieces it does describe. The chapters range from about 5,000 to about 17,000 words each. The course description notes that a careful manual review of a single textbook can take hours, which is why the book teaches an AI-assisted first pass that you then check.

The sample workshop is one day. The certificate work that follows runs 30 days. A classroom A/B test takes about four weeks in the book's pilot: a pre-test in week 1, the lesson in weeks 2 and 3, and the post-test in week 4. The [sample timeline](workshops/grant-period-timeline.md) spreads a whole program from November 2026 to May 2027.

### Do I need special software or an AI account?

To read the book and score a resource by hand, you need a web browser and a word processor. An AI chat assistant becomes useful from [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md) on, and the workshop asks each teacher to bring a laptop with access to an AI agent tool.

Publishing uses a few free tools. [Chapter 4](chapters/04-open-formats-version-control/index.md) introduces Markdown, HTML, Git, and GitHub, and [Chapter 18](chapters/18-components-publishing-oer/index.md) shows how to publish with MkDocs and GitHub Pages. MkDocs is a free, Python-based site generator, and GitHub Pages is a free host, with usage limits and terms that change. The course description says experience with an AI assistant is helpful but not required.

**Example:** A teacher who only reads the chapters and scores one resource by hand needs nothing beyond a browser and a word processor.

### What does this book not cover?

The [course description](course-description.md) names six topics that are out of scope:

- Writing a complete textbook from scratch, or full instructional design for a course.
- Copyright law beyond what you need to read and apply open licenses.
- Training or fine-tuning AI models. The book uses existing AI agents.
- Programming beyond simple prompts, Markdown, and HTML.
- Learning management system administration and buying commercial materials.
- Statistical methods beyond basic comparisons of two groups.

Nothing in the book is legal advice. Where it touches fair use or student privacy law, it explains the idea and tells you to ask a qualified person.

**Example:** A teacher who wants to fine-tune a language model on their own lessons will need another source, because the book works with existing agents.

### Is this book itself an OER, and what license does it use?

The [license page](license.md) states that the book is released under Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). You may copy, share, and adapt it if you credit the author, do not use it commercially, and share your adaptations under the same license. The copyright holder reserves commercial rights.

That puts the book at the more restrictive end of what its own rubric rewards. [Chapter 2](chapters/02-open-licenses-attribution/index.md) explains that NonCommercial terms narrow reuse, and the open license metric loses points for them. The book recommends CC BY for the components you publish yourself. In practice, treat this book as free to share and adapt for noncommercial purposes, and not as fully open in the 5R sense.

### How do I report a problem or give feedback?

The [contact page](contact.md) invites feedback through the author's LinkedIn profile. The book's source is a public GitHub repository at [github.com/dmccreary/oer-evaluator](https://github.com/dmccreary/oer-evaluator), which is also where you can copy it.

When you report a factual error, use the habit [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md) teaches for evidence: say where you looked, what you saw, and which rule or source you compared it with. A report that names the page, the passage, and the source is quick to check and quick to fix.

**Example:** "Chapter 7, contrast section: the text lists one ratio, but the calculator I used gives a different ratio for the same two colors." [Chapter 18](chapters/18-components-publishing-oer/index.md) explains why a project should offer more than one feedback channel and say how quickly it will reply.

## Core Concepts

### What is an open educational resource?

An open educational resource (OER) is a teaching, learning, or research material that is in the public domain or released under an open license that gives everyone permission to retain, reuse, revise, remix, and redistribute it. Two tests apply. First, it must be an educational resource, meaning any material a teacher or learner uses to support teaching and learning. Second, it must be either in the public domain or openly licensed.

The format does not matter. A textbook, a quiz, a video, an image, and a simulation can all be OER. What makes a resource open is the permission it grants, not its price or its file type.

**Example:** An introductory statistics textbook under CC BY, which teachers may download, edit, and post on a school website, is an OER. A video lecture that streams without charge but forbids copying is free, and it is not an OER.

[Chapter 1](chapters/01-foundations-of-oer/index.md) defines the term and its related vocabulary.

### What are the 5R permissions?

The 5R permissions are the five rights that together define an open resource: retain, reuse, revise, remix, and redistribute. David Wiley named them. A question for each makes them easy to apply to a real resource:

- **Retain:** Can I make and keep my own copy?
- **Reuse:** Can I use it as it is?
- **Revise:** Can I change it?
- **Remix:** Can I combine it with other open work?
- **Redistribute:** Can I share copies with others?

The open license metric asks which of the five a resource actually grants, and the improvement work in this book depends on revise and redistribute.

**Example:** A teacher downloads a chapter (retain), assigns it as written (reuse), translates it into Spanish (revise), combines it with another open chapter (remix), and emails the result to a colleague (redistribute). That one resource passed all five tests.

See [Chapter 1](chapters/01-foundations-of-oer/index.md).

### What is the difference between a free resource and an open one?

Free describes price, and open describes permission. They are separate dials, and turning one tells you nothing about the other. A free resource costs the user nothing, whether or not the owner grants any permission to copy, change, or share it. An open resource grants the 5R permissions, and it may or may not cost money, for example when a print shop charges for a printed copy.

For that reason the rubric checks the legal terms, not the price. A free resource with all rights reserved scores low on the open license metric. The same distinction separates a zero textbook cost (ZTC) course, where students pay nothing, from an open course. A course built on e-books that the library licenses is ZTC, and it is not open.

**Example:** A publisher's free online reader that students cannot download or adapt is free. An open textbook that a school prints for $15 a copy is open.

[Chapter 1](chapters/01-foundations-of-oer/index.md) explains the distinction in detail.

### How do OER compare with a commercial textbook?

A commercial textbook is sold by a publisher for profit under traditional copyright, with most rights kept by the publisher, usually in print or as a paid digital edition. It is the cost and rights baseline against which OER are compared. Cost is a main reason teachers adopt OER, and the goal is course material affordability: the total price of materials is low enough that every student can get every item.

The rubric adds a second question that price alone cannot answer, which is whether the low-cost resource is also good and reusable. You can score a commercial textbook with the same ten metrics to see what a switch would gain or lose.

**Example:** The book's illustrative figures: a section of 30 students needs a $120 textbook plus a $40 access code, which is $160 per student and $4,800 in all. A digital open textbook costs $0. Optional printed copies at $15 each cost $450 for all 30 students.

See [Chapter 1](chapters/01-foundations-of-oer/index.md).

### Does public domain content count as OER?

Yes. The definition of OER covers resources that are in the public domain or that carry an open license. A public domain work is one that copyright does not cover, and there are three routes in: expiration of the copyright term, ineligibility for copyright, and dedication by the owner. Official work of U.S. federal employees, such as most NASA images, is ineligible, and a CC0 dedication is the common form of the third route.

Public domain works carry no license conditions, so they are easy to reuse. A reviewer still looks for a clear note that a work is in the public domain, because a reuser cannot simply assume it. Check each image on an agency page too, since partner images may keep their own copyright.

**Example:** A report that a United States federal agency wrote as part of its official duties is in the public domain. A photograph on the same page that a partner organization supplied may not be.

See [Chapter 1](chapters/01-foundations-of-oer/index.md) and [Chapter 2](chapters/02-open-licenses-attribution/index.md).

### What do BY, SA, NC, and ND mean in a Creative Commons license?

Creative Commons licenses are built from four elements:

- **Attribution (BY):** You must credit the creator, give the license and a link to it, and note any changes.
- **ShareAlike (SA):** An adaptation must carry the same license, or a compatible one.
- **NonCommercial (NC):** The work may not be used primarily for commercial advantage or monetary compensation.
- **NoDerivatives (ND):** You may share only the unchanged work.

BY appears in six of the seven Creative Commons tools, and SA and ND never appear together. Each element beyond BY takes a freedom away from the person who receives the work. CC BY is the most open of the six licenses, and CC BY-NC-ND is the most restrictive.

**Example:** CC BY-NC-SA asks for credit, no commercial use, and the same license on any adaptation.

The [License Switches MicroSim](sims/cc-license-switches/index.md) lets you flip the switches and watch the license change, and [Chapter 2](chapters/02-open-licenses-attribution/index.md) teaches the family in full.

### What is the ten-metric rubric?

The ten-metric rubric is the scoring guide at the center of this book. It rates an OER on ten metrics, five for quality and five for reusability, each scored as a whole number from 0 to 10, for a total out of 100. A shared rubric keeps scores comparable across reviewers, and splitting the judgment into ten metrics keeps a high total from hiding a failed area.

The rubric deliberately leaves some things out: whether students learn more from the resource, how well it fits your particular students, and your schedule or budget. Chapters 16 and 17 test whether higher scores go with better learning.

**Example:** A reviewer gives one resource 8 for readability, 3 for accessibility, and 9 for open license, continues through all ten metrics, and adds the scores.

Start with [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md). If you have also seen the [rubric specification](rubric-spec.md), read the answer on how the two relate in the Advanced Topic Questions.

### Which five metrics measure quality and which five measure reusability?

The five **quality** metrics measure how well the resource helps learners learn:

- Accuracy and currency ([Chapter 5](chapters/05-accuracy-currency/index.md))
- Alignment and readability, which are two separate metrics ([Chapter 6](chapters/06-alignment-readability/index.md))
- Accessibility ([Chapter 7](chapters/07-accessibility/index.md))
- Practice with feedback ([Chapter 8](chapters/08-practice-feedback/index.md))

The five **reusability** metrics measure how easily other people can find, change, and reuse the resource:

- Open license, modularity, and metadata ([Chapter 9](chapters/09-modularity-metadata/index.md))
- Editable source ([Chapter 4](chapters/04-open-formats-version-control/index.md))
- Portability ([Chapter 10](chapters/10-portability-reuse/index.md))

On the worksheet the metrics appear in a fixed order, quality first, and the numbers show order only. They do not show importance. Each half adds up to a subtotal of 0 to 50.

**Example:** The book's sample resource scored 7, 6, 8, 5, and 6 on the five quality metrics, a subtotal of 32, and 9, 5, 4, 8, and 7 on the five reusability metrics, a subtotal of 33.

### How is quality different from reusability?

Quality is the degree to which an OER helps its intended learners reach their intended learning outcomes. Reusability is how easily other people can find, change, and reuse the resource. They are independent. A resource can be strong in one and weak in the other, and all four combinations occur in practice.

The book names the four combinations: strong and open, good but locked, open but weak, and weak and locked. The cutoff between strong and weak is 25 of 50, and the book calls that a teaching choice, not a standard.

**Example:** A well-written lesson saved only as a locked PDF teaches well but is hard to reuse. A sloppy lesson under CC BY with clean source files is easy to reuse and may not be worth reusing.

!!! mascot-thinking "Two Scoreboards"
    ![Echo thinking](img/mascot/thinking.png){ class="mascot-admonition-img" }
    Picture two scoreboards side by side, one for how well the resource teaches and one for how freely it can travel. A resource can win one and lose the other, so read both before you decide anything.

See [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md).

### How do I choose a score from 0 to 10 for a metric?

Each metric has ten checks, and each check is a pass or a fail. Some checks are marked serious. You count the passes, convert the share to a band, and pick a number inside it:

- 0 percent of checks: score 0 (Absent).
- 1 to 24 percent: 1 to 2 (Very poor).
- 25 to 49 percent: 3 to 4 (Weak).
- 50 to 74 percent: 5 to 6 (Adequate).
- 75 to 89 percent: 7 to 8 (Good).
- 90 to 100 percent: 9 to 10 (Excellent).

Inside a two-number band, take the lower number if a serious check failed, and the higher number otherwise. A check that does not apply counts as passed, a check you did not test counts as failed until you test it, and a score of 10 requires every check to pass.

**Example:** The sample resource passed 8 of 10 accuracy and currency checks, a share of 80 percent, which falls in the 7 to 8 band. One failed check was serious, because a figure was outdated, so the score is 7.

[Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md) states the rules, and each metric chapter lists its own ten checks.

### How do I record evidence for a score?

Evidence has three parts: where you looked, what you saw, and which rule or check you compared it with. Write the citation as you find it, in that order, and add a date for anything that can change, such as a link test. If you sampled, record how you chose the sample and how large it was. Record passes as well as failures, so another reviewer can see what you actually checked.

An unchecked AI claim is not evidence, and neither is a hunch. Reviewer notes are leads that may turn into evidence once checked.

**Example:** "Figure 3 has no alt text; the check requires alt text on every informative image." Or, for a changeable fact: "Link test run 2026-10-12: 2 of 14 links return page not found."

The goal is that another reviewer can repeat your check in about a minute. See [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md) and [Chapter 11](chapters/11-manual-evaluation-adoption/index.md).

### How do I check whether a resource's facts and citations hold up?

Test a sample of at least 10 checkable facts, such as dates, numbers, names, definitions, and statements about cause. Spread them across sections. For each one, follow the fact-checking steps: write down the claim's exact words, decide what counts as a reliable source, find it (preferably the original), compare word for word and number for number, and record match, mismatch, or not addressed by the source. Silence is not support. Always check against a source independent of the resource, because copied errors spread, and report the sample size, as in "9 of 10 matched."

Then look at the citations. A complete reference has the author, year, title, publisher or journal, a link or identifier, and for a web page the date accessed. Trace important claims back to a primary source, and judge each source on four questions: is it relevant, reliable, retrievable, and current? Open each source and read the supporting line, because an AI agent can produce a reference that looks right and is not.

Ask a subject expert when the topic is outside your knowledge, bears on health, safety, or law, or your sample finds two or more mismatches in ten facts.

**Example:** In *Watershed Basics*, 9 of 10 sampled facts matched. The text says the Clearwater River is 410 miles long, and the State Water Agency now gives 398.

See [Chapter 5](chapters/05-accuracy-currency/index.md).

### How do I tell whether a resource is out of date?

Outdated content was correct when it was written and no longer is, which is why it differs from a factual error. Look for six signs: dates many years old, or "recent" and "new" with no date; replaced or discontinued products, versions, or standards; old statistics for a quantity that changes; screenshots of a redesigned interface; dead links; and no sign of an update in years for a fast-moving topic.

Content ages at different speeds. Basic mathematics and definitions age very slowly. Software screenshots, prices, web addresses, laws, and contact details age quickly and need a check every year or more often.

Find the publication date and the update date in the header or footer, the file properties, or the repository's commit history. A missing date is a currency concern, and an update date alone does not prove real review. Then run a link checker, record the test date, and read the status codes. A 301 means update the address, a 404 means find a replacement, a 403 means open it by hand, and a 200 still needs a look, because it can lead to the wrong page.

**Example:** On 2026-10-12, 2 of 14 links in the sample resource returned page not found. After repair, all 14 worked on 2026-10-24.

See [Chapter 5](chapters/05-accuracy-currency/index.md) and [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### How do I check that a resource aligns with my learning outcomes?

Start by writing the outcomes as capabilities and not topics, using measurable verbs such as list, describe, calculate, compare, and design. Avoid "know" and "understand," which you cannot test. Then build a three-column curriculum map with a row for each outcome, a column for the activities that teach it, and a column for the assessment items that check it.

Compute outcome coverage: the outcomes that are both taught and assessed, divided by all outcomes. Check that the Bloom level of each activity and item matches the outcome's level. An "explain" outcome with only vocabulary-choice items has the right topic at the wrong level. For standards alignment, read the standard, find its verb, and look for an activity that asks for it. A standard code on its own is a claim and not evidence. An outcome that is not taught, not assessed, or not assessed at its level is a content gap.

**Example:** In *Watershed Basics*, outcomes 1 and 2 are taught and quizzed, but outcome 3, predicting how paving changes runoff, has no section and no quiz item. Coverage is 2 of 3, or 67 percent, and the alignment score is 6.

See [Chapter 6](chapters/06-alignment-readability/index.md).

### What do adopt, revise, and reject mean?

They are the three decisions a review can support. Adopt means use the resource now. Revise means improve it first. Reject means set it aside. The scores point toward one of the three, and the review report that ends a review states the choice with reasons and names the strongest and weakest metrics.

The review informs the decision and does not make it. People with authority, such as a department or a district committee, make the adoption decision, and they weigh things the rubric does not measure.

**Example:** For the book's running sample, *Watershed Basics*, the original version scored 65 and the recommendation was revise. After improvements it scored 78, and the recommendation became adopt.

The next sections give the exact thresholds. [Chapter 11](chapters/11-manual-evaluation-adoption/index.md) shows how a recommendation is written.

### How do I decide whether to adopt, adapt, or create?

The three pathways run from least to most effort. Adopt relies on the retain and reuse permissions. Adapt relies on revise, and often remix. Create means you hold the rights and choose the license. The book offers a heuristic, not an official standard, that depends on three facts: how well the resource fits, whether revision is permitted, and how much time you have.

- Full fit: adopt.
- Partial fit and revision permitted: adapt.
- Partial fit and revision not permitted: keep searching.
- No fit and much time: create.
- No fit and little time: keep searching.

The chapter's illustrative line between little and much time is 40 hours.

**Example:** A teacher finds an open unit under CC BY that covers two of three outcomes. Revision is permitted and the fit is partial, so the rule says adapt.

See [Chapter 1](chapters/01-foundations-of-oer/index.md).

### What is the difference between an AI assistant and an AI agent?

An AI assistant answers questions and completes tasks in a conversation. It is fluent, it knows only what it learned in training plus what you give it, and it will answer even when it cannot do the task. An AI agent is built on a language model but adds tools, access to files, and a loop: it observes, decides, acts, and observes again.

Agents work at three levels of independence: suggest only, act with approval, or act alone. For evaluation, the book uses the first two, and an agent should never change the resource it is reviewing.

**Example:** Asking an assistant to explain the difference between CC BY and CC BY-SA is an assistant task. Having an agent read a folder of lesson files, run a link checker, and fill in the rubric worksheet is an agent task.

[Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md) introduces both.

### How does an AI agent score a resource against the rubric?

An agent reads the resource, which the book calls document ingestion. It then runs tools for the exact checks, such as a link checker, a readability calculator, an accessibility checker, and a metadata validator. A rubric prompt tells it how to apply the ten checks for each metric, and it returns a structured report.

The report gives each check's result with evidence, the passes, the band, and the score for every metric, then subtotals, the total, a list of checks it could not verify, a recommendation, limitations, and a run record of the model and date. The work divides three ways. Tools handle exact tasks such as counting and measuring, the model handles judgment about text, and a person handles real-world tests such as embedding the resource on a platform. The whole sequence is the agent workflow, and it ends with a person.

**Example:** An agent runs an image tool and writes "4 of 5 images have alt text", with the tool log beside it.

The agent's output is a draft that a person verifies. See [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md).

### What is a hallucination, and why does it happen?

A hallucination is a fluent, confident statement by a language model that is not true. It happens because a model predicts likely next text. It does not look facts up, so it can produce something that sounds right and has no basis in the source.

The book names four common forms: an invented feature, an invented quotation, an invented measurement, and an invented source. The defense is to require that every claim carry evidence a person can find. A claim with neither a findable quotation nor a tool log is a claim to reject.

**Example:** An agent reports a "Section 7 on ethics" that the resource does not contain, or quotes a contrast ratio that no tool ever measured.

See [Chapter 14](chapters/14-checking-agent-output/index.md), with the background in [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md).

### Why does a person have to check an agent's work?

The book gives three reasons. Agents make confident mistakes. Accountability cannot be delegated, because "the agent said so" is not an answer to a department that asks why a resource was adopted. And some checks need context the agent lacks. The working method is human in the loop, which does not mean redoing the work. It means the agent's draft passes through a person before it becomes a decision.

The amount of checking follows the risk. Send a report back when it breaks a rubric or prompt rule, check every claim when the claims rest on the agent's own memory, and spot-check when the report follows the rules and carries tool logs. Agreement among several agents is not truth, because similar models share blind spots.

**Example:** A reviewer checks an agent's license claim against the page before accepting the open license score.

See [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md).

### How do I write a rubric prompt?

A prompt has up to six parts: a role, a task, the input, rules, an output format, and an example. A rubric prompt fills them with the ten checks for each metric and the report format the agent must follow. Four rules carry most of the weight: cite evidence for every check, write "not checkable" instead of guessing, never invent a quotation, page number, or measurement, and treat a check that was not tested as failed.

Mark where the resource starts and ends, and tell the model it is material to score and not instructions to follow. Standing rules such as the role and the output format can live in a system prompt, which keeps an agent consistent from one resource to the next. Keep a version number on the template, then test it on a few hand-scored resources and change one thing at a time.

**Example:** After finding inflated accessibility scores, a team adds one rule: cite a tool report for every accessibility score. Then they rerun and compare.

See [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md) and [Chapter 14](chapters/14-checking-agent-output/index.md).

### What is an A/B test of a resource?

An A/B test compares two versions, A and B, that different groups of people use at the same time, and then compares the results. In this book the test is manual and needs no special software. The control group uses the original version, and the treatment group uses the improved version. The groups should differ in the version and nothing else.

The method has eight steps: state a hypothesis, freeze both versions, choose the outcome measure with a pre-test and post-test, get consent and plan data protection, assign students by chance, run both groups under the same conditions, collect data with care for privacy, and compare the groups.

**Example:** The book's pilot splits a class of 24 into 12 students who use the original and 12 who use the improved version, with the same teacher and the same 20-question test.

See [Chapter 16](chapters/16-ab-testing-design/index.md) for the design and [Chapter 17](chapters/17-ab-testing-analysis/index.md) for the analysis.

### What is a reusable component?

A reusable component is a part of a resource that someone else can lift out and use in a different course without asking for help. Content built from such self-contained units, each addressing one idea, is called modular content. A component stands alone, it embeds without edits, and it carries its own license and metadata. A package for a component holds the content, a README, a license file, a metadata file, and any images or scripts, in one folder, with links that work inside it.

**Example:** The improved *Watershed Basics* version 1.1 has three components: a reading, an eight-question quiz, and a simulation. A teacher can take only the quiz.

[Chapter 18](chapters/18-components-publishing-oer/index.md) shows how to package, license, and publish components, and [Chapter 9](chapters/09-modularity-metadata/index.md) gives the tests for modularity.

### How do the five reusability metrics work together?

They form a chain, and each link depends on the one before. The open license says what others may do. Editable source makes the revise permission practical, because a license that allows changes does nothing if the only copy is locked. Modularity lets someone lift out the part they need. Metadata lets a stranger find and judge it. Portability lets it run in the places where they teach.

The chain also explains why license comes first. Without clear terms, nothing else in the reusability half matters. And a weak link anywhere limits the whole.

**Example:** A CC BY textbook that exists only as a PDF can be revised legally, and not practically. Its license metric is high and its editable source metric is low, and a reuser needs both.

See [Chapter 9](chapters/09-modularity-metadata/index.md), [Chapter 4](chapters/04-open-formats-version-control/index.md), and [Chapter 10](chapters/10-portability-reuse/index.md).

### Why does the adoption rule need a floor of 5 on every metric?

Because a total can hide a failed metric. If the rule asked only for a total of 75, a resource could score 1 on open license and strongly on the other nine metrics, still reach 80, and be adopted even though others could not legally reuse it. The floor says that every metric must be at least 5 before a resource can be adopted, whatever the total.

The floor applies to every metric, not just the license. A resource with a total of 80 and an accessibility score of 3 is revised, not adopted, because barriers keep learners out. The book also advises reading the lowest metric before the total.

**Example:** A resource that scores 85 overall but only 4 on portability is revised, not adopted.

The rule is the book's starting point, not a standard, so a department may set its own. See [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md) and [Chapter 11](chapters/11-manual-evaluation-adoption/index.md).

### How do I score a resource by hand, step by step?

The book's review workflow has nine steps:

1. Save a dated copy of the resource and fill in the resource block of the worksheet.
2. Read the review checklist and gather your tools.
3. Read the whole resource once without scoring.
4. Score one metric at a time, writing the evidence as you go.
5. Add the subtotals and the total.
6. Hand the worksheet to a second reviewer who scored alone.
7. Compare, and reconcile every metric on which you differ by more than 3 points.
8. Apply the adoption threshold.
9. Write the report and the recommendation.

Scoring one metric at a time guards against the halo effect, and scoring alone before comparing guards against anchoring. Manual evaluation is slower than software, and it is the reference the book measures agents against.

See [Chapter 11](chapters/11-manual-evaluation-adoption/index.md) and the [sample rubric worksheet](workshops/sample-rubric-worksheet.md).

### How do I check an open license before I reuse a resource?

Look in three places for a license: the page footer or an about page, the first or last page of the file, and the file's properties. If all three are silent, treat the work as all rights reserved. Then read what the statement actually names: the license and its version, a link to the license text, the owner, and what the license covers. If a statement and the source disagree, the source wins.

Next, look at third-party content. A resource's overall license may not cover an image or chart that someone else made, and a caption that says "used with permission" is a separate right. Finally, build the credit line: title, author, source, and license, plus a note of any changes.

**Example:** "Free to use" is not a license. "This work is licensed under CC BY 4.0," with a link, in every page footer, is clear.

See [Chapter 2](chapters/02-open-licenses-attribution/index.md) and [Chapter 9](chapters/09-modularity-metadata/index.md).

### Why test with students if I already have rubric scores?

The rubric asks whether a resource has the properties that make it good. An A/B test asks whether students learn more from this version than from that one. They are different questions, and one does not answer the other. A resource can gain 13 rubric points from better metadata and teach no better.

This is the difference between reliability and validity. A reliable rubric gives similar scores whoever applies it. A valid rubric measures what it claims to measure, which here means higher scores go with better results for learners. Consistent scores can still measure the wrong thing, so the book ends with a test of whether rubric scores relate to learning.

**Example:** Adding metadata may raise the rubric total a lot and change nothing a student notices. A student test is the only way to find out.

See [Chapter 16](chapters/16-ab-testing-design/index.md), [Chapter 17](chapters/17-ab-testing-analysis/index.md), and [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md).

## Technical Detail Questions

### How is the total score calculated, and what are the score bands?

Add the ten metric scores. The five quality scores sum to the quality subtotal (0 to 50), the five reusability scores sum to the reusability subtotal (0 to 50), and the two subtotals sum to the total (0 to 100). Report the total together with both subtotals and the lowest metric, because a total can hide a weak metric.

The total falls in one of five named bands, with both ends included:

- Excellent: 90 to 100
- Good: 75 to 89
- Fair: 50 to 74
- Weak: 25 to 49
- Poor: 0 to 24

A band is a quick label for teachers and administrators. It is not the adoption decision, and a total in the Good band can still get a revise decision if one metric is below the floor.

**Example:** A quality subtotal of 38 and a reusability subtotal of 31 give a total of 69, which falls in the Fair band.

See [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md).

### What score does a resource need to be adopted?

The book's starting rule has three outcomes. **Adopt** when the total is at least 75 and every metric is at least 5. **Revise** when the total is at least 50 and the adopt rule is not met. **Reject** when the total is under 50.

The edges show how it works. A total of 75 with every metric at 5 or more is adopt. A total of 74 is revise. A total of 88 with one metric at 4 is revise. A total of 50 is revise, and a total of 49 is reject. These values are the book's starting rule and not a standard, so a department may set a stricter one.

**Example:** The original *Watershed Basics* scored 65. That is below 75, and its metadata score of 4 is below the floor of 5, so the decision is revise.

See [Chapter 11](chapters/11-manual-evaluation-adoption/index.md) and [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md).

### What contrast ratios does WCAG 2.1 AA require?

A contrast ratio compares the relative brightness of two colors on a scale from 1:1 to 21:1, where black on white is 21:1. WCAG 2.1 AA sets these minimums:

- Normal text: 4.5 to 1.
- Large text: 3 to 1. Large means at least 18 points, or at least 14 points if bold.
- Meaningful parts of controls and graphics: 3 to 1.

Tests use the unrounded ratio, so a ratio of 4.499 fails. Logos and purely decorative elements are not covered. Level AAA asks for 7 to 1, which is not required at AA. Free tools compute the ratio instantly, and the book advises measuring and not judging by eye.

**Example:** Gray #767676 on white measures 4.54 to 1 and passes. Gray #777777 on white measures 4.48 to 1 and fails, though no one can see the difference.

See [Chapter 7](chapters/07-accessibility/index.md).

### How do I write good alt text and handle decorative images?

Alt text answers the question "What does this image do here?" and not "What does it look like?" It lives in the image's alt attribute, and a screen reader speaks it aloud. Four habits make it good: say what matters in the context in a sentence or two, do not begin with "image of" or "picture of," do not repeat an adjacent caption, and never use a file name or a single word.

A decorative image adds visual interest but carries nothing a learner needs. Give it an empty alt attribute, written `alt=""`, so screen readers skip it. That is different from no alt attribute at all, because many screen readers then read out the file name. When you are unsure, write a short description. A chart or diagram needs a short alt text plus a longer description or a nearby data table.

An agent can draft alt text if you give it the surrounding paragraph and the lesson goal. Expect generic descriptions, details that are not in the image, wrong counts, and missing decorative roles, and accept, correct, or reject each draft.

**Example:** For a rain barrel photo, "photo" is poor. "A rain barrel at the end of a roof downspout holds runoff from the school roof" is good.

See [Chapter 7](chapters/07-accessibility/index.md) and [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### What do captions, transcripts, and audio description each do?

They serve different viewers, and none replaces the others. **Captions** are text synchronized with the audio of a video that shows spoken words and important sounds, for viewers who cannot hear or who watch without sound. A **transcript** is a complete, separate text version of the speech and key sounds. It helps deaf and hard-of-hearing users, screen reader users, and anyone who prefers reading, and it makes media searchable, but it does not replace captions for video. **Audio description** is spoken narration of important visual content that the soundtrack does not give, for viewers who cannot see it.

[Chapter 7](chapters/07-accessibility/index.md) says that at level AA, prerecorded video with sound needs captions and audio description. Automatic captions need checking, because they often mishear technical terms. Watch the whole video while you read the captions.

**Example:** A lecture video shows each sentence as it is spoken, plus "[applause]" for the sound of applause. When a speaker only points at a graph, a narrator says, "The graph line climbs steeply after year three."

### What makes a good multiple-choice question and answer key?

A multiple-choice question has a stem, a key (the correct answer), and distractors (the plausible wrong answers). The book lists seven flaws to look for: an ambiguous stem, an implausible distractor, a correct answer that is noticeably longer, an option such as "all of the above," a negative stem such as "which is NOT," a grammatical clue such as "a" versus "an," and a pattern in where the keys fall. Some research suggests that three well-written options can work as well as four or five, so judge the quality of options and not their number.

Spread the difficulty. The difficulty index is the share of learners who answer correctly, and a quiz should cover a range. A question bank tags each item by topic, outcome, and difficulty. An answer key gives final answers, and a worked solution shows every step. AI-drafted questions often have weak distractors, so review them.

**Example:** "Public Domain" is a plausible wrong answer to "Which license requires ShareAlike?" while "purple" is not.

See [Chapter 8](chapters/08-practice-feedback/index.md).

### What are the six core metadata fields, and what is Dublin Core?

The six core fields the book checks are title, author, subject, grade level, license, and description. They tell a stranger what a resource is, who made it, who it is for, and what they may do with it. Dublin Core is a metadata standard of fifteen general-purpose elements in four groups: content, responsibility, the copy, and relations. The book maps its fields onto it: author becomes Creator, license becomes Rights, and grade level becomes an education level term, since Dublin Core has no core element for it.

LRMI, now part of Schema.org, adds education-specific properties such as the learning resource type and typical age range. Completeness is the share of expected fields that hold valid values. A value such as "TBD" counts as invalid.

**Example:** A record with only title and author filled has two of six core fields, a completeness of 33 percent.

See [Chapter 9](chapters/09-modularity-metadata/index.md).

### What is the Flesch-Kincaid Grade Level, and how is it computed?

It is a readability formula that estimates the United States school grade needed to understand a text. It is the book's standard readability number. The formula is:

grade = 0.39 × (words ÷ sentences) + 11.8 × (syllables ÷ words) − 15.59

Use passages of at least 100 words, sample at least three from different sections, and compare the result with the audience's grade. A good fit is usually within about one grade of the audience's level. The formula counts surface features only. It cannot see idea difficulty, word familiarity, or organization, so treat the number as one piece of evidence.

**Example:** A passage with 6 sentences, 120 words, and 168 syllables has 20 words per sentence and 1.4 syllables per word. That gives 7.8 + 16.52 − 15.59 = 8.73, or grade 8.7.

Do not strip needed technical terms to lower the grade. Define them at first use. See [Chapter 6](chapters/06-alignment-readability/index.md).

### How do I judge readability beyond the grade level number?

Sample at least three passages from different sections, and then check what a formula cannot see. Sort the vocabulary into tiers. Everyday words need nothing. General academic words such as "analyze," "however," and "evidence" should be taught and used consistently. Subject terms such as "runoff" should be defined where they first appear, which means in the same sentence or the next, and listed in a glossary.

Check the habits of plain language: short sentences with one idea each, the active voice, common words where they are as accurate, and examples. Apply the jargon test. If a common word says the same thing, ask for it, and if the specialized word is necessary, ask for a definition. Headings should describe their sections, and paragraphs should be short and focused. Finally, ask someone from the audience to read a section aloud. Audience fit is the measure a formula cannot give.

**Example:** For a grade 6 to 7 audience, the sample resource's passages measured 6.4, 6.9, and 7.3, which fits. But a technical term is used before it is defined and there is no glossary, so readability scores 8.

See [Chapter 6](chapters/06-alignment-readability/index.md).

### What are the certificate requirements?

The Certificate of OER Quality Evaluation Using AI Agents has five requirements. A teacher:

1. Attends the full training day.
2. Completes the calibration exercise and explains every metric on which their score and the agent's differ by more than 3 points.
3. Submits an evaluation of one OER from their own subject, scored on all 10 metrics, with evidence for each score and a note on every agent finding they accepted, corrected, or rejected.
4. Publishes one improved component under a CC BY license, with metadata, that gains on at least two quality and two reusability metrics.
5. Submits both within 30 days of the workshop.

A reviewer who did not take part in the work checks each submission. The certificate is not a legal license, a government accreditation, or a promise that your later evaluations will be correct. [Chapter 19](chapters/19-training-certifying-reviewers/index.md) states the requirements separately from the capstone project's tests, so ask your program which one it asks you to complete. The same five requirements appear on the [sample rubric worksheet](workshops/sample-rubric-worksheet.md).

### What is the difference between a source format and a delivery format?

A source format is the format in which a resource is written and can be edited. A delivery format is for reading, printing, or showing. The book's analogy is that the recipe is the source and the cake is the delivery file. A reviewer scores the editable source metric on the source files and does not count the delivery file.

- **Good sources:** Markdown, plain text, HTML, OpenDocument text, CSV for data, and SVG for diagrams.
- **Usually acceptable:** Word (.docx), which is a published standard whose full fidelity depends on particular software.
- **Poor sources:** PDF, scanned pages, flattened images, and files from a page layout program you do not own.

An open file format is one whose specification is public and usable without a fee. A PDF alongside editable sources is fine. A PDF in place of them is a locked file, and it usually leaves the metric in the low bands.

See [Chapter 4](chapters/04-open-formats-version-control/index.md).

### What is the difference between formative and summative assessment?

Formative assessment happens during learning. It is low stakes and repeatable, and learners and teachers use it to adjust what comes next, which is why it is called assessment for learning. Summative assessment comes at the end and judges what was learned. The practice metric favors formative assessment, because practice with feedback is how learners improve before anyone grades them.

Self-check questions, quizzes with feedback, and retrieval practice are formative. A strong feedback message confirms or corrects, says why, names the likely misunderstanding, points to what to review, and does not blame. Immediate feedback, delivered right after the answer, lets a learner fix a mistake while it is fresh.

**Example:** A three-question check after each section that shows the correct answers at once is formative. A final exam is summative.

See [Chapter 8](chapters/08-practice-feedback/index.md).

### What is the difference between Git, GitHub, and a fork?

Git is a free, open-source version control tool that keeps a full record of every change to a set of files, on your own computer. Linus Torvalds created it in 2005. GitHub is a website that hosts Git repositories, which are project folders with their full history, so others can view, copy, and suggest changes. A fork is your own copy of someone else's repository on the same site. It is independent of the original and keeps a link back to it.

The four Git terms the book teaches are repository, commit (a saved snapshot with author, date, and message), branch (a separate line of work), and merge. A pull request is a proposal to merge your changes into the original, which the maintainer can accept or decline.

**Example:** A teacher forks a chemistry repository, translates the lessons, and sends a pull request that fixes 14 broken links.

See [Chapter 4](chapters/04-open-formats-version-control/index.md).

### What is a MicroSim, and where does it fit in a lesson?

A MicroSim is a small, interactive, browser-based simulation that teaches one idea. It lives in its own folder, is usually built with p5.js, embeds in a page with an iframe, and is published under an open license. A simulation suits a concept where you vary a quantity and see an effect, or a procedure you practice with immediate feedback. Plain text is better for fixed facts and definitions.

MicroSims can raise several metrics at once. They count as practice with feedback, they can score well on modularity because each stands alone, and they test portability, because an embed has to work on more than one platform. They also need the accessibility checks, such as keyboard use.

**Example:** The [License Switches MicroSim](sims/cc-license-switches/index.md) lets you turn the SA and NC switches on and off and see which freedom each one takes away.

See [Chapter 8](chapters/08-practice-feedback/index.md) for how simulations count as practice.

### What do tokens and the context window have to do with scoring a long resource?

A token is a small unit of text that a language model reads and writes, and it is also the unit of cost. One token is about three quarters of a word, so 100 words is about 133 tokens. The context window is the most text a model can consider at one time, and it has to hold the instructions, the resource, the conversation, and the model's own answer.

To estimate the fit, add the words in the instructions, the resource, and the expected answer, divide by 0.75, and compare with the window. If it will not fit, use a larger window, shorten the instructions, or split the resource. Splitting has a cost, because checks that span the whole resource can be missed.

**Example:** 2,400 words of resource plus 600 of instructions plus 800 of answer is 3,800 words, or about 5,067 tokens. That fits in an 8,000-token window.

See [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md).

### What is structured output, and why do agents use JSON?

Structured output is a model response organized in a predefined, regular format, so software can read it without guessing. JSON is the common choice: named fields and values in plain text, with double quotes around names, numbers unquoted, and braces and brackets for structure. The book's score schema has these fields: the metric, a list of checks (each with a number, a result of pass, fail, or not checkable, and evidence), the count of passes, the band, the score, and the checks that were not verified.

Structure makes reports comparable across resources and easy to total. A script can recount the passes and recompute the band from the agent's own checks. Validation only catches form and never truth, so a well-formed report can still contain invented evidence.

**Example:** `{"accessibility": 4, "evidence": "Most images lack alt text"}` is a small piece of structured output.

See [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md).

### What do agreement rate, mean absolute difference, and bias tell me?

They are three ways to compare an agent's scores with careful human scores. **Agreement rate** is the share of metrics where the agent is within a chosen threshold of the human. Report the threshold with it. **Mean absolute difference** is the average size of the gaps, ignoring sign, and a value near 0 means the agent sits close to the humans. **Bias** is the average signed difference, agent minus human. A positive bias means the agent is generous, and it is the number that detects score inflation.

Correlation checks the pattern and not the level, so an agent that is exactly one point too high everywhere still correlates perfectly.

**Example:** In the book's example, the first-draft agent agrees on 10 of 10 metrics at a threshold of 1, with a correlation of 1.00. Its mean absolute difference is 1.0 and its bias is +1.0, and its total of 75 turns a revise decision into adopt.

See [Chapter 14](chapters/14-checking-agent-output/index.md).

### What does Cohen's kappa add that agreement rate does not?

Cohen's kappa measures how well two raters agree on categories after correcting for the agreement expected by chance alone. The formula is kappa = (po − pe) ÷ (1 − pe), where po is the observed agreement and pe is the chance agreement. A value of 1 is perfect agreement, 0 is chance level, and a negative value is worse than chance. The usual labels run from Slight (0 to 0.20) through Moderate (0.41 to 0.60) and Substantial (0.61 to 0.80) up to Almost perfect (0.81 to 1.00). The book marks them as a rule of thumb to verify before citing.

It matters when one category is common. Two raters who both say "adopt" most of the time agree often by luck, and plain agreement hides that.

**Example:** On 20 resources, an agent and a human agree on 18, which is 90 percent. But the agent found only 1 of the 2 resources the human judged ready, and kappa is 0.44, only Moderate.

Always show the table of counts beside kappa. See [Chapter 14](chapters/14-checking-agent-output/index.md).

### How do I write a complete attribution statement?

Use the TASL pattern: Title, Author, Source, License. Add a change note if you adapted the work. Under Creative Commons 4.0, a complete credit also includes any copyright notice, the license name and a link to it, and a link to the work where practical, and it must not suggest that the creator endorses you. You need no approval from the author.

**Example:** "Watershed Basics" by Maria Lopez, example.org/watershed-basics, licensed under CC BY 4.0. Adapted: reading level lowered and two examples localized.

List every third-party item the same way, with its own title, author, source, and license. Agents can draft credit lines, and a person checks each against the source.

See [Chapter 2](chapters/02-open-licenses-attribution/index.md) and [Chapter 18](chapters/18-components-publishing-oer/index.md).

### How do I estimate the cost of running an agent on a batch of resources?

Cost depends on tokens. The cost of one run is the input tokens times the input price, plus the output tokens times the output price, divided by 1,000,000, because prices are quoted per million tokens. Output tokens cost more than input tokens. The total is the cost of one run times the number of resources times the number of runs.

Using illustrative prices of $2.00 per million input tokens and $8.00 per million output tokens, a run with 6,000 input tokens and 1,000 output tokens costs $0.012 plus $0.008, or $0.02. Five hundred resources at one run each cost $10.00, and three agents triple it to $30.00. Retries after an invalid answer add runs.

**Example:** Pilot on three resources before three hundred, give exact checks to free tools, and send only the parts a check needs.

Prices in a book go stale, so look up current rates. See [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md).

### How do I calculate learning gain and effect size from my A/B test data?

Work in four steps. First, compute each student's gain. The raw gain is the post-test minus the pre-test. The normalized gain is (post − pre) ÷ (100 − pre), which accounts for room to improve. Second, find the mean gain for each group. Third, subtract: the difference of means is the treatment mean minus the control mean. Fourth, divide that difference by the pooled standard deviation to get Cohen's d.

Compare gains and not post-test means alone, because the groups may have started at different levels.

**Example:** In the pilot, the control mean gain is 15.0 and the treatment mean gain is 22.0, a difference of 7.0. The pooled standard deviation is about 6.78, so d is about 1.03. The conventions call 0.2 small, 0.5 medium, and 0.8 large, and they are rules of thumb. Impressive pilot estimates tend to shrink when repeated.

See [Chapter 16](chapters/16-ab-testing-design/index.md) and [Chapter 17](chapters/17-ab-testing-analysis/index.md).

### How do I make A/B test data anonymous?

Coded data replaces names with codes but keeps a key, so it is not anonymous. Anonymized data has every link to a person removed, so no one, including the teacher, can tell whose scores they are. Start by collecting little: the version label, the pre-test, the post-test, and the grade level, with a code such as S01 and the key in a separate locked file.

To anonymize, drop columns you do not need, generalize details such as grade level instead of birthdate, hide results for groups smaller than your district's reporting size, and clean the comments of identifying detail. Destroy the key on the deletion date you stated in the consent letter, and make sure nothing else in the table points to a person.

**Example:** A class of 24 with gender, class period, and teacher name in the table can single out one student, even without names.

The test: could someone who knows the class pick out a single student? See [Chapter 16](chapters/16-ab-testing-design/index.md) and [Chapter 17](chapters/17-ab-testing-analysis/index.md).

### How do I get a resource to work in my learning management system?

A teacher can bring an OER into a learning management system (LMS) four ways: a link, an embed, an upload of the files, or an import of a package. A reviewer tests at least link and embed. An iframe embed uses a source address, a width, a height, and a title. It fails for three common reasons: the server forbids framing, an insecure page sits inside a secure one, or the platform strips frames.

Two standards from 1EdTech help. Common Cartridge packages a course into one compressed file with a manifest that other systems can import. Learning Tools Interoperability (LTI) lets an outside tool open inside a course and can send scores to the gradebook, which raises privacy questions. Both are pluses and not requirements.

**Example:** Open the page in a private window with no login, paste the iframe into a blank test page, and then repeat on a second platform such as Moodle or Canvas.

See [Chapter 10](chapters/10-portability-reuse/index.md) and [Chapter 9](chapters/09-modularity-metadata/index.md).

### How do the 3-point flag and the 1-point calibration threshold relate?

They serve different purposes. The 3-point flag from Chapters 3 and 11 is for finding disagreements worth discussing. Two reviewers agree on a metric if their scores differ by 3 or fewer, and a metric is flagged if they differ by more than 3. The workshop's calibration exercise uses the same flag between a teacher and an agent.

Chapter 14 uses a threshold of 1 for deciding whether an agent can be trusted as a first pass, and labels it a provisional teaching choice. Bands are two points wide, so a difference of 2 or more always moves a score into a different band. A loose threshold also fails to separate agents.

**Example:** In the book's three-agent comparison, all three agents agree on 10 of 10 metrics at a threshold of 3. At a threshold of 1, one of them agrees on only 4 of 10.

Set the threshold before you look at the numbers, so it cannot be bent to fit the results. See [Chapter 14](chapters/14-checking-agent-output/index.md).

### How does sample size relate to the size of effect I can detect?

Larger groups smooth out chance differences, and a smaller effect is harder to tell from chance, so it needs many more students. The book gives rule-of-thumb group sizes: 5 to 10 per group for a pilot only, about 25 per group for a large difference, about 65 for a medium one, and about 400 for a small one.

The planning rule is students per group ≈ 16 ÷ d², rounded up. An effect size d of 0.8 needs 25 per group, 0.5 needs 64, and 0.2 needs 400. Do not plan on the pilot's own d, since pilot estimates tend to shrink. Plan on about half of it, close to 0.5, which means about 64 per group.

**Example:** A pilot with d about 1.03 would suggest 16 students per group. Planning on roughly half that effect size gives about 64 per group instead.

These are rules of thumb, and a statistician should confirm them. A pilot of about 12 per group is not enough to prove an effect. Its job is to decide whether a larger test is worth running. See [Chapter 16](chapters/16-ab-testing-design/index.md) and [Chapter 17](chapters/17-ab-testing-analysis/index.md).

## Common Challenge Questions

### The agent cited a source I can't find. What should I do?

Treat it as a possible invented citation: a reference to a source that does not exist, or one that exists and does not say what the agent claims. Run four checks:

1. Search for the exact title.
2. Confirm that the journal exists and has the issue cited.
3. Resolve the identifier or link. A DOI that leads nowhere, or to a different article, is a strong sign of a problem, and a missing identifier is a weaker one.
4. Open the source and read the passage that is supposed to support the claim.

If you cannot find the source, reject the claim, record the decision and the reason in the findings log, and rescore without it. Never accept a claim you could not verify in time. Mark it "not verified." To prevent a repeat, add a rule to the prompt: cite only sources that appear in the resource or that you supplied, and write "no source found" otherwise.

**Example:** An agent cites a journal article with a believable title that no library holds. The reviewer rejects the claim, and the accuracy score is recomputed without it.

See [Chapter 14](chapters/14-checking-agent-output/index.md) and [Chapter 5](chapters/05-accuracy-currency/index.md).

### Why do agents misread licenses, and how do I catch it?

A license is a short, formal statement, and the neighboring licenses look alike. The book lists five predictable errors: treating one license as covering every item, confusing neighboring licenses such as reading CC BY-NC as CC BY, ignoring a restriction such as NoDerivatives, equating public with free, and missing ShareAlike. A related trap is reading the license of the site template instead of the content.

A misread license can lead to an unsafe adoption, so go to the source. Open the page and read the license statement itself. A good prompt asks the agent to quote the statement word for word, name each item it covers, and write "not stated" for anything the page does not mention. Then compare the quote with the page.

**Example:** An agent calls a resource CC BY because a link says "Creative Commons," although the terms say NonCommercial. Reading the statement catches it in seconds.

See [Chapter 14](chapters/14-checking-agent-output/index.md) and [Chapter 2](chapters/02-open-licenses-attribution/index.md).

### How can I tell whether an agent's score is overconfident?

An overconfident score is higher or more certain than its evidence supports. It is the quietest agent error because nothing is invented. Four signs give it away: a high score with no quoted evidence, a pass on a check that needs a tool but has no tool log, an empty "checks not verified" list, and round 9s and 10s across many metrics.

Use the quick test. Recompute the band from the agent's own ten checks by dividing the passes by ten, and compare it with the reported score. Then add rules to the prompt: a check that was not tested counts as failed, a check that cannot be verified is marked "not checkable" and listed, and a 10 requires every check to pass.

**Example:** An agent reports an 8, but its own table shows 6 of 10 checks passed. Sixty percent falls in the Adequate band of 5 to 6, so the 8 is overconfident by at least two points.

See [Chapter 14](chapters/14-checking-agent-output/index.md).

### My score and the agent's score differ by more than 3 points. What now?

The worksheet flags every metric where the two scores differ by more than 3, and the calibration exercise asks you to explain which score you trust and why. A disagreement is information. It points to unclear evidence, a possible agent error, or an ambiguous check in the rubric.

Use the reconciliation steps. Each side states its evidence, you repeat the check that the evidence rests on, and you choose the score the checked evidence supports. If neither side has enough evidence, gather more. Do not average the two scores, because an average is a number neither reviewer found.

**Example:** You scored accessibility 5 and the agent scored it 9. The agent said contrast was fine but attached no tool log, and the video has no captions. You keep your 5 and record why.

See [Chapter 11](chapters/11-manual-evaluation-adoption/index.md), [Chapter 14](chapters/14-checking-agent-output/index.md), and [Chapter 19](chapters/19-training-certifying-reviewers/index.md).

### The resource is CC BY-ND or has no license. Can I still improve it?

Read the license before the first edit, because an agent's edited version is a derivative work and the license decides what you may do with it. With CC BY-ND you may share only the unchanged work. You can make private changes, but you cannot publish an improved version. Adding alt text, lowering the reading level, and fixing errors are all changes. A resource with no license, or marked all rights reserved, cannot be published in a changed form either.

Your options are to ask the owner for written permission, or to choose another resource. Do not add a license yourself, since only the owner can grant one. If the license allows changes, the rules are simple: with CC BY credit the author and say you changed it, with CC BY-SA also release under CC BY-SA, and with a NonCommercial license avoid commercial use.

**Example:** A teacher can post a CC BY-ND article for a class as it is, but cannot share a translated version.

See [Chapter 15](chapters/15-improving-resources-with-ai/index.md) and [Chapter 2](chapters/02-open-licenses-attribution/index.md).

### The resource is only a PDF. What can I do?

A CC BY textbook that exists only as a PDF can be revised legally, and not practically. Start by asking the author for the Markdown, HTML, or word processing source. If none exists, you have two choices. You can convert the PDF to Markdown with a tool or an agent, or you can score the editable source metric low and note why. A PDF-only resource usually lands in the low bands of that metric.

Conversion needs careful review, because tables and equations convert poorly. The book lists six common errors: wrong column order, a flattened table, a lost heading, a garbled equation, a lost image, and a split word. Each has a quick check, such as reading a paragraph from each column and comparing every table and formula with the original.

**Example:** A tool converts a PDF chapter into Markdown, and a teacher repairs a broken table and a lost heading before publishing.

See [Chapter 4](chapters/04-open-formats-version-control/index.md) and [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### My accessibility checker reports no errors. Is the resource accessible?

Not necessarily. A clean scan is a starting point and never a pass. Checkers find missing alt attributes, weak contrast, unlabeled form fields, and some heading problems. They cannot judge whether alt text is useful, whether captions are accurate, or whether a heading describes its section.

Add the human checks. Read the alt text, listen to the page with a screen reader such as NVDA (free, for Windows) or VoiceOver (built into Apple devices), and put the mouse aside and press Tab through the page to see whether every function works by keyboard. Check captions on any video.

**Example:** In *Watershed Basics*, two of four alt texts are the single word "photo." A checker accepts them, and a reader using a screen reader learns nothing from them.

!!! mascot-warning "A Green Report Is Not a Pass"
    ![Echo warning](img/mascot/warning.png){ class="mascot-admonition-img" }
    Scanners approve alt text that says only "photo," because the attribute is present. Spend two minutes with the mouse set aside, pressing Tab through the page, and listen with a screen reader before you trust the score.

See [Chapter 7](chapters/07-accessibility/index.md) and [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md).

### The agent's rewrite changed the meaning of a passage. How do I catch that?

An agent can quietly alter what a passage says while it improves how it reads. The book lists five meaning-changing edits:

- A changed quantity, such as "about 6,000" becoming "more than 6,000."
- A changed strength, such as "can" becoming "always."
- A dropped qualifier, such as "most rain" becoming "rain."
- An added claim that the source never made.
- A dropped item, such as "the river and its tributaries" becoming "the river."

Do not rely on the agent's own summary, because it can leave a change out. Open a side-by-side difference view and ask the agent to list every claim it changed, added, or removed. Treat an added claim as rejected unless a source supports it, and log corrections separately from plain rewrites.

**Example:** Rewriting "may reduce" as "reduces" turns a possibility into a certainty and fails the check.

See [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### The agent gives a different score each time I run it. What should I do?

Language models do not always give the same answer twice, so measure the variation and do not guess at it. Run the same prompt on the same resource five times. Record the lowest score, the highest, the range (highest minus lowest), and the median. The book's illustrative rule is that a range of 1 or less is stable, and a range of 2 or more is unstable. An unstable metric goes to a person.

A median that matches the human score does not make an unstable metric trustworthy. If a metric is unstable, tighten the prompt by asking for a pass or fail on each of the ten checks, move exact checks to tools, and measure again.

**Example:** Five runs give accessibility scores of 5, 6, 5, 7, and 5, a range of 2 with a median of 5, so it is unstable. Practice scores of 4, 7, 6, 5, and 8 have a range of 4.

See [Chapter 14](chapters/14-checking-agent-output/index.md).

### My A/B test groups aren't comparable. What went wrong?

Most likely a confounding variable crept in, which is a second difference between the groups besides the version. Common ones are different teachers, different times of day, extra help for one group, different tests, and students choosing their own version. If the treatment group had a different teacher, you cannot tell whether the version or the teacher made the difference.

Defend against them with the one-difference rule: the groups differ in the version and nothing else. Assign students by chance. Simple random assignment can still be unlucky in a small class, so the book also teaches blocked assignment. Give the pre-test, sort by score, pair neighbors, and flip a coin within each pair. Also watch for sampling bias, such as only volunteers taking part.

**Example:** In a simulation on the book's class of 24, letting students choose built in a 23.8-point gap between groups. Simple random assignment had a median gap of about 4 points. Blocked assignment had a median of about 0.6.

See [Chapter 16](chapters/16-ab-testing-design/index.md).

### My class is small. Can I still learn anything from an A/B test?

Yes, if you call it a pilot and read the result as suggestive and not conclusive. A pilot of about 12 students per group is not enough to prove an effect. Its job is to check the procedure and the measures, to estimate the spread of the scores and the size of the effect, and to decide whether a larger test is worth running.

Pilots surface practical problems. In the book's pilot, the original version's quiz would not load for two students on school tablets, and three students scored 95 to 98, so the test had little room to show growth. Both findings improved the next round. Report the limits honestly: one class, a bundle of fixes tested together, and an effect size that often shrinks when repeated.

**Example:** The book's pilot found a 7-point difference in mean gain. The summary recommended a larger test and did not claim proof.

See [Chapter 16](chapters/16-ab-testing-design/index.md) and [Chapter 17](chapters/17-ab-testing-analysis/index.md).

### How do I handle third-party images with unclear licenses?

A resource's overall license may not cover an image, chart, or quotation that someone else made. A caption that says "used with permission" gives a separate right that does not travel with the rest. The phrase "except where otherwise noted" is a warning to check every image caption.

For each third-party item, find its own notice and record the title, author, source, and license. If you cannot find the terms, replace the item. An image whose terms forbid changes must be replaced and not edited. Also remember that someone who copied an image from a publisher cannot grant you a Creative Commons license for it, so trace it to the original creator. When two items carry licenses that cannot be satisfied together, you can pick a different resource, ask an owner in writing, or keep the works separate with their own notices.

**Example:** A photo in a CC BY chapter that is labeled "used with permission" has rights separate from the chapter's.

See [Chapter 2](chapters/02-open-licenses-attribution/index.md) and [Chapter 9](chapters/09-modularity-metadata/index.md).

## Best Practice Questions

### How do I decide which metric to improve first?

Start with the lowest-scoring metric, unless fixing it is too costly or needs the author's decision. There are three reasons. The adoption floor means any metric under 5 blocks adoption. The lowest scores are often the cheapest to raise. And the total hides the weakest area. If the lowest metric is expensive, do the cheaper fixes first and flag the expensive one.

Then write an improvement plan with five parts: the baseline, the gaps, the fixes, the order and budget in human hours, and the target. The plan is a forecast, written before the work and compared with the result afterward.

**Example:** For *Watershed Basics*, the plan starts with metadata (4 to 8, half an hour, +4), then accessibility (5 to 8, two hours, +3), then modularity, practice, and accuracy. It totals 7.5 hours, a projected gain of 14, and a target of 79. Accessibility goes before the cheaper modularity fix because a barrier to learners matters more.

See [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### How do I review a change an agent made before I publish it?

A named person examines each change in a difference view and decides whether to keep it. Nothing goes live on the agent's say-so, and the agent's own summary is not enough, because an agent can leave a change out. Match the depth of the check to the risk. High-risk changes, such as facts, numbers, quotations, citations, captions, license statements, and anything that touches meaning, get a full check. Low-risk changes, such as heading levels and formatting, get a spot check.

Record each decision in a change log entry with seven fields: when, where, what changed, why, who or what made it, who reviewed it, and the decision. Reusers need the log, since CC BY asks you to indicate changes. Future reviewers and your own re-score need it too.

**Example:** "May 3, section 2: shortened sentences; made by agent; reviewed by T. Nguyen; accepted."

See [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### How much of an agent's output should I verify?

Match the checking to the risk, because the two extremes both fail. With no oversight, a blind learner meets an uncaptioned video. Checking everything is accurate but saves no time. Risk-matched oversight catches errors where they occur and keeps most of the time saving.

Send the report back when it breaks a rule, such as a total that does not equal the sum of the scores. Check every claim when the claims rest on the agent's memory with no source. Spot-check when the report follows the rules and carries tool logs. A good sample includes at least one claim from each metric, every claim that decides a band or the floor of 5, and a few at random. Widen the sample if you find an error, and record which claims you checked.

!!! mascot-tip "Check the Decisive Claims First"
    ![Echo giving a tip](img/mascot/tip.png){ class="mascot-admonition-img" }
    Before anything else, find the claims that decide a band or the floor of 5. A mistake there flips the decision, while a mistake in a claim that moves no threshold costs you very little.

**Example:** A reviewer verifies 12 of 40 claims and records which ones were checked.

See [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md) and [Chapter 14](chapters/14-checking-agent-output/index.md).

### Which license should I choose for what I publish?

Ask three questions: do you allow commercial reuse, do you allow shared changes, and must changes carry the same license? The answers map to the license:

- Yes, yes, no: CC BY.
- Yes, yes, yes: CC BY-SA.
- No, yes, no: CC BY-NC.
- No, yes, yes: CC BY-NC-SA.
- Choose CC0 if you want no conditions at all.

The book favors CC BY for the components teachers publish, because it grants all five permissions with a single condition. The trade-offs are real. ShareAlike keeps adaptations open but limits what a remix can be combined with. NonCommercial blurs at the edges, such as a paid class, and it lowers the open license score. A published CC BY cannot be taken back for copies already out. Also check ownership, funders' requirements, third-party content, and, for software, use a license designed for code.

**Example:** An author who wants adaptations to stay open picks CC BY-SA, while one who wants the widest reuse picks CC BY.

See [Chapter 2](chapters/02-open-licenses-attribution/index.md). The capstone expects CC BY.

### How should I run a calibration session?

Have the reviewers score the same sample resources alone, then compare metric by metric, discuss every flagged metric until the evidence settles it, and record how to score similar cases in the future. That is consensus scoring, and it is not averaging. A suggested goal, which a team may change, is agreement within 3 points on at least 8 of 10 metrics. If a team misses it, repeat with a new sample.

To calibrate an agent, follow six steps. Build a calibration set of 10 to 20 resources, scored to consensus by two or more trained humans and hidden from the agent. Run the agent. Compute agreement rate, mean absolute difference, and bias. Trace the largest disagreements to causes by error type. Refine the prompt, one change per observed error, and rerun. Then confirm on a fresh set, because a prompt tuned on one set learns that set's quirks.

**Example:** Four reviewers each score two sample resources alone, then meet to discuss every metric on which they differ.

See [Chapter 11](chapters/11-manual-evaluation-adoption/index.md) and [Chapter 14](chapters/14-checking-agent-output/index.md).

### How big should a reusable component be?

Usually one idea or one learning objective, with its explanation, an example, and a check question. A piece that is too big cannot be partly reused, and one that is too small is not worth finding. Apply the lift test: copy the piece somewhere new, and it must still make sense and work.

Search the text for words that depend on the rest of the resource, such as "above," "below," "earlier," "next section," and "the figure." Phrases like these break when the piece is moved. Fix them by restating the idea or linking to the other piece by its own address. Giving a piece its own file does not make it standalone.

**Example:** A 12-page chapter split into six two-page lessons, each with its own objective and quiz, is far easier to reuse than the whole chapter. A quiz that says "use the table from Chapter 2" fails the lift test.

See [Chapter 9](chapters/09-modularity-metadata/index.md) and [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### How do I keep student data away from AI services?

Reviewing a resource needs no student data, so never paste student names, grades, or private records into an assistant. Student data covers names, ID numbers, grades, test results, written work, photographs, attendance, health and disability information, and anything identifying when combined with other details. Pasted text cannot be pulled back, and a deletion request may not undo it, because the service may store the text, staff may read it, and some services use it to improve models.

In the United States, FERPA restricts disclosure of identifiable student education records, and sending them to an AI company can be such a disclosure. The book gives no legal advice, so ask your school's privacy officer or technology office. Give agents the least file access they need, read-only if possible, and keep student records out of the folder.

**Example:** A published textbook chapter can go to an AI service. A grade spreadsheet with student IDs, a student photo, or a parent email thread cannot.

An A/B test does involve student data, so it needs consent, anonymizing, and an approved way to handle the data. See [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md) and [Chapter 16](chapters/16-ab-testing-design/index.md).

### When does a second agent add value, and when does it only add cost?

A second agent helps when it narrows what a person must check, and it adds only cost when it is treated as proof. In multi-agent review, several agents score the same resource independently. The spread is the highest score minus the lowest, and a triage rule sorts the results. A spread over 3 is flagged. Otherwise, if any agent quoted no evidence, check anyway. Otherwise accept for a spot check.

The cost multiplies, since three agents cost three times as much as one. Agreement among agents is not truth, because similar models share blind spots, and unanimous agreement with no evidence is especially suspect. A second-agent cross-check, in which the second agent hunts for faults in the first report instead of producing a fresh score, is a cheap first filter. It can miss errors and raise false alarms.

**Example:** In a test with 5 planted errors, a cross-check flagged 3 of 5, missed 2, and raised 1 false alarm.

See [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md) and [Chapter 14](chapters/14-checking-agent-output/index.md).

### How do changes in one metric affect the others when I improve a resource?

Fixes can have side effects, so re-score all ten metrics and not only the ones you touched. Re-scoring only the metrics you changed hides what else moved. Use the same rubric, evidence rules, prompt, and tools as the first scoring, and use a fresh agent session, because an agent that edited the resource scores it generously. Have a person verify every changed score and sample the rest.

**Example:** The improved *Watershed Basics* gained on five metrics, and its portability score fell from 7 to 6, because the new simulation's script is blocked on 1 of 3 test platforms. A partial re-score would have missed the drop. The total rose from 65 to 78, a gain of 13 against a projected 14.

The book's success test for an improvement is that at least two quality and two reusability metrics rise, every change is reviewed and logged, and no metric falls without a stated reason. See [Chapter 15](chapters/15-improving-resources-with-ai/index.md).

### How do I judge whether an improvement actually helped learners?

A score gain is not a learning gain. The score gain is the new total minus the old total, and it shows that the resource passes more of the rubric's checks. Whether students learn more is a different question that only a student test can answer. The book's example gains 13 points, which is 13 for 7.5 hours of work, or about 1.7 points per hour. A gain from better metadata may change nothing a student notices.

Then test. The A/B test compares gains between a control and a treatment group, and it can show only whether the whole bundle of fixes helped, not which fix did the work. Testing one fix at a time takes more students and time. Over many resources, the rubric-outcome correlation shows whether higher-scoring resources tend to produce larger gains.

**Example:** In the pilot, the improved version's mean gain was 22.0 against 15.0 for the original, a difference of 7.0 points.

See [Chapter 15](chapters/15-improving-resources-with-ai/index.md), [Chapter 16](chapters/16-ab-testing-design/index.md), and [Chapter 17](chapters/17-ab-testing-analysis/index.md).

### How would I build a reusable component from a lesson I already teach?

Work in six steps:

1. Pick one idea or objective, and remove references that depend on the rest of the lesson, such as "as shown above."
2. Give it a descriptive name, such as `watershed-quiz`, and not a name like `final-v2`.
3. Put everything in one folder: the content, a README, a license file, a metadata file, and any images or scripts, with links that stay inside the folder.
4. Add the license in three places, the visible page footer, the license file, and the metadata record, and list every third-party item with its title, author, source, and license.
5. Write a one- or two-sentence description that starts with what the component does, and record subject, grade level, and keywords.
6. Test it. Apply the lift test, then embed it by iframe on at least two platforms.

Finally, list it in an index page or catalog so teachers can find it.

**Example:** A folder with `index.html`, `quiz.js`, `README.md`, `LICENSE.txt`, `metadata.json`, and an `img` folder holds one packaged quiz.

See [Chapter 18](chapters/18-components-publishing-oer/index.md) and [Chapter 9](chapters/09-modularity-metadata/index.md).

### How do I use student surveys and comments alongside test scores?

Test scores say what students learned, and a survey and comments say what they experienced, including barriers. Follow five rules for the survey: ask the same questions of both groups, keep them neutral, put one idea in each, make them specific, and keep responses anonymous. A common format rates each statement from 1 (strongly disagree) to 5 (strongly agree). Avoid leading questions such as "Did you enjoy the great new simulation?", double-barreled ones such as "clear and fair," and vague ones such as "The lesson was good."

Ratings report opinion and not learning, and novelty can inflate them. For comments, code them into themes and count the students in each theme. Have two people code independently and resolve differences, and remove identifying detail before you quote anyone. Comments hint at causes without proving them.

**Example:** In the pilot, "helped me understand" averaged 3.5 for the control group and 4.3 for the treatment group. Seven of the 12 treatment students said the simulation helped. Two control students could not get the original quiz to load on school tablets, which explained a completion rate of 10 of 12, against 12 of 12 for treatment.

See [Chapter 17](chapters/17-ab-testing-analysis/index.md).

### How do I publish an improved resource so others can find and reuse it?

Publishing means a stable public address, an open license, and complete metadata. A file on a shared drive may be visible, and it is not open. The book gives eight steps in order: confirm the license, finish the metadata, freeze the tested version with release notes, package each component, build the site, deploy it, open the feedback channel and publish the maintenance plan, and list the resource in a clearinghouse and tell colleagues. Listing comes last, so a reader who arrives finds a finished resource.

A static site generator turns Markdown files and a settings file into finished web pages. MkDocs, Jekyll, and Hugo are examples. This book uses MkDocs with the Material theme, and GitHub Pages serves such a site at an address of the form `username.github.io/repository`. The first page should show the title, the license with a link, a citation, the version, a link to the source, and a contact for the author. Release notes use four headings: Added, Changed, Fixed, and Removed.

**Example:** A teacher publishes a library of four items, a reading, a quiz, a simulation, and a glossary, each as its own component under CC BY 4.0, and submits it to a catalog such as OER Commons or MERLOT.

A clearinghouse listing points to your site and does not move the resource. See [Chapter 18](chapters/18-components-publishing-oer/index.md).

### How do I find out whether anyone is reusing what I published?

An open license lets people reuse a resource without asking or telling you, so the picture is always partial. Read the signals by strength. Strong signals are a course page that links to you and credits you, a fork with changes, and a teacher's message. Weak signals are downloads, page views, and a star. Your own visits and automated crawlers are not evidence at all. Search for the resource's title and your attribution line.

Choose an analytics tool that records counts and not individuals, and remember that a page view is not a reader and a reader is not a learner. A drop over a holiday reflects the calendar. Combine four kinds of evidence in an impact report, keep them apart, and say how strong each is: reach (analytics), reuse (reuse tracking), learning (the A/B test), and experience (surveys, comments, and the issue list).

**Example:** A sample report cites about 3,500 page views in six months, reuse by at least three teachers, a learning gain of 22.0 against 15.0 in a pilot of 24, and 11 issues of which 7 are fixed, and it notes that the pilot was small and that a larger test is planned.

See [Chapter 18](chapters/18-components-publishing-oer/index.md).

### Why does a published resource need a maintenance plan and a feedback channel?

Without a maintenance plan, a resource drifts out of date, and a reuser cannot tell whether it is still safe to trust. A plan states who is responsible, what is checked, how often, and when the resource will be retired. The book's sample schedule runs the link checker every three months, checks changeable facts once a year, runs an accessibility scan once a year and after any large change, reviews open issues at every release, and decides once a year whether to retire the resource. Retiring is part of maintaining: mark the resource archived, with a note on its first page.

Offer more than one feedback channel, such as an issue tracker, a plain email address, and a short form, because a required account excludes some teachers. Never ask for student information, and state how quickly you will reply. A channel that is promised and then ignored is worse than none.

See [Chapter 18](chapters/18-components-publishing-oer/index.md).

## Advanced Topic Questions

### Does a higher rubric score predict more student learning?

That is the question of rubric validity, and the book answers it with a method and an illustration, not a finding. The method compares each resource's rubric total with the mean normalized gain its students achieved in an A/B test, using the normalized gain because pilots use different tests. A Pearson correlation near 1 would mean higher-scoring resources tend to produce larger gains.

In the chapter's illustration of seven resources, r is about 0.93, which means roughly 87 percent of the variation in gains goes with the rubric score. Read that number with care. Only two of the seven points, the original and improved *Watershed Basics*, come from the real pilot, and the other five are made-up pilots. With the weakest resource removed, r is still 0.92. A serious check needs 20 or more resources. And correlation does not show cause.

The illustration also teaches a habit: among three resources with the same total of 65, the gains differ, so read the lowest metric before the total.

See [Chapter 17](chapters/17-ab-testing-analysis/index.md) and [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md).

### Should an AI agent's score ever replace a human review?

The book's answer is no. The agent drafts and a person verifies, because accountability cannot be delegated and because even a well-calibrated agent makes errors that only checking finds. What calibration can earn is a more limited role: the agent becomes a first pass, with a person still verifying the claims that decide the outcome.

The book offers an illustrative first-pass standard, which each team should reset after its own pilot:

- Agreement rate at a threshold of 1: 80 percent or more.
- Absolute bias: 0.5 or less.
- Mean absolute difference: 1.0 or less.
- Kappa on the adoption decision: 0.61 or more.
- Run-to-run range per metric: 1 or less, or that metric goes to a person.

An agent that misses the standard only drafts evidence for a person. In the book's example, the first-draft agent has perfect agreement and correlation but a bias of +1.0, so it fails, because that bias turns a revise decision into adopt. Metrics that rest on exact checks suit a first pass best, and judgment metrics need close human checking.

See [Chapter 14](chapters/14-checking-agent-output/index.md) and [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md).

### What patterns do AI agent errors follow, and how does each type point to a fix?

Agent errors fall into four types, and each type tells you both how to catch it and how to change the prompt.

- **Factual error:** the report says something the resource does not. Catch it by opening the resource and checking the claim. Fix the prompt by demanding a quotation or location for every claim and a tool log for every measurement.
- **License error:** the license is misread. Compare the claim with the statement itself. Require the agent to quote the statement word for word.
- **Citation error:** the source is invented or does not support the claim. Look up the source and read the passage. Allow only sources that appear in the resource or that you supplied.
- **Scoring error:** the arithmetic or the band is wrong. Recount the passes, recompute the band, and re-add the total. Ask for a pass or fail on each of the ten checks, and let a spreadsheet or script add the total.

The patterns across types are telling. Errors cluster where a check needs a tool but no tool ran, where the agent relies on memory, and where scores run high with no evidence beside them. A small positive bias on every metric is score inflation, which no single claim check will reveal.

**Example:** A count that is off by one is a factual error, while a total that does not add up is a scoring error.

Track the types in the findings log, because a type that keeps recurring tells you which prompt rule to add next. See [Chapter 14](chapters/14-checking-agent-output/index.md).

### What are the trade-offs between automated checks and manual review?

Automation gives speed, repeatability, and low cost on exact tasks. It lacks context and judgment, so each tool has a blind spot. The book names four checks worth automating, and what each cannot find:

- **Link checker:** finds links that fail or have moved. It cannot tell that a working link leads to the wrong content.
- **Accessibility scan:** finds missing alt attributes and weak contrast. It cannot judge whether alt text is useful or captions are accurate.
- **License detection:** finds a missing license or a mismatch between page and metadata. It cannot tell whether the claim is true, and it can miss a license that appears only in an image.
- **Readability scan:** gives a reading level for sampled passages. It cannot see undefined terms or audience fit.

Manual review is slow, and it is the reference that software is measured against. It brings context, judgment, and real-world tests such as embedding a resource on a platform. The practical split is that tools take the exact checks, the model drafts judgments about text, and a person takes the real-world tests and verifies what decides the outcome. Cost also matters, and batches multiply it.

See [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md) and [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md).

### How does the rubric specification differ from the ten-metric rubric?

They are two different documents, and the book does not yet reconcile them. The ten-metric rubric in [Chapter 3](chapters/03-ten-metric-rubric-scoring/index.md) is the one every chapter teaches. It scores a resource on ten metrics from 0 to 10, adds them to a total out of 100, and ends in an adopt, revise, or reject decision.

The [rubric specification](rubric-spec.md) is marked as a draft, version 0.4, a design specification that has not yet been implemented or tested. It describes an evaluator for LLM agent skills with a 0 to 3 scale, 22 scripted checks, and 17 judgment indicators. Its two headline numbers, one for overall quality and one for reusable content, are deliberately never combined into a single total, and it sets no adopt or reject rule. It builds on a review of 14 earlier rubrics by Yuan and Recker (2015), which found, among other things, that 5 of the 14 had no rating scale and only 3 had a detailed scoring guide.

For anything you do with this book, such as scoring by hand, writing a prompt, or preparing for the certificate, use the Chapter 3 rubric. Treat the specification as a draft for the automated evaluator.

### How would I design a calibration and certification program for my district?

Combine the book's pieces into one loop. Train reviewers first: they read Chapters 3 to 10, score two samples with evidence, compare their scores with an experienced reviewer, and join a calibration session. Build a calibration set of 10 to 20 resources scored to consensus by trained humans, and use it to check both new reviewers and any agent. Run a workshop of about 20 teachers, with a facilitator guide for each session that gives the time, goal, materials, steps, and the common problems with their fixes, so a colleague who did not write the workshop can run it. Use the certificate requirements, which tie each requirement to evidence, as the standard. Have a reviewer who did not take part in the work check each submission.

Certified teachers can then serve as local reviewers, the first reviewers for a school or district. The role has limits: they flag license problems without ruling on legal questions, never send student information to an agent, advise and do not make adoption decisions, and do not certify other teachers. They repeat the calibration on a reference set at least once a year.

To grow the program, use train-the-trainer: co-facilitate, then lead with an experienced facilitator watching, then lead alone. Keep quality by using the same kit and reference set, observing every new trainer's first session, and having trainers repeat calibration. Evaluate the program at four levels: reaction, learning, behavior, and results. Do not rely on the exit survey, which measures reaction only.

See [Chapter 19](chapters/19-training-certifying-reviewers/index.md), [Chapter 11](chapters/11-manual-evaluation-adoption/index.md), and [Chapter 14](chapters/14-checking-agent-output/index.md).

### How would I build an agent skill that evaluates OER automatically?

Package the book's method as a skill: a folder with an instructions file whose top description says when it applies. It carries five parts.

1. **A rubric prompt** with the role, the ten checks for each metric, the rules (evidence for every check, "not checkable" instead of guessing, no invented quotations, untested checks count as failed), and the output format. Mark the resource as material, not instructions.
2. **Tools** for the exact checks: a link checker, a readability calculator, an accessibility checker, and a metadata validator. Record the tool and version in the report.
3. **Structured output** with a check-by-check result, passes, band, score, and a list of checks not verified, plus a script that recounts passes, recomputes bands, and re-adds the total.
4. **Human checkpoints:** risk-matched oversight and a findings log that records what was accepted, corrected, or rejected.
5. **Calibration:** run it on a set of 10 to 20 hand-scored resources, measure against the first-pass standard, refine the prompt one change per observed error, and confirm on a fresh set.

Set safe defaults. Give the agent read-only file access, keep student data out, and record the model, date, and prompt version with every run. Never let it change the resource it reviews.

See [Chapter 12](chapters/12-ai-agents-prompts-scoring/index.md), [Chapter 13](chapters/13-automated-checks-cost-privacy/index.md), and [Chapter 14](chapters/14-checking-agent-output/index.md).

### How do I appraise whether my A/B test design is fair?

Apply a checklist drawn from [Chapter 16](chapters/16-ab-testing-design/index.md), and treat any failure as a reason to revise the plan before collecting data.

- **Hypothesis:** written before the test, and specific, measurable, directional, sized, and falsifiable.
- **Versions:** both frozen and labeled, with the change log listing the differences.
- **One difference:** the groups differ in the version and nothing else, with the same teacher, instructions, time, and test.
- **Outcome measure:** one primary outcome, from a separate test and not the resource's own quiz.
- **Assignment:** by chance, blocked by pre-test score if the class is small.
- **Sample size:** stated honestly. A group of about 12 is a pilot, and its result is suggestive.
- **Consent and privacy:** consent before any data is collected, a real choice to decline at no cost, little data collected, and codes with a separate key.
- **Equity:** both versions work for every student, including those using assistive technology and those without a fast home connection, and the report says who took part.

Remember that a bundle of fixes shows only whether the bundle helped. For red flags, look at the book's own failures: students choosing their own version, a pre-test given before consent, and a small test claimed as proof.

See [Chapter 16](chapters/16-ab-testing-design/index.md) and [Chapter 17](chapters/17-ab-testing-analysis/index.md).
