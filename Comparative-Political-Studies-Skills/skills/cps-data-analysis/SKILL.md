---
name: cps-data-analysis
description: Use when running and reporting the analyses for a Comparative Political Studies (CPS) manuscript — estimation, uncertainty, robustness, and multi-method triangulation on comparative data. Sets analysis norms; it does not choose the identification strategy (see cps-research-design).
---

# Data Analysis (cps-data-analysis)

Once the design is fixed (`cps-research-design`), this skill governs how the analyses are run and
reported so a CPS reviewer trusts them. Comparative data bring distinctive hazards: few clusters
(countries), cross-national measurement error, missing data that differ by regime, and the temptation to
over-read a panel correlation as causal. The standard is modern, transparent, and replication-ready.

## When to trigger

- Estimating the main results, robustness, and heterogeneity
- A reviewer questioned standard errors, specification, measurement, or fragility of the result
- Deciding what goes in the main text vs. the supplementary/online appendix
- Triangulating quantitative estimates with case evidence

## Analysis priorities (in order)

1. **Main estimate that matches the design.** The headline specification should be the one the
   identification argument justifies — not the one with the biggest coefficient or most stars.
2. **Honest uncertainty.** Cluster at the assignment level (usually country / country-year); with few
   countries use wild-cluster bootstrap or randomization inference. Report CIs, not just stars.
3. **Measurement transparency.** Name the source and coding of each comparative variable (e.g., V-Dem,
   Polity, CSES, Manifesto Project); show robustness to alternative codings of the key construct.
4. **Robustness as a coherent story.** Alternative specifications, samples, codings, and estimators that
   probe the *threats named in the design* — not a scattershot table of every variant.
5. **Heterogeneity by theory.** Subgroups/scope conditions pre-specified by the mechanism
   (`cps-theory-building`), not data-mined; adjust for multiple comparisons.
6. **Mechanism evidence.** Tie the quantitative result to the mechanism — mediation cautiously, or case
   evidence in a multi-method design.

## Comparative-data hazards to address explicitly

| Hazard | Symptom | Fix |
|--------|---------|-----|
| Few clusters (countries) | over-rejection, tiny SEs | wild-cluster bootstrap / randomization inference |
| Cross-national measurement error | results flip across codings | show robustness to V-Dem/Polity/alt scales |
| Differential missingness | sample changes by regime type | report attrition; multiple imputation with caution |
| Time-series confounding | spurious trend correlations | unit + period FE; over-time placebo |

## Failure-mode audit

Run this audit before interpreting the main coefficient:

- **Concept equivalence:** Does the key variable mean the same thing across regimes, languages, regions, or
  institutions? If not, report measurement-invariance checks, alternative codings, or scope limits.
- **Selection into observation:** Are only more democratic, richer, more peaceful, or better-measured
  cases observed? Report the observation process and show how estimates change under credible sample
  restrictions.
- **Temporal dependence:** Are observations mechanically persistent across years? Use lag structure,
  unit trends, event-time plots, or placebo leads to avoid re-labeling persistence as effect.
- **Cluster leverage:** Does one country, region, election, conflict, or reform episode drive the result?
  Show leave-one-cluster-out or influence diagnostics for claims that hinge on few cases.
- **Subgroup multiplicity:** If theory predicts heterogeneity, pre-specify the dimensions and report how
  many comparisons were examined.

The output should connect each failure mode to a design threat. Do not add a robustness table unless it
answers a named threat in `cps-research-design`.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). CPS is comparative politics — cross-national and sub-national designs; emphasize identification and clustered / multiway inference.

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
## Checklist

- [ ] Headline specification = the one the design justifies
- [ ] SEs clustered at the assignment level; few-cluster correction where needed
- [ ] Every comparative variable's source and coding named; key construct robust to alt codings
- [ ] Robustness probes the design's named threats; not a kitchen sink
- [ ] Heterogeneity pre-specified by theory; multiple testing addressed
- [ ] Main text vs. appendix split is deliberate; every appendix result is referenced
- [ ] All results reproduce from the script destined for the CPS Dataverse

## Anti-patterns

- Treating a cross-national panel correlation as causal without the design to back it
- Default OLS SEs with 20 countries (massively over-rejects)
- Cherry-picking the coding of the key variable that gives significance
- Robustness theater — many variants that never test the actual threat
- Data-mined subgroups reported as confirmed heterogeneity
- Results in the paper that the deposited code does not reproduce

## Output format

```
【Headline result】estimate + CI, with the design it rests on
【Inference】clustering level + few-cluster correction if any
【Measurement】sources/codings + alt-coding robustness
【Failure-mode audit】concept equivalence / observation selection / temporal dependence / cluster leverage / multiplicity
【Robustness】the design-threats probed
【Heterogeneity】theory-driven subgroups + multiple-testing fix
【Reproducible?】script regenerates every exhibit [Y/N]
【Next】cps-tables-figures
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — clean → estimate → robustness → tables skeleton (Stata + Python)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation and inference packages (R / Stata / Python)
