# MobiSys Skills

面向 **MobiSys —— ACM International Conference on Mobile Systems, Applications, and
Services（移动系统、应用与服务国际会议）** 论文的 12 个 agent skills。MobiSys 是 ACM
SIGMOBILE 旗下关注**设备之上的系统**的会议：真正的贡献是跑在手机、可穿戴、车载或嵌入式
板卡上的系统本身，而不是底层的无线链路。它的姊妹会议 MobiCom 关心无线链路本身，MobiSys 则
关心其上层的一切 —— 移动运行时与操作系统、on-device 机器学习推理、感知流水线与服务、计算
offload，以及决定这些东西能否落地的 energy、latency 与 memory 预算。本包贴合一次真实
MobiSys 冲刺的节奏：**每年一次、位于 12 月初的单一截稿**（对应次年 6 月的会议）、**两轮
评审 + 早拒 + rebuttal**、HotCRP 上的 double-blind 投稿、12 页 ACM 双栏正文，以及以真实
硬件上测得的毫秒、毫焦、兆字节为语言的证据门槛。

官方依据核验日期：**2026-07-09**。已核验 `sigmobile.org` 上的 MobiSys 2026 Call for
Papers、Artifact Evaluation、Awards 与 Organizing-Committee 页面，`mobisys26.hotcrp.com`
的 deadlines 与 program-committee 页面，官方 `@ACMMobiSys` 发布的 CFP 公告，ACM Digital
Library 的 MobiSys 论文集，dblp 的 `conf/mobisys` 流（用于 exemplar 核验），以及 SIGMOBILE
Test-of-Time 奖页面。核验环境中直接抓取 `sigmobile.org` 与 `hotcrp.com` 均返回 **HTTP
403**，因此以下事实均通过对确切官方 URL 的搜索引擎渲染读取，并与 ACM DL、dblp、SIGMOBILE
新闻交叉核对；完整链路（含仍标 待核实 的项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

**周期状态（2026-07-09）：** **MobiSys 2026**（第 24 届，英国 Cambridge，2026 年 6 月 21–25
日）**刚刚结束** —— 论文截稿是 **2025 年 12 月 5 日**，评审通知与 rebuttal 在春季进行，会议
于 6 月下旬落幕，本包正是在会后数日撰写。**下一个开放窗口**是 **MobiSys 2027**：社区
聚合器与会议自身的节律把其论文截稿定在 **2026 年 12 月 5 日前后**、通知在 **2027 年 3 月**
前后，但核验时 2027 CFP 尚未确认发布，故这些日期在官方页面出现前均为 待核实。2027 的
举办地、chairs 与确切时钟均未核验。

## MobiSys 与姊妹会议的区别

以下是驱动各 skill 建议的 2026 周期机制，也是从无线网络会议或双截稿系统会议转来的作者最容易
踩的坑：

- **设备之上的系统才是贡献。** 判定标准是一个*移动或嵌入式系统、应用或服务*，其在真实硬件上
  的行为就是结果 —— on-device 推理引擎、移动 OS/运行时机制、感知服务、offload 调度器。纯
  PHY/MAC 或协议结果属于 MobiCom；传感网基础设施属于 SenSys；数据中心或分布式系统属于 NSDI。
- **每年一次截稿，而非滚动双截稿。** MobiSys 是 12 月初单一论文截稿、对应次年 6 月会议。这与
  MobiCom、NSDI 每年两次的模式相反，也改变了全部算法：错过一次就是错过一整年，workflow skill
  因此从这个唯一硬日期倒排。
- **两轮评审、早拒、然后 rebuttal。** 未进入第二轮的论文会收到附评审意见的早拒，便于作者
  重新规划；进入第二轮的论文随后有一个 **rebuttal 窗口**，仅限更正事实错误与回答具体问题。
  新结果只有在直接回应意见时才可加入，或可*承诺*在 camera-ready 前完成。
- **没有常设的一次性 revision 通道。** 与 MobiCom、NSDI 不同，2026 CFP 渲染版描述的是经由
  rebuttal 的 accept/reject，而非单独的大修再投路径；对你所投周期是否存在 revision 机制，请按
  待核实 处理。
- **12 页双栏、含图表计数。** 正文上限为 **12 页单倍行距、含图表的编号页**（ACM 模板）；
  references 与 appendices 不计入上限。
- **HotCRP 上 double-blind。** 自 2017 年起对评审隐藏作者身份；投稿与 rebuttal 在每届的
  `mobisys<yy>.hotcrp.com` 上进行，上传前有一个论文注册步骤。
