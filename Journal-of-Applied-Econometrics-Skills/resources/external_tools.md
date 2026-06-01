# External Tools & Resources for JAE-Style Applied Econometrics

Software, packages, and archives useful when preparing a *Journal of Applied
Econometrics* (JAE) submission — empirical, **replicable** economics that applies and
develops econometric techniques on real data, with a mandatory deposit to the JAE Data
Archive. The unifying constraint here is **reproducibility**: everything you report must
be regeneratable from plain-text data and code. Check licenses and current access terms
before use.

## 1. The JAE Data Archive (mandatory for accepted papers)

| Resource | Where | Use |
|----------|-------|-----|
| JAE Data Archive (current host) | ZBW Journal Data Archive — journaldata.zbw.eu | Deposit non-confidential data + programs on acceptance |
| JAE Data Archive (legacy host) | Queen's University — qed.econ.queensu.ca/jae/ | Historical archive (1994–2022); author instructions |
| re3data registry entry | re3data.org/repository/r3d100010130 | Archive metadata; ~1,487 datasets to mine for replication targets |

Archive format rules: every dataset needs a **plain-text ASCII readme**; data should be
**plain ASCII / CSV** text — proprietary binary formats (Stata `.dta`, SAS datasets) are
**not** acceptable on their own; ship the **programs** that regenerate every result.

## 2. Statistical software and reproducibility tooling

### Stata
- Time-series / macro-econometrics common at JAE: `var`, `vec`, `arima`/`arch`, `dfgls`, `forecast`, local-projection IRFs (`lpirf`)
- Panel: `xtreg`, `xtabond2` (Arellano–Bond/Blundell–Bond GMM), `reghdfe` (high-dimensional FE)
- Robust / HAC inference: `newey`, cluster-robust `vce()`, `boottest` (wild bootstrap)
- Export to archive-friendly text: `outsheet`/`export delimited` to CSV; never deposit `.dta` alone
- Reproducibility: `version` statement at top of every do-file; a master `run_all.do`

### R
- Time series & forecasting: `forecast`, `vars`, `urca` (unit roots/cointegration), `sandwich` + `lmtest` (HAC/robust SEs), `dynlm`
- Panel & GMM: `plm`, `gmm`, `fixest` (fast high-dimensional FE, fast clustered SEs)
- Reproducibility: `renv` (pinned package versions), `sessionInfo()` logged, `here` for paths
- Output: write results to `.csv`/`.txt`; build tables with `modelsummary` exporting to LaTeX

### Python
- Econometrics: `statsmodels`, `linearmodels` (panel IV, GMM, system estimators), `arch` (volatility/bootstrap)
- Reproducibility: pinned `requirements.txt`/`environment.yml`, fixed random seeds, `pandas` → CSV

## 3. Replication-and-discipline aids

| Tool | Use |
|------|-----|
| Make / Snakemake / a master script | One command regenerates every table and figure from raw data |
| Git (no large binaries) | Track code; keep the deposited package text-first |
| `cba`/AEA-style replication checklists | Self-audit before deposit (JAE has its own Replication Article category) |
| Code Ocean / Docker (optional) | Capsule the full environment for a one-click rerun |

## 4. Numerical-method / Monte Carlo support (for method-development papers)

- Monte Carlo design: report DGP, sample sizes, replication count, and seeds; ship the simulation script.
- Bootstrap/resampling: `boottest` (Stata), `boot` (R), `arch.bootstrap` (Python).
- Document any tuning constants so a referee can reproduce simulation tables exactly.

> JAE is **citation-style agnostic** and accepts **Free Format** first submissions — so
> tooling choices are yours, but the deposited code/data must satisfy the archive's
> plain-text rules. Re-confirm archive instructions at the source before depositing.
