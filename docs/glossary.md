---
title: Glossary of Terms
description: Alphabetical glossary of the terms used in OER Evaluator, with ISO 11179-style definitions, examples, and related terms.
---

# Glossary of Terms

This glossary defines the terms used in this book. Each entry gives a short definition, a note on why the term matters when you evaluate or improve an open educational resource (OER), and, for many terms, an example and related terms. Terms are listed alphabetically.

#### A/B Test

A comparison of two versions of something, A and B, in which comparable groups of people use each version at the same time and the results are compared.

The book teaches a manual A/B test with students, original version against improved version, and uses its results to calibrate automated scores.

**Example:** One class uses the original lesson and another uses the improved lesson, and both take the same post-test.

*See also:* Control Group, Treatment Group

#### Accept Correct or Reject

The three outcomes of checking one claim from an agent's report: accepted when true as stated, corrected when right in substance but wrong in a detail, and rejected when false, invented, or impossible to verify.

Every checked claim lands in one of the three, and the findings log records the choice.

**Example:** A claim of "12 images" is corrected to 13 after a count, and a citation that cannot be found is rejected.

#### Accessibility

The degree to which a resource can be used by people with a wide range of abilities, including those who rely on assistive technology.

Accessibility is a learning, ethical, and legal concern. The book uses WCAG 2.1 AA as its working standard.

**Example:** A page with real headings and image descriptions works for a student who uses a screen reader.

*See also:* WCAG 2.1 AA, Universal Design for Learning

#### Accessibility Checker

A software tool that scans a page or document for accessibility defects, such as missing alt text, low contrast, or skipped heading levels.

Automated checkers find only part of the problems, so a human check completes the work.

#### Accessibility Metric

A rubric metric, worth up to 10 points, that scores whether people with disabilities can perceive, operate, and understand a resource, using checks drawn from the Web Content Accessibility Guidelines (WCAG) 2.1 level AA.

It is a quality metric, and a low score blocks adoption because barriers keep learners out.

*See also:* WCAG 2.1 AA, Accessibility Checker

#### Accessible Math

Mathematical notation presented in a form, such as MathML or readable text, that assistive technology can read aloud and navigate, and not as a picture alone.

Equations saved as images are unreadable to screen readers, so math-heavy OER need this check.

#### Accuracy Metric

A rubric metric, worth up to 10 points, that scores whether the facts, figures, and claims in a resource are correct and traceable to credible sources.

It is one of the five quality metrics. Evidence includes checked facts, the quality of citations, and expert comments.

**Example:** A biology page that names the wrong organ for a function loses points on this metric.

*See also:* Factual Error, Fact Checking

#### Adopt Revise or Reject

The three decisions a review can lead to: use the resource now, improve it first, or set it aside, chosen by applying the adoption threshold to its scores.

The OER Evaluator's output ends in one of these three outcomes, with reasons.

**Example:** A total of 82 with every metric at 5 or more supports adopt, a total of 62 supports revise, and a total of 41 supports reject.

*See also:* Adoption Threshold, Adoption Decision

#### Adoption Decision

The formal choice, made by a person or group with authority, whether to use a resource in a course or school, after weighing a review and local needs.

A review informs the decision and does not make it, because a department or committee also weighs things the rubric does not measure.

**Example:** A district committee reads a review report and votes to pilot a resource.

*See also:* Adoption Recommendation, Adopt Revise or Reject

#### Adoption Recommendation

A reviewer's written advice to decision-makers that states which decision the scores support, gives reasons in plain words, and names the strongest and weakest metrics.

It is the part of the review that busy readers actually read.

*See also:* Review Report, Adoption Decision

#### Adoption Threshold

A decision rule that turns scores into one of three outcomes; in this book's starting values, adopt when the total is at least 75 and every metric is at least 5, reject when the total is under 50, and revise otherwise.

These values are the book's starting rule and not a standard, so a department may set its own. The floor of 5 stops one failed metric from hiding inside a high total.

**Example:** A resource with a total of 80 but an accessibility score of 3 is revised and not adopted.

*See also:* Adopt Revise or Reject, Total Score

#### Agent Disagreement

A difference in the scores or findings of two agents, or of an agent and a human, on the same metric.

A disagreement is information. It points to unclear evidence, a possible agent error, or an ambiguous check in the rubric.

**Example:** One agent scores metadata 8 and another scores it 4, so a reviewer opens the metadata record.

#### Agent Error Rate

The share of an agent's checked claims that were corrected or rejected, found by dividing the number not accepted as stated by the number verified.

It gives a plain number for how far an agent can be trusted on a given task.

**Example:** If a reviewer verified 40 claims and 6 were corrected or rejected, the rate is 6 divided by 40, or 15 percent.

#### Agent Error Type

A category of mistake that an agent makes, such as a factual, license, citation, or scoring error, used to organize what a reviewer finds.

Naming the type tells the reviewer how to catch it and tells the prompt writer how to fix it.

**Example:** A count that is off by one is a factual error, while a total that does not add up is a scoring error.

*See also:* Hallucination, Findings Log

#### Agent Evaluation Report

The document an agent produces from a scoring run, giving for each metric the score, checks, and evidence, plus subtotals, total, band, unverified checks, and a recommendation.

It is what a human reviewer reads and verifies, so its structure is designed to make checking easy.

*See also:* Agent Scoring, Verification Step

#### Agent Scoring

The use of an AI agent to assign the ten metric scores to a resource, with evidence, by following the rubric.

Agent scoring is fast and repeatable but needs checking, so the book pairs it with verification and calibration.

**Example:** An agent scores a chapter and returns a total of 71 with evidence for each metric.

*See also:* Rubric Prompt, Agent Evaluation Report

#### Agent Skill

A packaged set of instructions, and sometimes helper scripts and reference files, that an agent loads when a task matches it.

A skill lets someone write down a procedure once and reuse it. The book's evaluation procedure can be packaged this way.

**Example:** A folder with a text file of scoring instructions and a short description telling the agent when to use it.

#### Agent Workflow

The designed sequence of steps, tools, and human checkpoints that an agent and its human partner follow to produce a trustworthy evaluation.

It is the agent's version of the review workflow and ends with a person.

**Example:** The agent reads files, runs link and accessibility tools, drafts scores, and hands a report to a reviewer who verifies it.

*See also:* Human in the Loop, Review Workflow

#### Agreement Rate

The share of metrics on which an agent's score falls within the score difference threshold of the human score, written as a percentage.

It summarizes human and agent agreement in one percentage that teachers can read at a glance.

**Example:** If 8 of 10 metrics agree, the agreement rate is 80 percent.

*See also:* Score Difference Threshold, Inter-Rater Agreement

#### AI Agent

A software system built on a language model that carries out multi-step tasks toward a goal by reading files, using tools, and making decisions with limited human direction at each step.

The OER Evaluator uses agents to draft scores and improvements, and a person verifies the results.

**Example:** An agent reads a folder of lesson files, runs a link checker, and fills in the rubric worksheet.

*See also:* Agent Skill, Agent Workflow

#### AI Alt Text Generation

The use of an AI model to draft text descriptions for images in a resource, which a person then checks and corrects.

It makes a tedious job quick, but drafts can be wrong, so each one is accepted, corrected, or rejected.

**Example:** An agent drafts descriptions for 20 images, and a reviewer corrects 4 of them.

*See also:* Alt Text, Accept Correct or Reject

#### AI Assistant

A software program that uses artificial intelligence, usually a large language model, to answer questions and complete tasks in a conversation with a person.

An assistant answers when asked, while an agent works through several steps. The book starts with assistants and moves to agents.

**Example:** A teacher asks an assistant to explain the difference between CC BY and CC BY-SA.

*See also:* AI Agent, Large Language Model

#### AI Cost

The money a service charges for a language model's work, usually calculated from the number of tokens sent and received.

Cost shapes how many resources a department can score with agents, and prices change often, so reviewers look up current rates.

**Example:** A batch of fifty chapters costs more than a single chapter because it processes far more tokens.

*See also:* Token, Batch Evaluation

#### Alignment Metric

A rubric metric, worth up to 10 points, that scores how well a resource's content, activities, and assessments match its stated learning outcomes and relevant standards.

Alignment links a resource to what a course is trying to achieve. A resource can be accurate and still not useful if it is poorly aligned.

*See also:* Learning Outcome, Outcome Coverage

#### All Rights Reserved

A phrase in a copyright notice indicating that the rights holder keeps every right and grants no permissions beyond those given by law.

It signals that reuse requires asking the owner. The OER Evaluator treats it as the opposite of an open license.

**Example:** A footer reading "© 2022 Example Press. All rights reserved."

#### Alt Text

A short written description of an image, stored in the page code, that a screen reader speaks aloud when it reaches the image.

Missing or poor alt text is a leading accessibility defect. AI agents can draft it, and people check it for accuracy.

**Example:** For a bar chart: "Bar chart showing quality scores rising from 62 to 81 after revision."

*See also:* Decorative Image, AI Alt Text Generation

#### Anonymized Data

Data from which every link to a particular person has been removed, so that no one, including the teacher, can tell whose scores they are.

It differs from coded data, which replaces names with codes but keeps a key. Anonymized data gives stronger privacy.

**Example:** A score table lists "Student 1, Student 2, and so on" with no key kept anywhere.

#### Answer Key

A list of the correct answers to a set of questions, often with a brief explanation of why each answer is right.

Without a key, a teacher cannot check work quickly or trust that an item is right, so the practice metric looks for one.

**Example:** "Question 4: B. CC BY-NC restricts commercial use."

*See also:* Feedback Message, Worked Solution

#### ARIA Labels

Attributes from the Accessible Rich Internet Applications specification that give interactive page elements a name or description for assistive technology.

They help screen reader users with custom controls such as simulation buttons. They patch gaps, and plain HTML elements need them less.

#### Assessment Alignment

The degree to which quiz and test questions measure the same knowledge and level of thinking as the stated learning objectives.

Misaligned assessments reward the wrong learning. The OER Evaluator checks whether each objective has matching questions.

**Example:** An objective to "design a lesson" paired with a multiple-choice recall quiz is misaligned.

*See also:* Bloom Cognitive Levels, Learning Objective

#### Attribution Requirement

A condition in many open licenses under which anyone using a work credits its creator and notes the license, the source, and any changes.

Attribution is the one condition of CC BY and appears in most other Creative Commons licenses. The OER Evaluator checks that a resource credits its own borrowed materials correctly.

**Example:** A reused diagram carries a line naming its creator, the source link, and the license.

*See also:* Attribution Statement, TASL Attribution Format

#### Attribution Statement

A written credit line placed with a reused work that names its creator, gives its source, and states its license.

A complete credit line is what a reuser needs to follow the license, and a missing one is a common license error. Agents can draft these, and a person checks them against the source.

**Example:** "Prairie Dawn" by A. Writer, from example.org, licensed under CC BY 4.0.

#### Audience Fit

The degree to which a resource matches its intended users' reading level, prior knowledge, language, culture, and purpose, taken together.

A grade number alone cannot capture fit, so a human check completes the readability score.

#### Audio Description

A spoken narration added to a video that describes important visual content, such as actions, scenes, and on-screen text, for viewers who cannot see it.

Without it, a blind learner misses what is shown. A video whose normal narration already explains every visual needs less.

**Example:** A narrator says "The graph line climbs steeply after year three" when the speaker only points at the screen.

*See also:* Transcript, Captions

#### Author Field

The metadata field that names the person or organization responsible for creating a resource, so reusers can give credit and contact the source.

Credit lines depend on it, so the OER Evaluator checks that it is filled and matches the visible byline.

#### Automated Accessibility Scan

A tool-driven test that examines a page's code for known accessibility problems and produces a list of defects for a person to review.

Scans find only part of the problems, so a person completes the check with a screen reader or keyboard test.

**Example:** A scan reports missing alt text, low contrast, and an empty link.

#### Automated License Detection

A tool or agent step that finds license statements and markings in a resource and identifies which license each one names.

It saves time but can misread vague or conflicting notices, so a person confirms it against the statement.

**Example:** A detector reports "CC BY 4.0" from a footer link.

#### Automated Link Checker

A program that visits every link in a resource and reports which links work, which redirect to another address, and which fail.

It supplies fast, objective evidence for the currency metric and is the first automated check the book teaches.

**Example:** A tool lists 4 dead links among 60 and records the date of the test.

#### Automated Readability Scan

A tool-driven test that computes readability formula results, such as grade level, for a resource's text, usually page by page.

It shows where text is too hard, though only a person can judge audience fit.

**Example:** A scan flags three pages above grade 12 in a seventh-grade unit.

#### Batch Evaluation

The running of the same rubric prompt over many resources, one after another, so that a whole collection can be scored.

It saves time for a department or repository, but errors repeat across the batch, so spot checks matter.

**Example:** A librarian has an agent score thirty open textbooks and ranks them by total.

#### Before-and-After Comparison

A study design that compares one group's scores before and after using a single version of a resource, with no second group.

It is weak evidence, because anything that happened between the two tests can explain a gain. The book prefers a controlled A/B test.

**Example:** A teacher gives a pre-test, teaches the improved lesson, gives a post-test, and sees a gain of 18 points, which other factors could also explain.

