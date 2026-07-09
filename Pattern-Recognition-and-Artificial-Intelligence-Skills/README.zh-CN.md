# 《模式识别与人工智能》技能包（中文详版） · Pattern Recognition and Artificial Intelligence (PR&AI) Skills

本页是《模式识别与人工智能》(Pattern Recognition and Artificial Intelligence, PR&AI) 中文投稿技能包
的详版说明；速览见 [`README.md`](README.md)。本包面向向《模式识别与人工智能》投稿的作者，把一次
投稿从选题、写作、实证、投稿、修回到录用见刊的完整弧线拆成 12 个可调用的中文 agent 技能。

## 一、本刊定位与主办

《模式识别与人工智能》(Pattern Recognition and Artificial Intelligence, PR&AI) 由**中国自动化学会、
国家智能计算机研究开发中心、中国科学院合肥智能机械研究所**共同主办，**科学出版社**出版，创刊于
**1989 年**，**月刊**，编辑部设于合肥。刊号 **CN 34-1089/TP**、**ISSN 1003-6059**。本刊是 CCF 推荐
**B 类**中文科技期刊，被北大核心、CSCD、科技核心(统计源)等收录（以最新目录为准）。它专注**模式
识别 (Pattern Recognition)、人工智能 (Artificial Intelligence)、机器学习、计算机视觉、自然语言
处理、智能系统**等 AI 细分方向，比综合性计算机刊更聚焦人工智能。

> 事实核验日期 2026-07-09，双源交叉核实，访问方式与全部 **待核实** 项见
> [`resources/official-source-map.md`](resources/official-source-map.md)。影响因子、录用率、版面费、
> 主编等未双源确认者一律标 **待核实**，本包不杜撰。

## 二、与兄弟中文刊的分工

同一批建设的兄弟中文 CS 刊各有侧重，选刊时按学科落点区分：

| 期刊 | 侧重 | 与本刊关系 |
|---|---|---|
| 《模式识别与人工智能》PR&AI | 模式识别/AI/机器学习/视觉/NLP（本刊） | AI 细分专业刊 |
| 《自动化学报》 | 控制、自动化、系统 | 控制为主，AI 为其分支 |
| 《计算机学报》 | 计算机全学科综合 | 综合刊，AI 只是其一 |
| 《软件学报》 | 系统与软件工程 | 软件方法为主 |
| 《电子学报》 | 电子、通信、信号 | 硬件/信号为主 |
| 《计算机科学》 | 计算机综合，偏应用与快报 | 综合刊 |

若你的工作是**纯控制**更适合《自动化学报》，是**软件工程方法**更适合《软件学报》；若核心贡献在
**模式识别/机器学习/视觉/NLP 的算法与模型**，PR&AI 是对口落点。

## 三、投稿关键事实（以官网当期须知为准）

- **投稿方式**：官方投稿系统 `http://manu46.magtech.com.cn/Jweb_prai/` 的"**作者中心**"在线投稿；
  上传前确认文件无病毒。编辑部邮箱 `bjb@iim.cas.cn`，电话 `0551-65591176`。
- **字数**：全文 **18000~44000 字**（含图表，长文体例）。
- **审稿周期(官方口径)**：一般 **6 个月内**给评审结果；超过 6 个月，作者通知编辑部并获确认回复后
  可自行处理。（二手另有 3~4 个月说法，属报告值，**待核实**。）
- **格式**：中文题名+英文题名、**中文摘要约 200 字 + English Abstract 约 200 词**（报道性四要素：
  目的、方法、结果、结论）、**中英文关键词 3~5 个**、中图分类号(**TP**)、作者简介与基金项目、
  参考文献 **GB/T 7714**（中文文献中英文对照）。
- **学术规范**：编辑部做**重复率检测**，未通过退回作者；要求原创创新价值；一稿多投禁止。

## 四、12 个技能与建议顺序

1. **选题定位**：[`prai-topic-selection`](skills/prai-topic-selection/SKILL.md) 判契合与稿件类型。
2. **全流程编排**：[`prai-workflow`](skills/prai-workflow/SKILL.md) 拉时间线。
3. **写作体例**：[`prai-writing-style`](skills/prai-writing-style/SKILL.md) 搭中文长文骨架。
4. **相关工作**：[`prai-related-work`](skills/prai-related-work/SKILL.md) delta 优先立创新。
5. **实验证据**：[`prai-experiments`](skills/prai-experiments/SKILL.md) 公平基线+统计严谨。
6. **可复现性**：[`prai-reproducibility`](skills/prai-reproducibility/SKILL.md) 固定环境/种子。
7. **补充材料**：[`prai-supplementary`](skills/prai-supplementary/SKILL.md) 分正文与附录。
8. **投稿自审**：[`prai-submission`](skills/prai-submission/SKILL.md) 就绪审计与退稿分诊。
9. **审稿流程**：[`prai-review-process`](skills/prai-review-process/SKILL.md) 建模各环节杠杆。
10. **答复修回**：[`prai-author-response`](skills/prai-author-response/SKILL.md) 逐条答复。
11. **制品可用性**：[`prai-artifact-evaluation`](skills/prai-artifact-evaluation/SKILL.md) 代码数据。
12. **录用定稿**：[`prai-camera-ready`](skills/prai-camera-ready/SKILL.md) 校样与出版。

## 五、使用纪律

本包所有面向作者的结论必须与官网当期《投稿指南》一致；任何标 **待核实** 的数字（版面费、精确
审稿周期、影响因子、主编、审稿是否双盲）不得以确定口径写入结论。区分官方"6 个月"周期口径与二手
报告值，不把二手影响因子当定论。

## 许可

MIT License · Copyright (c) 2026 Bryce Wang。
