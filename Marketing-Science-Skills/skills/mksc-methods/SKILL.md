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

## Output format

```
【Genre】structural / analytical / causal-ML / experiment
【Model→estimator】GMM / MLE-SMLE / SMM / hierarchical Bayes
【Identification】instruments/variation → parameters; exogeneity defense
【Normalizations/assumptions】substantive vs. convenience
【Computation】solver, fixed point, starting values, multiplicity
【Next step】mksc-data-analysis
```
