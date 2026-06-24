---
name: eer-robustness
description: Use when a European Economic Review (EER) result must be shown to survive specification, sample, measurement, and inference changes — the robustness battery referees demand. Builds the stress tests and organizes them; it does not establish the core identification or write the prose.
---

# Robustness & Sensitivity (eer-robustness)

## When to trigger

- The headline estimate exists but its fragility has not been probed
- A referee (or co-author) suspects the result is driven by one sample/spec choice
- Inference assumptions (clustering, dependence, multiple testing) are unexamined
- A structural/quantitative result's sensitivity to parameters is not shown

## The EER robustness bar

A general-interest result must be **believable beyond the authors' favorite specification**. EER referees — methods-aware under single-anonymized review — expect a **disciplined battery**, not a scattershot appendix: vary the things that *could plausibly overturn the result*, report them transparently, and say which (if any) move the estimate. The goal is a result that is **robust where it matters and honest where it is fragile**. Robustness is not infinite specification mining; choose tests with a *reason*.

## The robustness battery (choose by design)

| Dimension | Test | Why it matters |
|-----------|------|----------------|
| Specification | add/drop controls; alternative functional form; FE structure | shows the estimate is not a control artifact |
| Sample | leave-one-out (unit/region/year); alternative windows; trimming outliers | shows no single observation drives it |
| Measurement | alternative outcome/treatment definitions; alternative data source | shows it is not a coding choice |
| Estimator | heterogeneity-robust DiD vs TWFE; alternative IV/RDD bandwidth | shows method-robustness |
| Inference | clustering level; wild-cluster bootstrap (few clusters); spatial/cross-sectional dependence; randomization inference | shows SEs are valid under real dependence |
| Multiple testing | Romano–Wolf / Bonferroni–Holm across families | guards against cherry-picked significance |
| Structural | parameter sensitivity; alternative calibration targets; grid/tuning | shows quantity is not a tuning artifact |
| Pre-trends | honest-DiD sensitivity (Rambachan–Roth); placebo timing | bounds violations of parallel trends |

## How to organize it

1. **Pick the threats that could actually overturn the claim** — tie each test to a specific objection.
2. **Lead with the most dangerous test**, not the easiest one.
3. **Report a coefficient-stability table or specification curve** so the reader sees the distribution of estimates.
4. **State the verdict honestly:** "the estimate ranges X–Y across N specifications; it loses significance only when Z."
5. **Push the long tail to the Supplementary material**, keep the load-bearing tests in-text.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). EER is a general economics field journal; the DiD/IV/RDD chain serves its applied lane.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER) or `benjamini_hochberg`.
- **OVB sensitivity:** `oster_delta` / `sensemakr`.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists missing checks + the exact
  `suggest_function` for each.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Decisive checks in the body, exhaustive battery in the appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Each robustness test is tied to a named objection (not decorative)
- [ ] Sample robustness: leave-one-out and alternative windows shown
- [ ] Inference robustness: clustering justified; few-cluster / dependence handled
- [ ] Estimator robustness: modern vs naive estimator agree (or the gap is explained)
- [ ] Multiple-testing correction where several outcomes are tested
- [ ] Structural: parameter/calibration sensitivity reported
- [ ] A coefficient-stability table or spec curve summarizes the distribution
- [ ] Fragilities stated honestly, not hidden

## Anti-patterns

- A robustness appendix that only adds controls and never threatens the result
- Reporting 20 specs that all "confirm" the result while omitting the one that breaks it
- Clustering at a convenient level to shrink standard errors
- Specification mining presented as robustness (no rationale per test)
- Burying a fragility the referee will find anyway — better to disclose and bound it
- Significance stars substituting for a coefficient-stability view

## Worked vignette (illustrative)

An IO paper finds a merger raised prices 4%. A weak appendix re-runs with more controls. An EER battery: leave-one-market-out (range 3.1–4.6%, illustrative), alternative price index, synthetic-control placebo on untreated markets, wild-cluster bootstrap (28 markets), and a Romano–Wolf correction across the three outcomes. Verdict stated plainly: "the price effect is 3.1–4.6% and significant in all but the trimmed-outlier sample, where it is 2.0% (s.e. 1.1)." The reader trusts the number because its fragility was mapped.

## Output format

```
【Core claim under test】one sentence
【Threats probed】[spec / sample / measurement / estimator / inference / MHT / structural]
【Most dangerous test + result】[...]
【Estimate range across specs】X–Y (where it breaks: Z)
【Honest fragilities】[...]
【Next step】eer-tables-figures (present the battery) or eer-referee-strategy
```
