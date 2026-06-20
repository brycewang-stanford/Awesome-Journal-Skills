---
name: jle-replication-package
description: Use when assembling the data and code package for a The Journal of Law and Economics (JLE) manuscript to satisfy the journal's replication policy — data, programs, and computation details available for replication before publication. Builds the deposit and README; it does not run the analysis or write the paper.
---

# Replication Package & JLE Data Policy (jle-replication-package)

## When to trigger

- The paper is empirical (or has simulations/experiments) and you are heading toward acceptance, or want to build the package early
- An R&R or conditional acceptance asks you to prepare the data + code deposit
- You need to write the README and a data-availability statement to JLE standard
- Some data are restricted (sealed court records, proprietary firm data) and you must plan the deposit around that

## Why this matters at JLE

JLE's stated policy is to publish empirical/simulation/experimental papers **only if the data are clearly and precisely documented and readily available to any researcher for replication**, and authors of accepted papers must provide the **data, programs, and other computation details sufficient to permit replication, prior to publication** (检索于 2026-06；以官网为准; verify on journals.uchicago.edu/journals/jle/data-policy). This is a **pre-publication** requirement, not an acceptance-day formality. JLE does not run the AEA-style openICPSR pipeline; the obligation is documentation and availability — so build a package any researcher could re-run, and treat it as a gate, not a chore. Law-and-economics data raise distinctive access issues (court records, sealed cases, regulatory filings, proprietary market data) that you must plan for explicitly.

## What the package must contain

| Component | Requirement |
|-----------|-------------|
| **Data files** | All data used to produce the results, documented; or, for restricted data, a precise access path |
| **Analysis + transformation code** | Every script from raw legal/regulatory data → cleaned data → each table/figure |
| **Master script** | One `run_all` that regenerates every exhibit from the inputs |
| **README** | Data sources and provenance, computational requirements, run instructions, and an exhibit-to-code map |
| **Data-availability statement** | Provenance and access terms for each dataset (court system, agency, vendor), stated in the paper |
| **Legal-data documentation** | How statutes/cases were coded, the coding protocol, and inter-coder checks for hand-coded doctrine |

## Handling restricted or proprietary legal data

- Sealed court records, individual case files, and proprietary market data often **cannot be redistributed.** Deposit all code regardless, and document the exact access procedure (court/agency/vendor, application steps, cost, approximate wait, any data-use agreement).
- Provide a **synthetic or public extract** so the code runs and a verifier can check the logic where the real data cannot be shared.
- For **hand-coded legal variables** (a damages-cap index, a liability-standard classification), deposit the coding protocol, the source documents list, and inter-coder reliability so the measurement is reproducible.
- Flag any restricted-data or exemption situation **early in the process**, not at the pre-publication check.

## Reproducibility hygiene (build as you go)

- **Pin versions:** Stata `version` + recorded `ssc`/`net` package versions; `requirements.txt`/conda env (Python); `renv.lock` (R).
- **Set and report seeds** for every simulation, bootstrap, and randomization/permutation step.
- **No absolute paths** — one root macro/variable; relative paths thereafter.
- **Exhibit-to-code map** in the README: Table 2 → `code/05_did.do`, Figure 1 → `code/06_event_study.R`, etc.
- **Run it clean** on a fresh checkout before depositing.

> Adapt the vendored skeleton in [`../../resources/code/`](../../resources/code/) (master script → clean → descriptive → DiD/IV/RD → mechanism → robustness → tables) as the package backbone.

## Checklist

- [ ] One `run_all` master script regenerates every table and figure from the inputs
- [ ] All data documented and available (or restricted-data access path fully documented + synthetic extract provided)
- [ ] README with complete exhibit-to-code map and computational requirements
- [ ] Data-availability statement for every dataset, with provenance and access terms
- [ ] Hand-coded legal variables: coding protocol + sources + inter-coder reliability deposited
- [ ] Software/package versions pinned; seeds set and reported; no absolute paths; clean fresh run
- [ ] Restricted-data / sealed-records situations flagged early, not at the pre-publication check

## Anti-patterns

- Treating the deposit as an acceptance-day task — the policy requires materials available **before publication**
- Depositing code with absolute paths or unrecorded package versions (will not reproduce)
- Hand-coded legal variables with no coding protocol or reliability check (measurement not reproducible)
- Restricted court/market data discovered at the check with no access documentation or synthetic extract
- Unset seeds making bootstrap/permutation results non-reproducible

## Common legal-data provenance situations

Law-and-economics data come from a handful of recurring sources, each with its own access and documentation pattern. Name yours and document accordingly:

| Source | Access reality | What to document |
|--------|---------------|------------------|
| Court records (PACER, state dockets) | often public but fee-gated or rate-limited; some sealed | the query/scrape procedure, date pulled, sealed-case handling |
| Administrative / regulatory filings (SEC EDGAR, agency dockets) | usually public | the form types, vintage, and any parsing code |
| Enforcement / litigation databases (vendor) | proprietary, license-restricted | the vendor, license terms, and a synthetic extract |
| Statute / case coding (hand-built) | you create it | the coding manual, sources, and inter-coder reliability |
| Linked administrative microdata (sealed) | DUA-restricted, non-redistributable | the application path, DUA terms, wait time, synthetic schema |

The reproducibility obligation is the same in every row: someone who legitimately obtains the source must be able to re-run your code and recover every exhibit.

## Worked vignette (illustrative)

A paper on judge assignment uses individual case records the court provides only under a data-use agreement. The author cannot redistribute them, so the package deposits: (i) all cleaning and analysis code; (ii) a documented access path (the court's data-request form, the DUA terms, the ~10-week wait); (iii) a synthetic case file with the same schema so `run_all` executes end-to-end and a verifier can confirm the logic; and (iv) the judge-leniency leave-out construction script. The hand-coded ruling-type variable ships with its coding manual and a 200-case inter-coder reliability table. Any researcher who obtains the records can reproduce every exhibit — the JLE standard.

## Output format

```
【Master script】run_all regenerates all exhibits from inputs? [Y/N]
【Data】documented + available, or restricted path + synthetic extract? [state]
【README】exhibit-to-code map + computational requirements complete? [Y/N]
【DAS】provenance + access terms for every dataset? [Y/N]
【Legal coding】protocol + sources + inter-coder reliability deposited? [Y/N/NA]
【Reproducibility】versions pinned + seeds + no absolute paths + clean fresh run? [Y/N]
【Restricted/sealed】flagged early? [Y/N/NA]
【Next step】jle-referee-strategy (or jle-submission)
```
