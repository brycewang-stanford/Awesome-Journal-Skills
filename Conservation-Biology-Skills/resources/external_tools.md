# External Tools & Resources for Conservation Biology

Data sources, software, and packages useful when preparing a *Conservation Biology* submission.
*Conservation Biology* publishes **empirical conservation science** — population, community, and
landscape ecology; extinction risk and population viability; protected-area design and systematic
conservation planning; human-wildlife interactions; and conservation policy and practice — drawing on
both the natural and social sciences. The bar is **direct relevance to the conservation of biological
diversity**, so match every tool to a design that yields actionable inference. Check licenses and
current access terms before use, and verify any journal-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by domain

### Species, occurrence & status
| Source | Provider | Typical use |
|--------|----------|-------------|
| GBIF | Global Biodiversity Information Facility | Species occurrence records, ranges |
| IUCN Red List | IUCN | Extinction-risk status, threats, range maps |
| Map of Life / eBird | MOL / Cornell Lab | Distributions, citizen-science observations |
| Movebank | MPI-AB | Animal tracking / telemetry data |
| TRAFFIC / CITES Trade DB | TRAFFIC / CITES | Wildlife trade and trafficking |

### Habitat, land cover & protected areas
| Source | Provider | Typical use |
|--------|----------|-------------|
| World Database on Protected Areas (WDPA) | UNEP-WCMC / Protected Planet | Protected-area boundaries and attributes |
| Global Forest Watch / Hansen | WRI / UMD | Forest cover and loss |
| Copernicus / Landsat / Sentinel | ESA / USGS | Remote-sensing land cover and change |
| WorldClim / CHELSA | — | Climate layers for niche/SDM work |
| Human Footprint / GHSL | WCS / JRC | Anthropogenic pressure, human population |

### Socio-economic & policy
| Source | Provider | Typical use |
|--------|----------|-------------|
| LSMS / DHS surveys | World Bank / USAID | Livelihoods near conservation areas |
| Governance indicators (WGI, QoG) | World Bank / U. Gothenburg | Policy and institutional context |
| Conservation-intervention databases (Conservation Evidence) | U. Cambridge | What works in conservation |

## 2. Software by method

### R (dominant in ecology and conservation)
- Spatial / SDM: `sf`, `terra`, `dismo`, `sdm`, `ENMeval`, `biomod2`, `spThin`
- Population / demography: `popbio`, `unmarked` (occupancy/N-mixture), `RMark`/`marked` (capture-recapture), `secr` (spatial capture-recapture), `vortexR` (PVA post-processing)
- Mixed / hierarchical models: `lme4`, `glmmTMB`, `brms`, `nimble`/`rstan` (Bayesian), `INLA`
- Systematic planning: `prioritizr`, `Marxan`/`marxan` workflows, `zonator` (Zonation)
- Meta-analysis / synthesis: `metafor`, `revtools` (screening), `PRISMA2020`
- Trends / monitoring: `rtrim`, `mgcv` (GAMs), `TMB`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Python
- `pandas`, `numpy`, `geopandas`, `rasterio`, `scikit-learn`, `statsmodels`
- SDM / ML: `pyimpute`, `elapid`, gradient-boosting / random-forest libraries
- `matplotlib` / `seaborn` / `plotnine` for exhibits; pin with `requirements.txt`

### GIS & remote sensing
- QGIS, GRASS, Google Earth Engine (large-area land-cover change), R `terra`/`sf`
- Marxan / Zonation for spatial prioritization; Circuitscape for connectivity

## 3. Study design, power & synthesis
- Design: BACI / before-after-control-impact, control-impact, space-for-time; occupancy and
  distance-sampling design (`unmarked`, `Distance`); camera-trap / eDNA survey planning
- Power / sample size: simulation-based power for occupancy, capture-recapture, and trend detection
- Systematic review / evidence synthesis: **PRISMA** flow, Collaboration for Environmental Evidence
  (CEE) guidelines, ROSES reporting; preregistration via **OSF Registries** where applicable
- Population viability analysis: Vortex, RAMAS for extinction-risk projection

## 4. Figures, maps & exhibits (Conservation Biology rewards clear, accessible exhibits)
- Maps for spatial variation and study areas (`ggplot2` + `sf`, `tmap`); inset/locator maps with scale
  bar and projection stated
- Effect / forest plots (`broom` + `ggplot2`), partial-dependence and predicted-probability plots,
  Kaplan-Meier / survival curves, occupancy and abundance plots
- **Mask or coarsen precise locations of threatened species, nests, or trafficked taxa** to avoid
  conservation harm; state that you have done so
- Colorblind-safe palettes; legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the *Conservation Biology* Style
  Guide (the journal uses an author-date style); keep one consistent style
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **double-blind** manuscript
  (no author names/affiliations; neutralize identifying self-references) plus a separate title page
- Respect per-type word limits (counts run from the first word of the Abstract through the last word of
  Literature Cited; tables and figure legends are excluded); keep the abstract within the cap

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Wiley ScholarOne Manuscript Central** (`mc.manuscriptcentral.com/cobi`) |
| Owner / publisher | **Society for Conservation Biology (SCB)** / **Wiley** |
| Review model | **Double-blind** (adopted 2014) — anonymize the manuscript and the authors' identities |
| Article types | Contributed Papers · Research Notes · Reviews · Essays · Conservation Practice and Policy · Comments · Diversity · Letters (plus Registered Reports) |
| Word limits | Contributed Papers 7,000 in current Wiley listings; abstract ≤ 300; final caps for other article types belong to the live Instructions for Authors page |
| Data policy | Data-availability statement required for research/synthesis articles; journal-specific Wiley tier encourages data sharing; archive shareable data/code with a persistent identifier and document restrictions for sensitive data |

## 7. Cautions
1. **Run an upload-week live check** for per-type word/abstract caps, accepted article types,
   declarations, editor/board, APC, and production-file prompts on the official Wiley/SCB pages.
2. **Lead with conservation relevance** — *Conservation Biology* requires results to have **direct
   implications for the conservation of biological diversity**; a sound but inconsequential study is
   off-fit (see `conbio-conservation-relevance-and-implications`).
3. **Anonymize properly** — the journal is **double-blind**; strip author metadata and neutralize
   obvious self-references.
4. **Protect sensitive data** — mask precise locations of threatened, exploited, or trafficked taxa;
   explain how, and provide an access path for restricted data.
5. **Use modern ecological-inference tools** — account for detection (occupancy/distance sampling),
   spatial autocorrelation, and pseudoreplication; do not over-generalize from one site or short series.
6. **Build the data/code package as you go** — even when sharing is restricted, the manuscript needs a
   data-availability statement and a defensible access or masking plan (see
   `conbio-reporting-and-data-policy`).
