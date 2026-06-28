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

## Acceptance-stage replication gate

Do not wait until conditional acceptance to discover that the archive cannot be
built. Run this gate before initial submission and again when the paper enters
revision.

| Gate | Pass condition | Blocker to surface early |
|---|---|---|
| Exhibit inventory | Every main-text and appendix table/figure maps to one script and one input dataset | Hand-built table, untracked spreadsheet edit, or private intermediate file |
| Data rights | Each dataset is classified public, restricted, proprietary, confidential, or author-generated | No redistribution right or unclear crosswalk ownership |
| Repository plan | Public repository path, DOI plan, CC0 posture, and embargo/waiver status recorded | Deposit location or license undecided |
| Code portability | A clean clone runs from raw/public inputs or approved restricted mount points | Absolute paths, local user directories, hidden credentials |
| Reviewer audit trail | Read-me explains what a referee can reproduce now and what requires restricted access | DAS promises more than the archive can deliver |

## Waiver logic

Request a waiver at initial submission when data cannot be publicly deposited.
State how other researchers can obtain the data and commit to provide reasonable
guidance.

## Waiver evidence test

A waiver is not a reason to ship a thin package. Before asking for one, prepare
evidence that the non-public data barrier is real and that the reproducibility
route remains usable.

| Question | Strong answer | Weak answer |
|---|---|---|
| Why can the data not be posted? | Contract, statute, IRB term, license, or agency rule named in plain language | "Confidential" without a source |
| How can another researcher apply? | Agency/vendor/contact path, application steps, and expected constraints | "Contact the authors" only |
| What can still be checked? | Code, dictionary, synthetic data, logs, exhibit map, and public-source rebuild scripts | PDF tables only |
| What does the DAS say? | Same access route and limits as the footnote and read-me | DAS, footnote, and read-me disagree |

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

## Exhibit-to-script map

The read-me should include a compact manifest. This is the fastest way to catch
irreproducible tables before upload.

| Exhibit | Output file | Producing script | Data requirement | Notes |
|---|---|---|---|---|
| Table 1 | `tables/table1_balance.tex` | `03_tables/table1_balance.do` | public-use extract | Rebuilds from raw survey download |
| Figure 2 | `figures/event_study.pdf` | `04_figures/event_study.R` | restricted admin file | Runs only on approved secure machine |
| Appendix Table A4 | `tables/a4_placebo.tex` | `05_appendix/placebo.py` | synthetic test + restricted file | Synthetic version verifies code path |

Use the actual filenames from the project. If an exhibit has no producing
script, treat that as a package defect, not a documentation detail.

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
- Compare the archive footnote, Data Availability Statement, waiver request,
  read-me, and repository landing page for identical access claims.
- Save the run log and unresolved exceptions in the project archive before
  acceptance, so the team can fix blockers before production deadlines.

## Output format

```text
[Data status] public / restricted / proprietary / confidential / mixed
[Archive plan footnote] ...
[DAS] ...
[Waiver needed] yes/no + reason
[Replication gate] exhibit map / data rights / repository plan / code portability / audit trail
[Restricted-data route] public deposit / partial waiver / full waiver + access path
[Dry-run result] clean / stochastic differences documented / blocked
[RCT PAP status] ...
[Next step] jhr-submission
```
