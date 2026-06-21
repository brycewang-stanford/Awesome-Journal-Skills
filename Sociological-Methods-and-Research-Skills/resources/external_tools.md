# External Tools — Sociological Methods & Research

Access date: 2026-06 (检索于 2026-06；以官网为准)

Use these after reopening the current SAGE/ASA author pages. SMR is a methods journal: the
deliverable is your *own* released software, so the most important "tool" is a clean, citable package
plus a reproducible pipeline (see
[`../skills/smr-software-and-reproducibility/SKILL.md`](../skills/smr-software-and-reproducibility/SKILL.md)).

## Official workflow

- SAGE SMR home: https://journals.sagepub.com/home/smr
- SAGE SMR author instructions: https://journals.sagepub.com/author-instructions/smr
- SAGE US SMR journal page: https://us.sagepub.com/en-us/nam/journal/sociological-methods-research
- ScholarOne Manuscripts (reach the SMR site via the author-instructions page)
- ASA style (American Sociological Association) — in-text and reference style required by SMR
- DataCite — dataset reference style required by SMR
- ORCID — self-link in ScholarOne (strongly encouraged)

## Reproducibility and deposit

- A trusted public repository for code/data/materials (e.g., a tagged release with a DOI). SMR's
  availability statement expects a permanent, citable location, not a personal homepage.
- For double-anonymized review, an **anonymized/blinded** repository for the review copy; reveal the
  public, citable version at acceptance.
- Seed-fixed master script that reproduces the simulation grid, tables, figures, and the empirical
  illustration; a smoke-test mode for long simulations.

## Software ecosystems common in SMR papers

- **R** (e.g., packages on CRAN for SEM/`lavaan`-style models, multilevel models, missing-data
  multiple imputation, finite mixtures/latent class, network analysis, and text-as-data) — the most
  common environment for releasing a method.
- **Stata** (user-written `.ado` packages and the SSC archive) — widely used for regression-model
  methods, marginal effects, and decomposition/mediation tools.
- **Python** — increasingly used for computational social science / text-as-data methods.
- **Mplus**, **OpenMx** — latent-variable and SEM-specific environments authors may target or compare
  against.

## Discipline data sources (for the empirical illustration)

- Public, depositable survey and administrative datasets common in sociology (general social surveys,
  panel studies, census/administrative microdata, and named public archives). Prefer data that sit in
  the failure regime the method addresses and that can be shared under the availability policy.

## Do not infer

- Do not assume APA/Chicago/numeric referencing — SMR requires **ASA** style (and **DataCite** for
  datasets); confirm on the live author page.
- Do not treat the venue-neutral shared causal-inference code kit as SMR's deliverable; SMR expects
  the paper's own released method software.
- Do not attribute **Sociological Methodology** (ASA annual) tools/policies to **Sociological Methods
  & Research**.
