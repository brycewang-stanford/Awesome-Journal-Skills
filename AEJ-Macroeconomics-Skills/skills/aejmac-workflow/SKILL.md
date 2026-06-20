---
name: aejmac-workflow
description: Use when deciding which aejmac-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for an American Economic Journal: Macroeconomics (AEJ: Macro) submission. Routes — it does not replace — the specialized skills.
---

# AEJ: Macro Workflow Router (aejmac-workflow)

## Overview

This is the router. It tells you **which aejmac-* skill to use at the current stage** of a manuscript aimed at the *American Economic Journal: Macroeconomics* (AEJ: Macro) — the **American Economic Association's** quarterly, broad-interest macro journal (founded 2009; one of four AEJs). AEJ: Macro rewards papers that bring **quantitative discipline and policy relevance** to a substantive macro question across growth, business cycles, monetary and fiscal policy, labor-macro, international macro, and macro-finance.

The defining feature of AEJ: Macro is **methodological breadth**: it publishes both **quantitative-theoretical** work (DSGE, heterogeneous-agent, structural estimation, calibrated models) **and** **identified-empirical** work (SVAR, local projections, narrative identification, micro-data macro). A paper does not have to be one or the other — the bar is that whichever tool you use, the **mapping from model/data to the macro conclusion is disciplined**.

Default assumption: unless the user says otherwise, treat the target as AEJ: Macro. Operational tells that you are at AEJ: Macro and not a field-macro or general-interest sibling: submission via the **AEA submission system**; a **membership-scaled submission fee** (member/nonmember × income tier; 检索于 2026-06，以官网为准); **single-blind** external review managed by the editor/coeditors; **JEL codes** required; the **AEA Data Editor** (Lars Vilhuber) runs a **pre-publication reproducibility check** — covering simulation and calibration code, not only regression scripts — with materials deposited at the **AEA Data and Code Repository on openICPSR**. Editor as of 2026: **Ayşegül Şahin** (检索于 2026-06；以官网为准). Re-verify volatile specifics on the official AEA pages.

## When to trigger

- The user asks "what should I do next?"
- A draft needs its current bottleneck diagnosed
- Work is ping-ponging between model/estimation, identification, framing, writing, and the response letter
- An AEJ: Macro decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Question feels narrow / field-macro / not broad-interest | `aejmac-topic-selection` |
| Contribution vs. the macro frontier is fuzzy or undersold | `aejmac-literature-positioning` |
| Empirical identification (SVAR / LP / narrative / IV) is shaky | `aejmac-identification` |
| A quantitative model needs calibration / estimation discipline | `aejmac-theory-model` |
| Headline number not shown robust to specification / sample / tuning | `aejmac-robustness` |
| Exhibits are dense; IRFs/fan charts/fit plots unclear | `aejmac-tables-figures` |
| Prose buries the question; abstract/intro do not land | `aejmac-writing-style` |
| Data/code/simulation deposit, README, or AEA Data Editor prep | `aejmac-replication-package` |
| Want to anticipate referee objections / desk-reject odds | `aejmac-referee-strategy` |
| Ready to submit via the AEA system; need a preflight | `aejmac-submission` |
| Received an R&R; need a response-letter strategy | `aejmac-rebuttal` |

## Default order

1. `aejmac-topic-selection` — lock the broad-interest macro question
2. `aejmac-literature-positioning` — stake the contribution vs. the macro frontier
3. `aejmac-identification` — SVAR / LP / narrative / IV credibility (empirical branch)
4. `aejmac-theory-model` — calibration / structural-estimation discipline (quantitative branch)
5. `aejmac-robustness` — show the headline number is not fragile
6. `aejmac-tables-figures` — IRFs, fan charts, model-fit exhibits done right
7. `aejmac-writing-style` — make the idea land (abstract + intro last; ≤100-word abstract)
8. `aejmac-replication-package` — assemble the AEA-compliant data/code/simulation package
9. `aejmac-referee-strategy` — pre-empt the objections macro referees raise
10. `aejmac-submission` — AEA system preflight
11. `aejmac-rebuttal` — after the R&R

> `aejmac-identification` and `aejmac-theory-model` are siblings, not a strict order: an empirical paper leans on the former, a quantitative paper on the latter, and a hybrid paper visits both. `aejmac-writing-style` is a late-stage polish; do not rewrite the intro before the headline number settles.

## Anti-patterns

- Skipping `aejmac-replication-package` until acceptance — the AEA Data Editor verifies **before** publication, and for macro this includes simulation/calibration code, not just data cleaning
- Letting `aejmac-tables-figures` polish IRFs while the identification or calibration is still moving
- Treating AEJ: Macro like a field outlet (J. Monetary Economics / RED) — the bar is **broad macro interest plus AEA process**, not just technical correctness for specialists
- Choosing a method (DSGE vs. SVAR vs. LP) before deciding what the paper must *measure* — let the question pick the tool

## Routing by paper archetype

AEJ: Macro spans several macro branches, and the bottleneck differs by branch. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| empirical shock-identification (monetary/fiscal) | SVAR / narrative / proxy-VAR credibility | `aejmac-identification` |
| dynamic-effects estimation | local-projection specification + inference | `aejmac-identification` → `aejmac-robustness` |
| quantitative DSGE / HANK | calibration targets + parameter identification | `aejmac-theory-model` |
| structural estimation | what data moments identify each parameter | `aejmac-theory-model` → `aejmac-robustness` |
| model + evidence hybrid | does the model match the identified empirical response | `aejmac-identification` + `aejmac-theory-model` |

## Worked routing example (illustrative)

A user says: "My HANK model matches the data, but a referee says my monetary-shock series is not credibly exogenous and the consumption response is not robust to the lag length." That is two distinct AEJ: Macro pushbacks — *identification of the shock* (owned by `aejmac-identification`, narrative/high-frequency branch) and *fragility of the dynamic response* (owned by `aejmac-robustness`). The model side (`aejmac-theory-model`) only matters once the empirical target it is matched to is credible. Route to identification first; once the shock and the response settle (say the peak MPC-driven consumption response stabilizes at 1.4%, 90% CI [0.9, 1.9], illustrative), return to `aejmac-tables-figures` and `aejmac-rebuttal`.

## Minimal decision snippet

```
if decision_letter_arrived:          -> aejmac-rebuttal
elif ready_to_submit:                -> aejmac-submission
elif anticipating_referees:          -> aejmac-referee-strategy
elif data_code_deposit:              -> aejmac-replication-package
elif exhibits_unclear:               -> aejmac-tables-figures
elif headline_fragile:               -> aejmac-robustness
elif model_calibration_estimation:   -> aejmac-theory-model
elif shock_or_design_shaky:          -> aejmac-identification
elif claim_or_positioning_fuzzy:     -> aejmac-literature-positioning
else:                                -> aejmac-topic-selection
```
