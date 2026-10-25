# Quiz: Accessibility

Test your understanding of WCAG 2.1 AA, alt text, contrast, media alternatives, keyboard use, screen readers, and accessibility checkers with these review questions.

---

#### 1. What are the four principles of WCAG, often abbreviated POUR?

<div class="upper-alpha" markdown>
1. Perceivable, organized, usable, and reliable
2. Photographic, operable, universal, and readable
3. Practical, open, understandable, and responsive across devices
4. Perceivable, operable, understandable, and robust
</div>

??? question "Show Answer"
    The correct answer is **D**. The Web Content Accessibility Guidelines group their testable success criteria under four principles. Content must be perceivable, so users can sense it through sight or hearing or touch. It must be operable, including without a mouse. It must be understandable, so users can follow what it says and how it works. And it must be robust, so it works with browsers and assistive technology. Each criterion carries a level of A, AA, or AAA.

    **Concept Tested:** WCAG

    **See:** [WCAG](index.md#wcag)

---

#### 2. What does conformance to WCAG 2.1 AA require?

<div class="upper-alpha" markdown>
1. Meeting every level A criterion and every level AA criterion
2. Meeting only the level AA criteria and none of the level A criteria
3. Meeting every level A, level AA, and level AAA criterion
4. Passing an automated accessibility checker with no errors
</div>

??? question "Show Answer"
    The correct answer is **A**. WCAG 2.1 AA is version 2.1 at conformance level AA, which means a resource meets every level A criterion and every level AA criterion. This book targets it because many school and college policies cite it, and because it protects the main groups of learners while staying practical for a teacher to check. Level AAA is the highest level and is not required for whole sites, and a clean checker report (D) is not the same as conformance.

    **Concept Tested:** WCAG 2.1 AA

    **See:** [WCAG 2.1 AA](index.md#wcag-21-aa)

---

#### 3. How should a decorative image, such as a thin border line, be marked in HTML so that a screen reader skips it?

<div class="upper-alpha" markdown>
1. Leave out the alt attribute entirely so that the reader skips the image altogether
2. Give it alt text that says "decoration" so that readers know it is not content
3. Use its file name as the alt text so that the image is still identified
4. Give it an empty alt attribute, written as `alt=""`, so that the reader skips it
</div>

??? question "Show Answer"
    The correct answer is **D**. A decorative image adds appearance only, so a screen reader should skip it, and an empty alt attribute tells the reader to do that. An image with no alt attribute at all is a different case, because many screen readers then read out the file name, which is useless. Alt text that says "decoration" (B) makes the reader announce something that carries no information. When a learner might wonder what the image is, write a short description instead.

    **Concept Tested:** Decorative Image

    **See:** [Decorative Image](index.md#decorative-image)

---

#### 4. Why should alt text describe what an image does in its context instead of only how it looks?

<div class="upper-alpha" markdown>
1. Screen readers cannot announce descriptions that are longer than one word, so short text is always required
2. A reader who cannot see the image needs text that does the same job the image does for a sighted reader
3. Alt text is shown only on printed copies of a page, where the appearance of an image does not matter
4. Describing the appearance would repeat the page's heading and so add nothing for the reader
</div>

??? question "Show Answer"
    The correct answer is **B**. Good alt text answers "what does this image do here?" A photo of a river in a lesson about meanders needs alt text that mentions the bends, while the same photo used only for mood needs none. Say what matters in a sentence or two, do not begin with "image of," do not repeat an adjacent caption, and never leave a file name or a single word such as "photo."

    **Concept Tested:** Alt Text

    **See:** [Alt Text](index.md#alt-text)

---

#### 5. Which media alternative narrates the important visual information in a video that the soundtrack does not already give?

<div class="upper-alpha" markdown>
1. Captions
2. Keyboard navigation
3. Color independence
4. Audio description
</div>

??? question "Show Answer"
    The correct answer is **D**. Audio description is spoken narration of actions, scene changes, on-screen text, and charts. It serves learners who are blind or have low vision, and it fills the gap when an instructor says "as you can see here" and points to a chart that is never described. Captions (A) are timed text of speech and important sounds for learners who cannot hear. At level AA, prerecorded video with sound needs captions and audio description.

    **Concept Tested:** Audio Description

    **See:** [Audio Description](index.md#audio-description)

---

#### 6. A page contains an image with no alt attribute, and the image file is named river.png. What does a screen reader typically say?

<div class="upper-alpha" markdown>
1. "Image, river dot png," reading the file name aloud to the listener
2. Nothing, because the image is skipped and the reader moves on to the next element
3. "Image, a river," describing the picture to the listener in words
4. "Image, decorative," announcing that the image carries no meaning
</div>

??? question "Show Answer"
    The correct answer is **A**. A screen reader reads the page's underlying structure and does not look at the picture, so without alt text it often falls back on the file name. That is useless to the listener. An empty alt attribute is what makes a reader skip an image (B), and no screen reader describes a photo by itself (C). Wording varies between programs, so listen to a page for five minutes before you score.

    **Concept Tested:** Screen Reader

    **See:** [Screen Reader](index.md#screen-reader)

---

#### 7. A reviewer measures four text-and-background pairs. Which one passes for normal-size body text under WCAG 2.1 AA?

<div class="upper-alpha" markdown>
1. Gray on white with a contrast ratio of 4.61 to 1
2. Gray on white with a contrast ratio of 3.03 to 1
3. White on orange with a contrast ratio of 2.33 to 1
4. Pale gray on white with a contrast ratio of 1.36 to 1
</div>

??? question "Show Answer"
    The correct answer is **A**. Normal text needs a contrast ratio of at least 4.5 to 1. A ratio of 3.03 to 1 (B) meets only the 3 to 1 minimum for large text, which means at least 18 points, or 14 points if bold. The other two pairs fail for every size. Pass or fail can hinge on a difference no one can see, so reviewers measure with a tool instead of judging by eye.

    **Concept Tested:** Contrast Ratio

    **See:** [Contrast Ratio](index.md#contrast-ratio)

---

#### 8. A reviewer applies the ten accessibility checks to a lecture video series. Check 7 (captions), check 8 (transcripts or audio description), and check 10 (page language, link text, table headers) fail, and the other seven pass. What score does the chapter's rule give?

<div class="upper-alpha" markdown>
1. 6, because 70 percent falls in the 5 to 6 band and the higher number applies
2. 7, because seven checks passed, so the score equals the number of passes
3. 5, because 70 percent falls in the 5 to 6 band and uncaptioned video is a serious failure
4. 3, because three checks failed, so the score equals the number of failures
</div>

??? question "Show Answer"
    The correct answer is **C**. Seven of ten checks pass, a share of 70 percent, which falls in the 5 to 6 band. A failed check is serious when it keeps a group of learners out of the content altogether, and video with no captions is one of the named examples. When a serious check fails, choose the lower number in the band, so the score is 5. The higher number (A) applies only when no serious check fails.

    **Concept Tested:** Accessibility Metric

    **See:** [Scoring Accessibility](index.md#scoring-accessibility)

---

#### 9. An automated checker reports zero errors for a page, but every image on the page has the alt text "photo." Which analysis is correct?

<div class="upper-alpha" markdown>
1. The page passes the accessibility metric, because the tool reports no errors on any of its images
2. The checker is faulty, because any good checker would flag one-word alt text as a failure
3. The checker confirms alt text exists but cannot judge whether it is useful, so the page still fails that check
4. Alt text is no longer required once an automated checker reports no errors for the page
</div>

??? question "Show Answer"
    The correct answer is **C**. A checker finds real problems quickly, such as images with no alt attribute, weak contrast, and unlabeled form fields. It cannot tell whether alt text is useful, and it cannot tell whether a heading describes its section. A clean report is therefore not a pass. Run the tool, then do the human checks: read the alt text, listen with a screen reader, and tab through the page.

    **Concept Tested:** Accessibility Checker

    **See:** [Accessibility Checker](index.md#accessibility-checker)

---

#### 10. A chart marks the winning team in green and the losing team in red and offers no other cue. Which learners does this exclude, and what is the fix?

<div class="upper-alpha" markdown>
1. Only learners who use a screen reader, so add alt text to the chart and nothing else
2. Learners who are color blind or print in gray, so add a second cue such as a label, pattern, or icon
3. Only learners who are deaf or hard of hearing, so add captions to the chart
4. No one, because red and green contrast strongly, so no change is needed to the chart
</div>

??? question "Show Answer"
    The correct answer is **B**. Color independence means color is never the only way a resource conveys information. A learner who is color blind cannot tell the two colors apart, and a learner who prints in gray loses the distinction. Strong contrast between two colors does not help when the difference is in hue (D). The same rule applies to links in a paragraph, which need an underline or another cue beyond a slightly different color.

    **Concept Tested:** Color Independence

    **See:** [Color Independence](index.md#color-independence)
