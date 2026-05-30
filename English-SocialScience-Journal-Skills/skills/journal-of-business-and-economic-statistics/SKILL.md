---
name: journal-of-business-and-economic-statistics
description: Use when targeting Journal of Business and Economic Statistics (JBES) or deciding whether a manuscript at the statistics/econometrics interface fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Business and Economic Statistics (journal-of-business-and-economic-statistics)

## Journal positioning

JBES is an American Statistical Association journal at the interface of statistics and econometrics, publishing both methodological contributions and serious applications to business and economic data. Its territory is time series and forecasting, microeconometrics, and statistical methods applied to economic problems, with the dual standard of statistical soundness and economic relevance. The readership spans statisticians and econometricians, so a paper must be rigorous as method and meaningful as economics/business.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ASA / Taylor & Francis site and the editorial submission system.

## When to trigger

- The author names JBES as the target venue, or wants a statistics/econometrics-interface home.
- A paper develops a statistical/econometric method with a clear business or economic application.
- A time-series, forecasting, or microeconometric paper needs re-framing so the methodological contribution and rigor are foregrounded.
- The author needs JBES's desk-reject risks and a credible methods-interface alternative list.

## Scope & topic fit

- Time series econometrics and forecasting, including volatility, macro/financial time series, and forecast evaluation.
- Microeconometrics applied to business and economic microdata.
- Statistical methodology developed for, or evaluated on, economic and business problems.
- Bayesian and computational methods with economic/business applications.

## Method & evidence bar

- Methodological rigor is the filter: new methods need derived properties, correct inference, and demonstrated advantage over existing tools.
- Applications must be substantive and the method appropriate to the data and question; identification and inference are scrutinized.
- Forecasting claims need proper out-of-sample evaluation and honest comparison to credible benchmarks.
- Both a pure method with no application and an application with weak statistics will struggle; the contribution should advance method-and-application together.

## Structure & house style

- The introduction states the problem, the methodological contribution, and the application early, and explains the statistical and economic relevance.
- Position against the relevant statistics/econometrics literature; relate properties and performance to existing methods explicitly.
- Uses an unstructured abstract; a supplement carries proofs, derivations, simulations, and replication materials.
- Exhibits report estimates/forecasts with proper inference and honest benchmark comparisons; simulation evidence supports method claims.

## Official-submission checklist

- Search the live site for "Journal of Business and Economic Statistics submission guidelines / instructions for authors" and follow the current ASA/Taylor & Francis version.
- Re-check formatting, abstract requirements, anonymization, and supplement/code standards on the submission system.
- Re-check the current data and code / reproducibility policy and supplementary-materials requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the methodological contribution and the business/economic problem it serves.
- [ ] The contribution is stated as a method advance / property / improved inference, not as statistical significance.
- [ ] The introduction positions the paper against the relevant statistics/econometrics frontier.
- [ ] Method properties are derived and supported by simulation; applications use correct inference.
- [ ] Code, data, and supplement are ready for the reproducibility policy.

## Common desk-reject triggers

- A method paper with no application or no demonstrated advantage over existing tools.
- An application with inappropriate or under-justified statistical methods.
- Forecasting claims without proper out-of-sample evaluation or credible benchmarks.
- Significance reported without method validation, magnitude, or relevance.

## Re-routing decision

- Pure econometric theory → `journal-of-econometrics`; methods-in-application with rich data and replication → `journal-of-applied-econometrics`.
- Technically heavy econometrics/theory → `international-economic-review`; general-interest applied result → `american-economic-review`.
- Quantitative-macro time series with a structural model → `review-of-economic-dynamics` or `journal-of-monetary-economics`; broad general field → `european-economic-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Business and Economic Statistics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the method + application clear JBES's interface bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / abstract / supplement / reproducibility / code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
