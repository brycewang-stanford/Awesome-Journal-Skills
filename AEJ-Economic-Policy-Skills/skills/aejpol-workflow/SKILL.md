---
name: aejpol-workflow
description: Use when deciding which aejpol-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an AEJ: Economic Policy manuscript. Routes — it does not replace — the specialized skills.
---

# AEJ: Policy Workflow Router (aejpol-workflow)

## Overview

This is the router. It tells you **which aejpol-* skill to use at the current stage** of a manuscript aimed at the *American Economic Journal: Economic Policy* (AEJ: Policy) — the **American Economic Association's** quarterly journal for the **economic analysis OF policy**. AEJ: Policy rewards a paper built around a **clear policy question** whose answer carries a **welfare, cost-benefit, or distributional implication**, identified credibly (quasi-experimental / RCT / applied theory) and reproducible to AEA standards. The policy question and its counterfactual are the through-line of every skill below.

Default assumption: unless the user says otherwise, treat the target as AEJ: Policy. Operational tells that you are at AEJ: Policy and not a sibling: review is **single-blind** through the **AEA submission system** (the manuscript carries the title/byline/affiliations); **JEL codes** are required; the **AEA Data and Code Availability Policy** and the **AEA Data Editor** run a **pre-publication** reproducibility check on a deposit in the **AEA Data and Code Repository (openICPSR)**; the bar is **broad policy interest + credible causal evidence + a welfare/cost-benefit reading**, not a field-public-finance bar (J. Public Economics) or an identification-for-its-own-sake bar (AEJ: Applied). Re-verify volatile specifics (submission fee, editors) on the official AEA pages — official AEA pages checked 2026-06-20.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between identification, the policy framing, exhibits, and the response letter
- An AEJ: Policy decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| No sharp policy question, or fit vs. JPubE / AEJ:Applied / AER unclear | `aejpol-topic-selection` |
| Contribution vs. the policy-evaluation literature is fuzzy or undersold | `aejpol-literature-positioning` |
| Causal design (DID / IV / RDD / RCT) for the policy's effect is shaky | `aejpol-identification` |
| Need a model/welfare framework to read estimates as a policy effect | `aejpol-theory-model` |
| Estimate stability, sensitivity, and threats need stress-testing | `aejpol-robustness` |
| Exhibits are dense; significance asterisks still present | `aejpol-tables-figures` |
| Prose buries the policy takeaway; abstract/intro do not land | `aejpol-writing-style` |
| Data/code deposit, README, AEA Data Editor prep, restricted-data path | `aejpol-replication-package` |
| Want to anticipate the referees' objections before submitting | `aejpol-referee-strategy` |
| Ready to submit via the AEA system; need a preflight | `aejpol-submission` |
| Received an R&R; need a response-letter strategy | `aejpol-rebuttal` |

## Default order

1. `aejpol-topic-selection` — lock the policy question + the welfare/cost-benefit stake
2. `aejpol-literature-positioning` — stake the contribution vs. the policy-evaluation frontier
3. `aejpol-identification` — credible quasi-experimental / RCT evaluation of the policy
4. `aejpol-theory-model` — the framework that maps estimates to a welfare/policy object
5. `aejpol-robustness` — sensitivity, threats, specification stability
6. `aejpol-tables-figures` — exhibits without significance asterisks; a policy-relevant headline exhibit
7. `aejpol-writing-style` — translate estimates into a clear policy takeaway (abstract + intro last)
8. `aejpol-replication-package` — assemble the AEA-compliant deposit
9. `aejpol-referee-strategy` — pre-empt the objections referees will raise
10. `aejpol-submission` — AEA system preflight
11. `aejpol-rebuttal` — after the R&R

> `aejpol-writing-style` is a late-stage polish; do not rewrite the intro before identification/robustness settle.

## Anti-patterns

- Treating AEJ: Policy like J. Public Economics (field-only, no broad-interest policy framing) or AEJ: Applied (identification-driven applied micro with no policy question)
- Deferring `aejpol-replication-package` to acceptance — the AEA Data Editor checks **before** publication
- Letting `aejpol-tables-figures` polish exhibits while identification is still moving
- Reporting a clean causal estimate with **no** welfare / cost-benefit / distributional reading — the AEJ: Policy "so what"

## Routing by paper archetype

The bottleneck differs by how the policy is identified. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| reform / law change (staggered) | TWFE bias; modern DID; pre-trends | `aejpol-identification` |
| eligibility threshold / formula | RDD / bunching design + density test | `aejpol-identification` |
| field experiment / RCT of a program | estimand + pre-registration + welfare cost | `aejpol-topic-selection` → `aejpol-identification` |
| sufficient-statistics / structural welfare | mapping reduced-form estimate to welfare | `aejpol-theory-model` |

## Worked routing example (illustrative)

A user says: "My estimate of a tax-credit expansion on employment is clean, but a referee says the paper 'has no policy point' and the welfare claim is hand-waved." Two AEJ: Policy pushbacks — *no welfare/cost-benefit reading* and *takeaway not framed as a policy lesson* — owned by `aejpol-theory-model` (the welfare mapping) and `aejpol-writing-style` (the takeaway). Route to `aejpol-theory-model` to turn the employment elasticity into a marginal-value-of-public-funds / cost-per-job number, then `aejpol-writing-style` for the policy sentence.

## Minimal decision snippet

```
if decision_letter_arrived:        -> aejpol-rebuttal
elif ready_to_submit:              -> aejpol-submission
elif anticipating_referees:        -> aejpol-referee-strategy
elif exhibits_or_significance:     -> aejpol-tables-figures
elif estimate_unstable:            -> aejpol-robustness
elif welfare_mapping_missing:      -> aejpol-theory-model
elif identification_shaky:         -> aejpol-identification
elif claim_or_positioning_fuzzy:   -> aejpol-literature-positioning
else:                              -> aejpol-topic-selection
```
