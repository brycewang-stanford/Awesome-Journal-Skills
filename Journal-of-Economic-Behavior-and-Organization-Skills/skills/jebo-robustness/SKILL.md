---
name: jebo-robustness
description: Use when a Journal of Economic Behavior & Organization (JEBO) result may be fragile to demand effects, multiple comparisons, specification, or tuning. Organizes robustness by the behavioral threat each check addresses — for experiments, observational designs, and simulations; it does not redesign the identification or write the prose.
---

# Robustness Strategy (jebo-robustness)

## When to trigger

- An experiment has several treatment arms / outcomes and you have not corrected for multiplicity
- A referee could attribute the effect to **experimenter demand**, confusion, or order effects
- An observational result moves with controls, sample windows, or estimator choice
- An agent-based result might be an artifact of grid, seed, or tuning choices
- You have a long, unstructured "robustness" appendix and no map from check to threat

## Organize robustness by behavioral threat, not by appendix list

At JEBO the right question is never "did we run enough checks?" but "for each way this could *not* be the behavioral mechanism, did we show it survives?" Build a threat → check map. The threats differ sharply across the four archetypes.

### Experiments (lab/online/field)

| Threat | Check JEBO referees expect |
|--------|----------------------------|
| Experimenter demand | demand-treatment bounds (de Quidt-style), neutral framing, obfuscated objective |
| Multiple comparisons | pre-registered primary outcome; MHT correction (Romano–Wolf, List–Shaikh–Xu, BH) across arms/outcomes |
| Comprehension / confusion | results hold among subjects passing comprehension checks |
| Order / sequence effects | randomize order; show within-order stability |
| Subject pool / platform | replicate across pools (student vs. Prolific vs. field); attention screens on online samples |
| Bots / inattentive online subjects | attention checks, completion-time filters, duplicate-IP screening |
| Selection / attrition | balance among completers; Lee bounds if differential |

### Observational behavioral empirics

- Specification curve / multiverse over reasonable controls and windows; show the headline is not a knife-edge.
- Inference robustness: clustering level, wild-cluster bootstrap with few clusters, randomization inference where natural.
- Placebo / falsification: effect absent where the mechanism predicts none; pre-trend tests for DID.
- Sensitivity to unobservables (Oster δ; Rambachan–Roth honest-DID for parallel-trend violations).

### Simulation / agent-based

- Parameter sweeps over the behavioral-rule space; report the region where the result holds.
- Seed sensitivity (many runs, report distribution not one path); grid/step-size invariance.
- Sensitivity of emergent regularities to the behavioral rule chosen (e.g., reinforcement vs. EWA learning).

## Distinguish "the effect is real" from "the mechanism is the claimed one"

JEBO's distinctive robustness demand is **mechanism robustness**: even a real, replicable effect can be driven by a *different* behavioral channel than claimed. Where possible, add a check that separates your mechanism from the leading alternative (a moderation test the rival channel does not predict, a mediation analysis with the caveats stated, or a treatment that shuts the rival channel off).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEBO spans behavioral/experimental and applied micro; randomization inference for experiments, DiD/IV for observational claims.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Every robustness exhibit is labeled with the specific threat it neutralizes
- [ ] Experiments: demand effects bounded; primary outcome pre-registered; MHT correction reported
- [ ] Comprehension/order/subject-pool/attention threats addressed for the relevant design
- [ ] Observational: spec-curve + inference robustness + placebo/falsification + unobservables sensitivity
- [ ] Simulation: parameter sweeps + seed/grid sensitivity reported
- [ ] At least one check separates the claimed mechanism from the leading alternative
- [ ] The headline magnitude is reported with honest uncertainty across specifications

## Anti-patterns

- A robustness appendix that lists 20 regressions without saying what threat each rebuts
- Reporting only the cell that survives MHT, omitting the corrected p-values across all arms
- Treating "the effect replicates" as proof the *mechanism* is the claimed one
- Online experiments with no attention/bot screening
- An agent-based headline shown for a single seed and a single grid
- Hand-picked control sets that quietly maximize the coefficient

## Output format

```text
【Archetype】experiment / observational / simulation
【Threat → check map】
  - <threat 1> → <check>
  - <threat 2> → <check>
【Multiplicity】primary outcome pre-registered? MHT method:
【Mechanism vs. alternative】<test separating claimed channel from rival>
【Headline stability】<range of estimate across specs + uncertainty>
【Next step】jebo-tables-figures
```
