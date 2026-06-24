---
name: popdevr-data-analysis
description: Use when executing and reporting the analysis for a Population and Development Review (PDR, Wiley / Population Council) manuscript so it survives expert, double-anonymized review — correct rate construction, honest uncertainty, and demographic methods done right, with the development/policy meaning of each quantity made clear. Guides analysis and reporting norms; it does not fabricate results.
---

# Data Analysis (popdevr-data-analysis)

PDR reviewers are expert demographers *and* development scholars, and the journal expects analyses that
are reproducible and interpretable to a broad readership. Analyze as if a methodologist will re-derive
your rates and an economist will ask what each number means for development — because both may. This
skill covers execution and reporting norms; method choice lives in `popdevr-research-design`.

## When to trigger

- Constructing rates and life tables; building the results section
- Running a decomposition, event-history, APC, or projection analysis
- A reviewer asked for robustness, sensitivity, or alternative specifications
- Making the analysis reproducible and its development meaning explicit before deposit

## Analysis norms PDR expects

1. **Get the denominators right.** Exposure (person-years), the correct base population, and
   age/period alignment are where demographic analyses live or die. Document how rates were built.
2. **Report uncertainty honestly.** Confidence/credible intervals for rates, life-expectancy
   contributions, projection scenarios, and derived quantities — not just point estimates or stars.
   Bootstrap or delta-method intervals for decomposition components and life-table functions.
3. **Decomposition with clear components.** State precisely what each component (rate vs. composition,
   age contribution, factor) represents and which maps to a development channel; ensure components sum
   to the total being explained.
4. **APC discipline.** Be explicit about the identification problem; report under the stated constraint
   and show sensitivity to plausible alternatives — never imply a unique decomposition.
5. **Survival/event-history rigor.** Check proportional hazards; handle censoring, truncation, and
   competing risks correctly; report on the right time scale (age, duration, period).
6. **Right inference for the data.** Survey/design weights and complex-design variance where applicable;
   cluster at the appropriate level; small-sample corrections when groups (e.g., countries) are few.
7. **Make the development meaning explicit.** For each headline quantity, say what it implies for the
   social, economic, or environmental outcome — the PDR bar is not a clean estimate alone.

## Demographic and comparative computation specifics
- Document data version/vintage (e.g., HMD/HFD/WPP release, DHS round), harmonization steps, and any
  smoothing/graduation applied to rates.
- For projections: report the scenarios, base population, transition-rate assumptions, and sensitivity;
  tie scenarios to development or policy futures where that is the contribution.
- For cross-country work: be explicit about comparability (definitions, coverage, data quality) before
  reading a cross-national contrast as a development effect.

## Reproducibility while you work (not at the end)
- One **master script** regenerates every table, figure, life table, decomposition, and projection from
  the (raw or constructed) data.
- **Set and report seeds** for bootstrap and simulation.
- Pin software/package versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` installs).
- Keep table/figure numbers in the manuscript matched to script outputs (see
  `popdevr-transparency-and-data`).

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). PDR is population studies blending quantitative and policy work; apply the chain to its empirical-causal papers.

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

- Mismatched numerator/denominator or wrong exposure (the classic demographic error)
- Point estimates of life expectancy, decomposition components, or projections with no uncertainty
- An APC model presented as the uniquely correct partition
- Reading a cross-country correlation as a development effect without addressing comparability
- A results section whose rates and decompositions the code cannot reproduce

## Evidence pass for PDR

Run this as a concrete capability pass. First lock the population process, the development/policy
linkage, the data and time scale, the selection/measurement issue, and the uncertainty; then test
whether the manuscript addresses PDR's broad audience who inspect both the population evidence and its
development meaning.

- **Primary move:** Audit unit, comparison, uncertainty, missingness, sensitivity, comparability, and
  reproducibility before making any prose or submission recommendation.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch
  the manuscript directly.
- **Sibling comparison:** compare against *Demography* and *Population Studies* (methods-forward),
  *Population Research and Policy Review* (applied policy), and *Studies in Family Planning* (programs);
  if a neighbor has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for
  volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Main quantity】rate / e0 / decomposition / hazard / projection + magnitude + interval
【Development meaning】what it implies for the social/economic/environmental outcome
【Exposure / denominator check】correctly constructed? [Y/N]
【Decomposition】components defined + sum to total? [Y/N/NA]
【APC / comparability】constraint stated / cross-country comparability addressed? [Y/N/NA]
【Inference】weights/clustering/competing risks handled? [Y/N]
【Reproducible】master script + seeds + pinned versions? [Y/N]
【Next】popdevr-tables-figures
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — life-table, decomposition, survival, APC, and projection packages
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-availability and reproducibility expectations
