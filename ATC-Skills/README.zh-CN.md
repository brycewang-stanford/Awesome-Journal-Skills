# ATC Skills

面向 **ATC —— ACM SIGOPS Annual Technical Conference** 论文的 12 个 agent skills。该会议约五十年间
名为 **USENIX Annual Technical Conference（USENIX ATC）**，自 2026 届起转由 **ACM SIGOPS** 主办。
ATC 是系统社区**综合、务实**的会议：相比 OSDI/SOSP 这类更挑剔的旗舰会，它覆盖更宽的计算机系统面，
看重真实实现与实验结果，并设有专门的 **Operational Systems（运营系统）** 通道。本包覆盖一次 ATC
投稿的完整流程：判断项目属于 ATC 还是应投 OSDI、NSDI、EuroSys、FAST 或 workshop；应对**第一轮只读
前两页的两轮评审**；准备 double-blind 的 HotCRP 匿名投稿；利用 72 小时作者回复；处理**条件录用与
shepherding**；直到完成 camera-ready 与获得 artifact 徽章。

官方依据于 **2026-11-24 重新核验**（直接抓取）：ATC 2027 SIGOPS 主页、call for papers 与组织者页，
`atc27.hotcrp.com`，ATC 2026 主页、call 与 HotCRP 截止时钟，sysartifacts ATC 2026 页面，USENIX
ATC '25 artifact call，USENIX 停办公告，以及 ACM SIGOPS 会议列表。最初 2026-07-09 的核验因
`sigops.org`、`usenix.org` 当时返回 403，是通过搜索引擎渲染读取的。完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> **USENIX ATC 已停办。** USENIX 在 **USENIX ATC '25（2025 年 7 月）** 之后结束了 USENIX Annual
> Technical Conference；不存在 USENIX ATC '26 或之后的届次。会议以相同缩写延续为 **ACM SIGOPS
> Annual Technical Conference**（首届 SIGOPS 版本：ATC 2026，香港，2026 年 11 月）。本包现描述
> **ATC 2027**。

> 缩写冲突提醒：**ATC** 也指 *American Transplant Congress* 与某 *Academic Tax Conference*，
> **都不是**本 ATC。本包事实均不来自它们。本 ATC 是计算机系统会议。

## ATC 与同类会议的区别

以下会议机制（按 2027 cycle 核验，2026-11-24 重新核验）驱动了 skills 中的大部分建议，也对应了从
OSDI/SOSP、NSDI、旧版 USENIX ATC 乃至 ATC 2026 转投作者最常犯的错误：

- **主办方、名称与日历都变了，而且还在变。** 约五十年的 **USENIX ATC** 之后，ATC 成为 **ACM SIGOPS**
  会议。ATC 2026 于 2026 年 11 月 15-18 日在香港举行（六月截止）；**ATC 2027 于 2027 年 6 月 28 日至
  7 月 1 日在法国雷恩举行**，投稿截止 **2027 年 1 月 19 日（AoE）**。不要沿用 USENIX 时代或 2026 的假设。
- **第一轮只读前两页。** 投稿经两轮评审；**第一轮以论文前两页为准**，淘汰范围不符、动机不清、难以理解、
  贡献过小、相关工作定位不当或评估薄弱的论文。引言须自成一体。（ATC 2026 曾用单独的两页扩展摘要，
  2027 年已取消。）
- **每篇论文都有 72 小时作者回复**（2027 年 4 月 3-5 日）：只能更正事实、回答审稿人问题 —— 不得加新
  实验或数据，不得承诺后续工作。
- **上限更紧。** 长文 ≤ **12** 页、短文 ≤ **6** 页，不含参考文献但**含附录**；每位作者最多 **2** 篇投稿。
- **“综合”正是要点。** ATC 覆盖 OS、运行时、存储、网络、ML for systems / systems for ML、虚拟化、
  分布式系统、性能、可靠性、能耗与故障排查，强调**实现与实验结果**；主要贡献不在系统的论文可能被 desk reject。
