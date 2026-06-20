# External Tools & Resources for CR-Style Communication Research

Data sources, software, and packages useful when preparing a *Communication Research* (CR) submission.
CR is SAGE's **quantitative, social-scientific** communication journal: a submission is typically a
**hypothesis-testing experiment, survey/panel, or content analysis** with rigorous measurement and
explicit theory, across media effects and processing, persuasion and message effects, interpersonal
and organizational communication, health and political communication, or new-media use and effects.
Match tools to your design. Check licenses and current access terms before use, and verify any
CR-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Data sources by area

### Media effects, political & health communication (survey / panel / experiment)
| Source | Provider | Typical use |
|--------|----------|-------------|
| ANES / CES (CCES) | Michigan-Stanford / Harvard | Political communication, campaign exposure, vote choice |
| Pew Research Center datasets | Pew | News use, social media, audience attitudes |
| General Social Survey (GSS) | NORC | Long-run media/attitude trends |
| Health Information National Trends Survey (HINTS) | NCI | Health communication, information seeking |
| Online panels (Prolific, CloudResearch/MTurk, Lucid/Cint) | Vendors | Powered message experiments and surveys |

### Computational / text-as-data (when hypothesis-testing)
| Source | Provider | Typical use |
|--------|----------|-------------|
| GDELT, Media Cloud | GDELT / Media Cloud | News coverage at scale, agenda dynamics |
| Comparative Agendas Project | CAP | Policy/news attention over time |
| News archives (LexisNexis, ProQuest) | Vendors | Content-analysis corpora |
| Social-media APIs / academic access (where permitted) | Platforms | Posts, networks, diffusion (mind ToS + ethics) |

## 2. Software by method

### R
- Experiments/ANOVA: `afex`, `emmeans`, `marginaleffects`, `effectsize`; power: `pwr`, `Superpower`, `simr`
- Mediation/moderation/SEM: `lavaan`, `mediation`, `processR`/`bruceR` (PROCESS-style), `semTools`
- Content analysis & reliability: `irr`, `tidycomm` (ICR), `irrCAC` (Krippendorff's alpha, Gwet's AC)
- Text-as-data: `quanteda`, `stm`, `text2vec`, `tidytext`; embeddings/LLM pipelines (validate vs. humans)
- Multilevel/panel: `lme4`, `nlme`; surveys: `survey`; reproducibility: `renv`, `targets`

### SPSS / Mplus / Stata
- **SPSS + PROCESS macro (Hayes)** — the standard in media-effects mediation/moderation work
- **Mplus** / `lavaan` — SEM, latent-variable measurement (CFA), longitudinal models
- Stata: `reghdfe`, `coefplot`, `sem`/`gsem`; `kappaetc` for intercoder agreement

### Python
- `pandas`, `numpy`, `statsmodels`, `pingouin` (effect sizes, ANOVA)
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers`, `gensim`
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

## 3. Measurement, reliability & validity (a CR priority)
- Scale reliability: Cronbach's **alpha** and McDonald's **omega**; report both where relevant
- Measurement model: **CFA** with fit indices (CFI, RMSEA, SRMR), AVE/CR for convergent/discriminant validity
- **Common-method-variance** checks (marker variable, CFA marker, unmeasured-latent-method-factor)
- Content analysis: documented codebook, trained coders, **intercoder reliability** (Krippendorff's alpha)
  on an adequate subsample, stated unit of analysis

## 4. Open science, preregistration & transparency
- Preregistration / registered analyses: **OSF Registries**, AsPredicted; note preregistration in the cover letter
- Repositories with persistent identifiers: **OSF**, **Dataverse**, ICPSR; **QDR** for controlled-access materials
- **Data-availability statement** — prepare it as you write (see `commres-transparency-and-data`)
- Power/design: a-priori power for experiments/surveys; simulation-based power for multilevel/conjoint designs

## 5. Figures & exhibits (CR rewards effect sizes + uncertainty)
- Coefficient/forest plots, marginal-effects and predicted-value plots (`marginaleffects`, `ggeffects`)
- **Mediation path diagrams**; **simple-slopes / Johnson–Neyman** interaction plots
- SEM/CFA path and measurement-model diagrams (`semPlot`, `lavaanPlot`)
- Colorblind-safe palettes; figures legible in grayscale; vector output (PDF/EPS) for print

## 6. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to **APA**; one consistent style
- Report statistics per APA (M, SD, test with df, **effect size**, exact p)
- Prepare a **double-anonymized** main document (no names/affiliations/acknowledgments, third-person
  self-citation, stripped file metadata) plus a separate title page

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **SAGE Track** (ScholarOne) — guidelines at `journals.sagepub.com/author-instructions/crx` |
| Publisher | **SAGE Publishing**; founded 1974; bimonthly; ISSN 0093-6502 / 1552-3810 |
| Review model | **Double-anonymized**; **two independent reviews** required to back a Revise/Accept |
| Length | Manuscript **≤ 45 pages, double-spaced, inclusive of references** (检索于 2026-06；以官网为准) |
| Style | **APA**; report SDs and effect sizes |
| Submission fee | None for the standard route; optional Gold-OA **APC** after acceptance (待核实) |
| Data policy | **Data-availability statement**; open-materials/data and preregistration (待核实 on requirement level) |

## 8. Cautions
1. **Verify volatile specifics** (editors, exact caps, fee/APC, data/ORCID requirement level) on the
   official SAGE page — they change; unverified items are marked 待核实.
2. **CR is quantitative** — match an experiment, survey/panel, or content analysis with valid
   measurement; do not submit qualitative/interpretive work to this venue.
3. **Test the mechanism** — report mediation with bootstrap CIs and moderation with simple slopes;
   a bare main effect rarely clears the bar.
4. **Report in APA** — effect sizes, SDs, and CIs, not significance stars alone.
5. **Anonymize properly** — remove identifiers from the main document *and* supplements; write
   self-citations in the third person.
