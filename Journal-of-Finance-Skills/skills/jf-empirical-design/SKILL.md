---
name: jf-empirical-design
description: Use when designing or stress-testing an asset-pricing test for a The Journal of Finance (JF) manuscript — factor models, Fama–MacBeth vs. panel, standard-error corrections, out-of-sample discipline. For corporate causal claims use jf-identification.
---

# Asset-Pricing Test Design (jf-empirical-design)

## When to trigger

- You have a candidate predictor / anomaly / factor and must decide how to test it
- You are unsure whether to run Fama–MacBeth, time-series factor regressions, or a panel
- You report t-stats but have not addressed the standard-error subtleties of cross-sectional asset pricing
- A referee will ask "is this data mining / does it survive multiple testing / does it work out of sample?"

> Scope: this skill is for **asset-pricing tests**. For corporate/empirical causal effects, route to `jf-identification`.

## Choosing the test

| Goal                                            | Workhorse design                                            |
|-------------------------------------------------|-------------------------------------------------------------|
| Does characteristic X price the cross-section?  | Fama–MacBeth cross-sectional regressions + portfolio sorts  |
| Is a candidate factor priced / spanned?         | Time-series regressions; GRS test; spanning vs. established factors |
| Compare competing factor models                 | Alphas of test assets; max-Sharpe / HJ distance; model comparison |
| Does a signal predict returns?                  | Predictive regressions + long-short; in/out-of-sample R² (Campbell–Thompson) |
| Panel with firm/time variation                  | Panel with appropriate fixed effects and clustering         |

## JF-specific standards

JF asset-pricing referees engage the JF-published canon — **Sharpe (1964) CAPM, Fama–French (1992), Jegadeesh–Titman (1993) momentum, Carhart (1997)** — and expect you to benchmark against the right factors (recall the FF three-factor model is JFE 1993). They also expect:
- **Errors-in-variables / Shanken correction** on Fama–MacBeth standard errors where betas are estimated.
- **Multiple-testing discipline**: a new anomaly must survive the "factor zoo" critique (Harvey, Liu & Zhu, JF) — adjusted t-thresholds, not the naive 1.96.
- **Out-of-sample** evidence for predictability claims, not just in-sample fit.
- **Economic magnitude** (Sharpe gain, alpha in bps), since JF writes for a general-interest reader.
- Exhaustive specifications go to the **Internet Appendix** (bundled in the same PDF; see `jf-internet-appendix`), keeping the body within 60 pages.

## Worked vignette — a risk-vs-mispricing horse race

*Illustrative numbers.* A new characteristic predicts the cross-section: a long–short decile spread of 0.60%/month, raw t = 3.3. The JF question is not "is it significant?" but "is it risk or mispricing, and does it survive the canon?"

1. **Benchmark against the right factors.** Regress on Fama–French five factors + momentum; suppose the alpha is 0.42%/month (t = 2.9). The shrinkage from 0.60 already shows part of the spread is known-factor exposure.
2. **Clear the multiple-testing bar.** If mined from many candidates, t = 2.9 must beat the factor-zoo cutoff (Harvey–Liu–Zhu argue ~3.0, illustratively); a borderline t is a referee magnet.
3. **Risk vs. mispricing.** For risk, show the characteristic loads on priced covariance (GRS test). For mispricing, show the alpha concentrates among hard-to-arbitrage names and decays after ~6 months. JF rewards a paper that *adjudicates*.
4. **Out-of-sample.** Campbell–Thompson out-of-sample R² for the predictive version; in-sample-only reads as data-snooping.
5. **Economic magnitude.** Translate to an annualized Sharpe gain (≈ 0.35) so the general-interest reader sees the stake.

The full grid — all factor models, subperiods, cost nets — goes to the **Internet Appendix**; the body carries the alpha table, GRS test, and OOS result.

### Referee-pushback patterns and the JF-specific fix
| Pushback you will hear                              | JF-specific fix                                                  |
|----------------------------------------------------|------------------------------------------------------------------|
| "It's just exposure to known factors"              | Report alphas vs. FF5 + momentum; show the residual spread       |
| "t = 3.3 after mining is not 1.96 territory"       | Apply the factor-zoo-adjusted threshold; disclose the search     |
| "Is this risk or mispricing?"                      | Run the horse race (GRS / covariance vs. arbitrage-limits decay) |
| "In-sample only"                                   | Add out-of-sample R² (Campbell–Thompson) or a holdout            |
| "These are illiquid microcaps"                     | Value-weighted, NYSE-breakpoint, post-cost version               |

## Calibration anchors for JF asset pricing
- The flagship rewards tests that **adjudicate a first-order question** (covariance risk vs. correctable mispricing) over a bare predictive regression.
- SE and multiple-testing conventions evolve; the EIV/Shanken correction and factor-zoo threshold are durable, but confirm the favored estimators and benchmark factor sets against recent JF issues.
- Economic magnitude in interpretable units (Sharpe gain, bps alpha) is non-negotiable in the body, since JF writes for a non-specialist reader.

## Execution bridge (StatsPAI / Stata MCP)

Run the asset-pricing battery, don't just specify it. Full map:
[`shared-resources/empirical-methods/execution-with-mcp.md`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JF asset-pricing instantiation:

- **Factor regressions / time-series alphas:** `feols` with the right SEs
  (`vcov="HC3"` or Newey–West / clustered) — read the alpha and t off the return, not
  off a memory of the spec.
- **The factor-zoo haircut (the JF-salient one):** after disclosing how many signals
  were screened, apply `romano_wolf` (step-down, accounts for cross-signal correlation)
  or `benjamini_hochberg`, and report the alpha that survives the adjusted threshold —
  the executed Harvey–Liu–Zhu discipline.
- **Fama–MacBeth + Shanken EIV correction** are Stata-canonical: run them through the
  Stata MCP (`mcp__stata-mcp__stata_do`) with the vendored `resources/code/` skeleton
  (`asreg`/`xtfmb`, Shanken-adjusted SEs) and reconcile to the Python alpha.
- **Emit JF-format exhibits** with `etable`; hand formatting to `jf-tables-figures`.

Report the **economic magnitude** (bps/month alpha, Sharpe gain) the body requires;
the full factor-model grid and all screened signals go to the bundled Internet Appendix.
If a server is not connected, adapt `resources/code/` and flag any unverified number.

## Checklist

- [ ] Test matched to the question (FM / time-series / panel)
- [ ] Standard errors correct for the design (Shanken, NW, clustering)
- [ ] New factor/anomaly survives a multiple-testing-adjusted threshold
- [ ] Out-of-sample check for any predictability claim
- [ ] Benchmarked against the standard factor models, attributed correctly
- [ ] Economic magnitude reported, not just t-stats

## Anti-patterns

- Reporting raw t > 1.96 as decisive after mining many signals (the factor-zoo trap)
- Fama–MacBeth t-stats with no EIV/Shanken adjustment
- In-sample-only predictability dressed up as a discovery
- Crowding every robustness table into the body instead of the Internet Appendix

## Output format

```
【Test chosen + why】...
【SE correction (Shanken/NW/cluster)】...
【Multiple-testing threshold cleared?】yes / no
【Out-of-sample evidence?】yes / no
【Economic magnitude】...
【Next step】jf-robustness
```
