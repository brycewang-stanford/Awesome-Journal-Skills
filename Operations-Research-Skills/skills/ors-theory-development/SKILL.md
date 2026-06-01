---
name: ors-theory-development
description: Use when formulating the model and stating results for an Operations Research (OR) manuscript — defining the optimization/stochastic/simulation model, assumptions, and the theorems, propositions, and lemmas that carry the contribution. Builds the mathematical object and its claimed results; it does not prove them in detail (ors-methods) or run the computational study (ors-data-analysis).
---

# Model & Result Development (ors-theory-development)

## When to trigger

- You are turning an OR problem into a precise mathematical model.
- You need to decide what to claim — and as what (theorem vs. proposition vs. conjecture).
- A reviewer will ask whether your assumptions are necessary or merely convenient.

## Build the model the OR way

*Operations Research* rewards a clean mathematical object and **provable** results.
For the dominant OR/MS methodologies:

- **Optimization model:** state decision variables, objective, constraints, and the
  feasible region precisely. Identify structure (convexity, total unimodularity,
  submodularity, conic representability) — structure is what enables theorems and
  efficient algorithms.
- **Stochastic / probabilistic model:** specify the probability space, the process
  (Markov chain, queue, MDP), the information/filtration, and the performance measure
  (steady-state cost, regret, tail probability). State stability/ergodicity conditions.
- **Simulation model:** specify the stochastic dynamics and the estimand, and how a
  consistent estimator with quantifiable error will be obtained.
- **Decision-analytic model:** specify the utility/risk measure, the information
  structure, and the optimality criterion.

## State results at the right strength

| Claim type | Use when |
|------------|----------|
| **Theorem** | A central, fully proved result (optimality, complexity, convergence rate, bound) |
| **Proposition** | A supporting proved result of lesser scope |
| **Lemma** | A technical step used inside a proof |
| **Corollary** | An immediate consequence |
| **Conjecture** | Stated explicitly as unproven; never disguised as a theorem |

Each formal statement needs explicit hypotheses; tie every assumption to where the
proof uses it (this is what `ors-methods` will then discharge).

## Assumptions discipline

- **Justify, don't smuggle.** For every assumption, say why it holds in the motivating
  application or why it is standard, and whether results degrade gracefully without it.
- **Minimality.** Reviewers probe whether an assumption is *necessary*; pre-empt with a
  counterexample showing the result fails when it is dropped, or a remark that it can be
  relaxed.
- **Tightness.** Where you prove a bound or rate, indicate whether it is tight (a
  matching instance) — tightness is a strong OR contribution.

## Frame significance without equations (for the intro)

OR requires an **equation-free introduction**: articulate the problem, the results,
and their significance in words. Develop the model here, but draft the plain-language
version of each result so the intro can state "we show that ..." without notation.

## Anti-patterns

- A model so general it admits no theorem, or so special it is uninteresting.
- Assumptions chosen to make a proof easy with no application grounding.
- Calling a numerically supported regularity a "theorem."
- Hiding the key assumption in notation rather than stating it.

## Output format

```
【Model】variables / objective / constraints / process / estimand ...
【Structure exploited】convexity / submodularity / ergodicity / ...
【Results】Thm/Prop/Lemma list with one-line plain-language each
【Assumptions】each justified + necessity noted
【Plain-language for intro】"we show ..." (no notation)
【Next step】ors-methods
```
