# External Tools & Resources for GCB-Style Global-Change Biology

Data sources, software, and packages useful when preparing a *Global Change Biology* (GCB) submission.
GCB studies **mechanistic links between global environmental change and biological systems** — climate
change, rising CO2 / tropospheric ozone, nitrogen deposition, land-use change, warming, drought, and
ocean change — across any level of organization from **molecular to biome**, in **aquatic or
terrestrial**, **managed or natural** systems. Match tools to your system and design. Check licenses and
current access terms before use, and verify any GCB-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by domain

### Climate, atmosphere & drivers
| Source | Provider | Typical use |
|--------|----------|-------------|
| ERA5 / ERA5-Land reanalysis | ECMWF / Copernicus (C3S) | Gridded temperature, precipitation, radiation forcing |
| WorldClim / CHELSA | WorldClim / WSL | Bioclimatic layers for niche & distribution models |
| CMIP6 / CMIP5 | ESGF / WCRP | Climate-model projections, scenario (SSP/RCP) forcing |
| TerraClimate / CRU TS | U. Idaho / UEA | Long-run climate water balance, drought indices |
| NOAA GML / Mauna Loa | NOAA | Atmospheric CO2, trace-gas concentrations |

### Ecosystems, carbon & biogeochemistry
| Source | Provider | Typical use |
|--------|----------|-------------|
| FLUXNET / AmeriFlux / ICOS | FLUXNET community | Eddy-covariance CO2/H2O/energy fluxes, GPP/NEE/ET |
| MODIS / Landsat / Sentinel | NASA / USGS / ESA | Phenology, LAI, NDVI/EVI, land cover, disturbance |
| SoilGrids / ISRIC / WoSIS | ISRIC | Soil carbon, texture, profiles |
| Global Carbon Project / TRENDY | GCP | Carbon budgets, terrestrial model ensembles |
| ForC / Global Forest Watch | various | Forest carbon stocks/fluxes, deforestation |

### Biodiversity, species & traits
| Source | Provider | Typical use |
|--------|----------|-------------|
| GBIF | GBIF | Species occurrence records (distribution/range shifts) |
| TRY Plant Trait Database | TRY consortium | Functional traits for trait-based ecology |
| BIEN / sPlot | BIEN / iDiv | Vegetation plots, ranges, community composition |
| OBIS | OBIS | Marine biodiversity occurrence |
| PhenoCam / NPN | PhenoCam / USA-NPN | Ground phenology observations |

## 2. Software by method

### R (dominant in global-change ecology)
- Spatial / climate: `terra`, `sf`, `stars`, `exactextractr`, `climateR`
- Species distribution / niche: `dismo`, `biomod2`, `ENMeval`, `sdm`, `flexsdm`
- Mixed / hierarchical models: `lme4`, `glmmTMB`, `nlme`, `brms`, `INLA`
- Time series / phenology / trends: `phenex`, `greenbrown`, `bfast`, `mgcv` (GAMs)
- Meta-analysis (common in GCB syntheses): `metafor`, `orchaRd`
- Multivariate community ecology: `vegan`, `mvabund`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Python
- `xarray`, `netCDF4`, `dask` for gridded climate/Earth-observation cubes
- `rioxarray`, `geopandas`, `rasterio` for geospatial work
- `scikit-learn`, `statsmodels`, `pandas`, `numpy`; `scikit-image` for remote-sensing
- Process/ecosystem modelling and ML emulators; pin with `requirements.txt` / `conda` env export

### Process & ecosystem models
- Land-surface / DGVMs: CLM, JULES, ORCHIDEE, LPJ-GUESS, ED2 (carbon/water/vegetation dynamics)
- Crop / managed systems: APSIM, DSSAT; soil C: RothC, Century/DayCent
- Document model version, forcing, spin-up, and parameterization for reproducibility

## 3. Design, synthesis & uncertainty
- Manipulative experiments: warming (OTC, infrared), eCO2 (FACE), N addition, rainfall manipulation,
  reciprocal transplants — report dose, duration, replication, and realism/extrapolation limits
- Observational/gradient and long-term networks (ILTER, NEON) — confounding and space-for-time caveats
- Meta-analysis / evidence synthesis: PRISMA-style search, effect sizes (log response ratio, Hedges' g),
  heterogeneity, publication-bias checks; report the protocol
- Uncertainty: propagate measurement + model + scenario uncertainty; ensembles over single runs

## 4. Figures & exhibits (GCB rewards mechanism-first, accessible exhibits)
- A **graphical abstract** linking an environmental **driver** to a biological **response** (not a site
  map or phylogeny)
- Driver-response curves, dose-response, partial-effect/marginal plots; maps for spatial pattern (`tmap`,
  `ggplot2` + `sf`); flux/time-series with uncertainty ribbons; forest plots for meta-analysis
- Colour-blind-safe palettes (`viridis`, Okabe-Ito), legible in grayscale; vector output for line art;
  live-check the current resolution and file-format specifications before upload

## 5. Data, code & references
- Archive **data** in a DOI-minting public repository: **Dryad**, **Zenodo**, **PANGAEA** (Earth/
  environmental), Figshare; deposit **code** in **Zenodo** (GitHub release → Zenodo DOI)
- A **data availability statement** is mandatory; **"available on request" is not accepted** — deposit
  before acceptance (see `gcb-reporting-and-data-policy`)
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote; GCB uses an author-date style — keep one
  consistent style and confirm the current template

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne / Manuscript Central** (`mc.manuscriptcentral.com/gcb`) — confirm current URL |
| Publisher | **Wiley** |
| Review model | Editor-mediated expert review; live-check current anonymity / transparent-review options |
| Article types | Research Articles · Technical Advances · Reviews · GCB Reviews · Mini Reviews · Opinions · Perspectives |
| Length | Research Articles currently route to **up to 8,000 words**; abstract **300 words**; 6–10 keywords or phrases |
| Graphical abstract | **Required** — driver-to-response mechanism |
| Data / code policy | Archive data + code in a public repo with a **DOI** as a condition of publication |

## 7. Cautions
1. **Verify volatile specifics** (word/abstract caps, article types, fee/APC, data-policy wording, review
   model) on the official Wiley page immediately before submission.
2. **Lead with mechanism and global-change significance** — GCB wants the causal link between a driver and
   a biological response, not a local description or a conservation action plan.
3. **Match scale and inference** — manipulative, observational/gradient, and modelling designs each have
   their own extrapolation limits; state them.
4. **Archive data and code as you go** — deposit with a DOI before publication; "available on request" is
   rejected.
5. **Quantify uncertainty** — propagate measurement, model, and scenario uncertainty; prefer ensembles to
   single runs.
