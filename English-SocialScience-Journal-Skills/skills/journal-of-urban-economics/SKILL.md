---
name: journal-of-urban-economics
description: Use when targeting Journal of Urban Economics (JUE) or deciding whether an urban-, regional-, or spatial-economics manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of Urban Economics (journal-of-urban-economics)

## Journal positioning

JUE is the field flagship for urban, regional, and spatial economics, publishing the most consequential work on agglomeration, housing, local labor markets, transportation, and place-based policy. It rewards papers that answer a substantive spatial-economics question with credible identification or a serious spatial-equilibrium model. The readership is urban and regional economists, so a paper must combine a spatial mechanism with state-of-the-art empirical or structural execution.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Elsevier site and the editorial submission system.

## When to trigger

- The author names JUE as the target venue, or wants the urban/regional-economics field flagship.
- An urban or spatial paper has credible identification or a spatial-equilibrium model but is narrower than a top-5 result.
- A regional or local-policy paper needs re-framing so the contribution reads as spatial economics — agglomeration, sorting, spatial equilibrium — rather than local description.
- The author needs JUE's desk-reject risks and a credible urban/regional alternative list.

## Scope & topic fit

- Agglomeration economies, firm and worker location, and the spatial organization of economic activity.
- Housing markets, prices, supply, land use, gentrification, and residential sorting.
- Local labor markets, migration, commuting, and regional adjustment.
- Transportation, infrastructure, and place-based and local public policy.

## Method & evidence bar

- Identification is the filter: experiments, quasi-experiments, DiD, IV, and RDD must be credible, with spatial confounders (sorting, selection, spatial correlation) pre-empted.
- Spatial-equilibrium and quantitative spatial models must identify parameters transparently and justify counterfactuals.
- Inference must handle spatial dependence and clustering appropriately; measurement of geography, prices, and amenities should be defensible.
- The contribution is a credible spatial mechanism or effect with interpretation, not a significant coefficient on a geographic variable.

## Structure & house style

- The introduction states the spatial question, the data or model, the identification/structure, and the headline result early, and says why the spatial dimension is essential.
- Position against the relevant urban/regional literature; "first to study X in city/region Y" is not a contribution without an advance.
- Uses an unstructured abstract and JEL codes; an online appendix carries robustness, spatial-inference detail, and modeling.
- Exhibits report interpretable magnitudes and transparent identification (event studies, maps, first stages) and address spatial correlation.

## Official-submission checklist

- Search the live site for "Journal of Urban Economics guide for authors / submission guidelines" and follow the current Elsevier version.
- Re-check formatting, abstract/JEL requirements, anonymization, and figure/table standards on the submission system.
- Re-check the current data and code availability / replication policy and any geographic-data disclosure requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why the spatial dimension is essential to this result.
- [ ] The contribution is stated as a spatial mechanism / credible effect, not as statistical significance.
- [ ] The introduction positions the paper against the current urban/regional frontier on this question.
- [ ] Identification handles spatial sorting/selection; inference handles spatial dependence.
- [ ] Data, code, and robustness appendix are ready for the official policy.

## Common desk-reject triggers

- A spatial correlation with sorting/selection and no credible identification.
- Inference that ignores spatial dependence and clustering.
- "First to study X in location Y" with no spatial mechanism or methodological advance.
- A paper that is really general labor/public economics with no genuine spatial contribution.

## Re-routing decision

- General-interest at the top → `american-economic-review`; broad applied micro → the AEA applied outlet or `review-of-economics-and-statistics`.
- Local labor/migration with a labor-core framing → `journal-of-labor-economics` or `journal-of-human-resources`; place-based public policy → `journal-of-public-economics`.
- Environmental/spatial questions → `journal-of-environmental-economics-and-management`; technically heavy spatial structure/econometrics → `international-economic-review` or `journal-of-applied-econometrics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of Urban Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the identification / spatial model clear JUE's field bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / JEL / data-code policy / geographic data / exhibits>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
