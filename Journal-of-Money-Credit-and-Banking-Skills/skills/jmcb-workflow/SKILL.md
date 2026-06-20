---
name: jmcb-workflow
description: Use when deciding which jmcb-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Money, Credit and Banking (JMCB) submission. Routes — it does not replace — the specialized skills.
---

# JMCB Workflow Router (jmcb-workflow)

## Overview

This is the router. It names **which jmcb-* skill to use at the current stage** of a manuscript aimed at the *Journal of Money, Credit and Banking* (JMCB) — the monetary-economics, banking, and macro-finance outlet **owned by the Ohio State University Department of Economics and published by Wiley-Blackwell** (founded 1969). JMCB rewards **policy-relevant** work that bridges theory and evidence on monetary transmission, bank balance sheets, credit frictions, and central-bank policy — whether the engine is a monetary/banking model (DSGE, search-and-matching banks) or empirics (SVAR, local projections, high-frequency monetary surprises, micro-banking panels).

Operational tells you are at JMCB and not a sibling: submission runs through **Editorial Express** (not Wiley's ScholarOne or Editorial Manager); there is a **submission fee** (US$150 subscriber / US$200 non-subscriber, refunded minus US$50 if desk-rejected; waived for resubmissions — 检索于 2026-06；以官网为准); the journal **strongly recommends ≤40 pages** including references, tables, and figures but **excluding the online appendix**; and it carries the historical **JMCB Data Archive** legacy (the Dewald–Thursby–Anderson 1986 replication study and the 2006 "Got Replicability?" follow-up were both about this journal). Editors as of 2026 include Sanjay Chugh and Pok-sang Lam (OSU), Robert DeYoung (Kansas), and Kenneth D. West (待核实；以官网为准).

## When to trigger

- The user asks "what should I do next?" on a JMCB-targeted paper
- A draft needs its current bottleneck diagnosed (fit, identification, evidence, exhibits, submission)
- Work is ping-ponging between the model/empirics, framing, exhibits, and the response letter
- A JMCB decision letter arrived and the user needs to switch into revision mode
- The team is weighing JMCB against the Journal of Monetary Economics, AEJ:Macro, Review of Economic Dynamics, or the Journal of Banking & Finance

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/audience fit uncertain; might be a JME or JBF paper instead | `jmcb-topic-selection` |
| Contribution vs. the monetary/banking frontier is fuzzy or undersold | `jmcb-literature-positioning` |
| Macro identification (SVAR/narrative/HF surprises) or micro-banking causal design is shaky | `jmcb-identification` |
| Bank/central-bank data construction, measurement, or sample is fragile | `jmcb-empirical-design` |
| Results may be specification-, sample-, or inference-sensitive | `jmcb-robustness` |
| Exhibits are dense; IRFs/coefficient plots do not answer the question | `jmcb-tables-figures` |
| Online appendix is too thin, too sprawling, or carries main claims | `jmcb-internet-appendix` |
| Intro/abstract bury the policy message; prose misses the JMCB voice | `jmcb-writing-style` |
| Close to submission; need the 40-page + Editorial Express preflight | `jmcb-submission` |
| Likely objections (and which editor desk) should be anticipated | `jmcb-referee-strategy` |
| A decision letter or referee report needs a response plan | `jmcb-rebuttal` |

## Default order

1. `jmcb-topic-selection` — lock the monetary/banking/macro-finance question and policy stakes
2. `jmcb-literature-positioning` — stake the contribution vs. JME, AEJ:Macro, RED, JBF
3. `jmcb-identification` — macro identification or micro-banking causal design
4. `jmcb-empirical-design` — bank/central-bank data, measurement, sample construction
5. `jmcb-robustness` — specification, sample, and inference fragility
6. `jmcb-tables-figures` — IRFs, coefficient plots, balance-sheet tables that read cleanly
7. `jmcb-internet-appendix` — offload supporting material; keep the 40-page core self-contained
8. `jmcb-writing-style` — make the policy idea land (abstract + intro last)
9. `jmcb-submission` — Editorial Express preflight, fee, page limit, data exemption
10. `jmcb-referee-strategy` — anticipate objections before submitting
11. `jmcb-rebuttal` — after the R&R

> `jmcb-writing-style` is a late-stage polish; do not rewrite the intro before identification and the evidence hierarchy settle. `jmcb-referee-strategy` is most useful *before* submission (to harden the paper) and again when a report lands.

## Anti-patterns

- Treating JMCB as interchangeable with the **Journal of Monetary Economics** (more theory/field-macro depth) or **AEJ:Macro** (general-interest macro) — JMCB prizes the policy bridge and institutional detail
- Routing a pure corporate-finance or asset-pricing paper here when it belongs at **JBF** or a finance field journal
- Letting `jmcb-tables-figures` polish IRFs while the SVAR identification is still moving
- Deferring the data/code question to acceptance — the journal's replication heritage means referees ask early
- Polishing prose before the contribution and evidence hierarchy are stable

## Routing by paper archetype

JMCB spans four engines, and the binding constraint differs by engine. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Quantitative monetary/banking model (DSGE, banking-friction) | what disciplines the parameters; policy-relevant counterfactual | `jmcb-identification` → `jmcb-empirical-design` |
| Macro identification (SVAR / narrative / HF monetary surprises) | shock identification + IRF inference | `jmcb-identification` |
| Micro-banking causal design (bank/loan-level panel) | clustering, weak-IV, staggered-policy bias | `jmcb-identification` → `jmcb-empirical-design` |
| Measurement / policy-evaluation (central-bank, regulation) | data construction + robustness to sample/window | `jmcb-empirical-design` → `jmcb-robustness` |

## Worked routing example (illustrative)

A user says: "My local-projection estimates of how a monetary-policy shock hits small-bank lending look fine, but a referee says the shock is contaminated by the Fed's information effect and the bank panel SEs are understated." Those are two distinct JMCB pushbacks — *shock identification* (informationally robust high-frequency surprises, à la the information-effect critique) and *inference* (clustering at the bank and time level). Route to `jmcb-identification` first to clean the shock, then `jmcb-robustness` for two-way clustering and a Driscoll–Kraay alternative; only once the lending elasticity is stable (say it settles at −1.8%, illustrative) return to `jmcb-tables-figures` and `jmcb-rebuttal`.

## Where the pack overlaps and how to sequence

Three pairs of skills frequently get conflated; keep them distinct. `jmcb-identification` owns the *causal/structural argument* (is the shock clean, is it supply not demand), while `jmcb-empirical-design` owns the *data the argument runs on* (construction, measurement, sample) — fix identification logic first, then harden the data, then stress both in `jmcb-robustness`. `jmcb-referee-strategy` is *anticipatory* (war-game objections before submission), while `jmcb-rebuttal` is *reactive* (respond to a report that arrived). `jmcb-tables-figures` and `jmcb-internet-appendix` both touch exhibits, but the first is about making the core exhibits legible and the second about what to offload — run them together near the end, after the evidence is final.

## Minimal decision snippet

```
if decision_letter_arrived:           -> jmcb-rebuttal
elif anticipating_objections:         -> jmcb-referee-strategy
elif ready_to_submit:                 -> jmcb-submission
elif appendix_thin_or_overloaded:     -> jmcb-internet-appendix
elif exhibits_unclear:                -> jmcb-tables-figures
elif results_fragile:                 -> jmcb-robustness
elif data_or_measurement_weak:        -> jmcb-empirical-design
elif identification_shaky:            -> jmcb-identification
elif contribution_fuzzy:              -> jmcb-literature-positioning
else:                                 -> jmcb-topic-selection
```
