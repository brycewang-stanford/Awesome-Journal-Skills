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

## Department-fit map: which lane bar applies

Because Management Science is the multidisciplinary INFORMS flagship of many departments, "the rigor bar" is the bar of the department whose editor desk-screens you.

| Candidate department | The standard it enforces |
|----------------------|--------------------------|
| Optimization and Decision Analytics | Provable structure or bounds, not just a solver run |
| Stochastic Models and Simulation | Honest confidence intervals; analytical structure where possible |
| Behavioral and Decision Analysis | Pre-registration, manipulation/attention checks, power |
| Finance / Accounting (empirical) | Credible exogenous variation; clustered SE |

## Worked micro-example (illustrative): designing an operations field experiment

A team wants to claim algorithmic shift-recommendations raise gig-driver retention, aiming at the Operations Management / Behavioral lane. Design A compares drivers who opted in versus those who did not — opt-in is self-selected, so a referee reads the gap as selection, not effect. Design B randomizes recommendations on for 50% of new drivers, powered for a 4-point lift (illustrative), and pre-commits market-clustered errors. Design B clears the bar by ruling out selection by construction; Design A is desk-vulnerable on identification despite the data existing.

## Referee-pushback patterns and the venue-specific fix

- **"Which department is this, and does the method meet that bar?"** Name the home department and confirm the design meets its specific standard — a generic "rigorous method" claim does not survive the multi-department desk.
- **"Solved numerically; where is the structural insight?"** A solver run alone reads as Operations Research engineering; add comparative statics or bounds so the managerial reading is general.

## Calibration anchors

- The journal spans analytics-to-behavioral, so a method exemplary in one department may look under-powered to another; match the design to the reviewer pool, not your own training. The unifying premium is rigor *and* a clear management contribution; confirm current Disclosure requirements against the author guidelines.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane** (field data, natural experiments, behavioral
experiments), estimate and audit rather than only specify. Full map:
[`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Lab / field experiments:** randomization-based inference and `romano_wolf` for the
  many-outcome family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool** (a behavioral referee wants the
multiple-testing haircut; an econometric referee wants the weak-IV-robust CI). Note:
**structural estimation, optimization, and analytical modeling are outside this
causal-inference toolchain** — use the field's own solvers and say so. A run end-to-end
(synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).

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
