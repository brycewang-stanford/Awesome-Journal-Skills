---
name: review-of-finance
description: Use when targeting Review of Finance or deciding whether a finance manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Review of Finance (review-of-finance)

## Journal positioning

Review of Finance is the flagship journal of the European Finance Association and the leading European top-tier finance journal, broad and rigorous across the major subfields. It sits just below the finance "top-3" (JF/JFE/RFS) in the elite tier: it wants serious, well-identified contributions to asset pricing, corporate finance, banking, and microstructure, and is a natural home for excellent work that is one notch narrower than a top-3 paper. The readership is international and spans the whole finance profession.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the EFA / Review of Finance / Oxford site and the editorial submission system.

## When to trigger

- The author names Review of Finance (or the elite European/field tier) as the target venue.
- A finance paper is strong and well-identified but narrower than a JF/JFE/RFS contribution, and the author wants a top elite-tier home.
- An applied paper using financial data needs re-framing into a finance contribution with a clear mechanism.
- The author needs Review of Finance's desk-reject risks and a credible top-3 / elite-field alternative list.

## Scope & topic fit

- Asset pricing (empirical and theoretical), cross-section of returns, factor models, with credible robustness.
- Corporate finance, governance, M&A, capital structure, payout, ownership, with credible identification.
- Banking/intermediation, liquidity, market microstructure, household and behavioral finance.
- Internationally oriented finance questions and well-executed work across the field's core paradigms.

## Method & evidence bar

- Identification and economic mechanism, not just significant loadings: a return predictor or corporate-finance effect must survive standard-error corrections, alternative explanations, and out-of-sample / placebo scrutiny.
- Asset-pricing empirics meet current inference standards (multiple-testing/p-hacking, proper standard errors, factor-zoo skepticism).
- Corporate-finance causal claims need a real source of variation (shocks, regulation, discontinuities) with modern DiD/IV/RDD rigor.
- Theory must deliver testable, economically interpretable implications.

## Structure & house style

- The introduction states the question, the economic mechanism, the identification, and the headline magnitude early, and explains why it matters for finance.
- Distinguish the contribution from the nearest top-3 and Review of Finance papers explicitly; "no one has tested X" is not a contribution.
- Review of Finance uses an unstructured abstract and JEL codes; an Internet Appendix carries robustness and secondary results.
- Exhibits report economic magnitudes (not only t-stats); the central result should be readable from one table.

## Official-submission checklist

- Search the live site for "Review of Finance submission guidelines" and follow the current EFA/Oxford version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and the disclosure policy (data sources, conflicts, prior circulation).
- Re-check the current data/code and Internet Appendix requirements and any replication expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters to the broad finance profession.
- [ ] The contribution is stated as mechanism / identification / new measurement, not as a significant coefficient.
- [ ] The introduction positions the paper against the most recent top-3 and Review of Finance work on this question.
- [ ] Inference is robust to current standards (clustering, multiple testing, out-of-sample, placebo).
- [ ] Disclosure, data sources, and the Internet Appendix are ready.

## Common desk-reject triggers

- A "new anomaly / new factor" paper that does not clear the multiple-testing and robustness bar.
- A corporate-finance regression with endogeneity and no credible source of variation.
- Significant coefficients reported without economic magnitude or mechanism.
- A paper that is really accounting or economics framed as finance, or a thin contribution better suited to a broad-volume outlet.

## Re-routing decision

- Top-3 importance → `journal-of-finance`, `journal-of-financial-economics`, `review-of-financial-studies`.
- Peer elite-field venues → `journal-of-financial-and-quantitative-analysis`, `journal-of-corporate-finance`, `journal-of-financial-intermediation`.
- Banking/markets/international → `journal-of-banking-and-finance`, `journal-of-financial-markets`, `journal-of-international-money-and-finance`.
- Quantitative/derivatives theory → `mathematical-finance`; econometrics-of-finance → `journal-of-empirical-finance`; practitioner-relevant corporate finance → `financial-management`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Review of Finance
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / mechanism clear the elite-finance bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / disclosure / Internet Appendix / data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
