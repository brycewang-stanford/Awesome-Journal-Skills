---
name: worlddev-workflow
description: Use when deciding which worlddev-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a World Development (WD) submission. Routes — it does not replace — the specialized skills.
---

# World Development Workflow Router (worlddev-workflow)

## Overview

This is the router. It tells you **which worlddev-* skill to use at the current stage** of a manuscript aimed at *World Development* (WD) — the **multidisciplinary** development-studies journal published by **Elsevier** (founded 1973, monthly, ISSN 0305-750X / online 1873-5991). WD's defining feature, and the thing every routing decision must respect, is that it is **methodologically pluralist**: it publishes econometric and experimental work, but equally qualitative case studies, process tracing, ethnography, participatory methods, political-economy analysis, and policy/practice papers. The shared bar is **real-world development relevance** in low- and middle-income contexts — poverty, inequality, livelihoods, institutions, governance, aid and NGOs, agriculture and food security, health and education, conflict, gender, and environment-development.

The single biggest router mistake is treating WD as if it were an econometrics journal. It is not. Route a regression-discontinuity paper and a multi-site qualitative study through the same chain, but enter the chain at different links and apply a different bar for "credible evidence." Editors as of 2026: **Jampel Dell'Angelo and Angelika Rettberg** (检索于 2026-06；以官网为准). Review is **double-anonymized**; submission is via **Elsevier Editorial Manager**; abstract **≤250 words**, **3–6 keywords**.

## When to trigger

- The user asks "what should I do next?" on a WD-targeted draft
- A draft is ping-ponging between framing, evidence, exhibits, and submission checks
- The contribution is unclear relative to siblings (JDE, WBER, JDS, EDCC)
- A WD decision letter arrived and the user needs to switch into revision mode
- A quantitatively-trained author has a qualitative or mixed-methods paper and is unsure how WD will judge it

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/audience/outlet fit uncertain; is this WD or a sibling? | `worlddev-topic-selection` |
| Contribution vs. the development literature is fuzzy or undersold | `worlddev-literature-positioning` |
| Causal claim rests on OLS+controls; or a qual/mixed claim lacks an inference logic | `worlddev-identification` |
| The conceptual/analytical framework (development theory) is loose or decorative | `worlddev-theory-model` |
| Results may be specification-, sample-, measurement-, or interpretation-sensitive | `worlddev-robustness` |
| Exhibits dense; significance asterisks present; maps/qual evidence underused | `worlddev-tables-figures` |
| Prose is jargon-heavy and does not reach a multidisciplinary, policy audience | `worlddev-writing-style` |
| Data/code deposit, qualitative-transparency, or anonymization for review | `worlddev-replication-package` |
| Likely double-anonymized referee objections should be pre-empted | `worlddev-referee-strategy` |
| Close to submission; need the Editorial Manager preflight | `worlddev-submission` |
| An R&R or reject-and-resubmit arrived; need a response-letter plan | `worlddev-rebuttal` |

## Default order

1. `worlddev-topic-selection` — lock the development question and WD-vs-sibling fit
2. `worlddev-literature-positioning` — stake the contribution across disciplines
3. `worlddev-identification` — causal design OR the inference logic of a qual/mixed paper
4. `worlddev-theory-model` — the conceptual/analytical framework that organizes the evidence
5. `worlddev-robustness` — sensitivity (quant) or trustworthiness/triangulation (qual)
6. `worlddev-tables-figures` — exhibits, maps, and qualitative displays without asterisks
7. `worlddev-writing-style` — reach the multidisciplinary reader (abstract + intro last)
8. `worlddev-replication-package` — Elsevier data policy + qualitative transparency
9. `worlddev-referee-strategy` — anticipate double-anonymized objections
10. `worlddev-submission` — Editorial Manager preflight
11. `worlddev-rebuttal` — after the decision letter

> Writing-style is late-stage polish; do not rewrite the intro before the framework and evidence settle.

## Routing by paper archetype

The binding constraint differs by what kind of paper this is. Read the archetype, then enter at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Quantitative causal (DID, IV, RDD, RCT) | credible design + clustering at the right level | `worlddev-identification` |
| Qualitative (cases, process tracing, ethnography) | inference logic + transparency, not "more N" | `worlddev-identification` → `worlddev-theory-model` |
| Mixed-methods | integration — how strands actually combine, not run in parallel | `worlddev-theory-model` → `worlddev-identification` |
| Political-economy / institutional analysis | conceptual framework doing real analytical work | `worlddev-theory-model` |
| Policy / practice / aid-effectiveness | "so what for whom" + external validity | `worlddev-topic-selection` → `worlddev-writing-style` |

## Anti-patterns

- Treating WD as interchangeable with **Journal of Development Economics** (rigorous development econometrics) — WD values relevance and methodological breadth, not only identification rigor
- Treating WD as **World Bank Economic Review** (Bank-affiliated, more economics-centric) or **Journal of Development Studies** (interdisciplinary but more political/sociological framing)
- Routing a qualitative paper as if "weak identification" were the problem when the real problem is an unstated inference logic
- Polishing prose before the framework, evidence hierarchy, and contribution are stable
- Letting an appendix carry claims the main text must establish

## Output format

```text
【Target】World Development (WD)
【Archetype】quant-causal / qualitative / mixed / political-economy / policy-practice
【Current bottleneck】fit / contribution / design / framework / evidence / exhibits / style / replication / submission / revision
【Next skill】<one worlddev-* skill>
【Reason】why this is the binding constraint for THIS archetype
【Source check】official facts verified or marked 待核实
```
