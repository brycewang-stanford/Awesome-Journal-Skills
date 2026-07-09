# PODS 技能包

面向 **PODS —— ACM SIGMOD/SIGACT 数据库系统原理研讨会（Symposium on Principles of Database
Systems）** 投稿的十二个智能体技能。PODS 是每年与 SIGMOD 同期举办的**数据库理论**研讨会。本技能包
覆盖一次 PODS 投稿的完整链路：判断你的工作是一个**定理**（投 PODS）还是一个**系统**（投
SIGMOD/VLDB/ICDE），以及 PODS 与其姊妹理论会议 ICDT 之间的取舍；把论文写成开篇即给出**精确模型与
精确结论**的形态；构建理论审稿人信服的分析性证据（上下界相互匹配、分类完备、假设陈述正确）；准备
轻量级双盲的 EasyChair 投稿及其**完整证明附录**；应对多轮投稿周期与带 shepherd 的 **revision（修订）**
环节；并完成 **PACMMOD PODS 分卷** 的 camera-ready 与 arXiv 完整版。

官方信息核对于 **2026-07-09**：PODS 2026（班加罗尔）与 PODS 2027（亨廷顿海滩）的征稿与重要日期页、
PACMMOD PODS 分卷页、PODS 的 EasyChair 站点，以及 sigmod.org 的 PODS 奖项页。在核验环境中直接抓取
`sigmod.org` 与 `dl.acm.org` 返回 403，因此官方页面通过搜索引擎对确切 URL 的渲染快照阅读，并与 ACM
数字图书馆（PACMMOD）、dblp 及 databasetheory.org 社区镜像交叉核对；完整的溯源链（含所有仍标注
待核实 的条目）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名混淆提醒：**PODC** 是 ACM *分布式*计算原理研讨会（Principles of *Distributed* Computing），
> 与本会不同；**ICDT** 是 EDBT/ICDT 联盟中 PODS 的姊妹数据库理论会议。本技能包中的事实均不来自对
> 它们与 PODS 的混淆。

## PODS 与其兄弟会议的不同之处

以下经 2026/2027 周期核实的机制，构成了各技能建议的主体，也正是从系统类数据库旗舰会议或纯理论会议
转投而来的作者最常踩的坑：

- **贡献是定理，不是系统。** PODS 论文是模型、界、二分（dichotomy）、逻辑与可证明最优的算法。跑分
  取胜属于 SIGMOD/VLDB/ICDE；PODS 审稿人读的是你的证明。
- **每年多个投稿周期。** PODS 设**两个周期**（PODS 2026：论文截止 2025-06-10 与 2025-12-10）。被拒
  距离下一次机会仅一个季度——但存在再投禁投期，所以仓促投稿仍有代价。
- **带 shepherd 的 revision 环节。** 首轮决定为 **accept / reject / revision**；revision（minor 或
  major）会邀请提交修订稿，需由 **shepherd** 判定满意后方可录用——更接近期刊的 R&R，而非普通 rebuttal。
- **轻量级双盲评审。** 隐去作者姓名与单位，自引用第三人称，投稿时申报利益冲突（COI）——这是相对
  PODS 早年单盲传统的改变。
- **使用 `acmsmall`，而非 sigconf。** `\documentclass[acmsmall,review,anonymous]{acmart}`，正文
  **不含参考文献不超过 15 页**，**参考文献不限长度**，并附**在投稿时随文提交的证明附录**——PODS
  不允许在线/外部附录，因此所有证明都随论文一并提交。
- **没有 artifact 评审；“artifact”就是证明。** 作为理论会议，PODS 没有系统类的 artifact 环节，也没有
  ACM 徽章。其对应物是完整的证明附录，以及按社区惯例发布、并与 PACMMOD 版本 DOI 互链的 **arXiv 完整版**。
- **在 PACMMOD 发表，在 PODS 报告。** 录用论文发表于 **PACMMOD（ACM 数据管理会刊）的 PODS 分卷**，
  并受邀在研讨会上作报告。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`pods-topic-selection`](skills/pods-topic-selection/SKILL.md) | 用“定理 vs 系统”和“结论替换测试”在 PODS 与兄弟会议（SIGMOD/VLDB/ICDE 系统、ICDT 理论、LICS/ICALP、TODS/JACM）间选择。 |
