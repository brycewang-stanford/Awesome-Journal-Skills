*===============================================================================
* 06_dml.do —— Double machine learning (Chernozhukov et al. 2018)
*
* Reporting discipline (identification): report (1) model type (partially linear
*   PLR / interactive) (2) cross-fitting folds K (commonly 5 or 10) (3) nuisance-
*   function learners (lasso / random forest / gradient boosting), ideally with a
*   learner-robustness comparison (4) Neyman orthogonal score standard errors.
*===============================================================================
use "$clean/analysis.dta", clear
global Y   Y
global D   D
global X   "size lev roa age group industry_* area_*"   // High-dimensional controls

*--- Route A: ddml + pystacked (ensemble learner, recommended) ----------------
* ssc install ddml, replace
* ssc install pystacked, replace      // requires local Python + scikit-learn
ddml init partial, kfolds(5) reps(5)
ddml E[Y|X]: pystacked $Y $X, type(reg) methods(ols lassocv rf gradboost)
ddml E[D|X]: pystacked $D $X, type(reg) methods(ols lassocv rf gradboost)
ddml crossfit
ddml estimate, robust

*--- Route B: high-dimensional lasso (Belloni-Chernozhukov-Hansen partial linear)
* ssc install pdslasso, replace
* pdslasso $Y $D ($X), robust

di as result "===== 06_dml.do done ====="
