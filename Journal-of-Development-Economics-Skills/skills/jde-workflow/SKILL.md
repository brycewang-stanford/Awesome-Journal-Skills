---
name: jde-workflow
description: Use when deciding which jde-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Development Economics (JDE) submission. Routes — it does not replace — the specialized skills.
---

# JDE Workflow Router (jde-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jde-* skill to use at the current stage** of a manuscript aimed at the *Journal of Development Economics*.

Default assumption: unless the user says otherwise, treat the target as JDE — the **leading field journal
in development economics**, published by **Elsevier** and edited by Editors-in-Chief **A. Foster** and
**K. Macours**. It is highly selective: roughly **1,300 submissions a year**, only about a quarter sent
for review, and roughly **6-8% published**. Submission is via **Editorial Manager** under
**single-anonymized review**, with a **USD 50 non-refundable submission fee** for original manuscripts.
JDE has three distinctive routes: a permanent **pre-results review / Registered Reports** track (run
with BITSS), an **AER: Insights-style short-paper** limited-revision track, and a standard full-length
track — plus a **three-papers-per-author-per-12-months** cap and a **mandatory replication / Option C
data-policy** regime.

## When to trigger

- The user asks "what should I do next?"
- The user hands over a draft and needs the current bottleneck diagnosed
- Work is ping-ponging between empirics, framing, writing, and response letters
- A JDE decision letter arrived and the user needs to switch into revision mode
- The user is deciding between the full-length, short-paper, and pre-results routes

## Routing table

| Current symptom                                                       | Next skill                       |
|-----------------------------------------------------------------------|----------------------------------|
| Idea feels small / not clearly a development-economics contribution   | `jde-topic-selection`            |
| Contribution relative to the development literature is fuzzy          | `jde-literature-positioning`     |
| The "so what for development" is undersold or buried                  | `jde-contribution-framing`       |
| Empirics rest on OLS + controls; causal claim undefended              | `jde-identification-strategy`    |
| Estimation, heterogeneity, attrition, or inference choices are shaky  | `jde-data-analysis`              |
| Tables are dense; paper is not figure-forward enough                  | `jde-tables-figures`             |
| Prose buries the idea; abstract/intro do not land the question        | `jde-writing-style`              |
| Need the data/code deposit, or pre-empting referee replication        | `jde-replication-and-data-policy`|
| Unsure how JDE review works (routes, timelines, single-anonymized)    | `jde-review-process`             |
| Ready to submit via Editorial Manager; need a preflight checklist     | `jde-submission`                 |
| Received an R&R; need a response-letter strategy                      | `jde-rebuttal`                   |

## Default order

1. `jde-topic-selection` — lock a first-order development question
2. `jde-literature-positioning` — stake the contribution against the development frontier
3. `jde-contribution-framing` — make the development takeaway explicit
4. `jde-identification-strategy` — make the causal design credible in an LMIC setting
5. `jde-data-analysis` — estimation, heterogeneity, attrition, inference
6. `jde-tables-figures` — finalize figure-forward exhibits
7. `jde-writing-style` — polish prose (abstract + intro last)
8. `jde-replication-and-data-policy` — assemble the Mendeley Data deposit
9. `jde-review-process` — pick the right route and understand the pipeline
10. `jde-submission` — Editorial Manager preflight
11. `jde-rebuttal` — after the R&R

> If your design is prospective, route to `jde-review-process` early — the **pre-results review** track reviews and accepts the design *before* results exist.

## Worked routing example (illustrative)

A user arrives with a fielded cluster-randomized agricultural-extension trial, results in hand, and an unfocused draft. Diagnose the bottleneck before sequencing:

- The causal design is sound (randomized at the village level), so **skip ahead** of `jde-identification-strategy` except to confirm clustering and attrition.
- The draft reports coefficients but no development lesson → the live bottleneck is `jde-contribution-framing`, then `jde-literature-positioning` to stake the increment.
- Because the result is sharp and self-contained (~5,000 words, *illustrative*), flag the **short-paper** route early via `jde-review-process` so the team writes to the 6,000-word / 5-exhibit cap rather than over-building.
- Only after framing and identification settle should `jde-tables-figures` and `jde-writing-style` polish.

## Stage-to-symptom quick map

| Stage symptom                                  | Route to                          |
|------------------------------------------------|-----------------------------------|
| "Is this even a development paper?"            | `jde-topic-selection`             |
| "Results exist but the lesson is fuzzy"        | `jde-contribution-framing`        |
| "A referee will call the design weak"          | `jde-identification-strategy`     |
| "An R&R letter just arrived"                   | `jde-rebuttal`                    |
| "Design not yet fielded"                       | `jde-review-process` (pre-results)|

## Router output

```
【Current stage】topic / framing / identification / analysis / exhibits / writing / replication / review / submission / rebuttal
【Live bottleneck】one sentence
【Route now to】jde-<skill>
【Route candidate (full-length / short-paper / pre-results)】+ why
【Within 3-per-12-months cap?】[Y/N]
```

## Anti-patterns

- **Do not** skip `jde-contribution-framing` — JDE referees judge the development contribution first
- **Do not** let `jde-tables-figures` polish exhibits while identification is still shaky
- **Do not** treat `jde-replication-and-data-policy` as optional — data/code can be requested *at the review stage*
- **Do not** submit a fourth paper inside a 12-month window — the cap is enforced
