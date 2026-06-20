---
name: amann-workflow
description: Use when deciding which amann-* sub-skill to invoke next for a Academy of Management Annals manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (amann-workflow)

## Overview

This router sequences the twelve-skill stack for **Academy of Management Annals (Annals)**. The journal's center of gravity is commissioned and high-level reviews that synthesize management and organization research. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Academy of Management / Taylor & Francis; submission route to re-check live: Academy of Management submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at Annals and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing Annals with nearby venues: Academy of Management Review, Journal of Management, Journal of Management Studies, and Annual Review outlets.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `amann-topic-selection` |
| a review proposal or commissioned-article pitch needs shape | `amann-proposal-framing` |
| coverage of the literature is uneven or unsystematic | `amann-literature-synthesis` |
| the draft reads like a list rather than an argument | `amann-organizing-framework` |
| evidence quality, causal weight, or balance needs discipline | `amann-evidence-standards` |
| exhibits are hard to read or do not answer the question | `amann-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `amann-writing-style` |
| editor-facing scope and revision strategy needs alignment | `amann-editor-strategy` |
| the paper is close to submission and needs a final preflight | `amann-submission` |
| review-cycle expectations and revision choreography need planning | `amann-review-process` |
| editor/referee feedback on a review article needs synthesis | `amann-revision` |

## Default order

`amann-workflow → amann-topic-selection → amann-proposal-framing → amann-literature-synthesis → amann-organizing-framework → amann-evidence-standards → amann-tables-figures → amann-writing-style → amann-editor-strategy → amann-submission → amann-review-process → amann-revision`

## Journal-specific lenses
- Scope lens: commissioned and high-level reviews that synthesize management and organization research.
- Field vocabulary to keep visible: integrative review; theory synthesis; agenda setting; management field map; conceptual reconciliation.
- Sibling boundary: Academy of Management Review, Journal of Management, Journal of Management Studies, and Annual Review outlets.
- Writing standard: field-defining synthesis that reorganizes theory rather than merely cataloging papers.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating Annals as interchangeable with Academy of Management Review
- Treating Annals as interchangeable with Journal of Management
- Treating Annals as interchangeable with Journal of Management Studies
- Using a generic top-five-economics or generic management template without the Annals audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Academy of Management Annals
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one amann-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
