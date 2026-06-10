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

## Deposit assembly order

Build the package in this sequence — each step catches a different failure class before the archive does:

1. **Export** every input the paper touches to documented CSV/TXT; delete nothing from the pipeline that an exhibit needs.
2. **Freeze** the environment: software names, versions, OS, package list, and all seeds, written into the readme.
3. **Cold-run** the master script in a clean directory on a second machine; diff regenerated tables against the accepted manuscript digit by digit.
4. **Strip** absolute paths, credentials, and licensed raw files you may not redistribute (replace with extraction code + access instructions).
5. **Name** files so the mapping is mechanical: `table1.csv`, `fig2_data.txt`, programs that announce which exhibit they build.

## readme.txt skeleton for the archive deposit

```text
README for [Author(s)], "[Title]", Journal of Applied Econometrics
1. Data files: [name] — source, sample span, units, variable list
2. Provenance: where each series was obtained; access date; license
3. Programs: run order; master script; software + version; seeds
4. Mapping: program → table/figure in the published paper
5. Confidential components: description + how to apply for access
Contact: [author email]
```

Plain ASCII, no markup — the archive's own holdings are flat text and the readme should match.

## Replication Articles and the archive trail

JAE's dedicated replication track exists because the archive makes published results re-runnable. If you are submitting to it: pick a prominent target paper, obtain its archived (or otherwise public) data and code, and report what you find whether it confirms, qualifies, or overturns — negative replications are explicitly in scope. Separate three failure sources in your write-up: data revisions since the original, implementation/coding differences, and genuine fragility of the result. Confirm current track-specific instructions against the journal's author guidelines before submitting.

## Deposit pitfalls that bounce packages

- A `.dta` or SAS file with no CSV/TXT sibling — violates the archive's plain-text rule outright.
- Readme describes an earlier draft's tables; the accepted version renumbered them.
- Bootstrap or simulation results that drift run-to-run because a seed was never set.
- "Data available on request" used where the data are merely inconvenient, not confidential — the exception is for genuinely restricted data, and the investigator carries the permission burden.

## Output format

```
【Data】complete non-confidential set deposited? [Y/N]
【Format】plain ASCII/CSV + readme, no bare .dta/SAS? [Y/N]
【Programs】replicate every result; master script runs? [Y/N]
【Cold-run】clean-machine rerun matches published digits? [Y/N]
【Confidential】readme + access path + extraction programs? [Y/N/NA]
【Host】ZBW Journal Data Archive (journaldata.zbw.eu)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Data Archive instructions, host history, format rules
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — exporting to text, master scripts, environment capsules
