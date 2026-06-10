---
name: acr-workflow
description: Use when deciding which acr-* sub-skill to invoke next, or when sequencing manuscript work from fit positioning through rebuttal for 《会计研究》 (Accounting Research). Routes — does not replace — the specialized skills.
---

# 《会计研究》工作流（acr-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 acr-* skill**。

默认假设：目标是国内会计学第一刊《会计研究》（财政部主管、中国会计学会主办，月刊，CSSCI 唯一会计刊、NSFC 管理科学 A 类）。衡量标准是**会计议题的实证贡献 + 准确的制度/准则细节 + 信息机制**，而非金融定价机理或纯方法复杂度。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能投《会计研究》/ 下一步做什么"
- 拿不准落点是会计议题还是公司金融机理
- 有上市公司面板数据但讲不出"会计信息/披露/准则"故事
- 收到 R&R 外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定是会计议题还是金融机理、对不对口 | `acr-fit-positioning` |
| 选题像"X 影响 Y"的一般效应，缺会计学贡献 | `acr-topic-selection` |
| 文献只堆近年实证、没进会计脉络 | `acr-literature-review` |
| 制度背景/准则条款/执行时点写得含糊 | `acr-institutional-standards` |
| 会计度量直接用现成指标、没交代构造 | `acr-measurement` |
| 实证只有 OLS、识别不过关 | `acr-identification` |
| 有主结果但没机制、或机制写成定价渠道 | `acr-mechanism` |
| 缺稳健性 / 度量与制度控制不足 | `acr-robustness` |
| 表格列数过多 / 没解读经济量级 | `acr-tables-figures` |
| 文末贡献只有"丰富文献"、缺准则/监管启示 | `acr-implications` |
| 准备投稿，需要体例与系统 checklist | `acr-submission` |
| 收到 R&R，需要写回复 | `acr-rebuttal` |

## 默认顺序

1. `acr-fit-positioning` — 先判断是会计议题还是金融机理，别把金融稿硬投会计刊
2. `acr-topic-selection` — 立会计学贡献与中国制度情境
3. `acr-literature-review` — 进入会计脉络对话（盈余质量/审计/披露）
4. `acr-institutional-standards` — 把准则/监管背景写准（条款、时点）
5. `acr-measurement` — 透明构造会计度量
6. `acr-identification` — 准则/监管外生变更优先的识别
7. `acr-mechanism` — 信息机制（降低不对称/提高披露/约束盈余管理）
8. `acr-robustness` — 替换度量、控制治理/制度变量、安慰剂
9. `acr-tables-figures` — 主表/主图 + 经济量级解读
10. `acr-implications` — 准则/监管/实务启示
11. `acr-submission` — 投稿前 preflight（页下注、著者—出版年制、线上系统）
12. `acr-rebuttal` — 外审后

## 决策口诀

- "落点在会计信息/审计/披露/准则" → 本刊对口，进 `acr-topic-selection`
- "落点在融资/投资/股价定价机理" → 改投《金融研究》（先过 `acr-fit-positioning`）
- "盈余管理只用一个代理变量" → `acr-measurement` + `acr-robustness`
- "制度背景说不清准则哪条、何时实施" → `acr-institutional-standards`
- "机制写成'提高了股价信息含量'但没说披露/盈余渠道" → `acr-mechanism`

## 与本仓库其它期刊包的差异

- 偏融资/投资/定价机理：转 **journal-of-financial-research**（金融机理）
- 偏公司治理的管理学理论 / 案例：转 **nankai-business-review**（治理偏管理理论）
- 偏干净因果 + 经济学理论：转 **economic-research**
- 偏税收/产业政策的宏观或产业效应：转 **china-industrial-economics**
- 《会计研究》要的是**会计信息生产与披露 + 准则制度细节 + 信息机制**

## 反模式

- **不要**跳过 `acr-fit-positioning` 就动笔——它最常救稿（避免把金融稿投错门）
- **不要**在度量未交代构造时去抠表格与文风
- **不要**让 `acr-rebuttal` 在正文未修订前生成回复

## 本刊全流程的审稿期待（决策表）

《会计研究》由中国会计学会主办，是 CSSCI 唯一权威顶级会计学期刊。路由按"当前最薄弱的会计学环节"跳转，而非机械按序。下表对齐各阶段审稿期待与退稿模式：

| 阶段 | 审稿期待 | 常见退稿模式 |
|------|----------|--------------|
| 对口 | 落点在会计信息/披露/审计 | 金融稿贴会计背景 |
| 识别 | 准则外生变更 DID | TWFE 不回应异质性 |
| 机制 | 信息渠道直接测 | 写成定价渠道 |

## 微型走查：一篇稿子如何走完路由（数字示意）

虚构稿《关键审计事项披露与盈余质量》入口走查（示意）：因变量"盈余质量"是会计产出 → 对口进选题；贡献立为"关键审计事项披露通过提高鉴证针对性改善盈余质量"，制度抓手为强制披露起始年份（待核实）；盈余质量用 |DA| 度量，以强制披露起始为冲击做 DID，事件研究图处理前近零、主系数 −0.012（t≈2.2）；测关键审计事项条目数作为信息中介，方向一致；收尾接稳健性→表格→启示→投稿→回复。

> 上述系数为演示路由衔接的示意值，非真实结果。

## 路由追问与本刊语境修法

- 用户问"下一步做什么" → 找当前最薄弱环节（常是机制或识别），按路由表跳转，而非线性顺推。
- 用户问"这能投《会计研究》吗" → 先过 acr-fit-positioning 判落点，再决定进流程或改投。

## 校准锚点

本刊为月刊、三审终审 + 双向匿名、审稿周期约三个月。各阶段顺序可因稿件状态调整；体例、审稿时限等以编辑部最新《投稿指南》为准。

## 输出格式

```
【当前阶段】<识别>
【下一个 Skill】acr-...
【落点确认】会计议题 / 金融机理（若后者→改投）
【缺口】[度量 / 识别 / 机制 / 制度背景 ...]
```
