---
name: aejmic-identification
description: Use when the question is what makes the result tight or what the data identify for an American Economic Journal: Microeconomics (AEJ: Micro) manuscript — covering both (a) structural/empirical-IO and experimental identification and (b) for pure theory, which assumptions drive the result and how robust the mechanism is. Stress-tests credibility; it does not build the model (see aejmic-theory-model).
---

# Identification & What Makes the Result Tight (aejmic-identification)

AEJ: Micro is theory-first, so "identification" here is **two things**. For pure theory it means: **which assumptions are doing the work**, and how tight/robust the mechanism is. For structural and experimental work it means the standard **data-to-object mapping**. Pick the branch.

## When to trigger

- (Theory) A referee asks whether the result is a knife-edge artifact of one assumption
- (Theory) You cannot say cleanly which primitive drives the comparative static
- (Structural) Parameters are estimated but it is unclear *what in the data* identifies them
- (Experimental) The estimand or the assumptions behind the treatment effect are not pinned down

## Branch A: Pure theory — what makes the result tight

The AEJ: Micro bar is that the reader sees **exactly which assumption is load-bearing** and how far the mechanism extends.

- **Decompose the assumptions.** For each substantive assumption, ask: is the result *false* without it, *weaker* without it, or *unchanged* (then it was WLOG — say so)? The result is "tight" when you can name the assumption that breaks it.
- **Comparative statics as identification.** Show the sign/magnitude of the key comparative static and **what primitive drives it** (single-crossing? a supermodularity? a curvature condition?). Monotone-comparative-statics tools (Topkis, Milgrom–Shannon) make the driver explicit.
- **Necessity, not just sufficiency.** Where you can, show the assumption is *necessary* (a counterexample when it fails), not merely sufficient — this is what makes a characterization tight.
- **Robustness of the mechanism** (then hand to `aejmic-robustness` for full extensions): does the result survive a small perturbation of the information structure, the timing, or the type distribution?

## Branch B: Structural / empirical IO

- **Name what identifies each parameter.** Tie parameters to specific data features / moments; argue identification from the model's structure, not "the estimator converged."
- **Targeted vs. untargeted moments;** report a sensitivity/informativeness measure so readers see which data move which parameters.
- **Estimation regularity:** objective (MLE/GMM/MSM), starting values, tolerances, multi-start; Monte Carlo recovery of known parameters.
- **Counterfactual validity:** argue the estimated parameters are policy-invariant enough for the counterfactual (Lucas critique).
- For reduced-form companions, use design-appropriate diagnostics (pre-trends, first-stage strength, density tests) and **report SEs, not asterisks**.

## Branch C: Experimental (theory-grounded)

- **Design maps to the model:** each treatment isolates a model primitive or prediction; state the **estimand**.
- **Pre-registration** in a recognized registry where applicable; report deviations; include instructions/transcripts.
- Randomization balance; attrition (Lee bounds if differential); multiple-hypothesis adjustment; external-validity scope.

## Checklist

- [ ] Branch chosen; the "what makes it tight / what identifies it" question answered in one sentence
- [ ] Theory: each substantive assumption classified (false/weaker/WLOG without it); the load-bearing one named
- [ ] Theory: key comparative static signed with its driving primitive; necessity shown where possible
- [ ] Structural: each parameter tied to identifying moments; sensitivity + Monte Carlo recovery
- [ ] Experimental: estimand stated; pre-registered; balance/attrition/MHT handled
- [ ] Inference (applied): SEs / coverage sets, never asterisks; clustering correct

## Anti-patterns

- (Theory) A result whose driving assumption is never identified — "it just works"
- (Theory) Claiming a characterization is tight without a counterexample when the assumption fails
- (Structural) "The estimator converged" presented as identification
- (Structural) A counterfactual on calibrated parameters with no policy-invariance argument
- (Experimental) No pre-registration or no stated estimand; significance asterisks instead of SEs

## Worked vignette (illustrative)

A matching paper proves stability is preserved under a new preference domain. A referee suspects it rides on a substitutability condition. The AEJ: Micro answer names it: "Substitutability is load-bearing — without it, Example 3 exhibits an empty core; with the weaker 'unilateral substitutes' condition the existence result survives but uniqueness fails." That sentence makes the result tight: the necessary assumption is named, and the cost of relaxing it is shown.

## Output format

```
【Branch】theory / structural / experimental
【What makes it tight / data-to-object】one sentence
【Load-bearing assumption(s) or identifying moments】[...]
【Tightness evidence】counterexample-on-failure / sensitivity+Monte Carlo / balance+estimand
【What it does NOT establish】[...]
【Next step】aejmic-robustness (extensions/edge cases)
```
