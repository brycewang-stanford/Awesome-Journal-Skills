---
name: joe-identification-strategy
description: Use when the assumptions, regularity conditions, identification result, and asymptotic theory of a Journal of Econometrics (JoE) methodological paper are the bottleneck. Stress-tests the formal core — what is assumed, what is proved, and how general it is — before tables are drafted.
---

# Identification & Asymptotic Strategy (joe-identification-strategy)

## When to trigger

- The estimand is not formally identified, or identification is asserted not proved
- Regularity conditions are stated loosely or are non-primitive (they smuggle in the conclusion)
- The limiting distribution / convergence rate is claimed without a derivation path
- You are unsure the result is general enough, or whether the conditions are verifiable

## The JoE formal bar

At the *Journal of Econometrics*, "identification strategy" means the **formal core**: the assumptions under which the estimand is identified, the estimator is consistent, and inference is valid. The house norm is **mathematical rigor** — proofs and asymptotic derivations are expected, and referees probe whether conditions are *primitive and verifiable*, whether the asymptotics are honest, and whether the result generalizes beyond a convenient special case. This is methodology, not applied causal design: the deliverable is theorems plus the Monte Carlo that shows the asymptotics bite in finite samples.

## The formal-core checklist

### 1. Identification

- State the **estimand** and the model precisely. Prove **identification** (the map from the distribution of observables to the parameter is unique) before estimation. Distinguish point vs. partial identification.
- If identification is weak or fails on a boundary (weak instruments, near-unit-root, near-singular Jacobian), say so and provide identification-robust inference rather than hiding it.

### 2. Assumptions / regularity conditions

- List each assumption and label it (moment existence, smoothness, mixing/dependence, bandwidth/rate conditions, rank/full-rank, parameter-space compactness).
- For each: is it **primitive** (on the DGP/data) or **high-level** (on objects derived from the estimator)? Prefer primitive; justify any high-level condition and verify it for a leading example.
- Check none of them silently assume the conclusion (e.g., assuming the very uniform convergence you need).

### 3. Asymptotic theory

- Lay out the proof path: consistency (ULLN / argmax) → rate → asymptotic distribution (CLT / Delta method / empirical-process tools) → variance estimator.
- State the **convergence rate** and the **limiting distribution**; derive or cite the **standard-error / variance estimator** and prove it is consistent.
- Handle nuisance parameters, tuning (bandwidth, lag length, penalty), and any first-stage estimation (Neyman-orthogonality / influence-function corrections) explicitly.

### 4. Generality

- State the **class** of models/DGPs the result covers; flag what is excluded and why.
- Show the result **nests** or extends known cases (a sanity check and a positioning device).

### 5. Proof exposition

- Map theorems → lemmas; keep the main text's intuition, push routine algebra to an appendix.
- Make each step auditable; a referee should reconstruct the argument without guessing.

## Numerical / Monte Carlo confirmation (light here, full in joe-data-analysis)

- Cross-check a derived asymptotic variance against a high-replication Monte Carlo; a mismatch usually signals an algebra error. The full size/power design lives in `joe-data-analysis`.

## Assumption audit

Turn the formal core into an assumption audit table:

| Assumption | Primitive or high-level? | Used in which theorem step? | How it can fail |
| --- | --- | --- | --- |
| Moment / tail condition | Prefer primitive | ULLN, CLT, variance consistency | Heavy tails, weak moments |
| Dependence / mixing | Primitive where possible | LLN/CLT under panels or time series | Persistent shocks, clustering |
| Rank / identification | Primitive if stated on observables | Identification, invertibility, asymptotic linearity | Weak instruments, singular Jacobian |
| Smoothness / tuning rate | Often high-level unless verified | Expansion, bias control, bandwidth/penalty | Boundary points, bad bandwidth |

Use the table to police the paper's language. If an assumption is high-level, either verify it for a leading example or state clearly that it is a sufficient technical condition. If a theorem relies on an assumption that is never invoked in the proof map, delete or relocate it.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Econometrics is a methods venue — estimator validity + simulation evidence are the contribution; pair estimates with diagnostics and Monte-Carlo where relevant.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- "Under standard regularity conditions" with no list and no verification
- High-level assumptions chosen so the theorem is one line — but unverifiable in any real model
- Asserting asymptotic normality with no derivation or no consistent variance estimator
- Ignoring weak/partial identification when the design is on its boundary
- Treating assumptions as a preamble rather than linking each one to a theorem step

## Output format

```
【Estimand & model】...
【Identification】point/partial; proof sketch
【Assumptions】[A1 primitive, A2 high-level (justified), ...]
【Assumption audit】primitive/high-level, theorem use, failure mode
【Asymptotics】rate + limiting distribution + variance estimator
【Generality】class covered; what is excluded; nested cases
【Proof plan】theorems → lemmas → appendix
【Next step】joe-data-analysis
```
