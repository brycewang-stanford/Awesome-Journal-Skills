---
name: jfm-robustness
description: Use when results may be sensitive to liquidity-measure choice, sample filters, microstructure noise, or inference for a Journal of Financial Markets (JFM) manuscript. Builds the design-based robustness ledger; it does not invent evidence or citations.
---

# Robustness Strategy (jfm-robustness)

## When to trigger

- The headline holds with the chosen liquidity measure but you have not shown it survives alternatives
- Results may flip with a different sample period, asset universe, or filter rule
- Inference uses plain OLS standard errors on data that are autocorrelated and cross-correlated (panel of stocks over time)
- Microstructure noise (bid-ask bounce, stale quotes, discreteness) could be generating the effect
- A referee will ask "is this the mechanism or the measurement?" and you need each check mapped to a specific threat

## The JFM robustness ledger

JFM referees do not want a wall of robustness tables; they want **each check tied to a named threat** to the microstructure interpretation. Build the ledger threat-first.

| Threat to the microstructure claim | Robustness check that addresses it |
|------------------------------------|-------------------------------------|
| It's the measure, not the mechanism | Re-run with alternative liquidity/impact constructs (quoted↔effective↔realized; Amihud↔intraday impact) |
| It's the filter / sample | Vary inclusion screens, period, asset universe, price/penny screens; subsample by cap/volume |
| It's microstructure noise | Account for bid-ask bounce / discreteness; realized-volatility noise corrections; sampling-frequency sensitivity |
| It's the diurnal pattern | Time-of-day controls or within-bin estimation |
| It's confounded by volatility/volume | Condition on or partial out volatility and volume; show the effect is not mechanical |
| It's bad inference | Cluster by stock and by time (two-way); Newey-West for autocorrelation; wild-cluster bootstrap with few venues |
| It's a few names / event days | Drop influential stocks/days; winsorize; report the distribution, not just the mean |

## Sequencing the checks

1. **Measurement robustness first** — if the result is an artifact of one liquidity construct, nothing else matters.
2. **Inference next** — panel microstructure data are doubly correlated; default OLS SEs overstate precision. State the clustering and why.
3. **Design robustness** — for a market-structure event, placebo dates, alternative control groups, donor sensitivity; honest pre-trends.
4. **Mechanism robustness last** — show the effect strengthens where the microstructure mechanism predicts (e.g., larger in high-adverse-selection names) — this converts robustness into corroboration.

Keep a one-line rationale per check ("addresses the concern that …"). Park the bulk in the Internet Appendix; keep the load-bearing ones in the main text (see `jfm-tables-figures`).

## The microstructure-noise battery

Bid-ask bounce, price discreteness, and stale quotes can manufacture spurious patterns, so a dedicated noise battery is often expected. Standard moves: show the result is not an artifact of the bid-ask bounce (e.g., using mid-quote rather than transaction prices, or signed measures); test sensitivity to the sampling frequency (5-min vs. 1-min vs. tick) since noise dominates at the finest frequencies; for realized-volatility-based measures, apply a noise-robust estimator; and confirm the effect is not driven by the minimum-tick discreteness alone. Naming this battery explicitly signals to the referee that you know microstructure noise is the field's characteristic confounder.

## Worked ledger (illustrative)

Headline: a market-structure change narrows effective spreads by 12 bps. The threat-mapped ledger reads: (1) *measure* — repeat with quoted and realized spreads and with Amihud; effect 9-14 bps across measures; (2) *sample* — split by market cap and by sub-period; significant in both halves; (3) *noise* — show it is not driven by tighter discreteness alone by controlling for the binding-tick fraction; (4) *inference* — two-way cluster by stock and day, t falls from 6.1 to 3.4 but stays significant; (5) *confound* — partial out contemporaneous volatility and volume, effect 10 bps; (6) *mechanism corroboration* — effect is twice as large in high-adverse-selection (high-PIN) names, exactly where theory predicts. Each line names the threat it kills; the corroboration line turns a defensive section into evidence for the mechanism.

## Calibrating how much is enough

JFM does not reward a 20-table robustness appendix; it rewards the *right* checks. The decision rule: include a check if a competent microstructure referee would otherwise doubt the interpretation. Measurement and inference are nearly always load-bearing (keep in main text). Sub-period splits and influential-name drops are usually appendix material. A check that does not map to a named threat should be cut, not kept "to be safe" — orphan tables signal the authors are unsure which concern is real.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JFM is market microstructure and asset pricing — liquidity, price discovery, and cross-sectional return tests where the factor-zoo multiple-testing haircut is salient.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Headline survives at least one alternative liquidity/impact measure
- [ ] Results shown stable across sample period, universe, and key filters
- [ ] Microstructure-noise concern (bounce/discreteness/stale quotes) addressed
- [ ] Inference clusters appropriately (two-way stock×time / Newey-West / wild bootstrap as fits the data)
- [ ] Volatility/volume confound partialled out or shown non-mechanical
- [ ] For market-structure events: placebos, alternative controls, pre-trends
- [ ] Each check has a one-line threat it answers; no orphan robustness tables

## Inference is the most-failed robustness dimension at JFM

Microstructure data tempt authors into overstated precision because the samples are enormous — millions of trades, thousands of stock-days — so t-statistics look huge under naive standard errors. But the observations are not independent: a stock's liquidity is autocorrelated over days, and all stocks share common daily shocks. The correct default is **two-way clustering by stock and by day**; with a market-structure event affecting few venues, add a **wild-cluster bootstrap** for few-cluster bias; with persistent intraday series, consider **Newey-West**. Report the t-statistic under the correct scheme, not the inflated naive one, and state the choice in the table notes. A referee who sees an implausible t = 40 will assume the inference is wrong and discount the whole paper — pre-empt it.

## Anti-patterns

- A robustness section that is a table dump with no stated threat per check
- Plain OLS standard errors on a stock×day panel (understates correlation; JFM referees catch this)
- Showing the result only for the one liquidity measure that works
- Confusing "I added more controls" with "I addressed microstructure noise"
- Hiding a fragile subsample instead of reporting and explaining it

## Turning robustness into corroboration

The strongest JFM robustness sections do not merely show the result does not break — they show it behaves the way the microstructure theory predicts. If the mechanism is adverse selection, the effect should be larger in high-information-asymmetry names (high PIN, small caps, around earnings); if it is inventory cost, larger in low-volume, hard-to-hedge names; if it is fragmentation, larger where venue competition is most intense. A heterogeneity pattern that lines up with the proposed channel is far more persuasive than another column of stable coefficients, because it rules out alternative explanations that would not predict the same cross-section. Plan one such "mechanism-corroboration" cut and give it main-text space; it converts a defensive section into affirmative evidence.

## Output format

```text
【Journal】Journal of Financial Markets (JFM)
【Skill】jfm-robustness
【Measure robustness】alternatives tried + result holds? [Y/N]
【Inference】clustering / NW / bootstrap chosen + rationale
【Noise & confounds】bounce/discreteness + volatility/volume handled? [Y/N]
【Design checks】placebo / alt controls / pre-trends (if event) ?
【Mechanism corroboration】effect strongest where theory predicts? [Y/N]
【Ledger】each check ↔ named threat? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jfm-tables-figures
```
