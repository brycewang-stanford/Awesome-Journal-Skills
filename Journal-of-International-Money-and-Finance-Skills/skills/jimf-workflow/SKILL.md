---
name: jimf-workflow
description: Use when deciding which jimf-* sub-skill to invoke next for a Journal of International Money and Finance manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jimf-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of International Money and Finance (JIMF)**. The journal's center of gravity is international finance, exchange rates, global banking, capital flows, and open-economy macro-finance. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JIMF and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JIMF with nearby venues: Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jimf-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jimf-literature-positioning` |
| causal or structural credibility is the bottleneck | `jimf-identification` |
| market-data design or measurement is fragile | `jimf-empirical-design` |
| results may be specification-, sample-, or inference-sensitive | `jimf-robustness` |
| exhibits are hard to read or do not answer the question | `jimf-tables-figures` |
| appendix materials are too thin or too sprawling | `jimf-internet-appendix` |
| the introduction, abstract, or prose misses the journal voice | `jimf-writing-style` |
| the paper is close to submission and needs a final preflight | `jimf-submission` |
| likely objections should be anticipated before submission | `jimf-referee-strategy` |
| a decision letter or referee report needs a response plan | `jimf-rebuttal` |

## Default order

`jimf-workflow → jimf-topic-selection → jimf-literature-positioning → jimf-identification → jimf-empirical-design → jimf-robustness → jimf-tables-figures → jimf-internet-appendix → jimf-writing-style → jimf-submission → jimf-referee-strategy → jimf-rebuttal`

## Journal-specific lenses
- Scope lens: international finance, exchange rates, global banking, capital flows, and open-economy macro-finance.
- Field vocabulary to keep visible: exchange-rate pass-through; capital-flow shocks; global financial cycle; sovereign risk; cross-border banking.
- Sibling boundary: Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics.
- Writing standard: international-finance identification that respects exchange-rate regimes and cross-country comparability.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JIMF as interchangeable with Journal of International Economics
- Treating JIMF as interchangeable with Journal of Monetary Economics
- Treating JIMF as interchangeable with JMCB
- Using a generic top-five-economics or generic management template without the JIMF audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of International Money and Finance
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jimf-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
