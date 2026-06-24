---
name: jwe-identification
description: Use when the identification strategy is the bottleneck for a 《世界经济》 (The Journal of World Economy) manuscript — external shocks (tariffs, trade agreements, exchange-rate reforms, FDI negative-list) as quasi-experiments, plus shift-share / Bartik and gravity designs. Stress-tests exogeneity and inference, including the modern shift-share critiques.
---

# 开放经济识别策略（jwe-identification）

> 在《世界经济》（IWEP + 中国世界经济学会主办，月刊），识别策略的外生变动最好锚在**国际/制度性冲击**上（关税战、入世、汇改、外资负面清单、全球需求冲击），而非国内政策的副产品——这是本刊区别于综合性/金融类期刊的识别口味。shift-share 与引力-PPML 是本刊高频设计，其现代推断批评（GPSS/BHJ/AKM）也是本刊审稿人高频追问点。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 实证主体仅 OLS + 控制变量，外生性靠"我们认为"
- 用 shift-share / Bartik 暴露度但不讨论 exposure 外生性与推断
- 引力模型用 OLS-log、零贸易直接丢
- 有外部冲击但没想清"为何对个体外生"

## 设计优先级（开放经济场景）

1. **外部 / 制度性冲击 + DID / event-study**：关税战、入世、自贸区、汇改、外资负面清单
2. **shift-share / Bartik 暴露度**（进口渗透、出口需求冲击）——需现代推断
3. **引力模型（PPML）** 估贸易政策（协定、关税）效应
4. **IV**（外部冲击作工具，论证排他性）
5. OLS + 严密外生性讨论（理论实证 / 结构估计中可接受）

## 分支路径

### 分支 A：外部冲击 DID / event-study
- 冲击是否真外生于个体（关税由贸易伙伴决定 / 政策非内生于被处理者）？
- staggered 处理 → 用 Goodman-Bacon 分解 + Callaway-Sant'Anna / Sun-Abraham，别裸用 TWFE
- 平行趋势：事件研究图必画；安慰剂（随机处理时点 / 对象）
- 预期效应：被处理者是否提前响应（前置项）

### 分支 B：shift-share / Bartik（重点）
- 暴露度 = 初期份额 × 共同冲击（如 ADH 的进口渗透）
- **现代推断批评必须回应**：
  - Goldsmith-Pinkham-Sorkin-Swift：识别力来自**份额**，须检验份额外生、报告 Rotemberg 权重
  - Borusyak-Hull-Jaravel：识别力来自**冲击**，须冲击层面随机性 + 相应推断
  - Adão-Kolesár-Morales：标准误须按暴露结构调整（常规聚类会过度拒绝）
- 至少报告：份额外生性论证、Rotemberg 权重 top 来源、shock-level 或 exposure-robust 标准误

### 分支 C：引力模型
- **用 PPML**（Santos Silva-Tenreyro）处理异方差与零贸易，别用 OLS-log
- 进出口国×年 + 国家对固定效应（multilateral resistance）
- 贸易政策变量（协定 / 关税）内生性：滞后 / IV / 事件研究

### 分支 D：IV（外部冲击为工具）
- 第一阶段 F ≥ 10；弱工具用 Anderson-Rubin / weak-IV-robust CI
- 排他性三段论：理论 + 制度 + 安慰剂
- 报告 reduced form

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《世界经济》是国际经济实证刊，跨国/企业面板；强调识别与聚类。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 必查清单

- [ ] 外部冲击对个体的外生性有制度 / 理论证据，不只"我们认为"
- [ ] staggered DID 回应了异质性处理偏误
- [ ] shift-share 报告份额外生性 + Rotemberg 权重 + exposure-robust SE
- [ ] 引力用 PPML + 多边阻力固定效应
- [ ] 平行趋势 / 安慰剂 / 弱工具 检验齐全
- [ ] 标准误聚类层次与暴露 / 冲击结构匹配

## 反模式

- shift-share 当普通 IV 用，标准误常规聚类、不提 exposure-robust 推断
- 关税 / 协定当外生但不论证对方为何这样定
- 引力 OLS-log 丢零贸易
- TWFE + staggered 不讨论 Bacon 分解

## 《世界经济》识别审稿期待表

本刊（IWEP + 中国世界经济学会主办的 CSSCI 权威顶级期刊）的识别口味，是外生变动锚在国际/制度性冲击上、并通过现代推断检验。下表把退修信号显性化。

| 审稿期待 | 达标 | 退修/退稿信号 |
|----------|------|----------------|
| 外生性锚国际冲击 | 关税战/入世/汇改/负面清单作准实验 | 外生性靠"我们认为"，OLS+控制 |
| staggered DID 现代化 | Goodman-Bacon 分解 + CS/Sun-Abraham | 裸用 TWFE 不谈异质性处理偏误 |
| shift-share 现代推断 | 份额外生+Rotemberg 权重+exposure-robust SE | 当普通 IV 用，常规聚类 |
| 引力用 PPML | PPML+多边阻力 FE+零贸易保留 | OLS-log 丢零贸易 |

## 微型走查：进口竞争 shift-share 的推断体检（示意）

设以 ADH 式进口渗透暴露度（初期行业份额×对手国对华出口冲击）识别就业效应。按本 skill 体检：

```
走查体检：
  识别力来源 → 判断来自份额还是冲击（GPSS vs BHJ）→ 本设定份额主导
  份额外生 → 检验初期份额与前趋势相关性，报告平衡性
  Rotemberg 权重（示意）→ top5 行业贡献约 6 成识别力，列出并讨论其可信度
  标准误 → 常规聚类 se 0.012 → AKM exposure-robust se（示意）0.021，结论不变号
  推断口径 → 按暴露结构而非行政区聚类，避免过度拒绝
报告清单：份额外生论证□ Rotemberg top□ exposure-robust SE□
```

> 走查中的权重占比与标准误为示意占位，仅演示现代 shift-share 推断流程，非真实估计。

## 审稿人追问模式 + 本刊语境修法

- 追问"shift-share 标准误是否过度拒绝" → 补 AKM/BHJ 的 exposure-robust 推断，并说明识别力来源。
- 追问"关税/协定凭什么对个体外生" → 给制度+理论+安慰剂三段论，论证对方为何这样定。
- 追问"staggered 处理有没有异质性偏误" → 报 Goodman-Bacon 分解，改用 Callaway-Sant'Anna 或 Sun-Abraham。

## 校准锚点（本刊已刊论文形态）

本刊识别类论文多以国际/制度性冲击为准实验，配事件研究图、安慰剂与现代 shift-share/引力推断；裸 TWFE 与 OLS-log 引力较难通过审稿。具体识别规范与推断要求以编辑部最新稿约及审稿惯例为准。

## 输出格式

```
【识别策略】外部冲击DID / shift-share / 引力PPML / IV / 结构
【外生性论证】制度□ 理论□ 安慰剂□
【shift-share 推断】份额外生□ Rotemberg□ exposure-robust SE□
【已完成检验】[平行趋势, 安慰剂, 弱工具, ...]
【缺失检验】[...]
【下一步】jwe-transmission-channel
```
