# Accounting-Research Tools & Resources (CAR)

This document lists external data sources, analysis software, and writing tools
commonly used when preparing a manuscript for **Contemporary Accounting Research
(CAR)**. CAR is deliberately method-agnostic — it welcomes archival/capital-markets,
experimental, analytical/modeling, field, survey, and qualitative work — so the
toolkit spans several research traditions. Map your tools to CAR's **Data Integrity
and Code Sharing Policy** (effective May 1, 2020): plan from day one for a data
availability statement, a public code repository, variable-definition documentation,
and six-year data/code retention. Always verify current licensing terms and CAR/CAAA
policies before relying on any resource.

## 1. Data Sources

### Archival / capital-markets accounting
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat (North America / Global) | S&P Global | Financial statements, fundamentals |
| CRSP | Center for Research in Security Prices | Returns, prices, market data |
| I/B/E/S | LSEG | Analyst forecasts, earnings expectations |
| Audit Analytics | Ideagen | Auditor, restatement, internal-control data |
| Thomson Reuters / Refinitiv (SDC) | LSEG | M&A, ownership, governance |
| BoardEx / ISS | Various | Boards, executives, governance indices |
| WRDS | Wharton | Hosted access + linking tables for the above |
| SEC EDGAR (10-K, 8-K, proxy) | SEC | Disclosure text, filings, XBRL financials |

### Experimental / survey / field data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Qualtrics | Qualtrics | Experiment and survey instruments |
| Prolific / MTurk / CloudResearch | Various | Online participant pools (non-professional) |
| Professional participant panels | Big-4 / firm relationships | Auditor, manager, investor subjects |
| Field-site / proprietary firm data | Partner organizations | Field studies, internal data (see policy item 2) |

### Analytical / modeling
| Tool | Use |
|------|-----|
| Mathematica / Maple | Symbolic modeling, comparative statics, proofs |
| MATLAB / Python (SymPy) | Numerical solutions, simulations, calibration |

## 2. Analysis Software & Packages

### Archival / capital-markets econometrics
- **Stata**: `reghdfe` (high-dimensional fixed effects), `ivreg2`/`ivreghdfe` (IV/2SLS), `xtreg`, `csdid`/`did` (modern difference-in-differences), `psmatch2`/`teffects` (matching), `winsor2` (winsorizing — document cutoffs per policy).
- **SAS**: still common for large CRSP/Compustat builds and event studies.
- **R**: `fixest`, `plm`, `sandwich`/`lmtest` (clustered/robust SE), `MatchIt`, `did`.
- **Python**: `pandas`, `linearmodels`, `statsmodels` for panel and event-study work.

### Experimental analysis
- ANOVA/ANCOVA and planned contrasts; mediation/moderation via **PROCESS** (Hayes), R `mediation`, or `lavaan` indirect effects with bootstrap CIs.
- Manipulation- and attention-check reporting; pre-registration via **AsPredicted** / **OSF Registries**.
- Power analysis: **G*Power**, R `pwr` / `simr` (especially for interactions).

### Analytical / modeling
- Document model setup, assumptions, equilibrium concept, and comparative statics; keep symbolic-math notebooks reproducible.

### Qualitative / field
- **NVivo**, **ATLAS.ti**, **Dedoose** for coding; maintain an audit trail and representative quotations.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; configure to an author-date style, then reconcile to the CAR Style Guide |
| EndNote | Broad style support |
| Overleaf / LaTeX | CAR accepts LaTeX; accepted papers may use Wiley's New Journal Design (NJD) template |
| Microsoft Word | CAR accepts Word; submit final files in Word or PDF |
| Grammarly / language tools | Permitted, but generative-AI use must be declared and described in Methods |

CAR's exact reference format is governed by the **CAR Style Guide** (author-date
style typical of accounting journals); set your manager to an author-date style and
reconcile against the current Style Guide before final submission.

## 4. Submission & Process

- **Submission portal**: Editorial Manager (EM) at editorialmanager.com/car.
- **Required files**: separate title page, blind manuscript, signed author declaration, ethics-approval verification (any human participants), and proof of payment for the submission fee.
- **Submission fee**: CA/US $250 (CAAA members) / $600 (non-members), Visa or Mastercard; receipt uploaded; reviewer-earned fee waivers accepted as proof of payment.
- **Bilingual abstracts**: the CAAA translates your abstract into French for publication.
- **Originality**: no concurrent submission; disclose substantial overlap with any other paper in the author declaration.

## 5. Reproducibility & Transparency (Data Integrity & Code Sharing Policy)

1. At submission, describe how data were acquired/produced and their sources; attach the full instrument for surveys/experiments.
2. For proprietary organizational data, agree to provide a credible verification means on editor request and disclose any non-disclosure restrictions.
3. Disclose which authors had data access and ran the analyses.
4. Before acceptance, provide a data availability statement with a repository link and cite the data in the reference list.
5. Archive the code that builds your final dataset in a public repository, documenting variable definitions, observation-omission rules (outliers), and modifications (winsorizing, truncating); assure six-year retention per NSF guidelines.

## 6. Verify Before You Rely

Editorial team, the submission portal, fee amounts, formatting limits, the CAR Style
Guide, and the Data Integrity & Code Sharing Policy change over time. Always confirm
current requirements on the official CAAA/CAR author-guideline pages and in Editorial
Manager before submitting.
