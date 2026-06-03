# External Tools & Resources for ES&T-Style Environmental Science & Engineering

Data sources, instruments, software, and packages useful when preparing an *Environmental Science &
Technology* (ES&T) submission. ES&T is **multidisciplinary**: a submission may be environmental
chemistry, environmental engineering, ecotoxicology/environmental health, atmospheric/aquatic/soil
science, fate–transport modeling, treatment and resource recovery, biogeochemistry, sustainability/
energy, or the science–policy interface. Match tools to your sub-area and design. Check licenses and
current access terms before use, and verify any ES&T-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Analytical chemistry & measurement

| Technique | Typical use | Reporting/QA notes |
|-----------|-------------|--------------------|
| LC-MS/MS, GC-MS, HRMS (Orbitrap/QTOF) | Trace organics, transformation products, suspect/non-target screening | Report LOD/LOQ, recoveries, internal standards, blanks |
| ICP-MS / ICP-OES | Trace metals/metalloids | Certified reference materials (CRMs), spike recoveries |
| IC, TOC/TN analyzers | Ions, dissolved carbon/nitrogen | Calibration range, QC checks |
| FTIR, Raman, XRD, XPS, SEM/TEM-EDS | Surface/solid characterization, nanomaterials | Instrument settings, replicate spectra |
| Sensors / passive samplers | In-situ and time-integrated monitoring | Calibration, sampling rates, field blanks |

QA/QC backbone: method blanks, field blanks, matrix spikes, duplicates, surrogate/internal standards,
calibration curves with reported R², LOD/LOQ, and recovery ranges — reviewers expect these.

## 2. Data sources & reference databases

| Source | Provider | Typical use |
|--------|----------|-------------|
| US EPA (CompTox, ECOTOX, WQP, AQS, TRI) | US EPA | Chemical properties, toxicity, water/air quality, emissions |
| PubChem / ChemSpider / CAS | NIH / RSC / ACS | Chemical identity, properties, CAS RN |
| NIST WebBook / NIST mass-spec libraries | NIST | Thermochemistry, reference spectra |
| MassBank / MoNA / mzCloud | community | Non-target/suspect screening spectral matching |
| GenBank / ENA / SRA, GEO/ArrayExpress | NCBI / EBI | Sequence, omics for environmental microbiology |
| GBIF / WQX / GEMStat | global | Biodiversity, water-quality monitoring |
| Copernicus / NASA Earthdata / MODIS | ESA / NASA | Remote sensing, atmospheric/land products |

## 3. Fate, transport & process modeling

- Multimedia/fate: **EPI Suite**, **SimpleBox**, fugacity (Mackay-type) models
- Aquatic chemistry/speciation: **PHREEQC**, **Visual MINTEQ**, **MINEQL+**
- Reactive transport / hydrology: **HYDRUS**, **MODFLOW/MT3D**, **OpenFOAM** (CFD)
- Atmospheric chemistry/transport: **CMAQ**, **WRF-Chem**, **GEOS-Chem**, **HYSPLIT** (back-trajectories)
- Kinetics/photochemistry: rate-constant fitting, quantum-yield and EE/O reporting for AOPs
- Life-cycle & sustainability: **SimaPro**, **openLCA**, **GREET**; report functional unit + boundaries
- Exposure/risk: **EPA IRIS**, benchmark-dose tools, probabilistic (Monte Carlo) exposure models

## 4. Statistics, cheminformatics & reproducibility

### R
- `tidyverse`, `drc` (dose-response), `survival`, `vegan`/`phyloseq` (community ecology/microbiome)
- `ggplot2` for exhibits; `mixOmics`, `ropls` for multivariate/omics; `nlme`/`lme4` for mixed models

### Python
- `pandas`, `numpy`, `scipy`, `statsmodels`, `scikit-learn`
- `RDKit` (cheminformatics, QSAR descriptors), `matchms`/`pyteomics` (mass spec), `pymatgen`
- `matplotlib`/`seaborn` for figures; pin with `requirements.txt` / `pip freeze`

### Reproducibility
- Environment pinning: `renv.lock` (R), `requirements.txt` / `conda env export` / Docker
- Pipelines: `targets` (R), `snakemake` / `Nextflow`; set and report random seeds
- Deposit code + processed data so the SI and figures can be regenerated (see `est-reporting-and-reproducibility`)

## 5. Figures, structures & the TOC graphic

- Plotting: `ggplot2`, `matplotlib`/`seaborn`, OriginPro, GraphPad Prism
- Chemical structures/schemes: ChemDraw, RDKit, BKChem; reaction/mass-balance schematics
- Maps/spatial: `sf`/`tmap` (R), QGIS, ArcGIS for sampling-site and spatial-variation maps
- **TOC/abstract graphic**: a single clear visual abstract that *illustrates* the paper without
  duplicating a figure — colorblind-safe, legible at small size, vector where possible (see
  `est-figures-and-tables`)

## 6. Reference management & writing

- Reference managers: Zotero, EndNote, Mendeley, BibTeX/BibLaTeX — format to **ACS style**
  (numbered citations; see the ACS Style Quick Guide)
- Typesetting: the ACS Word/LaTeX templates (the `achemso` LaTeX class) or Word; assemble the main
  manuscript + a separate **Supporting Information** PDF
- Provide the **TOC graphic** as a separate file; include a **data-availability statement**

## 7. Submission, ethics & data deposition

| Item | Note |
|------|------|
| Submission portal | **ACS Publishing Center** / **ACS Paragon Plus** — confirm current entry URL |
| Publisher | **American Chemical Society (ACS)** |
| Review model | Editor desk-screen, then typically **three** expert reviewers (reviewer anonymity) |
| Plagiarism screening | **iThenticate / CrossCheck** on submission |
| Data deposition | Public repositories: **Dryad, figshare, Zenodo, OSF**; sequence → **GenBank/ENA/DDBJ**; omics → **GEO/ArrayExpress**; proteomics → **PRIDE/ProteomeXchange**; mass spec → **MassIVE/MetaboLights/MassBank** |
| Data-availability statement | Required; cite accession codes / DOIs |
| Safety | Report unexpected/significant hazards or risks in the Methods |

## 8. Cautions

1. **Verify volatile specifics** (exact word limits, figure word-equivalents, submission-system name,
   blinding model, editor, metrics, APC) on the official ACS/ES&T pages — they change; unverified
   items are marked 待核实.
2. **QA/QC is non-negotiable** — blanks, spikes, recoveries, LOD/LOQ, replicates, and CRMs make or
   break analytical credibility at ES&T.
3. **Close the mass/energy balance** where the design implies one; unexplained losses invite rejection.
4. **Environmental relevance over novelty-of-method** — match concentrations, matrices, and conditions
   to real environmental systems, not just idealized lab spikes.
5. **Build the SI and data deposit as you go** — they are reviewed with the manuscript and expected to
   be public on publication.
