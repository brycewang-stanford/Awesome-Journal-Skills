---
name: expecon-workflow
description: Use when deciding which expecon-* sub-skill to invoke next for a Experimental Economics manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (expecon-workflow)

## Overview

This router sequences the twelve-skill stack for **Experimental Economics (Experimental Economics)**. The journal's center of gravity is laboratory, field, online, and artefactual experiments in economics. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Springer for the Economic Science Association; submission route to re-check live: Springer Nature submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at Experimental Economics and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing Experimental Economics with nearby venues: JEBO, Games and Economic Behavior, Management Science, and Journal of Risk and Uncertainty.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `expecon-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `expecon-literature-positioning` |
| causal or structural credibility is the bottleneck | `expecon-identification` |
| the model, mechanism, or conceptual frame is loose | `expecon-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `expecon-robustness` |
| exhibits are hard to read or do not answer the question | `expecon-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `expecon-writing-style` |
| data, code, or computational documentation needs packaging | `expecon-replication-package` |
| likely objections should be anticipated before submission | `expecon-referee-strategy` |
| the paper is close to submission and needs a final preflight | `expecon-submission` |
| a decision letter or referee report needs a response plan | `expecon-rebuttal` |

## Default order

`expecon-workflow → expecon-topic-selection → expecon-literature-positioning → expecon-identification → expecon-theory-model → expecon-robustness → expecon-tables-figures → expecon-writing-style → expecon-replication-package → expecon-referee-strategy → expecon-submission → expecon-rebuttal`

## Journal-specific lenses
- Scope lens: laboratory, field, online, and artefactual experiments in economics.
- Field vocabulary to keep visible: experimental protocol; incentive compatibility; pre-analysis plan; treatment contrast; subject-pool design.
- Sibling boundary: JEBO, Games and Economic Behavior, Management Science, and Journal of Risk and Uncertainty.
- Writing standard: protocol-transparent experimental economics with credible incentives and robust inference.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating Experimental Economics as interchangeable with JEBO
- Treating Experimental Economics as interchangeable with Games and Economic Behavior
- Treating Experimental Economics as interchangeable with Management Science
- Using a generic top-five-economics or generic management template without the Experimental Economics audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Experimental Economics
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one expecon-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
