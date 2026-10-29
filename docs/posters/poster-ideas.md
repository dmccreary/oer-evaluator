---
title: Infographic Poster Ideas
description: Thirty ideas for overlay infographic posters that summarize a concept or compare items in OER Evaluator, with the reason each is useful and tips for making it well.
---

# Infographic Poster Ideas

This page lists ideas for **infographic posters** for *OER Evaluator*. The book has two poster-style MicroSims but no overlay infographic posters yet. I read the outlines of all 19 chapters and their worked-example tables, and looked for places where a reader has to hold a comparison or a multi-part idea in mind from prose. Each idea below turns one of those into a single picture that can be understood at a glance and then explored.

Each poster is meant to be wrapped by an interactive overlay, so a reader can hover or click for detail and take a short quiz. Two overlay types are used:

- **Grid:** two to six large rectangular zones, side by side. Best for comparisons. Printed zone headings can be part of the artwork.
- **Callout:** five to fifteen numbered markers on one illustration. Best for anatomy and process. The artwork should contain no text, because the overlay supplies every label.

Many chapters already have a MicroSim that practices the same idea by sorting or matching. A poster does a different job: it is the reference picture a reader comes back to. Where an idea overlaps a MicroSim, the entry says so, and the poster's quiz mode can reuse that MicroSim's items. Chapter 2 has no entry because the Six Creative Commons Licenses Poster already covers its main comparison, and Chapter 11 has none because its decision rule is covered by poster 4.

**Tips that apply to every poster:**

- **One idea per poster, and the title states it.** A reader should get the point in about ten seconds. Everything else belongs in the overlay.
- **Use a wide landscape canvas**, such as 1200 by 700 pixels, which suits the side-navigation layout of this book.
- **Copy rules and numbers from the chapter.** Do not round, recompute, or reword them. Where the chapter marks an example as illustrative, the poster must say so too.
- **Choose the production route by how exact the content must be.** Image models garble text and numbers. Draw anything with exact values, such as radar charts, bell curves, and tables of counts, in code (SVG, Chart.js, or Plotly) and export it as the poster image. Use a generated illustration only when it carries no text, and let the overlay add the labels.
- **Build the poster to pass the rubric it teaches.** Reviewers will score each poster as a component. Give it alt text and a long description in its lesson page, text contrast of at least 4.5 to 1, and a meaning that never depends on color alone (add an icon, shape, or word). Keep the editable source (the SVG or the image prompt plus `data.json`), a `metadata.json` record, and an iframe-ready `main.html`.
- **Use the same two colors for the same two ideas in every poster.** Pick one for quality metrics and one for reusability metrics, and keep them. Pair every traffic-light color with an icon.
- **Keep Echo the Loon off the artwork.** Echo belongs in the mascot admonition on the lesson page, where the placement rules in `CONTENT-GENERATION-GUIDE.md` apply.
- **Avoid brand logos and real interface screenshots.** They age quickly and raise trademark questions. Draw generic stand-ins.

**Summary of the thirty ideas:**

| # | Poster | Chapter | Overlay | Job |
|---|--------|---------|---------|-----|
| 1 | The OER Evaluator Loop | All | Callout, 8 | Summary of the whole book |
| 2 | Free Is Not Open: Price and Permission | 1 | Grid, 4 | Comparison |
| 3 | The 5R Permissions: Five Things You May Do | 1 | Grid, 5 | Summary |
| 4 | From Ten Scores to One Decision | 3 | Callout, 6 | Process |
| 5 | Five Resources, Five Shapes | 3 | Grid, 5 | Comparison |
| 6 | Source Files and Delivery Files | 4 | Grid, 3 | Comparison |
| 7 | Fork and Pull Request: Two Lanes, Seven Steps | 4 | Callout, 7 | Process |
| 8 | Following a Claim Back to Its Source | 5 | Callout, 4 | Process |
| 9 | How Fast Does Content Spoil? | 5 | Grid, 3 | Comparison |
| 10 | Bloom's Ladder: Six Levels, Measurable Verbs | 6 | Grid, 6 | Summary |
| 11 | Four Principles, Five Learners | 7 | Grid, 4 | Summary |
| 12 | What a Screen Reader Hears | 7 | Grid, 2 | Comparison |
| 13 | Feedback That Teaches | 8 | Grid, 4 | Comparison |
| 14 | Woven or Modular? The Lift-Out Test | 9 | Grid, 2 | Comparison |
| 15 | You Can't Reuse What You Can't Find | 9 | Grid, 3 | Comparison |
| 16 | Link, Embed, Import, or LTI: Four Ways Into an LMS | 10 | Grid, 4 | Comparison |
| 17 | Model, Assistant, Agent, Skill | 12 | Grid, 4 | Comparison |
| 18 | Weak Prompt, Strong Prompt | 12 | Grid, 2 | Comparison |
| 19 | What Each Automated Check Can and Cannot Find | 13 | Grid, 4 | Comparison |
| 20 | Safe to Send? Student Data and AI Services | 13 | Grid, 3 | Comparison |
| 21 | Four Ways an Agent Gets It Wrong | 14 | Grid, 4 | Comparison |
| 22 | Agreement Is Not Skill | 14 | Grid, 3 | Summary |
| 23 | The Fix Toolkit | 15 | Callout, 13 | Summary |
| 24 | Can I Publish My Improved Version? | 15 | Grid, 6 | Comparison |
| 25 | The A/B Test on One Page | 16 | Callout, 7 | Process |
| 26 | Five Ways a Test Can Lie to You | 16 | Grid, 5 | Comparison |
| 27 | Reading an Effect Size | 17 | Grid, 3 | Comparison |
| 28 | Component in a Box | 18 | Callout, 7 | Anatomy |
| 29 | A One-Day Workshop Timeline | 19 | Callout, 8 | Process |
| 30 | Four Levels of Training Evaluation | 19 | Grid, 4 | Summary |

