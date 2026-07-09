# IEEE INFOCOM Skills

面向 **IEEE INFOCOM —— IEEE International Conference on Computer Communications** 论文的 12 个
agent skills。INFOCOM 是 IEEE Communications Society（ComSoc）网络方向的旗舰会议，也是计算机网络
领域规模最大、覆盖面最广的会场之一。本包覆盖一次 INFOCOM 投稿的完整流程：判断项目属于 INFOCOM
还是应投 SIGCOMM、NSDI、MobiCom 或 IEEE/ACM 网络期刊；构建 INFOCOM 审稿人期望的“分析＋系统”证据；
在严格的 **IEEEtran** 双栏篇幅内准备 double-blind 的 **EDAS** 投稿；挺过自动审稿分配与
**early-reject（早期拒稿）** 阶段；直到完成 IEEE Xplore camera-ready。

官方依据核验日期：**2026-07-09**。已核验 INFOCOM 2026（东京）与 INFOCOM 2027（檀香山）的 Call for
Papers 与 Submission Guidelines 页面、Final Paper Submission Guidelines、EDAS 门户、ComSoc 会议
列表、IEEE Xplore 及 dblp。核验环境中直接抓取 `ieee-infocom.org`、`ieeexplore.ieee.org` 与统计
镜像返回 403，因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与 ComSoc 列表、IEEE/Wikipedia 的
INFOCOM 沿革、dblp 会议录及社区统计交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## INFOCOM 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 SIGCOMM/NSDI、
理论会议或 IEEE 期刊转投作者最常犯的错误：

- **它是大型旗舰，选择性来自体量。** INFOCOM 每年约 1,400-1,500 篇投稿，录用率约 **18-20%**
  （INFOCOM 2025：272/1,458 ≈ 18.7%）。规模 —— 而非小型 PC —— 决定了一切：自动审稿匹配、
  early-reject 筛选、跨子领域的庞大审稿池。
- **走 IEEE，而非 ACM/USENIX。** 论文发表于 **IEEE INFOCOM Proceedings 与 IEEE Xplore**，使用
  **IEEEtran** 双栏模板 —— `\documentclass[10pt, conference, letterpaper]{IEEEtran}`，v1.8，
  10pt Times。不要沿用 `acmart` 单栏习惯。
- **含附录在内的硬篇幅上限。** **最多 10 页**，其中 **≤9 页** 容纳所有正文、图、表 **及附录**，
  仅参考文献可占用第 10 页。评审阶段没有单独的 supplementary 通道；审稿人需要读的一切都在这九页内。
- **EDAS 上的 double-blind 与自动分配。** 投稿经 **EDAS**；PDF 必须匿名（标题页、正文、元数据）；
  论文由自动分配系统按稿件与审稿人发表记录的匹配指派给 TPC。
- **early-reject 阶段，且（传统上）无 rebuttal。** INFOCOM 2027 在最终决定（2026-12-08）前设有
  **early-reject 通知（2026-10-09）**。与 SIGCOMM/NSDI 不同，INFOCOM **传统上不提供标准的作者
  rebuttal** —— 投出的 PDF 必须自我辩护。某届是否新增回复窗口，每年 待核实。
- **每位作者五篇上限。** 一个人在某届 INFOCOM 至多出现在 **五篇** 投稿上；超出的按接收顺序丢弃。
- **系统之外的分析/优化传统。** INFOCOM 覆盖面广 —— 无线、协议、边缘/IoT、测量 —— 但保留强烈的
  **建模/理论**文化（排队论、调度、优化、博弈论、网络经济学），带证明与仿真的定理是一等贡献，而非
  二等选项。

## Skills

