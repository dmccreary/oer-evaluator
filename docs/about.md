---
title: "About This Book"
description: "About OER Evaluator: its purpose, audience, design, why the book is itself an example of an open educational resource, and the author behind it."
---

# About This Book

## Welcome from Echo

!!! mascot-welcome "Welcome!"
    ![Echo the Loon waving welcome](./img/mascot/welcome.png){ class="mascot-admonition-img" }
    I'm Echo, and I'll be your guide through this book. You are about to learn how to judge an open educational resource, score it, and improve it. Along the way you will see that this very book is one. Let's dive in and check the evidence!

## Why This Intelligent Textbook

Teachers can now find thousands of free, openly licensed textbooks. Finding one is easy. Knowing whether it is *good*, and whether you can legally and practically reuse it in your own course, is the hard part. A careful manual review of one textbook can take hours, and two reviewers with different checklists often reach different conclusions.

The need for open materials is widely recognized:

- In November 2019, the member states of UNESCO adopted the **Recommendation on Open Educational Resources**, the first international standard-setting instrument on OER.[^1]
- The widely used definition of OER centers on the **5R permissions**: retain, reuse, revise, remix, and redistribute.[^2]
- Research syntheses of student outcomes with OER generally find results comparable to commercial textbooks, with large savings for students.[^3]

If a resource's quality and reusability can't be measured the same way twice, then adoption decisions rest on opinion. This book teaches a repeatable method instead: a **10-metric rubric** worth 10 points each, five for quality and five for reusability. You will learn to score a resource by hand, direct an AI agent to make the first pass, check the agent's evidence, and test with students whether an improvement helped.

This book takes a different approach from a traditional textbook. It is built on a **learning graph of 351 interconnected concepts**, introduced in prerequisite order across 19 chapters. It includes **20 interactive MicroSims** for hands-on exploration, a quiz and annotated reference list for every chapter, a glossary, and an FAQ. It is free to read, with no paywalls and no access codes.

## This Book Is Itself an OER

Most books about OER describe the idea from the outside. This one is also an example you can inspect. Every claim the book makes about open resources can be checked against the book itself:

