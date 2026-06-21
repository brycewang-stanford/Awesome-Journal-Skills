---
name: aejpol-replication-package
description: Use when assembling the data and code deposit for an AEJ: Economic Policy manuscript to satisfy the AEA Data and Code Availability Policy and the AEA Data Editor's pre-publication reproducibility check. Builds the openICPSR deposit, README, and restricted-data access paths; it does not run the analysis or write the paper.
---

# Replication Package — AEA Data Editor Compliance (aejpol-replication-package)

## When to trigger

- A conditional acceptance / R&R asks for the data and code deposit
- You want to build the replication package as you go (recommended — the check is **before** publication)
- Some data are proprietary or restricted and you need a compliant access path
- The AEA Data Editor returned the package with required changes

## The AEA reproducibility regime (检索于 2026-06；以官网为准)

AEJ: Policy is an AEA journal and follows the **AEA Data and Code Availability Policy**. For accepted papers, authors deposit data, code, and documentation in the **AEA Data and Code Repository at openICPSR**, and the **AEA Data Editor** (Lars Vilhuber) runs a **reproducibility check before the paper is published**, not after. A **Data and Code Availability Statement** is required. Build the deposit to pass on the first pass.

### What the deposit must contain
- **All code** that produces every table, figure, and in-text number, organized so a single master script (`run_all`) regenerates the results from the analysis data.
- **Data** that can be shared, in the repository; for data that cannot, the exact **provenance and access instructions** (see restricted-data path below).
- A **README** following the AEA Data Editor's template: data sources and citations, data-availability statement, computational requirements (software + versions + packages), runtime, the map from code files to exhibits, and instructions to reproduce.
- **Dependencies pinned**: Stata `.ado` versions, R `renv.lock`, Python `requirements.txt`/`conda` env; seeds set and reported for any simulation/bootstrap/randomization inference.

### Restricted / proprietary data path
- State the **Data Availability Statement** clearly: which data are public, which are restricted, and how a replicator obtains the restricted parts (provider, application process, cost, approximate wait).
- Provide everything that *can* be shared (cleaning and analysis code, derived public extracts, synthetic or example data) so the Data Editor can verify the pipeline even without the raw restricted file.
- Confirm the access path is real and current — the Data Editor verifies it.
- Note any partial-reproducibility scope (e.g., one table from confidential data) in the README.

### Code posting during review
Review is single-blind, so the submission need not be anonymized; the openICPSR deposit is prepared at acceptance. Posting a working-paper code repository earlier is fine and does not conflict with the review process.

## Checklist

- [ ] Data and Code Availability Statement drafted (public vs. restricted, sources cited)
- [ ] One master script regenerates every exhibit and in-text number from analysis data
- [ ] README follows the AEA Data Editor template (sources, requirements, runtime, code→exhibit map)
- [ ] Software, package, and `.ado` versions pinned; seeds set and reported
- [ ] Restricted data: provenance + concrete access instructions + shareable code/extracts provided
- [ ] Deposit targets the AEA Data and Code Repository at openICPSR
- [ ] Ran the package clean on a fresh machine/folder before submitting to the Data Editor

## Anti-patterns

- Treating reproducibility as a post-acceptance afterthought — the check is pre-publication
- A README that lists files but no code→exhibit map or version/runtime information
- "Data available on request" with no access process for restricted data (non-compliant)
- Unpinned package versions or unset seeds, so results do not regenerate
- Hard-coded absolute paths that break on the Data Editor's machine
- Leaving an in-text number that no script in the deposit produces

## README skeleton (AEA Data Editor template, abbreviated)

A compliant README typically carries these sections, in order:
1. **Overview** — what the package contains and the paper it reproduces.
2. **Data availability statement** — each dataset: public / restricted; source citation; how to obtain.
3. **Computational requirements** — OS, software + versions, every package/`.ado` + version, hardware.
4. **Description of programs/code** — the `run_all` master and what each script does.
5. **Instructions to replicators** — exact run order and expected runtime.
6. **Map from code to output** — which script produces which table/figure/in-text number.
7. **Notes** — any partial-reproducibility scope and why.

## Worked vignette (illustrative)

A health-policy paper uses confidential claims data plus public state-policy data. Compliant deposit: a Data Availability Statement marking the claims data restricted (provider, DUA process, ~3-month wait) and the policy data public; the full cleaning/analysis code; a synthetic claims extract so the Data Editor can run the pipeline end-to-end; a README mapping `04_did.do` → Table 3 and Figure 2 with Stata 18 + `csdid`/`reghdfe` versions and an 18-minute runtime. The package regenerates every exhibit from the synthetic + public data on a clean machine.

## Output format

```
【Availability statement】public vs. restricted data + sources cited
【Master script】run_all regenerates all exhibits? [Y/N]
【README】AEA-template fields present (requirements/runtime/code→exhibit map)? [Y/N]
【Versions + seeds】pinned and reported? [Y/N]
【Restricted-data path】access instructions + shareable code/extract provided? [Y/N]
【Target repo】AEA Data and Code Repository (openICPSR)
【Next step】aejpol-submission
```
