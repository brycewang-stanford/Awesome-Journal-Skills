---
name: socs-quantitative
description: Use for the quantitative path in 《社会学研究》 (Sociological Studies) — analyzing survey data (CGSS/CFPS/CLDS) with regression / Logit / multilevel / event-history (survival) / sequence analysis, and interpreting results as a sociological mechanism rather than entering an econometric identification arms race. Use when the draft only reports coefficients.
---

# 定量路径（socs-quantitative）

## 触发时机

- 数据是 CGSS / CFPS / CLDS / 人口普查等社会调查
- 已有回归结果，但只报系数与显著性，缺社会学解读
- 担心审稿人嫌"识别不干净"，想往因果军备竞赛上加码

## 立场：方法服务社会学问题

本刊不是因果识别竞赛场。**系数本身不是发现，社会过程才是。**识别要诚实、稳健，但目标是揭示机制与异质性的**社会学含义**，不是把工具变量堆到无懈可击。描述性事实若揭示重要社会结构，本刊比经济学刊更接纳。

## 方法工具箱（按问题选，不是越炫越好）

| 问题形态 | 常用方法 |
|----------|----------|
| 连续/类别结果的影响因素 | OLS / Logit / 多项 Logit / 有序 Logit |
| 嵌套结构（个体嵌入地区/学校/家庭） | 多层模型（HLM）、随机效应 |
| 事件发生与时机（初婚、离职、流动） | 事件史 / 生存分析（Cox、离散时间） |
| 生命历程的状态序列 | 序列分析、最优匹配 |
| 潜变量与测量结构 | 结构方程、潜类别 |
| 代际/流动结构 | 对数线性、流动表分析 |

## 数据与测量规范

- 交代抽样、权重、缺失处理（CGSS/CFPS/CLDS 的设计权重与追访结构）
- 关键变量的**社会学操作化**：为什么这样测，测的是哪个理论构念
- 报告样本量随模型变化、稳健性来源；区分横截面与面板含义

## 把定量做成社会学的关键

- **机制**：不止"X 显著"，而是"经由什么社会过程"——转 `socs-mechanism-social-process`
- **异质性**：按结构位置（阶层、城乡、性别、世代）切分，并给社会学解释
- **解读**：把效应量翻译成可理解的社会后果（多少机会差距、多大流动壁垒）

## 微型走查示例（CGSS·城乡教育回报，数字为示意）

设有定量稿，基于 CGSS 多年混合截面，估出高等教育对城镇户籍者收入回报约为 38%、对农村户籍者约为 22%（示意）。把它做成社会学：

```
× 经济学式写法：教育回报城镇 38% > 农村 22%，建议加大农村教育投入。
  —— 落在政策建议，异质性只切城乡，无结构含义。

√ 社会学化改造：
  方法由问题定：用分组回归 + 交互项刻画"回报的结构性分化"，
    而非追加工具变量去"洗干净"教育的因果效应（本刊不奖励识别军备）。
  操作化的社会学理由：把"户籍"测为制度性身份而非控制变量，
    它对应"机会结构的制度分割"这一构念。
  机制（接 socs-mechanism）：同等学历在城乡劳动力市场被
    差别定价——城镇部门的正式雇佣、社会网络与信号机制放大学历价值，
    农村/非正式部门则压缩之，于是教育非但未必弥合城乡差距，
    反而成为新的分化通道。
  异质性的结构解释：差距随进入正式部门的概率而扩大（按部门切，
    而非简单按"东中西"切）。
  效应翻译：约 16 个百分点的回报落差，意味着同一张文凭在两类
    制度位置上兑换出显著不同的生命机会。
  稳健性：报告不同年份子样本、权重前后结果，区分横截面解读边界。
  落点：修正"教育是均等器"的判断，提出教育回报的"制度分割"机制。
```

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《社会学研究》兼有定性与定量；下面的链路服务其定量因果支线，定性/概念建构另循其标准。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 自检清单

- [ ] 方法由问题决定，不是为炫技选难模型
- [ ] 变量操作化有社会学理由，对应理论构念
- [ ] 抽样/权重/缺失处理交代清楚
- [ ] 系数已翻译成社会过程与社会后果，不止显著性
- [ ] 异质性按结构位置切分并有解释
- [ ] 不把"识别更干净"当作主要贡献

## 审稿人追问 + 本刊语境修法

社会学审稿人与经济学审稿人的追问点不同，对症修法：

- 追问（社会学向）："系数我看到了，社会过程在哪？" → 修法：每个核心结果后补一句机制翻译，转 `socs-mechanism-social-process`。
- 追问："这个变量为什么这么测？它测的是哪个理论构念？" → 修法：补操作化的社会学理由，将测量与构念对齐。
- 追问："异质性只切东中西，看不出结构含义。" → 修法：改按阶层/城乡/性别/世代/部门等结构位置切分，并给社会学解释。
- 追问（偏经济学向）："识别不够干净，存在内生性。" → 修法：诚实报告稳健性与边界，同时说明本文目标是揭示机制而非估计净效应（参见 `socs-fit-positioning`）。
- 追问："权重/缺失/样本变化没交代。" → 修法：补抽样设计、设计权重、缺失处理与各模型样本量变化。

## 反模式

- 把显著性当结论，无机制无解读
- 识别军备竞赛，喧宾夺主盖过社会学问题
- 异质性只切"东中西"，无结构含义
- 罗列模型不报告稳健性与样本变化

## 输出格式

```
【数据】CGSS/CFPS/CLDS/普查（年份、样本、权重）
【方法】<回归/多层/事件史/序列…> 及理由
【关键构念操作化】<…>
【机制】社会过程 = <…>（→ socs-mechanism-social-process）
【异质性】按 <结构位置> + 社会学解释
【下一步】socs-mechanism-social-process
```
