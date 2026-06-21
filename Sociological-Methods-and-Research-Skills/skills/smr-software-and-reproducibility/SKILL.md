---
name: smr-software-and-reproducibility
description: Use when preparing the released software, code, data, and reproducibility materials for a Sociological Methods & Research (SMR) paper — a usable package plus scripts that recreate every table, figure, and simulation, and the SMR data-and-code availability statement. Builds the reproducibility layer; does not write the manuscript.
---

# SMR Software and Reproducibility

Use this to meet SMR's defining expectation: a methods paper should ship a **method other people can
run**. SMR readers adopt methods, so released, documented software and a reproducible pipeline are
not optional extras — a beautiful estimator with no usable code is a method no one will use, and
reviewers know it.

## What "released software" means at SMR

- A **package or well-structured code** implementing the method in a mainstream environment (R, Stata,
  Python — whatever the audience uses), with a documented interface, not a private analysis script.
- **Worked usage**: a minimal example that runs the method on toy or example data, so a reader can
  confirm it works before adapting it.
- **Versioned and citable**: deposit in a trusted public repository (e.g., a tagged release with a DOI)
  rather than a personal homepage that can disappear.

## The reproducibility pipeline

Every exhibit in the paper must be regenerable:

- A **README** stating software versions, dependencies, expected runtime, and the entry-point command.
- A **master script** that runs the full pipeline: simulation grid → tables → figures → illustration,
  with **seeds fixed** so Monte Carlo results reproduce exactly.
- **One command per exhibit** mapping (or a clear table) so a replicator knows which script produces
  Table 2, Figure 3, etc.
- For long simulations, provide a **smoke-test mode** (few replications) that runs quickly and a
  full-run mode that reproduces the paper.

## The SMR availability statement

SMR requires a **data-and-code availability statement** (检索于 2026-06；以官网为准):

- Disclose **how the study data, code, and materials can be permanently accessed** — repository name,
  DOI/URL, and any access conditions.
- **Code and materials** are expected; **data** should be deposited where possible, and restricted data
  must state the reason and the access path/conditions in the statement.
- Use a **trusted public repository**; reference datasets in **DataCite** style.
- Write the statement at submission, not at acceptance — it is part of the manuscript's conformance.

## Anonymization of the package under double-anonymized review

- The released materials submitted for review must not deanonymize: strip author names, institutional
  paths, and account handles from code, README, and repository metadata.
- Use an **anonymized repository** (e.g., a blinded archive) for the review copy; reveal the public,
  citable version at acceptance.

## Checklist

- [ ] The method is released as a usable package/structured code, not a private script.
- [ ] A minimal runnable usage example is included.
- [ ] The code is versioned and deposited in a trusted, citable public repository.
- [ ] A README states versions, dependencies, runtime, and the entry command.
- [ ] A master script reproduces every table, figure, and the simulation, with seeds fixed.
- [ ] An exhibit→script map lets a replicator find each result.
- [ ] A smoke-test mode exists for long simulations.
- [ ] The data-and-code availability statement is written, with repository/DOI and any access conditions.
- [ ] The review-copy materials are anonymized.

## Anti-patterns

- **Private analysis script as "software"**: code that only the authors can run.
- **Unseeded simulation**: Monte Carlo results that cannot be reproduced.
- **Disappearing host**: code on a personal homepage with no archive/DOI.
- **Missing exhibit map**: a replicator cannot tell which script makes which table.
- **Availability statement deferred** to acceptance, or vague ("available on request").
- **Deanonymizing repo metadata** in the review copy.

## Output format

```text
[Reproducibility status] release-ready / needs work / not ready
[Software] package/structured code? usage example? citable deposit?
[Pipeline] master script + seeds + exhibit map present? smoke-test mode?
[Availability statement] written? repository/DOI + access conditions stated?
[Anonymization] review-copy materials clean? yes/no
[Next SMR skill] smr-submission
```
