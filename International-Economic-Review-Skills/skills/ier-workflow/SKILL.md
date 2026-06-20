---
name: ier-workflow
description: Use when deciding which ier-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for an International Economic Review (IER) manuscript. Routes — it does not replace — the specialized skills.
---

# IER Workflow Router (ier-workflow)

## Overview

This is the router. It tells you **which ier-* skill to use at the current stage** of a manuscript aimed at the *International Economic Review* (IER) — the broad, rigor-leaning general-interest journal founded in **1960** "to provide a forum for modern quantitative economics," owned by the **Economics Department of the University of Pennsylvania** together with the **Institute of Social and Economic Research (ISER), Osaka University**, and published with Wiley. "International" names the Penn–Osaka partnership (and the Klein Lectures it hosts), not a field restriction: IER covers **economic theory, econometrics, quantitative/structural macro, and applied micro**, with a pronounced **theory/structural tilt** and a premium on methodological rigor, generality, and a clean model-to-evidence link.

Default assumption: unless the user says otherwise, treat the target as IER. Operational tells that you are at IER and not a sibling: submission runs through **Editorial Express** (editorialexpress.com/ier), not ScholarOne/Manuscript Central (检索于 2026-06；以官网为准); there is a **flat US$150 / ¥15,000 submission fee** and the paper is not reviewed until it is paid; the manuscript ceiling is **≤50 pages, double-spaced**; the journal adopted the **AER data availability policy effective Jan 1, 2022**. Editor names and exact figures are volatile — re-verify on the official Penn/Wiley pages (待核实).

## When to trigger

- The user asks "what should I do next?" on an IER-bound draft
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between theory/model, identification, evidence, exhibits, and the response letter
- An IER decision letter arrived and the user needs to switch into revision mode
- The team is weighing IER against Econometrica/QE, a top-5, or a field journal

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels narrow / not clearly general-interest quantitative | `ier-topic-selection` |
| Contribution vs. the frontier or vs. sibling journals is fuzzy | `ier-literature-positioning` |
| The model is the contribution but its assumptions/results aren't tight | `ier-theory-model` |
| Empirical causal design or structural parameter identification is shaky | `ier-identification` |
| Results may be specification-, sample-, or inference-sensitive | `ier-robustness` |
| Exhibits are dense or do not answer the question | `ier-tables-figures` |
| Prose buries the idea; intro/abstract do not land for a broad audience | `ier-writing-style` |
| Data/code deposit, README, proof appendix, or AER-policy prep | `ier-replication-package` |
| Likely referee objections should be anticipated before submission | `ier-referee-strategy` |
| Ready to submit via Editorial Express; need a preflight | `ier-submission` |
| Received an R&R; need a response-letter strategy | `ier-rebuttal` |

## Default order

1. `ier-topic-selection` — lock a general-interest quantitative question
2. `ier-literature-positioning` — stake the contribution vs. the frontier and siblings
3. `ier-theory-model` — make the model tight (assumptions, results, comparative statics)
4. `ier-identification` — structural parameter or empirical causal identification
5. `ier-robustness` — stability to specification, sample, and inference choices
6. `ier-tables-figures` — exhibits that carry the argument
7. `ier-writing-style` — make the idea land for a broad rigor audience (intro/abstract last)
8. `ier-replication-package` — AER-policy package + proof appendix
9. `ier-referee-strategy` — anticipate objections, pre-empt the obvious referee
10. `ier-submission` — Editorial Express preflight (fee + ≤50pp + format)
11. `ier-rebuttal` — after the R&R

> For a theory paper, `ier-theory-model` precedes `ier-identification`; for an applied paper they often swap. Do not let `ier-writing-style` rewrite the intro before the model and evidence settle.

## Routing by paper archetype

IER spans four broad branches, and the binding constraint differs by branch. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| pure / applied theory | which assumptions are load-bearing; is the result general or knife-edge | `ier-theory-model` |
| structural / quantitative macro | parameter identification + numerical discipline + counterfactual validity | `ier-theory-model` → `ier-identification` |
| econometric theory / method | what the estimator buys over incumbents; asymptotics + finite-sample evidence | `ier-theory-model` → `ier-robustness` |
| applied micro (causal) | credible design (staggered DID, weak IV, RDD) tied to a mechanism | `ier-identification` |

## Worked routing example (illustrative)

A user says: "My quantitative trade model fits the moments, but a referee says the welfare gain is an artifact of the elasticity I calibrated and the proof of equilibrium uniqueness is hand-waved." That is two distinct IER pushbacks — *a load-bearing assumption / parameter is undefended* (owned by `ier-identification` for what pins the elasticity, and `ier-theory-model` for the uniqueness argument) and *the headline number isn't robust* (owned by `ier-robustness`). Route to `ier-theory-model` first to make the equilibrium argument airtight, then `ier-identification` to show what in the data moves the elasticity, then `ier-robustness` to bound the welfare number — only then back to `ier-tables-figures` and `ier-rebuttal`.

## How IER differs from its siblings (use this to route a mis-targeted paper)

- **Econometrica / Quantitative Economics** are Econometric Society journals: method-first, membership-gated, no flat per-paper submission fee, ScholarOne-style portals. IER is Penn–Osaka-owned, broad/theory-leaning, flat US$150 fee, Editorial Express portal.
- **Top-5 (AER/QJE/JPE/REStud/Eca)** demand topical importance on top of rigor; IER rewards rigor and generality without requiring the "splash."
- **Field journals (JIE, J. of Econometrics, etc.)** want depth in one field; IER wants the result to travel beyond it. If a draft fits a sibling better, route the user to `ier-topic-selection` to reframe or to retarget before going further down the chain.

## Anti-patterns

- Treating IER as interchangeable with Econometrica/QE (Econometric Society, method-first, no flat fee) or with a fee-free top-5
- Polishing prose before the model, identification, and evidence hierarchy are stable
- Skipping `ier-replication-package` until acceptance — the AER policy and proof appendix are part of the contribution, not an afterthought
- Submitting past the 50-page ceiling or before the $150 fee clears (the paper is not even reviewed)

## Minimal decision snippet

```
if decision_letter_arrived:        -> ier-rebuttal
elif ready_to_submit:              -> ier-submission
elif anticipating_referees:        -> ier-referee-strategy
elif data_code_or_proofs:          -> ier-replication-package
elif exhibits_dense:               -> ier-tables-figures
elif results_fragile:              -> ier-robustness
elif identification_shaky:         -> ier-identification
elif model_not_tight:             -> ier-theory-model
elif contribution_fuzzy:           -> ier-literature-positioning
else:                              -> ier-topic-selection
```
