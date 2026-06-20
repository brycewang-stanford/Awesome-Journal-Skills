# External Tools & Resources for Annals-of-the-AAG-Style Geography

Data sources, software, and packages useful when preparing an *Annals of the American Association of
Geographers* submission. The Annals is a **four-area, method-plural** geography journal: a submission may
be spatial-quantitative / GIScience, remote-sensing / physical-environmental, qualitative human
geography, or nature-society mixed methods. Match tools to your area and design. Check licenses and
current access terms before use, and verify any Annals-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by area

### Human geography & nature-society (people, places, environment-society)
| Source | Provider | Typical use |
|--------|----------|-------------|
| US Census / ACS (via tidycensus, data.census.gov) | US Census Bureau | Demographic, socioeconomic, tract/block-group geographies |
| IPUMS (USA / International / NHGIS) | University of Minnesota | Harmonized micro + historical boundary GIS |
| Global Human Settlement Layer (GHSL) | EC JRC | Built-up area, population grids |
| WorldPop / Gridded Population of the World | WorldPop / CIESIN | Gridded population for the Global South |
| OpenStreetMap (Overpass, osmnx) | OSM community | Streets, POIs, building footprints |
| EJSCREEN / CDC SVI | US EPA / CDC | Environmental justice, social vulnerability |

### Physical geography, earth & environmental + remote sensing
| Source | Provider | Typical use |
|--------|----------|-------------|
| Landsat / Sentinel (via Earth Engine, USGS EarthExplorer, Copernicus) | USGS / ESA | Multispectral imagery, land cover, change |
| MODIS / VIIRS | NASA | Daily-scale land surface, fire, vegetation |
| SRTM / ASTER GDEM / Copernicus DEM | NASA / ESA | Terrain, hydrology, geomorphometry |
| ERA5 / CHIRPS / Daymet | ECMWF / UCSB / ORNL | Climate reanalysis and precipitation |
| GBIF / species occurrence | GBIF | Biogeography, species distribution models |
| NLCD / ESA WorldCover / Dynamic World | USGS / ESA / Google | Land-cover baselines and validation |

### Cross-cutting
| Source | Provider | Typical use |
|--------|----------|-------------|
| Natural Earth / GADM | Natural Earth / GADM | Base maps and administrative boundaries |
| Google Earth Engine catalog | Google | Petabyte-scale geospatial archive + compute |

## 2. Software by method

### Spatial analysis & statistics
- **R**: `sf`, `terra`/`stars`, `spdep` (Moran's I, spatial lag/error), `spatialreg`, `GWmodel`/`mgwr`
  (GWR/MGWR), `gstat` (kriging), `spatialsample`/`blockCV` (spatial cross-validation), `INLA` (spatial Bayesian)
- **Python**: `geopandas`, `rasterio`, `xarray`/`rioxarray`, `PySAL` (esda, spreg, libpysal), `mgwr`,
  `pyproj`, `rasterstats`, `scikit-learn` + `spatial CV`
- **GIS desktop**: QGIS (open source), ArcGIS Pro; GRASS GIS for terrain/hydrology

### Remote sensing & physical
- **Google Earth Engine** (JavaScript/Python API) for large-area classification and time series
- **Python**: `rasterio`, `rio-xarray`, `scikit-image`, `eo-learn`, `torchgeo`; SNAP for Sentinel
- Accuracy/validation: confusion-matrix and area-adjusted accuracy workflows (Olofsson et al. practice)

### Qualitative & mixed-methods (human geography)
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, documents, fieldnotes
- Participatory / PPGIS: Maptionnaire, KoBoToolbox, ODK for field data collection
- Discourse/text-as-data: `quanteda`, `spaCy`, topic models where appropriate

## 3. Cartography & figures (held to cartographic standard here)
- Map making: QGIS, `tmap`/`ggplot2`+`sf` (R), `geoplot`/`matplotlib`+`contextily` (Python), ArcGIS Pro
- Classification (choropleth): `classInt` (R), `mapclassify` (Python) — name the method and class count
- Color: ColorBrewer / `cmocean` / `viridis` — colorblind-safe, grayscale-legible; match scheme to data type
- Output: vector (PDF/EPS/SVG) for line art; high-resolution raster for imagery; follow the Graphics Guidelines

## 4. Reproducibility, provenance & geoprivacy
- Pin versions: `renv` (R), `conda`/`requirements.txt` (Python); pipelines: `targets`, `snakemake`
- Repositories: Zenodo, OSF, Figshare, Dryad for data/code with DOIs (verify the Annals' current preference)
- Geomasking / privacy: aggregation, areal reporting, donut/Gaussian masking for identifiable point data
- Document CRS/projection, source licenses, access dates, and the full processing chain

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **Chicago Manual of Style
  (author-date)** house style; keep one consistent style
- Typesetting: LaTeX (TeX Live / Overleaf) or Word; prepare a **double-anonymous** manuscript plus a
  separate title page; include 3-5 italicized, alphabetized keywords at the end of the abstract

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne Manuscripts** (via the Taylor & Francis journal page) |
| Owner / publisher | **AAG** / **Taylor & Francis (Routledge)** |
| Review model | **Double-anonymous**; 1-3 referees (one editor/designate); Commentary Responses single-anonymous |
| Areas | Geographic Methods · Human Geography · Nature and Society · Physical Geography, Earth & Environmental · General Geography |
| Article length | Article **≤ 11,000 words** (inclusive); Forum ≤ 25,000; Commentary < 2,000 |
| Style | **Chicago Manual of Style** (author-date); 3-5 italicized keywords |
| Data policy | Follow Taylor & Francis editorial policies + AAG ethics; document provenance + geoprivacy (verify) |

## 7. Cautions
1. **Verify volatile specifics** (editors/terms, exact caps, abstract length, fee/APC, data policy,
   Graphics Guidelines) on the official AAG/Taylor & Francis pages — they change; unverified items are 待核实.
2. **Take space seriously** — spatial autocorrelation, MAUP/scale, projection, and validation are design
   issues, not afterthoughts.
3. **Match method to area** — the Annals judges spatial-quant, remote-sensing, qualitative, and
   nature-society work on its own terms; do not force one template.
4. **Hold maps to cartographic standard** — projection, classification, legend, source, accessibility.
5. **Protect location privacy** — mask identifiable points and sensitive sites; document why.
