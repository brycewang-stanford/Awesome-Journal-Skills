---
name: mksc-theory-development
description: Use when building the formal model for a Marketing Science manuscript — turning a marketing phenomenon into an analytical (game-theoretic) model or a structural econometric model with a clear identification argument. Develops the model and mechanism; it does not run the estimation (mksc-data-analysis) or pick the empirical genre at a high level (mksc-methods).
---

# Model & Mechanism Development (mksc-theory-development)

## When to trigger

- The phenomenon is interesting but there is no formal model yet
- The "mechanism" is verbal and needs to be written as primitives, payoffs, and equilibrium
- A structural story lacks an identification argument (what variation pins down each parameter)
- An analytical model lacks crisp comparative statics or testable predictions

## In Marketing Science, "theory" means a model

Unlike behavior-first venues where theory is a verbal mechanism, here a contribution is carried by a **mathematical model**. Build whichever genre the question demands.

### Analytical (game-theoretic) models

- State **primitives**: players (firms, consumers, platform), action spaces, information structure, timing, and payoffs.
- Solve for **equilibrium** (Nash/subgame-perfect/Bayesian) and prove existence/uniqueness where needed.
- Derive **comparative statics** — sign how equilibrium prices, advertising, or profits move with a parameter — and surface the counterintuitive result that is the contribution.
- Keep assumptions transparent and motivated by marketing institutions (double marginalization, competitive response, targeting).

### Structural econometric models

- Write a **demand** model (random-coefficients/BLP logit, nested logit, dynamic discrete choice) and, where relevant, a **supply/equilibrium** condition (FOCs, pricing game).
- State **micro-foundations**: utility, state transitions, firm objective.
- Make the **identification argument explicit before estimation**: which moments/instruments (cost shifters, BLP instruments, exclusion restrictions, panel variation, experiments/discontinuities) identify preferences, dynamics, and supply parameters — and why they are exogenous.
- Define the **counterfactual** the estimated model will simulate; the model must be rich enough to answer it and no richer.

## Connecting reduced-form or behavioral evidence

If you include experiments, surveys, or reduced-form results, tie them to the model: as model-free evidence motivating an assumption, as a source of identifying variation, or as validation of a mechanism the model formalizes.

## Checklist

- [ ] Primitives (players, actions, information, timing, payoffs) fully specified
- [ ] Equilibrium concept stated; existence/uniqueness addressed (analytical)
- [ ] Comparative statics / testable predictions derived (analytical)
- [ ] Demand (and supply) specified with micro-foundations (structural)
- [ ] Identification argument explicit: variation/instruments → each parameter
- [ ] The counterfactual question the model must answer is named up front

## Anti-patterns

- A regression relabeled as "a model" with no primitives or equilibrium.
- A structural model with parameters but no identification argument.
- Assumptions chosen for tractability that contradict the marketing institution.
- Comparative statics asserted, not derived.


## Theory pass for Marketing Science

Treat this skill as an executable review pass, not a prose hint. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then judge whether the current manuscript answers the venue's real reader: quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Do the pass:** Name the construct, mechanism, boundary condition, and falsifiable implication separately; do not let a literature summary masquerade as theory.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Genre】analytical / structural
【Primitives】players, actions, info, timing, payoffs
【Equilibrium / estimand】concept; existence/uniqueness OR demand+supply
【Identification】variation/instruments → parameters; exogeneity logic
【Predictions / counterfactual】key comparative static OR policy to simulate
【Next step】mksc-literature-positioning then mksc-methods
```
