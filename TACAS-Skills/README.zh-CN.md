# TACAS Skills

面向 **TACAS —— International Conference on Tools and Algorithms for the Construction and Analysis
of Systems** 论文的 12 个 agent skills。TACAS 是 **ETAPS**（European Joint Conferences on Theory
and Practice of Software）的主会议之一，是形式化方法验证领域"工具与算法"一端的会议。本包覆盖一次
TACAS 投稿的完整流程：在**四个论文类别**（research、case-study、regular tool、tool-demonstration）
之间做选择；构建健全（sound）的算法与诚实的 benchmark 证据；按正确的**分类别盲审模型**准备 EasyChair
投稿；满足对 tool paper 录用起决定作用的**强制 artifact 评审**；并交付 **Springer LNCS 金色开放获取**
的 camera-ready 及获得的 ETAPS artifact 徽章。

官方依据核验日期：**2026-07-09**。已核验 TACAS 2026 / ETAPS 2026（Turin）与 TACAS 2027 / ETAPS 2027
（Copenhagen）的 call、ETAPS 联合 CfP 与 proceedings 政策、Springer LNCS 卷页、`tacas.info` artifact
评审页面，以及 SV-COMP 站点。核验环境中直接抓取 `etaps.org`、`link.springer.com`、`tacas.info` 返回
403，因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与 Springer LNCS、dblp 及 SV-COMP 站点交叉核对；
完整记录（含所有 待核实 项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> 同类会议提醒：TACAS **不是** CAV、VMCAI、FMCAD 或 SPIN。若干经典验证工具（NuSMV、CPAchecker、Storm）
> 首发于 CAV 而非 TACAS。本包任何 exemplar 均经 dblp/LNCS 核验后才归属 TACAS。

## TACAS 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 CAV、期刊或纯理论
验证会议转投作者最常犯的错误：

- **四个论文类别，各有各的规则。** **regular research**（≤16 页）、**case-study**（≤16 页）、
  **regular tool**（≤16 页）、**tool-demonstration**（≤6 页）在篇幅、匿名与 artifact 义务上各不相同。
  选类别是实质决定，不是贴标签。
- **分类别盲审模型。** **regular research 双盲**；**case-study、tool、tool-demonstration 单盲**，
  署名并公开工具。给错类别做匿名是真实错误。
- **Artifact 评审是一等公民，且对 tool 强制。** regular tool 与 tool-demonstration 论文**必须**在
  论文之后不久提交 artifact，与 PC **并行**评审，其结果**计入录用决定**；research 与 case-study 的
  artifact 为**自愿且录用后**提交。徽章（**Available / Functional / Reusable**）由 ETAPS Artifact
  Evaluation Committee 授予并印在论文首页。
- **走 LNCS 路线，金色开放获取。** TACAS 使用 Springer **`llncs.cls`**（不是 ACM `acmart` 或 IEEE
  `IEEEtran`），proceedings **自 2018 年起为 CC-BY 金色开放获取**，版权归作者所有 —— 无作者侧 APC。
- **ETAPS 伞会与单一年度轮次。** TACAS 与 **ESOP、FASE、FoSSaCS** 共处 ETAPS 共同日程，经 **EasyChair**
  投稿，采用带 rebuttal 的**单一年度评审轮**（与 ESOP 的两轮不同）。
- **主办 SV-COMP。** TACAS 是 **International Competition on Software Verification（SV-COMP）** 的
  东道主，并共处 VerifyThis —— 要在公共 task set 上被排名的 verifier 属于竞赛贡献，而非独立 tool paper。

## Skills

