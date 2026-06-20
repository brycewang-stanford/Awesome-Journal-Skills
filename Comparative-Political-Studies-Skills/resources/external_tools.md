# External Tools & Resources for CPS-Style Comparative Politics

Data sources, software, and packages useful when preparing a *Comparative Political Studies* (CPS)
submission. CPS is a **comparative-politics** journal and methodologically pluralist: a submission may be
large-N quantitative/causal, formal/game-theoretic, qualitative/comparative-historical, experimental, or
multi-method, drawn from democratization & regimes, institutions, behavior & participation, ethnic
politics & conflict, comparative political economy, or parties & elections. Match tools to your subfield
and design. Check licenses and current access terms before use, and verify any CPS-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Comparative data sources by theme

### Regimes, democracy & governance
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Democracy/regime indicators, fine-grained panel |
| Polity5 | Center for Systemic Peace | Regime type / authority characteristics |
| Freedom House | Freedom House | Civil liberties and political rights |
| QoG (Quality of Government) | U. Gothenburg | Compiled cross-country governance data |
| World Bank WGI / WDI | World Bank | Governance and development indicators |

### Behavior, parties & elections
| Source | Provider | Typical use |
|--------|----------|-------------|
| CSES | Comparative Study of Electoral Systems | Cross-national survey, electoral behavior |
| Manifesto Project (CMP/MARPOR) | WZB | Party positions from manifestos |
| ParlGov / CLEA | ParlGov / Constituency-Level Elections | Parties, elections, government composition |
| Comparative Political Data Set (CPDS) | U. Zurich/Bern | Institutions and politico-economic variables, OECD |
| World/European/Regional Values Surveys | WVS/EVS | Cross-national attitudes and values |

### Conflict & ethnic politics
| Source | Provider | Typical use |
|--------|----------|-------------|
| ACLED | ACLED | Conflict events and fatalities |
| UCDP / PRIO | Uppsala / PRIO | Armed conflict, battle deaths |
| EPR (Ethnic Power Relations) | ETH Zurich | Ethnic group access to power |
| Correlates of War (COW) | COW Project | Interstate conflict, alliances, capabilities |

### Political economy & development
| Source | Provider | Typical use |
|--------|----------|-------------|
| Penn World Table | Groningen | Cross-country output, prices, productivity |
| OECD / IMF / World Bank | OECD/IMF/WB | Fiscal, welfare, macro panels |
| LIS (Luxembourg Income Study) | LIS | Comparable household income/inequality |

### Qualitative & comparative-historical
| Source | Provider | Typical use |
|--------|----------|-------------|
| Archives / primary texts | Various | Interpretive and historical-comparative work |
| Elite/expert interviews, fieldwork notes | Author-collected | Process tracing, paired case studies |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R (dominant in comparative methodology)
- Causal inference: `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Panel / few-cluster: `plm`, `clubSandwich` (CR2/CR3), `fwildclusterboot` (wild-cluster bootstrap)
- Survey/experiments: `survey`, `cregg`/`cjoint` (conjoint), `DeclareDesign`, `ri2` (randomization inference), `sensemakr`
- Measurement/scaling: `MCMCpack`, `emIRT`, `wnominate`; QCA: `QCA`, `SetMethods`
- Text-as-data: `quanteda`, `stm`; networks: `igraph`, `statnet`/`ergm`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), `coefplot`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, documents, fieldnotes
- Process tracing: explicit tests (hoop / smoking-gun / straw-in-the-wind); Bayesian process tracing
- QCA (fuzzy/crisp set) for medium-N configurational comparison
- Transparency: Annotation for Transparent Inquiry (ATI) for active citation of qualitative sources

## 3. Preregistration, design & transparency
- Preregistration / pre-analysis plans: **OSF Registries**, EGAP, AsPredicted; for CPS, the anonymized
  plan is **optional** and submitted as **supplementary material** (mark registered vs. exploratory)
- Power/design: `DeclareDesign` (declare → diagnose → redesign); simulation-based power for clustered
  and conjoint designs
- Replication/reproduction package destined for the **CPS Dataverse on Harvard Dataverse**
  (`dataverse.harvard.edu/dataverse/cps`) — gates final acceptance for quantitative papers
  (see `cps-transparency-and-data`)

## 4. Figures & exhibits (CPS rewards comparative-legible exhibits)
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  and predicted-probability plots (`marginaleffects`), conjoint AMCE plots
- Small multiples and sorted dot plots for cross-country comparison; maps (`sf`, `tmap`) only when
  geography is the point
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **APA-style author-date** (SAGE house);
  keep a single consistent style; ensure in-text cites and the list agree exactly
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare an **anonymized** manuscript (no
  identifying metadata or obvious self-references) plus a separate title page
- Link the **ORCID** for the submitting author in SAGE Track

## 6. Process & portal
| Item | Note (检索于 2026-06；以官网为准) |
|------|------|
| Submission portal | **SAGE Track (ScholarOne)** — reuse an existing account if you reviewed/authored within the past year |
| Publisher | **SAGE Publications** (CPS since 1968) |
| Review model | **Anonymous** — anonymize the manuscript; identifying info on a separate title page |
| Article length | Articles **max 11,000 words**; references, tables, figures **excluded**; abstract **~150 words, unstructured** |
| References | **APA-style author-date** |
| Identifiers | **ORCID required for the submitting author** |
| Submission fee | None stated (verify); any open-access APC handled by SAGE after acceptance |
| Data policy | Quantitative papers deposit replication materials to the **CPS Dataverse**; **data availability statement** required |

## 7. Cautions
1. **Verify volatile specifics** (editors, exact caps, fee/APC, data-policy wording, reference style) on
   the official SAGE page — they change; unverified items are marked 待核实.
2. **Anonymize properly** — CPS uses anonymous review; strip author metadata and obvious self-references.
3. **Show comparative leverage** — match the data and design to a genuinely comparative claim, not a
   single-case snapshot.
4. **Handle few-clusters honestly** — with a small number of countries, default SEs over-reject; use
   wild-cluster bootstrap or randomization inference.
5. **Build the replication package as you go** — for quantitative papers it gates final acceptance at the
   CPS Dataverse, not waved through at the end.
