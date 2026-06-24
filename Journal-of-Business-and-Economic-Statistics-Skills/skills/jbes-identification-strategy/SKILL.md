---
name: jbes-identification-strategy
description: Use when the methodological core of a Journal of Business & Economic Statistics (JBES) paper is the bottleneck — assumptions, regularity conditions, asymptotic theory, and Monte Carlo design for a new estimator, test, or algorithm. Stress-tests the method's validity, not a causal design.
---

# Method Validity & Asymptotics (jbes-identification-strategy)

## When to trigger

- The estimator/test is proposed but its assumptions and limiting theory are not nailed down
- The asymptotic distribution, consistency, or rate is asserted without full conditions
- The Monte Carlo design does not yet show where the method holds and where it breaks
- For an applied paper, what parameter your method identifies (and under what conditions) is unclear

## What "identification" means at a methods journal

At JBES the load-bearing question is usually not a causal-design story but **whether the method delivers valid inference for its target under stated conditions**. Because JBES demands methodological novelty with **clear empirical relevance**, the assumptions cannot be so strong that no real data set — including the paper's own application — satisfies them. The credibility ladder a referee applies, strongest first:

1. **Identification of the target** — the parameter/functional is identified from the population moments the method uses, under stated conditions.
2. **Regularity conditions** — explicit (moment existence, smoothness, mixing/dependence, rate and rank conditions), each motivated and as weak as the result allows.
3. **Asymptotic theory** — consistency, limiting distribution, convergence rate, and the asymptotic variance; uniformity if claimed.
4. **Finite-sample evidence** — Monte Carlo on size, power, coverage, bias/RMSE across DGPs and sample sizes, including assumption-stressing regimes.
5. **Method robustness** — behavior under dependence, heavy tails, weak identification, high dimension, or misspecification, as the problem invites.

## Branch paths

- **New estimator** — identifying moment/objective; consistency and limiting distribution under explicit conditions; a consistent (often HAC/cluster-robust) variance estimator.
- **New test** — null, alternative, and null limiting distribution; asymptotic and finite-sample **size control** plus **power** against relevant alternatives; nuisance-parameter and boundary handling.
- **Computational/algorithmic** — correctness (same target as the slow method), complexity/scalability gain, numerical accuracy, timing, and the feasible-application payoff.
- **Applied paper** — what parameter is identified and the assumptions the method requires; dependence/weak-identification-robust inference; defend that the application needs the novelty.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the identification claim, don't only argue it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JBES is a business / economic-statistics venue — reviewers weigh estimator validity and simulation evidence, so pair every estimate with its diagnostics and, where relevant, a Monte-Carlo check.

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

- [ ] Target parameter/functional and its identification conditions stated
- [ ] Regularity conditions explicit and as weak as the result allows
- [ ] Consistency, limiting distribution, and rate established under those conditions
- [ ] A consistent, robust variance estimator provided
- [ ] Monte Carlo covers size, power, coverage, bias/RMSE across DGPs and n
- [ ] Breakdown regimes shown, not hidden; MC standard errors reported
- [ ] The required conditions are plausible in the empirical application

## Anti-patterns

- Asserting an asymptotic distribution with no full set of conditions
- Assumptions so strong no real data set (or the paper's own application) satisfies them
- Monte Carlo only under favorable DGPs; no breakdown shown
- Rejection rates reported with no Monte Carlo standard errors
- A "robust" variance claim with no proof or coverage simulation

## Worked vignette: nailing down a weak-IV-robust estimator's validity

A hypothetical JBES paper proposes a debiased estimator for a structural elasticity under many weak instruments, applied to demand estimation on scanner data (numbers **illustrative**). The credibility ladder forces order: (1) the target elasticity is identified from the conditional-moment restriction as instrument strength shrinks; (2) regularity conditions are weak — finite fourth moments and a concentration-parameter rate; (3) the limiting normal distribution and rate are established with a consistent, heteroskedasticity-robust variance; (4) Monte Carlo across a concentration-parameter grid shows coverage of an illustrative 93.8% near nominal 95% where 2SLS collapses; (5) the breakdown under heavy-tailed shocks is shown. Crucially, the scanner application's first stage is weak — exactly the regime the conditions target — so the assumptions are plausible for the paper's data.

## Referee-pushback patterns on method validity (venue-specific fixes)

| JBES referee objection | Fix this skill enforces |
|----|----|
| "Your assumptions hold for no real dataset, including yours." | Weaken conditions to what the result needs; show the application satisfies them |
| "The asymptotic distribution is asserted without full conditions." | List every regularity condition the limit theorem uses, each motivated |
| "The robust variance claim is unproven." | Prove consistency of the variance estimator and confirm coverage in simulation |

Calibration anchor (hedged): at JBES, "identification" usually means **valid inference for the target under stated conditions**, not a causal-design narrative — but the conditions must be plausible for business/economic data, since a real application is part of scope. Where a condition's necessity is uncertain, state it as sufficient and flag the gap.

## Output format

```
【Object】estimator / test / algorithm / applied-target
【Target + identification】parameter and conditions: ...
【Regularity conditions】[listed] — as weak as possible? [Y/N]
【Asymptotics】consistency / distribution / rate / variance estimator [status each]
【Monte Carlo】DGPs, n grid, size/power/coverage, MC SEs, breakdown shown? [Y/N each]
【Empirical plausibility】conditions hold in the application? [Y/N]
【Next step】jbes-data-analysis
```
