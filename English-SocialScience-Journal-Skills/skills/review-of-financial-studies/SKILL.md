---
name: review-of-financial-studies
description: Use when targeting Review of Financial Studies (RFS) or deciding whether a finance manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Review of Financial Studies (review-of-financial-studies)

## Journal positioning

The Review of Financial Studies is published by the Society for Financial Studies and, with JF and JFE, one of the finance "top-3." It is the top-3 outlet most associated with methodological innovation — new methods, new theory, and new ways of looking at asset pricing and corporate finance — and it runs a registered-reports track for hypothesis-driven empirical work. The readership is the whole finance profession, so a paper must matter beyond its niche and ideally push the methodological or conceptual frontier.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the SFS / RFS / Oxford site and the editorial submission system.

## When to trigger

- The author names RFS (or the finance top-3) as the target venue.
- A finance paper introduces a new method, a new theoretical angle, or a methodologically innovative empirical design, and the author is choosing among JF / JFE / RFS.
- The author is considering RFS's registered-reports track for a pre-specified, hypothesis-driven study.
- The author needs RFS's desk-reject risks and a credible top-3 / top-field alternative list.

## Scope & topic fit

- Asset pricing (empirical and theoretical) and corporate finance, with a premium on methodological or conceptual novelty rather than one more anomaly.
- Banking/intermediation, market microstructure, household and behavioral finance, FinTech and new-data settings.
- Theory that opens a new question or a new modeling approach, and empirical work that brings a new identification or estimation idea.
- Pre-registered, hypothesis-driven empirical studies suitable for the registered-reports format.

## Method & evidence bar

- RFS rewards methodological innovation, but the new method must be correct, well-motivated, and shown to matter — not novelty for its own sake.
- Asset-pricing empirics meet current inference standards (multiple-testing/p-hacking, proper standard errors, factor-zoo skepticism, out-of-sample and placebo evidence).
- Corporate-finance causal claims need a real source of variation with modern DiD/IV/RDD rigor and pre-empted confounders.
- Theory must deliver testable, economically interpretable implications; registered reports must specify hypotheses, data, and analysis in advance.

## Structure & house style

- The introduction states the question, the methodological or conceptual advance, the identification or model, and the headline magnitude early, and says why it matters for finance broadly.
- Distinguish the contribution from the nearest JF/JFE/RFS papers explicitly; "no one has tested X" is not a contribution.
- RFS uses an unstructured abstract and JEL codes; an Internet Appendix carries robustness, derivations, and secondary results.
- Exhibits report economic magnitudes (not only t-stats); the central result should be legible from one table or figure.

## Official-submission checklist

- Search the live site for "Review of Financial Studies submission guidelines" and follow the current SFS/Oxford version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and the disclosure policy (data sources, conflicts, prior circulation).
- Re-check the current registered-reports track rules and the data/code and Internet Appendix requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters to the broad finance profession.
- [ ] The contribution is stated as method / theory / identification / new measurement, not as a significant coefficient.
- [ ] The introduction positions the paper against the most recent JF/JFE/RFS work on this question.
- [ ] Inference is robust to current standards; if a registered report, the pre-specified design is complete.
- [ ] Disclosure, data sources, and the Internet Appendix are ready.

## Common desk-reject triggers

- A "new method" that is unmotivated, incorrect, or shown not to change any substantive conclusion.
- A "new anomaly / new factor" paper that does not clear the multiple-testing and robustness bar.
- A corporate-finance regression with endogeneity and no credible source of variation.
- A paper that is really accounting (`the-accounting-review`, `journal-of-accounting-and-economics`) or economics (`journal-of-political-economy`) framed as finance.

## Re-routing decision

- Broad top-3 importance with less methodological novelty → `journal-of-finance`; quantitatively serious / structural empirics → `journal-of-financial-economics`.
- Second-tier-elite finance → `review-of-finance`, `journal-of-financial-and-quantitative-analysis`, `journal-of-corporate-finance`.
- Banking/intermediation, markets, or international → `journal-of-financial-intermediation`, `journal-of-financial-markets`, `journal-of-international-money-and-finance`.
- Pure quantitative/derivatives theory → `mathematical-finance`; econometrics-of-finance methods → `journal-of-empirical-finance`; large-volume applied → `journal-of-banking-and-finance`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Review of Financial Studies
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the method / identification / theory clear the finance top-3 bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / registered reports / Internet Appendix / data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
