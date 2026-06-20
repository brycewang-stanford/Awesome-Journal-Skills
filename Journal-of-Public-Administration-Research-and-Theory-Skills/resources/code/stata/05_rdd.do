*===============================================================================
* 05_rdd.do —— Regression discontinuity (Calonico-Cattaneo-Titiunik approach)
*
* Reporting discipline (identification):
*   (1) rdplot binned visualization, showing the jump at the cutoff
*   (2) rdrobust local linear + triangular kernel + MSE-optimal bandwidth
*       * Report the "Robust" row (bias-corrected point estimate and CI),
*         not only the conventional CI
*   (3) rddensity manipulation test (Cattaneo-Jansson-Ma, supersedes McCrary 2008)
*   (4) Robustness: covariate continuity, alternative bandwidths, donut RD,
*       placebo cutoffs
*
* Data assumptions: Y outcome; X running variable (centered so the cutoff c=0)
*===============================================================================
use "$clean/analysis.dta", clear
global Y   Y
global X   running_centered             // Running variable, = 0 at the cutoff
local  c = 0

*--- 1. Visualization: binned scatter + polynomial fit ------------------------
rdplot $Y $X, c(`c') p(1) kernel(triangular) ///
    graph_options(title("Outcome jump at the cutoff") xtitle("Running variable") ytitle("$Y"))
graph export "$figs/rdplot.png", replace width(2000)

*--- 2. Optimal bandwidth (MSE-optimal) --------------------------------------
rdbwselect $Y $X, c(`c') kernel(triangular) bwselect(mserd)

*--- 3. Main estimate: local linear + bias-corrected robust CI (report Robust row)
rdrobust $Y $X, c(`c') p(1) kernel(triangular) bwselect(mserd) vce(hc3)
* Report the "Robust" row's point estimate and robust CI (the core CCT 2014 contribution)

*--- 4. Manipulation test (density discontinuity; CJM supersedes McCrary) ------
rddensity $X, c(`c')
rdplotdensity (rddensity $X, c(`c')) $X
graph export "$figs/rddensity.png", replace width(2000)

*--- 5. Robustness -----------------------------------------------------------
* 5a. Covariate continuity (covariates should not jump at the cutoff)
foreach v in size lev roa {
    rdrobust `v' $X, c(`c') p(1) kernel(triangular)
}
* 5b. Multi-bandwidth sensitivity
foreach h in 3 5 7 {
    rdrobust $Y $X, c(`c') h(`h')
}
* 5c. Donut RD (drop observations near the cutoff to rule out precise manipulation)
rdrobust $Y $X if abs($X) > 0.5, c(`c')
* 5d. Placebo cutoffs (no effect should appear at non-true cutoffs)
rdrobust $Y $X, c(-3)
rdrobust $Y $X, c(3)

di as result "===== 05_rdd.do done; main result reports the Robust row + rddensity ====="
