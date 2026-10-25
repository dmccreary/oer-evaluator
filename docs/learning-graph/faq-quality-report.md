---
title: FAQ Quality Report
description: Scripted quality checks for the OER Evaluator FAQ, covering question counts, Bloom's Taxonomy balance, answer quality, concept coverage, and link validity.
---

# FAQ Quality Report

Generated 2026-10-24 by the faq-generator skill. The numbers come from scripted checks on `docs/faq.md`, not a human read of every answer. Bloom's levels and difficulty ratings are labels the author of the FAQ assigned to each question, so the distribution table shows balance of intent and not a test result.

## Overall Statistics

- **Total Questions:** 103
- **Overall Quality Score:** 95/100
- **Content Completeness Score:** 100/100 (course description 98/100, valid 351-concept graph, 351 glossary terms, more than 240,000 words, every concept placed in a chapter)
- **Concept Coverage:** 88% (310/351 concepts)
- **Broken links:** 0   **Anchor links:** 0   **Near-duplicate questions:** 0

## Category Breakdown

| Category | Questions | Target range | Avg words | Avg difficulty (1 easy to 3 hard) |
| --- | --- | --- | --- | --- |
| Getting Started | 15 | 10 to 15 | 122 | 1.07 |
| Core Concepts | 28 | 20 to 30 | 156 | 1.46 |
| Technical Details | 25 | 15 to 25 | 159 | 1.96 |
| Common Challenges | 12 | 10 to 15 | 158 | 2.17 |
| Best Practices | 15 | 10 to 15 | 171 | 2.27 |
| Advanced Topics | 8 | 5 to 10 | 208 | 3.00 |

## Bloom's Taxonomy Distribution

Overall, actual against the skill's target:

| Level | Questions | Actual | Target | Deviation |
| --- | --- | --- | --- | --- |
| Remember | 20 | 19% | 20% | -1% ✓ |
| Understand | 31 | 30% | 30% | +0% ✓ |
| Apply | 31 | 30% | 25% | +5% ✓ |
| Analyze | 12 | 12% | 15% | -3% ✓ |
| Evaluate | 6 | 6% | 7% | -1% ✓ |
| Create | 3 | 3% | 3% | -0% ✓ |

Sum of absolute deviations: 10 percentage points. Bloom's score: 20/25.

By category, actual against the category's own target:

| Category | Remember | Understand | Apply | Analyze | Evaluate | Create |
| --- | --- | --- | --- | --- | --- | --- |
| Getting Started | 60% (60%) | 40% (40%) | 0% (0%) | 0% (0%) | 0% (0%) | 0% (0%) |
| Core Concepts | 18% (20%) | 39% (40%) | 32% (30%) | 11% (10%) | 0% (0%) | 0% (0%) |
| Technical Details | 24% (30%) | 40% (40%) | 28% (20%) | 8% (10%) | 0% (0%) | 0% (0%) |
| Common Challenges | 0% (10%) | 25% (30%) | 58% (40%) | 17% (20%) | 0% (0%) | 0% (0%) |
| Best Practices | 0% (0%) | 7% (10%) | 53% (40%) | 13% (30%) | 20% (15%) | 7% (5%) |
| Advanced Topics | 0% (0%) | 0% (0%) | 0% (10%) | 38% (30%) | 38% (30%) | 25% (30%) |

Each cell shows actual percent, with the target in parentheses.

## Answer Quality Analysis

- **Examples:** 85/103 (83%). Target 40% or more. 7/7
- **Links to chapter or reference files:** 103/103 (100%). Target 60% or more. 7/7
- **Average length:** 158 words. Target 100 to 300. 6/6
- **Complete answers:** 100%. 5/5
- **Average reading grade (Flesch-Kincaid, estimated):** 7.8

Answer quality score: 25/25

## Concept Coverage

**Covered:** 310 of 351 concepts. A concept counts as covered when its label appears in a question or answer, or a question lists it.

**Not covered:** 41 concepts, listed with their priority in the [FAQ Coverage Gaps](faq-coverage-gaps.md) report.

Coverage score: 30/30

## Organization Quality

- Logical categorization: 5/5
- Progressive difficulty: 5/5
- No duplicates: 5/5
- Clear questions: 5/5

Organization score: 20/20

## Overall Quality Score: 95/100

- Coverage: 30/30
- Bloom's Distribution: 20/25
- Answer Quality: 25/25
- Organization: 20/20

## Recommendations

1. **Medium priority.** Apply questions are 5 points above target; rebalance when adding questions.
2. **Low priority.** In Common Challenges, Apply questions are 58% against a category target of 40%. The labels follow what each answer asks of the reader, so add questions at the thinner level when the category next grows.
3. **Low priority.** In Best Practices, Analyze questions are 13% against a category target of 30%. The labels follow what each answer asks of the reader, so add questions at the thinner level when the category next grows.
4. **Low priority.** Re-run the generator after the chapters are revised, since answers quote thresholds and score bands that live in the chapters.
