---
name: aejmac-theory-model
description: Use when the quantitative model is the bottleneck for an American Economic Journal: Macroeconomics (AEJ: Macro) manuscript — DSGE, New Keynesian, heterogeneous-agent (HANK / Aiyagari-Bewley), or structural estimation — and calibration, parameter identification, solution accuracy, or counterfactual validity need discipline. For empirical shock identification see aejmac-identification.
---

# Quantitative Theory & Model Discipline (aejmac-theory-model)

## When to trigger

- Parameters are calibrated or estimated but it is unclear *what disciplines* each one
- A DSGE/HANK model is solved but the solution method / accuracy is unstated
- A counterfactual or welfare number is reported with no validity argument (Lucas critique)
- Untargeted moments are never shown, so the model's fit is asserted not demonstrated
- You are unsure the model clears AEJ: Macro's quantitative-discipline bar

## The AEJ: Macro model bar

AEJ: Macro welcomes quantitative-theoretical macro, but the standard is **discipline, not decoration**: a calibration or structural estimate must be tied to data, the solution must be accurate enough for the claim, and the counterfactual must be defensible. The model exists to deliver a **broad-interest macro quantity** (a multiplier, a welfare cost, a share of inequality, a propagation magnitude), not to display machinery.

## Discipline paths

### Path A: Calibration discipline
- **Source every parameter.** Externally calibrated (cited micro/macro estimates) vs. internally calibrated (matched to targeted moments) — label each and give the target.
- **Targeted moments table.** Show data vs. model on the moments you matched.
- **Untargeted-moment validation.** Show the model matches moments it was *not* asked to match — this is the credibility payoff for calibration.
- **Sensitivity.** Report how the headline quantity moves with the key parameters (and which moment moves which parameter).

### Path B: Structural estimation discipline
- **Name what identifies each parameter** — the data feature / moment, not "the likelihood." Report a sensitivity / informativeness measure (e.g., a sensitivity matrix) so readers see which data move which parameter.
- **Estimator stated** (MLE / GMM / SMM / indirect inference / Bayesian) with priors (if Bayesian), starting values, tolerances, and multi-start evidence of a global enough optimum.
- **Monte Carlo recovery**: simulated data return the true parameters.

### Path C: Solution accuracy & numerics
- State the **solution method** (perturbation order, projection, value-function iteration, sequence-space Jacobian for HANK) and **why it suffices** for the nonlinearity/size of shock studied.
- For occasionally-binding constraints (ZLB, borrowing limits) or large shocks, justify global vs. local methods.
- Report accuracy diagnostics (Euler-equation errors, grid/refinement checks) where the claim depends on accuracy.
- Set and report seeds for any simulation.

### Path D: Counterfactual & welfare validity
- Argue the estimated/calibrated parameters are **policy-invariant** enough for the counterfactual (Lucas critique); show they are not functions of the policy you change.
- State the **welfare metric** (consumption-equivalent, etc.) and carry uncertainty into the counterfactual quantity.
- For HANK: be explicit about the distributional channel and the role of the MPC distribution / liquidity.

## Checklist

- [ ] Every parameter labeled external vs. internal, with its source/target
- [ ] Targeted-moment fit shown; untargeted-moment validation shown
- [ ] Structural: each parameter tied to identifying moments; sensitivity + Monte Carlo recovery
- [ ] Solution method named and justified for the nonlinearity/shock size; accuracy diagnostics where needed
- [ ] Seeds reported; numerics reproducible for the AEA Data Editor (simulation code counts)
- [ ] Counterfactual: policy-invariance argued; welfare metric stated with uncertainty
- [ ] The model delivers one memorable, broad-interest macro quantity

## Anti-patterns

- "We calibrate to standard values" with no targets and no sensitivity
- Reporting targeted-moment fit only, never untargeted moments (fit asserted, not validated)
- A first-order perturbation used to study a large nonlinear shock (ZLB, big crisis) without justification
- A welfare/counterfactual number with no policy-invariance argument
- Treating estimation convergence as identification ("the optimizer found a minimum")
- A model with rich machinery but no headline macro quantity a general reader remembers

## Worked vignette: disciplining a HANK fiscal multiplier (illustrative)

A HANK model reports a fiscal multiplier of 1.3. A referee asks what disciplines it. The AEJ: Macro answer ties the multiplier to the **MPC distribution**: the model is calibrated to match the empirical distribution of MPCs (targeted), and then matches the *untargeted* share of hand-to-mouth households and the consumption response to a transfer from independent micro evidence. A sensitivity check shows the multiplier moves from 1.1 to 1.5 as the liquid-wealth target varies over its empirical range — making visible that the multiplier is governed by liquidity, not a free parameter. Solution by sequence-space Jacobian; Euler-error diagnostics reported (illustrative).

## Output format

```
【Model type】NK-DSGE / HANK / Aiyagari-Bewley / structural-estimation
【Headline quantity】... (with units)
【Parameter discipline】external vs. internal; targeted + untargeted moments
【Identification (structural)】moment ↔ parameter; sensitivity; MC recovery
【Numerics】solution method + why it suffices; accuracy diagnostics; seeds
【Counterfactual validity】policy-invariance + welfare metric + uncertainty
【Next step】aejmac-robustness
```
