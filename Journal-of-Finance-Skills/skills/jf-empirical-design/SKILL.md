---
name: jf-empirical-design
description: Use when designing or stress-testing an asset-pricing test for a The Journal of Finance (JF) manuscript — factor models, Fama–MacBeth vs. panel, standard-error corrections, out-of-sample discipline. For corporate causal claims use jf-identification.
---

# Asset-Pricing Test Design (jf-empirical-design)

## When to trigger

- You have a candidate predictor / anomaly / factor and must decide how to test it
- You are unsure whether to run Fama–MacBeth, time-series factor regressions, or a panel
- You report t-stats but have not addressed the standard-error subtleties of cross-sectional asset pricing
- A referee will ask "is this just data mining / does it survive multiple testing / does it work out of sample?"

> Scope: this skill is for **asset-pricing tests** (cross-section of returns, factor models, predictability). For corporate / empirical causal effects, route to `jf-identification`.

## Choosing the test

| Goal                                            | Workhorse design                                            |
|-------------------------------------------------|-------------------------------------------------------------|
| Does characteristic X price the cross-section?  | Fama–MacBeth cross-sectional regressions + portfolio sorts  |
| Is a candidate factor priced / spanned?         | Time-series regressions; GRS test; spanning regressions vs. established factors |
| Compare competing factor models                 | Alphas of test assets; max-Sharpe / Hansen–Jagannathan distance; model comparison tests |
| Does a signal predict returns?                  | Predictive regressions + portfolio long-short; in- and out-of-sample R² (Campbell–Thompson) |
| Panel with firm/time variation                  | Panel regression with appropriate fixed effects and clustering |

Pair regression evidence with **portfolio sorts**: JF readers expect both the economically interpretable spread (a tradable long-short return and its Sharpe ratio / alpha) and the regression coefficient.

## Standard errors — get these right

- **Fama–MacBeth** SEs with a **Shanken correction** when betas are estimated (errors-in-variables).
- **Newey–West** (or Hansen–Hodrick) for overlapping returns / autocorrelated series; justify the lag length.
- **Two-way clustering** (firm and time) for panels where both dimensions have correlated residuals.
- Report which correction is used and why; do not present naive OLS SEs for predictive or overlapping data.

## Multiple-testing & out-of-sample discipline

JF is acutely sensitive to factor / anomaly data mining. Address it head-on:

- Cite and apply the multiple-testing logic of Harvey, Liu & Zhu, "…and the Cross-Section of Expected Returns" — a t-stat of 2.0 is not enough when the predictor was chosen from many candidates.
- Report a **higher hurdle** (e.g., Bonferroni / FDR-adjusted, or the elevated t-thresholds in the multiple-testing literature) when the signal was selected from a pool.
- Provide **out-of-sample** evidence: a holdout period, a different market / asset class, or post-publication data.
- Pre-empt "this is in-sample overfitting" by showing the result is not driven by a single decade, a microcap tail, or one industry.

## Checklist

- [ ] Test type is justified by the economic question (sorts + FM, time-series alphas, spanning, predictive)
- [ ] Portfolio sorts AND regressions are both reported; the long-short spread has an economic magnitude (return, Sharpe, alpha)
- [ ] Standard errors use the correct correction (Shanken / Newey–West / two-way clustering) and it is stated
- [ ] Factor exposures are controlled against the relevant established model (e.g., CAPM, Fama–French 3/5-factor, momentum, q-factor)
- [ ] Multiple-testing is addressed when the signal came from a search
- [ ] Out-of-sample / subperiod / size-bucket robustness is shown
- [ ] Microcap and illiquidity concerns are handled (value-weighting, NYSE breakpoints, exclude penny stocks)

## Anti-patterns

- Reporting only the best-performing signal out of many with a naive t > 2
- A long-short return that survives only in equal-weighted microcaps
- Ignoring errors-in-variables (no Shanken correction) in two-pass cross-sectional tests
- Overlapping long-horizon returns with OLS standard errors
- A "new factor" that is spanned by existing factors once you regress it on them
- Claiming predictability with strong in-sample R² but no out-of-sample test

## Output format

```
【Test type】FM / time-series alpha / spanning / predictive / panel
【Economic magnitude】long-short return / Sharpe / alpha = ...
【SE correction】Shanken / Newey–West / two-way cluster
【Benchmark model】CAPM / FF3 / FF5+MOM / q-factor
【Multiple-testing handled?】yes / no
【Out-of-sample evidence】[...]
【Next step】jf-robustness
```
