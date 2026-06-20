---
name: respol-workflow
description: Use when deciding which respol-* sub-skill to invoke next for a Research Policy manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (respol-workflow)

## Overview

This router sequences the twelve-skill stack for **Research Policy (Research Policy)**. The journal's center of gravity is innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at Research Policy and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing Research Policy with nearby venues: Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `respol-topic-selection` |
| the management-theory contribution is underdeveloped | `respol-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `respol-literature-positioning` |
| methods and construct validity need alignment | `respol-methods` |
| analysis design, estimation, or qualitative coding needs review | `respol-data-analysis` |
| the theoretical contribution needs sharper positioning | `respol-contribution-framing` |
| exhibits are hard to read or do not answer the question | `respol-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `respol-writing-style` |
| the paper is close to submission and needs a final preflight | `respol-submission` |
| review-cycle expectations and revision choreography need planning | `respol-review-process` |
| a decision letter or referee report needs a response plan | `respol-rebuttal` |

## Default order

`respol-workflow → respol-topic-selection → respol-theory-development → respol-literature-positioning → respol-methods → respol-data-analysis → respol-contribution-framing → respol-tables-figures → respol-writing-style → respol-submission → respol-review-process → respol-rebuttal`

## Journal-specific lenses
- Scope lens: innovation, science policy, technology management, entrepreneurship, R&D, and knowledge production.
- Field vocabulary to keep visible: innovation system; science policy; patent evidence; R&D organization; technology diffusion.
- Sibling boundary: Strategic Management Journal, Management Science, Industrial and Corporate Change, and Journal of Business Venturing.
- Writing standard: innovation-policy argument linking mechanisms, institutions, and technology evidence.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating Research Policy as interchangeable with Strategic Management Journal
- Treating Research Policy as interchangeable with Management Science
- Treating Research Policy as interchangeable with Industrial and Corporate Change
- Using a generic top-five-economics or generic management template without the Research Policy audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Research Policy
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one respol-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
