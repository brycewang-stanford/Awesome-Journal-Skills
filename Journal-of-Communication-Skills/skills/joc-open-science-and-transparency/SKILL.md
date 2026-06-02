---
name: joc-open-science-and-transparency
description: Use when preparing the open-science and transparency materials for a Journal of Communication (JoC) manuscript. JoC requires a Data Availability Statement and supports Open Science Badges for open data, open materials, and preregistration. Covers quantitative, computational, and qualitative transparency and the restricted-data path. Prepares the materials; it does not waive requirements.
---

# Open Science & Transparency (joc-open-science-and-transparency)

JoC requires a **Data Availability Statement** on every article and offers **Open Science Badges** for
open data, open materials, and preregistration. Transparency is not an afterthought — build the
statement and supporting materials as you write so submission and any badge claim go smoothly.

## When to trigger

- Drafting the **Data Availability Statement** (a submission requirement)
- Deciding whether to pursue **Open Science Badges** (open data / open materials / preregistration)
- Preparing a **preregistration** for a prospective design (note it in the cover letter)
- Data cannot be fully shared (privacy, ethics, platform/legal restrictions) and you need the path forward

## What JoC expects (verify current wording on the policy page)

1. **Data Availability Statement (required).** State where the data are (repository + identifier),
   under what conditions they can be accessed, and — if they cannot be shared — **why**, with
   instructions for how others might obtain them.
2. **Open Science Badges (optional, earned).**
   - **Open Data** — data and a codebook deposited in a trusted repository with a persistent identifier.
   - **Open Materials** — stimuli, instruments, code, and protocols deposited so the study can be reproduced.
   - **Preregistration** — a time-stamped, registered design/analysis plan; note it in the cover letter.
3. **Quantitative / computational materials.** Data, code, codebook, and documentation sufficient to
   regenerate every reported result; master script + README + pinned versions + seeds; for automated
   text measures, include the human-validation materials.
4. **Qualitative materials.** Share the materials that support the claims (e.g., coding schemes,
   evidence tables, de-identified excerpts) with access controls where needed (QDR for controlled access).

## When data cannot be shared (restricted-data path)

- **Explain why** in the Data Availability Statement (ethical/privacy concerns, platform terms of
  service, or legal restrictions by the provider).
- Provide **instructions on how others can obtain the data** (access process, application, provider contact).
- Where possible, provide **synthetic or de-identified data** so the code can be run.

## Build-as-you-go checklist

- [ ] **Data Availability Statement** drafted (repository, identifier, access conditions, or exemption)
- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step; software/package **versions pinned**
- [ ] Open Science Badge materials staged (open data / open materials / preregistration) where claimed
- [ ] Content analysis: codebook + intercoder-reliability report included
- [ ] Materials **anonymized** (no author-identifying paths/links) for double-anonymous review

## Anti-patterns

- Submitting without a Data Availability Statement (it is required)
- Claiming a badge whose materials are not actually deposited or do not reproduce the results
- A personal URL instead of a trusted repository with a persistent identifier
- Claiming data are restricted without giving an access path or synthetic substitute
- De-anonymizing the manuscript via an open-materials link during review

## Output format

```
【Data Availability Statement】drafted? repository + identifier or exemption? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Badges sought】open data / open materials / preregistration (materials staged?)
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】exemption note + access path + synthetic data?
【Qualitative transparency】coding scheme / evidence documented? [Y/N/NA]
【Next】joc-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (OSF, QDR)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Data Availability Statement requirement + Open Science Badges
