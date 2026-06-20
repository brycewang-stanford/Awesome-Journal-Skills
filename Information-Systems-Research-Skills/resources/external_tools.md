# Information Systems Research Tools & Resources (ISR)

This document lists external data sources, modeling and analysis software, and writing
tools commonly used when preparing a manuscript for **Information Systems Research (ISR)**.
ISR is deliberately **sociotechnical and intradisciplinary** and houses **both** rigorous
behavioral/empirical research **and** analytical economic, econometric, and design-science
modeling as co-equal genres, so the toolkit spans several traditions at once. Always verify
licensing terms and current INFORMS/ISR policies before using any resource.

## 1. Data Sources

### Digital-platform, IT-artifact, and trace data (sociotechnical IS phenomena)
| Source | Provider | Typical use |
|--------|----------|-------------|
| GitHub / GitLab APIs | Microsoft / GitLab | Open-source collaboration, software teams, OSS governance |
| App store / mobile-app panels (data.ai, Sensor Tower) | Vendors | App adoption, platform competition, in-app behavior |
| Platform/marketplace logs (Amazon, eBay, Airbnb, Uber, freelancing) | Firm partnerships / scrapes | Two-sided markets, reviews, pricing, matching |
| Online-community / social-media APIs (Reddit, X, Stack Overflow) | Platforms | Knowledge contribution, UGC, network effects |
| Web/clickstream & A/B-test logs | Firm field sites | Use behavior, recommender and nudge effects |
| Crowdfunding (Kickstarter, Indiegogo) | Platforms | Digital entrepreneurship, signaling |

### Firm-, market-, and IT-investment data (economic/strategic IS)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Compustat / CRSP | S&P Global / CRSP | IT-investment value, firm performance, productivity |
| Ci Technology / Harte-Hanks (CiTDB) | Aberdeen | Firm-level IT hardware/software stock |
| USPTO / PatentsView | US PTO | IT innovation, patents, citations |
| SEC EDGAR (10-K, 8-K) | SEC | IT/security disclosure text, breaches, governance |

### Survey, experiment, and behavioral-IS data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Qualtrics / Prolific / MTurk / CloudResearch | Various | Online surveys, behavioral experiments, vignettes |
| Field experiments with platform/firm partners | Partner orgs | Causal tests of design and policy interventions |
| Eye-tracking / fMRI / physiological (NeuroIS) | Lab vendors | Cognition, affect, attention to IT artifacts |

## 2. Analysis & Modeling Software

ISR evaluates two co-equal traditions; pick the stack that matches your genre.

### Analytical / economic & game-theoretic modeling
- **Mathematica**, **Maple** — closed-form derivation, comparative statics, proof support.
- **MATLAB**, **Python** (`SymPy`, `NumPy`, `SciPy`) — numerical solution, simulation of equilibria.
- **GAMS / AMPL / Gurobi / CPLEX** — optimization for analytical/design models (the INFORMS OR lineage).
- Game-theoretic / mechanism-design write-ups belong in the paper; lengthy proofs go to the electronic companion.

### Econometrics & causal inference (empirical economic IS)
- **Stata**: `reghdfe` (high-dimensional FE), `ivreghdfe`/`ivreg2` (IV/2SLS), `csdid`/`did` (modern DiD), `rdrobust` (RDD), `psmatch2`/`teffects` (matching).
- **R**: `fixest`, `did`, `rdrobust`, `MatchIt`, `sandwich` (robust/clustered SE); **Python** `linearmodels`, `econml`, `DoubleML`.

### Behavioral measurement, SEM & multilevel
- **Mplus**, **R** `lavaan` / `semTools` (CFA/SEM, measurement invariance), `psych` (alpha/EFA), **SmartPLS** (PLS-SEM, common in IS).
- Multilevel: **R** `lme4`/`lmerTest`, **Stata** `mixed`; Hayes **PROCESS** for moderation/mediation.

### Design science & computational artifacts
- Prototyping/build environments for the IT artifact; **Python**/**R** for ML, NLP (`transformers`, `spaCy`), and text-as-data.
- Evaluation harnesses, benchmark datasets, and user studies to demonstrate utility per design-science guidelines.
- Agent-based / discrete-event simulation: **NetLogo**, **AnyLogic**, **SimPy**.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; configure to an author-date (INFORMS/Chicago) output style |
| EndNote | Broad style support; INFORMS author-date |
| Overleaf / LaTeX | Useful for analytical papers; verify the portal accepts the format and that an electronic-companion file is separable |
| Grammarly | Language polish |

INFORMS/ISR uses an **author-date** reference style: alphabetized references, with in-text citations by
author name and year. Reconcile final details against the current official ISR examples before submitting.

## 4. Submission & Process

- **Submission portal**: INFORMS ScholarOne / Manuscript Central (verify the current ISR link on the official INFORMS/ISR site).
- **Contribution statement**: prepare the **~500-word contribution statement** required in every cover letter (effective June 1, 2023).
- **Editor/reviewer nominations**: be ready to nominate **2 Senior Editors**, **2 Associate Editors**, and
  **5 preferred reviewers including at least 2 ERB members**, with conflicts screened.
- **Electronic companion**: keep proofs, measurement items, and supplementary analyses in a separable online appendix (text capped at 32 pages, 38 total).
- **ORCID / disclosures**: the submitting author must provide an ORCID ID; prepare conflict-of-interest,
  funding, ethics, provenance, and data-rights certifications for ScholarOne.

## 5. Reproducibility & Transparency

1. Keep clean, commented scripts (do-files, R/Python scripts, Mathematica/MATLAB notebooks, solver inputs) that regenerate every table, figure, and proof.
2. Document data sources, sample-construction steps, exclusion rules, and (for analytical work) all assumptions and parameter ranges.
3. Prepare the electronic companion for proofs, robustness checks, full measurement items, and additional analyses.
4. Where data can be shared, prepare a de-identified dataset and codebook. ISR's active source-backed
   rule is **data provenance certification**; do not overstate a repository-deposit mandate.
5. Verify all licensing, platform-ToS, and confidentiality terms before depositing or sharing data.

## 6. Verify Before You Rely

Editorial team, submission links, formatting limits, fees, and transparency/data policies change over
time. Always confirm current requirements on the official ISR submission guidelines (INFORMS PubsOnline)
before submitting. See `official-source-map.md` for every URL and access date.
