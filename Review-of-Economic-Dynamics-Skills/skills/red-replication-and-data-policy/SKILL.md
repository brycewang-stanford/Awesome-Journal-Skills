---
name: red-replication-and-data-policy
description: Use when building the Review of Economic Dynamics (RED) data-and-code archive to the journal's actual "Availability of Data and Computer Code for Published Papers" policy and Elsevier Option C data instructions — covering computational and empirical papers, the specific readme.txt requirements, .zip/.gz/.gzip submission to the RED code editor, posting on the RED site, RePEc Computer Codes indexing, repository/data-statement metadata, and the proprietary-data exemption.
---

# Replication & Data/Code Policy for RED (red-replication-and-data-policy)

## When to trigger

- Preparing the materials that must be in place **before final acceptance**
- A computational paper unsure whether code-only (no data) still triggers the policy (it does)
- Handling proprietary/confidential data and the exemption process

## RED's policy (verified)

RED enforces an **Availability of Data and Computer Code for Published Papers** policy. Before final
acceptance, authors must provide data and code sufficient for others to replicate the results. RED's
culture is **code-first** — the policy covers **computational as well as empirical** papers, and
archives are first-class, citable objects. The Elsevier Guide also applies **Option C** research-data
instructions: deposit research data in a relevant repository and cite/link it in the article when possible,
or provide a data-availability statement explaining why sharing is not possible.

- **Empirical papers**: final datasets **plus** the code that manipulates them and, if applicable, how
  the final dataset was derived from original sources.
- **Computational / theoretical papers**: the **final programs** that generate the results.
- **readme.txt (required)** — must specify the **software/OS used**, **program execution order**,
  **expected computation time**, and **random seeds** where applicable. These requirements are notably
  specific, reflecting reproducibility norms for simulation-heavy work.
- **Format & delivery**: package as **open-standard archives — .zip, .gz, or .gzip** — to the RED
  data/code editor **Christian Zimmermann**.
- **Posting & indexing**: materials are posted on the **RED website** and indexed on **RePEc** (the RED
  **"Computer Codes"** series at IDEAS/RePEc).
- **Elsevier Option C layer**: prepare repository DOI/links and data/software citations where possible;
  if data cannot be shared, prepare the data-availability statement during submission.
- **Exemptions**: proprietary/confidential-data exemptions must be **approved by the Coordinating Editor
  at the time of submission** — note this in the cover letter, not after acceptance.

## Checklist

- [ ] Final data (empirical) or final programs (computational), with a master run-all script
- [ ] readme.txt lists software/OS, execution order, expected runtime, and random seeds
- [ ] Packaged as .zip/.gz/.gzip; addressed to the RED code editor
- [ ] Repository DOI/links and data/software citations prepared, or data statement explains limits
- [ ] Proprietary-data exemption (if any) flagged to the Coordinating Editor at submission
- [ ] Archive verified to reproduce headline tables/figures from scratch

## Anti-patterns

- Assuming a code-only computational paper is exempt (it is not)
- A readme missing seeds, runtime, or execution order
- Treating a RED website archive as a substitute for the Elsevier Option C data statement
- Raising a proprietary-data exemption after acceptance instead of at submission

## Archive manifest

Create a manifest before final acceptance:

```text
Result | Script/program | Inputs | Runtime | Seed | Output path | README line | DOI/data statement
```

For computational RED papers, include solution routines, calibration files, counterfactual scripts,
transition-path programs, and plotting scripts. For empirical RED papers, include raw-to-final data
construction, estimation commands, and table/figure exports. The manifest should make it obvious which
program recreates the dynamic result, not merely which folder contains code.

## Archive layout that satisfies the policy

A package the RED code editor can verify without correspondence (adapt names to your stack):

```text
red-archive-v1.zip
├── readme.txt           # REQUIRED fields: software/OS, execution order, runtime, seeds
├── run_all.sh           # one command reproduces every exhibit
├── src/
│   ├── solve_model.jl       # household problem (EGM) + GE loop
│   ├── calibrate.jl         # internal calibration to targets in targets.csv
│   ├── counterfactuals.jl   # policy experiments, transition paths
│   └── accuracy_checks.jl   # Euler-error and grid-refinement diagnostics
├── data/
│   ├── moments/targets.csv  # every calibration target with its source
│   └── raw/ (or access instructions if proprietary)
├── output/              # regenerated tables/figures mapped to paper numbering
└── Manifest.toml / requirements.txt / Dynare version pin
```

For runtime, be honest at the step level: a global-solution model whose full rerun takes days should say
so in readme.txt and provide cached intermediates plus the code that regenerates them.

## Failure modes the code editor's check catches

- Code that solves a slightly different model than the paper's final equations (drift across revisions)
- Hard-coded local paths or undeclared toolbox dependencies that break execution on another machine
- Missing seeds, so SMM draws or simulated panels differ run to run and moments will not match the tables
- Proprietary inputs with no access instructions and no simulated stand-in, leaving the code path untestable

## Output format

```text
[Archive status] ready / missing readme / missing code / exemption needed
[Replication object] empirical data / computational program / mixed
[Required readme fields] software_OS / order / runtime / seeds
[Delivery risk] archive format / code editor / proprietary data / RePEc posting / Option C data statement
[Next repair] <single file or script to fix>
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — policy URL and the RePEc Computer Codes series
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — environment-capture and archive tooling
