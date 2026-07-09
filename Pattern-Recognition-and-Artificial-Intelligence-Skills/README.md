# 《模式识别与人工智能》技能包 · Pattern Recognition and Artificial Intelligence (PR&AI) Skills

> English readers: this is a Chinese-language pack. A fuller Chinese guide is in
> [`README.zh-CN.md`](README.zh-CN.md).

面向**《模式识别与人工智能》(Pattern Recognition and Artificial Intelligence, PR&AI)** 投稿的
12 个中文 agent 技能。《模式识别与人工智能》是由**中国自动化学会、国家智能计算机研究开发中心、
中国科学院合肥智能机械研究所**共同主办、**科学出版社**出版、创刊于 **1989 年**的
**CCF 推荐 B 类模式识别/人工智能专业中文月刊**，专注模式识别 (Pattern Recognition)、人工智能
(Artificial Intelligence)、机器学习、计算机视觉、自然语言处理与智能系统等 AI 细分方向，以高水平
原创**长文**(18000~44000 字)为主，实行编辑初审→专家外审→主编终审的同行评审与多轮修回。本包覆盖
一次 PR&AI 投稿的完整弧线：判断选题是否契合本刊 AI 细分定位、把中文长文写到符合体例、搭建经得起
外审的模式识别/机器学习实证证据、按官方口径完成投稿、应对多轮修回，直到录用定稿与见刊。

官方依据核验日期：**2026-07-09**。已通过官方投稿系统 `manu46.magtech.com.cn/Jweb_prai`、备用官网
`prai.hfcas.ac.cn`、CNKI 期刊主页与 CCF 推荐中文科技期刊目录**双源交叉核实**关键事实；核验环境对
官网直接抓取返回 403，故通过搜索引擎渲染阅读并与 CNKI/CCF 目录交叉核对，完整记录（含全部 **待核实**
项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。凡未双源确认的影响
因子、版面费、审稿周期、主编等一律标 **待核实**，本包不杜撰。

> 名称辨析：本刊《模式识别与人工智能》英文作 Pattern Recognition and Artificial Intelligence
> (PR&AI)，与 Elsevier 的英文期刊 *Pattern Recognition* 及 *IEEE TPAMI* 是**不同期刊**，请勿混淆。

## 本刊相对兄弟中文刊的特色

- **AI 细分方向专业刊**：聚焦模式识别、机器学习、计算机视觉、自然语言处理、智能系统，比综合性的
  《计算机学报》(全学科) 更聚焦 AI，与《自动化学报》(控制为主)、《软件学报》(系统软件)、
  《电子学报》(电子通信) 的学科侧重明显不同。
- **合肥编辑部 + 玛格泰克投稿系统**：编辑部设于中国科学院合肥智能机械研究所，投稿走
  `manu46.magtech.com.cn/Jweb_prai` 的"作者中心"。
- **长文体例**：全文 **18000~44000 字**（含图表），给足空间把方法、模型与实验讲透。
- **同行评审 + 6 个月周期口径**：编辑初审→专家外审→主编终审；官方口径一般 **6 个月内**给评审
  结果，超期作者可通知编辑部后自行处理。
- **中文科技规范**：报道性中文摘要(约 200 字)+English Abstract(约 200 词)、中英文关键词(3~5)、
  中图分类号(TP)、参考文献 **GB/T 7714** 且中文文献中英文对照。
- **学术规范红线**：编辑部对稿件做**重复率检测**，未通过退回作者；要求成果具创新性学术价值。

## 12 个技能

| 技能 | 作用 |
|---|---|
| [`prai-topic-selection`](skills/prai-topic-selection/SKILL.md) | 判断选题是否契合本刊 AI 细分定位、与兄弟刊分工、选稿件类型 |
| [`prai-workflow`](skills/prai-workflow/SKILL.md) | 从选题到见刊的全流程时间线与技能编排 |
| [`prai-writing-style`](skills/prai-writing-style/SKILL.md) | 中文长文体例：中英文摘要、关键词、中图分类号、GB/T 7714 |
| [`prai-related-work`](skills/prai-related-work/SKILL.md) | delta 优先的相关工作与文献综述，确立创新性 |
| [`prai-experiments`](skills/prai-experiments/SKILL.md) | 实验设计与呈现：RQ、公平基线、统计严谨、消融 |
| [`prai-reproducibility`](skills/prai-reproducibility/SKILL.md) | 可复现性：环境/种子/数据固定、污染防范、复现包 |
| [`prai-supplementary`](skills/prai-supplementary/SKILL.md) | 按"决定性"划分正文与附录/补充材料 |
| [`prai-submission`](skills/prai-submission/SKILL.md) | 投稿就绪审计：模板、六件套、查重、字数、退稿风险分诊 |
| [`prai-review-process`](skills/prai-review-process/SKILL.md) | 同行评审流程建模与各环节作者杠杆 |
| [`prai-author-response`](skills/prai-author-response/SKILL.md) | 审稿意见逐条答复与修回说明 |
| [`prai-artifact-evaluation`](skills/prai-artifact-evaluation/SKILL.md) | 代码与数据可用性（讲清本刊现状与做法） |
| [`prai-camera-ready`](skills/prai-camera-ready/SKILL.md) | 录用后定稿、校样、缴费与出版排期 |

## 资源

| 路径 | 内容 |
|---|---|
| [`resources/official-source-map.md`](resources/official-source-map.md) | 官方与交叉来源、访问方式说明、已核验事实与全部 **待核实** 项 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官网/投稿系统/CCF 目录入口与作者侧自查工具 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 如何自行挑选与核验本刊范文（不杜撰篇目属性） |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构示例：中文摘要+引言"改前→改后" |
| [`resources/code/README.md`](resources/code/README.md) | 复现包与查重/匿名化自查思路 |

## 许可

MIT License · Copyright (c) 2026 Bryce Wang。事实性内容以官网当期《投稿指南》为准，标 **待核实**
者不作定论。
