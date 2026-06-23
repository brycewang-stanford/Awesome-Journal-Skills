---
name: pubar-transparency-and-data
description: Use when preparing the transparency / reproducibility materials for a Public Administration Review (PAR) manuscript. PAR is a signatory of the Center for Open Science TOP Guidelines and has adopted transparency standards (data citation, data sharing via Dataverse/QDR, reporting documentation, pre-registration). Covers quantitative and qualitative transparency and the restricted-data path. Prepares the package; it does not waive requirements.
---

# Transparency & Data Policy (pubar-transparency-and-data)

PAR **endorses the Center for Open Science's Transparency and Openness Promotion (TOP) Guidelines** and
has adopted transparency standards for authors (检索于 2026-06；以官网为准). Build the materials as you
go so a transparency request at review or acceptance does not stall the paper.

## When to trigger

- Building the reproducibility / transparency materials and the data-availability statement
- A reviewer or editor requested data, code, or documentation
- Data cannot be fully shared (privacy, FOIA limits, agency restrictions, IRB) and you need the path
- Deciding whether to pursue **pre-registration** badges

## What PAR's TOP standards cover (verify current wording)

1. **Data & materials citation.** Cite all research materials and data sources used, with persistent
   identifiers where available — treat data as a citable research output.
2. **Data sharing.** PAR encourages depositing data in an appropriate repository — **Dataverse** for
   quantitative data, the **Qualitative Data Repository (QDR)** for qualitative data — with a
   data-availability statement in the manuscript.
3. **Reporting documentation.** PAR recommends documenting research design, data preparation, and
   analysis decisions in a **supplementary document**, following the relevant reporting standard where
   applicable (e.g., CONSORT for experiments, STROBE for observational, PRISMA for reviews, COREQ for
   qualitative).
4. **Pre-registration.** Pre-registration of studies and/or analysis plans is supported, and
   **badges** may be available — register *before* data collection/analysis (see `pubar-research-design`).

## Build-as-you-go checklist

- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction steps, and how to reproduce each exhibit
- [ ] **Seeds** set and reported for every stochastic step
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Exhibit numbers in the manuscript **match** the deposited output exactly
- [ ] **Data-availability statement** drafted (where data live, or why they cannot be shared)
- [ ] Reporting-standard supplement (CONSORT/STROBE/PRISMA/COREQ) where applicable
- [ ] Pre-registration / pre-analysis plan linked (anonymized) where applicable

## Transparency package by evidence type

Build the package around the evidence product, not around a generic folder dump.

| Evidence type | Minimum package | PAR-specific risk |
|---|---|---|
| Administrative microdata | Data dictionary, construction log, access conditions, replication code, and an approved restricted-data statement if raw data cannot ship | A practitioner-facing claim with no auditable data provenance |
| Survey / experiment | Instrument, sampling frame, recruitment/consent language, randomization code, preregistration or exploratory label, and cleaning scripts | Treatments or outcomes cannot be interpreted by public managers |
| Qualitative interviews / fieldwork | Interview protocol, coding scheme, memo trail, anonymized excerpts or controlled-access deposit, and IRB/consent constraints | Over-disclosure that harms participants, or under-documentation that blocks audit |
| Case comparison / process tracing | Case-selection memo, source inventory, evidence tests, chronology, and rival-explanation log | "Illustrative" cases presented as field-wide lessons |
| Public datasets / dashboards | Persistent links, download dates, version snapshots, transformation scripts, and archived outputs | Live web data change after review and no longer reproduce the exhibits |

## Restricted-data decision tree

1. **Can raw data be public?** Deposit the exact analysis data plus code in Dataverse or another
   persistent repository and cite it in the Data Availability Statement.
2. **Can de-identified analysis data be public?** Deposit the de-identified data and document what
   was removed, masked, top-coded, aggregated, or perturbed.
3. **Can synthetic or toy data run the code?** Provide synthetic data plus a validation note that the
   code path reproduces the tables/figures but not the confidential estimates.
4. **Can only metadata be shared?** Provide a data-access route, DUA/IRB constraints, variable list,
   and a read-only replication log that maps each exhibit to the restricted source.
5. **Is nothing shareable?** Treat this as an editor-facing exception request; explain why the claim is
   still auditable and which independent checks remain possible.

For every restricted path, separate **legal/ethical inability** from **convenience**. Convenience is
not a transparency rationale.

## When data cannot be shared (restricted-data path)

- **Explain why** the data are restricted (privacy, IRB, agency/legal restrictions, FOIA limits).
- Provide **instructions on how others can obtain the data** (access process, agency contact, DUA).
- Where feasible, **provide synthetic data** or de-identified extracts so the code can be run.
- For qualitative data, **QDR** supports controlled-access sharing with appropriate protections.

## Reproducibility smoke test

Before submission, run a clean-room check:

- start from a fresh directory or container with only the repository/deposit files;
- install from the recorded environment file;
- run the master script end to end;
- compare every printed table/figure number against the manuscript;
- record any manual step, proprietary software dependency, or restricted-data substitution.

If the smoke test fails, do not call the package "reproducible"; report the remaining limitation
honestly in the Data Availability Statement.

## Anti-patterns

- Treating transparency as a post-acceptance afterthought
- Depositing code that does not actually reproduce the printed tables/figures
- A personal URL or dead link instead of a persistent repository (Dataverse/QDR)
- Claiming data are restricted with no access path or synthetic substitute
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Repository】Dataverse (quant) / QDR (qual) — materials staged? [Y/N]
【Evidence type】admin / survey-experiment / qualitative / case-process / public-dataset
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions + reporting standard? [Y/N]
【Data-availability statement】drafted? [Y/N]
【Restricted data?】public / de-identified / synthetic / metadata-only / exception request
【Smoke test】fresh-run status + remaining manual step
【Pre-registration】badge pursued? [Y/N/NA]
【Next】pubar-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (QDR)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — PAR TOP guidelines + Dataverse/QDR
