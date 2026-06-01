# Quantitative-Marketing Tools & Resources (Marketing Science)

This document lists external data sources, estimation/optimization software, and writing
tools commonly used when preparing a quantitative-marketing manuscript for **Marketing
Science** (INFORMS / ISMS). The journal's center of gravity is **mathematical modeling**:
structural econometric demand/supply models, analytical (game-theoretic) models, and
rigorously applied econometrics, statistics, and machine learning. The toolkit below
reflects that modeling core rather than a survey/scale-validation tradition. Always verify
licensing terms and the current Marketing Science Replication and Disclosure Policy before
using or depositing any resource.

## 1. Data Sources

### Consumer panels, scanner & retail data
| Source | Provider | Typical use |
|--------|----------|-------------|
| NielsenIQ / Nielsen Consumer Panel & Scanner (Kilts Center) | University of Chicago Booth (Kilts) | Household purchase panels, store scanner, demand estimation |
| Numerator / IRI (Circana) academic data | Circana / Numerator | CPG purchases, promotions, market response |
| dunnhumby / Tesco "The Complete Journey" | dunnhumby | Loyalty, basket, promotion response |
| JD.com / Alibaba academic datasets (MSOM, JD competitions) | Platforms | E-commerce demand, recommendation, pricing |

### Digital, advertising & platform data
| Source | Use |
|--------|-----|
| Google/Meta/Criteo ad-auction & log data (field experiments) | Ad effectiveness, auctions, attribution |
| App store / mobile telemetry, clickstream | Search, conversion, funnel models |
| Web-scraped prices, reviews, listings | Pricing dynamics, text-as-data, branding |
| Twitter/X, Reddit, review corpora | Word-of-mouth, sentiment, topic models |

### Firm / financial / public data (linkable, licensed)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat / CRSP | S&P Global / CRSP | Firm performance, marketing-finance links |
| Census / BLS / American Community Survey | US Government | Demographics for demand heterogeneity |
| Kantar / Comscore / SafeGraph (foot traffic) | Various | Media, online behavior, store visits |

> Replication note: for licensed data (e.g., NielsenIQ, Compustat, CRSP) the journal does
> not expect raw redistribution — provide access instructions and the code that builds and
> links the analysis sample, per the Replication and Disclosure Policy.

## 2. Modeling, Estimation & Optimization Software

### Structural econometrics (demand & supply)
- **Demand systems**: BLP / random-coefficients logit (`pyBLP` in Python; `BLPestimatoR` in R), nested/mixed logit, AIDS.
- **Dynamic & discrete-choice dynamics**: dynamic programming, Rust nested fixed-point, CCP (Hotz–Miller), Bajari–Benkard–Levin for dynamic games.
- **Estimation method**: GMM, MLE/SMLE, simulated method of moments; **MATLAB**, **Python** (`numpy`/`scipy`/`statsmodels`), **R**, **Julia** for custom likelihoods and equilibrium solving.

### Analytical / game-theoretic modeling
- **Mathematica**, **Maple**, or **SymPy** (Python) for symbolic comparative statics, equilibrium derivation, and signing of effects.
- Tools for proofs, fixed-point/equilibrium existence, and clean comparative-statics tables.

### Bayesian hierarchical & choice models
- **Stan** (`cmdstanpy`/`rstan`), **PyMC**, **bayesm** (R), **JAGS** — hierarchical Bayes for heterogeneity, conjoint, and choice data.
- **Sawtooth** for conjoint/choice-experiment fielding and design.

### Optimization (INFORMS lineage)
- **Gurobi**, **CPLEX**, **AMPL**, **JuMP** (Julia), `scipy.optimize`, `Knitro` — for solving pricing/assortment/equilibrium and counterfactual policies.

### Machine learning applied to marketing
- **Python** (`scikit-learn`, `xgboost`, `pytorch`), causal ML (`econml`, `grf`/`causalforestDML`, double/debiased ML) for heterogeneous treatment effects, uplift, and policy learning tied to a model.
- Text-as-data: embeddings, topic models, LLM-based feature extraction (document provenance for replication).

### Field experiments & causal identification
- A/B testing platforms and geo-experiments; randomization-inference and clustered SEs.
- Quasi-experimental identification (DiD, synthetic control, RD, IV) where the structural/analytical model motivates the estimand.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| LaTeX + INFORMS style files | Recommended; use the INFORMS LaTeX style and Style-Instructions.pdf from the Author Portal |
| MS Word (INFORMS template) | Accepted; uploaded as Word or PDF |
| Zotero / BibTeX | Configure to INFORMS author-year reference style — in-text (Norman 1977), alphabetical reference list |
| Overleaf | Convenient for INFORMS LaTeX collaboration |
| Grammarly | Language polish |

In-text citations are author-year in INFORMS style — e.g., (Norman 1977) or Norman (1977) —
with references listed alphabetically at the end. Configure your reference manager
accordingly and reconcile against the current INFORMS Style Guide.

## 4. Submission & Process

- **Submission portal**: ScholarOne Manuscripts (mc.manuscriptcentral.com/mksc); verify the current link on the official Marketing Science pages.
- **Blinding**: double-anonymous review for regular submissions — remove names, institutions, and acknowledgments; the cover letter is seen by the Editor/AE but not reviewers.
- **Preferred handlers**: you may suggest 2 preferred Associate Editors and 3 preferred reviewers.
- **Self-overlap**: disclose and cite any of your own published/under-review work the submission builds on, and state how it goes beyond.
- **Tracks**: Regular (Original Article), Frontiers in Marketing Science (≤ 6,000 words total), Database papers, Practice Papers/Practice Prize (500–1,000-word Impact Statement, single-blind), Science-to-Practice.

## 5. Reproducibility & Transparency (Replication and Disclosure Policy)

1. Keep clean, commented estimation code (MATLAB/Python/R/Julia/Stan) and a master script that regenerates every table, figure, and counterfactual from the analysis sample.
2. Document data provenance, sample construction, and any cleaning/exclusion rules; for licensed data, ship the access instructions and linking/build code rather than raw data.
3. Provide the estimation routines, starting values, optimizer settings, and (for structural work) the equilibrium-solving code and tolerances needed to reproduce essential results.
4. Prepare an online appendix for derivations, identification arguments, robustness, and additional specifications.
5. Verify all licensing and confidentiality terms before depositing or sharing data and code.

## 6. Verify Before You Rely

Editorial team, submission links, fees, formatting, word caps (e.g., the Frontiers 6,000-word
limit), and the Replication and Disclosure Policy change over time. Always confirm the current
requirements on the official Marketing Science submission and replication pages and the INFORMS
Author Portal before submitting.
