# Marketing-Research Tools & Resources (JMR)

This document lists external data sources, analysis software, and writing tools commonly
used when preparing a manuscript for the **Journal of Marketing Research (JMR)**. JMR
deliberately spans two methodological traditions in one journal — **behavioral experiments**
(lab and field) in consumer behavior and **econometric / structural / analytical modeling**
in marketing science — plus dedicated **methods contributions**. The toolkit below is
organized around that split. Always verify licensing terms and current AMA/SAGE policies
(exact p-values, Data Availability Statement, Web Appendix) before relying on any resource.

## 1. Data Sources

### Behavioral / experimental (consumer behavior)
| Source | Provider | Typical use |
|--------|----------|-------------|
| Prolific / CloudResearch / MTurk | Various | Online experiments and survey samples |
| Qualtrics | Qualtrics | Survey programming, randomization, attention checks |
| Eye-tracking / response-time (Inquisit, Gorilla) | Various | Process measures, implicit measures |
| Field-experiment partners (retail, app, email) | Firm collaborations | Randomized field interventions |

### Marketing-science / modeling (panel, scanner, digital)
| Source | Provider | Typical use |
|--------|----------|-------------|
| NielsenIQ / IRI (Circana) scanner & panel | Kilts Center (academic access) | Brand choice, pricing, promotion response |
| Numerator / comScore / clickstream | Various | Digital path-to-purchase, online behavior |
| Kantar / GfK panels | Various | Household purchase panels |
| Platform / ad-server logs (Meta, Google) | Firm collaborations | Auctions, targeting, attribution |
| Compustat / CRSP | S&P Global / CRSP | Firm-level marketing-finance outcomes (e.g., stock returns) |

### Text / unstructured marketing data
| Source | Use |
|--------|-----|
| Reviews (Amazon, Yelp), social media | UGC, sentiment, topic models, embeddings |
| Search/trends, app analytics | Demand signals, engagement |

## 2. Analysis Software & Packages

### Behavioral experiments (design, estimation, process)
- **R**: `afex`/`emmeans` (ANOVA, contrasts, estimated marginal means), `lme4` (mixed designs), `effectsize` (Cohen's d, eta-squared, reporting effect sizes JMR requires).
- **PROCESS macro** (Hayes) in SPSS/R — mediation, moderation, conditional indirect effects with bootstrapped CIs.
- **Power**: G*Power, R `pwr`/`simr`, and simulation for interactions; pre-registration on AsPredicted / OSF.

### Econometric & structural marketing-science modeling
- **Stata**: `reghdfe` (high-dimensional FE), `ivreghdfe`/`ivreg2` (IV/2SLS), `csdid`/`did` (modern DiD), `xtreg`.
- **R**: `fixest`, `did`, `MatchIt`, `sandwich` (robust/clustered SE), `bayesm` (hierarchical Bayes choice models).
- **Structural / choice**: random-coefficient logit (BLP-style demand), dynamic and discrete-choice estimation; tools in MATLAB, **Julia**, Python, or custom GMM/MLE/MCMC code.
- **Bayesian**: Stan, PyMC, JAGS for hierarchical/heterogeneity models.

### Machine learning / text
- **Python**: `scikit-learn`, `statsmodels`, `transformers`/embeddings, causal-ML (`econml`, `doubleml`); R `tidymodels`, `grf` (causal forests).

## 3. Reference & Writing Tools

| Tool | Note |
|------|------|
| Zotero | Free; configure to **AMA author-year** output style |
| EndNote | Broad style support; verify AMA style template |
| Overleaf / LaTeX | JMR accepts a 12-point LaTeX font; keep the 50-page print limit in mind |
| Grammarly | Language polish |

JMR uses **AMA author-year** citation/reference style (e.g., "Thorelli (1960)"). Configure your
reference manager accordingly and reconcile against the current SAGE/AMA author instructions.

## 4. Reproducibility & the Web Appendix (JMR-specific)

The **Web Appendix** is a first-class, replication-oriented artifact at JMR — a single separate
PDF, excluded from the 50-page limit, with tables/figures labeled using a **'W' prefix**
(e.g., "Table W1", "Figure W1"). Use it for supplementary analyses, full stimuli, robustness,
estimation details, and additional studies.

1. Keep clean, commented scripts (R / Stata / Python / Julia / Mplus) that regenerate every
   table and figure, including 'W'-prefixed Web Appendix exhibits.
2. Prepare a **Data Availability Statement** for the title page (required by current AMA policy).
3. Be ready to share computer code, instruments/stimuli, and materials on editor request, and to
   provide data/materials needed to replicate and validate results before final acceptance.
4. Report **exact p-values (three digits), standard errors, and effect sizes** — the journal-level
   reporting mandate — in every empirical table.
5. Disclose any AI-generated content in the main document and Acknowledgments.

## 5. Submission & Process

- **Submission portal**: ScholarOne / Manuscript Central at **mc.manuscriptcentral.com/ama_jmr** (verify the current link).
- **ORCID**: keep an ORCID linked to your account.
- **Plagiarism/originality**: every submission is screened with **iThenticate**.
- **Review**: **double-anonymized**; two independent reviews are required to reach a Revise/Accept decision.

## 6. Verify Before You Rely

Editorial team (mid-2026 handover from Hamilton to Thomadsen's team), submission links, the
50-page limit, fees/APC, and the AMA Research Transparency Policy change over time. Always
confirm current requirements on the SAGE author instructions and the AMA submission-guidelines
page before submitting.
