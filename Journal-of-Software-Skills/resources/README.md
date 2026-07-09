# 《软件学报》资源目录 (Journal of Software, JOS Resources)

面向《软件学报》(Journal of Software, JOS) 技能包的行动型资源。`skills/` 给出方法与判断；本
目录让智能体能够把一篇稿件按本刊（软件学科中文旗舰、CCF 推荐 A 类）的口径落地：对照范例、
核对官方格式、准备可复现材料、走通在线投稿与多轮修回。

## 目录内容

| 资源 | 用途 |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | 一篇虚构软件工程稿件的中文摘要+引言"改前→改后"示例，演示《软件学报》的写作弧线。示例为教学虚构，不含真实数据、不杜撰政策。 |
| [`exemplars/library.md`](exemplars/library.md) | 按"贡献形态×方法"组织的、经检索核实的《软件学报》真实论文对标表，附自检问题，并给出兄弟刊（计算机学报/自动化学报等）易混辨析。 |
| [`official-source-map.md`](official-source-map.md) | 给出可投稿建议前，核对本刊在线投稿、GB/T 7714 格式、审稿链、专刊机制、收录情况的官方与交叉来源，含 access-method note 与 待核实 清单。 |
| [`external_tools.md`](external_tools.md) | 官网、作者园地、CNKI/万方、CCF 目录、ChinaSoft 专刊等入口，以及网关被拦时的交叉核实渠道。 |
| [`code/README.md`](code/README.md) | 复现材料工具适配：证据—论点矩阵、代码/数据可用性核查、无依赖的目录冒烟检查脚本用法。 |

## 范围说明 (Scope Note)

这是一个**中文软件学科期刊**包，不是英文会议包，也不是经济学/机器学习包。请勿把
OpenReview/PMLR 那套会议机制或 Stata/DiD/IV 计量工具搬进来。《软件学报》的证据是软件学科的
证据：真实系统与数据集、可信基线、统计显著性与效应量、威胁有效性 (threats to validity) 的
论证，以及可检视的代码/数据材料，且需通过初审→外审→复审→主编终审的多轮中文同行评审。

## 建议路线

1. **动笔前**——用 [`../skills/jos-topic-selection`](../skills/jos-topic-selection/SKILL.md)
   判断稿件是否契合《软件学报》的软件学科定位（区别于《计算机学报》的全学科综合），
   再用 [`../skills/jos-writing-style`](../skills/jos-writing-style/SKILL.md) 搭中文写作骨架。
2. **做实验时**——把 [`../skills/jos-experiments`](../skills/jos-experiments/SKILL.md) 与
   [`../skills/jos-reproducibility`](../skills/jos-reproducibility/SKILL.md) 放在手边；
   威胁有效性要在设计期命名，代码/数据出处要在采集期锁定。
3. **对标与核对**——用 [`exemplars/library.md`](exemplars/library.md) 对标贡献形态，再用
   [`official-source-map.md`](official-source-map.md) 与 [`external_tools.md`](external_tools.md)
   核对当前投稿口径，最后进入
   [`../skills/jos-submission`](../skills/jos-submission/SKILL.md) 的在线投稿审计。
