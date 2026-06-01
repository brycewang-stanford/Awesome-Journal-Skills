---
name: jom-workflow
description: Use when deciding which jom-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Operations Management (JOM) submission. Routes — it does not replace — the specialized skills.
---

# Journal of Operations Management Workflow (jom-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jom-* skill to use right now** for your JOM manuscript.

Default assumption: unless the user says otherwise, treat the target as **JOM** — the flagship outlet for *original, empirical* operations and supply chain management research, published by **Wiley on behalf of the Association for Supply Chain Management (ASCM, formerly APICS)**, established 1980, eight issues a year, on the FT50 list. JOM's defining bar is that **operations must be at the heart of the research question, not just in the context**, and the work must be empirical — "it is the observation that renders the research empirical." JOM explicitly does **not** publish purely analytical models or optimization techniques ("these belong in operations research, industrial engineering, or analytical OM journals"). Reviewers and Department Editors ask "is the operations phenomenon real and observed?" as insistently as "is the theory advanced?"

> Editorial structure: Co-Editors-in-Chief Elliot Bendoly (Ohio State) and Rogelio Oliva (Texas A&M); the journal routes every submission to one of **12 Departments**, each with its own Department Editors. Verify the current masthead and roster before relying on names. Fees, the APC, abstract limit, and exact length rules change — confirm on the ASCM/JOM and Wiley pages (some are 待核实 in `resources/official-source-map.md`).

## When to trigger

- "What should I do next?" with a half-built empirical OM manuscript
- You have operational data and a result but no clear OM-theoretic story
- A reviewer/Department Editor pushes on "is operations really the heart of this?" and you are unsure which stage is the bottleneck
- You received a JOM decision letter (R&R or reject-and-resubmit) and need to switch into response mode
- You are unsure which of the 12 Departments should route your paper

## Routing table

| Current symptom                                                              | Next skill                  |
|------------------------------------------------------------------------------|-----------------------------|
| Idea is vague; unclear if operations is the heart and if it is JOM-fit       | `jom-topic-selection`       |
| Hypotheses are descriptive; no OM mechanism (behavioral/operational logic)   | `jom-theory-development`    |
| Front end reads as a gap; the OM/SCM conversation is not engaged             | `jom-literature-positioning`|
| Design may not match (survey vs archival vs field vs experiment vs IBR)      | `jom-methods`               |
| Have data; unsure about measurement, CMB, endogeneity, estimator            | `jom-data-analysis`         |
| Results exist but the "so what for OM theory and practice" is thin           | `jom-contribution-framing`  |
| Tables/figures cluttered, off APA/house style, or not self-explanatory       | `jom-tables-figures`        |
| Prose is jargon-heavy, passive, or buries the operations argument            | `jom-writing-style`         |
| Ready to submit; need Department routing, cover-letter protocol, checklist   | `jom-submission`            |
| Want to understand the asymmetric double-anonymous review before/after submit| `jom-review-process`        |
| Received an R&R; need to plan and draft the point-by-point response          | `jom-rebuttal`              |

## Default order

`jom-topic-selection → jom-theory-development → jom-literature-positioning → jom-methods → jom-data-analysis → jom-contribution-framing → jom-tables-figures → jom-writing-style → jom-submission → jom-review-process → jom-rebuttal`

## Output format

```
【Stage detected】...
【Why】(operations-as-heart? empirical? theory advance?) ...
【Use this skill next】jom-<role>
【After that】...
```
