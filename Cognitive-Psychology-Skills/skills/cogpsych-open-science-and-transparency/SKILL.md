---
name: cogpsych-open-science-and-transparency
description: Use when meeting Cognitive Psychology (Elsevier) open-science expectations — sharing data, model code, analysis scripts, and materials so the modeling is reproducible, depositing in repositories with persistent identifiers, completing the Elsevier research-data and competing-interest declarations, and preregistering where applicable. Prepares compliance; it does not waive requirements. Verify current wording on the official guide for authors.
---

# Open Science & Transparency (cogpsych-open-science-and-transparency)

Because the contribution is a **model fit to data**, reproducibility here means more than open data: it
means the **model code and analysis scripts regenerate every reported fit**. Authors are strongly
encouraged to share data, model code, and materials. This skill prepares the deposits and the Elsevier
declarations early, so the modeling is reproducible at submission rather than promised at acceptance.
Confirm the current policy wording on the journal's guide for authors (检索于 2026-06；以官网为准).

## When to trigger

- Building the data, model-code, and materials deposits
- Completing Elsevier's research-data statement and competing-interest declaration
- Deciding whether (and how) to claim a restriction on sharing sensitive/third-party data
- Linking a preregistration and reporting its status
- A reviewer or editor flagged transparency or reproducibility

## What to prepare (verify current wording on the official page)

1. **Open data.** Deposit trial-level data with a **codebook/data dictionary** in a repository that
   mints a **persistent identifier (DOI)** (OSF, Mendeley Data, Dataverse, Zenodo). State availability
   in the Elsevier research-data statement.
2. **Model and analysis code (the venue-specific must).** Deposit the **model-fitting code** and
   analysis scripts with seeds and pinned versions; the reported fits, figures, and tables must
   **regenerate in a fresh session**. This is what makes a model-driven paper reproducible.
3. **Materials.** Deposit stimuli, item pools, counterbalancing schemes, and task code with a DOI.
4. **Preregistration (where applicable).** For confirmatory tests and pre-committed model comparisons,
   link a preregistration; keep confirmatory vs. exploratory consistent with it.
5. **Elsevier declarations.** Complete the **declaration of competing interest**, funding/role
   statement, author contributions, and any required ethics/consent statements per Elsevier policy.

## Build-it-right checklist

- [ ] **Data** deposited with a **DOI** + a codebook/data dictionary
- [ ] **Model-fitting code** deposited; all fits regenerate in a fresh session (run log included)
- [ ] **Analysis scripts** deposited; seeds set, package versions pinned
- [ ] **Materials** (stimuli, item pools, task/counterbalancing) deposited with a DOI
- [ ] **Preregistration** linked (where applicable); confirmatory vs. exploratory consistent
- [ ] **Research-data statement** + **competing-interest declaration** + funding/contributions completed
- [ ] Any **restriction** on sharing clearly justified (what is withheld, why, and the access path)

## Restrictions (handle honestly)

- If data/materials cannot be fully shared (sensitive populations, licensed/proprietary stimuli, IRB
  limits), state exactly **what** is withheld, **why**, and **how** others can access or approximate it
  (application path, synthetic data, code release). Code transparency is usually still expected even when
  data are restricted.

## Reproducibility statement — worked draft (illustrative)

A model statement for the recognition-memory program; confirm required headings on the official page.

```
Open Practices
Data:        Trial-level confidence-ROC data for Experiments 1-3 are at OSF
             (DOI 10.XXXX/osf.io/abcde), with a codebook.
Model code:  The UVSD/DPSD fitting code (R/Stan) reproduces all reported fits,
             model-comparison values, and figures in a fresh session; a seeded
             run log and pinned environment are included (DOI 10.XXXX/.../fghij).
Materials:   Stimulus pools, list construction, and task code are deposited
             (DOI 10.XXXX/osf.io/klmno).
Preregistration: The model space and comparison criteria were preregistered
             before data collection (osf.io/pqrst); one post hoc bias analysis
             is reported as exploratory.
Declarations: Competing interests: none. Funding and author contributions as
             stated. (If applicable: data-sharing restriction + access path.)
```

## Transparency-readiness decision table

| Situation | What to deposit / state |
|-----------|-------------------------|
| Fully shareable data + model code + materials | DOIs for each + a fresh-session run log |
| Sensitive human data | synthetic/aggregated data + IRB-gated access path; still share model code |
| Licensed/proprietary stimuli | share what the license allows; cite source; share task/model code |
| Secondary/third-party dataset | link source, share derivation + fitting scripts, document version |
| "Available on request" | replace with a persistent DOI before submission |

## Reviewer / editor pushback and the venue fix

- "I can't reproduce your model fits" → ship seeded model code + a pinned environment + a fresh-session
  run log; the fits must regenerate, not just the data exist.
- "No DOI, just a personal link" → swap transient links for persistent identifiers (OSF, Mendeley Data,
  Zenodo).
- "Statement says open but the repo is empty" → deposit first, write the statement from live DOIs.
- "Competing-interest/data statement missing" → complete the Elsevier declarations before upload.

## Anti-patterns

- Sharing data but not the **model-fitting code** (the fits cannot be reproduced)
- "Available on request" instead of a persistent identifier
- Code that does not regenerate the reported fits in a fresh session
- Claiming a sharing restriction without a justification or an access path
- Omitting the Elsevier competing-interest / research-data declarations

## Output format

```
【Open data】deposited + DOI + data dictionary? [Y/N]
【Model code】deposited + fits regenerate in a fresh session? [Y/N]
【Analysis scripts】seeded + versions pinned? [Y/N]
【Materials】deposited + DOI? [Y/N]
【Preregistration】linked + consistent (where applicable)? [Y/N/NA]
【Elsevier declarations】competing interest + research-data + funding? [Y/N]
【Next】cogpsych-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — OSF, Mendeley Data, Zenodo, Stan/JAGS, `renv`, preregistration templates
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Elsevier research-data and code-sharing policy
