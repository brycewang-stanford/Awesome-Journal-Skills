---
name: ectj-identification-strategy
description: Use when stress-testing identification, assumptions, asymptotics, regularity conditions, and proofs in a The Econometrics Journal (EctJ) submission, including proof placement under RES printed-appendix rules and pairing every asymptotic claim with finite-sample evidence referees can audit.
---

# EctJ Identification Strategy

Use this for theory and methods integrity. EctJ readers will tolerate compactness, but not
hidden assumptions or vague asymptotic claims.

## Audit

- State the population object, identifying restrictions, estimator or test statistic, and
  target parameter before derivations.
- Label each regularity condition by role: existence, identification, consistency,
  asymptotic normality, bootstrap validity, finite-sample approximation, or computation.
- Show why the leading case is not a toy example; connect assumptions to the empirical
  application.
- Keep proofs in the main text or printed appendix when current RES guidance requires that;
  do not park mathematical proofs only in the online appendix.
- Separate theorem statements from implementation advice and simulation claims.
- Flag any assumption that is convenient but empirically fragile.

## Referee attack surface

EctJ referees usually attack the bridge between compact theory and practical use. Pre-answer these points:

- **Object drift**: the target parameter in the theorem is not the object estimated in the application.
- **Assumption opacity**: a regularity condition is stated but never tied to a data feature or estimator step.
- **Leading-case weakness**: the theorem solves a toy case whose constraints make the empirical example
  irrelevant.
- **Proof placement risk**: critical derivations are hidden in unreviewed online material or an untraceable
  appendix.
- **Simulation mismatch**: the Monte Carlo design does not probe the assumption most likely to fail.

For each attack, write the exact theorem, assumption, table, or paragraph that will answer it.

## Assumption ledger

Create a compact ledger before rewriting the theory section:

```text
Condition | Role | Where used | Empirical/simulation check | If weakened
```

Use the ledger to remove decorative assumptions and expose missing ones. If a condition is used only for
proof convenience, say whether it can be relaxed, whether it is standard in the closest EctJ-adjacent
literature, and whether the simulation explores failure near that boundary. If a condition is essential
but empirically unverifiable, the paper needs an interpretation paragraph that tells applied readers what
kind of data-generating process would make it plausible.

Do not let notation hide the identification argument. A reader should be able to trace, in order, the
target object, restrictions, estimator or statistic, asymptotic claim, and finite-sample diagnostic.

## Worked trace: a debiased panel treatment-effect estimator

A hypothetical EctJ vignette (illustrative throughout): the paper proposes an orthogonalized
estimator for an average treatment effect in a panel where nuisance functions are fit by machine
learning. The traceable chain referees expect:

- **Target object**: the ATE under unconfoundedness conditional on high-dimensional firm controls.
- **Restrictions**: overlap bounded away from zero; nuisance estimators converging faster than
  n^{-1/4}; cross-fitting with K=5 folds.
- **Estimator**: the Neyman-orthogonal score averaged over folds.
- **Asymptotic claim**: root-n normality with a variance estimator valid under cross-fitting.
- **Finite-sample diagnostic**: coverage simulated at n in {250, 1000}; the rate condition is
  stressed by deliberately slowing one nuisance learner and showing where coverage degrades.

If any link is missing, that link is what the report will quote back. A rate condition of the
n^{-1/4} kind is exactly the assumption that must be tied to a data feature: say which learner
plausibly meets it in the application and what the simulation shows when it fails.

## Proof-economy rules for the compact format

- Every theorem keeps its full proof in the printed paper or printed appendix; the online appendix
  carries only secondary lemmas, and only when current RES guidance permits it — confirm against
  the journal's current author guidelines before moving any derivation out of print.
- A leading-case theorem may delegate generality to a remark, but the remark must say what breaks
  in the general case, not just that extensions are straightforward.
- Each asymptotic statement should name the exhibit where its finite-sample counterpart appears;
  EctJ referees treat unpaired asymptotics as an unfinished result.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). The Econometrics Journal is a methods venue — estimator validity + simulation; pair estimates with diagnostics.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```text
[Identification status] defensible / needs repair / not ready
[Target object] <parameter, estimator, test, or procedure>
[Critical assumptions] <condition -> role>
[Proof gaps] <missing lemma, rate, regularity, or edge case>
[Applied connection] <how the application validates the setup>
```