- **运营系统论文是一等公民。** Operational Systems Track 以新洞见、数据或经验评判部署论文，可披露系统
  背后的机构。
- **先 double-blind，后 shepherd。** 录用论文为**条件录用**，须通过 **shepherd**；所有录用论文以口头
  和/或海报形式报告，并非每篇都有口头报告时段。
- **artifact 徽章。** 由 Artifact Evaluation Committee 在录用后单独排期评定（USENIX 传承：Available /
  Functional / Reproduced；ATC '25：94% Functional，77% Reproduced）。ATC 2027 artifact call 尚未发布。
- **开放获取与 APC。** USENIX ATC 免费公开 proceedings、slides 与视频；SIGOPS 版本以 **ACM Open
  Access** 出版，所在机构未加入 ACM Open 的作者需付 APC。

## Skills

| Skill | 作用 |
| --- | --- |
| [`atc-topic-selection`](skills/atc-topic-selection/SKILL.md) | 在 ATC 与同类会议（OSDI、SOSP、NSDI、EuroSys、FAST、HotOS/workshop）间选路，用综合性 vs 挑剔性、部署系统测试与日历判断。 |
| [`atc-workflow`](skills/atc-workflow/SKILL.md) | 从 2027 年 1 月 19 日截止倒排年度计划，经两轮评审、72 小时回复、条件录用 shepherding、artifact 评审与 5 月 28 日 camera-ready。 |
| [`atc-writing-style`](skills/atc-writing-style/SKILL.md) | 构建系统论文：能独立通过第一轮的前两页、实现-测量叙事、两栏格式下的篇幅纪律。 |
| [`atc-related-work`](skills/atc-related-work/SKILL.md) | 覆盖系统文献 lane，对照 OSDI/NSDI/EuroSys/FAST 定位，并保持自引 double-blind。 |
| [`atc-experiments`](skills/atc-experiments/SKILL.md) | 让证据匹配论断：真实 testbed、诚实 baseline、端到端加 microbenchmark、尾延迟与方差、负载真实性。 |
| [`atc-reproducibility`](skills/atc-reproducibility/SKILL.md) | 构建 artifact 证据：钉死环境、通往关键数字的一键路径、匿名可运行的评审包。 |
| [`atc-supplementary`](skills/atc-supplementary/SKILL.md) | 按评审轮次与决策重要性划分前两页、正文、计入页数的附录与 artifact。 |
| [`atc-submission`](skills/atc-submission/SKILL.md) | HotCRP 终审：含附录的 12/6 页篇幅、每人两篇上限、double-blind 清扫、AoE 截止前的 desk-reject 分诊。 |
| [`atc-review-process`](skills/atc-review-process/SKILL.md) | 建模流程 —— 两轮（前两页门槛）、72 小时回复、条件录用、shepherding、口头 vs 海报 —— 及作者杠杆点。 |
| [`atc-author-response`](skills/atc-author-response/SKILL.md) | 撰写 72 小时作者回复、重投修改说明，以及 shepherd 会逐条核对的 description-of-changes。 |
| [`atc-artifact-evaluation`](skills/atc-artifact-evaluation/SKILL.md) | 在 AEC 自身截止日，将录用论文的包转化为 Available / Functional / Reproduced 徽章。 |
| [`atc-camera-ready`](skills/atc-camera-ready/SKILL.md) | 去匿名、完成 shepherd 要求的修改、补全 ACM Open Access 元数据、通过生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十四个带 URL 与访问日期的来源；已核验 ATC 2027 事实；ATC 2026 与 USENIX ATC 历史；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口（SIGOPS CFP、ATC HotCRP、USENIX 遗留页、ACM DL）与网关阻断时的交叉核对来源。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经核验的 USENIX ATC 论文，覆盖多种贡献形态（含 Test-of-Time 与 Best Paper），附自检问题与同类会议护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构存储缓存论文的前两页（摘要+引言）按 ATC 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 ATC 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./ATC-Skills
claude plugin install atc-skills
```

也可直接使用文件：每个 `skills/atc-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 ATC 还是 OSDI/NSDI？” → `atc-topic-selection`
- “按 ATC 2027 规则审我的稿” → `atc-submission`
- “让前两页能过第一轮” → `atc-writing-style`
- “拿到条件录用 —— 规划 shepherd 修改” → `atc-author-response`
- “把 artifact 准备到 ATC 徽章标准” → `atc-artifact-evaluation`

