---
name: journal-of-corporate-finance
description: Use when targeting Journal of Corporate Finance (JCF) or deciding whether a corporate-finance manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Corporate Finance (journal-of-corporate-finance)

## Journal positioning

The Journal of Corporate Finance is an Elsevier journal and the leading specialist outlet dedicated to corporate finance: governance, M&A, capital structure, payout, ownership, and the financial decisions of firms. It sits in the strong field tier, with an explicit emphasis on credible identification, and is the natural home for excellent corporate-finance work that is one notch narrower than a top-3 contribution. The readership is corporate-finance researchers.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Elsevier / JCF site and the editorial submission system.

## When to trigger

- The author names JCF (or corporate-finance field venues) as the target venue.
- A corporate-finance paper is well-identified but narrower than a JF/JFE/RFS contribution and the author wants a specialist home.
- A general finance or governance paper needs re-framing as a firm-financial-decision contribution.
- The author needs JCF's desk-reject risks and a credible top-3 / elite-field alternative list.

## Scope & topic fit

- Corporate governance, boards, ownership structure, blockholders, and shareholder activism.
- Mergers and acquisitions, takeovers, restructuring, and the market for corporate control.
- Capital structure, financing decisions, payout policy, dividends, and repurchases.
- Executive compensation, investment policy, and the broader financial decision-making of firms.

## Method & evidence bar

- Credible identification is the journal's stated priority: causal claims need a real source of variation (regulatory shocks, plausibly exogenous events, discontinuities) with modern DiD/IV/RDD rigor and pre-empted confounders.
- Endogeneity must be confronted head-on; a panel regression with firm fixed effects alone rarely suffices for a causal claim.
- Measurement of governance, ownership, and financing variables must be defensible.
- Inference meets current standards (clustering, robustness, placebo where relevant).

## Structure & house style

- The introduction states the corporate-finance question, the mechanism, the identification, and the headline magnitude early.
- Distinguish the contribution from the nearest corporate-finance papers explicitly; "no one has tested X in this sample" is not a contribution.
- JCF uses an unstructured abstract and JEL codes; an online appendix carries robustness and secondary results.
- Exhibits report economic magnitudes (not only t-stats); the central result should be readable from one table.

## Official-submission checklist

- Search the live site for "Journal of Corporate Finance guide for authors" and follow the current Elsevier version.
- Re-check the submission fee, formatting, abstract/JEL, anonymization, and the disclosure policy (data sources, conflicts, prior circulation).
- Re-check the current data/code and online-appendix requirements and any replication expectations.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters for corporate-finance theory or practice.
- [ ] The contribution is stated as mechanism / identification / measurement, not as a significant coefficient.
- [ ] The introduction positions the paper against the most recent corporate-finance work on this question.
- [ ] Endogeneity is confronted with a credible design, not just fixed effects.
- [ ] Disclosure, data sources, and the online appendix are ready.

## Common desk-reject triggers

- A governance/financing regression with endogeneity and no credible source of variation.
- A correlation framed as causal with only fixed-effects "control" for confounders.
- Weak or undefended measurement of key governance/ownership variables.
- A paper that is really asset pricing, banking, or accounting framed as corporate finance.

## Re-routing decision

- Top-3 corporate-finance importance → `journal-of-finance`, `journal-of-financial-economics`, `review-of-financial-studies`.
- Peer elite-field venues → `review-of-finance`, `journal-of-financial-and-quantitative-analysis`.
- Bank-centric financing/intermediation → `journal-of-financial-intermediation`; broad applied, large volume → `journal-of-banking-and-finance`; practitioner-relevant → `financial-management`.
- Governance-as-accounting/disclosure → the accounting venues; economics of the firm → `journal-of-political-economy` / field econ venues.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Corporate Finance
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / mechanism clear the corporate-finance field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / disclosure / online appendix / data>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
