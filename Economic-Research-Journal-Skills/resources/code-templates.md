# 现代因果推断代码模板（命令 + 引文速查）

> 面向《经济研究》《中国工业经济》级别审稿要求。命令名与安装行已于 2026-06 联网核实。
> **精确选项语法以 Stata 内 `help <cmd>` 为准**（各包随版本更新选项）。
>
> **本文件 = 命令出处与引文速查；可运行的分步脚本见 [`resources/code/`](code/)（`*.do`）。** 二者互补：
> `code/` 给从清洗到 DID 的端到端 `.do` 流程，本文件给每个命令的来源、引文与「审稿一句话检查」。
> 配合 [`skills/er-identification`](../skills/er-identification/SKILL.md)、
> [`skills/er-robustness`](../skills/er-robustness/SKILL.md) 使用。

---

## 0. 一次装齐（Stata）

```stata
* 交错 DID 异质性稳健估计量
ssc install bacondecomp
ssc install drdid, all replace
ssc install csdid
ssc install eventstudyinteract
ssc install avar
ssc install did_multiplegt_dyn
ssc install did_imputation
ssc install did2s
* 事件研究 / Honest DiD
ssc install eventdd
ssc install coefplot
ssc install honestdid          // 或 net install from mcaceresb/stata-honestdid
* IV
ssc install ivreg2
ssc install ivreghdfe
ssc install ftools
ssc install reghdfe
ssc install weakivtest
ssc install weakiv
* RDD（优先 net install 取最新，SSC 版常滞后）
net install rdrobust,  from(https://raw.githubusercontent.com/rdpackages/rdrobust/master/stata)  replace
net install rddensity, from(https://raw.githubusercontent.com/rdpackages/rddensity/master/stata) replace
* 稳健性套餐
ssc install winsor2
ssc install psmatch2
ssc install boottest
ssc install psacalc
```

R 端：`install.packages(c("bacondecomp","did","fixest","didimputation","did2s","DIDmultiplegtDYN","rdrobust","rddensity","ivreg"))`；
`remotes::install_github(c("asheshrambachan/HonestDiD","jonathandroth/pretrends"))`。

---

## 1. 交错 DID（处理时点不同 → 必须用异质性稳健估计量）

**问题**：处理时点不同（staggered）且效应异质时，传统 TWFE 系数是各 2×2 DID 的加权平均，含「已处理组当对照」的**坏比较 + 负权重**，符号都可能错（Goodman-Bacon 2021；de Chaisemartin & D'Haultfœuille 2020；Sun & Abraham 2021；Borusyak, Jaravel & Spiess 2024）。

### 1.1 先做诊断：Goodman-Bacon 分解

```stata
ssc install bacondecomp
bacondecomp Y treat, ddetail        // 暴露各 2×2 DID 的权重与坏比较占比
```

### 1.2 主推估计量（任选其一作主表，另一两种作稳健性）

```stata
* Callaway & Sant'Anna (2021)：分组-时间 ATT(g,t)，never/not-yet-treated 作对照
csdid Y x1 x2, ivar(id) time(year) gvar(first_treat) method(dripw)
estat event                          // 动态效应（事件研究）
estat simple                         // 汇总 ATT
csdid_plot                           // 事件研究图

* Sun & Abraham (2021)：cohort × 相对时间 交互加权（IW）
eventstudyinteract Y rel_*, cohort(first_treat) control_cohort(never_treat) ///
    absorb(id year) vce(cluster id)

* de Chaisemartin & D'Haultfœuille（可开关 / 非二元 / 连续处理）
did_multiplegt_dyn Y id year D, effects(5) placebo(3)

* Borusyak, Jaravel & Spiess (2024) 填补法（效率最高）
did_imputation Y id year first_treat, allhorizons pretrends(5)
```

R 对应：`did::att_gt(...) |> aggte(type="dynamic")`；`fixest::feols(Y ~ sunab(cohort, year) | id + year)`；`didimputation::did_imputation(...)`；`DIDmultiplegtDYN::did_multiplegt_dyn(...)`。

**审稿一句话**：是否报告 Bacon 分解暴露负权重？主结果是否来自异质性稳健估计量（CS/SA/dCDH/BJS）而非裸 TWFE？

---

## 2. 事件研究与平行趋势（含 Honest DiD 敏感性）

```stata
* 事件图（交错设计下裸 TWFE 事件图有偏，应辅以稳健估计量事件图）
eventdd Y x1 x2 i.id i.year, timevar(rel_time) ci(rcap)
* 预趋势联合检验（注意：不显著 ≠ 平行趋势成立，存在功效不足问题）
test rel_m5 rel_m4 rel_m3 rel_m2

* Rambachan & Roth (2023) Honest DiD：事后违反 ≤ M̄×事前最大违反 下的稳健 CI 与 breakdown 值
ssc install honestdid
honestdid, pre(1/4) post(5/9) mvec(0.5(0.5)2) coefplot
```

R：`HonestDiD::createSensitivityResults_relativeMagnitudes(betahat, sigma, numPrePeriods, numPostPeriods, Mbarvec)`；功效用 `pretrends` 包（Roth 2022）。

**审稿一句话**：是否报告 Honest-DiD 在何 M̄ 下结论翻转？是否避免仅凭「预趋势不显著」下结论、并报告了预趋势检验功效？

---

## 3. 工具变量（IV）

