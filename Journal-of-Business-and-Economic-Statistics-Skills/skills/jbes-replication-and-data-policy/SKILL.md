---
name: jbes-replication-and-data-policy
description: Use when assembling the reproducible data-and-code supplement for a Journal of Business & Economic Statistics (JBES) paper under the American Statistical Association (ASA) data-sharing and reproducibility policy. Builds the supplement; it does not run the analysis itself.
---

# Replication & Data Policy (jbes-replication-and-data-policy)

## When to trigger

- The paper is heading toward submission/acceptance and a code+data supplement is needed
- You want a reproducible pipeline early to pre-empt referee replication requests
- Raw data are restricted/proprietary and you need a disclosure-compliant plan
- You need to write a data availability statement

## Why this matters at JBES

JBES is owned by the **American Statistical Association** and published by Taylor & Francis, so it follows **ASA's data-sharing and reproducibility policy** rather than the AEA Data Editor regime. Under that policy, the ASA **strongly encourages** authors to include **data sets and code as supplementary material** that demonstrate the article's results, to make the underlying data **publicly available**, and to include a **data availability statement**; individual ASA journal editors may set their own (possibly stricter) rules, and authors may request a **waiver** for confidentiality/security reasons. Important: JBES does **NOT** use the JAE Data Archive — that archive belongs to the *Journal of Applied Econometrics*, a separate Wiley journal. Whether JBES **mandates** code+data at acceptance with a dedicated reproducibility check (as JASA does) versus merely encouraging it could not be confirmed and is **待核实** — verify on the live instructions page.

## Supplement anatomy (methods paper)

```
supplement/
  README.{md,pdf}      # data sources, software versions, run order, runtime, exhibit map
  code/
    00_setup           # installs/pins packages, sets paths, sets seeds
    01_simulation      # regenerates every Monte Carlo table/figure
    02_application     # regenerates every empirical table/figure
  data/
    raw/               # as obtained, or access instructions if restricted
    derived/           # built by code, never hand-edited
  output/              # regenerated, checked against the manuscript
```

## README must specify

- **Provenance** of every data source (version/vintage, access date); for restricted data, exact access steps.
- **Software environment** with pinned versions (`renv.lock`, `requirements.txt`, recorded `ssc`/`net` + Stata version).
- **Run order** via one master script; expected wall-clock runtime, hardware, and total Monte Carlo replications.
- **Seeds** for every simulation/bootstrap/randomization step.
- **Exhibit map** linking each table/figure (including simulation tables) to the script that produces it.

## Checklist

- [ ] One master script regenerates every table and figure, including all Monte Carlo numbers
- [ ] Software and package versions pinned and documented
- [ ] Random seeds set and reported for all stochastic steps
- [ ] Data availability statement drafted (ASA expectation)
- [ ] Restricted/proprietary data have documented access steps + a runnable proxy
- [ ] No hand-edited derived data; absolute paths removed
- [ ] Output regenerated and checked against the manuscript numbers
- [ ] Live JBES enforcement (mandatory vs encouraged) verified (待核实)

## Anti-patterns

- A zip of scripts with no README and no run order
- Hard-coded local paths that break on another machine
- Missing seeds, so Monte Carlo numbers cannot be reproduced
- Assuming the JAE Data Archive applies (it does not — that is a different journal)
- Asserting JBES mandates deposit without checking (status is 待核实)

## Output format

```
【Master script】regenerates all tables/figures incl. Monte Carlo? [Y/N]
【Env pinned】versions + packages documented? [Y/N]
【Seeds】set + reported? [Y/N]
【Data availability statement】drafted? [Y/N]
【Restricted data】access steps + runnable proxy? [Y/N / NA]
【Policy check】live JBES enforcement verified? [Y/N — 待核实]
【Next step】jbes-review-process
```