*See also:* A/B Test, Control Group

#### Bloom Cognitive Levels

The six ordered categories of thinking named in the 2001 revision of the taxonomy first developed by Benjamin Bloom and colleagues: Remember, Understand, Apply, Analyze, Evaluate, and Create.

Matching the level of an objective to the level of its practice items is a key alignment check.

#### Bloom's Taxonomy

A classification of thinking skills, in its 2001 revised form, arranged from simpler to more complex: Remember, Understand, Apply, Analyze, Evaluate, and Create.

The book uses these levels to set outcomes and to check whether practice questions ask for the same level of thinking as the objectives.

**Example:** A question asking learners to list the 5Rs is at Remember, while one asking them to judge a resource is at Evaluate.

*See also:* Bloom Cognitive Levels, Measurable Verb

#### Broken Link Check

A test that follows each link in a resource and records whether it reaches a working page, an error, or a redirect.

It gives hard evidence for the currency metric. Results change over time, so the date of the check is recorded.

**Example:** A checker reports that 6 of 80 links return errors.

*See also:* Automated Link Checker, Link Rot

#### Browser Compatibility

The ability of a web resource to display and work correctly in the major web browsers and on the different devices that learners use.

A resource that fails in a student's browser fails for that student. The portability metric checks several browsers.

**Example:** A simulation that runs in Chrome, Firefox, Safari, and Edge.

#### Calibration Against Humans

The process of testing an agent's scores against careful human scores on a set of resources, then adjusting the prompt until the two agree well enough for the agent's purpose.

It is how an agent earns the trust a teacher is asked to place in it.

**Example:** A team compares an agent's scores with consensus human scores on twenty resources and finds a bias of +1.0.

#### Calibration Exercise

The workshop session in which each teacher scores a sample resource by hand, runs an agent on the same resource, and compares the two sets of scores.

It is the teaching version of calibration against humans, and it shows teachers directly where an agent errs.

**Example:** Teachers find that the agent scored accessibility two points higher than their own scores.

*See also:* Calibration Session, Calibration Against Humans

#### Calibration Session

A meeting in which reviewers score the same sample resources, compare scores metric by metric, and discuss differences until they apply the rubric in the same way.

Calibration is what turns a written rubric into a shared one, because two reviewers can read the same descriptor differently.

**Example:** Four reviewers each score two sample resources alone, then meet to discuss every metric on which they differ.

*See also:* Consensus Scoring, Score Reconciliation

#### Capstone Project

The culminating work of the book, in which a person evaluates one open resource from their own subject, improves it with AI agents on at least two quality and two reusability metrics, tests the change with students, and publishes it under CC BY.

It applies every skill in the book to a resource that matters to the learner.

**Example:** A teacher improves a unit on fractions, runs a small A/B test, and posts the new version.

*See also:* Improvement Challenge, Professional Development

#### Caption Generation

The use of speech-to-text software or an AI model to draft synchronized captions for a video or audio recording, which a person then corrects.

Automatic captions often misspell names and technical terms, so human correction is part of the process.

**Example:** A tool drafts captions for a lecture, and a teacher fixes three misspelled terms.

#### Captions

Text synchronized with the audio of a video that shows spoken words and important sounds, for viewers who cannot hear or choose to watch without sound.

WCAG 2.1 AA expects captions on prerecorded video with sound. Speech-to-text software can draft them, and a person corrects them.

**Example:** A lecture video shows each sentence as it is spoken, plus "[applause]" for the sound.

*See also:* Transcript, Caption Generation

#### CC BY

A Creative Commons license that permits anyone to copy, adapt, and distribute a work for any purpose, including commercial use, provided the creator is credited.

CC BY is the least restrictive Creative Commons license and the one this book favors for the components teachers publish. It grants all five permissions with a single condition, attribution.

**Example:** A photograph under CC BY can appear in a school textbook with a credit line naming its creator.

*See also:* Attribution Requirement, TASL Attribution Format

#### CC BY-NC

A Creative Commons license that permits copying and adapting a work with credit to the creator, but only for noncommercial purposes.

The NonCommercial limit restricts some permissions, so this book does not treat a CC BY-NC resource as open in the full 5R sense. The OER Evaluator notes the limit on the open license metric.

**Example:** A free workshop can reuse a CC BY-NC worksheet, while a company selling a paid course with it raises a question.

#### CC BY-NC-ND

The most restrictive of the six main Creative Commons licenses, permitting others only to copy and share a work unchanged, with credit, and for noncommercial purposes.

It allows use but not revision or remixing, so a resource under it scores low on the open license metric. Improving it would first require the owner's separate permission.

**Example:** An article under this license can be handed out as is, but not edited into a new handout.

*See also:* CC BY-NC, CC BY-ND

#### CC BY-NC-SA

A Creative Commons license that combines credit to the creator, a noncommercial-use limit, and a requirement that adapted versions carry the same license.

It stacks two restrictions, so remixing is possible only with works under compatible terms. The OER Evaluator reads both limits when scoring the open license metric.

**Example:** A teacher adapts a CC BY-NC-SA worksheet and shares the new version under the same terms for noncommercial use.

*See also:* ShareAlike Requirement, NonCommercial Requirement

#### CC BY-ND

A Creative Commons license that permits copying and sharing a work in unchanged form, with credit to the creator, but does not permit sharing adapted versions.

NoDerivatives blocks revision and remixing, the permissions that improvement work needs. The OER Evaluator records it as a restriction on the open license metric.

**Example:** A teacher can post a CC BY-ND article for a class but cannot share a translated version.

*See also:* NoDerivatives Requirement, Revise Permission

#### CC BY-SA

A Creative Commons license that permits copying and adapting a work, including for commercial use, if the creator is credited and adapted versions carry the same license.

ShareAlike keeps adaptations open but limits what a remix can be combined with. The OER Evaluator checks compatibility when a resource mixes sources.

**Example:** A teacher who adapts CC BY-SA text shares the adapted version under CC BY-SA too.

*See also:* ShareAlike Requirement, License Compatibility

#### CC0 Dedication

A Creative Commons tool by which a creator gives up copyright and related rights as far as the law allows, placing a work as close to the public domain as possible.

CC0 is a dedication and not a license in the strict sense, and it attaches no conditions, not even credit. The OER Evaluator treats it as the most open status a resource can have.

**Example:** A data table released under CC0 can be used in a lesson without a credit line.

*See also:* Public Domain, CC BY

#### Certificate

A record issued by a program to show that a person has completed defined work to a defined standard; in this book, the credential for evaluating OER quality with AI agents.

Earning it shows that a teacher attended training, calibrated against an agent, evaluated a real resource, and improved it.

**Example:** A teacher receives the certificate after a reviewer approves the submission.

*See also:* Certificate Requirements, Certificate Submission

#### Certificate Requirements

The conditions a teacher meets to earn the certificate, each linked to the evidence that shows the condition has been met.

Clear conditions let a teacher plan the work and let a reviewer judge it fairly.

**Example:** One requirement calls for an evaluation scored on all ten metrics with evidence.

*See also:* Certificate, Certificate Submission

#### Certificate Submission

The package of evidence a teacher sends to earn the certificate, including the worksheet, the agent's scores, the findings log, and a link to the published improved component.

It lets a reviewer judge the work without being present.

**Example:** A teacher uploads a worksheet, a findings log with five entries, and the link to a CC BY component.

*See also:* Submission Review, Findings Log

#### Change Log Entry

The record of one change to a resource, answering when it was made, where, what changed, why, who or what made it, who reviewed it, and what was decided.

The log serves reusers, reviewers, and the agent's own checkers, and CC BY asks reusers to indicate changes.

**Example:** "May 3, section 2: shortened sentences; made by agent; reviewed by T. Nguyen; accepted."

*See also:* Changelog, Human Review of Changes

#### Changelog

A dated list of the notable changes made in each version of a resource, written for the people who use it and wish to know what is new.

A changelog tells reusers what is new and what has been fixed. It is also the record behind release notes.

**Example:** "v1.2: Added alt text to all figures; fixed two broken links."

#### Chapter Splitting

The division of a long resource into smaller, self-contained pieces, each with its own title, purpose, and objective, so they can be used separately.

Splitting raises modularity and lets teachers reuse one part.

**Example:** A 40-page chapter becomes five lessons that each have an objective and a quiz.

#### Chapter Structure

The division of a textbook's concepts into chapters in an order that places every concept after the concepts it depends on.

A structure that breaks the order makes readers meet a term before it is defined.

**Example:** A chapter on re-scoring comes after the chapter that defines improvement plans.

*See also:* Concept Dependency, Learning Graph

#### Citation Quality

The degree to which a resource's references are real, complete, relevant to the claims they support, and drawn from credible sources.

Citation quality is part of the accuracy evidence. It is also where AI agents often fail, by inventing sources that do not exist.

#### Cohen's Kappa

A statistic that measures how well two raters agree on categories after correcting for the agreement expected by chance alone.

It guards against false confidence, since two raters who both say "adopt" most of the time will agree often by luck.

**Example:** If a human and an agent each say "adopt" for most resources, kappa shows whether they agree more than chance would predict.

#### Color Contrast

The difference in brightness between text or graphics and their background, which determines how easily people can see them in different lighting.

Low contrast shuts out learners with low vision and anyone reading in bright light.

#### Color Independence

A design property in which meaning is carried by more than color alone, through added text, labels, patterns, or icons.

Learners with color blindness would otherwise miss information. Reviewers check charts and instructions for it.

**Example:** A chart marks passing and failing bars with green and red and also with the words "pass" and "fail."

#### Commercial Textbook

A textbook sold by a publisher for profit under traditional copyright, with most rights kept by the publisher, usually in print or as a paid digital edition.

Commercial textbooks are the cost and rights baseline against which OER are compared. A teacher can still score one with the rubric to see what a switch would gain or lose.

**Example:** A calculus text bundled with a single-use online homework code is a commercial textbook.

#### Common Cartridge

An IMS Global (1EdTech) standard file format that packages course content, such as pages, quizzes, and links, so it can move between learning management systems.

Exporting to it is a sign of portability. The OER Evaluator notes whether a resource offers it.

**Example:** A teacher exports a unit as a Common Cartridge file from one system and imports it into another.

#### Community Contribution

A change, correction, or addition to a shared resource that is proposed by someone outside the original author team, such as a reader or a colleague.

Contributions are a benefit of open resources, and on GitHub they arrive as pull requests that the owner reviews.

**Example:** A reader fixes a typo in a lesson and sends a pull request.

*See also:* Pull Request, Feedback Channel

#### Completion Rate

The share of students who finished an activity out of all those who started it, usually written as a percentage.

It shows whether a version is usable. A low rate can signal confusion or technical trouble.

#### Complex Image Description

A longer text explanation of a chart, diagram, or map that holds too much detail for alt text, placed near the image or linked from it.

Complex visuals carry lessons that a short description cannot. The accessibility metric checks that they have fuller descriptions.

#### Component Discoverability

The degree to which the people who need a component can find it, through its name, description, metadata, and the places where it is listed.

A component no one can find is not reused. Discoverability comes from a clear name, a complete metadata record, a plain-language description, and listing in places teachers look.

**Example:** A component named "Hands-On Fractions Quiz, Grade 4" with keywords and a description appears in search results.

*See also:* Metadata Completeness, OER Clearinghouse

#### Component Granularity

The size of a component, in terms of how much content one piece contains, ranging from a single idea to a whole book.

A piece that is too big cannot be partly reused, and one that is too small is not worth finding. About one idea or objective with its explanation and practice is usually a good size.

**Example:** A 12-page chapter split into six two-page lessons.

*See also:* Chapter Splitting, Modular Content

#### Component Library

An organized collection of reusable components, with an index that lets a visitor see what is there and choose what they need.

A library turns a pile of packages into something a teacher can browse.

**Example:** A website lists forty components by subject, each in its own folder.

*See also:* Reusable Component, Component Discoverability

#### Component Licensing

The practice of giving each component its own license statement and credit lines, so it keeps its terms when it travels alone.

A reuser who copies only a quiz still sees its license, its author, and what it adapted.

**Example:** A quiz page shows "CC BY 4.0" in its footer, in its folder, and in its metadata.

*See also:* License Statement, Attribution Statement

#### Component Packaging

The gathering of everything a component needs into one folder that can be copied, downloaded, or embedded as a unit.

A package holds the content, a short README, a license file, a metadata file, and any images or scripts, with links that work inside it.

**Example:** A folder holding a simulation, its README, license file, and metadata record.

#### Concept Dependency

A link between two concepts showing that a learner needs to understand one of them first, which places that concept earlier in a learning sequence.

In this book's graph each link points from a concept to its prerequisite, so the arrow reads "needs."

**Example:** Score Band depends on Total Score, because a band is read from the total.

*See also:* Learning Graph, Chapter Structure

#### Confounding Variable

A factor other than the version being tested, such as teacher, time of day, or prior knowledge, that differs between groups and could explain the result.

If the treatment group had a different teacher, one cannot tell whether the version or the teacher made the difference.

**Example:** A morning class and an afternoon class differ in alertness as well as in which version they used.

#### Consensus Scoring

A process in which two or more reviewers each score alone, compare their scores, and discuss each difference until they agree on one final score per metric.

