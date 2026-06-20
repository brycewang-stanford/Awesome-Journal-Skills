---
name: jeem-replication-package
description: Use when assembling the data and code deposit for a Journal of Environmental Economics and Management (JEEM) manuscript — meeting JEEM's data-availability/replication expectation, documenting monitoring/satellite/admin/restricted environmental data, and writing a README that reproduces every exhibit. Builds the package; it does not run the analysis or invent data.
---

# Replication Package (jeem-replication-package)

## When to trigger

- The paper is heading to submission or acceptance and the data/code deposit is not assembled
- The analysis uses **restricted or proprietary** environmental data (utility, satellite, admin pollution, parcel) and you must document a replication path you cannot fully share
- The Editor must be told *at submission* that the data-availability conditions cannot be fully met
- Code reproduces exhibits manually rather than from a single master script

## JEEM's replication expectation

JEEM has a long-standing policy: **all data used must be clearly documented, computational methods explained in enough detail to permit replication, and the data made available to any researcher for replication** — and the **Editor must be notified at submission if these conditions cannot be met** (检索于 2026-06；以官网为准; re-check the current guide for authors, as Elsevier data-availability and code-sharing requirements are tightening). Environmental papers routinely hit this wall because the data are spatial, sensor-derived, or proprietary; the package must show a *credible reproduction path* even when raw data cannot be posted.

## Why environmental papers fail replication more often

Three structural features make environmental replications fragile, and the package must address each head-on. First, **versioning:** satellite and weather products are reissued (collection upgrades, reanalysis vintages), so a result is irreproducible unless the exact version is pinned. Second, **spatial operations:** geocoding, reprojection, and spatial joins are easy to do interactively and impossible to reproduce unless scripted with the CRS recorded. Third, **proprietary inputs:** utility, parcel, and licensed sensor data often cannot be posted at all, so the package must substitute derived/synthetic data and a precise access protocol. A package that ignores these three will pass a casual check and fail a serious one.

## Building the package

1. **One master script reproduces everything.** A single entry point (e.g., `make` / `run_all`) that goes raw → cleaned → every table and figure, with no manual steps. Map each exhibit to the script that builds it.
2. **Document every data source by provenance.** For each source: name, version/vintage, access date, license, geographic unit and CRS, and exactly how it was obtained — pollution monitors (EPA AQS), satellite products (MODIS/Sentinel, with retrieval algorithm and grid), weather (PRISM/ERA5), parcel/assessor, permit registries, survey instruments.
3. **Handle restricted data explicitly.** If raw data cannot be shared (utility billing, confidential parcel, licensed satellite), provide the **derived/aggregated data** that can be, the **exact access protocol** for the rest (provider, application, cost, embargo), and synthetic or sample data so the code runs end-to-end.
4. **Preserve the spatial pipeline.** Geocoding, projection, buffer construction, and spatial joins are where environmental replications break — script them and record CRS/version of every spatial operation; do not rely on a one-off GIS click-path.
5. **Pin the computational environment.** Software versions, packages/seeds, and any HPC/cluster details; environmental papers with weather grids or large rasters need runtime and memory noted.
6. **For stated-preference work**, include the full survey instrument, the experimental design (choice sets, blocking), and the elicitation script.

## Notifying the Editor about data constraints

JEEM's policy requires telling the Editor *at submission* if the data-availability conditions cannot be fully met — do not wait for acceptance. Draft a short data-availability statement that says, per source, whether it is bundled, derived-and-bundled, or restricted-with-access-protocol, and name any source you genuinely cannot share with the reason (license, confidentiality). Pair every restricted source with what you *can* provide: aggregated data, the code that processed it, and synthetic/sample data so the pipeline runs. A candid, complete statement at submission is far better received than a discovered gap at the replication check.

## Checklist

