# External Tools & Resources for JPSP-Style Personality & Social Psychology

Data sources, software, and packages useful when preparing a *Journal of Personality and Social
Psychology* (JPSP) submission. JPSP is a **long-format, multi-study** journal split into **three
independently edited sections** — Attitudes and Social Cognition (ASC), Interpersonal Relations and
Group Processes (IRGP), and Personality Processes and Individual Differences (PPID). A typical paper
is a **theory-driven package of several studies** (experiments, surveys, dyadic/longitudinal designs,
archival or intensive-longitudinal data) with **integrative / internal meta-analysis** across studies.
Match tools to your section and designs. Check licenses and current access terms before use, and
verify any JPSP-specific policy in [`official-source-map.md`](official-source-map.md).

## 1. Designing the multi-study package

- **Power & sample-size planning:** G*Power (effects/contrasts), `pwr` (R), `Superpower` /
  `ANOVA_power` (factorial within/between), `simr` (mixed/multilevel power by simulation),
  `pwrss` — plan **each study** and the **smallest effect size of interest**, not just the headline.
- **Sequential / Bayesian designs:** sequential analysis with alpha-spending; Bayes factor design
  analysis (`BFDA`); useful when adding studies adaptively across the package.
- **Design diagnosis:** `DeclareDesign` (declare → diagnose → redesign) to check that the whole
  multi-study plan recovers the target estimands.

## 2. Software by analysis type

### R (dominant in personality/social psychology)
- Core modeling: `lme4` / `lmerTest` (multilevel, repeated measures), `nlme`, `afex` (factorial
  ANOVA done right), `emmeans` (estimated marginal means, simple effects)
- Mediation/moderation/process: `mediation`, `lavaan` (SEM, indirect effects), `processR` /
  PROCESS-style conditional process analysis, `semTools`
- Individual differences / psychometrics (PPID): `psych` (reliability, EFA), `lavaan`/`mirt` (CFA,
  IRT), `careless` (insufficient-effort responding), measurement invariance via `lavaan`/`semTools`
- Dyadic & relationships (IRGP): Actor-Partner Interdependence Model (APIM) via `nlme`/`lme4`,
  `fSRM` (social relations model), round-robin/SRM designs
- Effect sizes & uncertainty: `effectsize`, `MOTE`, bootstrapped CIs (`boot`)
- **Internal meta-analysis across your own studies:** `metafor` (random-effects, forest plots),
  `meta` — pool effects from the studies in the package (a JARS/IRGP expectation)
- Reproducibility: `renv` (pin versions), `papaja` (APA-formatted R Markdown manuscripts), `targets`

### Python
- `pandas`, `numpy`, `statsmodels` (mixed models, OLS/logit), `pingouin` (effect sizes, ANOVA,
  reliability), `semopy` (SEM), `scipy.stats`; `matplotlib`/`seaborn` for exhibits
- Pin with `requirements.txt` / `pip freeze`; set and report random seeds

### SPSS / SAS / Mplus / JASP
- PROCESS macro (Hayes) for SPSS/SAS (mediation/moderation); Mplus for SEM, mixture models, and
  complex multilevel SEM; JASP for Bayesian and frequentist analyses with transparent output

## 3. Reporting standards & transparency (JPSP requires these)

- **APA Journal Article Reporting Standards (JARS):** JARS-Quant, JARS-Qual, JARS-Mixed — use the
  matching table/checklist for experiments, non-experimental, replication, or meta-analytic designs
  (https://apastyle.apa.org/jars). Report participant flow, exclusions, all manipulations and
  measures, and effect sizes with intervals.
- **Preregistration:** OSF Registries, AsPredicted — register hypotheses, design, sampling plan, and
  analysis; clearly mark **registered vs. exploratory** analyses in the manuscript.
- **Registered Reports:** Stage-1 protocol (intro + methods + analysis plan) reviewed before data;
  JPSP publishes Registered Reports.
- **Trusted repositories for data/code/materials:** OSF, ResearchBox, Harvard Dataverse, ICPSR
  (restricted/sensitive data) — JPSP is **TOP Level 2**: state availability and post to a trusted
  repository with persistent identifiers; data must stay available **5+ years** post-publication.

## 4. Figures, tables & APA 7th exhibits

- `ggplot2` + `papaja`/`apaTables` for APA-style tables; `sjPlot` (regression/SEM tables and plots);
  raincloud plots and within-subject CIs for repeated measures; forest plots (`metafor`) for the
  internal meta-analysis; path diagrams for SEM (`semPlot`, `lavaanPlot` or `tikz`)
- Embed tables/figures **in the manuscript text** (JPSP house rule); colorblind-safe palettes;
  legible in grayscale; vector output for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote — format to the **APA Publication Manual
  (7th edition)**; the `apa7` LaTeX class or `papaja` produce APA-compliant manuscripts
- Prepare a **masked manuscript** (no author-identifying information in text, properties, or
  acknowledgments) plus a separate title page — JPSP uses masked review for all submissions
- Keep the **abstract ≤ 250 words**; if a section requires a post-abstract limitations statement,
  keep it within its cap (see 待核实 in the source map)

## 6. Process & per-section portals
| Item | Note |
|------|------|
| Owner / publisher | **American Psychological Association (APA)** |
| Sections (each independently edited) | **ASC** · **IRGP** · **PPID** — choose one; each has its own editor and portal |
| Submission portals (Editorial Manager) | ASC `editorialmanager.com/asc` · IRGP `editorialmanager.com/irg` · PPID `editorialmanager.com/pid` |
| Review model | **Masked review** for all submissions (authors and reviewers mutually masked) |
| Format | Long-format, **multi-study** packages; APA 7th; **JARS** required; tables/figures embedded |
| Length | ASC intro + discussion **≤ 3,500 words**; IRGP intro + discussion **≤ 5,000 words**, **≤ 5 studies** in main text; PPID "as succinctly as possible" (待核实); abstract **≤ 250 words** |
| Transparency | **TOP Level 2 (Requirement)**; state data/code/materials repository + preregistration; Registered Reports accepted; **badges not offered** |
| Submission fee | None stated (verify); any open-access APC handled by APA after acceptance |

## 7. Cautions
1. **Pick the right section first.** ASC, IRGP, and PPID are independently edited with their own
   rules; submitting to the wrong section costs you a desk re-route or rejection. Verify the live
   per-section guidelines — they differ and change (待核实 markers in the source map).
2. **Build for length and multiple studies.** JPSP is **not** a short-report journal: reviewers
   expect a developed theory and a coherent multi-study package, not a single experiment.
3. **Plan the internal meta-analysis up front.** Pooling effects across your own studies (forest
   plot, random-effects estimate) is an explicit IRGP expectation and strengthens any package.
4. **Mask properly.** Strip identifying text and file metadata; provide a separate title page.
5. **JARS + TOP Level 2 are mandatory, not optional polish.** Report to standard and disclose
   data/code/materials availability and preregistration status to a trusted repository.
