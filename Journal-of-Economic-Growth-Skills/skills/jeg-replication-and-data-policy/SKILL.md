---
name: jeg-replication-and-data-policy
description: Use when preparing Journal of Economic Growth (JEG) data availability statements, replication code, calibration files, digitized historical sources, GIS layers, and Springer Nature research-data documentation for empirical, quantitative, or theoretical growth and comparative-development papers.
---

# Replication & Data Policy (jeg-replication-and-data-policy)

## When to trigger

- The paper uses empirical growth data, historical data, simulations, or calibration code
- You need a Data Availability Statement for Springer Nature
- Data are public, proprietary, restricted, or author-constructed

## Policy stance

JEG follows Springer Nature research-data policy: original research articles need
a Data Availability Statement. A journal-specific mandatory data editor or code
archive was not confirmed in the source map, but reproducible materials are still
expected for credible growth work.

## Package checklist

- Data README with sources, access dates, licenses, and restrictions.
- Code pipeline that regenerates tables and figures.
- Calibration file listing parameter values and sources.
- Public repository or DOI for shareable data/code when allowed.
- Restricted-data instructions and contact/access procedure when data cannot be
  redistributed.

## Growth package layout

Use a structure that separates empirical and model artifacts:

```text
replication/
  README.md
  data_sources.md
  code/
  calibration/
  output_tables/
  output_figures/
  manuscript_map.md
```

`manuscript_map.md` should list each table/figure, the script that creates it, the input data or
calibration file, and the expected output path. For theory-only papers, include the scripts that create
numerical examples, calibration tables, or transition-path figures.

## Calibration/data audit

For each calibrated or empirical object, record:

```text
Object | Source | Transformation | Moment/target | Script | Manuscript location
```

This catches common growth-paper replication failures: undocumented historical series, country-code
harmonization drift, purchasing-power or deflator choices, calibration targets that do not match the
reported table, and transition-path scripts that cannot be rerun from a clean checkout. If data are
constructed by hand from historical sources, include the transcription notes and source images or access
instructions when permissions allow.

## Historical and geospatial documentation duties

Deep-determinants packages carry failure modes beyond a standard code archive:

- **Digitized historical sources**: archive the scan references, transcription rules, and the share of pages double-entered for error checking; record the holding archive and license for every map or census volume.
- **GIS layers**: state the projection/CRS, raster resolution, and the construction chain (e.g., least-cost-path cost-surface parameters); ship shapefiles, or exact download instructions when redistribution is barred.
- **Boundary harmonization**: include the crosswalk between historical polities and modern units with the rule applied to split or merged units — referees at this venue do re-run persistence results on alternative crosswalks.
- **Distance and terrain variables**: the build script matters more than the variable itself; one undocumented cost-surface assumption can move headline coefficients.

## Worked vignette — packaging a deep-roots paper

Illustrative inventory for a manuscript instrumenting institutions with a historical shock across 1,800 districts:

- `data_sources.md` lists 6 sources: two public cross-country series, one digitized 19th-century census (scans archived, license noted), one proprietary geocoded survey (access instructions only, no raw deposit), and two constructed GIS rasters with full build scripts.
- `manuscript_map.md` covers 9 exhibits, each tied to a script; Table 3's Conley standard errors are flagged as depending on the spatial-weights script with a fixed seed.
- The known-gap note records that the survey vendor forbids redistribution; the Data Availability Statement says so and points to the application procedure — confirm the exact statement wording against the journal's current author guidelines.

## Deposit decision rules

- Public secondary data → deposit extracts plus build code; cite the original source DOI.
- Author-digitized historical data → deposit the dataset and transcription notes; at this journal that dataset is often the paper's most durable contribution.
- Proprietary or restricted data → deposit code plus a masked or synthetic sample where the license allows, and document the access path step by step.
- Simulation/calibration-only papers → deposit the full solver and parameter files so every transition path regenerates exactly from a clean checkout.

## Output format

```text
[Data status] public / restricted / proprietary / simulated / mixed
[Statement draft] ...
[Code archive] ...
[Calibration files] ...
[Gaps before submission] ...
[Next step] jeg-submission
```
