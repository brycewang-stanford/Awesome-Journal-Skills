---
name: jais-workflow
description: Use when deciding which jais-* sub-skill to invoke next for a Journal of the Association for Information Systems manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jais-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of the Association for Information Systems (JAIS)**. The journal's center of gravity is information systems theory, digital innovation, sociotechnical systems, methods, and cumulative IS scholarship. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Association for Information Systems; submission route to re-check live: AIS eLibrary / journal submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JAIS and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JAIS with nearby venues: MIS Quarterly, Information Systems Research, JMIS, and Management Science.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jais-topic-selection` |
| the management-theory contribution is underdeveloped | `jais-theory-development` |
| the contribution relative to adjacent journals is fuzzy | `jais-literature-positioning` |
| methods and construct validity need alignment | `jais-methods` |
| analysis design, estimation, or qualitative coding needs review | `jais-data-analysis` |
| the theoretical contribution needs sharper positioning | `jais-contribution-framing` |
| exhibits are hard to read or do not answer the question | `jais-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jais-writing-style` |
| the paper is close to submission and needs a final preflight | `jais-submission` |
| review-cycle expectations and revision choreography need planning | `jais-review-process` |
| a decision letter or referee report needs a response plan | `jais-rebuttal` |

## Default order

`jais-workflow → jais-topic-selection → jais-theory-development → jais-literature-positioning → jais-methods → jais-data-analysis → jais-contribution-framing → jais-tables-figures → jais-writing-style → jais-submission → jais-review-process → jais-rebuttal`

## Journal-specific lenses
- Scope lens: information systems theory, digital innovation, sociotechnical systems, methods, and cumulative IS scholarship.
- Field vocabulary to keep visible: sociotechnical system; IS theory; digital innovation; methodological pluralism; cumulative contribution.
- Sibling boundary: MIS Quarterly, Information Systems Research, JMIS, and Management Science.
- Writing standard: theory-forward IS research with method fit and clear community contribution.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JAIS as interchangeable with MIS Quarterly
- Treating JAIS as interchangeable with Information Systems Research
- Treating JAIS as interchangeable with JMIS
- Using a generic top-five-economics or generic management template without the JAIS audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of the Association for Information Systems
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jais-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
