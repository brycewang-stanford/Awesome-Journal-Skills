---
name: jfr-identification
description: Use when the identification strategy is the bottleneck for a 《金融研究》 (Journal of Financial Research) manuscript — policy shocks (MPA / 资管新规 / LPR / 注册制), high-frequency monetary-policy surprises, DID, IV, RDD — stress-testing the design before drafting tables.
---

# 因果识别策略（jfr-identification）

## 触发时机

- 实证主体仅 OLS + 控制变量，谈"相关"不谈"因果"
- 宏观题靠时间序列相关讲故事，缺冲击识别
- DID 用 TWFE 但没回应异质性处理批评
- IV 第一阶段弱 / 排他性存疑

## 设计优先级（《金融研究》口味，强 → 弱）

1. **自然实验式政策冲击 + DID**（MPA 考核、资管新规、LPR 改革、注册制等监管/政策变动）
2. **高频识别**：货币政策意外（政策公告窗口的利率/价格高频反应）
3. **断点回归**（清晰的监管门槛：资本充足率、规模、评级阈值）
4. **工具变量**（强工具 + 排他性论证；金融题常用制度/地理/历史工具）
5. **倾向得分匹配 + DID**
6. 宏观时序方法：**VAR / 局部投影（local projection）/ 符号约束**，用于刻画传导
7. OLS + 严密内生性讨论（结构估计或理论实证中可接受）

## 分支路径

### 分支 A：政策冲击 DID

- 是否 staggered（分批生效）？→ 必须 Goodman-Bacon 分解 + Callaway-Sant'Anna 或 Sun-Abraham
- 平行趋势：事件研究图必画；处理前系数应不显著
- 安慰剂：随机分配处理组/处理时点 500–1000 次
- 把"政策外生于个体决策"用制度细节论证（见 jfr-institutional-background）

### 分支 B：高频货币政策意外

- 用政策公告窗口（如 MLF/OMO/LPR 公布）的高频价格变动构造意外
- 窗口选择与基准资产说明清楚；剔除同窗其它信息
- 与低频结果交叉印证（局部投影 IRF）

### 分支 C：宏观传导（VAR/LP）

- 识别假设明确（递归/符号约束/外部工具）
- 报告脉冲响应 + 置信带；稳健于滞后阶数与变量排序
- 区分"价格型"与"数量型"货币政策工具

### 分支 D：IV / RDD

- IV 第一阶段 F **≥ 10**（弱工具 → Anderson-Rubin 稳健 CI）；排他性给理论/制度/安慰剂三段；报告 reduced form
- RDD：McCrary 操纵检验 + 最优带宽（CCT）+ ≥ 3 个带宽稳健性 + 协变量平滑

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《金融研究》是中文金融顶刊，企业金融因果链 + 资产定价的多重检验(factor-zoo)。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 必查清单

- [ ] 平行趋势 / 平滑性 / 弱工具 检验齐全
- [ ] 安慰剂（处理对象/时点随机）做了
- [ ] 标准误聚类层次合理（公司/银行/行业/地区 × 时间）
- [ ] 风险类指标稳健（VaR/CoVaR/SRISK 等口径一致）
- [ ] 回应"预期效应/抢跑"（政策前调整）

## 微型走查：资管新规（2018）对银行表外扩张的 DID

示意稿，数字均为虚构演示，展示一条政策冲击识别如何过审：

- **冲击与处理强度**：2018 年资管新规打破刚兑、限制非标。以各银行**新规前表外理财/总资产**为处理强度（连续 DID），高暴露银行受冲击更大。
- **基准结果**：高暴露组在新规后表外资产增速较低暴露组下降约 6.5 个百分点（聚类到银行层面，t≈3.1）。
- **平行趋势**：事件研究图显示新规前 6 个季度处理强度 × 时点交互系数均不显著，新规当季起显著为负。
- **staggered 检查**：本例为单一时点冲击，不涉分批处理；若改用各地落地时点差异，则须 Goodman-Bacon 分解，并换 Callaway-Sant'Anna 估计量。
- **安慰剂**：随机打乱处理强度 1000 次，真实系数落在虚拟分布 1% 尾部之外。
- **外生性论证**：新规为央行等五部委统一发布、对全行业一刀切，单家银行无法影响其颁布 → 政策外生于个体决策。

## 审稿人追问模式与本刊语境下的修法

| 审稿人追问 | 背后担心 | 本刊语境修法 |
|------------|----------|--------------|
| "高暴露银行本就增速放缓，不是新规所致？" | 处理组事前趋势不同 | 出事件研究图证前趋势平，必要时加 PSM-DID |
| "银行是否预期到新规提前缩表（抢跑）？" | 预期效应污染 | 检验新规前系数，剔除征求意见稿窗口 |
| "TWFE 在连续处理下还可信吗？" | 异质性处理偏误 | 改用双重稳健或异质性稳健估计量 |
| "风险度量为何时而 VaR 时而 CoVaR？" | 口径不一致 | 全文统一风险口径，附录报告替代度量 |

## 校准锚点

本刊高质量实证稿的识别证据通常包含**事件研究图 + 安慰剂 + 至少一组替代识别或子样本**，宏观题另配脉冲响应与稳健性区间。"只有基准 DID 表、无前趋势图"的稿件在外审阶段几乎必被要求补做。具体期待以编辑部最新稿约与近期已刊论文为准。

## 反模式

- TWFE + staggered 不谈异质性处理偏误
- 货币政策题用时序相关冒充因果，无冲击识别
- "我们认为该监管外生于公司决策"却无制度/数据证据
- IV 用"外生事件 × 上期内生变量"，排他性站不住
- 风险度量随意（VaR 与 CoVaR 混用口径）
- 连续处理 DID 直接套 TWFE，不检验异质性处理偏误

## 输出格式

```
【识别策略】政策冲击DID / 高频意外 / VAR-LP / IV / RDD / 结构
【已完成检验】[平行趋势, 安慰剂, 弱工具, McCrary, ...]
【缺失检验】[...]
【聚类层次】...
【外生性论证】制度□ 数据□ 安慰剂□
【下一步】jfr-mechanism
```
