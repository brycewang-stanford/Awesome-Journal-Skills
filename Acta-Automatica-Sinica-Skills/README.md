# 《自动化学报》技能包 · Acta Automatica Sinica (AAS) Skills

> English readers: this is a Chinese-language pack. A fuller Chinese guide is in
> [`README.zh-CN.md`](README.zh-CN.md).

面向**《自动化学报》(Acta Automatica Sinica, AAS)** 投稿的 12 个中文 agent 技能。
《自动化学报》是由**中国自动化学会与中国科学院自动化研究所**共同主办、中国科学院主管、创刊于
**1963 年**（前身《自动化》）的**控制与自动化学科中文旗舰月刊**，聚焦控制理论与控制工程、模式
识别与智能系统、机器人、人工智能在自动化中的应用，有**中英文双语与综述长文传统**，实行**双盲
三审制**与多轮退修。本包覆盖一次 AAS 投稿的完整弧线：判断选题是否契合本刊控制/自动化定位、把
中文长文写到符合体例、搭建经得起外审的实验与理论证据、按官方口径完成在线投稿、应对多轮退修，
直到录用定稿与见刊。

官方依据核验日期：**2026-07-09**。已通过官网 `aas.net.cn`、CNKI 期刊主页与 CCF / 中国自动化学会
期刊目录**双源交叉核实**关键事实；核验环境对官网直接抓取受限，故通过搜索引擎渲染阅读并与
CNKI/万方/维普及 ISSN 门户交叉核对，完整记录（含全部 **待核实** 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。凡未双源确认的影响因子、
版面费、审稿周期、主编等一律标 **待核实**，本包不杜撰。

> 名称辨析：本刊《自动化学报》英文作 Acta Automatica Sinica (AAS)，是**中文刊**（投审稿系统
> `mc03.manuscriptcentral.com/aas-cn`）；与中国自动化学会主办、2014 年创刊的**英文刊**
> 《IEEE/CAA Journal of Automatica Sinica (JAS)》是**不同期刊**，请勿混淆。

## 本刊相对兄弟中文刊的特色

- **控制与自动化学科导向**：聚焦控制理论与控制工程、模式识别与智能系统、机器人、人工智能在
  自动化中的应用，学科侧重是**控制/智能**而非计算导向，区别于计算全学科的《计算机学报》、偏
  软件的《软件学报》、偏电子通信的《电子学报》与《计算机研究与发展》《计算机科学》。
- **中英文双语 + 综述长文传统**：栏目分**综述、论文、短文**；报道性中英文摘要并重，综述稿有
  专门体例。
- **双盲三审制**：投稿前须彻底删除作者信息；编辑初审 → 双盲外审 → 退修/复审 → 主编终审。
- **作者承诺前置**：全部作者签名 + 第一作者单位公章的《作者承诺》须与稿件同时提交，**收到后
  才初审**。
- **原创与署名红线**：不接受翻译稿、非一稿多投；**不接收将 AI 工具作为署名作者**的稿件。
- **对作者的稿酬**：见刊后赠样刊 2 本、3 个月内一次性支付稿酬（版面费是否收取 **待核实**）。

## 12 个技能

| 技能 | 作用 |
|---|---|
| [`aas-topic-selection`](skills/aas-topic-selection/SKILL.md) | 判断选题是否契合本刊控制/自动化定位、与兄弟刊分工、选栏目 |
| [`aas-workflow`](skills/aas-workflow/SKILL.md) | 从选题到见刊的全流程时间线与技能编排 |
| [`aas-writing-style`](skills/aas-writing-style/SKILL.md) | 中文长文体例：中英文摘要、关键词、中图分类号、GB/T 7714 |
| [`aas-related-work`](skills/aas-related-work/SKILL.md) | delta 优先的相关工作与文献综述，确立创新性 |
| [`aas-experiments`](skills/aas-experiments/SKILL.md) | 实验/仿真设计与呈现：RQ、公平基线、稳定性分析、消融 |
| [`aas-reproducibility`](skills/aas-reproducibility/SKILL.md) | 可复现性：环境/种子/数据固定、污染防范、复现包 |
| [`aas-supplementary`](skills/aas-supplementary/SKILL.md) | 按"决定性"划分正文与附录/补充材料 |
| [`aas-submission`](skills/aas-submission/SKILL.md) | 投稿就绪审计：匿名化、作者承诺、查重、退稿风险分诊 |
| [`aas-review-process`](skills/aas-review-process/SKILL.md) | 双盲三审制流程建模与各环节作者杠杆 |
| [`aas-author-response`](skills/aas-author-response/SKILL.md) | 审稿意见逐条答复与退修说明 |
| [`aas-artifact-evaluation`](skills/aas-artifact-evaluation/SKILL.md) | 代码与数据可用性（讲清本刊无独立徽章制度的现状与做法） |
| [`aas-camera-ready`](skills/aas-camera-ready/SKILL.md) | 录用后定稿、校样、稿酬与出版排期 |

## 资源

| 路径 | 内容 |
|---|---|
| [`resources/official-source-map.md`](resources/official-source-map.md) | 官方与交叉来源、访问方式说明、已核验事实与全部 **待核实** 项 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官网/投审稿系统/学会目录入口与作者侧自查工具 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 如何自行挑选与核验本刊范文（不杜撰篇目属性） |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构示例：中文摘要 + 引言"改前→改后" |
| [`resources/code/README.md`](resources/code/README.md) | 复现包与查重/匿名化自查思路 |

## 许可

MIT License · Copyright (c) 2026 Bryce Wang。详见 [`LICENSE`](LICENSE)。
