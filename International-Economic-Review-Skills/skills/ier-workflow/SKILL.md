---
name: ier-workflow
description: Use when deciding which ier-* sub-skill to invoke next for a International Economic Review manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (ier-workflow)

## Overview

This router sequences the twelve-skill stack for **International Economic Review (IER)**. The journal's center of gravity is general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Wiley for the Economics Department of the University of Pennsylvania and the Osaka University Institute of Social and Economic Research; submission route to re-check live: Wiley / ScholarOne-style online submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at IER and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing IER with nearby venues: QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `ier-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `ier-literature-positioning` |
| causal or structural credibility is the bottleneck | `ier-identification` |
| the model, mechanism, or conceptual frame is loose | `ier-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `ier-robustness` |
| exhibits are hard to read or do not answer the question | `ier-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `ier-writing-style` |
| data, code, or computational documentation needs packaging | `ier-replication-package` |
| likely objections should be anticipated before submission | `ier-referee-strategy` |
| the paper is close to submission and needs a final preflight | `ier-submission` |
| a decision letter or referee report needs a response plan | `ier-rebuttal` |

## Default order

`ier-workflow → ier-topic-selection → ier-literature-positioning → ier-identification → ier-theory-model → ier-robustness → ier-tables-figures → ier-writing-style → ier-replication-package → ier-referee-strategy → ier-submission → ier-rebuttal`

## Journal-specific lenses
- Scope lens: general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach.
- Field vocabulary to keep visible: general-equilibrium discipline; structural clarity; international readership; theory-empirics balance; concise identification.
- Sibling boundary: QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review.
- Writing standard: formal economics argument with enough intuition for a broad journal audience.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating IER as interchangeable with QJE
- Treating IER as interchangeable with JPE
- Treating IER as interchangeable with REStud
- Using a generic top-five-economics or generic management template without the IER audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】International Economic Review
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one ier-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