Consensus works when the decision rests on evidence and not on seniority or persistence.

**Example:** Two reviewers differ on accessibility, 4 and 7; after checking the images together, both agree on 5.

#### Content Gap

A topic, skill, or explanation that a course's learning outcomes call for but that a given resource leaves out or covers too thinly.

Gaps explain why a good resource may still not fit a course. The OER Evaluator lists them in the review report.

#### Content Update

A revision that brings out-of-date facts, examples, or data in a resource up to date with current information from reliable sources.

It is a high-risk change because it affects meaning, so it gets a full check against the source.

**Example:** Replacing a ten-year-old statistic with a recent one from the same agency.

#### Context Window

The maximum amount of text, measured in tokens, that a language model can consider at one time, including the prompt and its own reply.

Long resources may not fit, which is one reason to split them into smaller pieces.

**Example:** A 300-page book may exceed the window, so an agent reads it chapter by chapter.

*See also:* Token, Chapter Splitting

#### Contrast Ratio

A number from 1:1 to 21:1 that compares the relative brightness of two colors, with higher values meaning greater separation.

WCAG 2.1 AA sets minimums of 4.5:1 for normal text and 3:1 for large text, and free tools compute the ratio instantly.

**Example:** Black text on white measures 21:1, the highest possible value.

*See also:* Color Contrast, WCAG 2.1 AA

#### Control Group

The group of students in a test who use the original version of a resource, providing the baseline for comparison.

Without it one can say how students did with the improved version but not how they would have done without it.

**Example:** Twelve students use the original lesson and serve as the control group.

*See also:* Treatment Group, Original Version

#### Controlled Vocabulary

A fixed list of approved terms used to label resources, so that the same idea always receives the same label across a collection.

Consistent labels improve search and make metadata easier for machines to compare.

**Example:** Every record uses "Earth science" and never "earth sciences" or "geoscience."

*See also:* Keywords, Subject Field

#### Copyright

A legal right, in United States law, held by the creator of an original work, that controls who may copy, adapt, distribute, or publicly display it.

Copyright applies to nearly every work from the moment it is created, so reuse needs a license or permission. The OER Evaluator therefore looks for a clear statement of rights on every resource; this book explains the idea and does not give legal advice.

**Example:** A teacher's lesson plan is protected the moment it is written, even without a copyright symbol.

#### Course Material Affordability

The extent to which the total price of textbooks and other course materials is low enough that students can obtain every item they need.

Cost is a main reason teachers adopt OER. Affordability is the goal, and the ten metrics decide whether a low-cost resource is also good and reusable.

**Example:** A student who waits until midterm to buy a $200 textbook shows a course with weak affordability.

#### Creative Commons

A nonprofit organization that publishes a family of standard public copyright licenses and tools so creators can grant permissions in advance.

Most OER carry a Creative Commons license, so reading these licenses accurately is a core reviewer skill and a common place for AI agents to err.

**Example:** A footer showing the Creative Commons logo and the letters "BY" identifies a CC BY work.

*See also:* CC BY, CC0 Dedication

#### Cross-Reference Dependence

The reliance of a component on other parts of its resource through phrases such as "as shown above" or "see section 4."

These references break when the component is moved. The fix is to restate the idea or link to the other piece by its own address.

**Example:** A quiz that says "use the table from Chapter 2" fails when used alone.

#### Currency Metric

A rubric metric, worth up to 10 points, that scores whether a resource's content, examples, and links are up to date for its subject and still working.

Currency sits beside accuracy among the quality metrics. A resource with dead links or old data scores lower.

**Example:** A technology chapter that still describes a discontinued tool loses points.

*See also:* Outdated Content, Link Rot

#### Curriculum Map

A chart showing what a course teaches, when, and how each part connects to outcomes and assessments, usually organized by week or unit.

A map lets a reviewer see where a candidate resource would fit and what gaps would remain.

#### Data Collection

The gathering of the measurements a test needs, in the same way for both groups, according to a plan made beforehand.

A plan covers what is collected, when, by whom, and where it is kept.

**Example:** A teacher records pre-test and post-test scores for both groups in one table.

#### Decorative Image

An image that adds visual interest but conveys no information needed to learn the content, and is marked so that screen readers skip it.

Marking decorative images spares screen reader users from needless noise. Deciding whether an image is decorative takes human judgment.

#### Defined Terms

Specialized words in a resource whose meanings are stated in the text at the point where each word first appears.

Readers who meet an unexplained term must guess. The OER Evaluator checks that each term is explained at first use or in a glossary.

#### Derivative Work

A new work that is based on, adapts, or incorporates an earlier work, such as a translation or a revised edition.

Improved resources are derivative works, so the original's license must allow adaptation, and NoDerivatives terms rule it out.

**Example:** A Spanish translation of an open lesson.

*See also:* Revise Permission, CC BY-ND

#### Description Field

The metadata field that gives a short plain-language summary of what a resource contains and who it is for, shown in search results.

Search results often show it, and a clear description helps a teacher decide at a glance.

#### Difference of Means

The mean of the treatment group minus the mean of the control group, used to estimate how much more students gained with the improved version.

It is the single number that answers the test hypothesis, though it needs context such as sample size.

**Example:** If the treatment mean gain is 22 and the control mean gain is 15, the difference of means is 7 points.

*See also:* Effect Size, Mean Score

#### Distractor Quality

The degree to which the wrong options in a multiple-choice question are plausible and reveal common misunderstandings, so that guessing is less likely to succeed.

Weak wrong options let learners guess. Reviewers check them, and AI-drafted questions often have implausible ones.

**Example:** "Public Domain" is a plausible wrong answer to "Which license requires ShareAlike?" while "purple" is not.

#### Document Ingestion

The process of reading a file or web page into a form an AI system can use, such as extracting its text, images, and structure.

Poor ingestion, such as losing a table, leads to wrong scores, so reviewers check what the agent actually saw.

**Example:** An agent converts a PDF chapter to plain text before scoring it.

*See also:* File Access, PDF-to-Markdown Conversion

#### Document Language

The human language declared in a page's code, such as English or Spanish, so that software knows how to pronounce and process the text.

A missing declaration makes screen readers mispronounce words, and it is a quick automated check.

#### Dublin Core

A metadata standard of fifteen general-purpose elements, such as title, creator, subject, description, and rights, for describing any kind of resource.

It is a simple, widely supported vocabulary that gives this book's metadata checks a common baseline.

**Example:** A record that fills the Title, Creator, and Rights elements.

*See also:* Metadata Record, LRMI

#### Editable Source Metric

A rubric metric, worth up to 10 points, that scores whether a resource is available in a form others can open and change with common tools, and not only as a fixed copy.

Without editable source, the Revise permission exists only on paper. It is one of the five reusability metrics.

*See also:* Source Format, Open File Format

#### Educational Resource

A material, such as a text, video, image, quiz, or software tool, that is created or chosen to support teaching and learning.

Everything the OER Evaluator scores begins as an educational resource, so the rubric is written to apply across formats from slide decks to simulations.

**Example:** A slide deck on fractions, a recorded lecture, and a practice quiz are each educational resources.

#### Effect Size

A standardized measure of how big a difference between two groups is, expressed in units that do not depend on the test, so that results can be compared across studies.

It shows whether a difference is large enough to matter, not just whether it exists.

**Example:** An effect size of 0.5 means the group means differ by half a standard deviation.

#### Embeddable Component

A component that can be placed inside another web page, by link or by an iframe, and displayed there without being copied.

Embedding lets teachers use a simulation in their own course page, and later improvements reach every page that embeds it.

**Example:** A one-line iframe tag puts a quiz inside a course page.

*See also:* Iframe Embedding, MicroSim

#### Equity Consideration

A check that a resource, and the test of it, work fairly for all the students who might use them, including those using assistive technology or learning English.

An average result can hide the fact that a version helps some students and leaves others out.

**Example:** A reviewer checks whether the improved version helps students with screen readers as much as other students.

*See also:* Sampling Bias, Accessibility

#### Evidence Citation

A short written record of one piece of evidence, written so that another reviewer can find the same observation within a minute.

The simple form gives where, what, and which rule, with a date for anything that can change, such as a link test. It makes the worksheet auditable.

#### Evidence for a Score

A specific, checkable observation that supports a metric score, stating where the reviewer looked, what they saw, and which check they compared it with.

Recorded evidence lets another reviewer repeat the check and agree or disagree for stated reasons. The OER Evaluator asks agents to give evidence for every score.

**Example:** "Figure 3 on the page has no alt text; the check requires alt text on every informative image."

*See also:* Evidence Citation, Evidence Recording

#### Evidence Recording

The practice of writing down, for each metric score, the observations that support it, in a form others can check.

Recorded evidence turns a score into a claim that can be tested, and it is required of agents too.

#### Exit Survey

A short survey given at the end of a workshop, while the experience is fresh, to learn how participants experienced it and what they feel able to do.

It measures reaction only, so it is one part of a training evaluation and not the whole.

**Example:** Five questions rating the day's sessions and one asking what to change.

*See also:* Training Evaluation, Student Survey

#### Expert Review

An evaluation of a resource's content by a person with deep knowledge of the subject, who judges whether it is correct, complete, and current.

A rubric reviewer cannot always judge technical accuracy, so expert review backs up the accuracy score in specialized subjects.

#### Export Format

A file type in which a resource or its data can be saved out of one system for use in another, such as HTML, PDF, Markdown, or Common Cartridge.

Good export options give users a way out of a platform, which protects their work.

#### Facilitator Guide

A document that tells the person running a workshop what to do in each session, including time, goal, materials, steps, and likely questions.

A colleague who did not write the workshop needs a guide to run it, which makes the workshop reusable.

**Example:** A guide for the calibration session lists the sample resources and the consensus scores.

*See also:* Workshop Agenda, Training Kit

#### Fact Checking

The process of comparing a resource's claims with reliable, independent sources to confirm that each claim is correct, one claim at a time.

Fact checking supplies the evidence for the accuracy metric. It is slow for a whole resource, so reviewers sample claims or ask subject experts.

#### Factual Error

A statement in a resource that is wrong when checked against reliable sources, such as an incorrect date, number, definition, or explanation.

Factual errors lower the accuracy score and mislead learners. They also appear in AI agent reports as a distinct kind of mistake.

**Example:** A history page that says the Declaration of Independence was signed in 1786.

*See also:* Fact Checking, Agent Error Type

#### Fair Use

A United States legal doctrine that permits limited use of copyrighted material without permission, judged case by case through four factors: purpose, nature of the work, amount used, and effect on the market.

Fair use depends on the facts and gives downstream users no right to reuse a resource. The OER Evaluator flags fair-use claims for human review, and this book is not legal advice.

**Example:** A teacher quoting two sentences in a classroom critique may rely on fair use, while whether another use qualifies depends on the facts.

#### Feedback Channel

A way for readers to tell the authors of a resource about problems and ideas, such as an issue tracker, an email address, or a short form.

Easy-to-find channels turn readers into helpers and surface errors early.

**Example:** Every page links to a form titled "Report a problem."

*See also:* Issue Tracking, Community Contribution

#### Feedback Message

A response shown to a learner after an answer or action that says whether it was right and explains why or how to improve.

Feedback turns practice into learning, while a bare "Wrong" helps little.

**Example:** "Not quite. CC BY-ND forbids sharing changed versions. Try again."

#### FERPA

The Family Educational Rights and Privacy Act, a United States federal law that protects the privacy of student education records at schools that receive federal funding.

The book names FERPA to remind reviewers that student records need care. It gives general information and not legal advice.

**Example:** A school asks its privacy officer before uploading graded student work to any online tool.

#### Few-Shot Example

A sample input paired with a good output that is placed in a prompt to show a model the pattern to follow.

Showing is often clearer than telling, and one sample row of an evidence table sets the level of detail wanted.

**Example:** A prompt includes one scored resource with evidence before asking for a second.

#### File Access

The ability of an agent to read, and sometimes write, files on a computer or in a folder that a person has made available to it.

It lets an agent open a resource's source files and save a report, and it creates a risk if the agent can reach files it should not, such as student records.

**Example:** An agent has read-only access to a folder of lesson files.

#### Findings Log

A record of every agent claim a reviewer checked and what was decided, with columns for the finding, the decision, and the reason.

The log makes the review auditable and supplies the numbers for measuring an agent's error rate. In certification, a log with no reasons raises doubt.

**Example:** A log of five entries shows three accepted, one corrected, and one rejected, each with a reason.

*See also:* Accept Correct or Reject, Agent Error Rate

#### Flesch-Kincaid Grade Level

A readability formula that estimates the United States school grade needed to understand a text, based on average words per sentence and average syllables per word.

It is the book's standard readability number and is simple to compute. A result of 9.0 suggests ninth-grade difficulty.

**Example:** A paragraph with long sentences and long words may score 13.2, while a plainer rewrite scores 8.1.

*See also:* Readability Formula, Reading Level

#### Fork

A personal copy of someone else's repository, made on the same hosting service, that can be changed without affecting the original.

Forking is how a teacher adapts an OER while keeping a link back to the source, and it puts the revise and remix permissions to work.

**Example:** A teacher forks a chemistry repository and translates the lessons.

#### Formative Assessment

