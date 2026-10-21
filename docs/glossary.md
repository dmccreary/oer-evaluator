# Glossary of Terms

#### A/B Test

A controlled classroom experiment in which learners are assigned to two groups—one studying with the original version of an educational resource (Control Group) and the other studying with the revised version (Treatment Group)—to measure whether the revision improves student learning or engagement outcomes.

Running an empirical trial with real students tests whether raising a resource's rubric score with AI agents actually translates into better human learning.

**Example:** To test whether adding an interactive MicroSim and self-check questions to Chapter 3 helps students master license compatibility, an instructor assigns half the class the original text and half the enhanced module, then compares their post-test scores.

See also: Control Group, Treatment Group, Rubric-Outcome Correlation.

#### Accept Correct or Reject

The three-action triage decision that a human reviewer applies to each individual metric score, evidence citation, or suggested edit produced by an AI agent: approve it as accurate (Accept), modify the score or text to fix a partial flaw (Correct), or discard a hallucinated or invalid finding (Reject).

Walking through an agent's evaluation report item by item with this three-choice protocol keeps the human educator firmly in control while saving hours of drafting time.

**Example:** Reviewing an agent's ten metric scores, the teacher **Accepts** seven well-supported scores, **Corrects** the Readability score from 8 to 6 after noting undefined jargon, and **Rejects** a hallucinated claim about a broken link that actually works.

See also: Human in the Loop, Findings Log, Agent Evaluation Report.

#### Accessibility

The inclusive design of educational materials, interfaces, and media so that people with disabilities can perceive, understand, navigate, and interact with them independently and effectively.

In OER evaluation, inclusive design is treated as a core component of instructional quality rather than an optional technical afterthought.

**Example:** Providing text alternatives for diagrams, captions for audio, and full keyboard control ensures that blind, deaf, and motor-impaired students can use the same open textbook as their peers.

See also: Accessibility Metric, Universal Design for Learning, WCAG.

#### Accessibility Checker

A software tool or browser extension—such as WAVE, axe DevTools, or Lighthouse—that inspects webpages or documents against WCAG rules to flag detectable issues like missing alt text, low contrast, and skipped headings.

Automated checkers speed up OER evaluation by catching common technical violations instantly, though a human reviewer still verifies whether alt text and captions are actually meaningful.

**Example:** Running the WAVE browser extension on an open textbook chapter immediately highlights four images lacking `alt` attributes and two subheadings with insufficient color contrast.

See also: Automated Accessibility Scan, WCAG 2.1 AA, Accessibility Metric.

#### Accessibility Metric

The fourth quality metric in the ten-metric rubric, which evaluates whether a resource meets WCAG 2.1 AA standards so learners with visual, auditory, motor, or cognitive disabilities can perceive, navigate, and interact with all content.

Because public schools and colleges have legal and ethical obligations to serve all students equitably, low accessibility scores require repair before classroom adoption.

See also: Accessibility, WCAG 2.1 AA, Automated Accessibility Scan.

#### Accessible Math

The representation of equations and scientific notation using semantic markup such as MathML or screen-reader-compatible MathJax/KaTeX rendering rather than flat, unsearchable raster images of formulas.

Semantic math markup allows screen readers to speak equations accurately (e.g., "the fraction a plus b over c") and lets low-vision users zoom in without pixelation.

**Example:** Writing the mean absolute difference formula in LaTeX rendered by MathJax with assistive MathML enabled lets a blind statistics student navigate inside the numerator and denominator term by term.

See also: Alt Text, Screen Reader, Accessibility Metric.

#### Accuracy Metric

The half of the first quality metric in the ten-metric rubric that evaluates whether a resource's facts, formulas, definitions, code, and explanations are correct, verifiable, and supported by credible citations.

Because factual errors directly mislead learners, any significant inaccuracies sharply cap the score on this criterion.

See also: Currency Metric, Factual Error, Fact Checking.

#### Adopt Revise or Reject

The three-tier decision framework used at the conclusion of an OER evaluation to classify a resource as ready for immediate classroom use (Adopt), suitable after targeted improvements (Revise), or too flawed or legally restricted to use (Reject).

Framing the evaluation around these three concrete actions ensures that every rubric review leads directly to a practical next step.

**Example:** A resource scoring 88/100 with a CC BY license is marked **Adopt**; a resource scoring 68/100 with missing alt text and weak quizzes is marked **Revise**; an inaccurate book under CC BY-NC-ND is marked **Reject**.

See also: Adoption Decision, Score Band, Improvement Plan.

#### Adoption Decision

The formal institutional or instructor determination of whether to select a candidate open educational resource for a course, either as-is or following planned adaptations.

Anchoring this determination in documented rubric scores and cited evidence protects academic quality and makes the choice transparent to colleagues and administrators.

See also: Adopt Revise or Reject, Adoption Recommendation, OER Adoption.

#### Adoption Recommendation

A written justification included at the end of a review report that advises a teacher, curriculum committee, or department chair to adopt, revise, or reject a resource, supported by specific rubric subtotals and evidence.

When presenting an open textbook proposal to a school board or department, a structured evidence-based justification is far more persuasive than informal praise.

**Example:** The review report concludes: "Recommend **Adopt after Minor Revision**: Quality Subtotal is 43/50, and the single weak metric (Accessibility: 5/10 due to 19 missing alt texts) can be repaired with an AI agent in under two hours."

See also: Review Report, Adopt Revise or Reject, Adoption Decision.

#### Adoption Threshold

The minimum total score and individual metric floor that an institution or department establishes as a prerequisite before approving an open educational resource for classroom use.

Setting minimum floors on critical metrics like accuracy, open licensing, and accessibility prevents a high total score from masking a fatal defect.

See also: Score Band, Adoption Decision, Adopt Revise or Reject.

#### Agent Disagreement

A discrepancy that occurs when two independent AI agents—or an AI agent and a human reviewer—assign substantially different scores or conflicting evidence assessments to the same rubric metric on the same resource.

Significant divergence between raters serves as an automatic warning flag that either the resource has an ambiguous edge case or one of the raters made an error.

See also: Score Difference Threshold, Score Reconciliation, Multi-Agent Review.

#### Agent Error Rate

The percentage or proportion of an AI agent's evaluation findings, citations, or metric scores that are found to be factually incorrect, hallucinated, or out of tolerance when audited against human verification.

Tracking this metric over time quantifies whether prompt refinements and tool integrations are genuinely making the automated evaluator more trustworthy.

**Example:** If an AI agent produces 50 evidence citations across a ten-metric report and source verification reveals that 3 of those citations point to nonexistent passages, its citation error rate is 6%.

See also: Findings Log, Agreement Rate, Prompt Refinement.

#### Agent Error Type

A diagnostic category used to classify mistakes found in an AI agent's evaluation report—specifically factual errors, license misreadings, invented or inaccurate citations, and scoring errors (such as inflation or misapplied descriptors).

Sorting agent mistakes into clear categories helps prompt engineers target the exact weakness in their rubric instructions or tool pipeline.

See also: Hallucination, Invented Citation, License Misreading, Overconfident Score.

#### Agent Evaluation Report

The structured document generated by an AI agent after auditing an educational resource, containing the ten metric scores, quality and reusability subtotals, total score, verbatim evidence citations, and prioritized improvement suggestions.

Reviewers treat this generated document as a draft worksheet to be audited and annotated using the Accept, Correct, or Reject workflow.

**Example:** After analyzing `docs/chapters/04-cells/index.md`, the agent outputs a Markdown report scoring the chapter at 71/100 and listing the exact line numbers of six broken links and eleven missing image descriptions.

See also: Review Report, Agent Scoring, Accept Correct or Reject.

#### Agent Scoring

The automated process in which an AI agent inspects an open educational resource against a rubric prompt and assigns numeric 0–10 point values and evidence citations to each metric.

While an agent can complete a first-pass evaluation of a chapter in under two minutes, its scores remain provisional hypotheses until a human reviewer verifies the cited evidence.

**Example:** An educator runs an evaluation agent on a candidate algebra textbook to generate initial ten-metric ratings and pinpoint the three weakest chapters before conducting a focused human review.

See also: Rubric Prompt, Agent Evaluation Report, Human in the Loop.

Contrast with: Manual Evaluation.

#### Agent Skill

A reusable, modular package of instructions, system prompts, rubric descriptors, output schemas, and helper scripts that teaches an AI agent how to perform a specialized domain task reliably.

Packaging the OER evaluation methodology as a shareable skill allows any educator to run consistent, high-quality rubric assessments with a single command.

**Example:** A folder containing a `SKILL.md` instruction file, the ten-metric scoring descriptors, and a Python link-checker script equips an agent to audit any Markdown textbook automatically.

See also: AI Agent, Rubric Prompt, Agent Workflow.

#### Agent Workflow

A structured, multi-step pipeline in which one or more AI agents combine deterministic scripts, rubric scoring prompts, verification passes, and file operations to evaluate or improve an educational resource from start to finish.

Breaking a complex evaluation into distinct stages—scan, score, verify citations, and format report—produces far higher reliability than a single monolithic prompt.

See also: Review Workflow, Multi-Agent Review, Human in the Loop.

#### Agreement Rate

The simple percentage of rubric metrics or evaluation items on which two raters—such as a human educator and an AI agent—assign the exact same score or scores within a pre-specified tolerance (for example, within 1 point on a 10-point scale).

While easy to calculate and explain to faculty colleagues, simple percentage concordance is often paired with Cohen's kappa or mean absolute difference for a complete reliability picture.

**Example:** Across ten rubric metrics on a chapter, if the teacher and the AI agent assign scores within 1 point of each other on eight of the ten metrics, their within-one-point agreement rate is 80%.

See also: Inter-Rater Agreement, Score Difference Threshold, Cohen's Kappa.

#### AI Agent

A software system built around a large language model that can autonomously pursue a defined goal by planning steps, reading files, invoking external tools or scripts, and producing structured outputs.

Unlike a passive chat window where a user must copy and paste text one paragraph at a time, an agent can inspect an entire textbook repository, run link and accessibility scripts, and compile a complete rubric report.

**Example:** Directed by an evaluation skill, a coding agent reads all twelve chapter files in `docs/chapters/`, executes a Python readability script, scores all ten rubric metrics with line-number citations, and saves the report to disk.

See also: Agent Skill, Tool Use, Agent Workflow.

#### AI Alt Text Generation

The use of a multimodal vision-language model or AI agent to inspect figures, photographs, and diagrams in an educational resource and draft concise, context-appropriate `alt` text descriptions for human review.

Because hundreds of existing OER textbooks lack image descriptions, vision-assisted drafting can turn a week-long manual accessibility backlog into a one-hour review session.

See also: Alt Text, Accessibility Metric, Human Review of Changes.

#### AI Assistant

An interactive conversational software application powered by a large language model that responds to user prompts by generating text, answering questions, analyzing documents, or writing code.

While a basic chat interface can help brainstorm examples or summarize a passage, structured OER evaluation benefits from moving beyond ad-hoc chatting to repeatable prompts and agent skills.

**Example:** A teacher pastes a textbook paragraph into a conversational web chat and asks it to suggest a simpler eighth-grade rewrite for struggling readers.

See also: Large Language Model, AI Agent, Prompt.

#### AI Cost

The monetary expense and computational resource consumption—typically billed per million input and output tokens—incurred when running large language models and AI agents to evaluate or improve educational materials.

Designing token-efficient workflows (such as using deterministic scripts for counting and sorting, and avoiding redundant parallel agent overhead) keeps AI evaluation affordable for teachers on tight budgets.

**Example:** Evaluating a 4,000-word chapter with a single well-designed agent call consumes roughly 6,000 total tokens—costing just a few cents—whereas an inefficient multi-agent loop can waste ten times as much budget.

See also: Token, Context Window, Batch Evaluation.

#### Alignment Metric

The second quality metric in the ten-metric rubric, which evaluates whether a resource provides clear, measurable learning outcomes and whether its instructional content and assessments directly match those outcomes and target standards.

Even accurate, readable prose fails as a course material if it teaches topics unrelated to the course objectives or tests skills it never explained.

**Example:** A chapter that begins with five Bloom-aligned learning objectives, teaches each objective in a dedicated section, and tests all five in the end-of-chapter quiz earns a 10 on this metric.

See also: Learning Outcome, Assessment Alignment, Outcome Coverage.

#### All Rights Reserved

The default legal status under copyright law in which the creator retains every exclusive right provided by statute and grants no advance permissions for others to copy, adapt, or distribute the work.

Even when a webpage has no copyright symbol or notice at the bottom, copyright law automatically applies this restrictive status by default.

**Example:** A teacher's personal website hosting worksheet PDFs with no license statement is legally protected as all rights reserved, meaning others cannot remix those worksheets without written permission.

See also: Copyright, Free Resource, Proprietary License.

Contrast with: Public Domain, Open License.

#### Alt Text

A concise written description embedded in the HTML `alt` attribute or Markdown image syntax that communicates the purpose and essential information of an image to screen reader users.

Adding accurate image descriptions is one of the highest-impact improvements an AI agent can perform on an existing open textbook.

**Example:** For a bar chart showing OER adoption growth, writing `![Bar chart showing faculty OER adoption rising from 18% in 2018 to 42% in 2024](chart.png)` gives non-visual readers the exact data takeaway.

See also: Decorative Image, Complex Image Description, AI Alt Text Generation.

#### Anonymized Data

Experimental or assessment records from which all direct and indirect personal identifiers—such as student names, email addresses, student ID numbers, and exact timestamps—have been permanently removed so no row can be traced back to an individual learner.

Once a dataset is fully de-identified, summary statistics and aggregate distributions can be safely analyzed with scripts and included in open evaluation reports.

**Example:** Replacing `"Maria Gonzalez (ID #904182)"` with `"Participant_014, Group: Treatment, Pre: 4, Post: 9, Gain: +5"` produces a de-identified row safe for statistical aggregation.

See also: Student Data Privacy, Student Privacy in Testing, Data Collection.

#### Answer Key

A reference guide or embedded data structure that identifies the correct response for every practice problem or quiz question in an educational resource.

Many open textbooks drop points on the Practice Metric because they include end-of-chapter questions but withhold the solutions, leaving self-learners unable to check their work.

**Example:** Providing a collapsible solutions block at the end of each problem set ensures students studying at home can verify whether their rubric subtotals are correct.

See also: Worked Solution, Feedback Message, Practice Metric.

#### ARIA Labels

Accessible Rich Internet Applications attributes—such as `aria-label`, `aria-labelledby`, and `aria-live`—added to HTML elements and interactive controls to supply accessible names, roles, and state updates to assistive technologies.

When building custom interactive quizzes or JavaScript MicroSims, ARIA attributes ensure screen readers can announce button functions and dynamic score changes.

**Example:** Adding `aria-label="Adjust sample size per group"` to a simulation slider ensures a screen reader user knows exactly what parameter the control modifies.

See also: Screen Reader, Keyboard Navigation, MicroSim.

#### Assessment Alignment

The degree of correspondence between a resource's stated learning outcomes and its quizzes, practice problems, and assignments in both topic coverage and cognitive level.

Students experience frustration and poor learning measurement when a textbook teaches conceptual analysis in the text but tests obscure trivia in the quiz.

**Example:** If a learning outcome asks learners to calculate Cohen's kappa for two reviewers, an aligned assessment item requires computing or interpreting that statistic rather than merely defining the term.

See also: Alignment Metric, Practice Metric, Learning Outcome.

#### Attribution Requirement

The legal condition present in all six standard Creative Commons licenses requiring reusers to give appropriate credit to the creator, provide a link to the license, and indicate if changes were made.

Educators who adapt or remix open textbooks fulfill this obligation by writing clear attribution statements for every source used.

**Example:** When an instructor includes an open diagram in a slide deck, including a caption with the creator's name, the source link, and "CC BY 4.0" satisfies this legal condition.

See also: Attribution Statement, TASL Attribution Format, CC BY.

#### Attribution Statement

A written credit line included with a reused or adapted open resource that identifies the original title, author, source URL, license name, and any modifications made.

Every improved OER published in this course includes complete credit notices to respect creator rights and comply with open license terms.

**Example:** "Adapted from 'Introduction to Sociology 3e' by OpenStax, available at https://openstax.org, licensed under CC BY 4.0; reading level simplified and five quiz items added by Dan McCreary."

See also: TASL Attribution Format, Attribution Requirement, Derivative Work.

#### Audience Fit

The alignment between a resource's reading level, tone, examples, cultural references, and prerequisite assumptions and the actual characteristics of the intended learners.

A resource can be well-written in the abstract yet score poorly on readability if its examples and complexity target the wrong educational tier.

**Example:** An open statistics module that illustrates probability using graduate-level quantum mechanics equations has poor fit for an introductory community college business course.

See also: Readability Metric, Reading Level, Prerequisite Knowledge.

#### Audio Description

A narrated audio track or spoken commentary added to a video that describes important visual details—such as on-screen diagrams, facial expressions, or laboratory actions—that cannot be understood from the main soundtrack alone.

When a video instructor points silently to parts of a graph saying "look at how this curve drops here," blind learners depend on spoken visual narration to understand the lesson.

**Example:** During a pause in a chemistry lab video, a secondary narration track announces, "The clear solution in Beaker B turns bright magenta after three drops of indicator are added."

See also: Captions, Transcript, Accessibility Metric.

#### Author Field

The metadata element that identifies the person, team, or organization primarily responsible for creating or adapting the intellectual content of an educational resource.

Recording creator names accurately in the metadata record enables automated tools and downstream educators to generate proper legal attribution statements.

**Example:** Listing `authors: ["Elena Rostova", "Marcus Vance"]` in the textbook's metadata configuration credits both co-authors and populates the citation block automatically.

See also: Metadata Record, TASL Attribution Format, Attribution Requirement.

#### Automated Accessibility Scan

A programmatic audit using tools such as axe-core, Pa11y, Lighthouse, or custom HTML/Markdown parsers to detect technical WCAG violations including missing image alt attributes, skipped heading levels, empty links, and low color contrast.

While automated scans catch roughly 40 to 50 percent of WCAG issues instantly and reproducibly, human review is still required to judge whether alt text and captions are actually accurate.

**Example:** An automated pre-check script scans a chapter's compiled HTML and reports zero missing `alt` attributes, one `H1`-to-`H3` heading skip on line 92, and two buttons lacking ARIA labels.

See also: Accessibility Checker, Accessibility Metric, WCAG 2.1 AA.

#### Automated License Detection

The programmatic inspection of a resource's frontmatter, HTML meta tags, Schema.org JSON-LD blocks, and footer text using pattern matching or AI parsing to identify declared open licenses and flag missing or conflicting notices.

Automated license scripts quickly surface whether a repository declares a machine-readable Creative Commons license or contains uncredited third-party media files.

See also: Open License Metric, License Field, Machine-Readable Metadata.

#### Automated Link Checker

A deterministic software script or command-line utility that extracts all hyperlinks from a resource's source files, sends HTTP requests to each URL, and reports broken links, timeouts, or redirects.

Running an automated link scan gives reviewers objective, reproducible data for scoring the Currency Metric and building a link repair list.

**Example:** A Python script parses all `.md` files in `docs/chapters/`, tests 142 external URLs via `HEAD` and `GET` requests, and outputs a CSV listing four dead `404` links and two expired domains.

See also: Broken Link Check, Link Rot, Link Repair.

#### Automated Readability Scan

A software script that strips markup formatting from a chapter's prose, counts sentences, words, and syllables, and computes standardized readability indices such as the Flesch-Kincaid Grade Level.

Feeding exact, script-computed grade-level numbers into an evaluation report prevents an LLM from guessing readability scores impressionistically.

**Example:** A Python script runs across all twelve chapters of an open biology textbook and outputs a summary table showing that Chapter 7 spikes to a 13.8 Flesch-Kincaid grade level while all other chapters average 9.4.

See also: Readability Formula, Flesch-Kincaid Grade Level, Readability Metric.

#### Batch Evaluation

The automated execution of an AI evaluation workflow across multiple chapters, modules, or candidate textbooks in a systematic sequence, producing a comparable set of rubric scores and summary metrics for the entire collection.

Batch processing makes it feasible for a librarian or department coordinator to screen twenty-five chapters of a textbook or ten competing repositories in a single afternoon.

**Example:** A script iterates over all fifteen chapter directories in an open chemistry textbook, running the evaluation agent on each chapter and compiling a master heatmap table of all 150 metric scores.

See also: Agent Workflow, JSON Output, AI Cost.

#### Before-and-After Comparison

A side-by-side tabular and visual analysis presenting a resource's original metric scores, subtotals, and concrete defects alongside its post-improvement scores, resolved evidence, and net score gains.

Documenting the baseline and improved states clearly communicates the value of AI-assisted OER stewardship to colleagues, administrators, and repository users.

See also: Score Gain, Re-Scoring, Original Version, Improved Version.

#### Bloom Cognitive Levels

The six ordered tiers of thinking complexity in the revised Bloom's Taxonomy—Remember, Understand, Apply, Analyze, Evaluate, and Create—used to categorize learning outcomes and assessment items.

Matching the cognitive tier of a practice question to the cognitive tier of its corresponding learning outcome is a core check under the Alignment and Practice metrics.

**Example:** Asking a student to list the 5R permissions operates at the Remember tier, whereas asking the student to critique an AI agent's rubric report operates at the Evaluate tier.

See also: Bloom's Taxonomy, Learning Outcome, Assessment Alignment.

#### Bloom's Taxonomy

A hierarchical classification framework of educational learning objectives organized into six cognitive process levels: Remember, Understand, Apply, Analyze, Evaluate, and Create.

The OER Evaluator rubric uses this framework to check whether a resource progresses beyond rote memorization to higher-order thinking and aligned practice.

See also: Bloom Cognitive Levels, Measurable Verb, Question Difficulty.

#### Broken Link Check

The inspection of all internal and external hyperlinks in an educational resource to identify URLs that fail to resolve, return error status codes, or redirect to irrelevant pages.

