---
name: ceq-workflow
description: Use when deciding which ceq-* sub-skill to invoke next, or when sequencing manuscript work from fit judgment through rebuttal for 《经济学(季刊)》 (China Economic Quarterly, CEQ). Routes — does not replace — the specialized skills.
---

# 《经济学(季刊)》工作流（ceq-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 ceq-* skill**。

默认假设：目标是国内最贴近国际主流范式的中文刊 CEQ（北大 CCER/NSD 主办，2001 年创办，2021 年起全年六期）。衡量标准是**可信识别 + 国际可对话**，方法规范性要求在国内经济学刊中最高。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能冲 CEQ / 下一步做什么"
- 手头有实证结果但识别策略立不住
- 学科或方法对口性摇摆（该投 CEQ 还是经济研究）
- 收到 R&R 外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定够不够格、对不对口 CEQ | `ceq-fit-positioning` |
| 选题模糊 / 只有相关性 / 国际同行看不懂贡献 | `ceq-topic-selection` |
| 文献只堆近年国内回归、没对标具体 field 文献 | `ceq-literature-review` |
| 实证仅 OLS+控制 / 识别策略不过关 | `ceq-identification` |
| DID 用 TWFE 跑交错处理，未回应异质性批评 | `ceq-modern-did` |
| 聚类层级没理由 / 弱工具 / 多重检验未校正 | `ceq-inference` |
| 主结果有了但没机制证据 | `ceq-mechanism` |
| 全用表、没事件研究图 / 拟合图 | `ceq-figures` |
| 英文摘要质量差 / 贡献是套话 | `ceq-abstract-english` |
| 准备投稿，需要体例与系统 checklist | `ceq-submission` |
| 收到 R&R，需要写回复 | `ceq-rebuttal` |

## 默认顺序

1. `ceq-fit-positioning` — 先判断匹配度，识别立不住别投
2. `ceq-topic-selection` — 把干净因果/可建模/国际可对话的问题定下来
3. `ceq-literature-review` — 对标具体 field 文献定位贡献（中英并重）
4. `ceq-identification` — 结构或准实验，识别假设显式化
5. `ceq-modern-did` — 若用 DID，过现代交错/异质性合规
6. `ceq-inference` — 聚类、弱工具、多重检验、标准误
7. `ceq-mechanism` — 机制渠道证据
8. `ceq-figures` — 事件研究/拟合图最终化（图优于表）
9. `ceq-abstract-english` — 英文摘要 + 对标 field 的贡献陈述
10. `ceq-submission` — 投稿前 preflight（夹注体例、JEL、系统、匿名）
11. `ceq-rebuttal` — 外审后

> `ceq-abstract-english` 与 `ceq-figures` 是**后段定稿阶段**触发，识别未立住前不要做。

## 决策口诀

- "我只有相关性" → `ceq-topic-selection` / `ceq-identification`（不解决因果别投）
- "DID 是 TWFE 跑交错处理" → `ceq-modern-did`
- "审稿人会挑标准误" → `ceq-inference`
- "贡献写成'丰富了研究'" → `ceq-literature-review` + `ceq-abstract-english`

## 与本仓库其它期刊包的差异

- **理论贡献厚但识别一般** → 转 economic-research（《经济研究》）
- **偏产业政策实证** → 转 china-industrial-economics（《中国工业经济》）
- **偏金融/资产定价/银行** → 转 journal-of-financial-research（《金融研究》）
- **偏开放宏观/国际贸易** → 转 journal-of-world-economy（《世界经济》）
- CEQ 要的是**国际可对话的干净识别**，技术规范权重最高、政策口号最不吃香

## 阶段症状 → Skill 路由（决策树）

下面把"当前最痛的一句话症状"映射到唯一下一步，避免在并行 skill 间打转。本路由依据 CEQ 的偏好排序：识别与可对话性优先于写作与体例。

```
START
 ├─ 不确定该不该投 CEQ ───────────────► ceq-fit-positioning
 ├─ 只有相关性 / 选题看不出贡献 ──────► ceq-topic-selection
 ├─ 贡献是"丰富/填补"套话 ───────────► ceq-literature-review
 ├─ 实证仅 OLS+控制 / 识别立不住 ────► ceq-identification
 │    └─ 用 DID 且处理交错 ──────────► ceq-modern-did
 │    └─ 聚类/弱工具/多重检验存疑 ───► ceq-inference
 ├─ 主效应干净但机制是断言 ──────────► ceq-mechanism
 ├─ 全用表、无事件研究/拟合图 ───────► ceq-figures
 ├─ 英文摘要中式/贡献空话 ───────────► ceq-abstract-english
 ├─ 准备投稿、要体例与系统核对 ──────► ceq-submission
 └─ 收到 R&R 外审意见 ───────────────► ceq-rebuttal
RULE: 识别未立住前，不要分叉去 ceq-figures / ceq-abstract-english。
```

## 一稿到底的串联示例（CEQ 视角）

虚构稿件《碳交易试点与企业减排》从无到投的 skill 串联，演示路由如何随阶段推进（示意，非真实评审）：

```
週次  阶段症状                          调用 skill            产出
W1   "这能冲 CEQ 吗？"                 ceq-fit-positioning   两高一中→可冲，先补识别
W1   "选题像政策评估"                  ceq-topic-selection   重塑为"碳定价→技术替代"机制问
W2   "综述堆国内回归"                  ceq-literature-review 对标 3 篇 field，写差异段
W2   "试点外生吗"                      ceq-identification    分批+门槛，三条假设成文
W3   "交错处理用了 TWFE"               ceq-modern-did        CS/SA 重估，Bacon 分解
W3   "省级处理却企业聚类"              ceq-inference         省级聚类+wild bootstrap
W4   "机制只有中介回归"                ceq-mechanism         排除法+预设异质性
W4   "主结果全是表"                    ceq-figures           事件研究图+剂量反应图
W5   "英文摘要直译超词"                ceq-abstract-english  五句法压到 ~95 词
W5   "投前核体例"                      ceq-submission        夹注/JEL/匿名 preflight
后续 "收到 R&R"                        ceq-rebuttal          逐条三段式，指页码补证
```

## 反模式

- **不要**跳过 `ceq-fit-positioning` 就动笔——它最常救稿（避免硬投）
- **不要**在识别未立住时去抠英文摘要和图
- **不要**让 `ceq-rebuttal` 在正文未修订前生成回复
- **不要**在 `ceq-modern-did` 与 `ceq-inference` 间反复横跳——先定估计量，再配套标准误