## The OER Evaluator Loop

**Chapter:** all, placed on the home page and the chapters index · **Overlay:** Callout, 8 markers · **Slug:** `oer-evaluator-loop`

**Description.** A single closed loop, drawn as a circular path with eight stations. The stations follow the book: understand OER and licenses (Chapters 1 and 2), score a resource by hand with the ten-metric rubric (3 to 11), direct an AI agent to make a first pass (12 and 13), check the agent's evidence (14), improve the lowest metrics with agents (15), test the change with students in an A/B test (16 and 17), calibrate the agent against those results (14 and 17), and publish and train others (18 and 19). The arrow that returns from the calibration station to the agent's first pass is the one that matters, because it is how automated scores earn trust.

**Why it is useful.** The book has 19 chapters and 351 concepts, and the course description describes a path from evaluation to improvement to testing, with the test results used to check and calibrate the automated scores. No single image shows that path yet. A reader who sees the loop first knows why each chapter exists. Each marker can link to its chapters, and the quiz can ask which station comes right after "check the agent".

**Tips for a high-quality infographic.**

- Make the order unmistakable with numbered stations and one-way arrows. Draw only one loop.
- Make the return arrow from the calibration station back to the agent's first pass the strongest line on the poster, and give it its own note in the overlay that says test results calibrate the agent.
- Group the stations into three color families (evaluate, improve, test and publish) and keep the total to four colors.
- Keep the artwork free of text and let the overlay name each station. Take chapter numbers from `chapters/index.md` and recheck them whenever chapters move.

## Free Is Not Open: Price and Permission

**Chapter:** 1 · **Overlay:** Grid, 4 zones · **Slug:** `price-and-permission`

**Description.** A two-by-two matrix. The horizontal axis is price (costs the user nothing, or costs money), and the vertical axis is permission (may edit and share, or may not). The four zones use the chapter's own examples. A lesson plan under CC BY is free and open. A publisher's sample chapter marked "All rights reserved" is free and closed. A commercial textbook from the campus store costs money and is closed. An open textbook that a print shop sells at cost is open, and only its printed copy costs money. A bracket around the two open zones marks them as OER, because the chapter defines OER by permission, not by price.

**Why it is useful.** Confusing *free* with *open* is the most common misunderstanding in the field, and it leads teachers to adopt materials they may not edit or share. The chapter treats it in a table and a sorting MicroSim. A matrix shows at a glance that price and permission are independent, and it sets up the open license metric in Chapter 9.

**Tips for a high-quality infographic.**

- Use a matrix, not a list, because independence is the lesson. Draw two dials above it, as in Echo's note that price and permission are separate dials.
- Do not color free as good and paid as bad. Use one hue for the open row and a neutral for the closed row, and add an open and closed padlock icon so meaning does not rest on color.
- Draw one recognizable object per cell, taken from the chapter. Do not use publisher logos or invent brand names.
- Leave out dollar figures. The chapter's $160 example is illustrative and belongs in the overlay with that label.

## The 5R Permissions: Five Things You May Do

**Chapter:** 1 · **Overlay:** Grid, 5 zones · **Slug:** `five-r-permissions`

**Description.** Five equal panels in the chapter's order: Retain, Reuse, Revise, Remix, Redistribute. Each panel pairs the plain-language meaning with the chapter's test question, such as "Can I make and keep my own copy?" and shows a small scene of a teacher doing it: saving a copy, using a lesson as it is, editing a sentence, combining two lessons, and handing copies to colleagues. A thin connector under the panels shows the chapter's point that the permissions build on one another, from having a copy to using it to changing it to combining and sharing it.

**Why it is useful.** The 5Rs are the vocabulary of every later chapter. Revise leads to editable source, Remix to license compatibility, and Redistribute to ShareAlike. It works as a classroom-wall reference and as a handout. The Five R Scenario Matcher already practices the matching, and its scenarios can supply the quiz mode.

**Tips for a high-quality infographic.**

- Give the five panels identical structure, size, and icon style, so the only thing that changes is the verb.
- Print the test question in the largest text of each panel. It is the part readers will remember.
- Use a sequence cue, such as small arrows, and avoid a ranking cue, because the permissions are not levels of importance.
- Keep money symbols away from Redistribute, since several licenses forbid commercial use and the picture should not suggest otherwise.

## From Ten Scores to One Decision

**Chapter:** 3, applied again in 11 · **Overlay:** Callout, 6 markers · **Slug:** `ten-scores-to-one-decision`

**Description.** A funnel or staircase that follows the chapter's layers. Ten metric scores, each 0 to 10, combine into two subtotals of 50 points (quality, metrics 1 to 5; reusability, metrics 6 to 10). The subtotals add to a total out of 100, the total falls into a score band (Excellent 90 to 100, Good 75 to 89, Fair 50 to 74, Weak 25 to 49, Poor 0 to 24), and the band and a floor produce a decision: Adopt when the total is at least 75 and every metric is at least 5, Revise when the total is at least 50 and the Adopt rule is not met, and Reject below 50. A sixth marker sits on the floor as a gate, with the chapter's "One Gap" resource caught at it: nine metrics of 9 and one of 4 give a total of 85, which is Good, and the decision is still Revise.

**Why it is useful.** Chapter 3 teaches the layers one section at a time, and the chapter lists "a total of 75 or more always means Adopt" as a misconception. A funnel shows how each layer loses detail and why the floor exists. Chapter 11 uses the same rule for real decisions. The Total Score Calculator practices the arithmetic, and the poster is the map of the rule.

**Tips for a high-quality infographic.**

- Narrow the funnel at each layer to show detail being lost, and keep the ranges and rules exactly as Chapter 3 prints them.
- Label the thresholds as this book's starting rule. The chapter calls the threshold a teaching choice and not a standard.
- Show the One Gap example as a small inset with real numbers, so the floor is demonstrated and not only described.
- Color Adopt, Revise, and Reject as a traffic light and add a check, a pencil, and a cross so the decision never depends on color.

