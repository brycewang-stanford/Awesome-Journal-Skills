---
name: ceq-modern-did
description: Use when a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript uses difference-in-differences with staggered adoption or heterogeneous treatment effects — to bring it into compliance with modern estimators (Callaway–Sant'Anna, de Chaisemartin–D'Haultfœuille, Sun–Abraham) instead of bare two-way fixed effects. Bare TWFE on staggered timing is a near-certain reject at CEQ.
---

# 现代 DID 合规（ceq-modern-did）

## 触发时机

- 处理时点**交错**（不同单位不同时间被处理），但只跑了 TWFE
- 处理效应可能随队列/时间**异质**
- 审稿人提"负权重 / 坏比较 / 前置效应"等批评

## 核心判断：你的 DID 是哪一类？

| 情形 | 是否有 TWFE 偏误 | 处理 |
|------|------------------|------|
| 单一时点、两组 | 通常无 | 标准 DID 即可，仍画事件研究图 |
| 交错处理 + 同质效应 | 轻 | 仍建议稳健估计量交叉验证 |
| 交错处理 + 异质效应 | **严重（负权重）** | **必须**用现代估计量 |
| 连续/强度处理 | 视情形 | 用 de Chaisemartin–D'Haultfœuille 等专用估计量 |

## 必做四步（交错处理）

1. **诊断**：Goodman-Bacon 分解，报告"坏比较"（already-treated 作对照）的权重；或 de Chaisemartin–D'Haultfœuille 负权重诊断。
2. **现代估计量**（至少一种，建议交叉验证两种）：
   - Callaway–Sant'Anna（`csdid` / `did`）：分组-时间 ATT 聚合
   - de Chaisemartin–D'Haultfœuille（`did_multiplegt(dyn)`）：适配连续/可逆处理
   - Sun–Abraham（`eventstudyinteract`）：交互加权事件研究
3. **事件研究图**：用上述估计量画动态效应（见 `ceq-figures`），而非 TWFE 的污染系数。
4. **对照报告**：TWFE 与现代估计量并列，说明差异来源。

## 易踩坑

- 用 TWFE 事件研究图当"平行趋势成立"——其前置系数本身被污染
- 把 not-yet-treated 与 already-treated 混作对照而不说明
- 连续处理直接套 Callaway–Sant'Anna（其默认针对二元吸收处理）
- 只报现代估计量的点估计，不报其聚合方式与对照组定义

## 自检清单

- [ ] 已诊断是否交错 + 是否异质（决定要不要现代估计量）
- [ ] 至少一种现代估计量；建议两种交叉验证
- [ ] 事件研究图来自现代估计量，前置系数近零
- [ ] 报告了对照组定义（never/not-yet-treated）与聚合权重
- [ ] TWFE 与现代估计量并列，差异有解释
- [ ] 连续/可逆处理用了适配的估计量

## 反模式

- 裸 TWFE 跑交错处理直接声称因果（CEQ 退稿高发）
- 不做负权重/坏比较诊断
- "我们也跑了 Callaway-Sant'Anna，结果稳健"但不展示、不解释

## 现代 DID 合规对照表（症状→估计量→必报项）

下表把交错 DID 的常见症状映射到本刊期待的估计量与必须报告的内容。CEQ 对此把关在国内刊中最严：裸 TWFE 跑交错+异质处理几乎是确定退稿。具体口径以编辑部最新稿约与外审为准。

| 数据症状 | 本刊期待估计量 | 必报项 |
|----------|----------------|--------|
| 二元吸收处理、交错 | Callaway–Sant'Anna | never/not-yet 对照定义、聚合权重 |
| 连续/强度处理 | de Chaisemartin–D'Haultfœuille | 平均/动态效应、负权重诊断 |
| 想要干净事件研究 | Sun–Abraham | 参照期、前置联合检验 |
| 怀疑平行趋势 | + honest-DID 敏感性 | 违背可容忍范围下结论是否变 |
| 需说服审稿人偏误来源 | + Goodman-Bacon 分解 | 坏比较权重占比 |

## 微型走查：TWFE 与现代估计量并列

虚构稿件《排污权交易试点与企业绿色专利》，处理交错（试点分批），效应大概率随队列异质。初稿只跑 TWFE。按本 skill 的四步走一遍（示意数字）：

```
① 诊断（Goodman-Bacon 分解）：
   "坏比较"（already-treated 作对照）权重占 31% → 不可忽视
② 现代估计量交叉验证：
   TWFE 事件研究：前置系数 t=-3..-1 显著为负（疑似偏误污染）
   Callaway–Sant'Anna：前置 [-0.01,0.02] 跨 0（平行趋势可视）
   Sun–Abraham：与 CS 一致，处理后 t=+2 约 +0.08
③ 事件研究图：用 CS/SA 系数画，前置近零、处理后单调
④ 对照报告：TWFE β=+0.045，CS β=+0.079
   差异来自坏比较稀释 → 说明 TWFE 低估
honest-DID：允许前置斜率违背至 1.5×最大前置偏差，效应仍 >0
```

走查要点：TWFE 与 CS 系数差一截（0.045 vs 0.079），且 Bacon 分解显示 31% 权重来自坏比较——这就是"必须用现代估计量"的实证理由，而非走过场。把对照写进正文，比只说"稳健"有说服力得多。

## 审稿人追问模式与修法

- "TWFE 跑交错，你处理负权重了吗？"——修法：报 Bacon 分解坏比较权重，并用 CS/dCDH 重估、并列对照。
- "你的平行趋势就靠 TWFE 前置系数？那本身被污染了"——修法：改用现代估计量的前置系数，并补前置联合检验。
- "前置看着不平，结论稳吗？"——修法：上 honest-DID，报告在合理违背范围内结论是否翻转（与 `ceq-inference` 的稳健推断衔接）。

## 输出格式

```
【处理结构】单时点 / 交错 / 连续
【异质性风险】低 / 高（是否需现代估计量）
【诊断】Bacon 分解 / 负权重 已做 □
【现代估计量】CS □ dCDH □ SA □（用了哪些）
【事件研究图】来自现代估计量 □
【缺口】<待补>
【下一步】ceq-inference
```
