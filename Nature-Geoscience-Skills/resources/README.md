# Nature Geoscience Resources

Action-oriented resources for the Nature Geoscience (Nat. Geosci.) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model a Nature-style "Here we show" abstract + opening,
benchmark against well-known Earth-science advances, and find the right data sources and repositories.
Pair each with the relevant `skills/ngeo-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a Nature Geoscience **abstract + opening** in house style (one Earth-system advance, "Here we show," accessible to non-specialists, quantified uncertainty, within the ~3,000-word / ~200-word-abstract limits). Illustrative **fictional** study — no real-paper facts, no invented policy. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **well-known Earth-science advances** organized by subfield × evidence type. Design positioning only — coarse citations, no fabricated numbers; community-journal siblings explicitly excluded. |
| [`external_tools.md`](external_tools.md) | Earth-science data sources (reanalysis, satellite, proxy), repositories (PANGAEA / Zenodo / Dryad / Figshare), and the geospatial + climate-model software stack, plus where to confirm **live** Nature Geoscience limits and policy. |
| [`official-source-map.md`](official-source-map.md) | The real official Nature Geoscience / Nature Portfolio URLs behind every hard fact in this pack, with a checked date. |

## Authoritative source

Nature Geoscience policy (word/display-item/reference limits, content types, the online Methods
requirement, the Nature Portfolio Reporting Summary, data/code availability, and the submission portal)
is **volatile** and lives on the **official author pages** — `nature.com/ngeo` — not duplicated here.
Always verify the current limit and requirements there before submitting; the in-pack skills
([`ngeo-length-management`](../skills/ngeo-length-management/SKILL.md),
[`ngeo-submission`](../skills/ngeo-submission/SKILL.md),
[`ngeo-methods`](../skills/ngeo-methods/SKILL.md)) each repeat this "verify on the author page" caveat.
See [`official-source-map.md`](official-source-map.md) for the entry points.

## No vendored analysis-code kit (by design)

Unlike the economics packs in this repo, this pack has **no `code/` kit** — the econometrics code kit
(Stata + Python DID/IV/RDD pipelines) that ships with this repository's economics packs is
**deliberately not vendored** here, because it has no purchase on Earth-system science. Earth-system
research spans field geochemistry, seismology, remote sensing, paleoclimate, oceanography, and
Earth-system modelling; a single fixed pipeline is **not discipline-appropriate**.
[`external_tools.md`](external_tools.md) instead points to the domain data sources and the open
geospatial/climate software stack (xarray, Iris, CDO, GDAL/QGIS, CMIP output) that authors actually use.
The action layer for Nature Geoscience is editorial and structural — framing the one broad-interest
advance, grounding it in data with quantified uncertainty, and fitting the Article container — which the
`skills/` plus the resources above already cover.

## Suggested workflow

1. **Gate the result first** with [`../skills/ngeo-scope-fit`](../skills/ngeo-scope-fit/SKILL.md): is it a
   broad Earth-system advance with quantitative grounding? If not, retarget to a community journal.
2. **Frame the one advance** with
   [`../skills/ngeo-results-framing`](../skills/ngeo-results-framing/SKILL.md) and polish prose with
   [`../skills/ngeo-writing-style`](../skills/ngeo-writing-style/SKILL.md); model the abstract + opening on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
3. **Ground and fit** with [`../skills/ngeo-methods`](../skills/ngeo-methods/SKILL.md),
   [`../skills/ngeo-length-management`](../skills/ngeo-length-management/SKILL.md), and
   [`../skills/ngeo-supplementary`](../skills/ngeo-supplementary/SKILL.md); source data and repositories
   from [`external_tools.md`](external_tools.md).
4. **Benchmark** your subfield × evidence type against
   [`exemplars/library.md`](exemplars/library.md); make the editorial case with
   [`../skills/ngeo-cover-letter`](../skills/ngeo-cover-letter/SKILL.md) and run the final check with
   [`../skills/ngeo-submission`](../skills/ngeo-submission/SKILL.md).
5. **Confirm live policy** (limits, Reporting Summary, content types) on the official author pages — see
   [`official-source-map.md`](official-source-map.md).
