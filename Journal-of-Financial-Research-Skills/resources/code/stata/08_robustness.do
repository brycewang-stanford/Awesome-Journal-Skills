*===============================================================================
* 08_robustness.do —— 稳健性检验体系（配套 er-robustness）
*   组织原则：按"回应何种识别威胁"分类，而非无脑罗列。
*===============================================================================
use "$clean/analysis.dta", clear
global Y   rd_invest
global D   treat
global X   "size lev roa age soe"

*--- A. 针对遗漏变量 / 内生性 -------------------------------------------------
* A1. 加更高维固定效应（行业×年份、省份×年份）
reghdfe $Y $D $X, absorb(id year industry#year province#year) vce(cluster id)
* A2. Oster (2019) δ 边界：观测变量选择问题严重时，评估不可观测选择
reghdfe $Y $D $X, absorb(id year) vce(cluster id)
* psacalc delta $D, mcontrol($X)        // δ>1 表示结论对不可观测较稳健

*--- B. 针对测量误差 / 变量定义 ----------------------------------------------
* B1. 替换被解释变量度量（如研发强度 ↔ 研发支出对数）
* B2. 替换核心解释变量度量

*--- C. 针对样本选择 ---------------------------------------------------------
* C1. 剔除直辖市 / 特殊样本
reghdfe $Y $D $X if !inlist(province,"北京","上海","天津","重庆"), absorb(id year) vce(cluster id)
* C2. PSM 后再估（匹配可比样本）
* C3. 不同时间窗

*--- D. 针对估计方法 / 标准误 ------------------------------------------------
* D1. 双向聚类
reghdfe $Y $D $X, absorb(id year) vce(cluster id year)
* D2. 少聚类（处理集中在少数簇 / 聚类数<~40）→ wild cluster bootstrap
reghdfe $Y $D $X, absorb(id year) cluster(id)
boottest $D, reps(9999) cluster(id) seed(20260606)
* D3. 缩尾比例敏感性（1/99 → 5/95 → 不缩尾）

*--- E. DID 专属稳健性 ------------------------------------------------------
* E1. 安慰剂——随机化处理时点/对象 500 次，看真实系数是否在分布尾部
cap drop placebo_b
tempname M
postfile `M' double b using "$clean/placebo.dta", replace
forvalues i = 1/500 {
    preserve
        bys id: gen _rt = .
        * 随机指派伪处理（示意：打乱 gvar）
        gen _u = runiform()
        sort _u
        * ... 构造 fake_treat ...
        qui reghdfe $Y fake_treat $X, absorb(id year) vce(cluster id)
        post `M' (_b[fake_treat])
    restore
}
postclose `M'
use "$clean/placebo.dta", clear
* 真实系数 b0 应落在安慰剂分布的极端尾部
* histogram b, xline(`=b0')
use "$clean/analysis.dta", clear
* E2. 异质性稳健估计量（见 03_did_modern.do 的 csdid / did_imputation）
* E3. 排除同期其他政策干扰（加同期政策虚拟变量）

di as result "===== 08_robustness.do 完成 ====="
