*===============================================================================
* 05_rdd.do —— 断点回归（Calonico-Cattaneo-Titiunik 现代做法）
*
* 投稿口径（er-identification）：
*   (1) rdplot 分箱可视化，展示断点处跳跃
*   (2) rdrobust 局部线性 + 三角核 + MSE 最优带宽
*       ★ 报告 "Robust" 行（稳健偏差校正点估计与 CI），不要只报常规 CI
*   (3) rddensity 操纵检验（Cattaneo-Jansson-Ma，已取代 McCrary 2008）
*   (4) 稳健性：协变量连续性、不同带宽、donut RD、安慰剂断点
*
* 范文对标（确属《经济研究》）：刘生龙、周绍杰、胡鞍钢《义务教育法与中国城镇
*   教育回报：基于断点回归设计》，《经济研究》2016 年第 2 期。
*
* 数据假设：Y 结果；X 驱动变量（running variable，已中心化使断点 c=0）
*===============================================================================
use "$clean/analysis.dta", clear
global Y   wage_ln
global X   birthyear_centered           // 驱动变量，断点处 = 0
local  c = 0

*--- 1. 可视化：分箱散点 + 多项式拟合 ----------------------------------------
rdplot $Y $X, c(`c') p(1) kernel(triangular) ///
    graph_options(title("断点处结果跳跃") xtitle("驱动变量") ytitle("$Y"))
graph export "$figs/rdplot.png", replace width(2000)

*--- 2. 最优带宽（MSE-optimal）---------------------------------------------
rdbwselect $Y $X, c(`c') kernel(triangular) bwselect(mserd)

*--- 3. 主估计：局部线性 + 稳健偏差校正 CI（核心，报告 Robust 行）----------
rdrobust $Y $X, c(`c') p(1) kernel(triangular) bwselect(mserd) vce(hc3)
* 报告中用 "Robust" 行的点估计与稳健 CI（CCT 2014 的核心贡献）

*--- 4. 操纵检验（密度断点；CJM 已取代 McCrary）----------------------------
rddensity $X, c(`c')
rdplotdensity (rddensity $X, c(`c')) $X
graph export "$figs/rddensity.png", replace width(2000)

*--- 5. 稳健性 ---------------------------------------------------------------
* 5a. 协变量连续性（断点处协变量不应跳跃）
foreach v in size lev roa {
    rdrobust `v' $X, c(`c') p(1) kernel(triangular)
}
* 5b. 多带宽敏感性
foreach h in 3 5 7 {
    rdrobust $Y $X, c(`c') h(`h')
}
* 5c. donut RD（剔除断点附近样本，排除精确操纵）
rdrobust $Y $X if abs($X) > 0.5, c(`c')
* 5d. 安慰剂断点（在非真实断点处不应有效应）
rdrobust $Y $X, c(-3)
rdrobust $Y $X, c(3)

di as result "===== 05_rdd.do 完成；主结果报告 Robust 行 + rddensity ====="
