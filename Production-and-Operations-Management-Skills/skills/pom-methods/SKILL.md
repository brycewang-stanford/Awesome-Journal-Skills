---
name: pom-methods
description: Use when selecting or auditing the method for a Production and Operations Management (POM) manuscript — analytical modeling (optimization, stochastic models, game theory), empirical identification, behavioral experiments, simulation, or operations data science. Matches method to the operations question; it does not execute the analysis (pom-data-analysis).
---

# Method Fit (pom-methods)

## When to trigger

- The method may not match the operations question (level, uncertainty, causality)
- You must choose between an analytical model, an empirical design, an experiment, or a data pipeline
- A reviewer says "the method does not support the claim" or "this is a methods paper, not OM"

## POM mandates no single method — but the method must fit and be rigorous

POM explicitly places **no restriction on research methods**, while being historically anchored in analytical modeling. Pick the method the *question* demands, and route to the matching Department.

| Operations question / claim                                  | Method                                                              |
|--------------------------------------------------------------|--------------------------------------------------------------------|
| Optimal policy under cost/service objective                  | Optimization (LP/MIP/convex, dynamic programming); characterize the policy |
| Decisions under demand/lead-time uncertainty                 | Stochastic modeling, queueing, inventory theory, MDP/ADP           |
| Strategic interaction (suppliers, competitors, platforms)    | Game theory (Nash/Stackelberg); prove equilibrium existence/uniqueness |
| Causal operational effect from field data                    | Empirical OM: DiD, IV, RD, matching with a clear identification strategy |
| Human operational decision bias                              | Behavioral/experimental OM (lab/online); randomization, manipulation checks |
| Systems too complex for closed form                          | Discrete-event simulation; validation, warm-up, replications, CIs  |
| Prediction feeding an operational decision                   | Operations data science (ML / forecasting), tied to a decision/loss |

## What each track must defend

- **Analytical:** assumptions grounded in operations reality; solution concept; structural results; sensitivity/comparative statics; managerial interpretation. Robustness = relaxing key assumptions, not just numerical examples.
- **Empirical OM:** identification (what makes the effect causal), measurement in decision-relevant units, unit of analysis, external validity to other operations settings.
- **Behavioral OM:** design, incentives, randomization, manipulation and attention checks, and **operational realism** (does the lab task map to a real operations decision?).
- **Operations data science:** validation design, leakage checks, and — critically — the **operational value**: does a better prediction change a feasible policy (predict-then-optimize)?
- **Simulation:** parameter provenance, validation against known cases, sensitivity, and a replication package.

## The POM bar on method

A method exists to serve an **OM contribution** judged interesting to practicing managers. If the paper's value is mainly a technical advance with thin OM decision content, a methods journal may fit better. Keep heavy derivations, solver details, and extra robustness for the unlimited online **e-companion** so the 32-page main document stays focused.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). POM spans analytical and empirical OM; apply the chain below to its empirical-OM papers, and note when a contribution is analytical / optimization.

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
## Checklist

- [ ] Method matches the operations question and the target Department
- [ ] Analytical: solution concept + structural results + assumption-relaxing robustness
- [ ] Empirical: identification strategy and decision-relevant measurement stated
- [ ] Behavioral: randomization, manipulation checks, operational realism
- [ ] Data science: validation, leakage, and decision/operational value
- [ ] Derivations/extra material slated for the e-companion


## Methods pass for Production and Operations Management

Use this as a second-pass capability check. First lock the operational decision, the performance metric, and the implementable lever; then test whether the manuscript addresses POM reviewers who want operational insight tied to production, service, supply-chain, or platform decisions.

- **Primary move:** Name assumptions, diagnostics, robustness, falsification, and failure modes; do not accept a method section that hides the decisive validity threat.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Management Science for broader OR/MS theory, Operations Research for method-first optimization, MSOM for manufacturing/service operations depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Method family】optimization / stochastic / game-theory / empirical / behavioral / simulation / data-science
【Operations question】<decision problem>
【Validity risks】assumptions / identification / measurement / leakage / validation
【Practice tie】how the method yields a manager-usable result
【e-companion plan】proofs / extra analyses to move online
【Next step】pom-data-analysis
```
