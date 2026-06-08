*===============================================================================
* 06_dml.do —— 双重机器学习（Chernozhukov et al. 2018）
*
* 投稿口径（er-identification）：报告 (1) 模型类型（偏线性 PLR / 交互式）
*   (2) 交叉拟合折数 K（常用 5 或 10）(3) 干扰函数学习器（lasso / 随机森林 /
*   梯度提升），最好做学习器稳健性对比 (4) Neyman 正交得分标准误。
*===============================================================================
use "$clean/analysis.dta", clear
global Y   rd_invest
global D   digital
global X   "size lev roa age soe industry_* province_*"   // 高维控制

*--- 路线 A：ddml + pystacked（集成学习器，推荐）----------------------------
* ssc install ddml, replace
* ssc install pystacked, replace      // 需本机 Python + scikit-learn
ddml init partial, kfolds(5) reps(5)
ddml E[Y|X]: pystacked $Y $X, type(reg) methods(ols lassocv rf gradboost)
ddml E[D|X]: pystacked $D $X, type(reg) methods(ols lassocv rf gradboost)
ddml crossfit
ddml estimate, robust

*--- 路线 B：高维 lasso（Belloni-Chernozhukov-Hansen 部分线性）-------------
* ssc install pdslasso, replace
* pdslasso $Y $D ($X), robust

di as result "===== 06_dml.do 完成 ====="
