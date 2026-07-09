# 资源目录 — 《中国科学：信息科学》(SSI)

面向《中国科学：信息科学》(Scientia Sinica Informationis, SSI) 技能包的行动型资源。
`skills/` 给出建议，本目录让智能体据此为一篇 SSI 形状的中文论文建模、对标已核实范例、
并按国家级大信息学科旗舰的三审三校流程准备可复现材料。

## 目录内容

| 资源 | 用途 |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | 查看一篇信息科学论文"引言 + 中英文摘要"的改写前后对照（虚构示例，不杜撰任何刊物政策）。 |
| [`exemplars/library.md`](exemplars/library.md) | 对标 SSI 的栏目形状（评述/论文/快报）与写作范式，避免与英文姊妹刊 SCIS 及兄弟刊混淆。 |
| [`official-source-map.md`](official-source-map.md) | 投稿前确认 SSI 当期栏目、投稿方式、版面费、审稿流程与中英文关系。 |
| [`external_tools.md`](external_tools.md) | 打开 SSI 官网、投稿系统、SciEngine、LaTeX 模板等官方入口与交叉核实 surface。 |
| [`code/README.md`](code/README.md) | 使用仓库共享的可复现材料工具：证据-论点矩阵、可用性自查、依赖无关的打包 smoke 检查。 |

## 范围说明

这是一本**中文信息科学综合旗舰**期刊包：《中国科学：信息科学》(SSI) 覆盖计算机、控制、
通信、电子/微电子等大信息学科，以**重大原创与综述（评述）**为主，定位高。因此：

- 不要套用英文 ML 会议的 OpenReview/PMLR 机制，也不要套用经济学期刊的 DiD/IV/RDD 计量套件。
- SSI 的"证据"是信息科学证据：清晰的问题动机、可靠的实验或理论依据、公平的对比、
  以及对创新高度与科学价值的论证，并经三审三校把关。
- 中文写作规范（中英文双语摘要、关键词、参考文献著录、量与单位）与投稿系统 LaTeX 排版是硬约束。

## 建议流程

1. 先用 [`../skills/ssi-topic-selection`](../skills/ssi-topic-selection/SKILL.md) 与
   [`../skills/ssi-writing-style`](../skills/ssi-writing-style/SKILL.md) 定栏目、定语言、定框架
   ——在动笔前判断该投 SSI（还是英文 SCIS，或计算机学报/自动化学报等兄弟刊）是最高杠杆的决定。
2. 用 [`../skills/ssi-experiments`](../skills/ssi-experiments/SKILL.md) 与
   [`../skills/ssi-reproducibility`](../skills/ssi-reproducibility/SKILL.md) 及
   [`code/README.md`](code/README.md) 建立证据与可复现材料。
3. 对标 [`exemplars/library.md`](exemplars/library.md)，再用
   [`official-source-map.md`](official-source-map.md) 与
   [`external_tools.md`](external_tools.md) 确认当期政策，最后用
   [`../skills/ssi-submission`](../skills/ssi-submission/SKILL.md) 做投稿前审计。
