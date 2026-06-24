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

## Methodology pushback patterns and the OR fix

| Referee remark | Underlying defect | Fix that meets the OR bar |
|----------------|-------------------|----------------------------|
| "Proof of Theorem X has a gap" | an assumption invoked implicitly | name where each hypothesis is used; add a lemma to bridge the step |
| "The rate is asserted, not established" | rate read off numerical curves | prove it analytically (Lyapunov / contraction / first-order) with tracked constants |
| "Algorithm has no guarantee" | a fast heuristic without analysis | attach an approximation factor, ε-stationarity, or regret/convergence bound |
| "Bound may not be tight" | only an upper bound shown | exhibit a matching instance, or reframe explicitly as best-known |
| "Simulation conclusions unreliable" | point estimates, no error control | report CIs (batch-means/regenerative) and variance reduction with the rule |
| "Structural result not connected to the application" | theorem floats free of the decision | show the guarantee changes the operational policy it motivates |

Operations Research, as the INFORMS flagship, lives on **soundness and strength of
analysis**: a heuristic without a guarantee is an *INFORMS Journal on Computing* artifact,
not an OR methodological contribution. The machinery table above exists so each
claim is discharged by analysis a referee can verify line by line.

## Worked machinery walk-through (illustrative)

Target result: an approximation algorithm for a stochastic-covering problem with a
claimed 1.5-factor guarantee (illustrative). Machinery selection from the table:
**LP-rounding + primal-dual** for the factor; **concentration (martingale)** to control
the stochastic constraint; **an oracle lower bound** to argue the factor cannot be
pushed below 1.5 without stronger assumptions. Proof hygiene: each of the three
assumptions (bounded second moment, independence across stages, integral demand) is
cited exactly where the argument needs it; the full rounding analysis goes to the
e-companion, the main text keeps the primal-dual sketch and the tight-instance
construction. This produces a theorem-grade result *and* a tightness statement — the
combination OR referees reward over a bare upper bound.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Operations Research is predominantly analytical / optimization / stochastic modeling; use the chain below only for its empirical/causal papers — modeling, optimization, and simulation are outside this causal-inference toolchain.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
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