Low-stakes checking of learning during instruction that gives learners and teachers information they can use to adjust study or teaching before a final grade.

Self-check questions and quizzes are formative, and they are the core of the practice metric.

**Example:** A three-question check after each section that shows the correct answers at once.

*See also:* Self-Check Question, Quiz

#### Free Resource

A material offered to users at no price, whether or not the owner grants any permission to copy, change, or share it.

Free to read is not the same as open. The OER Evaluator checks the legal terms and not the price, because a free resource with all rights reserved scores low on the open license metric.

**Example:** A video lecture that streams without charge but forbids copying is a free resource and not an OER.

*See also:* Open Educational Resource, All Rights Reserved

#### Git

A free, open-source version control tool that tracks changes to files in a project and lets many people work on copies and merge their changes.

Git is the tool behind this book's repository and behind most open course projects on GitHub.

**Example:** A teacher saves a change with the note "Fix broken links in chapter 3."

#### GitHub Pages

A free hosting service from GitHub that serves a static website directly from the files in a repository, at a public web address.

It gives teachers a stable public address for a resource without running a server. This book is published this way.

**Example:** A site appears at an address of the form username.github.io/repository.

*See also:* MkDocs, Publishing OER

#### GitHub Repository

A project folder, with its full change history, hosted on the GitHub website, where others can view, copy, and suggest changes to the files.

A public repository makes a resource easy to find, copy, and improve. This book's source lives in one.

**Example:** A teacher publishes lesson files in a repository so colleagues can download them.

#### Glossary

An alphabetical list of a resource's key terms with short definitions, gathered in one place so readers can look up unfamiliar words quickly.

A glossary supports readability and reuse. In this book each entry follows ISO 11179 rules for precise, non-circular definitions.

#### Glossary Generation

The use of an AI model to find a resource's key terms and draft definitions for a glossary, which a person then reviews for accuracy.

It saves effort, and each definition is still checked for accuracy and for wording that avoids circularity.

**Example:** An agent proposes 40 terms and one-sentence definitions for a unit.

#### Grade Level Field

The metadata field that states the school grade or education level a resource is intended for, so teachers can filter and compare resources.

Teachers filter by grade, and a missing value forces them to open each resource to judge its fit.

#### Hallucination

A statement produced by a language model that sounds confident and fluent but is false, unsupported, or invented, with no basis in the source material.

Hallucinations are why every agent claim needs checking. They can appear in scores, evidence, and citations.

**Example:** An agent reports a "Section 7 on ethics" that the resource does not contain.

#### Heading Repair

The correction of a resource's heading levels so that they form a logical, unbroken outline, often drafted by an agent.

It is a low-risk change that improves both readability and accessibility.

**Example:** An agent changes a level 4 heading that follows a level 1 heading to level 2.

#### Heading Structure

The nested order of heading levels on a page, such as a main heading followed by second-level and third-level headings, without skipped levels.

Screen reader users jump from heading to heading, so a broken order makes navigation hard. It is a common accessibility check and a task agents can help with.

#### Headings and Subheadings

Labels that divide a text into sections and show how sections relate, with larger headings introducing major parts and smaller ones introducing the parts inside them.

Headings help readers scan and also let screen readers navigate, so they link readability and accessibility.

#### HTML

HyperText Markup Language, the standard markup language that structures web pages with elements such as headings, paragraphs, links, and images.

HTML is the delivery format of web resources and an open format. Many accessibility checks inspect its structure.

**Example:** The code h2 around the words "Score Band" creates a second-level heading.

*See also:* Markdown, Open File Format

#### Human in the Loop

A way of working in which a person reviews, approves, or corrects an automated system's output at the points where errors matter.

It does not mean redoing the work. It means the machine's draft passes through a person before it becomes a decision, which is the book's whole method.

**Example:** A reviewer checks an agent's license claim against the page before accepting the score.

*See also:* Verification Step, Human Review of Changes

#### Human Review of Changes

The step in which a named person examines each change an agent made to a resource and decides whether to keep it, before the change is published.

Nothing goes live on the agent's say-so, and the agent's summary is not enough because an agent can leave a change out. High-risk changes get a full check.

**Example:** A teacher opens a difference view and checks every changed number against the source.

*See also:* Accept Correct or Reject, Human in the Loop

#### Iframe Embedding

The method of showing one web page inside another using the HTML iframe element, so a simulation or video can appear within a course page.

It is how MicroSims are placed in lessons, and it supports reuse without copying.

**Example:** A teacher pastes one line of code and a simulation appears inside a course page.

#### Immediate Feedback

A response delivered at the moment a learner submits an answer, before moving to the next item, so a mistake can be fixed while it is fresh.

It works well in digital practice. MicroSims and automatically graded quizzes can provide it.

**Example:** A quiz shows "Correct" or an explanation right after each click.

*See also:* Feedback Message, MicroSim

#### Impact Reporting

The honest account, given to the people who care, of what a published resource has done, drawing on reach, reuse, learning results, and user experience.

It combines usage analytics, reuse tracking, test results, and surveys into one report.

**Example:** A one-page report cites page views, three adopting schools, a 7-point learning difference, and student comments.

*See also:* Usage Analytics, Reuse Tracking

#### Improved Version

The resource after the improvement plan has been carried out, frozen and labeled for use against the original in a test.

Its change log lists the differences between the two versions.

**Example:** "Watershed Basics v1.1," with a change log of 25 edits.

*See also:* Original Version, Change Log Entry

#### Improvement Challenge

A structured exercise in which a person takes one real resource, improves it on stated metrics with help from agents, reviews and logs every change, re-scores it, and reports the gain.

It is the working form of the improvement chapter, and the book's capstone project is a larger version of it.

**Example:** A teacher raises a resource's metadata and accessibility scores, logs each change, and reports a total gain of 12 points.

*See also:* Re-Scoring, Capstone Project

#### Improvement Plan

A ranked list of the changes that would raise a resource's scores, with each change's expected score gain and effort.

The plan turns scores into work. It is compared with the actual gain after re-scoring.

**Example:** A plan lists metadata first at half an hour, then accessibility at two hours.

*See also:* Lowest Metric First, Score Gain

#### Informed Consent

A person's agreement to take part in a test, given freely after learning in plain language what taking part involves, with guardians deciding for minors.

Students are young people whose time and information are being used, so they and their families need a real choice.

**Example:** A letter explains the test, states that participation is optional, and asks guardians to agree.

#### Intelligent Textbook

A textbook built as a website from a learning graph, chapters in dependency order, a glossary, quizzes, and interactive simulations called MicroSims.

The graph gives the book a map of its own contents, and MicroSims give readers practice. This book is an example.

**Example:** This book, published as a MkDocs site with a learning graph and MicroSims.

*See also:* Learning Graph, MicroSim

#### Inter-Rater Agreement

The extent to which two or more independent reviewers assign the same or nearly the same scores to the same resource, usually measured with a statistic.

The book flags a metric when two reviewers differ by more than 3 points and uses agreement rate and Cohen's Kappa to measure agreement among humans and between humans and agents.

#### Interactive Simulation

A computer model of a process or system that learners can change by adjusting controls and then watch how the results respond.

Simulations suit ideas that are hard to explain in text. MicroSims are the kind this book builds.

**Example:** A page where learners move sliders for ten metric scores and watch the score band change.

#### Invented Citation

A reference produced by an AI model that looks real, with plausible authors, title, and journal, but does not exist or does not support the claim.

Invented citations are a common form of hallucination and are caught by looking up each source.

**Example:** An agent cites a journal article with a believable title that no library holds.

#### Issue Tracking

The practice of recording every reported problem or request about a resource in one shared list, where each item has a status and can be assigned, discussed, and closed.

It keeps problems from being lost, and it gives readers a public place to report errors.

**Example:** A reader reports a wrong answer in a quiz, and an author closes the item after fixing it.

*See also:* Feedback Channel, Maintenance Plan

#### Jargon

Specialized words or phrases belonging to a profession or field that people outside it often do not understand without explanation.

Jargon is acceptable when it is defined and a barrier when it is not. The readability metric looks for unexplained jargon.

**Example:** A lesson for ninth graders that uses "heteroscedasticity" with no explanation.

*See also:* Defined Terms, Plain Language

#### JSON Output

A model response written in JSON (JavaScript Object Notation), a plain-text format of named fields and values that software can read reliably.

JSON is a common form of structured output for agent scores.

**Example:** {"accessibility": 4, "evidence": "Most images lack alt text"}

*See also:* Structured Output, Machine-Readable Metadata

#### Keyboard Navigation

The ability to reach and use every control on a page with the keyboard alone, using keys such as Tab, Enter, and the arrow keys, without a mouse.

People who cannot use a mouse depend on it, and interactive MicroSims are a frequent failure point.

#### Keywords

Words or short phrases attached to a resource that capture its main topics and help people and search tools find it.

Good keywords match the words a teacher would type into a search box.

#### Large Language Model

A machine-learning system trained on very large amounts of text to predict and generate language, so that it can answer questions, summarize, and write.

These models power the book's agents. They can make confident mistakes, which is why every claim is checked.

**Example:** The system behind an assistant that drafts alt text for an image.

*See also:* Hallucination, Token

#### Learning Gain

The amount by which a student's or group's score rose from the pre-test to the post-test, usually expressed in points or as a share of possible improvement.

The simplest form is the raw gain, post-test minus pre-test. The book also uses a normalized form that accounts for room to improve.

**Example:** A student who scores 40 and then 70 has a raw gain of 30 points.

*See also:* Pre-Test, Difference of Means

#### Learning Graph

A map of the concepts of a subject in which each concept is linked to the concepts it depends on.

It answers "What must a learner know before this?" and helps teachers place a component in a sequence and authors order a textbook.

**Example:** In a learning graph, Re-Scoring points to Improvement Plan because the first needs the second.

*See also:* Concept Dependency, Intelligent Textbook

#### Learning Objective

A specific statement of what a learner can do after a single lesson or activity, naming an observable action and often a condition or level of performance.

Objectives are the small steps that build toward outcomes. They let the OER Evaluator and agents check whether practice questions test what a lesson teaches.

**Example:** "The learner will identify the license on five resources, with at least four correct."

*See also:* Learning Outcome, Measurable Verb

#### Learning Outcome

A statement of the knowledge, skill, or ability a learner is expected to demonstrate at the end of a course, program, or unit.

Outcomes are what the alignment metric measures a resource against. Their wording decides what counts as coverage.

**Example:** "Students will evaluate an open resource using a ten-metric rubric."

*See also:* Learning Objective, Measurable Verb

#### License Clarity

The degree to which a resource's license statement is visible, specific, and unambiguous about which terms apply to the whole work and to its parts.

Clarity matters as much as the license chosen. Agents often misread vague statements, so reviewers check them.

**Example:** "CC BY 4.0" with a link on every page is clear, while "free to use" is not.

*See also:* License Statement, License Misreading

#### License Compatibility

The condition in which the terms of two licenses can both be satisfied at once, so works under each can be combined into one new work.

Compatibility decides whether a remix can be published and under which license. The OER Evaluator checks it whenever a resource contains material from more than one source.

**Example:** A CC BY chapter and a CC BY-SA chapter can be combined, and the result is shared under CC BY-SA.

*See also:* License Conflict, Remix Permission

#### License Conflict

A situation in which the terms of two licenses on different parts of a work cannot both be satisfied by a single combined version.

Conflicts are a hidden reuse problem. The OER Evaluator reports them so a team can fix the sources before publishing.

**Example:** A CC BY-SA chapter and a CC BY-ND chapter cannot be merged into one shared book.

#### License Field

The metadata field that records the terms under which a resource may be reused, preferably as a standard name plus a link to the full text.

Machines read this field so repositories can filter by license. It needs to match the visible license statement.

**Example:** License: CC BY 4.0, with a link to the Creative Commons legal text.

*See also:* License Statement, Machine-Readable Metadata

#### License Misreading

An agent error in which a resource's license is read wrongly, for example reported as CC BY when the page says CC BY-NC, or reported as present when it is absent.

A misread license can lead to an unsafe adoption, so license claims get checked against the statement itself.

**Example:** An agent calls a resource CC BY because a link says "Creative Commons," although the terms say NonCommercial.

*See also:* Automated License Detection, Agent Error Type

#### License Selection

The decision a creator makes about which set of standard public legal terms to place on a work before sharing it with others.

The book walks teachers through this choice when they publish improved components, favoring CC BY for the widest reuse.

**Example:** An author who wants adaptations to stay open picks CC BY-SA, while one who wants the widest reuse picks CC BY.

*See also:* CC BY, License Compatibility

#### License Statement

A notice attached to a work that names the legal terms it is released under and points to the full text of those terms.

A visible, specific statement is the first thing a reuser looks for, and the OER Evaluator scores its presence and clarity. Without one, a work remains under default copyright.

**Example:** "This work is licensed under CC BY 4.0," with a link, in the footer of every page.

*See also:* License Clarity, License Statement Repair

#### License Statement Repair

The correction or addition of a resource's license statement so that it is visible, specific, and consistent with the license that actually applies.

An agent may draft wording, but a person decides which license applies.

**Example:** A teacher adds a "CC BY 4.0" line with a link to the footer of every page.

