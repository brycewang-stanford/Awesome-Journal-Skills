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
