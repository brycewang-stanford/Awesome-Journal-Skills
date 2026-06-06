*===============================================================================
* 07_mechanism.do —— 机制检验（江艇 2022 口径）
*
* ★ 方法论要点（er-mechanism / 江艇 2022《因果推断经验研究中的中介效应与
*   调节效应》,《中国工业经济》2022 年第 5 期）：
*   - 不再使用中介效应"逐步法"（Baron-Kenny 三步法）/ Sobel 检验 /
*     Bootstrap 间接效应占比 —— 四大刊已普遍不接受。
*   - 正确做法：只估计 D → M（机制变量 M 作为被解释变量），沿用与主回归
*     D → Y 完全相同的识别策略；M → Y 这一环用经济学理论 / 制度背景 /
*     已有文献来论证，而不是用一个内生回归去"证明"。
*   - 即：机制检验 = 可信地识别"处理确实改变了机制变量 M" + 理论说明"M 影响 Y"。
*===============================================================================
use "$clean/analysis.dta", clear
global D    treat
global X    "size lev roa age soe"
* 机制变量（与主回归处理 D 之后、结果 Y 之前测量；构造不得用未来信息）
global Ms   "earnings_mgmt internal_control"     // 例：盈余管理、内部控制

*--- D → M：对每个机制变量，复用主回归识别策略（此处交叠 DID/TWFE 示例）----
eststo clear
foreach m of global Ms {
    eststo m_`m': reghdfe `m' $D $X, absorb(id year) vce(cluster id)
    * 解读：处理显著改变了机制变量 M（这是被可信识别的因果环节）
}
esttab m_* using "$tables/t_mechanism.rtf", replace ///
    b(3) se(3) star(* 0.1 ** 0.05 *** 0.01) ///
    keep($D) label title("表X 机制检验：处理对机制变量的影响") ///
    addnotes("注：括号内为企业层面聚类稳健标准误。M→Y 的逻辑由理论与已有文献论证（见正文）。")

*--- 不要做的事（保留作为反面提醒，勿启用）---------------------------------
* 中介逐步法 / Sobel：sgmediation Y, mv(M) iv(D) cv($X)      // ✗ 已不接受
* Bootstrap 间接效应占比                                       // ✗ 不报告

di as result "===== 07_mechanism.do 完成；M→Y 用理论论证，勿跑内生中介回归 ====="