#### Link Repair

The correction of broken or outdated links by finding the current address or a replacement source and updating the reference.

It directly raises the currency score. Replacements must be checked, because a link that works may point to the wrong page.

**Example:** An agent finds the new address of a moved article and replaces the dead link.

#### Link Rot

The gradual failure of web links over time, as pages move, change, or disappear, so that a link leads to an error or to unrelated content.

Link rot is among the most common currency problems in OER. Automated link checkers find it quickly, and agents can help repair it.

**Example:** A reference link that now returns a "page not found" error.

*See also:* Broken Link Check, Link Repair

#### Link Sharing

The ability to give others access to a resource, or a part of it, by sending a stable web address.

Links that stay put and open the content directly make sharing easy. The portability metric looks for them.

#### Link Text

The visible, clickable words of a hyperlink, which tell readers and assistive technology such as screen readers where the link leads.

Phrases like "click here" say nothing when links are read out as a list. The accessibility metric checks for descriptive link text.

**Example:** "Read the WCAG overview" says more than "click here."

*See also:* Screen Reader, Accessibility Checker

#### LMS Import

The process of loading a resource's content into a learning management system (LMS) from a file or link, so it appears as part of a course.

Many teachers work inside an LMS, so easy import raises a resource's practical reuse.

**Example:** Uploading a package to a course page creates twelve modules.

#### Local Reviewer Role

A position, held by a trained and certified teacher, in which they act as the first reviewer of resources for their school or district.

The role has limits: a local reviewer flags license problems but does not rule on legal questions, never sends student information to an agent, and advises but does not make adoption decisions.

**Example:** A colleague brings a resource, and the local reviewer scores it, verifies the agent, and names the metric to fix first.

*See also:* Reviewer, Train-the-Trainer

#### Lowest Metric First

A planning approach that orders improvement work by starting with the resource's lowest-scoring metric, unless fixing it is too costly or needs the author.

It works because a low metric can block adoption, low scores often have cheap large gains, and a total hides the weakest area.

**Example:** A resource with metadata at 4 and the rest at 5 or above starts its plan with metadata.

#### LRMI

The Learning Resource Metadata Initiative, a set of properties, now part of Schema.org, for describing educational features of a resource, such as its audience, type, and educational level.

LRMI adds education-specific fields to the general fields of Dublin Core, and the metadata metric rewards records that use it.

**Example:** A page marked with a learning resource type of "quiz" and an educational level of "grade 7."

*See also:* Schema.org Markup, Dublin Core

#### LTI Integration

The connection of an outside tool to a learning management system using Learning Tools Interoperability (LTI), an IMS Global (1EdTech) standard that lets the tool open inside a course.

LTI lets a hosted simulation run within a course page and, in some cases, send scores back.

**Example:** A simulation hosted elsewhere opens inside a course module.

*See also:* LMS Import, Platform Lock-In

#### Machine-Readable Metadata

Descriptive information about a resource stored in a structured, standard format that software can read and process automatically without a person interpreting it.

Statements written only for human eyes cannot be harvested at scale, so the metadata metric rewards structured forms.

**Example:** A data file with named fields for title, author, and license.

*See also:* Schema.org Markup, JSON Output

#### Maintenance Plan

A written commitment about how a published resource will be kept in good condition: who is responsible, what is checked, how often, and when the resource will be retired.

Without one, a resource drifts out of date and a reuser cannot tell whether it is still safe to trust.

**Example:** A plan states that links are checked every six months by the department librarian.

*See also:* Issue Tracking, Release Notes

#### Manual Evaluation

The scoring of a resource by a human reviewer who reads it, runs the checks, chooses the ten metric scores, and records the evidence.

It is slower than software, and it is the reference against which software is measured. The book teaches it before any AI agent is used.

**Example:** A teacher spends an afternoon scoring one open textbook chapter on all ten metrics.

*See also:* Reviewer, Review Workflow

#### Markdown

A lightweight plain-text writing format in which simple symbols mark headings, lists, and links, and which converts easily to HTML.

Markdown is this book's preferred source format because it is easy to edit, compare, and convert, and agents handle it well.

**Example:** The line "## Score Band" marks a second-level heading.

*See also:* HTML, PDF-to-Markdown Conversion

#### Mean Absolute Difference

The average size of the gaps between two sets of scores, found by ignoring whether each gap is positive or negative and averaging the sizes.

A value near 0 means the agent's scores sit close to the human scores.

**Example:** Gaps of 1, 0, 3, and 2 points average 1.5 points.

#### Mean Score

The arithmetic average of a set of scores, found by adding all the scores together and dividing by the number of scores.

It is the most common way to summarize a group with one number.

**Example:** Scores of 60, 70, and 80 have a mean score of 70.

#### Measurable Verb

An action verb, such as identify, compare, or design, that names behavior a teacher can observe and assess, used when writing learning objectives.

Verbs like "understand" are hard to test. Measurable verbs make objectives checkable and tie them to levels of Bloom's Taxonomy.

#### Metadata Completeness

The degree to which a resource's metadata record fills the fields that matter for finding, judging, and reusing it, expressed as a share of those fields.

Completeness is often the cheapest score to raise. A record with two of six core fields filled can reach six in minutes.

**Example:** A record with only title and author filled has two of the six core fields: title, author, subject, grade level, license, and description.

*See also:* Metadata Record, Metadata Generation

#### Metadata Generation

The creation of a resource's metadata fields, such as description and keywords, by reading the resource, often drafted by an agent.

It is a quick way to raise the metadata score. A person confirms that the entries match the resource.

**Example:** An agent drafts a description, subject, and keywords from a lesson page.

#### Metadata Metric

A rubric metric, worth up to 10 points, that scores how complete, accurate, and machine-readable the descriptive information about a resource is.

Good metadata is how strangers find a resource. It is one of the five reusability metrics.

*See also:* Metadata Record, Metadata Completeness

#### Metadata Record

A structured set of descriptive fields about a resource, such as title, author, subject, grade level, license, and description, stored with or apart from the resource.

Records let search tools and repositories find resources. Agents can draft them from a resource's content.

**Example:** A record lists the title "Watershed Basics," subject Earth science, grade level 6 to 8, and license CC BY 4.0.

*See also:* Dublin Core, Metadata Generation

#### Metric Score

A whole number from 0 to 10 that a reviewer assigns to one rubric metric for one resource, based on recorded evidence.

Ten metric scores add up to the total. The OER Evaluator compares human and agent scores one metric at a time.

**Example:** A reviewer who finds most images lack alt text gives the accessibility metric a 4.

*See also:* Score Scale, Evidence for a Score

#### MicroSim

A small, interactive, browser-based educational simulation that can be embedded in a web page with an iframe, usually built with p5.js, and published under an open license.

MicroSims are the interactive core of this book, and they serve as practice items that can also score well on modularity and portability.

**Example:** A p5.js sim where learners drag sliders to see how ten metric scores add up to a total.

*See also:* Interactive Simulation, Iframe Embedding

#### MicroSim Building

The process of designing and coding a MicroSim, often drafted by an AI agent from a written specification and then tested by a person.

MicroSim building turns text-heavy concepts into practice, and it earns practice and modularity points.

**Example:** A teacher describes a slider demonstration, and an agent produces a first working version.

#### MkDocs

A static site generator, written in Python and designed for documentation, that builds a website from Markdown files and a settings file.

This book is built with MkDocs and its Material theme, so its source stays plain text and its pages are easy to republish.

**Example:** A configuration file lists the site title, menu, and theme, and one build command writes the site.

*See also:* Static Site Generator, GitHub Pages

#### Modular Content

Content built from separate, self-contained units that each address one idea and can be rearranged or reused without the others.

Modular content lets a teacher assign one unit, and it lets reviewers and agents improve one piece at a time.

**Example:** A textbook where each section is its own page with its own objective, quiz, and license.

#### Modularity Metric

A rubric metric, worth up to 10 points, that scores whether a resource is divided into self-contained parts that can be used, moved, or replaced independently.

A resource that can be used only whole is hard to adapt. This metric is one of the five reusability metrics.

*See also:* Modular Content, Standalone Component

#### Multi-Agent Review

An evaluation in which two or more agents, often with different roles or prompts, score or check the same resource and their results are compared.

Agreement among agents is not proof, because similar models can share blind spots, so a person still checks the evidence.

**Example:** One agent scores a resource, and a second agent audits the first agent's report.

#### Multiple-Choice Question

A test item that presents a question stem and several answer options, of which one is correct and the others are plausible wrong answers.

These items are easy to score automatically, but writing good ones takes skill.

**Example:** "Which license permits commercial use with credit? A. CC BY, B. CC BY-NC, C. CC BY-ND, D. CC BY-NC-ND."

*See also:* Distractor Quality, Question Bank

#### No-Login Access

The condition in which a resource can be opened and used without creating an account, remembering a password, or signing in to any service.

Required logins block sharing and downloading, and students lose access when accounts expire. The portability metric rewards resources without them.

**Example:** A lesson page that opens directly from a shared link.

#### NoDerivatives Requirement

A license condition limiting reuse to unchanged copies of a work, so that adapted or remixed versions cannot be shared.

This condition blocks the revision and remixing that improvement work needs. The OER Evaluator warns about it before a team plans changes.

#### NonCommercial Requirement

A license condition limiting use of a work to purposes not primarily directed toward commercial advantage or private monetary compensation.

What counts as commercial can be unclear, for example in a paid class or a school fundraiser. The OER Evaluator flags the limit and leaves legal interpretation to qualified counsel.

**Example:** A district uses a CC BY-NC worksheet in free classes, while a company selling a course built on it raises a NonCommercial question.

#### OER Adaptation

The act of modifying an existing openly licensed material, by editing, translating, or reformatting it, to fit a new audience, course, language, or format.

Adaptation sits between using a resource as is and creating a new one. The book's improvement workflow is a guided form of it.

**Example:** Replacing urban examples in a biology chapter with local rural ecosystems.

#### OER Adoption

The decision by an instructor or institution to select an existing openly licensed material and use it, unchanged or with small edits, as a course's main teaching material.

Adoption is the decision the whole rubric supports. The ten metrics give evidence before a course commits to a resource.

**Example:** A department replaces a commercial algebra text with an open one for next fall.

#### OER Clearinghouse

A catalog that lists open educational resources from many sources and links to each, so teachers can search in one place.

A listing makes a resource easier to discover, though each catalog has its own submission rules and review process.

**Example:** A teacher submits an improved component to a national catalog so others can find it.

*See also:* OER Repository, Component Discoverability

#### OER Creation

The act of authoring a new teaching or learning material from scratch and releasing it for others to retain, reuse, revise, remix, and redistribute.

Creation is the most labor-intensive route to OER. Applying the rubric while writing helps avoid fixing the same problems later.

#### OER Quality

The degree to which an open educational resource helps its intended learners reach their intended learning outcomes, judged by what the resource does and not by how it looks.

Quality describes the fit between a resource and a learner, and it is one of the two halves of the rubric. The OER Evaluator measures it with five metrics.

#### OER Repository

An online service that stores openly licensed teaching materials, with descriptions and subject labels, so users can search for and download them.

Repositories are where many teachers first find candidates. Their listings are only as good as the metadata behind them, which the metadata metric scores.

**Example:** A statewide library site lists open textbooks by subject and grade.

#### Offline Access

The ability to use a resource without an internet connection, by downloading it or by storing its pages on the device.

Students with limited internet depend on it, and it follows from the retain permission.

#### Open Educational Resource

A teaching, learning, or research material that is in the public domain or released under a license granting everyone permission to retain, reuse, revise, remix, and redistribute it.

Open educational resources (OER) are what this book teaches readers to evaluate and improve. The OER Evaluator asks whether a candidate is good for learners and also whether it is truly open for reuse.

**Example:** An introductory statistics textbook under CC BY that teachers may download, edit, and post on a school website.

*See also:* The 5R Permissions, Open License, Free Resource

#### Open File Format

A file format whose specification is publicly documented and free to use, so any software can read and write it.

Open formats protect a resource from vendor lock-in and keep it editable for years.

**Example:** A lesson saved as HTML opens in any browser or text editor.

*See also:* Markdown, Platform Lock-In

#### Open License

A public legal grant of permission, published by a rights holder, that lets anyone retain, reuse, revise, remix, and redistribute a work, sometimes with stated conditions.

An open license is the legal core of an OER, and the first reusability metric asks whether a resource has a clear one. NonCommercial and NoDerivatives variants restrict some of the 5R permissions, so they are not fully open in the 5R sense.

**Example:** A page footer that reads "CC BY 4.0" with a link to the full terms.

*See also:* Open License Metric, Creative Commons

#### Open License Metric

A rubric metric, worth up to 10 points, that scores how fully and clearly a resource's legal terms give the public the five permissions to retain, reuse, revise, remix, and redistribute it.

Without clear terms, nothing else in the reusability half matters. NonCommercial and NoDerivatives terms lose points.

**Example:** A resource with a visible CC BY statement scores near 10, while one with no statement scores near 0.

*See also:* Open License, License Clarity

#### Open Pedagogy

A teaching approach in which students help create, revise, or share openly licensed materials as a regular part of their coursework, and do not only consume them.

