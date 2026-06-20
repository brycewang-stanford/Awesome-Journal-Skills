---
name: qe-replication-and-data-policy
description: Use to assemble a Quantitative Economics (QE) replication package that passes the Econometric Society Data Editor's pre-acceptance reproducibility check — raw data, code, documentation, README, and any exemption requests — under the DCAS-compatible ES Data and Code Availability Policy (NOT the JAE archive). Builds and audits the package; it does not run the estimation.
---

# Replication & Data Policy (qe-replication-and-data-policy)

## When to trigger

- You are preparing data and code for a QE submission or an accepted paper
- You need to know exactly what the ES Data Editor checks and when
- Some data are proprietary or restricted and you need to plan an exemption
- You want the package built so the pre-acceptance reproducibility check passes on the first pass

## The QE / Econometric Society replication regime (source map refreshed 2026-06-20)

QE follows the **Econometric Society Data and Code Availability Policy**, shared across *Econometrica*, *Quantitative Economics*, and *Theoretical Economics* and **compatible with DCAS** (the Data and Code Availability Standard). Key facts:

- The Society publishes empirical / experimental / simulation papers **only if data and code are clearly documented and non-exclusive** to the authors.
- **Before acceptance**, authors must provide **raw data, code, and documentation** sufficient to **replicate all results** in the paper and approved online appendices.
- The **ES Data Editor** process conducts **reproducibility checks before final acceptance**. Partial-check scope must be **documented in the README**.
- Replication / supplementary materials are **posted with the article**.
- For **long-running or hard-to-access computations**, simplified/manageable versions and **summary output files** are encouraged.
- Any request for **exemption or limits on data/code access** must be **stated at initial submission** and is at editor discretion.

> **Important:** QE uses this **centralized ES system and the ES Data Editor Website**, **NOT** the JAE (Journal of Applied Econometrics) Data Archive. Do not prepare a JAE-style deposit.

## Building the package

1. **Raw data** (or, for restricted data, the access pathway + the code that would run on it) plus all intermediate data-build steps.
2. **Code** that runs end to end: one master script (`run_all`) regenerating every table, figure, and number from raw inputs.
3. **Documentation / README**: data sources and licenses, software and exact versions, hardware/run-time notes, the mapping from scripts to exhibits, seeds, and **any partial-check scope**.
4. **Environment pinning**: `renv.lock`, `requirements.txt`/`conda`, `Project.toml`/`Manifest.toml`, recorded Stata `ssc`/`net` versions.
5. **Heavy computations**: include manageable versions and summary output files so the Data Editor can verify without re-running everything.
6. **Experimental/own-data**: include instructions/survey transcripts and the pre-registration reference (effective Jan 1, 2026).

## Proprietary / restricted data
- State the exemption or access-limit request **at initial submission** (not at acceptance).
- Provide all **code** even when raw data cannot be shared, plus instructions to obtain access and synthetic or sample data where possible.
- Document exactly which results the Data Editor can and cannot reproduce, in the README.

## Checklist

- [ ] Raw data + full build pipeline included (or restricted-data access path + code)
- [ ] One master script regenerates every result from raw inputs
- [ ] README maps scripts to exhibits; lists sources, versions, seeds, run times
- [ ] Environment pinned across all languages used
- [ ] Heavy computations have manageable versions + summary output files
- [ ] Any exemption / access limit stated at initial submission
- [ ] Partial-check scope documented in the README
- [ ] Built against the **ES Data Editor** regime (DCAS), not the JAE archive

## Anti-patterns

- Preparing a JAE Data Archive deposit by mistake (QE uses the ES system)
- Leaving the package until acceptance — the reproducibility check is **before** acceptance
- Code that depends on absolute local paths or unpinned package versions
- Requesting a proprietary-data exemption only at acceptance instead of at submission
- A README that does not map scripts to the specific tables and figures

## Output format

```
【Regime】ES Data and Code Availability Policy (DCAS) — NOT JAE archive
【Data】raw + build pipeline included? (or restricted-data path + code) [Y/N]
【Master script】regenerates all results from raw? [Y/N]
【README】sources/versions/seeds/script-to-exhibit map? [Y/N]
【Heavy computation】manageable version + summary outputs? [Y/N or N/A]
【Exemption】stated at initial submission? [Y/N or N/A]
【Next step】qe-review-process (pre-acceptance Data Editor check)
```
