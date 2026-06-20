# Entrepreneurship-Research Tools & Resources (JBV)

This document lists external data sources, analysis software, and writing tools commonly used when preparing an entrepreneurship manuscript for the **Journal of Business Venturing (JBV)**. JBV is methodologically pluralistic — it publishes econometric work on novel venture datasets, experiments, qualitative process studies, and mixed methods — so the toolkit spans several traditions. The unifying demand is that the work advance theory about the **entrepreneurial phenomenon**, so choose tools that fit a venture-creation question, not a method for its own sake. Always verify licensing terms and current JBV/Elsevier policies before using any resource.

## 1. Data Sources

### Entrepreneurship & new-venture data
| Source | Provider | Typical use |
|--------|----------|-------------|
| GEM (Global Entrepreneurship Monitor) | GEM Consortium | Cross-national entrepreneurship rates, nascent activity |
| PSED I/II (Panel Study of Entrepreneurial Dynamics) | U. Michigan / consortium | Nascent entrepreneurs, gestation activities |
| Kauffman Firm Survey (KFS) | Kauffman Foundation | New-firm formation, financing, survival |
| PitchBook | Morningstar | VC/PE deals, valuations, exits |
| Crunchbase | Crunchbase | Startups, funding rounds, founders |
| VentureXpert / Refinitiv (SDC) | LSEG | Venture capital, IPOs, M&A exits |
| Orbis / Amadeus | Bureau van Dijk | Global firm-level founding and ownership data |
| Census BDS / LBD / LEHD | US Census Bureau | Firm entry/exit, job creation by young firms |

### Crowdfunding, accelerators & ecosystems
| Source | Use |
|--------|-----|
| Kickstarter / Indiegogo (scraped or API) | Reward crowdfunding campaigns, backer behavior |
| Kiva / LendingClub | Microfinance, peer-to-peer venture lending |
| AngelList / Wellfound | Angel investment, early-stage hiring |
| Y Combinator / accelerator cohorts | Cohort-based ecosystem and selection studies |
| USPTO / PatentsView | Founder/venture innovation, patents, citations |

### Cognition, behavior & survey/experiment data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Prolific / MTurk / CloudResearch | Various | Entrepreneurial decision experiments, conjoint, vignettes |
| Qualtrics | Qualtrics | Founder/team surveys, scale administration |
| LinkedIn / job postings | Various | Founding-team formation, mobility into entrepreneurship |

## 2. Analysis Software & Packages

### Quantitative entrepreneurship econometrics
- **Stata**: `xtreg`/`reghdfe` (panel/high-dimensional FE on venture panels), `ivreg2`/`ivreghdfe` (IV/2SLS for endogenous founding choices), `did`/`csdid` (modern DiD for policy/ecosystem shocks), `streg`/`stcox` (venture survival/hazard), `heckman` and `teffects`/`psmatch2` (selection into entrepreneurship).
- **R**: `fixest`, `plm`, `survival`, `did`, `MatchIt`, `sandwich` (clustered/robust SE).
- **Count/limited DV** (counts of ventures, funding events): Poisson/negative binomial, logit/probit, Tobit, zero-inflated models.

### Selection, survival & rare-outcome modeling
- Survival/event-history for venture exit, IPO, and failure (Cox, parametric AFT, competing risks).
- Heckman / Roy-type selection models for the choice to found and for survivorship bias in venture samples.

### Experiments & cognition
- Power analysis: **G*Power**, R `pwr` / `simr` (simulation-based power for interactions).
- Conjoint / metric-conjoint and policy-capturing designs for entrepreneurial judgment (e.g., R `cjoin`, `conjoint`).
- Pre-registration: **AsPredicted**, **OSF Registries**.

### Qualitative & mixed methods (process / narrative)
- **NVivo**, **ATLAS.ti**, **Dedoose** — coding of founder interviews and venture cases.
- Templates for Gioia-method data structures, process models, and narrative/interpretive theorizing — appropriate given JBV's stated openness to "theories, narratives, and interpretations."
- **fsQCA** (fuzzy-set Qualitative Comparative Analysis) for configurational venture-condition studies.

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Mendeley | Elsevier-native; CSL templates for Elsevier journal styles |
| Zotero | Free; supports numbered and Elsevier journal styles |
| EndNote | Broad journal style support |
| Overleaf / LaTeX | Optional; submit editable source files and follow the current Guide for Authors file requirements |
| Grammarly | Language polish |

JBV allows flexible reference formatting at first submission if each reference is complete and the style is consistent. The current Guide for Authors says the journal style after acceptance uses numbered references in square brackets, so reconcile references against the live guide before revision or proof.

## 4. Submission & Process

- **Submission portal**: Elsevier **Editorial Manager** (editorialmanager.com/jbvi) — verify the current link on the official ScienceDirect JBV page.
- **Co-submission**: Data in Brief / MethodsX artifacts can be attached on the "Attach files" page in Editorial Manager.
- **Anonymization**: prepare a separate title page and an anonymized manuscript (no author names, affiliations, or acknowledgements; third-person self-citation).
- **Declarations**: include a declaration of competing interest, CRediT author-contribution statement, and generative-AI disclosure statement if AI tools were used.
- **Highlights**: submit 3 to 5 article highlights, each no more than 85 characters including spaces.
- **Graphical abstract**: encouraged but optional; submit as a separate file if used.
- **ORCID**: keep an ORCID linked to your Editorial Manager account.

## 5. Reproducibility & Transparency

1. Keep clean, commented scripts (do-files, R scripts) that regenerate every table/figure.
2. Document venture-sample construction, survivorship/selection handling, and exclusion rules — critical given high attrition in new-venture panels.
3. Prepare a data availability statement explaining where data are deposited and cited, or why sharing is not possible (e.g., proprietary VC or confidential founder data).
4. Deposit de-identified data and a codebook when legally possible, consistent with JBV's Elsevier Option C research-data policy.
5. Verify all licensing and confidentiality terms (PitchBook, Crunchbase, proprietary VC data) before depositing or sharing.

## 6. Verify Before You Rely

Editorial team, area-editor domains, submission links, formatting expectations, APC, and transparency/data policies change over time. Always confirm current requirements on the official JBV Guide for Authors, editorial-board page, open-access page, and Editorial Manager portal before submitting.
