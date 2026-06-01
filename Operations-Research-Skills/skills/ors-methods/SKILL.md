---
name: ors-methods
description: Use when designing the proof technique, algorithm, or simulation protocol for an Operations Research (OR) manuscript — choosing the right machinery (duality, dynamic programming, probabilistic coupling, convergence analysis, simulation output analysis) to actually establish the claimed results. Establishes the results; it does not state the model (ors-theory-development) or run the experiments (ors-data-analysis).
---

# Proof & Algorithm Methodology (ors-methods)

## When to trigger

- The model and claims exist (`ors-theory-development`) and now must be *proved* or *guaranteed*.
- You need to pick a proof strategy or design an algorithm with provable guarantees.
- A reviewer says "the proof of Theorem X has a gap" or "the rate is not established."

## Match the machinery to the result

*Operations Research* is mathematically rigorous: the contribution lives or dies on
the soundness and strength of the analysis. Pick technique by methodology:

| Result you need | Typical machinery |
|-----------------|-------------------|
| Optimality / strong duality | LP/conic duality, KKT, polyhedral / total unimodularity, submodularity |
| Approximation guarantee | LP/SDP rounding, primal-dual, greedy + submodular bounds |
| Complexity / hardness | reductions (NP-hardness), oracle lower bounds |
| Convergence & rate | monotonicity/Lyapunov, fixed-point/contraction, first-order analysis |
| Steady-state / stability | Foster-Lyapunov, regenerative arguments, fluid/diffusion limits |
| Stochastic comparison / bounds | coupling, stochastic dominance, martingale/concentration inequalities |
| MDP / dynamic decisions | dynamic programming, value/policy iteration, ADP with error bounds |
| Heavy-traffic / asymptotics | functional CLT, weak convergence, state-space collapse |

## Algorithm design with guarantees

- State **what the algorithm guarantees**: exact/optimal, an approximation factor, an
  ε-stationary point, or a regret/convergence rate — and under which assumptions.
- Give **complexity** (time, iterations, oracle calls; per-iteration cost and total).
- Separate the **method** from its **proof of correctness/convergence**; a fast
  heuristic without analysis is not an OR methodological contribution on its own.

## Simulation methodology (when the analysis is empirical-stochastic)

- Specify the estimator and argue **consistency**; quantify error with valid
  confidence intervals (batch means, regenerative, or replication-based).
- Use **variance reduction** (common random numbers, control variates) and justify it.
- For ranking-and-selection / simulation optimization, state the statistical
  guarantee (e.g., probability of correct selection) and the budget rule.

## Proof hygiene OR reviewers expect

- Every assumption used is invoked explicitly where the proof needs it.
- Long proofs go to an **e-companion** (which must not be longer than the manuscript);
  the main text keeps the key idea and a proof sketch.
- Constants and rates are tracked, not hidden in "O(·)" when tightness is claimed.

## Anti-patterns

- A "proof" that silently adds an assumption mid-argument.
- Claiming a rate from numerical curves rather than analysis.
- An algorithm with no guarantee presented as the central contribution.
- Simulation conclusions with no confidence intervals or variance control.

## Output format

```
【Result → technique】each Thm/Prop mapped to its machinery
【Algorithm】guarantee (exact/approx/rate) + complexity
【Simulation】estimator, CI method, variance reduction (if used)
【Proof hygiene】assumptions invoked explicitly; e-companion plan
【Open gaps】[...]
【Next step】ors-data-analysis
```
