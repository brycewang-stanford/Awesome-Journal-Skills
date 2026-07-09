# HRI Skills

面向 **HRI —— ACM/IEEE International Conference on Human-Robot Interaction（人机交互国际会议）**
论文的 12 个 agent skills。HRI 是人机交互领域旗舰级的**跨学科**会议，汇聚机器人学、HCI、心理学与
设计等视角，围绕同一个核心问题：人与机器人如何互动。本包覆盖一次 HRI 投稿的完整流程：判断项目属于
HRI 还是应投 CHI、ICRA/IROS、RO-MAN、CoRL 或期刊；在 HRI 的**五个 full-paper track** 中选择正确的
一个；设计能经受跨学科审稿群体审视的 human-subjects 研究（Wizard-of-Oz、被试间/被试内、统计功效、
effect size 与质性严谨性并重、validated scales、IRB）；准备 double-blind 的 **PCS** 投稿及其必备的
video figure；应对**两阶段评审 + rebuttal**；直至完成 ACM+IEEE 双库发表的 camera-ready。

官方依据核验日期：**2026-07-09**。已核验 HRI 2026（Edinburgh）full-papers call、Overview of Review
Process 与 Reviewer Guidelines；alt.HRI、Late-Breaking Reports、video 与 Student Design 各 call；ACM
Digital Library 与 IEEE Xplore 的 HRI proceedings；IEEE-RAS 联合赞助页面；dblp；以及 HRI 2027
（Santa Clara）公告。核验环境中直接抓取 `humanrobotinteraction.org`、`dl.acm.org` 与
`ieeexplore.ieee.org` 返回 403，因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与 ACM DL、IEEE
Xplore、dblp 及 IEEE-RAS 交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名冲突提醒：**THRI**（ACM *Transactions on Human-Robot Interaction*）与 **JHRI**（*Journal of
> Human-Robot Interaction*）是**期刊**，不是本会议；**HAI** 与 **RO-MAN** 是**另外的会议**。本包中的
> 事实均不来自它们，除非作为明确的 venue 辨析。

## HRI 与同类会议的区别

以下会议机制（按 2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 CHI、纯机器人会议
（ICRA/IROS/CoRL）或心理学背景转投作者最常犯的错误：

- **证据是关于“人”的，而非只是系统。** HRI 的重心是 **human-subjects 研究**。主导问题不是“机器人能不能
  work”，而是“当一个人与它互动时会发生什么”——用真实被试、可辩护的设计、**带 effect size 的统计**、
  以及日益重要的质性严谨性来测量。这是与 ICRA/IROS/CoRL（系统与学习 benchmark 文化）的最大差别。
- **机器人的 embodiment 是核心。** 与 CHI 的通用 HCI 不同，HRI 要求有一个机器人——物理或虚拟的具身
  agent——以及与它的互动。没有机器人的纯屏幕界面研究是 CHI 论文；没有 human-in-the-loop 的自主性结果
  是 ICRA/IROS 论文。
- **五个按贡献类型划分的 track，各对应一个 subcommittee。** Full paper 须在
  **User Studies · Technical · Design · Theory and Methods · Systems** 中恰选其一，由匹配该贡献类型的
  subcommittee 评审。审稿人按“这一类贡献”的标准评判——design 论文不以 User Studies 的标准苛求，反之亦然。
- **两阶段 double-blind 评审 + rebuttal。** 每篇论文有一个 1AC 和一个 2AC、三位外审、一次作者
  **rebuttal**、一轮线上讨论，以及做出决定的 **program-committee meeting**。rebuttal 是真实杠杆，
  常常改变分数。
- **video figure 是一等公民。** HRI 的互动是时序、具身的；展示互动的补充 **video** 是被期待的，并实质
  影响审稿人对贡献的理解。
- **ACM + IEEE，使用 ACM `acmart` 模板。** HRI 由 ACM（SIGCHI / AI SIG）与 IEEE（RAS）联合赞助；录用
  论文同时进入 **ACM DL 与 IEEE Xplore**。Full paper 用 ACM Primary Article Template，**8 页**
  （含图，**不含**参考文献）——不是 CHI 的篇幅，也不是 IEEEtran 机器人栏宽。
- **human-subjects 伦理会被执行。** 投稿即受 ACM Policy on Research Involving Human Participants and
  Subjects 约束；IRB/伦理审查、知情同意与诚实报告是审稿群体会主动核查的社区规范。

## Skills

