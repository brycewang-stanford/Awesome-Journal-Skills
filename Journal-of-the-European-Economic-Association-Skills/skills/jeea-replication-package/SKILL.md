---
name: jeea-replication-package
description: Use when assembling the data and code replication package for a Journal of the European Economic Association (JEEA) manuscript so it clears the JEEA Data Editor's pre-acceptance verification under the DCAS standard. Builds the package and README; it does not run the analysis.
---

# Replication Package (jeea-replication-package)

## When to trigger

- The paper has empirical, simulation, or experimental work and acceptance is in sight
- A co-editor or the JEEA Data Editor asked for the data-and-code deposit
- You want the package built *before* submission so the Data Editor check is painless
- Results were produced ad hoc and you need a one-click reproduction path

## The JEEA data & code bar (source map refreshed 2026-06-20)

JEEA **endorses DCAS — the Data and Code Availability Standard — and applies it (since Feb 1, 2024)**. JEEA publishes empirical/simulation/experimental papers **only if** the data are clearly and precisely documented and readily available for replication; for accepted papers the authors must supply, **before publication**, the data, programs, and computation details sufficient to permit replication. The **JEEA Data Editor (Maia Güell)** runs a verification check, and an empirical paper can only be formally accepted after the Data Editor confirms the results replicate. Replication packages are posted publicly through the **JEEA Community at Zenodo** after the check. Build the package as you go — do not leave it to acceptance.

## Package structure

```
replication/
  README.md            <- the map: data sources, software/versions, how to run, what each output is
  data/
    raw/               raw data (read-only) OR access instructions if restricted
    clean/             generated; rebuilt by code
  code/
    00_master.*        one script regenerates EVERY table and figure from raw data
    01_..09_*          ordered steps (clean → analyze → robustness → exhibits)
  output/
    tables/  figures/  generated outputs, named to match the paper
```

## README must state

- **Data provenance and access:** every source, with citation; for restricted/proprietary data, exact access instructions and any exemption/limited-access request (state at submission).
- **Software and versions:** Stata/R/Python/Julia versions; pinned packages (`renv.lock`, `requirements.txt`/conda env, `Project.toml`); recorded Stata `ssc`/`net` versions.
- **How to run:** the one master script, expected runtime, and hardware notes for long jobs.
- **Output map:** which script produces which table/figure (named to match the paper exactly).
- **Seeds:** set and reported for every simulation / bootstrap / randomization-inference step.
- **Partial-check scope:** if any result cannot be fully reproduced (confidential data, huge compute), document exactly what the Data Editor can and cannot verify, and provide simplified/manageable versions plus summary outputs.

## Checklist

- [ ] One master script regenerates all tables and figures from raw data
- [ ] Software versions and packages pinned and recorded
- [ ] Every seed set and reported (simulation / bootstrap / RI)
- [ ] README maps each output to the script that produces it (paper-matching names)
- [ ] Restricted data: access instructions + exemption/limited-access request stated at submission
- [ ] Partial-check scope documented; simplified versions + summary outputs shipped where needed
- [ ] Package ZIP readied for JEEA's online data submission platform and later Zenodo community deposit

## Anti-patterns

- Leaving the package to post-acceptance — the Data Editor check **gates** formal acceptance
- A README that lists files but never says how to run them end-to-end
- Unpinned package versions, so the Data Editor's run diverges from yours
- Unset/unreported seeds, so simulation or bootstrap results do not reproduce
- Output filenames that do not match the table/figure numbers in the paper
- Hiding that a key result rests on confidential data instead of documenting the access path

## Output format

```
【Master script】regenerates all exhibits from raw? [Y/N]
【Versions/seeds】pinned + reported? [Y/N]
【README output map】each table/figure → script? [Y/N]
【Restricted data】access + exemption stated? [Y/N or N/A]
【Partial-check scope】documented? [Y/N or N/A]
【Zenodo/DCAS】package readied for JEEA community? [Y/N]
【Next step】jeea-referee-strategy
```
