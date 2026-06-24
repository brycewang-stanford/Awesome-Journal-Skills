---
name: ier-identification
description: Use when the identification argument is the bottleneck for an International Economic Review (IER) manuscript — structural parameter identification, empirical causal identification, or for a theory result, what makes it tightly pinned. Stress-tests the data-to-object mapping to IER's rigor bar; it does not run the estimation.
---

# Identification Strategy (ier-identification)

## When to trigger

- A structural model's parameters are estimated but it is unclear *what in the data* identifies each one
- The headline counterfactual is suspected to be driven by a calibrated elasticity nobody defends
- An empirical causal claim rests on OLS + controls, or TWFE on staggered timing
- A referee says the result is "calibration in disguise" or "not credibly identified"
- For a theory paper, you need to confirm the result is *pinned* (which assumption identifies it) — though the tightness craft lives in `ier-theory-model`

## The IER identification bar

IER prizes a **clean model-to-evidence link**, so identification is judged by one test: is the **mapping from data to the object of interest explicit and defended**? The object differs by branch, and so does what "identified" means. Pick the branch and make the mapping transparent — a referee should be able to point at the data feature that moves each estimate.

### Branch A: Structural / quantitative (the IER core)

This is where most IER identification debates happen. The failure mode is treating "the estimator converged" as if it were identification.

- **Name what identifies each parameter.** Tie every structural parameter to a specific data moment or feature, and argue identification from the model's structure — e.g., "the trade elasticity is identified by the response of bilateral flows to tariff variation," not "by the GMM objective."
- **Targeted vs. untargeted moments.** Report fit to targeted moments; then show untargeted moments the model was *not* fit to but still matches — this is the out-of-sample discipline IER readers want.
- **Sensitivity / informativeness.** Report a sensitivity matrix (à la Andrews–Gentzkow–Shapiro) so readers see which moment moves which parameter, and by how much.
- **Estimation regularity.** State the objective (MLE / GMM / MSM / SMM / indirect inference), starting values, tolerances, and global-optimum evidence (multi-start). Show Monte Carlo recovery of known parameters.
- **Counterfactual validity.** Argue the estimated parameters are policy-invariant enough for the counterfactual you run (the Lucas critique applies); show they are not functions of the policy you change.

### Branch B: Empirical causal design (applied micro)

- **DID / event study.** With staggered adoption, move beyond TWFE (Callaway–Sant'Anna, Sun–Abraham, de Chaisemartin–D'Haultfœuille); show a clean event study with leads; report a Goodman-Bacon decomposition.
- **IV.** Strong first stage; with weak instruments use Anderson–Rubin / weak-IV-robust sets; defend exclusion in theory, institutions, and falsification.
- **RDD.** Density test (McCrary / Cattaneo–Jansson–Ma); optimal bandwidth + robustness; covariate smoothness; bias-corrected CIs.
- Cluster at the assignment level; address few-cluster issues (wild-cluster bootstrap).

### Branch C: Econometric method / theory

- Identification here means the conditions under which the estimand is point- (or partially-) identified. State them as assumptions, show what the data must satisfy, and connect to the tightness craft in `ier-theory-model`.
- Where point identification fails, do not abandon the object — characterize the **identified set** and show how it shrinks with stronger but credible assumptions. IER referees respect honest partial identification over an overclaimed point estimate.

### The boundary with ier-theory-model

These two skills divide one question. `ier-theory-model` asks "is the result tight and general as a *theoretical* object" — which assumptions are load-bearing, is the comparative static signed. `ier-identification` asks "is the object recoverable from *data*" — what moment moves the parameter, what variation supports the causal claim. A structural paper needs both: a tight model whose parameters are also empirically pinned. When a referee says "this is calibration in disguise," that is an identification failure even if the model is theoretically immaculate — route it here, not to `ier-theory-model`.

### The sensitivity matrix as the IER identification exhibit

For structural papers, the most persuasive single piece of identification evidence is a **sensitivity matrix** (Andrews–Gentzkow–Shapiro) showing, for each parameter, how its estimate would move if each targeted moment shifted. This converts the abstract claim "the model is identified" into a checkable map: the referee sees that the trade elasticity is driven mainly by the tariff-flow moment, the fixed cost by the extensive-margin moment, and so on. When a parameter's row shows it responds to *every* moment a little and *no* moment a lot, that is the data signature of weak identification — and reporting it honestly, with the corrective (a better moment, or a partial-identification statement), is far stronger than hiding it behind a converged objective.

