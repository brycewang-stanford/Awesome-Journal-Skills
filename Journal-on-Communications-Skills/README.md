# 《通信学报》技能包 · Journal on Communications (JOC) Skills

> English readers: this is a Chinese-language pack for **《通信学报》(Journal on
> Communications, JOC)**. A fuller Chinese guide is in
> [`README.zh-CN.md`](README.zh-CN.md).

面向**《通信学报》(Journal on Communications, JOC)** 投稿的 12 个中文 agent 技能。
《通信学报》是由中国科学技术协会主管、**中国通信学会(China Institute of Communications)** 主办的
通信学科中文旗舰**月刊**（每月 25 日出版），实行**初审→外审→终审**三阶段评审、终审由编委会负责。
本包覆盖一次 JOC 投稿的完整弧线：判断选题是否契合本刊**通信学科**定位、把中文科技长文写到符合
体例、搭建经得起外审的实证证据、按官方口径完成投稿、应对修回，直到录用定稿与见刊。整个流程中，
《通信学报》与 Journal on Communications (JOC) 两个刊名会自然并现，方便工具在中英文语境下检索。

官方依据核验日期：**2026-07-09**。已通过官网 `infocomm-journal.com/txxb`、CBPT 投稿系统
`cbpt.infocomm-journal.com`、CNKI/万方期刊主页与 CCF 推荐中文科技期刊目录**双源交叉核实**关键事实；
核验环境对官网页面的直接抓取返回 HTTP 403，故通过搜索引擎渲染阅读并与 CNKI/万方/CCF 目录交叉核对，
完整记录（含全部 **待核实** 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。凡未双源确认的影响因子、
版面费、审稿周期、主编等一律标 **待核实**，本包不杜撰。

> 名称辨析：本刊《通信学报》英文作 **Journal on Communications (JOC)**，与《中国通信》
> (China Communications)、《电子学报》(Acta Electronica Sinica) 等是**不同期刊**，请勿混淆。

## 本刊相对兄弟中文刊的特色

- **聚焦通信学科**：专注通信理论与技术、无线/移动通信、网络与交换、信息安全与密码、信号处理，
  区别于宽电子学科的《电子学报》、偏计算机综合的《计算机学报》、偏系统软件的《软件学报》、偏控制的
  《自动化学报》、偏信息科学基础的《中国科学:信息科学》。
- **中文科技长文规范**：中英文摘要（结构式，目的/方法/结果/结论）、中英文关键词、中图分类号 **TN**、
  文献标识码与文章编号、参考文献 **GB/T 7714**；全文约 12000 字符（约 12 页），综述可延至约 15 页。
- **三审制**：编辑初审→专家外审→**编委会终审**；审稿周期约 1~3 个月（**待核实**精确口径）。
- **学术规范红线**：知网查重，与已发表论文**重复率超过 20% 不予收录**；一稿多投明确禁止。
- **费用透明**：不收稿件处理费；初审通过后审稿费 300 元/篇；录用后版面费 600 元/面（以投稿系统内
  当期通知为准）。

## 12 个技能

| 技能 | 作用 |
|---|---|
| [`jonc-topic-selection`](skills/jonc-topic-selection/SKILL.md) | 判断选题是否契合本刊通信学科定位、与兄弟刊分工、选稿件类型 |
| [`jonc-workflow`](skills/jonc-workflow/SKILL.md) | 从选题到见刊的全流程时间线与技能编排 |
| [`jonc-writing-style`](skills/jonc-writing-style/SKILL.md) | 中文长文体例：中英文摘要、关键词、中图分类号 TN、GB/T 7714 |
| [`jonc-related-work`](skills/jonc-related-work/SKILL.md) | delta 优先的相关工作与文献综述，确立创新性 |
| [`jonc-experiments`](skills/jonc-experiments/SKILL.md) | 通信实验设计与呈现：链路/系统级仿真、信道模型、统计严谨 |
| [`jonc-reproducibility`](skills/jonc-reproducibility/SKILL.md) | 可复现性：仿真参数/信道/种子固定、数据集与代码可用 |
| [`jonc-supplementary`](skills/jonc-supplementary/SKILL.md) | 按"决定性"划分正文与附录/补充材料/多媒体附件 |
| [`jonc-submission`](skills/jonc-submission/SKILL.md) | 投稿就绪审计：模板、行文次序、查重、栏目、退稿风险分诊 |
| [`jonc-review-process`](skills/jonc-review-process/SKILL.md) | 三审制流程建模与各环节作者杠杆 |
| [`jonc-author-response`](skills/jonc-author-response/SKILL.md) | 审稿意见逐条答复与修回说明 |
| [`jonc-artifact-evaluation`](skills/jonc-artifact-evaluation/SKILL.md) | 代码与数据可用性（讲清本刊无独立徽章制度的现状与做法） |
| [`jonc-camera-ready`](skills/jonc-camera-ready/SKILL.md) | 录用后定稿、校样、缴费与出版排期 |

## 使用方式

1. 先读 [`jonc-topic-selection`](skills/jonc-topic-selection/SKILL.md) 判断选题是否契合本刊；
2. 用 [`jonc-workflow`](skills/jonc-workflow/SKILL.md) 规划时间线；
3. 写作阶段配合 [`jonc-writing-style`](skills/jonc-writing-style/SKILL.md)、
   [`jonc-related-work`](skills/jonc-related-work/SKILL.md)、
   [`jonc-experiments`](skills/jonc-experiments/SKILL.md)；
4. 投稿前跑 [`jonc-submission`](skills/jonc-submission/SKILL.md) 审计；
5. 收到意见后用 [`jonc-review-process`](skills/jonc-review-process/SKILL.md)、
   [`jonc-author-response`](skills/jonc-author-response/SKILL.md)；
6. 录用后用 [`jonc-camera-ready`](skills/jonc-camera-ready/SKILL.md) 收尾。

## 权威来源

- 官网：`https://www.infocomm-journal.com/txxb`
- 投稿系统：`http://cbpt.infocomm-journal.com/`
- 信息源对照与 **待核实** 清单：[`resources/official-source-map.md`](resources/official-source-map.md)

## 许可

MIT License · © 2026 Bryce Wang。本包为独立编写的写作辅助资料，非《通信学报》/Journal on
Communications (JOC) 官方出品；一切以编辑部当期公告为准。
