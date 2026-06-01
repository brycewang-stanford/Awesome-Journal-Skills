---
name: jape-replication-and-data-policy
description: Use when assembling the mandatory JAE Data Archive deposit for an accepted Journal of Applied Econometrics paper — plain-ASCII/CSV data with a readme, the programs that replicate every result, and the confidential-data exception. Encodes the archive's actual format rules (no bare .dta/SAS) and its history (Queen's 1994–2022, now ZBW).
---

# Replication & Data Policy for JAE (jape-replication-and-data-policy)

Use this from day one, not only after acceptance — the deposit is the journal's signature norm.

## When to trigger

- Preparing the data/code deposit for an accepted JAE paper
- Handling confidential or restricted data under JAE's policy
- Auditing whether your package meets the archive's format rules before deposit

## The signature requirement

JAE's defining norm: **authors of accepted papers must deposit a complete set of the data used onto the Journal's Data Archive, unless the data are confidential.** The archive has held data for **all papers accepted since January 1994** and also stores **programs, technical appendices, and supplementary material**. Hosted at **Queen's University (1994–2022, maintainer J. G. MacKinnon)**, it **moved to ZBW's Journal Data Archive (journaldata.zbw.eu) in 2022** (~1,487 datasets).

## Format rules (do not get this wrong)

- Every dataset needs a **plain-text ASCII readme** (source, variables, units, provenance).
- Data must be **plain ASCII / CSV**. **Proprietary binary (Stata `.dta`, SAS) is NOT acceptable on its own** — export to documented CSV/TXT.
- Supply the **programs** that replicate the results, ordered so a master script runs end to end from raw inputs to every exhibit; note software/version and seeds.

## Confidential-data exception

If data are confidential, **still provide a readme describing the data and its source in enough detail that others can apply for access**, and ideally the extraction programs. **Responsibility for permission rests with the investigator.** Note proprietary data in the cover letter/paper.

## Output format

```
【Data】complete non-confidential set deposited? [Y/N]
【Format】plain ASCII/CSV + readme, no bare .dta/SAS? [Y/N]
【Programs】replicate every result; master script runs? [Y/N]
【Confidential】readme + access path + extraction programs? [Y/N/NA]
【Host】ZBW Journal Data Archive (journaldata.zbw.eu)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Data Archive instructions, host history, format rules
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — exporting to text, master scripts, environment capsules
