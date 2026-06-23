---
name: tar-workflow
description: Use when deciding which tar-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The Accounting Review (TAR) manuscript. Routes — it does not replace — the specialized skills.
---

# The Accounting Review Workflow (tar-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which tar-* skill to use right now** for your TAR manuscript.

Default assumption: unless the user says otherwise, treat the target as **The Accounting Review (TAR)** — the flagship journal of the American Accounting Association (AAA, aaahq.org), covering archival/empirical and analytical accounting across financial accounting, capital markets, auditing and assurance, management accounting, taxation, and accounting information systems. TAR's stated policy is explicitly **open to all rigorous research methods** and names no preferred methodology; the single overriding publication criterion is the **significance of the contribution to the accounting literature**. In practice the published mix is dominated by large-sample archival/empirical work, alongside a substantial experimental stream and analytical/theory papers (待核实 as a characterization, not policy). The action editor and a minimum of two reviewers will ask "what do we learn about accounting that we did not know?" as hard as "is identification clean?"

> Editorial team: Senior Editor **Mohan Venkatachalam (Duke, Fuqua)** — sitting since June 2026, succeeding Kathryn Kadous (Emory); named Lead Editors (Hribar, Maydew, Mittendorf, Rennekamp) handle assignments, decision letters, desk rejections, and appeals; Ad hoc Editors cover specialized topics/methods. Submission fee ($285 member / $680 non-member, re-verified 2026-06-23) and full roster — 待核实; confirm on the official AAA pages.

## When to trigger

- "What should I do next?" with a half-built TAR manuscript
- You have a clean archival sample and a result but no sharp accounting contribution
- A reviewer pushes on identification, the data-authenticity/code-access policy, or contribution and you are unsure which stage is the bottleneck
- You received a TAR decision letter and need to switch into response mode
- You keep bouncing between identification, theory/model, and writing without a plan

## Routing table

| Current symptom                                                        | Next skill                  |
|------------------------------------------------------------------------|-----------------------------|
| Idea is vague; not sure it is contribution-driven or TAR-fit           | `tar-topic-selection`       |
| Predictions are descriptive; no economic mechanism or model            | `tar-theory-development`    |
| Front end reads as gap-spotting; the accounting conversation not joined | `tar-literature-positioning`|
| Design may not identify the effect (endogeneity, selection, timing)    | `tar-methods`               |
| Have data; unsure about estimator, clustering, FE, robustness          | `tar-data-analysis`         |
| Results exist but the "so what for accounting" is thin                 | `tar-contribution-framing`  |
| Tables/figures cluttered, off Chicago style, or not self-explanatory   | `tar-tables-figures`        |
| Prose is jargon-heavy, passive, or buries the result                   | `tar-writing-style`         |
| Ready to submit; need the Editorial Manager preflight                  | `tar-submission`            |
| Want to understand how TAR double-blind review/decisions work          | `tar-review-process`        |
| Received an R&R; need to plan and draft the response                   | `tar-rebuttal`              |

## Default order

1. `tar-topic-selection` — lock a contribution-driven question with TAR fit
2. `tar-theory-development` — build the economic mechanism / analytical model and predictions
3. `tar-literature-positioning` — engage the focal accounting literature; state the conversation
4. `tar-methods` — design identification (DiD, IV, RDD, setting, shock) matched to the question
5. `tar-data-analysis` — estimator, fixed effects, clustering, robustness, data-authenticity code
6. `tar-contribution-framing` — turn results into an explicit accounting contribution
7. `tar-tables-figures` — finalize main exhibits in Chicago house style
8. `tar-writing-style` — full-manuscript prose polish (result front-loaded, active voice)
9. `tar-submission` — Editorial Manager preflight (anonymization, AI disclosure, ORCID, files)
10. `tar-review-process` — set expectations for double-blind, multi-round review
11. `tar-rebuttal` — after an R&R, plan revisions then draft the response letter

> `tar-tables-figures` and `tar-writing-style` are **late-stage polish**. Do not invoke them while identification or the contribution is still unsettled — you will polish an argument you may still have to rebuild.

## Decision shortcuts

- "I have a finding but no accounting story" → `tar-topic-selection` then `tar-contribution-framing`
- "My intro says 'no one has studied X'" (gap-spotting) → `tar-literature-positioning`
- "My treatment is endogenous / staggered adoption" → `tar-methods` then `tar-data-analysis`
- "Reviewer asks for the code that builds my Compustat sample" → `tar-data-analysis` (data-authenticity)
- "An analytical model needs comparative statics" → `tar-theory-development`
- "Submitting this week" → `tar-submission`
- "Got an R&R with two reviewers + the editor" → `tar-review-process` then `tar-rebuttal`

## Difference vs. JAR / JAE and the AAA family

- **TAR**: AAA flagship; open to all rigorous methods, contribution-to-the-literature is the bar; double-blind review; Editorial Manager at editorialmanager.com/accr; 55-page initial limit; Chicago Manual of Style.
- **JAR** (Journal of Accounting Research, Chicago Booth) and **JAE** (Journal of Accounting and Economics, Elsevier) are the other two "top-3" archival accounting journals but are separately owned and run their own review and style norms — use a venue-specific stack.
- **Journal of Financial Reporting** is the one AAA journal using **single-blind** review; TAR is **double-blind**.

If your study is purely a methods demonstration with no accounting contribution, TAR is the wrong venue.

## Anti-patterns

- **Do not** skip `tar-theory-development` and report a correlation — TAR rejects atheoretical "regression-mining."
- **Do not** let `tar-tables-figures` beautify exhibits before identification and the contribution are settled.
- **Do not** let `tar-rebuttal` draft a response letter before you have actually revised the manuscript and the code.
- **Do not** treat `tar-writing-style` as a substitute for a clean identification strategy or a real contribution.
