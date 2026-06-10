---
name: en-journal-workflow
description: Use when deciding which English economics / finance / management / accounting / marketing / operations / information-systems journal skill to invoke next, comparing fit across the 100-journal English roadmap, or routing a manuscript before venue-specific re-framing.
---

# English econ / business journal workflow (en-journal-workflow)

## Purpose

This is the routing skill. It does not replace a single-journal profile; it first
classifies the manuscript by **discipline, contribution type, method shape, and
audience**, then routes into the matching per-journal skill for fit and re-framing.

## Resources to Load When Needed

- If the venue is unclear, read `../../resources/worked-examples/venue-routing.md`
  before choosing a target.
- If two sibling fields look plausible, read
  `../../resources/exemplars/selection-patterns.md`.
- Before submission-ready advice, use `../../resources/official-source-map.md`
  to open the current official author instructions for the chosen journal.

## Ask four things first

1. **Contribution type:** new identification / causal effect, new theory or model,
   new measurement or method, new fact/anomaly, or integrative review?
2. **Method shape:** reduced-form causal, structural, pure theory/proof,
   econometric method, lab/field experiment, survey/SEM, qualitative/inductive,
   optimization/analytics, or design-science?
3. **Discipline audience:** general economics, a specific econ field, finance,
   accounting, strategy/OB/management, marketing, operations, or information systems?
4. **Submission goal:** swing for a top-5 / top-3 / elite-list venue, or optimize
   topic–venue fit and review odds at a strong field journal?

## Quick routing

| Manuscript signature | Prefer skill |
|---|---|
| General-interest econ, top-5 ambition | `american-economic-review` / `quarterly-journal-of-economics` / `journal-of-political-economy` |
| Theorem / new estimator with proofs | `econometrica` / `journal-of-economic-theory` / `econometric-theory` |
| Strong applied micro, narrower than top-5 | `aej-applied-economics` / `review-of-economics-and-statistics` / `journal-of-human-resources` |
| Macro / growth / dynamics | `aej-macroeconomics` / `journal-of-monetary-economics` / `review-of-economic-dynamics` / `journal-of-economic-growth` |
| Micro theory / mechanism / games | `aej-microeconomics` / `journal-of-economic-theory` / `games-and-economic-behavior` |
| Policy-facing applied economics | `aej-economic-policy` / `journal-of-public-economics` / `economic-policy` |
| Trade / open economy / development | `journal-of-international-economics` / `journal-of-development-economics` / `world-development` |
| Econometric methods / applied econometrics | `journal-of-econometrics` / `journal-of-applied-econometrics` / `journal-of-business-and-economic-statistics` / `quantitative-economics` |
| Field econ (labor/health/urban/enviro/law) | `journal-of-labor-economics` / `journal-of-health-economics` / `journal-of-urban-economics` / `journal-of-environmental-economics-and-management` / `journal-of-law-and-economics` |
| Finance, top-3 ambition | `journal-of-finance` / `journal-of-financial-economics` / `review-of-financial-studies` |
| Finance, elite field | `review-of-finance` / `journal-of-financial-and-quantitative-analysis` / `journal-of-financial-intermediation` / `journal-of-corporate-finance` |
| Banking / markets / international finance | `journal-of-banking-and-finance` / `journal-of-financial-markets` / `journal-of-international-money-and-finance` / `journal-of-empirical-finance` |
| Management theory (no data) | `academy-of-management-review` / `academy-of-management-annals` |
| Management empirics, theory-driven | `academy-of-management-journal` / `journal-of-management-en` / `journal-of-management-studies` |
| Strategy / firm performance | `strategic-management-journal` / `organization-science` |
| Org theory / sociology of orgs / qualitative | `organization-studies` / `human-relations` / `administrative-science-quarterly` |
| HRM / international business / innovation | `human-resource-management` / `journal-of-international-business-studies` / `research-policy` |
| Entrepreneurship | `journal-of-business-venturing` / `entrepreneurship-theory-and-practice` |
| Marketing modeling vs. behavior | `marketing-science` / `journal-of-marketing-research` vs `journal-of-consumer-research` / `journal-of-consumer-psychology` |
| Marketing strategy / broad | `journal-of-marketing` / `journal-of-the-academy-of-marketing-science` |
| Accounting (archival/analytical/markets) | `the-accounting-review` / `journal-of-accounting-research` / `journal-of-accounting-and-economics` / `review-of-accounting-studies` |
| Accounting (interpretive/critical) | `accounting-organizations-and-society` / `contemporary-accounting-research` |
| OM / OR / analytics | `management-science` / `operations-research` / `manufacturing-and-service-operations-management` / `production-and-operations-management` / `journal-of-operations-management` |
| Information systems | `mis-quarterly` / `information-systems-research` / `journal-of-management-information-systems` / `journal-of-the-association-for-information-systems` / `informs-journal-on-computing` |

## Sibling-Journal Disambiguation

| Confusable targets | Decision rule |
|---|---|
| AER/QJE/JPE vs field journals | Use a top-5 only when the paper changes a broad economics conversation; strong identification alone is not enough. |
| JF/JFE/RFS vs finance field journals | Decide whether the contribution is asset pricing, corporate finance, intermediation, microstructure, or international finance before choosing prestige tier. |
| AMR vs AMJ vs ASQ | AMR is theory-only; AMJ is empirical theory-building; ASQ expects organization-theory depth and often sociological leverage. |
| JM vs JMR vs Marketing Science | JM is strategy/managerial broad contribution; JMR is empirical/methodological marketing research; Marketing Science expects modeling, optimization, or quantitative marketing depth. |
| MISQ/ISR vs CS venues | Use IS journals only when the information-systems theory or organizational technology contribution is central; route pure algorithms to CS/AI. |

## Decision rules

- Correlation without identification or mechanism: fix the contribution before
  swinging for a top-5/top-3 venue.
- "First to study X in context Y" is not a contribution at elite venues — name
  the conceptual or methodological advance, or route to a field journal.
- A new factor / anomaly without multiple-testing and out-of-sample discipline is
  not a finance top-3 paper.
- Management empirics with no theoretical contribution belong below AMJ/AMR, or
  need reframing.
- A modeling/optimization paper with no managerial-theory payoff routes to
  OM/OR/IS analytics venues, not to AMJ.
- Always enter the single-journal skill's official-submission checklist before
  submitting; never rely on a stale template.

## Output format

```text
[Top journal skill] <skill-name>
[Alt 1] <skill-name> (reason)
[Alt 2] <skill-name> (reason)
[Do not submit to] <journal> (one-line mismatch reason)
[Biggest current gap] topic / theory / identification / mechanism / formatting / official requirements
[Next step] invoke <skill-name> for single-venue fit and re-framing
```