| What the book teaches | Where you can see it in this book |
|---|---|
| An OER has an open license | The [license page](license.md) states the terms, and the footer repeats them on every page |
| Editable source in open formats | Every page is plain Markdown in a public [GitHub repository](https://github.com/dmccreary/oer-evaluator) |
| Modularity | Each chapter, quiz, and MicroSim is its own self-contained page that can be reused alone |
| Metadata | Each page carries title, description, and date metadata in its front matter |
| Portability | The site is static HTML that can be copied, hosted anywhere, or forked in minutes |
| Practice with feedback | Every chapter ends with a quiz, and the MicroSims respond to what you do |
| Accessibility | Images have alt text, headings follow a logical order, and pages use a readable font and contrast |
| Version control | The full edit history is public, so you can see exactly what changed and when |

Treat the book as a worked case. As you learn each metric, turn it on this book and score it. The [Rubric Specification](rubric-spec.md) defines the same scale you will use on any other resource. If you find a place where this book falls short, that is a useful result. The repository accepts corrections and improvements.

!!! mascot-tip "Tip"
    ![Echo the Loon giving a tip](./img/mascot/tip.png){ class="mascot-admonition-img" }
    Evaluate this book as you read it. Scoring a resource you are already holding is the fastest way to learn the rubric.

One honest note on licensing: this book uses CC BY-NC-SA 4.0. The NonCommercial term keeps it free for teachers, but it also limits some kinds of reuse. You will learn in Chapter 2 why that choice costs points on the open-license metric. Seeing a trade-off in the book you are reading makes it easier to recognize in other resources.

## How to Use This Book

This textbook is designed for self-paced study. Each chapter builds on the previous ones, so reading in order is recommended. The book includes:

- **19 Chapters** covering OER foundations, open licenses, the 10-metric rubric, quality and reusability metrics, AI-agent evaluation, improving resources, A/B testing with students, and training reviewers
- **20 Interactive MicroSims** embedded in chapters, browser-based simulations you can manipulate to explore concepts
- **Quizzes** at the end of each chapter, 190 questions in all
- **Annotated References** for every chapter
- **Glossary** with definitions for 351 concepts
- **FAQ** with 100 common questions and answers
- **Learning Graph** that shows how all of the concepts depend on one another
- **Search** available from any page using the search bar

The [Learning Graph](learning-graph/index.md) shows how concepts connect across chapters. If you want to explore non-linearly or check the prerequisites for a topic, start there. The [course description](course-description.md) lists the learning outcomes and the topics that are not covered.

## About the Author

![Dan McCreary](./img/dan-headshot-small.png){ width="150px" align="right" }

Dan McCreary is a semi-retired AI researcher, solution architect, and educator who has spent more than three decades helping Fortune 100 organizations reason over massive datasets. At Optum he founded the Generative AI Center of Excellence and led the team that built one of the world's largest healthcare knowledge graphs, spanning over 25 billion vertices, to unify member, provider, and patient insights.

Dan is **new to the OER field**. He came to it from a different direction: decades of work on the knowledge representation strategies, such as knowledge graphs, ontologies, and concept dependency models, that power AI agents. That background shapes this book. Evaluating an OER is a knowledge representation problem. A rubric is a structured model of what "good" means, an AI agent can apply that model only if the model is explicit, and the evidence an agent cites is only trustworthy if it can be checked against the source. Dan brings the habits of a knowledge engineer, such as making definitions precise, tracing every claim to evidence, and mapping prerequisites, to a field that has long relied on informal judgment. He is learning from the OER community as he writes, and he welcomes corrections from practitioners who know the field better than he does.

He is the co-author of *Making Sense of NoSQL* (Manning Publications), the founding chair of the NoSQL Now! conference, and a frequent keynote speaker on semantic search, ontology strategy, and AI hardware. Beyond industry, Dan has mentored students as a STEM volunteer since 2014 and now applies the same rigor to building open educational resources. You can visit the [Intelligent Textbooks Case Studies](https://dmccreary.github.io/intelligent-textbooks/case-studies/) to see over 87 textbooks that Dan has created or co-created with other authors.

**Selected Credentials**

- B.A. in Physics and Computer Science from Carleton College
- M.S.E.E. from the University of Minnesota
- MBA coursework at the University of St. Thomas
- Patent holder in semantic search and ontology management techniques
- Advocate for large-scale Enterprise Knowledge Graph adoption across healthcare and education
- Long-time promoter of accessible, low-cost AI-powered learning experiences

## Related Textbooks

This book is one of a family of open, interactive textbooks built with the same tools. If you want to build an OER like this one, or understand the techniques behind it, these are the best places to continue.

| Textbook | What it covers |
|---|---|
| [Building Intelligent Textbooks With AI](https://dmccreary.github.io/intelligent-textbooks/) | The main guide to designing and building intelligent textbooks with open source tools such as MkDocs Material, including case studies of finished books |
| [Agent Skills for Intelligent Textbooks](https://dmccreary.github.io/ibook-skills/) | The portable AI agent skills that generate the chapters, quizzes, glossary, MicroSims, and site features of a book like this one, tested on Claude, OpenAI Codex, Google Antigravity, Gemini, and Cursor |
| [Learning Graphs](https://dmccreary.github.io/learning-graphs/) | How to create and maintain learning graphs (concept dependency graphs), the structure that orders every chapter in this book |
| [Intelligent Book Template](https://dmccreary.github.io/intelligent-book-template/) | A starter template for creating a new interactive textbook with MkDocs and Material for MkDocs |
| [Adding Voice to Your Textbook](https://dmccreary.github.io/adding-voice-to-your-textbook/) | A practical pattern for adding a page-aware voice tutor to an interactive textbook |
| [The Art of Processing](https://dmccreary.github.io/p5-textbook/) | An interactive textbook on the p5.js library, with many MicroSim examples |

For a larger list, see the [case studies index](https://dmccreary.github.io/intelligent-textbooks/case-studies/) in the Intelligent Textbooks book.

## How to Cite This Book

If you reference this textbook in academic work, curriculum proposals, lesson plans, or other publications, please use one of the following citation formats.

**APA (7th edition)**

McCreary, D. (2026). *OER Evaluator*. https://dmccreary.github.io/oer-evaluator/

**Chicago (17th edition)**

McCreary, Dan. 2026. *OER Evaluator*. https://dmccreary.github.io/oer-evaluator/.

**MLA (9th edition)**

McCreary, Dan. *OER Evaluator*. 2026, dmccreary.github.io/oer-evaluator/.

**BibTeX**

```bibtex
@book{mccreary2026oerevaluator,
  title     = {OER Evaluator},
  author    = {McCreary, Dan},
  year      = {2026},
  url       = {https://dmccreary.github.io/oer-evaluator/},
  note      = {Interactive intelligent textbook}
}
```

To cite a specific chapter, append the chapter number and title. For example:

McCreary, D. (2026). Chapter 1: Foundations of Open Educational Resources. In *OER Evaluator*. https://dmccreary.github.io/oer-evaluator/chapters/01-foundations-of-oer/

## License

This work is released under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](license.md). You are free to share and adapt the material for non-commercial purposes as long as you give appropriate credit and share your adaptations under the same license.

## References

[^1]: UNESCO. (2019). *Recommendation on Open Educational Resources (OER)*. Adopted by the 40th General Conference of UNESCO. <https://www.unesco.org/en/open-educational-resources>
[^2]: Wiley, D. (n.d.). *Defining the "Open" in Open Content and Open Educational Resources*. Open Content. <https://opencontent.org/definition/>
[^3]: Hilton, J. L., III. (2020). Open educational resources, student efficacy, and user perceptions: a synthesis of research published between 2015 and 2018. *Educational Technology Research and Development, 68*, 853–876. <https://doi.org/10.1007/s11423-019-09700-4>
