---
name: ecj-identification
description: Use when the empirical identification strategy is the bottleneck for a The Economic Journal (EJ) manuscript — quasi-experimental designs (DID, IV, RDD, event study) or structural estimation. Stress-tests the design and its economic interpretation before drafting tables; it does not write the model from scratch (see ecj-theory-model).
---

# Identification & Economic Interpretation (ecj-identification)

## When to trigger

- The empirical core is OLS + controls with no defended causal claim
- Staggered DID estimated with TWFE without addressing heterogeneity-bias critiques
- IV with a weak first stage or a thin exclusion argument
- Structural estimation where the source of parameter identification is not spelled out
- A clean causal effect exists but its *economic* interpretation, and its general relevance, are not pinned down

## The EJ bar: credible identification AND broad economic meaning

EJ accepts both reduced-form and structural work across all fields, but the bar has two parts that must *both* clear:

1. **Credible identification** — the estimate isolates the causal/structural object you claim, to a standard a demanding referee accepts.
2. **Economic meaning of broad interest** — the estimate maps onto a parameter or margin that economists *outside the subfield* care about. A precisely identified but parochial effect is a field-journal paper here, because EJ's defining bar is broad relevance.

Reduced-form work should connect to a model or mechanism (see `ecj-theory-model`); structural work must make its identification transparent. Because EJ runs a **reproducibility check via the EJ Data Editor** before final acceptance (DCAS-endorsed; deposit to Zenodo — see `ecj-replication-package`), every identification claim must come from code that actually executes and reproduces. EJ's exposition premium also applies here: the identifying assumption must be stated in plain words a generalist can evaluate, not hidden in notation.

## Design priority (strong → acceptable)

The right design is dictated by the economics, not by fashion. As a rough ordering of what travels well at EJ:

1. **Quasi-experiment (DID, RDD, event study) mapped to a model prediction** — reduced form whose coefficient has a stated, broadly interesting economic interpretation.
2. **Structural estimation tied to a model** — when the question is about a deep parameter, welfare, or counterfactuals; identification of parameters argued explicitly.
3. **Strong IV with a theory-grounded exclusion restriction** — first-stage strength plus an economic story for exogeneity and exclusion.
4. **RCT / lab evidence interpreted through a mechanism**, with external-validity discussion.
5. **OLS with a serious endogeneity discussion** — acceptable in theory-empirics or descriptive-with-model papers, not as the sole causal claim.

## Branch paths

### Branch A — DID / event study
- Staggered timing? Diagnose negative-weighting with Goodman-Bacon; estimate with a heterogeneity-robust estimator (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille, or Borusyak–Jaravel–Spiess).
- Pre-trends: show the event-study plot; do not lean only on a low-power joint pre-trend test — argue economically why pre-trends are flat.
- Map the coefficient to a model object: what does the ATT *mean* economically, and for whom does it generalize?
- Placebo: randomize treatment timing/units; report the distribution.

### Branch B — IV
- First-stage strength: report effective F (Montiel Olea–Pflueger); if weak, use Anderson–Rubin / weak-IV-robust CIs.
- Exclusion: defend in three registers — theory, institutional detail, and a placebo/over-identification check.
- Report the reduced form, not just 2SLS.
- State the LATE interpretation: whose behavior does the instrument move, and is that the population the economics is about?

### Branch C — RDD
- McCrary / `rddensity` manipulation test.
- Optimal bandwidth (Calonico–Cattaneo–Titiunik) plus ≥3 bandwidth-robustness checks; bias-corrected CIs.
- Covariate smoothness at the cutoff; placebo cutoffs.

### Branch D — Structural estimation
- State the model's microfoundations and the moments/variation that identify each parameter (a "what identifies what" paragraph is expected).
- External validation: do estimated parameters match independent evidence or untargeted moments?
- Provide counterfactuals and welfare, and show sensitivity to key assumptions.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). The Economic Journal is general-interest economics; the DiD/IV/RDD chain serves its broad applied lane.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Identifying assumption stated in one plain sentence and defended economically
- [ ] Design-appropriate diagnostics done (pre-trends / first-stage F / manipulation test / parameter identification)
- [ ] Placebo or falsification test reported
- [ ] Standard errors clustered at the level of treatment assignment, justified
- [ ] The estimated object is given an explicit economic interpretation of broad interest
- [ ] Reduced-form work connects to a model or mechanism; structural work makes identification transparent
- [ ] Selection / general-equilibrium / external-validity threats to interpretation acknowledged
- [ ] The numbers come from code that runs (EJ Data Editor will rerun it)

## Anti-patterns

- TWFE on staggered treatment with no discussion of heterogeneity bias
- A precisely identified effect with no statement of what it means, or of why a generalist should care
- IV exclusion asserted ("we argue the instrument is exogenous") without evidence
- Structural estimates with no "what identifies what" discussion — the model becomes a black box
- Clustering at the wrong level to manufacture significance
- An identification claim resting on numbers the deposited code cannot reproduce

## Output format

```
【Design】structural / DID / IV / RDD / event study / other
【Identifying assumption】one plain sentence
【Economic interpretation of the estimate】... (and why it is of broad interest)
【Diagnostics done】[pre-trends, first-stage F, manipulation, param-ID, ...]
【Diagnostics missing】[...]
【Clustering level】... (justification)
【External-validity / GE caveats】...
【Next】ecj-theory-model (if mechanism not yet formalized) or ecj-robustness
```
