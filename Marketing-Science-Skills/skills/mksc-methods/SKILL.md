---
name: mksc-methods
description: Use when the empirical/analytical approach is the bottleneck for a Marketing Science manuscript — choosing among structural econometrics, analytical modeling, and model-disciplined causal/ML methods, and making the model estimable and identified. Designs the approach; it does not execute the estimation and counterfactuals (mksc-data-analysis).
---

# Methods & Identification (mksc-methods)

## When to trigger

- You must choose between a structural, analytical, or reduced-form/causal-ML approach
- The model is written but not yet estimable (parameters, moments, normalization)
- Identification is hand-waved ("we use instruments") without specifics
- A reviewer says "the design cannot identify the structural parameters"

## Choose the genre that fits the claim

Marketing Science is methodologically plural around a modeling core: structural econometrics, analytical models, econometric/statistical analysis, ML tools, surveys, and experiments — all judged by whether they develop, test, or rigorously apply a formal model.

| Claim / goal                                   | Approach that earns it                                            |
|------------------------------------------------|-------------------------------------------------------------------|
| Quantify demand and simulate a policy          | Structural demand (BLP/mixed logit), supply FOCs, counterfactual  |
| Forward-looking behavior, adoption, churn      | Dynamic discrete choice / dynamic games (Rust, BBL, CCP)          |
| Strategic-interaction insight, comparative statics | Analytical (game-theoretic) model                             |
| Bidding, sponsored search, marketplaces        | Auction/structural-IO model with equilibrium bidding             |
| Heterogeneous treatment effects tied to a model| Causal ML (double/debiased ML, causal forests) disciplined by theory |
| Causal effect from field variation             | Field experiment / quasi-experiment as identifying variation      |

A field experiment or quasi-experiment is welcome **when it identifies a model primitive or validates a mechanism**, not as a stand-alone reduced-form result.

## Make the model estimable and identified

- **Estimator**: match it to the model — GMM (BLP moment conditions), MLE/SMLE, simulated method of moments, or hierarchical Bayes (MCMC) for rich heterogeneity.
- **Instruments / identifying variation**: name them concretely (cost shifters, BLP/Hausman/differentiation instruments, exclusion restrictions, randomized or discontinuity variation) and defend exogeneity.
- **Normalizations and functional form**: state outside-good normalization, scale/location normalizations, and which assumptions are substantive vs. convenience.
- **Computation**: specify the solver, equilibrium/inner-loop fixed point, starting values, and how you handle multiple equilibria or local optima.

## For analytical papers

Specify the equilibrium concept, solve it, and prove the claims; relegate long proofs to an appendix but state the key steps. Plan to validate counterintuitive predictions and discuss robustness to the modeling assumptions that drive them.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Marketing Science is heavily structural/analytical; the chain below serves its reduced-form / field-experiment lane — structural demand and analytical modeling are outside this causal-inference toolchain.

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

- [ ] Genre (structural / analytical / causal-ML / experiment) matches the claim
- [ ] Estimator matches the model (GMM/MLE/SMM/Bayes) and is stated
- [ ] Identifying variation/instruments named and exogeneity defended
- [ ] Normalizations and substantive vs. convenience assumptions separated
- [ ] Computation (solver, fixed point, starting values, multiple equilibria) planned
- [ ] Any experiment/quasi-experiment tied to a model primitive, not free-standing

## Anti-patterns

- A structural model "estimated" with no stated moments or instruments.
- Reduced-form regressions presented as the whole contribution at MKSC.
- Ignoring multiplicity of equilibria or optimizer convergence.
- Treating convenience assumptions as if they were innocuous.


## Methods pass for Marketing Science

Use this as a second-pass capability check. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then test whether the manuscript addresses quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Primary move:** Name assumptions, diagnostics, robustness, falsification, and failure modes; do not accept a method section that hides the decisive validity threat.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Genre】structural / analytical / causal-ML / experiment
【Model→estimator】GMM / MLE-SMLE / SMM / hierarchical Bayes
【Identification】instruments/variation → parameters; exogeneity defense
【Normalizations/assumptions】substantive vs. convenience
【Computation】solver, fixed point, starting values, multiplicity
【Next step】mksc-data-analysis
```
