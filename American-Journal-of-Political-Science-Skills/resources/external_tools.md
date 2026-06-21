# External Tools & Resources for AJPS-Style Political Science

Data sources, software, and packages useful when preparing an *American Journal of Political Science*
(AJPS) submission. AJPS is a **generalist but quantitatively leaning** political-science journal:
most published work uses statistical, experimental, computational, or formal-empirical methods across
American politics, comparative politics, international relations, political behavior, institutions, and
methodology. Whatever the method, the deposited replication package will be **re-run by a third-party
verifier before publication**, so pick tooling that is scriptable, version-pinnable, and
seed-reproducible from the start. Check licenses and current access terms before use, and verify any
AJPS-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Data sources by subfield

### American politics & political behavior
| Source | Provider | Typical use |
|--------|----------|-------------|
| ANES (American National Election Studies) | Michigan/Stanford | Vote choice, opinion, turnout |
| CES / CCES (Cooperative Election Study) | Harvard | Large-N US survey, district analysis |
| General Social Survey (GSS) | NORC | Long-run US attitudes |
| Voteview / DW-NOMINATE | UCLA | Roll-call ideal points |
| DIME (Bonica) / FEC | Stanford / FEC | Campaign finance, donor ideology |

### Comparative politics & IR
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Democracy/regime indicators, panel |
| CSES | Comparative Study of Electoral Systems | Cross-national electoral behavior |
| Correlates of War (COW) | COW Project | Conflict, alliances, capabilities |
| ACLED / UCDP | ACLED / Uppsala | Conflict events and fatalities |
| Manifesto Project (MARPOR) | WZB | Party positions from manifestos |
| QoG (Quality of Government) | U. Gothenburg | Compiled cross-country governance data |

### Qualitative & multi-method
| Source | Provider | Typical use |
|--------|----------|-------------|
| Elite/expert interviews, fieldnotes, archives | Author-collected | Process tracing, case studies |
| Qualitative repositories / controlled-access archives | Varies | Sharing/citing qualitative data when legal, ethical, and consistent with AJPS exemption rules |

## 2. Software by method (favor scriptable, seedable, version-pinnable tools)

### R (dominant in AJPS quantitative work)
- Causal inference: `fixest`, `did` (Callaway-Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Experiments/surveys: `survey`, `cregg`/`cjoint` (conjoint), `DeclareDesign`, `ri2` (randomization inference), `sensemakr`
- Measurement/IRT/scaling: `emIRT`, `MCMCpack`, `wnominate`, `pscl`
- Text-as-data: `quanteda`, `stm`, `text2vec`; embeddings/LLM pipelines (validate against labeled samples)
- Bayesian: `brms`, `rstan`/`cmdstanr`
- Reproducibility: `renv` (pin versions for the verifier), `targets` (pipelines), `here` (paths)

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), `coefplot`
- Record `version` and `which`/`ssc` install lines so the verifier can reconstruct the environment

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`; `pyfixest` for high-dimensional FE
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze` / a lockfile

### Formal / game-theoretic
- Symbolic math (Mathematica, SymPy) for equilibrium derivations; agent-based / simulation in R/Python
  with reported seeds; tie comparative statics to the empirical test

## 3. Replication-package tooling (built for AJPS third-party verification)
- **readme.txt** that names and describes every file (group as "Data files", "Stata .do files",
  "Files to Reproduce Table 1", etc.)
- A single **master script** that runs the modular scripts in order and sets the working directory once
- **set seed** for every stochastic step (Monte Carlo, bootstrap, jitter); explicit **software-version**
  statements (e.g., "R version 4.3.2", "Stata/MP 18.0")
- Deposit destined for the **AJPS Dataverse on Harvard Dataverse**; the Cornell Center for Social
  Sciences verification route re-runs the code against the **numerical results in the main
  text** (see `ajps-replication-and-verification`)
- Preregistration / pre-analysis plans: **OSF Registries**, EGAP, AsPredicted — share anonymized; mark
  registered vs. exploratory analyses

## 4. Figures & exhibits
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  and predicted-probability plots (`marginaleffects`), conjoint AMCE plots
- Maps (`sf`, `tmap`) for geographic variation; network diagrams (`igraph`, `ggraph`) where structure matters
- Colorblind-safe palettes, grayscale-legible; vector output (PDF/EPS) for print; remember exhibit
  headers and notes **count toward the AJPS word limit**

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **APSA Style Manual for Political
  Science** (rev. 2018, updated 2023) **or** **Chicago Manual of Style (18th ed.)**; references use
  authors' **full first and last names**
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **fully anonymized** manuscript
  (no names, affiliations, acknowledgments, funding, conference mentions; third-person self-citation)
- Double-spaced, 12-point, >= one-inch margins; title page carries the **abstract and word count**

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** (`http://www.editorialmanager.com/ajps/`) — confirm current URL |
| Owner / publisher | **MPSA** / **Wiley** |
| Review model | **Double-blind** — fully anonymize the manuscript |
| Submission types | Article (<= 10,000 words) · Research Note (<= 4,000, methodology/meta-analysis) · Correspondence (<= 4,000) |
| Abstract | **<= 150 words** |
| Supporting Information | **<= 25 pages** for original submissions, uploaded as "Appendix" |
| Verification | Third-party, **pre-publication**, re-runs code vs. main-text numbers; deposit to **AJPS Dataverse** |

## 7. Cautions
1. **Live-check volatile specifics** (portal prompts, Wiley license/APC choices, later policy updates)
   on the official AJPS / MPSA / Wiley pages.
2. **Anonymize fully** — AJPS is double-blind; strip names, affiliations, acknowledgments, funding,
   conference mentions, and first-person self-citations.
3. **Engineer reproducibility from day one** — your code will be **re-run by an independent verifier**
   before publication, not skimmed; seeds, versions, and a master script are not optional.
4. **Match the type to the contribution** — a Research Note is reserved for **methodology and
   meta-analyses**, not a short empirical paper; Correspondence is for critiques of published AJPS work.
5. **Count exhibit text** — table/figure headers and notes and printed footnotes count toward the word
   limit; references and online SI do not.
