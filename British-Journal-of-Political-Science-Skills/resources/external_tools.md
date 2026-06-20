# External Tools & Resources for BJPS-Style Political Science

Data sources, software, and packages useful when preparing a *British Journal of Political Science*
(BJPS / BJPolS) submission. BJPS is a **broad, internationally-oriented generalist** journal: a
submission may be quantitative, qualitative, formal/game-theoretic, experimental, computational, or
interpretive, drawn from comparative politics, international relations, political theory, political
behaviour and public opinion, political economy, or political methodology — and from related disciplines
(sociology, social psychology, economics, philosophy). Match tools to your subfield and design. Check
licenses and current access terms before use, and verify any BJPS-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by subfield (international by design)

### Comparative politics & political economy
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Democracy/regime indicators, panel |
| Polity5 / Freedom House | CSP / Freedom House | Regime type and civil liberties |
| QoG (Quality of Government) | U. Gothenburg | Compiled cross-country governance data |
| Comparative Political Data Set (CPDS) | U. Zurich/Bern | OECD political-economy time series |
| Manifesto Project (CMP/MARPOR) | WZB | Party positions from manifestos |
| Comparative Welfare States / SWIID | various | Welfare effort, inequality (Solt) |

### International relations
| Source | Provider | Typical use |
|--------|----------|-------------|
| Correlates of War (COW) | COW Project | Interstate conflict, alliances, capabilities |
| ACLED / UCDP | ACLED / Uppsala | Conflict events and fatalities |
| KOF Globalisation Index | ETH Zurich | Economic/social/political globalization |
| World Bank WDI / IMF | World Bank / IMF | Macro and development indicators |

### Political behaviour & public opinion (cross-national)
| Source | Provider | Typical use |
|--------|----------|-------------|
| CSES | Comparative Study of Electoral Systems | Cross-national survey, electoral behaviour |
| European Social Survey (ESS) | ESS ERIC | Comparable attitudes across Europe |
| World/European Values Surveys (WVS/EVS) | WVS/EVS | Long-run cross-national values |
| Eurobarometer | European Commission | EU public opinion |
| National election studies (BES, ANES, etc.) | various | Within-country vote choice and opinion |

### Political theory & qualitative
| Source | Provider | Typical use |
|--------|----------|-------------|
| Archives / primary texts | Various | Interpretive and historical work |
| Elite/expert interviews, fieldwork notes | Author-collected | Process tracing, case studies |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R (dominant in political methodology)
- Causal inference: `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Survey/experiments: `survey`, `cregg`/`cjoint` (conjoint), `DeclareDesign`, `ri2` (randomization inference), `sensemakr`
- Measurement/IRT/scaling: `emIRT`, `MCMCpack`, `wnominate`, `pscl`; equivalence testing for cross-national measures
- Text-as-data: `quanteda`, `stm` (structural topic models), `text2vec`; LLM/embeddings pipelines
- Networks: `igraph`, `statnet`/`ergm`
- Bayesian: `brms`, `rstan`/`cmdstanr`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), `coefplot`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, Taguette (open source), MAXQDA — coding interviews, documents, fieldnotes
- Process tracing: explicit hypothesis tests (hoop / smoking-gun / straw-in-the-wind); Bayesian process tracing
- Transparency: Annotation for Transparent Inquiry (ATI) for active citation of qualitative sources

## 3. Preregistration, design & transparency
- Preregistration / pre-analysis plans: **OSF Registries**, EGAP, AsPredicted; share the **anonymized**
  plan in an appendix or via an OSF link and mark registered vs. exploratory analyses
- Power/design: `DeclareDesign` (declare → diagnose → redesign), simulation-based power for clustered
  and conjoint designs
- Replication data + code destined for the **BJPolS Dataverse on Harvard Dataverse** (DA-RT signatory;
  see `bjps-transparency-and-data`)

## 4. Figures & exhibits (size to Cambridge's box; see `bjps-tables-figures`)
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  and predicted-probability plots (`marginaleffects`), conjoint AMCE plots
- Maps for geographic variation (`sf`, `tmap`); network diagrams where structure matters
- Colourblind-safe palettes and figures legible in grayscale; export at ≥ 300 dpi; size tables within
  ~190 × 120 mm and figures within ~200 × 133 mm

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **Cambridge house style**
  (**Harvard author-date**); keep a single consistent style
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or **MS Word**; double-spaced, ≥ 12-point; prepare a
  **double-blind** manuscript (no identifying metadata, no funding notes, no self-references) plus a
  separate title page
- Include an ORCID iD for the corresponding author (待核实 requirement)

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | Editorial Manager (`editorialmanager.com/bjpols`) — confirm current URL (待核实) |
| Owner / publisher | **Cambridge University Press**; associated with the British Academy |
| Review model | **Double-blind**, usually ≥ 2 referees — anonymize the manuscript |
| Formats | Research Articles (~10,000) · Letters (~4,000) · Comments |
| Abstract | **≤ 150 words** (all article types) |
| Submission fee | None stated; **Comments carry no APC**; verify any OA APC for Articles/Letters |
| Data policy | DA-RT signatory; replication data + code to the **BJPolS Dataverse** at acceptance |

## 7. Cautions
1. **Verify volatile specifics** (editors, exact caps, fee/APC, portal URL, data-policy wording) on the
   official Cambridge/BJPS pages — they change; unverified items are marked 待核实.
2. **Anonymize properly** — BJPS is double-blind; strip author metadata, funding notes, website links,
   and obvious self-references.
3. **Match method to subfield** — BJPS judges quantitative, qualitative, formal, and interpretive work
   on its own terms; do not force a single template onto every paper.
4. **Build the replication package as you go** — it is deposited to the BJPolS Dataverse at acceptance.
5. **Write for a broad, international audience** — a BJPS paper must speak past its subfield and its
   country of study.
