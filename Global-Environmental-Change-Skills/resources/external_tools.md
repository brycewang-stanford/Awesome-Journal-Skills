# External Tools & Resources for GEC-Style Research

Data sources, software, and packages useful when preparing a *Global Environmental Change* (GEC)
submission. GEC is an **interdisciplinary, social-science-leading** journal on the **human and policy
dimensions** of global environmental change: a submission may be quantitative, qualitative, or
mixed-methods, drawing on environmental social science, human geography, political ecology, economics,
sociology, public policy, and socio-ecological systems science. Match tools to your question and
method, not the other way round. Check licenses and current access terms before use, and verify any
GEC-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Data sources by theme

### Climate, vulnerability & adaptation
| Source | Provider | Typical use |
|--------|----------|-------------|
| IPCC reports & WGII data | IPCC | Synthesis of climate impacts, adaptation, vulnerability framings |
| ND-GAIN Country Index | Notre Dame | Cross-country vulnerability and readiness to adapt |
| EM-DAT | CRED, UCLouvain | Disaster losses, exposure, displacement |
| Climate projections (CMIP/CORDEX) | WCRP | Hazard/exposure layers to pair with social data |

### Environmental governance, policy & behavior
| Source | Provider | Typical use |
|--------|----------|-------------|
| World Values Survey / EVS | WVS Association | Environmental attitudes, values, behavior |
| ESS / Eurobarometer | ESS ERIC / EC | Climate concern, policy support in Europe |
| ENVIPOLCON / CCLW climate-laws | LSE Grantham | Climate legislation and policy adoption |
| OECD Environment / EPI | OECD / Yale-Columbia | Policy indicators, environmental performance |

### Land, food, water, oceans & socio-ecological systems
| Source | Provider | Typical use |
|--------|----------|-------------|
| FAOSTAT | FAO | Food systems, agriculture, land use |
| Global Forest Watch / Hansen | WRI / Maryland | Deforestation, land-cover change |
| Gridded population & DHS | CIESIN / DHS Program | Exposure, livelihoods, household well-being |
| SES Library / commons databases | SESMAD / IASC | Socio-ecological systems and commons governance |

### Geospatial & integration
- Boundary/exposure data: **GADM**, **Natural Earth**, **WorldPop**, **GHSL** (settlements)
- Earth-observation: **Google Earth Engine**, **Copernicus / Sentinel**, **NASA EarthData**

## 2. Software by method

### Quantitative (R / Stata / Python)
- R causal & panel: `fixest`, `did` (Callaway-Sant'Anna), `MatchIt`, `WeightIt`, `sensemakr`, `estimatr`
- R multilevel / SEM: `lme4`, `brms`, `lavaan`, `piecewiseSEM` (common in human-dimensions work)
- Survey & experiments: `survey`, `cregg`/`cjoint` (conjoint), `DeclareDesign`
- Stata: `reghdfe`, `csdid`, `ivreghdfe`, `mixed`, `gsem`, `coefplot`
- Python: `pandas`, `statsmodels`, `linearmodels`, `geopandas`, `xarray`, `scikit-learn`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, documents, fieldnotes
- Process tracing & QCA: explicit hypothesis tests; `QCA`/`SetMethods` (R) for set-theoretic analysis
- Mixed-methods integration: joint displays, triangulation matrices; document the integration logic

### Systems, scenarios & participatory methods
- Systems mapping / causal-loop & fuzzy cognitive maps; agent-based models (`NetLogo`, `Mesa`)
- Scenario & pathways work (SSP/RCP framings); participatory and stakeholder methods (workshops, Delphi)
- Spatial analysis: `sf`, `terra`, `tmap` (R); QGIS / Google Earth Engine

## 3. Conceptual frameworks & design
- Vulnerability / risk: IPCC AR5+ (hazard × exposure × vulnerability), entitlements, livelihoods (SLF)
- Governance: institutional analysis (IAD/SES Ostrom framework), adaptive & polycentric governance
- Transitions: multi-level perspective (MLP), socio-technical transitions, just-transition framings
- Always **make the framework do work**: it should generate the question, structure the analysis, and
  organize the interpretation (see `gec-conceptual-framework`)

## 4. Figures & exhibits (GEC rewards clear, integrative exhibits)
- Coefficient/forest plots (`ggplot2`/`broom`, `coefplot`); marginal-effects plots (`marginaleffects`)
- Conceptual-framework diagrams, systems maps, pathway/flow diagrams (drawio, `DiagrammeR`, TikZ)
- Maps for spatial variation (`sf`, `tmap`, QGIS); colorblind-safe palettes; legible in grayscale
- Vector output (PDF/EPS) for print; supply required Highlights (3-5 bullets, <=85 chars) as a separate
  editable file

## 5. Writing & references
- Reference managers: Zotero, Mendeley, BibTeX/BibLaTeX — any internally consistent reference style is
  accepted at submission; the journal style is applied after acceptance at proof.
- Typesetting: LaTeX (Elsevier `elsarticle` class, Overleaf) or Word; keep the abstract <=250 words
- Plain-language summaries help reach the policy and interdisciplinary audience GEC serves

## 6. Preregistration, data & transparency
- Preregistration / pre-analysis plans: **OSF Registries**, AsPredicted (for experiments/surveys)
- Repositories for a Data Availability Statement: institutional repository, **Dryad**, **Zenodo**,
  **OSF**, **figshare**, or a domain archive; deposit code with the data and cite the dataset
- Elsevier supports **research-data linking** and **Data in Brief**; document access controls for
  sensitive human-subjects data (see `gec-submission` and the Elsevier research-data policy)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Elsevier online submission system |
| Owner / publisher | **Elsevier** (ISSN 0959-3780 print / 1872-9495 online) |
| Review model | **Double-anonymized** — title page and anonymized manuscript are separate files |
| Article length | Research Articles **up to 8,000 words**; Perspectives **up to 3,000 words**; abstract **<=250 words** |
| Highlights | Required: **3-5 bullets, <=85 characters each**, as a separate editable file |
| Data policy | Elsevier **Option C**; deposit/cite/link research data, or explain why sharing is restricted |

## 8. Cautions
1. **Verify volatile specifics** (APC, editors, special calls, and policy wording) on the official
   Elsevier/ScienceDirect pages before filing.
2. **Lead with the human dimension** — GEC wants a significant social-science component, not a natural-
   science result with a policy sentence bolted on.
3. **Make the framework and the policy implications real** — interdisciplinary rigor plus genuine
   real-world relevance is the bar (see `gec-conceptual-framework`, `gec-policy-relevance-and-implications`).
4. **Match method to question** — quantitative, qualitative, and mixed methods are all welcome when
   done rigorously; for mixed methods, state the integration logic explicitly.
5. **Build transparency as you go** — prepare the Data Availability Statement and a clean replication
   archive before submission, not after acceptance.