- **三枚独立的 ACM artifact 徽章。** 单盲的 Artifact Evaluation Committee 评定 *Artifacts
  Available*、*Artifacts Evaluated — Functional*、*Results Reproduced*；作者可申请一枚、两枚
  或全部三枚，通过的徽章会印在论文与 ACM DL 上。评审在自己的机器上运行作者提交的 workflow
  脚本 —— 一种脚本优先、强势的 artifact 文化。
- **证据在设备上测得。** MobiSys 评审期待真实手机、可穿戴或嵌入式板卡；以焦耳计的 energy、
  以毫秒计的 latency、memory footprint、thermal 行为，以及当贡献是服务时的部署或用户研究。
  纯仿真或单次运行的结果在这里会被读作“评估不足”。
- **canon 是移动系统，且极易被误归。** MAUI、SoundSense、Odessa、MCDNN、DeepMon 都是 MobiSys
  论文；SIGMOBILE Test-of-Time 奖（跨会议、十年视野）提醒我们：该领域被引最多的结果，也最常被
  在 MobiCom、SenSys、OSDI、NSDI 之间误标。

## Skills

| Skill | 作用 |
| --- | --- |
| [`mobisys-topic-selection`](skills/mobisys-topic-selection/SKILL.md) | 判定贡献是否为 MobiSys 所奖励的移动/嵌入式*系统*，并把无线机制、传感网、分布式系统、ubicomp 或早期想法的错配分流到 MobiCom、SenSys、NSDI/OSDI、IMWUT 或 HotMobile。 |
| [`mobisys-workflow`](skills/mobisys-workflow/SKILL.md) | 从 12 月单一截稿倒排，经两轮评审、rebuttal、通知、artifact evaluation、camera-ready 到 6 月现场，并预留设备实验的前置时间。 |
| [`mobisys-writing-style`](skills/mobisys-writing-style/SKILL.md) | 在 12 页双栏内搭建 移动痛点 → 系统设计 → on-device 证据 的主线，用 latency/energy 分布替代最高级形容词。 |
| [`mobisys-related-work`](skills/mobisys-related-work/SKILL.md) | 覆盖移动系统的文献车道 —— offload、on-device ML、移动 OS、感知、能耗 —— 用 dblp/ACM DL 核验会议来源以避开 MobiCom/SenSys/OSDI 陷阱，并做 blind-safe 自引。 |
| [`mobisys-experiments`](skills/mobisys-experiments/SKILL.md) | 设计真实设备评估：energy 仪器、latency 与帧率尾部、memory 与 thermal 预算、调优过的系统 baseline，以及当贡献是服务时的部署/用户研究。 |
| [`mobisys-reproducibility`](skills/mobisys-reproducibility/SKILL.md) | 记录设备、OS、SoC、模型版本与功耗仪器的溯源，使结果能在另一部手机上重现，并尽早判定哪些数据与固件可合法发布。 |
| [`mobisys-supplementary`](skills/mobisys-supplementary/SKILL.md) | 在 12 页正文、references、可选 appendices、演示 video/媒体与 HotCRP 字段之间分配内容，在评审自由裁量下保持论文自足。 |
| [`mobisys-artifact-evaluation`](skills/mobisys-artifact-evaluation/SKILL.md) | 为 AEC 打包：申请三枚 ACM 徽章中的哪些、为没有同款设备的评审提供 hardware-optional 路径，以及证明功能性的 workflow 脚本。 |
| [`mobisys-submission`](skills/mobisys-submission/SKILL.md) | 最终 HotCRP 审查：正确站点、UTC 截止、12 页双栏检查、含设备/trace 泄露的 double-blind 清扫、注册前置与 desk-reject 分诊。 |
| [`mobisys-review-process`](skills/mobisys-review-process/SKILL.md) | 建模两轮流程的结果空间 —— 早拒、rebuttal、accept —— 评审构成，以及系统与服务评审如何给 on-device 主张打分。 |
| [`mobisys-author-response`](skills/mobisys-author-response/SKILL.md) | 在 rebuttal 的范围限制内执行：先更正事实错误、回答具体问题、只加入直接回应的结果、诚实承诺 camera-ready 工作。 |
| [`mobisys-camera-ready`](skills/mobisys-camera-ready/SKILL.md) | 交付去匿名的双栏终版、完成 ACM rights 与元数据、协调 artifact 徽章、规划 Cambridge 现场报告与 demo。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 带 URL 与访问日期的官方来源、已核验事实清单、访问方式说明（sigmobile.org / hotcrp.com 直接抓取均 403）与显式 待核实 登记。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 在线官方入口（站点、HotCRP、ACM DL、dblp、SIGMOBILE）及每周期应跑的作者侧核验流程。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇元数据核验过的 MobiSys 论文（2009–2017），覆盖 offload/能耗、手机端感知、感知 offload、on-device DNN 服务、移动 GPU 推理，各附 self-check，另有 do-not-misattribute 防线。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构 on-device 推理论文的首页改写，示范如何以移动系统贡献与 on-device 证据开篇，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 到共享 ML 会议可复现套件的适配器，外加通用工具无法做的 MobiSys 专项检查（设备溯源、能耗边界、hardware-optional 冒烟运行）。 |

