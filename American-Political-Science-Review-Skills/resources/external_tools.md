# External Tools & Resources for APSR-Style Political Science

Data sources, software, and packages useful when preparing an *American Political Science Review*
(APSR) submission. APSR is a **discipline-wide generalist** journal: a submission may be quantitative,
qualitative, formal/game-theoretic, experimental, computational, or interpretive, drawn from
American politics, comparative politics, international relations, political theory, public policy, or
political methodology. Match tools to your subfield and design. Check licenses and current access
terms before use, and verify any APSR-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by subfield

### American politics
| Source | Provider | Typical use |
|--------|----------|-------------|
| ANES (American National Election Studies) | Michigan/Stanford | Vote choice, opinion, participation |
| CCES / CES (Cooperative Election Study) | Harvard | Large-N US survey, district-level analysis |
| General Social Survey (GSS) | NORC | Long-run US social/political attitudes |
| Voteview / DW-NOMINATE | UCLA | Congressional roll-call ideal points |
| FEC / DIME (Bonica) | FEC / Stanford | Campaign finance, donor ideology |

### Comparative politics & IR
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Democracy/regime indicators, panel |
| Polity5 / Freedom House | CSP / Freedom House | Regime type and civil liberties |
| CSES | Comparative Study of Electoral Systems | Cross-national survey, electoral behavior |
| Correlates of War (COW) | COW Project | Interstate conflict, alliances, capabilities |
| ACLED / UCDP | ACLED / Uppsala | Conflict events and fatalities |
| Manifesto Project (CMP/MARPOR) | WZB | Party positions from manifestos |
| QoG (Quality of Government) | U. Gothenburg | Compiled cross-country governance data |

### Political theory & qualitative
| Source | Provider | Typical use |
|--------|----------|-------------|
| Archives / primary texts | Various | Interpretive and historical work |
| Elite/expert interviews, fieldwork notes | Author-collected | Process tracing, case studies |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R (dominant in political methodology)
- Causal inference: `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Survey/experiments: `survey`, `cregg`/`cjoint` (conjoint), `DeclareDesign` (design diagnosis), `ri2` (randomization inference), `sensemakr` (sensitivity)
- Measurement/IRT/scaling: `emIRT`, `MCMCpack`, `wnominate`, `pscl`
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
- Preregistration / pre-analysis plans: **OSF Registries**, EGAP, AsPredicted; for APSR, share the
  **anonymized** plan in an appendix or via an OSF link and mark registered vs. exploratory analyses
- Power/design: `DeclareDesign` (declare → diagnose → redesign), simulation-based power for clustered
  and conjoint designs
- Replication/reproduction package destined for the **APSR Dataverse on Harvard Dataverse**
  (see `apsr-transparency-and-data-policy`)

## 4. Figures & exhibits (APSR rewards clear, accessible exhibits)
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  and predicted-probability plots (`marginaleffects`), conjoint AMCE plots
- Maps for geographic variation (`sf`, `tmap`); network diagrams where structure matters
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **APSA Style Manual for
  Political Science** (author-date); keep a single consistent style
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **double-anonymous** manuscript
  (no identifying metadata, no obvious self-references) plus a separate title page
- Include a **word count on the front page**; an ORCID iD for the corresponding author

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** (`editorialmanager.com/apsr`) — confirm current URL |
| Owner / publisher | **APSA** / **Cambridge University Press** |
| Review model | **Double-anonymous** — anonymize the manuscript |
| Tracks | Regular Articles · Research Notes · Replications and Reappraisals · Syntheses · Registered Reports |
| Article length | Most Articles **< 11,000 words**; Research Notes **< 7,000 words**; abstract **≤ 150 words** |
| Submission fee | None stated (verify); any open-access APC handled by Cambridge after acceptance |
| Data policy | Reproducibility package to the **APSR Dataverse** after **conditional acceptance**, verified by the editorial office |

## 7. Cautions
1. **Verify volatile specifics** (editors, exact caps, fee/APC, accepted tracks, data-policy wording)
   on the official APSA/Cambridge pages — they change; unverified items are marked 待核实.
2. **Anonymize properly** — APSR is double-anonymous; strip author metadata and obvious self-references.
3. **Match method to subfield** — APSR judges quantitative, qualitative, formal, and interpretive work
   on its own terms; do not force a single template onto every paper.
4. **Build the reproducibility package as you go** — it is verified by the editorial office at
   conditional acceptance, not waved through.
5. **Write for the whole discipline** — an APSR paper must speak past its subfield to a general
   political-science audience.
