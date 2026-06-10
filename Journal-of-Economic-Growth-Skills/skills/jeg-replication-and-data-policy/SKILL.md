---
name: jeg-replication-and-data-policy
description: Use when preparing Journal of Economic Growth data availability, code, calibration files, and Springer Nature research-data statements for empirical or theoretical growth papers.
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

## Output format

```text
[Data status] public / restricted / proprietary / simulated / mixed
[Statement draft] ...
[Code archive] ...
[Calibration files] ...
[Gaps before submission] ...
[Next step] jeg-submission
```
