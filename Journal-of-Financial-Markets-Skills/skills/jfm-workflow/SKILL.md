---
name: jfm-workflow
description: Use when deciding which jfm-* sub-skill to invoke next for a Journal of Financial Markets manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jfm-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Financial Markets (JFM)**. The journal's center of gravity is market microstructure, asset pricing, liquidity, trading, and financial-market design. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JFM and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JFM with nearby venues: Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jfm-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jfm-literature-positioning` |
| causal or structural credibility is the bottleneck | `jfm-identification` |
| market-data design or measurement is fragile | `jfm-empirical-design` |
| results may be specification-, sample-, or inference-sensitive | `jfm-robustness` |
| exhibits are hard to read or do not answer the question | `jfm-tables-figures` |
| appendix materials are too thin or too sprawling | `jfm-internet-appendix` |
| the introduction, abstract, or prose misses the journal voice | `jfm-writing-style` |
| the paper is close to submission and needs a final preflight | `jfm-submission` |
| likely objections should be anticipated before submission | `jfm-referee-strategy` |
| a decision letter or referee report needs a response plan | `jfm-rebuttal` |

## Default order

`jfm-workflow → jfm-topic-selection → jfm-literature-positioning → jfm-identification → jfm-empirical-design → jfm-robustness → jfm-tables-figures → jfm-internet-appendix → jfm-writing-style → jfm-submission → jfm-referee-strategy → jfm-rebuttal`

## Journal-specific lenses
- Scope lens: market microstructure, asset pricing, liquidity, trading, and financial-market design.
- Field vocabulary to keep visible: microstructure mechanism; liquidity measurement; trading venue design; price discovery; high-frequency evidence.
- Sibling boundary: Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science.
- Writing standard: precise institutional detail, clean market data, and careful measurement of frictions.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JFM as interchangeable with Journal of Finance
- Treating JFM as interchangeable with Journal of Financial Economics
- Treating JFM as interchangeable with Review of Financial Studies
- Using a generic top-five-economics or generic management template without the JFM audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Financial Markets
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jfm-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