- [ ] A single master script reproduces every table and figure from raw inputs, no manual steps
- [ ] Each exhibit is mapped to the code that produces it
- [ ] Every data source documented: provenance, version, access date, license, unit, CRS
- [ ] Restricted data: derived data shared, exact access protocol given, sample/synthetic data lets code run
- [ ] Editor notified at submission if data-availability conditions cannot be fully met
- [ ] Spatial pipeline (geocode, projection, buffers, joins) scripted with CRS/versions recorded
- [ ] Software versions, package versions, and seeds pinned; runtime/memory noted for large grids
- [ ] Survey instrument and choice-experiment design included for stated-preference papers

## Environmental data sources to document by name

JEEM replications break most often on the data layer, because environmental inputs are heterogeneous and versioned. Name the exact source and vintage for each:

- **Pollution monitors:** EPA AQS (or national equivalent), station IDs, pollutant, averaging window, and how missing/invalid readings were handled.
- **Satellite / remote sensing:** product (MODIS AOD, Sentinel-5P, VIIRS nightlights), retrieval algorithm and collection version, grid resolution, and the cloud/quality mask applied.
- **Weather / climate:** PRISM, ERA5, Daymet — vintage, variable definitions, and the aggregation (degree-days, bins) with the script that built them.
- **Spatial boundaries:** TIGER/Line, census, or cadastral shapefiles with year and CRS; document every reprojection.
- **Administrative / proprietary:** permit registries, utility billing, assessor/parcel records — provider, extract date, and the licensing/embargo terms that constrain sharing.

## Worked vignette (illustrative)

A paper merges satellite PM2.5, EPA monitors, and assessor parcel data to estimate amenity capitalization. The replicator cannot reproduce the exposure variable because the satellite product version and the cloud mask were never stated, and the parcel-to-grid spatial join was done by hand. The JEEM fix: a master script that pulls the named satellite collection version, applies the recorded quality mask, and runs the spatial join with the logged CRS; the proprietary parcel data is replaced with a synthetic parcel file so the code runs end-to-end, plus the exact assessor access protocol for the real data. The package now reproduces every exhibit from one command.

## Reproducibility is part of the contribution

Treat the package as part of the paper, not a chore at the end. Environmental-economics estimates feed policy debates, so a result that cannot be independently reproduced is a result a regulator should not act on — and JEEM's policy reflects that. Building the master script and provenance documentation as you go (rather than reconstructing them at acceptance) also catches your own errors early: a pipeline that runs clean from raw data to every exhibit is itself evidence of correctness. The packages that fail are the ones assembled hastily after the science is "done"; the ones that pass were designed for reproduction from the first analysis script.

## Anti-patterns

- A code folder with no master script — referees/replicators must guess the run order
- "Data available on request" with no derived data, no access protocol, and no Editor notification
- Spatial joins and projections done by hand in GIS, impossible to reproduce
- Posting cleaned data but omitting the cleaning code that produced it
- Hard-coded local file paths that break outside the author's machine
- Omitting satellite retrieval algorithm/version or weather product vintage (silent irreproducibility)

## The README a JEEM replicator needs

Write the README for someone who has the package and none of your tacit knowledge. It should state, up front: the software and versions, the single command that reproduces everything, the expected runtime and memory (large raster/grid jobs can run for hours), and a table mapping each manuscript exhibit (Table 1, Figure 3, ...) to the script and the output file that produces it. Then a data section listing every source with its provenance block, flagging which sources are bundled, which are derived, and which require an access protocol. A replicator should be able to reproduce every shareable result without emailing you — and know exactly how to obtain the restricted pieces.

## Output format

```text
【Journal】Journal of Environmental Economics and Management
【Skill】jeem-replication-package
【Master script】one entry point reproduces all exhibits? [Y/N]
【Data provenance】every source: version/access-date/license/unit/CRS? [Y/N]
【Restricted data】derived data + access protocol + sample data provided? [Y/N]
【Editor notice】notified at submission if conditions unmet? [Y/N / n/a]
【Spatial pipeline】geocode/projection/buffers/joins scripted with CRS? [Y/N]
【Environment】software/package versions + seeds pinned? [Y/N]
【Source status】verified URL / 待核实 / not asserted
【Next skill】jeem-referee-strategy
```
