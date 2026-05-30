---
name: rfs-workflow
description: Use when deciding which rfs-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a The Review of Financial Studies (RFS) manuscript. Routes — does not replace — the specialized skills.
---

# RFS Manuscript Workflow (rfs-workflow)

## Overview

This is the router. It does not replace any specialized skill — it tells you **which rfs-* skill to use right now**.

Default assumption: unless the user says otherwise, treat the target as **The Review of Financial Studies (RFS)** — published by Oxford University Press for the Society for Financial Studies (SFS), one of the "top-3" finance journals alongside the *Journal of Finance* and the *Journal of Financial Economics*. RFS shares JF/JFE's high causal-inference and asset-pricing bar but is distinctively **receptive to genuinely new questions, new data, new methods, and well-integrated theory + empirics**. The governing tension at RFS is always **novelty AND rigor** — never one without the other.

## When to trigger

- The user asks "what should I do next?"
- A draft arrives and you must diagnose the current bottleneck
- The user is thrashing between empirics, writing, and revision
- A decision letter from RFS arrives and you must switch into rebuttal mode
- The user is unsure whether the paper is novel enough OR rigorous enough for RFS

## Routing table

| Current symptom                                                        | Next skill                     |
|------------------------------------------------------------------------|--------------------------------|
| Idea feels incremental / "me-too"; unsure it clears RFS's novelty bar  | `rfs-topic-selection`          |
| Related-work positioning is weak; unclear delta vs. JF/JFE/RFS papers  | `rfs-literature-positioning`   |
| Core claim is causal but design is OLS + controls / endogeneity open   | `rfs-identification`           |
| Design choices unsettled: panel, factor model, structural, sample      | `rfs-empirical-design`         |
| Main result exists but is fragile / multiple-testing not addressed     | `rfs-robustness`               |
| Tables overloaded; figures not publication-grade; SEs unclear          | `rfs-tables-figures`           |
| Main paper is bloated; checks/derivations belong elsewhere             | `rfs-internet-appendix`        |
| Prose is dense, hedged, or buries the contribution                     | `rfs-writing-style`            |
| Preparing to submit; need ScholarOne preflight + cover letter          | `rfs-submission`               |
| Choosing/excluding referees; anticipating reviewer objections          | `rfs-referee-strategy`         |
| Received an R&R or reject-and-resubmit; need a response letter         | `rfs-rebuttal`                 |

## Default order

1. `rfs-topic-selection` — lock the novel question + the contribution to finance theory/practice
2. `rfs-literature-positioning` — situate against JF/JFE/RFS and define the precise delta
3. `rfs-identification` — pin the causal-inference / asset-pricing identification strategy
4. `rfs-empirical-design` — sample construction, estimators, factor/structural choices
5. `rfs-robustness` — alternative specs, placebo, multiple-testing, out-of-sample
6. `rfs-tables-figures` — finalize main exhibits and standard-error reporting
7. `rfs-internet-appendix` — move proofs, extra tables, and details to the IA
8. `rfs-writing-style` — sharpen contribution framing and prose (polish stage)
9. `rfs-submission` — ScholarOne preflight + cover letter + fee/format checks
10. `rfs-referee-strategy` — referee suggestions and objection pre-mortem
11. `rfs-rebuttal` — after the decision letter

> `rfs-writing-style` is a **late-stage polish** trigger. Do not run it while the identification or novelty story is still unsettled.

## Decision heuristics

- "I have clean data but no new question" → `rfs-topic-selection`
- "I cite the literature but cannot state my one-sentence delta" → `rfs-literature-positioning`
- "My DID is TWFE and I have not addressed staggered-adoption bias" → `rfs-identification`
- "My cross-sectional asset-pricing result rests on a self-selected factor" → `rfs-empirical-design`
- "I tested 40 predictors and reported the 3 that worked" → `rfs-robustness`
- "My main table has 11 columns and no clustering note" → `rfs-tables-figures`
- "Reviewers will want 20 more tables I cannot fit" → `rfs-internet-appendix`
- "The abstract hides what is new" → `rfs-writing-style`
- "I submit Friday" → `rfs-submission`
- "I want to suggest/exclude referees" → `rfs-referee-strategy`
- "I have three reports and an R&R" → `rfs-rebuttal`

## Differences vs. JF / JFE stacks

RFS overlaps heavily with the JF and JFE skill stacks on the causal-inference bar. The distinctive RFS lever is **receptivity to novelty**: a genuinely new question, dataset, or method (fintech, climate finance, intermediary asset pricing, household and behavioral finance) plus tightly integrated theory and evidence is rewarded more explicitly at RFS. A technically clean paper that merely re-runs a known design on new data without a new question is a weak RFS fit even if it would survive at a field journal.

## Anti-patterns

- **Do not** skip `rfs-literature-positioning` and jump to identification — reviewers judge the contribution first.
- **Do not** let `rfs-tables-figures` polish exhibits before identification and robustness hold up.
- **Do not** let `rfs-rebuttal` draft a response letter before the manuscript itself is revised.
- **Do not** pursue rigor while ignoring novelty (or novelty while ignoring rigor) — RFS rejects both halves alone.
