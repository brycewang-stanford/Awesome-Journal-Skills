# External Tools and Data Sources for Nature Geoscience Submissions

This document collects the data sources, repositories, computation, figure, and manuscript tools
commonly used when preparing a Nature Geoscience (Nat. Geosci.) submission. It is a practical
reference; always verify current Nature Geoscience / Nature Portfolio requirements on the official
author pages (Checked: 2026-07-16).

## 1. Earth-system observational and reanalysis data

| Source | Use |
|--------|-----|
| **ERA5 (ECMWF / Copernicus C3S)** | Global atmospheric reanalysis (hourly, 1940–present) — the workhorse for atmosphere/climate diagnostics |
| **MERRA-2 (NASA GMAO)** | Atmospheric reanalysis with aerosol and chemistry fields |
| **ORAS5 / GLORYS / ECCO** | Ocean reanalyses (state estimation) for circulation and heat content |
| **NCEP/NCAR, JRA-55/JRA-3Q** | Alternative atmospheric reanalyses for robustness/spread |
| **HadCRUT / GISTEMP / Berkeley Earth** | Instrumental surface-temperature records |
| **GEBCO** | Global bathymetry and terrain grid (ocean + land elevation) |
| **ETOPO** | Global relief model (topography + bathymetry) |

## 2. Satellite and remote-sensing datasets

| Source | Use |
|--------|-----|
| **NASA Earthdata / DAACs** | MODIS, VIIRS, GRACE/GRACE-FO (mass change), ICESat-2 (elevation), SMAP (soil moisture), OCO-2 (CO2) |
| **Copernicus / Sentinel (ESA)** | Sentinel-1 (SAR/InSAR), Sentinel-2 (optical), Sentinel-3 (ocean/land), Sentinel-5P (trace gases) |
| **USGS EarthExplorer / Landsat** | Long optical record for land-surface and glacier change |
| **Copernicus Marine (CMEMS)** | Ocean color, SST, sea level, sea ice |
| **NSIDC** | Sea-ice concentration/extent, ice sheets, snow |

## 3. Paleoclimate, geochemistry, and solid-Earth data

| Source | Use |
|--------|-----|
| **NOAA NCEI Paleoclimatology / WDS-Paleo** | Ice cores, tree rings, corals, speleothems, marine/lake sediments |
| **PANGAEA** | The community repository for Earth & environmental data (also a deposit target) |
| **EarthChem / GEOROC / PetDB** | Igneous/metamorphic geochemistry compilations |
| **IRIS/SAGE, FDSN** | Seismological waveforms and station metadata |
| **IGSN** | Globally unique sample identifiers for physical specimens (cores, rocks) |

## 4. Climate-model and simulation output

| Source | Use |
|--------|-----|
| **CMIP6 / CMIP7 (ESGF)** | Coupled climate-model output for projections, attribution, intercomparison |
| **PMIP** | Paleoclimate model intercomparison (deep-time / Quaternary experiments) |
| **CESM, MPI-ESM, UKESM, GFDL** | Earth-system models for bespoke simulations |
| **WRF / MPAS / ICON** | Regional and global atmospheric modelling |
| **MOM6 / NEMO / MITgcm** | Ocean general-circulation modelling |

## 5. Geospatial and analysis software stack

### Python
- `xarray`, `dask` — labelled N-D arrays for gridded climate/ocean data at scale
- `numpy`, `scipy`, `pandas` — numerics, statistics, tabular data
- `cartopy`, `matplotlib`, `cmocean`, `cmcrameri` — maps and perceptually-uniform, color-blind-safe colormaps
- `metpy`, `xesmf`, `esmpy` — meteorological calculations and regridding
- `rasterio`, `rioxarray`, `geopandas`, `shapely` — raster/vector GIS
- `pyproj` — projections and coordinate transforms
- `obspy` — seismology; `pyleoclim` — paleoclimate time series

### R
- `terra`, `sf`, `stars` — spatial raster/vector analysis
- `ncdf4` — NetCDF I/O

### Command-line / other
- **CDO**, **NCO** — fast NetCDF operators for climate data
- **GDAL/OGR** — the universal geospatial translator
- **QGIS**, **GMT (Generic Mapping Tools)** — GIS and publication maps
- **Panoply** — quick NetCDF/HDF visualisation
- **Julia** (`Oceananigans.jl`, `ClimateTools.jl`) — high-performance simulation

## 6. Data and code repositories (for the availability statements)

| Repository | Use |
|------------|-----|
| **PANGAEA** | Preferred community repository for Earth & environmental datasets (DOI-minting) |
| **Zenodo** | DOI-minting archive for datasets and code; pairs with a GitHub release |
| **Dryad** | Curated data repository with DOIs |
| **figshare** | Datasets, figures, supplementary files with DOIs |
| **ESSOAr / EarthArXiv** | Earth-science preprint servers (disclose any preprint to the editor) |
| **GitHub / GitLab** | Code hosting; archive a release to Zenodo for a citable code DOI |

State a concrete repository + accession/DOI, not "available on request"; verify current Nature Portfolio
data and code policy and the preferred-repository list.

## 7. Manuscript preparation and references

| Tool | Use |
|------|-----|
| **Overleaf + Springer Nature LaTeX template** | Nature-format authoring; or submit in Word per the current template |
| **Zotero / Mendeley / EndNote** | Reference management; Nature reference style |
| **Nature Portfolio Reporting Summary** | Required submission form — complete it consistently with Methods |
| **Grammarly / LanguageTool** | Grammar/style; but Nature edits substantially for non-specialist accessibility |
| **latexdiff / Word track-changes** | Marked-up manuscript for resubmission |

## 8. Notes

1. **Verify volatile specifics** (word/display-item/reference limits, content types, Reporting Summary,
   portal, APC) on the official Nature Geoscience author pages — they change.
2. **Ground models in observations.** A model result with no data anchor and no uncertainty is a
   classic desk-reject; use reanalysis/satellite/proxy data to validate.
3. **Deposit, don't promise.** Use a community repository (PANGAEA) where possible; mint a DOI for data
   and custom code before submission.
4. **Honest cartography.** State projection, scale, units, and data source; use perceptually-uniform,
   color-blind-safe colormaps (cmocean, cmcrameri/batlow) — never rainbow/jet for quantitative fields.
5. **Reproducibility.** Version datasets and code; keep the Reporting Summary consistent with Methods.
