# Empirical OM & Supply-Chain Research Tools & Resources (JOM)

This document lists external data sources, analysis software, and writing tools commonly used when preparing an **empirical** operations and supply chain management manuscript for the **Journal of Operations Management (JOM)**. JOM publishes survey, archival/secondary-data, field, case, experimental, behavioral, and intervention-based research — but **not** purely analytical models or optimization techniques. The toolkit below therefore centers on *observation-grounded* OM research. Always verify licensing terms and current JOM/Wiley/ASCM policies before using any resource.

## 1. Data Sources

### Operations / supply-chain archival & secondary data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat | S&P Global Market Intelligence | Inventory, COGS, plant/segment financials, performance |
| Compustat Segments | S&P Global | Business/geographic segment operations |
| Bloomberg / Refinitiv | LSEG | Supply-chain relationships, ESG, firm financials |
| FactSet Revere / Bloomberg SPLC | FactSet / Bloomberg | Buyer–supplier network links |
| Mergent / Capital IQ | Moody's / S&P | Customer–supplier disclosures |
| WRDS | Wharton | Hosted access to Compustat/CRSP/IBES and linking tables |
| ImportGenius / Panjiva | S&P Global | Bill-of-lading import/export shipment records |
| UN Comtrade / WITS | UN / World Bank | Trade flows by product and country |

### Operations-specific registries & disclosures
| Source | Use |
|--------|-----|
| FDA recalls / NHTSA recalls | Product recall events, quality failures |
| SEC EDGAR (10-K, 8-K) | Supply-chain risk text, MD&A, internal controls |
| CDP (Carbon Disclosure Project) | Sustainable-operations / emissions data |
| EPA TRI / FLA / audit databases | Environmental and social compliance, factory audits |
| AHRQ / HCUP / CMS | Healthcare-operations utilization and outcomes |
| USPTO / PatentsView | Process and product innovation, project management |

### Survey, behavioral, and field/primary data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Qualtrics / Prolific / MTurk / CloudResearch | Various | Survey instruments and behavioral-OM experiments |
| IMSS / GMRG / HPM | Research consortia | Cross-country manufacturing-practice surveys |
| Plant/site field access, partner firms | Author-arranged | Field studies, case studies, intervention-based research |
| ERP/MES/WMS/POS extracts | Partner organizations | Transaction-level operational data |

## 2. Analysis Software & Packages

> JOM is empirical: the toolkit is for *estimation and inference on observed data*, not for building optimization models. Use these to test theory against operations data.

### Survey-based measurement & SEM
- **Mplus** — latent constructs, CFA, full SEM, multilevel SEM, FIML for missing data.
- **R**: `lavaan` (SEM/CFA), `semTools` (reliability, measurement invariance), `psych` (alpha, EFA).
- **Stata**: `sem`, `gsem`; **AMOS** / **SmartPLS** (PLS-SEM where formative constructs or prediction dominate).

### Archival / secondary-data econometrics (panel & causal)
- **Stata**: `reghdfe` (high-dimensional FE), `xtreg`, `ivreghdfe`/`ivreg2` (IV/2SLS), `csdid`/`did` (staggered DiD), `psmatch2`/`teffects` (matching), `xtabond2` (dynamic panel/GMM), `heckman` (selection).
- **R**: `fixest`, `plm`, `did`, `MatchIt`, `sandwich` (cluster-robust SE).
- Useful for inventory, recall, supplier-relationship, and disruption studies where endogeneity is the central threat.

### Behavioral-OM experiments
- Power analysis: **G*Power**, R `pwr` / `simr` (simulation-based power for interactions, repeated measures).
- Design/analysis: ANOVA, mixed models (`lme4`, `lmerTest`), mediation/moderation via **PROCESS** (Hayes) or `mediation`.
- Pre-registration: **AsPredicted**, **OSF Registries**.

### Count / duration / event outcomes (common in OM)
- Recalls, defects, disruptions, project milestones: Poisson/negative-binomial (`fixest`, Stata `nbreg`), hazard/survival (`survival`, Stata `stcox`/`streg`).

### System dynamics & simulation as a *complement* (not a substitute) to observation
- **Vensim**, **Stella**, **AnyLogic**, `R simmer` — to formalize feedback structure behind an *empirically grounded* argument (e.g., behind intervention-based or field work); JOM still requires the observation that renders the research empirical.

### Qualitative / case / intervention-based research
- **NVivo**, **ATLAS.ti**, **Dedoose** — coding of interviews, field notes, archival documents.
- Templates for Gioia-style data structures, process models, and intervention/action-research logs.

### Text & network analysis
- **Python**: `pandas`, `spaCy`, `gensim`, `networkx` (supply-network structure, 10-K risk text).
- **R**: `quanteda`, `igraph`, `tidytext`.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; supports APA output (JOM uses APA) |
| EndNote | Broad journal style support; Wiley styles available |
| Mendeley | Wiley/Elsevier-friendly |
| Overleaf / LaTeX | Optional; Wiley provides templates — verify the ReX portal accepts the format |
| Grammarly | Language polish |

JOM uses **APA** citation/reference style; configure your reference manager to APA. References may be in any consistent format at first submission, but Wiley applies final styling at proof stage.

## 4. Submission & Process

- **Submission portal**: Wiley Research Exchange (ReX) at wiley.atyponrex.com/journal/JOOM.
- **Department routing**: name **2 Departments (one preferred)** from JOM's 12 Departments in the cover letter.
- **Reviewer recommendations**: recommend **≥3 Associate Editors** and **≥3 ERB reviewers** free of conflicts.
- **Required checklist**: complete and attach the JOM submission checklist — submissions are not considered without it.
- **Disclosures**: AI use, prior dissertation/conference versions, prior data use, and any previous reject-and-resubmit decisions.
- **Originality**: iThenticate/CrossCheck similarity screening (no single source >~1% outside quotations; overall >15% must be justified).
- **ORCID**: keep an ORCID linked to your Wiley account.

## 5. Reproducibility & Transparency

1. Keep clean, commented scripts (do-files, R scripts, Mplus inputs) that regenerate every table and figure.
2. Document data provenance: source extracts, sample-construction steps, exclusion rules, and any buyer–supplier link matching.
3. Prepare a Wiley **Data Availability Statement**; where possible, archive de-identified data, code, scripts, and materials in a public repository with a persistent identifier (DOI/accession) and cite the shared data.
4. Prepare an online supplement for additional analyses, instruments, and robustness checks.
5. Verify all confidentiality terms with partner firms before depositing or sharing operational data.

## 6. Verify Before You Rely

Editorial team, Department roster, submission links, formatting limits, fees, APC amount, and data/transparency policies change over time. Always confirm current requirements on the official ASCM/JOM page, the Wiley JOM Author Guidelines, and the JOM author-resource hub before submitting. Items not confirmed on an authoritative page are flagged **待核实** in `official-source-map.md`.
