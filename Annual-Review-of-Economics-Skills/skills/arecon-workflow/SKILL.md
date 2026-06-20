---
name: arecon-workflow
description: Use when deciding which arecon-* sub-skill to invoke next for a Annual Review of Economics manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (arecon-workflow)

## Overview

This router sequences the twelve-skill stack for **Annual Review of Economics (AREcon)**. The journal's center of gravity is commissioned review articles synthesizing major areas of economics for specialists and adjacent economists. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Annual Reviews; submission route to re-check live: Annual Reviews editorial process. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at AREcon and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing AREcon with nearby venues: Journal of Economic Literature, Journal of Economic Perspectives, Handbook chapters, and Academy of Management Annals.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `arecon-topic-selection` |
| a review proposal or commissioned-article pitch needs shape | `arecon-proposal-framing` |
| coverage of the literature is uneven or unsystematic | `arecon-literature-synthesis` |
| the draft reads like a list rather than an argument | `arecon-organizing-framework` |
| evidence quality, causal weight, or balance needs discipline | `arecon-evidence-standards` |
| exhibits are hard to read or do not answer the question | `arecon-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `arecon-writing-style` |
| editor-facing scope and revision strategy needs alignment | `arecon-editor-strategy` |
| the paper is close to submission and needs a final preflight | `arecon-submission` |
| review-cycle expectations and revision choreography need planning | `arecon-review-process` |
| editor/referee feedback on a review article needs synthesis | `arecon-revision` |

## Default order

`arecon-workflow → arecon-topic-selection → arecon-proposal-framing → arecon-literature-synthesis → arecon-organizing-framework → arecon-evidence-standards → arecon-tables-figures → arecon-writing-style → arecon-editor-strategy → arecon-submission → arecon-review-process → arecon-revision`

## Journal-specific lenses
- Scope lens: commissioned review articles synthesizing major areas of economics for specialists and adjacent economists.
- Field vocabulary to keep visible: field synthesis; research frontier; conceptual map; evidence stocktake; future agenda.
- Sibling boundary: Journal of Economic Literature, Journal of Economic Perspectives, Handbook chapters, and Academy of Management Annals.
- Writing standard: agenda-setting synthesis that clarifies what the field knows, disputes, and should do next.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating AREcon as interchangeable with Journal of Economic Literature
- Treating AREcon as interchangeable with Journal of Economic Perspectives
- Treating AREcon as interchangeable with Handbook chapters
- Using a generic top-five-economics or generic management template without the AREcon audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Annual Review of Economics
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one arecon-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
