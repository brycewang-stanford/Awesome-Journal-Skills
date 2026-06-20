---
name: jleo-replication-package
description: Use when assembling the data and code replication package for a Journal of Law, Economics, and Organization (JLEO) manuscript — building reproducible paths from institutional/organizational/political data sources (court records, contracts, legislative data, firm-boundary data) to every exhibit. Builds the package; it does not run new analysis.
---

# Replication Package (jleo-replication-package)

## When to trigger

- A coauthor or referee needs to reproduce every table and figure from raw institutional data
- The paper relies on hand-collected institutional data (court records, contracts, legislative votes, agency rulings) whose construction is undocumented
- Some institutional data are proprietary or confidential (firm contracts, sealed court records) and access terms must be stated
- The code runs on one machine but the path from raw source to final exhibit is not reproducible
- You need a Data Availability Statement and a README before submitting or at the revision stage

## Reproducibility for institutional data

JLEO is an OUP economics journal; OUP and COPE expect transparency, and the field increasingly expects a working replication package even where OUP does not run a dedicated data-editor check (verify the current JLEO data-and-code policy on the official OUP page — 待核实). The distinctive challenge at JLEO is that the data are often **institutional artifacts** — court dockets, procurement contracts, committee assignments, constitutional provisions — that require careful, documented construction from primary sources. Build the package so a stranger reproduces every number.

### Build the package
1. **One-command build.** A master script runs raw → cleaned → analysis → every exhibit in order, with a fixed random seed where any randomness enters.
2. **Document the institutional data construction.** For hand-coded institutional variables (an asset-specificity index, a judicial-independence score, a governance-form classification), provide the coding protocol, the source documents, and inter-coder reliability if human coding was involved. This is where JLEO replication most often fails.
3. **State data provenance and access.** For each source: origin (court system, regulator, commercial provider), access date, license/terms, and whether others can obtain it. Confidential firm or court data: state the access procedure and provide the code plus a synthetic or restricted-use path.
4. **Map exhibits to scripts.** A table lists, for each table/figure in the paper, the script and line that produces it.
5. **Pin the environment.** Software versions, packages, and (for proprietary software) the exact commands; note OS if results are sensitive.
6. **Data Availability Statement.** A clear DAS naming which data are public, which are restricted, and how to request access, consistent with OUP/COPE expectations.

## Checklist

- [ ] A master script reproduces every exhibit end-to-end, raw → final, with seeds fixed
- [ ] Hand-coded institutional variables have a documented coding protocol and source documents
- [ ] Inter-coder reliability reported where institutional variables were human-coded
- [ ] Each data source has provenance, access date, and license/terms stated
- [ ] Confidential institutional data have a stated access procedure and a code-only or synthetic path
- [ ] An exhibit→script map lets a reader find the code behind any table or figure
- [ ] Environment (software/package versions) pinned; a Data Availability Statement drafted

## Anti-patterns

- A zip of scripts with no master file and no order — the reviewer cannot tell what to run
- Hand-coded institutional indices with no coding protocol, so the key variable cannot be reconstructed
- "Data available on request" with no procedure, for institutional data others genuinely cannot get
- Hard-coded absolute paths and unpinned package versions that break on another machine
- Treating the package as an afterthought for institutional data that took months to build by hand

## Worked vignette (illustrative)

A paper builds a governance-form variable by reading 3,000 procurement contracts and classifying each as arm's-length, hybrid, or integrated. The replication risk is the classification, not the regression. The package therefore includes: the coding manual with decision rules, a sample of coded contracts, a second coder's classifications on a 10% subsample with the agreement rate (say κ = 0.84, illustrative), and the script that turns the coded file into the analysis dataset — so the institutional measure, not just the estimation, is reproducible.

## Referee / editor concern mapped to the package fix

- *"How did you classify governance form? I cannot reproduce the key variable."* → Ship the coding manual, source-document samples, and inter-coder reliability — not just the final dataset.
- *"Your court/contract data are confidential; how can this be replicated?"* → State the exact access procedure and provide a code-only path plus a synthetic dataset that runs the full pipeline.
- *"Which script produces Table 4?"* → Include the exhibit→script map and a one-command master build with seeds fixed.
- *"What is the data-and-code policy here?"* → Confirm the current JLEO/OUP policy live (待核实) and draft a Data Availability Statement consistent with COPE expectations.

## Output format

```text
【Master build】one command raw→exhibits, seeds fixed? [Y/N]
【Institutional data construction】coding protocol + sources documented? [Y/N]
【Inter-coder reliability】reported where human-coded? [Y/N/NA]
【Provenance & access】per-source origin/date/license stated? [Y/N]
【Confidential data path】access procedure + code/synthetic path? [Y/N/NA]
【Exhibit→script map】present? [Y/N]
【DAS + environment】drafted and pinned? [Y/N]
【Next skill】jleo-referee-strategy
```