## Five Resources, Five Shapes

**Chapter:** 3 · **Overlay:** Grid, 5 zones · **Slug:** `five-resources-five-shapes`

**Description.** Five small radar charts side by side, one for each profile in the chapter's total score example. Watershed Basics scores 32 and 33 for a total of 65 (Fair, Revise). Open Algebra scores 43 and 47 for 90 (Excellent, Adopt). Locked Chemistry E-book scores 44 and 21 for 65 (Fair, Revise). One Gap scores 45 and 40 for 85 (Good, Revise). Thin Material scores 14 and 23 for 37 (Weak, Reject). Each chart has ten spokes, five in the quality color on one side and five in the reusability color on the other. The comparison to point out is that Watershed Basics and Locked Chemistry both total 65 yet look nothing alike: one is balanced and mediocre, the other is lopsided, with strong quality and locked-down reuse.

**Why it is useful.** The chapter argues that quality and reusability must be reported separately and that a total hides the shape. A shape is learned faster than a table. The poster also prepares Chapter 15's rule of fixing the lowest metric first, because the notch in a shape is the first thing to fix.

**Tips for a high-quality infographic.**

- Compute each chart from the actual scores and draw it in code. Use the same 0 to 10 scale and the same spoke order, metrics 1 to 10, in all five.
- Add a faint ring at 5, the floor, so any spoke that dips inside it is visible without reading a number.
- Print only the total, band, and decision under each chart, and leave the ten individual scores for the overlay panel.
- Mark the two 65s with a bracket labeled "same total, different shape", and label all five as illustrative examples, as the chapter does.

## Source Files and Delivery Files

**Chapter:** 4 · **Overlay:** Grid, 3 zones · **Slug:** `source-and-delivery-files`

**Description.** Three zones: good source, usually acceptable, and poor source. Markdown and plain text, HTML, OpenDocument text, CSV for data, and SVG for diagrams sit in the first zone. A Word document sits in the second, because it is a published standard whose full fidelity depends on particular software. A PDF and a page-layout or design-program file sit in the third. Every file is drawn as a document tile with its extension printed large, and carries two small badges, one answering "is the format open?" and one answering "is it a good source for editing?" The PDF is the instructive tile: its format is open and it is still a poor source.

**Why it is useful.** Editable source is metric 9, and the most common failure is a resource distributed only as a PDF. Many teachers assume an open format is an editable one. Two badges separate those two questions. The File Format Triage MicroSim practices the sort.

**Tips for a high-quality infographic.**

- Keep the extensions (.md, .html, .odt, .csv, .svg, .docx, .pdf) short and legible. They are safe to print on the artwork or to add through the overlay.
- Make the two badges different shapes as well as different colors.
- Use generic document tiles. Do not use the logos of word processors or PDF software.
- Put a thin arrow across the top from "source: change this" to "delivery: read this", so the vocabulary is on the poster.

## Fork and Pull Request: Two Lanes, Seven Steps

**Chapter:** 4 · **Overlay:** Callout, 7 markers · **Slug:** `fork-and-pull-request`

**Description.** A two-lane diagram. The top lane is the original repository and its maintainer. The bottom lane is your own copy. The seven steps follow the chapter's sequence: find the repository, fork it, make and save a change with a message, open a pull request, the maintainer reads and comments, you answer with more changes, and the maintainer merges. The arrows cross between lanes at the fork, the pull request, and the merge. A faint dotted branch shows the other ending, a declined pull request.

**Why it is useful.** Git vocabulary is the hardest part of Chapter 4, and the picture shows something a list cannot: whose copy each step happens in. It is also how an improved resource finds its way back to its author, which matters again in Chapters 15 and 18. The Fork and Pull Request Sequencer practices the order.

**Tips for a high-quality infographic.**

- Number the steps 1 to 7 along one left-to-right path so the order reads without effort.
- Use a physical picture: a photocopied binder for the fork, a sticky note for the pull request, a stamp for the merge. Keep Git terms for the markers.
- Draw a generic interface, not screenshots of a real code-hosting site.
- Keep the declined branch faint so it does not compete with the main path.

## Following a Claim Back to Its Source

**Chapter:** 5 · **Overlay:** Callout, 4 markers · **Slug:** `claim-source-chain`

**Description.** A chain of four links showing the chapter's worked example. The claim "Wetlands filter pollutants" appears in a resource's footnote 4, which cites a textbook, which cites a review article, which summarizes several studies, one of which reports measurements of pollutant levels before and after water passed through a wetland. The first three links are drawn as other people's summaries. The fourth is drawn as the place where the measurement was made. A flag at the second link reads "a reviewer who stops here has only found that a textbook agrees".

**Why it is useful.** Chapter 5 separates primary from secondary sources, and Chapter 14 warns about invented citations. A reader needs to see that confirming a citation exists is not the same as tracing the claim. The chapter's rule that the further back you trace, the more you can trust the check, is easier to feel as a chain than to read as a sentence.

**Tips for a high-quality infographic.**

- Draw each link as a different object (a footnote mark, a textbook, an article, a lab bench) and make the original source differ in shape, not only in color.
- Keep the claim wording identical to the chapter.
- Do not print real journal names or citations. The chapter's examples are invented, and the poster should say "illustrative" so no one searches for them.
- Add a "stopped here" flag at link two, because the early stop is the mistake the poster exists to prevent.

## How Fast Does Content Spoil?

**Chapter:** 5 · **Overlay:** Grid, 3 zones · **Slug:** `content-shelf-life`

