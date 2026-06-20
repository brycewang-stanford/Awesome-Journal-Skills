---
name: jru-workflow
description: Use when deciding which jru-* sub-skill to invoke next, or when sequencing manuscript work from question through rebuttal for a Journal of Risk and Uncertainty (JRU) submission. Routes — it does not replace — the specialized skills.
---

# JRU Workflow Router (jru-workflow)

## Overview

This is the router. It tells you **which jru-* skill to use at the current stage** of a manuscript aimed at the *Journal of Risk and Uncertainty* (JRU) — the field's leading specialized outlet for **decision-making under risk and uncertainty**. Founded in 1988 and edited since by **W. Kip Viscusi** (Vanderbilt), published by **Springer** (Springer Nature Link; ISSN 0895-5646 print / 1573-0476 electronic), JRU is the home journal of expected utility *and its alternatives* (prospect theory, rank-dependent utility, ambiguity / Knightian uncertainty), of risk-preference measurement, of the **value of a statistical life (VSL)**, and of insurance, precaution, and intertemporal risk. It publishes decision **theory**, lab and field **experiments**, and **empirical / structural** estimation side by side.

Default assumption: unless the user says otherwise, treat the target as JRU. Operational tells that you are at JRU and not a sibling: the paper's object is a **risk or uncertainty primitive** — a utility/probability-weighting representation, an elicited risk or ambiguity parameter, a VSL, an insurance-demand elasticity — not a market design, a game-theoretic equilibrium, or a generic behavioral anomaly. Volatile process specifics (exact word/abstract limits, OA fees, board members) are marked `(检索于 2026-06；以官网为准)` or 待核实; never invent them.

## When to trigger

- The user asks "what should I do next?" on a JRU-bound draft
- A draft needs its current bottleneck diagnosed (theory vs. elicitation vs. estimation)
- Work is ping-ponging between the decision model, the experiment, the empirics, and the response letter
- A JRU decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels like a generic anomaly, not a risk/uncertainty primitive | `jru-topic-selection` |
| Contribution vs. EU/PT/ambiguity literature is fuzzy or oversold | `jru-literature-positioning` |
| The decision-theoretic representation or axioms are loose | `jru-theory-model` |
| What identifies the risk/ambiguity parameter (elicitation or structural) is unclear | `jru-identification` |
| Results may be sensitive to spec, sample, incentive frame, or inference | `jru-robustness` |
| Exhibits bury the choice patterns / parameter estimates | `jru-tables-figures` |
| Prose buries the decision model; abstract/intro do not land | `jru-writing-style` |
| Experiment data, z-Tree/oTree code, or structural code need packaging | `jru-replication-package` |
| Want to anticipate the likely referee objections before submission | `jru-referee-strategy` |
| Ready to submit via Springer's portal; need a preflight | `jru-submission` |
| Received an R&R / reject-and-resubmit; need a response strategy | `jru-rebuttal` |

## Default order

1. `jru-topic-selection` — lock a genuine risk/uncertainty primitive
2. `jru-literature-positioning` — stake the contribution vs. EU and its alternatives
3. `jru-theory-model` — get the decision-theoretic representation right
4. `jru-identification` — what elicits or estimates the parameter
5. `jru-robustness` — incentive-, spec-, and inference-robustness
6. `jru-tables-figures` — make choice patterns and estimates legible
7. `jru-writing-style` — make the idea land (abstract + intro last)
8. `jru-replication-package` — assemble experiment instructions + data + code
9. `jru-referee-strategy` — wargame the report before it arrives
10. `jru-submission` — Springer portal preflight
11. `jru-rebuttal` — after the decision letter

> `jru-writing-style` is a late-stage polish; do not rewrite the intro before the representation and the elicitation/estimation settle.

## Anti-patterns

- Treating JRU as interchangeable with Experimental Economics (which is **method**-general — it cares whether the experiment is well-run, not whether the object is a risk primitive)
- Treating JRU as JEBO (broad behavioral / organizational) or Theory and Decision (pure axiomatics with no measurement)
- Polishing exhibits while the parameter estimates are still moving
- Letting an appendix carry the axiom or the incentive-compatibility argument the main text must establish

## Routing by paper archetype

JRU spans four risk-and-uncertainty branches, and the binding constraint differs by branch. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| decision-theory / representation | axioms ↔ functional form ↔ behavioral content | `jru-theory-model` |
| lab/field experiment eliciting risk or ambiguity | incentive-compatible mechanism + estimand | `jru-identification` → `jru-robustness` |
| structural / empirical risk preferences (VSL, insurance) | what variation identifies the parameter | `jru-identification` |
| replication / methods comparison of elicitation devices | design + data + code transparency | `jru-replication-package` → `jru-robustness` |

## Worked routing example (illustrative)

A user says: "We elicit ambiguity aversion with a matching-probabilities task and estimate an α-MEU model, but a referee says the elicitation is not incentive-compatible and the model is unfalsifiable." That is two distinct JRU pushbacks — *the mechanism does not truthfully reveal the preference* (owned by `jru-identification`) and *the representation has no behavioral content* (owned by `jru-theory-model`). Fix the representation first so the estimand is well-defined, then defend the mechanism; only once the headline ambiguity parameter is stable do you return to `jru-tables-figures` and `jru-rebuttal`.

## Sibling-venue routing (when JRU may be the wrong home)

Part of routing is catching a paper that should not be at JRU at all. If the diagnosis below fits, the binding step is `jru-topic-selection` (to re-anchor) or a different venue entirely:

| Tell | Likely better home |
|------|--------------------|
| The contribution is the experimental technique, not a risk primitive | Experimental Economics |
| Several behavioral findings, no single decision-theoretic claim | JEBO |
| Pure axiomatization with no measurable implication | Theory and Decision |
| A managerial decision tool rather than a positive risk claim | Management Science (decision analysis) |

If the primitive is the headline and the application is merely the setting, JRU is right — route into the chain at `jru-topic-selection`.

## Minimal decision snippet

```
if decision_letter_arrived:        -> jru-rebuttal
elif ready_to_submit:              -> jru-submission
elif anticipating_referees:        -> jru-referee-strategy
elif exhibits_unclear:             -> jru-tables-figures
elif results_fragile:              -> jru-robustness
elif parameter_id_unclear:         -> jru-identification
elif representation_loose:         -> jru-theory-model
elif contribution_fuzzy:           -> jru-literature-positioning
else:                              -> jru-topic-selection
```
