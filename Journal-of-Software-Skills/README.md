# 《软件学报》技能包 (Journal of Software Skills)

面向《软件学报》(Journal of Software, JOS) 投稿的 12 个中文智能体技能。《软件学报》由**中国
科学院软件研究所**与**中国计算机学会 (CCF)** 联合主办，是 **CCF 推荐 A 类中文科技期刊**、
中文软件学科的旗舰刊物（月刊）。本包覆盖一次投稿的完整弧线：判断稿件是否契合《软件学报》
(Journal of Software) 的软件学科定位（区别于《计算机学报》的全学科综合）、按中文科技写作规范
与 GB/T 7714 打磨稿件、通过 jos.org.cn 在线投稿系统提交、走完初审→外审→复审→主编终审的
多轮修回、直到录用后定稿清样与见刊。

> English one-liner: A 12-skill Chinese-language depth pack for the **Journal of Software (JOS,
> 《软件学报》)** — the CCF class-A Chinese software-discipline journal. 中文说明见
> [`README.zh-CN.md`](README.zh-CN.md)。

官方依据核对于 **2026-07-09**：《软件学报》官网 jos.org.cn 的投稿指南与"作者园地"、CCF 推荐
中文科技期刊目录、CCF ChinaSoft 中国软件大会专刊征稿页，并与 CNKI/万方期刊主页交叉核对。
构建环境中直接抓取官网返回 403，官方页面通过搜索渲染读取并多源交叉核实；完整来源与全部
**待核实**项见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 《软件学报》与兄弟刊的区别

《软件学报》(Journal of Software) 与几本 CCF A 类中文期刊学科重叠但侧重不同，这些差异驱动了
本包的大量建议：

- **软件学科专注**：本刊聚焦软件工程、系统软件、程序设计语言与编译、数据库、网络与分布式、
  软件安全、形式化方法等**软件方向**，区别于《计算机学报》(Chinese Journal of Computers) 的
  全计算机学科综合、《自动化学报》的控制方向、《电子学报》的电子与信息方向。
- **中英文双语要素**：需中英文题目、中文摘要 + English Abstract、中英文关键词、中图分类号，
  参考文献按 **GB/T 7714** 著录——这是中文期刊区别于英文会议的硬规范。
- **分层同行评审 + 多轮修回**：稿件经领域/责任编委初审→外审专家评审→责任编委复审→主编
  终审，"修改后再审"是常见决定且可能多轮，一般 6 个月内通知结果。
- **专刊 (special issue) 传统**：本刊长期设专刊，多与 **CCF ChinaSoft 中国软件大会**联动，
  由特约（客座）编辑组稿，主题如形式化方法、大模型软件质量、云原生数据库、RISC-V 系统软件、
  软件可信赖性与安全等。
- **在线投稿唯一入口**：仅接受 jos.org.cn 在线投稿系统提交，不收纸质稿与邮件投稿。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`jos-topic-selection`](skills/jos-topic-selection/SKILL.md) | 判断稿件是否契合《软件学报》的软件学科定位，与计算机学报/自动化学报等兄弟刊路由，选栏目与专刊。 |
| [`jos-workflow`](skills/jos-workflow/SKILL.md) | 把选题→写作→投稿→审稿→修回→定稿→见刊的全流程倒排计划，指明每步调用哪个技能。 |
| [`jos-writing-style`](skills/jos-writing-style/SKILL.md) | 中文科技写作规范：中英文摘要、关键词、中图分类号、引言首页弧线、术语一致、GB/T 7714。 |
| [`jos-related-work`](skills/jos-related-work/SKILL.md) | 软件学科文献分线、差异优先定位增量、中英文均衡引用、综述分类框架。 |
| [`jos-experiments`](skills/jos-experiments/SKILL.md) | RQ 契约、真实系统与数据集、可信基线、统计显著性与效应量、抗污染大模型评测、威胁有效性。 |
| [`jos-reproducibility`](skills/jos-reproducibility/SKILL.md) | 数据/代码可用性声明、环境固定、出处锁定与输出缓存、可复现材料组织。 |
| [`jos-supplementary`](skills/jos-supplementary/SKILL.md) | 正文/附录切分（决定录用的内容不得移出正文）、补充材料与多媒体附件。 |
| [`jos-submission`](skills/jos-submission/SKILL.md) | 在线投稿前的完整审计：模板、双语要素、GB/T 7714、栏目定位、学术规范、退稿风险。 |
| [`jos-review-process`](skills/jos-review-process/SKILL.md) | 稿件状态链、多轮修回机制、6 个月时序、分层评审角色与作者施力点。 |
| [`jos-author-response`](skills/jos-author-response/SKILL.md) | 修回说明（答复审稿人）：逐条回应、意见分级、修改标注、多轮一致性。 |
| [`jos-artifact-evaluation`](skills/jos-artifact-evaluation/SKILL.md) | 本刊代码/数据可用性现状（无强制轨道）、把材料做成加分项、专刊要求与归档。 |
| [`jos-camera-ready`](skills/jos-camera-ready/SKILL.md) | 录用后定稿：2021 版模板、双语一致性、GB/T 7714 复核、校样纪律与出版事务。 |

## 资源目录

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 官方与交叉来源、已核实事实、access-method note、待核实清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官网、作者园地、CNKI/万方、CCF 目录、ChinaSoft 专刊入口与交叉核实渠道。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经检索核实的《软件学报》真实论文对标表（按贡献形态），含兄弟刊辨析。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构软件工程稿件的中文摘要+引言"改前→改后"示例。 |
| [`resources/code/README.md`](resources/code/README.md) | 复现材料共享工具适配，及本刊专属核查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./Journal-of-Software-Skills
claude plugin install jos-skills
```

也可直接使用文件：每个 `skills/jos-*/SKILL.md` 都是独立的指令文件，其 frontmatter 的
`description` 说明何时触发。典型调用：

- "这篇稿子该投《软件学报》还是《计算机学报》？" → `jos-topic-selection`
- "按《软件学报》投稿要求审一遍我的稿子" → `jos-submission`
- "收到修改后再审，帮我组织修回说明" → `jos-author-response`
- "录用了，帮我做定稿清样核对" → `jos-camera-ready`

## 事实纪律

本包把三类陈述保持可区分：

1. **已核实事实**——可追溯到 [`resources/official-source-map.md`](resources/official-source-map.md)
   的编号来源（如主办单位、月刊、CCF A 类、在线投稿、6 个月内通知、GB/T 7714、专刊传统）。
2. **二手报道**——仅经二手渲染读到并标注（如收录数据库年份、篇幅经验值）。
3. **待核实**——核对时无法确认者显式标注（如现任主编与编委会名单、影响因子数值、版面费、
   录用率、摘要字数硬约束、AI 使用披露政策）。

任何以"已核实"口吻呈现二手或待核实材料的地方，都应视为缺陷并对照官网订正。**不杜撰任何
影响因子、录用率、版面费、审稿周期或主编姓名。**

## 维护说明

- 文中日期、篇幅、专刊主题均为**快照**；本刊栏目与专刊逐期调整，投稿前先核对官网当期信息。
- 影响因子、版面费、录用率、编委会名单等属易变或待核实项，以《软件学报》(Journal of
  Software) 官网、CNKI/万方与编辑部通知为准。
- 新增对标论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核实流程——熟悉的题名不等于本刊发表。

## 许可

MIT，见 [`LICENSE`](LICENSE)。中文详版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
