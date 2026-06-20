---
name: jie-replication-and-data-policy
description: Use when preparing the replication package for a Journal of International Economics (JIE) manuscript — JIE requires that all materials needed to replicate published papers (computer programs and data sets) be deposited in the journal's secure repository (Mendeley Data). Builds the deposit; it does not run your analysis.
---

# Replication & Data Policy (jie-replication-and-data-policy)

## When to trigger

- Your JIE paper is heading toward acceptance and the data/code deposit is due
- You want to build the replication package as you go, not scramble at the end
- You have proprietary or restricted trade/macro data and need a compliant plan

## JIE's data/replication policy (verified 2026-06-20)

JIE requires that **all results be capable of replication**, and that **all materials needed to replicate published papers — including computer programs and data sets — be made available** at the journal's **secure repository**. In practice, replication files for published JIE papers are deposited and made available via **Mendeley Data** for the journal. Treat the deposit as a condition tied to publication: assemble it before acceptance, not after.

## What to deposit

- **Code**: every script that turns raw data into each table, figure, and reported number — including data-cleaning, gravity/PPML estimation, panel/local-projection code, and any structural solver/calibration code.
- **Data**: the analysis data sets, plus instructions to obtain any data you cannot redistribute (see proprietary case below).
- **A master script** (`run_all`) that regenerates every exhibit end-to-end.
- **A README** documenting software versions, package versions, run order, expected runtime, and a mapping from each table/figure to the script that produces it.

## International-economics specifics

- **Public-but-licensed sources** (UN Comtrade, BACI/CEPII, WITS, IMF/BIS): ship your extraction and cleaning code plus exact query parameters and access dates; do not redistribute data you are not licensed to repost.
- **Proprietary firm-level customs or bank data**: provide the **programs** and a clear data-availability statement explaining the access route, even when the microdata cannot be shared. Replicability of the pipeline is still required.
- **Structural papers**: deposit the model solver, calibration files, and counterfactual code (Dynare `.mod` files, Julia/MATLAB sources), not just regression scripts — the counterfactual must be reproducible.
- **Reproducibility hygiene**: pin versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` versions), set and report seeds for any simulation/estimation.

## Checklist

- [ ] Master `run_all` regenerates every table and figure from raw inputs
- [ ] README maps each exhibit → script; lists software/package versions and run order
- [ ] All estimation, gravity/PPML, and structural-solver code included
- [ ] Data sets included, or a data-availability statement for restricted/proprietary data with the access route
- [ ] Query parameters and access dates recorded for licensed public sources
- [ ] Seeds set and reported; versions pinned
- [ ] Package staged for deposit in the JIE secure repository (Mendeley Data) before acceptance

## Anti-patterns

- Promising "code available on request" instead of depositing it
- Depositing regression scripts but omitting the structural solver/calibration files
- Reposting Comtrade/BACI/proprietary data you are not licensed to share
- No README mapping exhibits to scripts, so the package is unrunnable
- Building the package only after acceptance, then discovering it does not reproduce

## Data-availability decision aid for international-economics sources

Match each input to the right deposit treatment; the wrong choice either breaches a license or makes the pipeline unrunnable.

- **Public-but-licensed (Comtrade, BACI/CEPII, WITS, IMF IFS/BOP, BIS, PWT, External Wealth of Nations):** deposit extraction/cleaning code plus exact query parameters and access dates; do not repost raw files you cannot redistribute.
- **Proprietary microdata (firm-level customs, bank or transaction records):** deposit the full programs and a data-availability statement naming the provider and access route; the pipeline must replicate even when the microdata cannot ship.
- **Self-constructed data (a new tariff/NTM measure, a hand-coded RTA or default history):** deposit the data and construction code — often the paper's novelty, so it must be reproducible.

## Worked deposit example (illustrative structure)

A gravity-plus-counterfactual paper. `run_all.do` calls in order: `01_build_baci.do` (BACI → clean dyad-year panel), `02_merge_gravity.do` (CEPII covariates), `03_ppml.do` (the `ppmlhdfe` estimates behind Tables 2–4), `04_counterfactual.jl` (the exact-hat-algebra welfare exercise behind Figure 5), and `05_exhibits.do` (regenerates every exhibit). The README maps each exhibit to its script, lists package versions, records the BACI access date and Comtrade query string, sets the bootstrap seed, and notes the raw BACI files are reproducible from the recorded query but not redistributed. Stage all of this for the JIE secure repository (Mendeley Data) before acceptance.

## Output format

```
【Master script】run_all regenerates all exhibits? [Y/N]
【README】exhibit→script map + versions + run order? [Y/N]
【Code included】cleaning / PPML / panel / structural solver? [Y/N each]
【Data】shared / data-availability statement for restricted sources? [which]
【Reproducibility】seeds reported, versions pinned? [Y/N]
【Repository】staged for JIE secure repo (Mendeley Data)? [Y/N]
【Next step】jie-review-process / jie-submission
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and the data sources whose licenses constrain redistribution
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JIE data-policy and Mendeley Data sources
