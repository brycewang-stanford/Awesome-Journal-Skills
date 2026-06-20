# External Tools & Resources for Agricultural-Systems-Style Research

Data sources, models, software, and packages useful when preparing an *Agricultural Systems* (AgSy)
submission. AgSy is a **systems-science journal**: a submission analyzes **interactions, trade-offs, and
emergent behavior** across components and hierarchical levels (field → farm → landscape → region →
food system), usually through the **integration of conceptual, empirical, and dynamic modelling**. Match
tools to the system boundary and the modelling approach, not to a single agronomic factor. Check
licenses and current access terms before use, and verify any AgSy-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Simulation & systems models by scale

### Field / cropping-system process models
| Model | Provider | Typical use |
|-------|----------|-------------|
| APSIM | CSIRO / APSIM Initiative | Crop–soil–water–N dynamics; cropping-system simulation, scenario analysis |
| DSSAT (CSM) | DSSAT Foundation | Multi-crop process simulation; calibration and seasonal analysis |
| STICS | INRAE | Generic soil–crop model for systems and rotations |
| DNDC / DayCent | UNH / CSU | Biogeochemistry, soil C/N, greenhouse-gas (N2O, CH4) fluxes |

### Whole-farm, livestock & bio-economic models
| Model | Provider | Typical use |
|-------|----------|-------------|
| Whole-farm simulators (e.g., IFSM, FarmDESIGN, NUANCES-FARMSIM) | Various | Farm-scale resource flows, nutrient balances, trade-offs |
| Bio-economic / mathematical-programming models (GAMS, FSSIM, MIDAS) | Various | Farm decision-making under constraints; whole-farm optimization |
| Livestock & grazing systems models (GRAZPLAN/GrassGro, RUMINANT) | CSIRO / ILRI | Animal production, feed budgets, crop–livestock integration |

### Landscape, regional & food-system models
| Model | Provider | Typical use |
|-------|----------|-------------|
| Agent-based models (NetLogo, Mesa, GAMA) | Various | Farmer decision heterogeneity, adoption, emergent landscape patterns |
| Integrated assessment / land-use models (GLOBIOM, MAgPIE, CAPRI) | IIASA / PIK / EU | Regional-to-global food-system, land-use, and policy scenarios |
| System dynamics (Vensim, Stella, `pysd`) | Various | Stocks/flows, feedbacks, long-run system behavior |

## 2. Software for systems analysis, calibration & uncertainty

### R
- Calibration / sensitivity / uncertainty: `sensitivity`, `FME`, `BayesianTools`, `hydroPSO`, `nloptr`
- Model evaluation: `hydroGOF` (RMSE, NSE, KGE, bias), `Metrics`, `verification`
- Multi-objective trade-offs / optimization: `mco`, `nsga2R`, `rgenoud`
- Workflows & reproducibility: `targets`, `renv`, `tidyverse`, `sf`/`terra` (spatial), `simecol`
### Python
- `SALib` (Sobol/Morris sensitivity), `SAlib`-driven UA; `scipy.optimize`, `pymoo` (multi-objective)
- `pandas`, `numpy`, `xarray` (gridded output), `pysd` (system dynamics), `mesa` (ABM)
- `scikit-learn` / surrogate (emulator) models for expensive simulators; `matplotlib`/`seaborn`
### Other
- GAMS / Pyomo / Julia (JuMP) for mathematical-programming and bio-economic optimization
- Apsimx / DSSAT shells and R/Python wrappers (`apsimx`, `DSSAT`) for batch runs and calibration

## 3. Data sources for systems & food-system analysis

| Source | Provider | Typical use |
|--------|----------|-------------|
| FAOSTAT | FAO | Production, land use, food balance, emissions by country |
| GYGA (Global Yield Gap Atlas) | UNL / WUR | Yield gaps and potential by climate zone |
| Soil & weather: ISRIC SoilGrids, NASA POWER, AgERA5 | ISRIC / NASA / ECMWF | Model inputs across scales |
| Farm Accountancy Data Network (FADN), LSMS-ISA | EU / World Bank | Farm economics, household and smallholder systems |
| Long-term experiments & farm networks | Various | Calibration/validation data for systems models |

## 4. Reproducibility for data *and* models (AgSy applies Elsevier's research-data policy)
- Deposit research data **and code/models** in a repository (Mendeley Data, Zenodo, OSF, or a domain repository),
  cite and link the dataset in the article; if data cannot be shared, **state why** (see
  `agsy-reproducibility-and-data-policy`).
- Document **model version, parameter sets, calibration data, and run scripts**; pin software versions
  (`renv.lock` / `requirements.txt` / environment files); set and report **seeds** for stochastic runs.
- Consider model-description standards (e.g., **ODD protocol** for agent-based models) so others can
  re-implement the model.

## 5. Figures & exhibits (AgSy rewards exhibits that show interactions and trade-offs)
- Trade-off / Pareto-front plots; radar/spider charts for multi-indicator sustainability profiles
- Time-series of state variables; observed-vs-simulated (1:1) plots with fit statistics
- Sankey/flow diagrams for resource, nutrient, or energy flows; conceptual system diagrams (boxes/arrows)
- Maps for landscape/regional variation (`sf`, `terra`, `tmap`); colorblind-safe palettes, vector output

## 6. Writing & references
- Reference managers: Zotero, Mendeley, BibTeX/BibLaTeX — format to the journal's reference style
- Typesetting: LaTeX (Elsevier `elsarticle`) or Word; prepare **Highlights**, a **graphical abstract**,
  a **CRediT** statement, a **declaration of competing interest**, funding disclosure, and any required
  AI-use disclosure

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | Use the current ScienceDirect **Submit your article** link / Editorial Manager path |
| Publisher | **Elsevier** (ISSN 0308-521X print / 1873-2267 online) |
| Review model | **Single anonymized**; suitable submissions typically go to a minimum of two reviewers; editor decides |
| Article types | Original scientific papers (~8,000 words), short communications (~4,000), perspectives (~2,000, rapid review), comments (~1,000), reviews |
| Abstract | **≤ 250 words**; 1-7 keywords; **Highlights** required as 3-5 bullets of max 85 characters each; **graphical abstract** required |
| OA / subscription | Open Access APC **USD 3,850 excluding taxes**; subscription route has no publication fee charged to authors |
| Data/code policy | Option C: deposit research data, cite and link it, or explain why sharing is not possible; code and models are research data |

## 8. Cautions
1. **Live-check volatile specifics** (editors, APC, submission-system URL, graphical-abstract specs,
   and article-type consultation rules) on the official Elsevier/ScienceDirect pages before a real
   upload.
2. **Center the system, not a single factor** — AgSy wants interactions, hierarchical levels, and
   trade-offs, not a one-treatment field trial.
3. **Describe and evaluate the model** — version, calibration data, evaluation metrics, and uncertainty;
   a black-box simulation will not survive review.
4. **Make data *and* models reproducible** — the Elsevier policy treats code and models as research data.
5. **Show decision relevance** — connect the systems analysis to a management, design, or policy choice.
