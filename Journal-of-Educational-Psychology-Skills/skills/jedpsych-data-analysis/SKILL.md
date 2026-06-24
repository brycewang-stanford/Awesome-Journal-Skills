---
name: jedpsych-data-analysis
description: Use when analyzing and reporting results for a Journal of Educational Psychology manuscript. JEP expects analyses that respect nesting (multilevel/SEM/growth models), report educationally meaningful effect sizes with confidence intervals, test mechanisms (mediation/moderation), and follow JARS with full disclosure. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (jedpsych-data-analysis)

The Journal of Educational Psychology holds analyses to the standards of a rigorous psychological research
journal *operating in nested educational settings*. The recurring requirements are: **model the nesting**
(students in classes in schools), report **effect sizes with confidence intervals** that are
**educationally interpretable**, test the **mechanism** (mediation/moderation), and disclose fully under
**JARS**. Analysis scripts and data are expected to be shareable and reproducible.

## When to trigger

- Running and reporting the main and supporting analyses
- A reviewer asked for multilevel modeling, effect sizes, mechanism tests, or disclosure
- Reconciling preregistered analyses with exploratory follow-ups
- Preparing analysis scripts and a codebook for deposit

## Reporting norms JEP expects

1. **Respect the nesting.** Use multilevel (hierarchical linear) models, SEM, or growth models that
   account for students nested in classrooms/schools. Cluster-robust or random-effects inference is
   expected; ignoring clustering deflates standard errors and is a standard JEP rejection reason.
2. **Educationally meaningful effect sizes + uncertainty.** Report a standardized effect (e.g., Hedges's
   *g*, a multilevel *d*, R²/variance explained, or a growth-rate difference) **with a confidence
   interval**, and interpret it in learning terms (e.g., months of progress, percentile shift) — not just
   p-values and stars.
3. **Test the mechanism.** JEP is theory-driven: where the hypothesis includes a learning/motivational
   process, fit the mediation (with appropriate multilevel mediation methods) or moderation, not only the
   total effect.
4. **Full disclosure (JARS).** Report how sample size was determined, all conditions and measures, all
   exclusions/attrition (with reasons and counts), missing-data handling (e.g., FIML/multiple imputation),
   and model specification. Confirmatory vs. exploratory must be clearly separated.
5. **Appropriate inference.** Justify the model; report assumptions/diagnostics and fit indices for SEM;
   correct for multiple comparisons across many outcomes; consider robustness to alternative specifications.

## Robustness and missing data

- Show the result survives reasonable alternative specifications (covariate sets, model form, with/without
  exclusions). Handle attrition and missingness with principled methods (FIML, MI) and report rates by arm.

## Worked micro-example (illustrative numbers)

A preregistered cluster-randomized reading-comprehension trial (48 classrooms, ~1,100 students). The
confirmatory analysis is a two-level model with a pretest covariate and a preregistered mediation test.

```
Confirmatory (preregistered) — primary effect
  Two-level model (students within classrooms), pretest-adjusted:
  classroom-level treatment effect on transfer comprehension
  g = 0.23, 95% CI [0.06, 0.40]; ICC = 0.14; ~2.0 months of progress.
  Inference uses random classroom intercepts; SEs respect clustering.
Confirmatory (preregistered) — mechanism
  Multilevel mediation: monitoring gain mediates ~40% of the effect,
  indirect 95% CI [0.02, 0.13] (excludes 0).
Sensitivity: holds with/without the preregistered attrition exclusions
  (g 0.23 → 0.21), and under FIML for missing posttests.
Exploratory (labeled): larger effect for initially low-comprehension
  readers (ATI); reported as exploratory, flagged for future confirmation.
```

Why this passes JEP scrutiny: the model respects nesting; the effect carries a CI *and* an educational
interpretation; the mechanism is tested, not asserted; the sensitivity line pre-empts the "fragile-to-
exclusions" reviewer; and the ATI is honestly demoted to exploratory.

## Analysis-stage reviewer pushback and the venue fix

| Reviewer pushback | What it signals here | JEP fix |
|-------------------|----------------------|---------|
| "You ignored clustering" | deflated SEs from nesting | refit a multilevel/random-effects model; report the ICC |
| "Effect size, and what does it mean for learning?" | post-reform interpretability bar | add a CI and an educational metric (months/percentile) |
| "Mechanism untested" | total effect without theory | fit the preregistered multilevel mediation/moderation |
| "Which analyses were preregistered?" | forking-paths suspicion | give the disclosure table; relabel post hoc as exploratory |
| "How was attrition handled?" | missing-data validity | report rates by arm; use FIML/MI; show robustness |

## Calibration anchors

- One well-powered, properly nested effect with a tight CI and a clear educational interpretation beats a
  pile of stars from a model that treated students as independent — the latter is a routine JEP reject.
- Prefer estimation language ("the intervention raised transfer comprehension by g = 0.23, ~2 months of
  progress, 95% CI [...]") to dichotomous "significant/not."
- Mechanism evidence is what makes the paper educational *psychology* rather than evaluation; budget the
  mediation/moderation test as a first-class result, not an afterthought.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JEdPsych mixes field/lab experiments and observational school data; multilevel (student-in-class-in-school) inference and many-outcome corrections matter most.

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

- Treating nested students as independent (single-level OLS on clustered data)
- p-values and stars with no effect size, CI, or educational interpretation
- Reporting a total intervention effect with no test of the theorized mechanism
- Selective reporting of conditions, measures, or exclusions (undisclosed flexibility)
- Ad hoc deletion of missing data with no principled method or robustness check

## Output format

```
【Model】multilevel / SEM / growth — nesting respected? [Y/N]
【Main result】effect size + CI + educational interpretation
【Mechanism】mediation/moderation tested as hypothesized? [Y/N/NA]
【Disclosure】N-determination + all exclusions/attrition + all measures (JARS)? [Y/N]
【Confirmatory vs exploratory】clearly separated? [Y/N]
【Reproducible】scripts + codebook + missing-data method? [Y/N]
【Next】jedpsych-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `lme4`/`nlme`, `lavaan`/Mplus, `mediation`, `metafor`, `effectsize`, missing-data tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JARS statistical and disclosure requirements
