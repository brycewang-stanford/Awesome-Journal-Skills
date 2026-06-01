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