Reviewers run link inspections as a standard step when scoring the Currency Metric and preparing an improvement plan.

**Example:** Testing all 45 URLs in a chapter reveals three dead external links and one broken internal anchor to a missing glossary entry.

See also: Link Rot, Automated Link Checker, Link Repair.

#### Browser Compatibility

The ability of a web-based educational resource and its interactive components to render accurately and function without errors across all major modern web browsers, including Chrome, Firefox, Safari, and Edge.

Using standard HTML5, CSS, and well-supported JavaScript libraries like p5.js ensures that students on Chromebooks, Macs, iPads, and Windows PCs have an identical learning experience.

**Example:** Testing a newly built MicroSim on desktop Chrome, macOS Safari, and mobile Firefox confirms that its control sliders and canvas resize properly on every student device.

See also: Portability Metric, Responsive Layout, HTML.

#### Calibration Against Humans

The empirical process of running an AI evaluation agent on a benchmark set of resources that have already been scored by consensus human reviewers, comparing the resulting ratings, and adjusting the agent's prompts and tools until its scores align closely with human judgment.

Human expert consensus serves as the anchor that keeps automated rubric evaluation grounded in real classroom expectations.

**Example:** An instructional design team scores five diverse OER chapters by hand, runs their rubric skill on the same five chapters, and refines the prompt descriptors until the mean absolute difference drops below 1.2 points per metric.

See also: Consensus Scoring, Prompt Refinement, Mean Absolute Difference.

#### Calibration Exercise

A hands-on training activity during a workshop in which all participants independently score the exact same short sample OER passage using the rubric, compare their ratings on a shared display, and examine the text evidence together to align their scoring standards.

Working through a concrete passage with deliberate flaws builds shared understanding of the 0–10 descriptors far faster than reading rubric rules passively.

**Example:** Workshop participants spend fifteen minutes scoring a two-page sample chapter that looks polished at first glance but hides a CC BY-NC-ND license in the footer and skips from `H1` to `H4` headings.

See also: Calibration Session, Consensus Scoring, Teacher Training Workshop.

#### Calibration Session

A structured meeting in which two or more reviewers independently score the same sample resource using the rubric, compare their metric-by-metric ratings, and discuss discrepancies to align their interpretation of the scoring descriptors.

Holding a group alignment exercise before a large textbook review project reduces reviewer bias and dramatically increases inter-rater agreement.

**Example:** Five science teachers independently score the same open ecology chapter, project their ten metric scores side by side on a screen, and resolve why their Practice Metric ratings ranged from 4 to 8.

See also: Consensus Scoring, Inter-Rater Agreement, Calibration Exercise.

#### Capstone Project

The culminating synthesis assignment of the course in which a learner evaluates a subject-area OER on all ten metrics, uses AI agents to improve quality and reusability, tests the revision with students, and publishes the result under CC BY.

Completing this end-to-end project integrates every skill in the learning graph and produces a genuinely improved open resource for the global teaching commons.

See also: Certificate Requirements, Before-and-After Comparison, Publishing OER.

#### Caption Generation

The automated creation of time-synchronized text captions and transcripts for instructional videos and audio files using speech-to-text AI models, followed by human editing for technical terms and speaker punctuation.

Adding accurate synchronized text raises a video resource's Accessibility Metric score to WCAG 2.1 AA compliance while helping students in noisy or quiet study environments.

**Example:** Running an open-source speech recognition model on a twelve-minute lecture video produces a `.vtt` subtitle file in ninety seconds, after which the instructor fixes three misspelled chemical names.

See also: Captions, Transcript, Accessibility Metric.

#### Captions

Time-synchronized text displayed on screen during a video that transcribes spoken dialogue and identifies important non-speech sounds for deaf, hard-of-hearing, and non-native language learners.

Unlike a static document transcript, synchronized on-screen text lets viewers follow spoken explanations while simultaneously watching visual demonstrations in a video.

**Example:** An instructional screencast showing how to run an accessibility checker includes synchronized text at the bottom of the video player that matches the narrator's voice word for word.

See also: Transcript, Audio Description, Caption Generation.

#### CC BY

The Creative Commons Attribution license, which permits anyone to copy, redistribute, adapt, and build upon a work for any purpose, including commercially, provided appropriate credit is given to the creator.

Because it enables all five 5R permissions with minimal friction, this license earns the maximum score on the open license metric.

See also: Attribution Requirement, Creative Commons, Open License Metric.

Contrast with: CC BY-NC-ND.

#### CC BY-NC

The Creative Commons Attribution-NonCommercial license, which allows users to copy, adapt, and share a work with credit, provided the use is not primarily intended for commercial advantage or monetary compensation.

This license supports classroom adaptation and redistribution but prevents commercial publishers from selling the work for profit and limits remixing with CC BY-SA content.

**Example:** A university professor can customize a CC BY-NC lab manual and print copies at cost for students, but a for-profit tutoring company cannot sell the manual in a paid course package.

See also: NonCommercial Requirement, License Compatibility, Creative Commons.

#### CC BY-NC-ND

The Creative Commons Attribution-NonCommercial-NoDerivatives license, the most restrictive of the six main Creative Commons licenses, allowing only verbatim noncommercial sharing with credit and prohibiting any adaptations.

Materials carrying this license cannot be improved with AI agents and redistributed, making them unsuitable for OER adaptation workflows.

See also: NoDerivatives Requirement, NonCommercial Requirement, Open License Metric.

Contrast with: CC BY, CC0 Dedication.

#### CC BY-NC-SA

The Creative Commons Attribution-NonCommercial-ShareAlike license, which permits noncommercial copying and adaptation with credit, provided all derivative works carry the same noncommercial share-alike terms.

Although common in older educational repositories, this license creates remix restrictions because its derivatives cannot be combined with standard CC BY-SA works.

**Example:** An instructor who adapts a CC BY-NC-SA workbook by adding new exercises must publish the revised workbook under the identical CC BY-NC-SA license and prohibit commercial sales.

See also: NonCommercial Requirement, ShareAlike Requirement, License Conflict.

#### CC BY-ND

The Creative Commons Attribution-NoDerivatives license, which allows anyone to copy and redistribute a work in its exact, unedited form with credit, even commercially, but forbids distributing modified versions.

Because it prohibits revising and remixing, a resource under this license fails two of the 5R permissions and scores poorly on the open license metric.

**Example:** A teacher can distribute copies of a CC BY-ND article to students, but cannot legally publish a simplified reading-level rewrite or translate the text into another language.

See also: NoDerivatives Requirement, The 5R Permissions, Revise Permission.

#### CC BY-SA

The Creative Commons Attribution-ShareAlike license, which permits copying, adaptation, and commercial use as long as credit is given and any derivative work is released under the exact same or a compatible license.

While fully supporting the 5R permissions, the copyleft condition restricts which other licensed materials can be remixed with the work.

**Example:** Wikipedia articles use this license, meaning any textbook chapter that incorporates paragraphs from Wikipedia must also be shared under CC BY-SA.

See also: ShareAlike Requirement, License Compatibility, Creative Commons.

#### CC0 Dedication

A legal tool from Creative Commons that allows creators to waive all copyright and related rights in a work to the fullest extent permitted by law, placing it effectively into the worldwide public domain.

Resources dedicated under this waiver allow unrestricted reuse, adaptation, and integration without even requiring legal attribution, though academic citation remains good practice.

**Example:** A data science instructor releases a synthetic student grade dataset under CC0 so anyone can analyze, modify, and bundle the data into any resource without attribution friction.

See also: Public Domain, Creative Commons, Open License.

#### Certificate

A formal credential awarded to an educator, librarian, or instructional designer who successfully completes the course training and demonstrates competency in evaluating, improving, testing, and publishing an open educational resource with AI agents.

Earning a verified credential recognizes faculty expertise in OER quality stewardship and AI literacy for professional advancement or continuing education credit.

**Example:** Upon passing the capstone portfolio review, a high school science teacher receives a signed digital credential in *OER Quality Evaluation and AI-Assisted Improvement*.

See also: Certificate Requirements, Certificate Submission, Capstone Project.

#### Certificate Requirements

The explicit set of performance criteria and portfolio deliverables—such as a manual and AI evaluation report, a verified findings log, measurable score gains on at least two quality and two reusability metrics, an A/B test design or results summary, and a CC BY published module—needed to earn the course certificate.

Publishing transparent, measurable completion criteria ensures that every certified evaluator has demonstrated end-to-end practical mastery across all six Bloom taxonomy levels.

**Example:** To qualify for certification, a candidate's portfolio must show a verified score gain of at least +15 total points spread across at least two quality and two reusability metrics, with zero unresolved license or citation errors.

See also: Certificate, Certificate Submission, Capstone Project.

#### Certificate Submission

The compiled portfolio package—containing the original resource link, baseline and post-improvement rubric worksheets, AI agent findings log, git diff or repository link of the improved CC BY resource, and A/B test documentation—submitted by a candidate for credential evaluation.

Structuring the portfolio around reproducible links and verifiable evidence allows reviewers to audit the candidate's work efficiently.

**Example:** A candidate submits a single Markdown portfolio file linking to their public GitHub fork, the before-and-after rubric tables, the 10-item verification log, and the anonymized pre/post-test summary from their classroom trial.

See also: Certificate Requirements, Submission Review, Capstone Project.

#### Change Log Entry

A concise, dated record added to a resource's changelog or attribution block that specifies exactly who modified the resource, when the edits occurred, and which content, accessibility, or structural improvements were made.

Under Creative Commons licenses (beginning in version 4.0 and standard best practice across all versions), adapters must indicate that changes were made to the original work.

**Example:** Adding `"2026-04-15 (Prof. K. Lin): Simplified Section 2 reading level from Grade 13 to Grade 9, added alt text to Figures 1–8, and added a 10-question formative quiz"` satisfies legal and editorial transparency.

See also: Changelog, Attribution Statement, Derivative Work.

#### Changelog

A structured project file or repository section that lists notable additions, corrections, and structural modifications grouped chronologically by version release.

Maintaining an explicit log of changes fulfills the Creative Commons requirement to indicate modifications and helps adopting teachers see what improved after an AI enhancement pass.

See also: Change Log Entry, Revision History, Release Notes.

#### Chapter Splitting

The refactoring of an overly long, monolithic textbook chapter into two or more smaller, self-contained modular lessons—each with its own metadata header, learning objectives, summary, and practice quiz.

Breaking massive chapters into focused units directly raises the Modularity Metric and makes it easy for teachers to assign or reorder individual topics.

**Example:** An adapter splits a 16,000-word chapter covering all of cell biology into three standalone 4,500-word modules: *Cell Structure*, *Membrane Transport*, and *Cellular Respiration*, updating `mkdocs.yml` navigation accordingly.

See also: Modularity Metric, Component Granularity, Cross-Reference Dependence.

#### Chapter Structure

The macro-level organization of an educational resource into an ordered sequence of chapters and internal sections derived from the topological sort of its learning graph.

When chapter order follows the dependency graph, every concept a student encounters builds naturally on concepts defined in earlier sections.

**Example:** Organizing the textbook so licensing and the 10-metric rubric come first, manual and AI evaluation come second, AI-assisted improvement comes third, and classroom A/B testing comes fourth reflects a dependency-driven design.

See also: Learning Graph, Scope and Sequence, Modularity Metric.

#### Citation Quality

The credibility, relevance, recency, and verifiability of the reference sources cited to support claims within an educational resource.

Evaluating citation quality distinguishes between chapters backed by peer-reviewed scholarship and chapters relying on dead links, opinion blogs, or fabricated AI references.

**Example:** A nutrition chapter citing recent peer-reviewed medical journals and World Health Organization reports exhibits high citation quality compared to one citing commercial supplement websites.

See also: Source Citation, Accuracy Metric, Source Verification.

#### Cohen's Kappa

A statistical coefficient ($\kappa$, typically ranging from $0$ to $1$) that measures inter-rater agreement for categorical decisions—such as Adopt, Revise, or Reject classifications or score bands—while correcting for the amount of agreement that would occur purely by random chance.

Because two raters who both assign "Adopt" to 80% of textbooks will agree most of the time just by chance, correcting for baseline probability provides a far more honest measure of rubric reliability than raw percentage agreement.

**Example:** When two reviewers classify twenty candidate OER chapters into Adopt, Revise, or Reject and achieve $\kappa = 0.78$, their concordance falls into the "substantial agreement" tier above chance.

See also: Inter-Rater Agreement, Rubric Reliability, Agreement Rate.

#### Color Contrast

The visual difference in luminance between foreground elements (such as text or chart lines) and their background color, determining how easily readers with low vision or color vision deficiencies can read the content.

Insufficient luminance difference is one of the most frequent accessibility failures caught by automated scanning tools in open textbooks and MicroSims.

**Example:** Dark navy text on a white background provides crisp readability, whereas light gray text on a pale yellow callout box is nearly illegible for many learners.

See also: Contrast Ratio, Color Independence, WCAG 2.1 AA.

#### Color Independence

The accessibility requirement that color is never used as the sole visual means of conveying information, indicating an action, prompting a response, or distinguishing a graphical element.

Adding text labels, patterns, symbols, or shapes alongside color cues ensures that learners with color blindness or monochrome displays do not miss critical meaning.

See also: Color Contrast, Accessibility Metric, WCAG 2.1 AA.

#### Commercial Textbook

A proprietary instructional book produced by a traditional publisher and sold or rented to students under restrictive copyright terms that forbid unauthorized copying, adaptation, or redistribution.

High prices and restrictive digital access leases associated with proprietary books motivate institutions to adopt and evaluate open alternatives.

**Example:** A \$220 chemistry textbook with a single-semester digital access code that expires after finals week represents a standard publisher product.

See also: Course Material Affordability, Proprietary License.

Contrast with: Open Textbook, Open Educational Resource.

#### Common Cartridge

An open interoperability specification maintained by 1EdTech (formerly IMS Global) for packaging digital course materials, discussion prompts, web links, and QTI assessments into a single `.imscc` archive that imports across different LMS platforms.

Supporting this standard archive format boosts a textbook's Portability Metric score for institutions that centralize instruction inside an LMS.

**Example:** Exporting an open psychology course as a `.imscc` cartridge allows instructors at three different universities using Canvas, Moodle, and Blackboard to import the exact same module structure.

See also: LMS Import, Export Format, Portability Metric.

#### Community Contribution

Improvements, translations, new quiz banks, interactive MicroSims, errata fixes, or local case studies created by external educators or students and shared back into an open educational resource project.

When a textbook scores high on the five reusability metrics, educators at other institutions can easily contribute enhancements that benefit everyone using the book.

**Example:** Three high school teachers from different states each build one p5.js MicroSim for an open physics textbook and submit pull requests that add their simulations to the shared repository.

See also: Pull Request, Open Pedagogy, Publishing OER.

#### Completion Rate

The percentage of students assigned an educational resource, module, or practice quiz who finish reading the material and submitting the required activity within the allotted study window.

Dense walls of text and confusing navigation often cause struggling learners to abandon a reading partway through; improvements in Readability and Modularity frequently boost the proportion of students who finish.

**Example:** Splitting a 12,000-word chapter into three short modular lessons with embedded self-checks raises the percentage of students completing the homework reading from 64% in the control group to 91% in the treatment group.

See also: Time on Task, Outcome Measure, Modularity Metric.

#### Complex Image Description

A detailed multi-sentence or structured text explanation accompanying an intricate diagram, data chart, map, or infographic whose full instructional meaning cannot fit into a brief alt text attribute.

When an image contains rich relationships or multiple data series, evaluators look for a long description in the surrounding prose, a collapsible details block, or an accessible data table.

**Example:** Beneath a detailed flowchart of the Creative Commons license compatibility rules, the author provides a complete Markdown table listing every source-and-target license pair for screen reader users.

See also: Alt Text, Table Accessibility, Accessibility Metric.

#### Component Discoverability

The ease with which educators, librarians, search engines, and AI agents can locate a specific reusable component when searching by concept name, subject, grade level, or instructional format.

Rich metadata, descriptive titles, Schema.org/LRMI markup, and registration in OER clearinghouses ensure that newly created simulations and modules actually reach the teachers who need them.

**Example:** Tagging a standalone WCAG contrast-checker MicroSim with descriptive keywords, LRMI educational properties, and a clear summary description allows teachers searching for "color contrast interactive activity" to find it immediately.

See also: Metadata Metric, Keywords, OER Clearinghouse.

#### Component Granularity

The size and scope of an individual instructional unit within a resource—ranging from a single figure or two-minute MicroSim (fine granularity) to a full semester textbook (coarse granularity).

Choosing the right unit size balances ease of reuse with instructional coherence: chapters that are 80 pages long are too coarse to reuse easily, whereas 50-word fragments lack sufficient context.

See also: Modularity Metric, Chapter Splitting, Modular Content.

#### Component Library

A curated, searchable collection or directory of reusable educational components—such as `docs/sims/` for MicroSims or a shared repository of quizzes and modules—organized with consistent metadata and status indicators.

Maintaining an indexed catalog of open building blocks allows teachers and curriculum designers to browse and assemble interactive lessons without reinventing the wheel.

**Example:** The `docs/sims/` directory in an intelligent textbook acts as a local catalog of interactive simulations, each with its own standardized folder, screenshot preview, and embed instructions.

See also: Reusable Component, Component Discoverability, OER Repository.

#### Component Licensing

