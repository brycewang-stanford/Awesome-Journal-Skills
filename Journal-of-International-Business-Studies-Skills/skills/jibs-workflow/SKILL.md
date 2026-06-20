---
name: jibs-workflow
description: Use when deciding which jibs-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of International Business Studies (JIBS) manuscript. Routes — it does not replace — the specialized skills.
---

# Journal of International Business Studies Workflow (jibs-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jibs-* skill to use right now** for your JIBS manuscript.

Default assumption: unless the user says otherwise, treat the target as JIBS — the flagship, top-ranked *international-business* journal, established 1970, published by Palgrave Macmillan (Springer Nature) on behalf of the **Academy of International Business (AIB)**, of which it is the official journal. JIBS studies cross-border, multi-country, and **multilevel** phenomena: MNEs, internationalization, cross-cultural management, international strategy/finance/economics, and global political economy, with **country and culture treated as explicit levels of analysis**. The non-negotiable bar: a manuscript must address a real-world international-business **phenomenon, problem, or puzzle** and state explicitly what it contributes to **IB theory** — incremental single-country extensions are discouraged. JIBS is paradigmatically and methodologically **pluralistic** (quantitative, qualitative, mixed, theory); rigor and a clear IB theoretical contribution are the gatekeepers, not any one method.

> Editorial team context: Rosalie L. Tung (Simon Fraser University) is the current Editor in Chief on the Springer journal home and editorial-board page, with Anne Hoekman listed as Managing Editor. The submission route is the JIBS online tool at mc.manuscriptcentral.com; optional gold open access is priced on the Springer "How to publish with us" page.

## When to trigger

- "What should I do next?" with a half-built JIBS manuscript
- You have cross-country data and a result but no clear IB theoretical story
- A reviewer/editor pushes on "phenomenon" or "contribution to IB theory"
- You received a JIBS decision letter (R&R or reject) and need to switch into response mode
- You keep bouncing between theory, cross-national measurement, and writing without a plan

## Routing table

| Current symptom                                                            | Next skill                  |
|----------------------------------------------------------------------------|-----------------------------|
| Idea is vague; not sure it is a real IB phenomenon or JIBS-fit              | `jibs-topic-selection`      |
| Hypotheses ignore country/culture levels or lack an IB mechanism           | `jibs-theory-development`   |
| Front end reads as gap-spotting; the IB conversation is not engaged        | `jibs-literature-positioning`|
| Design may not match a cross-country/multilevel claim                       | `jibs-methods`              |
| Have data; unsure about measurement equivalence, CMV, endogeneity, models  | `jibs-data-analysis`        |
| Results exist but the "so what for IB theory" is thin                      | `jibs-contribution-framing` |
| Exhibits not self-explanatory or off the JIBS Style Guide                  | `jibs-tables-figures`       |
| Prose buries the phenomenon or the contribution                            | `jibs-writing-style`        |
| Ready to submit; need the Springer Nature / DART preflight                 | `jibs-submission`           |
| Want to understand JIBS double-blind review/decisions before/after submit  | `jibs-review-process`       |
| Received an R&R; need to plan and draft the response                       | `jibs-rebuttal`             |

## Default order

1. `jibs-topic-selection` — lock a phenomenon-driven, JIBS-fit question
2. `jibs-theory-development` — build the cross-level IB mechanism and derive hypotheses
3. `jibs-literature-positioning` — engage the IB conversation; state what you join
4. `jibs-methods` — match a cross-country/multilevel design to the question
5. `jibs-data-analysis` — measurement equivalence, CMV, endogeneity, the right estimator
6. `jibs-contribution-framing` — turn results into an explicit IB theoretical contribution
7. `jibs-tables-figures` — finalize main exhibits per the JIBS Style Guide
8. `jibs-writing-style` — full-manuscript prose polish (phenomenon-forward, author-date)
9. `jibs-submission` — Springer Nature preflight (anonymization, DART/DAS, format, files)
10. `jibs-review-process` — set expectations for the double-blind, multi-round process
11. `jibs-rebuttal` — after an R&R, plan revisions then draft the response letter

> `jibs-tables-figures` and `jibs-writing-style` are **late-stage polish**. Do not invoke them while the phenomenon, IB contribution, or identification is still unsettled.

## Decision shortcuts

- "I have a finding but no IB theory story" → `jibs-topic-selection` then `jibs-theory-development`
- "My intro says 'no one has studied X in country Y'" (gap-spotting) → `jibs-literature-positioning`
- "Single-country sample" → `jibs-topic-selection` (is this really IB?) then `jibs-methods`
- "Same-respondent survey across countries" → `jibs-data-analysis` (CMV + measurement equivalence)
- "Internationalization-as-process, regressor may be endogenous" → `jibs-methods` then `jibs-data-analysis`
- "Reviewer cites a 'From the Editors' methods editorial" → `jibs-data-analysis`
- "Submitting this week" → `jibs-submission`
- "Got an R&R with area editor + reviewers" → `jibs-review-process` then `jibs-rebuttal`

## Difference vs. AMJ / SMJ / IB-adjacent stacks

- **JIBS**: international business — the contribution must be to *IB* theory and engage cross-border/multilevel phenomena; AIB's official journal; methodologically pluralistic; DART transparency regime.
- **AMJ**: general empirical management (often single-country); empirical *and* theoretical contribution; AOM journal.
- **SMJ**: strategy/performance questions; not specifically cross-border or culture-as-level.
- **JWB / Management International Review / GSJ**: IB-adjacent, but JIBS sets the field's bar for phenomenon-based rigor and cross-national validity.

If your study has no genuine cross-border, multi-country, or culture/country-as-level dimension, JIBS is likely the wrong venue.

## Anti-patterns

- **Do not** skip `jibs-theory-development` and jump to analysis — JIBS rejects atheoretical, phenomenon-free work.
- **Do not** treat a single-country convenience sample as "international" without theorizing country/culture.
- **Do not** let `jibs-tables-figures` beautify exhibits before the model and contribution are settled.
- **Do not** let `jibs-rebuttal` draft a response letter before you have actually revised the manuscript.
