---
name: est-reporting-and-reproducibility
description: Use when assembling the Supporting Information (SI), data-availability statement, and public-data/code deposit for an Environmental Science & Technology (ES&T) manuscript. ES&T expects materials, data, and protocols to be deposited in public databases and a data-availability statement, with SI submitted alongside the manuscript. It guides reporting and deposit; it does not generate the underlying data.
---

# Reporting & Reproducibility (est-reporting-and-reproducibility)

ES&T strongly encourages public data and expects authors to make **materials, data, and protocols**
available through public databases, with a **data-availability statement** and a **Supporting
Information** file submitted alongside the manuscript and reviewed with it. Build these as you go, not
the night before submission.

## When to trigger

- Assembling the **Supporting Information (SI)** PDF/files
- Writing the **data-availability statement** and choosing repositories
- Depositing data, spectra, sequences, code, and protocols
- Making sure every figure/table can be regenerated from deposited data

## What ES&T expects

1. **Supporting Information.** Submitted simultaneously as separate file(s); describe contents and
   file type in the SI paragraph (e.g., "Additional analytical methods, calibration data, and NMR
   spectra (PDF)"). Available to reviewers; free to readers on publication.
2. **Data-availability statement.** State where the data live and how to access them; cite
   **accession codes / DOIs**.
3. **Public deposition by data type** (see `resources/external_tools.md`):
   - Sequences → **GenBank / ENA / DDBJ**; omics/microarray → **GEO / ArrayExpress**;
     proteomics → **PRIDE / ProteomeXchange**; mass spectra → **MassIVE / MetaboLights / MassBank**.
   - General data/code → **Dryad, figshare, Zenodo, OSF**.
4. **Methods reproducibility.** Report instrument settings, reagents/standards, QA/QC, and analysis
   steps in enough detail to reproduce; deposit analysis code with seeds and pinned versions.
5. **Restricted data.** If data cannot be fully shared (privacy/legal), explain why and give README
   instructions on how to obtain it; provide what can be shared.

## SI assembly checklist

- [ ] Extended methods, reagents/standards, instrument parameters
- [ ] Calibration curves, QA/QC tables (blanks, recoveries, CRMs, LOD/LOQ)
- [ ] Supplementary figures/tables/spectra referenced in order (Figure S1, Table S1…)
- [ ] Data-availability statement with accession/DOI
- [ ] Code/scripts deposited; figures regenerate from deposited data
- [ ] Page/word limits and file formats per ACS SI guidance (待核实 on specifics)

## Deposition routing: data type → repository

ES&T expects deposition in the *community-standard* repository for each data type, not a generic
catch-all. Reviewers in a sub-field know the canonical home and notice when data are not there
(confirm any volatile mandate against the journal's current author guidelines — 待核实):

| Data type | Expected repository | Reviewer's note if missing |
|-----------|--------------------|-----------------------------|
| DNA/RNA sequences | GenBank / ENA / DDBJ | not independently checkable |
| Omics / microarray | GEO / ArrayExpress | non-standard, hard to reuse |
| Proteomics | PRIDE / ProteomeXchange | unverifiable identifications |
| Mass spectra / metabolomics | MassIVE / MetaboLights / MassBank | spectra not reusable |
| General data / code | Dryad, figshare, Zenodo, OSF | "available on request" red flag |

## Worked micro-example (illustrative — SI for a PFAS fate study)

For the river-PFAS study, a reviewer-ready Associated Content package (illustrative) contains:

- **SI PDF:** extended LC-MS/MS methods, transition list and collision energies, the QA/QC table
  (field blanks, 92% recovery, per-analyte LOQ), calibration curves (R² > 0.99, illustrative), and
  the ROS censoring detail — each item S-numbered and referenced in order from the main text.
- **Deposited:** raw and processed concentration tables plus the analysis code (with the random seed
  for the bootstrap CI and pinned package versions) on Zenodo with a DOI; the mass spectra on MassIVE.
- **Data-availability statement:** "Concentration data and analysis code are available at Zenodo
  (DOI: 10.xxxx/illustrative); raw mass spectra are deposited at MassIVE (accession: illustrative)."

The test that catches drift: re-run the deposited master script on a clean machine — every figure and
the 2.4 ng/L headline number must regenerate exactly. If they do not, the SI and manuscript have
diverged.

## Referee-pushback patterns and the venue-specific fix

- *"Data available on request is not sufficient."* → Deposit in the type-appropriate repository and
  cite the accession/DOI in the statement.
- *"Methods not reproducible."* → Move instrument settings, standards, and QA/QC into the SI in
  enough detail to repeat the work; deposit code with seeds and versions.
- *"SI contents not described."* → Write the SI paragraph naming each file and its type.

## Anti-patterns

- "Data available on request" with no statement, repository, or accession
- An SI that is a dumping ground with no described contents or ordering
- Spectra/sequences/omics not deposited in the expected community database
- Code that does not run, or that cannot regenerate the manuscript's exhibits
- Leaving SI + deposition to submission day, so numbers drift from the manuscript

## Output format

```
【SI contents】described + ordered (S-numbered)? [Y/N]
【Data-availability statement】present with accession/DOI? [Y/N]
【Deposition】data type → repository (GenBank/GEO/PRIDE/MassIVE/Dryad/Zenodo/OSF)
【Code】deposited, seeds + pinned versions, regenerates exhibits? [Y/N]
【Restricted data】justified + README to obtain? [N/A or Y/N]
【Next】est-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories by data type; reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — data-availability and SI policy
