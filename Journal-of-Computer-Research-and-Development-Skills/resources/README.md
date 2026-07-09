# 《计算机研究与发展》资源目录 (JCRD Resources)

面向《计算机研究与发展》(Journal of Computer Research and Development, JCRD) 技能包的行动型资源。
`skills/` 给方法，本目录让 agent 能把一篇稿件建模成 JCRD 形态、对照可核验样例做基准，并按本刊
**双盲评审**与**专题(special topic)组稿**的要求准备中文长文与可用的代码/数据材料。

## 目录内容

| 资源 | 用途 |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | 给投稿级建议前，确认本刊当期投稿须知、双盲规则、专题栏目、刊号与分级，并查看访问方式说明与 待核实 清单。 |
| [`external_tools.md`](external_tools.md) | 打开官网、投稿系统与 CCF/CNKI/万方交叉核对入口，以及 GB/T 7714 与中英文摘要工具、作者端核查清单。 |
| [`exemplars/library.md`](exemplars/library.md) | 对照 JCRD 的贡献形态（综述、体系结构、人工智能、安全、系统等）与姊妹刊（计算机学报、软件学报）辨析，并附自检问题。 |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | 看一份中文摘要与引言按 JCRD 弧线改写的 before→after（虚构示例，不杜撰政策）。 |
| [`code/README.md`](code/README.md) | 指向仓库共享的可复现材料工具，并给出 JCRD 专用（双盲、数据可用性）检查。 |

## 范围说明

这是**中文计算机综合期刊**包，其论文以**中文长文**发表、走**双盲多轮同行评审**，并常以**专题**
组织。请勿套用英文会议的 OpenReview/HotCRP 机制，也勿套用经济学期刊的 Stata/DiD 计量工具。JCRD 的
证据是计算机学科证据：真实系统与数据集、可信基线、充分实验或严谨综述，并配一份诚实的代码与数据
可用性说明，全程保持作者身份对外审匿名。

## 建议流程

1. 先用 [`../skills/jcrd-topic-selection`](../skills/jcrd-topic-selection/SKILL.md) 与
   [`../skills/jcrd-writing-style`](../skills/jcrd-writing-style/SKILL.md) 定位选题与栏目/专题 ——
   在动笔前判断投 JCRD 常规栏目还是**对口专题**，是最高杠杆动作。
2. 用 [`../skills/jcrd-experiments`](../skills/jcrd-experiments/SKILL.md) 与
   [`../skills/jcrd-reproducibility`](../skills/jcrd-reproducibility/SKILL.md) 及
   [`code/README.md`](code/README.md) 构建证据与可用性材料。
3. 对照 [`exemplars/library.md`](exemplars/library.md) 做基准，再用
   [`official-source-map.md`](official-source-map.md) 与 [`external_tools.md`](external_tools.md)
   确认当期规则，最后用 [`../skills/jcrd-submission`](../skills/jcrd-submission/SKILL.md) 做双盲
   投稿终审。
