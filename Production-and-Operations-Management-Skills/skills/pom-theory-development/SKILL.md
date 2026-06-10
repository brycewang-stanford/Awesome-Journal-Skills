---
name: pom-theory-development
description: Use when building the model or mechanism for a Production and Operations Management (POM) manuscript — formalizing assumptions, deriving equilibria/propositions for analytical work, or developing OM hypotheses for empirical/behavioral work. Builds the argument; it does not run the analysis (pom-data-analysis) or frame the contribution (pom-contribution-framing).
---

# Model & Theory Development (pom-theory-development)

## When to trigger

- You have an operations question but no formal model or sharp mechanism
- Your assumptions are mathematically convenient but operationally unmotivated
- A reviewer says "the model is not well grounded in practice" or "the mechanism is unclear"
- Empirical results are interpreted as bare correlations with no operations mechanism

## POM's dominant track: analytical modeling — done rigorously

POM is historically anchored in **analytical/mathematical modeling** (operations-research / management-science-style optimization, stochastic modeling, and game theory), so theory development most often means **building a model**, not deriving verbal hypotheses. Make every modeling choice defensible:

- **Decision primitive & objective.** Name the operational decision (capacity, inventory, pricing, scheduling, sourcing, routing, staffing) and the objective (cost, profit, fill rate, waiting time, welfare).
- **Assumptions tied to operations reality.** Justify each assumption (lead times, demand distribution, information structure, rationality) against an operational constraint — not analytical convenience.
- **Solution concept.** For optimization, characterize the optimal policy (e.g., base-stock, (s, S), threshold) and structural properties (monotonicity, convexity). For game-theoretic models, state the equilibrium concept (Nash, Stackelberg), and prove existence/uniqueness.
- **Propositions over hand-waving.** State results as numbered propositions/theorems; full proofs go to the e-companion, with intuition in the main text.

## Empirical, behavioral, and data-science tracks

- **Empirical OM:** derive hypotheses from an operations mechanism, then identify it with archival data; specify the estimand and the causal logic before estimation.
- **Behavioral OM:** ground predictions in decision biases (e.g., newsvendor pull-to-center, bullwhip from misperception of feedback) and design the experiment to isolate the mechanism.
- **Operations data science:** state the prediction/decision task and the operational loss the model improves (e.g., predict-then-optimize), not accuracy for its own sake.

## The practice-relevance gate

Every mechanism must answer: **what does a practicing operations manager do differently?** Convert results into decision levers (a policy, a contract term, a staffing rule), not just comparative statics. POM weights this alongside rigor.

## Checklist

- [ ] Decision primitive, objective, and assumptions stated and operationally justified
- [ ] Analytical: solution concept, structural results, equilibrium existence proven (proofs in e-companion)
- [ ] Empirical/behavioral: mechanism → hypothesis → identification/experiment chain explicit
- [ ] Result expressed as a managerial lever, not only a sign of a derivative
- [ ] Mechanism generalizes beyond the focal instance/dataset

## Anti-patterns

- Method novelty substituted for an OM theory contribution.
- Assumptions chosen for tractability with no operational story.
- "Curvature" or a significant interaction reported with no operational mechanism.
- Practice implications that merely restate the result without an actionable decision.


## Operating pass for Production and Operations Management

Use this as a second-pass capability check. First lock the operational decision, the performance metric, and the implementable lever; then test whether the manuscript addresses POM reviewers who want operational insight tied to production, service, supply-chain, or platform decisions.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Management Science for broader OR/MS theory, Operations Research for method-first optimization, MSOM for manufacturing/service operations depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Decision primitive】capacity / inventory / pricing / routing / staffing ...
【Mechanism】queueing / contracting / incentives / learning / behavioral friction ...
【Result form】proposition/theorem (proof→e-companion) | hypothesis (→identification)
【Assumption risk】assumption + operational defense
【Practice lever】decision changed by the result
【Next step】pom-literature-positioning or pom-methods
```
