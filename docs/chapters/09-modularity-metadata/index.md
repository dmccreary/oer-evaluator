---
title: "Modularity and Metadata"
description: "Shows how to score the open license, modularity, and metadata metrics, including standalone components, Dublin Core records, controlled vocabularies, and machine-readable metadata that help others find and reuse a resource."
generated_by: claude skill chapter-content-generator
date: "2026-10-23 22:22:46"
version: 1.11
---

# Modularity and Metadata

## Summary

Shows how to score the open license, modularity, and metadata metrics, including standalone components, Dublin Core records, controlled vocabularies, and machine-readable metadata that help others find and reuse a resource. It starts the reusability metrics, which score how easily others can find and reuse a resource. After this chapter you can judge whether a resource is split into standalone components and whether its metadata lets others find it.

## Concepts Covered

This chapter covers the following 23 concepts from the learning graph:

| Concept | Concept Impact Score |
|---------|-----------------------|
| Open License Metric | 2 |
| License Clarity | 1 |
| Modularity Metric | 21 |
| Modular Content | 20 |
| Standalone Component | 15 |
| Component Granularity | 1 |
| Cross-Reference Dependence | 1 |
| Embeddable Component | 8 |
| Metadata Metric | 98 |
| Metadata Record | 97 |
| Dublin Core | 92 |
| Title Field | 14 |
| Author Field | 14 |
| Subject Field | 17 |
| Grade Level Field | 15 |
| License Field | 15 |
| Description Field | 14 |
| Keywords | 3 |
| Controlled Vocabulary | 1 |
| LRMI | 1 |
| Schema.org Markup | 3 |
| Machine-Readable Metadata | 2 |
| Metadata Completeness | 13 |

## Prerequisites

This chapter builds on concepts from:

- [Chapter 2: Open Licenses and Attribution](../02-open-licenses-attribution/index.md)
- [Chapter 3: The Ten-Metric Rubric and Scoring](../03-ten-metric-rubric-scoring/index.md)
- [Chapter 4: Open File Formats and Version Control](../04-open-formats-version-control/index.md)

---

