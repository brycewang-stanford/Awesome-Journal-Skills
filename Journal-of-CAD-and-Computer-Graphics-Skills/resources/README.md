# 资源目录 — 《计算机辅助设计与图形学学报》(Journal of Computer-Aided Design & Computer Graphics, JCAD&CG)

本目录为面向《计算机辅助设计与图形学学报》(Journal of Computer-Aided Design & Computer
Graphics, JCAD&CG) 的技能提供支撑材料：帮助作者按图形学/CAD 的对照范式打磨稿件、按官方
口径核实事实、并准备好经得起外审的图形与几何支撑材料。

## 目录内容

| 资源 | 用途 |
|---|---|
| [`official-source-map.md`](official-source-map.md) | 核实本刊投稿系统、审稿流程、栏目、格式与周期等事实的官方与交叉来源，含访问方式说明与全部 **待核实** 项 |
| [`external_tools.md`](external_tools.md) | 官网/投稿系统/CCF 目录等入口，以及查重、GB/T 7714、图形结果呈现、演示视频、匿名化、可复现的作者侧自查工具 |
| [`exemplars/library.md`](exemplars/library.md) | 如何为本刊挑选与核验图形学/CAD 范文（只给方法与定位，不杜撰具体篇目属性） |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | 一份虚构图形学示例论文的中文摘要与引言"改前→改后"，示范本刊首页范式 |
| [`code/README.md`](code/README.md) | 复现包与查重/匿名化脚本思路，衔接可复现性与制品技能 |

## 范围说明

本包面向**中文图形学/CAD 方向期刊**，不是英文会议包，也不是经济学/统计的计量工具包。请勿把
OpenReview/PMLR 机制或 Stata/DiD/IV 计量套件搬进来。JCAD&CG 的证据是计算机图形学与计算机
辅助设计的证据：几何精度、渲染质量、可视化有效性、用户研究与主客观评测，经由同行评议与
多轮修回的中文论文评审。

## 建议使用顺序

1. **选题与写作**：先用 [`../skills/jcadcg-topic-selection`](../skills/jcadcg-topic-selection/SKILL.md)
   判契合，再用 [`../skills/jcadcg-writing-style`](../skills/jcadcg-writing-style/SKILL.md) 搭骨架。
2. **搭建证据**：用 [`../skills/jcadcg-experiments`](../skills/jcadcg-experiments/SKILL.md) 与
   [`../skills/jcadcg-reproducibility`](../skills/jcadcg-reproducibility/SKILL.md)，并参考
   [`code/README.md`](code/README.md)。
3. **核实与投稿**：对照 [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md)，
   在 [`official-source-map.md`](official-source-map.md) 与 [`external_tools.md`](external_tools.md)
   核实当期口径后，用 [`../skills/jcadcg-submission`](../skills/jcadcg-submission/SKILL.md) 做投稿自审。