### Distinguishing calibration from estimation cleanly

IER's structural readers draw a sharp line between *estimated* parameters (recovered from data with stated identification) and *calibrated/external* parameters (set from outside the model). Both are legitimate, but conflating them invites the "calibration in disguise" reject. State explicitly which parameters are estimated and which are external; for each external one, cite the source and carry it into the `ier-robustness` range analysis. The failure mode is presenting an externally-set parameter as if the model estimated it — referees notice, and the credibility of the whole exercise drops.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). IER is theory-forward and quantitative; the chain below serves its empirical lane — structural / quantitative estimation uses the field's own solvers.

1. `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to list
   the checks the design still owes.
2. **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
   `honest_did_from_result` (the pre-trend test is low-power, Roth 2022).
3. **IV:** `effective_f_test` + an `anderson_rubin_ci` (valid under weak instruments),
   not a 2SLS t-stat alone.
4. **RDD:** `rdrobust` (bias-corrected) + `rddensity` / `mccrary_test` for manipulation.
5. **OVB:** `oster_delta` / `sensemakr` — how strong a confounder would have to be.

Report the economic magnitude; route the full battery to the appendix; keep every
number reproducible. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md). If StatsPAI/Stata are not connected, adapt the
vendored `resources/code/` skeleton and flag any unverified number.
## Checklist

- [ ] Branch chosen; the data-to-object mapping stated in one sentence
- [ ] Structural: each parameter tied to an identifying moment/feature; sensitivity matrix + Monte Carlo recovery shown
- [ ] Structural: untargeted-moment validation reported; counterfactual policy-invariance argued
- [ ] Empirical: design-appropriate diagnostics (pre-trends / density / first-stage / balance); modern estimator where TWFE would bias
- [ ] Inference: clustering at the assignment level; few-cluster correction if needed
- [ ] The claim never exceeds what the identification supports; what it does NOT identify is stated

## Anti-patterns

- "The estimator converged" or "the likelihood is maximized" presented as identification (structural)
- A headline counterfactual driven by a calibrated parameter with no identifying argument
- TWFE on staggered treatment with no heterogeneity-bias discussion (empirical)
- Running a policy counterfactual without arguing the parameters are policy-invariant
- Reporting only targeted-moment fit and calling the model validated

## Worked vignette: identifying a trade elasticity (illustrative)

A quantitative trade model is estimated and the welfare gain from a tariff cut is the headline. A referee asks what identifies the trade elasticity. A weak answer points at the GMM objective. An IER answer points at a data feature: the elasticity is identified by how bilateral flows respond to plausibly-exogenous tariff variation, and the sensitivity matrix shows that this moment moves the elasticity from, say, 4.0 to 5.5 (illustrative) — making identification visible. Pair it with Monte Carlo recovery (simulated data returns the true elasticity within a few percent) and an untargeted moment the model still matches.

## Referee pushback mapped to the identification fix

- *"This is calibration in disguise — not credibly identified."* → Show the sensitivity matrix tying each parameter to a moment; report untargeted-moment fit.
- *"Your counterfactual assumes policy-invariant parameters you never defend."* → Argue invariance (Lucas critique); show the parameters are not functions of the policy you change.
- *"Staggered TWFE is biased here."* → Re-estimate with Callaway–Sant'Anna / Sun–Abraham; show flat event-study leads and a Goodman-Bacon decomposition.
- *"The exclusion restriction is asserted, not defended."* → Defend it in theory, institutions, and a falsification test; if instruments are weak, report Anderson–Rubin sets.

## Output format

```text
【Journal】International Economic Review
【Skill】ier-identification
【Branch】structural / empirical-causal / econometric-method
【Data-to-object mapping】one sentence: what feature identifies the key object
【Identification evidence】[sensitivity matrix + Monte Carlo / pre-trends+first-stage+density / formal conditions]
【Out-of-sample / falsification】untargeted moments or placebo/falsification shown? [Y/N]
【Counterfactual / external validity】policy-invariance or generalizability argued? [Y/N]
【What it does NOT identify】the object(s) out of reach
【Verdict】credible / needs-work
【Next skill】ier-robustness
```