## 安装与使用

作为 Claude Code 插件（本目录是带有自己 marketplace manifest 的自足插件）：

```bash
# 从仓库 clone 后
claude plugin marketplace add ./MobiSys-Skills
claude plugin install mobisys-skills
```

或直接使用文件：每个 `skills/mobisys-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 告诉 agent 何时触发。典型调用：

- “这是 MobiSys 论文还是 MobiCom / SenSys 论文？” → `mobisys-topic-selection`
- “从 12 月截稿倒排出日程” → `mobisys-workflow`
- “评审出了 —— 在范围内起草 rebuttal” → `mobisys-author-response`
- “上传 HotCRP 前审查 PDF” → `mobisys-submission`

## 2026-27 锚点事实（带日期快照，非永久规则）

- **MobiSys 2026** 为第 **24** 届：**2026 年 6 月 21–25 日，英国 Cambridge**，由剑桥大学
  协办、隶属 ACM SIGMOBILE；General Chairs 为 **Fahim Kawsar** 与 **Cecilia Mascolo**（program
  chairs 待核实）。
- MobiSys 2026 时间线（按页面所示 UTC/AoE）：**论文注册 2025-11-28**、**论文提交
  2025-12-05**；两轮评审 + 早拒 + rebuttal；会议于 2026 年 6 月下旬结束。
- 格式：**12 页单倍行距双栏、含图表**；references 与 appendices 不计入上限；
  `mobisys26.hotcrp.com` 上 **double-blind**。
- Artifact evaluation 提供三枚独立 **ACM 徽章**（Available、Functional、Results
  Reproduced），单盲、脚本优先；论文集见 **ACM Digital Library**。
- **MobiSys 2027**（第 25 届）：论文截稿报告在 **2026-12-05** 前后、通知在 **2027 年 3 月**
  前后 —— 官方 CFP 发布前均为 待核实；举办地与 chairs 未核验。

## 事实纪律

全包始终区分三类陈述：

1. **已核验的 2026 周期事实** —— 可追溯到 source map 的编号来源（如 Cambridge 日期、2025-12-05
   截稿、12 页双栏预算、三枚 ACM 徽章名、两轮 + rebuttal 流程）。
2. **报告性事实** —— 仅由一致的二手渲染承载并如实标注（如社区聚合器给出的 MobiSys 2027 12 月
   截稿与 3 月通知；经 SIGMOBILE 奖页面与作者机构确认的 Test-of-Time 与 Best-Paper 选择）。
3. **待核实项** —— 显式标注并以问题形式表述（如 program chairs、rebuttal 窗口长度、本周期是否
   存在 revision 通道，以及 2027 举办地、chairs 与日期的一切）。

在任何 skill 中把第 2 或第 3 类当作第 1 类陈述都属 bug；请对照在线页面修正。

## 维护说明

- 上述每个日期、上限与规则都是 **2026 周期快照**。MobiSys 每届重发规则 —— 在给出 deadline
  敏感建议前，请重新打开当年 `sigmobile.org/mobisys/<year>` 的 CFP 与对应的
  `mobisys<yy>.hotcrp.com/deadlines` 页面。
- 截稿是单一的 **12 月** 硬性节点，以 UTC/AoE 打印；错过即失去一年，且时钟约定可能变动 ——
  切勿沿用上一周期的本地换算。
- 页数上限、double-blind 例外、rebuttal 范围以及是否存在 revision 路径都可能逐届变化；请以
  在线 CFP 为准，不要沿用旧规则。
- Chairs 逐届轮换；命名前请核对 organizing-committee 页面，并把 2027 委员会视为完全未核验。
- Artifact 徽章遵循 ACM 不断演进的 artifact-review 术语；每周期请核对当年 Artifact
  Evaluation 页面与 ACM 的徽章定义。
- 新增 exemplar 必须通过
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的会议核验流程；
  移动系统 canon 中最著名的论文最常被在 MobiCom、SenSys、OSDI、NSDI 之间误归。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English README: [`README.md`](README.md)。
