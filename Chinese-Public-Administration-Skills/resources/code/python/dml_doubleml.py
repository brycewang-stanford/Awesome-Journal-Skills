"""
dml_doubleml.py —— 双重机器学习（DoubleML，Bach et al. 2022）

对应 Stata 06_dml.do。偏线性模型 (PLR)：Y = θ·D + g(X) + ε，D = m(X) + v。
报告要素：模型类型、交叉拟合折数 K、干扰函数学习器、正交得分标准误，并对
不同学习器做稳健性对比（Chernozhukov et al. 2018）。
"""
from __future__ import annotations
import pandas as pd
from doubleml import DoubleMLData, DoubleMLPLR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LassoCV

df = pd.read_stata("data/clean/analysis.dta")
y_col = "rd_invest"
d_col = "digital"
x_cols = [c for c in df.columns if c.startswith(("size", "lev", "roa",
          "industry_", "province_"))]

dml_data = DoubleMLData(df, y_col=y_col, d_cols=d_col, x_cols=x_cols)

learners = {
    "lasso": (LassoCV(), LassoCV()),
    "rf": (RandomForestRegressor(n_estimators=500, min_samples_leaf=5),
           RandomForestRegressor(n_estimators=500, min_samples_leaf=5)),
    "gbm": (GradientBoostingRegressor(), GradientBoostingRegressor()),
}

# 对每种学习器估计，做稳健性对比
for name, (ml_l, ml_m) in learners.items():
    plr = DoubleMLPLR(dml_data, ml_l=ml_l, ml_m=ml_m, n_folds=5, n_rep=5)
    plr.fit()
    print(f"[{name}] theta = {plr.coef[0]:.4f}  se = {plr.se[0]:.4f}  "
          f"95%CI = {plr.confint().values.round(4).tolist()}")
