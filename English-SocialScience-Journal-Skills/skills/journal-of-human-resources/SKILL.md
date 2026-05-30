---
name: journal-of-human-resources
description: Use when targeting Journal of Human Resources (JHR) or deciding whether an applied-microeconomics manuscript on labor, education, health, or welfare fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Human Resources (journal-of-human-resources)

## Journal positioning

JHR is a leading field journal for applied microeconomics on human capital and well-being — labor, education, health, and welfare/poverty — with a strong taste for microdata and credible, policy-relevant identification. It rewards careful empirical work that answers a question people care about with a research design the reader can trust. The readership is applied micro and labor/education/health economists, so the paper must combine a substantive question with state-of-the-art causal inference.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the journal/University of Wisconsin Press site and the editorial submission system.

## When to trigger

- The author names JHR as the target venue, or wants a strong applied-micro home for a labor/education/health/welfare paper.
- A microdata empirical paper has credible identification but is narrower than a top-5 general-interest result.
- A policy-evaluation paper needs re-framing so the contribution reads as a credible causal estimate with mechanism and policy relevance.
- The author needs JHR's desk-reject risks and a credible applied-micro alternative list.

## Scope & topic fit

- Labor economics: employment, wages, human capital, family, immigration, discrimination.
- Education: schooling, returns, interventions, teacher/school effects, early childhood.
- Health economics and health behaviors, especially with a human-capital or well-being angle.
- Welfare, poverty, inequality, and the evaluation of social programs and transfers.

## Method & evidence bar

- Identification is central: the design (experiment, quasi-experiment, DiD, IV, RDD) must be credible and the threats pre-empted, not waved away.
- Microdata and measurement quality matter — sample, variable construction, and selection issues should be handled transparently.
- Modern estimators and correct inference are baseline: appropriate DiD methods for staggered adoption, defensible instruments, density/covariate evidence for RDD, proper clustering.
- The contribution should be a credible causal estimate plus mechanism and policy reading, not a significant coefficient alone.

## Structure & house style

- The introduction states the question, the data, the identification strategy, and the headline estimate early, and says why the answer matters for policy or human capital.
- Position against the relevant applied-micro literature; "no one has estimated X for group Y" is not a contribution without a design or conceptual advance.
- Uses an unstructured abstract and JEL codes; an online appendix carries robustness, heterogeneity, and data detail.
- Exhibits should report interpretable magnitudes and clear identification (e.g., event-study plots, balance tables), not only point estimates.

## Official-submission checklist

- Search the live site for "Journal of Human Resources submission guidelines / instructions for authors" and follow the current version.
- Re-check submission fee, formatting, abstract/JEL requirements, anonymization, and figure/table standards on the submission system.
- Re-check the current data and code availability / replication policy and any deposit requirement.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this labor/education/health/welfare result matters for policy or human capital.
- [ ] The contribution is stated as a credible causal estimate / mechanism, not as statistical significance.
- [ ] The introduction positions the paper against the current applied-micro frontier on this question.
- [ ] Identification threats are addressed by design; estimator and inference choices are state-of-the-art.
- [ ] Data, code, and robustness appendix are ready for the official policy.

## Common desk-reject triggers

- A microdata regression with selection/endogeneity and no credible identification.
- "First to study X for population Y" with no design or conceptual advance.
- Outdated methods (naive TWFE on staggered policy, weak IV, cosmetic RDD).
- Significance reported without magnitude, mechanism, or policy interpretation.

## Re-routing decision

- General-interest at the top → `american-economic-review`; broad applied micro → the AEA applied outlet or `review-of-economics-and-statistics`.
- Labor-core and field-leading → `journal-of-labor-economics`; health-core → `journal-of-health-economics`; public/welfare-policy core → `journal-of-public-economics`.
- Urban/regional labor markets → `journal-of-urban-economics`; technically heavier econometric identification → `international-economic-review` or `journal-of-applied-econometrics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Human Resources
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification clear JHR's applied-micro bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / JEL / data-code policy / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
