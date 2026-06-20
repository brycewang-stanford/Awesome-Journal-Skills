# International-Business Research Tools & Resources (JIBS)

This document lists external data sources, analysis software, and writing tools
commonly used when preparing a manuscript for the **Journal of International Business
Studies (JIBS)**. Because JIBS studies cross-border, multi-country, and multilevel
phenomena, the toolkit is organized around two distinctive needs that ordinary
single-country management work does not face: (1) assembling and harmonizing
**cross-country** data across heterogeneous national sources, and (2) defending
**measurement equivalence** and **multilevel** structure when constructs travel
across countries and cultures. Always verify licensing terms and the current
JIBS/AIB and DART transparency policies before using any resource.

## 1. Cross-country & MNE data sources

### Country-level institutional, cultural, and macro data
| Source | Provider | Typical IB use |
|--------|----------|----------------|
| Hofstede / GLOBE / Schwartz culture scores | Hofstede Insights / GLOBE / Schwartz | Cultural-distance and cross-cultural constructs |
| World Bank WDI / WGI | World Bank | Macro controls; Worldwide Governance Indicators |
| IMF, OECD, UNCTAD (incl. FDI stocks/flows) | IMF / OECD / UNCTAD | Trade, FDI, institutional/economic context |
| Worldwide Governance / Economic Freedom / Polity | Various | Institutional quality, political risk |
| CEPII (gravity, distance, common language) | CEPII | Bilateral distance, gravity-model covariates |
| KOF Globalisation Index | ETH Zurich | Globalization exposure by country-year |

### MNE / firm and subsidiary data (multi-country)
| Source | Provider | Typical IB use |
|--------|----------|----------------|
| Orbis / Amadeus | Bureau van Dijk | Global firm- and subsidiary-level financials |
| Compustat Global / Worldscope | S&P / LSEG | Cross-listed and non-US firm financials |
| Thomson/Refinitiv SDC (cross-border M&A, JVs, alliances) | LSEG | Entry mode, FDI deals, alliances |
| PATSTAT / USPTO / EPO | EPO / USPTO | Cross-border innovation, patent flows |
| fDi Markets | Financial Times | Greenfield FDI projects by location |

### Survey / micro and cross-national panels
| Source | Provider | Typical IB use |
|--------|----------|----------------|
| World Values Survey / Hofstede modules | WVS / IVS | Individual-level cultural values |
| GEM (Global Entrepreneurship Monitor) | GEM | Cross-national entrepreneurship rates |
| Manager/subsidiary surveys (Qualtrics, multi-language) | Various | Primary cross-country survey data |

> Cross-country merges hinge on consistent country and currency coding (ISO-3166, ISO-4217), year alignment, and documented handling of country-name changes; keep a transparent country-year key.

## 2. Analysis software & packages (matched to JIBS rigor demands)

### Measurement equivalence / invariance (a first-order JIBS concern)
- **Mplus** — multi-group CFA, configural/metric/scalar invariance, alignment method, multilevel SEM.
- **R**: `lavaan` + `semTools` (`measurementInvariance`, `measEq.syntax`), `sirt`/`MIE` for alignment.
- **Stata**: `sem`/`gsem` with group constraints for invariance testing.

### Multilevel / hierarchical models (firm-in-country, individual-in-firm-in-country)
- **R**: `lme4`, `nlme`, `lmerTest`; `multilevel` (ICC, r_wg) for aggregation justification.
- **Stata**: `mixed`, `melogit`, `meqrlogit`; **HLM** software; Mplus for multilevel SEM.

### Endogeneity & causal identification (incl. "dynamic endogeneity")
- **Stata**: `xtreg`/`reghdfe` (FE), `ivreg2`/`ivreghdfe` (IV/2SLS), `xtabond2`/`xtdpdgml` (dynamic-panel GMM for internationalization-as-process), `teffects`/`psmatch2` (matching), `heckman` (selection), `csdid` (modern DiD).
- **R**: `fixest`, `plm`, `pgmm` (dynamic panel), `MatchIt`, `sandwich` (clustered/robust SE).

### Common-method-variance (CMV) checks
- Marker-variable and unmeasured-latent-method-factor models in **Mplus** / `lavaan`; CFA-based Harman alternatives. (A single-factor test alone is not sufficient for JIBS — see jibs-data-analysis.)

### Configurational / set-theoretic methods
- **R**: `QCA`, `SetMethods`; **fsQCA** software — increasingly seen in IB and covered by a JIBS methods editorial.

### Qualitative & mixed methods (case-based IB research)
- **NVivo**, **ATLAS.ti**, **Dedoose** for coding; templates for Gioia-style data structures, process models, and cross-case comparison in multi-country case designs.

## 3. Reference & writing tools

| Tool | Note |
|------|------|
| Zotero | Free; configure an author-date (name, year) style to match the JIBS Style Guide |
| EndNote | Broad journal-style support; reconcile against the JIBS Style Guide |
| Mendeley | Elsevier |
| Overleaf / LaTeX | Optional; confirm the submission portal accepts the format |
| DeepL / professional translation | Useful for multi-language survey instruments and back-translation |

The JIBS Style Guide specifies 11-point Times New Roman, double-spaced, with author-date in-text citations; configure your reference manager accordingly and reconcile against the current guide.

## 4. Submission & transparency (JIBS-specific)

- **Submission portal:** JIBS uses the online submission tool at **mc.manuscriptcentral.com**, reached from
  the Springer/AIB JIBS pages; verify the live link before upload.
- **DART / Data Accessibility Statement:** prepare a Data Accessibility Statement describing data availability; where data can be shared, deposit in a reputable repository with a **DOI** (e.g., OSF, ICPSR, Harvard Dataverse, Zenodo) and record the DOI.
- **Code of Ethics:** read the JIBS Code of Ethics before submitting.
- **ORCID:** keep an ORCID linked to your account.
- **Originality:** manuscripts are screened with iThenticate/CrossCheck.

## 5. Reproducibility & transparency

1. Keep clean, commented scripts (do-files, R scripts, Mplus inputs) that regenerate every table and figure, including all country-year merges.
2. Document each country-level source, the sample-construction and country-inclusion rules, and any country-year exclusions.
3. Record measurement-equivalence test results (configural/metric/scalar) as supplementary evidence reviewers will ask for.
4. Prepare an online appendix for additional analyses, robustness, and full invariance/endogeneity diagnostics.
5. Where data can be shared, deposit a de-identified dataset and codebook with a DOI consistent with the DART policy; otherwise, document in the DAS why availability is limited.

## 6. Verify before you rely

Editorial team, submission links, word limits, fees, the optional open-access APC amount, and DART wording
change over time. Always confirm current requirements on the official JIBS submission-guidelines page and
the JIBS Style Guide before submitting.
