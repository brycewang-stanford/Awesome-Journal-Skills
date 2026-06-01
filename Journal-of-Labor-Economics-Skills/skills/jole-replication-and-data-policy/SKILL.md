---
name: jole-replication-and-data-policy
description: Use when assembling the data and code deposit for an accepted Journal of Labor Economics (JOLE) paper — the JOLE Dataverse Repository, the AER data-availability policy (adopted Feb 2009), and proprietary-data handling. Builds the replication package; it does not run analysis.
---

# Replication & Data Policy (jole-replication-and-data-policy)

## When to trigger

- Your JOLE paper is accepted (or about to be) and you must deposit data and code
- Your data are proprietary or restricted and you need to handle the policy correctly
- You want to build the replication package as you go, not scramble at acceptance
- A referee or editor asks how the results can be reproduced

## JOLE's actual data policy

JOLE publishes papers containing **empirical, simulation, or experimental** results **only if the data are clearly documented and readily available for replication.** The mechanics:

- **Deposit target:** after acceptance, authors upload **data, programs, and sufficient documentation to permit replication (in electronic form) to JOLE's Dataverse Repository — prior to publication.** The deposit is part of the path to print, not an optional extra.
- **Minimum for econometric / simulation papers:** the **dataset(s)** and the **programs used to run the final models**, plus a **description of how intermediate datasets and programs were used to build the final dataset** from the raw inputs. In other words, document the full chain from raw data to estimation, not just the last regression.
- **Policy lineage:** JOLE **adopted the AER (American Economic Review) data-availability policy in February 2009**, applying to articles submitted after that date. If you know the AER/AEA model, JOLE's expectations will be familiar.
- **Proprietary or restricted data:** authors must **notify the editor at submission** if the data are proprietary or the requirements otherwise cannot be met. Do not wait until acceptance to disclose this — flag it in the cover letter (see jole-submission, jole-review-process). Even with restricted data, you are generally expected to provide the **programs** and enough documentation for a qualified replicator to reproduce results given access.
- **Ethics:** operate under UChicago Press / COPE guidelines, with explicit attention to **confidential data and research on vulnerable / human subjects**.

## Building the package (do this as you go)

1. **One master script** (`run_all`) that regenerates **every table and figure** from the analysis data.
2. **Document the chain** from raw inputs → cleaning → intermediate files → final estimation dataset, matching the policy's "intermediate datasets/programs" requirement.
3. **README** describing data sources, access conditions, software/package versions, run order, and expected outputs.
4. **Pin the environment** (Stata `ssc`/`net` versions, `renv.lock`, `requirements.txt`) and **set/report seeds** for bootstrap, randomization inference, and simulation.
5. **Restricted data:** include the code and a clear description of how to obtain access (e.g., FSRDC, register agreements); provide synthetic or public extracts where licensing permits.
6. **Stage early:** assemble this alongside the analysis so the post-acceptance Dataverse upload is a packaging step, not a reconstruction.

## Checklist

- [ ] Data + programs + documentation prepared for the **JOLE Dataverse Repository**
- [ ] Master script regenerates **all** tables and figures
- [ ] Raw → intermediate → final data chain documented (per AER-style policy)
- [ ] README with sources, access terms, software versions, run order
- [ ] Seeds set and reported; environment pinned
- [ ] **Proprietary/restricted data flagged to the editor at submission**, with code + access path provided
- [ ] Human-subjects / confidential-data handling consistent with COPE / UChicago Press ethics

## Anti-patterns

- Treating the deposit as optional — JOLE publishes empirical work only if it is replicable
- Depositing only the final regression code without the data-build chain
- Discovering at acceptance that proprietary data were never flagged to the editor
- A package that cannot reproduce a table because the seed or version was not recorded
- Assuming "restricted data" exempts you from providing **programs** and documentation
- Reconstructing the package from memory at the last minute instead of building it as you go

## Output format

```
【Deposit target】JOLE Dataverse Repository (data + programs + docs) [ready Y/N]
【Master script】regenerates all exhibits? [Y/N]
【Data chain】raw → intermediate → final documented? [Y/N]
【Environment】versions pinned + seeds reported? [Y/N]
【Proprietary data】flagged to editor at submission + access path provided? [Y/N/NA]
【Ethics】COPE / human-subjects handling noted? [Y/N/NA]
【Next step】jole-submission (or back to jole-review-process)
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — labor data sources and version-pinning / reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — the JOLE data-policy URL and its verification status
