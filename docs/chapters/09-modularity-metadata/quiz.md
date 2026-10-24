# Quiz: Modularity and Metadata

Test your understanding of license clarity, standalone components, Dublin Core, the six core metadata fields, and metadata completeness with these review questions.

---

#### 1. What does a reviewer do in the lift test for a standalone component?

<div class="upper-alpha" markdown>
1. Counts how many pages the component spans in the original resource and compares it with others
2. Copies the component to a new place and checks that it still works there with everything it needs
3. Asks the author whether the component was intended to stand alone, and accepts the answer
4. Runs an automated accessibility checker on the component and records the number of errors
</div>

??? question "Show Answer"
    The correct answer is **B**. A standalone component works on its own, without the rest of the resource around it. The test is to lift it out: copy the piece into an empty file and read it cold. A reading that begins "as we saw in the last section" fails, a quiz that refers to "the diagram above" fails, and a simulation that needs a script from a sibling folder fails. A component passes when everything it needs travels with it.

    **Concept Tested:** Standalone Component

    **See:** [Standalone Component](index.md#standalone-component)

---

#### 2. In Dublin Core, which element holds a resource's license or rights statement?

<div class="upper-alpha" markdown>
1. Source
2. Relation
3. Description
4. Rights
</div>

??? question "Show Answer"
    The correct answer is **D**. Dublin Core is a standard vocabulary of 15 core elements. The Rights element records the license or rights statement, which is why this book's license field maps to it. Author maps to Creator, and grade level uses the education level term because Dublin Core has no core element for it. Source (A) records a resource from which this one is derived, and Relation (B) records a related resource.

    **Concept Tested:** Dublin Core

    **See:** [Dublin Core](index.md#dublin-core)

---

#### 3. Why does the chapter say that a wrong value in a metadata field is worse than a blank field?

<div class="upper-alpha" markdown>
1. Blank fields are scored as valid, while wrong values are scored as invalid
2. A blank field lets a search tool fill in the correct value automatically
3. A wrong value makes a record look complete and sends searchers to the wrong place
4. A wrong value always makes the resource fail the open license metric
</div>

??? question "Show Answer"
    The correct answer is **C**. Metadata completeness counts fields filled with valid values. A placeholder such as "TBD", a guess, or a license that does not match the page counts as invalid, so the record looks complete when it is not. It also misleads: a record that says CC BY next to a page that says CC BY-NC invites a dispute. Leave a field empty until you know the value, and then count it as missing.

    **Concept Tested:** Metadata Completeness

    **See:** [Metadata Completeness](index.md#metadata-completeness)

---

#### 4. How do subject terms differ from keywords in a metadata record?

<div class="upper-alpha" markdown>
1. Subject terms are written for machines to read, while keywords are written only for people
2. Subject terms describe what the resource is about, often from a shared list, while keywords are free extra words
3. Subject terms are free text with no rules at all, while keywords must come from a fixed list
4. Subject terms record the grade level of the resource, while keywords record only its topic
</div>

??? question "Show Answer"
    The correct answer is **B**. Subject terms describe the topic, ideally from a shared list such as the ERIC Thesaurus, and two to five usually serve a resource. Keywords supplement them with everyday and alternative terms, such as "stormwater" beside "runoff." Too few keywords make a resource hard to find, and too many unrelated ones, called keyword stuffing, make it appear in searches where it does not belong. A controlled vocabulary gathers variants under one term.

    **Concept Tested:** Keywords

    **See:** [Keywords](index.md#keywords)

---

#### 5. Why do phrases such as "as shown above" and "see section 4" reduce a component's modularity?

<div class="upper-alpha" markdown>
1. Each phrase is a thread that breaks when the component is moved to a new place
2. Each phrase makes the component too long to embed in another page
3. The Dublin Core standard does not allow such phrases in a resource
4. Each phrase prevents the component from carrying its own license
</div>

??? question "Show Answer"
    The correct answer is **A**. Cross-reference dependence is the way a component relies on other parts of its resource. When the component moves, "above" points at nothing. The fix is to restate the idea in one sentence, or to link to the other piece by its own address, so the reference works wherever the component lands. A reviewer searches for words such as "above," "below," "earlier," "next section," and "the figure" and checks each one.

    **Concept Tested:** Cross-Reference Dependence

    **See:** [Cross-Reference Dependence](index.md#cross-reference-dependence)

---

#### 6. A teacher embeds a simulation with an iframe whose `src` is just `main.html`. What is wrong, and what is the fix?

<div class="upper-alpha" markdown>
1. The width is fixed at a number of pixels, so it should be changed to 100 percent
2. The frame has no title, so a title attribute should be added for screen reader users
3. The simulation needs a login, so the iframe should be removed from the course page
4. A relative address points to a file that exists only beside the original page, so use a complete public address
</div>

??? question "Show Answer"
    The correct answer is **D**. For a component to embed, it needs its own complete address, it must open with no login, and the frame must fit any page. A relative address such as main.html works only where that file sits next to the page. Replace it with a full address such as https://example.org/sims/runoff/main.html. The snippet gives no information about the width (A), the title (B), or a login (C), so the address is the clear defect.

    **Concept Tested:** Embeddable Component

    **See:** [Embeddable Component](index.md#embeddable-component)

---

#### 7. A metadata record has valid Title, Author, Subject, and Grade level fields, a License value of "TBD," and an empty Description. Using the six core fields, what is its metadata completeness?

<div class="upper-alpha" markdown>
1. 67 percent
2. 83 percent
3. 100 percent
4. 50 percent
</div>

??? question "Show Answer"
    The correct answer is **A**. Completeness is the number of fields filled with a valid value, divided by the number of fields expected, times 100. Only four fields are valid, because a placeholder such as "TBD" counts as invalid and the Description is empty. Four divided by six is about 0.67, so completeness is 67 percent. Counting the "TBD" field as valid would give 83 percent (B). Completeness shows what is missing and says nothing about whether what is there is good.

    **Concept Tested:** Metadata Completeness

    **See:** [Metadata Completeness](index.md#metadata-completeness)

---

#### 8. A reviewer applies the ten modularity checks to a single long page. Checks 1 and 2 fail, which are serious, and so do checks 3, 5, 8, 9, and 10. Only checks 4, 6, and 7 pass. What score does the chapter's rule give?

<div class="upper-alpha" markdown>
1. 4, because 30 percent falls in the 3 to 4 band and the higher number applies
2. 5, because three checks passed and two serious checks failed, so the score is 5
3. 3, because 30 percent falls in the 3 to 4 band and failing checks 1 and 2 is serious
4. 1, because the page cannot be taken apart at all, so no points are earned
</div>

??? question "Show Answer"
    The correct answer is **C**. Three of ten checks pass, a share of 30 percent, in the 3 to 4 band. Checks 1 and 2 are serious because failing them means the resource cannot be taken apart at all. When a serious check fails, choose the lower number in a two-number band, so the score is 3. The higher number (A) applies only when no serious check fails. The score depends on the share of checks passed and not on how many serious checks failed.

    **Concept Tested:** Modularity Metric

    **See:** [The Modularity Metric](index.md#the-modularity-metric)

---

#### 9. A teacher searches for "grade 6 watershed quiz." Record A has a clear title, subject terms, grades 6 to 7, a license, and a description of a reading and eight-question quiz. Record B has only the title "Reading 4." Record C has the title "Watershed Basics" and an author, with nothing else. Which analysis is best?

<div class="upper-alpha" markdown>
1. All three records are found equally, because a title alone is enough for a search to match
2. A is found and understood, B cannot be found, and C may be found but its grade and license are unknown
3. Record C ranks highest, because naming an author helps a search engine more than any other field
4. Record B is found, because a unique title such as "Reading 4" always matches any search
</div>

??? question "Show Answer"
    The correct answer is **B**. A search matches the words in a resource's metadata. Record A has fields that mention the topic, grade, and contents, so it is found and a teacher can tell what it is. Record B has no field that mentions a watershed. Record C may match on its title, but without a grade level or license the teacher cannot tell whether it fits or whether she may reuse it. A resource whose metadata is missing may as well not exist.

    **Concept Tested:** Metadata Metric

    **See:** [The Metadata Metric](index.md#the-metadata-metric)

---

#### 10. A reviewer finds that a page footer says CC BY-NC, while the license field in the metadata says CC BY. Which analysis is best?

<div class="upper-alpha" markdown>
1. The record and the page disagree, so the license is unclear and must be confirmed and made to match
2. The page always wins automatically, so the metadata can stay as it is and be ignored
3. There is no problem, because both are Creative Commons licenses and both allow reuse
4. The more permissive license is the valid one, so CC BY applies to the whole resource
</div>

??? question "Show Answer"
    The correct answer is **A**. The license field must agree with the statement on the page, and a mismatch invites a dispute. Unclear licensing is a risk for the reuser, because the safe assumption is that no permission was granted. Both licenses are Creative Commons licenses, but they grant different permissions, since NC bars commercial use (C). The reviewer should trace the work to its owner, confirm the license, and fix both places, and a mismatched value counts as invalid.

    **Concept Tested:** License Field

    **See:** [License Field](index.md#license-field)
