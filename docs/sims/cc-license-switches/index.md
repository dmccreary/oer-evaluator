---
title: Creative Commons License Switches
description: A panel of three switches (Attribution, ShareAlike, NonCommercial) that shows how each Creative Commons element changes the license name and takes a freedom away from the person who receives the work.
image: /sims/cc-license-switches/cc-license-switches.png
og:image: /sims/cc-license-switches/cc-license-switches.png
twitter:image: /sims/cc-license-switches/cc-license-switches.png
social:
   cards: false
status: built
quality_score: 100
---

# Creative Commons License Switches

<iframe src="main.html" height="562px" width="100%" scrolling="no"></iframe>

[Run the Creative Commons License Switches MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 2: Open Licenses and Attribution](../../chapters/02-open-licenses-attribution/index.md){ .md-button }

To edit the sketch, paste the contents of `cc-license-switches.js` into the [p5.js editor](https://editor.p5js.org/).

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/cc-license-switches/main.html"
        height="562px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Picture the elements of a Creative Commons license as switches on a panel. The **Attribution (BY)** switch is always on, because every Creative Commons license requires credit to the creator. Each other switch you turn on takes a freedom away from the person who receives the work.

This MicroSim gives you the three switches that keep a work open for adaptation:

| Switch | What it does when you turn it on | Freedom taken away |
|---|---|---|
| **BY** Attribution | Locked on. Credit to the creator is always required. | None. This is the baseline of every Creative Commons license. |
| **SA** ShareAlike | Adaptations must carry the same license as the original. | Picking the license for your remix. |
| **NC** NonCommercial | The work may not be used for commercial advantage or monetary compensation. | Using the work commercially. |

Two freedoms never change on this panel: sharing the unchanged work and adapting, translating, or remixing it, both with credit. The four switch positions give four licenses:

| Switches on | License | Freedoms kept |
|---|---|---|
| BY | CC BY 4.0 | 4 of 4 |
| BY, SA | CC BY-SA 4.0 | 3 of 4 |
| BY, NC | CC BY-NC 4.0 | 3 of 4 |
| BY, NC, SA | CC BY-NC-SA 4.0 | 2 of 4 |

### Controls

- **BY switch (locked):** click it and a message explains why it stays on.
- **SA switch:** turns the ShareAlike requirement on or off.
- **NC switch:** turns the NonCommercial requirement on or off.

Clicking a switch or its label flips it, and the keyboard works too: press Tab to reach a switch and Space to flip it. After each flip the license name changes, the freedom that moved flashes, and a message says what was taken away or given back. A screen reader announces the same result.

### What the panel leaves out

- **NoDerivatives (ND)** is not on this panel. ND takes away the freedom to adapt, and it cannot be combined with ShareAlike. [Chapter 2](../../chapters/02-open-licenses-attribution/index.md) covers all four elements and the six licenses they form.
- **CC0** is a public domain dedication, not a license, so it has no switches.
- The text follows the 4.0 licenses. Earlier versions differ in small ways, and the panel is a study aid, not legal advice. Read the license deed for the exact terms.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **explain** how the ShareAlike and NonCommercial elements each narrow what a person receiving a Creative Commons work may do, and can name the license that results from any setting of the switches. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The five R permissions from [Chapter 1](../../chapters/01-foundations-of-oer/index.md): retain, reuse, revise, remix, and redistribute.
- The Attribution, ShareAlike, and NonCommercial requirements as defined in [Chapter 2](../../chapters/02-open-licenses-attribution/index.md).

### Activities

1. **Predict (2 min).** Before touching a switch, write down which freedom you think NonCommercial takes away and which one ShareAlike takes away.
2. **Explore (3 min).** Flip SA and NC in all four combinations. For each license, record its name and how many freedoms are kept.
3. **Locate the extremes (2 min).** Find the license that keeps all four freedoms and the one that keeps the fewest. Explain in one sentence what the second one costs the person who receives the work.
4. **Try the locked switch (1 min).** Click BY. Explain why Creative Commons does not let you turn it off.

### Assessment

Ask learners to answer without the MicroSim, then check each answer by flipping the switches.

1. A district wants to sell printed copies of an openly licensed worksheet. Which of the two optional switches must be off? *(NC must be off. NC forbids commercial use.)*
2. A teacher translates a CC BY-SA reading. Under which license must she share the translation? *(CC BY-SA, the same license. ShareAlike requires it.)*
3. How many freedoms does CC BY-NC-SA keep on this panel, and which two are taken away? *(Two of four. Commercial use and picking the license for a remix.)*
4. Why is the BY switch locked on? *(Every Creative Commons license requires credit to the creator.)*

### Connection to the OER Evaluator rubric

The more switches are on, the fewer freedoms remain, and the lower a license sits on the openness spectrum. Some definitions of openness are strict: the [Open Definition](https://opendefinition.org/licenses/) accepts CC BY and CC BY-SA, which allow commercial use, and does not accept the NC licenses. [Chapter 9](../../chapters/09-modularity-metadata/index.md) shows how the rubric scores a resource's license along this spectrum.

## References

1. [Creative Commons: About CC Licenses](https://creativecommons.org/share-your-work/cclicenses/). Plain-language description of the four license elements and the six licenses.
2. [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Commons Deed.
3. [Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/). Commons Deed.
4. [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). Commons Deed.
5. [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). Commons Deed.
6. [Open Definition: Conformant Licenses](https://opendefinition.org/licenses/). Open Knowledge Foundation list of licenses that meet the Open Definition.
