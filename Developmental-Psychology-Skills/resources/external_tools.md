# External Tools & Resources for Developmental Psychology Submissions

Software, repositories, and packages useful when preparing a *Developmental Psychology* (APA) submission.
Developmental Psychology is an **empirical lifespan-development** journal whose claims are about
**change** (age effects, within-person trajectories, mechanisms), reported under **APA 7th edition +
JARS** and the **Transparency and Openness Promotion (TOP)** guidelines. The tools below support
developmental designs, change-modeling analysis, and open-science compliance. Verify any journal-specific
policy in [`official-source-map.md`](official-source-map.md).

## 1. Preregistration & study planning
| Tool | Use |
|------|-----|
| **OSF Registries** (osf.io) | Preregister developmental hypotheses, the invariance-test plan, and the growth model; mint a DOI |
| **AsPredicted** | Lightweight preregistration (9 questions) |
| Secondary-data preregistration templates | For confirmatory tests on existing panels (NICHD, ECLS, ELS) |
| **APA JARS materials** | JARS-Quant / JARS-Qual / MARS reporting checklists |

## 2. Open data, materials & persistent identifiers
| Repository | Use |
|------------|-----|
| **OSF** (osf.io) | Data, materials, scripts, codebooks; component DOIs |
| **ICPSR** | Archived social/behavioral datasets with DOIs and restricted-access options |
| **Databrary** | Purpose-built sharing of **identifiable developmental video/audio** under permission |
| **Harvard Dataverse / Zenodo / figshare** | General-purpose data/material archiving with DOIs |
| **GitHub + Zenodo release** | Versioned analysis code with a citable DOI |

> Developmental Psychology asks for **persistent identifiers (DOIs)** and a **data-availability statement**.
> Data from minors are shared via consent-consistent, permission-based archives — not posted openly.

## 3. Developmental data archives (secondary analysis)
- **NICHD Study of Early Child Care and Youth Development (SECCYD)** — longitudinal early-childhood panel
- **ECLS** (Early Childhood Longitudinal Study), **ELS**, **Add Health**, **MIDUS** (lifespan/adulthood)
- **Fragile Families / Future of Families**, **PSID Child Development Supplement**
- **ManyBabies** consortium data (infant replication) — when relevant to an infancy contribution

## 4. Power & sample-size justification (for the change parameter)
- **Monte Carlo power simulation** in **Mplus** or R (`simsem`, `lavaan` + `simulateData`) for growth/SEM
- R: `simr` (mixed-model power via simulation), `pwr`, `WebPower`, `Superpower`
- Power for latent growth slopes, age × condition interactions, and cross-lagged paths — not just t-tests

## 5. Analysis (model change; report effect sizes + CIs)
### R (dominant)
- Latent growth / SEM: `lavaan`, `tidySEM`; invariance: `semTools` (`measurementInvariance`, `compareFit`)
- Multilevel / mixed growth: `lme4`, `lmerTest`, `nlme`, `brms` (Bayesian)
- Cross-lagged / RI-CLPM: `lavaan` syntax, `dynr`; mediation/moderation: `mediation`, `lavaan`, `interactions`
- Missing data: `mice` (multiple imputation), FIML via `lavaan`/`lme4`
- Effect sizes: `effectsize`, `MOTE`, `marginaleffects`, `parameters`; meta-analysis: `metafor`
- Reproducibility: `renv`, `targets`, Quarto / R Markdown
### Mplus
- Growth models, multilevel SEM, measurement invariance, mixture/GMM, Monte Carlo power
### Python
- `statsmodels` (mixed models), `semopy` (SEM), `pingouin` (effect sizes + CIs), `pandas`, `numpy`

## 6. Tables, figures & reproducible reporting
- **APA Publication Manual, 7th edition** — required style
- `papaja` (R) — APA 7th-edition manuscripts from R Markdown
- `ggplot2` + spaghetti/growth-curve recipes for trajectory figures (age on the x-axis, CI bands)
- Quarto / R Markdown / Jupyter — analysis and manuscript from one reproducible source

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager**, `editorialmanager.com/dvl` |
| Publisher | **American Psychological Association (APA)** |
| Editor | Koraly Pérez-Edgar (检索于 2026-06；以官网为准) |
| Review model | **Masked peer review** available on request |
| Length tiers | brief report (~4,500) / larger (~10,500) / multi-study or longitudinal (~15,000) — 检索于 2026-06；以官网为准 |
| Front matter | APA abstract + **Public Significance Statement** (2–3 sentences, ~30–70 words) |
| Style / reporting | **APA 7th edition** + **JARS** (JARS-Quant / JARS-Qual / MARS) |
| Transparency | **TOP** guidelines — data-availability statement, DOIs, preregistration, sample-size justification |

## 8. Cautions
1. **Verify volatile specifics** (editor, exact length tiers, abstract ceiling, masked-review and TOP
   wording) on the official APA page — they change.
2. **Model change, don't snapshot it** — use growth/multilevel/SEM, and **test measurement invariance**
   before interpreting trajectories.
3. **Handle attrition** with FIML/MI and an attrition analysis; do not delete dropouts.
4. **Report effect sizes and CIs**, justify sample size for the change parameter, and disclose all
   exclusions, conditions, and measures (JARS).
5. **Share data ethically** — DOIs for de-identified data; permission-based archives (Databrary) for
   identifiable data from minors; a justified data-availability statement.
