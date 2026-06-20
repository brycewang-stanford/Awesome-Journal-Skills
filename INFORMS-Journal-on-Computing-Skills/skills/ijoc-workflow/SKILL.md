---
name: ijoc-workflow
description: Use when deciding which ijoc-* sub-skill to invoke next for a INFORMS Journal on Computing manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (ijoc-workflow)

## Overview

This router sequences the twelve-skill stack for **INFORMS Journal on Computing (IJOC)**. The journal's center of gravity is operations research and computing, algorithms, optimization, machine learning, simulation, and computational decision systems. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: INFORMS; submission route to re-check live: INFORMS / ScholarOne submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at IJOC and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing IJOC with nearby venues: Operations Research, Management Science, Manufacturing & Service Operations Management, and ACM/IEEE computing venues.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `ijoc-topic-selection` |
| the management-theory contribution is underdeveloped | `ijoc-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `ijoc-literature-positioning` |
| methods and construct validity need alignment | `ijoc-methods` |
| analysis design, estimation, or qualitative coding needs review | `ijoc-data-analysis` |
| the theoretical contribution needs sharper positioning | `ijoc-contribution-framing` |
| exhibits are hard to read or do not answer the question | `ijoc-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `ijoc-writing-style` |
| the paper is close to submission and needs a final preflight | `ijoc-submission` |
| review-cycle expectations and revision choreography need planning | `ijoc-review-process` |
| a decision letter or referee report needs a response plan | `ijoc-rebuttal` |

## Default order

`ijoc-workflow → ijoc-topic-selection → ijoc-theory-development → ijoc-literature-positioning → ijoc-methods → ijoc-data-analysis → ijoc-contribution-framing → ijoc-tables-figures → ijoc-writing-style → ijoc-submission → ijoc-review-process → ijoc-rebuttal`

## Journal-specific lenses
- Scope lens: operations research and computing, algorithms, optimization, machine learning, simulation, and computational decision systems.
- Field vocabulary to keep visible: algorithmic contribution; computational experiment; optimization benchmark; reproducible code; decision analytics.
- Sibling boundary: Operations Research, Management Science, Manufacturing & Service Operations Management, and ACM/IEEE computing venues.
- Writing standard: computational OR contribution with transparent algorithms, benchmarks, and reproducibility.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating IJOC as interchangeable with Operations Research
- Treating IJOC as interchangeable with Management Science
- Treating IJOC as interchangeable with Manufacturing & Service Operations Management
- Using a generic top-five-economics or generic management template without the IJOC audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】INFORMS Journal on Computing
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one ijoc-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
