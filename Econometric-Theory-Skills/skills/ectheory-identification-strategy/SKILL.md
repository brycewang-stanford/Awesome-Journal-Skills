---
name: ectheory-identification-strategy
description: Use when the assumptions, regularity conditions, and asymptotic results are the bottleneck for an Econometric Theory (ET) theorem-proof paper — adapt "identification" to mean stating defensible assumptions, proving the limit theory, and establishing generality, not causal design.
---

# Assumptions, Results & Proof Plan (ectheory-identification-strategy)

## When to trigger

- The estimator/test is stated but the **regularity conditions** under which it works are not pinned down
- A proof has a gap, or an assumption is doing suspicious load-bearing work
- You need to decide what limit theory applies (stationary vs nonstationary, fixed vs growing dimension)
- You are unsure your result clears ET's rigor bar before drafting theorems

## The ET rigor bar (theory journal — adapt "identification" accordingly)

At ET the analogue of an "identification strategy" is a **complete, defensible assumption set plus a
correct, general proof**. The most common ET referee objection is an unstated or implausibly strong
regularity condition. Treat the assumption-result-proof triple as the spine:

1. **Assumptions.** State each one explicitly and minimally. For every assumption ask: is it
   necessary, can it be weakened, and is it satisfied by a leading example DGP? Distinguish
   primitive conditions from high-level ones; if you use high-level conditions, show they hold in a
   concrete case.
2. **Results.** State theorems precisely — the object, the mode of convergence (in probability, in
   distribution, almost surely, uniformly), the rate, and the limiting law (normal, mixed-normal,
   functional of Brownian motion, non-standard).
3. **Proof exposition.** Give a readable proof: a roadmap up front, key lemmas isolated, and the
   probabilistic machinery named (LLN/CLT, triangular-array CLT, FCLT/weak convergence,
   empirical-process bounds, mixing / near-epoch dependence, concentration inequalities).
4. **Generality.** Show the result is not an artifact of a special case — handle dependent data,
   non-standard limits, or growing dimension where relevant.

## Branch paths by environment

- **Stationary, fixed dimension** — standard LLN/CLT; verify moment and dependence conditions; give
  the asymptotic variance explicitly and a consistent estimator of it.
- **Nonstationary / unit-root / cointegration** — FCLT and continuous-mapping arguments; limits as
  functionals of Brownian motion; care with normalizing rates (e.g., super-consistency).
- **High-dimensional / many regressors** — dimension growing with n; concentration inequalities,
  sparsity or regularization conditions; uniformity over the parameter space.
- **Non-standard inference / partial identification** — characterize the (possibly non-normal) limit,
  size control under the least-favorable configuration, and robustness of the inference.
- **Semiparametric / nonparametric** — empirical-process / stochastic-equicontinuity arguments;
  bandwidth/tuning conditions; bias-variance trade-off made explicit.

## Checklist

- [ ] Every assumption stated explicitly, minimally, and motivated by a leading example
- [ ] High-level conditions verified in at least one primitive case
- [ ] Mode of convergence, rate, and limiting law stated precisely in each theorem
- [ ] Proof has a roadmap; lemmas isolated; probabilistic tools named
- [ ] Asymptotic variance / limiting functional given, with a consistent estimator where relevant
- [ ] Generality shown (dependence, nonstationarity, or dimension handled, as applicable)
- [ ] No claim exceeds what the assumptions support

## Anti-patterns

- An assumption that secretly assumes the conclusion (e.g., directly assuming asymptotic normality)
- High-level conditions that are never shown to hold in any concrete DGP
- A proof sketch that hides the hard step (uniformity, the non-standard limit, the edge case)
- Plain CLT machinery applied to nonstationary or high-dimensional data without justification
- Stating a rate or limit law without the supporting convergence argument

## Output format

```
【Environment】stationary / nonstationary / high-dimensional / non-standard / semiparametric
【Assumptions】listed + each justified by a leading example? [Y/N]
【Result】object, mode of convergence, rate, limiting law
【Proof plan】roadmap + key lemmas + named tools
【Generality】what is handled beyond the base case
【Gaps】[...]
【Next step】ectheory-contribution-framing
```
