# External Tools & Resources for Governance-Style Comparative Governance Research

Data sources, software, and packages useful when preparing a *Governance: An International Journal of
Policy, Administration, and Institutions* submission. *Governance* is a **comparative and international**
venue for **executive politics, public policy, public administration, and the organization of the
state**: a submission may be quantitative, qualitative, comparative-historical, or configurational
(QCA/fsQCA), spanning regulatory governance, bureaucratic and institutional reform, the policy process,
governance networks, accountability, and the state. Match tools to your question and design. Check
licenses and current access terms before use, and verify any *Governance*-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources for comparative governance, policy & administration

### Governance, institutions & state capacity (cross-national panels)
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem (Varieties of Democracy) | University of Gothenburg | Democracy/regime, accountability, state-capacity indicators, panel |
| Quality of Government (QoG) | University of Gothenburg | Compiled cross-country governance, bureaucracy, corruption data |
| Worldwide Governance Indicators (WGI) | World Bank | Six aggregate governance dimensions (voice/accountability, government effectiveness, regulatory quality, rule of law, corruption control, political stability) |
| Bertelsmann Sustainable Governance Indicators (SGI) | Bertelsmann Stiftung | Governance/policy-performance scores across OECD/EU |
| Freedom House / Polity5 | Freedom House / CSP | Regime type, civil liberties, institutional constraints |

### Public policy, agendas & parties
| Source | Provider | Typical use |
|--------|----------|-------------|
| Comparative Agendas Project (CAP) | CAP consortium | Policy-agenda content coded across countries and venues |
| ParlGov | University of Bremen | Parties, elections, cabinets in parliamentary democracies |
| Manifesto Project (CMP/MARPOR) | WZB | Party policy positions from manifestos |
| OECD government & public-finance data | OECD | Government at a Glance, public employment, budgeting, public-sector reform |

### Regulation & regulatory governance
| Source | Provider | Typical use |
|--------|----------|-------------|
| OECD Product Market Regulation (PMR) | OECD | Cross-country indicators of regulatory restrictiveness |
| OECD Indicators of Regulatory Policy and Governance (iREG) | OECD | RIA, stakeholder engagement, ex-post review practices |
| Independent regulatory agency datasets | Various academic | Formal independence / accountability of agencies (verify provenance per study) |

### Qualitative, comparative-historical & administrative
| Source | Provider | Typical use |
|--------|----------|-------------|
| National statistical offices / administrative records | Government bodies | Administrative outcomes, public-sector performance |
| Elite/expert interviews, archival records, fieldwork | Author-collected | Process tracing, case studies, comparative-historical work |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R
- Causal inference (panel): `fixest`, `did` (Callaway–Sant'Anna), `did2s`, `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Configurational analysis: `QCA`, `SetMethods`, `admisc` (crisp-, multi-value, and fuzzy-set QCA; consistency/coverage, robustness)
- Sensitivity / robustness: `sensemakr` (omitted-variable sensitivity), `modelsummary`/`marginaleffects` for reporting
- Measurement/scaling: `MCMCpack`, `emIRT` for latent governance indices
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- `boottest` (wild-cluster bootstrap), `coefplot` for exhibits
- `fuzzy`/`fsqca`-style workflows are typically run in R; document the QCA engine and version

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels` (panel IV / fixed effects)
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`
- Text-as-data where policy documents are the corpus: `spaCy`, `scikit-learn`, `sentence-transformers`

### QCA / fsQCA tools
- **fsQCA** (the dedicated desktop application) and the R **`QCA`** package are the standard engines
- Report calibration thresholds, the truth table, consistency and coverage, and a robustness check on
  thresholds and case membership — configurational claims live or die on transparent calibration

### Qualitative & mixed-methods (CAQDAS)
- **NVivo**, **ATLAS.ti**, **MAXQDA**, **Taguette** (open source) — coding interviews, documents, fieldnotes
- Process tracing: explicit hypothesis tests (hoop / smoking-gun / straw-in-the-wind); document the
  evidentiary logic, not just the narrative

## 3. Transparency, preregistration & deposit
- Replication/reproduction package + a **Data Availability Statement** are central for *Governance*:
  state whether materials are available and how to access them (see `govern-transparency-and-data`)
- DOI-citable repositories (recommended): **OSF**, **Harvard Dataverse**, **Zenodo**; **QDR** for
  access-controlled qualitative data
- Preregistration / pre-analysis plans: **OSF Registries**, EGAP, AsPredicted — *Governance* allows an
  **anonymized pre-analysis plan** as supplementary material; mark registered vs. exploratory analyses

## 4. Figures & exhibits
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  plots (`marginaleffects`); for QCA, XY plots of consistency/coverage and solution tables
- Maps for cross-national variation (`sf`, `tmap`); network diagrams for governance-network structure
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — keep one consistent style; confirm the current
  *Governance* reference style on the live author guidelines (待核实 in `official-source-map.md`)
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **double-blind** manuscript
  (no identifying metadata, no obvious self-references) plus a **separate title page**
- Put the **word count on the title page**; provide an ORCID iD per Wiley norms (待核实)

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Wiley submission system ("Wiley Authors" / Research Exchange)** — confirm current URL (检索于 2026-06；older sources reference ScholarOne — verify live) |
| Owner / publisher | In association with **IPSA SOG (RC27)** / **Wiley(-Blackwell)** |
| Review model | **Double-blind** — at least two referees review anonymously; anonymize the manuscript + separate title page |
| Article length | **≤ 9,000 words excluding citations/bibliography** (official working cap; a third-party listing says 3,000–5,000 — 待核实); abstract **~150 words** |
| Data policy | **Data Availability Statement required**; DOI-citable deposit recommended; anonymized pre-analysis plan may be supplied as supplementary material |
| Submission fee | None stated; any open-access APC handled by Wiley after acceptance (待核实) |

## 7. Cautions
1. **Verify volatile specifics** (editors, exact word/abstract caps, submission portal, fee/APC,
   reference style, ORCID) on the official Wiley/IPSA SOG pages — they change; unverified items are
   marked 待核实.
2. **Anonymize properly** — *Governance* is double-blind; strip author metadata and obvious
   self-references, and supply a separate title page.
3. **Match method to question** — *Governance* judges quantitative, qualitative, comparative-historical,
   and configurational work on its own terms; do not force a single template onto every paper.
4. **Mind the scope guard** — **corporate governance** and stand-alone **literature reviews /
   bibliometric analyses** are out of scope; do not pitch them here. Distinguish *Governance* from its
   Wiley sibling **Regulation & Governance** (regulatory studies) and from **PAR / JPART / JPAM**.
5. **Write the Data Availability Statement honestly** — it is a mandatory statement; deposit replication
   materials in a DOI-citable repository where you can, and explain access restrictions where you cannot.
