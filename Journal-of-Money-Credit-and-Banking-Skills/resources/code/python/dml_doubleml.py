"""
dml_doubleml.py —— Double machine learning (DoubleML, Bach et al. 2022)

The counterpart of Stata 06_dml.do. Partially linear model (PLR):
Y = theta*D + g(X) + eps, D = m(X) + v. Reporting elements: model type,
cross-fitting folds K, nuisance-function learners, orthogonal-score standard
errors, and a learner-robustness comparison (Chernozhukov et al. 2018).
"""
from __future__ import annotations
import pandas as pd
from doubleml import DoubleMLData, DoubleMLPLR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LassoCV

df = pd.read_stata("data/clean/analysis.dta")
y_col = "Y"
d_col = "D"
x_cols = [c for c in df.columns if c.startswith(("size", "lev", "roa",
          "industry_", "area_"))]

dml_data = DoubleMLData(df, y_col=y_col, d_cols=d_col, x_cols=x_cols)

learners = {
    "lasso": (LassoCV(), LassoCV()),
    "rf": (RandomForestRegressor(n_estimators=500, min_samples_leaf=5),
           RandomForestRegressor(n_estimators=500, min_samples_leaf=5)),
    "gbm": (GradientBoostingRegressor(), GradientBoostingRegressor()),
}

# Estimate with each learner for a robustness comparison
for name, (ml_l, ml_m) in learners.items():
    plr = DoubleMLPLR(dml_data, ml_l=ml_l, ml_m=ml_m, n_folds=5, n_rep=5)
    plr.fit()
    print(f"[{name}] theta = {plr.coef[0]:.4f}  se = {plr.se[0]:.4f}  "
          f"95%CI = {plr.confint().values.round(4).tolist()}")
