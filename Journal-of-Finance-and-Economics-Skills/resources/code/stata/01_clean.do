*===============================================================================
* 01_clean.do —— 数据清洗（原始 → 分析样本）
*
* 原则（er-reproducibility）：原始数据只读不改；所有样本筛选、变量构造、缩尾
*   都在代码里留痕，可追溯。最终产出 data/clean/analysis.dta。
*===============================================================================

*--- 1. 读入原始数据，合并 ----------------------------------------------------
use "$raw/firm_financials.dta", clear          // 主表（如 CSMAR 财务）
merge m:1 stkcd year using "$raw/governance.dta", keep(master match) nogen
merge m:1 city  year using "$raw/policy.dta",     keep(master match) nogen
* 合并键务必明确（此处 stkcd×year / city×year）；记录每次 merge 的匹配率

*--- 2. 样本筛选（每一步留痕，便于在正文"数据"小节交代）---------------------
drop if industry == "金融业"                    // 剔除金融业
drop if regexm(stknm, "ST")                     // 剔除 ST / *ST
drop if mi(rd_invest) | mi(treat)               // 剔除关键变量缺失
* 形成非平衡 / 平衡面板；如需平衡：bys id: keep if _N == 期数

*--- 3. 变量构造（给出公式与来源注释，对应变量定义表）-----------------------
gen     size = ln(asset)                         // 企业规模 = ln(总资产)，来源 CSMAR
gen     lev  = debt / asset                      // 资产负债率
gen     roa  = ni / asset                        // 总资产收益率
label var size "企业规模(资产对数)"
label var lev  "资产负债率"
label var roa  "总资产收益率"

* 处理变量：首次受处理年份 gvar（交叠 DID 必备）
bys id (year): egen _first = min(cond(treat==1, year, .))
gen gvar = cond(mi(_first), 0, _first)           // 从不处理者 gvar = 0
drop _first

*--- 4. 缩尾（winsorize），缓解极端值；比例在稳健性中做敏感性 ----------------
winsor2 rd_invest size lev roa, cuts(1 99) replace

*--- 5. 保存分析样本 ----------------------------------------------------------
compress
label data "分析样本，由 01_clean.do 生成，请勿手动修改"
save "$clean/analysis.dta", replace
di as result "===== 01_clean.do 完成，N = " _N " ====="
