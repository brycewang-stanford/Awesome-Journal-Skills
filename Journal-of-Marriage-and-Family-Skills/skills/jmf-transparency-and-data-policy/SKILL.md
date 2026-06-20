---
name: jmf-transparency-and-data-policy
description: Use when preparing the reproducibility / replication and data-sharing materials for a Journal of Marriage and Family (JMF) manuscript. JMF asks for replication-level detail and Wiley applies a data-sharing policy with a data availability statement; many family datasets are restricted-use. Covers quantitative and qualitative transparency and the restricted-data path. Prepares the package; it does not waive requirements.
---

# Transparency & Data Policy (jmf-transparency-and-data-policy)

JMF expects enough detail on design and procedures to **facilitate replication**, and Wiley applies a
**data-sharing policy** requiring a **Data Availability Statement** for research and synthesis articles. Many family datasets
(PSID, Add Health, Fragile Families, NSFG) are **restricted-use** and cannot be redistributed — so plan
transparency around *access*, not redistribution. Live-check the current JMF/Wiley wording before upload.

## When to trigger

- Building the reproducibility/replication and data-availability materials
- Writing the **data availability statement** for the manuscript
- Your data are **restricted-use** and cannot be posted
- A **replication** submission (materials expectations are central)

## What JMF / Wiley expect

1. **Replication-level detail.** The Method and any supplements describe the sample derivation,
   measures, coding, and analytic approach in enough detail that a competent reader could reproduce
   the study. Brief reports are explicitly welcomed for **replications** and **important null findings**.
2. **Data availability statement.** Wiley's data-sharing policy requires a statement in research and
   synthesis articles confirming whether data are shared and how they can be accessed; check whether
   JMF adds journal-specific wording at upload.
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

## Transparency expectations by data type at JMF

| Data type | What can be shared | Access path to document | Common trap |
|-----------|--------------------|--------------------------|-------------|
| Public-use survey (e.g., some NSFG files) | Constructed analytic code + variable derivations | Cite dataset DOI/release; link repository | Posting a redistributable file you re-shaped without the version |
| Restricted-use panel (PSID, Add Health, Fragile Families) | Code + README; not the raw data | Application/agreement steps so an authorized user reproduces | "Available on request" with no access route |
| Couple/dyadic micro-data | De-identified derived measures where terms allow | Provider contact + agreement | Re-identifiable couples or children in shared excerpts |
| Qualitative family interviews | Coding scheme, evidence tables, masked excerpts | Access controls per IRB/consent | Exposing identifying family detail |

For the flagship journal of family science, the Wiley data-sharing policy and a data availability statement
sit alongside JMF's expectation of replication-level methodological detail. Because so many family datasets
are restricted-use, transparency at JMF is engineered around *documented access*, not redistribution.

## Worked micro-example (illustrative)

A divorce-timing paper uses restricted PSID-linked data that cannot be posted. The transparency package:
(1) a data availability statement reading, in effect, "Data are from the Panel Study of Income Dynamics
(release YYYY) and are restricted-use; access requires a PSID sensitive-data agreement — see README for the
application steps"; (2) a master script that regenerates all six tables and two figures from the
constructed file, with seeds fixed for the multiple-imputation and bootstrap steps; (3) a synthetic dataset
of the same schema so a reader without the agreement can run the pipeline end-to-end and confirm it
executes; (4) precise dataset citation with release/version. The release year and agreement name here are
illustrative placeholders to confirm against the provider.

## Referee/editor-facing pitfalls and the fix

- *"How would anyone reproduce this?"* Replace "available on request" with the concrete application process,
  provider contact, and required agreements for the restricted family dataset.
- *"Code doesn't reproduce the printed tables."* Ship one master script that builds every exhibit, plus
  pinned package versions (`renv.lock`/`requirements.txt`) and recorded seeds.
- *"Qualitative materials would identify families."* Share coding schemes and masked evidence tables under
  access controls rather than raw transcripts.

## Calibration anchors (hedged where uncertain)

- That JMF expects replication-level detail and that Wiley requires a Data Availability Statement are
  stable features; live-check whether the JMF upload workflow adds journal-specific wording or
  repository expectations beyond Wiley's general policy.
- Brief reports are an established channel for replications and important null findings, which raises the
  premium on a clean reproducibility package; treat this as a venue norm to verify, not a quota.

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
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Wiley data-sharing policy and JMF replication guidance
