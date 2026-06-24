---
name: cogpsych-data-analysis
description: Use when analyzing data and fitting/comparing models for a Cognitive Psychology (Elsevier) manuscript. The journal expects principled model fitting and comparison (AIC/BIC/Bayes factors), parameter and model recovery, (generalized) linear mixed models or hierarchical Bayesian estimation where apt, and effect sizes with uncertainty — all reproducible from shared code. Guides the analysis and modeling; it does not fabricate results.
---

# Data Analysis & Model Fitting (cogpsych-data-analysis)

Cognitive Psychology holds analyses to a **model-based** standard: fit the formal model, **compare it
to rivals with principled criteria**, demonstrate that parameters and models are **recoverable**, use
**mixed models or hierarchical Bayesian estimation** where the design demands it, and report **effect
sizes with uncertainty** for behavioral results — all regenerable from deposited code. This is the
experiment-to-model-fit loop that defines the venue.

## When to trigger

- Fitting the formal model and comparing it to rival accounts
- Running the behavioral analyses (mixed models, hierarchical Bayesian, contrasts)
- A reviewer asked for model comparison, recovery, robustness, or fuller disclosure
- Preparing analysis/model code and a data dictionary for deposit

## Reporting norms Cognitive Psychology expects

1. **Fit and compare models, don't just fit one.** Report fit for your model **and** the rival(s) under
   matched flexibility; compare with **AIC/BIC**, cross-validation, or **Bayes factors** as
   appropriate, and say what the comparison licenses.
2. **Show recovery.** Demonstrate **parameter recovery** (can the fitting procedure recover known
   parameters from simulated data) and **model recovery** (does the comparison criterion pick the
   generating model) — without these, a fit edge is not interpretable.
3. **Use the right hierarchical structure.** Crossed random effects over subjects *and* items call for
   **(generalized) linear mixed models**; for cognitive models, **hierarchical Bayesian** estimation
   pools strength across participants. Justify the structure; don't aggregate away the variance.
4. **Effect sizes + uncertainty for behavior.** Report standardized/unstandardized effect sizes with
   **confidence/credible intervals** for key behavioral results, not just p-values and stars.
5. **Confirmatory vs. exploratory.** Separate pre-committed model comparisons and tests from
   exploratory model exploration; do not present a post hoc winning model as predicted.
6. **Reproducible.** Model and analysis code, with seeds and pinned versions, regenerate every reported
   fit, figure, and table in a fresh session (see `cogpsych-open-science-and-transparency`).

## Robustness

- Show the conclusion survives reasonable alternative model specifications, priors (for Bayesian fits),
  and exclusion choices; report sensitivity, not a single fragile fit. Report convergence diagnostics
  (e.g., R-hat, ESS) for Bayesian models.

## Worked micro-example (illustrative numbers)

A preregistered three-experiment recognition-memory program fitting UVSD vs. DPSD to confidence-ROC data.

```
Model comparison (preregistered) — pooled across Exps 1-3
  Fit (hierarchical Bayesian, matched flexibility):
    UVSD favored: dBIC = 14 vs. DPSD; Bayes factor ~ 30 in favor of UVSD
  Recovery (required): parameter recovery good (recovered d', sigma within
    credible intervals); model recovery ~ 92% correct at the design's N/trials
  Diagnostic signature: z-ROC slope 0.78, 95% CrI [0.72, 0.84], and linear
    (no reliable curvature) — the qualitative pattern UVSD predicts and DPSD
    forbids, consistent across all three experiments
Behavioral effect (mixed model)
  List-strength manipulation on d': b = 0.31, 95% CI [0.18, 0.44]
Exploratory (labeled)
  A small response-bias drift surfaced post hoc; reported as exploratory
```

Why this passes Cognitive Psychology scrutiny: the model is **compared** (not just fit), **recovery**
makes the comparison interpretable, the **qualitative signature** corroborates the fit index, hierarchy
respects subject/item variance, and the exploratory drift is honestly demoted.

## Analysis-stage reviewer pushback and the venue fix

| Reviewer pushback | What it signals here | Cognitive Psychology fix |
|-------------------|----------------------|--------------------------|
| "You only fit your model" | one-model storytelling | fit the rival under matched flexibility; report AIC/BIC/BF and what it licenses |
| "Better fit may be overfitting" | flexibility imbalance | add model recovery + cross-validation; penalize complexity |
| "Can you recover these parameters?" | identifiability doubt | run and report parameter + model recovery simulations |
| "Aggregated means hide variance" | wrong error structure | refit with crossed-random-effects mixed model / hierarchical Bayesian |
| "Is this the model you predicted?" | post hoc selection | pre-commit the comparison; relabel post hoc fits exploratory |
| "I can't rerun your fits" | reproducibility gate | ship seeded model code + a fresh-session run log |

## Calibration anchors

- A model that is **fit, compared, and recovered** is the unit of evidence here — a single fit with a
  good index but no rival and no recovery is not persuasive.
- Trust a **crossed qualitative prediction** over a marginal fit advantage; report both and lead with
  the signature the rival forbids.
- Respect the data's hierarchy: aggregating over subjects or items inflates false positives and can
  bias parameter estimates; use mixed/hierarchical models and justify the random-effects structure.
- For Bayesian fits, report priors, convergence, and sensitivity — a fit without diagnostics is not
  reproducible evidence.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Cognitive Psychology is experimental — within-subject designs and mixed models dominate; report the model, the effect size, and multiple-comparison control.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the supplement. See
the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Fitting only your model with no rival and no comparison criterion
- Claiming a fit advantage without matched flexibility, recovery, or cross-validation
- Aggregating to cell means and ignoring crossed subject/item variance
- p-values and stars with no effect size or interval for behavioral results
- Presenting a post hoc winning model as a predicted result
- Model/analysis code that does not regenerate the reported fits

## Output format

```
【Model comparison】rivals fit under matched flexibility + criterion (AIC/BIC/BF)? [Y/N]
【Recovery】parameter + model recovery reported? [Y/N]
【Hierarchy】mixed model / hierarchical Bayesian where apt + diagnostics? [Y/N]
【Behavioral effects】effect sizes + intervals? [Y/N]
【Confirmatory vs exploratory】separated? [Y/N]
【Reproducible】seeded code + data dictionary + fresh-session check? [Y/N]
【Next】cogpsych-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — modeling, model-comparison, `lme4`/`brms`/Stan, JAGS, recovery simulation
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — statistical and modeling expectations
