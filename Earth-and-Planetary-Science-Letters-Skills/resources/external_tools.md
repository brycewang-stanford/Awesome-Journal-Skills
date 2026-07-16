# External Tools & Resources for EPSL-Style Earth & Planetary Science

Repositories, databases, and software commonly used when preparing an *Earth and Planetary Science
Letters* (EPSL) submission. EPSL spans geochemistry, geophysics, geochronology, geodynamics,
petrology, paleomagnetism, and planetary interiors — match the tooling to your sub-field. Licenses
and access terms change; verify before relying on any of them, and confirm journal policy in
[`official-source-map.md`](official-source-map.md).

## 1. FAIR data repositories (deposition targets)

| Repository | Data type | Notes |
|------------|-----------|-------|
| **EarthChem Library** | geochemical / isotopic datasets | NSF-supported; per-dataset DOIs; the community standard for geochemistry |
| **PANGAEA** | Earth & environmental observational data (marine, paleoclimate, field campaigns) | editor-curated, DOI-issuing, FAIR-aligned |
| **IRIS / EarthScope** | seismic waveforms, station metadata, derived products | cite network/dataset DOIs |
| **MagIC** | paleomagnetic and rock-magnetic data | the designated archive for the paleomag community |
| **NASA PDS** (and ESA PSA) | planetary mission data and derived products | cite bundle, instrument, and version |
| **Zenodo / GitHub+Zenodo** | code, model configurations, reduction scripts | archive a released version with a DOI, not a live repo URL |
| **CSDCO / SESAR** | core material and sample registration (IGSN) | IGSNs make samples citable and traceable |

## 2. Reference databases (positioning & compilation)

| Source | Use for |
|--------|---------|
| **GEOROC** | global igneous-rock geochemistry compilations |
| **PetDB** | ocean-floor rock and mineral chemistry |
| **EarthChem Portal** | federated search across geochemical databases |
| **USGS geochronology & NAVDAT** | dated volcanic/plutonic records |
| **Global CMT, ISC catalogs** | earthquake source parameters |
| **Macrostrat** | stratigraphic and rock-record context |
| **PDS Geosciences Node** | gravity, topography, spectroscopy for planetary bodies |

## 3. Geochronology & isotope tooling

- **IsoplotR** (R / web) — isochrons, concordia, weighted means, MSWD; the standard reduction/plot kit
- **ET_Redux** — U-Pb ID-TIMS data reduction with full uncertainty propagation (tracer, decay constants)
- **iolite / LADR** — LA-ICP-MS session reduction, downhole corrections
- **Squid/Prawn (SHRIMP)**, **ArArCALC** (Ar-Ar), **HeFTy / QTQt** (thermochronology inverse models)
- **CRONUS / CREp calculators** — cosmogenic-nuclide exposure ages and erosion rates
- **Bchron / Bacon / astrochron** (R) — Bayesian age–depth models and astrochronology
- Community norms: report σ-level, reference materials with values used, decay constants with
  citations — see `epsl-data-analysis`.

## 4. Geophysics & geodynamics

- **ObsPy** (Python) — waveform handling, instrument response, catalogs
- **SPECFEM3D**, **AxiSEM** — seismic wave propagation; **SES3D / tomography kits** for inversion
- **ASPECT**, **CitcomS**, **Underworld** — mantle-convection and lithosphere dynamics codes
- **PyGIMLi / SimPEG** — general geophysical inversion frameworks (with resolution diagnostics)
- **GPlates / pyGPlates** — plate reconstructions and paleogeography
- **Generic Mapping Tools (GMT) / PyGMT** — maps, cross-sections, grids; the field's plotting lingua franca

## 5. Petrology, mineral physics & phase equilibria

- **MELTS / alphaMELTS / rhyolite-MELTS** — melting and crystallization thermodynamics
- **Perple_X / THERMOCALC / Theriak-Domino** — phase-diagram and pseudosection computation
- **BurnMan** (Python) — mineral-physics EOS modeling for interior structure
- Experimental-petrology reporting: pressure calibration, run durations, demonstration of
  equilibrium (reversals/time series) — see `epsl-study-design`.

## 6. Statistics, reproducibility & general scientific computing

- Python: `numpy`, `scipy`, `pandas`, `xarray`, `matplotlib`, `cartopy`, `emcee`/`PyMC` (Bayesian
  inference), `cmcrameri` (perceptually uniform, colorblind-safe colormaps — use these instead of jet)
- R: `tidyverse`, `IsoplotR`, `astrochron`, `provenance`
- Environment pinning: `requirements.txt` / `conda env export` / `renv.lock`; containerize long
  pipelines; set and report seeds for MCMC/bootstrap steps
- The regeneration test: deposited data + archived scripts must rebuild every figure and headline
  number (see `epsl-reporting-and-reproducibility`)

## 7. Writing, references & submission mechanics

| Item | Note |
|------|------|
| Submission system | **Editorial Manager** (Elsevier) — entry via the ScienceDirect journal page |
| Templates | Elsevier Word guidance / `elsarticle` LaTeX class |
| References | journal author–date house style; managers: Zotero, Mendeley, BibTeX (re-check the current CSL/style file) |
| Declarations | competing interests, CRediT roles, funding, generative-AI use (Elsevier policy) |
| Identifiers | ORCID for the corresponding author; IGSN for samples where applicable |

## 8. Cautions

1. **Re-check volatile specifics** — the letters word cap, highlights requirement, reference
   formatting, editor roster, and any open-access fee — on the official Elsevier/EPSL pages; this
   pack flags them "re-check" rather than asserting stale values.
2. **Deposit in the community archive, not a catch-all** — a geochemist expects EarthChem, a
   seismologist IRIS/EarthScope, a paleomagnetist MagIC; a generic upload reads as evasion.
3. **Uncertainty budgets are the currency** — internal vs external vs systematic terms, σ-levels
   defined, MSWD interpreted; an undefined ± will draw a referee query at minimum.
4. **Never present smoothed models as observations** — inversions ship with resolution tests.
5. **Version the constants** — decay constants, reference-material values, and velocity models are
   community-revised; cite the values used so your numbers stay portable.
