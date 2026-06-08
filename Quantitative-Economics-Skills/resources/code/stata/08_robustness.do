*===============================================================================
* 08_robustness.do —— Robustness check system (companion to robustness guidance)
*   Organizing principle: classify by "which identification threat it answers",
*   not a mindless list.
*===============================================================================
use "$clean/analysis.dta", clear
global Y   Y
global D   treat
global X   "size lev roa age group"

*--- A. Against omitted variables / endogeneity ------------------------------
* A1. Add higher-dimensional fixed effects (industry x year, area x year)
reghdfe $Y $D $X, absorb(id year industry#year area#year) vce(cluster id)
* A2. Oster (2019) delta bound: when selection on observables is severe, assess
*     selection on unobservables
reghdfe $Y $D $X, absorb(id year) vce(cluster id)
* psacalc delta $D, mcontrol($X)        // delta>1 means the result is robust to unobservables

*--- B. Against measurement error / variable definition ----------------------
* B1. Replace the outcome measure (e.g., intensity <-> log level)
* B2. Replace the core regressor measure

*--- C. Against sample selection ---------------------------------------------
* C1. Drop special subsamples
reghdfe $Y $D $X if special_flag == 0, absorb(id year) vce(cluster id)
* C2. Re-estimate after PSM (comparable matched sample)
* C3. Alternative time windows

*--- D. Against estimation method / standard errors --------------------------
* D1. Two-way clustering
reghdfe $Y $D $X, absorb(id year) vce(cluster id year)
* D2. Few clusters (treatment concentrated in few clusters / #clusters < ~40) -> wild cluster bootstrap
reghdfe $Y $D $X, absorb(id year) cluster(id)
boottest $D, reps(9999) cluster(id) seed(20260606)
* D3. Winsorization-share sensitivity (1/99 -> 5/95 -> none)

*--- E. DID-specific robustness ----------------------------------------------
* E1. Placebo -- randomize the treatment timing/units 500 times, check whether
*     the real coefficient lies in the tail of the distribution
cap drop placebo_b
tempname M
postfile `M' double b using "$clean/placebo.dta", replace
forvalues i = 1/500 {
    preserve
        bys id: gen _rt = .
        * Randomly assign a fake treatment (illustrative: shuffle gvar)
        gen _u = runiform()
        sort _u
        * ... construct fake_treat ...
        qui reghdfe $Y fake_treat $X, absorb(id year) vce(cluster id)
        post `M' (_b[fake_treat])
    restore
}
postclose `M'
use "$clean/placebo.dta", clear
* The real coefficient b0 should fall in the extreme tail of the placebo distribution
* histogram b, xline(`=b0')
use "$clean/analysis.dta", clear
* E2. Heterogeneity-robust estimators (see csdid / did_imputation in 03_did_modern.do)
* E3. Rule out concurrent policy interference (add a concurrent-policy dummy)

di as result "===== 08_robustness.do done ====="