Open pedagogy gives students real authorship. Its products need the same license and quality checks as any other OER.

**Example:** Students write a glossary chapter that is published under CC BY for future classes.

#### Open Textbook

A full-length textbook released under a license that lets anyone read it online, adapt it, and share it without paying the publisher.

Open textbooks are the most common whole-course OER and often the first resource a teacher scores with the rubric. Their size also makes modularity a frequent weak spot.

**Example:** OpenStax publishes open textbooks for college courses that instructors can assign at no cost to students.

#### Original Version

The resource exactly as it was before the improvements, frozen and labeled for use as the baseline in a test.

It must be the same version that received the baseline score. If it quietly changes, the comparison is unfair.

**Example:** "Watershed Basics v1," saved in the version history before any edits.

#### Outcome Coverage

The proportion of a course's stated learning outcomes for which a resource supplies teaching content, practice, or assessment, expressed as a fraction or percentage.

Coverage reveals gaps before adoption. Low coverage may mean pairing the resource with others.

**Example:** A resource that addresses 7 of a course's 10 outcomes has 70 percent coverage.

*See also:* Content Gap, Learning Outcome

#### Outcome Measure

The thing measured to decide which version did better, such as a score on a test of the skills the resource teaches.

It answers "What would I see in students if the improved version worked?" and it is chosen before the test.

**Example:** The score on a 20-question post-test aligned to the unit's objectives.

*See also:* Pre-Test, Post-Test

#### Outdated Content

Material in a resource that was accurate when written but no longer reflects current facts, practices, standards, or tools, so it can mislead readers.

Outdated content lowers the currency score and misleads learners, especially in fast-changing subjects.

#### Overconfident Score

A score that is higher or more certain than its evidence supports, such as a 9 for a metric the agent did not fully check.

It is the quietest agent error because nothing is invented. Signs include a high score with no quoted evidence.

**Example:** An agent gives accessibility a 9 without running any tool.

#### PDF-Only Distribution

The practice of publishing a resource only as a PDF file, with no editable source, which fixes the layout but makes changes difficult.

It is a common editable source failure. PDF-to-Markdown conversion is one fix, though quality varies.

**Example:** A textbook offers a PDF download and nothing else.

*See also:* PDF-to-Markdown Conversion, Editable Source Metric

#### PDF-to-Markdown Conversion

The process of turning the content of a PDF file into editable Markdown text, recovering headings, lists, and tables as far as possible.

It addresses PDF-only distribution but needs careful review, since tables and equations often convert poorly.

**Example:** A tool converts a PDF chapter into Markdown, and a teacher fixes a broken table.

*See also:* PDF-Only Distribution, Markdown

#### Peer Review

The practice in which teachers examine each other's work, here by swapping improved components and re-scoring them with the same rubric.

A second reviewer catches what an author is too close to see, and reading others' work sharpens one's own.

**Example:** Two teachers swap components and compare their new scores with the author's.

*See also:* Expert Review, Submission Review

#### Pilot Test

A small first run of a test, done to check the procedure and to learn what a larger test would need.

A pilot is not a weak version of the real test. It checks timing, instructions, and measures before more students are involved.

**Example:** A single class of 24 students tries the A/B test procedure.

*See also:* Sample Size, Results Summary

#### Plain Language

A style of writing that uses short sentences, common words, and clear organization so the intended reader understands on first reading.

Plain language lowers reading difficulty without lowering rigor, and it is the aim of a reading level rewrite.

**Example:** "Use the form" instead of "utilize the aforementioned form."

*See also:* Jargon, Reading Level Rewrite

#### Platform Lock-In

The dependence of a resource on one platform in a way that makes leaving costly or impossible, for example because its content cannot be exported.

Signs include proprietary storage formats, no export, and features that exist only inside one vendor's system. The portability metric scores lock-in down.

#### Portability Metric

A rubric metric, worth up to 10 points, that scores how easily a resource can be moved, opened, and used across devices, browsers, platforms, and learning management systems.

Portability is the fifth reusability metric. A resource that works only in one place has little value beyond it.

*See also:* Platform Lock-In, Browser Compatibility

#### Post-Test

An assessment given after students use a resource, to measure what they learned, and usually matched in content and difficulty to the pre-test.

It is matched to the pre-test and the learning objectives so that the two can be compared.

**Example:** The same students take a parallel 20-question quiz after the lesson.

*See also:* Pre-Test, Learning Gain

#### Practice Metric

A rubric metric, worth up to 10 points, that scores whether a resource gives learners chances to practice and receive feedback that tells them how to improve.

It is the fifth quality metric. Resources that explain without offering practice teach less than they appear to.

*See also:* Formative Assessment, Feedback Message

#### Practice Problem

A task that asks learners to apply a skill, such as solving, calculating, or writing, so that they gain fluency through repeated effort.

Problems that come with worked solutions score higher on the practice metric.

**Example:** "Compute the quality subtotal for metric scores 7, 5, 8, 6, and 9."

#### Practice Question Generation

The use of an AI model to draft quiz questions, answer keys, and feedback messages from a resource's content, for a person to review.

It can raise the practice score quickly, but drafts need checking for accuracy and for weak wrong answers.

**Example:** An agent drafts ten multiple-choice questions for a chapter, and a teacher rewrites two.

*See also:* Self-Check Question, Distractor Quality

#### Pre-Test

An assessment given before students use a resource, to measure what they already know, so that later learning can be compared with this starting point.

It sets a starting point so that learning gain can be calculated.

**Example:** Students take a 20-question quiz before the lesson begins.

*See also:* Post-Test, Learning Gain

#### Prerequisite Knowledge

The facts, vocabulary, and skills a learner needs to have mastered before starting a lesson or course in order to learn from it successfully.

A resource that states its prerequisites helps teachers decide where it fits. The same idea drives the learning graph.

#### Preserving Original Meaning

A quality of an edit in which the form of a resource's text changes while the claims, qualifiers, and intent of the author remain the same.

An agent can quietly drop a qualifier or turn a possibility into a certainty. Each change like that misleads readers who trust the source.

**Example:** Rewriting "may reduce" as "reduces" changes the meaning and fails this test.

*See also:* Reading Level Rewrite, Human Review of Changes

#### Primary Source

An original record from the time or person under study, such as a document, data set, photograph, or interview, that others have not interpreted.

Citing primary sources gives readers the strongest evidence for a claim, and reviewers value them above summaries.

#### Professional Development

The continuing learning that teachers do throughout their careers to improve their practice, through activities such as workshops, courses, and projects.

A workshop and capstone project count as professional development when hands-on and based on the teacher's own material, though credit depends on local rules.

**Example:** A teacher completes the workshop and capstone and reports the hours to their school.

*See also:* Teacher Training Workshop, Certificate

#### Prompt

The written instructions, questions, and supporting material that a person gives to a language model to tell it what to do.

The wording of a prompt strongly shapes the answer. Much of the book's agent work is careful prompt design.

**Example:** "Score this chapter on readability and quote the evidence for your score."

*See also:* Prompt Template, System Prompt

#### Prompt Iteration

The cycle of running a prompt, examining the results, adjusting the wording, and running it again to obtain better outputs.

Iteration is how a first rough prompt becomes a reliable one.

**Example:** A teacher rewrites a prompt three times until the agent stops skipping the evidence column.

#### Prompt Refinement

The targeted revision of a prompt in response to errors found in calibration, followed by a rerun to see whether the errors shrink.

Each change targets one observed error, so its effect can be seen.

**Example:** After finding inflated accessibility scores, a team adds a rule to cite a tool report for every accessibility score.

#### Prompt Template

A reusable prompt with fixed instructions and blank slots that are filled with new content, such as a resource's text, each time it is used.

Templates make evaluations repeatable across many resources.

**Example:** A template with a blank for the chapter text and fixed instructions for scoring.

#### Proprietary License

A legal agreement in which a rights holder grants only narrow, listed uses of a work, such as viewing it or using a single copy, and keeps control of everything else.

A proprietary agreement signals a resource that cannot be revised or shared, so it earns a low open license score. A reviewer reads the terms to learn what use is actually allowed.

**Example:** An e-book agreement that lets one student account read the text and forbids sharing it.

#### Public Domain

A status held by creative works that copyright does not cover, either because protection has expired, was never available, or was waived by the owner, so anyone may use them freely.

Public-domain works carry no license conditions, which makes them easy to reuse. The OER Evaluator still looks for a clear note that a work is in the public domain, since a reuser cannot simply assume it.

**Example:** A report written by a United States federal agency as part of official duties is in the public domain.

#### Publication Date

The date on which a resource was first released to the public, shown on the resource or recorded in its metadata.

It gives a reviewer a first estimate of whether content is current. A missing date counts against both currency and metadata.

#### Publishing OER

The act of making a resource openly available at a stable public address, under an open license and with complete metadata, so that anyone can find, use, and adapt it.

Publishing differs from posting a file, because a resource on a shared drive cannot be found or trusted by strangers.

**Example:** A teacher posts an improved lesson on a public site with a CC BY statement and a metadata record.

*See also:* Static Site Generator, GitHub Pages

#### Pull Request

A proposal, made on a code-hosting site, to merge changes from one copy of a project into another, which the owner can review, discuss, and accept or decline.

Pull requests let improvements flow back to an author, and they match the book's human review of changes.

**Example:** A teacher fixes 14 broken links in a fork and sends a pull request to the original author.

#### Qualitative Feedback

What students or teachers say in their own words, such as written comments, answers to open questions, or short interviews, about a lesson or resource.

It explains the why behind the numbers.

**Example:** A comment that the quiz would not open on a tablet explains a drop in completion.

#### Quality Dimension

A group of five rubric metrics that measure how well a resource helps learners learn: accuracy and currency, alignment, readability, accessibility, and practice with feedback.

Its subtotal is worth up to 50 points. Reading it apart from the reusability half shows where a resource is strong or weak.

#### Quality Rubric

A scoring guide that lists criteria for judging a resource and describes what each level of performance looks like on every criterion.

The Ten-Metric Rubric is this book's rubric of this kind. Using one shared guide keeps scores comparable across reviewers.

*See also:* Ten-Metric Rubric, Scoring Descriptor

#### Quality Subtotal

The sum of a resource's five quality metric scores, which ranges from 0 to 50 and shows how well the resource helps learners learn.

Reading it beside the reusability subtotal shows which half of the rubric needs work.

**Example:** Quality scores of 8, 7, 9, 6, and 5 give a subtotal of 35.

*See also:* Reusability Subtotal, Total Score

#### Quality Versus Reusability

A distinction between how well a resource teaches and how easily others can adapt and share it, two independent qualities, so a resource can be strong in one and weak in the other.

All four combinations occur in practice, so the book keeps two subtotals and reads them side by side.

**Example:** A well-written lesson saved only as a locked PDF teaches well but is hard to reuse.

*See also:* Quality Dimension, Reusability Dimension

#### Question Bank

A stored collection of test or practice questions, tagged by topic and difficulty, from which teachers can assemble many different quizzes.

A bank lets teachers build new quizzes and supports retrieval and spaced practice. It also raises a resource's reuse value.

#### Question Difficulty

A measure of how hard a question is for the intended learners, often expressed as the share of learners who answer it correctly.

A balanced mix of easy and hard questions keeps practice useful, and tagging difficulty makes a question bank easier to use.

#### Quiz

A short set of questions that checks what learners know about a topic, often scored, and used for practice or low-stakes assessment.

Quizzes are common in OER. The practice metric looks at their quality, answer keys, and feedback.

**Example:** Ten multiple-choice questions at the end of a chapter.

*See also:* Question Bank, Answer Key

#### Random Assignment

The use of chance, such as a coin flip or a list of random numbers, to decide which version each student receives.

Chance spreads hidden differences between students evenly across groups, so the version is the likelier cause of any difference.

**Example:** A teacher draws names from a hat to place students in the control or treatment group.

*See also:* Confounding Variable, Sampling Bias

#### Re-Scoring

The scoring of an improved resource on all ten metrics again, using the same rubric, evidence rules, prompt, and tools as the first scoring.

Using the same method both times makes any change in score a fair measure of improvement.

**Example:** After improvements, a resource rises from a total of 62 to 78 on the same rubric.

#### Readability Formula

A mathematical formula that estimates how hard a text is to read, typically from sentence length and word length or difficulty.

Formulas are fast and repeatable, and tools or agents can run them. They ignore meaning, so the book treats their results as a screen and not a verdict.

#### Readability Metric

A rubric metric, worth up to 10 points, that scores how easily the intended audience can read and understand a resource, using reading level, vocabulary, structure, and fit.

It combines a formula result with human judgment of audience fit, because neither alone is enough.

*See also:* Reading Level, Audience Fit

#### Reading Level

An estimate of the school grade or reading skill a person needs in order to understand a given text without difficulty.

Matching reading level to the audience is central to the readability metric. Formulas give a number, and a person checks it.

#### Reading Level Rewrite

The revision of text, often drafted by an AI model, to bring its reading level closer to the intended audience's while keeping its meaning.

It carries a risk of changing meaning, so a person compares the rewrite with the source.

**Example:** An agent shortens long sentences in a grade 13 passage to reach grade 9.

*See also:* Plain Language, Preserving Original Meaning

#### Redistribute Permission

