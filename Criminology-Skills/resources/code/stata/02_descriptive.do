*===============================================================================
* 02_descriptive.do —— Descriptive statistics, variable definitions,
*   (DID) treatment-group balance
*===============================================================================
use "$clean/analysis.dta", clear
global Y      Y
global X      "size lev roa age group"

*--- 1. Descriptive statistics table (mean/sd/quantiles/N); export as a table -
estpost summarize $Y treat $X, detail
esttab using "$tables/t1_sumstats.rtf", replace ///
    cells("count(fmt(0)) mean(fmt(3)) sd(fmt(3)) min(fmt(3)) p50(fmt(3)) max(fmt(3))") ///
    nonumber noobs label ///
    title("Table 1 Descriptive statistics") ///
    addnotes("Note: continuous variables winsorized at the 1st and 99th percentiles. Sources in the variable-definition table.")

*--- 2. Treatment vs control mean differences (pre-treatment, "quasi-random" evidence)
* Compare the two groups one period before treatment on observable characteristics
estpost ttest $X if year == treat_year - 1, by(treated_ever)
esttab using "$tables/t_balance.rtf", replace ///
    cells("mu_1(fmt(3)) mu_2(fmt(3)) b(star fmt(3)) se(fmt(3))") ///
    label title("Pre-treatment characteristics: treated vs control")

*--- 3. Correlation matrix (optional, for the appendix) ----------------------
* pwcorr $Y treat $X, star(0.05)

di as result "===== 02_descriptive.do done ====="
