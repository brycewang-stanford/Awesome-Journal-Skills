*===============================================================================
* 03_did_modern.do —— Baseline DID + modern staggered DID + event study
*
* Reporting discipline (identification):
*   Staggered (multi-period) DID must NOT report only TWFE. The standard chain is
*     (1) TWFE baseline (a familiar starting point for readers)
*     (2) Goodman-Bacon (2021) decomposition, exposing "bad comparisons /
*         negative weights"
*     (3) A heterogeneity-robust estimator as the main result (at least one of:
*         CS / SA / dCDH / BJS)
*     (4) Event-study plot to check parallel trends and dynamic effects
*     (5) Placebo tests (see 08_robustness.do)
*
* Data assumptions: panel with variables id (unit), year, treat (currently
*   treated 0/1), gvar (first treated period; never-treated set to 0 or .,
*   per each command's requirement), Y (outcome), controls (control list).
*===============================================================================

use "$clean/analysis.dta", clear
global Y      Y                               // <- outcome variable
global X      "size lev roa age group"        // <- control variables
xtset id year

*-------------------------------------------------------------------------------
* (1) TWFE baseline -- two-way fixed effects (familiar start, but may be biased
*     under staggered adoption)
*-------------------------------------------------------------------------------
eststo twfe: reghdfe $Y treat $X, absorb(id year) vce(cluster id)

*-------------------------------------------------------------------------------
* (2) Goodman-Bacon decomposition -- diagnose the source of TWFE bias
*     (diagnostic only, not an estimator). Applies to staggered designs with no
*     covariates; used to expose "bad comparison" weights.
*-------------------------------------------------------------------------------
preserve
    bacondecomp $Y treat, ddetail
    graph export "$figs/bacon_decomp.png", replace width(2000)
restore

*-------------------------------------------------------------------------------
* (3) Heterogeneity-robust estimators -- main result (pick one as primary, the
*     rest as robustness)
*-------------------------------------------------------------------------------

* --- 3a. Callaway & Sant'Anna (2021): group-time ATT, then aggregate ---
* gvar = first treated period; never-treated units gvar = 0
csdid $Y $X, ivar(id) time(year) gvar(gvar) method(dripw)
estat simple                                   // overall ATT
estat event                                     // dynamic effects (event-study style)
csdid_plot, title("Callaway-Sant'Anna dynamic effects")
graph export "$figs/es_csdid.png", replace width(2000)
eststo cs_att: estat simple

* --- 3b. Borusyak, Jaravel & Spiess (2024) imputation estimator (most efficient) ---
* Order: Y groupid timeid first_treat (never-treated first_treat set to missing .)
did_imputation $Y id year gvar, autosample minn(0)
eststo bjs_att

* --- 3c. Sun & Abraham (2021) interaction-weighted (IW) estimator ---
* Requires relative-time dummies and a never-treated / last-treated control group
* gen rel = year - gvar  (for never-treated, gvar==0, set rel to a large value or missing)
* eventstudyinteract $Y g_*, cohort(gvar) control_cohort(nevertreat) ///
*     absorb(i.id i.year) vce(cluster id)

* --- 3d. de Chaisemartin & D'Haultfoeuille: non-binary / reversible treatment ---
* did_multiplegt_dyn $Y id year treat, effects(5) placebo(3) cluster(id)

*-------------------------------------------------------------------------------
* (4) Event-study plot (TWFE version, for parallel-trends visualization;
*     dynamic main result uses 3a/3c)
*     Note: under staggered adoption the TWFE event study itself may be biased,
*     so the CS version is provided alongside (above).
*-------------------------------------------------------------------------------
cap drop rel
gen rel = year - gvar if gvar > 0
* Use the period just before treatment (rel == -1) as the omitted base group
forvalues k = 5(-1)2 {
    gen lead`k' = rel == -`k'
}
gen lead1 = 0                                   // base period
forvalues k = 0/5 {
    gen lag`k' = rel == `k'
}
reghdfe $Y lead5 lead4 lead3 lead2 lag0 lag1 lag2 lag3 lag4 lag5 $X, ///
    absorb(id year) vce(cluster id)
* coefplot draws 95% CI and a vertical dashed line at the treatment point (see 09_tables.do)

* Parallel-trends joint test: pre-treatment lead coefficients jointly zero
test lead5 lead4 lead3 lead2

di as result "===== 03_did_modern.do done; report the main result with CS / BJS ====="
