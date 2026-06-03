---
name: jmf-transparency-and-data-policy
description: Use when preparing the reproducibility / replication and data-sharing materials for a Journal of Marriage and Family (JMF) manuscript. JMF asks for replication-level detail and Wiley applies a data-sharing policy with a data availability statement; many family datasets are restricted-use. Covers quantitative and qualitative transparency and the restricted-data path. Prepares the package; it does not waive requirements.
---

# Transparency & Data Policy (jmf-transparency-and-data-policy)

JMF expects enough detail on design and procedures to **facilitate replication**, and Wiley applies a
**data-sharing policy** (typically including a **data availability statement**). Many family datasets
(PSID, Add Health, Fragile Families, NSFG) are **restricted-use** and cannot be redistributed — so plan
transparency around *access*, not redistribution. Verify the current JMF/Wiley wording on the policy
pages (待核实).

## When to trigger

- Building the reproducibility/replication and data-availability materials
- Writing the **data availability statement** for the manuscript
- Your data are **restricted-use** and cannot be posted
- A **replication** submission (materials expectations are central)

## What JMF / Wiley expect (verify current wording)

1. **Replication-level detail.** The Method and any supplements describe the sample derivation,
   measures, coding, and analytic approach in enough detail that a competent reader could reproduce
   the study. Brief reports are explicitly welcomed for **replications** and **important null findings**.
2. **Data availability statement.** Wiley's data-sharing policy generally calls for a statement in the
   article confirming whether data are shared and how they can be accessed (the exact JMF tier is
   待核实 — confirm on the Wiley author page).
3. **Analysis code.** Deposit code that regenerates the reported tables and figures in an approved
   repository (e.g., **OSF**, **ICPSR**, Harvard Dataverse) where data terms allow. Master script +
   README + pinned versions + seeds.
4. **Qualitative materials.** Share what the data terms and human-subjects protections allow (e.g.,
   coding schemes, excerpts, evidence tables), with access controls where needed; do not expose
   identifiable family information.

## Restricted-use family data (the common case)

- **State the restriction** and who imposes it (e.g., data-provider agreement, IRB, privacy of minors).
- Provide **README instructions on exactly how others obtain the data** (application process, provider
  contact, required agreements) so the analysis is reproducible by an authorized user.
- Where feasible, provide **synthetic or derived data** plus full code so the pipeline can be run.
- Cite the dataset and version precisely (DOI/release) so reviewers know exactly what you used.

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, sample derivation, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for imputation, bootstrap, and stochastic steps
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] **Data availability statement** drafted (shared / restricted + access path)
- [ ] Restricted data: restriction note + access instructions + synthetic data where feasible
- [ ] Preregistration / pre-analysis plan linked (anonymized) where applicable

## Anti-patterns

- Treating transparency as a post-acceptance afterthought
- A vague "data available on request" with no access path for restricted family data
- Posting identifiable information about couples, children, or families
- Code that does not actually reproduce the printed tables/figures
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Replication detail】sample/measures/coding documented? [Y/N]
【Data availability statement】shared / restricted + access path drafted? [Y/N]
【Code deposit】master script reproduces tables/figures (OSF/ICPSR/Dataverse)? [Y/N]
【Restricted data】restriction note + access instructions + synthetic data?
【Qualitative transparency】materials documented within human-subjects limits? [Y/N/NA]
【Next】jmf-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories, reproducibility tooling, and restricted-data handling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Wiley data-sharing policy and JMF replication guidance (待核实 items)
