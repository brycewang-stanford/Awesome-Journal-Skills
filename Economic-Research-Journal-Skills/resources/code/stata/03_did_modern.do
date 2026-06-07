*===============================================================================
* 03_did_modern.do —— 基准 DID + 现代交叠 DID + 事件研究
*
* 投稿口径（er-identification）：
*   交叠（多时点）DID 不能只报 TWFE。标准流程为
*     (1) TWFE 基准（读者熟悉的起点）
*     (2) Goodman-Bacon (2021) 分解，展示"坏比较 / 负权重"问题
*     (3) 异质性稳健估计量做主结果（至少一种：CS / SA / dCDH / BJS）
*     (4) 事件研究图检验平行趋势与动态效应
*     (5) 安慰剂检验（见 08_robustness.do）
*
* 数据假设：面板，变量 id（个体）year（年份）treat（当期是否受处理 0/1）
*           gvar（首次受处理年份；从不受处理者设为 0 或 .，按各命令要求）
*           Y（结果）controls（控制变量列表）
*===============================================================================

use "$clean/analysis.dta", clear
global Y      rd_invest                       // ← 结果变量
global X      "size lev roa age soe"          // ← 控制变量
xtset id year

*-------------------------------------------------------------------------------
* (1) TWFE 基准——双向固定效应（读者熟悉的起点，但交叠下可能有偏）
*-------------------------------------------------------------------------------
eststo twfe: reghdfe $Y treat $X, absorb(id year) vce(cluster id)

*-------------------------------------------------------------------------------
* (2) Goodman-Bacon 分解——诊断 TWFE 偏误来源（仅诊断，非估计量）
*     仅适用于 staggered 且无协变量的简单设定；用于说明"坏比较"权重
*-------------------------------------------------------------------------------
preserve
    bacondecomp $Y treat, ddetail
    graph export "$figs/bacon_decomp.png", replace width(2000)
restore

*-------------------------------------------------------------------------------
* (3) 异质性稳健估计量——主结果（任选其一为主，其余作稳健性）
*-------------------------------------------------------------------------------

* --- 3a. Callaway & Sant'Anna (2021)：group-time ATT 再聚合 ---
* gvar = 首次受处理年份；从不受处理者 gvar = 0
csdid $Y $X, ivar(id) time(year) gvar(gvar) method(dripw)
estat simple                                   // 总体 ATT
estat event                                     // 动态效应（事件研究式）
csdid_plot, title("Callaway-Sant'Anna 动态效应")
graph export "$figs/es_csdid.png", replace width(2000)
eststo cs_att: estat simple

* --- 3b. Borusyak, Jaravel & Spiess (2024) 插补估计量（最有效率）---
* 顺序：Y groupid timeid first_treat（从不处理者 first_treat 设为缺失 .）
did_imputation $Y id year gvar, autosample minn(0)
eststo bjs_att

* --- 3c. Sun & Abraham (2021) 交互加权（IW）---
* 需先生成相对时间虚拟变量与 never-treated / last-treated 控制组
* gen rel = year - gvar  （gvar==0 的从不处理者 rel 设为很大的数或缺失）
* eventstudyinteract $Y g_*, cohort(gvar) control_cohort(nevertreat) ///
*     absorb(i.id i.year) vce(cluster id)

* --- 3d. de Chaisemartin & D'Haultfœuille：可处理非二值 / 可逆处理 ---
* did_multiplegt_dyn $Y id year treat, effects(5) placebo(3) cluster(id)

*-------------------------------------------------------------------------------
* (4) 事件研究图（TWFE 版，用于平行趋势可视化；动态主结果用 3a/3c）
*     注意：交叠设定下 TWFE 事件研究本身可能有偏，故同时给出 CS 版（见上）
*-------------------------------------------------------------------------------
cap drop rel
gen rel = year - gvar if gvar > 0
* 以处理前一期 (rel == -1) 为基准组，遗漏之
forvalues k = 5(-1)2 {
    gen lead`k' = rel == -`k'
}
gen lead1 = 0                                   // 基准期
forvalues k = 0/5 {
    gen lag`k' = rel == `k'
}
reghdfe $Y lead5 lead4 lead3 lead2 lag0 lag1 lag2 lag3 lag4 lag5 $X, ///
    absorb(id year) vce(cluster id)
* coefplot 画 95% CI、处理时点垂直虚线（见 09_tables.do 的绘图段）

* 平行趋势联合检验：处理前各 lead 系数联合为 0
test lead5 lead4 lead3 lead2

di as result "===== 03_did_modern.do 完成；主结果建议以 CS / BJS 报告 ====="
