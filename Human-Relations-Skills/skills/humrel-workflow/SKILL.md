---
name: humrel-workflow
description: Use when deciding which humrel-* sub-skill to invoke next for a Human Relations manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (humrel-workflow)

## Overview

This router sequences the twelve-skill stack for **Human Relations (Human Relations)**. The journal's center of gravity is work, employment, organizations, social relations, power, identity, and critical management. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: SAGE for the Tavistock Institute; submission route to re-check live: SAGE / ScholarOne submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at Human Relations and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing Human Relations with nearby venues: Organization Studies, Journal of Management Studies, Administrative Science Quarterly, and Work Employment and Society.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `humrel-topic-selection` |
| the management-theory contribution is underdeveloped | `humrel-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `humrel-literature-positioning` |
| methods and construct validity need alignment | `humrel-methods` |
| analysis design, estimation, or qualitative coding needs review | `humrel-data-analysis` |
| the theoretical contribution needs sharper positioning | `humrel-contribution-framing` |
| exhibits are hard to read or do not answer the question | `humrel-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `humrel-writing-style` |
| the paper is close to submission and needs a final preflight | `humrel-submission` |
| review-cycle expectations and revision choreography need planning | `humrel-review-process` |
| a decision letter or referee report needs a response plan | `humrel-rebuttal` |

## Default order

`humrel-workflow → humrel-topic-selection → humrel-theory-development → humrel-literature-positioning → humrel-methods → humrel-data-analysis → humrel-contribution-framing → humrel-tables-figures → humrel-writing-style → humrel-submission → humrel-review-process → humrel-rebuttal`

## Journal-specific lenses
- Scope lens: work, employment, organizations, social relations, power, identity, and critical management.
- Field vocabulary to keep visible: workplace relation; power and identity; employment institution; qualitative insight; social theory.
- Sibling boundary: Organization Studies, Journal of Management Studies, Administrative Science Quarterly, and Work Employment and Society.
- Writing standard: socially grounded organization research that links theory, context, and lived work.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating Human Relations as interchangeable with Organization Studies
- Treating Human Relations as interchangeable with Journal of Management Studies
- Treating Human Relations as interchangeable with Administrative Science Quarterly
- Using a generic top-five-economics or generic management template without the Human Relations audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Human Relations
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one humrel-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
