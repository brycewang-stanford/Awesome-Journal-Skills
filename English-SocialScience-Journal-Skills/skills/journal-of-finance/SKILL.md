---
name: journal-of-finance
description: Use when targeting Journal of Finance (JF) or deciding whether a finance manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Finance (journal-of-finance)

## Journal positioning

The Journal of Finance is the official journal of the American Finance Association and, with JFE and RFS, one of the finance "top-3." It publishes the most consequential work across asset pricing, corporate finance, banking/intermediation, and household finance, judged on whether the question and result move the field. The readership is the whole finance profession plus financial economists in economics departments, so a paper must matter beyond its niche.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AFA / Wiley site and the editorial submission system.

## When to trigger

- The author names JF (or the finance top-3) as the target venue.
- A finance paper has a clean design or a genuinely new asset-pricing/corporate-finance insight and the author is choosing among JF / JFE / RFS.
- An applied paper using financial data needs re-framing into a finance contribution rather than an economics or accounting one.
- The author needs JF's desk-reject risks and a credible top-3 / top-field alternative list.

## Scope & topic fit

- Asset pricing (empirical and theoretical), cross-section of returns, factor models — but the bar for "new factor / new anomaly" papers is now very high.
- Corporate finance, governance, M&A, capital structure, payout, with credible identification.
- Financial intermediation, banking, liquidity, market microstructure, household and behavioral finance.
- Empirical regularities that are robust and economically meaningful, not data-mined.

## Method & evidence bar

- Identification and economic mechanism, not just significant loadings: a return predictor or corporate-finance effect must survive standard-error corrections, alternative explanations, and out-of-sample / placebo scrutiny.
- Asset-pricing empirics are held to current inference standards (multiple-testing/p-hacking concerns, proper standard errors, factor-zoo skepticism).
- Corporate-finance causal claims need a real source of variation (shocks, regulation, discontinuities), with the usual DiD/IV/RDD rigor and pre-empted confounders.
- Theory must deliver testable, economically interpretable implications, not only existence results.

## Structure & house style

- The introduction states the question, the economic mechanism, the identification, and the headline magnitude early, and explains why it matters for finance broadly.
- Distinguish the contribution from the nearest JF/JFE/RFS papers explicitly; "no one has tested X" is not a contribution.
- JF uses an unstructured abstract and JEL codes; an Internet Appendix carries robustness and secondary results.
- Exhibits report economic magnitudes (not only t-stats); the central result should be readable from one table.

## Official-submission checklist

- Search the live site for "Journal of Finance submission guidelines" and follow the current AFA/Wiley version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and the disclosure policy (data sources, conflicts, prior circulation).
- Re-check the current data/code and Internet Appendix requirements and any replication expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters to the broad finance profession.
- [ ] The contribution is stated as mechanism / identification / new measurement, not as a significant coefficient.
- [ ] The introduction positions the paper against the most recent JF/JFE/RFS work on this question.
- [ ] Inference is robust to current standards (clustering, multiple testing, out-of-sample, placebo).
- [ ] Disclosure, data sources, and the Internet Appendix are ready.

## Common desk-reject triggers

- A "new anomaly / new factor" paper that does not clear the multiple-testing and robustness bar.
- A corporate-finance regression with endogeneity and no credible source of variation.
- Significant coefficients reported without economic magnitude or mechanism.
- A paper that is really accounting (`the-accounting-review`, `journal-of-accounting-and-economics`) or economics (`journal-of-political-economy`) framed as finance.

## Re-routing decision

- Excellent but more specialized → `journal-of-financial-economics` (often more empirical/structural) or `review-of-financial-studies`.
- Second-tier-elite finance → `review-of-finance`, `journal-of-financial-and-quantitative-analysis`, `journal-of-financial-intermediation`.
- Banking/markets/international → `journal-of-banking-and-finance`, `journal-of-financial-markets`, `journal-of-international-money-and-finance`.
- Accounting-information or disclosure core → the accounting venues; macro-finance → `journal-of-monetary-economics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Finance
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / mechanism clear the finance top-3 bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / disclosure / Internet Appendix / data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
