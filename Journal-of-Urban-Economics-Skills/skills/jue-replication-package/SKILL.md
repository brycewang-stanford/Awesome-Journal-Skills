---
name: jue-replication-package
description: Use when assembling the data and code deposit for a Journal of Urban Economics (JUE) manuscript under its mandatory replication policy — especially geocoded, restricted, or proprietary spatial data. Builds the JUE-compliant replication folder and confidentiality path; it does not run the analysis or write the prose.
---

# Replication Package (jue-replication-package)

## When to trigger

- The paper contains empirical, simulation, or experimental work — JUE's **mandatory replication policy** applies
- The data is **geocoded, restricted, or proprietary** (addresses, parcels, admin records) and you need a confidentiality path
- You are at acceptance and must upload the replication folder *before publication*
- A spatial pipeline (geocoding, GIS joins, distance/ring construction) is undocumented and not reproducible
- A coauthor assumes the deposit can wait until after publication — it cannot

## JUE's mandatory replication policy (检索于 2026-06；以官网为准)

JUE will publish a paper only if the data and code are **clearly documented and readily available for replication**. At **acceptance, before publication**, authors of papers with empirical work, simulations, or experiments must upload a **replication folder to a major data repository**. The minimum deposit is:

1. **The dataset(s)** used to generate all estimates reported in the paper;
2. **A description of how intermediate datasets and programs** were used to build the final dataset(s);
3. **The complete set of code** from raw data to final results — except where code would reveal confidential information about the data.

**Proprietary / confidential data:** authors may request an exemption from providing data and/or code. The request must be made in the **submission cover letter to the editor**. Even with an exemption, document the pipeline and provide whatever code does not reveal confidential information so the path to results is auditable.

## Spatial-data deposits are harder than they look

Urban papers carry data hazards that generic replication checklists miss:

- **Geocoding is not reproducible by default.** Pin the geocoder, version, and date; deposit the crosswalk from addresses to coordinates (or a de-identified version) so distance/boundary variables can be regenerated.
- **Restricted address/parcel data.** Provide a synthetic or aggregated extract plus exact instructions to obtain the restricted file (agency, application, access tier), and deposit all code that runs against it.
- **GIS layers and shapefiles.** Deposit or cite the exact boundary/shapefile vintages (tracts, school zones, transit lines); boundaries change across years and silently break replication.
- **Spatial construction code.** Ring/donut buffers, distance-to-boundary, market-access, and spatial-weight matrices must be in the code, with the distance cutoffs and projection (CRS) stated.

## Building the folder

1. **One-click master script** (`run_all`) raw → cleaned → estimates → exhibits, with a stated software/version environment.
2. **README** mapping each table/figure to the script that produces it; list data sources with access tiers and the GIS-layer vintages.
3. **Separate raw, intermediate, and final data** so reviewers can re-run from any stage.
4. **Confidential path:** if exempt, the README states what is withheld, why, and how a researcher with access can reproduce it; the cover-letter exemption is filed.
5. **Verify on a clean machine** before deposit — the most common failure is hard-coded local paths and unstated CRS/geocoder versions.

## Restricted-data access paths common in urban work

Urban papers lean on data that cannot simply be posted; document the *path*, not just the absence:

- **Census/admin microdata in an RDC/FSRDC enclave** — state the dataset, the project-approval route, and deposit all code that runs inside the enclave plus disclosure-cleared output; a researcher with clearance must be able to reproduce.
- **Proprietary real-estate / transaction data** (CoreLogic, Zillow ZTRAX-type, MLS) — cite the vendor and vintage, deposit construction code, and provide a synthetic or aggregated extract where the license permits.
- **Geocoded individual records** — deposit the de-identified crosswalk or the construction code that maps protected addresses to the spatial variables (distance, ring, boundary side), withholding only the raw identifiers.
- **Mobility / GPS / cell-phone data** — document the provider, the spatial and temporal resolution, and the aggregation that produces the analysis file.

In every case the cover-letter exemption names what is withheld and why, and the README states exactly how an authorized researcher reproduces the results.

## Checklist

- [ ] Replication folder targets a major repository; deposit planned for acceptance (before publication)
- [ ] All datasets behind reported estimates included (or exemption requested in the cover letter)
- [ ] Intermediate-data construction described; raw → final pipeline complete
- [ ] Geocoder/version/date pinned; address↔coordinate crosswalk (or de-identified) deposited
- [ ] GIS layer/shapefile vintages cited; CRS/projection stated
- [ ] Spatial construction code (buffers, distance, weights, market access) included with cutoffs
- [ ] `run_all` master script verified on a clean machine; README maps exhibits to scripts
- [ ] Confidential-data exemption documented if applicable
- [ ] Restricted-access path (RDC/vendor/enclave) named with the route to reproduce
- [ ] Folder assembled during the R&R as a correctness check, not left to acceptance

## Anti-patterns

- Assuming the deposit waits until after publication (JUE requires it at acceptance, before publication)
- Geocoding with an unpinned service, so distance/boundary variables cannot be regenerated
- Depositing code but not the GIS-layer vintages, so boundaries silently differ across years
- Hard-coded local paths and an unstated CRS that break the spatial pipeline on another machine
- Claiming proprietary data without filing the cover-letter exemption or documenting the access path
- A README that lists files but never maps each table/figure to the code that makes it

## Why early assembly pays off

Although JUE requires the deposit only at acceptance, assembling the folder during the R&R (or before submission) protects you twice. First, the act of building a one-click `run_all` from raw geocoded data to final maps routinely surfaces silent errors — a wrong CRS, a stale shapefile vintage, a dropped buffer — that would otherwise survive into the published result. Second, an acceptance deadline is the worst time to discover a restricted-data path cannot be reproduced or that a vendor license forbids posting an extract; the exemption and access instructions take time to negotiate. Treat the replication folder as a correctness check on the spatial pipeline, not a post-acceptance formality.

## Output format

```text
【Policy trigger】empirical/simulation/experimental? deposit at acceptance planned? [Y/N]
【Datasets】all reported-estimate data included / exemption requested in cover letter
【Pipeline】raw→intermediate→final documented; run_all verified clean? [Y/N]
【Geocoding】geocoder+version pinned; crosswalk deposited? [Y/N]
【GIS layers】shapefile vintages cited; CRS stated? [Y/N]
【Spatial code】buffers/distance/weights/market-access included with cutoffs? [Y/N]
【Confidential path】exemption + access instructions documented? [Y/N/NA]
【Next skill】jue-referee-strategy
```
