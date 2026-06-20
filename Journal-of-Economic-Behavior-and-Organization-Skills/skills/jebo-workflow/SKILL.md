---
name: jebo-workflow
description: Use when deciding which jebo-* sub-skill to invoke next for a Journal of Economic Behavior and Organization manuscript. Routes the workflow; it does not replace the specialized skills.
---

# Workflow Router (jebo-workflow)

## Overview

This router sequences the twelve-skill stack for **Journal of Economic Behavior and Organization (JEBO)**. The journal's center of gravity is behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings. Use the router to decide the next skill, not to replace specialist review.

Publisher / platform notes checked for this pack: Elsevier; submission route to re-check live: Editorial Manager / Elsevier submission. Volatile facts are treated as `检索于 2026-06；以官网为准`.

## When to trigger
- A manuscript is being aimed at JEBO and the next bottleneck is unclear.
- A draft is moving between framing, design, evidence, exhibits, and submission checks.
- A decision letter arrived and you need to choose between revision strategy and rebuttal drafting.
- The team is comparing JEBO with nearby venues: Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics.

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| scope, audience, or outlet fit is uncertain | `jebo-topic-selection` |
| the contribution relative to adjacent journals is fuzzy | `jebo-literature-positioning` |
| causal or structural credibility is the bottleneck | `jebo-identification` |
| the model, mechanism, or conceptual frame is loose | `jebo-theory-model` |
| results may be specification-, sample-, or inference-sensitive | `jebo-robustness` |
| exhibits are hard to read or do not answer the question | `jebo-tables-figures` |
| the introduction, abstract, or prose misses the journal voice | `jebo-writing-style` |
| data, code, or computational documentation needs packaging | `jebo-replication-package` |
| likely objections should be anticipated before submission | `jebo-referee-strategy` |
| the paper is close to submission and needs a final preflight | `jebo-submission` |
| a decision letter or referee report needs a response plan | `jebo-rebuttal` |

## Default order

`jebo-workflow → jebo-topic-selection → jebo-literature-positioning → jebo-identification → jebo-theory-model → jebo-robustness → jebo-tables-figures → jebo-writing-style → jebo-replication-package → jebo-referee-strategy → jebo-submission → jebo-rebuttal`

## Journal-specific lenses
- Scope lens: behavioral economics, organization, institutions, experiments, and decision-making outside frictionless textbook settings.
- Field vocabulary to keep visible: behavioral mechanism; institutional setting; laboratory evidence; field-experiment design; organizational incentives.
- Sibling boundary: Experimental Economics, Games and Economic Behavior, Management Science, and Journal of Public Economics.
- Writing standard: mechanism-forward behavioral evidence with transparent experimental or institutional design.
- Source discipline: quote only facts that are in `resources/official-source-map.md` or clearly marked 待核实.

## Anti-patterns
- Treating JEBO as interchangeable with Experimental Economics
- Treating JEBO as interchangeable with Games and Economic Behavior
- Treating JEBO as interchangeable with Management Science
- Using a generic top-five-economics or generic management template without the JEBO audience.
- Polishing prose before the design, contribution, and evidence hierarchy are stable.
- Letting the appendix carry claims that the main text must establish.

## Output format

```text
【Target】Journal of Economic Behavior and Organization
【Current bottleneck】fit / contribution / design / evidence / exhibits / style / submission / revision
【Next skill】<one jebo-* skill>
【Reason】why this step is the binding constraint
【Source check】official facts verified or marked 待核实
```
