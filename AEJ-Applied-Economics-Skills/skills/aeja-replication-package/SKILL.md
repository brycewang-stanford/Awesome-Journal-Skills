---
name: aeja-replication-package
description: Use when assembling the data and code replication package for an American Economic Journal: Applied Economics (AEJ: Applied) manuscript to pass the AEA Data and Code Availability Policy and the AEA Data Editor's pre-publication reproducibility check. Builds the openICPSR deposit and README; it does not run the analysis or write the paper.
---

# Replication Package & AEA Data Policy (aeja-replication-package)

## When to trigger

- The paper is empirical and you are heading toward acceptance (or want to build the package early)
- An R&R or conditional acceptance asks you to prepare the data + code deposit
- You need to write the README and Data Availability Statement to AEA standard
- Some data are restricted/proprietary and you must plan the deposit around that

## Why this is the AEJ: Applied signature

The single most distinctive AEJ: Applied differentiator is the **AEA Data and Code Availability Policy**, administered by the **AEA Data Editor (Lars Vilhuber)**. Papers offered a revise-and-resubmit are asked to submit a data replication package at resubmission, and accepted papers must clear the Data Editor's compliance and reproducibility checks before publication. The default home is the **AEA Data and Code Repository on openICPSR**; other trusted repositories require appropriate Data Editor access. Build this package as you analyze; do not treat it as an acceptance-day formality.

## What the package must contain

| Component | Requirement |
|-----------|-------------|
| **Data files** | All data used, *unzipped*, in open/documented formats; or, for restricted data, a precise access path |
| **Analysis + transformation code** | Every script from raw data → cleaned data → each table/figure |
| **Master script** | One `run_all` that regenerates every exhibit from raw inputs |
| **README** | AEA README template: data sources, access, computational requirements, run instructions, exhibit-to-code mapping |
| **Data Availability Statement (DAS)** | States provenance and access terms for each dataset; required in the paper |
| **Instruments** | Survey instruments / experiment instructions for own-data studies |

## Handling restricted or proprietary data

- You **cannot** deposit restricted data, but you **must** still deposit all code and document the exact access procedure (provider, application steps, cost, approximate wait).
- Provide a small **synthetic or public extract** so the code runs and the Data Editor can verify logic where possible.
- Declare any **restricted-data or exemption request at the earliest opportunity** — limited-access arrangements are at editor/Data-Editor discretion and must be flagged, not discovered at the check.

## Reproducibility hygiene (build as you go)

- **Pin versions:** Stata `version` + recorded `ssc`/`net` package versions; `requirements.txt`/conda env (Python); `renv.lock` (R).
- **Set and report seeds** for every simulation, bootstrap, and randomization-inference step.
- **No absolute paths** — one root macro/variable; relative paths thereafter.
- **Exhibit-to-code map** in the README: Table 3 → `code/05_main.do`, Figure 2 → `code/06_event_study.R`, etc.
- **Run it clean** on a fresh checkout before depositing; the Data Editor will.

> Adapt the vendored skeleton in [`../../resources/code/`](../../resources/code/) (master script → clean → descriptive → DID/IV/RD/DML → mechanism → robustness → tables) as the package backbone.

## Checklist

- [ ] One `run_all` master script regenerates every table and figure from raw data
- [ ] All data deposited unzipped (or restricted-data access path fully documented + synthetic extract provided)
- [ ] README follows the AEA template with a complete exhibit-to-code map
- [ ] Data Availability Statement written for every dataset, with access terms
- [ ] Software/package versions pinned; seeds set and reported
- [ ] No absolute paths; runs clean on a fresh checkout
- [ ] Restricted-data / exemption requests declared early, not at the check
- [ ] Own-data studies include survey instruments / experiment instructions

## Anti-patterns

- Treating the package as an acceptance-day task — the check is **pre-publication** and gates publication
- Depositing code that depends on absolute paths or unrecorded package versions (fails to reproduce)
- Zipped data, missing intermediate files, or a README with no exhibit-to-code mapping
- Restricted data discovered at the check with no access documentation or synthetic extract
- Unset seeds making bootstrap/RI results non-reproducible

## Output format

```
【Master script】run_all regenerates all exhibits from raw? [Y/N]
【Data】all deposited unzipped, or restricted path + synthetic extract? [state]
【README】AEA template + exhibit-to-code map complete? [Y/N]
【DAS】written for every dataset with access terms? [Y/N]
【Reproducibility】versions pinned + seeds set + no absolute paths + clean fresh run? [Y/N]
【Restricted/exemption】declared early? [Y/N/NA]
【Next step】aeja-referee-strategy (or aeja-submission)
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — reproducible Stata + Python skeleton to adapt as the package backbone
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official AEA URLs behind the data/code policy
