---
name: jmgmt-data-analysis
description: Use when estimation and results are the bottleneck for a Journal of Management (JOM) manuscript — SEM/CFA, HLM/multilevel, regression and interactions, mediation/moderation, and meta-analytic estimation with artifact corrections. Runs and validates the analysis; it does not design the study (jmgmt-methods) or frame the contribution (jmgmt-contribution-framing).
---

# Data Analysis (jmgmt-data-analysis)

## When to trigger

- The model is fit but a reviewer questions the measurement model or fit indices
- Mediation/moderation is tested in a way a JOM methods reviewer would challenge
- Nested data are being analyzed without modeling the nesting
- A meta-analysis needs the right estimator, corrections, and heterogeneity diagnostics
- Results are reported with significance asterisks and no effect sizes

## The JOM analysis bar

JOM houses some of the field's leading **research-methods** scholars and runs methods reviews, so analysis is read by an unusually demanding audience. The expectation is a **transparent measurement model before the structural model**, **effect sizes and confidence intervals** alongside tests (not p-stars alone), and analysis choices that match the level and design set in `jmgmt-methods`. Report enough that the analysis is reconstructable from the paper and the (anonymized) data transparency table.

## Branch paths

### Branch A: SEM / CFA (latent-variable micro models)
- Report the **measurement model first**: standardized loadings, reliability (composite reliability/ω, not only α), AVE, and a **discriminant-validity** check (AVE vs. squared inter-construct correlations, or HTMT).
- Report multiple **fit indices** (χ²/df, CFI/TLI, RMSEA with CI, SRMR) — never a single index.
- For mediation, report the **indirect effect with a bootstrap CI** (e.g., 5,000 resamples, bias-corrected); do not infer mediation from a Sobel test alone or from two significant paths.
- Compare the hypothesized model against a theoretically motivated alternative.

### Branch B: Multilevel / HLM (nested data)
- Report **null-model ICC(1)/ICC(2)** to justify multilevel modeling; group-mean-center level-1 predictors where the theory concerns within-group effects, and say which centering and why.
- Model **random slopes** when testing cross-level moderation; report the variance components.
- Test cross-level interactions with adequate level-2 N; do not over-interpret a cross-level slope from few groups.

### Branch C: Regression / interactions (archival or single-level)
- Report standardized and unstandardized coefficients, robust/clustered SEs as appropriate, and **effect sizes** (ΔR², f²).
- **Probe interactions**: simple slopes at ±1 SD, an interaction plot, and a region-of-significance (Johnson–Neyman) where useful.
- For curvilinear claims, test the quadratic term *and* report the turning point with a CI.
- Carry the endogeneity strategy from `jmgmt-methods` through to the estimates (first-stage strength, exclusion logic).

### Branch D: Meta-analysis
- Use the chosen model (Hunter–Schmidt psychometric vs. Hedges–Olkin random-effects); report **k, total N, corrected mean effect, 95% CI, and the 80% credibility interval**.
- Report heterogeneity (Q, I², τ²); run **moderator/meta-regression** tied to competing theories.
- Run **publication-bias diagnostics** (funnel/trim-and-fill, Egger's, PET-PEESE or selection models) and discuss robustness.

## Robustness the JOM audience expects

Because JOM reviewers are methods-literate, anticipate the standard robustness asks rather than waiting for them: report the focal result under alternative specifications (with/without controls, alternative operationalizations), show it is not driven by influential cases, and — for archival work — report the endogeneity-corrected estimate alongside the naive one so the reader sees how much the correction moves the coefficient. Park the full robustness battery in the online supplement and summarize it in a sentence in the main text; the 50-page limit makes the supplement essential, not optional.

## Worked vignette (illustrative)

A multilevel paper claims a cross-level moderation: team climate strengthens the individual-level link between role clarity and performance. The weak version reports a significant level-2 × level-1 product term and stops. The JOM-grade version reports the **ICC(1) = .18** that justifies HLM, grand-mean-centers the level-2 moderator and group-mean-centers the level-1 predictor (stating why), fits a **random-slope** model, reports the cross-level interaction with its CI, and **plots the simple slopes** of role clarity at high vs. low team climate. The plot, not the p-value, is what convinces a reviewer the moderation is real and correctly modeled.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Journal of Management covers empirical management broadly (including meta-analysis); the chain below serves primary causal / panel work.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or
  `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`;
  multilevel data → cluster at the right level.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive battery in the appendix. See the
executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Measurement model reported before the structural model (loadings, CR/ω, AVE, discriminant)
- [ ] Multiple fit indices reported, not a single favorable one
- [ ] Mediation tested with bootstrap CIs; moderation probed with simple slopes/plots
- [ ] Nested data modeled with HLM; ICC and centering reported and justified
- [ ] Effect sizes and CIs reported alongside significance (not asterisks alone)
- [ ] Endogeneity strategy reflected in the estimates (first-stage, diagnostics)
- [ ] (Meta) corrected effects, credibility intervals, heterogeneity, bias diagnostics
- [ ] Analysis matches the level and design from jmgmt-methods

## Reproducibility under masked review

JOM's masked review and its data transparency table mean the analysis must be *describable* in enough detail to reconstruct without revealing the authors. Report the software and key package versions, the estimator and its options (e.g., MLR estimation, bootstrap resamples, centering choices), and how missing data were handled (FIML vs. listwise vs. multiple imputation). Where a method has researcher degrees of freedom — moderator coding in a meta-analysis, item parceling in SEM — state the choice and show the result is not an artifact of it. This is what turns "trust me" into "check me" for a methods-literate referee.

## Anti-patterns

- **Structural model without a measurement model** — reporting paths before establishing the constructs
- **Cherry-picked fit index** (only CFI, hiding a bad RMSEA)
- **Mediation by two significant paths** or a bare Sobel test, no bootstrap CI
- **Unprobed interactions** — a significant product term with no simple slopes or plot
- **OLS on nested data**, ignoring non-independence
- **p-stars without effect sizes** — JOM wants the magnitude, not just the verdict
- **Meta-analysis with no artifact corrections, no credibility interval, no bias check**

## Output format

```
【Branch】SEM/CFA / HLM / regression / meta-analysis
【Measurement】loadings, CR/ω, AVE, discriminant (HTMT?) ...
【Fit / model comparison】CFI/TLI/RMSEA(CI)/SRMR; alt model ...
【Focal effects】coef + effect size + CI (no asterisk-only)
【Mediation/moderation】bootstrap CI / simple slopes / J-N ...
【Multilevel】ICC, centering, random slopes ...
【Meta】k, N, corrected effect, 80% CV, I², bias checks ...
【Next step】jmgmt-contribution-framing
```