| [`pods-workflow`](skills/pods-workflow/SKILL.md) | 围绕 PODS 多周期日程做项目规划：摘要—论文两步截止、48 小时 rebuttal、带 shepherd 的 revision、PACMMOD camera-ready 与 arXiv 完整版。 |
| [`pods-writing-style`](skills/pods-writing-style/SKILL.md) | 开篇即给出精确模型与结论，精确陈述定理，匹配上下界，在 acmsmall 页数内保持每个证明完整且双盲。 |
| [`pods-related-work`](skills/pods-related-work/SKILL.md) | 在*结论层面*对照 PODS/ICDT/逻辑文献定位，写“差异优先”的对比，并保持自引用双盲。 |
| [`pods-experiments`](skills/pods-experiments/SKILL.md) | 让严格性与主张匹配：匹配下界、二分完备性、正确的复杂度假设，仅在必要时给出经验性佐证。 |
| [`pods-reproducibility`](skills/pods-reproducibility/SKILL.md) | 让论文可验证：主张—证明映射、自足的附录证明、诚实的假设与范围，以及 arXiv 完整版惯例。 |
| [`pods-supplementary`](skills/pods-supplementary/SKILL.md) | 在 acmsmall 页数下划分正文与随文附录，遵守 PODS 不设外部附录的规定与双盲卫生。 |
| [`pods-submission`](skills/pods-submission/SKILL.md) | EasyChair 投稿终检：周期选择、摘要+COI 登记、acmsmall 格式、证明附录、匿名扫查与桌拒风险分诊。 |
| [`pods-review-process`](skills/pods-review-process/SKILL.md) | 建模评审流程——轻量双盲、每周期两轮、accept/reject/revision、shepherd——并指出作者的杠杆点。 |
| [`pods-author-response`](skills/pods-author-response/SKILL.md) | 撰写两个回合：约 48 小时的 rebuttal（纠正误读），以及把每一条必办项映射到具体改动的 revision 说明信。 |
| [`pods-artifact-evaluation`](skills/pods-artifact-evaluation/SKILL.md) | PODS 版的“artifact 评审”：形式主张核验——完整证明、主张—证明映射与 arXiv 完整版，而非徽章。 |
| [`pods-camera-ready`](skills/pods-camera-ready/SKILL.md) | 去匿名、补全 PACMMOD 元数据、落实 shepherd 要求的修订，并发布且 DOI 互链 arXiv 完整版。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十一个来源含 URL 与访问日期；已核实的 2026/2027 事实；访问方式说明；显式的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口与网关被封时的交叉核对来源，及作者侧核验流程。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经检索核实、覆盖五种贡献形态的 PODS 论文（Test-of-Time 与最佳论文得主），附自查问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构“二分定理”论文的摘要与引言，按 PODS 结构改写的 before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 对接共享的投稿就绪工具，并为理论论文改写（主张—证明矩阵、证明附录清单）——不含代码 artifact，因为 PODS 没有。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./PODS-Skills
claude plugin install pods-skills
```

或直接使用文件：每个 `skills/pods-*/SKILL.md` 都是独立指令文件，其 frontmatter 的 `description`
告诉智能体何时触发。典型用法：

- “这篇该投 PODS 还是 SIGMOD/ICDT？” → `pods-topic-selection`
- “按 PODS 研究轨规则审我的草稿” → `pods-submission`
- “我们拿到 revision——规划带 shepherd 的再投” → `pods-author-response`
- “把证明附录和 arXiv 完整版准备好” → `pods-artifact-evaluation`

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- PODS 2026 是**第 45 届**：印度班加罗尔，与 SIGMOD 同期，**2026 年 5 月 31 日 – 6 月 5 日**。两个
  周期：论文 **2025-06-10** 与 **2025-12-10**（摘要早一周）。PODS 程序委员会主席 Ke Yi（HKUST）。
- PODS 2027 是**第 46 届**：美国加州亨廷顿海滩，**2027 年 6 月 13–19 日**。两个周期：周期一论文
  **2026-05-30**；周期二摘要+COI **2026-10-10**、论文 **2026-10-17**（通知 2027-01-19、修订
  2027-02-19、终审 2027-03-12）。截至 2026-07-09，此**周期二为下一个生效截止**。
- 格式：**`acmsmall[review,anonymous]`**，正文**不含参考文献 15 页** + 参考文献不限 + 随文附录。评审：
  在 **EasyChair** 上**轻量级双盲**。决定：**accept / reject / revision**（带 shepherd）。发表：
  **PACMMOD PODS 分卷**。

## 事实纪律

本技能包区分三类陈述，并在各技能中保持其可辨识：

1. **已核实的 2026/2027 事实**——带日期/页数并溯源到源图中的编号来源（如两周期日程、15 页 acmsmall
   预算、PACMMOD 发表）。
2. **转述事实**——仅通过二手渲染读到并如实标注（如 PODS 2026 周期二的确切 rebuttal/通知日期）。
3. **核验时不可确认者**——显式标注 待核实（如首个采用双盲的 PODS 届次、PODS 2027 程序委员会名单、
   跨周期再投的确切措辞、任何生成式 AI 使用披露政策）。

若任何陈述以第 1 类口吻呈现第 2 或第 3 类材料，应视为缺陷，并对照最新官方页面修正。

## 维护须知

- 上述每个日期与页数都是**周期快照**。PODS 每届都会重新决定其结构（包括周期数量与时间），因此每年
  首先核验节奏。
- PODS 没有常设主编；PODS 程序委员会主席每届轮换。PACMMOD 为开放获取，成本模型是注册费，且至少一名
  作者到场报告。
- 新增示例论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验
  流程——一个熟悉的结论并不能证明它出自 PODS（许多数据库理论里程碑其实是 ICDT、LICS 或期刊论文）。

## 许可证

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
