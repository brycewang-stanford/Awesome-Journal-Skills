---
name: restud-replication-package
description: Use when assembling the data and code deposit for an accepted empirical The Review of Economic Studies (REStud) manuscript, writing the README, or auditing reproducibility before the journal's Data Editor runs the pre-publication reproducibility check. Builds a deposit-ready package; does not run the analysis. Verify the current REStud/OUP data policy on the official page.
---

# REStud Replication Package (restud-replication-package)

## When to trigger

- A conditional acceptance arrived and the Data Editor's reproducibility check is coming
- Drafting the README at any point (recommended: from day one of the project)
- Auditing reproducibility before submitting the deposit
- A prior deposit was returned for incomplete provenance or non-running code

## REStud's actual data & code availability policy

REStud has a **Data Editor** (Miklós Koren; verified 2026-05-30) and follows the **AEA Data and Code Availability Standard (DCAS)**, the same standard the AEA journals and Econometric Society use. Its defining feature, which differs from journals that merely "encourage sharing": the Data Editor runs a **reproducibility check on the data and code before the paper is published** — the code is actually executed to confirm it reproduces the reported results, and publication is conditional on passing. Accepted papers' replication packages are **deposited at Zenodo** (the journal's / Society's Zenodo community), where the package receives a DOI; you may reserve the DOI in advance and finalize after the check. **Exemptions exist for confidential / proprietary / restricted data** — notify the editors *at submission* — but even then you must provide the **code plus a clear description of how to obtain the data**. Authors may also be asked for materials at the review stage if a referee or editor requests it. Exact forms, repository, and timing **change — verify on https://www.restud.com/submissions/ and the REStud Data Editor site (https://restud.github.io/data-editor/before/) before depositing.**

## Repository structure

```text
replication-package/
├── README.md (or README.pdf)
├── LICENSE                     (MIT/CC-BY for code; data per source license)
├── data/
│   ├── raw/                    (original files, never modified)
│   ├── intermediate/           (cleaned analytic datasets)
│   └── codebook/               (variable definitions, source mapping)
├── code/
│   ├── 00_setup.do             (or .R / .py)
│   ├── 01_clean.do
│   ├── 02_analysis.do
│   ├── 03_tables.do
│   └── 04_figures.do
├── output/
│   ├── tables/
│   └── figures/
└── docs/
    ├── data_appendix.pdf
    └── computing_environment.txt
```

## README required sections

1. **Overview** — what the package does, which paper, software required.
2. **Data availability and provenance** — for every dataset: source (URL/institution), citation, license/terms, date accessed, whether included and if not, why. Restricted data: commit to ≥ 5-year preservation, assist reasonable requests, make code public, document access fully.
3. **Dataset list** — table: Filename | Description | Source | Notes.
4. **Computational requirements** — OS, software versions, packages, runtime, peak memory.
5. **Description of programs** — what each script does and the run order; name the master script.
6. **Instructions to replicators** — literal step-by-step from a clean state.
7. **List of tables/figures → programs** — map every published exhibit to the script and line that produces it (this is exactly what the Data Editor reruns).

## Coding discipline (adopt from day one)

- **One master script** runs the whole pipeline end-to-end — the Data Editor will run it on a clean machine.
- **Relative paths only** — never `/Users/yourname/...`.
- **Set the random seed** explicitly in any stochastic step.
- **Version-pin packages**: Stata `version 18.0` + a setup do-file; R `renv`; Python `requirements.txt` with `==` pins.
- **Log files** for every run.
- For structural/theory-empirical papers: deposit the estimation code, the solver/optimizer settings, and the counterfactual code; document convergence criteria and starting values.

## Checklist

- [ ] Master script runs from a clean state on a different machine (mirrors the Data Editor's check)
- [ ] All paths relative; random seeds set
- [ ] Software and package versions documented and pinned
- [ ] README covers every dataset's provenance
- [ ] Every published table/figure mapped to its producing script and line
- [ ] Restricted data: provenance + runnable code + synthetic-data smoke test where possible
- [ ] Files visible in the repository, not hidden behind one opaque ZIP
- [ ] Package laid out to the **AEA DCAS** template (README + data + code + DCAS-style data-availability statement)
- [ ] Zenodo deposit drafted / DOI reserved
- [ ] Current REStud Data Editor forms and policy verified on the official page

## Anti-patterns

- Waiting until acceptance to start the deposit — the pre-publication check delays papers that fail it
- "Data available from the authors upon request" — does not satisfy REStud's policy
- A README written for collaborators rather than for an unknown replicator (or the Data Editor)
- Hardcoded absolute paths; unpinned packages; a master script that errors on a clean machine
- Depositing summary tables but not the code that produced the regressions
- Assuming the deposit is just a courtesy upload — at REStud it is *verified by execution* (DCAS check by the Data Editor) before publication
- Treating proprietary data as a pass on the deposit — code and an access description are still required, and the editors must be told at submission

## Output format

```
【DEPOSIT TYPE】public-data | restricted-data | hybrid
【README STATUS】complete / incomplete
【REPRODUCIBILITY CHECK】self-tested clean / not yet (Data Editor reruns before publication)
【STRUCTURAL CODE INCLUDED】yes / n/a
【POLICY VERIFIED ON OFFICIAL PAGE】yes / no
【NEXT SKILL】restud-referee-strategy | restud-submission
```
