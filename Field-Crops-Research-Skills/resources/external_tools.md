# External Tools & Resources for FCR-Style Field Crops Research

Data sources, software, and packages useful when preparing a *Field Crops Research* (FCR) submission.
FCR is an **empirical agronomy and crop-science** journal: a submission is typically a **field-based**
experimental or modelling study on crop ecology, crop physiology, agronomy, or crop improvement, with
**multi-season and/or multi-environment** relevance and, usually, **yield data**. Match tools to your
design — controlled-environment-only work is out of scope (see `fcr-topic-selection`). Check licenses
and current access terms before use, and check any FCR-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources & reference datasets

| Source | Provider | Typical use |
|--------|----------|-------------|
| Global Yield Gap Atlas (GYGA) | UNL / WUR | Yield-gap benchmarking against water-limited / potential yield |
| FAOSTAT | FAO | National/regional crop area, yield, production context |
| WorldClim / CHELSA | Research consortia | Gridded climate covariates for environment characterisation |
| NASA POWER / ERA5 | NASA / ECMWF | Daily weather (radiation, temperature, rainfall) for modelling and phenology |
| SoilGrids / ISRIC | ISRIC | Soil properties for site characterisation |
| GenStat / IRRI variety & MET archives | VSN / IRRI | Multi-environment trial (MET) reference data |
| Genesys / GRIN | Crop Trust / USDA | Germplasm and genetic-resource passport data |

## 2. Experimental design & field data

- **Design**: `agricolae` (R: RCBD, split-plot, lattice, augmented designs, AMMI), `FielDHub`
  (interactive field layouts), `desplot` (visualise field plot maps), GenStat / CycDesigN for
  resolvable incomplete-block and alpha designs
- **Capture / metadata**: ICASA / AgMIP data standards; Crop Ontology; document plot dimensions,
  randomization, replication, sowing/harvest dates, management, and weather in relation to phenology
- **Phenotyping / sensing**: tools for canopy reflectance, NDVI, UAV/remote-sensing pipelines —
  integrate with agronomy/physiology, not as stand-alone (per FCR scope)

## 3. Statistics & modelling

### R (widely used in agronomy)
- Mixed models for MET / G×E: `lme4`, `nlme`, `asreml-R` (commercial), `sommer`, `statgenSTA` /
  `statgenGxE`, `metan` (AMMI, GGE, stability), `agriCensData`
- Spatial field-trial models: `SpATS` (P-spline spatial analysis), `breedR`
- Means separation / contrasts done properly: `emmeans` (estimated marginal means), `multcomp`
- Repeated-measures / nonlinear growth: `nlme`, `growthrates`, dose-response `drc`
- Meta-analysis of published trials: `metafor`

### Crop simulation models
- **APSIM**, **DSSAT**, **STICS**, **CROPGRO/CERES**, **WOFOST**, **AquaCrop** — yield-gap decomposition,
  scenario analysis, G×E×M; report version, cultivar coefficients, calibration/validation split

### Python / other
- `pandas`, `numpy`, `statsmodels`, `pymc` (Bayesian), `scikit-learn` for ML-assisted analysis;
  `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt`
- Stata: `mixed` / `meglm` for mixed models; `margins` for adjusted means

## 4. Figures & exhibits (FCR rewards clear agronomic exhibits)

- Yield vs. environment-index (Finlay–Wilkinson) plots; AMMI biplots and GGE biplots for G×E
- Boundary-line / yield-gap plots; response curves (N, water, density) with fitted models and CIs
- Time-series of crop development against thermal time / phenology with weather overlays
- Colourblind-safe palettes; legible in grayscale; vector output (PDF/EPS) for print; show **SE/SED or
  LSD and units** on every exhibit

## 5. Writing & references
- Reference managers: Zotero, Mendeley, BibTeX/BibLaTeX, EndNote — use the **Elsevier / FCR reference
  style** (Elsevier numbered or name–year as specified); keep one consistent style
- Typesetting: LaTeX (Elsevier `elsarticle` class) or Word; prepare **highlights** (3–5 bullets,
  ≤ 85 characters each) and an **abstract ≤ 400 words**
- Reporting: SI units; full agronomic detail (cultivar, soil, weather, management, plot size,
  replication) so the experiment is reproducible

## 6. Process & portal

| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** at `submit.elsevier.com/FIELD` |
| Publisher | **Elsevier** (ISSN **0378-4290**) |
| Review model | **Single anonymized** — typically ≥ 2 reviewers |
| Article types | Original Research Paper · Review (usually invited) · Short Communication · Opinion · Loomis Review (invited) |
| Multi-environment rule | Field experiments should include **≥ 2 seasons and/or multiple locations/environments** |
| Abstract / highlights | Abstract **≤ 400 words**; **3–5 highlights**, each **≤ 85 characters** |
| Data policy | Elsevier Policy Type 3 / Option C: **state data availability at submission**; co-submit data/methods to **Data in Brief / MethodsX** where relevant |
| AI disclosure | **Declare any use of generative AI** in preparation |
| Open access | Optional OA APC shown by ScienceDirect: **USD 3,500** excluding taxes; subscription route has no open-access publication fee |

## 7. Cautions
1. **Scope first** — FCR rejects controlled-environment-only (greenhouse/pot/root-restricting) work,
   horticultural/woody-perennial/non-cultivated species, and corroborative/descriptive/local-only
   studies. Confirm fit before investing (see `fcr-topic-selection`).
2. **Multi-environment relevance** — a single-site, single-season trial usually does not meet the bar;
   design for **≥ 2 seasons and/or multiple environments** and analyse **G×E** properly.
3. **Use the right statistics** — mixed models for MET / block-design / split-plot data; report **SED/LSD**
   and estimated marginal means, not bare means with stars.
4. **Document the agronomy** — cultivar, soil, weather (linked to phenology), and management must let a
   reader reproduce the experiment.
5. **Run an upload-week live check** on the official Elsevier pages for editor names, prices, file
   prompts, and article-type menus before pressing submit.
