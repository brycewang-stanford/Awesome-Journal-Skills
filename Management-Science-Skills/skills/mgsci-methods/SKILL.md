---
name: mgsci-methods
description: Use when choosing and defending the method for a Management Science (INFORMS) manuscript — selecting an analytical modeling approach (optimization, stochastic, game/economic theory) or an empirical design (econometric identification, lab/field experiment, structural, data science) that matches the question and the Department's standards. It designs; it does not execute the analysis (mgsci-data-analysis).
---

# Methods & Design (mgsci-methods)

## When to trigger

- The method may not match the question (wrong model class, weak identification)
- You must choose between an analytical model and an empirical study — or combine them
- A Department Editor or reviewer will probe whether the design can actually support the claim
- You need to pick the field-appropriate standard for your Department lane

Management Science has **no single dominant method by design**. Each **Department** sets its own field-appropriate expectations. Pick the lane the question demands, then meet that lane's rigor bar.

## Analytical-modeling design

| Question / claim                                   | Approach                                                  |
|----------------------------------------------------|----------------------------------------------------------|
| Optimal policy under constraints                   | Mathematical programming / optimization (LP/MIP/convex)  |
| Dynamics, queues, inventory, uncertainty           | Stochastic processes, MDPs, dynamic programming          |
| Strategic interaction among decision-makers        | Game theory / mechanism design; state the equilibrium concept |
| Pricing/incentives under information frictions     | Economic-theory model; contracts, signaling, screening   |
| Intractable models / policy evaluation             | Simulation with variance reduction and honest CIs        |

For analytical work the design *is* the model: define the decision problem, assumptions, solution concept, and what you will prove. Plan the comparative statics that will carry the managerial insight, and the extensions that will demonstrate robustness of the qualitative result.

## Empirical design

| Question / claim                          | Design                                                       |
|-------------------------------------------|--------------------------------------------------------------|
| Causal effect from observational data     | Quasi-experiment: DiD, IV, RDD, event study; clustered SE    |
| Causal effect under control               | Lab or field experiment with randomization & manipulation checks |
| Mechanism / primitive recovery            | Structural estimation tied to a model                        |
| Prediction / pattern at scale             | Data-science pipeline with honest out-of-sample validation   |

For empirical work, the **identification strategy** is the heart of the design — name the source of variation and the threats it rules out *before* estimation. Behavioral and Marketing experiments need pre-registration, manipulation/attention checks, and adequate power.

## The unifying rigor + relevance bar

Whatever the lane, the design must (a) be able to support the specific claim and (b) yield a **decision-relevant insight that travels across departments**. A method that is rigorous but produces no managerial reading, or a managerial story the design cannot actually test, will not clear the bar.

## Reproducibility is designed in, not bolted on

Management Science verifies data and code for accepted papers before publication (Data and Code Disclosure Policy, articles on/after July 1, 2019). Design your pipeline — analytical numerics or empirical estimation — so a single master script regenerates every result from raw inputs.

## Anti-patterns

- A model class chosen for tractability that cannot answer the actual question.
- An empirical claim of causality with no credible identification (selection ignored).
- Experiments without manipulation checks, power analysis, or pre-registration.
- Treating reproducibility as an afterthought when verification is mandatory.

## Output format

```
【Lane】analytical / empirical / combined
【Approach】[model class or identification strategy]
【Why it fits the claim】...
【Department standard met】...
【Reproducibility plan】master script regenerates all results: yes/no
【Next step】mgsci-data-analysis
```
