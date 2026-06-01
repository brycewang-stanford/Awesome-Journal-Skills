---
name: car-workflow
description: Use when deciding which car-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Contemporary Accounting Research (CAR) manuscript. Routes — it does not replace — the specialized skills.
---

# Contemporary Accounting Research Workflow (car-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which car-* skill to use right now** for your CAR manuscript.

Default assumption: unless the user says otherwise, treat the target as **Contemporary Accounting Research (CAR)** — the premier research journal owned and sponsored by the Canadian Academic Accounting Association (CAAA) and published by Wiley (partnership since 2010), appearing quarterly (Mar/Jun/Sep/Dec). CAR is deliberately **method-agnostic**: it welcomes "interesting and intellectually rigorous work in all topic areas of accounting, using any appropriate method, and based in any discipline or research tradition." In practice the published mix is dominated by quantitative archival/capital-markets work, but CAR is also one of the most receptive top-tier outlets for experimental, analytical/modeling, field, and qualitative accounting research — so the first routing question is always *which research tradition you are in*, because methods, analysis, and contribution framing diverge sharply across archival, experimental, analytical, and qualitative papers.

> Editorial team changes: Anup Srivastava (University of Calgary) is Editor-in-Chief, supported by Deputy EICs Elizabeth Demers, Alexander Edwards, and Hervé Stolowy and ~24 subject Editors; the EIC reviews all acceptance decisions. Verify the current masthead at caaa.ca/car-editorial-team. Fees, the Style Guide, and the Data Integrity & Code Sharing Policy change — confirm on the official CAAA/CAR pages.

## When to trigger

- "What should I do next?" with a half-built CAR manuscript
- You have a result but are unsure whether the contribution lands in accounting theory or practice
- A reviewer pushes on identification (archival), internal validity (experiment), or robustness of a model's assumptions (analytical)
- You received a CAR decision letter and need to switch into response mode
- You keep bouncing between method, analysis, and writing without a plan

## Routing table

| Current symptom                                                          | Next skill                  |
|--------------------------------------------------------------------------|-----------------------------|
| Idea is vague; unsure it fits CAR's broad-tent accounting scope          | `car-topic-selection`       |
| Predictions are descriptive; no theoretical/economic mechanism           | `car-theory-development`    |
| Front end reads as gap-spotting; the accounting conversation is missing  | `car-literature-positioning`|
| Design/identification may not match the question (archival/exp/analytic) | `car-methods`               |
| Have data; unsure about estimation, robustness, or code-sharing prep     | `car-data-analysis`         |
| Results exist but the "so what for accounting" is thin                   | `car-contribution-framing`  |
| Exhibits cluttered, off CAR Style Guide, or not self-contained           | `car-tables-figures`        |
| Prose buries the question/finding; not in accounting house style         | `car-writing-style`         |
| Ready to submit; need the Editorial Manager preflight                    | `car-submission`            |
| Want to understand CAR's double-anonymous review before/after submit     | `car-review-process`        |
| Received an R&R; need to plan and draft the response                     | `car-rebuttal`              |

## Default order

1. `car-topic-selection` — lock a question that fits CAR and your research tradition
2. `car-theory-development` — build the mechanism / hypotheses / model
3. `car-literature-positioning` — join an accounting conversation
4. `car-methods` — match design and identification to the question
5. `car-data-analysis` — estimate, run robustness, and prepare code-sharing
6. `car-contribution-framing` — make the accounting contribution explicit
7. `car-tables-figures` — finalize exhibits in CAR Style Guide format
8. `car-writing-style` — full-manuscript prose polish
9. `car-submission` — Editorial Manager preflight (blind file, title page, fee, ethics)
10. `car-review-process` — set expectations for the two-reviewer, EIC-approved process
11. `car-rebuttal` — after an R&R, revise then draft the response letter

> `car-tables-figures` and `car-writing-style` are **late-stage polish**. Do not invoke them while identification (archival), internal validity (experiment), or the model (analytical) is unsettled.

## Decision shortcuts

- "Archival design, treatment may be endogenous" → `car-methods` then `car-data-analysis`
- "Experiment — worried about confounds and manipulation checks" → `car-methods`
- "Analytical model — is the contribution just a new comparative static?" → `car-contribution-framing`
- "Need to upload code and a data availability statement" → `car-data-analysis` then `car-submission`
- "Submitting this week; what does Editorial Manager need?" → `car-submission`
- "Got an R&R from two reviewers and a subject Editor" → `car-review-process` then `car-rebuttal`

## Anti-patterns

- **Do not** route an archival paper, an experiment, and an analytical model through identical analysis advice — CAR's big-tent scope means the standards differ by tradition.
- **Do not** let `car-tables-figures` beautify exhibits before the design and contribution settle.
- **Do not** let `car-rebuttal` draft a response before the manuscript is actually revised.
- **Do not** treat polish as a substitute for a genuine accounting contribution.
