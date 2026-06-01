---
name: jape-data-analysis
description: Use when running estimation and inference for a Journal of Applied Econometrics (JAE) manuscript so the analysis is reproducible and archive-ready — every table/figure regeneratable from plain-text data and programs you will deposit in the JAE Data Archive. Covers robust inference, master-script discipline, Monte Carlo evidence, and the archive's plain-ASCII/CSV format rule.
---

# Data Analysis for JAE (jape-data-analysis)

## When to trigger

- Setting up the estimation pipeline for a JAE paper
- Choosing inference (HAC, clustered, bootstrap) for real-data estimates
- Making sure the analysis will satisfy the JAE Data Archive before you submit

## Analyze for reproducibility from day one

JAE's identity is **replicable** applied work, and accepted papers must deposit data and (typically) programs in the **JAE Data Archive**. Structure the analysis as if a referee will rerun it:

- One **master script** (`run_all.do` / `make` / `Snakefile`) regenerates **every** exhibit from raw inputs — no manual steps.
- Pin software (`version` in Stata, `renv`/`sessionInfo()` in R, pinned `requirements.txt` in Python); fix and log all seeds.
- Document sample construction, variable definitions, and estimation commands so the path from raw or documented restricted data to final exhibits is transparent.
- Write intermediate and final results to **plain text** (CSV/TXT), matching the archive format — never let `.dta` be the only copy.

## Inference appropriate to real data

Match inference to structure: HAC/Newey–West for serial correlation; cluster-robust SEs for panels; wild/cluster bootstrap with few clusters; weak-IV-robust inference for IV. State which adjustment you use and why.

## Monte Carlo, where used

If you stress-test a method, report the DGP, sample sizes, replication count, and seeds, and ship the simulation script so the tables regenerate exactly. Simulations should illuminate the *empirical* problem, not stand alone.

## Output format

```
【Master script】regenerates all exhibits? [Y/N]
【Repro】versions pinned + seeds fixed? [Y/N]
【Inference】HAC / clustered / bootstrap / weak-IV — matched? [Y/N]
【Archive format】plain CSV + readme alongside (not .dta-only)? [Y/N]
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — archive format-rule sources
