# Quiz: Reusable Components and Publishing OER

Test your understanding of packaging, learning graphs, publishing with MkDocs and GitHub Pages, maintenance, reuse tracking, and impact reporting with these review questions.

---

#### 1. Besides its content and any images or scripts, which files does a packaged reusable component contain?

<div class="upper-alpha" markdown>
1. A README, a license file, and a metadata file
2. A grade book, a rubric, and an answer key
3. A change log, a class roster, and a consent letter
4. A build script, a database, and a login page
</div>

??? question "Show Answer"
    The correct answer is **A**. Component packaging gathers everything a component needs into one folder that can be copied, downloaded, or embedded as a unit. The README says what the component is, how to embed it, and how to credit it. The license file states the terms, and the metadata file holds the record from Chapter 9 in a form a program can read. All links inside the package should be complete addresses or point to files inside it.

    **Concept Tested:** Component Packaging

    **See:** [Component Packaging](index.md#component-packaging)

---

#### 2. What does the command `mkdocs build --strict` do?

<div class="upper-alpha" markdown>
1. It builds the site and pushes the finished pages to the branch that GitHub Pages serves
2. It deploys the site without building it first, so broken links go unnoticed
3. It builds the site and stops with an error on a broken link or a page missing from the menu
4. It deletes every page that is not listed in the menu, which removes unlinked files
</div>

??? question "Show Answer"
    The correct answer is **C**. MkDocs is a static site generator that reads Markdown files and a settings file called mkdocs.yml and writes a complete website. The strict option turns a broken internal link into an error, which matters because a published resource with a broken link would fail the accuracy and portability checks the rubric applies to everyone else's resources. Option A describes `mkdocs gh-deploy`. Run the strict build first and deploy only when it passes.

    **Concept Tested:** MkDocs

    **See:** [MkDocs](index.md#mkdocs)

---

#### 3. In this book's learning graph, an arrow runs from Score Gain to Re-Scoring. How should the arrow be read?

<div class="upper-alpha" markdown>
1. Re-Scoring needs Score Gain, so Score Gain should be learned first
2. Score Gain needs Re-Scoring, so Re-Scoring should be learned first
3. Score Gain and Re-Scoring are two names for the same concept
4. Score Gain is optional, and Re-Scoring is required
</div>

??? question "Show Answer"
    The correct answer is **B**. A concept dependency is a link saying one concept needs another first, and in this book's graph each arrow points from the concept to the concept it depends on, so the arrow reads "needs." Learn the concept at the arrow's tip first. A valid graph has no loops: if A needs B and B needs A, neither could be learned first. A chapter structure then puts every prerequisite in the same chapter or an earlier one.

    **Concept Tested:** Concept Dependency

    **See:** [Concept Dependency](index.md#concept-dependency)

---

#### 4. Why does a listing in an OER clearinghouse not replace the resource's own repository and site?

<div class="upper-alpha" markdown>
1. Clearinghouses reject resources that carry open licenses, so a listing is not possible
2. A listing stores a frozen copy of the resource that can never be updated later
3. Clearinghouses require every visitor to log in before they can view a listing
4. A listing only points to the resource, so the repository and site stay the source of truth
</div>

??? question "Show Answer"
    The correct answer is **D**. An OER clearinghouse, such as OER Commons or MERLOT, is a catalog that lists open resources from many sources and links to each so that teachers can search in one place. A listing makes a resource more discoverable and does not move it. The catalog searches the subject, grade level, and description you supply, so good metadata is what makes a listing useful. List the resource last, once everything else is ready.

    **Concept Tested:** OER Clearinghouse

    **See:** [OER Clearinghouse](index.md#oer-clearinghouse)

---

#### 5. For one release of Watershed Basics, the author removes an outdated 2019 rainfall chart, adds a glossary entry for "aquifer," corrects a quiz script path so the quiz loads on tablets, and updates the river length from 410 to 398 miles. Under which headings do these four changes go, in that order?

<div class="upper-alpha" markdown>
1. Added, Removed, Changed, Fixed
2. Removed, Changed, Added, Fixed
3. Removed, Added, Fixed, Changed
4. Changed, Added, Fixed, Removed
</div>

??? question "Show Answer"
    The correct answer is **C**. Release notes group changes under four headings. Added covers something new, such as the glossary entry. Changed covers something that existed and now reads differently, such as the updated river length. Fixed covers a corrected defect, such as the broken script path. Removed covers something taken out, such as the outdated chart. The change log entries are the raw material, and the release notes are the condensed version for readers who will not read every entry.

    **Concept Tested:** Release Notes

    **See:** [Release Notes](index.md#release-notes)

---

#### 6. A reader writes, "Please remove the credit line; it looks cluttered." How should the maintainer respond?

<div class="upper-alpha" markdown>
1. Fix it in the next patch, because a cluttered page counts as a defect
2. Schedule it for a later release, together with other requests about the page design
3. Decline politely, because the license requires credit to be given to the creator
4. Answer and close by pointing to the README, which already explains the credit line
</div>

??? question "Show Answer"
    The correct answer is **C**. Issue tracking records every report with a status so that each is decided. A request that conflicts with the license, the purpose, or the evidence is declined politely. CC BY 4.0 requires credit to the creator, so the maintainer cannot remove the line. Defects that harm accuracy, access, or function are fixed soon, worthwhile improvements are scheduled, and questions the documentation already answers are answered and closed.

    **Concept Tested:** Issue Tracking

    **See:** [Issue Tracking](index.md#issue-tracking)

---

#### 7. A contributor proposes changing "about 6,000 square miles" to "more than 6,000 square miles" and gives no source. What should the maintainer do?

<div class="upper-alpha" markdown>
1. Accept it, because it is a very small change that most readers will not notice
2. Decline it permanently, because contributors may not change figures
3. Accept it and thank the contributor in the release notes for the careful correction
4. Ask for changes first, because the edit alters the meaning and needs a source
</div>

??? question "Show Answer"
    The correct answer is **D**. A community contribution gets the same review as the author's own changes. The review checks that the meaning is kept or the change is a labeled correction, that the license is compatible, that third-party material is credited, and that no personal data is collected. Changing "about" to "more than" is a changed quantity, so it needs a source before it is accepted. Decline is for contributions that cannot be fixed, such as one that collects student names.

    **Concept Tested:** Community Contribution

    **See:** [Community Contribution](index.md#community-contribution)

---

#### 8. Page views for all three components of a resource fall sharply in December and January. Which analysis is best?

<div class="upper-alpha" markdown>
1. The pattern fits the school calendar, since holidays cut visits to every component
2. The drop shows that students stopped learning from the resource over the holidays
3. The drop shows that the simulation is the weakest component, because it fell the furthest
4. The drop proves that a link is broken on every page of the library, so all readers are blocked
</div>

??? question "Show Answer"
    The correct answer is **A**. Usage analytics show reach and patterns, and they mislead easily. A page view is not a reader, a reader is not a learner, and a dip in the holidays reflects the calendar. All three components fell together, so a flaw in one component is unlikely to explain it. Always read the counts alongside the calendar and next to the learning evidence from the A/B test, and choose a tool that records counts and not individuals.

    **Concept Tested:** Usage Analytics

    **See:** [Usage Analytics](index.md#usage-analytics)

---

#### 9. An author's report lists 300 downloads from a clearinghouse, 1,200 page views, three repository stars, and one teacher's course page that embeds the simulation and credits the author. Which analysis of the reuse evidence is correct?

<div class="upper-alpha" markdown>
1. All four signals are equally strong evidence of reuse, because each involves a reader
2. Only the embedded course page is strong evidence of reuse; downloads, views, and stars show interest
3. The downloads are the strongest evidence, because they are the largest number
4. None of the four signals is evidence of reuse, because every one of them can be faked
</div>

??? question "Show Answer"
    The correct answer is **B**. Strong signals show someone using the resource: a course page that links to or embeds a component and credits you, a copy of your repository with changes, and a message from a teacher describing use. Downloads, page views, and stars are weak evidence, because they show interest and not use. Your own visits and automated crawlers are not evidence at all. Search for your title and your attribution line, since a reuser who followed the license will have written them.

    **Concept Tested:** Reuse Tracking

    **See:** [Reuse Tracking](index.md#reuse-tracking)

---

#### 10. A draft impact report says, "The library had 3,500 page views in six months, so students learned more from it." What is the best judgment of this sentence?

<div class="upper-alpha" markdown>
1. It is sound, because page views indicate learning and 3,500 views is a large number for a small resource
2. It is sound, because a count of 3,500 views is large enough to show that students learned from it
3. It is flawed only because it should give the number of downloads in place of the views
4. It claims learning from page views, but views show reach, and learning evidence comes from the A/B test
</div>

??? question "Show Answer"
    The correct answer is **D**. Impact reporting draws on four kinds of evidence: reach from usage analytics, reuse from reuse tracking, learning from the A/B test of Chapters 16 and 17, and experience from surveys, comments, and the issue list. A good report keeps the kinds apart, says how strong each is, and claims no more than the evidence shows. For Watershed Basics, the learning claim rests on a 22.0 versus 15.0 gain in a pilot of 24 students, with its limits stated.

    **Concept Tested:** Impact Reporting

    **See:** [Impact Reporting](index.md#impact-reporting)
