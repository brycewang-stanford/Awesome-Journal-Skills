*===============================================================================
* 09_tables.do —— Export final tables and event-study figures
*   Conventions: three-line tables, no vertical rules, <= 6 columns (rule of
*   thumb; defer to the target venue), cluster-robust SE in parentheses below
*   coefficients, notes stating the clustering level and significance definitions.
*===============================================================================
use "$clean/analysis.dta", clear
global Y   Y
global D   treat
global X   "size lev roa age group"

*--- Baseline regression table (add controls / fixed effects column by column) -
eststo clear
eststo c1: reghdfe $Y $D,            absorb(id year) vce(cluster id)
eststo c2: reghdfe $Y $D $X,         absorb(id year) vce(cluster id)
eststo c3: reghdfe $Y $D $X,         absorb(id year industry#year) vce(cluster id)

esttab c1 c2 c3 using "$tables/t2_baseline.rtf", replace ///
    b(3) se(3) star(* 0.1 ** 0.05 *** 0.01) ///
    keep($D $X) label ///
    stats(N r2_a, fmt(0 3) labels("Observations" "Adjusted R2")) ///
    mgroups("Dependent variable: Y", pattern(1 0 0)) ///
    indicate("Controls=$X" "Unit FE=*id*" "Year FE=*year*") ///
    title("Table 2 Baseline regression results") ///
    addnotes("Note: cluster-robust standard errors (unit level) in parentheses; *** ** * denote 1%, 5%, 10% significance.")

*--- Event-study figure (coefplot; period before treatment as base, 95% CI,
*    vertical dashed line at the treatment point) ----------------------------
* Immediately after the event-study regression in 03_did_modern.do:
* coefplot, keep(lead* lag*) vertical yline(0) xline(...) ///
*     ciopts(recast(rcap)) levels(95) ///
*     xtitle("Years relative to treatment") ytitle("Treatment effect") ///
*     title("Figure X Parallel trends and dynamic effects")
* graph export "$figs/event_study.png", replace width(2400)

di as result "===== 09_tables.do done; tables/figures exported to output/ ====="
