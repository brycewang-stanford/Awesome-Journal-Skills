---
name: jf-workflow
description: Use when deciding which jf-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for The Journal of Finance (JF). Routes — it does not replace — the specialized skills.
---

# Journal of Finance Workflow (jf-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which jf-* skill to invoke for the stage you are at** when preparing a manuscript for *The Journal of Finance* (JF), the American Finance Association's flagship general-interest journal published by Wiley.

Default assumption: unless the user says the target is JFE, RFS, or another outlet, treat the paper as aimed at JF. That means the editor and associate editors will reward an **important, broadly interesting question**, clean identification (corporate/empirical) or a well-motivated asset-pricing test, **economic significance**, and **polished, accessible** exposition that a general AFA reader can follow.

## When to trigger

- The user asks "what should I do next?"
- The user hands over a draft and needs the current bottleneck diagnosed
- Work is bouncing between empirics, writing, and referee replies and it feels disorganized
- A JF decision letter (reject / R&R) arrived and you need to switch into response mode

## Routing table

| Current symptom                                                  | Next skill                  |
|------------------------------------------------------------------|-----------------------------|
| Idea feels narrow; unsure it is "general interest" enough for JF | `jf-topic-selection`        |
| Lit review is a list; contribution vs. JF/JFE/RFS papers unclear | `jf-literature-positioning` |
| Corporate/empirical paper is OLS + controls; endogeneity unaddressed | `jf-identification`     |
| Asset-pricing test design unclear (factors, FM vs. panel, SEs)   | `jf-empirical-design`       |
| Main result exists but robustness / multiple-testing is thin     | `jf-robustness`             |
| Too many tables/columns; exhibits not publication-grade          | `jf-tables-figures`         |
| Proofs, extra tables, and secondary robustness clog the main text | `jf-internet-appendix`     |
| Prose is dense / jargon-heavy / buries the main finding          | `jf-writing-style`          |
| About to submit; need a Manuscript Central / ScholarOne preflight | `jf-submission`            |
| Want to anticipate the referee / pick suggested reviewers        | `jf-referee-strategy`       |
| Received an R&R and need to draft the response                   | `jf-rebuttal`               |

## Default order

1. `jf-topic-selection` — lock the general-interest question and economic significance
2. `jf-literature-positioning` — place the paper against the finance literature; state the marginal contribution
3. `jf-identification` — (corporate/empirical) defend the causal claim
4. `jf-empirical-design` — (asset pricing) design the test: factors, estimator, standard errors
5. `jf-robustness` — multiple-testing discipline, out-of-sample, sensitivity
6. `jf-tables-figures` — finalize main exhibits
7. `jf-internet-appendix` — move proofs / extra tables / secondary results out of the main text
8. `jf-writing-style` — polish for accessible, general-interest exposition
9. `jf-submission` — pre-submission preflight (portal, fee, membership, formatting)
10. `jf-referee-strategy` — anticipate referee objections; pick reviewers
11. `jf-rebuttal` — after the R&R

> `jf-identification` and `jf-empirical-design` are **branch siblings**: use the first for corporate/empirical causal claims, the second for asset-pricing tests. Many papers touch both — run whichever is the binding constraint first.
> `jf-writing-style` and `jf-tables-figures` are **late polish** — do not burn time there while identification or the test design is still unsettled.

## Decision shortcuts

- "I have a clean result but it's a niche question" → `jf-topic-selection` (general interest is the JF gate)
- "My intro cites everything but never says what's new" → `jf-literature-positioning`
- "Reviewer will say the treatment is endogenous" → `jf-identification`
- "I sorted on 200 signals and report the best one" → `jf-empirical-design` then `jf-robustness` (multiple testing)
- "My factor result flips when I change the sample" → `jf-robustness`
- "The paper is 70 pages and the main table is on page 40" → `jf-internet-appendix` + `jf-writing-style`
- "Submitting tomorrow" → `jf-submission`
- "Got three referee reports" → `jf-rebuttal`

## Differences vs. JFE / RFS skill stacks

JF, JFE, and RFS are the "top three" finance journals but reward different things:

- **JF**: general interest first; somewhat shorter, more accessible articles; technical depth pushed to the Internet Appendix; broad AFA readership.
- **JFE**: rewards depth and methodological heft; tolerates longer, more technical papers.
- **RFS**: prizes theoretical framing and structural/mechanism contribution alongside empirics.

If the paper is long, highly technical, and aimed at specialists, JFE or RFS may fit better than JF.

## Anti-patterns

- **Do not** skip `jf-literature-positioning` and jump to identification — JF editors read the contribution claim first and ask "why does the field care?"
- **Do not** let `jf-tables-figures` beautify exhibits while the identification / test design is still fragile
- **Do not** let `jf-rebuttal` draft a response letter before you have actually revised the manuscript and Internet Appendix
- **Do not** treat statistical significance as the deliverable — JF wants **economic** significance
