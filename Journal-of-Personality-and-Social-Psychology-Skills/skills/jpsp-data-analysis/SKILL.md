---
name: jpsp-data-analysis
description: Use when analyzing and reporting the multi-study package for a Journal of Personality and Social Psychology (JPSP) manuscript to JARS standard — effect sizes with uncertainty, honest robustness, and an internal meta-analysis that pools effects across studies. Guides analysis and reporting norms; it does not fabricate results.
---

# Data Analysis & Internal Meta-Analysis (jpsp-data-analysis)

JPSP reviewers are methodologically sophisticated and the journal requires **JARS** reporting and
**TOP Level 2** transparency. Two things set JPSP analysis apart from short-report work: (1) you are
analyzing a **set of studies**, and (2) the section expects you to **integrate across them** — an
**internal meta-analysis** is a core move, explicitly prioritized in IRGP guidance. This skill covers
execution and reporting; design lives in `jpsp-study-design`.

## When to trigger

- Analyzing studies and building the results sections
- Pooling effects across your own studies (internal meta-analysis)
- A reviewer asked for robustness, mechanism, or alternative-explanation analyses
- Reconciling preregistered vs. exploratory analyses

## Analysis norms JPSP expects

1. **Effect sizes with uncertainty.** Report standardized effect sizes and **confidence (or credible)
   intervals**, not just p-values/stars; state the **substantive magnitude**, per JARS.
2. **Internal meta-analysis across studies.** Pool the comparable effects from all studies (including
   any reported only in the supplement) into a **random-effects estimate with a forest plot**;
   report heterogeneity. This is the package's strongest summary and an explicit section expectation.
3. **Accessible results sections.** Write results for readers with **general statistical expertise**;
   relegate complex justification to tables, notes, or supplements (IRGP house rule; verify).
4. **Honest robustness.** Show specifications that could *break* an effect (alternative measures,
   exclusions, estimators); report what held and what did not.
5. **Mechanism done right.** Report mediation/process with bootstrapped indirect effects and CIs;
   do not over-claim causal mediation from cross-sectional data.
6. **Alternative explanations.** Provide the focused alternative-explanation analyses the section asks
   for (construct validity, confounds, alternative mediators/causal models).
7. **Registered vs. exploratory.** Clearly separate confirmatory (preregistered) from exploratory
   analyses; reconcile and justify any deviations from the plan.
8. **Measurement.** Report reliability and, where relevant, measurement invariance (especially PPID
   individual-differences and dyadic work).

## Reproducibility while you work (not at the end)

- A **master script** regenerates every table and figure from the raw/constructed data, per study.
- **Set and report seeds** for bootstrap, simulation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`).
- Post data/code/materials to a **trusted repository** with a persistent identifier (TOP Level 2).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JPSP is predominantly experimental social/personality psychology; randomization inference, mediation done right (`mediate`, not naive controlling-away), power, and family-wise corrections are decisive.

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

- Stars-only tables with no effect sizes or intervals
- Reporting each study in isolation and skipping the internal meta-analysis
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Over-claiming causal mediation from correlational designs
- Burying a failed study instead of pooling it honestly into the meta-analysis

## Reviewer-pushback patterns and the analysis-side fix

These are the recurring post-credibility-revolution objections a JPSP section reviewer raises about results, and the move that defuses each. The fix is an *analysis-and-reporting* fix — design lives in `jpsp-study-design`.

| Reviewer says | What they distrust | The JPSP-fit fix |
|---------------|--------------------|------------------|
| "Stars only — where are the effect sizes?" | You hid magnitude behind significance | Report d/r/β with **95% CIs** and a sentence on substantive meaning, per JARS |
| "Each study reads in isolation" | No cumulative claim | Add the **internal meta-analysis**: pooled estimate + forest plot + heterogeneity (I²) |
| "This could be a confound" | Alternative causal account | A focused alternative-explanation analysis or a study that manipulates the confound |
| "Mediation is over-claimed" | Causal language on cross-sectional data | Bootstrapped indirect effect with CI, hedged: "consistent with, not proof of, the path" |
| "Was this predicted?" | Suspected HARKing | A confirmatory/exploratory table mapping each test to the **preregistration**; flag deviations |

## Worked micro-example: pooling a preregistered three-study package

*Illustrative numbers — invented to show the reporting logic, not real results.*

Three ASC studies estimate the same gratitude→construal effect. Per-study d (95% CI): S1 = 0.34 [0.10, 0.58], S2 = 0.21 [−0.02, 0.44], S3 = 0.40 [0.16, 0.64]. S2 alone is "non-significant" — the trap that invites a reviewer to call the package inconsistent. The **internal meta-analysis** instead reports a random-effects pooled d ≈ 0.31, 95% CI [0.18, 0.45], low heterogeneity (I² ≈ 12%). That one sentence — *"across three preregistered studies, pooled d = 0.31 [0.18, 0.45]"* — is the strongest summary in the paper and exactly what an ASC reviewer means by integrative analysis. Report S2 inside the pool, not as a footnote.

## Output format

```
【Per-study effects】effect size + CI + substantive meaning
【Internal meta-analysis】pooled random-effects estimate + heterogeneity + forest plot
【Mechanism】indirect effect + bootstrapped CI (design caveats)
【Robustness】specs that could break it → what held
【Registered vs exploratory】clearly separated?
【JARS + repository】reported to standard + data/code/materials posted? [Y/N]
【Next】jpsp-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — metafor (internal meta-analysis), lavaan/PROCESS, effect-size + reliability tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JARS, TOP Level 2, and IRGP integrative-analysis expectation
