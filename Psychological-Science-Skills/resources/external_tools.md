# External Tools & Resources for Psychological Science Submissions

Software, repositories, and packages useful when preparing a *Psychological Science* (APS) submission.
Psychological Science is an **empirical, short-report** journal with **strong open-science
requirements** (open data + materials, a Research Transparency Statement, preregistration considered
in editorial decisions) and demanding statistical standards (effect sizes, confidence intervals,
sample-size justification, full disclosure). Tools below support those norms. Verify any
journal-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Preregistration & registered reports
| Tool | Use |
|------|-----|
| **OSF Registries** (osf.io) | Preregister hypotheses, design, and analysis plan; mint a DOI |
| **AsPredicted** | Lightweight preregistration (9 questions) |
| **OSF Registered Reports / Stage 1 templates** | For the Registered Reports track (Stage 1 → in-principle acceptance → Stage 2) |
| Secondary-data preregistration templates | For Registered Reports with Existing Data |

## 2. Open data, materials & persistent identifiers
| Repository | Use |
|------------|-----|
| **OSF** (osf.io) | Data, materials, analysis scripts, codebooks; component DOIs |
| **Harvard Dataverse / ICPSR** | Archived datasets with DOIs |
| **figshare / Zenodo** | General-purpose data/material archiving with DOIs |
| **GitHub + Zenodo release** | Versioned analysis code with a citable DOI |

> Psychological Science requires **persistent identifiers (DOIs)** for shared data/materials and a
> **Research Transparency Statement** between the Introduction and Methods. Prepare these early.

## 3. Power analysis & sample-size justification
- **G*Power** — classic power analysis for t-tests, ANOVA, regression, correlations
- R: `pwr`, `Superpower` (factorial ANOVA), `simr` (mixed-model power via simulation), `pwrss`
- Simulation-based power for complex designs (your own Monte Carlo)
- For sequential designs / Bayes: sequential analysis and Bayes-factor design analysis tools

## 4. Analysis (effect sizes + uncertainty are required)
### R (dominant)
- Estimation/"new statistics": `effectsize`, `MOTE`, `emmeans`, `marginaleffects`, `parameters`
- Mixed models: `lme4`, `lmerTest`, `brms` (Bayesian); SEM: `lavaan`
- Robustness/meta: `metafor` (meta-analysis), `WRS2` (robust methods)
- Reproducibility: `renv` (pin versions), `targets`, R Markdown / Quarto for reproducible reports
### Python
- `pingouin` (effect sizes + CIs), `statsmodels`, `scipy.stats`, `numpy`, `pandas`
- `matplotlib` / `seaborn`; pin with `requirements.txt`
### JASP / jamovi
- GUI tools that report effect sizes, CIs, and Bayesian alternatives by default

## 5. Reproducible reporting & disclosure
- **Quarto / R Markdown / Jupyter** — analysis and manuscript from one reproducible source
- `papaja` (R) — APA 7th-edition manuscripts from R Markdown
- The **"21-word solution"** style disclosure of all conditions, measures, exclusions, and how
  sample size was determined; report total excluded observations and reasons
- Computational reproducibility check before deposit (fresh-session run of the master script)

## 6. Writing, style & format
- **APA Publication Manual, 7th edition** — required style
- `papaja`, Zotero/BibTeX with an APA CSL style, EndNote
- **Embed tables and figures in the main text** near where they are discussed
- Anonymize the initial submission (no author-identifying information)
- Watch the **word format**: Introduction + Discussion + Footnotes + Acknowledgments + Appendices
  **≤ 2,000 words combined**; Method + Results excluded (typically ≤ 2,500); **150-word** structured
  abstract stating sample sizes, populations, and design limitations

## 7. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Manuscript Central**, `mc.manuscriptcentral.com/psci` |
| Owner / publisher | **Association for Psychological Science (APS)** / **SAGE** |
| Review model | Anonymized peer review |
| Main format | **Research Article** (2,000-word combined Intro+Discussion; Method+Results excluded) |
| Other formats | Registered Reports (Stage 1/2), Registered Reports with Existing Data, Commentary (≤1,000) |
| Abstract | **150 words**, must state sample sizes, populations, design limitations |
| Open science | **Open data + materials required** (case-by-case exemptions) + Research Transparency Statement + preregistration considered |

## 8. Cautions
1. **Verify volatile specifics** (editor, exact word format, open-science wording, accepted types) on
   the official APS page — they change; the format and open-science rules were revised for 2024.
2. **Open data/materials are required, not optional** — plan deposits and DOIs before submission.
3. **The Research Transparency Statement is graded** — "limits on transparency will be a factor in
   editorial decisions"; justify any constraint.
4. **Report effect sizes and CIs**, justify sample size (power analysis if appropriate), and disclose
   all exclusions, conditions, and measures.
5. **Mind the unusual word format** — it rewards tight reasoning; long literature reviews do not fit.
