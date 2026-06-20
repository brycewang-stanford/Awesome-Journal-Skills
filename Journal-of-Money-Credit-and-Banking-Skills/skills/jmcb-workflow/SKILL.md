---
name: jmcb-workflow
description: Use when deciding which jmcb-* sub-skill to invoke next for a Journal of Money, Credit and Banking manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jmcb-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Money, Credit and Banking (JMCB)**. The journal's center of gravity is monetary economics, banking, credit markets, financial intermediation, and macro-finance. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Wiley for the Ohio State University Department of Economics; submission route to re-check live: Wiley online submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JMCB and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JMCB with nearby venues: Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance, and Journal of Financial Intermediation.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jmcb-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jmcb-literature-positioning` |
| causal or structural credibility is the bottleneck | `jmcb-identification` |
| market-data design or measurement is fragile | `jmcb-empirical-design` |
| results may be specification-, sample-, or inference-sensitive | `jmcb-robustness` |
| exhibits are hard to read or do not answer the question | `jmcb-tables-figures` |
| appendix materials are too thin or too sprawling | `jmcb-internet-appendix` |
| the introduction, abstract, or prose misses the journal voice | `jmcb-writing-style` |
| the paper is close to submission and needs a final preflight | `jmcb-submission` |
| likely objections should be anticipated before submission | `jmcb-referee-strategy` |
| a decision letter or referee report needs a response plan | `jmcb-rebuttal` |

## Default order

`jmcb-workflow → jmcb-topic-selection → jmcb-literature-positioning → jmcb-identification → jmcb-empirical-design → jmcb-robustness → jmcb-tables-figures → jmcb-internet-appendix → jmcb-writing-style → jmcb-submission → jmcb-referee-strategy → jmcb-rebuttal`

## Journal-specific lenses
- Scope lens: monetary economics, banking, credit markets, financial intermediation, and macro-finance.
- Field vocabulary to keep visible: monetary transmission; bank balance sheets; credit frictions; central-bank relevance; macro-finance identification.
- Sibling boundary: Journal of Monetary Economics, Review of Economic Dynamics, Journal of Finance, and Journal of Financial Intermediation.
- Writing standard: policy-relevant macro-finance evidence with transparent timing and institutional detail.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JMCB as interchangeable with Journal of Monetary Economics
- Treating JMCB as interchangeable with Review of Economic Dynamics
- Treating JMCB as interchangeable with Journal of Finance
- Using a generic top-five-economics or generic management template without the JMCB audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Money, Credit and Banking
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jmcb-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
