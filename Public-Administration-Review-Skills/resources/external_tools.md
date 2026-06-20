# External Tools & Resources for PAR-Style Public Administration

Data sources, software, and packages useful when preparing a *Public Administration Review* (PAR)
submission. PAR is the **practice-bridging flagship of public administration**: a submission may be
quantitative, experimental, qualitative, or mixed-methods, drawn from public personnel/HR, public
budgeting & finance, performance management, collaborative governance, public service motivation,
bureaucratic behavior, or policy implementation. Match tools to your subfield and design. Check
licenses and current access terms before use, and verify any PAR-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by subfield

### Government, personnel & management
| Source | Provider | Typical use |
|--------|----------|-------------|
| FedScope / OPM data | U.S. Office of Personnel Management | Federal workforce, turnover, demographics |
| Federal Employee Viewpoint Survey (FEVS) | OPM | Employee engagement, satisfaction, PSM proxies |
| Census of Governments / ASPEP | U.S. Census Bureau | State & local employment, payroll, finances |
| Government Finance (Annual Survey of State & Local Gov't Finances) | U.S. Census Bureau | Budgeting, revenue/expenditure |
| USASpending.gov | U.S. Treasury | Federal awards, grants, contracts |

### Performance, governance & cross-national
| Source | Provider | Typical use |
|--------|----------|-------------|
| Worldwide Governance Indicators (WGI) | World Bank | Cross-national governance quality |
| Quality of Government (QoG) | U. Gothenburg | Compiled cross-country governance data |
| V-Dem | U. Gothenburg | Democracy/state-capacity indicators |
| COPLAC / state performance dashboards | Various states | Agency performance measurement |
| Local Government surveys (ICMA) | ICMA | Management practices, service delivery |

### Surveys, experiments & qualitative
| Source | Provider | Typical use |
|--------|----------|-------------|
| Original bureaucrat/manager surveys | Author-collected | Managerial behavior, decision experiments |
| Citizen/coproduction surveys | Author-collected / panels | Citizen-state interaction, satisfaction |
| Elite/expert interviews, fieldwork | Author-collected | Process tracing, implementation cases |
| Qualitative Data Repository (QDR) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R
- Causal inference: `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`
- Experiments: `cregg`/`cjoint` (conjoint), `DeclareDesign`, `ri2` (randomization inference), `sensemakr`
- Multilevel / SEM (common in PA): `lme4`, `lavaan`, `brms`
- Measurement / scaling: `psych`, `MplusAutomation`
- Text-as-data: `quanteda`, `stm`; reproducibility: `renv`, `targets`

### Stata
- `reghdfe`, `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- `mixed`/`meglm` (multilevel), `sem`/`gsem` (SEM), `boottest` (wild-cluster bootstrap), `coefplot`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels`; `DoubleML` for DML
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, documents, fieldnotes
- Process tracing: explicit hypothesis tests (hoop / smoking-gun / straw-in-the-wind)

## 3. Transparency, pre-registration & reporting (PAR is a TOP signatory)
- Pre-registration / pre-analysis plans: **OSF Registries**, AsPredicted, EGAP; PAR supports
  pre-registration **badges** — register before data collection and mark registered vs. exploratory
- Data sharing: **Dataverse** (quantitative) and the **Qualitative Data Repository (QDR)** (qualitative)
- Reporting standards PAR recommends documenting against: **CONSORT** (experiments), **STROBE**
  (observational), **PRISMA** (reviews), **COREQ** (qualitative)
- Keep a supplementary document of research-design, data-prep, and analysis decisions

## 4. Figures & exhibits (translate effects for managers)
- Coefficient/forest plots, event-study and RD plots, **marginal-effects / predicted-probability**
  plots (`marginaleffects`) — express magnitudes in managerial terms
- Maps for cross-jurisdiction variation (`sf`, `tmap`); network diagrams for collaborative governance
- Colorblind-safe palettes; legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **APA author–date** (confirm edition)
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **double-blind** manuscript
  (no identifying metadata, prior work in the third person) plus a separate title page
- Draft the **Evidence for Practice** (3–5 practitioner takeaways) alongside the contribution

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** (`editorialmanager.com/par`) per the PAR submission page; some guidance/seed cite **ScholarOne** — confirm the live URL. 待核实 |
| Owner / publisher | **ASPA** / **Wiley** |
| Review model | **Double-blind** — anonymize the manuscript |
| Article types | Scholarly Take · Conceptualizing PA · Early Career Intel · Practically Speaking · Public Administration in Print |
| Length | **≤ 8,000 words** incl. abstract/endnotes/references; tables/figures/appendices excluded; abstract **≤ 150 words** |
| Evidence for Practice | **3–5** takeaway points; encouraged at submission, required at revision |
| Submission fee | None stated (verify); any open-access APC handled by Wiley after acceptance. 待核实 |
| Data policy | TOP-guideline transparency; Dataverse/QDR; data-availability statement |

## 7. Cautions
1. **Verify volatile specifics** (editors, exact caps, fee/APC, portal, data-policy wording) on the
   official Wiley/ASPA pages — they change; unverified items are marked 待核实.
2. **Anonymize properly** — PAR is double-blind; strip author metadata and refer to prior work in the
   third person.
3. **Match method to subfield** — PAR judges quantitative, experimental, qualitative, and mixed work on
   its own terms; do not force a single template onto every paper.
4. **Build transparency materials as you go** — PAR is a TOP signatory; prepare the data-availability
   statement and repository deposit early.
5. **Bridge research and practice** — every PAR article needs honest Evidence for Practice, not
   decorative takeaways.
