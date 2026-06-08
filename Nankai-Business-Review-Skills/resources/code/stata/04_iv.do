*===============================================================================
* 04_iv.do —— 工具变量（现代弱工具诊断与稳健推断）
*
* 投稿口径（er-identification）：
*   不要只报 "F>10"。标准报告要素：
*     (1) 第一阶段 Kleibergen-Paap rk Wald F（异方差 / 聚类下有效）
*     (2) 对照 Stock-Yogo 临界值
*     (3) 有效 F（Montiel Olea & Pflueger 2013），单内生变量更稳妥
*     (4) 弱工具稳健推断：Anderson-Rubin 检验与置信区间
*     (5) 过度识别：Hansen J；排他性需理论 + 制度 + 安慰剂三段论证
*===============================================================================
use "$clean/analysis.dta", clear
global Y   rd_invest
global D   digital                  // 内生解释变量
global Z   "iv_distance iv_peer"    // 工具变量
global X   "size lev roa"           // 外生控制

*--- 1. 主估计：ivreg2 自动报告 KP rk Wald F、Hansen J、内生性检验 ----------
ivreg2 $Y $X (${D} = $Z), robust first
* first 选项打印第一阶段；关注 "Kleibergen-Paap rk Wald F statistic"
* 与 Stock-Yogo 临界值比较（ivreg2 输出中给出）

*--- 2. 有效 F 检验（Montiel Olea–Pflueger，对异方差/自相关稳健）-----------
* 需单内生变量；紧跟 ivreg2 之后运行
weakivtest

*--- 3. 弱工具稳健推断：Anderson-Rubin / CLR / K 检验与置信区间 -------------
* 恰好识别时 AR 对弱工具完全稳健；过度识别下看 CLR
weakiv ivreg2 $Y $X (${D} = $Z), robust

*--- 4. reduced form（审稿人常要求报告）------------------------------------
reghdfe $Y $Z $X, absorb(id year) vce(cluster id)

*--- 5. Lewbel (2012) 异方差识别工具（作为外部工具的稳健性 / 补充）---------
* ssc install ivreg2h, replace
* ivreg2h $Y $X (${D} = $Z), robust

di as result "===== 04_iv.do 完成；报告 KP F + 有效 F + AR 区间 ====="
