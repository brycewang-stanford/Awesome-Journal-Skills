# External Tools & Resources for SPQ-Style Sociological Social Psychology

Data sources, software, and packages useful when preparing a *Social Psychology Quarterly* (SPQ)
submission. SPQ is the journal of **sociological social psychology** — it studies the **link between
social structure and the individual** across three broad traditions: **symbolic interaction**, **social
structure and personality (SSP)**, and **group processes**, plus allied programs in **status and
expectation states**, **identity theory**, and **affect/emotion** (e.g., affect control theory). A
submission may be a **laboratory experiment**, a **survey or survey experiment**, an **observational or
ethnographic study**, or a **mixed-methods** design. Match tools to your tradition and method. Check
licenses and current access terms before use, and verify any SPQ-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by tradition

### Social structure and personality (SSP) — survey / secondary data
| Source | Provider | Typical use |
|--------|----------|-------------|
| General Social Survey (GSS) | NORC | Attitudes, self-concept, stress, social ties over time |
| Americans' Changing Lives (ACL) | ICPSR / Michigan | Social structure, health, and the self across the life course |
| MIDUS (Midlife in the U.S.) | ICPSR | Psychological well-being, control, social roles |
| Panel Study of Income Dynamics (PSID) | Michigan | Life-course position, mobility, household context |
| Add Health | UNC / ICPSR | Adolescent identity, networks, status, transitions to adulthood |
| ICPSR general archive | University of Michigan | Replication and secondary analysis of social-psychological data |

### Group processes & status — experimental
| Source | Provider | Typical use |
|--------|----------|-------------|
| Lab experiments (standardized experimental settings) | Author-run | Status, expectation states, exchange, legitimacy, justice |
| Online experiment platforms (e.g., subject pools, panels) | Author-run | Vignette / factorial-survey experiments, group-process designs |
| Affect Control Theory dictionaries (EPA ratings) | ACT research groups | Sentiment / impression-formation modeling (Interact, BayesACT) |

### Symbolic interaction & interpretive — observation / interviews
| Source | Provider | Typical use |
|--------|----------|-------------|
| Fieldwork notes, participant observation | Author-collected | Meaning-making, self, interaction order |
| In-depth / narrative interviews | Author-collected | Identity work, accounts, emotion management |
| Conversation / interaction recordings | Author-collected | Sequential analysis of interaction (with consent) |

## 2. Software by method

### R
- Survey / SSP: `survey`, `srvyr` (complex-survey design), `lavaan` (SEM / measurement of latent constructs), `psych` (scale reliability), `mediation`
- Experiments / factorial surveys: `cregg`/`cjoint` (conjoint / vignette), `emmeans` (estimated marginal means), `afex` (factorial ANOVA), `lme4`/`brms` (multilevel models for nested group data)
- Status / network structure: `igraph`, `statnet`/`ergm`, `sna`
- Reproducibility: `renv` (pin versions), `targets` (pipelines), `here`

### Stata
- `mixed`/`meglm` (multilevel for group/dyadic data), `sem`/`gsem` (latent constructs, measurement)
- `margins` + `marginsplot` (predicted values, interactions), `reghdfe`, `estout`/`esttab`
- Survey estimation: `svy:` prefix for GSS/PSID-type complex designs

### Python
- `pandas`, `numpy`, `statsmodels`, `pingouin` (effect sizes), `semopy` (SEM)
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Affect control & formal social-psychological models
- **Interact** / **BayesACT** for affect control theory; expectation-states simulation tools where applicable

### Qualitative & interpretive
- CAQDAS: NVivo, ATLAS.ti, MAXQDA, Taguette (open source) — coding interviews, fieldnotes, interaction
- Transcription and sequential/coding schemes for interaction analysis; memoing and grounded-theory workflows

## 3. Measurement, reliability & design
- Validate scales and latent constructs (Cronbach's alpha / omega, CFA); report reliability — SPQ work
  often rests on **measured social-psychological constructs** (identity salience, mastery, status, affect)
- Factorial-survey / vignette design: balanced decks, randomization of dimensions, attention checks
- Experimental design: manipulation/standardized-setting checks, attrition, power/MDE, IRB and consent
- Preregistration where appropriate (OSF Registries, AsPredicted) — useful but **not required** by SPQ

## 4. Figures & exhibits (SPQ rewards clear, self-contained exhibits)
- Coefficient / predicted-probability and marginal-effects plots (`marginaleffects`, `coefplot`, `ggplot2`)
- Path / SEM diagrams for mediation and measurement models; interaction plots for moderation
- Network diagrams where group structure is the point; clean tables for nested/multilevel models
- Colorblind-safe palettes, legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **ASA Style Guide** (author-date)
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **blinded manuscript** plus a
  **separate title page** file (title, authors, affiliations, running head, approximate word count)
- Abstract **≤ 150 words**, non-identifying, with a few **keywords**; author names omitted from the abstract page

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **SageTrack / ScholarOne Manuscript Central** — confirm current URL |
| Owner / publisher | **ASA** / **SAGE** |
| Review model | **Masked / blinded** — separate title page + blinded manuscript; under-blinded papers are temporarily rejected |
| Article length | **≤ 10,000 words** (all parts, excl. supplementary materials); **Notes ≤ 5,000 words** |
| Abstract | **≤ 150 words**, non-identifying, plus keywords |
| Fee | **$25** processing fee on first submission; **waived** for resubmissions and **ASA student members** |
| Data policy | Sharing data/code/materials is **encouraged but NOT required**; willingness to share **has no impact on acceptance** (ASA data-sharing norm) |

## 7. Cautions
1. **Live-check operational specifics** (submission link, editor-office email, fee workflow,
   open-access prompts, and file handling) on the official SAGE/ASA pages before upload.
2. **Blind properly** — SPQ is masked; submit a blinded manuscript plus a separate title page, or the
   editorial office will temporarily reject it.
3. **Sharing is encouraged, not mandated** — do **not** treat SPQ like an open-data-required journal;
   willingness to share has no effect on acceptance. Still document constructs and analyses well.
4. **Match method to tradition** — SPQ judges experiments, surveys, and observation/ethnography on
   their own terms; do not force one template onto every paper.
5. **Center the structure-individual link** — an SPQ paper is social-psychological *and* sociological;
   it must connect social structure or process to the self, interaction, or group.
