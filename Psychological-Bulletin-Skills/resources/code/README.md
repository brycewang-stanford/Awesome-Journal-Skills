<!-- Vendored from shared-resources/empirical-methods/code (Stata 18 MP verified, 2026-06) for Psychological-Bulletin-Skills self-containment. Do not edit commands here; edit the canonical source. -->
# Code Template Library (Stata + Python)

> Adapted from the verified Economic-Research-Journal-Skills/resources/code library (Stata 18 MP, 2026-06); translated to English and made venue-neutral.

A reproducible code skeleton for empirical causal-inference research, venue-neutral and ready to copy-and-adapt. It serves both as "ready-to-run" templates for each identification method and as a concrete layout for a one-click reproduction workflow.

> **Verified-on-Stata-18 (per the source library):** the core command chains were run end-to-end on synthetic data on Stata 18 MP and ran successfully (2026-06): `reghdfe` (TWFE), `bacondecomp`, `csdid`, `did_imputation`, the event-study + parallel-trends joint test, `esttab` three-line-table export, `ivreg2` + KP rk F, `weakivtest` effective F, `rdrobust`, and `rddensity`. All command syntax has been checked. For version-sensitive points (see below), defer to the latest official documentation.

> **Stata do-file rule (verified):** in **do-file mode** a loop body must NOT share a line with `{` — a newline is required after the opening brace. This library follows that rule throughout (see the `forvalues` / `foreach` blocks).

## How to use

1. Organize the project as below, with the scripts in this directory under `code/`:

```
project/
  ├── data/raw/         raw data (read-only)
  ├── data/clean/       cleaned data
  ├── code/             <- scripts in this directory
  ├── output/tables/
  └── output/figures/
```

2. Open `stata/00_master.do`, change `global root` to your project root, and uncomment the dependency-install block on the first run.
3. Run `do code/00_master.do` for a one-click pass: clean -> describe -> identify -> mechanism -> robustness -> export tables/figures.

Throughout the scripts, illustrative names are kept generic: `Y` (outcome), `D` / `treat` (treatment), `id` (unit), `year`, `gvar` (first treated period), and a `controls` list (`size lev roa age group`).

## Stata scripts at a glance

| File | Purpose |
|------|---------|
| `00_master.do` | One-click master: paths, dependencies, fixed random seed |
| `01_clean.do` | Raw -> analysis sample: merge, recorded filtering, variable construction, winsorize |
| `02_descriptive.do` | Descriptive-statistics table; treatment/control balance |
| `03_did_modern.do` | TWFE baseline -> Bacon decomposition -> CS/BJS/SA/dCDH -> event study |
| `04_iv.do` | IV: KP rk F + effective F (`weakivtest`) + AR-robust inference (`weakiv`) |
| `05_rdd.do` | RDD: `rdrobust` bias-corrected robust CI + `rddensity` manipulation test |
| `06_dml.do` | Double machine learning: `ddml` + `pystacked` multi-learner |
| `07_mechanism.do` | Mechanism: estimate D->M only; argue M->Y by theory |
| `08_robustness.do` | Robustness system organized by identification threat + placebo + wild bootstrap |
| `09_tables.do` | Three-line tables (`esttab`) and event-study figure export |

## Python scripts at a glance

| File | Purpose |
|------|---------|
| `python/clean_panel.py` | Large-scale micro-panel cleaning (pandas), outputs `analysis.dta` |
| `python/dml_doubleml.py` | DoubleML PLR, multi-learner robustness comparison |
| `python/event_study_plot.py` | Publication-grade event-study / parallel-trends plot (matplotlib, >= 300 dpi) |

## Modern estimators and command quick reference

| Method | Paper | Stata | Python / R |
|--------|-------|-------|------------|
| Staggered DID | Callaway & Sant'Anna (2021) | `csdid` | R `did::att_gt` |
| Staggered DID | Sun & Abraham (2021) | `eventstudyinteract` | R `fixest::sunab` |
| Staggered DID | Borusyak, Jaravel & Spiess (2024) | `did_imputation` | R `didimputation` |
| Staggered DID | Gardner (2022) two-stage | `did2s` | R `did2s` |
| Staggered DID | de Chaisemartin & D'Haultfoeuille | `did_multiplegt_dyn` | R `DIDmultiplegtDYN` |
| Bias diagnosis | Goodman-Bacon (2021) | `bacondecomp` | — |
| IV effective F | Montiel Olea & Pflueger (2013) | `weakivtest` | — |
| Weak-IV-robust | Anderson-Rubin / CLR | `weakiv` | — |
| RDD | Calonico-Cattaneo-Titiunik (2014) | `rdrobust` `rddensity` | R/Python same-name packages |
| DML | Chernozhukov et al. (2018) | `ddml` `pdslasso` | Python `DoubleML` |
| Few-cluster inference | Roodman et al. (2019) | `boottest` | — |
| Selection-bias bound | Oster (2019) | `psacalc` | — |

> Install uniformly with `ssc install <pkg>, replace`.

## Version-sensitive points (defer to latest official docs)

- **de Chaisemartin & D'Haultfoeuille:** `did_multiplegt_dyn` supersedes the older `did_multiplegt`. Use the `_dyn` command and confirm option names against current docs.
- **Weak-IV inference:** Stata 19 ships built-in weak-IV-robust inference; on Stata 18 and earlier this library uses the community-contributed `weakivtest` / `weakiv`. Prefer the built-in path where available.
- **Manipulation test:** `rddensity` (Cattaneo-Jansson-Ma) supersedes the older McCrary (2008) density test.
- **DID estimator choice:** report at least one heterogeneity-robust estimator (CS / SA / BJS / dCDH) as the main result rather than TWFE alone; package option names evolve, so verify against the latest documentation.
