---
name: fcr-data-analysis
description: Use when executing and reporting the statistical analysis for a Field Crops Research (FCR) manuscript — mixed models for multi-environment and blocked/split-plot designs, genotype-by-environment (G×E) and stability analysis, estimated marginal means with SED/LSD, and crop-model evaluation. FCR requires data analysed with appropriate statistics that match the design and address the objectives. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (fcr-data-analysis)

FCR requires that **data be analysed with appropriate statistics** and that results be **concise and
address the objectives**. For field-crop work that almost always means **mixed models** that respect
the design (blocks, split-plots, environments) — not a one-way ANOVA on pooled plots. Analysis
execution lives here; design decisions live in `fcr-experimental-design`.

## When to trigger

- Building the analysis and results section from trial or modelling data
- A reviewer asked for the correct error structure, G×E modelling, or proper means separation
- Reconciling main effects with interactions across environments
- Evaluating a crop model against observations

## Analysis norms FCR expects

1. **Match the model to the design.** Use a **linear mixed model** with the error structure implied by
   the layout: blocks, whole-plot vs. sub-plot errors (split-plot), environment as a factor, and
   correct **random effects** (e.g., environment, block, genotype-within-environment). A wrong error
   term inflates significance.
2. **G×E done properly.** Test and interpret genotype/treatment × environment; where ranking matters,
   use **Finlay–Wilkinson**, **AMMI**, or **GGE biplot** stability analysis. Report whether the
   treatment effect is consistent or environment-dependent.
3. **Means separation the right way.** Report **estimated marginal (adjusted) means** with **SE / SED
   or LSD** at a stated α; avoid bare means with significance stars and avoid over-using multiple-range
   tests on quantitative factors — fit a **response curve** instead (N, water, density).
4. **Report uncertainty and effect size.** Give the magnitude of the agronomic effect (e.g., kg ha⁻¹,
   % yield change) with intervals, and its **agronomic** meaning — not just p-values.
5. **Check assumptions.** Residual diagnostics, variance homogeneity across environments, and
   transformation/weighting where needed; consider **spatial models** for heterogeneous fields.
6. **Meta-analysis.** If synthesising published trials, use proper meta-analytic models (effect sizes,
   heterogeneity, weighting) — not vote-counting.

## Crop-model evaluation

- Report fit statistics on **independent validation** data: RMSE, **nRMSE**, mean bias, modelling
  efficiency (EF), and (with care) R²; show observed-vs-simulated with the 1:1 line.
- Separate calibration from validation; state cultivar coefficients and model version.

## Reproducibility while you work

- One analysis script regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for any stochastic/bootstrap/simulation step; pin software/package versions.
- Keep table/figure numbers matched to script outputs (supports the data-availability deposit — see
  `fcr-reporting-and-data-policy`).

## Anti-patterns

- One-way ANOVA on pooled plots, ignoring blocks/split-plot/environment structure
- Pseudoreplication: treating sub-samples within a plot as independent replicates
- Mean-separation letters (a/b/c) slapped on a quantitative dose — fit a curve
- Reporting significance without effect size, interval, or agronomic interpretation
- Pooling environments and hiding a strong G×E interaction

## Output format

```
【Model】mixed model: fixed = ___, random = ___, error structure = ___
【G×E】tested? consistent vs. environment-dependent? stability method
【Means】adjusted means + SED/LSD at α; response curve where quantitative
【Effect size】magnitude (units) + interval + agronomic meaning
【Diagnostics】assumptions checked? spatial model if needed? [Y/N]
【Model eval (if any)】RMSE/nRMSE/EF on independent data
【Next】fcr-figures-and-tables
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — mixed-model and G×E packages (lme4, asreml, metan, SpATS) and crop-model tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — appropriate-statistics and concise-results expectations
