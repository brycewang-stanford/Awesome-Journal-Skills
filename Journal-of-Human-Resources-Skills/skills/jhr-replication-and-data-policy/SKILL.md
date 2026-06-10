---
name: jhr-replication-and-data-policy
description: Use when preparing Journal of Human Resources data and replication materials: archive plan footnote, public repository deposit, CC0 license, Data Availability Statement, read-me file, waiver requests, RCT pre-analysis-plan statements, and code package.
---

# Replication & Data Policy (jhr-replication-and-data-policy)

## When to trigger

- The paper is being prepared for JHR submission or acceptance
- You need the archive-plan footnote, Data Availability Statement, or waiver
- Data are restricted, proprietary, administrative, or RCT-based

## JHR policy core

JHR's data policy is unusually concrete: accepted papers must preserve data and
post replication materials in a well-curated public repository where possible,
with a public-domain CC0 1.0 Universal license. At submission, include an archive
plan footnote with a persistent link if available, or request a waiver at initial
submission.

## Package contents

- Data files that can legally be shared
- Code and models needed to reproduce all tables and figures
- Read-me file explaining the sequence
- Data Availability Statement on the title page
- Restricted-data access instructions or waiver justification
- For RCTs: pre-analysis plan registration and deviations

## Waiver logic

Request a waiver at initial submission when data cannot be publicly deposited.
State how other researchers can obtain the data and commit to provide reasonable
guidance.

## Restricted-data package

When the data cannot be public, still prepare:

- synthetic or public-use data that exercises every script path when possible;
- data dictionary with variable construction and source tables;
- access instructions, application links, and approval constraints;
- log showing which outputs require restricted data;
- archive-plan footnote explaining the waiver and reproducibility route.

## Deposit decisions by data source

| Data source | What can usually be deposited | Waiver posture |
|---|---|---|
| Public-use surveys (CPS, ACS, NLSY, PSID extracts) | Extraction code plus the analysis file, or code that rebuilds it from raw downloads | Rarely needed; check redistribution terms of each survey |
| State administrative records (UI wages, K-12, Medicaid) | Code, codebooks, aggregate exhibits; microdata stays with the agency | Waiver expected; document the access route precisely |
| Own RCT microdata | De-identified analysis files under CC0 where consent and IRB allow | Partial waiver for identifying fields; PAP registration stated |
| Proprietary/commercial data | Code, pseudo-data, purchase or license instructions | Waiver with a named acquisition path |
| Linked or matched files | Each source assessed separately; the crosswalk is often the binding constraint | Mixed: deposit what is public, waiver the link keys |

Repository choice and licensing details evolve — confirm against the journal's
current author guidelines before depositing.

## Worked waiver scenario: UI wage records

Illustrative case: earnings outcomes come from one state's unemployment-insurance
wage records under a data-use agreement that bars any microdata release.

1. Footnote at submission: names the agency, the agreement, and states that
   code, codebooks, and a synthetic test file will be archived under CC0.
2. The read-me lists the application steps and typical approval constraints a
   replicator faces, and which exhibits need the restricted extract.
3. Every script runs against the synthetic file end-to-end so reviewers can
   verify logic without the data.
4. The Data Availability Statement mirrors the footnote — the two must not
   drift apart between submission and acceptance.

## Read-me skeleton for the JHR archive

```text
README
  1. Data sources & access (public files included; restricted: how to apply)
  2. Software & versions (Stata/R/Python; packages pinned)
  3. Run order: 00_master -> 01_clean -> 02_analysis -> 03_exhibits
  4. Runtime & hardware notes; random seeds fixed where used
  5. Exhibit map: each table/figure -> producing script -> data requirement
  6. License: CC0 1.0 Universal (data and code deposited)
```

## Pre-acceptance dry run

- Clone the package to a clean directory and run it without manual edits.
- Confirm every main-text and appendix exhibit regenerates byte-stable or with
  documented stochastic variation.
- Check that no intermediate file under a restrictive license leaks into the
  deposit.

## Output format

```text
[Data status] public / restricted / proprietary / confidential / mixed
[Archive plan footnote] ...
[DAS] ...
[Waiver needed] yes/no + reason
[RCT PAP status] ...
[Next step] jhr-submission
```
