# PODC 技能包

面向 **PODC —— ACM 分布式计算原理研讨会（ACM Symposium on Principles of Distributed
Computing）** 投稿的十二个 agent 技能。PODC 是 SIGACT-SIGOPS 联合主办的**分布式计算理论**旗舰会议。
本技能包覆盖一次 PODC 投稿的完整弧线：判断一个结果是否"适合 PODC"，还是应投往 DISC、SPAA、
STOC/FOCS/SODA 或某个系统类会议；把模型、定理与证明打磨到分布式理论程序委员会所要求的标准；准备
**轻量级双盲（lightweight double-blind）** 的 HotCRP 投稿，处理"前 10 页讲清价值 + 不限长度完整版"
的篇幅规则；在常规论文与 **Brief Announcement（简短通告）** 之间做取舍；并完成 ACM 会议论文集的
camera-ready 以及承载完整证明的 arXiv 完整版。

官方信息核对日期为 **2026-07-09**：PODC 2026 征稿启事与重要日期页、`podc.org` 主页与程序委员会页、
PODC 2026 HotCRP 站点、ACM 数字图书馆的 PODC 论文集，以及 dblp。核验环境中直接抓取 `podc.org` 与
`dl.acm.org` 会报错，因此官方页面通过搜索引擎对确切 URL 的**渲染快照**阅读，并与 dblp、ACM DL 论文集、
DMANET 征稿公告和 wikicfp 交叉核对；完整取证链路（含所有仍标注 **待核实** 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名撞车提醒：**PODC 不是 PODS。** `PODS` 是 ACM 数据库系统原理研讨会（SIGMOD 周内的数据库理论会议）；
> PODC 是分布式计算理论研讨会。一字之差、两个社区——本包中没有任何事实来自 PODS。

## PODC 与兄弟会议的不同之处

以下经 2026 周期核验的会议机制，驱动了各技能中的大部分建议，也正是来自系统会议、来自串行理论、或来自
DISC 的作者最常犯错的地方：

- **这是"看证明"的会议，不是"看工件"的会议。** PODC 评审的是**模型、定理与证明**。没有工件评审、没有
  徽章赛道；理论论文里"能不能跑"的对应物是"证明是否闭合、模型与失效假设是否诚实陈述"。一篇只有测量、
  没有可分析保证的分布式**系统**论文，通常并不匹配。
- **10 页论文集篇幅 + 不限长度的完整版。** 被接收的常规论文在 **双栏 ACM 论文集格式** 下最多 **10 页**；
  **投稿本身不限页数**，但只有摘要与**标题页之后的前 10 页**保证会被阅读，超出部分由程序委员会酌情阅读。
  鼓励作者直接提交含全部证明的**完整版**作为投稿。
- **轻量级双盲评审。** PODC 2026 采用轻量级双盲：投稿中不得出现作者姓名、单位与邮箱。这相对 PODC 历史上
  的单盲是一个真实变化——请每个周期核对确切措辞。
- **Brief Announcements 赛道。** 除常规论文外，PODC 接收 **Brief Announcement**（投稿至多 5 页、发表
  至多 3 页），用于在研工作、已在别处完整发表的结果、或篇幅较小的贡献——它是一个真正的策略选项，而非
  安慰奖。
- **arXiv 完整版是常态。** 把含全部证明的完整版发到 arXiv 是标准且受鼓励的做法；PODC 不把预印本当作
  一稿多投问题，社区会去读 arXiv 版以获取 10 页论文集容不下的证明。
- **与 DISC 共享的奖项生态。** **Dijkstra 奖**（十年影响力）与**分布式计算原理博士论文奖**由 PODC 与
  DISC **联合**颁发；该领域把两个会议视为"同一个理论社区的两次年会"。
- **分布式模型就是全部。** 消息传递 vs. 共享内存；同步 vs. 异步 vs. 部分同步；崩溃 vs. 拜占庭 vs.
  自稳定失效；LOCAL vs. CONGEST；轮数/消息/空间复杂度——模型与代价度量既决定正确性、也决定新颖性。
  这正是 PODC 区别于 STOC/FOCS/SODA 串行理论之处。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`podc-topic-selection`](skills/podc-topic-selection/SKILL.md) | 在 PODC 与其邻居（DISC、SPAA、OPODIS/SIROCCO/SSS、STOC/FOCS/SODA、ICDCS/DSN/OSDI、AFT/FC，以及 PODS 命名陷阱）之间，按模型、代价度量与日历选路。 |
