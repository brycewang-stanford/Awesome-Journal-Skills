# Accounting-Research Tools & Resources (TAR)

This document lists external data sources, analysis software, and writing tools commonly used when
preparing an archival/empirical or analytical accounting manuscript for **The Accounting Review
(TAR)**, published by the American Accounting Association (AAA). TAR is open to all rigorous methods
across financial accounting, capital markets, auditing, management accounting, taxation, and
accounting information systems, but the de facto core is large-sample archival work with substantial
experimental and analytical streams. Because TAR's data-authenticity policy requires you to provide
a precise data description and **access to the computer code** that processes the data, keep
reproducible scripts from the first regression. Always verify licensing terms and current
AAA/TAR policies before using any resource.

## 1. Data Sources

### Financial accounting & capital markets (archival core)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat (North America / Global) | S&P Global / WRDS | Financial statements, fundamentals, accruals |
| CRSP | Center for Research in Security Prices | Returns, prices, market reactions (event studies) |
| I/B/E/S | LSEG / WRDS | Analyst forecasts, consensus, surprises |
| Thomson Reuters / Refinitiv 13F & insider | LSEG / WRDS | Institutional holdings, insider trades |
| RavenPack / EDGAR text | Various | Disclosure tone, readability, narrative measures |
| SEC EDGAR (10-K, 10-Q, 8-K, DEF 14A) | U.S. SEC | Filings, restatements, disclosure text, XBRL |

### Auditing & assurance
| Source | Provider | Typical use |
|--------|----------|-------------|
| Audit Analytics | Audit Analytics / WRDS | Auditor, fees, going-concern, restatements, ICFR |
| PCAOB inspection reports & AuditorSearch | PCAOB | Inspection deficiencies, engagement partner identity |

### Taxation
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat tax footnote items + ETR | S&P Global / WRDS | Effective/cash tax rates, tax avoidance, BTD |
| IRS SOI / country-by-country (where available) | IRS / OECD | Aggregate tax, multinational profit shifting |

### Management accounting & AIS
| Source | Use |
|--------|-----|
| Proprietary firm field data (under NDA) | Cost systems, budgeting, internal performance metrics |
| ERP / system logs, transaction-level data | AIS controls, process and fraud-risk research |

### Experimental / behavioral stream (notable at TAR)
| Source | Use |
|--------|-----|
| Qualtrics / Prolific / professional participant pools | Investor, auditor, and manager judgment experiments |
| Practitioner panels (e.g., recruited CPAs, analysts) | Expertise-sensitive tasks requiring IRB approval |

## 2. Analysis Software & Packages

### Large-sample archival econometrics (primary)
- **Stata**: `reghdfe` (high-dimensional fixed effects: firm/year/industry), `ivreghdfe`/`ivreg2` (IV/2SLS), `xtreg`, `csdid`/`did` (staggered DiD), `psmatch2`/`teffects` (matching), `rdrobust` (RDD), `boottest` (wild-cluster bootstrap), `estout`/`outreg2` (exhibit export).
- **R**: `fixest` (fast high-dimensional FE, multiway clustering), `did`, `MatchIt`, `rdrobust`, `sandwich`/`lmtest` (clustered/robust SE), `modelsummary` (tables).
- **SAS**: still common with WRDS for sample construction and merges; `PROC SQL`, macro-driven panel building.
- **Python**: `pandas`/`linearmodels` (panel, IV), `wrds` API, `statsmodels`.

### Analytical / theory papers
- **Mathematica** or **Maple** — symbolic derivation, comparative statics, signaling/agency models.
- **LaTeX** with `amsmath`/`amsthm` — proofs, propositions, equilibrium derivations.
- Numerical solvers (MATLAB / Python `scipy`) for models without closed-form solutions.

### Experimental / behavioral
- Power analysis: **G*Power**, R `pwr`/`simr`.
- Estimation: ANOVA/ANCOVA, mediation (PROCESS / `lavaan` indirect effects), planned contrasts.
- Pre-registration: **AsPredicted**, **OSF Registries**.

### Text / disclosure measurement
- Readability and tone: Loughran-McDonald financial sentiment dictionaries; `textstat`, custom Python pipelines.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; configure to **Chicago Manual of Style (16th ed.)**, TAR's house style |
| EndNote | Broad style support; load a Chicago author-date style |
| Overleaf / LaTeX | Common for analytical papers; verify Editorial Manager accepts the format |
| Grammarly | Language polish; spelling per Webster's Collegiate Dictionary |

TAR uses **The Chicago Manual of Style (16th ed.)**, not APA — configure your reference manager to a
Chicago author-date style and reconcile against the current AAA Manuscript Preparation Guide.

## 4. Submission & Process

- **Submission portal**: Editorial Manager at `editorialmanager.com/accr` (verify the current link).
- **ORCID**: required for all authors — keep an ORCID linked.
- **AI disclosure**: prepare the AI disclosure statement (tools, extent, reasons) for placement
  immediately after the abstract and before the body; update it on resubmission.
- **Conflict of Interest**: complete the COI form at submission.
- **Plagiarism/originality**: manuscripts are screened with plagiarism-detection software.
- **Submission caps**: mind the eight first-round submissions per author per rolling 24 months, and
  the 10-author byline cap.

## 5. Reproducibility & Data-Authenticity (TAR-specific)

TAR's data-authenticity policy is differentiated by data type — build your archive accordingly:

1. **Publicly available databases** (Compustat, CRSP, I/B/E/S, Audit Analytics): provide a precise
   description of the data **and** access to the computer code used to process it.
2. **Data abstracted from public sources** (hand-collected from filings, PCAOB reports): provide the
   abstraction methodology **and** code access.
3. **Privately collected data** (proprietary field data, experiments): provide sufficient detail for
   reader confidence; corroborating third parties are acceptable.
4. Keep clean, commented scripts (do-files, R/SAS scripts) that regenerate every table and figure
   from raw extracts; document sample-construction steps, merges, and exclusion screens.
5. For experiments, retain IRB approval, instruments, and randomization/analysis code.

## 6. Verify Before You Rely

Editorial team, the Editorial Manager link, formatting limits, the submission fee, submission caps,
and data-authenticity policy change over time. Always confirm current requirements on the official
TAR Editorial Policy, Guide for Authors, and the AAA Manuscript Preparation Guide before submitting.
