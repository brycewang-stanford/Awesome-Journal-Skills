# External Tools & Resources for JEG-Style Growth Research

Data sources, software, and packages useful when preparing a *Journal of Economic
Growth* (JEG) submission. JEG publishes **both theory and empirics** in growth and
dynamic macroeconomics, so this list spans cross-country/panel growth data, modern
panel and causal econometrics, and the numerical/symbolic tooling a growth-theory
paper needs. Check licenses and current access terms before use; verify all
JEG-specific process facts on the official Springer page (see `official-source-map.md`).

## 1. Data sources (empirical growth & development macro)

### Cross-country & long-run growth
| Source | Provider | Typical use |
|--------|----------|-------------|
| Penn World Table (PWT 10.x) | Groningen Growth & Development Centre | Real GDP, TFP, capital, cross-country levels/growth |
| Maddison Project Database | Groningen / Maddison Project | Very long-run GDP per capita, historical convergence |
| World Bank WDI / World Development Indicators | World Bank | Standard cross-country growth covariates |
| Barro-Lee Educational Attainment | Barro & Lee | Human-capital / schooling stocks (a JEG-core variable) |
| IMF WEO / International Financial Statistics | IMF | Macro aggregates, financial development |

### Demography, human capital, institutions, geography
| Source | Provider | Typical use |
|--------|----------|-------------|
| UN World Population Prospects | United Nations | Fertility, mortality, demographic transition (JEG-core) |
| Gapminder / historical fertility series | Gapminder + academic archives | Long-run fertility-growth dynamics |
| Polity / V-Dem | Center for Systemic Peace / V-Dem | Political economy of growth, institutions |
| CEPII GeoDist / gravity | CEPII | Trade-and-growth, geography instruments |
| Long-run historical/geographic datasets | Various academic archives | Unified-growth-theory deep determinants (待核实 per-source license) |

## 2. Software for empirical growth work

### Stata
- Dynamic panel / growth regressions: `xtabond2` (Arellano-Bond / Blundell-Bond system GMM), `xtdpdgmm`
- Panel & FE at scale: `reghdfe`, `xtreg`
- Cross-country convergence: beta/sigma-convergence scripts; `xtunitroot` for panel unit roots
- Causal designs (where a clean shock exists): `csdid`, `did_multiplegt_dyn`, `ivreg2`, `rdrobust`
- Inference with few clusters / countries: `boottest` (wild-cluster bootstrap)

### R
- Panel/GMM: `plm`, `pdynmc` (dynamic panel GMM); FE/IV via `fixest::feols`
- Convergence & spatial: `splm`, growth-accounting helpers
- Robust/cluster inference: `sandwich`, `clubSandwich`, `fwildclusterboot`
- Reproducibility: `renv` (pin versions), `targets` (pipeline)

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels` (panel IV/FE, system GMM via `linearmodels`)
- `pip freeze` / `requirements.txt` to pin the environment

## 3. Tooling for growth THEORY (models, proofs, computation)

Many JEG papers are theoretical (OLG, endogenous-growth, unified-growth-theory models).
For these, the "replication" object is often a **numerical example or calibration**, not a dataset.

- **Symbolic / analytical**: Mathematica, SymPy (Python), Maple — for steady-state algebra, comparative statics, stability conditions.
- **Numerical dynamic macro**: Dynare (perfect-foresight & stochastic transition paths), MATLAB/Octave, Julia (`NLsolve`, `DifferentialEquations.jl`), Python (`scipy.optimize`) for solving transition dynamics, calibrating OLG economies, and producing phase diagrams / transition plots.
- **Calibration & quantitative growth**: document parameter sources, targets, and solution method so a reader can reproduce every numerical figure.
- **Typesetting proofs**: LaTeX with `amsmath`/`amsthm` (theorem/lemma/proof environments) — relevant because JEG prefers LaTeX submission.

## 4. Identification & assumptions toolkit (calibrate to your paper type)

| Paper type | Core checks | Tools |
|------------|-------------|-------|
| Cross-country / panel growth (empirical) | Endogeneity of regressors, weak/many instruments in system GMM (Hansen-J, AR(2)), instrument-count parsimony | `xtabond2`, `pdynmc`, `linearmodels` |
| Causal growth shock (DID/IV/RDD) | Pre-trends, first-stage strength, density/balance | `csdid`, `ivreg2`, `rdrobust` |
| Growth THEORY | Existence/uniqueness of equilibrium, stability of steady state, transversality, sign of comparative statics, generality of assumptions | symbolic algebra + numerical solver |
| Quantitative / calibrated model | Externally vs internally calibrated parameters, sensitivity to key elasticities, model fit to growth facts | Dynare / Julia / MATLAB |

## 5. Figures (growth papers are convergence- and transition-forward)
- Convergence scatterplots (initial GDP vs subsequent growth), binned scatters
- Transition-path / phase-diagram plots for theoretical models
- Event-study or impulse-response plots where a shock is identified
- Vector output (PDF/EPS) for print resolution; avoid chartjunk

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX — set to **author-year**, formatted to **APA 7th edition** (JEG's required style).
- Typesetting: **LaTeX is preferred** by JEG (Springer Nature LaTeX template); use the template to satisfy formatting and ensure an editable source file at every submission/revision. Word (.docx) is accepted as an editable alternative.

## 7. Process & portal (verify on the official page — see official-source-map.md)
| Item | Note |
|------|------|
| Submission portal | Springer Nature "Submit manuscript" (`submission.nature.com/new-submission/10887/3`) |
| Submission fee | **None** (no submission/handling fee) |
| Open access | Optional Open Choice APC GBP 3,090 / USD 4,590 / EUR 3,590 (待核实 — revised periodically) |
| Abstract | 150-250 words |
| Title page | JEL codes + 4-6 keywords + ORCID + Statements/Declarations |
| Data policy | Springer Nature **Data Availability Statement** (no journal-specific code archive; 待核实) |
| Publisher | Springer Nature |

## 8. Cautions
1. **Verify volatile specifics** (APC, editors, review model, portal URL, word limit) on the official Springer page — several are 待核实 here.
2. **Match estimator to design** — naive cross-country OLS growth regressions with endogenous regressors are a known pitfall; system GMM has its own instrument-proliferation traps (cap and test instruments).
3. **For theory papers, "reproducibility" = a documented numerical example**, not a dataset — still pin software and report the solution method.
4. **Provide an editable source file** (LaTeX or .docx) at every submission and revision, or the paper is not considered for review.
