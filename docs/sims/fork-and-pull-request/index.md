---
title: "Fork and Pull Request: Two Lanes, Seven Steps"
description: "A two-lane diagram of the seven steps for improving a resource you do not own: find it, fork it, change your copy, propose the change, review, respond, and merge."
image: /sims/fork-and-pull-request/fork-and-pull-request.png
og:image: /sims/fork-and-pull-request/fork-and-pull-request.png
twitter:image: /sims/fork-and-pull-request/fork-and-pull-request.png
social:
   cards: false
status: built
hide:
  - toc
---

<iframe src="main.html" height="806px" width="100%" scrolling="no"></iframe>

[Run the Fork and Pull Request: Two Lanes, Seven Steps MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Chapter 4: Open File Formats and Version Control](../../chapters/04-open-formats-version-control/index.md){ .md-button }

To change the content, edit `data.json` in this folder. The artwork is `fork-and-pull-request.svg`, and `scripts/posters/specs/` holds the code that draws it.

You can add this MicroSim to any web page with this `iframe`:

```html
<iframe src="https://dmccreary.github.io/oer-evaluator/sims/fork-and-pull-request/main.html"
        height="806px"
        width="100%"
        scrolling="no"></iframe>
```

## Description

Git vocabulary is the hardest part of Chapter 4, and this poster shows what a list cannot: whose copy each step happens in. The top lane is the original repository and its maintainer. The bottom lane is your own copy. The seven steps run left to right, and the arrows cross between the lanes at the fork, the pull request, and the merge. A faint dotted branch shows the other ending, a declined pull request. The pictures are physical: a photocopied binder for the fork, a sticky note for the pull request, and a rubber stamp for the merge.

This MicroSim is a **callout overlay**: the poster is a drawing made for this book (SVG) with no text in it, and every label comes from the numbered markers.

| # | Part | What it shows |
|---|---|---|
| 1 | Find the repository | Find the repository of the resource you want to improve. You cannot copy what you have not found. |
| 2 | Fork it to make your own copy | Fork the repository to make your own copy. You change your copy, not the original. |
| 3 | Make your change and save it with a message | Make your change in your copy and save it with a message that says what you did. A pull request needs a change to propose. |
| 4 | Open a pull request | Open a pull request that proposes your change to the original repository. The maintainer can only review a change that has been proposed. |
| 5 | The maintainer reads and comments | The maintainer reads your pull request and leaves comments. The review follows the proposal. |
| 6 | You answer with more changes | You answer any comments by adding more changes to your copy. You respond to what the review found. |
| 7 | The maintainer merges | The maintainer merges the pull request into the original. Merging is the last step, after the review is satisfied. |

### Controls

- **Explore and Quiz buttons:** switch modes.
- **Numbered markers and labels:** hover over a marker or a label to read about that part of the poster.
- **Quiz mode:** the labels are hidden. Read the prompt, then press the marker it names. A wrong press lets you try again.
- **Try Again:** repeats the quiz after the last question.

### Good to Know

Quiz mode scores each marker as you answer it. The MicroSim does not store your answers. The artwork carries no text, so every name and number you read comes from the overlay.

- The drawing is a generic interface with no screenshots or logos of a real code-hosting site.
- The sequence shows the successful path. The faint branch is the other ending.

## Lesson Plan

### Learning Objective

After using this MicroSim, the learner can **order** the seven steps of the fork and pull request workflow and **say** in which copy each step happens. (Bloom level: Understand.)

### Grade Level

Adult learners: teachers (K-12 and college), instructional designers, librarians, and OER coordinators.

### Duration

5-10 minutes.

### Prerequisites

- The meaning of a repository, a fork, and a pull request from [Chapter 4](../../chapters/04-open-formats-version-control/index.md).

### Activities

1. **Explore (3 min).** Hover over markers 1 to 7 in order. Which steps happen in the top lane and which in the bottom lane?
2. **Quiz (3 min).** Press **Quiz** and find each step from its description.
3. **Discuss (4 min).** What does the faint dotted branch show, and what would you do after a declined pull request?

### Assessment

Ask learners to answer without the MicroSim, then check each answer against the poster.

1. Where do you make your change? *(In your own copy, the fork, never in the original.)*
2. Can a pull request be sent before the change is made? *(No. A pull request needs a change to propose.)*
3. Must the maintainer accept every pull request? *(No. A maintainer may decline it.)*

### Connection to the OER Evaluator rubric

This is how an improved resource finds its way back to its author, which matters again in Chapter 15 (improving a resource) and Chapter 18 (publishing components).

## References

1. [Git](https://en.wikipedia.org/wiki/Git) - Wikipedia - Explains Git's distributed model, commits, branches, and history. Background for the chapter's version control section and for reading repository history as evidence when scoring editable source.
2. [Hello World](https://docs.github.com/en/get-started/using-github/hello-world) - GitHub Docs - A short tutorial that creates a repository, a branch, a commit, and a pull request. Gives teachers hands-on experience with the version control steps this chapter describes.
3. [Version Control with Git](https://swcarpentry.github.io/git-novice/) - Software Carpentry - A free lesson for beginners on tracking changes, viewing history, and collaborating with Git, written for people who are not programmers. A gentle companion to the chapter's version control section.
