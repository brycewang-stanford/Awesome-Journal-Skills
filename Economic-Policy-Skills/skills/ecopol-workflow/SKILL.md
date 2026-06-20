---
name: ecopol-workflow
description: Use when deciding which ecopol-* sub-skill to invoke next for a Economic Policy manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (ecopol-workflow)

## Overview

This router sequences the twelve-skill stack for **Economic Policy (Economic Policy)**. The journal's center of gravity is policy-relevant economics papers written for an expert but broad policy audience. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Oxford University Press / CEPR and partner institutions; submission route to re-check live: OUP submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at Economic Policy and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing Economic Policy with nearby venues: AEJ Economic Policy, Journal of Public Economics, IMF Economic Review, and World Bank Economic Review.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `ecopol-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `ecopol-literature-positioning` |
| causal or structural credibility is the bottleneck | `ecopol-identification` |
| the model, mechanism, or conceptual frame is loose | `ecopol-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `ecopol-robustness` |
| exhibits are hard to read or do not answer the question | `ecopol-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `ecopol-writing-style` |
| data, code, or computational documentation needs packaging | `ecopol-replication-package` |
| likely objections should be anticipated before submission | `ecopol-referee-strategy` |
| the paper is close to submission and needs a final preflight | `ecopol-submission` |
| a decision letter or referee report needs a response plan | `ecopol-rebuttal` |

## Default order

`ecopol-workflow → ecopol-topic-selection → ecopol-literature-positioning → ecopol-identification → ecopol-theory-model → ecopol-robustness → ecopol-tables-figures → ecopol-writing-style → ecopol-replication-package → ecopol-referee-strategy → ecopol-submission → ecopol-rebuttal`

## Journal-specific lenses
- Scope lens: policy-relevant economics papers written for an expert but broad policy audience.
- Field vocabulary to keep visible: policy question; European policy debate; CEPR audience; welfare implication; transparent counterfactual.
- Sibling boundary: AEJ Economic Policy, Journal of Public Economics, IMF Economic Review, and World Bank Economic Review.
- Writing standard: policy-first economics that states the decision problem, evidence, and limits plainly.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating Economic Policy as interchangeable with AEJ Economic Policy
- Treating Economic Policy as interchangeable with Journal of Public Economics
- Treating Economic Policy as interchangeable with IMF Economic Review
- Using a generic top-five-economics or generic management template without the Economic Policy audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Economic Policy
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one ecopol-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
