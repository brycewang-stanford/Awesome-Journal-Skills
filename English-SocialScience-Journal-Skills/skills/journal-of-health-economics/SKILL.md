---
name: journal-of-health-economics
description: Use when targeting Journal of Health Economics (JHE) or deciding whether a health-economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Health Economics (journal-of-health-economics)

## Journal positioning

JHE is the field flagship for health economics, publishing the most consequential work on healthcare markets, insurance, provider behavior, health behaviors, and health policy. It rewards papers that answer a substantive health-economics question with credible identification and an economic mechanism, not just a health-services correlation. The readership is health economists and applied microeconomists, so the paper must combine policy relevance with state-of-the-art causal inference or structural modeling.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Elsevier site and the editorial submission system.

## When to trigger

- The author names JHE as the target venue, or wants the health-economics field flagship.
- A health-economics paper has credible identification but is narrower than a top-5 general-interest result.
- A health-services or health-policy paper needs re-framing so the contribution reads as economics — markets, incentives, behavior — rather than description.
- The author needs JHE's desk-reject risks and a credible health/applied-micro alternative list.

## Scope & topic fit

- Healthcare markets, provider and hospital behavior, competition, and pricing.
- Health insurance: design, selection, moral hazard, and reform evaluation.
- Health behaviors and the production of health (risky behaviors, prevention, addiction).
- Health policy and program evaluation, mortality/morbidity outcomes, and the economics of long-term care and aging.

## Method & evidence bar

- Identification is the filter: experiments, quasi-experiments, DiD, IV, and RDD must be credible with threats pre-empted; structural models must identify parameters transparently.
- Health data quality and measurement matter — claims, administrative, and survey data have known pitfalls that must be handled.
- Modern estimators and correct inference are baseline (appropriate DiD for staggered policy, defensible instruments, density/covariate evidence for RDD, proper clustering).
- The contribution is a credible causal/structural answer plus mechanism and policy reading, not a significant coefficient on a health outcome.

## Structure & house style

- The introduction states the health-economics question, the data, the identification/structure, and the headline result early, and says why it matters for health markets or policy.
- Position against the relevant health-economics literature; "first to study X in healthcare setting Y" is not a contribution without an advance.
- Uses an unstructured abstract and JEL codes; an online appendix carries robustness, heterogeneity, and data detail.
- Exhibits report interpretable magnitudes and transparent identification (event studies, balance, first stages), not only point estimates.

## Official-submission checklist

- Search the live site for "Journal of Health Economics guide for authors / submission guidelines" and follow the current Elsevier version.
- Re-check formatting, abstract/JEL requirements, anonymization, and figure/table standards on the submission system.
- Re-check the current data and code availability / replication policy and any ethics/IRB and data-use disclosures for health data.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this result matters for healthcare markets, insurance, or health policy.
- [ ] The contribution is stated as a credible causal/structural answer + mechanism, not as statistical significance.
- [ ] The introduction positions the paper against the current health-economics frontier on this question.
- [ ] Identification threats are addressed by design; estimator and inference choices are state-of-the-art.
- [ ] Data, code, and any health-data disclosures are ready for the official policy.

## Common desk-reject triggers

- A health-services correlation with endogeneity and no credible identification.
- "First to study X in healthcare context Y" with no economic mechanism or methodological advance.
- Outdated methods (naive TWFE on staggered policy, weak IV, cosmetic RDD).
- A paper that is really clinical/epidemiological with no economics contribution.

## Re-routing decision

- General-interest at the top → `american-economic-review`; broad applied micro → the AEA applied outlet or `review-of-economics-and-statistics`.
- Labor/education/welfare-adjacent health → `journal-of-human-resources`; public-finance/insurance-policy core → `journal-of-public-economics`.
- Urban/regional health access → `journal-of-urban-economics`; technically heavy identification/structure → `international-economic-review` or `journal-of-applied-econometrics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Health Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / structure clear JHE's field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / data-code policy / health-data ethics / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