```stata
* 2SLS 吸收高阶固定效应
ivreghdfe Y x1 x2 (endog = z), absorb(id year) cluster(id) first

* 弱工具：Montiel-Olea & Pflueger 有效 F（异方差/聚类稳健，取代 Stock-Yogo）
ivreg2 Y x1 x2 (endog = z), cluster(id)
weakivtest                            // 报告 effective F 与 MOP 临界值

* 弱工具稳健推断：Anderson-Rubin CI（弱工具下仍有效）
weakiv                                // AR / CLR / K 检验及对应 CI
```

**必报**：第一阶段（`first`）+ 简约式（z 对 Y 的 OLS）+ 排他性的理论/制度/安慰剂论证。

**审稿一句话**：报的是 effective F（MOP）而非仅 KP rk F？弱工具时给了 AR 稳健 CI？报告并讨论了简约式？

---

## 4. 断点回归（RDD，Cattaneo 团队 rdpackages）

```stata
* 核心估计：局部多项式 + 稳健偏差校正 CI（模糊 RD 加 fuzzy(D)）
rdrobust Y X, c(0)
rdbwselect Y X, c(0) bwselect(mserd)       // MSE-最优带宽
* 操纵检验（Cattaneo-Jansson-Ma 2020，优于原始 McCrary，无需预分箱）
rddensity X, c(0)
rdplotdensity ...                          // 密度图
rdplot Y X, c(0)                           // 含最优分箱拟合图
* 稳健性：带宽 0.5/0.75/1.25/2×；甜甜圈剔除断点邻域；协变量/假断点安慰剂；p(1) vs p(2)
rdrobust Y X if abs(X-0)>delta, c(0)       // donut RDD
```

**审稿一句话**：报告了 rddensity 操纵检验（无堆积）+ 协变量在断点连续？主结果是 robust bias-corrected CI 且对带宽/阶数稳健？避免高阶全局多项式（Gelman-Imbens 2019）？

---

## 5. 中文期刊标准稳健性套餐

| 检验 | 命令 / 做法 |
| --- | --- |
| 替换变量 | 换度量口径 / 对数化 / 滞后期重估 |
| 缩尾 | `winsor2 var, cuts(1 99) replace`（上下 1%） |
| 排除其他政策干扰 | 加同期他政策虚拟变量；剔除受影响样本/年份 |
| 安慰剂（随机化推断） | 随机抽取处理组与时点重复 500/1000 次，看真值是否落在伪分布尾部（循环 `bsample`/`permute`） |
| PSM-DID | `psmatch2 treat covs, ...` → 共同支撑样本跑 DID；`pstest` 查匹配后平衡 |
| Heckman | `heckman Y X, select(selvars) twostep`；报 λ/IMR、ρ |
| 改变聚类层级 | 不同层级 `vce(cluster .)`；少簇用 wild bootstrap：`boottest treatvar` |
| 高阶固定效应 | `reghdfe Y X, absorb(id year ind#year prov#year) vce(cluster id)` |
| Oster (2019) δ | `psacalc delta Xkey, rmax(1.3*r2)`——报告使 β=0 所需 δ；经验阈值 δ≥1 |

**审稿一句话**：安慰剂是「随机抽处理组与时点的分布检验」而非单点反事实？聚类层级稳健、少簇用了 wild bootstrap？报告了 Oster δ？

---

## 6. 机制 / 中介——现代规范（务必读 江艇 2022）

**核心引据**：江艇（2022）《因果推断经验研究中的中介效应与调节效应》，《中国工业经济》2022 年第 5 期，第 100–120 页（CNKI: GGYY202205006）。

**为何弃用「逐步回归三步法 + Sobel」**：中介变量 M 几乎总内生（M 与 Y 共受未观测因素影响），X→M→Y 中的 M→Y 段无随机化、**无因果识别**；Sobel/Bootstrap 只精化 a×b 的统计推断，不解决识别。机械三步法已是减分项。

**推荐做法**：
1. 机制部分**只需可信识别 X→M**——用与主回归相同的外生冲击/DID/IV，把被解释变量换成机制变量 M。
2. **M→Y 交给理论 + 异质性分组**：依据理论论证「若 M 是渠道，则在 M 起作用的子样本中 X→Y 应更强」，做分组检验而非把内生 M 当外生回归元。

```stata
* 机制：识别 X→M（与主回归同一识别策略）
reghdfe M treatXpost x1 x2, absorb(id year) vce(cluster id)
* 理论驱动的异质性分组（按 M 相关维度），看主效应是否符合理论预测
reghdfe Y c.treatXpost##c.Mexposure x1 x2, absorb(id year) vce(cluster id)
```

**不要**把 Sobel / 三步法系数乘积作为主要机制证据。

---

### 待核实 / 语法存疑
精确选项以 `help <cmd>` 为准：`csdid` 的 `method()`、`did_multiplegt_dyn` 的 `effects()/placebo()`、`honestdid` 的 `mvec()/pre()/post()`、`psacalc` 的 `rmax()`、`eventstudyinteract` 的 `rel_*`/cohort 变量需先手动构造。`did2s` 在 Stata（Kyle Butts SSC 移植）与 R（CRAN）同名但选项不同。

**来源**：江艇 2022（CNKI GGYY202205006）；csdid/did_imputation/eventstudyinteract/bacondecomp/honestdid（RePEc/boc）；did_multiplegt_dyn（GitHub chaisemartinPackages）；weakivtest（Pflueger-Wang, Stata Journal）；rdrobust/rddensity（rdpackages.github.io）；Rambachan-Roth 2023；Roth 2022；Oster 2019。
