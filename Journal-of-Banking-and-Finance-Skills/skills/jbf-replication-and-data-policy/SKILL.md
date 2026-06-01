---
name: jbf-replication-and-data-policy
description: Use when preparing the data availability statement, code archive, Mendeley Data or repository materials, and proprietary-data documentation for a Journal of Banking & Finance manuscript under Elsevier research-data expectations.
---

# Replication & Data Policy (jbf-replication-and-data-policy)

## When to trigger

- The paper uses CRSP, Compustat, BankFocus, Dealscan, TRACE, Call Reports, hand-collected data, or simulations
- You need a data availability statement for Elsevier/JBF submission
- You want a legal and useful replication package despite proprietary data

## Policy stance

JBF follows Elsevier research-data expectations rather than a dedicated journal-run
replication archive. The exact JBF-specific mandatory wording should be checked on
the live Guide for Authors. Treat data/code sharing as expected good practice:
include a data availability statement, share what can be shared, and document what
cannot be redistributed.

## Package structure

```text
README.md
data_access/          # licensed-data instructions, not raw proprietary files
code/
  00_setup.*
  01_build_sample.*
  02_main_tables.*
  03_figures.*
  04_robustness.*
output/
  tables/
  figures/
requirements.*        # renv.lock / requirements.txt / Stata package list
```

## Data availability statements

- **Public data**: name source, URL, access date, and archive copy if permitted.
- **Proprietary data**: identify vendor, product, access terms, and exact query or
  extraction instructions; do not redistribute restricted files.
- **Hand-collected data**: share the dataset if rights allow, with coding rules.
- **No external data / simulation**: state that no external data were used and
  provide simulation code and seeds.

## Code expectations

- One master script regenerates all tables and figures.
- Random seeds and software versions are recorded.
- Output files match manuscript numbering.
- Confidential paths and author identity are removed before double-anonymized submission.

## Output format

```text
[Data status] public / proprietary / confidential / simulated / mixed
[Statement draft] ...
[Shareable files] ...
[Restricted files] ...
[Reproducibility gaps] ...
[Next step] jbf-submission
```
