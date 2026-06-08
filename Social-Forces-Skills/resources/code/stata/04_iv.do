*===============================================================================
* 04_iv.do —— Instrumental variables (modern weak-IV diagnostics and robust
*   inference)
*
* Reporting discipline (identification):
*   Do not report only "F>10". The standard reporting elements are
*     (1) First-stage Kleibergen-Paap rk Wald F (valid under heteroskedasticity
*         / clustering)
*     (2) Compare against Stock-Yogo critical values
*     (3) Effective F (Montiel Olea & Pflueger 2013), more robust with a single
*         endogenous regressor
*     (4) Weak-IV-robust inference: Anderson-Rubin test and confidence interval
*     (5) Overidentification: Hansen J; exclusion needs theory + institutional
*         argument + placebo
*===============================================================================
use "$clean/analysis.dta", clear
global Y   Y
global D   D                        // Endogenous regressor
global Z   "z1 z2"                  // Instruments
global X   "size lev roa"          // Exogenous controls

*--- 1. Main estimate: ivreg2 auto-reports KP rk Wald F, Hansen J, endogeneity test
ivreg2 $Y $X (${D} = $Z), robust first
* The first option prints the first stage; look at "Kleibergen-Paap rk Wald F statistic"
* and compare with Stock-Yogo critical values (printed in ivreg2 output)

*--- 2. Effective F test (Montiel Olea-Pflueger, robust to heterosk./autocorr.) -
* Requires a single endogenous regressor; run immediately after ivreg2
weakivtest

*--- 3. Weak-IV-robust inference: Anderson-Rubin / CLR / K test and CI ---------
* Under exact identification AR is fully robust to weak instruments; under
* overidentification consult CLR
weakiv ivreg2 $Y $X (${D} = $Z), robust

*--- 4. Reduced form (reviewers often request it) -----------------------------
reghdfe $Y $Z $X, absorb(id year) vce(cluster id)

*--- 5. Lewbel (2012) heteroskedasticity-based instrument (supplementary check)
* ssc install ivreg2h, replace
* ivreg2h $Y $X (${D} = $Z), robust

di as result "===== 04_iv.do done; report KP F + effective F + AR interval ====="
