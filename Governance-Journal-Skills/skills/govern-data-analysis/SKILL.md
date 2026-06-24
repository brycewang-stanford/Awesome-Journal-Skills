---
name: govern-data-analysis
description: Use when executing and reporting the analysis for a Governance: An International Journal of Policy, Administration, and Institutions manuscript — cross-national inference, clustering and uncertainty, robustness, multi-method triangulation, measurement validity for governance indices, small-N comparative samples, and sensitivity to unobserved confounders. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (govern-data-analysis)

*Governance* reviewers are comparative-method sophisticated and the journal requires a **Data
Availability Statement** describing whether and how replication materials can be accessed. Analyze as if
a competent reader will follow your inference across countries — because they will. This skill covers
execution and reporting norms; design decisions live in `govern-research-design`.

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling pre-specified vs. exploratory analyses (an anonymized pre-analysis plan may be supplied)
- Making the analysis reproducible before drafting the Data Availability Statement

## Analysis norms Governance expects

1. **Cross-national inference, done carefully.** Be explicit about what is identified off within-country
   over-time variation vs. cross-country variation, and which the argument needs. Country-year panels
   with two-way fixed effects answer a different question than a pure cross-section — say which.
2. **Cluster and quantify uncertainty correctly.** Cluster at the level of treatment assignment (often
   country or reform unit); report confidence/credible intervals and effect magnitudes, not just stars.
3. **Robustness that probes, not decorates.** Show specifications that could *break* the result —
   alternative governance measures, country/period subsamples, dropping influential cases, alternative
   estimators — and say what you learned.
4. **Triangulate across methods.** Where the design is mixed, show that quantitative and qualitative
   estimates corroborate; own and interpret divergence rather than hiding it.
5. **Measurement validity for governance indices.** Validate the construct; show the result is not an
   artifact of one index (V-Dem vs. WGI vs. QoG vs. Bertelsmann) or one calibration; carry index
   uncertainty (e.g., V-Dem credible intervals) into the inference where feasible.
6. **Pre-specification discipline.** Clearly separate **pre-specified** from **exploratory** analyses;
   if a pre-analysis plan was supplied, reconcile and justify any deviations.

## Small-N comparative samples (the recurring Governance problem)

- Few countries/clusters break standard cluster-robust SEs: use **wild-cluster bootstrap** or
  randomization/permutation inference; report the cluster count honestly.
- With a small donor pool, consider **synthetic control** (and its placebo/leave-one-out checks) rather
  than over-claiming from a few-unit panel.
- For set-theoretic (QCA) work, report consistency and coverage and probe robustness to calibration and
  threshold choices; do not present a single solution formula as definitive.
- Resist over-fitting: in small samples, a long covariate list and a "clean" table are a warning sign,
  not reassurance.

## Sensitivity to unobserved confounders

Institutional outcomes are confounded by hard-to-measure history and capacity. Report how strong an
unobserved confounder would have to be to overturn the result (e.g., Oster's δ/bounds, sensemakr-style
robustness values, E-values). State the benchmark covariate you compare against.

## Reproducibility while you work (not at the end)

- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, permutation inference, simulation, and any stochastic step.
- Pin software/package versions; record the exact governance-index version and download date.
- Keep manuscript table/figure numbers matched to script outputs, ready for the Data Availability Statement.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Governance is public administration and institutions research — comparative and causal designs on governance reforms; the chain serves its quantitative-causal lane, while comparative-historical / qualitative work uses its own standards.

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

- Stars-only tables with no effect sizes, intervals, or substantive interpretation across countries
- Standard cluster-robust SEs with a handful of countries (few-cluster bias ignored)
- "Robustness" that reruns near-identical specs to manufacture stability
- Treating one governance index as truth; never checking an alternative measure
- Mining for a significant cross-national interaction and theorizing it post hoc
- A results section whose numbers a reader could not reproduce from the materials

## Output format

```
【Main estimate】magnitude + interval + cross-national substantive meaning
【Inference】clustering level; few-cluster correction if N small
【Measurement】index + version; result holds across alternative measures? [Y/N]
【Robustness】specs that could break it → what held
【Sensitivity】strength of unobserved confounder needed to overturn (δ / RV / E-value)
【Pre-specified vs exploratory】clearly separated?
【Reproducible】master script + seeds + pinned index versions? [Y/N]
【Next】govern-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, few-cluster inference, synthetic control, QCA, and sensitivity packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Data Availability Statement and pre-analysis-plan policy