| Skill | 作用 |
| --- | --- |
| [`infocom-topic-selection`](skills/infocom-topic-selection/SKILL.md) | 在 INFOCOM 与同类（SIGCOMM、NSDI、MobiCom、ICNP、IEEE/ACM ToN、JSAC）间选路，用贡献形态、“建模 vs 造系统”轴与日历判断。 |
| [`infocom-workflow`](skills/infocom-workflow/SKILL.md) | 从 7 月底截止日倒排单个夏季周期，经 abstract-then-paper 两步、early-reject 检查点、通知、IEEE Xplore camera-ready 与报告。 |
| [`infocom-writing-style`](skills/infocom-writing-style/SKILL.md) | 构建网络论文骨架：先给问题与系统模型，定理或协议设计要有回报，在真实或仿真网络上评估，全部塞进九页。 |
| [`infocom-related-work`](skills/infocom-related-work/SKILL.md) | 覆盖网络文献 lane，写 delta-first 定位，并在 EDAS 上保持自引匿名。 |
| [`infocom-experiments`](skills/infocom-experiments/SKILL.md) | 让证据匹配论断形态：写清并证明假设的分析、具名仿真器与 seeds 的仿真、真实流量的 testbed/测量，以及诚实 baseline。 |
| [`infocom-reproducibility`](skills/infocom-reproducibility/SKILL.md) | 在没有正式 artifact track 的情况下让结果可核：钉死仿真配置、尽量开放代码/数据、把证明与参数留在页数内。 |
| [`infocom-supplementary`](skills/infocom-supplementary/SKILL.md) | 在含附录的九页预算内生存：决定什么进正文、什么压缩，以及为何评审阶段没有 supplementary 逃生口。 |
| [`infocom-submission`](skills/infocom-submission/SKILL.md) | EDAS 终审：abstract-then-paper 元数据步骤、IEEEtran 篇幅、double-blind 清扫、五篇上限、desk-reject 分诊。 |
| [`infocom-review-process`](skills/infocom-review-process/SKILL.md) | 建模流程 —— 大体量、自动分配、double-blind、early-reject、TPC 讨论、（传统上）无 rebuttal —— 及作者杠杆点。 |
| [`infocom-author-response`](skills/infocom-author-response/SKILL.md) | 面对现实：因通常无 rebuttal 而写出自我辩护的投稿；并在 early-reject、reject 或某届确实提供的回复窗口下正确行动。 |
| [`infocom-artifact-evaluation`](skills/infocom-artifact-evaluation/SKILL.md) | 尽管 INFOCOM 无常设 artifact-evaluation track，仍为可信度与 IEEE 复现徽章打包代码与数据，并理解该缺失带来的影响。 |
| [`infocom-camera-ready`](skills/infocom-camera-ready/SKILL.md) | 去匿名、通过 **PDF eXpress**、完成 **IEEE eCF** 版权表、满足作者注册规则、通过 IEEE Xplore 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经核验的 INFOCOM 论文，覆盖分析型、协议型与测量型贡献形态，附自检问题与同类会议防混淆提示。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构边缘调度研究的摘要与引言按 INFOCOM 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 INFOCOM 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./INFOCOM-Skills
claude plugin install infocom-skills
```

也可直接使用文件：每个 `skills/infocom-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 INFOCOM 还是 SIGCOMM/NSDI？” → `infocom-topic-selection`
- “按 INFOCOM 的 IEEEtran 篇幅与 double-blind 规则审我的稿” → `infocom-submission`
- “拿到 early-reject —— 怎么办？” → `infocom-author-response`
- “把 camera-ready 过 PDF eXpress 送进 IEEE Xplore” → `infocom-camera-ready`

## 目录结构

```text
INFOCOM-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                     # 英文说明
├── README.zh-CN.md               # 本文件
├── LICENSE                       # MIT
├── assets/cover.svg              # 封面
├── skills/
│   └── infocom-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `infocom-topic-selection`；INFOCOM 与 SIGCOMM/NSDI/MobiCom 高度重叠，按贡献
   形态与日历选择很重要。浏览 exemplars 看 INFOCOM 的分析型与系统型贡献长什么样。
2. **构建证据时** —— 让 `infocom-experiments` 与 `infocom-reproducibility` 贴着研究；仿真器 seed
   与证明假设无法事后补救。
3. **写作时** —— 用 `infocom-writing-style` 对照 worked example 打磨正文，用 `infocom-supplementary`
   守住含附录的九页预算，用 `infocom-related-work` 做 delta-first 定位。
4. **截止周** —— 提前一周录入 abstract/元数据，再用 `infocom-submission` 对 EDAS 上的匿名终稿
   逐项过审。
5. **投稿后** —— 用 `infocom-review-process` 校准预期，用 `infocom-author-response` 应对 early-reject
   检查点与任何回复窗口，随后 `infocom-camera-ready` —— 若结果不利，则用 `infocom-topic-selection`
   的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- INFOCOM 2026 为**第 45 届**：日本东京，**2026 年 5 月 18-21 日**。abstract 2025-07-24，full
  paper 2025-07-31（AoE），通知 2025-12-08，camera-ready 2026-01-09。EDAS `N33581`。
- INFOCOM 2027 为**第 46 届**：美国檀香山，**2027 年 5 月 24-27 日**；abstract 2026-07-24，full
  paper 2026-07-31（AoE）；**early-reject 2026-10-09**；录用 2026-12-08。这是 2026-07-09 时的下一个
  live 目标。
- 出版：**IEEE Xplore**。格式：**IEEEtran** 双栏，**最多 10 页 / ≤9 页正文含附录**。评审：EDAS 上
  **double-blind** ＋自动分配；每作者 ≤5 篇；传统上**无 rebuttal**（每届 待核实）。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 IEEEtran 10/9 页
   预算、EDAS double-blind 规则、early-reject 日期）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如来自统计镜像的历史录用率）。
3. **核验期不可确定项** —— 明确标为 待核实（如当届是否提供 rebuttal、是否有 artifact-evaluation
   track、完整 TPC Co-Chair 名单、AI 披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。INFOCOM 每届重定结构 —— 包括是否运行 early-reject 或任何
  rebuttal —— 每年先核验时间线。
- INFOCOM 无常任 editor-in-chief、无 APC；General 与 TPC Co-Chairs 每届轮换。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的工具
  或作者名并不能证明该论文发表于 INFOCOM（SIGCOMM/NSDI/MobiCom 表面上很像）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
