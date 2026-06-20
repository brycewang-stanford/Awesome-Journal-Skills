---
name: jru-workflow
description: Use when deciding which jru-* sub-skill to invoke next for a Journal of Risk and Uncertainty manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jru-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Risk and Uncertainty (JRU)**. The journal's center of gravity is risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Springer; submission route to re-check live: Springer Nature submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JRU and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JRU with nearby venues: Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jru-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jru-literature-positioning` |
| causal or structural credibility is the bottleneck | `jru-identification` |
| the model, mechanism, or conceptual frame is loose | `jru-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jru-robustness` |
| exhibits are hard to read or do not answer the question | `jru-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jru-writing-style` |
| data, code, or computational documentation needs packaging | `jru-replication-package` |
| likely objections should be anticipated before submission | `jru-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jru-submission` |
| a decision letter or referee report needs a response plan | `jru-rebuttal` |

## Default order

`jru-workflow → jru-topic-selection → jru-literature-positioning → jru-identification → jru-theory-model → jru-robustness → jru-tables-figures → jru-writing-style → jru-replication-package → jru-referee-strategy → jru-submission → jru-rebuttal`

## Journal-specific lenses
- Scope lens: risk, uncertainty, decision theory, behavioral choice, insurance, and experimental evidence on risky decisions.
- Field vocabulary to keep visible: risk preference; uncertainty attitude; prospect-theory test; insurance behavior; experimental elicitation.
- Sibling boundary: Experimental Economics, Journal of Economic Behavior and Organization, Games and Economic Behavior, and Management Science.
- Writing standard: decision-theoretic clarity with careful measurement of risk and uncertainty.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JRU as interchangeable with Experimental Economics
- Treating JRU as interchangeable with Journal of Economic Behavior and Organization
- Treating JRU as interchangeable with Games and Economic Behavior
- Using a generic top-five-economics or generic management template without the JRU audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Risk and Uncertainty
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jru-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
