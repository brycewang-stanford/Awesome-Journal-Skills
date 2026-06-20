---
name: eer-replication-package
description: Use when assembling the data and code deposit for a European Economic Review (EER) manuscript under Elsevier's mandatory replication policy. Builds a reproducible package and README; it does not run the analysis or write the paper.
---

# Replication Package (eer-replication-package)

## When to trigger

- The paper contains empirical work, simulations, or experiments
- Results are stabilizing and the deposit should be assembled (not at the last minute)
- Preparing for acceptance, when the replication materials must be provided
- A referee or editor asks about data/code availability

## The EER replication bar

EER operates a **mandatory replication policy**: authors of accepted papers with empirical, simulation, or experimental content must provide, **prior to publication**, the **data, programs, and computational details sufficient to permit replication** of the reported results (检索于 2026-06；以官网为准). Elsevier's data-and-code availability framework applies; deposits typically go to a repository (e.g., **Mendeley Data** / Zenodo) and are linked from the article. Re-confirm on the official EER policy page whether there is **pre-acceptance verification by a data editor**, the exact deposit location, and the handling of restricted data — do **not** assert a verification step or repository that the current policy does not state. Build the package **as you go** so the deposit is not a scramble at acceptance.

## What to assemble

### Data
- **Raw data** (or, for restricted data, the access path + a data-availability statement explaining how a replicator obtains it).
- **Intermediate/analysis files** with a clear lineage from raw to final.
- A **data dictionary / codebook** for constructed variables.
- A **data-availability statement** matching what the article claims.

### Code
- **One master script** (`run_all`) that regenerates **every table and figure** from raw data.
- Scripts ordered and numbered (clean → construct → analyze → exhibits).
- **Pinned environment**: package versions recorded (`requirements.txt`/`conda` for Python, `renv.lock` for R, recorded Stata `ssc`/`net` versions; `Project.toml`/`Manifest.toml` for Julia).
- **Seeds set and reported** for simulation / bootstrap / randomization inference.

### Documentation (README)
- Software + versions; hardware/runtime notes; expected outputs mapped to **specific tables/figures**.
- Any **partial-reproduction scope** (e.g., confidential data) stated honestly.
- License for the code; data-use terms respected.

## Checklist

- [ ] `run_all` master script regenerates every reported table and figure from raw data
- [ ] Raw + intermediate data included, or a clear restricted-data access path given
- [ ] Data dictionary / codebook for constructed variables
- [ ] Environment pinned (language + package versions recorded)
- [ ] Seeds set and reported for all stochastic steps
- [ ] README maps each script/output to specific exhibits; runtime noted
- [ ] Data-availability statement matches the article and the deposit
- [ ] Deposit location confirmed against the current EER/Elsevier policy (检索于 2026-06)
- [ ] Restricted/proprietary data handled per policy; partial-repro scope documented

## Anti-patterns

- Leaving the package to acceptance week — it controls the publication timeline
- A code dump with no master script and no mapping from output to exhibits
- Unpinned environments ("it ran on my laptop") that a replicator cannot reproduce
- Unset seeds making simulation/bootstrap results non-reproducible
- A data-availability statement that overclaims what is actually deposited
- Asserting a data-editor verification step or repository not stated in the current policy

## Worked vignette (illustrative)

An applied-micro paper ships a single `.zip`: `00_run_all.do`, numbered `01_clean` → `05_tables`, a `data/raw` folder with a public extract plus a documented access path for the confidential employer–employee link, an `renv`-style version log of Stata packages, seeds fixed in the bootstrap, and a README mapping every do-file to the table/figure it produces and noting the confidential-data partial-reproduction scope. At acceptance the deposit goes to the repository the policy specifies and the article links it.

## Output format

```
【Content】empirical / simulation / experimental (replication policy applies)
【Master script】run_all regenerates all exhibits? [Y/N]
【Data】raw included OR restricted-access path documented? [Y/N]
【Environment】versions pinned + seeds set/reported? [Y/N]
【README】outputs mapped to exhibits + partial-repro scope? [Y/N]
【Deposit】location confirmed vs current policy (检索于 2026-06)? [Y/N]
【Next step】eer-referee-strategy or eer-submission
```