| Skill | 作用 |
| --- | --- |
| [`tacas-topic-selection`](skills/tacas-topic-selection/SKILL.md) | 在 TACAS 与同类会议（CAV、VMCAI、FMCAD、SPIN、期刊）之间选路，并（特色地）在四个类别中选对一个，区分 tool paper 与 SV-COMP 参赛。 |
| [`tacas-workflow`](skills/tacas-workflow/SKILL.md) | 从 EasyChair 截止日倒排单轮年度计划，经 tool paper 强制 artifact 截止日、rebuttal、通知、自愿 artifact、LNCS camera-ready 与报告。 |
| [`tacas-writing-style`](skills/tacas-writing-style/SKILL.md) | 首页给出构造/分析贡献与显式 soundness 论断；结构匹配类别；守住 16/6 页 LNCS 篇幅。 |
| [`tacas-related-work`](skills/tacas-related-work/SKILL.md) | 覆盖验证文献 lane，写 delta-first 定位，致谢 solver/benchmark，并保持 research 论文自引匿名。 |
| [`tacas-experiments`](skills/tacas-experiments/SKILL.md) | 公共 benchmark、公平配置的 baseline、诚实的 wall-clock 报告、soundness 校验、clean VM 上的可复现，及 SV-COMP 与 tool-paper 评估之别。 |
| [`tacas-reproducibility`](skills/tacas-reproducibility/SKILL.md) | 面向 ETAPS clean 评审 VM 打包：钉死依赖、离线运行、claim-to-script 映射、诚实的可复现层级。 |
| [`tacas-supplementary`](skills/tacas-supplementary/SKILL.md) | 按决策重要性划分正文、附录/网站与 artifact —— 决定录用的内容不得置于正文之外。 |
| [`tacas-submission`](skills/tacas-submission/SKILL.md) | EasyChair 终审：选类别、守 LNCS 篇幅、用对盲审模式、备好 tool paper 强制 artifact、desk-reject 分诊。 |
| [`tacas-review-process`](skills/tacas-review-process/SKILL.md) | 建模流程 —— 分类别盲审、带 rebuttal 的单一年度 PC 轮、并行强制 artifact 评审 —— 及作者杠杆点。 |
| [`tacas-author-response`](skills/tacas-author-response/SKILL.md) | 撰写单轮短 rebuttal，以可核验证据回应 soundness、baseline 公平性与 artifact 质疑，按类别要求匿名。 |
| [`tacas-artifact-evaluation`](skills/tacas-artifact-evaluation/SKILL.md) | 通过两轮模型将包转化为 ETAPS 徽章（Available / Functional / Reusable）—— tool 与 PC 并行强制，research 录用后自愿。 |
| [`tacas-camera-ready`](skills/tacas-camera-ready/SKILL.md) | 去匿名（research）、补全 LNCS 元数据与 Springer CC-BY 版权表、把 artifact 链接永久化、把获得的徽章加到首页。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方 ETAPS/TACAS/EasyChair/LNCS/SV-COMP 入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经 dblp/LNCS 核验、跨类别的 TACAS 论文（BMC、CBMC、Z3、LTSmin），附同类会议护栏与自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构 bounded-refinement-checker 工具论文的引言按 TACAS 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 TACAS 专用检查（clean-VM 运行、徽章就绪）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./TACAS-Skills
claude plugin install tacas-skills
```

也可直接使用文件：每个 `skills/tacas-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- "这是 TACAS research paper、tool paper，还是 SV-COMP 参赛？" → `tacas-topic-selection`
- "按 TACAS 类别规则审我的稿，再上 EasyChair" → `tacas-submission`
- "把工具的 artifact 准备到强制评审与徽章标准" → `tacas-artifact-evaluation`
- "审稿人质疑我们的 soundness 与 baseline 公平性 —— 起草 rebuttal" → `tacas-author-response`

## 目录结构

```text
TACAS-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面
├── skills/
│   └── tacas-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `tacas-topic-selection`；TACAS 与 CAV 重叠，且你选的**类别**决定篇幅、盲审模式
   与 artifact 义务。浏览 exemplars 看 TACAS 的 foundational 与 tool 贡献长什么样。
2. **构建工具/证据时** —— 让 `tacas-experiments` 与 `tacas-reproducibility` 贴着工作；公共 benchmark、
   公平 baseline 与 clean-VM artifact 无法在截止日临时补。
3. **写作时** —— 用 `tacas-writing-style` 对照 worked example 打磨正文，用 `tacas-supplementary` 划分
   正文/附录/artifact，用 `tacas-related-work` 做 delta-first 定位。
4. **截止周** —— 用 `tacas-submission` 对终稿 LNCS PDF 逐项过审，随后（tool paper）在论文后的强制
   artifact 截止日提交 artifact。
5. **投稿后** —— 用 `tacas-review-process` 校准预期，用 `tacas-author-response` 应对 rebuttal，随后
   `tacas-artifact-evaluation` 与 `tacas-camera-ready` —— 若结果不利，则用 `tacas-topic-selection`
   的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- TACAS 2026 为**第 32 届**，随 **ETAPS 2026（第 29 届）**在**意大利都灵**（都灵大学）举办，
  **2026 年 4 月 11-16 日**（主会议 4 月 13-16 日）。转述周期：论文 2025-10-16，tool 强制 artifact
  2025-10-30，rebuttal 2025-12-08 至 10，通知 2025-12-22，自愿 artifact 2026-01-08。2026-07-09 时该届
  已结束，live 下一目标为 TACAS 2027。
- TACAS 2027 为**第 33 届**，随 **ETAPS 2027（第 30 届）**在**丹麦哥本哈根**，**2027 年 4 月 10-15 日**；
  ETAPS 2027 自愿 artifact 截止 2027-01-11。
- 类别：**research / case-study / regular tool / tool-demonstration**。格式：Springer **`llncs.cls`**，
  经 **EasyChair**。评审：**research 双盲、tool/case-study 单盲**，带 rebuttal 的单一年度轮。Artifact：
  tool/tool-demo **强制**，research/case-study **自愿**；徽章 **Available / Functional / Reusable**。
  Proceedings：**LNCS，金色开放获取（CC-BY）**。TACAS 主办 **SV-COMP**（TACAS 2026 为第 15 届）。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如四个类别、分类别盲审
   模型、tool paper 强制 artifact、LNCS 金色开放获取）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如 TACAS 2026 精确投稿数与 PC 主席名单）。
3. **核验期不可确定项** —— 明确标为 待核实（如完整 PC-chair/AEC 名单、ETAPS 奖项名单、各类别精确
   日期差异）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。TACAS/ETAPS 每届重定结构 —— 篇幅、徽章集合、日程 —— 每年先在当前
  ETAPS 联合 CfP 与 TACAS 页面核验。
- TACAS 无常任 editor-in-chief、无作者侧 APC；PC 主席每届轮换，ETAPS 集中资助金色开放获取。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程 —— 熟悉的工具名并不能证明该论文发表于 TACAS（CAV 是最易混淆者）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
