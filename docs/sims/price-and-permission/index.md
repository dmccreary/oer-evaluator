---
title: Free Is Not Open: Price and Permission
description: A two-by-two matrix that shows price and permission are separate dials, so a free resource can be closed and a paid copy of an open resource can still be open.
image: /sims/price-and-permission/price-and-permission.png
og:image: /sims/price-and-permission/price-and-permission.png
twitter:image: /sims/price-and-permission/price-and-permission.png
social:
   cards: false
status: built
hide:
  - toc
---

# Free Is Not Open: Price and Permission

<iframe src="main.html" height="765px" width="100%" scrolling="no"></iframe>

[Run the Free Is Not Open: Price and Permission MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 1: Foundations of Open Educational Resources](../../chapters/01-foundations-of-oer/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `price-and-permission.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/price-and-permission/main.html"
        height="765px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

This poster is a two-by-two matrix. The columns ask what the resource costs the user. The rows ask whether the user may edit and share it. The four cells use the four examples from Chapter 1. The point is that the two questions are independent: a zero on the price dial says nothing about the permission dial. A resource is OER because of what its license permits, not because of what it costs.

This MicroSim is a **grid overlay**: the poster is a drawing made for this book (SVG), and each zone is a clickable rectangle over it.

| Zone | What it shows |
|---|---|
| Free and open | Free and open: costs nothing and grants permissions. |
| Open, with a paid print copy | Open, with a paid print copy: the license, not the price, makes it OER. |
| Free but closed | Free but closed: no price, but no permission to edit or share. |
| Paid and closed | Paid and closed: costs money and grants no permissions. |

### Controls

- **Explore and Quiz Me buttons:** switch modes. Quiz Me starts a new run.
- **The zones:** hover over a zone or press it to read its summary and facts in the panel below the poster.
- **Quiz questions:** read the question, then press the zone that answers it. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each question as you answer it. The MicroSim does not store your answers. The poster prints its own headings, so the sim adds no labels on top of it.
- The dollar amounts in the chapter, such as the $15 printed copy, are illustrative and are left off the poster.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **explain** why a resource that costs nothing is not necessarily open, using the four cells of the price and permission matrix. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The definition of an open educational resource from [Chapter 1](../../chapters/01-foundations-of-oer/index.md).

### Activities

1. **Explore (3 min).** Press each of the four zones and read the facts. Which zone surprises you most?
2. **Quiz (3 min).** Press **Quiz Me** and place all four examples.
3. **Apply (4 min).** Pick three resources you used this month and say which zone each belongs in. What would you need to check to be sure?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. A library e-book costs the reader nothing but forbids copying. Which zone is it in? *(Free but closed.)*
2. A lesson plan licensed CC BY 4.0 is posted on a teacher blog. Is it OER? *(Yes. It is open, and the price does not matter.)*
3. A print shop sells an open textbook at cost. Is the printed copy still OER? *(Yes. The license grants the permissions even though the paper copy costs money.)*

### Connection to the OER Evaluator rubric

Open license is the first reusability metric in the ten-metric rubric. The rubric scores what you may do with a resource, never what it costs, which is why this matrix comes before any scoring.

## References

1. [Open educational resources](https://en.wikipedia.org/wiki/Open_educational_resources) - Wikipedia - Defines OER, traces the movement's history, and lists the 5R permissions with examples of repositories and national policies. Anchors this chapter's definition of an OER and its distinction between open and merely free materials.
2. [Free content](https://en.wikipedia.org/wiki/Free_content) - Wikipedia - Surveys definitions of free and open content, separating works that merely cost nothing from works that grant freedoms to reuse and modify. Supports the chapter's section explaining why free does not mean open.
3. [Definition of Open](https://opencontent.org/definition/) - opencontent.org - David Wiley's own statement of the 5R permissions (retain, reuse, revise, remix, redistribute) and why a license must grant all five. This is the source of the 5R framework used throughout the book.
4. [Open Educational Resources](https://www.unesco.org/en/open-educational-resources) - UNESCO - UNESCO's OER hub, including the 2019 Recommendation on OER, the first international standard-setting instrument for openly licensed materials. Shows how governments define OER and why they encourage adoption.
