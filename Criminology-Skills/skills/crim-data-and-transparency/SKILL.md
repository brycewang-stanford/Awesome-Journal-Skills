---
name: crim-data-and-transparency
description: Use when preparing the data, replication, and transparency materials for a Criminology (ASC / Wiley) manuscript — data-availability statements, reproducibility packages, preregistration, and handling restricted criminal-justice data under DUAs. Criminology operates under growing open-science norms (Wiley open-science badges, ICPSR/NACJD archiving). Prepares the package; it does not waive requirements.
---

# Data & Transparency (crim-data-and-transparency)

Criminology research increasingly travels with its data and code. Expert reviewers and editors expect
that your reported tables and figures could be reproduced, and Wiley supports open-science badges. Much
criminal-justice data is **restricted**, so plan provenance, access, and an exemption path early —
build the package as you go.

## When to trigger

- Building the reproducibility/replication package and the data-availability statement
- Deciding whether and how to preregister a prospective study
- Working with restricted data (juvenile records, NACJD restricted-use, agency administrative data)
- A reviewer asked how the analysis can be reproduced or the data accessed

## What to prepare (verify current Criminology wording — 待核实)

1. **Data-availability statement.** State where data and code live (e.g., **ICPSR / NACJD**, OSF, a
   Wiley/Dryad repository) or why they cannot be shared. Confirm the journal's required wording and any
   mandatory deposit on the live policy page (待核实).
2. **Reproducibility package.** Data (or synthetic/derived substitutes), a **master script** that
   regenerates every table and figure, a **README** documenting provenance and construction, **seeds**
   for stochastic steps, and **pinned** software/package versions.
3. **Preregistration (prospective work).** Lodge a pre-analysis plan (OSF Registries, AsPredicted) and
   mark **registered vs. exploratory** analyses; a preprint can go to **CrimRxiv**.
4. **Open-science badges.** Wiley offers **Open Data**, **Open Materials**, and **Preregistered** badges
   via the Center for Open Science; confirm whether *Criminology* currently issues them (待核实).

## Restricted criminal-justice data (common in criminology)

- **Explain why** the data cannot be shared (juvenile confidentiality, agency/IRB restrictions, DUAs).
- Provide **README instructions on exactly how others obtain it** — the application process, the archive
  (often **NACJD restricted-use**), enclave requirements, and contacts.
- Where feasible, **provide synthetic or de-identified derived data** so the code can be exercised.

## Build-as-you-go checklist

- [ ] Data-availability statement drafted to the journal's current requirement (待核实)
- [ ] One **master script** regenerates **every** table and figure from raw/constructed data
- [ ] **README** documents data provenance, construction, and how to reproduce each exhibit
- [ ] **Seeds** set/reported for every stochastic step (bootstrap, RI, EM-based trajectory fits)
- [ ] Software/package **versions pinned** (`renv.lock` / `requirements.txt` / recorded installs)
- [ ] Restricted data: exemption note + access path (NACJD/agency) + synthetic substitute where feasible
- [ ] Preregistration linked (anonymized) where applicable; registered vs. exploratory marked

## Anti-patterns

- Treating data/transparency as a post-acceptance afterthought
- A data-availability statement that says "available on request" with no archive or access path
- Depositing code that does not actually reproduce the printed tables/figures
- Claiming data are restricted without giving an access route or synthetic substitute
- Undocumented, un-seeded, unpinned code that "works on my machine"

## Output format

```
【Data-availability statement】drafted to current requirement (待核实)? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】exemption note + access path (NACJD/agency) + synthetic data?
【Preregistration】lodged + registered vs. exploratory marked? [Y/N/NA]
【Badges】Open Data / Materials / Preregistered targeted? [list / 待核实]
【Next】crim-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — ICPSR/NACJD archiving, preregistration, reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — open-science badges and data-policy items (待核实)