**Description.** A market-stall picture with three shelves, based on the chapter's table of how quickly six kinds of content go out of date. The slow shelf holds basic mathematics and definitions (check at each major review) and the sequence of historical events (also at each major review). The middle shelf holds statistics and survey results and standards, curricula, and guidelines (check every few years, or when new data or a revision appear). The fast shelf holds software screenshots, prices, and web addresses, and laws, policies, and contact details (check every year or more often). Each item wears a date stamp.

**Why it is useful.** Currency is half of metric 1, and reviewers often apply one rule to every page. The poster gives a quick triage and a recheck schedule, and it supports the revision-history and link-rot ideas in the same chapter. The Outdated Content Spotter practices the judgment.

**Tips for a high-quality infographic.**

- Print the "how often to check" wording verbatim, because it is the useful data. Do not turn "every few years" into a number the chapter does not give.
- Keep the six items from the chapter and resist adding more.
- Use a gradient from long-lasting to short-lived and add calendar icons so the order does not depend on shade.
- Keep the produce-stall metaphor literal and light. A date stamp on each item carries the idea without extra text.

## Bloom's Ladder: Six Levels, Measurable Verbs

**Chapter:** 6 · **Overlay:** Grid, 6 zones · **Slug:** `bloom-ladder`

**Description.** A six-step staircase using the revised taxonomy. From the bottom: Remember (list, name, define), Understand (explain, summarize, interpret), Apply (calculate, use, solve), Analyze (distinguish, differentiate, examine), Evaluate (judge, critique, justify), and Create (design, compose, construct). Each step carries the chapter's example objective. A side panel shows the mismatch the chapter warns about, an outcome that says "predict" taught by activities that only ask for recall.

**Why it is useful.** The alignment metric, the outcome verb checks, the quiz bank, and this book's own learning outcomes all use Bloom's levels, so readers return to this reference constantly. The side panel shows why the level of an outcome and its activities must match. The Bloom Level Sorter and Outcome Verb Checker practice the classification.

**Tips for a high-quality infographic.**

- Make the verbs the largest text on each step. They are the part people use when they write or audit an objective.
- Use the 2001 revised names (verbs), not the original nouns, to match the course description.
- Draw a staircase and not a pyramid. A pyramid suggests fewer outcomes at the top, which the chapter does not claim.
- Use a single-hue ramp from light to dark and also number the steps, so order survives a grayscale print.

## Four Principles, Five Learners

**Chapter:** 7 · **Overlay:** Grid, 4 zones · **Slug:** `pour-principles-learners`

**Description.** Four zones for the WCAG principles, Perceivable, Operable, Understandable, and Robust, each showing the chapter's example criterion and the learner it protects. Perceivable covers the blind learner who needs text descriptions, the deaf learner who needs captions, and the learner with low vision who needs strong contrast. Operable covers the learner who cannot use a mouse and needs keyboard navigation. Understandable covers the learner with a reading disability who needs clear structure and short paragraphs. Robust covers assistive technology, where custom controls expose a name and role.

**Why it is useful.** Accessibility (metric 4) is full of standards language, and teachers need the human reason first. The chapter pairs principles with criteria in one table and learners with features in another, and the poster joins them. Mapping learners to principles is an editorial choice, since some features serve more than one, so the author should confirm it. The WCAG Principles Sorter practices the sort.

**Tips for a high-quality infographic.**

- Lead with the person and not the standard. Show varied people using the resource successfully, and avoid images that invite pity.
- Make the letters P, O, U, and R the structural device, with four equal zones.
- Model the lesson: give the poster alt text and a long description, as the chapter's complex image description section teaches, and meet the contrast rules it covers.
- Separate the zones with borders and labels, never with color alone.

## What a Screen Reader Hears

**Chapter:** 7 · **Overlay:** Grid, 2 zones · **Slug:** `what-a-screen-reader-hears`

**Description.** A page on the left, speech bubbles on the right, in four rows taken from the chapter. A real heading is announced as "Heading level 2, How water moves". An image with good alt text is announced as "Image, A river meandering through a valley". An image with no alt attribute is announced as "Image, river.png", and an image with an empty alt attribute is announced as nothing at all, which is correct only for a decorative image. The same photograph appears in every row, so the only difference is the markup.

**Why it is useful.** Hearing the result is more persuasive than reading a rule. The chapter's own note says five minutes with a screen reader changes how you write alt text, and a poster of speech bubbles gives a taste of that without any software. It suits a workshop wall. The Screen Reader Announcement Matcher and Alt Text Evaluator practice the judgments.

**Tips for a high-quality infographic.**

- Show what is seen in one color with an eye icon, and what is heard in another with a speaker icon.
- Quote the announcements verbatim and add the chapter's small caution that wording varies between programs.
- Keep the image identical across the rows.
- Do not show a real screen reader's name or interface.

## Feedback That Teaches

**Chapter:** 8 · **Overlay:** Grid, 4 zones · **Slug:** `feedback-that-teaches`

**Description.** One question and one wrong answer, answered four ways. The question is "Which describes infiltration?", and the learner chose "water flowing over the ground". The four messages are "Wrong.", "Incorrect. The answer is A.", "Good try!", and "Not quite. Water flowing over the ground is runoff. Infiltration is water soaking into the ground, so the answer is A." Each is rated against the chapter's criteria: says the answer was wrong, explains why, points toward the right idea, and does not blame. Only the last one passes all four.

**Why it is useful.** Feedback is the part of practice that does the teaching (metric 5), and Chapter 15 has agents write practice questions, so the same yardstick applies to what they produce. Holding the situation constant makes the difference between messages the only thing a reader sees. The Feedback Message Rater practices the rating.

**Tips for a high-quality infographic.**

- Build the poster as live text in HTML or SVG so the wording stays exact, and do not let an image model rephrase the messages.
- Show a small learner reaction beside each message (puzzled, still puzzled, understanding) and keep the tone kind.
- Present the four criteria as a legend with a check or cross per message, so the rating never depends on color.
- Order the messages from least to most helpful.

## Woven or Modular? The Lift-Out Test

