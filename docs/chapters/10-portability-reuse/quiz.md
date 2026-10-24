# Quiz: Portability and Reuse Across Platforms

Test your understanding of browser compatibility, no-login access, embedding, LMS import, Common Cartridge, and platform lock-in with these review questions.

---

#### 1. What is a responsive layout?

<div class="upper-alpha" markdown>
1. A page design that adapts to the screen size, so the same page reads well on a phone, tablet, and monitor
2. A page that responds to each quiz answer with a feedback message that explains the answer
3. A page that loads faster when the learner is signed in to the learning platform
4. A page that saves a copy of itself automatically so that it can be used offline
</div>

??? question "Show Answer"
    The correct answer is **A**. A responsive layout uses flexible widths and text that wraps. A page with a fixed width forces a phone user to scroll sideways and pinch, and a resource inside an iframe on a narrow page overflows. A reviewer tests by narrowing the browser window to the width of a phone and checking that nothing is cut off or overlaps. Feedback messages (B) belong to the practice metric, and offline copies (D) belong to offline access.

    **Concept Tested:** Responsive Layout

    **See:** [Responsive Layout](index.md#responsive-layout)

---

#### 2. Which standard lets an external tool open inside a learning management system and exchange information with it, such as sending a learner's score back to the gradebook?

<div class="upper-alpha" markdown>
1. Common Cartridge
2. LTI integration
3. Iframe embedding
4. Link sharing
</div>

??? question "Show Answer"
    The correct answer is **B**. Learning Tools Interoperability, from the standards group 1EdTech, makes an external tool look like part of the course while it runs on another company's server. It is more powerful than a link and more demanding, because it passes information about learners between systems, which raises the privacy questions of Chapter 13. Common Cartridge (A) packages content for import, and an iframe (C) or a link (D) only displays or opens a page.

    **Concept Tested:** LTI Integration

    **See:** [LTI Integration](index.md#lti-integration)

---

#### 3. Why is a required login a barrier to a resource's portability?

<div class="upper-alpha" markdown>
1. It always makes the resource cost money, because every account requires a paid subscription
2. It makes the resource unreadable on phones, because login pages never adapt to small screens
3. It prevents the resource from carrying an open license, because licenses cannot cover accounts
4. It stops embedding because the frame shows a sign-in form, blocks link sharing, and adds a privacy burden
</div>

??? question "Show Answer"
    The correct answer is **D**. A login breaks portability in three ways. A frame on someone else's page would show a sign-in form instead of the resource. A person who receives a link cannot open it. And an account holds personal data, which adds a privacy burden. Some content, such as a teacher's answer key, may reasonably need a login, but a resource that claims to be open should offer its learner-facing content without one.

    **Concept Tested:** No-Login Access

    **See:** [No-Login Access](index.md#no-login-access)

---

#### 4. Why does the chapter say that a resource whose only copy lives inside a web service is "exactly as portable as the service is permanent"?

<div class="upper-alpha" markdown>
1. Web services always delete content after one year, so every hosted resource disappears
2. Open licenses expire when a resource is hosted on a web service that charges a fee
3. Without an export, a reuser cannot back up or move the resource, so it lasts only as long as the service
4. Creative Commons requires every resource to offer an export format in order to be licensed
</div>

??? question "Show Answer"
    The correct answer is **C**. An export format is the exit door. A resource that can be downloaded in an open format, such as HTML, Markdown, or a standard package, can be backed up, moved to a new host, and used offline. A resource with no download depends entirely on the service that holds it. The risk is practical and not legal: licenses do not expire when a resource is hosted (B), and no license requires an export (D).

    **Concept Tested:** Export Format

    **See:** [Export Format](index.md#export-format)

---

#### 5. Why are resources built from plain HTML, CSS, and JavaScript usually more portable than resources that rely on browser plug-ins?

<div class="upper-alpha" markdown>
1. Plug-ins cannot display text or images, so pages built with them are always blank
2. Open web standards work in the main browsers, while a plug-in like Flash can be discontinued and stop working
3. Plain HTML always downloads faster than any plug-in, so pages load more quickly
4. Browsers require the learner to install a plug-in before they open any page at all
</div>

??? question "Show Answer"
    The correct answer is **B**. Browser compatibility means working correctly in the main browsers, such as Chrome, Firefox, Safari, and Edge, and in recent versions of each. Resources built on open web standards usually work everywhere. Adobe Flash powered many educational animations, and when it was discontinued, the content that depended on it stopped working. A reviewer opens a resource in at least three browsers and notes any that fail.

    **Concept Tested:** Browser Compatibility

    **See:** [Browser Compatibility](index.md#browser-compatibility)

---

#### 6. A teacher wants to copy a whole unit, with its pages, quizzes, and files, into her course, and she also wants a colleague who uses a different learning management system to receive the same unit. Which method fits best?

<div class="upper-alpha" markdown>
1. A link to each page of the unit
2. An iframe embed of the unit's home page
3. A Common Cartridge import
4. An LTI tool
</div>

??? question "Show Answer"
    The correct answer is **C**. A Common Cartridge is a single compressed file that holds the content together with a manifest, a list of what is inside and how it is organized. It can be imported into different learning management systems, which is why it is the common exchange form for course material. Links (A) and embeds (B) leave the content at its original address, and an LTI tool (D) runs an external tool inside the course rather than copying a unit into it.

    **Concept Tested:** LMS Import

    **See:** [Common Cartridge](index.md#common-cartridge)

---

#### 7. A teacher places an iframe for an open simulation on a secure (https) course page. The frame stays blank, and the simulation's address begins with http. What is the most likely cause?

<div class="upper-alpha" markdown>
1. A browser refuses to mix an insecure frame into a secure page, so the address must use https
2. The simulation's server tells browsers not to show the page inside a frame
3. The simulation requires a login, so the frame shows a sign-in form instead
4. The simulation uses a fixed layout that is cut off on a narrow phone screen
</div>

??? question "Show Answer"
    The correct answer is **A**. Iframe embedding can fail on a particular platform for several reasons. The server may tell browsers not to show the page in a frame, the page may be served over an insecure connection that a secure page's browser refuses to mix in, or the platform may strip frames out of what its users write. A login would show a sign-in form (C), not a blank frame, and a fixed layout (D) would show the simulation cut off. Test on more than one platform.

    **Concept Tested:** Iframe Embedding

    **See:** [Iframe Embedding](index.md#iframe-embedding)

---

#### 8. A reviewer applies the ten portability checks to a page that does not open in the main browsers. Checks 1 and 5 fail, and the other eight pass. What score does the chapter's rule give?

<div class="upper-alpha" markdown>
1. 8, because 80 percent falls in the 7 to 8 band and the higher number applies
2. 6, because two checks failed and each failed check subtracts two points from 10
3. 7, because 80 percent falls in the 7 to 8 band and failing the browser check is serious
4. 5, because failing the browser check caps the score at 5 whatever else passes
</div>

??? question "Show Answer"
    The correct answer is **C**. Eight of ten checks pass, a share of 80 percent, which falls in the 7 to 8 band. A failed check is serious when it stops a reuser from using the resource at all in a common setting, and not opening in the main browsers, needing a login, and being unable to embed all qualify. When a serious check fails, choose the lower number in the band, so the score is 7. The higher number (A) applies only when no serious check fails.

    **Concept Tested:** Portability Metric

    **See:** [Scoring Portability](index.md#scoring-portability)

---

#### 9. A reviewer saves a resource's page to a folder and opens it without an internet connection. The styling is lost and the quiz stops working, because the page loads fonts and a quiz library from other websites. Which portability check does this reveal as failing?

<div class="upper-alpha" markdown>
1. Check 2, because a login is needed to view the content
2. Check 5, because the layout does not adapt to a phone-width screen
3. Check 6, because no downloadable copy in an open format is offered
4. Check 9, because the resource cannot be used offline from a saved copy
</div>

??? question "Show Answer"
    The correct answer is **D**. Offline access is the ability to use a resource without an internet connection. A single web page with its files can often be saved and opened from a folder, as long as it does not load code or images from elsewhere on the web. Here the saved copy depends on outside fonts and a library, so it breaks. The page itself can be downloaded, so check 6 is not the failing check, and nothing in the description involves a login or a phone.

    **Concept Tested:** Offline Access

    **See:** [Offline Access](index.md#offline-access)

---

#### 10. An author builds a lesson on a free platform. The lesson is openly licensed and free to read, but its interactive parts exist only inside the vendor's system, and the platform offers no export. Which analysis is correct?

<div class="upper-alpha" markdown>
1. The resource is fully portable, because it is free to read and openly licensed
2. The license grants permissions, but the content is locked in, so portability should score poorly
3. The resource is portable, because learners do not need to pay anything to use it
4. Lock-in is a risk only for the author and does not affect people who reuse the resource
</div>

??? question "Show Answer"
    The correct answer is **B**. Platform lock-in is dependence on one platform in a way that makes leaving costly or impossible. Signs include content in a vendor's proprietary format, no export, features that exist only in the vendor's system, and accounts that would be lost on leaving. The test is whether you could move the resource to another host in an afternoon with nothing lost. Lock-in is a risk to every reuser (D), because the resource lives only as long as the platform's business model.

    **Concept Tested:** Platform Lock-In

    **See:** [Platform Lock-In](index.md#platform-lock-in)
