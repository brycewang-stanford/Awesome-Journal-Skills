---
name: jfe-identification
description: Use when the causal identification or inference design is the bottleneck for a Journal of Financial Economics (JFE) manuscript — natural experiments, IV, staggered DID, RDD, and explicit endogeneity/selection treatment. Stress-tests the design before drafting tables; it does not finalize factor construction or estimators (see jfe-empirical-design).
---

# Identification & Endogeneity (jfe-identification)

## When to trigger

- The empirical core is OLS + controls with endogeneity hand-waved away
- A DID uses two-way fixed effects with staggered adoption and you have not addressed the heterogeneous-treatment-effects bias
- Your IV's exclusion restriction or relevance is undefended
- Selection into the sample or treatment is plausible and unaddressed
- A referee could say "your X is endogenous to your Y"

## The JFE identification bar

JFE referees expect endogeneity and selection to be treated explicitly, and they expect every plausible alternative explanation to be ruled out — not waved away. Corporate-finance papers are held to a credible-design standard; asset-pricing papers to a disciplined-inference standard (see `jfe-empirical-design`). This skill covers the corporate-finance causal side; the design/estimator side lives in `jfe-empirical-design`.

JFE corporate finance descends from **Jensen & Meckling (1976), "Theory of the firm: Managerial behavior, agency costs and ownership structure"** — the agency-cost foundation and the journal's single most-cited paper. Modern reviewing keeps that demand for an economic *mechanism* but layers on a hard requirement for credible identification: a correlation between a governance/financing variable and an outcome will not survive review unless the endogeneity is convincingly handled. The best corporate-finance paper each year wins the **Jensen Prize**.

## Design priority (strong -> weaker)

1. **Natural experiment / exogenous shock + DID** (regulatory change, plausibly random policy, court ruling)
2. **Regression discontinuity** (a sharp rule with a running variable: index inclusion, covenant threshold, vote share)
3. **Instrumental variables** (strong first stage + a genuinely defensible exclusion restriction)
4. **Matching / entropy balancing + DID** (to reduce, not eliminate, selection)
5. **Structural estimation** (when the question is about deep parameters or counterfactuals)
6. OLS + controls (acceptable only with a frank endogeneity discussion and as a complement, rarely as the headline)

## Branches

### Branch A — DID / natural experiment
- Is adoption **staggered**? If so, two-way FE is biased under heterogeneous effects — use a modern estimator (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille, or stacked regression) and report a Goodman-Bacon decomposition.
- Parallel trends: plot the event study; show pre-trends are flat.
- Treatment exogeneity: argue why the shock is unrelated to the outcome's trajectory; address anticipation.
- Placebos: randomize treatment timing/units; falsification on unaffected outcomes.

### Branch B — IV
- First-stage strength: report the first-stage F / effective F (Olea–Pflueger); if weak, use weak-IV-robust inference (Anderson–Rubin).
- Exclusion: defend in three registers — theory, institutional detail, and a falsification/placebo.
- Report the reduced form and discuss the LATE/complier interpretation.
- Address whether the instrument itself could be endogenous.

### Branch C — RDD
- Manipulation test of the running variable (McCrary / `rddensity`).
- Optimal bandwidth (Calonico–Cattaneo–Titiunik) plus at least three bandwidth-sensitivity checks.
- Covariate continuity at the threshold; fuzzy-RDD first stage if applicable.

### Branch D — selection / sample construction
- State the population and every filter; show how filters could induce selection.
- Heckman / bounds / reweighting where selection is plausible — and say what each assumes.

### Branch E — structural
- Make the economic mechanism and identifying assumptions explicit.
- Provide a counterfactual and validate against reduced-form moments where possible.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFE is finance top-3 (with JF, RFS) — corporate-causal chain for corporate papers, factor-zoo haircut for asset pricing; attribute canon to the correct top-3 journal.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] The identifying variation is named and its exogeneity argued, not assumed
- [ ] Staggered DID uses a heterogeneity-robust estimator + Bacon decomposition
- [ ] Parallel-trends / continuity / first-stage-strength evidence is shown
- [ ] Placebo and falsification tests are run
- [ ] Standard errors are clustered at the level of treatment assignment
- [ ] Every alternative explanation a referee would raise has a counter-test
- [ ] Anticipation / pre-treatment manipulation is addressed

## Anti-patterns

- Two-way FE on staggered adoption with no acknowledgment of the bias literature
- An IV that is "an exogenous event times a lagged endogenous variable" — referees ask why the lag is exogenous
- "We argue the shock is exogenous" with no supporting evidence
- RDD reported at one bandwidth with no sensitivity
- Clustering at the wrong level (e.g., firm when treatment is at the state level)
- Treating endogeneity as a robustness footnote rather than the design's spine

## Output format

```
【Design】natural experiment / RDD / IV / matching+DID / structural / OLS
【Identifying variation】...
【Tests done】[parallel trends, first-stage F, McCrary, placebo, ...]
【Tests missing】[...]
【Cluster level】...
【Alternatives ruled out】[...] | 【Still open】[...]
【Next】jfe-empirical-design
```