**Chapter:** 9 · **Overlay:** Grid, 2 zones · **Slug:** `woven-or-modular`

**Description.** On the left, a woven design: one long page where explanation, quiz, and simulation are interlaced threads of a single cloth, so pulling out the quiz unravels the rest. On the right, a modular design: a reading, a quiz, and a simulation as three separate blocks, each in its own folder, with a hand lifting one block away. Four short rows come from the chapter's table (structure, taking out the quiz, revising the simulation, reuse by another teacher). A thin strip along the bottom shows the degrees of modularity, from a single page to sections, to one file per part, to each part packaged with its own license and metadata.

**Why it is useful.** Modularity is metric 7, and the lift-out test is the practical way to score it. The cloth-and-blocks metaphor is easy to remember. It prepares Chapter 18's component packaging. The Standalone Lift Test practices the judgment.

**Tips for a high-quality infographic.**

- Show the same three pieces in the same colors on both sides, so the eye sees that only the construction differs.
- Put the chapter's failure phrases on sticky notes in the woven side: "as we saw in the last section" and "the diagram above".
- Write the four rows in parallel wording, and keep the degrees strip thin so it does not crowd the comparison.
- Keep the metaphor concrete (cloth against bricks) and do not add a third metaphor.

## You Can't Reuse What You Can't Find

**Chapter:** 9 · **Overlay:** Grid, 3 zones · **Slug:** `cant-reuse-what-you-cant-find`

**Description.** A mock search results page for the query "watershed grade 6 reading open license", with the chapter's three records as result cards. Resource A has a full record (title, subject Earth science, grade 6 to 7, license CC BY 4.0, a clear description) and ranks high. Resource B has only the title "Reading 4", and the search cannot find it. Resource C has the title "Watershed Basics" and an author but no subject, grade, or license, so it may be found, yet the teacher cannot tell the grade or whether she may reuse it. Empty fields show as dashed placeholders.

