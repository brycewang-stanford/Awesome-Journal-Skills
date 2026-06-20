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

## When data cannot be shared (restricted-data path)

- **Explain why** the data are restricted (privacy, IRB, agency/legal restrictions, FOIA limits).
- Provide **instructions on how others can obtain the data** (access process, agency contact, DUA).
- Where feasible, **provide synthetic data** or de-identified extracts so the code can be run.
- For qualitative data, **QDR** supports controlled-access sharing with appropriate protections.

## Anti-patterns

- Treating transparency as a post-acceptance afterthought
- Depositing code that does not actually reproduce the printed tables/figures
- A personal URL or dead link instead of a persistent repository (Dataverse/QDR)
- Claiming data are restricted with no access path or synthetic substitute
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Repository】Dataverse (quant) / QDR (qual) — materials staged? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions + reporting standard? [Y/N]
【Data-availability statement】drafted? [Y/N]
【Restricted data?】reason + access path + synthetic data?
【Pre-registration】badge pursued? [Y/N/NA]
【Next】pubar-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and qualitative-transparency options (QDR)
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — PAR TOP guidelines + Dataverse/QDR
