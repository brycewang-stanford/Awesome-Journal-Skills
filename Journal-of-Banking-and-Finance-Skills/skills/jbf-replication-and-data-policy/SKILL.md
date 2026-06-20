---
name: jbf-replication-and-data-policy
description: Use when preparing the required data statement, code archive, repository deposit/link, and proprietary-data documentation for a Journal of Banking & Finance manuscript under Elsevier Option C research-data expectations.
---

# Replication & Data Policy (jbf-replication-and-data-policy)

## When to trigger

- The paper uses CRSP, Compustat, BankFocus, Dealscan, TRACE, Call Reports, hand-collected data, or simulations
- You need a data availability statement for Elsevier/JBF submission
- You want a legal and useful replication package despite proprietary data

## Policy stance

JBF follows Elsevier **Option C** research-data instructions. At submission, authors
must state data availability. For shareable data, deposit the research data in a
relevant repository and cite/link it in the article. If data cannot be shared,
state why (for example, proprietary, sensitive, confidential, or licensing limits).
JBF does not operate a dedicated journal-run replication archive, so the practical
package should combine a repository deposit where rights allow, code, metadata,
and a precise access route for restricted inputs.

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

## Proprietary-data audit

For licensed banking/finance sources, add a `data_access/README.md` that records:

- vendor/product, query filters, identifiers, and date accessed;
- variables needed to recreate the analysis;
- any hand-cleaning or link-table rules;
- whether a pseudo dataset can exercise the full code path;
- who can legally access the raw data and under what license.

## Source-by-source sharing matrix

| Typical JBF source | Redistribution | What the package carries instead |
| --- | --- | --- |
| US Call Reports / FDIC SDI | public — share extracts | pull scripts with vintage, date, and series mnemonics |
| Orbis Bank Focus / BankScope legacy | licensed — do not share | query filters, consolidation codes, variable list, access date |
| DealScan | licensed — do not share | extraction steps, facility/package level, link-table code |
| CRSP / Compustat (when used) | licensed — do not share | WRDS query description and merge keys |
| Hand-collected regulatory events | usually shareable | coding manual, per-event sources, inter-coder checks |
| Confidential supervisory data | cannot leave the authority | aggregate descriptives plus the access route for replicators |

## Worked statement draft (illustrative)

```text
Data availability. Bank balance-sheet data come from US Call Reports (FFIEC,
public; pull scripts and vintages in /code/01). Loan-facility data are from
DealScan under license; we provide extraction filters and borrower link-table
code but not raw files. Hand-collected deregulation dates and coding rules are
deposited with the package. All tables and figures regenerate from run_all
with the licensed inputs in place; a synthetic sample exercises the full
pipeline without them.
```

## Pre-submission package audit

- [ ] `run_all` executes on a clean machine with only the licensed inputs mounted
- [ ] every manuscript exhibit maps to exactly one output file, with matching numbering
- [ ] the synthetic or masked sample passes every script end to end
- [ ] vendor vintages and download dates recorded for Bank Focus, DealScan, and any WRDS pulls
- [ ] no author-identifying paths or initials in code comments (double-anonymized review)
- [ ] repository deposit linked and cited where rights allow, or non-sharing reason stated clearly

A package failing two or more boxes usually signals deeper pipeline debt; route back to `jbf-data-analysis` before drafting the statement.

## Editor pushbacks on data

- "The package cannot run without DealScan." → ship a synthetic or masked sample that exercises every script end to end.
- "Which Bank Focus vintage?" → record vendor vintage and download date; bank coverage shifts across vintages.
- "Confidential supervisory data make this unreviewable." → document the authority's access procedure and provide all code plus aggregate moments; the data statement must explain the access limits.

## Output format

```text
[Data status] public / proprietary / confidential / simulated / mixed
[Statement draft] ...
[Shareable files] ...
[Restricted files] ...
[Reproducibility gaps] ...
[Next step] jbf-submission
```
