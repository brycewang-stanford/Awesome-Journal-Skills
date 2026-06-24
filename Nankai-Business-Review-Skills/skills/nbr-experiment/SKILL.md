---
name: nbr-experiment
description: Use for experimental studies submitted to 《南开管理评论》 (Nankai Business Review) — design (between/within, scenario/vignette, lab/field), manipulation checks, randomization and confound control, effect sizes and power, and mediation/moderation via experimental-causal-chain or measurement-of-mediation designs. Use when a hypothesis is tested by manipulating an independent variable rather than measuring it.
---

# 实验法（nbr-experiment）

## 触发时机

- 自变量是**操纵**出来的（情境/启动/任务），不是测量
- 用情境实验（vignette/scenario）、实验室或现场实验做因果推断
- 想用实验补强问卷研究的内部效度（多研究设计）

## 设计要点

- 明确**被试间 / 被试内 / 混合**设计，给出各组样本量与分配
- 操纵材料**预测试（pilot）**：确认操纵有效、强度适中、无混淆
- **随机分配**到条件，报告分配方式；现场实验交代随机化层级

## 设计选型速查

| 设计 | 适用 | 本刊注意点 |
|------|------|-----------|
| 情境/卷面实验（vignette） | 操纵感知类构念（领导风格、算法反馈） | 材料须本土化改写并预测试，防"翻译腔"折损真实感 |
| 实验室实验 | 行为因变量（合作、投入、选择） | 报告被试来源（学生/在职），讨论可推广性 |
| 现场实验 | 组织内真实干预 | 交代随机化层级与企业配合细节；在本刊稀缺但竞争力强 |

## 走查示例：AI 反馈与员工创意

设想 2（反馈来源：AI / 主管）× 2（效价：肯定 / 否定）被试间情境实验，因变量为创意任务表现：
1. 预测试 60 人确认 AI/主管操纵的感知差异显著、材料真实感均值过线（如 7 点量表 > 5）
2. 正式实验各组 n ≥ 50，随机分配由平台自动完成并在文中报告
3. 操纵检验：来源感知主效应显著，且不影响"反馈具体性"评分（排除混淆）
4. 结果报告 η²p 与功效；交互显著后做简单效应分解
5. 研究 2 直接操纵中介（自我效能高/低启动）构成实验因果链——比只测中介更能说服本刊审稿人

## 多研究组合策略

本刊组织行为与营销类稿件常以"问卷 + 实验"双研究互补：问卷立外部效度，实验补内部效度。组合时让两个研究共用同一条机制链，不要各测各的；两研究在样本与情境上的差异，应在讨论中作为稳健性证据陈述。若实验先行（研究 1），可用企业在职样本问卷（研究 2）检验机制在真实组织中的再现，顺序由理论成熟度决定。

## 操纵检验与混淆控制

- **操纵检验（manipulation check）**：证明操纵确实改变了目标构念，且**未同时改变**其它构念
- **混淆排查**：需求特征、注意力检验（attention check）、可信度/真实感评分
- 报告**剔除标准**（未通过注意力/操纵检验者）及剔除前后稳健性

## 统计与效应量

- 报告**效应量**（Cohen's d / η²p / f），不只报 p 值
- 交代**功效分析（power）**或样本量依据
- 多重比较做校正；必要时报告贝叶斯因子或等效性检验
- **机制**：用**实验因果链**（操纵中介变量）或**测量中介 + Bootstrap**检验过程；调节用交互 + 简单斜率

## 执行桥（StatsPAI / Stata MCP）

把设计**跑出来并审计**，而不是只做描述。完整映射见
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md)。《南开管理评论》是中国情境实证管理刊；实验用随机化推断 + 多重检验，问卷-SEM 与测量循其规范，定性案例另循其标准。

- `detect_design` → `recommend` → 用 `as_handle=true` 拟合 → `audit_result` 列出尚欠的检查。
- **观察性因果：**交错 DID（`callaway_santanna` / `sun_abraham` + `bacon_decomposition` +
  `honest_did_from_result`）；IV（`effective_f_test` + `anderson_rubin_ci`）；RDD（`rdrobust` +
  `mccrary_test`）。
- **实验：**随机化推断 + `romano_wolf` 做多结果族错误率控制。
- **敏感性：**`oster_delta` / `sensemakr`。

正文报告**经济量级**，完整 battery 进附录；每个数字都能复现。端到端真跑示例见
[JF 执行 walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md)。若 StatsPAI/Stata 未连接，改用 `resources/code/` 并标注未验证数字。
## 自检清单

- [ ] 设计类型、各条件样本量、随机分配交代清楚
- [ ] 操纵做了预测试，正文有操纵检验且无混淆
- [ ] 有注意力检验与明确剔除标准（含稳健性）
- [ ] 报告效应量与功效/样本量依据，不只 p 值
- [ ] 机制用因果链或测量中介（Bootstrap），不止"显著差异"
- [ ] 讨论了生态效度 / 外部效度的局限

## 反模式

- 只报均值差异显著，不报效应量与功效
- 操纵无预测试、无操纵检验，自称"成功操纵"
- 事后随意剔除被试，不报标准与稳健性
- 把"组间差异显著"直接当成机制成立

## 评审质疑与补救

| 质疑 | 补救 |
|------|------|
| "学生被试能代表员工吗？" | 补在职样本重复实验，或论证目标构念在该人群同样被激活 |
| "操纵可能同时改变了别的构念" | 报告备择构念上的操纵检验差异不显著 |
| "只有显著性没有效应量" | 补 d / η²p 与敏感性功效分析 |
| "情境材料不像中国企业的真实场景" | 出示本土化改写过程与预测试真实感评分 |

## 输出格式

```
【设计】被试间/内/混合｜条件数 <…>｜各组 n <…>
【操纵】预测试□｜操纵检验：通过□ 无混淆□
【质控】注意力检验□｜剔除标准 <…>
【统计】效应量 <d/η²p>｜功效/样本量依据 <…>
【机制】因果链 / 测量中介(Boot CI) <…>
【下一步】nbr-china-context / nbr-discussion-contribution
```
