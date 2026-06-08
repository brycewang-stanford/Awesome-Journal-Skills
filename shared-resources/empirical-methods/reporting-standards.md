# Reporting Standards (modern empirical inference)

Venue-neutral reference for the inference and reporting choices that top empirical
journals now treat as table stakes. Pairs with `reviewer-objection-checklist.md`
(what referees attack) and `code/` (runnable templates). Commands are Stata-first
with R/Python equivalents; defer to each package's latest official docs for
version-sensitive options.

---

## 1. Standard errors — match the variance to the dependence

| Situation | What to do | Stata | R / Python |
|---|---|---|---|
| Within-group correlation | Cluster-robust SE at assignment level | `reghdfe y x, vce(cluster id)` | `fixest::feols(..., cluster=~id)` |
| Two dimensions of correlation | Two-way clustering | `vce(cluster firm year)` | `feols(..., cluster=~firm+year)` |
| Few clusters (< ~40) | Wild cluster bootstrap | `boottest` after regression | `fwildclusterboot` / `wildboottestjlr` |
| Spatial correlation | Conley spatial HAC | `acreg`, `ols_spatial_HAC` | `conleyreg` (R) |
| Serial correlation, long panels | Driscoll-Kraay or cluster-by-unit | `xtscc` | `feols(..., vcov="DK")` |

**Rules of thumb**
- Cluster at the level at which treatment is *assigned*, not the level at which
  data are *observed* (e.g. policy at the state level → cluster by state, even with
  firm-year data).
- Reporting more conservative SE (e.g. one level up) is usually safe; reporting
  *less* conservative invites the objection.
- With few clusters, the wild bootstrap p-value — not the asymptotic one — is the
  number to report.

---

## 2. Weak-instrument diagnostics (IV)

Report all four; "first-stage F > 10" alone is no longer sufficient:

1. **Kleibergen-Paap rk Wald F** — valid under heteroskedasticity/clustering
   (replaces Cragg-Donald under non-i.i.d. errors). `ivreg2 ... , robust first`.
2. **Stock-Yogo** critical values for the maximal bias/size you tolerate.
3. **Effective F** (Montiel Olea & Pflueger 2013) for a single endogenous
   regressor: `weakivtest`.
4. **Weak-IV-robust inference**: Anderson-Rubin (and CLR/K) confidence sets —
   `weakiv`. Under just-identification AR is fully robust to weak instruments.

Always also **report the reduced form**.

---

## 3. Multiple hypothesis testing

When the paper reports many outcomes, subgroups, or specifications, unadjusted
p-values overstate significance. Choose by goal:

| Goal | Method | Tool |
|---|---|---|
| Control family-wise error across few tests | Romano-Wolf stepdown | `rwolf` / `rwolf2` |
| Many tests, control false-discovery rate | Sharpened FDR q-values (Benjamini-Hochberg / Anderson 2008) | `wyoung`, BH in any stack |
| Pre-registered primary vs secondary | Hierarchy + correction within the secondary family | — |

Report both the unadjusted and adjusted values; do not silently drop either.

---

## 4. DiD / event-study reporting

- Reference period **t−1** (omitted); plot **95% CIs**; mark the treatment time.
- **Joint test** that pre-period coefficients = 0 (don't eyeball the figure).
- Pre-trends **power / honest-DiD sensitivity** (Roth 2022; Rambachan & Roth 2023):
  report the magnitude of pre-trend the design could *not* have detected.
- Main estimate from a **heterogeneity-robust** estimator; TWFE shown as benchmark.

---

## 5. RDD reporting

- **Robust bias-corrected CI** (Calonico-Cattaneo-Titiunik 2014) as the headline;
  conventional CI may accompany it but not replace it.
- **MSE-optimal bandwidth** (`bwselect(mserd)`), plus a bandwidth-sensitivity panel.
- **Manipulation test** via `rddensity` (Cattaneo-Jansson-Ma), not McCrary 2008.
- Covariate-continuity / placebo-outcome checks; donut and placebo-cutoff panels.

---

## 6. Tables and figures

- **Three-line (booktabs) tables**; no vertical rules; align decimals.
- Report **coefficient, SE (in parentheses), N, and the relevant fit/first-stage
  statistic**; stars defined in the note; never stars without the SE.
- **Effect sizes in interpretable units** (e.g. "a 1-SD increase in X raises Y by
  β units = z% of the mean"), not just significance.
- Figures: show **uncertainty** (CIs/bands); label axes in real units; make them
  legible in grayscale.
- One canonical exporter: `esttab`/`estout` (Stata), `modelsummary` (R),
  `stargazer`/`pandas` (Python) — keep formatting reproducible from code.

---

## 7. Reproducibility (what data editors now check)

- One-click master script (`00_master`/`run_all`) reproduces every number from raw
  data; fixed random seeds; pinned package versions / install script.
- Read-only raw data; a documented raw→clean pipeline with sample-selection counts
  ("started with N, dropped X for reason, final N").
- A `README` mapping each table/figure to the script that produces it.
- Honest data-availability statement; if data are restricted, provide the code and
  a synthetic/sample dataset so the pipeline runs.

---

## 8. Quick pre-submission inference audit

- [ ] SE clustered at assignment level; few-cluster bootstrap if needed
- [ ] IV: KP rk F + effective F + AR robust CI + reduced form
- [ ] DiD: heterogeneity-robust main + event study + honest-DiD sensitivity
- [ ] RDD: robust bias-corrected CI + rddensity + bandwidth sensitivity
- [ ] Multiple testing corrected when many outcomes/subgroups reported
- [ ] Effect sizes interpreted in real units; magnitudes benchmarked
- [ ] One-click reproduction from raw data with seeds + version pinning

---

*Provenance: modern applied-econometrics reporting practice; commands cross-checked
against the verified chains in `code/`. Pair with each journal's
`official-source-map.md` for venue-specific limits (word counts, data-policy,
house citation style).*
