# External Tools & Resources for JoC-Style Communication Research

Data sources, software, and packages useful when preparing a *Journal of Communication* (JoC)
submission. JoC is the **flagship, generalist journal of the International Communication Association**:
a submission may be quantitative (surveys, experiments, content analysis), computational/text-as-data,
qualitative, or critical/interpretive, drawn from communication theory and methodology, media effects,
political communication, health communication, computational communication, or interpersonal /
organizational communication. Match tools to your subfield and design. Check licenses and current
access terms before use, and verify any JoC-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by tradition

### Media effects, political & health communication (survey / panel)
| Source | Provider | Typical use |
|--------|----------|-------------|
| ANES / CES (CCES) | Michigan-Stanford / Harvard | Political communication, campaign exposure, vote choice |
| Pew Research Center datasets | Pew | News use, social media, audience attitudes |
| General Social Survey (GSS) | NORC | Long-run media/attitude trends |
| Health Information National Trends Survey (HINTS) | NCI | Health communication, information seeking |
| World/European Values Surveys, Eurobarometer | Various | Cross-national media and opinion |

### Computational / text-as-data
| Source | Provider | Typical use |
|--------|----------|-------------|
| Social-media APIs / academic access (where permitted) | Platforms | Posts, networks, diffusion (mind ToS + ethics) |
| GDELT, Media Cloud | GDELT / Media Cloud | News coverage at scale, agenda dynamics |
| Comparative Agendas Project | CAP | Policy/news attention over time |
| News archives (LexisNexis, ProQuest) | Vendors | Content analysis corpora |

### Qualitative / critical
| Source | Provider | Typical use |
|--------|----------|-------------|
| Interviews, focus groups, ethnographic fieldnotes | Author-collected | Audience reception, production studies |
| Archives / media texts / platform artifacts | Various | Critical/cultural and discourse analysis |
| QDR (Qualitative Data Repository) | Syracuse | Sharing/citing qualitative data with access controls |

## 2. Software by method

### R
- Experiments/surveys: `survey`, `cregg`/`cjoint` (conjoint), `emmeans`, `marginaleffects`, `pwr`/`Superpower` (power)
- Content analysis & reliability: `irr`, `tidycomm` (ICR), `irrCAC` (Krippendorff's alpha, Gwet's AC)
- Text-as-data: `quanteda`, `stm` (structural topic models), `text2vec`, `tidytext`; embeddings/LLM pipelines
- Mediation/moderation/SEM: `lavaan`, `mediation`, `processR` (PROCESS-style), `semTools`
- Multilevel/panel: `lme4`, `nlme`; networks: `igraph`, `statnet`/`ergm`
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### SPSS / Mplus / Stata
- SPSS + **PROCESS macro** (Hayes) — common in media-effects mediation/moderation work
- **Mplus** / `lavaan` — SEM, latent-variable measurement, longitudinal models
- Stata: `reghdfe`, `ivreg2`, `coefplot`; `kappaetc` for intercoder agreement

### Python
- `pandas`, `numpy`, `statsmodels`, `pingouin`
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers`, `gensim`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, documents, media texts
- Reflexivity, audit trails, and transparent coding schemes for trustworthiness

## 3. Open science, preregistration & transparency
- Preregistration / registered analyses: **OSF Registries**, AsPredicted; note pre-registration in the
  **cover letter**; JoC supports **Open Science Badges** for **open data, open materials, and
  preregistration**
- **Data Availability Statement** is **required** — prepare it as you write (see
  `joc-open-science-and-transparency`)
- Power/design: a-priori power analysis for experiments and surveys; simulation-based power for
  multilevel and conjoint designs
- Content-analysis transparency: codebook, intercoder-reliability report, and coded data deposited where ethics allow

## 4. Figures & exhibits (JoC rewards clear, accessible exhibits)
- Coefficient/forest plots (`ggplot2`/`broom`, `coefplot`), marginal-effects and predicted-probability
  plots (`marginaleffects`), conjoint AMCE plots, mediation path diagrams
- Reliability and agreement summaries; corpus/topic-model diagnostics for computational work
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **APA 7th edition** (author-date);
  keep a single consistent style
- Typesetting: **Microsoft Word (.docx)** is required by JoC (PDF not accepted); 12-pt Times New Roman,
  double-spaced, 1.0-inch margins
- Prepare a **double-anonymous** main document (no names/affiliations/acknowledgments, third-person
  self-citation, stripped file metadata) plus a separate title page

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Manuscript Central** (`mc.manuscriptcentral.com/jcom`) — confirm current URL |
| Society / publisher | **ICA** / **Oxford University Press** |
| Review model | **Double-anonymous** — anonymize the main document and supplemental materials |
| Formats | Original research articles · occasional special issues · **JoC Forum** (3,000–6,000 words) |
| Length | Main document **≤ 35 pages** (incl. abstract, text, references, tables, figures, endnotes); abstract **≤ 150 words** |
| Style | **APA 7th edition**; Word (.docx), 12-pt Times New Roman, double-spaced |
| Submission fee | None stated (verify); hybrid **open-access APC** handled by OUP after acceptance |
| Data policy | **Data Availability Statement required**; Open Science Badges for open data/materials/preregistration |

## 7. Cautions
1. **Verify volatile specifics** (editors, exact caps, fee/APC, accepted formats, open-science wording)
   on the official OUP/ICA pages — they change; unverified items are marked 待核实.
2. **Anonymize properly** — JoC is double-anonymous; remove identifiers from the main document *and*
   supplemental materials, and write self-citations in the third person.
3. **Match method to tradition** — JoC judges quantitative, computational, qualitative, and critical
   work on its own terms; do not force a single template onto every paper.
4. **Prepare the Data Availability Statement and any badge materials as you go** — the statement is a
   submission requirement, not an afterthought.
5. **Speak to communication broadly** — a JoC paper should matter beyond a single subfield or platform.
