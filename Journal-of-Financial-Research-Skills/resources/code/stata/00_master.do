*===============================================================================
* 00_master.do —— 一键复现主控文件
*
* 用途：《经济研究》投稿实证项目的可复现骨架。从原始数据到正文每一张表 / 图，
*       全链路由本文件按顺序驱动，确保"干净环境下一键重跑即可复现"。
*
* 使用：把本目录放到项目根目录的 code/ 下，修改下方 global root 为你的项目根路径，
*       然后在 Stata 中 `do code/00_master.do` 即可。
*
* 配套技能：er-reproducibility（目录与复现规范）、er-identification、er-mechanism、
*          er-robustness、er-tables-figures。
*===============================================================================

clear all
set more off
version 17                          // 声明 Stata 版本，保证语法可复现；按实际版本修改
set seed 20260606                  // 固定随机种子（bootstrap / 安慰剂 / ML 全局可复现）

*--- 路径：唯一需要按机器修改的地方 ------------------------------------------
global root "/path/to/your/project"          // ← 改成你的项目根目录
global raw    "$root/data/raw"
global clean  "$root/data/clean"
global tables "$root/output/tables"
global figs   "$root/output/figures"
cap mkdir "$clean"
cap mkdir "$tables"
cap mkdir "$figs"

*--- 一次性安装依赖（首次运行取消注释；之后注释掉以加速）----------------------
* ssc install reghdfe, replace
* ssc install ftools, replace
* ssc install estout, replace          // esttab / estout 三线表
* ssc install csdid, replace           // Callaway & Sant'Anna (2021)
* ssc install drdid, replace
* ssc install did_imputation, replace  // Borusyak, Jaravel & Spiess (2024)
* ssc install did2s, replace           // Gardner (2022)
* ssc install eventstudyinteract, replace   // Sun & Abraham (2021)
* ssc install avar, replace
* ssc install did_multiplegt_dyn, replace   // de Chaisemartin & D'Haultfœuille
* ssc install bacondecomp, replace     // Goodman-Bacon (2021) 分解
* ssc install ivreg2, replace
* ssc install ranktest, replace
* ssc install weakivtest, replace      // Montiel Olea & Pflueger 有效 F
* ssc install weakiv, replace          // Anderson-Rubin 弱工具稳健推断
* ssc install rdrobust, replace        // Calonico-Cattaneo-Titiunik
* ssc install rddensity, replace
* ssc install lpdensity, replace
* ssc install boottest, replace        // 少聚类 wild cluster bootstrap
* ssc install winsor2, replace
* ssc install psacalc, replace         // Oster (2019) δ 边界

*--- 按顺序执行 ---------------------------------------------------------------
do "$root/code/01_clean.do"          // 数据清洗 → data/clean/analysis.dta
do "$root/code/02_descriptive.do"    // 描述性统计、变量定义表、平衡性
do "$root/code/03_did_modern.do"     // 基准 + 现代交叠 DID + 事件研究
do "$root/code/04_iv.do"             // 工具变量（如适用）
do "$root/code/05_rdd.do"            // 断点回归（如适用）
do "$root/code/06_dml.do"            // 双重机器学习（如适用）
do "$root/code/07_mechanism.do"      // 机制检验（D→M，江艇 2022 口径）
do "$root/code/08_robustness.do"     // 稳健性检验体系
do "$root/code/09_tables.do"         // 汇总导出正文表格

di as result "===== 全部脚本运行完毕，请核对 output/ 下的表与图 ====="
