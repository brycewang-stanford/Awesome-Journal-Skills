*===============================================================================
* 07_mechanism.do —— Mechanism test
*
* * Methodological point (mechanism):
*   - Avoid the mediation "stepwise" method (Baron-Kenny three-step) / Sobel test
*     / bootstrap indirect-effect share -- these are widely no longer accepted.
*   - The correct approach: estimate only D -> M (the mechanism variable M as the
*     dependent variable), using exactly the same identification strategy as the
*     main regression D -> Y; argue the M -> Y link with economic theory /
*     institutional background / prior literature, rather than "proving" it with
*     an endogenous regression.
*   - That is: a mechanism test = credibly identifying that "treatment did change
*     the mechanism variable M" + a theoretical argument that "M affects Y".
*===============================================================================
use "$clean/analysis.dta", clear
global D    treat
global X    "size lev roa age group"
* Mechanism variables (measured after treatment D and before outcome Y; their
* construction must not use future information)
global Ms   "mech1 mech2"

*--- D -> M: for each mechanism variable, reuse the main identification strategy
*    (staggered DID / TWFE example here)
eststo clear
foreach m of global Ms {
    eststo m_`m': reghdfe `m' $D $X, absorb(id year) vce(cluster id)
    * Reading: treatment significantly shifts mechanism variable M (the credibly identified causal link)
}
esttab m_* using "$tables/t_mechanism.rtf", replace ///
    b(3) se(3) star(* 0.1 ** 0.05 *** 0.01) ///
    keep($D) label title("Table X Mechanism test: effect of treatment on mechanism variables") ///
    addnotes("Note: cluster-robust standard errors (unit level) in parentheses. The M->Y logic is argued by theory and prior literature (see text).")

*--- Things NOT to do (kept as a reminder, do not enable) ---------------------
* Stepwise mediation / Sobel: sgmediation Y, mv(M) iv(D) cv($X)      // x not accepted
* Bootstrap indirect-effect share                                    // x not reported

di as result "===== 07_mechanism.do done; argue M->Y by theory, do not run an endogenous mediation regression ====="
