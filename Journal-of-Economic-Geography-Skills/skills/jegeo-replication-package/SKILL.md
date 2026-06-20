---
name: jegeo-replication-package
description: Use when assembling data, code, and spatial-data documentation for a Journal of Economic Geography (JEG) manuscript. Builds a credible, shareable package under JEG's encouragement-based post-acceptance policy; it does not invent data.
---

# Replication Package (jegeo-replication-package)

## When to trigger

- The analysis uses spatial data (shapefiles, geocoded points, raster, network ties) whose provenance and processing are not documented
- A referee asks "can this be reproduced?" and the answer is currently no
- You are deciding what to share given JEG's policy and any confidentiality constraints
- Spatial joins, projections, and unit-boundary versions were done interactively and are not scripted

## What JEG actually requires (and what it does not)

JEG's data/code policy is **encouragement-based and triggered after acceptance**, not a mandatory pre-acceptance replication archive (检索于 2026-06；以官网为准). Authors are asked at acceptance whether associated data exist and whether they wish to publish them as supplementary material; ORCID is required at submission. This is a genuine point of difference from QE, AEJ, and the AEA journals, which run a Data Editor reproducibility check before acceptance.

The practical implication: at JEG you are not forced to deposit, but a credible, well-documented package is a strong signal and pre-empts the reproducibility objection. **Build it as if it were required** — referees increasingly expect it, and editors may ask — but understand the timing and the discretion the policy gives you.

## Spatial data is the hard part

Replication in economic geography fails most often on the *spatial* steps, not the regressions. Document them explicitly:

| Spatial element | What to document |
|-----------------|------------------|
| Boundary/shapefile vintage | which year/version of the administrative units (boundaries change; results shift) |
| Projection / CRS | the coordinate reference system used for distance and area calculations |
| Geocoding | source, match rate, and how unmatched records were handled |
| Spatial joins | the exact join logic (point-in-polygon, nearest, buffer radius) |
| Distance / W construction | how the spatial weight matrix and any distance cutoffs were built |
| Raster/aggregation | resolution, zonal-statistic method, and the aggregation to analysis units |

## Confidential and proprietary spatial data

- Geocoded firm or individual data are often confidential and cannot be posted. Provide instead: the **derived analysis file** where licensing allows, the **full code**, a **synthetic or simulated example dataset** so the code runs, and clear access instructions for the restricted source.
- Note any disclosure-avoidance steps (aggregation, rounding) so a reader understands what was changed and why.

## Reproducibility tooling for spatial work

Spatial pipelines drift silently as upstream boundary files, projection libraries, and geocoding services change. Pin the moving parts:

- Record exact versions of the geospatial stack (e.g., GDAL/PROJ, `sf`/`sp`, `geopandas`, PostGIS) — a PROJ upgrade can shift distance calculations.
- Freeze and ship the boundary/shapefile actually used, or its exact source and vintage, rather than assuming a reader can re-download "the" boundaries.
- Set and report random seeds anywhere simulation, bootstrap, or Conley-cutoff resampling enters.
- Cache geocoding results (with match rates) so the pipeline does not silently re-query a changed external API.
- Where a containerized or environment-locked setup (Docker, `renv`, conda env) is feasible, include it — spatial dependencies are the ones most likely to break on another machine.

## Package contents

- [ ] README mapping each table/figure/map to the script that produces it
- [ ] Raw → analysis data pipeline scripted end to end (no manual GIS steps)
- [ ] Spatial provenance documented (boundary vintage, CRS, geocoding, joins, W)
- [ ] Software environment recorded (package/GIS-library versions, seeds)
- [ ] Confidential data handled via derived file + synthetic example + access path
- [ ] A data-availability statement drafted for the post-acceptance step
- [ ] Code runs top-to-bottom on a clean machine and reproduces the headline numbers

## Anti-patterns

- Interactive, unscripted GIS work ("I joined these in QGIS") that no one can reproduce
- Omitting the boundary/shapefile vintage so distances and units cannot be recreated
- Sharing code that calls a confidential file with no synthetic stand-in to run it
- Assuming JEG requires nothing because the policy is post-acceptance — then scrambling at acceptance
- A README that lists files but never maps exhibits to the scripts that build them
- Undocumented projection/CRS so distance-based results cannot be checked

## Worked vignette (illustrative)

A distance-decay result depends on a spatial weight matrix built from 2011-vintage NUTS-3 boundaries, but the boundaries were redrawn in 2016 and the README never says which were used. A reviewer rebuilds W with current boundaries and the decay shifts. The fix: freeze and document the boundary vintage and CRS, ship the W-construction script, and include a synthetic point dataset so the geocoding-and-join pipeline runs end to end even though the real firm coordinates are confidential. The package now reproduces the headline gradient and survives the reproducibility objection at JEG without depositing the restricted data.

## How JEG differs from the AEA/QE model (and why it matters)

It is tempting to import habits from journals with a mandatory Data Editor (QE, AEJ, the AER family), where a package is checked line-by-line *before* acceptance. JEG does not run that gate; the ask comes at acceptance and sharing is encouraged, not enforced. Two practical consequences:

- **Do not under-prepare** on the assumption "JEG doesn't check." Referees increasingly request reproducibility, and a documented spatial pipeline is a credibility signal that pre-empts the "can this be reproduced?" objection during review.
- **Do not over-engineer** to AEA-archive specs at submission time either — the binding work is documenting the *spatial* steps that actually break replication, not formatting to a checklist no one will run pre-acceptance.

The right posture: build a referee-grade package, lead with spatial provenance, and keep the data-availability statement ready for the post-acceptance step.

## Output format

```text
【Journal】Journal of Economic Geography
【Skill】jegeo-replication-package
【Policy understood】post-acceptance, encouragement-based (not pre-acceptance archive)? [Y/N]
【Spatial provenance】boundary vintage / CRS / geocoding / joins / W documented? [Y/N]
【Pipeline】raw→analysis fully scripted, no manual GIS? [Y/N]
【Confidential data】derived file + synthetic example + access path? [Y/N]
【Reproducibility】runs clean and matches headline numbers? [Y/N]
【Next skill】jegeo-referee-strategy
```
