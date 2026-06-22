---
name: pom-workflow
description: Use when deciding which pom-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Production and Operations Management (POM) manuscript. Routes — it does not replace — the specialized skills, and it identifies your method track (analytical / empirical / behavioral / data-science).
---

# Production and Operations Management Workflow (pom-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which pom-* skill to use right now** for your POM manuscript.

Default assumption: unless told otherwise, the target is **Production and Operations Management (POM)** — the flagship journal of the Production and Operations Management Society (POMS), published by SAGE since January 2024 (previously Wiley-Blackwell), ISSN 1059-1478, twelve issues per year, founded and edited by Kalyan Singhal (University of Baltimore). POM accepts the **full breadth of operations management** — analytical/mathematical modeling, empirical OM, behavioral/experimental OM, and operations data science — and routes every paper to one of many named **Departments** (Behavioral Operations, Supply Chain Management, Healthcare Operations, Sustainable Operations, Operations Management Data Analytics, plus interface departments). The non-negotiable bar: the work must be of **significant interest to practicing operations managers** *and* make a **substantial contribution to knowledge and practice**, executed rigorously by whatever method fits.

> Editors (verified 2026-06-22 via POMS / SAGE): **Kalyan Singhal** is founder & Editor-in-Chief and **Subodha Kumar** is Co-Editor-in-Chief; the department roster and Department Editors rotate. Verify the live masthead and departments at poms.org/journal. POM is hybrid open access on SAGE; the optional Sage Choice/open-access APC and any data-deposit mandate are **待核实** — see `resources/official-source-map.md`.

## When to trigger

- "What should I do next?" with a half-built POM manuscript
- You have a model or dataset but no clear managerial insight
- You are unsure which Department your paper belongs to
- You received a POM decision letter and need to switch into response mode
- You keep bouncing between model, analysis, and writing without a plan

## Routing table

| Current symptom                                                        | Next skill                  |
|------------------------------------------------------------------------|-----------------------------|
| Idea is vague; unclear if it is OM and POM-fit; no target Department   | `pom-topic-selection`       |
| Model/hypotheses lack a clear mechanism, assumptions, or propositions  | `pom-theory-development`    |
| Front end reads as gap-spotting; wrong department's literature engaged | `pom-literature-positioning`|
| Method may not match the question (model vs data vs experiment)        | `pom-methods`               |
| Have proofs/data; unsure about numerics, identification, robustness    | `pom-data-analysis`         |
| Results exist but the "so what for the operations manager" is thin     | `pom-contribution-framing`  |
| Exhibits cluttered, not self-explanatory, or off house style          | `pom-tables-figures`        |
| Prose buries the argument; over the 32-page cap                        | `pom-writing-style`         |
| Ready to submit; need the ScholarOne + department preflight            | `pom-submission`            |
| Want to understand POM department review before/after submit           | `pom-review-process`        |
| Received an R&R; need to plan and draft the response                   | `pom-rebuttal`              |

## Default order

1. `pom-topic-selection` — lock an OM question, POM fit, and target Department
2. `pom-theory-development` — build the model/mechanism; derive propositions or hypotheses
3. `pom-literature-positioning` — engage the right department's prior OM work
4. `pom-methods` — match method (optimization/stochastic/game-theory/empirical/behavioral/ML)
5. `pom-data-analysis` — execute proofs and numerics, or identification, estimation, robustness
6. `pom-contribution-framing` — turn results into a managerial-and-knowledge contribution
7. `pom-tables-figures` — finalize exhibits (result tables, comparative-statics plots, schematics)
8. `pom-writing-style` — full-manuscript polish; enforce 32-page cap and e-companion split
9. `pom-submission` — ScholarOne preflight (department routing, double-blind, same-data disclosure)
10. `pom-review-process` — set expectations; understand the no-resubmission rule
11. `pom-rebuttal` — after an R&R, revise then draft the point-by-point response

> `pom-tables-figures` and `pom-writing-style` are **late-stage polish**. Do not invoke them while the model, identification, or managerial insight is still unsettled.

## Decision shortcuts

- "I have an elegant model but no managerial takeaway" → `pom-topic-selection` then `pom-contribution-framing`
- "Which department do I submit to?" → `pom-topic-selection`
- "My intro says 'no one has modeled X'" (gap-spotting) → `pom-literature-positioning`
- "Reviewer says insight is not relevant to practice" → `pom-contribution-framing`
- "I am 6 pages over the 32-page cap" → `pom-writing-style` (move proofs to the e-companion)
- "I was rejected — can I resubmit to another department?" → `pom-review-process` (almost never)

## Difference vs. M&SOM / Management Science / JOM stacks

- **POM**: POMS/SAGE flagship; department-routed; rigor *and* practicing-manager relevance weighted together; 32-page cap with an unlimited online e-companion.
- **M&SOM / Management Science** (INFORMS): different limits and norms; not department-letter-routed the same way.
- **JOM / IJOPM**: often more empirical/process-oriented; different publishers and formats.

## Anti-patterns

- **Do not** submit without choosing a Department — misrouting wastes a cycle.
- **Do not** let `pom-tables-figures` beautify exhibits before the model is settled.
- **Do not** treat polish as a substitute for managerial relevance — POM's practice gate cannot be styled away.
- **Do not** plan a resubmission of a rejected paper to another department; it is barred unless explicitly invited.
