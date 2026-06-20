---
name: jhe-workflow
description: Use when deciding which jhe-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a Journal of Health Economics (JHE) submission. Routes — it does not replace — the specialized skills.
---

# JHE Workflow Router (jhe-workflow)

## Overview

This is the router. It tells you **which jhe-* skill to use at the current stage** of a manuscript aimed at the *Journal of Health Economics* (JHE) — Elsevier's field flagship for health economics. JHE publishes economic analyses that deepen understanding of the **value, production, or distribution of health or healthcare**: insurance design and demand, provider incentives and payment, healthcare markets and competition, medical technology and pharmaceuticals, health behaviors (smoking, obesity, addiction), health and human capital, health-policy evaluation, and health disparities. What earns space is **credible causal identification fused with institutional health-system knowledge** — a clean design that a referee who knows Medicaid, DRGs, or Part D would trust.

Operational tells that you are at JHE and not a sibling: submission is via **Elsevier Editorial Manager** (editorialmanager.com/jhlthec); review is **single-anonymized** (referees see authors — so anonymization is *not* a desk-reject trigger, unlike the AEA journals); the journal takes **papers of any length and encourages short papers**; the data/code policy is **"encouraged," not a mandatory pre-publication openICPSR deposit** (检索于 2026-06；以官网为准). Distinguish JHE from **AJHE** (ASHEcon/Chicago, US-health-policy-leaning), **Journal of Public Economics** (tax/transfer/public-finance core), **Health Economics** (Wiley, broader methods/measurement), and **AEJ: Economic Policy** (AEA policy generalist). JHE is the Elsevier field flagship — the question must be a *health-economics* question, not health as one application of a public-finance paper.

## When to trigger

- The user asks "what should I do next?" on a JHE-targeted draft
- A draft's current bottleneck needs diagnosing
- Work is ping-ponging between design, institutions, exhibits, and the response letter
- A JHE decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/fit unclear; is this health economics or a public-finance paper in disguise? | `jhe-topic-selection` |
| Contribution vs. the health-econ frontier is fuzzy or undersold | `jhe-literature-positioning` |
| Causal design (policy variation, eligibility RD, selection into insurance) is shaky | `jhe-identification` |
| A demand/insurance/provider model or its mechanism is loose | `jhe-theory-model` |
| Results may be specification-, sample-, or inference-fragile | `jhe-robustness` |
| Exhibits are dense; the health-policy result is hard to find | `jhe-tables-figures` |
| Prose buries the policy stakes; abstract/intro do not land | `jhe-writing-style` |
| Data deposit, restricted-data access path, code documentation needed | `jhe-replication-package` |
| Want to pre-empt likely referee objections before submission | `jhe-referee-strategy` |
| Ready to submit via Editorial Manager; need a preflight | `jhe-submission` |
| Received an R&R / decision letter; need a response-letter strategy | `jhe-rebuttal` |

## Default order

1. `jhe-topic-selection` — lock the health-economics question and audience
2. `jhe-literature-positioning` — stake the contribution vs. the health-econ frontier
3. `jhe-identification` — causal design or selection/identification
4. `jhe-theory-model` — the demand/insurance/provider model behind the estimate
5. `jhe-robustness` — specification, sample, inference, mechanism stress tests
6. `jhe-tables-figures` — exhibits that make the health-policy result legible
7. `jhe-writing-style` — make the policy stakes land (abstract + intro last)
8. `jhe-replication-package` — assemble the deposit / restricted-data access path
9. `jhe-referee-strategy` — pre-mortem the likely health-econ objections
10. `jhe-submission` — Editorial Manager preflight
11. `jhe-rebuttal` — after the decision letter

> `jhe-writing-style` is a late-stage polish; do not rewrite the intro before identification and the headline estimate settle.

## Routing by paper archetype

JHE spans several health-econ branches, and the binding constraint differs by branch. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Insurance/coverage expansion (Medicaid/Medicare/exchange) | policy-variation design + spillovers to non-targeted margins | `jhe-identification` |
| Provider incentives / payment reform (DRG, P4P, ACO) | endogenous provider response + selection of patients | `jhe-identification` → `jhe-theory-model` |
| Health behaviors (tobacco, obesity, addiction) | tax/price variation credibility + externalities framing | `jhe-identification` → `jhe-literature-positioning` |
| Insurance demand / selection (structural) | what identifies risk preferences/adverse selection | `jhe-theory-model` → `jhe-identification` |
| Medical-technology / pharma diffusion | measurement + restricted claims-data access | `jhe-identification` → `jhe-replication-package` |

## Worked routing example (illustrative)

A user says: "My Medicaid-expansion DiD looks fine, but a referee says the parallel-trends story is thin and the welfare interpretation overreaches what a coverage effect can show." Two distinct JHE pushbacks — *design credibility* (own `jhe-identification`: move past TWFE, honest-DID bounds, event-study leads) and *overclaiming* (own `jhe-theory-model` + `jhe-writing-style`: a coverage-take-up effect is not a health-production or welfare effect without the mapping). Route to `jhe-identification` first; only once the coverage estimate is stable (say it settles at 4.1pp take-up, s.e. 1.0, illustrative) do you return to frame the welfare claim honestly and re-present in `jhe-tables-figures`.

## Minimal decision snippet

```
if decision_letter_arrived:            -> jhe-rebuttal
elif ready_to_submit:                  -> jhe-submission
elif want_to_pre-empt_referees:        -> jhe-referee-strategy
elif data_or_code_needs_packaging:     -> jhe-replication-package
elif prose_buries_the_stakes:          -> jhe-writing-style
elif exhibits_hard_to_read:            -> jhe-tables-figures
elif results_may_be_fragile:           -> jhe-robustness
elif need_a_model_to_interpret:        -> jhe-theory-model
elif design_or_selection_shaky:        -> jhe-identification
elif contribution_fuzzy:               -> jhe-literature-positioning
else:                                  -> jhe-topic-selection
```

## What this router does NOT do

It diagnoses the binding constraint and names the next skill; it does not run analysis, draft prose, or build exhibits — those live in the specialist skills. If the user's bottleneck spans two stages (e.g., a design fix that also changes the welfare claim), route to the earlier upstream skill first and let it hand off, rather than trying to resolve both here.

## Anti-patterns

- Treating JHE like AJHE, JPubE, or Health Economics — wrong audience, wrong contribution test
- Submitting a public-finance or labor paper with health as a thin application
- Anonymizing as if review were double-blind (JHE is single-anonymized; wasted effort)
- Polishing prose before the design and headline estimate are stable
- Letting the appendix carry the institutional or identification claims the main text must establish

## Output format

```text
【Target】Journal of Health Economics (Elsevier field flagship)
【Current bottleneck】fit / contribution / design / model / robustness / exhibits / style / package / submission / revision
【Archetype】coverage / provider-incentive / health-behavior / selection-structural / medtech
【Next skill】<one jhe-* skill>
【Reason】why this is the binding constraint now
【Source check】official facts verified or marked 待核实
```
