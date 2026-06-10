---
name: rof-workflow
description: Use when deciding which rof-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Review of Finance (RoF) submission. Routes — it does not replace — the specialized skills.
---

# Review of Finance Workflow Router (rof-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which rof-* skill to use at the current stage** of a manuscript aimed at the *Review of Finance* (RoF) — the **official journal of the European Finance Association (EFA)**, published by **Oxford University Press**, covering **general-interest empirical and theoretical finance at the level of the top-three finance journals**. Operational tells: **Editorial Express** submission, a **real fee (EUR 350 / EUR 300 EFA members)** plus an optional **Fast-Track** (EUR 900, **14-day** decision), **double-blind** review, a **two-round decision philosophy**, a **hard 60-page cap** (incl. appendices, bibliography, figures, tables), a **150-word abstract**, **Chicago** citations, and a **Code Sharing and Data Availability Policy**. Re-verify volatile specifics on the official pages.

## When to trigger

- The user asks "what should I do next?"
- The user hands over a draft and needs the current bottleneck diagnosed
- An RoF decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom                                                          | Next skill                       |
|--------------------------------------------------------------------------|----------------------------------|
| Idea feels small / not obviously top-finance material                    | `rof-topic-selection`            |
| "So what?" / contribution to finance is fuzzy or undersold               | `rof-contribution-framing`       |
| Placement against the finance frontier is unclear; citations thin        | `rof-literature-positioning`     |
| Causal claim (empirical) or assumptions/results (theory) are undefended  | `rof-identification-strategy`    |
| Estimation, sample, variable construction, or robustness is the weak link| `rof-data-analysis`              |
| Tables are dense; exhibits blow the 60-page budget                       | `rof-tables-figures`             |
| Prose buries the idea; abstract/intro do not land in 150 words           | `rof-writing-style`              |
| Need the replication package / Data Availability Statement               | `rof-replication-and-data-policy`|
| Want to understand referee standards / two-round logic before submitting | `rof-review-process`             |
| Ready to submit via Editorial Express; need a preflight + fee decision   | `rof-submission`                 |
| Received an R&R; need a response-letter strategy                         | `rof-rebuttal`                   |

## Default order

1. `rof-topic-selection` → 2. `rof-contribution-framing` → 3. `rof-literature-positioning` → 4. `rof-identification-strategy` (causal design, or theory assumptions/results) → 5. `rof-data-analysis` (estimation/robustness, or numerical work) → 6. `rof-tables-figures` (within the 60-page cap) → 7. `rof-writing-style` (abstract ≤150 words, intro last) → 8. `rof-replication-and-data-policy` → 9. `rof-review-process` → 10. `rof-submission` (Editorial Express; regular vs. Fast-Track) → 11. `rof-rebuttal` (after the R&R).

> `rof-writing-style` is a late-stage polish. Do not rewrite the intro before identification/results are settled.

## Stage gates — exit criteria before advancing

Do not move down the default order until the current gate clears; the two-round philosophy makes pre-submission completeness the whole game.

```text
Gate A  idea        question survives the top-three-interest test ... rof-topic-selection
Gate B  claim       one-sentence quantified contribution stands ..... rof-contribution-framing
Gate C  placement   3-6 closest papers named, delta stated for each . rof-literature-positioning
Gate D  credibility identification or theory spine survives attack .. rof-identification-strategy
Gate E  evidence    magnitudes economic; robustness mapped to files . rof-data-analysis
Gate F  package     <=60 pages incl. everything; abstract <=150 ..... rof-tables-figures / rof-writing-style
Gate G  compliance  DAS + code/pseudo-data + disclosures drafted .... rof-replication-and-data-policy / rof-submission
PAY THE FEE ONLY AFTER GATE G.
```

## Sequencing around the EFA circuit and the fee

- RoF is the EFA's house journal: presenting at the EFA annual meeting (or a comparable European finance conference) before paying the fee is the cheapest way to surface the bucket-1 objections referees will raise.
- Choose Fast-Track (EUR 900, 14-day target) only for a finished paper under competitive pressure — e.g., several teams exploiting the same regulatory shock; a paper still failing Gate D or E burns the premium.
- Front-load the heavy robustness battery before first submission: under the two-round philosophy there is no "save it for the revision" reserve, because round two is for closing, not opening, issues.
- Build the replication package in parallel with Gate E rather than after acceptance — the Code Sharing and Data Availability Policy can delay publication until programs arrive, and proprietary-data exceptions must already be requested in the initial cover letter (Gate G).
- Re-verify fee, refund, and policy specifics against the journal's current author guidelines before paying anything.

## Anti-patterns

- **Do not** skip `rof-contribution-framing` and jump to estimation — RoF judges the finance contribution first.
- **Do not** ignore the 60-page cap until the end — it includes appendices, bibliography, figures, and tables.
- **Do not** draft a rebuttal before the revised manuscript exists; the two-round philosophy makes round one decisive.
