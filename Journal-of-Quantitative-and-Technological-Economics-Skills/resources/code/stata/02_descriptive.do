*===============================================================================
* 02_descriptive.do —— 描述性统计、变量定义表、（DID 处理组）平衡性
*   配套技能：er-tables-figures、er-data-sample
*===============================================================================
use "$clean/analysis.dta", clear
global Y      rd_invest
global X      "size lev roa age soe"

*--- 1. 描述性统计表（均值/标准差/分位数/N）；导出为三线表 -------------------
estpost summarize $Y treat $X, detail
esttab using "$tables/t1_sumstats.rtf", replace ///
    cells("count(fmt(0)) mean(fmt(3)) sd(fmt(3)) min(fmt(3)) p50(fmt(3)) max(fmt(3))") ///
    nonumber noobs label ///
    title("表1 描述性统计") ///
    addnotes("注：连续变量已在 1% 与 99% 分位缩尾。数据来源见变量定义表。")

*--- 2. 处理组 vs 控制组的均值差异（DID 设计的"准随机"佐证）------------------
* 处理前一期比较，展示两组在可观测特征上是否系统差异
estpost ttest $X if year == treat_year - 1, by(treated_ever)
esttab using "$tables/t_balance.rtf", replace ///
    cells("mu_1(fmt(3)) mu_2(fmt(3)) b(star fmt(3)) se(fmt(3))") ///
    label title("处理组与控制组处理前特征比较")

*--- 3. 相关系数矩阵（可选，放附录）-----------------------------------------
* pwcorr $Y treat $X, star(0.05)

di as result "===== 02_descriptive.do 完成 ====="
