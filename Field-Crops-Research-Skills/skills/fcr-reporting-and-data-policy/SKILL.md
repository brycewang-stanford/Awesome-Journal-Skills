---
name: fcr-reporting-and-data-policy
description: Use when preparing the reporting completeness and research-data materials for a Field Crops Research (FCR) manuscript. FCR requires a data-availability statement at submission, full agronomic reporting (cultivar, soil, weather vs. phenology, management, design), declaration of any generative-AI use, and supports data/methods co-submission to Data in Brief / MethodsX. Prepares the materials; it does not waive requirements.
---

# Reporting & Data Policy (fcr-reporting-and-data-policy)

FCR does not just want results — it wants the **agronomic context** that makes them interpretable and
reproducible, plus a **statement of data availability at submission**. Build these as you go so they
do not stall the submission.

## When to trigger

- Assembling the methods section for completeness before submission
- Writing the **data-availability statement** required at submission
- Deciding whether to co-submit a dataset/method to **Data in Brief** / **MethodsX**
- Disclosing any **use of generative AI** in preparing the manuscript

## Reporting completeness (FCR-specific)

A field-crop paper is reproducible only if the methods report all of:

- [ ] **Crop & cultivar(s)** and, where relevant, maturity group / genotype identity
- [ ] **Site(s) & seasons** with coordinates; the environments and what they represent
- [ ] **Soil** properties (type, texture, relevant chemistry) for each site
- [ ] **Weather** (radiation, temperature, rainfall) shown **in relation to crop phenology**
- [ ] **Management**: sowing date/density, fertilisation, irrigation, crop protection, tillage
- [ ] **Experimental design**: layout, randomization, replication, plot size, guard rows
- [ ] **Statistics**: model, error structure, software/version (see `fcr-data-analysis`)
- [ ] **Yield data** (encouraged) and the biophysical processes linked to it

## Data availability (state it at submission)

1. **Declare availability.** FCR/Elsevier requires authors to **state the availability of any data at
   submission**; the statement is published with the article on ScienceDirect.
2. **Share where possible.** Deposit data in a recognised repository (e.g., **Mendeley Data**, or a
   domain repository) and cite it with a persistent identifier; FCR datasets are hosted openly under
   Creative Commons terms on Mendeley Data.
3. **If data cannot be shared.** State the **reason** (e.g., sensitive, confidential, or
   provider-restricted) in the data-availability statement during submission.
4. **Co-submission.** Standalone datasets or methods can be forwarded to **Data in Brief** /
   **MethodsX** alongside the article.

## Other declarations

- **Generative AI.** Declare any use of generative-AI tools in the manuscript-preparation process at
  submission, per Elsevier policy.
- **Ethics / authorship / conflicts.** Standard Elsevier declarations (CRediT roles, competing
  interests, funding) where applicable.

## Anti-patterns

- A methods section missing soil, weather-vs-phenology, or management detail (not reproducible)
- Leaving the data-availability statement blank or to the last minute
- "Data available on request" with no reason and no repository where sharing was feasible
- Forgetting the generative-AI declaration
- Reported yields that the deposited data or analysis cannot regenerate

## Output format

```
【Reporting complete?】cultivar + site/season + soil + weather-vs-phenology + management + design + stats? [Y/N]
【Yield data linked to process?】[Y/N]
【Data-availability statement】shared (repo + ID) / restricted (reason) — drafted? [Y/N]
【Co-submission】Data in Brief / MethodsX relevant? [Y/N/NA]
【Generative-AI declaration】[Y/N/NA]
【Next】fcr-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — data repositories and reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-availability, AI-disclosure, and reporting policy