The permission within the 5Rs to share copies of a work, in its original or a changed form, with other people.

Redistribution is how an improved resource reaches colleagues. The OER Evaluator checks that nothing in the license or the hosting blocks sharing.

#### Release Notes

A short, readable summary of what changed in each released version of a resource, grouped as added, changed, fixed, and removed.

They tell reusers whether to update and what to expect.

**Example:** "Added: quiz for lesson 4. Fixed: three broken links."

#### Remix Permission

The permission within the 5Rs to combine a work with other materials, including other openly licensed works, to create a new work.

Remixing lets teachers build custom courses from several sources, but it works only when the licenses involved are compatible. The OER Evaluator flags terms that block it.

**Example:** Merging chapters from two open books into one reader for a single course.

*See also:* License Compatibility, License Conflict

#### Resource Selection

The process of finding candidate teaching materials, comparing them against stated criteria, and choosing which ones a course will use.

The OER Evaluator makes selection evidence-based by giving each candidate a total, two subtotals, and a band that can be compared side by side.

#### Responsive Layout

A web page design that adjusts the arrangement and size of content automatically to fit screens of different widths, from phones to wide monitors.

Many students read on phones, so layouts that adapt serve more learners.

#### Results Summary

A short written account of what a test showed, covering the question, method, results, limits, and next steps in one or two pages.

It is what a colleague, principal, or adopter reads, so it states results honestly, including limits.

**Example:** A one-page summary reports a 7-point difference, a sample of 24, and a caution that the test was a pilot.

*See also:* Pilot Test, Impact Reporting

#### Retain Permission

The first of the 5Rs, the right to make, own, and control copies of a work, such as by downloading, archiving, and backing it up.

Holding a copy protects a teacher when a website changes or disappears. The OER Evaluator checks that a resource can be downloaded and stored without a login.

**Example:** Saving a PDF of an open text to a school drive so class access never depends on a website.

*See also:* The 5R Permissions, Offline Access

#### Retrieval Practice

A study method in which learners recall information from memory, for example by answering questions, and not simply reread it.

Research on learning supports it, and the practice metric credits resources that include it.

#### Reusability Dimension

A group of five rubric metrics that measure how easily other people can find, change, and reuse a resource: open license, modularity, metadata, editable source, and portability.

Its subtotal is also worth up to 50 points. A resource can be excellent for learners and still be hard for others to reuse.

#### Reusability Subtotal

The sum of a resource's five reusability metric scores, which ranges from 0 to 50 and shows how easily others can find, change, and reuse the resource.

A low subtotal on a well-written resource means improvement work should focus on license, format, and metadata.

**Example:** Reusability scores of 9, 4, 6, 8, and 7 give a subtotal of 34.

*See also:* Quality Subtotal, Total Score

#### Reusable Component

A part of a resource that someone else can lift out and use in a different course without asking for help.

It stands alone, embeds without edits, and carries its own license and metadata.

**Example:** A single quiz packaged with its license and description.

*See also:* Component Packaging, Component Library

#### Reuse Permission

The permission within the 5Rs to use a work in its original form in many settings, such as a class, a website, or a video.

Reuse is the base permission every open license grants. The OER Evaluator treats a resource that cannot be used publicly without extra approval as weak on the open license metric.

#### Reuse Tracking

The effort to learn who is using a published resource and how they are using it, through signals such as links, copies, and reports from users.

An open license lets people reuse without asking or telling the author, so the picture is always partial. Signals include links, forks, and messages.

**Example:** An author notes that three schools forked the repository and one cited the lesson in a course syllabus.

*See also:* Usage Analytics, Impact Reporting

#### Review Checklist

A short list of items a reviewer gathers before scoring, such as the resource files, the license statement, and a blank worksheet, so the review does not stall.

It prevents stopping halfway to hunt for a missing piece, and it begins a manual review.

#### Review Report

The finished document that a review produces, containing the completed worksheet, subtotals, total, band, decision, and the improvements that would raise the score most.

It names the reviewer and the date and lists open questions, so a decision-maker can act without repeating the review.

*See also:* Adoption Recommendation, Rubric Worksheet

#### Review Workflow

The fixed, ordered set of steps a reviewer follows, from receiving a resource through scoring and reconciling to delivering a decision.

A fixed order keeps reviews comparable and keeps a reviewer from skipping the dull steps.

*See also:* Review Checklist, Agent Workflow

#### Reviewer

A person who applies the rubric to a resource, scoring each metric and recording the evidence behind each score so that others can check the judgment.

Reviewers are the book's main audience. A human reviewer's careful scores are the standard against which AI agent scores are checked.

#### Reviewer Bias

A systematic tendency in a reviewer's judgments, such as favoring familiar authors or scoring generously, that pulls scores away from what the evidence supports.

Bias is why the book asks for recorded evidence, second reviewers, and calibration sessions. The same idea underlies score inflation in agents.

**Example:** A reviewer who knows the author gives every metric a point more than the evidence supports.

*See also:* Calibration Session, Score Inflation

#### Reviewer Notes

Informal jottings a reviewer makes during a review, such as questions, hunches, and items to check later, that are not yet confirmed observations.

Notes differ from evidence. A note is a lead that may turn into evidence once checked, or may prove wrong.

#### Reviewer Training

The preparation new reviewers receive before scoring real resources, covering the rubric, the checks, the tools, and the habits that keep scores honest, and ending with practice and calibration.

Trained reviewers give more consistent scores, and the book's workshop and certificate build on this training.

*See also:* Calibration Session, Teacher Training Workshop

#### Revise Permission

The permission within the 5Rs to change a work by adapting, editing, translating, or reformatting it to fit a new need.

Revision is what lets an OER improve over time, and it is the permission that NoDerivatives terms withhold. The improvement work in this book depends on it.

**Example:** Translating a science chapter into Spanish for a local school.

*See also:* Derivative Work, CC BY-ND

#### Revision History

A dated record of the changes made to a resource since it was first published, showing what changed, when, and by whom.

It shows whether a resource is maintained, which supports the currency score, and it feeds the editable source checks.

#### Role Prompting

A prompting technique that tells a model to act as a specific role, such as an accessibility reviewer, to shape its focus and tone.

Roles help an agent concentrate on one task, and the book uses them for second-agent checks.

**Example:** "You are an accessibility reviewer. List every barrier you find."

#### Rubric Metric

One of the ten measurable criteria of the rubric, scored from 0 to 10 for a single aspect of a resource, such as accessibility or metadata.

Splitting the judgment into ten metrics keeps a high total from hiding a failed area. Each metric comes with checks and evidence to record.

#### Rubric Prompt

A prompt that tells an agent to score a resource against the ten-metric rubric and return its scores with evidence in a structured form.

It carries the checks from the metric chapters and the scoring rules, so it is where the book's rubric meets the agent.

**Example:** A prompt that lists each metric, its checks, and the report format the agent must follow.

*See also:* Prompt Template, Agent Scoring

#### Rubric Reliability

The consistency of a rubric's results when different reviewers, or the same reviewer at different times, score the same resource.

A reliable rubric produces similar scores whoever applies it. The book checks reliability with calibration and agreement statistics.

#### Rubric Validity

The degree to which a rubric measures what it claims to measure, which in this book means whether higher scores go with better results for learners.

A consistent rubric can still measure the wrong thing, so the book ends with a test of whether rubric scores relate to student learning.

#### Rubric Worksheet

A form on which a reviewer records everything about one review: the resource's identity, the ten metric scores, the evidence for each, the subtotals, and the total.

The worksheet makes reviews comparable, and it is the main document teachers submit when they seek the certificate. The book provides a sample worksheet.

**Example:** A completed worksheet lists "Accessibility: 4" with a note that most images lack alt text.

*See also:* Review Report, Evidence Recording

#### Rubric-Outcome Correlation

The strength of the statistical relationship between resources' rubric scores and the amount students learn from those resources, measured across several tested resources.

It closes the loop of the book. If higher-scoring resources tend to produce larger gains, the rubric measures something that matters.

**Example:** Seven resources are compared, and those with higher totals tend to show larger normalized gains.

*See also:* Rubric Validity, Score Correlation

#### Run-to-Run Variance

The variation in an agent's scores when it scores the same resource with the same prompt more than once, measured across repeated runs.

Language models do not always give the same answer twice. An agent whose score swings from 5 to 7 is not measuring anything stable on that metric.

**Example:** Five runs on one resource give accessibility scores of 5, 7, 6, 5, and 7.

#### Sample Size

The number of students included in a test, which affects how far the result can be trusted because larger groups smooth out chance differences.

A larger sample gives a steadier answer because chance fluctuations average out, while a small one can be swung by a few unusual students.

**Example:** A pilot with 24 students is small and gives a rough answer.

#### Sampling Bias

A systematic error in which the students in a test differ from the students one wants to learn about, so the result does not apply to them.

The result is true for the group tested and misleading about everyone else.

**Example:** Testing only honors students and then claiming the version works for all.

*See also:* Random Assignment, Equity Consideration

#### Schema.org Markup

Structured data added to a web page, using the shared Schema.org vocabulary, that tells search engines and other software what the page is about.

LRMI properties are expressed through it, so it connects educational metadata to everyday web search.

**Example:** A block of code on a page that names its title, license, and educational level.

*See also:* LRMI, Machine-Readable Metadata

#### Scope and Sequence

A document that lists the topics a course covers (the scope) and the order in which they are taught (the sequence).

It helps a reviewer judge whether a resource's order fits the course, and it links to the idea of prerequisites.

#### Score Band

A named range of total scores used to describe overall standing: Excellent 90 to 100, Good 75 to 89, Fair 50 to 74, Weak 25 to 49, and Poor 0 to 24.

Bands give teachers and administrators a quick label, but the band alone is not the adoption decision.

#### Score Correlation

A statistic, ranging from -1 to +1, that measures how closely two sets of scores for the same resources rise and fall together.

An agent can rank resources correctly while scoring every one too high, so correlation is read together with the average difference.

**Example:** An agent scores exactly one point above humans on every resource, so correlation is high even though the scores differ.

#### Score Difference Threshold

The largest gap between a human score and an agent score on a metric that still counts as agreement; this book flags gaps of more than 3 points.

The threshold is a choice, made before looking at the numbers, so that it cannot be bent to fit the results.

**Example:** A human 5 and an agent 8 agree, while a human 5 and an agent 9 are flagged.

#### Score Gain

The difference between a resource's total score after an improvement and its total score before the improvement, found by subtracting the earlier total from the later one.

A positive gain means the resource passes more of the rubric's checks. Reports state the gain in the total and on each metric.

**Example:** A resource that moves from 62 to 78 has a score gain of 16.

*See also:* Re-Scoring, Improvement Plan

#### Score Inflation

A systematic tendency of an agent to score higher than careful human reviewers do, across many metrics and many different resources.

Inflation is a pattern and not a single error. Even a small generous bias can push totals across an adoption line.

**Example:** An agent averages one point above human reviewers on nearly every metric.

*See also:* Overconfident Score, Calibration Against Humans

#### Score Reconciliation

The step-by-step handling of a metric on which two reviewers' scores differ by more than 3 points: each states evidence, they repeat the check, and they choose the score the evidence supports.

The step keeps large disagreements from being averaged away. It uses the same threshold as the book's flag for human and agent differences.

**Example:** Reviewers scoring 3 and 8 on metadata each show their evidence and then agree on 5 after rechecking.

#### Score Scale

The range of values a metric score can take, which in this book is whole numbers from 0 to 10 with no half points.

The same scale applies to all ten metrics, which lets scores be added and compared. Descriptors say what each level means.

#### Scoring Descriptor

A short statement that describes what one level of the score scale looks like for a metric, so different reviewers read the same score the same way.

Without descriptors, one reviewer's 7 is another reviewer's 9. Calibration sessions test whether the descriptors are clear enough.

**Example:** A descriptor for a 9 or 10 on alt text might say that every informative image has an accurate description.

*See also:* Score Scale, Calibration Session

#### Screen Reader

Assistive software that reads the content of a screen aloud or turns it into braille, used mainly by people who are blind or have low vision.

Screen reader behavior is the test for alt text, headings, link text, and table markup. Reviewers try one when they can.

#### Second-Agent Cross-Check

The use of a second agent to review the first agent's report, looking for unsupported claims, missing evidence, and arithmetic that does not add up.

It is a cheap first filter, but it does not replace human checking.

**Example:** A second agent is asked to list faults in the first report and not to produce a fresh score.

#### Secondary Source

A work that describes, interprets, or summarizes primary sources or other research, such as a textbook, review article, or encyclopedia entry.

Secondary sources explain well but sit one step away from the evidence. A resource that cites only these for disputed claims weakens its citation quality.

#### Self-Check Question

A question placed within a lesson that lets learners test their own understanding and see the answer without a teacher's grade.

Self-checks are the cheapest form of practice, and agents can draft them quickly, with human review.

**Example:** "Which of the 5Rs lets you translate a chapter?" followed by a reveal-answer button.

*See also:* Formative Assessment, Practice Question Generation

#### ShareAlike Requirement

A license condition under which adapted versions of a work are released under the same license or a compatible one.

ShareAlike affects how a resource can be combined with others. The OER Evaluator reads it before judging whether a remix is possible.