| Skill | 作用 |
| --- | --- |
| [`hri-topic-selection`](skills/hri-topic-selection/SKILL.md) | 在 HRI 与 CHI、ICRA/IROS、RO-MAN、CoRL、THRI 之间用“机器人具身”与“human-in-the-loop”测试选venue，再在五个 HRI track 中选对。 |
| [`hri-workflow`](skills/hri-workflow/SKILL.md) | 从 9 月摘要截止日倒排：rebuttal、PC meeting、camera-ready、3 月会议，并配套 alt.HRI / LBR / video / Student Design 的并行日历。 |
| [`hri-writing-style`](skills/hri-writing-style/SKILL.md) | 面向跨学科读者构建 HRI 论文：贡献与研究问题前置，hypotheses 与 measures 明确，描述机器人，主张与研究规模相称。 |
| [`hri-related-work`](skills/hri-related-work/SKILL.md) | 覆盖 HRI 的交叉文献（robotics + HCI + psychology + design），以 delta 定位，保持 double-blind 的自引匿名。 |
| [`hri-experiments`](skills/hri-experiments/SKILL.md) | 设计 human-subjects 研究：被试间/被试内、诚实的 Wizard-of-Oz、功效与样本量、**带 effect size 的统计**、mixed methods、validated scales、manipulation check、pre-registration。 |
| [`hri-reproducibility`](skills/hri-reproducibility/SKILL.md) | 让具身的 human-subjects 研究尽量可复现：WoZ 报告、研究材料、机器人行为规格、pre-registration，以及对复现极限的诚实说明。 |
| [`hri-supplementary`](skills/hri-supplementary/SKILL.md) | 规划事实上必备的 **video figure**、补充研究工具与附录——按“审稿人判断互动所必须看到的内容”划分。 |
| [`hri-submission`](skills/hri-submission/SKILL.md) | 最终 PCS 审查：摘要+论文两步截止日、track 选择、8 页 acmart 匿名格式、double-blind 排查、human-subjects 声明、desk-reject 排查。 |
| [`hri-review-process`](skills/hri-review-process/SKILL.md) | 建模流程——desk check、1AC/2AC + 三外审、rebuttal、线上讨论、PC meeting、按 track 的 subcommittee——并指出作者的杠杆所在。 |
| [`hri-author-response`](skills/hri-author-response/SKILL.md) | 写好这唯一一次高杠杆 rebuttal：回应三位审稿人与两位 AC，分诊研究设计与统计质疑，只承诺 camera-ready 能兑现的事。 |
| [`hri-artifact-evaluation`](skills/hri-artifact-evaluation/SKILL.md) | 打包代码、机器人行为、数据集与研究材料以开放共享并对接 HRI 可能提供的 ACM 徽章——并诚实说明复现具身人体研究的极限。 |
| [`hri-camera-ready`](skills/hri-camera-ready/SKILL.md) | 去匿名、补全 ACM+IEEE 双库发表元数据（CCS concepts、ORCID、版权表）、定稿 video，并通过 production 检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个来源含 URL 与访问日期；已核验的 2026 事实；access-method 说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方主页面、直连被拦时的交叉核对来源，以及作者侧核验步骤。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 已核验的 HRI 会议论文（按贡献形态），附 sibling-venue 辨析与自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构社交机器人研究的摘要与引言，按 HRI 结构 before → after 重写。 |
| [`resources/code/README.md`](resources/code/README.md) | 对接共享研究材料/复现工具的适配说明，以及通用工具无法做的 HRI 专属检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆目录执行
claude plugin marketplace add ./HRI-Skills
claude plugin install hri-skills
```

或直接使用文件：每个 `skills/hri-*/SKILL.md` 都是独立指令文件，其 frontmatter 的 `description`
告诉 agent 何时触发。典型调用：

- “这是 HRI 论文还是该投 CHI/ICRA？” → `hri-topic-selection`
- “这篇该投哪个 HRI track？” → `hri-topic-selection`
- “按 HRI full-paper 规则审我的稿” → `hri-submission`
- “审稿意见来了，帮我写 rebuttal” → `hri-author-response`
- “把 user study 设计到能过 HRI 审” → `hri-experiments`

## 2026/2027 cycle 锚定事实（历史快照，非永久规则）

- HRI 2026 为**第 21 届**，主题 **“HRI Empowering Society”**：**Edinburgh, Scotland, UK,
  2026-03-16 至 19**。Full-paper **摘要 2025-09-22**、**论文 2025-09-30**（AoE）；**rebuttal
  约 2025-11-12**；决定 2025-12；camera-ready 约 2026-01。截至 2026-07-09，该届已结束。
- HRI 2027 为**第 22 届**：**Santa Clara, California, USA, 2027-03-08 至 12**——截至 2026-07-09
  的下一个 full-paper 目标；请以其 call 为准核验确切日期与篇幅。
- Full paper：**8 页**（含图，**不含**参考文献），**ACM `acmart`** 匿名评审格式，**PCS** 门户，
  **五个 track**，**double-blind 两阶段**评审 + **rebuttal**，发表于 **ACM DL 与 IEEE Xplore**。
  配套 track：**alt.HRI**（2025-10-17）、**LBR / video / Student Design**（2025-12-08）。

## 事实纪律

本包区分三类陈述并保持可辨识：

1. **已核验 2026 事实** —— 带日期/篇幅并可追溯至 source map 中编号来源（如五个 track、8 页篇幅、
   两阶段 + rebuttal 评审、PCS）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如确切录用数、各 track best-paper 得主、camera-ready
   确切日期）。
3. **核验时不可确证项** —— 明确标 待核实（如本届确切的 `acmart` class 选项、任何 AI 使用披露政策、
   是否设正式 artifact-badge track）。

若任何陈述以第 1 类口吻呈现第 2、3 类内容，视为 bug，须对照官方页面修正。

## 维护说明

- 上述每个日期与篇幅都是 **cycle 快照**。HRI 每届重新决定其结构——包括 track 名称、摘要/论文两步、
  rebuttal 格式——请以当届 full-papers call 为准。
- HRI 无常任主编，各届轮换 chair。不要把**会议**与 **THRI**/**JHRI** 期刊混淆。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——著名机器人或熟悉的量表名并不能证明它是一篇 HRI **会议**论文（许多在 THRI、JHRI、
  IJSR 或 CHI）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
