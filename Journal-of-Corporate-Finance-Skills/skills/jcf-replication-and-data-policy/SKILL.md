---
name: jcf-replication-and-data-policy
description: Use when preparing the data-availability statement and code/data archive for a Journal of Corporate Finance (JCF) submission under Elsevier "Research Data" Option C — stating data availability at submission and depositing or explaining why data cannot be shared. It builds the data/code deliverables; it is not a substitute for vendor-license compliance.
---

# Replication & Data Policy (jcf-replication-and-data-policy)

## When to trigger

- Drafting the **data-availability statement** at submission
- Deciding what code/data to deposit and where, given vendor licenses
- Preparing the archive that supports the paper's tables and figures

## JCF data policy (verified; re-confirm on the official guide)

JCF follows **Elsevier "Research Data" Option C**. Authors are **required to state data availability at submission** and are **encouraged to deposit research data — including software, code, models, and algorithms — in a relevant repository** and cite/link it, or provide a statement explaining why the data cannot be shared.

There is **no dedicated JFE-Data-Archive-style mandatory replication-package mandate** for JCF (待核实 / none found): the policy is the standard **Elsevier data-availability-statement** framework, **not** a finance-society mandatory code/data archive.

## What this means in practice

- Most JCF data come from **licensed vendors** (Compustat, CRSP, SDC/Refinitiv, DealScan, BoardEx, ISS, Execucomp). You **cannot** redistribute the raw data.
- For licensed data, share **code + variable-construction details + access instructions**, and write a statement that data are available from the named vendor under license.
- For self-collected or public data (e.g., EDGAR text), deposit it with a DOI (Mendeley Data, Zenodo, openICPSR) and cite the deposit.

## Build checklist

- [ ] A **data-availability statement** drafted for submission (Option C wording)
- [ ] One master script (`run_all`) regenerating every table/figure
- [ ] Software/package versions pinned; seeds set for bootstrap/simulation
- [ ] Variable-construction documentation for each licensed source
- [ ] A DOI deposit for any shareable data/code, cited in the paper
- [ ] A clear statement of **why** any data cannot be shared (license/proprietary)

## Source-by-source sharing decisions

```text
Source                      | Deposit raw? | What to deposit instead
Compustat / CRSP / CCM      | No (license) | Pull scripts, link rules, filter code, variable formulas
SDC Platinum / Refinitiv    | No           | Deal-screen criteria, query dates, cleaning code
DealScan                    | No           | Facility-match code; loan-level filter documentation
BoardEx / ISS / Execucomp   | No           | Classification rules; year-by-year coverage notes
Hand-collected governance   | Usually yes  | The dataset itself with a DOI + collection protocol
EDGAR / public filings text | Yes          | Scraper code, parsed extracts, dictionary files
Derived firm-year variables | Check terms  | Many vendors bar derived-data sharing — confirm first
```

When in doubt about derived data, describe the construction completely rather than deposit — a license breach is worse than an opaque archive.

## Worked statement: mixed licensed and hand-collected inputs

Illustrative Option C wording for a governance paper combining BoardEx with hand-collected charter amendments:

```text
Data availability: Board and director data were obtained from BoardEx under license and cannot be
redistributed; access instructions and full variable-construction code are provided at [DOI]. The
hand-collected charter-amendment dataset and all analysis code are deposited at [repository, DOI].
Compustat and CRSP inputs are available from WRDS under subscription.
```

Adapt the names and repositories; the structure — what is licensed, what is deposited, where the code lives — is what the editor checks.

## Archive skeleton that survives a JCF revision

```text
archive/
  README.md            # inputs, licenses, runtime, expected outputs
  run_all.do|.R|.py    # single entry point; table/figure numbering matched
  build/               # pull + clean scripts per source (compustat.do, boardex.R, sdc.py)
  analysis/            # one script per exhibit (t3_main_did, f2_event_study)
  handcollected/       # shareable data + collection protocol
  output/              # regenerated exhibits land here
```

Number analysis scripts by exhibit so an R&R that renumbers tables is a rename, not an archaeology project. JCF revisions routinely add robustness exhibits; an archive organized per-exhibit absorbs them without breaking `run_all`.

## Anti-patterns

- Promising "data available on request" without an Option C statement.
- Attempting to upload raw Compustat/CRSP/SDC extracts (license violation).
- Leaving the archive to acceptance — build it alongside the analysis.
- A README that omits how to obtain the licensed inputs.

## Output

```
【DAS】Option C statement drafted? [Y/N]
【Archive】run_all + versions + seeds + var-construction? [Y/N each]
【Deposit】DOI for shareable data/code? [Y/N]; licensed-data note? [Y/N]
```
