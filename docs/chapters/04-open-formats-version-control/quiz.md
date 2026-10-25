# Quiz: Open File Formats and Version Control

Test your understanding of the editable source metric, open file formats, Markdown, and version control with Git and GitHub with these review questions.

---

#### 1. What is a fork of a repository?

<div class="upper-alpha" markdown>
1. A separate line of work inside the same repository that leaves the main line undisturbed
2. Your own independent copy of someone else's repository, which keeps a link back to the source
3. A proposal to merge changes from one copy of a repository into another copy, for the maintainer to review
4. A saved snapshot of changes, with an author, a date, and a message that says what was done
</div>

??? question "Show Answer"
    The correct answer is **B**. A fork is your own independent copy of someone else's repository, made on the same site. You can change it freely without affecting the original, and it keeps a link back to the source. Forking is the repository version of the revise and remix permissions: the open license gives you the right to change a resource, and the fork gives you the place to do it. Option A describes a branch, C a pull request, and D a commit.

    **Concept Tested:** Fork

    **See:** [Fork](index.md#fork)

---

#### 2. Which set of tests identifies an open file format?

<div class="upper-alpha" markdown>
1. The specification is published, anyone can implement it without paying, and free software opens it
2. The file is free to download, widely used, and created by a nonprofit organization
3. The file prints well, looks the same on every device, and is saved as a PDF by a design program
4. The file is plain text, is under one megabyte, and contains no images or any other media
</div>

??? question "Show Answer"
    The correct answer is **A**. Three questions test a format: is the specification published, can anyone implement it without paying a fee or asking permission, and does free software exist that opens it? A format that passes all three stays readable when a company changes its products or closes. Price, popularity, printing quality, and file size say nothing about openness. A file can also be an open standard and still be a poor source for editing, as the PDF shows.

    **Concept Tested:** Open File Format

    **See:** [Open File Format](index.md#open-file-format)

---

#### 3. Why is a resource that offers only a PDF a poor choice for a teacher who wants to revise it?

<div class="upper-alpha" markdown>
1. A PDF is a closed format that no free software can open, so it cannot be edited or even read at all
2. A PDF cannot carry an open license, so revision is not permitted even if the owner agrees
3. A PDF records how pages look, not how content is built, so a change means rebuilding the structure
4. A PDF is too large to download without creating a login, which blocks every revision attempt
</div>

??? question "Show Answer"
    The correct answer is **C**. A PDF is an open international standard and free software opens it, so option A is wrong. The problem is structure: a PDF records the appearance of each page, so changing a sentence means copying text out of the page, losing headings and tables, and rebuilding the layout. A license can be attached to a PDF, so the right to revise may exist even though the practical means do not. Ask the author for the source file.

    **Concept Tested:** PDF-Only Distribution

    **See:** [PDF-Only Distribution](index.md#pdf-only-distribution)

---

#### 4. What is the difference between a source format and a delivery format?

<div class="upper-alpha" markdown>
1. A source format is always an open standard that free tools can read, while a delivery format is always a closed one
2. A source format is meant for readers who study the content, while a delivery format is meant for authors who write it
3. A source format keeps the structure so the content can be changed, while a delivery format is for reading or printing
4. A source format is stored on GitHub in a repository, while a delivery format is stored on a school website
</div>

??? question "Show Answer"
    The correct answer is **C**. The chapter compares a source to a recipe and a delivery file to a cake. You can change an ingredient in the recipe and bake again, but you cannot take the sugar out of the cake. A source format such as Markdown, HTML, or a word processing file keeps headings, lists, and links. A delivery format such as a PDF or a scan often keeps only the appearance. Where a file is stored (D) does not decide which kind it is.

    **Concept Tested:** Source Format

    **See:** [Source Format](index.md#source-format)

---

#### 5. Why does version control help when several teachers improve the same open resource?

<div class="upper-alpha" markdown>
1. It stops anyone except the original author from changing the files, so no edits can conflict
2. It stores each person's edits in a separate copy that is never combined with the other copies
3. It converts every file to a PDF, so that all of the changes look the same to every reader
4. It records every change with an author, date, and message, combines edits, and can restore any earlier version
</div>

??? question "Show Answer"
    The correct answer is **D**. Version control replaces a folder of confusing copies such as lesson_final2.docx with one set of files and a recorded history. A reviser can see exactly what changed, a mistake can be undone by returning to an earlier state, and several people can work at once and combine their changes. A reuser can also judge a resource's health from the date of its last change. Open resources depend on this, because anyone may revise them.

    **Concept Tested:** Version Control

    **See:** [Version Control](index.md#version-control)

---

#### 6. A reviewer applies the ten editable source checks to a district unit. Check 3 (the source holds all of the content) and check 7 (a note explains how the pieces fit) fail, and the other eight pass. What score does the chapter's rule give?

<div class="upper-alpha" markdown>
1. 7, because 80 percent falls in the 7 to 8 band and the missing content blocks revision
2. 8, because 80 percent falls in the 7 to 8 band and the higher number is always used
3. 6, because each failed check lowers a score of 10 by two points
4. 5, because a failed check that blocks revision caps the score at 5
</div>

??? question "Show Answer"
    The correct answer is **A**. Eight of ten checks pass, a share of 80 percent, which falls in the 7 to 8 band. Check 3 blocks revision when it fails, because a reviser cannot change content that is missing from the source. When a failed check blocks revision, choose the lower number in the band, so the score is 7. The higher number (B) is correct only when no failed check blocks revision, as with the image and change-record failures in the chapter's Watershed Basics example.

    **Concept Tested:** Editable Source Metric

    **See:** [Scoring the Editable Source Metric](index.md#scoring-the-editable-source-metric)

---

#### 7. Which line of Markdown shows an image whose alt text is "A river flowing through a valley"?

<div class="upper-alpha" markdown>
1. `[A river flowing through a valley](https://example.org/images/river.png)`
2. `![A river flowing through a valley](https://example.org/images/river.png)`
3. `![https://example.org/images/river.png](A river flowing through a valley)`
4. `## A river flowing through a valley`
</div>

??? question "Show Answer"
    The correct answer is **B**. An image uses the same pattern as a link, with an exclamation mark in front: square brackets hold the alt text, and parentheses hold the address. Option A has no exclamation mark, so it creates a link and not an image. Option C swaps the alt text and the address. Option D creates a level-2 heading. Alt text is the description that a screen reader speaks, so a reviser should never leave the brackets empty.

    **Concept Tested:** Markdown

    **See:** [Markdown](index.md#markdown)

---

#### 8. A teacher finds a typo in an open lesson on GitHub and wants every teacher who uses the lesson to benefit from the fix. Which sequence should she follow?

<div class="upper-alpha" markdown>
1. Edit the original repository directly, then fork it to record the change
2. Fork the repository, fix the typo in her copy, then open a pull request to the original
3. Open a pull request first, then fork the repository and make the change
4. Fork the repository, fix the typo, and keep it in her fork, because pull requests are only for large changes
</div>

??? question "Show Answer"
    The correct answer is **B**. She forks the repository to make her own copy, makes the change in the fork, and then opens a pull request that proposes the change to the original. The maintainer reads it, comments, and may merge it. A pull request is how a small fix, such as a typo or missing alt text, travels to every teacher who uses the resource. A pull request needs a change to propose, so it cannot come first (C).

    **Concept Tested:** Pull Request

    **See:** [Pull Request](index.md#pull-request)

---

#### 9. A reviewer opens a repository and finds a README, a LICENSE file stating CC BY 4.0, and Markdown source files. The latest commit is four years old, and several open issues report errors that nobody has answered. What does this evidence most strongly suggest?

<div class="upper-alpha" markdown>
1. The resource is high quality, because it uses open formats and an open license and has a README
2. The resource has no editable source, because its commits are old and the files are therefore locked
3. The license is invalid, because the repository is no longer active and the owner has not replied
4. The resource has an open license and editable source but may be unmaintained, so accuracy and currency need checking
</div>

??? question "Show Answer"
    The correct answer is **D**. The license file and Markdown files are good evidence for the open license and editable source metrics. A last commit that is years old suggests the resource is no longer maintained, and unanswered issues that report errors point to problems in accuracy and currency. Open formats say nothing about quality (A), and the age of the commits does not remove the source files (B) or invalidate the license (C). Evidence from a repository can be checked and cited.

    **Concept Tested:** GitHub Repository

    **See:** [GitHub Repository](index.md#github-repository)

---

#### 10. A reviewer's editable source checks fail for four different resources. Which failed check would block a reviser from changing the content and so pull the score to the lower number in its band?

<div class="upper-alpha" markdown>
1. The images are PNG files, and no original or vector source files are offered for them
2. No short note explains how the pieces of the resource fit together or what each file does
3. The source file leaves out part of the content, such as tables and equations
4. No record of changes is available, such as a changelog or a list of past versions
</div>

??? question "Show Answer"
    The correct answer is **C**. A failed check blocks revision when a reviser cannot change the content without it. If the source omits tables or equations, those parts cannot be edited at all. A reviser can still change every word and replace any picture without the original image files (A), and a missing note (B) or change record (D) makes the work harder but does not stop it. The chapter marks checks 5, 7, and 8 as non-blocking.

    **Concept Tested:** Editable Source Metric

    **See:** [The Editable Source Metric](index.md#the-editable-source-metric)
