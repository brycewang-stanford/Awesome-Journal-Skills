---
name: jae-workflow
description: Use when deciding which jae-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Accounting and Economics (JAE) manuscript. Routes — it does not replace — the specialized skills.
---

# Journal of Accounting and Economics Workflow (jae-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jae-* skill to use right now** for your JAE manuscript.

Default assumption: unless the user says otherwise, treat the target as JAE — the Elsevier journal founded in **1979** by Ross L. Watts and Jerold L. Zimmerman (the originators of Positive Accounting Theory), published bimonthly (ISSN 0165-4101). JAE exists to **apply economic theory to explain accounting phenomena**: the role of accounting within the firm; the information content of accounting numbers in capital markets; accounting in financial contracting and the monitoring of agency relationships; the determination of accounting standards; and the regulation of corporate disclosure and the accounting profession. The non-negotiable bar is an **economics-based** argument tested with large-sample archival data (or built as an analytical model) — not normative, behavioral, or practitioner-oriented work. Editors desk-reject or redirect (Article Transfer Service) papers that miss this economics-relevance bar.

> Editorial team and policies change: verify the current masthead on ScienceDirect before naming editors or associate editors. The submission fee and Highlights/JEL requirements must be reconfirmed on the live Guide for Authors before upload.

## When to trigger

- "What should I do next?" with a half-built JAE manuscript
- You have a Compustat/CRSP result but no economics-based story for it
- A reviewer pushes on identification or on "what is the economic mechanism?"
- You received a JAE decision letter and need to switch into response mode
- You keep bouncing between theory, identification, and writing without a plan

## Routing table

| Current symptom                                                          | Next skill                  |
|--------------------------------------------------------------------------|-----------------------------|
| Idea is vague; unsure it is economics-based or JAE-fit (vs JAR/TAR/RAST) | `jae-topic-selection`       |
| Predictions are descriptive; no economic mechanism (agency/info/contracting) | `jae-theory-development` |
| Front end reads as gap-spotting; the economics literature not engaged    | `jae-literature-positioning`|
| Design may not identify the effect (endogeneity, selection, reverse causality) | `jae-methods`         |
| Have data; unsure about sample construction, FE, clustering, estimators  | `jae-data-analysis`         |
| Results exist but the "so what for accounting/economics" is thin         | `jae-contribution-framing`  |
| Tables overloaded, off Elsevier style, or not self-explanatory           | `jae-tables-figures`        |
| Prose is verbose, hedged, or buries the prediction                       | `jae-writing-style`         |
| Ready to submit; need the Editorial Manager + fee preflight              | `jae-submission`            |
| Want to understand JAE double-anonymized review before/after submit      | `jae-review-process`        |
| Received an R&R; need to plan and draft the response                     | `jae-rebuttal`              |

## Default order

1. `jae-topic-selection` — lock an economics-based question with JAE fit
2. `jae-theory-development` — specify the economic mechanism and derive predictions
3. `jae-literature-positioning` — engage the positive-accounting / economics conversation
4. `jae-methods` — design for identification (shocks, IV, DiD) matched to the prediction
5. `jae-data-analysis` — sample construction, fixed effects, two-way clustering, robustness
6. `jae-contribution-framing` — turn results into a contribution to accounting + economics
7. `jae-tables-figures` — finalize exhibits in Elsevier house style
8. `jae-writing-style` — full-manuscript prose polish
9. `jae-submission` — Editorial Manager preflight (anonymization, Highlights, JEL, fee)
10. `jae-review-process` — set expectations for double-anonymized, editor-final review
11. `jae-rebuttal` — after an R&R, plan revisions then draft the response letter

> `jae-tables-figures` and `jae-writing-style` are **late-stage polish**. Do not invoke them while the identification strategy or economic mechanism is still unsettled.

## Difference vs. JAR / TAR / RAST / JFE stacks

- **JAE**: economics-based positive accounting; Watts-Zimmerman tradition; voluntary Elsevier data-sharing default; fee-bearing submission; double-anonymized; editor-final model.
- **JAR** (Chicago/Wiley): also top-3 archival, but **mandates** a replication/code package.
- **TAR** (AAA flagship): broader methodological tent (experimental, analytical, archival).
- **RAST** (Review of Accounting Studies): archival capital-markets, often valuation-focused.
- **JFE** (finance): mandates a Mendeley Data code/data deposit — a sharper open-science bar than JAE.

If your paper is normative, behavioral-experimental, or practitioner-facing, JAE is the wrong venue.

## Anti-patterns

- **Do not** skip `jae-theory-development` and submit a "Compustat correlation" with no economic mechanism.
- **Do not** let `jae-tables-figures` beautify exhibits before identification is settled.
- **Do not** let `jae-rebuttal` draft a response before the manuscript is actually revised.
- **Do not** treat `jae-writing-style` as a substitute for identification — polish cannot rescue endogeneity.
