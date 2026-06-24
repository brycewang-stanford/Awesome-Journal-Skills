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

## Claim-to-archive ledger

Before submission, create a ledger with one row per main claim:

```text
Claim | Exhibit | Input data | Code target | Inference choice | Archive file
```

Use it to catch unsupported claims and archive gaps. If a row has no code target, the exhibit is not
reproducible. If a row has no inference rationale, a referee can challenge the standard errors before
engaging the economics. If a row has no archive file, the Data Archive package will not reproduce the
published paper.

The ledger also clarifies what belongs in the online appendix: diagnostics and robustness checks that
support a ledger row should be preserved there, even if the main article cannot spare space.

## Inference picker for archive-bound estimates

JAE referees rerun your code, so the inference choice must be defensible *and* visible in the deposited scripts. Default mapping:

| Data structure | Expected inference at JAE | What the table note states |
| --- | --- | --- |
| Time series, serial correlation | HAC / Newey–West; justify bandwidth/lag choice | Kernel, lag truncation, sample span |
| Panel, many clusters (≈40+) | Cluster-robust at the treatment/assignment level | Cluster variable and count |
| Panel, few clusters (<~30) | Wild cluster bootstrap (Rademacher/Webb weights) | Bootstrap type, replications, seed |
| IV with modest first stage | Weak-IV-robust (Anderson–Rubin CI; effective F) | First-stage F alongside the 2SLS column |
| Forecast comparisons | Diebold–Mariano-style tests with HAC variance | Loss function and comparison window |

## Few-cluster and weak-instrument trip wires

Two inference failures recur in JAE referee reports: cluster-robust SEs treated as valid with a handful of clusters, and 2SLS t-statistics reported without weak-IV diagnostics. Pre-empt both — report the cluster count in every clustered table, switch to wild cluster bootstrap p-values when it is small, and pair any IV column with the effective first-stage F plus an Anderson–Rubin interval. Put the bootstrap loop in the deposited code with its seed so the archived p-value regenerates digit-for-digit.

## Worked numbers: a 13-state policy panel (illustrative)

A staggered state-policy evaluation with 13 treated-side clusters: CRVE gives β = −0.042, s.e. 0.018, p ≈ 0.02; the wild cluster bootstrap (Webb weights, 9,999 draws, seed logged) gives p ≈ 0.08. The JAE-grade move is to report both, lead with the bootstrap, and let the online appendix carry the full grid (weight choice, replications, leave-one-cluster-out). The archived `infer_main.do` regenerates each p-value; the readme names the seed. Hiding the fragile p-value is the move referees at this venue are trained to catch.

## Monte Carlo specification block

When simulation evidence backs the empirical design, register it like an exhibit:

```text
DGP: [equations + parameter values, calibrated to the application]
Sample sizes: [matching the real data, plus stress values]
Replications: [count] | Seed: [value] | Software: [version]
Script: sims/mc_main.R → outputs tables/mc_table3.csv
Question answered: [which empirical inference concern this resolves]
```

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Applied econometrics: the estimator and its diagnostics are themselves the contribution, so foreground the weak-IV / pre-trend / sensitivity tooling.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Output format

```
【Master script】regenerates all exhibits? [Y/N]
【Repro】versions pinned + seeds fixed? [Y/N]
【Inference】HAC / clustered / bootstrap / weak-IV — matched? [Y/N]
【Few-cluster guard】cluster counts reported; bootstrap where small? [Y/N]
【Archive format】plain CSV + readme alongside (not .dta-only)? [Y/N]
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — estimation, inference, reproducibility tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — archive format-rule sources
