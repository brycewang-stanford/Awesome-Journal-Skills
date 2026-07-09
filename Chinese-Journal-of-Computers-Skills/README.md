# 《计算机学报》技能包 · Chinese Journal of Computers (CJC) Skills

> English readers: this is a Chinese-language pack. A fuller Chinese guide is in
> [`README.zh-CN.md`](README.zh-CN.md).

面向**《计算机学报》(Chinese Journal of Computers, CJC)** 投稿的 12 个中文 agent 技能。
《计算机学报》是由中国计算机学会(CCF)与中国科学院计算技术研究所主办、创刊于 1978 年的
**CCF A 类计算机学科综合性中文旗舰月刊**，以高水平原创**长文**为主，实行编辑初审→专家外审→
复审退修→主编终审的**三审制**与多轮修回。本包覆盖一次 CJC 投稿的完整弧线：判断选题是否契合本刊
综合定位、把中文长文写到符合体例、搭建经得起外审的实证证据、按官方口径完成投稿、应对多轮修回，
直到录用定稿与见刊。

官方依据核验日期：**2026-07-09**。已通过官网 `cjc.ict.ac.cn`、CNKI 期刊主页与 CCF 推荐中文科技
期刊目录**双源交叉核实**关键事实；核验环境对官网直接抓取返回 403，故通过搜索引擎渲染阅读并与
CNKI/CCF 目录交叉核对，完整记录（含全部 **待核实** 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。凡未双源确认的影响因子、
版面费、审稿周期、主编等一律标 **待核实**，本包不杜撰。

> 名称辨析：本刊《计算机学报》英文作 Chinese Journal of Computers (CJC)，与中科院计算所主办的
> 英文刊《计算机科学技术学报》(Journal of Computer Science and Technology, JCST) 是**不同期刊**，
> 请勿混淆。

## 本刊相对兄弟中文刊的特色

- **计算机全学科综合性**：覆盖理论、体系结构、软件、人工智能、数据库、网络、多媒体、图形学等，
  区别于偏软件工程/系统软件的《软件学报》、偏控制的《自动化学报》、偏电子通信的《电子学报》。
- **原创长文传统**：以完整、充分的原创研究长文为主，给足空间把方法、理论、系统与实验讲透。
- **三审制 + 多轮修回**：编辑初审→专家外审(2~3 名，双盲，约 20 天/轮)→复审退修(大修常重新送审)
  →主编终审(每月)；第 1 轮审理约 3~4 个月（经验值）。
- **中文科技规范**：报道性中英文摘要、中英文关键词、中图分类号(TP)、参考文献 **GB/T 7714** 且
  中文文献中英文对照、量与单位用法定计量单位。
- **学术规范红线**：学术不端总文字复制比**超过 30%** 初审退稿；一稿多投明确禁止。

## 12 个技能

| 技能 | 作用 |
|---|---|
| [`cjc-topic-selection`](skills/cjc-topic-selection/SKILL.md) | 判断选题是否契合本刊综合定位、与兄弟刊分工、选稿件类型 |
| [`cjc-workflow`](skills/cjc-workflow/SKILL.md) | 从选题到见刊的全流程时间线与技能编排 |
| [`cjc-writing-style`](skills/cjc-writing-style/SKILL.md) | 中文长文体例：中英文摘要、关键词、中图分类号、GB/T 7714 |
| [`cjc-related-work`](skills/cjc-related-work/SKILL.md) | delta 优先的相关工作与文献综述，确立创新性 |
| [`cjc-experiments`](skills/cjc-experiments/SKILL.md) | 实验设计与呈现：RQ、公平基线、统计严谨、消融 |
| [`cjc-reproducibility`](skills/cjc-reproducibility/SKILL.md) | 可复现性：环境/种子/数据固定、污染防范、复现包 |
| [`cjc-supplementary`](skills/cjc-supplementary/SKILL.md) | 按"决定性"划分正文与附录/补充材料 |
| [`cjc-submission`](skills/cjc-submission/SKILL.md) | 投稿就绪审计：模板、六件套、查重、匿名、退稿风险分诊 |
| [`cjc-review-process`](skills/cjc-review-process/SKILL.md) | 三审制流程建模与各环节作者杠杆 |
| [`cjc-author-response`](skills/cjc-author-response/SKILL.md) | 审稿意见逐条答复与修回说明 |
| [`cjc-artifact-evaluation`](skills/cjc-artifact-evaluation/SKILL.md) | 代码与数据可用性（讲清本刊无独立徽章制度的现状与做法） |
| [`cjc-camera-ready`](skills/cjc-camera-ready/SKILL.md) | 录用后定稿、校样、缴费与出版排期 |

## 资源

| 路径 | 内容 |
|---|---|
| [`resources/official-source-map.md`](resources/official-source-map.md) | 官方与交叉来源、访问方式说明、已核验事实与全部 **待核实** 项 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官网/投稿系统/CCF 目录入口与作者侧自查工具 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 如何自行挑选与核验本刊范文（不杜撰篇目属性） |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构示例：中文摘要+引言"改前→改后" |
| [`resources/code/README.md`](resources/code/README.md) | 复现包与查重/匿名化自查思路 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./Chinese-Journal-of-Computers-Skills
claude plugin install cjc-skills
```

也可直接使用：每个 `skills/cjc-*/SKILL.md` 都是独立指令文件，其 frontmatter 的 `description`
告诉 agent 何时触发。典型调用：

- "这篇工作适合投《计算机学报》还是软件学报？" → `cjc-topic-selection`
- "按本刊投稿须知审一下我的稿件" → `cjc-submission`
- "收到退修意见，帮我写答复信" → `cjc-author-response`
- "稿件录用了，接下来定稿要注意什么" → `cjc-camera-ready`

## 事实纪律

本包区分三类陈述：**已核验事实**（可双源追溯，如三审制、GB/T 7714、30% 查重红线）、**报告值**
（仅二手来源，如审理费 150 元、影响因子数值——引用前须核实）、**待核实项**（版面费、录用率、
主编等——不以确定口径写入结论）。给投稿级建议前，务必回到官网当期《投稿须知》核对易变项。

## 许可

MIT，见 [`LICENSE`](LICENSE)。中文说明见 [`README.zh-CN.md`](README.zh-CN.md)。
