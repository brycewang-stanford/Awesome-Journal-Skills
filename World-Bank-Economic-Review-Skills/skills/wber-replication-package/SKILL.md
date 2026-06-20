---
name: wber-replication-package
description: Use when assembling the data and code replication package for a The World Bank Economic Review (WBER) manuscript to meet WBER's condition-of-publication data/code release, the data availability statement with a DOI repository link, and the realities of restricted developing-country data. Builds the deposit and README; it does not run the analysis or write the paper.
---

# Replication Package & Data Policy (wber-replication-package)

## When to trigger

- The paper is empirical and headed toward acceptance (or you are building the package early)
- You need to write the data availability statement and the DOI repository link for the title page
- Some data are restricted, proprietary, or governed by a national statistics office and you must plan the deposit around that
- An R&R asks you to make data and code available
- You want to know what "condition of publication" actually requires here

## Why this is a WBER signature

WBER's most distinctive, stable policy is **transparency as a condition of publication**: authors must, where ethically and legally possible, **publicly release all data and the software code** underlying a published paper. By repute WBER is the only development *field* journal that routinely publishes data and code, and this fits the broader World Bank reproducible-research push. The manuscript must carry a **data availability statement** — on the title page / author-affiliation footnote — with a **persistent (preferably DOI) link** to the data in a repository (检索于 2026-06；以官网为准; verify exact wording on the OUP author guidelines). Build the package as you analyze; do not treat it as an acceptance-day formality.

## What the package must contain

| Component | Requirement |
|-----------|-------------|
| **Data files** | All data used, in open/documented formats; or, for restricted data, a precise documented access path |
| **Analysis + transformation code** | Every script from raw → cleaned data → each table/figure |
| **Master script** | One `run_all` that regenerates every exhibit from raw inputs |
| **README** | Data sources, access terms, computational requirements, run instructions, and an exhibit-to-code map |
| **Data Availability Statement** | On the title page; persistent DOI link to the repository deposit |
| **Instruments** | Survey instruments / enumerator manuals for own-data field studies |

## Handling restricted developing-country data

This is the WBER-specific hard part — much development data is governed by national statistics offices, ministries, or data providers (LSMS, DHS, census, tax records):

- You **cannot** post restricted microdata, but you **must** still deposit all code and document the exact access procedure: provider, application steps, any cost, approximate wait, and the data version/round used.
- Provide a small **synthetic or public extract** so the code runs end-to-end and a verifier can check the logic where the real data cannot be shared.
- For DHS/LSMS-type data, cite the **specific survey round and version** and the registration step a replicator must complete; do not assume "DHS data" is self-locating.
- Declare any **restricted-data or exemption situation at the earliest opportunity**, not at the final check — arrangements are at editor discretion.

## Reproducibility hygiene (build as you go)

- **Pin versions:** Stata `version` + recorded `ssc`/`net` package versions; `requirements.txt`/conda env (Python); `renv.lock` (R).
- **Set and report seeds** for every simulation, bootstrap, and randomization-inference step.
- **No absolute paths** — one root macro/variable; relative paths thereafter.
- **Exhibit-to-code map** in the README: Table 3 → `code/05_main.do`, Figure 2 → `code/06_event_study.R`.
- **Run it clean** on a fresh checkout before depositing.
- **Currency/PPP transparency:** document deflators, PPP conversion factors, and exchange-rate sources — replicators in development work need these to reproduce real-value results.

> Adapt the vendored skeleton in [`../../resources/code/`](../../resources/code/) (master → clean → descriptive → DiD/IV/RD → mechanism → robustness → tables) as the package backbone.

## Checklist

- [ ] One `run_all` master script regenerates every table and figure from raw data
- [ ] All data deposited (or restricted-data access path documented + synthetic/public extract provided)
- [ ] README has a complete exhibit-to-code map and computational requirements
- [ ] Data Availability Statement on the title page with a persistent DOI repository link
- [ ] Specific survey rounds/versions (DHS/LSMS/census/admin) cited with the registration step
- [ ] Software/package versions pinned; seeds set and reported; no absolute paths
- [ ] Deflators / PPP / exchange-rate sources documented
- [ ] Restricted-data / exemption situation declared early; field instruments included

## Anti-patterns

- Treating data/code release as optional or as an acceptance-day task — it is a condition of publication
- A title page with no data availability statement or no persistent DOI link
- "DHS/LSMS data" cited with no round, version, or registration path (not reproducible)
- Restricted data with no documented access procedure and no synthetic extract
- Absolute paths, unrecorded package versions, or unset seeds that break reproduction
- Undocumented deflators/PPP factors so real-value results cannot be regenerated

## Worked vignette (illustrative)

A poverty paper uses LSMS consumption data (restricted, registration-gated) plus a public price index. The team cannot post the LSMS microdata, so the package contains: every cleaning and analysis script; a README naming the **specific LSMS country, round, and version** and the exact registration steps a replicator must complete; a small **synthetic extract** with the same variable structure so `run_all` executes end-to-end; documented deflators and PPP factors; and pinned Stata package versions with seeds set for the bootstrap. The title page carries a data availability statement with a DOI link to the openICPSR-style deposit holding the code and synthetic data. Because the public price index *can* be shared, it is deposited in full. The package would let a verifier reproduce the logic, and reproduce the numbers entirely once they obtain LSMS access.

## Output format

```text
【Master script】run_all regenerates all exhibits from raw? [Y/N]
【Data】all deposited, or restricted path + synthetic extract? [state]
【DAS + DOI】title-page statement with persistent repository link? [Y/N]
【Survey provenance】DHS/LSMS/admin round + version + access step cited? [Y/N]
【Reproducibility】versions pinned + seeds + no absolute paths + clean run? [Y/N]
【Currency】deflators/PPP/FX documented? [Y/N]
【Restricted/exemption】declared early? [Y/N/NA]
【Next step】wber-referee-strategy
```

## Supplementary resources

- [`../../resources/code/`](../../resources/code/) — reproducible Stata + Python skeleton to adapt as the package backbone
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official OUP / WBER URLs behind the data policy
