---
name: jegeo-workflow
description: Use when deciding which jegeo-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a Journal of Economic Geography (JEG) submission. Routes — it does not replace — the specialized skills.
---

# JEG Workflow Router (jegeo-workflow)

## Overview

This is the router. It tells you **which jegeo-* skill to use at the current stage** of a manuscript aimed at the *Journal of Economic Geography* (JEG) — Oxford University Press's flagship for the **bridge between economics and geography**: agglomeration and clusters, regional and urban development, the economic geography of trade and global value chains, innovation and knowledge spillovers, institutions and space, evolutionary economic geography, and the location of firms and people.

The fact that defines JEG and every routing decision below: the journal deliberately spans **two communities** — "geographical economics" (the formal, quantitative New Economic Geography lineage of Krugman, Fujita, Venables, and the quantitative-spatial-model literature) AND "proper economic geography" (the institutional, evolutionary, and qualitative tradition of human geographers). Its masthead is drawn roughly equally from both (检索于 2026-06；以官网为准: EICs include Bathelt, Behrens, Coe, Iammarino, Kerr). A paper that speaks to only one community is the single most common desk-reject. Route accordingly: every stage must be defensible to an economist AND legible to a geographer.

Operational tells that you are at JEG and not a sibling: submission is via **ScholarOne / Manuscript Central** (`mc.manuscriptcentral.com/joeg`); review is **double-anonymous** (strip author identity); the **data/replication policy is encouragement-based and post-acceptance**, NOT a mandatory pre-acceptance archive (that distinguishes it sharply from QE, AEJ, and the AEA journals); standard articles run **≤8,000 words excluding references** with overflow pushed to an online appendix. Re-verify volatile specifics on the OUP page.

## When to trigger

- A manuscript is aimed at JEG and the next bottleneck is unclear
- A draft is ping-ponging between framing, design, mechanism, exhibits, and submission checks
- A decision letter arrived and you must choose between revising and drafting a rebuttal
- The team is comparing JEG with Journal of Urban Economics, Regional Science & Urban Economics, Regional Studies, or Economic Geography

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/audience/two-community fit is uncertain | `jegeo-topic-selection` |
| Contribution vs. adjacent journals and the NEG/EEG frontier is fuzzy | `jegeo-literature-positioning` |
| Causal or spatial-inference credibility is the bottleneck | `jegeo-identification` |
| The NEG model, quantitative-spatial framework, or conceptual frame is loose | `jegeo-theory-model` |
| Results may be spatial-scale-, weight-matrix-, sample-, or inference-sensitive | `jegeo-robustness` |
| Maps/exhibits are dense or do not answer the spatial question | `jegeo-tables-figures` |
| Intro/abstract/prose miss the two-audience JEG voice | `jegeo-writing-style` |
| Data, code, or spatial-data documentation needs packaging | `jegeo-replication-package` |
| Likely two-community objections should be pre-empted | `jegeo-referee-strategy` |
| Close to submission; need a ScholarOne preflight | `jegeo-submission` |
| A decision letter / referee report needs a response plan | `jegeo-rebuttal` |

## Default order

1. `jegeo-topic-selection` — lock a question that genuinely bridges the two communities
2. `jegeo-literature-positioning` — stake the contribution across NEG and human-geography frontiers
3. `jegeo-identification` — spatial causal design or quantitative-spatial identification
4. `jegeo-theory-model` — NEG/quantitative-spatial model OR conceptual framework
5. `jegeo-robustness` — spatial scale, weight matrix, spatial autocorrelation, Conley SEs
6. `jegeo-tables-figures` — maps that argue, not decorate
7. `jegeo-writing-style` — make it land for economists and geographers at once (intro last)
8. `jegeo-replication-package` — assemble shareable spatial data + code
9. `jegeo-referee-strategy` — anticipate the cross-disciplinary referee pair
10. `jegeo-submission` — ScholarOne preflight + double-anonymous scrub
11. `jegeo-rebuttal` — after the decision letter

> `jegeo-writing-style` is a late-stage polish; do not rewrite the intro before identification, mechanism, and the spatial-robustness story settle.

## Routing by paper archetype

JEG draws four recurring archetypes, and the binding constraint differs by branch. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| NEG / quantitative-spatial model (Krugman/Fujita/Redding-Rossi-Hansberg lineage) | parameter identification + calibration discipline | `jegeo-theory-model` → `jegeo-identification` |
| place-based-policy / regional causal evaluation | spatial DID/event-study + SUTVA across regions | `jegeo-identification` |
| evolutionary / institutional / qualitative geography | conceptual frame legible to economists; case-based inference | `jegeo-theory-model` → `jegeo-literature-positioning` |
| agglomeration / clusters / knowledge-spillover measurement | spatial-scale choice + spatial autocorrelation in inference | `jegeo-robustness` → `jegeo-identification` |

## Worked routing example (illustrative)

A user says: "My quantitative-spatial model of a high-speed-rail corridor estimates fine, but one referee (an economist) says the welfare counterfactual ignores spatial spillovers to non-connected regions, and the other (a geographer) says the paper has no mechanism — just a black-box gravity structure." That is two distinct JEG pushbacks from the two communities: *spatial spillover / general-equilibrium leakage* (own `jegeo-identification` and `jegeo-robustness` via Conley SEs and SUTVA) and *missing economic-geography mechanism* (own `jegeo-theory-model`, where the gravity coefficients must be tied to a story about why firms relocate). Route to `jegeo-theory-model` first to install the mechanism both referees can read, then to `jegeo-robustness` to bound the spillover, then `jegeo-rebuttal`.

## Anti-patterns

- Treating JEG as interchangeable with Journal of Urban Economics (Elsevier, urban economics, formal-only) or Economic Geography (more humanistic)
- Writing for only one community — formal model with no geographic mechanism, or rich case study with no engagement with the quantitative frontier
- Polishing prose before the spatial design and mechanism are stable
- Treating the data policy as a mandatory pre-acceptance archive (it is not) — or skipping it entirely
- Letting an online appendix carry a claim the 8,000-word main text must establish

## Minimal decision snippet

```
if decision_letter_arrived:            -> jegeo-rebuttal
elif ready_to_submit:                  -> jegeo-submission
elif anticipating_two_community_refs:  -> jegeo-referee-strategy
elif maps_or_exhibits_dense:           -> jegeo-tables-figures
elif spatial_scale_or_inference:       -> jegeo-robustness
elif identification_shaky:             -> jegeo-identification
elif model_or_mechanism_loose:         -> jegeo-theory-model
elif contribution_fuzzy:               -> jegeo-literature-positioning
else:                                  -> jegeo-topic-selection
```
