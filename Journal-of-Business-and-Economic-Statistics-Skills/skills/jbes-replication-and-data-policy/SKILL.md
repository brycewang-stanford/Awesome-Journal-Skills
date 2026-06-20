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

JBES is owned by the **American Statistical Association** and published by Taylor & Francis, so it follows **ASA's data-sharing and reproducibility policy** rather than the AEA Data Editor regime. Under that policy, the ASA **strongly encourages** authors to include **data sets and code as supplementary material** that demonstrate the article's results, to make the underlying data **publicly available**, and to include a **data availability statement**; individual ASA journal editors may set their own stricter rules, and authors may request a **waiver** for confidentiality/security reasons. Important: JBES does **NOT** use the JAE Data Archive — that archive belongs to the *Journal of Applied Econometrics*, a separate Wiley journal. Treat any stricter JBES-specific enforcement as a live T&F instructions check.

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
- [ ] Live JBES-specific enforcement checked if submission-ready advice is being given

## Anti-patterns

- A zip of scripts with no README and no run order
- Hard-coded local paths that break on another machine
- Missing seeds, so Monte Carlo numbers cannot be reproduced
- Assuming the JAE Data Archive applies (it does not — that is a different journal)
- Asserting JBES mandates deposit beyond ASA policy without checking the live T&F instructions

## Worked vignette: building a supplement for a Bayesian VAR forecasting paper

A hypothetical JBES paper proposes a hierarchical-shrinkage Bayesian VAR and forecasts US macro aggregates from FRED-MD (details **illustrative**). The supplement README pins R 4.3 with `renv.lock`, records the FRED-MD vintage (2024-03) and access date, and sets the Gibbs-sampler seed plus an illustrative 20,000 draws after a 5,000 burn-in. One master script runs `01_simulation` (coverage tables) then `02_application` (forecast figures), with an exhibit map tying Table 3 to its script and a stated 40-minute wall-clock on documented hardware. Because every posterior summary is seed-pinned, a referee who reruns it reproduces the numbers exactly — pre-empting the "I could not regenerate Table 3" report.

## Reproducibility-pushback patterns (venue-specific fixes)

| JBES referee/editor objection | Fix this skill enforces |
|----|----|
| "I could not reproduce the Monte Carlo numbers." | Set and report seeds for every stochastic step; pin the replication count |
| "Your scripts assume your machine." | Remove absolute paths; pin package versions via `renv.lock`/`requirements.txt` |
| "Where is the data availability statement?" | Draft it per ASA expectation; for restricted data give access steps plus a runnable proxy |

Calibration anchor (hedged): JBES follows **ASA data-sharing and reproducibility policy** under Taylor &
Francis — *not* the AEA Data Editor regime and *not* the JAE Data Archive (a different journal). ASA
strongly encourages a code-and-data supplement and a data availability statement; check live T&F
instructions before asserting stricter JBES-specific enforcement.

## Output format

```
【Master script】regenerates all tables/figures incl. Monte Carlo? [Y/N]
【Env pinned】versions + packages documented? [Y/N]
【Seeds】set + reported? [Y/N]
【Data availability statement】drafted? [Y/N]
【Restricted data】access steps + runnable proxy? [Y/N / NA]
【Policy check】live JBES-specific enforcement checked if needed? [Y/N]
【Next step】jbes-review-process
```