The practice of attaching an explicit, machine- and human-readable open license notice directly to an individual reusable component (such as inside a MicroSim's metadata, HTML source comments, and visible footer) so its legal terms travel with the asset even when embedded outside its parent textbook.

When another teacher embeds a simulation via an `iframe` or copies a quiz file into a new repository, a local license notice ensures downstream users know they have permission to reuse it.

**Example:** Including a `license: CC BY 4.0` tag in `docs/sims/ab-test-power/index.md` and a small CC BY credit link at the bottom of `main.html` keeps the legal terms visible wherever the simulation is embedded.

See also: Open License, License Selection, Reusable Component.

#### Component Packaging

The standardized organization of a reusable educational component's files—such as placing a MicroSim's `main.html`, JavaScript code, CSS stylesheet, `index.md` lesson plan, and metadata inside a dedicated kebab-case directory—so it can be moved, hosted, or embedded as a single unit without broken relative paths.

Consistent file structure ensures that copying a component folder from one textbook repository to another works immediately without hunting for scattered assets.

**Example:** Storing all code and assets for the license-compatibility simulator inside `docs/sims/license-compatibility/` using relative paths makes the entire folder portable across any MkDocs site.

See also: Reusable Component, Modularity Metric, Portability Metric.

#### Concept Dependency

A directed prerequisite link between two concepts in a learning graph indicating that mastery of the foundational concept is required to properly understand the target concept.

Mapping prerequisite links explicitly prevents authors from introducing advanced procedures in early chapters before their underlying building blocks have been taught.

**Example:** Understanding `Contrast Ratio` depends directly on first understanding `Color Contrast` and `WCAG 2.1 AA`, so the textbook introduces those foundational concepts first.

See also: Learning Graph, Prerequisite Knowledge, Scope and Sequence.

#### Confounding Variable

An extraneous factor other than the textbook version being tested—such as a different instructor, different time of day, unequal prior preparation, or extra tutoring—that differs systematically between the control and treatment groups and can distort the test results.

Good A/B test design holds instruction, time limits, and environment constant across both groups so any observed difference in learning can be attributed confidently to the resource improvements.

**Example:** If Professor Smith teaches the Control Group at 8:00 AM on Monday and Professor Jones teaches the Treatment Group at 11:00 AM on Wednesday, instructor style and class hour act as confounders that muddy the comparison.

See also: Random Assignment, Sampling Bias, A/B Test.

#### Consensus Scoring

A collaborative evaluation method in which multiple reviewers independently rate a resource and then discuss their evidence and reasoning to agree upon a single shared score for each rubric metric.

Consensus ratings formed by experienced human educators serve as the gold-standard benchmark ("ground truth") for calibrating and testing AI scoring agents.

**Example:** After one teacher scores a chapter's Alignment Metric at 7 and a second teacher scores it at 9, they review the missing assessment for Objective 3 together and agree on a final consensus score of 8.

See also: Score Reconciliation, Calibration Session, Calibration Against Humans.

#### Content Gap

A missing topic, unaddressed learning outcome, skipped prerequisite explanation, or absent skill step that leaves a resource incomplete for its intended curriculum.

Evaluators document missing sections during the rubric review so instructors can either supplement the gap with another open module or generate new content.

**Example:** A curriculum map reveals that an open introductory statistics book covers hypothesis testing and confidence intervals thoroughly but lacks any section on experimental design and A/B testing.

See also: Outcome Coverage, Alignment Metric, Improvement Plan.

#### Content Update

The revision of outdated facts, statistics, policy references, code syntax, or disciplinary explanations in an open educational resource to reflect current scholarship and real-world practice.

Because open textbooks live in editable source repositories, instructors can refresh obsolete passages immediately rather than waiting four years for a commercial publisher's next edition.

**Example:** An environmental science instructor updates a 2018 climate data table with the latest global atmospheric $\text{CO}_2$ measurements and recent international treaty milestones.

See also: Outdated Content, Currency Metric, Revise Permission.

#### Context Window

The maximum amount of text—measured in tokens and encompassing the system prompt, uploaded textbook files, tool outputs, and the model's generated response—that a large language model can process in a single interaction.

Knowing the capacity limit helps evaluators decide whether to feed an entire textbook at once or evaluate it chapter by chapter to prevent the model from overlooking middle sections.

**Example:** A 200,000-token context capacity can hold a complete 120,000-word open textbook in memory at once, though evaluating one 4,000-word chapter per call often yields more thorough line-by-line evidence citations.

See also: Token, Document Ingestion, Large Language Model.

#### Contrast Ratio

A numerical measurement ranging from 1:1 (identical colors) to 21:1 (black on white) that quantifies the relative luminance difference between foreground text and its background color.

To pass WCAG 2.1 AA under the Accessibility Metric, standard body text requires a ratio of at least 4.5:1 and large text or graphical user interface components require at least 3:1.

**Example:** Checking a button's white text (`#FFFFFF`) against a medium blue background (`#005A9C`) yields a ratio of 7.0:1, comfortably exceeding the 4.5:1 AA threshold.

See also: Color Contrast, WCAG 2.1 AA, Accessibility Checker.

#### Control Group

The baseline cohort of students in an educational A/B test who use the unmodified original version of a learning resource under otherwise identical instructional conditions.

Without a baseline comparison group studying the original material during the same unit, an instructor cannot tell whether post-test gains came from the textbook improvements or simply from classroom lectures.

See also: Treatment Group, Original Version, A/B Test.

Contrast with: Treatment Group.

#### Controlled Vocabulary

A standardized, predefined list of authorized terms, subject headings, or educational standard codes used to tag metadata fields consistently across a repository.

Restricting subject and grade-level tags to an agreed-upon list prevents fragmentation caused by synonyms, spelling variations, or arbitrary free-text labels.

**Example:** Requiring catalogers to select `"Secondary Education (Grades 9-12)"` from an official drop-down list prevents the chaos of some authors typing `"High School"`, others `"HS"`, and others `"9th-12th"`.

See also: Subject Field, Keywords, Metadata Completeness.

#### Copyright

A legal right granted by statute to the creator of an original work, giving the holder exclusive control over copying, adapting, distributing, and publicly displaying that work for a defined period.

Understanding baseline intellectual property law is essential because open licenses work alongside existing statutes rather than replacing them.

**Example:** The moment an instructor writes an original set of lecture notes, legal protection attaches automatically, preventing others from republishing the notes without permission.

See also: Open License, Public Domain, All Rights Reserved.

#### Course Material Affordability

The degree to which students can obtain required textbooks, software, and supplies without experiencing financial hardship or delaying enrollment.

Reducing financial barriers for learners is a primary institutional driver for adopting and improving openly licensed course materials.

**Example:** Replacing a \$180 publisher bundle with a freely downloadable open textbook saves a 30-student class \$5,400 in a single semester.

See also: Zero Textbook Cost Course, Open Textbook, Commercial Textbook.

#### Creative Commons

A global nonprofit organization that provides a standardized suite of open copyright licenses and public domain tools used to share creative and educational works legally.

Nearly all open textbooks and modular learning resources evaluated in K-12 and higher education rely on this licensing framework.

**Example:** By choosing a standard license from the organization's six main options, an author avoids hiring a lawyer to draft custom reuse terms.

See also: Open License, CC BY, CC0 Dedication.

#### Cross-Reference Dependence

A structural flaw in modularity where a chapter or section relies heavily on hard-coded references to other parts of the book (such as "see Chapter 3, page 42" or "using the dataset from yesterday's lesson"), making it confusing when used alone.

Reducing brittle internal pointers—or replacing them with explicit concept names and self-contained summaries—raises a resource's score on the Modularity Metric.

**Example:** Rewriting "As we saw in the previous chapter on pages 18–22..." to "Recall that under the 5R framework, Revise permission allows adapting content..." removes the dependency on the prior chapter's numbering.

See also: Modularity Metric, Standalone Component, Modular Content.

#### Currency Metric

The half of the first quality metric in the ten-metric rubric that evaluates whether a resource reflects up-to-date disciplinary knowledge, recent statistics, working external links, and active maintenance.

In fast-moving fields like computer science, health, and environmental science, accurate historical content can still fail learners if recent developments are missing.

**Example:** A web development tutorial last updated in 2014 that teaches deprecated HTML tags and contains 15 broken links scores poorly on currency even if its original code once worked.

See also: Accuracy Metric, Outdated Content, Link Rot.

#### Curriculum Map

A matrix or table that charts how chapters, lessons, activities, and assessments across a resource or course correspond to specific learning outcomes and academic standards.

Constructing or inspecting a mapping matrix immediately reveals both redundant topics and uncovered learning objectives.

**Example:** A spreadsheet showing which of the twelve textbook chapters address each of the eight departmental course outcomes helps faculty spot an unaddressed outcome before the semester starts.

See also: Standards Alignment, Outcome Coverage, Content Gap.

#### Data Collection

The systematic gathering and recording of quantitative and qualitative observations during an A/B test—including pre-test scores, post-test scores, completion logs, time-on-task records, and student survey responses.

Using clean, consistent spreadsheets with identical column structures for both the control and treatment groups makes subsequent calculation and verification straightforward.

See also: Anonymized Data, Outcome Measure, Student Survey.

#### Decorative Image

A visual element—such as a stylistic border, background flourish, or generic icon—that conveys no instructional information and is given an empty alt attribute (`alt=""`) so screen readers skip it smoothly.

Distinguishing purely ornamental graphics from informative figures prevents screen reader users from hearing cluttered, unhelpful descriptions.

See also: Alt Text, Screen Reader, Accessibility Metric.

#### Defined Terms

Key domain-specific words or phrases that are explicitly explained in the text upon first use and collected in a reference glossary to support learner comprehension.

The Readability Metric rewards resources that highlight new concepts visually and provide clear, non-circular explanations right when the student encounters them.

**Example:** When introducing "ShareAlike Requirement" for the first time, the chapter bolds the phrase, defines it in the same sentence, and links it to the book's glossary.

See also: Glossary, Vocabulary Level, Readability Metric.

#### Derivative Work

A new creative work based upon one or more preexisting works—such as a translation, reading-level adaptation, modularized remix, or annotated edition—in which the original material is recast, transformed, or modified.

Under copyright law, creating and distributing a modified version requires either an open license that omits the NoDerivatives (`ND`) restriction or explicit permission from the copyright holder.

**Example:** An open textbook chapter that has been translated into Spanish and enhanced with new worked examples and interactive MicroSims is a legal adaptation requiring proper attribution to the original author.

See also: Revise Permission, Remix Permission, Attribution Statement.

Contrast with: NoDerivatives Requirement.

#### Description Field

The metadata element that provides a concise summary of a resource's scope, learning objectives, and key features so prospective adopters can quickly judge its relevance.

Search engines, social media previews, and OER clearinghouses display this summary snippet below the page title in catalog listings.

**Example:** A two-sentence `description` in the chapter frontmatter summarizes that the module teaches the ten-metric OER rubric and includes an interactive scoring worksheet.

See also: Metadata Record, Dublin Core, Metadata Generation.

#### Difference of Means

The net numerical gap ($\bar{x}_{\text{treatment}} - \bar{x}_{\text{control}}$) between the average outcome score or average learning gain of the treatment group and that of the control group in an A/B test.

A positive difference in mean learning gain indicates that learners using the improved OER outperformed learners using the original version on average.

**Example:** When the Treatment Group achieves a mean learning gain of $+4.6$ points and the Control Group achieves a mean learning gain of $+2.8$ points on a 10-point scale, the difference of means is $+1.8$ points (+18 percentage points).

See also: Mean Score, Effect Size, Learning Gain.

#### Distractor Quality

The degree to which the incorrect options in a multiple-choice question represent plausible, diagnostic student misconceptions rather than absurd, giveaway, or trick choices.

When AI agents generate practice questions, reviewers inspect the wrong choices closely to ensure they are similar in length and tone to the correct answer and target real errors.

**Example:** In a question asking what "SA" stands for in CC BY-SA, using "ShareAlike" alongside plausible distractors like "Source Attributed" and "Standard Access" tests real knowledge better than joke options.

See also: Multiple-Choice Question, Practice Question Generation, Question Difficulty.

#### Document Ingestion

The technical step of loading, parsing, and converting an educational resource's files—such as Markdown chapters, HTML pages, or PDF documents—into clean text and structural metadata that an AI agent can analyze.

If the ingestion step strips out image `alt` tags, heading levels, or YAML frontmatter, the agent will be blind to the very features it needs to score Accessibility and Metadata.

**Example:** Reading the raw `.md` source files directly preserves every `![alt text](image.png)` tag and `#` heading marker, whereas copying text from a browser window strips those structural elements away.

See also: File Access, Context Window, PDF-to-Markdown Conversion.

#### Document Language

The machine-readable declaration—such as `<html lang="en">` or `<html lang="es">`—that specifies the primary natural language of a webpage or document, along with inline language tags for foreign-language passages.

Without an accurate language attribute, screen readers apply the wrong pronunciation rules and read text with an unintelligible accent.

**Example:** Setting `lang="en"` on an English textbook webpage and wrapping a French quotation in `<span lang="fr">` ensures assistive speech synthesizers switch pronunciation engines smoothly.

See also: Screen Reader, HTML, WCAG 2.1 AA.

#### Dublin Core

An internationally standardized set of fifteen core metadata elements—including Title, Creator, Subject, Description, Publisher, Date, Format, and Rights—widely used by libraries and OER repositories to catalog digital resources.

Using standard element names ensures that when an improved textbook is submitted to an OER clearinghouse, its catalog fields map cleanly without manual re-entry.

See also: Metadata Record, LRMI, Metadata Metric.

#### Editable Source Metric

The fourth reusability metric (Metric 9) in the ten-metric rubric, which evaluates whether a resource is distributed in clean, open, human- and machine-editable source files (such as Markdown or HTML in a version-controlled repository) rather than locked or layout-only formats.

Legal permission to revise an OER means little in practice if the author provides only a flattened PDF or scanned image that teachers cannot edit without painstaking reconstruction.

**Example:** A textbook whose full Markdown source, raw SVG diagrams, and build configuration are hosted in a public GitHub repository earns 10 out of 10 on this metric.

See also: Source Format, Open File Format, PDF-Only Distribution.

#### Educational Resource

A learning material, tool, or activity designed to support teaching, study, or skill development in an instructional setting.

This concept forms the baseline category from which open and commercial teaching materials are distinguished throughout the course.

**Example:** A printed biology lab manual, an interactive chemistry simulation, and a recorded history lecture all qualify as teaching materials used in a course.

See also: Open Educational Resource, Commercial Textbook, Free Resource.

#### Effect Size

A standardized statistical metric (commonly Cohen's $d$, calculated by dividing the difference of group means by the pooled standard deviation) that quantifies the practical magnitude of an A/B test difference independent of the test's point scale.

Reporting standardized magnitude helps educators judge whether an observed score gain is trivial ($d < 0.2$), moderate ($d \approx 0.5$), or large ($d \ge 0.8$) in real classroom impact.

**Example:** If the Treatment Group outgains the Control Group by 1.8 points and the pooled standard deviation of gains is 2.25 points, the standardized effect is $d = 1.8 / 2.25 = 0.80$, indicating a large positive instructional impact.

See also: Difference of Means, Mean Score, Sample Size.

#### Embeddable Component

A modular digital asset—such as a MicroSim, interactive quiz, chart, or video—designed with a clean, chrome-free URL and responsive layout so it can be inserted directly into any webpage or LMS page using an HTML `iframe`.

Providing a ready-to-copy `<iframe src="...">` snippet on a simulation's documentation page makes classroom integration a thirty-second task for any teacher.

**Example:** An instructional designer copies a three-line `iframe` tag from the OER Evaluator site and pastes it into a Canvas page to display the interactive rubric radar chart right inside the course module.

See also: Iframe Embedding, MicroSim, Reusable Component.

#### Equity Consideration

The proactive design and ethical requirement in OER evaluation, adaptation, and classroom A/B testing that ensures no group of students is disadvantaged by disability barriers, device or bandwidth limitations, biased examples, or withholding beneficial learning materials.

In classroom A/B testing, fairness means never intentionally degrading a resource, never letting experimental group assignment penalize course grades, and immediately sharing the improved resource with the control group after the post-test.

**Example:** Right after the 15-minute post-test concludes, the instructor gives the Control Group full access to the improved chapter with its interactive MicroSims and study quizzes so every student prepares equally for the midterm exam.

See also: Accessibility, Offline Access, Informed Consent.

#### Evidence Citation

A precise pointer—such as a section heading, page number, line number, URL, or direct quotation—that locates a piece of scoring evidence within the evaluated resource.

When an AI agent generates an evaluation report, checking its location pointers is the fastest way to catch hallucinated claims.

See also: Evidence for a Score, Source Verification, Invented Citation.

#### Evidence for a Score

Specific, verifiable facts, quotes, counts, or observations extracted directly from an evaluated resource to justify the numeric point value assigned to a rubric metric.

Requiring concrete proof prevents both human reviewers and AI agents from assigning arbitrary or impressionistic numbers.

**Example:** To justify a score of 4 on the Practice Metric, the reviewer records that the 25-page chapter contains only three end-of-chapter questions and zero answer explanations.

See also: Evidence Citation, Evidence Recording, Metric Score.

#### Evidence Recording

The practice of documenting concrete observations, exact quotes, file paths, line numbers, and defect counts alongside each metric score during an evaluation.

Detailed evidence notes turn a rubric score from an unverified personal opinion into an auditable diagnostic record that guides targeted improvements.

**Example:** While scoring the Modularity Metric at 5 out of 10, the reviewer records that the chapter is 14,200 words long and contains eight hard-coded references to "yesterday's lab in Chapter 2."

See also: Evidence for a Score, Evidence Citation, Reviewer Notes.

#### Exit Survey

A comprehensive end-of-course or end-of-workshop questionnaire completed by participating educators to assess their confidence across the course learning outcomes, rate the usefulness of the rubric and AI workflows, and suggest improvements to the training materials.

Feedback from completing teachers drives iterative improvements to the textbook's chapters, MicroSims, and workshop exercises.

See also: Training Evaluation, Student Survey, Teacher Training Workshop.

#### Expert Review

A thorough evaluation of an educational resource's disciplinary accuracy, depth, and currency conducted by a specialist with advanced training in the subject matter.

While AI agents can screen for common errors and outdated links, human domain specialists remain essential for validating subtle conceptual explanations.

**Example:** A practicing clinical microbiologist reviews an open nursing chapter on antibiotic resistance to confirm that dosage guidelines and mechanism descriptions are clinically sound.

See also: Accuracy Metric, Reviewer, Peer Review.

#### Export Format

A downloadable file representation—such as HTML, PDF, EPUB, DOCX, or Common Cartridge—generated from a resource's master source files to serve specific reading, printing, or importing needs.

Offering multiple distribution formats from a single Markdown source supports both online interactive learners and students who need offline or printed copies.

**Example:** From a single repository of Markdown chapters, a build script compiles a static HTML website for browser reading, an EPUB for e-readers, and a print-ready PDF for low-connectivity students.

See also: Source Format, Offline Access, Portability Metric.

#### Facilitator Guide

An instructor manual designed for the leader of a teacher training workshop, providing talking points, common participant misconceptions, timing cues, answer keys for sample evaluations, and troubleshooting tips for AI agent exercises.

As noted in the project rules, instructor-facing guides use a direct professional tone without student-facing mascot admonitions so workshop leaders can scan instructions rapidly during live sessions.

**Example:** The workshop leader's manual includes the pre-scored consensus rubric key for the sample ecology chapter and step-by-step instructions for helping participants spot three deliberate hallucinations planted in the sample AI report.

See also: Teacher Training Workshop, Workshop Agenda, Training Kit.

#### Fact Checking

The systematic process of verifying claims, dates, formulas, statistics, and examples in an educational resource against authoritative primary and secondary reference sources.

While AI agents can rapidly flag suspicious claims or calculation mismatches, human reviewers verify citations to ensure the agent did not hallucinate its own sources.

**Example:** Cross-checking every population statistic in an open geography chapter against the latest United Nations demographic database confirms the text's factual reliability.

See also: Accuracy Metric, Source Verification, Primary Source.

#### Factual Error

An objectively incorrect statement, calculation, formula, date, or technical claim within an educational resource that contradicts established disciplinary knowledge or primary evidence.

Reviewers and AI verification agents log every erroneous claim with its exact line or page location so authors can correct it before classroom use.

**Example:** Stating in a chemistry chapter that water boils at 100 degrees Fahrenheit at standard atmospheric pressure (instead of 100 degrees Celsius) is a clear factual mistake.

See also: Accuracy Metric, Fact Checking, Expert Review.

#### Fair Use

A statutory limitation and exception in United States copyright law that allows brief, transformative, or instructional use of copyrighted material without permission under a four-factor balancing test.

Because this exception is context-specific and legally uncertain for downstream reusers, relying on it inside an open textbook lowers the resource's portability and open license score.

**Example:** Quoting a four-line stanza from a copyrighted poem for critical analysis inside a literature chapter may qualify as lawful criticism, but it complicates global redistribution.

See also: Copyright, Third-Party Content, All Rights Reserved.

#### Feedback Channel

A visible, low-friction mechanism—such as an embedded "Report an Erratum" form, a repository issue link, or a dedicated contact email—provided inside an open educational resource so readers and adopting teachers can submit corrections and suggestions.

Providing a clear path for reader input supports continuous improvement between formal rubric evaluations.

**Example:** Every chapter footer in the online textbook includes both a direct link to open a GitHub issue for technical users and a simple two-field web form for teachers without GitHub accounts.

See also: Issue Tracking, Community Contribution, Maintenance Plan.

#### Feedback Message

An explanatory statement displayed to a learner after submitting an answer to a quiz or practice item, clarifying why the chosen option is correct or what misconception led to an error.

Diagnostic explanations turn a simple right-or-wrong check into a teaching moment that repairs misunderstandings on the spot.

See also: Immediate Feedback, Distractor Quality, Multiple-Choice Question.

#### FERPA

The Family Educational Rights and Privacy Act, a United States federal law that protects the privacy of student education records and restricts schools from disclosing personally identifiable student information without consent.

Educators adopting open resources, embedding external tools, or evaluating A/B test data design their workflows to comply strictly with federal student record protections.

**Example:** Choosing a static, no-login open textbook hosted on GitHub Pages with self-contained browser quizzes avoids transmitting protected student education records to third-party commercial servers.

See also: Student Data Privacy, Student Privacy in Testing, No-Login Access.

#### Few-Shot Example

One or more completed input-and-output demonstrations included inside a prompt to show a large language model the exact scoring strictness, evidence style, and formatting expected for a task.

Providing two concrete sample evaluations—such as one strong chapter scored at 88 and one flawed chapter scored at 52—calibrates the model's scoring scale far more effectively than instructions alone.

See also: Prompt, Calibration Against Humans, Score Inflation.

#### File Access

The permission and technical mechanism that allows an AI agent to read source files, directory trees, metadata configs, and images directly from a local workspace or Git repository, and write reports or edits back to disk.

Direct repository access lets an agent verify whether `mkdocs.yml`, image assets, and standalone MicroSim folders actually exist rather than relying on pasted text excerpts.

**Example:** With read access to the project directory, the agent inspects `docs/img/` to confirm whether referenced diagram files are present and checks `mkdocs.yml` to verify that every chapter is listed in navigation.

See also: Document Ingestion, AI Agent, Agent Workflow.

#### Findings Log

A structured table or audit record in which a reviewer documents each claim or score from an AI agent's evaluation, the result of the human verification check, the triage decision (Accept, Correct, or Reject), and the error type if a mistake occurred.

Keeping a systematic log across multiple chapters allows an evaluation team to calculate the agent's error rate and identify which rubric prompts need refinement.

**Example:** A spreadsheet tracking 100 metric evaluations across ten chapters records 84 accepted findings, 12 corrected scores, and 4 rejected hallucinations, providing concrete diagnostic data for prompt iteration.

See also: Accept Correct or Reject, Agent Error Rate, Agent Error Type.

#### Flesch-Kincaid Grade Level

A widely used readability formula that converts average sentence length and average syllables per word into a numeric score corresponding to a United States school grade level.

In OER evaluation, this score provides a reproducible benchmark for verifying before-and-after improvements when rewriting dense chapters.

See also: Readability Formula, Reading Level, Reading Level Rewrite.

#### Fork

A personal, independent copy of another author's Git repository hosted under the adapter's own account, allowing unrestricted experimentation and customization without altering the original project.

Creating a repository copy is the technical equivalent of exercising the 5R Retain, Revise, and Remix permissions on a version-controlled textbook.

**Example:** A community college instructor creates a personal copy of an open statistics repository on GitHub to translate the chapters into Spanish and customize the datasets for local industry.

See also: GitHub Repository, Pull Request, OER Adaptation.

#### Formative Assessment

Low-stakes or ungraded checks for understanding embedded throughout the learning process to give students and instructors actionable feedback on comprehension before a final exam.

The Practice Metric focuses primarily on these low-stakes learning checks because they actively drive comprehension while a student is reading the textbook.

**Example:** Three ungraded concept-check questions placed at the end of a section on Creative Commons licenses let learners spot and fix misunderstandings immediately.

See also: Self-Check Question, Quiz, Practice Metric.

#### Free Resource

A digital material available online at no monetary cost to the reader, but remaining under standard copyright restrictions that prohibit copying, editing, or redistributing without permission.

Reviewers frequently confuse no-cost web content with truly open content, leading to legal errors when attempting to adapt or republish materials.

**Example:** A free tutorial blog post with an "All Rights Reserved" footer can be linked in a syllabus, but a teacher cannot copy its text into a customized course pack.

See also: All Rights Reserved, Proprietary License, No-Login Access.

Contrast with: Open Educational Resource.

#### Git

The distributed, open-source version control system widely used to track changes in source code, Markdown textbooks, datasets, and educational simulations.

Learning basic repository commands allows educators and AI coding agents to branch, edit, verify, and publish open educational resources safely.

**Example:** After generating a new chapter quiz and repairing broken links, the author stages the files and creates a commit with a descriptive message explaining the improvements.

See also: Version Control, GitHub Repository, Fork.

#### GitHub Pages

A free static web hosting service integrated directly with GitHub repositories that automatically publishes compiled HTML, CSS, JavaScript, and MicroSim files to a public `github.io` URL whenever changes are deployed.

Combining a public GitHub repository with automated static hosting satisfies both the Editable Source Metric (raw Markdown in the repo) and the Portability Metric (free, no-login web access).

**Example:** Running `mkdocs gh-deploy` builds the textbook and pushes the static HTML files to the `gh-pages` branch, publishing the live course immediately at `https://dmccreary.github.io/oer-evaluator/`.

See also: GitHub Repository, MkDocs, Publishing OER.

#### GitHub Repository

A cloud-hosted project workspace on GitHub that stores a Git version-controlled directory of files along with issue trackers, pull requests, release notes, and automated web publishing tools.

In the OER Evaluator workflow, a public project workspace serves simultaneously as the editable source archive, collaboration hub, and GitHub Pages publishing engine.

**Example:** Any educator worldwide can visit `https://github.com/dmccreary/oer-evaluator` to inspect the raw Markdown chapters, view the commit log, or download the MicroSim source code.

See also: Git, GitHub Pages, Editable Source Metric.

#### Glossary

An alphabetical list of specialized terms used in an educational resource accompanied by precise, concise definitions, contextual discussions, and examples.

In an intelligent textbook, a standardized ISO 11179 glossary anchors terminology across all chapters, quizzes, and AI agent prompts.

**Example:** A 351-term reference page at the end of the textbook allows teachers and students to look up exact definitions for every concept in the course learning graph.

See also: Defined Terms, Glossary Generation, Readability Metric.

#### Glossary Generation

The automated extraction of key domain concepts from a learning graph or textbook and the drafting of standardized, ISO 11179-compliant definitions, contextual discussions, examples, and cross-references sorted alphabetically into a reference glossary.

Adding a comprehensive glossary improves the Readability Metric by giving students an authoritative lookup reference for every technical term in the course.

**Example:** Starting from a 351-concept learning graph, a serial AI agent writes precise 20-to-50-word non-circular definitions and concrete examples, which a Python script sorts alphabetically into `docs/glossary.md`.

See also: Glossary, Defined Terms, Readability Metric.

#### Grade Level Field

The metadata element that specifies the intended educational tier, age range, or academic level—such as Grades 9–12, Lower-Division Undergraduate, or Adult Professional Development—for which a resource is designed.

Reviewers compare this declared target tier directly against the text's Flesch-Kincaid reading level to verify audience fit.

**Example:** Setting `grade_level: "Grades 6-8 (Middle School)"` tells both repository search engines and readability auditing agents to evaluate the prose against a seventh-grade benchmark.

See also: Metadata Record, Reading Level, Audience Fit.

#### Hallucination

A plausible-sounding but factually false, fabricated, or unsupported statement generated by a large language model that is not grounded in the source document or reality.

Because language models predict probable word sequences rather than verifying truth, human reviewers always check agent claims against the actual textbook files.

See also: Invented Citation, Agent Error Type, Source Verification.

#### Heading Repair

The structural remediation of a document's section titles so that all headings use proper semantic markup (`#` through `####` in Markdown or `<h1>` through `<h4>` in HTML) in a strict, unbroken hierarchy without skipped levels or bolded paragraph fakes.

Fixing section hierarchy improves both the Readability Metric (clear visual outline) and the Accessibility Metric (screen reader navigation).

**Example:** An AI agent inspects a chapter that used bolded paragraphs (`**Section 1**`) and jumped from `# Title` straight to `#### Details`, converting them into a clean `#` $\rightarrow$ `##` $\rightarrow$ `###` hierarchy.

See also: Heading Structure, Headings and Subheadings, Accessibility Metric.

#### Heading Structure

The logical, sequential nesting of HTML or Markdown heading levels (`H1` through `H6`) without skipping levels or using visual font styling in place of semantic tags.

Assistive technologies rely on semantic heading tags to generate an interactive outline that lets blind users jump directly between chapter sections.

**Example:** Starting a page with `# Chapter Title` (`H1`), followed by `## Major Section` (`H2`), and `### Subsection` (`H3`) preserves a valid hierarchy, whereas jumping straight from `H1` to `H4` breaks navigation.

See also: Headings and Subheadings, Heading Repair, Screen Reader.

#### Headings and Subheadings

Descriptive titles placed at the start of major sections and subsections within a document to signal topic transitions and show the hierarchical outline of the material.

In addition to boosting visual readability for sighted learners, properly nested section titles allow screen reader users to navigate a chapter efficiently.

**Example:** Using a clear `## Quality Metrics` section title followed by five `###` subsection titles for each individual metric lets readers see the chapter's organization at a glance.

See also: Text Structure, Heading Structure, Readability Metric.

#### HTML

HyperText Markup Language, the foundational open standard used to structure and display content, headings, tables, images, and interactive components on the World Wide Web.

Whether authored directly or generated from Markdown, semantic web markup ensures that open textbooks work across every browser, screen reader, and device.

**Example:** Each standalone MicroSim in the textbook is packaged around a `main.html` file that loads JavaScript libraries and renders an interactive canvas inside any browser.

See also: Open File Format, Browser Compatibility, Table Accessibility.

#### Human in the Loop

A collaborative system design principle requiring a qualified human educator to review, verify, edit, and approve critical AI agent outputs—such as rubric scores, license judgments, and textbook edits—before they are finalized or published.

In OER evaluation and improvement, automation accelerates tedious scanning and drafting, but human teachers retain full pedagogical and legal authority.

**Example:** After an AI agent generates twenty new multiple-choice questions and rewrites a chapter's reading level, the course instructor reviews every question and diff block before merging the changes into the live textbook.

See also: Accept Correct or Reject, Human Review of Changes, Verification Step.

#### Human Review of Changes

The careful line-by-line inspection by a qualified educator of all text edits, alt text descriptions, metadata fields, quiz questions, and code produced by an AI agent before those modifications are committed and published.

Even well-prompted agents can accidentally oversimplify a key scientific nuance during a reading-level rewrite or write a plausible-looking quiz key that is wrong.

**Example:** Using a side-by-side `git diff` view, the instructor reads every paragraph of an AI-simplified physics lesson and corrects a sentence where the agent blurred the distinction between speed and velocity.

See also: Preserving Original Meaning, Human in the Loop, Spot Check.

#### Iframe Embedding

The technique of displaying an external web resource—such as a standalone MicroSim, interactive chart, or quiz—directly inside a parent webpage or LMS lesson using the HTML `<iframe>` element.

Designing interactive components with a clean, header-free `main.html` entry point makes them effortless to embed inside Canvas, Moodle, Blackboard, or another open textbook.

**Example:** Pasting `<iframe src="https://dmccreary.github.io/oer-evaluator/sims/ten-metric-rubric/main.html" width="100%" height="520"></iframe>` into a course page embeds the live interactive rubric directly in the student's reading flow.

See also: Embeddable Component, MicroSim, Portability Metric.

#### Immediate Feedback

Automated diagnostic guidance delivered to a learner the instant they submit a response to an interactive question or simulation step, without waiting for an instructor to grade the work.

Cognitive research shows that correcting errors right when the reasoning is fresh in working memory accelerates skill acquisition and prevents false concepts from taking root.

**Example:** Clicking "Check Answer" on an embedded web quiz instantly reveals a green checkmark and a two-sentence explanation of why the selected license combination is compatible.

See also: Feedback Message, Practice Metric, Interactive Simulation.

#### Impact Reporting

The synthesis and presentation of evidence demonstrating the real-world value of an open educational resource project—combining rubric score gains, A/B test learning outcomes, student textbook cost savings, and adoption counts—for departments, grant funders, or administrators.

Quantifying both financial savings and verified learning gains builds institutional support for ongoing OER stewardship and faculty release time.

See also: Course Material Affordability, Results Summary, Reuse Tracking.

#### Improved Version

The revised state of an open educational resource after applying and human-verifying AI-assisted enhancements across targeted quality and reusability metrics, used for the "after" rubric re-scoring and assigned to the treatment group in an A/B test.

Comparing the enhanced module against the baseline version on both the 100-point rubric and student post-tests completes the full evaluation-to-validation loop.

**Example:** Tagged as `v2.0-improved`, the enhanced chapter scores 87/100 on the rubric and includes repaired headings, WCAG-compliant alt text, complete Dublin Core metadata, and ten self-check questions.

See also: Original Version, Treatment Group, Score Gain.

Contrast with: Original Version.

#### Improvement Challenge

A practical constraint, trade-off, or technical hurdle encountered when revising an open educational resource—such as locked PDF layouts, restrictive ND licenses, subtle subject-matter nuances, or the risk of AI edits altering original meaning.

Recognizing which remediation tasks are easy for AI agents (like drafting metadata or alt text) versus which require careful human domain judgment prevents costly mistakes.

**Example:** Converting a dual-column chemistry PDF containing dozens of complex reaction diagrams into clean Markdown without corrupting chemical subscripts presents a classic technical remediation hurdle.

See also: PDF-to-Markdown Conversion, Preserving Original Meaning, Human Review of Changes.

#### Improvement Plan

A prioritized action document created after an OER evaluation that lists the specific quality and reusability metrics targeted for enhancement, the exact defects to fix, the AI-assisted workflows or human edits to execute, and the expected score gains.

Translating an evaluation report into a structured task list ensures that revision effort goes straight to the changes that matter most for learners and reusers.

**Example:** For a biology chapter scored at 64/100, the action plan targets two quality metrics (Accessibility: add 18 alt texts; Practice: generate a 10-item quiz) and two reusability metrics (Metadata: add YAML frontmatter; Modularity: split into two lessons).

See also: Lowest Metric First, OER Adaptation, Before-and-After Comparison.

#### Informed Consent

The ethical and institutional practice of explaining to students (or their parents/guardians for K-12 minors) the purpose, procedures, data privacy protections, and voluntary nature of an educational study before collecting research data.

Even in low-risk classroom curriculum evaluations, transparency and ensuring that no student's course grade is penalized by group assignment are foundational ethical duties.

**Example:** Before running the A/B comparison, the instructor explains how the two reading versions will be tested, guarantees that all data are anonymized, and gives both groups full access to the improved resource immediately after the post-test.

See also: Student Privacy in Testing, Equity Consideration, FERPA.

#### Intelligent Textbook

A modern, web-native open educational resource built around an explicit learning graph and enriched with interactive MicroSims, ISO 11179 glossaries, formative quizzes, and AI-agent workflows that support continuous evaluation and improvement.

This course both uses an intelligent textbook format and teaches educators how to upgrade traditional static OER into interactive, evidence-tested learning environments.

**Example:** Built with MkDocs Material on GitHub Pages, the OER Evaluator book combines dependency-mapped chapters, interactive p5.js simulations, automated quality scripts, and an embedded 351-term glossary.

See also: Learning Graph, MicroSim, MkDocs.

#### Inter-Rater Agreement

The degree of concordance among two or more independent evaluators—whether human reviewers or AI agents—when assigning scores to the same resource using the same rubric.

Measuring concordance tells an evaluation team whether their rubric descriptors and prompts are clear enough to support automated assessment.

**Example:** Comparing a faculty reviewer's ten metric scores against an AI agent's ten scores to see how many metrics fall within 1 point of each other measures rater concordance.

See also: Agreement Rate, Cohen's Kappa, Calibration Against Humans.

#### Interactive Simulation

A dynamic, browser-based software model that allows learners to manipulate variables through controls like sliders and buttons and observe the resulting behavior in real time.

When a concept involves multi-variable trade-offs or dynamic processes, an interactive model communicates cause and effect far better than static paragraphs.

**Example:** A web widget where learners toggle Creative Commons license elements on two source textbooks and watch a compatibility matrix update live lets them explore remix rules hands-on.

See also: MicroSim, Practice Metric, Universal Design for Learning.

#### Invented Citation

A specific type of AI hallucination in which a language model fabricates a nonexistent academic paper, author name, publication year, URL, or line-number quote either when writing content or when citing evidence in a rubric report.

Every citation generated by an AI agent during evaluation or content improvement requires direct verification against the source file or a trusted bibliographic database.

**Example:** An agent improving a psychology chapter inserts a smooth citation to "(Miller & Rodriguez, 2022, *Journal of Open Learning*)" with a DOI link that returns a 404 error because the article never existed.

See also: Hallucination, Evidence Citation, Source Verification.

#### Issue Tracking

The use of a structured ticketing board—such as GitHub Issues—where students, adopting instructors, and automated audit scripts can report typos, broken links, accessibility bugs, or content gaps and track them through resolution.

Public bug boards turn every classroom reader into a quality partner who can flag a problem in thirty seconds with an exact page URL.

See also: Feedback Channel, Maintenance Plan, GitHub Repository.

#### Jargon

Specialized, technical, or insider terminology used by experts within a discipline that is unfamiliar and confusing to novice learners when introduced without explanation.

While teaching essential disciplinary vocabulary is necessary, unexplained insider buzzwords and acronyms lower a resource's readability score.

See also: Vocabulary Level, Defined Terms, Plain Language.

#### JSON Output

A structured response formatted in JavaScript Object Notation (JSON) containing key-value pairs and arrays—such as metric IDs, integer scores, evidence arrays, and subtotals—that software programs can validate and parse directly.

When running batch evaluations or calibrating agent scores against human spreadsheets, JSON files eliminate brittle text-parsing errors.

See also: Structured Output, Batch Evaluation, Agent Evaluation Report.

#### Keyboard Navigation

The ability to reach, focus, and operate every interactive element on a webpage—including links, buttons, form controls, quizzes, and simulations—using only keyboard keys such as `Tab`, `Enter`, `Space`, and arrow keys without a mouse.

Learners with motor disabilities and blind screen reader users rely entirely on keyboard operability and visible focus indicators to interact with digital textbooks.

**Example:** A student presses `Tab` to move focus onto a MicroSim's slider control, uses the left and right arrow keys to adjust the parameter, and presses `Space` on the reset button.

See also: Screen Reader, ARIA Labels, Accessibility Metric.

#### Keywords

A list of specific topical words and phrases included in a metadata record to improve search engine indexing and help educators locate a resource by concept name.

Choosing concrete terms that match how teachers search—such as "5R permissions," "WCAG 2.1 AA," and "rubric calibration"—increases component discoverability.

**Example:** Adding `keywords: ["open educational resources", "creative commons", "license compatibility", "TASL attribution"]` helps a module surface when librarians search for licensing guides.

See also: Subject Field, Controlled Vocabulary, Component Discoverability.

#### Large Language Model

A deep-learning neural network trained on vast corpora of text and code that predicts and generates human-like language, enabling tasks such as summarization, rubric scoring, translation, and content drafting.

Understanding that these models generate probabilistic token sequences rather than consulting a verified fact database explains why they are powerful drafters yet prone to hallucinations.

See also: AI Assistant, AI Agent, Token, Hallucination.

#### Learning Gain

The individual or group improvement in mastery from before studying a resource to after studying it, calculated either as a raw score difference ($\text{Post-Test} - \text{Pre-Test}$) or as a normalized fraction of the possible improvement.

Tracking the change from baseline controls for differences in prior student preparation and isolates how much knowledge the resource actually added.

**Example:** A student who scores 3/10 on the pre-test and 8/10 on the post-test after using the improved chapter achieves a raw learning gain of $+5$ points.

See also: Pre-Test, Post-Test, Difference of Means.

#### Learning Graph

A directed acyclic graph (DAG) of educational concepts in which nodes represent discrete knowledge units and directed edges represent prerequisite relationships from foundational topics to advanced ones.

In an intelligent textbook, the concept graph serves as the master architectural blueprint that governs chapter sequencing, glossary coverage, quiz alignment, and MicroSim design.

See also: Concept Dependency, Chapter Structure, Intelligent Textbook.

#### Learning Objective

A specific, short-term instructional goal that breaks a broader learning outcome into a concrete, testable step within a single lesson or section.

Reviewers inspect chapter introductions to verify that objectives use action verbs rather than vague phrases like "understand" or "appreciate."

**Example:** "Classify a given Creative Commons license badge according to whether it permits commercial use and derivative works."

See also: Learning Outcome, Measurable Verb, Bloom's Taxonomy.

#### Learning Outcome

A formal statement describing the specific knowledge, skill, or capability that a learner will be able to demonstrate after completing a course, unit, or chapter.

Clear outcomes serve as the structural spine for evaluating alignment across a textbook's readings, simulations, and quizzes.

See also: Learning Objective, Measurable Verb, Alignment Metric.

#### License Clarity

The degree to which a resource's copyright status and open license terms are stated prominently, consistently, and unambiguously across the document and its embedded media assets.

Reviewers deduct points when a resource hides its license in an obscure repository page, states contradictory licenses in different chapters, or leaves image credits unmarked.

**Example:** Placing a consistent CC BY 4.0 badge, version link, and third-party media exception list on the copyright page and every chapter footer demonstrates high license clarity.

See also: License Statement, Open License Metric, Third-Party Content.

#### License Compatibility

The legal ability to combine two or more openly licensed works into a single derivative work or remix without violating the terms of any contributing license.

Before merging chapters, images, or simulations from different repositories, evaluators check a compatibility chart to verify that the licenses harmonize.

**Example:** A CC BY text and a CC BY-SA diagram are compatible and can be remixed together provided the combined module is released under CC BY-SA.

See also: Remix Permission, License Conflict, ShareAlike Requirement.

#### License Conflict

A legal incompatibility that occurs when two resources carry mutually exclusive license requirements, making it impossible to combine them into a single derivative work legally.

AI agents and human reviewers both examine third-party media and combined chapters to flag incompatible license pairs before publication.

**Example:** Attempting to merge a CC BY-SA chapter (which requires derivatives to allow commercial use under CC BY-SA) with a CC BY-NC chapter (which forbids commercial use) creates an irreconcilable conflict.

See also: License Compatibility, Remix Permission, License Misreading.

#### License Field

The metadata element that records the exact open license identifier, version number, and canonical legal URL governing the reuse of an educational resource.

Storing the license in a standardized field allows automated repository harvesters and AI agents to verify reuse permissions without guessing from free-text paragraphs.

See also: Metadata Record, License Statement, Automated License Detection.

#### License Misreading

An evaluation error in which a human reviewer or AI agent misinterprets the legal terms of a resource's license—such as overlooking a NonCommercial (`NC`) or NoDerivatives (`ND`) restriction, missing conflicting third-party image rights, or confusing free web access with an open license.

Because a flawed license reading can lead an educator into unlawful adaptation or redistribution, open license evidence is always double-checked by hand.

**Example:** Seeing the words "Creative Commons" in a book's footer, an uncalibrated AI agent awards 10/10 on the Open License Metric without noticing that the full badge is `CC BY-NC-ND 4.0`, which legally forbids any adaptation.

See also: Agent Error Type, License Conflict, Open License Metric.

#### License Selection

The decision by an author or adapter regarding which open license to apply when publishing an original or derivative educational resource.

In this course, educators are encouraged to select permissive licenses like CC BY whenever legally possible to maximize downstream reusability.

**Example:** After creating a new interactive physics MicroSim from scratch, the teacher selects CC BY 4.0 so colleagues worldwide can embed and modify the simulation freely.

See also: Open License, Publishing OER, Component Licensing.

#### License Statement

A visible text notice or machine-readable tag within a resource that identifies the specific license governing the work, its version number, the copyright holder, and a link to the legal code.

The rubric's open license metric deducts points when a resource lacks a clear, unambiguous notice on its title page or footer.

**Example:** A footer reading "This work by Jane Doe is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0)" provides complete clarity for reusers.

See also: Open License, License Clarity, License Statement Repair.

#### License Statement Repair

The remediation of missing, vague, or inconsistent copyright and licensing notices in an open resource by inserting a prominent, standardized license statement, canonical URL, and TASL attribution block on the title page, metadata record, and page footers.

Note that an adapter can only clarify or standardize a license that the copyright holder has already legally granted (or apply a license to the adapter's own original additions), never re-license someone else's all-rights-reserved work without permission.

**Example:** Where a repository README stated "This project is CC BY" but individual chapter pages had no notice, the maintainer adds a standard CC BY 4.0 footer and link to every page template, raising the Open License Metric score.

See also: License Statement, License Clarity, Open License Metric.

#### Link Repair

The maintenance process of fixing broken hyperlinks identified during a link check by updating moved URLs, replacing dead external pages with Internet Archive Wayback Machine snapshots, or substituting current authoritative sources.

Repairing dead links restores the Currency Metric score and prevents learners from hitting frustrating `404 Not Found` pages during study.

**Example:** After an automated link checker flags three dead government statistics URLs in Chapter 6, the reviewer replaces two with updated agency permalinks and points the third to a verified Wayback Machine archive snapshot.

See also: Link Rot, Broken Link Check, Automated Link Checker.

#### Link Rot

The gradual degradation of hyperlinks in a digital resource as external websites move, change URL structures, go offline, or place previously free pages behind paywalls.

Broken external references frustrate students and lower a resource's score on the Currency Metric until repaired or replaced with archived links.

**Example:** Five years after an open political science textbook was published, 40 percent of its links to news articles and government agency pages return "404 Not Found" errors.

See also: Broken Link Check, Automated Link Checker, Link Repair.

#### Link Sharing

The ability to direct students or colleagues to a specific chapter, section heading, glossary entry, or interactive simulation using a stable, permanent, deep-link URL.

Clean, predictable URLs with anchor IDs allow instructors to assign exact subsections inside a weekly syllabus without telling students to scroll through a massive file.

See also: Portability Metric, No-Login Access, Static Site Generator.

#### Link Text

The visible, clickable words inside a hyperlink that describe the destination or purpose of the link to the reader.

Under WCAG guidelines, link phrases should clearly identify where the link goes even when read out of context in a screen reader's link list, avoiding vague phrases like "click here" or raw URLs.

**Example:** Writing "Read the [Creative Commons Attribution 4.0 License Summary](https://creativecommons.org/licenses/by/4.0/)" is descriptive and accessible, whereas writing "To see the license, [click here](https://creativecommons.org/licenses/by/4.0/)" is ambiguous.

See also: Screen Reader, Accessibility Metric, WCAG 2.1 AA.

#### LMS Import

The process of transferring structured course content, modules, pages, and question banks into a school's Learning Management System (such as Canvas, Moodle, Brightspace, or Blackboard) using standardized package formats.

Resources that provide ready-to-import course cartridges or QTI quiz packages save adopting faculty hours of manual copy-pasting.

**Example:** A college instructor downloads an open textbook's Common Cartridge file and imports it into Canvas, automatically populating twelve weekly modules and twelve graded quizzes.

See also: Common Cartridge, LTI Integration, Portability Metric.

#### Local Reviewer Role

An institutional responsibility held by a trained teacher, librarian, or instructional designer who serves as the designated specialist on a school, department, or district committee for evaluating candidate OER and auditing AI-generated adaptations.

Building in-house expertise ensures that schools can sustain high-quality open curriculum adoption without relying on outside consultants.

**Example:** After earning the OER Evaluator certificate, a community college librarian is appointed as the campus specialist who reviews faculty OER adaptation grants and verifies license compatibility before publication.

See also: Reviewer, Train-the-Trainer, Professional Development.

#### Lowest Metric First

A prioritization strategy in OER improvement that directs remediation effort to a resource's lowest-scoring rubric metrics—especially any metric below the adoption threshold—before polishing metrics that already score 8 or above.

Raising a metric from 2/10 to 8/10 removes a critical blocker for students or teachers and yields a far larger jump in usability and total score than nudging an 8/10 up to 9/10.

**Example:** Faced with a chapter that scores 9 on Accuracy, 8 on Readability, 2 on Accessibility, and 3 on Practice, the teacher focuses the AI agent on generating alt text and self-check quizzes first.

See also: Improvement Plan, Adoption Threshold, Score Gain.

#### LRMI

The Learning Resource Metadata Initiative, a metadata specification maintained by DCMI and integrated into Schema.org that defines education-specific properties such as `educationalAlignment`, `typicalAgeRange`, `educationalUse`, and `timeRequired`.

Adding education-specific tags beyond basic Dublin Core tells search engines and AI agents not just what a webpage is about, but how it functions pedagogically in a classroom.

**Example:** Marking up a MicroSim page with `lrmi:educationalUse: "interactive simulation"` and `lrmi:typicalAgeRange: "14-18"` allows instructional search tools to filter specifically for high school interactive labs.

See also: Schema.org Markup, Dublin Core, Machine-Readable Metadata.

#### LTI Integration

Learning Tools Interoperability, a technical standard from 1EdTech that connects external interactive learning applications, simulations, or auto-graded homework systems securely to a host LMS, optionally passing student scores back to the gradebook.

While simple read-only embedding works via an `iframe`, LTI connections are used when an institution wants external practice scores recorded automatically in the course gradebook.

**Example:** A calculus department connects an open homework server to its LMS via LTI so students launch practice problems with single sign-on and see their completion points appear in Canvas automatically.

See also: LMS Import, Portability Metric, Student Data Privacy.

#### Machine-Readable Metadata

Descriptive catalog information formatted in a structured syntax—such as YAML frontmatter, JSON-LD, XML, or HTML `<meta>` tags—that software scripts and AI agents can parse automatically without human interpretation.

When metadata is structured for machines, automated repository harvesters and evaluation agents can verify completeness and license terms across hundreds of chapters in seconds.

**Example:** Storing a chapter's metadata in a structured YAML header allows a Python script to validate all six required fields automatically, whereas burying that information in an unstructured introductory paragraph does not.

See also: Metadata Record, Schema.org Markup, Automated License Detection.

#### Maintenance Plan

A documented schedule and stewardship strategy defining how an open educational resource will be periodically checked for broken links, updated for factual currency, monitored for community issue reports, and re-verified over time.

Even a textbook that scores 95/100 on publication day will gradually suffer from link rot and outdated statistics unless someone schedules regular upkeep.

**Example:** A department's stewardship plan specifies running an automated link and accessibility scan before every fall semester and conducting a full content currency review every two years.

See also: Link Rot, Issue Tracking, Currency Metric.

#### Manual Evaluation

The human-led process of inspecting an open educational resource by hand against the ten-metric rubric, assigning 0–10 scores to each criterion, and recording verifiable evidence citations on a rubric worksheet.

Learning to score a resource manually first builds the deep domain judgment needed to write effective AI prompts and catch agent scoring errors later.

**Example:** Before touching an AI tool, a teacher spends forty-five minutes reading Chapter 1 of a candidate biology textbook, testing its links and alt text by hand, and completing a ten-metric worksheet.

See also: Rubric Worksheet, Evidence Recording, Agent Scoring.

#### Markdown

A lightweight plain-text markup syntax that uses simple punctuation characters (such as `#` for headings, `*` for lists, and `[]()` for links) to format structured documents that convert cleanly into HTML and other publishing formats.

Because it is human-readable, version-control friendly, and ideal for AI agent processing, plain-text markup is the preferred source format for intelligent textbooks in this course.

**Example:** Writing `## Learning Outcomes` and a bulleted list in a `.md` file produces clean semantic `<h2>` and `<ul>` tags when compiled by MkDocs.

See also: Open File Format, Static Site Generator, PDF-to-Markdown Conversion.

#### Mean Absolute Difference

A statistical measure of scoring discrepancy calculated by taking the average of the absolute point differences ($|S_{\text{human}} - S_{\text{agent}}|$) across all evaluated metrics or resources, ignoring whether errors are positive or negative.

Unlike a simple average of raw differences (where a +4 inflation on one metric and a -4 harsh score on another would cancel out to zero), averaging the absolute values captures the true magnitude of disagreement.

**Example:** If the point gaps between a teacher and an agent across the five quality metrics are $+1, -2, 0, +3,$ and $-2$, the absolute differences are $1, 2, 0, 3, 2$, yielding a mean absolute difference of $8 / 5 = 1.6$ points per metric.

See also: Score Difference Threshold, Calibration Against Humans, Agreement Rate.

#### Mean Score

The arithmetic average ($\bar{x}$) of a set of numeric scores—calculated by summing all individual scores in a group and dividing by the number of participants in that group ($n$).

Computing the average pre-test, post-test, and learning gain for both the control and treatment groups is the first step in summarizing A/B test outcomes.

**Example:** If the 20 students in the Treatment Group earn a combined total of 168 points on a 10-point post-test, their group average is $168 / 20 = 8.4$ points.

See also: Difference of Means, Effect Size, Learning Gain.

#### Measurable Verb

An action word in a learning outcome or objective—such as define, calculate, compare, critique, or design—that specifies an observable behavior that can be directly assessed.

Outcomes written with observable action verbs make it straightforward for reviewers and AI agents to verify whether quiz questions match the stated goals.

**Example:** Replacing the vague phrase "Students will know about alt text" with the observable action "Students will write WCAG-compliant alt text for three data charts" makes the objective testable.

See also: Learning Objective, Bloom's Taxonomy, Alignment Metric.

#### Metadata Completeness

The proportion of required descriptive fields—specifically title, author, subject, grade level, license, and description—that are present, non-empty, and accurately populated in a resource's metadata record.

Under the Metadata Metric, reviewers and AI scripts check each of the six core fields and deduct points whenever fields are missing, placeholder-filled, or inconsistent with the text.

**Example:** A resource that includes title, author, and license in its YAML frontmatter but omits subject, grade level, and description achieves only 50% completeness on the core metadata checklist.

See also: Metadata Metric, Metadata Record, Metadata Generation.

#### Metadata Generation

The use of an AI agent or script to analyze a chapter's content and automatically draft a complete, standardized metadata record—including title, author, subject, target grade level, license, description, and Schema.org/LRMI tags.

Because writing catalog fields by hand across dozens of chapters is tedious, automated drafting quickly brings a textbook from 0/10 to 10/10 on the Metadata Metric once verified by the author.

See also: Metadata Metric, Metadata Record, Metadata Completeness.

#### Metadata Metric

The third reusability metric (Metric 8) in the ten-metric rubric, which evaluates whether a resource includes complete, accurate, human- and machine-readable descriptive metadata covering title, author, subject, grade level, license, and summary description.

Even the highest-quality open textbook remains invisible to educators and AI search agents if it lacks structured catalog records that describe what it teaches and who it is for.

**Example:** A textbook repository that includes YAML frontmatter on every page, a complete Dublin Core record, and Schema.org/LRMI JSON-LD tags in its HTML head earns 10 out of 10 on this metric.

See also: Metadata Record, Dublin Core, Metadata Completeness.

#### Metadata Record

A structured set of descriptive fields—such as title, creator, subject keywords, target audience, publication date, and license—that summarizes an educational resource for cataloging, search discovery, and attribution.

In OER evaluation, reviewers check both the visible frontmatter of a resource and its underlying HTML or repository files for a complete descriptive record.

**Example:** A YAML block at the top of a chapter file listing `title`, `author`, `subject`, `grade_level`, `license`, and `description` serves as a portable metadata record.

See also: Metadata Metric, Dublin Core, Machine-Readable Metadata.

#### Metric Score

The numeric value assigned to a single rubric criterion after evaluating the evidence found in a resource against the criterion's scoring descriptors.

Each individual score in the OER Evaluator rubric ranges from 0 to 10 points and contributes to either the quality or reusability subtotal.

**Example:** Because a chapter includes alt text on only half of its images and skips heading levels, the reviewer assigns a score of 5 out of 10 on the accessibility criterion.

See also: Rubric Metric, Score Scale, Evidence for a Score.

#### MicroSim

A lightweight, self-contained, openly licensed interactive educational simulation built with standard web technologies (such as HTML, CSS, and p5.js or Chart.js) designed to teach one specific concept and embed cleanly via an `iframe`.

In intelligent textbooks, these modular simulations boost both the Practice Metric (by offering active exploration) and the Modularity and Portability metrics (by working anywhere via a simple embed code).

**Example:** The OER Evaluator textbook embeds a standalone `rubric-calculator` simulation in `docs/sims/rubric-calculator/main.html` where teachers adjust ten metric sliders to see quality vs. reusability subtotals and adoption bands update in real time.

See also: Interactive Simulation, Iframe Embedding, MicroSim Building.

#### MicroSim Building

The design and coding of a self-contained interactive browser simulation—typically using HTML, CSS, and p5.js or Chart.js inside `docs/sims/<sim-id>/`—that lets learners manipulate variables to explore a complex concept from the chapter.

Replacing a static wall of explanatory text with a hands-on interactive model simultaneously elevates the Practice, Modularity, and Portability metrics.

See also: MicroSim, Interactive Simulation, Practice Metric.

#### MkDocs

A Python-based static site generator—commonly paired with the Material theme—designed for building clean, searchable, mobile-responsive documentation and intelligent textbooks from Markdown files and a single YAML configuration file.

The OER Evaluator textbook itself is built with this tool, using `mkdocs.yml` as the single source of navigation truth and `mkdocs build --strict` to verify that every link and page resolves cleanly.

See also: Static Site Generator, GitHub Pages, Intelligent Textbook.

#### Modular Content

Instructional material structured as discrete, self-contained units—such as individual lessons, chapters, quizzes, or simulations—that can be separated, rearranged, or combined into new courses without breaking comprehension.

Designing chapters as independent building blocks allows a college instructor to swap out Chapter 5 or embed just one simulation into an existing syllabus.

**Example:** Because each topic in an open data science course is packaged in its own folder with local images and explicit prerequisites, a high school teacher can adopt three specific modules for an elective unit.

See also: Modularity Metric, Standalone Component, Chapter Splitting.

#### Modularity Metric

The second reusability metric (Metric 7) in the ten-metric rubric, which evaluates whether a resource is divided into self-contained, appropriately sized chapters, sections, and components that can be reused, reordered, or embedded independently.

Instructors rarely adopt a massive textbook cover-to-cover if they only need two units; modular structure makes partial adoption and remixing effortless.

**Example:** A textbook organized into twelve standalone chapters—each with its own learning objectives, glossary definitions, self-contained figures, and independent URL—scores 9 out of 10 on modularity.

See also: Modular Content, Standalone Component, Cross-Reference Dependence.

#### Multi-Agent Review

An evaluation architecture in which two or more independent AI agents—often configured with different prompts, roles, or underlying models—evaluate the same resource or verify each other's findings to catch errors and measure agreement.

When two independent agents disagree by more than 2 points on a metric or when a critic agent flags an unverified quote, the workflow highlights that specific item for human inspection.

**Example:** A primary scoring agent drafts the ten metric ratings for a physics chapter, and a separate verification agent checks every quoted line number and license claim against the raw Markdown file before the teacher sees the report.

See also: Second-Agent Cross-Check, Agent Disagreement, Agent Workflow.

#### Multiple-Choice Question

A selected-response assessment item consisting of a question stem, one correct or best answer (the key), and two or more plausible incorrect options (distractors).

Because selected-response items can be graded automatically in a web browser, they are the primary format used for immediate-feedback quizzes in open textbooks.

**Example:** A question stem describes a textbook with no license notice and asks the learner to select its default legal status from four choices: CC BY, Public Domain, Fair Use, or All Rights Reserved.

See also: Distractor Quality, Answer Key, Feedback Message.

#### No-Login Access

The availability of an online educational resource for immediate reading, interaction, and downloading via a public URL without requiring students or teachers to create an account, enter an email address, or sign in.

Mandatory registration walls create friction for classroom adoption, block AI evaluation agents from inspecting pages, and raise student data privacy concerns under FERPA.

**Example:** Because the OER Evaluator textbook is hosted on public GitHub Pages, any student can click a chapter link on a syllabus and begin reading immediately without a password prompt.

See also: Portability Metric, Student Data Privacy, Link Sharing.

#### NoDerivatives Requirement

The license condition denoted by "ND" that permits copying and redistributing only verbatim copies of a work while prohibiting the distribution of modified, translated, or remixed versions.

In OER evaluation, the presence of an ND clause is a major reusability blocker because it forbids fixing accessibility errors, updating outdated facts, or modularizing chapters.

See also: CC BY-ND, CC BY-NC-ND, Revise Permission.

#### NonCommercial Requirement

The license condition denoted by "NC" that restricts uses of a work to those not primarily intended for or directed toward commercial advantage or monetary compensation.

Reviewers note this restriction during evaluation because it can complicate printing through commercial bookstores or hosting on ad-supported platforms.

**Example:** Under an NC restriction, a public school can distribute free digital copies of a workbook, but an online marketplace seller cannot print and sell bound copies for a profit margin.

See also: CC BY-NC, CC BY-NC-SA, Open License Metric.

#### OER Adaptation

The process of modifying, updating, reorganizing, or enhancing an existing open educational resource to fit local learning outcomes, accessibility standards, or student reading levels.

Chapters on AI-assisted improvement guide educators through systematic adaptations that raise both quality and reusability scores.

**Example:** An instructor takes a college-level open biology chapter, uses an AI agent to simplify the vocabulary for tenth-grade readers, and inserts five self-check questions.

See also: Revise Permission, Derivative Work, Improvement Plan.

Contrast with: OER Adoption, OER Creation.

#### OER Adoption

The instructional decision and process of selecting an existing open educational resource and assigning it in a course with little or no modification to its content.

When a resource scores high on quality metrics during evaluation, faculty can adopt it directly without spending time on major revisions.

**Example:** After scoring an open macroeconomics textbook at 88 out of 100 on the rubric, a department votes to assign it as the primary text for all fall sections.

See also: Adoption Decision, OER Adaptation, Resource Selection.

#### OER Clearinghouse

A centralized public catalog, referendum index, or federated search portal—such as OER Commons, MERLOT, or Mason OER Metafinder—that aggregates metadata records and links to openly licensed resources hosted across many different websites and repositories.

Registering a newly published or improved textbook in major index portals maximizes its discoverability for educators who do not browse GitHub directly.

**Example:** After deploying an improved environmental science textbook to GitHub Pages, the author submits its URL and Dublin Core metadata record to OER Commons so K-12 teachers searching by Next Generation Science Standards can find it.

See also: OER Repository, Metadata Record, Component Discoverability.

#### OER Creation

The authoring of an entirely new educational resource from scratch and releasing it under an open license for public use.

Although this course focuses on evaluating and improving existing materials rather than authoring full books from scratch, teachers often create new modular components like quizzes and MicroSims.

**Example:** A computer science teacher writes a brand-new interactive tutorial on recursion and releases the Markdown and JavaScript files under a CC BY 4.0 license.

See also: Publishing OER, Reusable Component, OER Adaptation.

#### OER Quality

The degree to which an open educational resource is accurate, up to date, aligned with learning outcomes, readable for its target audience, accessible to all learners, and supported by practice with feedback.

In the course rubric, pedagogical soundness is measured across five dedicated metrics worth up to 50 points of the total score.

See also: Quality Dimension, Quality Subtotal, Quality Versus Reusability.

#### OER Repository

A digital database, library, or platform that hosts, indexes, and provides search access to openly licensed educational materials and their descriptive metadata.

Evaluators use repositories both to locate candidate textbooks for review and to share improved versions with the broader teaching community.

**Example:** Platforms such as OER Commons, MERLOT, LibreTexts, and OpenStax Textbook Library allow instructors to filter open materials by subject, grade level, and license type.

See also: OER Clearinghouse, Metadata Record, Publishing OER.

#### Offline Access

The capability for students and teachers to download, store, and use an educational resource—including its text, images, and practice questions—on a local device without an active internet connection.

In rural districts, developing regions, correctional education programs, or households with unstable broadband, downloadable packages are essential for equitable learning.

**Example:** Providing a downloadable ZIP archive of the compiled static HTML site and a print-friendly PDF allows students to study the entire textbook during a bus commute with no Wi-Fi.

See also: Retain Permission, Export Format, Equity Consideration.

#### Open Educational Resource

A teaching, learning, or research material that resides in the public domain or carries an open license permitting anyone to retain, reuse, revise, remix, and redistribute it at no cost.

Evaluating and improving these openly licensed materials using a ten-metric rubric and AI agents is the central focus of this textbook.

**Example:** An introductory statistics textbook published under a CC BY 4.0 license that any instructor can download, edit, and share with students for free is a classic instance.

See also: The 5R Permissions, Open License, Open Textbook.

Contrast with: Commercial Textbook, Free Resource.

#### Open File Format

A published, non-proprietary file specification—such as Markdown (`.md`), HTML (`.html`), SVG (`.svg`), CSV (`.csv`), or EPUB (`.epub`)—that is free of legal restrictions and can be read and edited using free, cross-platform software tools.

Storing OER in vendor-neutral formats ensures that teachers and AI agents can inspect and modify the content without purchasing expensive commercial software licenses.

See also: Source Format, Markdown, HTML.

Contrast with: Platform Lock-In, PDF-Only Distribution.

#### Open License

A standardized legal permission attached by a copyright holder to a creative work that grants the public advance authorization to use, copy, modify, and share the work under specified conditions.

Without a clearly stated open license, a resource defaults to all-rights-reserved copyright and cannot be legally adapted or redistributed.

**Example:** Creative Commons licenses and open-source software licenses like the MIT License grant upfront legal permissions to users worldwide without requiring individual contracts.

See also: Creative Commons, License Statement, Open License Metric.

Contrast with: Proprietary License, All Rights Reserved.

#### Open License Metric

The first reusability metric (Metric 6) in the ten-metric rubric, which evaluates whether a resource carries a clearly visible, permissive open license that enables all 5R permissions without conflicting third-party restrictions.

Because legal permission is the gateway to every adaptation workflow, a score of 0 or 2 on this metric blocks teachers from legally publishing improved versions of the resource.

See also: Open License, License Clarity, The 5R Permissions.

#### Open Pedagogy

An instructional approach in which students actively participate in creating, revising, or improving openly licensed educational materials rather than merely consuming disposable assignments.

Student contributors can help author practice problems, verify citations, or build examples that remain in the textbook for future cohorts.

See also: Open Educational Resource, OER Adaptation, Community Contribution.

#### Open Textbook

A complete, structured textbook published under an open license and made freely available online for students and instructors to download, adapt, and print.

Full-length textbooks are the primary resource type evaluated with the 100-point rubric in this course.

**Example:** An OpenStax psychology volume that faculty can assign online for zero cost or customize by reordering chapters for a local syllabus illustrates this format.

See also: Open Educational Resource, Commercial Textbook, OER Adoption.

#### Original Version

The baseline, unedited state of an open educational resource prior to executing an improvement plan, used both for the "before" rubric evaluation and as the instructional material for the control group in an A/B test.

Archiving a clean snapshot of the starting resource ensures that before-and-after rubric comparisons and classroom experiments remain reproducible.

**Example:** Before running any AI remediation scripts, the teacher tags the baseline commit as `v1.0-original` in Git and records its initial 58/100 rubric score.

See also: Improved Version, Control Group, Before-and-After Comparison.

Contrast with: Improved Version.

#### Outcome Coverage

The extent to which the explanatory text, examples, and activities in a resource thoroughly address every stated learning outcome without omitting promised topics or including irrelevant tangents.

When an AI agent audits a chapter for alignment, it checks each stated objective against the body headings and paragraphs to confirm complete coverage.

**Example:** If a chapter lists four learning objectives at the top of the page but only explains the first three in the body text, its coverage is incomplete.

See also: Alignment Metric, Content Gap, Curriculum Map.

#### Outcome Measure

A specific quantitative or qualitative variable—such as post-test score, pre-to-post learning gain, module completion rate, time on task, or student satisfaction rating—recorded during an A/B test to evaluate how well a resource supported learners.

Selecting an assessment measure that directly aligns with the chapter's stated learning outcomes ensures the experiment tests real mastery rather than superficial trivia.

See also: Pre-Test, Post-Test, Completion Rate, Time on Task.

#### Outdated Content

Information, examples, statistics, software instructions, or terminology in a learning resource that has been superseded by newer research, policy changes, or technological advances.

Identifying obsolete passages during an evaluation creates a clear target list for AI-assisted content updates.

**Example:** An astronomy chapter published in 2004 that still lists Pluto as one of the nine major planets of the solar system contains outdated scientific classification.

See also: Currency Metric, Content Update, Publication Date.

#### Overconfident Score

A rubric rating assigned by an AI agent with authoritative, certain-sounding justification despite lacking sufficient evidence, overlooking clear defects in the text, or guessing on criteria the agent could not actually inspect.

Language models often adopt a confident tone even when they failed to inspect embedded media or external links, making independent evidence checks essential.

**Example:** An agent writes "Portability Metric: 10/10 — All interactive simulations load seamlessly on mobile browsers and export cleanly to Canvas," even though the agent only read a plain-text Markdown file and never opened a browser.

See also: Score Inflation, Agent Error Type, Verification Step.

#### PDF-Only Distribution

The practice of releasing an educational resource exclusively as a Portable Document Format (`.pdf`) file without providing the underlying Markdown, HTML, or word-processing master files.

Because PDFs lock text into fixed page coordinates and split paragraphs into visual lines, distributing only a PDF severely penalizes a resource on the Editable Source Metric.

**Example:** When an institution uploads a 300-page PDF textbook to a repository after losing the original InDesign and Word files, adapters are forced to run error-prone PDF-to-Markdown conversion before making edits.

See also: Editable Source Metric, PDF-to-Markdown Conversion.

Contrast with: Source Format, Open File Format.

#### PDF-to-Markdown Conversion

The technical workflow of extracting text, headings, lists, tables, mathematical formulas, and image files from a static PDF document and restructuring them into clean, editable Markdown source files.

Converting a PDF-only OER into version-controlled Markdown unlocks the Editable Source Metric and enables every subsequent AI improvement workflow.

**Example:** Using an optical layout parser and an AI cleanup pass, an instructional designer converts a 40-page CC BY PDF workbook into twelve clean `.md` files with extracted `.png` figures and native Markdown tables.

See also: PDF-Only Distribution, Markdown, Editable Source Metric.

#### Peer Review

The structured evaluation of an educator's rubric report, AI improvement plan, or adapted OER module by one or more fellow colleagues using standardized criteria and constructive evidence-based feedback.

Having a colleague inspect your before-and-after rubric comparison and human verification log catches blind spots before a resource is published or submitted for certification.

See also: Expert Review, Submission Review, Local Reviewer Role.

#### Pilot Test

A small-scale preliminary trial of an improved educational resource, quiz, or evaluation workflow with a handful of students or colleagues to catch obvious logistical errors, broken links, or confusing instructions before running a full classroom A/B test.

Having even five students walk through the pre-test, reading link, and post-test beforehand prevents a broken URL or mistyped answer key from ruining a 60-student experiment.

**Example:** Two days before the main classroom trial, the instructor asks four student teaching assistants to complete the online module and post-test, discovering and fixing a broken iframe path on mobile Safari.

See also: A/B Test, Sample Size, Qualitative Feedback.

#### Plain Language

A clear, direct writing style that uses active voice, short sentences, familiar everyday words, and logical organization so readers can understand the message on the first reading.

Adopting plain prose improves comprehension for all students, especially multilingual learners and readers with cognitive or learning differences.

**Example:** Writing "You can copy, edit, and share this book if you credit the author" communicates the legal rule far more clearly than a 60-word passive legalistic clause.

See also: Readability Metric, Jargon, Reading Level Rewrite.

#### Platform Lock-In

A technical dependency in which an educational resource relies on proprietary software, closed databases, or vendor-specific hosting features that prevent educators from moving, hosting, or editing the material elsewhere.

Even if a resource displays a Creative Commons badge in its footer, trapping the content inside a closed platform that cannot be exported defeats practical reusability.

**Example:** An online workbook built inside a proprietary SaaS platform that offers no HTML, Markdown, or Common Cartridge export locks teachers into paying for or staying on that specific website forever.

See also: Portability Metric, Editable Source Metric, Open File Format.

#### Portability Metric

The fifth reusability metric (Metric 10) in the ten-metric rubric, which evaluates how easily a resource can be accessed, viewed, embedded, downloaded, and imported across different browsers, devices, offline environments, and learning management systems without login walls or proprietary lock-in.

Even a well-written, openly licensed textbook fails teachers and students if it requires a mandatory account login, breaks on mobile screens, or refuses to embed in a school's LMS.

**Example:** A mobile-responsive static textbook site that requires zero login, works across all modern browsers, offers offline downloads, and embeds cleanly via `iframe` earns 10 out of 10 on this metric.

See also: No-Login Access, Browser Compatibility, Platform Lock-In.

#### Post-Test

An aligned assessment administered to students in both the control and treatment groups *after* they finish studying their respective versions of the educational resource, measuring their mastery of the learning outcomes.

To ensure fair comparison, both groups take the exact same post-assessment under identical time and testing conditions.

**Example:** After a 30-minute study session with either the original or improved chapter, all students complete the same 10-point mastery quiz so the instructor can compare group performance.

See also: Pre-Test, Learning Gain, Outcome Measure.

Contrast with: Pre-Test.

#### Practice Metric

The fifth quality metric in the ten-metric rubric, which evaluates whether a resource includes frequent, aligned formative assessments, practice problems, interactive activities, and immediate explanatory feedback that help learners verify mastery.

Reading passive prose without opportunities to test understanding produces an illusion of competence; strong OER embed active retrieval throughout every chapter.

**Example:** A chapter that includes embedded self-check questions after each section, a ten-question multiple-choice quiz with detailed answer explanations, and an interactive MicroSim earns 10 out of 10 on this metric.

See also: Formative Assessment, Immediate Feedback, Retrieval Practice.

#### Practice Problem

An open-ended exercise, scenario, or calculation task in an educational resource that requires the learner to apply a procedure or analyze a realistic case rather than selecting from preset options.

Combining selected-response quizzes with hands-on exercises ensures learners can perform authentic tasks like scoring a real textbook excerpt or writing a TASL attribution.

**Example:** An end-of-chapter exercise provides a flawed 300-word textbook passage with two broken links and an uncredited chart, asking the learner to score it on three metrics and write the evidence notes.

See also: Worked Solution, Worked Example, Practice Metric.

#### Practice Question Generation

The use of an AI agent to create aligned formative assessment items—including self-check questions, multiple-choice quizzes with diagnostic distractors, and worked practice problems—mapped directly to a chapter's learning outcomes and Bloom cognitive levels.

Generating targeted quizzes and immediate feedback explanations is one of the fastest ways to boost a passive reading resource on the Practice Metric.

**Example:** Prompted with a chapter's four learning objectives and text, an agent generates an eight-question multiple-choice quiz where every incorrect option includes a specific feedback message explaining the underlying misconception.

See also: Practice Metric, Quiz, Distractor Quality.

#### Pre-Test

A short baseline assessment administered to students in both the control and treatment groups *before* they read the assigned educational resource, measuring their prior knowledge of the target concepts.

Measuring starting knowledge confirms whether the two groups began on an equal footing and allows the teacher to calculate individual learning gains.

**Example:** At the start of Monday's class, all 50 students complete a 10-point diagnostic quiz on Creative Commons licenses, averaging 3.4 out of 10 in both groups before opening the reading.

See also: Post-Test, Learning Gain, Prerequisite Knowledge.

Contrast with: Post-Test.

#### Prerequisite Knowledge

The prior concepts, vocabulary, or skills that a learner needs to possess before starting a new resource, chapter, or module in order to succeed.

Stating prerequisites clearly in a chapter's metadata and opening summary helps both students and adopting teachers judge readiness and modular fit.

**Example:** A chapter on calibrating AI agents against human reviewers lists familiarity with the ten-metric rubric and basic mean-difference calculations as required background.

See also: Audience Fit, Concept Dependency, Scope and Sequence.

#### Preserving Original Meaning

The editorial principle that when simplifying prose, translating language, or splitting chapters during an OER adaptation, the core disciplinary facts, logical qualifications, and learning outcomes remain completely accurate and intact.

A reading-level rewrite that drops essential scientific conditions just to shorten sentences raises the Readability Metric at the unacceptable cost of damaging the Accuracy Metric.

**Example:** When simplifying a legal explanation of Creative Commons licenses for ninth graders, the editor replaces dense Latinate phrasing with plain English while carefully keeping the exact legal distinction between commercial and noncommercial uses.

See also: Reading Level Rewrite, Human Review of Changes, Accuracy Metric.

#### Primary Source

An original document, first-hand account, peer-reviewed research dataset, statutory text, or experimental record created directly at the time under study or by the original researchers.

High-quality educational resources ground key empirical claims and historical interpretations in original evidence rather than unverified summaries.

See also: Secondary Source, Source Citation, Citation Quality.

#### Professional Development

Ongoing structured learning, workshops, peer coaching, and credentialing pursued by educators, librarians, and instructional designers to expand their pedagogical expertise, open licensing fluency, and AI evaluation skills.

Positioning AI-assisted OER evaluation as a core professional skill empowers educators to take ownership of their curriculum materials while continuously improving student learning.

**Example:** A school district awards twenty hours of continuing education credit to teachers who complete the OER Evaluator course and publish an improved open module for their grade-level team.

See also: Teacher Training Workshop, Certificate, Local Reviewer Role.

#### Prompt

The specific natural-language instruction, question, context, and constraints provided as input to a large language model or AI agent to direct its task execution.

Clear, well-structured instructions that specify the rubric criteria and require exact line-number evidence dramatically improve the accuracy of AI evaluations.

**Example:** Asking "Is this chapter good?" is a vague input that yields generic praise, whereas providing the exact 0–10 Accessibility Metric descriptors and asking for a Markdown table of missing alt attributes is an effective instruction.

See also: Prompt Template, System Prompt, Rubric Prompt.

#### Prompt Iteration

The empirical cycle of testing a prompt on sample resources, inspecting the agent's errors or scoring drift against human benchmarks, modifying the instructions or examples, and re-testing until performance stabilizes.

No rubric prompt works perfectly on the first draft; systematic refinement is how educators eliminate recurring blind spots like license misreadings or score inflation.

**Example:** After noticing that Draft 1 of a prompt consistently gave 9/10 on the Practice Metric even when answer keys were missing, the author adds an explicit rule capping scores without solutions at 5/10 and tests Draft 2.

See also: Prompt Refinement, Calibration Against Humans, Agent Error Rate.

#### Prompt Refinement

Targeted edits made to an AI agent's rubric prompt—such as clarifying ambiguous descriptors, adding explicit point caps for missing features, or inserting calibrated few-shot examples—based on errors discovered during human calibration.

Iterative adjustments turn every discovered agent mistake into a permanent guardrail that prevents the same error on future textbooks.

See also: Prompt Iteration, Calibration Against Humans, Score Inflation.

#### Prompt Template

A reusable prompt structure containing fixed instructional text, rubric criteria, and output formatting rules alongside variable placeholders (such as `{{chapter_text}}` or `{{target_grade_level}}`) that are filled in for each run.

Using a standardized template guarantees that when evaluating twenty chapters across a textbook, every single chapter is judged by the exact same instructions.

**Example:** An evaluation template includes the ten metric definitions verbatim and ends with placeholders for `{{resource_title}}`, `{{declared_grade_level}}`, and `{{markdown_content}}`.

See also: Prompt, Rubric Prompt, Batch Evaluation.

#### Proprietary License

A restrictive legal agreement or terms-of-use contract that retains exclusive ownership with the publisher and grants users only limited, conditional access while forbidding copying, modification, or sharing.

Resources governed by proprietary terms fail the open license metric and cannot enter the AI improvement and republication pipeline.

**Example:** An end-user license agreement (EULA) on a publisher's homework platform that prohibits downloading questions or sharing screenshots is a proprietary contract.

See also: All Rights Reserved, Commercial Textbook.

Contrast with: Open License.

#### Public Domain

The legal status of creative works that are not protected by copyright law and may be freely used, modified, and shared by anyone without permission or attribution requirements.

Works in this category receive full points on the open license metric because they impose zero legal restrictions on educational reuse.

See also: CC0 Dedication, Copyright, Open Educational Resource.

Contrast with: All Rights Reserved.

#### Publication Date

The calendar date on which a specific version or edition of an educational resource was formally released to the public.

Checking the release date in a book's frontmatter or metadata record provides an initial signal of whether its examples and statistics may need refreshing.

**Example:** Seeing a 2016 release date on an artificial intelligence textbook alerts the reviewer to check whether modern transformer architectures and large language models are missing.

See also: Currency Metric, Revision History, Metadata Record.

#### Publishing OER

The process of compiling, licensing, formatting, and deploying an original or improved open educational resource to a public web server and indexing it in open repositories so educators and learners worldwide can access and reuse it.

Completing the OER cycle means sharing your verified improvements back to the educational commons rather than keeping repaired files isolated on a personal hard drive.

**Example:** After evaluating, improving, and A/B testing an open statistics module, the instructor compiles the Markdown source with MkDocs, deploys the site to GitHub Pages under CC BY 4.0, and registers the URL in OER Commons.

See also: Redistribute Permission, Static Site Generator, OER Clearinghouse.

#### Pull Request

A formal proposal submitted in a Git hosting platform asking the maintainers of an upstream repository to review and merge a set of committed improvements—such as typo fixes, alt text additions, or new quizzes—from a branch or fork.

When an educator uses AI agents to repair broken links or add WCAG alt text to an open textbook, submitting a merge proposal shares those improvements back with every school using the original book.

**Example:** After generating and verifying descriptive alt text for 40 diagrams in a forked biology textbook, the reviewer opens a merge request so the original authors can incorporate the accessibility upgrade with one click.

See also: Fork, GitHub Repository, Community Contribution.

#### Qualitative Feedback

Open-ended written comments, interview observations, or think-aloud notes collected from students or teachers that describe *why* a resource worked well or *where* specific passages, diagrams, or controls caused confusion.

Student comments often pinpoint exact usability flaws—such as a confusing slider label or an ambiguous quiz question—that raw test numbers alone cannot explain.

**Example:** Several students in the A/B test write on their survey that the new TASL attribution callout box made the legal rule click immediately, while noting that Question 4 in the quiz had two answers that looked identical.

See also: Student Survey, Results Summary, Pilot Test.

#### Quality Dimension

The half of the OER Evaluator rubric comprising five 10-point metrics—accuracy and currency, alignment, readability, accessibility, and practice—that assess how well a resource supports student learning.

Separating pedagogical effectiveness from technical and legal reusability helps reviewers diagnose whether a resource is good for students right now versus easy for teachers to adapt later.

**Example:** A beautifully written, accessible PDF textbook with great quizzes scores 48 out of 50 on this dimension even if its locked file format makes it hard to edit.

See also: OER Quality, Quality Subtotal, Reusability Dimension.

#### Quality Rubric

A structured evaluation instrument containing defined criteria, numeric point scales, and performance descriptors used to judge the instructional and technical merit of an educational resource.

Using a standardized rubric ensures that both human educators and AI agents evaluate textbooks against identical, transparent expectations.

**Example:** Instead of writing vague general impressions, a department uses a shared scoring rubric so every reviewer rates textbook accessibility and modularity on the same 0-to-10 scale.

See also: Ten-Metric Rubric, Rubric Metric, Scoring Descriptor.

#### Quality Subtotal

The sum of the five quality metric scores—accuracy and currency, alignment, readability, accessibility, and practice—yielding a value from 0 to 50 points.

Tracking this subtotal separately from reusability shows whether a resource is pedagogically strong for students even if it requires technical reformatting.

**Example:** A textbook that scores 9 on Accuracy/Currency, 8 on Alignment, 8 on Readability, 7 on Accessibility, and 8 on Practice achieves a quality subtotal of 40 out of 50.

See also: Quality Dimension, Reusability Subtotal, Total Score.

#### Quality Versus Reusability

The analytical distinction between how effectively a resource teaches students in its current form (quality) and how easily educators can legally and technically modify, embed, and share it (reusability).

A resource can excel on one dimension while failing on the other, which is why the 100-point rubric splits them into two separate 50-point subtotals.

**Example:** A scanned PDF of a classic, award-winning textbook under a CC BY-ND license has high instructional quality for readers but near-zero reusability for teachers who want to edit or modularize it.

See also: Quality Dimension, Reusability Dimension, Quality Subtotal, Reusability Subtotal.

#### Question Bank

A structured collection of assessment items organized by topic, learning outcome, and cognitive difficulty level from which quizzes, practice sets, or pre/post-tests can be drawn.

Maintaining an openly licensed pool of questions in an editable format allows instructors to generate varied quizzes or import items directly into a learning management system.

**Example:** A repository folder containing 150 tagged Markdown and QTI questions across ten chapters enables a teacher to assemble a randomized 20-question midterm in minutes.

See also: Quiz, LMS Import, Reusable Component.

#### Question Difficulty

The level of cognitive challenge posed by an assessment item, determined by the complexity of the underlying concept, the Bloom cognitive level required, and the subtlety of the options.

A well-balanced chapter quiz includes a progression of items ranging from foundational recall to multi-step application and evaluation scenarios.

**Example:** Asking a student to state the maximum points on the Ten-Metric Rubric is a low-difficulty recall item, whereas asking them to reconcile conflicting scores from two AI agents is a high-difficulty evaluation item.

See also: Bloom Cognitive Levels, Multiple-Choice Question, Assessment Alignment.

#### Quiz

A structured set of assessment items—commonly multiple-choice, true/false, or short-answer questions—designed to evaluate a learner's grasp of the concepts covered in a lesson or chapter.

In intelligent textbooks, per-chapter quizzes aligned to the learning graph provide both retrieval practice for students and outcome data for A/B testing.

**Example:** At the end of Chapter 4, a ten-item interactive quiz tests whether readers can score sample OER passages across the five quality metrics.

See also: Multiple-Choice Question, Question Bank, Practice Question Generation.

#### Random Assignment

An experimental procedure in which each participating student is allocated to either the Control Group or the Treatment Group by a chance mechanism (such as a random number generator or coin flip), giving every learner an equal probability of being in either group.

Allocating students by chance balances prior ability, motivation, and background knowledge across the two groups far more fairly than comparing an 8:00 AM honors section against a 3:00 PM general section.

**Example:** Using a spreadsheet randomizer within a single 40-student lecture class, the instructor assigns 20 randomly selected students Link A (Original Version) and 20 students Link B (Improved Version).

See also: Confounding Variable, Sampling Bias, A/B Test.

#### Re-Scoring

The evaluation of an adapted or improved educational resource using the exact same ten-metric rubric and verification rules applied before the revisions, in order to measure objective changes in quality and reusability.

Evaluating the revised resource under identical criteria verifies that the improvements actually solved the diagnosed problems without introducing new regressions.

**Example:** After adding alt text, repairing headings, generating a chapter quiz, and adding YAML metadata, the reviewer runs the ten-metric rubric evaluation a second time on the updated chapter files.

See also: Score Gain, Before-and-After Comparison, Improvement Plan.

#### Readability Formula

A mathematical equation that calculates an objective text difficulty score using measurable surface features such as average words per sentence and average syllables or characters per word.

Automated evaluation scripts run these formulas across Markdown files to give reviewers instant quantitative evidence for the Readability Metric.

**Example:** Formulas such as Flesch-Kincaid Grade Level, Gunning Fog, and SMOG analyze sentence and word lengths to estimate the years of education needed to read a passage smoothly.

See also: Flesch-Kincaid Grade Level, Automated Readability Scan, Reading Level.

#### Readability Metric

The third quality metric in the ten-metric rubric, which evaluates whether a resource's prose, sentence complexity, vocabulary, defined terms, headings, and worked examples are clear and appropriate for its target learners.

Even factually accurate and aligned content fails students if dense jargon and walls of unbroken text make it incomprehensible at their reading level.

**Example:** A high school biology chapter written in clear active voice at a ninth-grade Flesch-Kincaid level, with bolded glossary terms and subheadings every three paragraphs, scores 9 out of 10 on this metric.

See also: Reading Level, Plain Language, Audience Fit.

#### Reading Level

The quantitative estimate of the school grade or comprehension skill required for a reader to understand a passage of text, typically derived from sentence length and word complexity.

Checking whether a textbook's prose complexity matches its stated Grade Level Field is a rapid check that both human reviewers and automated scripts perform.

**Example:** An open textbook intended for seventh-grade general science that measures at a fourteenth-grade college graduate reading level has a severe comprehension mismatch.

See also: Readability Formula, Flesch-Kincaid Grade Level, Reading Level Rewrite.

#### Reading Level Rewrite

The targeted revision of dense, overly complex prose using plain language, shorter sentences, active voice, and explicit term definitions so the text's readability score matches the intended Grade Level Field without losing conceptual accuracy.

When a college-level open resource is adapted for high school or middle school learners, AI agents can draft a calibrated simplification pass that the teacher then verifies for disciplinary precision.

**Example:** Using a rewrite prompt, an instructor lowers a genetics section from a 14.5 Flesch-Kincaid grade level down to 9.1 by splitting 40-word passive sentences and defining "allele" and "phenotype" inline.

See also: Readability Metric, Flesch-Kincaid Grade Level, Preserving Original Meaning.

#### Redistribute Permission

The legal right to share copies of the original resource, or revised and remixed versions of it, with other educators, students, or the general public.

Publishing an improved textbook to a public repository after running AI enhancements relies on having clear authority to share the resulting files.

See also: The 5R Permissions, Publishing OER, OER Repository.

#### Release Notes

A human-readable summary published alongside a new version tag of an educational resource that highlights the major new features, metric score improvements, accessibility repairs, and known issues for adopting instructors.

Clear version summaries help faculty decide when to switch their course links to a newly updated edition between semesters.

**Example:** The release page for `v2.0` announces three new interactive MicroSims, full WCAG 2.1 AA compliance across all twelve chapters, a 24-point rubric score increase, and a downloadable Common Cartridge file.

See also: Changelog, Revision History, Publishing OER.

#### Remix Permission

The legal right to combine an original or modified resource with other open materials to create a new, integrated work such as a custom anthology or multi-source module.

Checking whether two resources can be legally combined requires evaluating both this permission and the compatibility of their respective licenses.

**Example:** An instructional designer merges two chapters from a CC BY statistics book with interactive simulations from a CC BY-SA repository to build a custom data science unit.

See also: The 5R Permissions, License Compatibility, Derivative Work.

#### Resource Selection

The systematic process of identifying, evaluating, and comparing candidate learning materials against instructional criteria to choose the best fit for a course.

Applying a standardized 10-metric rubric transforms selection from an informal browsing exercise into an evidence-based decision.

**Example:** A curriculum committee compares three candidate algebra textbooks using the 100-point rubric and selects the one with the highest combined quality and reusability score.

See also: Quality Rubric, Adoption Decision, OER Adoption.

#### Responsive Layout

A web design approach using flexible grids, relative sizing, and CSS media queries so that pages, tables, and interactive MicroSims automatically adapt their width and layout to fit desktop monitors, laptops, tablets, and smartphones.

Many college and high school students read course materials on phones or small Chromebooks; fixed-width pages that require horizontal scrolling penalize the Portability Metric.

See also: Portability Metric, Browser Compatibility, MicroSim.

#### Results Summary

A concise report or table compiling the findings of an A/B test—including sample sizes, control and treatment pre/post means, learning gains, effect size, completion rates, and key student feedback—alongside the resource's before-and-after rubric scores.

Presenting empirical classroom outcomes side by side with rubric scores provides complete transparency for adoption committees and agent calibration.

**Example:** A one-page summary table shows that raising Chapter 2's rubric score from 59 to 88 produced a $+1.9$-point difference in mean learning gain ($d = 0.74, N = 56$) and raised student clarity ratings from 3.1 to 4.6 out of 5.

See also: Rubric-Outcome Correlation, Difference of Means, Before-and-After Comparison.

#### Retain Permission

The legal right to make, own, and control personal copies of a learning material indefinitely, including downloading, storing, duplicating, and printing the content.

Without this foundational right, students lose access to their study materials when a semester subscription expires or a web server shuts down.

**Example:** A student exercising this right downloads a PDF and Markdown archive of an algebra textbook onto a personal laptop to keep for reference in future advanced courses.

See also: The 5R Permissions, Offline Access, Open Educational Resource.

#### Retrieval Practice

The learning strategy of actively recalling information and solving problems from memory—such as through self-check questions and quizzes—rather than passively rereading text.

Decades of memory research demonstrate that active recall strengthens long-term retention and transfer far more effectively than highlighting or reviewing notes.

**Example:** Closing the chapter summary and answering five short quiz questions from memory produces significantly higher retention on a post-test one week later than reading the summary three times.

See also: Spaced Practice, Practice Metric, Self-Check Question.

#### Reusability Dimension

The half of the OER Evaluator rubric comprising five 10-point metrics—open license, modularity, metadata, editable source, and portability—that assess how easily educators can legally and technically adapt, embed, and share a resource.

A resource that scores poorly on these five metrics traps valuable instructional content in a format or legal state that other teachers cannot customize.

**Example:** A textbook hosted in clean Markdown on GitHub under a CC BY license with complete Dublin Core metadata and standalone chapters scores 47 out of 50 on this dimension.

See also: Reusability Subtotal, Quality Versus Reusability, Quality Dimension.

#### Reusability Subtotal

The sum of the five reusability metric scores—open license, modularity, metadata, editable source, and portability—yielding a value from 0 to 50 points.

A low score on this subtotal signals that teachers will face legal or technical barriers if they try to customize, embed, or republish the material.

**Example:** A PDF-only resource with a CC BY-NC-ND license, no metadata file, and monolithic chapters might earn a reusability subtotal of only 12 out of 50.

See also: Reusability Dimension, Quality Subtotal, Total Score.

#### Reusable Component

A self-contained, openly licensed educational building block—such as a standalone chapter, glossary, question bank, or interactive MicroSim—packaged with clear metadata and clean embed or import files so other instructors can drop it directly into their own courses.

Designing improvements as modular assets multiplies the return on teacher effort because a single well-built simulation or quiz can serve hundreds of classrooms.

See also: Standalone Component, Embeddable Component, Component Library.

#### Reuse Permission

The legal right to use an unmodified learning material publicly or privately in a wide range of instructional contexts, such as a classroom, study group, website, or video lecture.

This right ensures that teachers can project, assign, or embed a resource across different course sections without seeking publisher clearance.

**Example:** A biology instructor projects diagrams from an openly licensed anatomy manual during a recorded lecture and posts the video on a public course website.

See also: The 5R Permissions, OER Adoption, Open License.

#### Reuse Tracking

The practice of documenting and monitoring where an open educational resource or its modular components have been adopted, forked, translated, or embedded across courses and institutions.

Because open resources require no purchase orders or mandatory logins, authors combine voluntary adoption forms, repository fork counts, and referrer logs to understand downstream reach.

**Example:** Combining GitHub fork counts, a voluntary "Tell Us You Adopted This Book" survey link, and OER Commons bookmark statistics shows that an improved algebra textbook is being used in 28 schools.

See also: Usage Analytics, Impact Reporting, OER Adoption.

#### Review Checklist

An itemized list of specific binary or short-answer checks that guide a reviewer through inspecting a resource for each rubric metric.

Checklists break abstract criteria like "accessibility" or "portability" into concrete, observable items so reviewers do not overlook key details.

**Example:** Under the Accessibility Metric, the checklist prompts the reviewer to verify four items: alt text on images, sequential heading levels, sufficient color contrast, and captions on videos.

See also: Quality Rubric, Rubric Worksheet, Manual Evaluation.

#### Review Report

A formal summary document presenting an evaluated resource's total score, quality and reusability subtotals, metric-by-metric scores with cited evidence, and a final adoption or revision recommendation.

Both human evaluators and AI scoring agents produce this structured artifact to communicate findings to instructors, departments, or improvement teams.

**Example:** A completed evaluation document for an open biology textbook summarizes its 74/100 score, highlights weak accessibility and metadata scores, and recommends targeted AI repairs before fall adoption.

See also: Agent Evaluation Report, Rubric Worksheet, Adoption Recommendation.

#### Review Workflow

The end-to-end sequence of steps followed to evaluate an educational resource—from ingesting files and running automated scans to conducting manual or AI-agent scoring, verifying evidence, reconciling discrepancies, and issuing a final report.

Following a repeatable sequence ensures no metric is skipped and allows human effort to focus where expert judgment matters most.

**Example:** In the hybrid evaluation pipeline, an automated script first checks links, readability, and metadata; an AI agent drafts the ten metric scores with citations; and a human teacher verifies the evidence and finalizes the report.

See also: Manual Evaluation, Agent Workflow, Human in the Loop.

#### Reviewer

A teacher, instructional designer, librarian, subject-matter expert, or trained peer who evaluates an open educational resource against a rubric and records evidence-backed scores.

Even when AI agents automate the initial scoring pass, human educators remain the final decision-makers who verify evidence and judge pedagogical fit.

**Example:** A high school chemistry teacher serves as the primary evaluator for three open lab manuals being considered by the district curriculum committee.

See also: Manual Evaluation, Human in the Loop, Local Reviewer Role.

#### Reviewer Bias

A systematic tendency for an evaluator to score a resource too generously, too harshly, or inconsistently due to personal preferences, visual impressions, or familiarity with the author.

Clear scoring descriptors, mandatory evidence citations, and team calibration sessions help minimize subjective distortion in rubric scores.

See also: Calibration Session, Rubric Reliability, Inter-Rater Agreement.

#### Reviewer Notes

The qualitative commentary written by an evaluator on a rubric worksheet to explain the reasoning behind a metric score, note borderline judgments, and suggest specific fixes for the improvement phase.

When two evaluators or an agent and a human disagree on a score, reading the accompanying notes immediately reveals why their interpretations differed.

See also: Evidence Recording, Rubric Worksheet, Score Reconciliation.

#### Reviewer Training

Instruction and guided practice provided to educators, librarians, or instructional designers so they understand the ten rubric metrics, apply scoring descriptors consistently, and know how to audit AI agent evaluations.

Well-trained evaluators achieve high inter-rater reliability and spot subtle AI hallucinations that untrained readers might rubber-stamp.

**Example:** Before evaluating district curriculum materials, twenty high school teachers complete a three-hour training workshop covering the 5R permissions, the 10-metric rubric, and hands-on calibration exercises.

See also: Calibration Session, Teacher Training Workshop, Professional Development.

#### Revise Permission

The legal right to adapt, adjust, modify, translate, or alter the content itself to better suit specific learners, cultural contexts, or instructional goals.

Improvement workflows in this course—such as using AI agents to rewrite reading levels, repair headings, or add practice questions—depend entirely on this legal right.

**Example:** A high school physics teacher translates an English open chapter into Spanish and replaces unfamiliar regional examples with local landmarks.

See also: The 5R Permissions, OER Adaptation, NoDerivatives Requirement.

#### Revision History

A chronological record of editions, updates, corrections, and version numbers documenting how an educational resource has been maintained over time.

A visible update log demonstrates active stewardship and helps adopting instructors see what changed between semester releases.

See also: Changelog, Version Control, Currency Metric.

#### Role Prompting

The prompt engineering technique of assigning a specific expert identity, professional perspective, and evaluative stance to a language model so its vocabulary, rigor, and priorities align with the task.

Telling an agent to act as a skeptical, evidence-demanding accessibility and OER auditor counteracts the default conversational tendency of language models to be overly polite and generous.

**Example:** Starting a prompt with "Act as a senior instructional designer and WCAG 2.1 AA compliance auditor who requires concrete line-number proof before awarding above 5 points on any metric" sharpens the evaluation.

See also: System Prompt, Prompt, Score Inflation.

#### Rubric Metric

A single evaluated criterion within a rubric that measures one distinct aspect of a resource on a defined numeric scale.

In the OER Evaluator framework, each of the ten criteria is worth 0 to 10 points and focuses on a specific property such as readability or editable source format.

See also: Ten-Metric Rubric, Metric Score, Scoring Descriptor.

#### Rubric Prompt

A specialized prompt that embeds the complete scoring descriptors, evidence rules, and point scales of the ten-metric OER rubric to instruct an AI agent how to evaluate a learning resource systematically.

Including the explicit 0–3, 4–6, 7–8, and 9–10 descriptors inside the prompt anchors the model's judgment and prevents vague, inflated ratings.

**Example:** A well-crafted rubric prompt provides the exact scoring rules for all five quality metrics and five reusability metrics and requires at least two quoted file citations for every score assigned.

See also: Prompt Template, Agent Scoring, Scoring Descriptor.

#### Rubric Reliability

The degree to which an evaluation rubric produces consistent, reproducible scores when applied to the same resource by different reviewers or across repeated scoring sessions.

High consistency across raters is essential if departments want to trust rubric scores when comparing candidate textbooks or validating AI agents.

**Example:** When three trained teachers independently score the same open history chapter and arrive at totals of 78, 79, and 80, the evaluation instrument demonstrates strong consistency.

See also: Inter-Rater Agreement, Cohen's Kappa, Rubric Validity.

#### Rubric Validity

The extent to which an evaluation rubric genuinely measures the educational quality and practical reusability of a resource and predicts real student learning and teacher adoption success.

In this course, educators test the predictive accuracy of rubric scores by running classroom A/B tests and checking whether higher-scored resources actually produce better student outcomes.

**Example:** If improving a chapter's practice and readability scores from 4 to 9 consistently leads to higher student post-test gains in A/B trials, those rubric metrics demonstrate strong empirical validity.

See also: Rubric-Outcome Correlation, Rubric Reliability, A/B Test.

#### Rubric Worksheet

A structured form, spreadsheet, or Markdown template where a reviewer records metric scores, subtotals, evidence citations, and explanatory notes during an evaluation.

Using a standardized template ensures that manual reviews and AI agent reports share the exact same fields for side-by-side comparison.

**Example:** During a workshop, teachers open a ten-row Markdown table template to log their 0–10 score and two supporting evidence bullets for each metric.

See also: Manual Evaluation, Evidence Recording, Review Report.

#### Rubric-Outcome Correlation

The empirical relationship between improvements in a resource's rubric metric scores (such as higher Readability, Accessibility, and Practice ratings) and measurable gains in student learning outcomes observed in classroom A/B tests.

Comparing A/B test results against automated rubric scores is the ultimate validation mechanism in this course: it reveals which metrics genuinely predict student learning and exposes superficial changes that merely game the score.

See also: Rubric Validity, Score Correlation, A/B Test, Calibration Against Humans.

#### Run-to-Run Variance

The degree to which an AI agent assigns slightly different numeric scores or cites different evidence when given the exact same resource and prompt across multiple independent executions.

Because large language models sample tokens probabilistically, setting a low sampling temperature (near zero) and relying on deterministic helper scripts helps keep repeated runs consistent.

**Example:** Running the exact same evaluation prompt five times on Chapter 3 produces total scores of 74, 75, 74, 74, and 76, demonstrating low variance ($\pm 1$ point) suitable for reliable assessment.

See also: Rubric Reliability, Agent Scoring, Tool Use.

#### Sample Size

The total number of students ($N$) participating in an A/B test—and specifically the number of learners in each comparison group ($n_1$ and $n_2$)—whose outcome data are collected and analyzed.

Larger group counts reduce the influence of random individual variation, whereas very small classroom pilots ($n < 15$ per group) are treated as exploratory indicators rather than definitive proof.

See also: Pilot Test, Effect Size, A/B Test.

#### Sampling Bias

A systematic distortion in experimental results that occurs when the students included in an A/B test—or assigned to one of its groups—do not fairly represent the target learner population, such as when only high-achieving volunteers complete the post-test.

Checking completion rates across both groups and avoiding voluntary self-selection into the new version prevents skewed conclusions.

**Example:** Letting students choose whether they want to try the new interactive MicroSim chapter creates self-selection bias if the most motivated students flock to the treatment group.

See also: Random Assignment, Confounding Variable, Equity Consideration.

#### Schema.org Markup

A collaborative structured-data vocabulary embedded in webpages (typically as JSON-LD scripts or HTML microdata) that enables search engines and AI crawlers to parse entity types, licenses, authors, and educational properties reliably.

Embedding structured JSON-LD in an open textbook's template ensures that every chapter automatically broadcasts rich metadata to web indexers.

See also: LRMI, Machine-Readable Metadata, Metadata Metric.

#### Scope and Sequence

The breadth and depth of topics covered in an educational resource (scope) combined with the logical chronological order in which those topics are introduced to learners (sequence).

A well-designed sequence ensures that foundational concepts are always taught before the advanced topics that depend on them.

See also: Prerequisite Knowledge, Learning Graph, Concept Dependency.

#### Score Band

A defined range of total rubric points—such as 85–100, 65–84, 45–64, or below 45—that maps a numeric evaluation result to an overall quality tier and recommended action.

Score bands help curriculum committees translate raw point totals into practical decisions about adopting, revising, or rejecting a resource.

**Example:** In the course workflow, a total score in the 85–100 band indicates a resource ready for immediate classroom adoption, whereas the 65–84 band recommends targeted AI-assisted revision prior to use.

See also: Total Score, Adoption Threshold, Adopt Revise or Reject.

#### Score Correlation

A statistical measure (such as the Pearson correlation coefficient $r$ or Spearman rank correlation $\rho$, ranging from $-1$ to $+1$) that quantifies how strongly two sets of numeric scores vary together across a collection of resources.

Evaluating correlation shows whether an AI agent ranks strong, medium, and weak textbooks in the same relative order as human experts—and whether rubric scores predict student learning gains in A/B tests.

**Example:** Across fifteen evaluated chapters, a correlation of $r = 0.89$ between human consensus total scores and AI agent total scores indicates that the agent reliably distinguishes high-quality chapters from weak ones.

See also: Rubric-Outcome Correlation, Calibration Against Humans, Mean Absolute Difference.

#### Score Difference Threshold

A pre-established numeric cutoff—commonly 3 points on a 10-point metric scale or 10 points on the 100-point total score—above which a discrepancy between a human reviewer's score and an AI agent's score requires mandatory investigation and reconciliation.

Setting an explicit numerical trigger focuses human review time on the exact metrics where the agent and educator saw the resource differently.

See also: Score Reconciliation, Agent Disagreement, Mean Absolute Difference.

#### Score Gain

The numeric increase in an individual rubric metric, subtotal, or total score ($\text{Score}_{\text{after}} - \text{Score}_{\text{before}}$) achieved after executing an improvement plan on an open educational resource.

In the course capstone and certificate requirements, educators demonstrate measurable improvement across at least two quality metrics and two reusability metrics.

**Example:** Raising a chapter's Accessibility score from 4 to 9 (+5 points), Practice from 3 to 8 (+5 points), Metadata from 2 to 10 (+8 points), and Modularity from 5 to 8 (+3 points) produces a total score gain of +21 points.

See also: Re-Scoring, Before-and-After Comparison, Capstone Project.

#### Score Inflation

The systematic bias of uncalibrated large language models to award overly generous, high rubric scores (such as 8s, 9s, and 10s) to mediocre or flawed educational resources out of a default tendency toward polite, positive responses.

Counteracting upward scoring drift requires explicit deduction rules in the rubric prompt, few-shot examples of low-scoring resources, and calibration against human raters.

**Example:** Before prompt calibration, an LLM gives a poorly structured, unedited textbook draft an 86/100 total score; after adding strict checklist deductions and human consensus anchors, the agent's score drops to a realistic 54/100.

See also: Overconfident Score, Calibration Against Humans, Role Prompting.

#### Score Reconciliation

The systematic process of investigating and resolving significant point differences—typically greater than 2 or 3 points on a metric—between two human reviewers or between a human reviewer and an AI agent.

Rather than simply averaging two conflicting numbers, reconciliation requires checking the underlying text evidence to determine which rater missed a fact or misapplied a descriptor.

**Example:** When an AI agent awards 9/10 on the Open License Metric but the human reviewer awards 3/10, inspecting the text reveals an "ND" (NoDerivatives) clause the agent overlooked, resolving the score to 3.

See also: Consensus Scoring, Score Difference Threshold, Agent Disagreement.

#### Score Scale

The defined numeric range and interval system used to assign points to a rubric metric, establishing the minimum, maximum, and intermediate performance tiers.

Each metric in the course rubric uses a 0-to-10 integer scale grouped into performance tiers such as weak (0–3), developing (4–6), strong (7–8), and exemplary (9–10).

**Example:** Using a 0-to-10 scale across all ten metrics allows the ten scores to sum cleanly to a 100-point percentage-equivalent total without complex weighting formulas.

See also: Metric Score, Scoring Descriptor, Total Score.

#### Scoring Descriptor

A concrete written statement in a rubric that specifies the observable features a resource exhibits to earn a particular point value or range on a metric.

Clear descriptors reduce guesswork and improve agreement between human reviewers and AI scoring agents.

**Example:** Under the Open License Metric, the descriptor for 9–10 points states: "Resource carries a clear, visible CC BY or CC0 notice with no conflicting third-party content restrictions."

See also: Quality Rubric, Score Scale, Inter-Rater Agreement.

#### Screen Reader

Assistive software—such as NVDA, JAWS, or VoiceOver—that converts digital text, semantic HTML structure, alt text, and ARIA labels into synthesized speech or refreshable Braille output for blind and visually impaired users.

Evaluating how a textbook sounds when read aloud by assistive software reveals why semantic headings, descriptive link text, and table headers matter so deeply.

See also: Alt Text, Heading Structure, ARIA Labels.

#### Second-Agent Cross-Check

A quality-assurance pattern in which a second, independent AI agent is prompted to audit the evaluation report or content edits produced by a first agent against the original source files and rubric rules.

Because catching an error in an existing report is often cognitively simpler than generating the report from scratch, a critic agent can flag many hallucinated line numbers or missed checklist items automatically.

**Example:** Agent A generates the ten-metric rubric report for a chapter, and Agent B receives both the raw chapter and Agent A's report with instructions to verify every quote and flag any score that violates a rubric cap.

See also: Multi-Agent Review, Agent Disagreement, Verification Step.

#### Secondary Source

A work that interprets, summarizes, synthesizes, or analyzes information originally presented in primary sources, such as a review article, encyclopedia entry, or textbook.

Well-curated secondary sources like Wikipedia and authoritative textbooks help students grasp broad concepts when paired with reliable primary references.

**Example:** A literature review article that synthesizes findings from fifty individual clinical trials on vaccine efficacy serves as a secondary reference for a health textbook.

See also: Primary Source, Source Citation, Citation Quality.

#### Self-Check Question

An embedded practice prompt placed directly within or immediately after an instructional section so an independent learner can test comprehension and view the solution on the spot.

In open textbooks used by self-directed learners or flipped classrooms, built-in self-checks replace the informal questions a lecturer would ask in person.

See also: Formative Assessment, Immediate Feedback, Practice Metric.

#### ShareAlike Requirement

The license condition denoted by "SA" that obligates anyone who distributes an adaptation or derivative of a work to license the new work under the same or a legally compatible license.

This viral or copyleft provision protects open access downstream but can cause license conflicts when combining resources with different share-alike terms.

**Example:** If an author remixes a CC BY-SA simulation into a new chapter, the resulting chapter must also be licensed under CC BY-SA rather than CC BY-NC.

See also: CC BY-SA, CC BY-NC-SA, License Compatibility.

#### Source Citation

A formal reference within a text or bibliography that identifies the book, article, dataset, or webpage from which a claim, statistic, quotation, or figure was obtained.

Credible, traceable citations allow reviewers and students to verify facts and raise a resource's score on the Accuracy and Currency metric.

**Example:** Including an inline reference to "(IPCC, 2023)" alongside a global temperature graph and listing the full report URL in the chapter references allows anyone to inspect the original data.

See also: Citation Quality, Primary Source, Invented Citation.

#### Source Format

The underlying file type and markup structure—such as Markdown, HTML, LaTeX, or DOCX—in which an author creates and maintains the master editable version of an educational resource.

Providing direct access to the master authoring files is essential so downstream educators can fix errors, update content, and rebuild the book cleanly.

**Example:** Even when a textbook is offered to students as a downloadable PDF and a static website, its master authoring files are the `.md` Markdown documents stored in its `docs/` directory.

See also: Editable Source Metric, Open File Format, Export Format.

Contrast with: PDF-Only Distribution.

#### Source Verification

The act of checking a quoted passage, line number, URL, or bibliographic citation in an evaluation report or chapter directly against the original source file or external publication to confirm that it exists and says what is claimed.

Direct look-up in the raw file is the single most reliable defense against invented citations and hallucinated rubric evidence.

**Example:** When the agent report cites `docs/chapters/02-licenses/index.md` line 118 as containing a TASL attribution example, the reviewer jumps to line 118 in the editor to confirm the exact quote is present.

See also: Invented Citation, Evidence Citation, Fact Checking.

#### Spaced Practice

An instructional design pattern that distributes review questions and skill application across multiple sections or chapters over time rather than massing all practice in a single block.

Interleaving earlier concepts into later chapter exercises prevents forgetting and helps learners see how foundational ideas connect to advanced workflows.

See also: Retrieval Practice, Practice Metric, Scope and Sequence.

#### Spot Check

A targeted verification technique in which a human reviewer inspects a random or strategic sample of an AI agent's claims, quotes, or generated items to assess trustworthiness without re-doing the entire task from scratch.

When evaluating a twelve-chapter textbook, auditing every single line of all twelve chapters manually takes days, whereas verifying a focused sample plus all flagged low scores catches systematic failures quickly.

**Example:** Out of 45 alt text descriptions generated by an AI agent across a module, the reviewer closely inspects 10 randomly selected diagrams plus all complex data charts to confirm quality before approving the batch.

See also: Verification Step, Source Verification, Human Review of Changes.

#### Standalone Component

A chapter, lesson, quiz, or interactive widget that includes all necessary context, definitions, and assets to function intelligibly when extracted from its parent textbook and used on its own.

When a component stands on its own feet, another educator can link to it or embed it via an `iframe` without forcing students to read five preceding chapters first.

**Example:** A MicroSim lesson page that states its concept definition, provides clear instructions above the simulation canvas, and includes three self-check questions works seamlessly as an independent homework activity.

See also: Modular Content, Embeddable Component, Reusable Component.

#### Standards Alignment

The explicit mapping between an educational resource's content and assessments and an external academic framework, such as state K-12 standards, Next Generation Science Standards, or professional accreditation criteria.

School districts and college departments rely on standards mappings to confirm that an open textbook fulfills mandated curriculum requirements.

**Example:** An open middle-school earth science module includes a metadata table linking each section and quiz item to specific Next Generation Science Standards (NGSS) performance expectations.

See also: Alignment Metric, Curriculum Map, Metadata Record.

#### Static Site Generator

A software build tool—such as MkDocs, Jekyll, Hugo, or Quarto—that compiles plain-text Markdown files, configuration templates, and media assets into a fast, secure, self-contained HTML website requiring no database or server-side application code.

Static websites are ideal for open textbooks because they load instantly, require zero login walls, resist security vulnerabilities, and can be hosted for free or downloaded for offline use.

**Example:** Running `mkdocs build --strict` compiles all Markdown chapters and MicroSims in `docs/` into a complete, portable HTML website inside the `site/` directory in a few seconds.

See also: MkDocs, GitHub Pages, Markdown.

#### Structured Output

Response text generated by a language model that strictly conforms to a predefined machine-parsable format or schema—such as a JSON object, YAML block, or standardized Markdown table—rather than free-form conversational prose.

Requiring predictable structure allows Python scripts and spreadsheet tools to aggregate scores, compute subtotals, and compare agent runs automatically.

**Example:** Instructing the agent to return every metric rating in a standardized four-column Markdown table (`| Metric | Score (0-10) | Evidence Citation | Recommended Fix |`) ensures every report is immediately comparable.

See also: JSON Output, Agent Evaluation Report, Rubric Prompt.

#### Student Data Privacy

The legal and ethical protection of personally identifiable student information—including names, grades, quiz responses, accommodation statuses, and browsing behavior—from unauthorized collection, disclosure, or third-party AI training.

When using AI tools or running classroom A/B tests, educators ensure that no identifiable student records are sent to external language model APIs or published in open repositories.

**Example:** Before analyzing student pre-test and post-test scores from an A/B trial with an analysis script, the teacher strips all student names and school ID numbers, replacing them with random participant codes.

See also: FERPA, Student Privacy in Testing, Anonymized Data.

#### Student Privacy in Testing

The application of data minimization, secure local storage, and strict de-identification throughout a classroom A/B test so that individual student identities, grades, and survey comments are never exposed publicly or sent to external AI services.

Protecting participant confidentiality ensures that classroom experiments remain ethical and compliant with school privacy policies.

**Example:** The instructor collects pre-test and post-test scores using anonymous four-digit participant codes and stores the mapping sheet offline in a locked school directory, never uploading identifiable rows to a repository or LLM prompt.

See also: Student Data Privacy, FERPA, Anonymized Data.

#### Student Survey

A brief questionnaire administered to learners after studying an educational resource to gather their structured ratings and open-ended perceptions of clarity, engagement, navigation ease, and helpfulness of quizzes or MicroSims.

Combining objective quiz gains with direct learner ratings reveals not only whether students learned more, but also whether the improved resource felt clearer and less frustrating to use.

See also: Qualitative Feedback, Outcome Measure, Exit Survey.

#### Subject Field

The metadata element that classifies the academic discipline, topic area, or curriculum domain covered by an educational resource, often drawn from a standardized taxonomy.

Accurate subject tagging allows teachers browsing large OER clearinghouses to filter millions of items down to their exact teaching discipline.

**Example:** Tagging an open module with `subject: "Environmental Science — Climate Systems"` ensures it appears when high school earth science teachers browse their discipline catalog.

See also: Metadata Record, Keywords, Controlled Vocabulary.

#### Submission Review

The formal audit of a candidate's certificate submission by a qualified instructor or peer review panel against the certificate requirements to verify that all rubric evidence, AI error checks, open license attributions, and score gains are accurate and complete.

Reviewers check the candidate's live repository and findings log directly to confirm that no hallucinated citations or unattributed third-party assets slipped into the published OER.

**Example:** An instructional design lead audits a candidate's submitted GitHub repository, verifies that `mkdocs build --strict` passes cleanly, checks the TASL attribution statement, and approves the portfolio for certification.

See also: Certificate Submission, Certificate Requirements, Peer Review.

#### System Prompt

The foundational framing instructions given to a large language model before user interaction begins, defining the model's persona, behavioral rules, evaluation standards, and output constraints.

Setting strict ground rules at the system level—such as "Never invent citations and always quote exact line numbers from the source file"—reduces overconfident scoring and fabrication.

See also: Prompt, Role Prompting, Rubric Prompt.

#### Table Accessibility

The structural markup of data tables using semantic header elements (`<th>`), scope attributes, and captions, while avoiding merged cells or layout tables, so screen readers can associate every data cell with its row and column labels.

When tables lack semantic header tags, assistive software reads a confusing stream of numbers without telling the student which metric or group each number belongs to.

**Example:** Marking the top row of a rubric comparison table with `<th scope="col">` allows a screen reader to announce "Quality Subtotal: 42" as the user moves across the row.

See also: Screen Reader, Accessibility Metric, HTML.

#### TASL Attribution Format

A standard mnemonic framework—standing for Title, Author, Source, and License—used to construct complete, legally compliant credit statements for openly licensed works.

Teaching reviewers and AI agents to verify all four elements ensures that attributions are never missing critical links or license versions.

**Example:** Writing "'Cell Division Diagram' (Title) by Maria Gomez (Author), from Wikimedia Commons (Source), licensed under CC BY-SA 4.0 (License)" follows the four-part structure exactly.

See also: Attribution Statement, Attribution Requirement, License Statement.

#### Teacher Training Workshop

A structured professional learning session in which educators learn to apply the ten-metric rubric, direct AI agents to evaluate and improve open resources, verify agent evidence, and plan classroom A/B tests through hands-on practice.

Practical workshops multiply institutional capacity by turning individual classroom teachers into skilled local OER evaluators.

**Example:** A college teaching center hosts a one-day hands-on workshop where twenty faculty members evaluate a textbook from their own discipline manually in the morning and calibrate an AI evaluation agent in the afternoon.

See also: Workshop Agenda, Facilitator Guide, Professional Development.

#### Ten-Metric Rubric

The specific 100-point evaluation framework taught in this course, consisting of five 10-point quality metrics and five 10-point reusability metrics.

Every manual evaluation, AI agent prompt, and before-and-after improvement comparison in the book is anchored to this ten-part structure.

**Example:** Evaluating an open chemistry chapter with this framework yields five quality scores (e.g., 8, 9, 7, 5, 6) and five reusability scores (e.g., 10, 6, 4, 8, 7) for a total of 70 out of 100.

See also: Quality Dimension, Reusability Dimension, Total Score.

#### Test Hypothesis

A specific, falsifiable prediction stated before running an A/B test that specifies which resource improvement is being tested and which measurable student outcome (such as learning gain, completion rate, or time on task) is expected to improve.

Writing the prediction in advance prevents cherry-picking favorable numbers after the data are collected.

**Example:** "Students who study the Improved Version of the licensing module (containing the interactive compatibility MicroSim and five self-check questions) will achieve a higher mean pre-to-post learning gain on the 10-item licensing test than students who study the Original Version."

See also: A/B Test, Outcome Measure, Learning Gain.

#### Text Structure

The organizational architecture of written content—including paragraphs, lists, tables, callout boxes, and section hierarchy—that guides a reader visually and logically through a topic.

Well-chunked pages prevent visual fatigue and help students scan, outline, and recall complex instructional material.

**Example:** Breaking a 1,500-word wall of text into four titled subsections with bulleted checklists and a summary comparison table transforms a dense essay into an approachable lesson.

See also: Headings and Subheadings, Readability Metric, Heading Structure.

#### The 5R Permissions

A framework defined by David Wiley that specifies five essential legal rights—retain, reuse, revise, remix, and redistribute—that a license grants for a work to qualify as a true open educational resource.

The rubric's open license metric scores a resource directly on how completely its license enables all five activities.

See also: Retain Permission, Reuse Permission, Revise Permission, Remix Permission, Redistribute Permission.

#### Third-Party Content

Text, images, charts, videos, or code created by someone other than the primary author and embedded within an educational resource under a separate license or legal exception.

An open textbook licensed under CC BY may still contain embedded photographs or graphs that carry restrictive terms, reducing the book's actual reusability.

See also: Fair Use, License Clarity, Open License Metric.

#### Time on Task

The amount of active time (typically measured in minutes) that a learner spends reading, interacting with simulations, and completing practice questions within an educational resource.

Interpreting study duration requires pairing it with learning gains: a clearer reading-level rewrite may help students reach mastery in *less* time, whereas an engaging new MicroSim may inspire students to spend *more* productive time exploring concepts.

**Example:** Log data show that students in the Treatment Group spent an average of 6 active minutes manipulating the rubric MicroSim and achieved a 22% higher post-test score in the same 30-minute class period.

See also: Completion Rate, Outcome Measure, Interactive Simulation.

#### Title Field

The descriptive metadata element that specifies the formal, human-readable name by which an educational resource, chapter, or reusable component is known and cited.

A clear, specific title helps educators identify the resource's topic in search results and forms the "T" in a standard TASL attribution statement.

**Example:** Naming a module `"Evaluating Open Licenses with the 5R Framework"` is far more informative in a repository search than naming it `"Chapter 2"` or `"Module_v3_final"`.

See also: Metadata Record, TASL Attribution Format, Dublin Core.

#### Token

The basic unit of text—typically a word, part of a word, number, or punctuation mark (roughly three-quarters of an English word on average)—that a large language model reads as input and generates as output.

Both context window limits and API usage costs are calculated directly from the number of input and output tokens processed during an evaluation or improvement task.

**Example:** A 3,000-word textbook chapter corresponds to roughly 4,000 input tokens, allowing an educator to estimate the exact compute cost before running a batch evaluation across fifty chapters.

See also: Context Window, AI Cost, Large Language Model.

#### Tool Use

The capability of an AI agent to invoke external software functions, command-line scripts, calculators, or web checkers during its reasoning loop and incorporate their deterministic outputs into its evaluation.

Delegating deterministic checks—such as counting words, calculating Flesch-Kincaid scores, or testing HTTP status codes—to external scripts eliminates LLM arithmetic and guessing errors.

**Example:** Instead of guessing whether a chapter's 38 external URLs work, the agent calls a Python link-checker tool, receives the exact list of three `404` URLs, and cites them in the Currency Metric score.

See also: AI Agent, Automated Link Checker, Automated Readability Scan.

#### Total Score

The overall numeric rating of an open educational resource calculated by adding the 50-point quality subtotal and the 50-point reusability subtotal on a 0-to-100 scale.

While the composite number provides a quick summary for score bands, reviewers always examine the two subtotals and individual metrics before making an adoption decision.

**Example:** Combining a quality subtotal of 42 and a reusability subtotal of 36 produces a total score of 78 out of 100, placing the textbook in the "adopt with minor revisions" band.

See also: Quality Subtotal, Reusability Subtotal, Score Band.

#### Train-the-Trainer

A capacity-building model in which experienced graduates of the OER Evaluator program are equipped with facilitation guides, slide decks, and sample repositories to lead teacher training workshops for colleagues at their own schools or districts.

Empowering certified educators to teach their peers scales evidence-based OER evaluation across entire school systems and university consortia.

**Example:** Four certified department chairs use the open Training Kit to lead summer workshops for 80 instructors across a state community college system.

See also: Training Kit, Facilitator Guide, Teacher Training Workshop.

#### Training Evaluation

The systematic assessment of a professional development workshop or course's effectiveness by analyzing participant exit surveys, pre-to-post calibration accuracy, and the quality of completed capstone portfolios.

Just as classroom OER are evaluated with evidence and outcome data, teacher training programs use empirical participant results to refine their facilitation guides and examples.

**Example:** Comparing participants' rubric scoring accuracy before and after the workshop shows that their mean absolute difference from expert consensus dropped from 2.7 points to 0.8 points per metric.

See also: Exit Survey, Teacher Training Workshop, Calibration Against Humans.

#### Training Kit

A complete, openly licensed package of workshop materials—including the Workshop Agenda, Facilitator Guide, slide decks, pre-flawed sample OER chapters for calibration exercises, consensus answer keys, and rubric worksheets—ready for any trainer to download and customize.

Releasing the workshop materials themselves under a CC BY license in an editable source format practices the exact reusability principles taught throughout the course.

**Example:** A district curriculum coordinator downloads the open workshop folder, customizes the agenda for a two-hour in-service day, and prints the ten-metric rubric worksheets for thirty middle school teachers.

See also: Train-the-Trainer, Facilitator Guide, Workshop Agenda.

#### Transcript

A complete text document containing all spoken words and descriptions of key visual or audio events from an audio recording or video lesson, readable independently at the learner's own pace.

Transcripts make podcasts and video lectures searchable, printable, and accessible to deaf-blind learners using refreshable Braille displays.

**Example:** Below an embedded ten-minute interview with an open licensing attorney, the chapter includes a collapsible text block containing the full speaker-labeled conversation.

See also: Captions, Audio Description, Accessibility Metric.

#### Treatment Group

The experimental cohort of students in an educational A/B test who use the newly improved, AI-enhanced version of a learning resource so their outcomes can be compared against the control group.

Comparing the performance of this group against the baseline cohort isolates the causal impact of the specific rubric improvements made to the resource.

**Example:** In the same 60-student biology course, the 30 students randomly assigned to Group B study the revised Markdown chapter featuring a Grade 9 reading-level rewrite, descriptive alt text, and an interactive cell-transport MicroSim.

See also: Control Group, Improved Version, A/B Test.

Contrast with: Control Group.

#### Universal Design for Learning

An educational framework developed by CAST that guides the design of flexible learning environments providing multiple means of engagement, representation, and action or expression to accommodate learner variability from the outset.

Building open resources with multiple representations—such as pairing written explanations with visual MicroSims and audio transcripts—benefits all students, not only those with formal accommodations.

See also: Accessibility, Accessibility Metric, MicroSim.

#### Usage Analytics

Privacy-respecting aggregate metrics—such as page views, chapter completion patterns, MicroSim interaction counts, and geographic distribution—collected on a published OER site without tracking personally identifiable student data.

Aggregate traffic patterns help authors see which chapters and simulations are heavily used and where learners spend the most time.

**Example:** Aggregate site statistics reveal that the interactive ten-metric rubric MicroSim receives 1,200 views per month and that Chapter 3 has the highest average reading time.

See also: Reuse Tracking, Impact Reporting, Student Data Privacy.

#### Verification Step

A mandatory quality-control check in an AI-assisted evaluation or improvement workflow where a human reviewer or independent deterministic script validates the accuracy of the agent's claims, quotes, and file edits.

Building explicit checkpoints into the workflow ensures that errors are caught before an adoption decision is made or an edited chapter is published.

**Example:** Before accepting an AI agent's Accessibility Metric score of 9/10, the reviewer performs a verification step by opening the chapter source file and confirming that the cited alt text strings actually exist and describe the charts accurately.

See also: Spot Check, Source Verification, Human in the Loop.

#### Version Control

A system that records changes to a set of files over time so authors and contributors can review revision history, compare differences line by line, revert mistakes, and collaborate without overwriting each other's work.

Hosting an open textbook under version tracking makes every AI-assisted edit transparent, auditable, and reversible during human review.

See also: Git, GitHub Repository, Revision History.

#### Vocabulary Level

The difficulty, abstraction, and specialized nature of the words used in an educational resource relative to the background knowledge of the target learner population.

Effective textbooks control word difficulty by using everyday language for general explanations while systematically introducing and defining essential technical terms.

**Example:** Replacing unnecessary ornate words like "utilize," "heretofore," and "ameliorate" with "use," "previously," and "improve" lowers vocabulary friction without sacrificing academic rigor.

See also: Plain Language, Jargon, Defined Terms.

#### WCAG

The Web Content Accessibility Guidelines, an internationally recognized set of technical standards developed by the World Wide Web Consortium (W3C) to make web content accessible to people with disabilities.

Organized around four foundational principles—Perceivable, Operable, Understandable, and Robust (POUR)—these guidelines define the specific technical criteria used in OER accessibility audits.

**Example:** The guideline requiring every non-decorative image to have a text alternative is one of the core rules defined in this international standard.

See also: WCAG 2.1 AA, Accessibility Metric, Accessibility Checker.

#### WCAG 2.1 AA

The specific version and intermediate conformance tier of the Web Content Accessibility Guidelines widely adopted as the legal and institutional benchmark for K-12 schools, universities, and open textbooks.

The OER Evaluator rubric uses this exact technical standard to score the Accessibility Metric and guide AI-assisted remediation.

**Example:** Meeting this conformance tier requires a minimum color contrast ratio of 4.5:1 for normal body text and synchronized captions for all prerecorded instructional videos.

See also: WCAG, Accessibility Metric, Contrast Ratio.

#### Word Processing File

An editable document created in office productivity software—such as OpenDocument Text (`.odt`), Microsoft Word (`.docx`), or Google Docs—commonly used by K-12 teachers and faculty to draft worksheets, syllabi, and readings.

While less suited than Markdown for automated web publishing and Git version tracking, a downloadable `.docx` or `.odt` file still provides a practical editable source for classroom teachers.

**Example:** Offering a downloadable `.docx` version of a lab worksheet alongside the web page allows a high school teacher to customize the instructions in Microsoft Word in five minutes.

See also: Source Format, Editable Source Metric, PDF-Only Distribution.

#### Worked Example

A step-by-step demonstration within the instructional text that shows a complete problem, the reasoning behind each intermediate action, and the final verified solution.

Cognitive science research shows that studying step-by-step demonstrations significantly reduces cognitive load for novices before they attempt independent practice problems.

**Example:** Before asking students to score a chapter on their own, the textbook walks through a complete ten-metric evaluation of a sample ecology chapter, showing every point calculation and evidence note.

See also: Readability Metric, Practice Problem, Worked Solution.

#### Worked Solution

A complete, step-by-step explanation provided in an answer key that shows not only the final answer to a practice problem but also the full reasoning path and rubric evidence used to reach it.

When students compare their own attempt against a detailed reasoning walkthrough, they can pinpoint exactly where their calculation or judgment diverged.

**Example:** Instead of merely listing "Score: 6/10" in the answer key, the solution explains which two checklist items passed, which one failed, and which line of the passage provided the evidence.

See also: Answer Key, Practice Problem, Worked Example.

#### Workshop Agenda

A time-blocked instructional plan for a teacher training workshop that sequences conceptual mini-lessons, group calibration exercises, hands-on AI agent labs, peer review sessions, and reflection discussions.

Pacing the session so participants spend at least two-thirds of their time actively scoring resources and checking agent output keeps professional learning engaging and practical.

**Example:** A three-hour schedule allocates 30 minutes to the 5R permissions and 10-metric rubric, 45 minutes to a group calibration exercise, 60 minutes to running and auditing an AI evaluation agent, and 45 minutes to drafting an improvement plan.

See also: Teacher Training Workshop, Facilitator Guide, Calibration Exercise.

#### Zero Textbook Cost Course

An academic course section in which students incur no out-of-pocket expense for required texts because the instructor uses openly licensed materials, library-licensed resources, or free readings.

Colleges often label these sections in registration systems so students can plan their semester budgets accurately.

**Example:** A community college English composition course that replaces a commercial reader with a curated set of CC BY essays qualifies for a ZTC designation in the course catalog.

See also: Course Material Affordability, OER Adoption, Open Educational Resource.

