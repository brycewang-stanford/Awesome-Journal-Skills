---
name: facct-artifact-evaluation
description: Use when preparing the accountability artifacts that accompany an ACM FAccT paper — datasheets for datasets, model cards, data statements, audit and impact-assessment documentation, and released code/data — since FAccT's culture centers documentation and accountability infrastructure rather than a formal ACM artifact-badging track; covers what makes each genre credible, anonymized-review versus public-release versions, and consistency with the paper's harm claims.
---

# FAccT Artifact Evaluation

Use this for the material that backs a FAccT paper's transparency and accountability claims. Note
the venue difference up front: FAccT does **not** run the SIGSOFT-style ACM Artifact Review and
Badging track that software-engineering venues use, and it does not hand out Available/Functional/
Reusable/Reproduced badges. **待核实**: confirm on the current Author Guide whether any optional
artifact/reproducibility appendix or badge scheme has been added for your cycle. What FAccT *does*
have is a strong norm of **accountability documentation** — datasheets, model cards, data
statements, audit trails, and impact assessments — plus released code and data. Treat those genres
as your artifact and make each one credible on its own.

## The FAccT documentation genres (know which your paper needs)

| Genre | What it documents | When your paper needs it |
|---|---|---|
| Datasheet for a dataset | Motivation, composition, collection, preprocessing, uses, distribution, maintenance | You release or rely on a dataset |
| Model card | Intended use, training data, evaluation **disaggregated by group**, ethical considerations, limits | You release or audit a model |
| Data statement (for language data) | Speaker/annotator demographics, curation rationale, language variety | You build or study a text/NLP corpus |
| Audit / evaluation report | Method, subgroup metrics, thresholds, what was and was not tested | Your contribution is an audit |
| Impact / risk assessment | Foreseeable harms, affected populations, mitigations, residual risk | Deployment or dual-use is plausible |

Pick the genres your claims actually require; a model audit with no model card, or a dataset paper
with no datasheet, reads as incomplete to this community.

## What a credible documentation artifact contains

```text
[Provenance]   where the data/model came from, when, under what terms and consent
[Composition]  who/what is in it, who is absent, and the resulting blind spots
[Disaggregation] evaluation broken out by protected/affected subgroup, with uncertainty
[Intended use]  what it is for — and an explicit "off-label" / do-not-use list
[Limits & harms] known failure groups and foreseeable adverse impacts, not just accuracy
[Maintenance]  who updates it, how issues are reported, how long it persists
[License]      a clear license for released code/data so others can lawfully reuse it
```

## Released code and data (the reproducibility half)

- Ship the analysis that turns data into the paper's disaggregated findings, with pinned data
  versions and seeds, so a reader can re-run the harm claim.
- Deposit released data or a public archive in a persistent location (e.g. a DOI-issuing repository)
  for the camera-ready; keep it consistent with the datasheet.
- For model-generated or scraped inputs, cache raw outputs and record model IDs, dates, and terms —
  a study that needs a live API or a since-changed website re-samples rather than reproduces.

## Anonymized review version vs. public release

- **At submission:** any documentation or code shipped for reviewers must be **anonymized** — no
  author names, institution paths, cluster URLs, or identity-revealing repositories, and the
  Positionality statement stays out entirely (it is not anonymous).
- **After acceptance:** replace anonymized placeholders with the public, licensed, persistently
  archived versions the camera-ready cites, and finalize the datasheet/model card so it matches the
  released artifact exactly.

## Consistency with the paper's harm claims

The artifact's job at FAccT is to make the paper's **accountability claims checkable**. Every
disparity, harm, or transparency benefit the paper asserts should be traceable into the
documentation or released analysis. A model card whose disaggregated numbers disagree with the
paper's table, or an impact assessment that omits the harm a reviewer can foresee, undercuts the
paper more than having no artifact at all.

## Vignette: an audit paper's artifact set

A paper auditing a commercial classifier ships: a **datasheet** for the evaluation dataset (how
assembled, subgroup composition, consent basis); a **model card**-style report for the audited
system as the authors understand it (intended use, disaggregated error, failure groups); the
**audit code** with pinned data and seeds regenerating each subgroup table; and a short **impact
assessment** naming who is harmed by both the system and by publishing the audit, with mitigations.
All anonymized for review, all public and licensed at camera-ready, all consistent with the paper's
tables.

## Calibration

- FAccT's artifact expectations are **documentation- and release-centered**, not badge-centered; do
  not import a Docker-image/badge checklist as if it were the bar.
- Whether any optional artifact appendix, reproducibility checklist, or badge exists is
  cycle-volatile — confirm on the current Author Guide (**待核实**).

## Output format

```text
[Genres needed] <datasheet / model card / data statement / audit report / impact assessment>
[Artifact role] anonymized review version / public release
[Contents] <provenance / disaggregation / intended-use / limits / license>
[Claim mapping] <paper harm claim -> where in the documentation/analysis it is checkable? yes/no>
[Consistency] <artifact numbers match the paper's tables? yes/no>
[Fixes before upload] <ordered list, kept anonymous for review>
```
