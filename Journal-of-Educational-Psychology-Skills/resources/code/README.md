# Code Kit — Journal of Educational Psychology

Small R templates for the analysis patterns that *Journal of Educational Psychology* reviewers expect
to see handled explicitly: classroom/school nesting, cluster-level power and balance, multilevel or
growth models, mediation with indirect-effect intervals, and JARS-ready reproducible tables.

The scripts use synthetic data by default. They are not a claim about any real study; they show the
minimum analysis skeleton a JEP manuscript should adapt before reporting results.

## Files

| File | Purpose | Key packages |
|---|---|---|
| `R/00_setup.R` | Fixed seed, synthetic student/class/school data, helper functions, and a tiny literacy-growth panel | base R |
| `R/01_cluster_design_diagnostics.R` | Cluster-randomized design diagnostics: ICC, cluster-size imbalance, treatment balance, minimum detectable effect sketch | base R; optional `lme4` |
| `R/02_multilevel_growth_model.R` | Multilevel growth and classroom-nesting models, with effect sizes and confidence intervals | base R; optional `lme4` |
| `R/03_sem_mediation_jars.R` | Learning-mechanism mediation template with bootstrap indirect-effect CI and JARS-style disclosure fields | base R; optional `lavaan` |
| `R/04_reproducible_tables.R` | APA/JEP table skeletons for descriptives, model summaries, and transparency notes | base R |

## Run Order

```r
source("R/00_setup.R")
source("R/01_cluster_design_diagnostics.R")
source("R/02_multilevel_growth_model.R")
source("R/03_sem_mediation_jars.R")
source("R/04_reproducible_tables.R")
```

The templates guard optional packages with `requireNamespace()`. Without optional packages, they still
run a base-R fallback so the diagnostics and table shapes remain visible.

## Mapping to Skills

- `R/01` supports `jedpsych-study-design`: randomization level, nesting, ICC, cluster imbalance, and
  power assumptions must be settled before recruitment.
- `R/02` supports `jedpsych-data-analysis` and `jedpsych-tables-figures`: model clustered or repeated
  observations before interpreting learning gains.
- `R/03` supports `jedpsych-theory-and-hypotheses` and `jedpsych-open-science-and-transparency`: the
  mechanism test should distinguish confirmatory, exploratory, and preregistered analyses.
- `R/04` supports `jedpsych-writing-style` and `jedpsych-submission`: JEP tables should carry effect
  sizes, CIs, sample units, and Transparency and Openness notes.

Use the official source map for venue facts and the live APA/JARS pages before submission.
