---
name: mw-identification
description: Use when the empirical identification strategy is the bottleneck for a Management-World manuscript — quasi-experimental designs (DID, IV, RDD, DML, event study) with Chinese policy shocks. Stress-tests the design before drafting tables.
---

# 因果识别策略（mw-identification）

## 触发时机

- 实证主体仅有 OLS + 控制变量，担心被退稿
- DID 用了 TWFE 但没回应近年异质性处理批评（Goodman-Bacon, de Chaisemartin, Sun-Abraham, Callaway-Sant'Anna）
- IV 第一阶段 F 弱 / 工具变量内生性疑虑
- 准备用双重机器学习但不确定怎么报告

## 设计优先级

《管理世界》编委的偏好排序（强 → 弱）：

1. **政策冲击 + DID（含 staggered / continuous treatment）**
2. **断点回归（清晰的政策门槛）**
3. **工具变量（强工具 + 排他性论证）**
4. **倾向得分匹配 + DID**
5. **合成控制法**
6. **双重机器学习 / 因果森林**
7. OLS + 内生性讨论（容易退稿）

## 分支路径

### 分支 A：DID

- 是否 staggered？→ 必须用 Goodman-Bacon 分解 + Callaway-Sant'Anna 或 Sun-Abraham
- 平行趋势检验：事件研究图必须画
- 安慰剂：随机分配处理组 500–1000 次
- 是否汇报 Bacon 分解的"坏比较"权重？

### 分支 B：IV

- 第一阶段 F **必须 ≥ 10**（弱工具 → 用 Anderson-Rubin 或 weak-IV-robust CI）
- 排他性论证至少需要 3 段：理论 / 制度 / 安慰剂
- 是否报告了 reduced form？

### 分支 C：RDD

- 是否做了 McCrary 检验？
- 带宽：是否使用最优带宽（Calonico-Cattaneo-Titiunik）+ 至少 3 个带宽稳健性？
- 协变量平滑性检验

### 分支 D：DML

- 报告 sample-split 数 + cross-fitting
- 报告 nuisance 函数选择（lasso / random forest / xgboost）
- 至少给出 5 种不同 ML 学习器的稳健性

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《管理世界》重中国情境实证 + 政策可操作；识别 + 经济量级，定性/案例另循其标准。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 必查清单

- [ ] 平行趋势 / 平滑性 / 弱工具 检验都做了
- [ ] 安慰剂检验做了（处理时点随机 / 处理对象随机）
- [ ] 主回归的标准误聚类层次合理（个体 / 个体+时间 / 处理层级）
- [ ] 是否有"两阶段"识别（先确认外生性，再估处理效应）
- [ ] 是否回应了"被处理者预期"问题

## 反模式

- TWFE + staggered 但不讨论异质性处理偏误
- IV 用"外生事件 × 上一期内生变量"——审稿人会问"为何上一期不影响当期"
- "我们认为该政策外生于公司决策"但没给证据
- RDD 用了截断带宽但不汇报带宽敏感性

## 本刊识别策略决策表

《管理世界》由国务院发展研究中心主办，是管理学与经济学并重的 CSSCI 权威顶级综合期刊，识别策略的审稿期待显著区别于纯方法论期刊：编委更看重"政策冲击是否真实服务国家重大战略、识别逻辑是否能讲成一个中国制度故事"，而非工具的新颖度。下表锚定本刊语境下的审稿决策（不确定的格式细节以编辑部最新稿约为准）：

| 识别情形 | 本刊编委倾向 | 退稿高风险信号 |
|---|---|---|
| 国家级试点政策（自贸区、注册制、低碳试点）+ staggered DID | 强烈认可，契合"服务国家战略"定位 | 不做异质性处理偏误诊断 |
| 行政审批门槛 + RDD | 认可（制度门槛清晰可信） | 门槛被操纵未做 McCrary |
| Bartik / 份额-移动份工具变量 | 谨慎接受，需排他性三段论 | 仅一句"我们认为外生" |
| 纯横截面 OLS + 控制变量 | 高概率退稿 | 把内生性讨论写成免责声明 |
| 跨国面板 + 方法论创新 | 与本刊定位错配，建议改投 | 中国情境缺位 |

### 常见退稿模式（识别维度）

- "政策外生性"只有断言没有制度证据——本刊编委会要求把试点遴选机制写进制度背景章节
- staggered DID 全程 TWFE，对 2021 年以来的异质性处理偏误文献只字不提
- 工具变量"看上去外生"，但与企业全要素生产率存在共同的宏观驱动，排他性论证缺位
- 用海外数据论证中国问题，识别再干净也难过"国家战略相关性"这一关

## 微型走查示例：数字化转型与企业全要素生产率

虚构一篇稿件，按本 skill 的决策规则走一遍（以下数字均为示意，仅示范判断流程）：

- **设定**：以 2018 年某省"企业上云"补贴试点为冲击，考察数字化转型对企业全要素生产率（TFP_LP）的影响，样本为 A 股制造业上市公司 2012—2022 年面板，N≈18,600（示意）。
- **走查分支 A（DID）**：试点分批推开 → 判定为 staggered → 触发规则"必须 Goodman-Bacon 分解 + Callaway-Sant'Anna"。示意结果：Bacon 分解显示"坏比较"权重 11%（示意），改用 CS 估计量后动态效应系数 0.032（示意），与 TWFE 的 0.041 接近但更稳。
- **平行趋势**：事件研究图 -5 至 -1 期系数均不显著（示意），处理后第 2 期起显著为正。
- **安慰剂**：随机抽取处理时点重复 1000 次，真实估计落在分布右尾 1% 外（示意）。
- **本刊语境校验**：补贴试点对应"数字中国"国家战略 → 通过战略相关性关；TFP 提升对应"高质量发展" → 政策含义落点清晰。
- **判定**：识别策略可进入下一阶段（mw-mechanism-heterogeneity），但需在制度背景章节补齐试点遴选的外生性证据。

## 审稿人追问模式 + 本刊语境修法

- 追问"试点地区是否本就数字化基础更好？" → 本刊修法：在制度背景中引用试点遴选文件，证明遴选依据与企业 TFP 无关，并补企业层面 pre-trend 平衡表。
- 追问"补贴可能同时改变了融资约束，机制不纯？" → 修法：把融资约束作为竞争性机制显式纳入 mw-mechanism-heterogeneity，而非回避。
- 追问"为什么不用更前沿的 DML？" → 本刊语境下，编委更认可"识别逻辑清晰可复述"，DML 可作稳健性而非主结果，避免为方法而方法。

## 校准锚点

本刊已刊实证论文的识别形态多为"国家级政策冲击 + staggered DID + 异质性处理偏误诊断 + 安慰剂 + 多重稳健性"，且识别章节与制度背景章节强耦合。新方法（DML、合成 DID）通常出现在稳健性部分而非主结果。具体年度格式与方法偏好以编辑部最新稿约为准。

## 输出格式

```
【识别策略】DID / IV / RDD / DML / 其他
【已完成检验】[平行趋势, 安慰剂, 弱工具, ...]
【缺失检验】[...]
【聚类层次】...
【国家战略相关性】强 / 中 / 弱
【下一步】mw-mechanism-heterogeneity
```
