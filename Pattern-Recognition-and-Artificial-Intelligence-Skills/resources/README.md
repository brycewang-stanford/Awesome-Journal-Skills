# 资源目录 — 《模式识别与人工智能》(Pattern Recognition and Artificial Intelligence, PR&AI) 技能包

本目录为《模式识别与人工智能》(Pattern Recognition and Artificial Intelligence, PR&AI) 中文投稿
技能包提供可操作的配套资源。`skills/` 给出方法与判断，本目录帮助 agent 把一篇模式识别/人工智能
方向的中文原创长文对照范式打磨、按官方口径核实事实、并准备好经得起初审→外审→终审的支撑材料。

## 目录内容

| 资源 | 用途 |
|---|---|
| [`official-source-map.md`](official-source-map.md) | 核实本刊投稿系统、审稿流程、格式与周期等事实的官方与交叉来源，含访问方式说明与全部 **待核实** 项 |
| [`external_tools.md`](external_tools.md) | 官网/投稿系统/CCF 目录等入口，以及查重、GB/T 7714、匿名化、可复现的作者侧自查工具 |
| [`exemplars/library.md`](exemplars/library.md) | 如何为本刊挑选与核验范文（只给方法与定位，不杜撰具体篇目属性） |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | 一份虚构示例论文的中文摘要与引言"改前→改后"，示范本刊长文首页范式 |
| [`code/README.md`](code/README.md) | 复现包与查重/匿名化脚本思路，衔接可复现性与制品技能 |

## 范围说明

本包面向**模式识别与人工智能方向的中文专业期刊**，不是英文会议包，也不是经济学/统计的计量工具包。
请勿把 OpenReview/PMLR 机制或 Stata/DiD/IV 计量套件搬进来。PR&AI 的证据是模式识别与机器学习学科的
实证证据：可信实验、公平基线、统计严谨、可复现制品，经由初审→外审→终审的中文长文评审。它比综合性
计算机刊更聚焦 AI 细分方向（Pattern Recognition / Artificial Intelligence / 机器学习 / 计算机视觉
/ 自然语言处理 / 智能系统）。

## 建议使用顺序

1. **选题与写作**：先用 [`../skills/prai-topic-selection`](../skills/prai-topic-selection/SKILL.md)
   判契合，再用 [`../skills/prai-writing-style`](../skills/prai-writing-style/SKILL.md) 搭长文骨架。
2. **搭建证据**：用 [`../skills/prai-experiments`](../skills/prai-experiments/SKILL.md) 与
   [`../skills/prai-reproducibility`](../skills/prai-reproducibility/SKILL.md)，并参考
   [`code/README.md`](code/README.md)。
3. **核实与投稿**：对照 [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)，
   在 [`official-source-map.md`](official-source-map.md) 与 [`external_tools.md`](external_tools.md)
   核实当期口径后，用 [`../skills/prai-submission`](../skills/prai-submission/SKILL.md) 做投稿自审。
