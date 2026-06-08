*===============================================================================
* 00_master.do —— One-click reproduction master file
*
* Purpose: A reproducible skeleton for an empirical project. From raw data to
*          every table / figure in the paper, the entire chain is driven in
*          order by this file, ensuring "a single clean-environment re-run
*          reproduces everything".
*
* Usage: Place this directory under code/ in your project root, change the
*        global root below to your project root path, then run
*        `do code/00_master.do` in Stata.
*===============================================================================

clear all
set more off
version 17                          // Declare Stata version for reproducible syntax; edit to match yours
set seed 20260606                  // Fix the random seed (bootstrap / placebo / ML globally reproducible)

*--- Paths: the only place that must be edited per machine ---------------------
global root "/path/to/your/project"          // <- change to your project root
global raw    "$root/data/raw"
global clean  "$root/data/clean"
global tables "$root/output/tables"
global figs   "$root/output/figures"
cap mkdir "$clean"
cap mkdir "$tables"
cap mkdir "$figs"

*--- One-time dependency install (uncomment on first run; re-comment to speed up)
* ssc install reghdfe, replace
* ssc install ftools, replace
* ssc install estout, replace          // esttab / estout publication tables
* ssc install csdid, replace           // Callaway & Sant'Anna (2021)
* ssc install drdid, replace
* ssc install did_imputation, replace  // Borusyak, Jaravel & Spiess (2024)
* ssc install did2s, replace           // Gardner (2022)
* ssc install eventstudyinteract, replace   // Sun & Abraham (2021)
* ssc install avar, replace
* ssc install did_multiplegt_dyn, replace   // de Chaisemartin & D'Haultfoeuille
* ssc install bacondecomp, replace     // Goodman-Bacon (2021) decomposition
* ssc install ivreg2, replace
* ssc install ranktest, replace
* ssc install weakivtest, replace      // Montiel Olea & Pflueger effective F
* ssc install weakiv, replace          // Anderson-Rubin weak-IV-robust inference
* ssc install rdrobust, replace        // Calonico-Cattaneo-Titiunik
* ssc install rddensity, replace
* ssc install lpdensity, replace
* ssc install boottest, replace        // few-cluster wild cluster bootstrap
* ssc install winsor2, replace
* ssc install psacalc, replace         // Oster (2019) delta bound

*--- Run in order -------------------------------------------------------------
do "$root/code/01_clean.do"          // Data cleaning -> data/clean/analysis.dta
do "$root/code/02_descriptive.do"    // Descriptive statistics, variable definitions, balance
do "$root/code/03_did_modern.do"     // Baseline + modern staggered DID + event study
do "$root/code/04_iv.do"             // Instrumental variables (if applicable)
do "$root/code/05_rdd.do"            // Regression discontinuity (if applicable)
do "$root/code/06_dml.do"            // Double machine learning (if applicable)
do "$root/code/07_mechanism.do"      // Mechanism test (D -> M)
do "$root/code/08_robustness.do"     // Robustness check system
do "$root/code/09_tables.do"         // Export final tables / figures

di as result "===== All scripts finished; please review tables and figures under output/ ====="
