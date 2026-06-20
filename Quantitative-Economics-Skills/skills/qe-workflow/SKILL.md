---
name: qe-workflow
description: Use when deciding which qe-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Quantitative Economics (QE) submission. Routes — it does not replace — the specialized skills.
---

# QE Workflow Router (qe-workflow)

## Overview

This is the router. It tells you **which qe-* skill to use at the current stage** of a manuscript aimed at *Quantitative Economics* (QE) — the empirically and computationally oriented general-interest journal of the **Econometric Society**, the sister of *Econometrica* (more theoretical/methodological) and *Theoretical Economics* (pure theory). QE rewards papers that **develop or apply quantitative methods to substantive economic questions** — empirical, structural/computational, experimental, or simulation-based — with **documented data and reproducible code**.

Default assumption: unless the user says otherwise, treat the target as QE. Operational tells that you are at QE and not a sibling or a generic top journal: **Econometric Society membership is required to submit** (at least one author a member); there is a **submission fee** (US$100 regular / US$50 student); the manuscript must be **posted publicly during review**; the **ES Data Editor** runs a pre-acceptance reproducibility check (DCAS-compatible, not the JAE archive); QE is **Open Access (CC BY-NC)** with a post-proof publication fee based on production cost per page. Wiley product metadata checked on 2026-06-20 lists **Bernard Salanié** as editor. Re-verify volatile specifics on the official ES and Wiley pages.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between data/estimation, framing, writing, and the response letter
- A QE decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels narrow / not clearly general-interest quantitative | `qe-topic-selection` |
| Contribution vs. the frontier is fuzzy or undersold | `qe-literature-positioning` |
| The "so what" / one-sentence claim is not sharp | `qe-contribution-framing` |
| Empirical causal design or structural identification is shaky | `qe-identification-strategy` |
| Estimation, moments, or data handling need work | `qe-data-analysis` |
| Exhibits are dense; significance asterisks still present | `qe-tables-figures` |
| Prose buries the idea; abstract/intro do not land | `qe-writing-style` |
| Data/code deposit, README, or ES Data Editor prep | `qe-replication-and-data-policy` |
| Want to understand referee timeline / desk-reject odds / transfer | `qe-review-process` |
| Ready to submit via the ES portal; need a preflight | `qe-submission` |
| Received an R&R; need a response-letter strategy | `qe-rebuttal` |

## Default order

1. `qe-topic-selection` — lock the substantive quantitative question
2. `qe-literature-positioning` — stake the contribution vs. the frontier
3. `qe-contribution-framing` — sharpen the one-sentence claim
4. `qe-identification-strategy` — causal design or structural identification
5. `qe-data-analysis` — estimation, moments, diagnostics
6. `qe-tables-figures` — exhibits without significance asterisks
7. `qe-writing-style` — make the idea land (abstract + intro last)
8. `qe-replication-and-data-policy` — assemble the ES-compliant package
9. `qe-review-process` — calibrate expectations / consider Econometrica transfer
10. `qe-submission` — ES portal preflight
11. `qe-rebuttal` — after the R&R

> `qe-writing-style` is a late-stage polish; do not rewrite the intro before identification/estimation settle.

## Anti-patterns

- Skipping `qe-replication-and-data-policy` until acceptance — the ES Data Editor checks **before** acceptance
- Letting `qe-tables-figures` polish exhibits while estimation is still moving
- Treating QE like Econometrica (method-first) or a generic fee-free top-5 journal

## Routing by paper archetype

QE spans four quantitative branches, and the bottleneck differs by branch. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| structural / computational estimation | numerical validation + parameter identification | `qe-identification-strategy` → `qe-data-analysis` |
| applied micro / finance causal design | staggered-DID or weak-IV credibility | `qe-identification-strategy` |
| experiment (own data) | pre-registration + estimand (Jan 2026 rules) | `qe-topic-selection` → `qe-identification-strategy` |
| simulation / measurement | robustness to grids/tuning + reproducibility | `qe-data-analysis` → `qe-replication-and-data-policy` |

## Worked routing example (illustrative)

A user says: "My structural labor model estimates fine, but a referee called the counterfactual numerically fragile and the welfare gain not robust." That is two distinct QE pushbacks — *numerical accuracy not validated* and *results not robust to specification* — both owned by `qe-data-analysis`, with the identification defense in `qe-identification-strategy`. Route there first; only once the headline welfare number is stable (say it settles at 4.2%, s.e. 0.6, illustrative) do you return to `qe-tables-figures` and `qe-rebuttal` to present and defend it.

## Minimal decision snippet

```
if decision_letter_arrived:        -> qe-rebuttal
elif ready_to_submit:              -> qe-submission
elif exhibits_or_significance:     -> qe-tables-figures
elif estimation_or_numerics:       -> qe-data-analysis
elif identification_shaky:         -> qe-identification-strategy
elif claim_or_positioning_fuzzy:   -> qe-contribution-framing / qe-literature-positioning
else:                              -> qe-topic-selection
```
