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

## Model-level pushback patterns and the OR fix

| Referee/AE remark | What it flags | Fix that meets the OR bar |
|-------------------|---------------|----------------------------|
| "Model too stylized to matter" | structure stripped to triviality | restore the feature that makes the decision realistic; reprove |
| "Model too general to say anything" | no exploitable structure | impose convexity/submodularity/ergodicity that the application supports |
| "Assumption is convenient, not necessary" | proof-driven hypothesis | add a counterexample showing the result fails without it, or relax it |
| "This is a conjecture, not a theorem" | numerically-supported claim labeled Theorem | downgrade to Conjecture, or supply the proof in `ors-methods` |
| "Structural result not connected to the application" | theorem floats free of the decision | state which operational policy the structure prescribes |

Because *Operations Research* is the INFORMS flagship for rigorous OR/MS methodology,
the editorial bar is a clean mathematical object whose structure **both** enables a
theorem **and** maps to a decision. A model that admits no theorem reads as
under-specified; one that admits a theorem but no operational reading reads as elegant
but irrelevant — the two failure modes the table above pre-empts.

## Worked formulation vignette (illustrative)

Stochastic-inventory control under correlated demand. **Model:** state = on-hand
inventory; action = order quantity; objective = expected discounted holding + backorder
cost; demand a Markov-modulated process (illustrative). **Structure exploited:**
K-convexity of the value function under the modulation. **Result strength:** Theorem 1
states an `(s,S)`-type policy is optimal (a *proved* central result); Proposition 1 gives
monotone comparative statics in the modulation rate (supporting); a Conjecture flags the
multi-product extension as *unproven*. **Assumptions discipline:** the bounded-demand
hypothesis is justified by capacity limits in the application and shown necessary via a
counterexample where unbounded demand breaks K-convexity. **Plain-language for the
intro:** "we show the optimal replenishment rule reduces to ordering up to a single
critical level that depends on the demand regime" — no notation, decision-relevant. This
gives `ors-methods` an explicit theorem-to-machinery handoff and keeps the structure
tethered to the operational policy.

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
