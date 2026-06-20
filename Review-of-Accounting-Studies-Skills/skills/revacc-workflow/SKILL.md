---
name: revacc-workflow
description: Use when deciding which revacc-* sub-skill to invoke next for a Review of Accounting Studies manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (revacc-workflow)

## Overview

This router sequences the twelve-skill stack for **Review of Accounting Studies (RAST)**. The journal's center of gravity is analytical, empirical, and experimental accounting research with strong economics foundations. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Springer; submission route to re-check live: Springer Nature submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at RAST and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing RAST with nearby venues: The Accounting Review, Journal of Accounting Research, Journal of Accounting and Economics, and Contemporary Accounting Research.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `revacc-topic-selection` |
| the management-theory contribution is underdeveloped | `revacc-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `revacc-literature-positioning` |
| methods and construct validity need alignment | `revacc-methods` |
| analysis design, estimation, or qualitative coding needs review | `revacc-data-analysis` |
| the theoretical contribution needs sharper positioning | `revacc-contribution-framing` |
| exhibits are hard to read or do not answer the question | `revacc-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `revacc-writing-style` |
| the paper is close to submission and needs a final preflight | `revacc-submission` |
| review-cycle expectations and revision choreography need planning | `revacc-review-process` |
| a decision letter or referee report needs a response plan | `revacc-rebuttal` |

## Default order

`revacc-workflow → revacc-topic-selection → revacc-theory-development → revacc-literature-positioning → revacc-methods → revacc-data-analysis → revacc-contribution-framing → revacc-tables-figures → revacc-writing-style → revacc-submission → revacc-review-process → revacc-rebuttal`

## Journal-specific lenses
- Scope lens: analytical, empirical, and experimental accounting research with strong economics foundations.
- Field vocabulary to keep visible: accounting disclosure; audit quality; capital-market accounting; tax and reporting; earnings information.
- Sibling boundary: The Accounting Review, Journal of Accounting Research, Journal of Accounting and Economics, and Contemporary Accounting Research.
- Writing standard: accounting research that links institutional reporting detail to credible economic mechanisms.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating RAST as interchangeable with The Accounting Review
- Treating RAST as interchangeable with Journal of Accounting Research
- Treating RAST as interchangeable with Journal of Accounting and Economics
- Using a generic top-five-economics or generic management template without the RAST audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Review of Accounting Studies
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one revacc-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
