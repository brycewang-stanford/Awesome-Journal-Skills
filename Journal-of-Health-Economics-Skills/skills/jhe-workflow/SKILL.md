---
name: jhe-workflow
description: Use when deciding which jhe-* sub-skill to invoke next for a Journal of Health Economics manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jhe-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Health Economics (JHE)**. The journal's center of gravity is health economics, insurance, provider incentives, medical technology, health policy, and health behavior. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JHE and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JHE with nearby venues: American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jhe-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jhe-literature-positioning` |
| causal or structural credibility is the bottleneck | `jhe-identification` |
| the model, mechanism, or conceptual frame is loose | `jhe-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jhe-robustness` |
| exhibits are hard to read or do not answer the question | `jhe-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jhe-writing-style` |
| data, code, or computational documentation needs packaging | `jhe-replication-package` |
| likely objections should be anticipated before submission | `jhe-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jhe-submission` |
| a decision letter or referee report needs a response plan | `jhe-rebuttal` |

## Default order

`jhe-workflow → jhe-topic-selection → jhe-literature-positioning → jhe-identification → jhe-theory-model → jhe-robustness → jhe-tables-figures → jhe-writing-style → jhe-replication-package → jhe-referee-strategy → jhe-submission → jhe-rebuttal`

## Journal-specific lenses
- Scope lens: health economics, insurance, provider incentives, medical technology, health policy, and health behavior.
- Field vocabulary to keep visible: provider incentives; insurance design; patient selection; clinical-policy margin; health-data privacy.
- Sibling boundary: American Journal of Health Economics, Journal of Public Economics, Health Economics, and AEJ Economic Policy.
- Writing standard: policy-relevant causal evidence with institutional health-system detail.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JHE as interchangeable with American Journal of Health Economics
- Treating JHE as interchangeable with Journal of Public Economics
- Treating JHE as interchangeable with Health Economics
- Using a generic top-five-economics or generic management template without the JHE audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Health Economics
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jhe-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
