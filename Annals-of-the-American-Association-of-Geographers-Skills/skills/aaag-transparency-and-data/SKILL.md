---
name: aaag-transparency-and-data
description: Use when handling data documentation, sharing, and spatial-data ethics for an Annals of the American Association of Geographers manuscript — provenance (sources, projections, processing), reproducibility, and geoprivacy / human-subjects protection. Prepares documentation; it does not over-state a verification gate the policy does not impose.
---

# Transparency & Spatial Data (aaag-transparency-and-data)

The Annals (Taylor & Francis, for the AAG) follows publisher and disciplinary norms for **data
availability and research integrity** rather than (as at some journals) a mandatory, editor-run
replication check before publication. The right posture is: **document spatial-data provenance
thoroughly, share what you ethically can, and protect location privacy.** Confirm the current data-
availability / sharing policy on the Taylor & Francis journal page (检索于 2026-06；以官网为准).

## When to trigger

- Preparing data documentation, a data-availability statement, or supplementary materials
- Deciding what spatial data can be shared given geoprivacy, IRB, license, or proprietary limits
- Documenting qualitative or restricted location data so claims remain credible
- A reviewer asked how others could verify or reproduce the spatial analysis

## Spatial-data provenance (the geography-specific core)

Document enough that another geographer could locate, re-project, and rebuild the dataset:

- **Sources & licenses** for every layer (census, satellite, OSM, administrative, field-collected),
  with access dates and terms.
- **Projection / CRS** and any re-projection; **areal units** and how they were defined or aggregated.
- **Processing chain** — classification, geocoding, spatial joins, resampling, filtering — as a logged,
  ordered pipeline, not "cleaned in GIS."
- **Temporal alignment** — vintages of layers and how they were harmonized.

## Geoprivacy & human subjects (overrides sharing)

- **Do not publish precise locations** of identifiable individuals/households; use geographic masking
  (aggregation, jittering, areal reporting) and state the method.
- IRB/consent for interviews, fieldwork, and participatory mapping; protect informant and site identity.
- Sensitive sites (sacred, endangered-species, conflict) may require deliberate spatial coarsening — say so.

## Reproducibility (good practice even without a pre-publication gate)

- **Master script** regenerates every table, figure, and map from raw/constructed data.
- **README/codebook**: provenance, projections, construction steps, and how to reproduce each exhibit.
- **Seeds** set for stochastic steps; software/package **versions pinned** (`renv.lock` / `requirements.txt`).
- Restricted data: a **data-availability statement** explaining what is shared, what is not and why,
  and an **access path**; provide **synthetic/masked data** so code can run where feasible.

## Transparency posture by data type (geography-specific)

Because the Annals spans four areas, the *availability* expectation lands differently on different
evidence. This grid keeps the posture honest; confirm mechanics against the current T&F policy.

| Data type | Typically shareable | Restricted | Provenance to document |
|-----------|---------------------|------------|------------------------|
| Public geospatial (census, OSM) | data + code | none | source, vintage, CRS, join keys |
| Satellite / DEM | processing code + IDs | bulk imagery (host link instead) | sensor, dates, correction, resolution |
| Field GPS of people/sites | masked/aggregated data | exact coordinates | masking method, IRB, consent |
| Interviews / ethnography | coding scheme | identifiable transcripts/locations | anonymization, composite-disclosure note |
| Proprietary/licensed layers | code + access path | the layer itself | license terms, how to obtain |

## Checklist

- [ ] Every layer's source, license, access date, and CRS documented
- [ ] Processing pipeline logged (classification/geocoding/joins/resampling)
- [ ] Geoprivacy handled — masking method stated for identifiable locations
- [ ] IRB/consent documented for human-subjects and field/participatory work
- [ ] Master script + README + seeds + pinned versions (where quantitative)
- [ ] Data-availability statement drafted; access path / synthetic data for restricted layers
- [ ] Current T&F data policy confirmed (do not assert a gate it does not impose)

## Anti-patterns

- "Data cleaned in GIS" with no provenance, CRS, or processing log
- Publishing exact coordinates of vulnerable people or sensitive sites
- Claiming open data that license or geoprivacy will not permit
- Asserting an editor-verified replication mandate the policy does not state
- Un-seeded, unpinned code that "works on my machine"

## Output format

```
【Provenance】sources + licenses + CRS + processing log documented? [Y/N]
【Geoprivacy】masking/aggregation for identifiable locations? [Y/N/NA]
【Human subjects】IRB/consent handled? [Y/N/NA]
【Reproducibility】master script + README + seeds + versions? [Y/N]
【Data-availability statement】shared / restricted (why) / access path / synthetic?
【Policy check】current T&F data policy confirmed? [Y/N/待核实]
【Next】aaag-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling, repositories, and geomasking options
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — T&F data-availability and AAG ethics references