**Why it is useful.** The principle behind the metadata metric is that you cannot reuse what you cannot find. A story of three cards persuades faster than the list of six core fields and the Dublin Core mapping. It also motivates the improvement plan in Chapter 15, where metadata is the cheapest fix (half an hour for four points in the chapter's example). The Metadata Entry Judge and Dublin Core Matcher practice the details.

**Tips for a high-quality infographic.**

- Draw a generic search page, never a real search engine's.
- Give the three cards identical layouts that differ only in how many fields are filled, and show the six core fields as a legend with matching icons.
- Print the query exactly as the chapter does.
- Mark each result as found, not found, or found but unclear, using icons and words as well as color.

## Link, Embed, Import, or LTI: Four Ways Into an LMS

**Chapter:** 10 · **Overlay:** Grid, 4 zones · **Slug:** `four-ways-into-an-lms`

**Description.** The same resource moving four ways toward the same generic learning management system. A link opens the resource at its own address. An embed (iframe) shows it inside your course page. A Common Cartridge import brings a single compressed file with a manifest into the LMS. An LTI tool opens inside the course but runs on another company's server and can send a score back to the gradebook. Arrows show the difference: one-way for the first three, two-way for LTI. The LTI zone carries a small shield, because passing learner information raises the privacy questions of Chapter 13. A footer strip names the barrier that stops all four, platform lock-in.

**Why it is useful.** Teachers constantly ask how to put a resource into their course, and the wrong method means a broken embed or a gradebook that never updates. The chapter's own objective is to choose among exactly these four for a given need. The LMS Integration Chooser practices the choice.

**Tips for a high-quality infographic.**

- Keep the destination identical in all four zones, so the contrast is the path.
- Show data flow with arrows, since one-way and two-way is the key difference.
- Use "learning management system" and generic shapes, with no vendor logos. Name 1EdTech correctly as the standards group.
- Keep each zone's text to what it does, what you keep, and what it needs.

## Model, Assistant, Agent, Skill

**Chapter:** 12 · **Overlay:** Grid, 4 zones · **Slug:** `model-assistant-agent-skill`

**Description.** Four layers, each built on the one before. A large language model predicts the next piece of text, one token at a time, and does not look facts up. An AI assistant is a program you talk to in ordinary language that answers and waits, powered by a model. An AI agent adds tools, files, and a loop of observe, decide, act, and observe the result. An agent skill is a packaged set of instructions, kept in a folder with a short description that tells the agent when to use it, and is the durable, shareable form of a rubric prompt. Each layer gets the book's own example: filling in the next word, pasting in a resource and asking for problems, listing 14 links and testing each, and the ten-metric rubric packaged as a skill.

**Why it is useful.** The vocabulary is the first barrier in the AI half of the book, and mixing the terms leads to wrong decisions about what to trust. The difference between an assistant that answers and an agent that acts across steps decides what a reviewer must check in Chapters 13 and 14. The Assistant or Agent Sorter and Tool or Model Sorter practice the distinctions.

**Tips for a high-quality infographic.**

- Use nested or stacked layers so "built on" is visible, and label the steps between them "adds tools and a loop" and "adds a saved procedure".
- Make each layer's one-line difference the largest text in its zone.
- Avoid robot and glowing-brain clichés, which overstate ability when the book teaches limits. Add a "limits" tag to the model layer: it does not look facts up, and it can sound sure when it is wrong.
- Leave out product and model names, which date quickly.

## Weak Prompt, Strong Prompt

**Chapter:** 12 · **Overlay:** Grid, 2 zones · **Slug:** `weak-and-strong-prompt`

**Description.** Two prompt cards side by side, each divided into the chapter's five parts: role, task, input, rules, and output format. The weak card says only "Check accessibility.", and the other four bands are empty and hatched. The strong card says "You are a careful reviewer of open educational resources.", "Apply the ten accessibility checks listed below to the resource.", the full text of the resource pasted below the checks, the rules "Quote evidence for every result" and "If a check cannot be verified from the text, write 'not checkable'", and a table with the columns check, result, and evidence. An arrow from the strong card's evidence column points to Chapter 14, where that evidence gets verified.

**Why it is useful.** Writing a rubric prompt is the first hands-on AI skill, and the five parts form a checklist. Empty bands show what is missing without any explanation. The poster compares prompts, and the Anatomy of a Prompt MicroSim labels the parts of one, so the two work together.

**Tips for a high-quality infographic.**

- Give both cards the same five colored bands in the same order.
- Set the prompt text as live text so the wording is exact.
- Draw the prompts as paper cards and not as a chat window, which avoids any brand interface.
- State plainly that a good prompt does not guarantee a good answer. Chapters 13 and 14 exist because answers still need checking.

## What Each Automated Check Can and Cannot Find

**Chapter:** 13 · **Overlay:** Grid, 4 zones · **Slug:** `automated-checks-finds-and-misses`

**Description.** Four tools, each split into a "finds" half and a "cannot find" half, taken from the chapter's table. A link checker finds links that return errors or have moved, and cannot find a working link that leads to the wrong content. An accessibility scan finds missing alt attributes, weak contrast, and missing labels, and cannot find whether alt text is useful or captions are accurate. License detection finds missing, mismatched, or unrecognized license statements, and cannot find whether the license claim is true. A readability scan gives a reading level for each passage and cannot find undefined terms, dense ideas, or audience fit. A footer reminds the reader to keep a human in the loop.

**Why it is useful.** Teachers over-trust a clean scan, and "the scan passed" does not mean "the resource is accessible". Pairing what each tool finds with what it misses is the lesson, and it motivates the human check that Chapter 14 formalizes. The Automated Check Matcher practices the matching.

**Tips for a high-quality infographic.**

- Give the "cannot find" half the same visual weight as the "finds" half. Making blind spots small is the usual mistake. Shade it and give it a dotted outline.
- Draw a beam of light for each tool that lights some items and leaves others dark.
- Use four identical zone layouts, each with a simple icon (chain link, access symbol, copyright mark, ruler).
- Keep the chapter's wording, and show only status codes that the book already uses.

## Safe to Send? Student Data and AI Services

**Chapter:** 13 · **Overlay:** Grid, 3 zones · **Slug:** `safe-to-send`

**Description.** Three chutes: send it, fix it first, and never send it. In the first go the published text of an open textbook chapter and a rubric prompt template. In the second goes a class's quiz scores with student names, because names make the scores personal data, so they must be anonymized or approved first. In the third go a spreadsheet of grades with student ID numbers, a student's photograph, and an email thread with a parent about a student. A footer carries the chapter's warning that once text is sent to an AI service you cannot pull it back, and names FERPA.

**Why it is useful.** A privacy mistake cannot be undone, and a teacher new to AI may paste a gradebook without thinking. The chapter has a ten-item sorter, and the poster becomes the rule posted beside the desk and on the wall of a workshop. It also supports the student-privacy rules for A/B tests in Chapter 16.

**Tips for a high-quality infographic.**

- Use traffic-light logic, but add icons and shapes (a check in a circle, a wrench in a triangle, a stop in an octagon) so it works in grayscale and for color-blind readers.
- Use only the chapter's items. Do not add legal advice, and keep "if you are not sure, ask before you send".
- Show the amber item with a visible "name" badge so the reason is obvious.
- Use a silhouette in place of any student photograph.

## Four Ways an Agent Gets It Wrong

**Chapter:** 14 · **Overlay:** Grid, 4 zones · **Slug:** `four-agent-error-types`

**Description.** Four specimen cards, one for each agent error type in the chapter. A factual error is a wrong claim about the resource, such as a feature that is absent; the reviewer opens the resource and checks. A license error is a wrong reading of the license; the reviewer compares the claim with the statement itself. A citation error is a reference that does not exist or does not support its claim; the reviewer looks up the source and reads the passage. A scoring error is a score that does not follow from the agent's own checks; the reviewer recounts the passes and recomputes the band and total. Each card also names the typical fix in the prompt. An inset shows the chapter's "A 9 that should be a 5": the agent reported a 9, and its evidence supports five passing checks.

**Why it is useful.** Classifying errors by type is a stated course outcome, and the type tells the reviewer how to catch the error and the prompt writer how to prevent it. A field-guide poster is a handy reference for the review desk and for the findings log. The planned Agent Error Type Sorter practices the classification.

**Tips for a high-quality infographic.**

- Put the false claim and the check that exposes it side by side on each card. The catch is the takeaway.
- Keep the four cards structurally identical: what it looks like, how to catch it, how to prevent it.
- Use a gently skeptical tone, in the spirit of Echo, and not a mocking one. Keep the mascot itself on the lesson page.
- Label the examples as invented, and do not print real journal or author names.

## Agreement Is Not Skill

**Chapter:** 14 · **Overlay:** Grid, 3 zones · **Slug:** `agreement-is-not-skill`

**Description.** The chapter's worked example as three panels. The first shows the count table for 20 resources: agent and human both say ready for 1, both say not ready for 17, and they disagree on 2 (one each way), so they agree on 18 of 20 (0.90). The second shows a stacked bar of chance agreement: 0.01 from both saying ready plus 0.81 from both saying not ready, which is 0.82, so most of the 90 percent is expected by luck. The third shows kappa as (0.90 − 0.82) / (1 − 0.82), which is 0.44. A line under the panels says the agent found only one of the two resources the human judged ready.

**Why it is useful.** This is the most counterintuitive statistic in the book, and teachers often report only the agreement rate. Seeing the chance baseline as a filled bucket makes the point without algebra. The chapter's advice to always show the count table beside kappa is built into the layout. The Inter-Rater Agreement Explorer and the planned Kappa Calculator practice the arithmetic.

**Tips for a high-quality infographic.**

- Draw the bars and table in code with exact proportions, and use the chapter's numbers (0.90, 0.82, 0.44) verbatim.
- Print the kappa formula once, in large type.
- Print the labels for kappa ranges as rules of thumb only. The chapter says to check the cutoffs against the source before quoting them, so leave numeric cutoffs off the poster.
- Highlight the diagonal of the count table so the 18 agreements are visible, and the single missed "ready" resource stands out.

## The Fix Toolkit

**Chapter:** 15 · **Overlay:** Callout, 13 markers · **Slug:** `fix-toolkit`

**Description.** A pegboard of tools, one for each of the chapter's thirteen fixes, hung in panels by the metric each mainly raises. Accessibility has AI alt text generation, caption generation, and heading repair. Readability has reading level rewrite and glossary generation. Accuracy and currency has link repair and content update. Metadata has metadata generation, open license has license statement repair, modularity has chapter splitting, editable source has PDF-to-Markdown conversion, and practice with feedback has practice question generation and MicroSim building. Each marker's panel shows the chapter's typical agent mistake and the human check, such as "an invented address; open every new link".

**Why it is useful.** Thirteen fixes in a table are hard to keep in mind, and the improvement plan starts from the lowest metric and asks which fix applies. The poster is a lookup from metric to fix, and every marker carries the reminder that nothing is applied without human review. The planned Fix and Metric Matcher practices the mapping.

**Tips for a high-quality infographic.**

- Group tools into eight panels using each metric's fixed color, and keep the tools in the chapter's order so marker numbers match the table.
- Keep the artwork free of text and let the overlay supply the tool names. Thirteen markers are near the readable limit, so leave generous spacing.
- Add a small "check by a person" icon to every tool.
- Draw tools that look like tools (a magnifier, a scissors, a wrench) and avoid anything that suggests the fix is automatic.

## Can I Publish My Improved Version?

**Chapter:** 15, building on 2 · **Overlay:** Grid, 6 zones plus a footer band · **Slug:** `can-i-publish-my-improved-version`

**Description.** A traffic-light card for each license, answering the one question the chapter's table answers: may you publish an improved version, and what must you do? CC0 is yes, with nothing required. CC BY is yes, with credit, a link to the license, and a note that you changed it. CC BY-SA is yes, under CC BY-SA. CC BY-NC is yes without commercial use. CC BY-NC-SA is yes without commercial use, under CC BY-NC-SA. CC BY-ND is no, since changes are for your own private use only. A footer band covers the seventh row of the table: no license means all rights reserved, so ask the owner first.

**Why it is useful.** An agent's edited copy is a derivative work, so the license must be read before the first edit. The chapter's warning says so. This poster answers a practical question for each license, which the Six Creative Commons Licenses Poster does not. It saves effort by stopping work on a resource that cannot be legally shared once improved. The planned Derivative Permission Checker practices the decision.

**Tips for a high-quality infographic.**

- Give every card the same rows: license badge, verdict, duties. Order the cards from most to least permissive, as the chapter does.
- Use the official Creative Commons icons and follow Creative Commons' guidance on using its marks. Do not redraw them.
- Use three verdict states (yes, yes with conditions, no) with icons as well as color.
- The chapter's table omits CC BY-NC-ND. Decide whether to add that row to the chapter or to the poster, so the two always agree.

## The A/B Test on One Page

**Chapter:** 16 · **Overlay:** Callout, 7 markers · **Slug:** `ab-test-on-one-page`

**Description.** A left-to-right flow of the whole design. A pool of students is randomly assigned to two groups. The control group uses the original version (v1, rubric total 65, Revise) and the treatment group uses the improved version (v1.1, total 78, Adopt). Both take the same pre-test before and the same post-test after, and the comparison is the learning gain. The seven markers are the hypothesis, random assignment, the control group (which receives ordinary teaching with the original, not no teaching), the treatment group, the pre-test, the post-test and gain, and consent and privacy. A time strip along the bottom follows Chapter 17's schedule: pre-test and assignment in week 1, use of the assigned version in weeks 2 and 3, and post-test and survey in week 4.

**Why it is useful.** The A/B test is the book's main method for checking whether an improvement helped, and its seven concepts are introduced in separate sections. The chapter has a section called "The Design on One Page", which a poster can show better than a table. A teacher can use it when drafting a test plan, and a reviewer can use it to check one. The planned A/B Test Anatomy and Test Plan Reviewer practice the same ground.

**Tips for a high-quality infographic.**

- Make the two groups mirror images, so the only visible difference is the version label. This makes the chapter's one-difference rule visible.
- Show random assignment as shuffled tokens, never as a teacher picking volunteers.
- Use plain student silhouettes with no identifying features, and show varied students.
- Keep the artwork free of text and let the overlay supply the labels, so the numbers 65 and 78 can follow the chapter if it changes.

## Five Ways a Test Can Lie to You

**Chapter:** 16 · **Overlay:** Grid, 5 zones · **Slug:** `five-confounders`

**Description.** Five paired panels, one per confounder in the chapter's table, each showing how it misleads and the defense. Different teachers: one teacher's enthusiasm lifts one group, so use one teacher for both. Different times of day: students are more alert at one time, so run both groups at the same time. Extra help: one group gets a review or hints, so use the same script and help. Different tests: the versions are measured in different ways, so use the same test and key. Student choice: motivated students pick one version, so assign at random. Each panel is a balance scale, tilted by a hidden weight in the problem half and level in the defense half.

**Why it is useful.** Small classroom tests fail on confounds far more often than on statistics. The poster is a pre-flight checklist for a test plan, and it shares the chapter's habit of asking what else is different. The Confounder Finder and Sampling Bias Spotter practice finding them.

**Tips for a high-quality infographic.**

- Draw each panel as a before and after pair: a tilted scale for the problem, a level scale for the defense.
- Follow the chapter's order, and keep the defense wording close to the chapter's.
- Give each confounder one simple icon from its own noun (a teacher, a clock, a helping hand, a test sheet, a raised hand).
- Keep the weights neutral, since the confounder is hidden and not villainous.

## Reading an Effect Size

**Chapter:** 17 · **Overlay:** Grid, 3 zones · **Slug:** `reading-an-effect-size`

**Description.** Three pairs of overlapping bell curves, one pair per rule-of-thumb size: d of 0.2 (small), 0.5 (medium), and 0.8 (large). In each pair the control group is one curve and the treatment group the other, with the two means marked and the overlap shaded. The more the curves separate, the larger d. Under the curves is the formula, d = (mean of treatment − mean of control) / pooled standard deviation. A caution strip carries the chapter's pilot, where a difference of 7.0 over a pooled standard deviation of about 6.78 gives d of about 1.03, with the warning that a big number from a small test (12 students per group) deserves a second look.

**Why it is useful.** Effect size is the hardest idea in the second half of the book for readers without statistics, and the course description limits statistics to basic comparisons of two groups. Overlapping curves give the intuition without algebra, and they show why the same difference means different things for different spreads. The Effect Size Explorer practices the calculation.

**Tips for a high-quality infographic.**

- Generate the curves from the normal density in code, with identical axes in all three panels. A generated image cannot be trusted to get the overlap right.
- Draw control in gray and treatment in the accent color, and shade the overlap with a pattern so it survives grayscale.
- Mark sizes as rules of thumb, and repeat the chapter's note that what counts as important depends on the cost of the change and the setting.
- If there is room, add a fourth zone showing the same difference with a wider spread, which targets the chapter's misconception that a bigger difference always means a bigger effect.

## Component in a Box

**Chapter:** 18 · **Overlay:** Callout, 7 markers · **Slug:** `component-in-a-box`

**Description.** An exploded-view drawing of a cardboard box labeled with a generic folder name, with the six parts of the chapter's quiz package floating above it: the page itself (`index.html`), the script it needs kept inside the folder (`quiz.js`), a README that says what the component is and how to use it, a license file, a metadata file, and an image folder. The box lid reads "everything it needs travels with it". Outside the box a dotted line runs from the page to a folder elsewhere, with a cross on it, showing the broken link that packaging prevents. A seventh marker sits on the three finished boxes of *Watershed Basics v1.1* (the reading, the quiz, and the simulation).

**Why it is useful.** Chapter 18 turns improved resources into reusable components, and packaging is the concrete step that makes the lift-out test from Chapter 9 and the portability checks from Chapter 10 pass. The poster ties together license, metadata, and portability in one image. The planned Component Package Inspector practices the inspection.

**Tips for a high-quality infographic.**

- Use an exploded view with six clearly different icons (page, script, readme, license, tag, picture folder).
- Print real file names in monospace, or add them through the overlay. Keep them consistent with the chapter's listing.
- Show the broken link as the failure mode, because the chapter's rule is that links must be complete addresses or point inside the package.
- Mention in the lesson page how this book's own MicroSim folders correspond to the example, so the poster does not seem to contradict them.

## A One-Day Workshop Timeline

**Chapter:** 19 · **Overlay:** Callout, 8 markers · **Slug:** `one-day-workshop-timeline`

**Description.** A horizontal timeline from 8:30 to 3:30 built from the chapter's sample agenda. The blocks are check-in and setup, the ten metrics, calibration by hand and then with the agent, checking the agent, lunch, the improvement challenge, peer review and publishing, and next steps. Under each block sits a token for what teachers leave with: a working agent session, a rubric card, hand and agent scores with gaps explained, a verified evaluation, an improved component with its new score, a published openly licensed component, and a certificate checklist. Arcs above the timeline show why the order matters, such as the rubric before calibration and checking before improving.

**Why it is useful.** A facilitator can print it for the room, and participants can see the logic of the day and what they will carry out of it. It makes the chapter's reasoning about order visible. It pairs with the Sample One-Day Schedule workshop page. The Workshop Agenda Sorter practices the ordering.

**Tips for a high-quality infographic.**

- Draw block widths in proportion to time, so the long improvement challenge looks long and the breaks look short.
- Make the "leave with" tokens the visual rhythm of the poster.
- Keep the times in the overlay data and not in the artwork, so a facilitator can adapt the agenda without redrawing.
- Label only the arcs that carry a reason from the chapter, and leave out the others.

## Four Levels of Training Evaluation

**Chapter:** 19 · **Overlay:** Grid, 4 zones · **Slug:** `four-levels-of-training-evaluation`

**Description.** A four-step staircase using the model of Donald Kirkpatrick that the chapter names: reaction, learning, behavior, and results. Each step asks its question and shows the chapter's illustrative evidence for a workshop of 20 teachers. For reaction, 19 of 20 returned the exit survey and 18 rated the day 4 or 5. For learning, 17 of 20 earned the certificate and their calibration scores differed from consensus by 1.1 points on average. For behavior, 12 of the 17 certified teachers scored another resource within three months. For results, 20 improved components were published and 9 were reused by another teacher within three months. An arrow beneath shows that later levels take longer to collect.

**Why it is useful.** Most workshops stop at a happy survey, which the chapter points out measures only the first level. The staircase shows what stronger evidence would look like, and it carries the cautions of Chapters 16 and 17 about causes and comparison groups. It is also a ready frame for a grant report, alongside the Grant Response and Grant-Period Timeline workshop pages. The Training Evaluation Matcher practices placing evidence.

**Tips for a high-quality infographic.**

- Mark every number "illustrative" in plain sight. The chapter says they are made up to show the form, and the poster must not look like a real result.
- Make the question the headline of each step and the evidence a smaller caption.
- Keep the numbers in a data file so a real workshop can replace them with its own.
- Add the chapter's reminder that counts of reuse are weaker evidence than learning.