!!! mascot-welcome "You Cannot Reuse What You Cannot Find"
    ![Echo waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    The reusability metrics ask whether another teacher can find a resource, know what it is, and lift out the part they need. This chapter covers three of them: whether the license is clear, whether the parts stand alone, and whether the description lets a search find it. Let's dive in and check the evidence!

The first five metrics of the rubric asked how well a resource teaches. The last five ask how easily others can reuse it, and the first three of those fill this chapter. A resource may be superb and still go unused, because no one can tell what license it has, because its best part is tangled into the rest, or because nothing records its subject, so a search never turns it up.

The order of the chapter follows a reuser's path. A teacher first needs to know what she may do, which is the open license metric. She then needs to take out only the part she wants, which is modularity. And before any of that, she must find the resource, which is the metadata metric and the largest part of the chapter.

## The Open License Metric

The **open license metric** is the sixth metric of the rubric. It asks whether a clear open license is stated on every component of the resource and whether attribution is complete. Chapter 2 taught you to read a license and to credit one, and this metric turns that skill into a score. It is scored with ten checks. The checks below are the book's list, and they replace the preview list in the Chapter 3 worked example. The score for *Watershed Basics* comes out the same.

A failed check is **serious** when it leaves a reuser unsure of their rights to some part of the resource. When a serious check fails, the score cannot go above the band's lower number, and a score of 10 requires every check to pass.

| # | Check | Serious if it fails? |
|---|---|---|
| 1 | A license is named on the main page | Yes |
| 2 | The license version is stated | No |
| 3 | A link to the license text is given | No |
| 4 | The owner is named | No |
| 5 | The scope of the license is stated | No |
| 6 | The license appears on every page or component | No |
| 7 | Machine-readable license marking is present | No |
| 8 | Every third-party item is identified and carries its own notice | Yes |
| 9 | Credit lines for reused material are complete | No |
| 10 | The license is an open license that permits revision and redistribution | Yes |

**Worked example: Watershed Basics.** Nine of the ten checks pass. Check 8 fails, because two of the three third-party images carry their own notice and the third has none. That gap is serious, since a reuser cannot tell whether the third image may be copied. The share is 90 percent, in the 9 to 10 band, and a failed check means the score is **9**.

### License Clarity

**License clarity** is how plainly a resource tells a reuser what the license is and what it covers. A clear statement names one specific license, gives its version, links to it, says what it covers, and gives the same answer everywhere the resource appears. A resource is unclear when the page says "CC BY" and the file says "some rights reserved", when a license covers the text and says nothing about the images, or when a resource says "free to use" and names no license. Unclear licensing is a risk for the reuser, because the safe assumption is that no permission was granted.

## Modular Content

**Modular content** is content built from separate, self-contained pieces that can be used alone or together, in the way a set of building blocks can be assembled in different shapes. A modular resource divides its material into sections, quizzes, simulations, figures, and glossaries that each have a clear purpose. Modularity helps learners, because short focused pieces are easier to study and review. It helps teachers more, because a teacher can take the one module she needs and leave the rest. It helps authors, since one module can be revised without touching the others.

**Worked example: one chapter, two designs.** A chapter on watersheds can be built in two ways.

| Feature | Woven design | Modular design |
|---|---|---|
| Structure | One long page that mixes explanation, a quiz, and a simulation | Separate pieces: a reading, a quiz, and a simulation |
| Taking out the quiz | Copy it from the middle of the page and repair the links | Link or embed the quiz's own page |
| Revising the simulation | Edit the whole page and risk breaking the reading | Edit the simulation's folder |
| Reuse by another teacher | Take everything or nothing | Take any piece |

Modularity is a matter of degree. At one end is a single page that mixes everything together. A step up is a page with clear sections, a step further has each part in its own file, and at the far end each part is packaged with its own license and metadata. Each step makes a part easier to take out and reuse, and a reviewer notes how far along the line a resource has gone.

### Standalone Component

A **standalone component** is a piece of a resource that works on its own, without the rest of the resource around it. The test is to *lift it out*. Copy the piece to a new place and ask whether it still makes sense and still works. A reading that begins "as we saw in the last section" fails. A quiz that refers to "the diagram above" fails. A simulation that needs a script from a sibling folder fails. A component passes when everything it needs travels with it, and when a reader who has never seen the rest can use it.

**Worked example: the lift test on Watershed Basics.** The reviewer tries to lift out each of three parts.

| Part | What happens when it is lifted out | Result |
|---|---|---|
| The reading | It begins with a definition and uses only terms it defines | Standalone |
| The quiz | It asks about "the river in section 2", which is not in the quiz page | Not standalone |
| The images | Each has its own file, caption, and alt text | Standalone |

!!! mascot-tip "Lift It Out Before You Score It"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Copy one component into an empty file and read it cold. Whatever confuses you in that empty file will confuse the next teacher who reuses it.

The first MicroSim of the chapter practices the lift test. It shows eight components, and for each one you decide whether it stands alone.

#### Diagram: Standalone Lift Test

<details markdown="1">
<summary>Standalone Lift Test</summary>
Type: microsim
**sim-id:** standalone-lift-test<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of eight components stands alone or depends on the rest of its resource, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Modular Content, Standalone Component (both defined in this chapter above this block).

**Evidence of Mastery:** For each component the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 7 of 8 correct on the first attempt. Reading the lift test is exploration, not evidence.

**Misconceptions:** (1) A component is standalone if it has its own file. (2) A short component is always standalone. (3) A reference to another section is harmless.

**Instructional Rationale:** Judging whether a component stands alone is an Evaluate-level action that applies a stated test. Eight components that differ in one detail each teach the learner to look for hidden dependencies.

**Content:**

The lift test, shown at all times: copy the component to a new place, and check that it makes sense without the rest, and that everything it needs comes with it.

The two bins: Stands alone, and Depends on the rest.

The eight components:

| # | Component shown to the learner | Correct bin | Why (shown as feedback) |
|---|---|---|---|
| 1 | A reading that opens with a definition and uses only terms it defines. | Stands alone | It needs nothing from other sections. |
| 2 | A quiz whose questions say "refer to the diagram in section 2". | Depends on the rest | The diagram is not part of the quiz. |
| 3 | A simulation in its own folder with its own page, instructions, and script. | Stands alone | Everything it needs travels with it. |
| 4 | A figure with its own caption and alt text but a caption that begins "as discussed above". | Depends on the rest | The caption refers to text that is not there. |
| 5 | A glossary page that defines each term in full. | Stands alone | Each definition is complete. |
| 6 | A section that begins "now that you have finished section 3, turn to section 4". | Depends on the rest | It assumes the reader came from section 3. |
| 7 | A worked example that restates the problem, the method, and the answer. | Stands alone | It holds everything needed to follow it. |
| 8 | A simulation page that loads a script from a different chapter's folder. | Depends on the rest | It breaks when moved without that folder. |

**Provenance:** The components are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The test follows the chapter section "Standalone Component".

**Rules:** Each component has exactly one correct bin, four per bin.

**Learner Activity:**

1. The learner sees one component and the two bins.
2. The learner places the component in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After component 8 the sim shows the summary.

**Feedback:** 8 components in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This [bin]. [Why]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can run the lift test." Below 7 it lists the Why text of each missed component.

**Starting State:** The first component, the lift test, and two empty bins. The question shown is "Would this still work if you copied it somewhere new?"

**Chapter Anchors:** The chapter's worked example lifts out the reading, the quiz, and the images from Watershed Basics, and finds that the quiz is not standalone because it refers to the river in section 2.
</details>

### Component Granularity

**Component granularity** is the size of a component: how much one piece contains. A component can be too big, such as a whole textbook when someone needs one idea. It can be too small, such as a single sentence, which is not worth finding or reusing. A useful size is usually one idea or one learning objective with its explanation, an example, and a check question. The right grain also depends on the reuser: a teacher planning a lesson wants a section, and a department building a course wants a unit.

### Cross-Reference Dependence

**Cross-reference dependence** is the way a component relies on other parts of its resource through words like "as shown above" or "see section 4". Each such phrase is a thread that breaks when the component moves. The fix is to restate the idea in one sentence, or to link to the other piece by its own address, so that the reference works wherever the component lands. A reviewer searches a component for phrases such as "above", "below", "earlier", "next section", and "the figure", and checks each one.

### Embeddable Component

An **embeddable component** is a component that can be placed inside another page, either by a link or by an *iframe*, an HTML element that displays one web page inside another. Embedding lets a teacher put your simulation in her course page without copying it, and any improvements you make later reach her page too. For a component to embed, it needs its own web address, it must open with no login, and it must be built so the other site's page does not break it.

An iframe is a short piece of HTML. Before the example, here is what its parts mean. The `src` attribute holds the address of the page to display. The `width` and `height` attributes set its size. The `title` attribute gives the frame a name that a screen reader announces, which the accessibility chapter requires.

```html
<iframe src="https://example.org/sims/runoff/main.html"
        width="100%" height="500"
        title="Runoff simulation"></iframe>
```

**Worked example: testing an embed.** A reviewer wants to know whether the runoff simulation can be embedded. She follows four steps.

1. She opens the simulation's address in a private browser window and confirms that it loads with no login.
2. She pastes the iframe above into a blank test page and opens that page.
3. She checks that the simulation appears, responds to the controls, and fits within the frame.
4. She repeats the test on a second platform, such as a course management system, and records what happened.

The MicroSim below checks your reading of iframe snippets. It shows six snippets of embed code, and for each one you decide whether it is fine or what needs fixing.

#### Diagram: Iframe Snippet Reviewer

<details markdown="1">
<summary>Iframe Snippet Reviewer</summary>
Type: microsim
**sim-id:** iframe-snippet-reviewer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** critique<br/>
**Learning Objective:** The learner will critique six iframe snippets by naming the problem in each or judging it fine, with at least 5 of 6 correct on the first attempt.

**Prerequisites:** Embeddable Component, Standalone Component (both defined in this chapter above this block).

**Evidence of Mastery:** For each snippet the learner chooses one of four verdicts. A choice is correct when it matches the Correct verdict column in Content. Mastery is at least 5 of 6 correct on the first attempt. Reading the attribute list is exploration, not evidence.

**Misconceptions:** (1) A relative address works anywhere. (2) A fixed width is harmless. (3) The title attribute is optional.

**Instructional Rationale:** Critiquing a snippet against a short list of requirements is an Evaluate-level action that a reviewer performs when testing portability. Six snippets, each with at most one defect, isolate the requirements.

**Content:**

The requirements, shown on request: the address must be complete and public; the frame must fit any page; the frame must have a title; the page must open with no login.

The four verdicts: Fine, Fix the address, Make the width flexible, Add a title.

The six snippets (all with example addresses):

| # | Snippet shown to the learner | Correct verdict | Why (shown as feedback) |
|---|---|---|---|
| 1 | iframe with src "https://example.org/sims/runoff/main.html", width "100%", height "500", title "Runoff simulation" | Fine | It has a complete address, a flexible width, and a title. |
| 2 | iframe with src "main.html", width "100%", height "500", title "Runoff simulation" | Fix the address | A relative address points to a file that exists only beside the original page. |
| 3 | iframe with src "https://example.org/sims/runoff/main.html", width "1200", height "500", title "Runoff simulation" | Make the width flexible | A fixed width of 1200 overflows a narrow page. |
| 4 | iframe with src "https://example.org/sims/runoff/main.html", width "100%", height "500" and no title | Add a title | A screen reader cannot name the frame. |
| 5 | iframe with src "https://example.org/sims/pendulum/main.html", width "100%", height "450", title "Pendulum simulation" | Fine | It has a complete address, a flexible width, and a title. |
| 6 | iframe with src "file:///Users/teacher/sims/runoff/main.html", width "100%", height "500", title "Runoff simulation" | Fix the address | The address points to a file on one person's computer, which no one else can open. |

**Provenance:** The snippets are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The requirements follow the chapter section "Embeddable Component". The addresses use the reserved example.org domain.

**Rules:** Each snippet has exactly one correct verdict. Two snippets are Fine, two are Fix the address, one is Make the width flexible, and one is Add a title.

**Learner Activity:**

1. The learner sees one snippet and the four verdicts.
2. The learner may open the requirements. Opening them does not change the score.
3. The learner chooses a verdict, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After snippet 6 the sim shows the summary.

**Feedback:** 6 snippets in a shuffled order, one attempt each. Correct: "Correct: [verdict]. [Why]". Incorrect: "Not quite. The verdict is [verdict]. [Why]". The summary shows "[n] of 6 correct on the first attempt". At 5 or more it adds "You can read embed code." Below 5 it lists the Why text of each missed snippet.

**Starting State:** The first snippet and the four verdicts. The question shown is "What, if anything, needs fixing?"

**Chapter Anchors:** The chapter's iframe example uses the attributes src, width, height, and title, and says a relative address, a fixed width, and a missing title are problems.
</details>

## The Modularity Metric

The **modularity metric** is the seventh metric of the rubric. It asks whether each section, quiz, or simulation stands alone and can be embedded elsewhere. It is scored with ten checks. A failed check is **serious** when it means the resource cannot be taken apart at all, which is checks 1 and 2. When a serious check fails, choose the lower number in a two-number band. Otherwise choose the higher number.

| # | Check | Serious if it fails? |
|---|---|---|
| 1 | The resource is divided into identifiable components | Yes |
| 2 | Each component has its own page, file, or address | Yes |
| 3 | Each component can be understood without reading the rest | No |
| 4 | Each component states the prior knowledge it assumes | No |
| 5 | Components are of useful size, one idea or objective each | No |
| 6 | Each component carries its own license statement and credits | No |
| 7 | Each component carries its own metadata | No |
| 8 | Interactive components embed without edits | No |
| 9 | Components keep working when moved, with no broken relative links | No |
| 10 | Each component is named so that a reuser can tell what it is | No |

**Worked example: Watershed Basics.** The reviewer applies the checks to the reading from Chapter 3.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | The page has a reading, a quiz, and images, each identifiable. |
| 2 | **Fail** | All parts sit in one HTML page, and the quiz has no address of its own. |
| 3 | Pass | The reading stands alone, and the images each have a caption. |
| 4 | **Fail** | No part states what students should know first. |
| 5 | Pass | The reading is one idea of about 2,400 words. |
| 6 | Pass | The footer on the page covers all of its parts. |
| 7 | **Fail** | No component has its own metadata. |
| 8 | **Fail** | The quiz cannot be embedded by itself. |
| 9 | **Fail** | The quiz script uses a relative path that breaks when the quiz is moved. |
| 10 | Pass | Each part has a clear heading or title. |

Five of ten checks pass, a share of 50 percent, in the 5 to 6 band. Check 2 failed and is serious, so the reviewer chooses the lower number, **5**, the score on the Chapter 3 worksheet. That worksheet recorded the main finding, that the quiz cannot be opened apart from the reading.

## The Metadata Metric

The **metadata metric** is the eighth metric of the rubric. It asks whether a resource records its title, author, subject, grade level, license, and description in a standard form, so that others can find it and tell what it is. *Metadata* means data about a resource: it describes the resource and is not part of its content. A library catalog card is metadata about a book. A teacher searching for a resource sees metadata first, and a resource whose metadata is missing may as well not exist, since nothing leads a searcher to it.

**Worked example: three records, one search.** A teacher searches a repository for "watershed grade 6 reading open license". The repository matches the words in each resource's metadata.

| Resource | Its metadata | Does the search find it? |
|---|---|---|
| A | Title "Watershed Basics", subject "Earth science", grade "6 to 7", license "CC BY 4.0", a clear description | Yes, and it ranks high |
| B | Title "Reading 4" and nothing else | No: no field mentions a watershed |
| C | Title "Watershed Basics" and an author, with no subject, grade, or license | Possibly, but the teacher cannot tell the grade or whether she may reuse it |

!!! mascot-thinking "Metadata Is for People and for Machines"
    ![Echo thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A person reads a description to decide whether a resource fits, and a search engine reads the same fields to decide whether to show it. A record that serves only one of them wastes the effort.

## Metadata Record

A **metadata record** is the structured set of fields that describes one resource, with a name and a value for each field. A record is like a catalog card: it has the same slots for every resource, so records can be compared, searched, and sorted. Fields hold short values, such as a title or a license, and a few hold a sentence or two, such as a description. A record can live inside the resource, as tags in a web page, or beside it, as a separate file.

**Worked example: before and after.** The first column shows what *Watershed Basics* records today, and the second shows a complete record. The field names follow Dublin Core, which the next section explains. The date and address are made up.

| Field | Today | Complete record |
|---|---|---|
| Title | Watershed Basics | Watershed Basics |
| Creator | Maria Lopez | Lopez, Maria |
| Subject | Missing | Watersheds; Water cycle; Earth science |
| Description | Missing | A short reading and eight-question quiz that explain what a watershed is and how water moves through one, for grades 6 and 7. |
| Education level | Missing | Grades 6 to 7 |
| Rights | Missing | CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ |
| Date | Shown on the page only | 2025-03-14 |
| Language | Missing | en |
| Identifier | Missing | https://example.org/watershed-basics |
| Type | Missing | Text; InteractiveResource |

## Dublin Core

**Dublin Core** is a standard vocabulary for describing resources, maintained by the Dublin Core Metadata Initiative and published as an international standard. Its core is a set of 15 elements, simple enough that anyone can fill them in, and it is used by library catalogs, repositories, and web publishers. The elements fall into four groups. Some describe the content: title, subject, description, type, and coverage. Some describe who is responsible: creator, contributor, publisher, and rights. Some describe the particular copy: date, format, identifier, and language. And two describe relations to other resources: source and relation. Dublin Core has also grown a larger set of terms, which includes useful ones for education such as *audience* and *education level*.

| Element | What it records |
|---|---|
| Title | The name of the resource |
| Creator | The person or organization mainly responsible |
| Subject | The topic, given as terms or phrases |
| Description | A summary of the content |
| Publisher | The organization that makes it available |
| Contributor | Others who contributed |
| Date | A date in the resource's life, such as when it was created |
| Type | The kind of resource, such as text or interactive resource |
| Format | The file format or medium |
| Identifier | An unambiguous reference, such as a web address |
| Source | A resource from which this one is derived |
| Language | The language of the content |
| Relation | A related resource |
| Coverage | A place or time the content covers |
| Rights | The license or rights statement |

This book's six core fields map onto Dublin Core as the table shows. Dublin Core has no core element for grade level, so the record uses the *education level* term.

| This book's field | Dublin Core element or term |
|---|---|
| Title | Title |
| Author | Creator |
| Subject | Subject |
| Grade level | Education level |
| License | Rights |
| Description | Description |

The MicroSim below practices the mapping. It shows ten pieces of information about a resource, and for each one you choose the Dublin Core element that holds it.

#### Diagram: Dublin Core Matcher

<details markdown="1">
<summary>Dublin Core Matcher</summary>
Type: microsim
**sim-id:** dublin-core-matcher<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Understand<br/>
**Bloom Verb:** classify<br/>
**Learning Objective:** The learner will classify each of ten pieces of information about a resource under the Dublin Core element that holds it, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** The Metadata Metric, Metadata Record, Dublin Core (all defined in this chapter above this block).

**Evidence of Mastery:** For each piece of information the learner commits one of eleven elements. A choice is correct when it matches the Correct element column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the element table is exploration, not evidence.

**Misconceptions:** (1) The author's name belongs in Contributor. (2) The license belongs in Description. (3) The format of a file is its type.

**Instructional Rationale:** Classifying information by field is an Understand-level action that a reviewer performs when reading or writing a record. Ten distinct fields teach the learner what each element is for.

**Content:**

The eleven elements offered: Title, Creator, Subject, Description, Date, Type, Format, Identifier, Source, Language, Rights.

The ten pieces of information:

| # | Information shown to the learner | Correct element | Why (shown as feedback) |
|---|---|---|---|
| 1 | Maria Lopez | Creator | The person mainly responsible for the resource. |
| 2 | https://example.org/watershed-basics | Identifier | An unambiguous reference to the resource. |
| 3 | en | Language | The language of the content. |
| 4 | 2025-03-14 | Date | A date in the resource's life. |
| 5 | CC BY 4.0 with a link to the license | Rights | The license is the rights statement. |
| 6 | A short reading and quiz that explain what a watershed is. | Description | A summary of the content. |
| 7 | Watersheds; Water cycle | Subject | The topics of the resource. |
| 8 | InteractiveResource | Type | The kind of resource. |
| 9 | text/html | Format | The file format or medium. |
| 10 | Adapted from an earlier lesson plan | Source | A resource from which this one is derived. |

**Provenance:** The pieces of information are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The element definitions follow the chapter section "Dublin Core".

**Rules:** Each piece of information has exactly one correct element, and the ten correct elements are all different.

**Learner Activity:**

1. The learner sees one piece of information and the eleven elements.
2. The learner may open the element table. Opening it does not change the score.
3. The learner chooses an element, and the choice is committed.
4. The sim shows whether it was correct and the Why text.
5. After item 10 the sim shows the summary.

**Feedback:** 10 items in a shuffled order, one attempt each. Correct: "Correct: [element]. [Why]". Incorrect: "Not quite. This belongs in [element]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can file information in a record." Below 9 it lists the Why text of each missed item.

**Starting State:** The first item, the eleven elements, and the element table closed. The question shown is "Which Dublin Core element holds this?"

**Chapter Anchors:** The chapter says Dublin Core has 15 core elements, that the rubric's author field is Creator and its license field is Rights, and that grade level uses the education level term.
</details>

## The Six Core Fields

### Title Field

The **title field** records the name of the resource. It is the first thing a searcher sees, so a good title is specific, descriptive, and unique. It tells the searcher the topic and, when it helps, the kind of resource. A title like "Lesson 3" or "Chapter 4" says nothing outside its original context. Titles should also stay stable, because other pages link to a resource by its title and repositories index it that way.

**Worked example: three titles for one resource.**

| Title | Verdict | Why |
|---|---|---|
| Lesson 3 | Poor | It names no topic, and many resources share it. |
| Water | Weak | It names a topic that is too broad to find the resource. |
| Watershed Basics: A Grade 6 Reading and Quiz | Good | It names the topic, the audience, and the kind of resource. |

Keep a resource's title stable once it is published, since links and repository entries use it. If a revised edition appears, change the version or the date in the record and keep the title, so readers can tell the editions apart and still find both. Avoid file names in place of titles, such as "final_v2", and avoid unusual characters that some systems cannot display.

### Author Field

The **author field** records who created the resource, and it is what lets others credit it, as Chapter 2 required. Record the person or the organization responsible, and use a consistent form, such as family name, then given name. Where a resource has several creators, list each. When someone adapts a resource, the record names the original creator and the person who adapted it separately, so that credit travels with the work. An organization can be an author, such as a district or a university department.

**Worked example: who goes in the field?**

| Situation | What to record |
|---|---|
| One teacher wrote the resource | The teacher's name |
| Two teachers wrote it together | Both names, in the order the authors prefer |
| A teacher adapted another author's CC BY lesson | The original author as creator, and the adapter as contributor |
| A district office produced it | The district office as the creator |

Consistency helps credit travel. "Lopez, Maria", "M. Lopez", and "Maria Lopez" look like three different people to a search tool. Many repositories also accept a persistent personal identifier, such as an ORCID iD, a number that belongs to one person for life and ties their works together, though teachers need not have one. Record the author the way the creator wishes to be credited, which may be a pen name or an organization.

### Subject Field

The **subject field** records what the resource is about, as one or more terms. It is the field searchers rely on most, after the title. Good subject terms are specific enough to separate the resource from others and come from a shared list where one exists, so that "runoff" and "run-off" do not fragment the results. A resource may have several subjects, such as a topic and a field: "Watersheds" and "Earth science".

**Worked example: subject terms for Watershed Basics.**

| Terms | Verdict | Why |
|---|---|---|
| Science | Too broad | Thousands of resources share it. |
| Watersheds; Water cycle; Earth science | Good | The terms are specific and standard. |
| stuff about rivers | Poor | It is vague and not a standard term. |

Subject terms and keywords differ. Subject terms describe what the resource is about, often from a shared list, and keywords are the extra words a searcher might type. Two to five subject terms usually serve a resource, enough to place it in its field without padding the list. The ERIC Thesaurus, maintained for education research, is one shared list that education repositories use.

### Grade Level Field

The **grade level field** records the learners a resource is written for, as a grade, a range of grades, an age range, or a level such as college. It is not the same as reading level. Grade level says who the resource is for, and reading level says how hard its text is. A searcher uses grade level to filter, so a consistent scheme matters: "6-7" in one record and "middle school" in another will not group together. Use one scheme across all your records.

**Worked example: three schemes.**

| Scheme | Example value | When it fits |
|---|---|---|
| Grade range | Grades 6 to 7 | Resources for U.S. schools |
| Age range | Ages 11 to 13 | Resources used across countries |
| Level | Introductory college | Higher education |

A resource can serve more than one level, and a record can say so with a range such as grades 6 to 8. Countries label grades differently, so a resource meant for international use should add an age range beside the grade. Grade level also differs from difficulty: a challenging resource for grade 6 and a gentle one for grade 9 may both be correctly labeled. Chapter 6's audience fit asks whether the level matches the text.

### License Field

The **license field** records the resource's license in the metadata, apart from the statement on the page. A good entry names the license and links to its text, so that software can read it. The field must agree with the statement on the page, and a record that says CC BY next to a page that says CC BY-NC invites a dispute. For a resource with parts under different licenses, the field names the license of the resource as a whole and each component carries its own.

**Worked example: three entries.**

| Entry | Verdict | Why |
|---|---|---|
| Free | Poor | It names no license. |
| CC BY | Weak | It names the license and gives no version or link. |
| CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ | Good | It names the license, the version, and the text. |

Repeat the license in the same words wherever it appears, so that a search tool and a person read the same thing. If you change the license when you adapt a resource, update the field at the same time, because an old value left behind is the most common cause of mismatched records.

### Description Field

The **description field** records a short summary of what the resource is, what it covers, and who it is for. It is the field a human reads when deciding whether to open the resource, and search engines also match on its words. A good description runs one to three sentences, uses the words a teacher would type to look for it, and says what the resource contains, such as a reading, a quiz, or a simulation. It is not an advertisement and not a copy of the first paragraph.

**Worked example: three descriptions.**

| Description | Verdict | Why |
|---|---|---|
| An amazing resource everyone will love! | Poor | It says nothing about the content. |
| Watershed. | Weak | It gives a topic and nothing else. |
| A short reading and eight-question quiz that explain what a watershed is and how water moves through one, for grades 6 and 7. | Good | It names the content, the topic, and the audience. |

Search tools often show only the start of a description in their results, so put the most important words first: the topic, the kind of resource, and the audience. Mention what is included, such as a quiz or a simulation, because a teacher choosing among resources wants to know. Avoid claims that the metadata cannot back up, like "complete" or "best".

!!! mascot-tip "Write the Description for the Searcher"
    ![Echo giving a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Imagine the words a busy teacher would type to find your resource, and make sure those words appear in the description. A searcher who types "grade 6 watershed quiz" should land on a description that says exactly that.

The next MicroSim judges field entries. It shows ten entries for the six fields, and for each one you decide whether it is good or needs work.

#### Diagram: Metadata Entry Judge

<details markdown="1">
<summary>Metadata Entry Judge</summary>
Type: microsim
**sim-id:** metadata-entry-judge<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Evaluate<br/>
**Bloom Verb:** judge<br/>
**Learning Objective:** The learner will judge whether each of ten metadata field entries is good or needs work, with at least 9 of 10 correct on the first attempt.

**Prerequisites:** Title Field, Author Field, Subject Field, Grade Level Field, License Field, Description Field (all defined in this chapter above this block).

**Evidence of Mastery:** For each entry the learner commits one of two bins. A placement is correct when it matches the Correct bin column in Content. Mastery is at least 9 of 10 correct on the first attempt. Reading the field guidance is exploration, not evidence.

**Misconceptions:** (1) Any filled field is a good field. (2) A short entry is always weak. (3) A license field only needs the license's short name.

**Instructional Rationale:** Judging an entry against what its field is for is an Evaluate-level action that a reviewer performs when scoring metadata. Ten entries across six fields, half good and half weak, teach the learner what each field needs.

**Content:**

The two bins: Good, and Needs work.

The ten entries:

| # | Field | Entry shown to the learner | Correct bin | Why (shown as feedback) |
|---|---|---|---|---|
| 1 | Title | Lesson 3 | Needs work | It names no topic and many resources share it. |
| 2 | Title | Watershed Basics: A Grade 6 Reading and Quiz | Good | It names the topic, audience, and kind of resource. |
| 3 | Author | Lopez, Maria | Good | It names the person in a consistent form. |
| 4 | Author | the teacher | Needs work | It names no one, so no one can be credited. |
| 5 | Subject | Watersheds; Water cycle; Earth science | Good | The terms are specific and standard. |
| 6 | Subject | Science | Needs work | It is too broad to separate the resource from others. |
| 7 | Grade level | Grades 6 to 7 | Good | It states the audience in one consistent scheme. |
| 8 | License | CC BY | Needs work | It gives no version and no link. |
| 9 | License | CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ | Good | It names the license, version, and text. |
| 10 | Description | An amazing resource everyone will love! | Needs work | It says nothing about the content. |

**Provenance:** The entries are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The guidance follows the chapter sections for each field.

**Rules:** Each entry has exactly one correct bin, five per bin.

**Learner Activity:**

1. The learner sees one field name and entry and the two bins.
2. The learner places the entry in a bin, and the placement is committed.
3. The sim shows whether it was correct and the Why text.
4. After entry 10 the sim shows the summary.

**Feedback:** 10 entries in a shuffled order, one attempt each. Correct: "Correct: [bin]. [Why]". Incorrect: "Not quite. This entry is [bin]. [Why]". The summary shows "[n] of 10 correct on the first attempt". At 9 or more it adds "You can judge a metadata entry." Below 9 it lists the Why text of each missed entry.

**Starting State:** The first entry with its field name and the two bins. The question shown is "Does this entry do its field's job?"

**Chapter Anchors:** The chapter's worked examples of titles, subjects, licenses, and descriptions give the same verdicts: Lesson 3 is poor, Science is too broad, CC BY alone is weak, and the amazing-resource description is poor.
</details>

### Keywords

**Keywords** are words or short phrases that a searcher might use to find a resource, recorded freely, with no fixed list. They supplement the subject field by adding the everyday and alternative terms that a person might type. A resource about runoff might carry the keywords "runoff", "stormwater", and "flooding". Keywords are easy to add and easy to get wrong in two ways: too few leaves the resource hard to find, and too many unrelated ones, a practice called keyword stuffing, makes it appear in searches where it does not belong.

### Controlled Vocabulary

A **controlled vocabulary** is a fixed list of approved terms that everyone describing resources agrees to use, so that the same idea always carries the same label. Where free keywords scatter the same idea across "runoff", "run-off", and "surface water flow", a controlled vocabulary gathers them under one term. The trade-off is effort: an author must learn the list, and a term the list lacks cannot be recorded. Many repositories use one for subjects and for grade levels, and a reviewer notes whether a resource's terms come from a shared list.

### LRMI

**LRMI**, the Learning Resource Metadata Initiative, is a specification that adds educational properties to web metadata. Where Dublin Core describes any resource, LRMI describes what matters in education: the type of learning resource, the educational level, the age range, the educational use, and the standards a resource is aligned to. LRMI is maintained by the Dublin Core Metadata Initiative, and its properties are part of Schema.org, the vocabulary described next. Four of its properties show the idea. The property `learningResourceType` says whether a resource is a lesson, a quiz, or a simulation. The property `typicalAgeRange` gives the ages it suits. The property `educationalAlignment` links it to a standard. And `timeRequired` says how long it takes.

### Schema.org Markup

**Schema.org markup** is a shared vocabulary that web pages use to tell search engines what they contain. Search engines read it to understand a page, and a resource marked up with it can be recognized as a learning resource, with its author, license, and level. The usual form is *JSON-LD*, a block of structured data placed in the page's head. Before the example, here is what its parts do. The `@type` line says what kind of thing the page describes. The other lines give property names, such as `name` and `license`, with their values.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "Watershed Basics",
  "author": { "@type": "Person", "name": "Maria Lopez" },
  "description": "A short reading and eight-question quiz that explain what a watershed is and how water moves through one, for grades 6 and 7.",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "educationalLevel": "Grades 6 to 7",
  "learningResourceType": "reading",
  "inLanguage": "en"
}
</script>
```

!!! mascot-encourage "It Looks Like Code, and You Can Read It"
    ![Echo encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    A block of JSON-LD can look intimidating, and it is only a list of names and values. You already read a form with labels and answers, and the left side of each line is the label. If you can read the record in the table earlier in this chapter, you can read this.

### Machine-Readable Metadata

**Machine-readable metadata** is metadata in a form that software can read and process, as opposed to text that only a person reads. A description written in a paragraph on a web page is for people. The same facts in a JSON-LD block, in tags in the page's head, or in a separate metadata file are for machines. Machine-readable metadata lets a repository harvest records automatically and a search engine filter by license or grade. In this book's convention, a MicroSim's folder can hold a metadata file beside its web page. A reviewer checks that a machine-readable copy exists and that it matches what the page says.

## Metadata Completeness

**Metadata completeness** is how many of a resource's expected metadata fields are filled in with valid values. It is a simple measure: count the fields that are filled and valid, divide by the number of fields expected, and multiply by 100. With the six core fields, a record that has four filled fields has a completeness of about 67 percent. Completeness shows what is missing and says nothing of whether what is there is good. A field filled with "TBD" is present and useless, and a value that does not match the resource is worse than a blank, because it misleads.

**Worked example: the completeness of two records.** The expected fields are the six core fields.

| Field | Watershed Basics today | Watershed Basics, complete record |
|---|---|---|
| Title | Filled | Filled |
| Author | Filled | Filled |
| Subject | Empty | Filled |
| Grade level | Empty | Filled |
| License | Empty | Filled |
| Description | Empty | Filled |
| Fields filled | 2 of 6 | 6 of 6 |
| Completeness | 33% | 100% |

!!! mascot-warning "A Wrong Value Is Worse Than a Blank"
    ![Echo warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Filling a field with "TBD", a guess, or the wrong license makes a record look complete and sends searchers to the wrong place. Leave a field empty until you know the value, and then count it as missing.

The MicroSim below puts the arithmetic into practice. It shows four records, and for each one you compute the completeness.

#### Diagram: Metadata Completeness Calculator

<details markdown="1">
<summary>Metadata Completeness Calculator</summary>
Type: microsim
**sim-id:** metadata-completeness-calculator<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the metadata completeness of each of four records over the six core fields, treating invalid values as empty, with at least 3 of 4 correct on the first attempt.

**Prerequisites:** Metadata Record, Metadata Completeness, Title Field, Author Field, Subject Field, Grade Level Field, License Field, Description Field (all defined in this chapter above this block).

**Evidence of Mastery:** For each record the learner enters the completeness as a whole-number percent, rounded to the nearest whole number. An answer is correct when it equals the Completeness column in Content. Mastery is at least 3 of 4 correct on the first attempt. Reading the formula is exploration, not evidence.

**Misconceptions:** (1) A filled field always counts. (2) Completeness measures quality. (3) A field filled with a placeholder is a partial credit.

**Instructional Rationale:** Calculating a percentage from a count is an Apply-level action, and requiring the learner to judge which values are valid first links the arithmetic to the judgment of entries. Four records with different mixes of empty and invalid fields make both steps necessary.

**Content:**

The formula, shown at all times: completeness = fields filled with a valid value, divided by 6, times 100, rounded to a whole number. A value is invalid when it is a placeholder like "TBD" or "unknown", or when it does not match the resource.

The four records, each over the fields Title, Author, Subject, Grade level, License, Description:

| # | Record | Field values | Valid fields | Completeness |
|---|---|---|---|---|
| 1 | Watershed Basics today | Title and Author filled; the other four empty | 2 | 33% |
| 2 | Draft Record | Title, Author, Subject, Grade level filled; License "TBD"; Description empty | 4 | 67% |
| 3 | Mismatched Record | Title, Author, Subject, Grade level, Description filled; License says CC BY but the page says CC BY-NC | 5 | 83% |
| 4 | Complete Record | All six fields filled with valid values | 6 | 100% |

**Provenance:** The records are illustrative cases written for this chapter, and the sim labels them "illustrative examples". The formula follows the chapter section "Metadata Completeness".

**Rules:** Completeness is (valid fields / 6) x 100, rounded to the nearest whole number. In record 3 the license value does not match the page, so it counts as invalid, which gives 5 valid fields. Each record has exactly one correct answer.

**Learner Activity:**

1. The learner sees a record with its six fields and their values.
2. The learner marks each field as valid or not valid, and counts the valid fields.
3. The learner enters the completeness percent and presses Check.
4. The sim shows the valid fields, the arithmetic, and the correct percent.
5. After record 4 the sim shows the summary.

**Feedback:** 4 records in the fixed order, one attempt each. Correct: "Correct: [percent]. [n] of 6 fields are valid." Incorrect: "Not quite. [n] of 6 fields are valid, which is [percent]. [Why a field was invalid, if one was]". The summary shows "[n] of 4 correct on the first attempt". At 3 or more it adds "You can measure completeness." Below 3 it shows the arithmetic for each missed record.

**Starting State:** Record 1 with its six fields shown and no answer entered. The question shown is "What is this record's completeness?"

**Chapter Anchors:** The chapter says completeness is valid fields divided by fields expected, times 100, that Watershed Basics today has 2 of 6 fields and 33 percent, and that a placeholder or a mismatched value counts as not valid.
</details>

The last illustration of the metadata half shows a record as a card. It has eight numbered markers, one for each part of a good record.

#### Diagram: Anatomy of a Metadata Record

<details markdown="1">
<summary>Anatomy of a Metadata Record</summary>
Type: infographic
**sim-id:** metadata-record-anatomy<br/>
**Library:** html<br/>
**Status:** Specified<br/>
**Bloom Level:** Remember<br/>
**Bloom Verb:** identify<br/>
**Learning Objective:** The learner will identify the eight parts of a metadata record from a description of how each looks, with at least 7 of 8 correct on the first attempt.

**Prerequisites:** Metadata Record, Dublin Core, Keywords, Machine-Readable Metadata, and the six core field sections (all defined in this chapter above this block).

**Evidence of Mastery:** In quiz mode the learner clicks the marker that matches a visual hint. A click is correct when it matches the marker named in the Hint column of Content. Mastery is at least 7 of 8 correct on the first attempt. Hovering in explore mode is exploration, not evidence.

**Misconceptions:** (1) The description repeats the title. (2) The identifier is the file name. (3) Keywords and subject are the same field.

**Instructional Rationale:** Identifying the parts of a record is a Remember-level task, and an illustration of a card gives each field a place. The quiz asks the learner to recognize a field by its look, which is how they will read a real record.

**Content:**

The illustration is a text-free flat drawing of a catalog record card. At the top is a wide bar for a title. Below it, in a column, are seven rows. The first holds a short bar and a small person icon. The second holds a short bar and a small tag icon. The third holds a block of three thin lines. The fourth holds a short bar and a small graduation-cap icon. The fifth holds a short bar and a small scales icon. The sixth holds a row of three small rounded tags. The seventh holds a short bar with a small calendar icon and a long underlined bar. The eight markers:

| # | Label | Hint (describes the look, not the name) | Description | Tip |
|---|---|---|---|---|
| 1 | Title | The wide bar at the top of the card. | The name of the resource, the first thing a searcher sees. | Make it specific and unique. |
| 2 | Creator | The row with a short bar and a small person icon. | The person or organization responsible, the basis for credit. | Use one consistent name form. |
| 3 | Subject | The row with a short bar and a small tag icon. | The topic, as specific terms from a shared list where possible. | Use more than one specific term. |
| 4 | Description | The block of three thin lines. | A short summary of what the resource is and who it is for. | Use the words a searcher would type. |
| 5 | Education level | The row with a short bar and a small graduation-cap icon. | The learners the resource is written for. | Use one scheme across all records. |
| 6 | Rights | The row with a short bar and a small scales icon. | The license, with its version and a link. | It must match the statement on the page. |
| 7 | Keywords | The row of three small rounded tags. | Free words a searcher might use, in addition to the subject. | Add everyday terms, and avoid stuffing. |
| 8 | Date and identifier | The row with a small calendar icon and a long underlined bar. | When the resource was made or updated, and its permanent address. | Use an address that will not change. |

**Provenance:** The parts follow the chapter sections "Metadata Record", "Dublin Core", "The Six Core Fields", and "Keywords". The illustration is synthetic, and the sim labels the card "illustrative example".

**Rules:** Each hint matches exactly one marker. The illustration contains no text, so every label comes from the table above. Markers are numbered 1 to 8 in the order of the table.

**Learner Activity:**

1. In explore mode the learner hovers or clicks a marker and reads its label, description, and tip.
2. In quiz mode the sim shows a hint.
3. The learner clicks the marker they think the hint describes.
4. If the first click is wrong, the sim says so and lets the learner try once more. If the second click is also wrong, the sim reveals the marker and its description.
5. After all 8 hints the sim shows the summary.

**Feedback:** 8 hints in a shuffled order, two attempts each. Only a correct first click counts as evidence. Correct: "Correct: [label]. [Description]". First wrong click: "Not quite. Look again at the hint: [hint]". Second wrong click: "This is [label]. [Description]". The summary shows "[n] of 8 correct on the first attempt". At 7 or more it adds "You can read a metadata record." Below 7 it lists the labels of the missed parts.

**Starting State:** The illustration with eight numbered markers, explore mode active, and the prompt "Hover a marker to see what it is."

**Chapter Anchors:** The chapter's complete record for Watershed Basics has the fields title, creator, subject, description, education level, rights, date, language, identifier, and type, and its six core fields are title, author, subject, grade level, license, and description.
</details>

## Scoring the Three Reusability Metrics

The open license and modularity checks appear earlier in this chapter. The metadata metric has its own ten checks, and a failed check is **serious** when the resource cannot be identified at all, which is the case when the title or the author is missing. When a serious check fails, choose the lower number in a two-number band. Otherwise choose the higher number.

| # | Check | Serious if it fails? |
|---|---|---|
| 1 | A title is recorded | Yes |
| 2 | An author or creator is recorded | Yes |
| 3 | A subject is recorded | No |
| 4 | A grade level or audience is recorded | No |
| 5 | The license is recorded in the metadata, and matches the page | No |
| 6 | A description is recorded | No |
| 7 | Keywords or controlled subject terms are included | No |
| 8 | A date and a permanent address are recorded | No |
| 9 | The metadata is in a machine-readable form | No |
| 10 | The record is complete and accurate, with no placeholders | No |

**Worked example: Watershed Basics.** The reviewer applies the checks to the reading from Chapter 3.

| # | Result | Evidence |
|---|---|---|
| 1 | Pass | The title is in the page's head. |
| 2 | Pass | The author is named in a tag in the page's head. |
| 3 | **Fail** | No subject is recorded. |
| 4 | **Fail** | No grade level is recorded in the metadata. |
| 5 | **Fail** | The file properties carry no license. |
| 6 | **Fail** | No description is recorded. |
| 7 | **Fail** | No keywords are recorded. |
| 8 | Pass | A publication date and the page address are present. |
| 9 | Pass | The title and author are in tags in the page's head that software can read. |
| 10 | **Fail** | Four of six core fields are empty, so the record is not complete. |

Four of ten checks pass, a share of 40 percent, in the 3 to 4 band. Neither serious check failed, because the title and the author are present, so the reviewer chooses the higher number, **4**, the score on the Chapter 3 worksheet. Completeness is 2 of 6 core fields, or 33 percent, and the metric's checks reach further than the six fields.

The last MicroSim of the chapter is a scoring practice for all three metrics. It shows nine cases, three for each metric, and for each one you choose the metric score.

#### Diagram: Reusability Metrics Scorer

<details markdown="1">
<summary>Reusability Metrics Scorer</summary>
Type: microsim
**sim-id:** reusability-metrics-scorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** apply<br/>
**Learning Objective:** The learner will apply the ten open license checks, the ten modularity checks, and the ten metadata checks, with the Chapter 3 scoring rules, to choose the metric score for each of nine cases, with at least 8 of 9 scores exactly correct on the first attempt.

**Prerequisites:** The Open License Metric, The Modularity Metric, The Metadata Metric, Metric Score, Scoring Descriptor (all defined in this chapter or in Chapter 3 above this block).

**Evidence of Mastery:** For each case the learner chooses a whole-number score from 0 to 10 after seeing the ten check results. A score is correct when it equals the Correct score column in Content. Mastery is at least 8 of 9 scores correct on the first attempt. Opening the check lists and the descriptor table is exploration, not evidence.

**Misconceptions:** (1) The three metrics use different scoring rules. (2) A serious failure always drops a full band. (3) Full completeness of the six fields earns a 10.

**Instructional Rationale:** Applying a scoring procedure to new cases is an Apply-level task. Nine cases across three check lists make the learner run the same procedure on different lists, with different serious checks.

**Content:**

The three ten-check lists are those in the chapter sections "The Open License Metric", "The Modularity Metric", and "Scoring the Three Reusability Metrics", each marked serious or not. The descriptor bands applied to the share of checks passed: 0% is 0; 1% to 24% is 1 to 2; 25% to 49% is 3 to 4; 50% to 74% is 5 to 6; 75% to 89% is 7 to 8; 90% to 100% is 9 to 10. Within a two-number band, choose the lower number when a serious check failed and the higher number otherwise. A score of 10 requires every check to pass.

The nine cases:

| # | Metric | Resource | Checks failed | Checks passed | Share | Band | Serious failure? | Correct score | Why (shown as feedback) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Open license | Open Algebra | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed. |
| 2 | Open license | Watershed Basics | 8 | 9 | 90% | 9 to 10 | Yes, check 8 | 9 | A failed check means the score is 9, and the failure is serious. |
| 3 | Open license | Mixed Rights Packet | 2, 3, 6, 8, 9 | 5 (checks 1, 4, 5, 7, 10) | 50% | 5 to 6 | Yes, check 8 | 5 | A serious failure puts the score at the lower number. |
| 4 | Modularity | Open Algebra | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed. |
| 5 | Modularity | Watershed Basics | 2, 4, 7, 8, 9 | 5 | 50% | 5 to 6 | Yes, check 2 | 5 | Components with no address of their own is serious, so the lower number applies. |
| 6 | Modularity | Single Long Page | 1, 2, 3, 5, 8, 9, 10 | 3 (checks 4, 6, 7) | 30% | 3 to 4 | Yes, checks 1 and 2 | 3 | The page cannot be taken apart, which is serious, so the lower number applies. |
| 7 | Metadata | Open Algebra | None | 10 | 100% | 9 to 10 | No | 10 | Every check passed. |
| 8 | Metadata | Watershed Basics | 3, 4, 5, 6, 7, 10 | 4 | 40% | 3 to 4 | No | 4 | The title and author are present, so no serious check failed and the higher number applies. |
| 9 | Metadata | Untitled Files | 1, 2, 3, 4, 5, 6, 7, 9, 10 | 1 (check 8) | 10% | 1 to 2 | Yes, checks 1 and 2 | 1 | The files have no title or author, which is serious, so the lower number applies. |

**Provenance:** The ten-check lists and the bands follow this chapter and Chapter 3. The nine cases are illustrative cases written for this chapter, and the sim labels them "illustrative examples". Cases 2, 5, and 8 are the chapter's worked examples.

**Rules:** A score is the band chosen from the share passed, and then the number chosen within the band by the serious-failure rule. A band of 9 to 10 gives 10 only when every check passes. Each case has exactly one correct score.

**Learner Activity:**

1. The sim shows case 1 with its ten check results and the name of the metric.
2. The learner may open the check list and the descriptor table.
3. The learner chooses a score from 0 to 10, and the choice is committed.
4. The sim shows the count of passes, the band, whether a serious check failed, and the correct score with the Why text.
5. After case 9 the sim shows the summary.

**Feedback:** 9 cases in the fixed order, one attempt each. Correct: "Correct: [score]. [Why]". Incorrect: "Not quite. [passes] checks passed, which is [share] and the [band] band. [Why]". The summary shows "[n] of 9 correct on the first attempt". At 8 or more it adds "You can score all three reusability metrics." Below 8 it lists the Why text of each missed case.

**Starting State:** Case 1 with all ten results shown and no score chosen. The question shown is "What open license score does this resource earn?"

**Chapter Anchors:** The chapter's worked examples score Watershed Basics 9 on open license, 5 on modularity, and 4 on metadata, each with the failed checks named in the chapter.
</details>

## Key Takeaways

- The **open license metric** asks for a clear open license on every component. **License clarity** means one specific license, a version, a link, and a scope, stated the same way everywhere.
- **Modular content** is built from separate pieces. A **standalone component** passes the lift test, **cross-reference dependence** breaks it, **component granularity** sets the useful size, and an **embeddable component** can sit inside another page. The **modularity metric** scores all of this.
- The **metadata metric** asks whether the resource can be found and identified. A **metadata record** holds the fields, **Dublin Core** names them, and the six core fields are the **title field**, **author field**, **subject field**, **grade level field**, **license field**, and **description field**.
- **Keywords** and a **controlled vocabulary** help search. **LRMI** and **Schema.org markup** carry educational metadata in a form search engines read, and **machine-readable metadata** lets software do the reading.
- **Metadata completeness** counts valid fields. It does not measure quality, and a wrong value is worse than a blank.

!!! mascot-celebration "You Can Check Whether It Can Be Found and Reused"
    ![Echo celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now score a resource's license, test whether its parts stand alone, read and write a metadata record, and score all three reusability metrics with evidence. A resource that can be found, understood, and lifted out is a resource that other teachers can actually use.

[See Annotated References](./references.md)