| [`podc-workflow`](skills/podc-workflow/SKILL.md) | 从 2 月截稿日倒推整个单周期年：双盲评审、通知、camera-ready 与 arXiv 完整版。 |
| [`podc-writing-style`](skills/podc-writing-style/SKILL.md) | 搭建分布式理论骨架：模型框、结果前置、证明结构，以及"前 10 页讲清价值"的纪律。 |
| [`podc-related-work`](skills/podc-related-work/SKILL.md) | 在分布式计算文献（PODC/DISC/SPAA/期刊）中定位，写出"模型与界都精确"的 delta，并保持自引的双盲安全。 |
| [`podc-experiments`](skills/podc-experiments/SKILL.md) | 实验的理论对应物：紧界、匹配下界、模型/假设的压力测试，以及诚实的可选仿真。 |
| [`podc-reproducibility`](skills/podc-reproducibility/SKILL.md) | 面向证明会议的"可复现性"：自洽的证明附录、可核对的模型假设、以及可选仿真的透明度。 |
| [`podc-supplementary`](skills/podc-supplementary/SKILL.md) | 在"保证被读的 10 页"与"完整版/附录"之间分配内容，使任何决定接收与否的材料都不落在第 10 页之后。 |
| [`podc-submission`](skills/podc-submission/SKILL.md) | HotCRP 终检：摘要注册、ACM 模板与 10 页价值预算、双盲清扫、常规论文与 Brief Announcement 的取舍、拒稿风险分诊。 |
| [`podc-review-process`](skills/podc-review-process/SKILL.md) | 建模评审流水线——轻量双盲、会读证明的程序委员会、接收/拒稿且无修订轮——以及作者杠杆所在。 |
| [`podc-author-response`](skills/podc-author-response/SKILL.md) | 撰写反驳（若该周期设有此环节）：纠正对证明的误读、补上缺失的引理或界，并守住匿名边界。 |
| [`podc-artifact-evaluation`](skills/podc-artifact-evaluation/SKILL.md) | PODC **没有工件赛道**——本技能把这份精力导向证明附录的完整性与模型/假设的严谨性，即理论论文真正的"评审"。 |
| [`podc-camera-ready`](skills/podc-camera-ready/SKILL.md) | 去匿名、在不丢失证明地图的前提下压到 10 页 ACM 论文集格式、补全 ACM 版权元数据、并把完整版发到 arXiv。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 带 URL 与访问日期的来源；已核验的 2026 事实；访问方式说明；显式的 待核实 清单；以及 PODC-vs-PODS 与 PODC-vs-DISC 护栏。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 直连被网关拦截时可用的官方面与交叉核对来源，以及作者侧的核验流程。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经网络核验、覆盖多种贡献形态（群体协议、无等待层级、失效检测器、不可能性、分布式图下界）的 PODC 论文，附自查问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构共识结果的摘要与引言，按 PODC 弧线重写的 before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 理论论文可能附带的"可选仿真/证明检查"脚本适配器，以及通用工具做不到的 PODC 专属检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是带有自身 marketplace 清单的自包含插件）：

```bash
# 在仓库克隆目录中
claude plugin marketplace add ./PODC-Skills
claude plugin install podc-skills
```

或直接使用文件：每个 `skills/podc-*/SKILL.md` 都是独立的指令文件，其 frontmatter 的 `description`
告诉 agent 何时触发。典型触发：

- "这是 PODC 论文，还是该投 DISC/SPAA/PODS？" → `podc-topic-selection`
- "按 PODC 2026 征稿启事审我的稿子" → `podc-submission`
- "这该投常规论文还是 Brief Announcement？" → `podc-submission` / `podc-supplementary`
- "把完整版和证明准备好投 arXiv 与 10 页 camera-ready" → `podc-camera-ready`

## 2026 周期锚定事实（历史快照，非永久规则）

- PODC 2026 为**第 45 届**：**Royal Holloway, University of London，Egham，英格兰**，
  **2026 年 7 月 6-10 日**，与 SPAA 2026 同地举办。由 **ACM SIGACT 与 SIGOPS** 联合主办。
  程序主席：**Eric Ruppert**。
- **日历：** 摘要注册 **2026-02-11**，全文投稿 **2026-02-16**（均为 23:59 AoE），通知 **2026-04-29**，
  camera-ready **2026-05-20**，站点 `podc26.hotcrp.com`。
- **格式：** ACM Master 模板（`acmart`），双栏论文集。常规投稿**不限页数**，但只有摘要与**标题页后前
  10 页**保证被读；被接收的常规论文占 **≤10 论文集页**。**Brief Announcement**：投稿 **≤5 页**，
  发表 **≤3 页**。
- **评审：** **轻量级双盲**（投稿中不得含作者姓名/单位/邮箱）。决定为接收/拒稿；**没有期刊式修订轮**。
- **惯例：** 鼓励 arXiv 完整版；部分论文获邀投 **JACM** 与 **Distributed Computing** 特刊。奖项：
  **最佳论文**、**最佳学生论文**、**最佳报告**；**Dijkstra 奖** 与 **博士论文奖** 与 DISC 联合颁发。

## 事实纪律

本包区分三类陈述，各技能均写成可辨别的样式：

1. **已核验的 2026 事实**——带日期/预算，且可追溯到来源图中的编号来源（如 2 月 11/16 截稿、10 页价值
   预算、轻量双盲规则、≤5/≤3 页 Brief Announcement）。
2. **转述事实**——仅通过二手渲染读到并明确标注（如程序主席之外的完整组委会名单）。
3. **核验时不可确证项**——显式标注 待核实（如 2026 周期是否设反驳/rebuttal 环节、2026 各奖项的确切机制、
   以及任何生成式 AI 使用披露政策）。

若任何陈述以第 1 类口吻呈现第 2 或第 3 类材料，视为 bug，并对照官方页面修正。

## 维护说明

- 上述每个日期与预算都是**周期快照**。PODC 每届会重新决定细节——包括是否设反驳环节、双盲的确切措辞——
  故每年动手前先核对当前征稿启事。
- PODC 没有常任主编；其轮换对应物是每届的程序主席与委员会，由 ACM SIGACT/SIGOPS 委任。没有 APC，
  成本模型是注册费，且每篇被接收论文须由至少一名作者到场报告。
- 新增范例论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验步骤——一个著名的分布式
  计算结果可能出现在 DISC、STOC、FOCS 或期刊（JACM、*Distributed Computing*），而非 PODC。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
