---
name: epsl-reporting-and-reproducibility
description: Use when assembling the supplementary material, data-availability statement, and FAIR data deposit for an Earth and Planetary Science Letters (EPSL) manuscript. EPSL follows Elsevier's research-data policies and the community expects deposition in discipline repositories — EarthChem, PANGAEA, IRIS/EarthScope, MagIC, NASA PDS, Zenodo. It guides reporting and deposit; it does not generate the data.
---

# Reporting & Reproducibility (epsl-reporting-and-reproducibility)

The letters format pushes almost everything load-bearing but non-narrative — full analytical tables,
method details, standards data, model configurations — into the supplement and the repositories.
That makes the supplement and deposit *part of the reviewed science*, not an afterthought. EPSL sits
inside Elsevier's research-data framework (data statements, repository linking), and its communities
run mature FAIR infrastructure; reviewers know the canonical archive for each data type and notice
absences. Re-check the current mandate wording on the official Guide for Authors.

## When to trigger

- Assembling supplementary text, tables, and figures
- Writing the data-availability statement and choosing repositories
- Depositing geochemical tables, waveforms, paleomagnetic data, model code, or mission-derived products
- Making sure a reader could re-derive every figure and headline number

## What to build

1. **A methods supplement that stands alone.** Instrumentation, chemistry/procedures, standards with
   measured-vs-accepted values, blank records, correction sequence, and reduction software with
   versions — enough that a peer lab could replicate the campaign.
2. **Complete data tables.** Every analysis (not just plotted ones), every correction applied, with
   units, σ-levels, and metadata columns (coordinates, sample IDs, stratigraphic height); machine-
   readable formats, not PDF-only.
3. **A data-availability statement with resolvable identifiers.** DOIs/accessions, not "available on
   request" — Elsevier's data policy and the community both treat that phrase as a red flag.
4. **Code and models.** Reduction scripts, inversion configurations, and model input decks deposited
   (Zenodo or equivalent) with versions pinned; state the random seed for stochastic steps.
5. **Restricted material handled explicitly.** Mission data under embargo or proprietary industry data:
   say what is withheld, why, and the release path.

## Deposition routing: data type → community repository

| Data type | Expected archive | Note |
|-----------|------------------|------|
| Geochemistry / isotope tables | **EarthChem Library** (DOI per dataset) | the NSF-backed geochemistry standard |
| Marine, paleoclimate, observational Earth data | **PANGAEA** | editor-curated, DOI-issuing, FAIR-aligned |
| Seismic waveforms / station products | **IRIS / EarthScope** services | cite network DOIs |
| Paleomagnetic / rock-magnetic data | **MagIC** | the community's designated archive |
| Planetary mission data / derived products | **NASA PDS** (or ESA PSA) | cite the archive bundle, instrument, version |
| Geochronology reduction files | EarthChem / Zenodo | include tracer + constants metadata |
| Code, model configs, notebooks | **Zenodo / GitHub+Zenodo DOI** | pin versions; archive the release, not the repo URL |

## Worked micro-example (illustrative — the deposit for the ash-bed geochronology Letter)

A reviewer-ready package for the extinction-tempo study (illustrative):

- **Supplement:** full CA-ID-TIMS procedure, tracer and decay constants with citations, standards
  table (measured vs accepted, per session), blank records, and the age-model priors.
- **EarthChem:** the complete grain-by-grain U-Pb table — including the two excluded inherited grains
  — with coordinates and bed heights, under its own DOI.
- **Zenodo:** the Bayesian eruption-tempo model config and scripts, seeded, versions pinned; rerunning
  it regenerates Figure 3 and the headline 66.021 Ma age exactly.
- **Statement:** "All isotopic data are available at EarthChem (DOI: illustrative); model code at
  Zenodo (DOI: illustrative)." One sentence, two resolvable identifiers.

The self-test before submission: hand the supplement + deposits to a colleague and ask them to
re-derive the abstract's numbers. Anything they cannot re-derive is under-reported.

## Referee-pushback patterns and the venue-specific fix

- *"Data availability inadequate."* → Replace "on request" with the discipline archive + DOI; EPSL's
  communities have a canonical home for nearly every data type.
- *"Methods insufficient to assess the ages."* → Move the full traceability chain (standards, blanks,
  constants, software versions) into the supplement.
- *"Figures cannot be reproduced from the tables."* → Deposit the reduction scripts and confirm the
  pipeline regenerates every exhibit.

## Anti-patterns

- "Data available from the corresponding author upon reasonable request"
- Plotted analyses only, with rejected/excluded data invisible everywhere
- PDF-only data tables that cannot be re-used
- Waveforms, paleomag, or mission products parked in a generic repository when a designated community archive exists
- A supplement assembled the night before submission, drifting from the manuscript's numbers

## Output format

```
【Supplement】methods + standards + blanks + full tables? [Y/N]
【Deposit】data type → repository + DOI/accession (list)
【Statement】written with resolvable identifiers? [Y/N]
【Code/models】archived, versioned, seeded? [Y/N or N/A]
【Re-derivable】abstract numbers regenerate from deposit? [Y/N]
【Next】epsl-writing-style
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — repositories and reproducibility tooling by data type
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Elsevier research-data policy links for EPSL
