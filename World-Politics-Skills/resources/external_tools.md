# External Tools & Resources for World Politics–Style Comparative Politics + IR

Data sources, software, and packages useful when preparing a *World Politics* submission. World Politics
is a **comparative-politics + international-relations specialist** (not a generalist political-science
venue, and not an IR-only journal): a submission typically asks a question that **travels across cases
or systems** and tests it with appropriate methods — comparative-historical, quantitative cross-national,
qualitative/case-based, experimental, or formal-empirical. The journal does **not** publish opinion or
policy pieces, stand-alone political theory, historical articles, or journalistic narratives. Match
tools to your design, check licenses and current access terms, and verify any World Politics policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources for cross-national / comparative + IR questions

### Regimes, institutions, governance (comparative politics)
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Democracy/regime indicators, disaggregated institutions, panel |
| Polity5 | Center for Systemic Peace | Regime authority and transitions over time |
| Freedom House | Freedom House | Civil liberties and political rights, cross-national |
| QoG (Quality of Government) | U. Gothenburg | Compiled cross-country governance/institutions data |
| DPI (Database of Political Institutions) | IDB / World Bank | Electoral rules, party systems, checks and balances |
| Comparative Manifesto Project (CMP/MARPOR) | WZB | Party positions from manifestos across countries |
| CSES | Comparative Study of Electoral Systems | Cross-national survey, electoral behavior |

### Conflict, cooperation, international relations
| Source | Provider | Typical use |
|--------|----------|-------------|
| Correlates of War (COW) | COW Project | Interstate war, alliances, national capabilities, trade |
| UCDP / PRIO | Uppsala / PRIO | Armed conflict and one-sided/non-state violence |
| ACLED | ACLED | Disaggregated political-violence and protest events |
| Polity / Militarized Interstate Disputes (MID) | COW | Dyadic conflict onset and escalation |
| IMF / World Bank WDI | IMF / World Bank | Trade, finance, development covariates |
| Design of Trade Agreements (DESTA) / IO datasets | Various | International institutions and agreements |

### Comparative-historical & qualitative
| Source | Provider | Typical use |
|--------|----------|-------------|
| National archives, state records, party documents | Various | Comparative-historical and process-tracing evidence |
| Elite/expert interviews, fieldwork notes | Author-collected | Case studies, mechanisms, process tracing |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R
- Cross-national panel & causal inference: `plm`, `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`, `sensemakr` (sensitivity)
- Time-series-cross-section: `panelView`, `prais`, panel-corrected SEs (`pcse`), error-correction models
- Measurement/scaling for institutions: `MCMCpack`, latent-variable / IRT models
- Survival/event-history (conflict onset, regime duration): `survival`, `coxme`
- Text-as-data (manifestos, treaties, speeches): `quanteda`, `stm`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `xtreg`, `xtscc` (Driscoll–Kraay), `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreghdfe`
- `stcox`/`streg` (durations), `boottest` (wild-cluster bootstrap), `coefplot`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels` (panel)
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & comparative-historical
- CAQDAS: NVivo, ATLAS.ti, Taguette (open source), MAXQDA — coding interviews, documents, archives
- Process tracing: explicit hypothesis tests (hoop / smoking-gun / straw-in-the-wind); Bayesian process tracing
- Comparative method: QCA (`QCA`, `SetMethods` in R) for set-theoretic cross-case analysis; typological theory
- Transparency: Annotation for Transparent Inquiry (ATI) for active citation of qualitative sources

## 3. Design & transparency
- Preregistration / pre-analysis plans (for experimental or prospective designs): **OSF Registries**, EGAP
- Power/design diagnosis: `DeclareDesign` (declare → diagnose → redesign)
- Replication package destined for the **World Politics Dataverse** for quantitative data — deposited
  **after acceptance, before publication** (see `wp-transparency-and-data-policy`); embargoes up to two
  years may be approved by the editorial committee

## 4. Figures & exhibits
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), marginal-effects and predicted-probability
  plots (`marginaleffects`), event-study and RD plots, survival curves for durations
- Maps for geographic/cross-national variation (`sf`, `tmap`); network diagrams for alliances/trade
- Comparative-historical exhibits: timelines, causal-process diagrams, evidence tables linking claims
  to sources; QCA truth tables and set-relation plots
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — follow the **World Politics Style Sheet**
  (author-date house style); keep one consistent style
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; manuscripts are **double spaced** with the
  **word count indicated**; prepare an **anonymized** manuscript (remove bylines and identifying
  information; remove self-citations where possible) for triple-blind review
- Abstract **≤ 150 words**; main text **≤ 12,500 words including notes and references** (tables,
  figures, and appendixes excluded); online supplementary material **≤ 15 pages**

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **ScholarOne** (`mc.manuscriptcentral.com/wp`) — confirm current URL |
| Sponsor / publisher | **PIIRS, Princeton University** / **Johns Hopkins University Press** (Cambridge through 2022) — 待核实 |
| Review model | **Triple-blind** — anonymize the manuscript (bylines and self-cites removed) |
| Article types | **Research articles** and **review articles** (review articles usually commissioned; all triple-blind reviewed) |
| Length | **≤ 12,500 words incl. notes and references**; tables/figures/appendixes excluded; abstract **≤ 150 words** |
| Online supplement | **≤ 15 pages** |
| Data policy | Quantitative data deposited in the **World Politics Dataverse** after acceptance, before publication; embargoes up to two years by editorial-committee approval |
| Ethics | **APSA Principles and Guidance for Human Subjects Research (2020)** for research engaging human participants |

## 7. Cautions
1. **Verify volatile specifics** (publisher, editors, exact limits, embargo terms, data-policy wording)
   on the official PIIRS/JHU pages — they change; unverified items are marked 待核实.
2. **Travel across cases.** World Politics rewards arguments and mechanisms that generalize beyond a
   single case or country — comparative + IR, not a one-case description and not pure IR theory.
3. **Stay in scope.** No opinion/policy pieces, stand-alone political theory, historical articles, or
   journalistic narratives — these are explicit non-fits.
4. **Anonymize for triple-blind.** Remove bylines and identifying information; remove self-citations
   where possible.
5. **Build the Dataverse package as you go** if you rely on quantitative data — it is deposited after
   acceptance and must let others replicate the exact numerical results.
