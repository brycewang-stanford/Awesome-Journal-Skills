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

## Minimum agronomic metadata table (what an FCR methods reviewer audits)

A methods reviewer for a field-crop journal reads for reproducibility line by line. The gaps that draw
"cannot evaluate" comments are predictable; carry this table so each item is on the page, not in a lab
notebook.

| Block | Must report | Why FCR cares |
|-------|-------------|---------------|
| Genotype | cultivar name, maturity group, seed source/year | G×E claims need genotype identity |
| Environment | site coordinates, elevation, seasons, what each environment represents | defines the target population of environments |
| Soil | classification, texture, depth, pH, organic C, available N/P/K | yield response is soil-conditional |
| Weather | radiation, max/min temperature, rainfall, **aligned to phenology** | lets readers interpret G×E |
| Management | sowing date/density, N/P/K rate and timing, irrigation, crop protection, tillage | the "M" in G×E×M |
| Design | layout, randomization, replication, plot size, guard rows | error structure depends on it |

## Worked data-availability vignette (illustrative)

*Illustrative; figures are for demonstration only.* A multi-environment trial of two wheat cultivars
across **3 seasons × 5 sites (15 site-years)** reports grain yields of 4.2–7.8 t ha⁻¹ and a per-plot
dataset of N rate, anthesis date, and yield. Drafting the statement: the plot-level table (15
site-years × 4 N rates × 3 reps ≈ 180 rows) is non-sensitive, so deposit it in **Mendeley Data** under
Creative Commons, cite it with the DOI, and state "data are openly available at [DOI]." One site's
soil-survey layer is licensed from a provider that forbids redistribution — for that layer only, state
the **restriction and its reason** rather than leaving a blanket "available on request." The published
statement must let a reader regenerate every yield mean and SED in the results. Check the repository
and statement wording against the journal's author guidelines during the final upload-week pass.

## Anti-patterns

- A methods section missing soil, weather-vs-phenology, or management detail (not reproducible)
- Leaving the data-availability statement blank or to the last minute
- "Data available on request" with no reason and no repository where sharing was feasible
- Forgetting the generative-AI declaration
- Reported yields that the deposited data or analysis cannot regenerate
- Depositing summary means only, so the plot-level structure (blocks, sub-plots) cannot be reconstructed

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
