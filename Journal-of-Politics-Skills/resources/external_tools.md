# External Tools & Resources for JOP-Style Political Science

Data sources, software, and packages useful when preparing a submission to *The Journal of Politics*
(JOP). JOP is a **general-interest, methodologically diverse** journal: a submission may be empirical,
experimental, formal/game-theoretic, computational, qualitative, or normative, drawn from American
politics, comparative politics, formal theory, international relations, methodology, political theory,
public administration, or public policy. Match tools to your subfield and design, and remember JOP's
two operational constraints — a **page budget** (not a word count) and a **replication-analyst** check
at conditional acceptance. Check licenses and current access terms before use, and verify any
JOP-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Data sources by subfield

### American politics
| Source | Provider | Typical use |
|--------|----------|-------------|
| ANES (American National Election Studies) | Michigan/Stanford | Vote choice, opinion, participation |
| CES / CCES (Cooperative Election Study) | Harvard | Large-N US survey, district-level analysis |
| General Social Survey (GSS) | NORC | Long-run US social/political attitudes |
| Voteview / DW-NOMINATE | UCLA | Congressional roll-call ideal points |
| FEC / DIME (Bonica) | FEC / Stanford | Campaign finance, donor ideology |

### Comparative politics & IR
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Democracy/regime indicators, panel |
| Polity5 / Freedom House | CSP / Freedom House | Regime type and civil liberties |
| CSES | Comparative Study of Electoral Systems | Cross-national electoral behavior |
| Correlates of War (COW) | COW Project | Interstate conflict, alliances, capabilities |
| ACLED / UCDP | ACLED / Uppsala | Conflict events and fatalities |
| Manifesto Project (MARPOR/CMP) | WZB | Party positions from manifestos |
| QoG (Quality of Government) | U. Gothenburg | Compiled cross-country governance data |

### Political theory, public policy & qualitative
| Source | Provider | Typical use |
|--------|----------|-------------|
| Archives / primary texts | Various | Interpretive, historical, normative work |
| Elite/expert interviews, fieldwork | Author-collected | Process tracing, case studies |
| Administrative / policy datasets | Govt. agencies | Public administration and policy analysis |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R (dominant in political methodology)
- Causal inference: `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Survey/experiments: `survey`, `cregg`/`cjoint` (conjoint), `DeclareDesign` (design diagnosis), `ri2` (randomization inference), `sensemakr` (sensitivity)
- Measurement/IRT/scaling: `emIRT`, `MCMCpack`, `wnominate`, `pscl`
- Text-as-data: `quanteda`, `stm`, `text2vec`; LLM/embeddings pipelines
- Networks: `igraph`, `statnet`/`ergm`
- Bayesian: `brms`, `rstan`/`cmdstanr`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), `coefplot`
- `estout`/`esttab` for exhibit export; record the **Stata version** for the JOP readme

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, Taguette (open source), MAXQDA — coding interviews, documents, fieldnotes
- Process tracing: explicit hypothesis tests (hoop / smoking-gun / straw-in-the-wind); Bayesian process tracing
- Transparency: active citation / evidence tables; QDR for controlled-access qualitative data

## 3. Fitting the JOP page budget (not a word count)

JOP counts **pages**, not words: Research Articles **≤ 35 pages**, Short Articles **≤ 10 pages**,
**double-spaced, 12-point, one-inch margins**, inclusive of text, notes, references, and exhibits.
- Push robustness grids, derivations, and secondary results into the **Online Appendix (≤ 25 pages)**,
  which is excluded from the 35 — but keep the main text self-standing.
- A dense reference list and large tables eat pages directly; budget them deliberately.
- The **Short Article** route rewards a single crisp contribution — do not pad it toward 35 pages.

## 4. Preregistration, design & transparency
- Preregistration / pre-analysis plans: **OSF Registries**, EGAP, AsPredicted; share the **anonymized**
  plan in the Online Appendix or via an anonymized link for double-blind review
- Power/design: `DeclareDesign` (declare → diagnose → redesign), simulation-based power
- Replication package destined for the **JOP Dataverse on Harvard Dataverse** — built so the JOP
  **replication analyst** can re-run it (see `jop-replication-and-data-policy`)

## 5. Figures & exhibits
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  and predicted-probability plots (`marginaleffects`), conjoint AMCE plots
- Maps for geographic variation (`sf`, `tmap`); network diagrams where structure matters
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print
- Every exhibit must be **regenerated by the deposited code** — no hand-edited final figures

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **JOP Style Guide**; keep one
  consistent style
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **double-blind** anonymous
  manuscript (no names, affiliations, or acknowledgments) plus a separate title/abstract page
- Abstract **≤ 150 words**; **4–5 keywords** below the abstract

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** (`editorialmanager.com/jop`) — confirm current URL |
| Owner / publisher | **SPSA** / **University of Chicago Press** (publisher since Jan 2015) |
| Review model | **Double-blind** — anonymize the manuscript |
| Categories | **Research Article** (≤ 35 pp) · **Short Article** (≤ 10 pp); Online Appendix ≤ 25 pp |
| Length basis | **Pages**, double-spaced 12-pt — *not* a word count (unlike APSR / AJPS) |
| Abstract | **≤ 150 words**, 4–5 keywords |
| Upload-stage charge / OA fee | No separate upload-stage charge identified in the refreshed official snippets; UChicago snippets show an optional open-access request fee of USD 2,500 to confirm on the live page |
| Data policy | Replication package to the **JOP Dataverse**, assessed by a **JOP replication analyst** at conditional acceptance; non-replicable papers are rejected |

## 8. Cautions
1. **Live-check volatile specifics** (editors, exact page limits, fee/APC, categories, data-policy wording)
   on the official UChicago Press / SPSA pages before upload; they change.
2. **Plan for pages, not words** — JOP's page budget is the binding constraint; APSR/AJPS word-count
   habits will mislead you.
3. **Anonymize properly** — JOP is double-blind; strip author metadata and obvious self-references.
4. **Build for the replication analyst** — JOP makes acceptance **contingent on replicability** and a
   JOP analyst re-checks materials at conditional acceptance; unscripted analyses cannot be repaired
   under deadline.
5. **Match method to the question** — JOP judges empirical, formal, qualitative, and normative work on
   its own terms across all subfields.
