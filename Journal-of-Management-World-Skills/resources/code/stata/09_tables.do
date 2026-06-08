*===============================================================================
* 09_tables.do —— 导出正文三线表与事件研究图（配套 er-tables-figures）
*   规范：三线表、无竖线、≤6 列（经验值，以投稿当期官网为准）、系数下方括号内
*   为聚类稳健标准误、注释含聚类层次与显著性定义。
*===============================================================================
use "$clean/analysis.dta", clear
global Y   rd_invest
global D   treat
global X   "size lev roa age soe"

*--- 基准回归表（逐列加控制 / 固定效应）-------------------------------------
eststo clear
eststo c1: reghdfe $Y $D,            absorb(id year) vce(cluster id)
eststo c2: reghdfe $Y $D $X,         absorb(id year) vce(cluster id)
eststo c3: reghdfe $Y $D $X,         absorb(id year industry#year) vce(cluster id)

esttab c1 c2 c3 using "$tables/t2_baseline.rtf", replace ///
    b(3) se(3) star(* 0.1 ** 0.05 *** 0.01) ///
    keep($D $X) label ///
    stats(N r2_a, fmt(0 3) labels("观测值" "调整 R²")) ///
    mgroups("被解释变量：研发投入", pattern(1 0 0)) ///
    indicate("控制变量=$X" "个体固定效应=*id*" "年份固定效应=*year*") ///
    title("表2 基准回归结果") ///
    addnotes("注：括号内为企业层面聚类稳健标准误；*** ** * 分别表示 1%、5%、10% 显著。")

*--- 事件研究图（coefplot；处理前一期为基准，95% CI，处理时点垂直虚线）-----
* 紧接 03_did_modern.do 的事件研究回归之后：
* coefplot, keep(lead* lag*) vertical yline(0) xline(...) ///
*     ciopts(recast(rcap)) levels(95) ///
*     xtitle("相对处理时点的年份") ytitle("处理效应") ///
*     title("图X 平行趋势与动态效应")
* graph export "$figs/event_study.png", replace width(2400)

di as result "===== 09_tables.do 完成；表/图已导出至 output/ ====="
