---
name: red-identification-strategy
description: Use when making the inferential backbone of a Review of Economic Dynamics (RED) manuscript credible, adapting to the paper type. For theoretical/computational papers it covers model assumptions, regularity conditions, and what disciplines the parameters; for empirical dynamic papers it covers causal design. RED's scope spans all three, so this skill branches accordingly.
---

# Identification & Model Logic for RED (red-identification-strategy)

## When to trigger

- Establishing why the paper's central claim is credible, before robustness
- Unsure whether RED expects a causal-design argument or a model-assumptions argument
- A computational paper where "identification" means parameter discipline, not instruments

## Branch by paper type (RED takes all three)

### Theoretical / computational dynamic models
The credibility question is about **assumptions, existence, and discipline**, not instruments:

- State the **model assumptions** and **regularity conditions** explicitly (preferences, technology,
  stationarity, boundedness, transversality); flag where existence/uniqueness of equilibrium is proved
  or assumed.
- Make **proof exposition** clean: state results as propositions, separate assumptions from claims,
  and put long proofs in an appendix while keeping the intuition in the body.
- Show **parameter discipline** — which parameters are calibrated to data targets, which are estimated,
  and which are free; justify each so results are not an artifact of free parameters.
- Discuss **generality**: what survives relaxing key assumptions, and where the result is knife-edge.

### Methodological / computational-method papers
- State the method's **regularity conditions** and where they bind; characterize **accuracy** and
  **convergence** of the numerical solution; report **asymptotics** where the method estimates parameters.
- Provide **Monte Carlo / numerical experiments** that show the method works under known data-generating processes.

### Empirical dynamic papers
- Make the **causal/identification design** explicit (the source of variation, the exclusion logic,
  the dynamic structure being estimated — e.g., VAR identification, local projections, structural estimation).
- Tie the empirical object back to **what it disciplines in the dynamic model**.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). RED is quantitative macro — mostly structural/calibration, which is outside this causal-inference toolchain; apply the chain to its empirical/reduced-form papers.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The right branch is chosen for the paper type
- [ ] Assumptions/conditions (theory) or identifying variation (empirics) are explicit and defended
- [ ] Parameter discipline is documented; results are not driven by undisciplined free parameters
- [ ] Generality / accuracy / robustness of the core claim is characterized

## Anti-patterns

- Importing reduced-form "identification" language into a calibrated model where it does not apply
- Hiding free parameters or equilibrium-existence gaps
- Asserting generality without showing what relaxing the assumptions does

## Parameter-discipline table

For quantitative papers, create a table with one row per key parameter:

| Parameter | Value | Source/target | Free or disciplined? | Sensitivity shown? |
|---|---|---|---|---|

Any parameter that is free and influential needs a sensitivity check or a narrower claim.

## Model-solution audit block

For computational claims, attach an audit record so a referee can see what the numbers rest on:

```text
SOLUTION AUDIT — [model name]
  Method:       EGM on the household problem; sequence-space Jacobian for GE transitions
  State space:  assets 250 pts (log-spaced); productivity 7-state Rouwenhorst
  Convergence:  policy-function sup-norm < 1e-9; market clearing < 1e-7
  Accuracy:     max log10 |Euler error| = -4.3 (off-grid simulation, 100k agents)
  Refinement:   headline counterfactual moves < 0.5% when grids are doubled
  Existence:    stationary-equilibrium existence proved/cited in Appendix A
```

Any blank line means the matching claim in the text should be weakened until the line can be filled.

## Worked discipline review: a search-and-matching draft

A draft calibrates a Diamond–Mortensen–Pissarides economy and claims wage rigidity explains unemployment
volatility. Illustrative review of its parameter discipline:

- **Matching elasticity 0.5**, externally set from the literature — acceptable, but the volatility claim
  is sensitive to it, so a ±0.15 band belongs in the robustness section.
- **Replacement rate 0.71**, internally calibrated to market tightness — a RED referee will notice this
  sits near the Hagedorn–Manovskii region where small match surplus generates volatility mechanically;
  report the result at a conventional 0.4 as well.
- **Rigidity parameter calibrated to the very volatility moment being explained** — circular. Move that
  moment out of the target set, or downgrade "explains" to "is consistent with".

## Credibility objections RED referees raise

| Objection | Branch | Fix |
|---|---|---|
| "A free parameter drives the result" | quantitative | sensitivity table or a narrower claim |
| "Equilibrium existence is assumed silently" | theory | state it as an assumption or prove it |
| "Accuracy not stress-tested at the calibrated point" | computational | Euler/den Haan check at exactly that parameterization |
| "The reduced-form estimate maps to no model object" | empirical | name the structural parameter or moment the estimate disciplines |

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — solvers and estimation toolkits
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope sources
