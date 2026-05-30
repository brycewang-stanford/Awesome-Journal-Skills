---
name: journal-of-financial-and-quantitative-analysis
description: Use when targeting Journal of Financial and Quantitative Analysis (JFQA) or deciding whether a finance manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Financial and Quantitative Analysis (journal-of-financial-and-quantitative-analysis)

## Journal positioning

The Journal of Financial and Quantitative Analysis is an elite field journal in finance, published with Cambridge University Press, known for quantitatively careful empirical corporate finance and asset pricing with attention to methodological soundness. It sits in the top elite tier just below the finance "top-3" (JF/JFE/RFS): JFQA rewards clean, well-measured, technically disciplined work rather than the broadest splash. The readership is the academic finance profession.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the JFQA / Cambridge site and the editorial submission system.

## When to trigger

- The author names JFQA (or the elite-field tier) as the target venue.
- A finance paper is quantitatively careful and well-identified but narrower than a top-3 contribution, and the author wants a strong field home.
- An applied paper using financial data needs re-framing as a methodologically clean finance contribution.
- The author needs JFQA's desk-reject risks and a credible top-3 / elite-field alternative list.

## Scope & topic fit

- Empirical asset pricing, cross-section of returns, factor models, with rigorous measurement and inference.
- Corporate finance, governance, M&A, capital structure, payout, with credible identification.
- Market microstructure, derivatives, fixed income, banking, and household finance with a quantitative bent.
- Methodologically careful empirical work where the measurement and econometrics are the point of pride.

## Method & evidence bar

- JFQA prizes quantitative care: correct standard errors, sensible measurement, and inference that holds up to scrutiny.
- Asset-pricing empirics meet current standards (multiple-testing/p-hacking, factor-zoo skepticism, out-of-sample and placebo evidence).
- Corporate-finance causal claims need a real source of variation with modern DiD/IV/RDD rigor and pre-empted confounders.
- Theory and structural work must be identified and the empirical implementation transparent.

## Structure & house style

- The introduction states the question, the mechanism, the identification, and the headline magnitude early, and explains why it matters for finance.
- Distinguish the contribution from the nearest top-3 and JFQA papers explicitly; "no one has tested X" is not a contribution.
- JFQA uses an unstructured abstract and JEL codes; an online/Internet Appendix carries robustness and secondary results.
- Exhibits report economic magnitudes (not only t-stats); the central result should be readable from one table.

## Official-submission checklist

- Search the live site for "Journal of Financial and Quantitative Analysis submission guidelines" and follow the current Cambridge version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and the disclosure policy (data sources, conflicts, prior circulation).
- Re-check the current data/code and online-appendix requirements and any replication expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters to the academic finance profession.
- [ ] The contribution is stated as mechanism / identification / measurement, not as a significant coefficient.
- [ ] The introduction positions the paper against the most recent top-3 and JFQA work on this question.
- [ ] Measurement, standard errors, and robustness meet current quantitative standards.
- [ ] Disclosure, data sources, and the online appendix are ready.

## Common desk-reject triggers

- A "new anomaly / new factor" paper that does not clear the multiple-testing and robustness bar.
- A corporate-finance regression with endogeneity and no credible source of variation.
- Sloppy measurement or inference in a journal that explicitly values quantitative care.
- A paper that is really accounting or economics framed as finance, or a thin contribution better suited to a broad-volume outlet.

## Re-routing decision

- Top-3 importance → `journal-of-finance`, `journal-of-financial-economics`, `review-of-financial-studies`.
- Peer elite-field venues → `review-of-finance`, `journal-of-corporate-finance`, `journal-of-financial-intermediation`.
- Banking/markets/international → `journal-of-banking-and-finance`, `journal-of-financial-markets`, `journal-of-international-money-and-finance`.
- Pure empirical-methods focus → `journal-of-empirical-finance`; quantitative/derivatives theory → `mathematical-finance`; practitioner-relevant → `financial-management`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Financial and Quantitative Analysis
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the measurement / identification clear the elite-field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / disclosure / online appendix / data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
