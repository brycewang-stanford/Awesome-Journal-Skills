---
name: sf-data-analysis
description: Use when executing and reporting the analysis for a Social Forces (SF) manuscript so it survives expert, double-anonymized review — honest uncertainty, robustness, and triangulation appropriate to quantitative, demographic, network, or computational work. Guides analysis norms; it does not fabricate results.
---

# Data Analysis (sf-data-analysis)

Social Forces built its standing on **methodological rigor**, and its reviewers are sophisticated. The
analysis must report uncertainty honestly, probe robustness that could actually break the result, and
stay reproducible. This skill covers execution and reporting norms; design decisions live in
`sf-research-design`. Keep an eye on the exhibit budget — results must fit within **10 tables and
figure panels** (see `sf-tables-figures`).

## When to trigger

- Running main and supporting analyses; building the results section
- A reviewer asked for robustness, heterogeneity, or alternative specifications
- Reconciling confirmatory vs. exploratory analyses
- Making the analysis reproducible before drafting the data availability statement

## Analysis norms SF expects

1. **Report uncertainty honestly.** Confidence/credible intervals, not just stars; the magnitude and
   substantive meaning of the estimate, not just its significance.
2. **Robustness that probes, not decorates.** Show specifications that could *break* the result
   (alternative measures, samples, estimators, fixed effects), and say what you learn.
3. **Heterogeneity with discipline.** Pre-specify subgroups where possible; correct for multiple
   comparisons; do not mine for a significant interaction and theorize it post hoc.
4. **Right inference.** Cluster at the assignment/sampling level; use survey weights and design-based
   inference for complex samples; small-cluster corrections (wild-cluster bootstrap) when clusters are few.
5. **Measurement.** Validate constructs; report reliability; show the result is not an artifact of a
   coding/scaling choice.
6. **Missing data.** Be explicit — multiple imputation or principled handling, not silent listwise
   deletion that changes the sample.

## Demographic / computational / network specifics
- Demographic: report standardization/decomposition choices; handle censoring and competing risks.
- Computational/text: document model/version, hyperparameters, seeds; validate against human labels.
- Network: state the null/baseline; report sensitivity to boundary and tie-definition choices.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table and figure from the (raw or constructed) data.
- **Set and report seeds** for bootstrap, simulation, imputation, and any stochastic step.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers matched to script outputs — and feed the **data availability statement**
  (see `sf-data-and-transparency`).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Social Forces is quantitative sociology — survey and administrative panels; emphasize identification, decomposition, and multilevel inference.

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
- "Robustness" that only reruns near-identical specs to manufacture stability
- p-hacking / fishing for a significant interaction; HARKing exploratory results into hypotheses
- Ignoring survey weights/design, or clustering at the wrong level
- A results section whose numbers the code cannot reproduce


## Evidence pass for Social Forces

Treat this skill as an executable review pass, not a prose hint. First lock the social mechanism, data scope, identification or interpretation, and contribution to a wider literature; then judge whether the current manuscript answers the venue's real reader: social-science reviewers who want generalizable social-process evidence across sociology, demography, and policy-adjacent topics.

- **Do the pass:** Audit the research design before polishing prose: unit of analysis, comparison set, uncertainty, sensitivity, missingness, and reproducibility must be visible.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ASR/AJS for top sociology theory stakes, Demography for population process, JMF for family-specific claims; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Main estimate】magnitude + interval + substantive meaning
【Identification check】(per research-design) result
【Robustness】specs that could break it → what held
【Heterogeneity】pre-specified? MHT-adjusted?
【Inference】weights/clustering/few-cluster handled correctly? [Y/N]
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】sf-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, demography, network, and text-as-data packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data availability statement requirement
