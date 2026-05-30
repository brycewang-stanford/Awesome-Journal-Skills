---
name: journal-of-financial-intermediation
description: Use when targeting Journal of Financial Intermediation (JFI) or deciding whether a banking / intermediation manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Financial Intermediation (journal-of-financial-intermediation)

## Journal positioning

The Journal of Financial Intermediation is an Elsevier journal and a leading specialist outlet for the economics of banks and financial intermediaries. It publishes theory and empirics on how intermediaries create liquidity, screen and monitor borrowers, allocate credit, and respond to regulation, and on the broader role of intermediation in the financial system. The readership is finance and banking economists, so a paper must make an intermediation contribution, not merely use bank data.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Elsevier / JFI site and the editorial submission system.

## When to trigger

- The author names JFI (or banking/intermediation field venues) as the target venue.
- A paper studies bank lending, liquidity creation, capital, runs, regulation, or intermediary balance sheets and the author wants a specialist home.
- A general finance or macro-finance paper needs re-framing around the intermediation mechanism.
- The author needs JFI's desk-reject risks and a credible banking / top-finance alternative list.

## Scope & topic fit

- Banking: lending, screening and monitoring, relationship lending, deposit and credit markets, bank capital and runs.
- Liquidity creation, maturity transformation, fragility, and the theory of intermediation.
- Financial regulation and supervision, deposit insurance, capital requirements, and their effects on credit.
- Shadow banking, FinTech intermediaries, securitization, and the architecture of the intermediation system.

## Method & evidence bar

- An intermediation mechanism must be central: a theory of why intermediaries exist or behave as they do, or empirics that isolate intermediary behavior.
- Empirical claims need credible identification — loan-level or bank-level variation, regulatory shocks, discontinuities — with modern DiD/IV/RDD rigor and pre-empted confounders.
- Theory must deliver testable, economically interpretable implications about intermediaries, not generic contracting results.
- Inference meets current standards (clustering at the right level, robustness, placebo where relevant).

## Structure & house style

- The introduction states the intermediation question, the mechanism, the identification or model, and the headline magnitude early.
- Distinguish the contribution from the nearest banking/intermediation papers explicitly; "no one has studied X bank" is not a contribution.
- JFI uses an unstructured abstract and JEL codes; an online appendix carries robustness, derivations, and secondary results.
- Exhibits report economic magnitudes (not only t-stats); the central result should be readable from one table.

## Official-submission checklist

- Search the live site for "Journal of Financial Intermediation guide for authors" and follow the current Elsevier version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and the disclosure policy (data sources, conflicts, prior circulation).
- Re-check the current data/code and online-appendix requirements and any replication expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters for the economics of intermediation.
- [ ] The contribution is stated as an intermediation mechanism / identification / model, not as a significant coefficient.
- [ ] The introduction positions the paper against the most recent banking/intermediation work on this question.
- [ ] Identification and inference (level of clustering, robustness) meet current standards.
- [ ] Disclosure, data sources, and the online appendix are ready.

## Common desk-reject triggers

- A paper that uses bank data but makes no intermediation contribution.
- A credit/lending regression with endogeneity and no credible source of variation.
- A generic contracting model with no specific intermediary mechanism.
- A paper that is really macro (`journal-of-monetary-economics`) or general corporate finance framed as intermediation.

## Re-routing decision

- Top-3 banking/intermediation work → `journal-of-finance`, `journal-of-financial-economics`, `review-of-financial-studies`.
- Peer elite-field venues → `review-of-finance`, `journal-of-financial-and-quantitative-analysis`.
- Broad applied banking / risk / regulation, large volume → `journal-of-banking-and-finance`; corporate-finance core → `journal-of-corporate-finance`.
- Macro-finance / monetary transmission → `journal-of-monetary-economics`, `journal-of-money-credit-and-banking`; international banking flows → `journal-of-international-money-and-finance`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Financial Intermediation
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the intermediation mechanism / identification clear the field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / disclosure / online appendix / data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
