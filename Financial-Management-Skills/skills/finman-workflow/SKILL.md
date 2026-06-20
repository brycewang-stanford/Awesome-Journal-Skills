---
name: finman-workflow
description: Use when deciding which finman-* sub-skill to invoke next for a Financial Management manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (finman-workflow)

## Overview

This router sequences the twelve-skill stack for **Financial Management (FM)**. The journal's center of gravity is corporate finance, investments, market institutions, and applied financial decision-making. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Wiley for the Financial Management Association; submission route to re-check live: Wiley online submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at FM and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing FM with nearby venues: Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `finman-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `finman-literature-positioning` |
| causal or structural credibility is the bottleneck | `finman-identification` |
| market-data design or measurement is fragile | `finman-empirical-design` |
| results may be specification-, sample-, or inference-sensitive | `finman-robustness` |
| exhibits are hard to read or do not answer the question | `finman-tables-figures` |
| appendix materials are too thin or too sprawling | `finman-internet-appendix` |
| the introduction, abstract, or prose misses the journal voice | `finman-writing-style` |
| the paper is close to submission and needs a final preflight | `finman-submission` |
| likely objections should be anticipated before submission | `finman-referee-strategy` |
| a decision letter or referee report needs a response plan | `finman-rebuttal` |

## Default order

`finman-workflow → finman-topic-selection → finman-literature-positioning → finman-identification → finman-empirical-design → finman-robustness → finman-tables-figures → finman-internet-appendix → finman-writing-style → finman-submission → finman-referee-strategy → finman-rebuttal`

## Journal-specific lenses
- Scope lens: corporate finance, investments, market institutions, and applied financial decision-making.
- Field vocabulary to keep visible: corporate policy; capital structure; payout and investment; governance channel; FMA audience.
- Sibling boundary: Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies.
- Writing standard: applied finance evidence that ties estimates to managerial or market decisions.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating FM as interchangeable with Journal of Corporate Finance
- Treating FM as interchangeable with Journal of Banking and Finance
- Treating FM as interchangeable with JFQA
- Using a generic top-five-economics or generic management template without the FM audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Financial Management
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one finman-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
