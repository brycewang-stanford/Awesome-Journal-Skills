---
name: psci-data-analysis
description: Use when analyzing and reporting results for a Psychological Science manuscript. The journal requires effect sizes with confidence intervals, full disclosure of exclusions/conditions/measures, and a clear confirmatory/exploratory split, with analysis scripts and data shared. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (psci-data-analysis)

Psychological Science holds analyses to high credibility standards: **effect sizes with confidence
intervals** for major results, **full disclosure** of how the data were handled, and a clean
**confirmatory vs. exploratory** separation. Analysis scripts and data are shared and can be checked.

## When to trigger

- Running and reporting the main and supporting analyses
- A reviewer asked for effect sizes, intervals, robustness, or disclosure
- Reconciling preregistered analyses with exploratory follow-ups
- Preparing analysis scripts and a data dictionary for deposit

## Reporting norms Psychological Science expects

1. **Effect sizes + uncertainty.** Report a standardized or unstandardized effect size **and a measure
   of uncertainty (e.g., confidence intervals)** for major results — not just p-values and stars.
2. **Full disclosure (the "21-word-solution" spirit).** Report **how sample size was determined**,
   **all** data exclusions (and reasons), **all** manipulations/conditions, and **all** measures. Total
   excluded observations must be stated.
3. **Confirmatory vs. exploratory.** Label preregistered confirmatory analyses separately from
   exploratory ones; do not present exploratory results as predicted (no HARKing).
4. **Appropriate inference.** Justify the model; report assumptions/diagnostics; correct for multiple
   comparisons when testing many outcomes; consider robust or Bayesian alternatives where apt.
5. **Replicability of the analysis.** Provide analysis scripts and a data dictionary; results should
   regenerate from the shared data in a fresh session (see `psci-open-science-and-transparency`).

## Robustness

- Show the result survives reasonable alternative specifications and exclusion choices; report
  sensitivity rather than a single fragile model. For small samples, be candid about uncertainty.

## Worked micro-example (illustrative numbers)

A preregistered two-study package on selective attention. **Study 1** (N = 240, between-subjects)
tests whether a brief mindfulness induction reduces attentional capture by emotional distractors.
The confirmatory analysis is a single preregistered contrast on reaction-time cost.

```
Confirmatory (preregistered) — Study 1
  Effect: induction vs. control on capture cost (ms)
  d = 0.34, 95% CI [0.08, 0.59], t(238) = 2.66, p = .008
  Sensitivity: holds with/without the 6 preregistered RT-outlier exclusions
               (d shifts 0.34 → 0.31), and under log-RT (d = 0.33)
Exploratory (labeled) — Study 1
  Trait-anxiety × condition interaction surfaced post hoc; reported as
  exploratory, flagged for confirmation in Study 2's preregistration
Confirmatory (preregistered) — Study 2 (N = 300, direct + extension)
  Replicates direct effect (d = 0.29, 95% CI [0.06, 0.51]) and
  preregisters the anxiety moderation that was exploratory in Study 1
```

Why this passes Psychological Science scrutiny: every confirmatory number carries an effect size and a
CI; the anxiety interaction is honestly demoted to exploratory and then *promoted to confirmatory* only
after preregistration in Study 2; the sensitivity line pre-empts the "fragile-to-exclusions" reviewer.

## Analysis-stage reviewer pushback and the venue fix

| Reviewer pushback | What it signals here | Psychological Science fix |
|-------------------|----------------------|---------------------------|
| "p = .048 — too close to the line, and the CI nearly spans zero" | post-credibility-revolution distrust of just-significant single tests | report the CI prominently, add the Study 2 replication, lead with the pooled estimate |
| "Which exclusions were preregistered?" | suspicion of undisclosed forking paths | give the disclosure table: rule, count, preregistered vs. post hoc, and the estimate with vs. without |
| "Means hide the distribution" | bar-of-means aesthetic distrusted | recompute and show effect size + CI; route exhibit to `psci-tables-figures` |
| "Is this confirmatory?" | HARKing concern | point to the preregistration timestamp; relabel anything generated after data as exploratory |
| "Reviewer 2 could not rerun your code" | reproducibility gate | ship a fresh-session run log; see `psci-open-science-and-transparency` |

## Calibration anchors

- One adequately powered effect with a tight CI beats three stars on an underpowered model — the
  journal's cautionary history is flashy-but-fragile single studies.
- Prefer estimation language ("the induction reduced capture cost by ~0.3 SD, 95% CI [...]") to
  dichotomous "significant/not." Bare p-value sentences read as pre-reform here.
- When N is modest, state the smallest effect the design could detect rather than implying precision
  you do not have; hedge magnitude claims to what the interval supports.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Psychological Science is short-format experimental psychology with strong open-science norms; preregister, run randomization inference, and report effect sizes with family-wise corrections.

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

- p-values and stars with no effect size or confidence interval
- Selectively reporting conditions, measures, or exclusions (undisclosed flexibility)
- HARKing exploratory findings into confirmatory hypotheses
- Optional-stopping / garden-of-forking-paths analyses presented as planned
- Analysis code that does not reproduce the reported numbers

## Output format

```
【Main result】effect size + confidence interval + meaning
【Disclosure】N-determination + all exclusions + all conditions + all measures reported? [Y/N]
【Confirmatory vs exploratory】clearly separated? [Y/N]
【Inference】assumptions/diagnostics, MHT handled?
【Reproducible】scripts + data dictionary + fresh-session check? [Y/N]
【Next】psci-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — `effectsize`, `emmeans`, `metafor`, JASP/jamovi, reproducible-report tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — statistical and disclosure requirements
