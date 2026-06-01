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
