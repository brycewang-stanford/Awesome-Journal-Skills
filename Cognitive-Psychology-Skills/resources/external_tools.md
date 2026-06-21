# External Tools & Resources for Cognitive Psychology Submissions

Software, frameworks, repositories, and packages useful when preparing a *Cognitive Psychology*
(Elsevier) submission. Cognitive Psychology is a **model-driven cognitive-science** journal: it rewards
**multi-experiment programs combined with formal/computational modeling**, with model **fitting and
comparison**, **parameter/model recovery**, and **reproducible model code**. The tools below support
those norms. Verify any journal-specific policy in [`official-source-map.md`](official-source-map.md)
and on the official guide for authors (检索于 2026-06；以官网为准).

## 1. Cognitive / computational modeling frameworks
| Tool | Use |
|------|-----|
| **Stan** (`rstan`, `cmdstanr`, `brms`) | Hierarchical Bayesian estimation of cognitive models; full posterior + diagnostics |
| **JAGS** / **PyMC** | Bayesian model fitting (Gibbs/HMC) for hierarchical cognitive models |
| **R** modeling toolkits | e.g. signal-detection / ROC tools, diffusion-model packages (`rtdists`, `RWiener`, `fast-dm`/`hddm` for drift-diffusion) |
| **ACT-R / general cognitive architectures** | Process-model implementations where the contribution is an architecture-level account |
| Custom likelihoods + optimizers | `optim`/`DEoptim` (R), `scipy.optimize` (Python) for maximum-likelihood model fits |

## 2. Model comparison, selection & recovery
- **Information criteria:** AIC, BIC, WAIC, LOO-CV (`loo` in R) for penalized comparison
- **Bayes factors:** `bridgesampling`, `BayesFactor` (R); marginal-likelihood estimation
- **Cross-validation:** k-fold / leave-one-subject-out for predictive comparison
- **Parameter recovery:** simulate from known parameters, refit, check recovery before interpreting fits
- **Model recovery:** simulate from each candidate model, confirm the criterion selects the generating model at your design's N/trials

## 3. (Generalized) linear mixed models & estimation
- R: `lme4`, `lmerTest`, `glmmTMB` (crossed subject/item random effects), `afex` (factorial designs)
- Bayesian multilevel: `brms`, `rstanarm`
- Effect sizes + uncertainty: `effectsize`, `emmeans`, `marginaleffects`, `parameters`
- Python: `statsmodels` (mixed LM), `pingouin`, `bambi` (Bayesian multilevel on PyMC)

## 4. Experiment building & stimulus control
- **PsychoPy**, **jsPsych**, **lab.js**, **OpenSesame**, **Gorilla** for controlled cognitive tasks
- Stimulus norming/control: word-frequency, length, familiarity databases; counterbalancing scripts
- Document the **full stimulus pool** and counterbalancing, not a curated subset

## 5. Open data, model code, materials & persistent identifiers
| Repository | Use |
|------------|-----|
| **OSF** (osf.io) | Data, materials, analysis + model code, codebooks; component DOIs; preregistration |
| **Mendeley Data** | Elsevier-affiliated data repository with DOIs |
| **Zenodo** (+ GitHub release) | Versioned model/analysis code with a citable DOI |
| **Harvard Dataverse / ICPSR** | Archived datasets with DOIs |

> Cognitive Psychology authors are strongly encouraged to share **data, model/analysis code, and
> materials**. Because the contribution is a *fitted model*, the reported fits must **regenerate in a
> fresh session** from deposited, seeded code — plan deposits and DOIs early.

## 6. Reproducibility, writing & style
- **Quarto / R Markdown / Jupyter** — analysis, modeling, and manuscript from one reproducible source
- `renv` (R) / `requirements.txt` or `conda` (Python) — pin versions; set and report random seeds
- `papaja` (R) — APA-style manuscripts from R Markdown
- Reference managers: Zotero / BibTeX / EndNote with the journal's required style
- A **fresh-session run** of the master model/analysis script before deposit (confirm all fits/figures regenerate)

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Elsevier Editorial Manager** (linked from the ScienceDirect guide for authors) |
| Publisher | **Elsevier** |
| Identity | Leading cognitive-science journal; **longer, integrative, model-driven** articles |
| Scope | Attention, perception, memory, learning, language, categorization, reasoning, problem-solving, judgment/decision-making; modeling/neuroscientific approaches and substantive reviews |
| Open science | Data + model/analysis code + materials sharing strongly encouraged; Elsevier research-data + competing-interest declarations |
| Review model / length / abstract | Volatile — confirm on the official guide for authors. 待核实 |

## 8. Cautions
1. **Verify volatile specifics** (editor, review model, length guidance, abstract limit, declarations)
   on the official Elsevier/ScienceDirect page — they change (检索于 2026-06；以官网为准).
2. **A model must be compared, not just fit** — report AIC/BIC/BF or cross-validation against a real
   rival under matched flexibility.
3. **Recovery is not optional** — parameter and model recovery make a fit interpretable.
4. **Respect the data hierarchy** — use mixed/hierarchical models; don't aggregate away subject/item
   variance.
5. **Reproducible model code is the venue-specific must** — fits must regenerate from deposited, seeded
   code in a fresh session.
