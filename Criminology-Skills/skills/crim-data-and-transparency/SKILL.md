---
name: crim-data-and-transparency
description: Use when preparing the data, replication, and transparency materials for a Criminology (ASC / Wiley) manuscript — data-availability statements, reproducibility packages, preregistration, and handling restricted criminal-justice data under DUAs. Criminology operates under growing open-science norms (Wiley open-science badges, ICPSR/NACJD archiving). Prepares the package; it does not waive requirements.
---

# Data & Transparency (crim-data-and-transparency)

Criminology research increasingly travels with its data and code. Expert reviewers and editors expect
that your reported tables and figures could be reproduced. Wiley's general data-sharing guidance requires
a Data Availability Statement for research- and synthesis-based articles, while the current Wiley ACT row
for *Criminology* lists the journal-specific data-sharing policy field as **No Policy**. Treat that as:
prepare a credible statement and package, but do not claim a journal-specific mandatory repository deposit
unless the live portal requires it.

## When to trigger

- Building the reproducibility/replication package and the data-availability statement
- Deciding whether and how to preregister a prospective study
- Working with restricted data (juvenile records, NACJD restricted-use, agency administrative data)
- A reviewer asked how the analysis can be reproduced or the data accessed

## What to prepare

1. **Data-availability statement.** State where data and code live (e.g., **ICPSR / NACJD**, OSF, a
   Wiley/Dryad repository) or why they cannot be shared. Use Wiley DAS templates and the live portal
   wording; do not imply mandatory deposit where restricted data make that impossible.
2. **Reproducibility package.** Data (or synthetic/derived substitutes), a **master script** that
   regenerates every table and figure, a **README** documenting provenance and construction, **seeds**
   for stochastic steps, and **pinned** software/package versions.
3. **Preregistration (prospective work).** Lodge a pre-analysis plan (OSF Registries, AsPredicted) and
   mark **registered vs. exploratory** analyses. Wiley ACT currently says *Criminology* does **not**
   accept preprints, so separate preregistration from manuscript preprint posting.
4. **Open-science badges.** Wiley offers **Open Data**, **Open Materials**, and **Preregistered** badges
   via the Center for Open Science on participating journals; follow the live submission prompts.

## Restricted criminal-justice data (common in criminology)

- **Explain why** the data cannot be shared (juvenile confidentiality, agency/IRB restrictions, DUAs).
- Provide **README instructions on exactly how others obtain it** — the application process, the archive
  (often **NACJD restricted-use**), enclave requirements, and contacts.
- Where feasible, **provide synthetic or de-identified derived data** so the code can be exercised.

## Build-as-you-go checklist

- [ ] Data-availability statement drafted to Wiley/current portal wording
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

## Restricted-data transparency decision table (criminology specifics)

Criminal-justice data is often restricted — juvenile records, agency systems, NACJD restricted-use
files behind enclaves. The ASC/Wiley open-science direction still expects a *credible reproducibility
path*, so the answer is rarely "cannot share." Match your situation to a tier.

| Data situation | Acceptable transparency move | What to deposit |
|----------------|------------------------------|-----------------|
| Public file (e.g., NCVS, UCR/NIBRS extracts) | full open deposit | data + master script + README |
| NACJD restricted-use | exemption note + exact application path | code + synthetic/derived data + access steps |
| Agency / juvenile confidential records | DUA or confidentiality exemption + contact | code + simulated data matching schema |

The principle: even when raw data cannot travel, the *code* and a runnable substitute should. Confirm
the final statement wording against the journal's current submission guidelines.

## Worked vignette: a restricted-data statement (illustrative)

A study uses a state juvenile-justice extract that cannot be redistributed. The package ships a master
script regenerating all 8 exhibits; a README documenting construction and the application process
(agency contact, IRB requirement, ~12-week window, illustrative); a synthetic dataset matching the
schema so reviewers can run the script; and seeds for the EM-based trajectory fit. The statement names
the restriction, the legal basis, and the access route — not "available on request."

## Transparency-stage referee pushback (with the Criminology fix)

- *"'Available on request' is not a path."* Fix: name the archive (NACJD/ICPSR) or the agency steps and contact.
- *"Code doesn't reproduce Table 3."* Fix: one master script regenerates every exhibit; verify before deposit.
- *"Restricted data with no way in."* Fix: give the access route plus a synthetic substitute.

## Output format

```
【Data-availability statement】drafted to Wiley/current portal wording? [Y/N]
【Reproduces tables/figures?】master script verified locally? [Y/N]
【Documentation】README + provenance + seeds + pinned versions? [Y/N]
【Restricted data?】exemption note + access path (NACJD/agency) + synthetic data?
【Preregistration】lodged + registered vs. exploratory marked? [Y/N/NA]
【Badges】Open Data / Materials / Preregistered targeted if portal offers them? [list / NA]
【Next】crim-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — ICPSR/NACJD archiving, preregistration, reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Wiley DAS guidance, ACT data-policy/preprint fields, and open-badge sources
