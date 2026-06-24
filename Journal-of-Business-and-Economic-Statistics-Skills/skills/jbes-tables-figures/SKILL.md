---
name: jbes-tables-figures
description: Use when designing the simulation tables and figures for a Journal of Business & Economic Statistics (JBES) methods paper so size, power, coverage, and the empirical results are legible to both statisticians and applied economists. Improves exhibits; it does not change results.
---

# Tables & Figures (jbes-tables-figures)

## When to trigger

- Simulation tables are dense and a reader cannot read off whether the method controls size
- Size, power, coverage, bias, and RMSE are scattered instead of side-by-side
- Figures lack confidence bands, or compare against no baseline
- Exhibit notes do not state the DGP, sample size, replications, or nominal level

## What JBES exhibits must communicate

A JBES paper is judged by method experts who read the tables as the evidence. Exhibits carry two distinct jobs: the **Monte Carlo exhibits** that establish the method's statistical properties, and the **empirical exhibits** that establish relevance on real data. Both must be readable by a statistician *and* an applied economist, since the journal bridges the two communities.

## Monte Carlo exhibits

- Put **size and power side-by-side** across DGPs and sample sizes; mark the nominal level so over/under-rejection is obvious.
- For interval methods, report **coverage and average length** together; for point estimators, **bias and RMSE** together.
- Always show the **incumbent baseline** in the same table under identical DGPs.
- Figures: size-power curves, coverage-vs-n plots, empirical-vs-nominal QQ plots, sampling distributions with the asymptotic reference overlaid.

## Empirical exhibits

- Report estimates with appropriate (HAC/cluster/dependence-robust) standard errors.
- Show the substantive payoff: what the new method changes relative to the standard approach.

## Self-contained notes (every exhibit)

State the DGP or data source, sample size(s), number of Monte Carlo replications, nominal level, the estimator/test, the inference method, and units. A reader should not need the body to interpret the table.

## Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result, not by retyping numbers (the usual source of
body-vs-appendix drift). Full map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md).

- **Tables:** `etable` (multi-model columns) or `did_summary_to_latex` straight from the
  `result_id` — one variable definition, one set of numbers, body and appendix in sync.
- **Figures:** `plot_from_result` / `enhanced_event_study_plot` / `event_study_table` —
  axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units.

See a full fitted-result → exhibit chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Size and power readable side-by-side, with nominal level marked
- [ ] Coverage shown with average length; bias shown with RMSE
- [ ] Incumbent baseline in the same exhibit under identical DGPs
- [ ] Figures have confidence bands / reference distributions
- [ ] Every note states DGP/data, n, replications, level, method, units
- [ ] Vector output (PDF/EPS); no chartjunk; legible in print
- [ ] Numbers match the manuscript text and the code output

## Anti-patterns

- A wall of numbers where size control cannot be read off at a glance
- Reporting power without size (or coverage without length)
- Omitting the baseline, so "improvement" is unquantified in the exhibit
- Notes that force the reader back into the body to decode the table
- Figures with no uncertainty and no reference distribution


## Worked vignette: a size-and-power table a referee can read

A hypothetical JBES paper reports a Monte Carlo size-power table for a new break test (numbers **illustrative**). The good version puts size and power side-by-side across n ∈ {120, 240, 480}, marks the 5% level in the caption, and shows the CUSUM benchmark in the same rows — so a reader sees the new test holds size at 5.2% while CUSUM over-rejects at 8.7%. The note states the DGP, replications, MC standard errors, level, and method.

## Exhibit-pushback patterns (venue-specific fixes)

| JBES referee objection | Fix this skill enforces |
|----|----|
| "I cannot read size control off this table." | Put size and power side-by-side; mark the nominal level in the note |
| "No baseline, so 'improvement' is unquantified." | Place the incumbent in the same exhibit under identical DGPs |
| "The note does not let me interpret the table alone." | State DGP/data, n, replications, level, method, and units in every note |

Calibration anchor (hedged): JBES exhibits serve two audiences — a statistician reading Monte Carlo
properties and an applied economist reading the payoff — so every table must be legible to both. Exact
format specifics are live T&F preflight items.

## Exhibit pass for Journal of Business & Economic Statistics

Run this as a concrete capability pass. First lock the statistical estimand, identification/simulation evidence, empirical illustration, and reproducibility path; then test whether the manuscript addresses econometrics/statistics reviewers who expect methodological credibility plus a business or economic use case.

- **Primary move:** For every table or figure, state the object, sample/case base, uncertainty display, and one sentence the exhibit proves for this venue.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Journal of Econometrics for theory-heavy methods, Econometric Theory for proof-first work, Quantitative Economics for economics-theory methods; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Exhibit】Monte Carlo / empirical
【Size+power】side-by-side with level marked? [Y/N]
【Coverage/length or bias/RMSE】paired? [Y/N]
【Baseline】incumbent in same exhibit? [Y/N]
【Notes】DGP/data, n, reps, level, method, units present? [Y/N]
【Next step】jbes-writing-style
```
