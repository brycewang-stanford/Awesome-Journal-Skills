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

## Anti-patterns

- Stars-only tables with no effect sizes or intervals
- Reporting each study in isolation and skipping the internal meta-analysis
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Over-claiming causal mediation from correlational designs
- Burying a failed study instead of pooling it honestly into the meta-analysis

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
