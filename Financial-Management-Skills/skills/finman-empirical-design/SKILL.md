---
name: finman-empirical-design
description: Use when the sample construction, variable measurement, panel structure, or inference of a Financial Management (FM) manuscript is fragile — before identification can be trusted or exhibits finalized. Hardens the data layer; it does not establish the causal claim (finman-identification) or run robustness (finman-robustness).
---

# Empirical Design (finman-empirical-design)

## When to trigger

- The sample comes from CRSP / Compustat / a vendor feed and the screens and survivorship choices are not documented
- A key variable (leverage, payout, governance index, a return measure) has several definitions and you picked one without justification
- The panel mixes frequencies, has look-ahead bias, or merges datasets on a fragile key
- Standard errors are reported but the clustering and cross-sectional/time dependence are not justified

## The FM empirical-design bar

FM publishes empirical finance across corporate, asset-pricing, and banking data, so the design layer is judged on whether **a competent referee could reconstruct your sample and trust your measures**. The journal's "less weight on trivial robustness" stance is a double-edged sword: it means you should not bury the paper in redundant checks, *but* it raises the premium on getting the **primary design right the first time** — the screens, the variable definitions, the merge, and the inference. FM referees in corporate finance are especially alert to silent sample screens, point-in-time vs. restated accounting data, and clustering that ignores the panel's dependence structure.

## The data-layer audit

| Layer | What FM referees check | Common failure |
|-------|------------------------|----------------|
| Sample frame | universe, date range, every screen stated with counts dropped | "standard filters" with no attrition table |
| Survivorship / look-ahead | delisted firms retained; accounting data point-in-time | using restated Compustat as if known contemporaneously |
| Variable construction | each key variable defined, winsorization level stated, source field named | a leverage measure that silently switches book/market |
| Merge integrity | join keys, match rate, unmatched-firm bias | CRSP-Compustat merge with an unreported low match rate |
| Panel structure | frequency, balanced vs. unbalanced, entry/exit handling | mixing annual and quarterly without stating it |
| Inference | clustering level justified by the dependence; few-cluster / two-way addressed | white SEs on a firm-year panel with serial correlation |

## Hardening sequence

1. **Build the attrition table.** Start from the raw universe and report the count dropped at each screen; this single exhibit answers most sample-construction doubts.
2. **Pin every key variable to a source field and a definition.** State winsorization (typically 1%/99%) and why; if a variable has competing definitions, justify yours and note the alternative goes to the appendix.
3. **Defend point-in-time discipline.** For accounting variables, use data as it would have been known; for returns, avoid look-ahead in signal construction.
4. **Justify the clustering.** Cluster at the level where the shocks are correlated (firm, industry, state); use two-way (firm and time) when both dimensions have common shocks; address few-cluster with wild-cluster bootstrap.
5. **Report power/economic scale.** State N, the dependent-variable mean, and the standard-deviation-scaled effect so a reader sees the magnitude in context.

## Execution bridge (StatsPAI / Stata MCP)

Run the asset-pricing battery, don't just specify it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Financial Management is empirical corporate finance + asset pricing; corporate-causal chain (DiD/IV/RDD) plus the factor-zoo haircut for cross-sectional pricing.

- **Factor regressions / time-series alphas:** `feols` with the right SEs (Newey–West /
  clustered) — read the alpha and t off the return.
- **Factor-zoo haircut:** after disclosing how many signals were screened, apply
  `romano_wolf` / `benjamini_hochberg` and report the alpha that survives.
- **Fama–MacBeth + Shanken EIV** are Stata-canonical — run via `mcp__stata-mcp__stata_do`
  with the vendored `resources/code/` (`asreg` / `xtfmb`).
- **Exhibits:** `etable`; hand formatting to the tables/figures skill.

Report the economic magnitude (bps/month alpha, Sharpe gain); full factor grid → appendix.
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Attrition table from raw universe to estimation sample, with counts per screen
- [ ] Every key variable defined, winsorization stated, source field named
- [ ] Survivorship and look-ahead bias addressed (point-in-time accounting; clean signals)
- [ ] Merge keys and match rate reported; unmatched-firm bias discussed
- [ ] Panel frequency and balanced/unbalanced status stated; entry/exit handled
- [ ] Clustering level justified; two-way / few-cluster handled where needed
- [ ] Dependent-variable mean and N reported so magnitudes are interpretable

## Anti-patterns

- "We apply standard filters" with no attrition table or counts
- Restated accounting data used as if it were known at the time (look-ahead)
- A leverage / payout / governance measure that silently switches definition across tables
- CRSP-Compustat (or vendor) merges with an unreported or low match rate
- White / homoskedastic SEs on a firm-year panel with obvious serial and cross-sectional dependence
- Reporting only t-statistics with no dependent-variable mean to anchor the magnitude

## Worked vignette (illustrative)

A draft studies payout on a "standard Compustat sample" with white standard errors. A referee cannot reconstruct it. The FM fix: add Table 1 Panel A as an attrition table (raw universe → drop financials/utilities → drop missing payout → final N), define payout precisely as dividends-plus-repurchases over assets winsorized at 1%/99%, switch to standard errors clustered by firm and year (the panel has both firm persistence and common market shocks), and report the dependent-variable mean so the coefficient's economic size is legible. The design is now reconstructable and the inference defensible.

## Data-source notes specific to finance

- **Compustat:** beware restated data — use point-in-time (PIT) snapshots for accounting variables that signals are built from; flag any look-ahead in the merge.
- **CRSP:** retain delisted securities and apply delisting returns; survivorship bias from dropping them inflates many results.
- **CRSP–Compustat link:** report the link table used and the match rate; unmatched firms skew toward small/young/foreign issuers.
- **Vendor / hand-collected data (governance, syndicated loans, microstructure):** describe coverage, the time window, and any sample selection the vendor's universe imposes — FM referees ask "what is *not* in this dataset?"
- **Returns:** state whether returns are gross or net, the holding-period convention, and how microcaps/penny stocks are treated.

## Referee pushback mapped to the design fix

- *"I can't reproduce your sample."* → Add the attrition table from the raw universe with counts dropped per screen.
- *"Your accounting variable uses restated data."* → Switch to point-in-time data and say so in the note.
- *"The standard errors look too small."* → Justify and report two-way (or wild-cluster) standard errors matched to the panel's dependence.
- *"Is this effect economically meaningful?"* → Report the dependent-variable mean and a one-SD-scaled effect.

## When the design choice is itself the contribution

Some FM papers earn their place through a *measurement* or *sample-construction* innovation — a cleaner proxy, a newly merged dataset, a hand-collected sample. When that is the contribution:

- **Validate the new measure** against an external benchmark or a known case, not just internal consistency.
- **Show what it captures that prior proxies miss**, with a side-by-side comparison.
- **Document construction in painstaking detail** in the internet appendix, because the measure *is* the asset and referees will probe it.
- **Connect the measurement gain to a substantive finding** — a better proxy is interesting at FM only if it changes what we conclude about a decision-relevant question.

## Output format

```
【Sample frame】universe + date range + screens (attrition table? [Y/N])
【Key variables】defined + winsorized + source fields named? [Y/N]
【Bias controls】survivorship / look-ahead handled? [Y/N]
【Merge】keys + match rate reported? [Y/N]
【Inference】clustering level justified; two-way/few-cluster handled? [Y/N]
【Magnitude】dep-var mean + N reported? [Y/N]
【Next skill】finman-robustness
```
