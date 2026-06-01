---
name: jar-workflow
description: Use when deciding which jar-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Accounting Research (JAR) manuscript. Routes — it does not replace — the specialized skills.
---

# Journal of Accounting Research Workflow (jar-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which jar-* skill to use right now** for your JAR manuscript.

Default assumption: unless the user says otherwise, treat the target as the **Journal of Accounting Research (JAR)** — one of the "top three" accounting journals, founded in 1963, sponsored by the **Chookaszian Accounting Research Center at the University of Chicago Booth School of Business** and published with Wiley-Blackwell (five issues a year). JAR publishes original research in all areas of accounting drawing on finance, economics, statistics, psychology, and sociology, using analytical, empirical-archival, experimental, and field-study methods. Its defining identity is rigorous **empirical-archival capital-markets** research in the **Ball-Brown** lineage. The non-negotiable bar: a clean **identification** strategy answering a question that matters for how accounting information is produced, disclosed, audited, or used in markets — credible causal inference and an economic story weigh as heavily as a sound regression.

> Governance is by a panel of **Senior Editors** (Berger, Costello, Hail, Nikolaev, Sapra, van Lent, Wittenberg Moerman), not a single editor-in-chief; Editorial Manager Lisa M. Heiberger. Fees, the conference theme, and the masthead change — verify on the Chookaszian Center JAR pages. Three things make JAR distinctive: a **tiered submission fee** ($750/$500/$50), a **mandatory data-and-code sharing policy**, and the **Ray Ball JAR Annual Conference** with its June conference issue. Impact factor (~4.9, 2023) is **approximate**.

## When to trigger

- "What should I do next?" with a half-built JAR manuscript
- You have an archival result but no clean identification or economic story
- A referee pushes on endogeneity, the channel, or "what do we learn about accounting?"
- You received a JAR decision letter (R&R or reject) and need to switch into response mode
- You are weighing the **Registered Reports** track or a **Ray Ball Conference** submission

## Routing table

| Current symptom                                                          | Next skill                  |
|--------------------------------------------------------------------------|-----------------------------|
| Idea is vague; unsure it is a real accounting question or JAR-fit        | `jar-topic-selection`       |
| No economic mechanism; predictions are atheoretical correlations         | `jar-theory-development`    |
| Front end reads as gap-spotting; the accounting literature not engaged   | `jar-literature-positioning`|
| Design/identification may not support the causal claim                   | `jar-methods`               |
| Have data; unsure about clustering, endogeneity, measurement of constructs | `jar-data-analysis`       |
| Results exist but "so what for accounting" is thin                        | `jar-contribution-framing`  |
| Tables/figures cluttered, off house style, or not self-explanatory       | `jar-tables-figures`        |
| Prose buries the research design and the economic argument               | `jar-writing-style`         |
| Ready to submit; need the Research Exchange + fee + data/code preflight   | `jar-submission`            |
| Want to understand JAR review, fees, or the conference/RR tracks          | `jar-review-process`        |
| Received an R&R; need to plan revisions and draft the response            | `jar-rebuttal`              |

## Default order

1. `jar-topic-selection` — lock an accounting question with a credible setting and JAR fit
2. `jar-theory-development` — build the economic mechanism and sign the predictions
3. `jar-literature-positioning` — engage the accounting conversation; state the marginal contribution
4. `jar-methods` — choose the identification strategy and the sample/setting
5. `jar-data-analysis` — clustering, endogeneity, construct measurement, robustness
6. `jar-contribution-framing` — turn the estimate into a contribution to accounting knowledge
7. `jar-tables-figures` — finalize the main descriptive/results/identification exhibits
8. `jar-writing-style` — full-manuscript prose polish (design-forward, economically literate)
9. `jar-submission` — Research Exchange preflight (anonymization, fee, data-and-code package)
10. `jar-review-process` — set expectations for the editor-panel, multi-round process
11. `jar-rebuttal` — after an R&R, revise then draft the point-by-point response

> `jar-tables-figures` and `jar-writing-style` are **late-stage polish**. Do not invoke them while identification or the economic story is still unsettled.

## Decision shortcuts

- "Archival result, treatment looks endogenous" → `jar-methods` then `jar-data-analysis`
- "Two-way clustering vs. firm-only?" → `jar-data-analysis`
- "Referee says the channel is unidentified" → `jar-theory-development` then `jar-methods`
- "High-outcome-risk study with new data collection" → consider **Registered Reports** via `jar-review-process`
- "Targeting the Ray Ball Conference" → `jar-review-process` (deadline, eligibility) then the design skills
- "Submitting next week" → `jar-submission` (fee within a week; data/code package)
- "Got an R&R from the editor panel" → `jar-review-process` then `jar-rebuttal`

## Difference vs. TAR / JAE / RAST / CAR stacks

- **JAR**: Chicago Booth (Chookaszian Center) / Wiley; empirical-archival capital-markets identity; **requires** data-and-code sharing; tiered fee; Ray Ball Conference; Registered Reports. Identification + economic story weighted heavily.
- **The Accounting Review (TAR)**: American Accounting Association journal; broad scope; no equivalent mandatory replication-hosting infrastructure.
- **Journal of Accounting & Economics (JAE)**: Elsevier; positive/economics-based, contracting and disclosure; **encourages** rather than requires code sharing.
- **Review of Accounting Studies (RAST)** / **Contemporary Accounting Research (CAR)**: strong empirical outlets with their own scopes and norms.

If your paper is purely a methods/statistics contribution with no accounting question, or has no identification leverage, JAR is likely the wrong venue.

## Anti-patterns

- **Do not** skip `jar-theory-development` and present a regression with no economic channel.
- **Do not** let `jar-tables-figures` beautify exhibits before identification is settled.
- **Do not** start `jar-submission` without the runnable data-and-code package the policy requires.
- **Do not** let `jar-rebuttal` draft a response before the manuscript is actually revised.