#### Source Citation

A reference in a resource that identifies where a fact, quotation, image, or idea came from, so a reader can find the original.

Citations let readers and reviewers verify claims. The OER Evaluator checks that citations exist and that agents have not invented them.

**Example:** "Smith, J. (2019). Soil Science. State Press, p. 44." placed after a statistic.

*See also:* Citation Quality, Invented Citation

#### Source Format

The file format in which a resource's original, editable content is stored, such as Markdown, HTML, or a word processing file.

The format decides how easily others can revise the resource, so the editable source metric inspects it.

**Example:** A lesson authored as Markdown files in a repository.

*See also:* Open File Format, PDF-Only Distribution

#### Source Verification

The confirmation of a claim by going to the original source, such as the license statement or the cited reference, and not to the agent's summary of it.

It is the strongest verification step.

**Example:** A reviewer opens a cited article to confirm that it says what the agent claims.

#### Spaced Practice

A study method that distributes practice over several sessions separated by time, instead of packing it into a single sitting.

Spacing improves long-term memory. A resource can support it by revisiting earlier ideas in later quiz sets.

#### Spot Check

The verification of a sample of an agent's claims and not all of them, chosen to include at least one claim per metric, claims that carry weight, and a few at random.

It saves effort when work is well evidenced and risk is low. An error found in the sample widens the check.

**Example:** A reviewer verifies 12 of 40 claims and records which ones were checked.

#### Standalone Component

A piece of a resource that makes sense and works when separated from the rest, without needing earlier or later material.

It is the test for modularity: lift the piece out and see whether it still works.

**Example:** A simulation page that explains its purpose and gives its own instructions.

#### Standards Alignment

A documented mapping between a resource's content and the published learning standards of a state, nation, or professional body, showing which standards each part addresses.

Teachers often need proof that a resource covers the standards they must teach. The alignment metric rewards a clear mapping over a vague claim.

#### Static Site Generator

A program that turns plain source files, usually Markdown plus a few settings, into a folder of finished web pages.

The pages are fixed files, so they are fast, cheap to host, and easy to copy, which suits open resources.

**Example:** A tool reads Markdown chapters and writes a complete website.

*See also:* MkDocs, GitHub Pages

#### Structured Output

A model response organized in a predefined, regular format, such as a table or labeled fields, so that software can read it without guessing.

Structured output makes agent reports comparable across resources and easy to total.

**Example:** A report with one row per metric holding the score, the evidence, and the checks.

#### Student Data Privacy

The protection of information about students, such as names, identification numbers, grades, and work, from being collected, shared, or used in ways they and their families have not agreed to.

Reviewing resources needs no student data, so the book keeps student records away from agents.

**Example:** A reviewer removes student names from a sample before any text goes to an AI service.

#### Student Privacy in Testing

The set of practices that keep information about students safe while a test is run and afterward, such as collecting little data, storing it securely, and removing identities.

Reviewing resources needs no student data, but an A/B test does, so this is where the rules for that data are set.

**Example:** A teacher stores scores under random codes in a password-protected file.

*See also:* Anonymized Data, Student Data Privacy

#### Student Survey

A short set of questions that asks students what they thought of a lesson or resource, including whether they could follow it and what got in the way.

Test scores say what students learned, while a survey says what they experienced, including barriers.

**Example:** Three rating questions and one open question given after the lesson.

*See also:* Qualitative Feedback, Exit Survey

#### Subject Field

The metadata field that names the topic or discipline a resource covers, preferably chosen from a standard list of terms.

Searchers filter by subject, so a missing or unusual value hides a resource.

#### Submission Review

The examination of a certificate submission against the requirements by a reviewer who did not take part in the work.

It checks that the evidence is real, that agent output was verified, and that claimed gains hold up.

**Example:** A reviewer re-checks the largest claimed gain and asks for a resubmission when the findings log shows no reasons.

*See also:* Certificate Requirements, Peer Review

#### System Prompt

Standing instructions given to a language model before a task begins that set its role, rules, and output format for everything that follows.

It keeps an agent consistent from one resource to the next.

**Example:** A system prompt tells the agent to act as a careful reviewer and to list the checks it could not verify.

#### Table Accessibility

The use of proper header cells, captions, and simple structure in a data table so that assistive technology can tell what each cell means.

Tables built for layout or full of merged cells confuse screen readers. The OER Evaluator checks for header rows and captions.

#### TASL Attribution Format

A four-part pattern for crediting a reused work that lists its Title, its Author, the Source where it was found, and its License.

TASL gives teachers a simple checklist for building a complete credit line. The book's examples and the OER Evaluator's reports use it.

**Example:** Title: Watershed Basics. Author: Pat Lee. Source: example.org/watershed. License: CC BY 4.0.

*See also:* Attribution Statement, Attribution Requirement

#### Teacher Training Workshop

A planned session in which teachers learn a skill by practicing it on their own material, here evaluating and improving OER with AI agents.

The workshop is where the book's methods are taught in person, and it leads toward the certificate.

**Example:** A one-day workshop where each teacher scores and improves a resource from their own subject.

*See also:* Workshop Agenda, Facilitator Guide

#### Ten-Metric Rubric

A scoring guide that rates an open educational resource on ten metrics, five for quality and five for reusability, each worth 10 points, for a total of 100.

It is the central instrument of this book. Later chapters teach how to score each metric by hand and with AI agents.

**Example:** A reviewer gives a resource 8 for readability, 3 for accessibility, 9 for open license, and so on through all ten metrics, then adds them.

*See also:* Rubric Metric, Total Score

#### Test Hypothesis

A prediction, written down before a test, about what the improved version will do for students compared with the original version.

It turns a hope such as "the new version is better" into a statement that data can support or fail to support, and writing it first prevents bending the claim to fit results.

**Example:** "Students using the improved version will gain at least 5 points more than students using the original."

#### Text Structure

The way the writing in a resource is organized, through headings, paragraph length, lists, examples, and summaries, to help readers see its shape.

Good structure helps readers find information again, and it helps tools split a resource into components.

#### The 5R Permissions

A framework, described by David Wiley, of five permissions that together define an open resource: retain, reuse, revise, remix, and redistribute.

The 5Rs are the working test for openness in this book. The open license metric asks which of the five a resource actually grants.

**Example:** A resource that a teacher can download, use in class, edit, combine with another, and share grants all five.

*See also:* Retain Permission, Open License

#### Third-Party Content

Material inside a resource, such as an image, chart, or quotation, that was made by someone other than the resource's author and may carry its own separate rights.

A resource's overall license may not cover such pieces, so the OER Evaluator looks for them when it scores license clarity.

**Example:** A photo in a CC BY chapter labeled "used with permission" has rights separate from the chapter's.

*See also:* Fair Use, License Clarity

#### Time on Task

The number of minutes a student spends actively working on a learning activity, recorded by a platform log or a teacher's timer.

It adds context to scores, since a version that takes much longer may carry a hidden cost.

#### Title Field

The metadata field that holds the name by which a resource is known, so people and search tools can recognize and list it.

A specific title helps discovery, and a vague one such as "Chapter 1" does not.

#### Token

A small unit of text, often a word or part of a word, that a language model reads and writes and by which usage and cost are measured.

Token counts determine both how much fits in the context window and what a service charges.

**Example:** A short word may be one token, while a long word may be split into several.

*See also:* Context Window, AI Cost

#### Tool Use

An agent's ability to call external programs, such as a link checker or a contrast calculator, and read the results.

Tools give hard evidence in place of guesses, so tool logs make an agent's report easier to trust.

**Example:** An agent runs a readability script on a chapter and cites the result.

#### Total Score

The sum of a resource's ten metric scores, which ranges from 0 to 100 and combines the quality subtotal and the reusability subtotal.

The total places a resource in a band and feeds the adoption rule, but it can hide a weak metric, so it is read together with the lowest metric.

**Example:** A quality subtotal of 38 and a reusability subtotal of 31 give a total of 69, which falls in the Fair band.

*See also:* Score Band, Adoption Threshold

#### Train-the-Trainer

A model in which people who have learned a skill are trained to teach it to others, so a program can grow beyond its founders.

It lets a program grow without relying on its founders, while guarding quality through supervised co-facilitation.

**Example:** A certified teacher co-facilitates a workshop with an experienced facilitator, then leads one.

*See also:* Training Kit, Facilitator Guide

#### Training Evaluation

The assessment of whether a training worked, for example by asking how participants reacted, what they learned, whether their behavior changed, and what results followed.

An exit survey measures only the first of these, so judging a program takes evidence over time.

**Example:** A program checks, three months later, whether certified teachers still review resources.

*See also:* Exit Survey, Teacher Training Workshop

#### Training Kit

The bundle of materials, packaged as an open resource, that lets a teacher or trainer run the workshop without help from the original team.

It follows the book's own advice: packaged, licensed under CC BY, with metadata and a version number.

**Example:** A downloadable folder with the agenda, facilitator guide, sample resources, and worksheets.

*See also:* Facilitator Guide, Component Packaging

#### Transcript

A complete text version of spoken audio or video content, including speaker names and key sounds, readable apart from the media.

Transcripts help deaf and hard-of-hearing users, screen reader users, and anyone who prefers reading, and they make media searchable.

#### Treatment Group

The group of students in a test who use the improved version of a resource, so that their results can be compared with those of the control group.

The word comes from medicine and names the thing being tested. Here, the treatment is the set of improvements.

**Example:** Twelve students use the improved lesson and serve as the treatment group.

*See also:* Control Group, Improved Version

#### Universal Design for Learning

A framework for designing instruction that gives learners multiple ways to engage with material, to understand it, and to show what they have learned.

It widens accessibility beyond disability to everyone's variation. The book uses it as a design lens alongside WCAG.

#### Usage Analytics

Counts of how a site is used, such as visits, pages viewed, where visitors come from, and which components are opened most.

They show reach and patterns, and they help plan, for example by showing that a component no one opens may need to be easier to find.

**Example:** A report shows the quiz page was opened 300 times last term.

*See also:* Reuse Tracking, Impact Reporting

#### Verification Step

A defined action a person takes to confirm or refute one claim in an agent's report, naming the claim, the way to test it, and the result that would confirm it.

Steps get stronger the further they move from the agent's own words, and the strongest is to go to the original source.

**Example:** To verify a license claim, open the page and read its license statement.

#### Version Control

A system that records every change to a set of files over time, who made it, and why, so earlier versions can be compared or restored.

It supports revision history, safe collaboration, and the change logs used in improvement work.

**Example:** An author restores a chapter to how it looked last month.

#### Vocabulary Level

The difficulty of the words in a text, judged by how common they are and how likely the intended audience is to know them.

Unexplained hard words are a major barrier to learners. Checking vocabulary level supplements a grade formula.

#### WCAG

The Web Content Accessibility Guidelines, a set of international technical recommendations published by the World Wide Web Consortium (W3C) for making web content usable by people with disabilities.

WCAG is the source of the book's accessibility checks. It groups its criteria into perceivable, operable, understandable, and robust, at levels A, AA, and AAA.

**Example:** One WCAG criterion calls for a text alternative for every informative image.

#### WCAG 2.1 AA

Version 2.1 of the Web Content Accessibility Guidelines at conformance level AA, the middle of three levels, which many institutions adopt as their accessibility target.

It is the standard the accessibility metric checks against, including contrast ratios of at least 4.5:1 for normal text and 3:1 for large text.

**Example:** Light gray text on white that measures 2.5:1 fails the AA contrast test.

*See also:* WCAG, Contrast Ratio

#### Word Processing File

A document file made by writing software, such as a .docx file, that stores text, styles, and images in one file.

Most teachers can edit these files, but they are harder to track in version control than plain text.

**Example:** A .docx lesson plan that a colleague edits and returns.

*See also:* Source Format, Version Control

#### Worked Example

A problem shown with its complete solution, step by step, with reasons for each step, so a learner can see how the answer is reached.

Worked examples support beginners and are a sign of practice quality. Agents can draft them, and a person checks the reasoning.

**Example:** A statistics page that shows how to compute a mean from five numbers, one step at a time.

*See also:* Worked Solution, Practice Problem

#### Worked Solution

A complete step-by-step answer to a practice problem that shows the reasoning, so learners can compare it with their own work.

It gives feedback at scale, but an error in a solution misleads learners, so reviewers check them.

**Example:** For the subtotal problem: 7 + 5 + 8 + 6 + 9 = 35.

*See also:* Practice Problem, Worked Example

#### Workshop Agenda

The schedule of a workshop, listing each session, its length, and what participants take away, in an order where each session prepares the next.

A good agenda orders the sessions so that each one prepares the next.

**Example:** A one-day agenda that moves from the rubric to calibration, then to checking the agent, then to improvement.

*See also:* Teacher Training Workshop, Facilitator Guide

#### Zero Textbook Cost Course

A class in which students pay nothing for required learning materials because the instructor uses open or library-provided resources, and which a college usually labels in its course schedule.

Many colleges label these classes in their schedules so students can choose them. OER adoption is a common way to reach that label, and the OER Evaluator helps confirm the free materials are also good ones.

**Example:** A community college marks a composition class "ZTC" because every reading is openly licensed.

*See also:* OER Adoption, Course Material Affordability