## 目录结构

```text
ATC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── atc-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `atc-topic-selection`；ATC 与 OSDI/NSDI/EuroSys/FAST 重叠，综合性 vs 挑剔性
   的取舍与一月截止的日历很重要。浏览 exemplars 看有持久影响力的 ATC 贡献长什么样。
2. **构建证据时** —— 让 `atc-experiments` 与 `atc-reproducibility` 贴着系统；testbed provenance
   与钉死的环境无法在投稿期补救。
3. **写作时** —— 用 `atc-writing-style` 打磨可独立成立的前两页与正文，用 `atc-supplementary`
   划分前两页/正文/附录/artifact，用 `atc-related-work` 做同类会议感知的定位。
4. **截止周** —— 用 `atc-submission` 对论文上传、作者上限与 double-blind 清扫逐项过审，赶在 2027 年
   1 月 19 日 AoE 截止前完成。
5. **投稿后** —— 用 `atc-review-process` 校准两轮预期，用 `atc-author-response` 应对 72 小时回复与
   shepherd 的 description-of-changes，随后 `atc-artifact-evaluation` 与 `atc-camera-ready` ——
   若结果不利，则用 `atc-topic-selection` 的路由表改投。

## 2027 周期锚点事实（带日期的快照，非永久规则）

- ATC 2027 为**第二届 ACM SIGOPS Annual Technical Conference**：**法国雷恩 Le Couvent des Jacobins，
  2027 年 6 月 28 日至 7 月 1 日**。General Chair David Bromberg；PC Chairs Vijay Chidambaram、
  Peter Pietzuch；AE Chairs Miguel Matos、Valerio Schiavoni。
- **日期：**投稿 **2027-01-19**（AoE，不延期）；作者回复 **2027-04-03 至 04-05**（72 小时）；通知
  **2027-04-27**；camera-ready **2027-05-28**。HotCRP：`atc27.hotcrp.com`。
- **评审：**两轮，第一轮以前两页为准；每篇均可提交作者回复。长文 **≤12 页**、短文 **≤6 页**（不含参考
  文献，含附录）；**两栏**，178×229 mm，10pt，`\documentclass[sigplan,10pt]{acmart}`。**Double-blind。**
  **每位作者 ≤2 篇。** **条件录用 + shepherding**；口头和/或海报报告。
- **出版：**ACM Open Access（ACM Open 之外的作者需付 APC；ATC CFP 未给出金额）。
- **历史：**ATC 2026（首届 SIGOPS 版本）于 2026 年 11 月 15-18 日在香港举行，截止 **2026-06-10**，
  第一轮评两页扩展摘要。USENIX ATC '25（2025 年 7 月）是最后一届 USENIX 版本。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如前两页第一轮、含附录的
   12/6 页篇幅、每人两篇上限）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如往届投稿数量）。
3. **核验期不可确定项** —— 明确标为 待核实（如 ATC 2027 artifact call 与徽章集合、camera-ready 页数、
   ATC 论文适用的具体 APC）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- ATC 仍在转型后调整：ATC 2026 同时改了名称、主办方、出版方与日历，ATC 2027 又取消扩展摘要、把截止
  移到一月、把附录计入页数并新增每人两篇上限。每项都要对照当前 SIGOPS call 重新核验 —— 尚无一项是稳定
  永久规则。
- ATC 无常任 editor-in-chief；chairs 每届在 SIGOPS 下轮换。USENIX 遗留的 ATC proceedings、slides
  与视频仍在 USENIX 站点；新版本在 ACM DL 以 Open Access 出版。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 著名系统
  名并不能证明该论文发表于 ATC（许多里程碑系统论文在 OSDI/SOSP/NSDI，而非 ATC）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
