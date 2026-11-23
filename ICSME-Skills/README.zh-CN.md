# ICSME Skills

面向 **ICSME —— IEEE International Conference on Software Maintenance and Evolution（IEEE 软件维护
与演化国际会议）** 论文的 12 个 agent skills。ICSME 是软件"首次发布之后"生命周期的专属会议：维护、
演化、逆向工程、程序理解、技术债、重构，以及 mining-software-repositories（仓库挖掘）证据。本包覆盖
一次 ICSME 投稿的完整流程：判断项目是否 ICSME-shaped（以及适合哪个 ICSME track），还是应投 ICSE、
FSE、SANER、MSR 或 SCAM；构建能经受审稿人审视的维护实证证据；准备 double-anonymous 的 EasyChair
投稿（IEEEtran 10+2 篇幅）及其 open-science 义务；应对**单轮**评审的 early-decision 分流与
author-response rebuttal；直到完成 IEEE Xplore camera-ready 与获得 ROSE-Festival artifact 徽章。

官方依据首次核验于 **2026-07-09**（ICSME 2026），并于 **2026-11-23 复核**，改以已上线的
**ICSME 2027** 页面为准：research-papers call、Important Dates、组委会、open-science policy，以及
Journal-First / Registered Reports / Artifact Evaluation / Benchmark & Dataset track 页面，均直接
抓取 `conf.researchr.org` 读取。完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名提醒：本会议 2013 年前称 **ICSM**，2014 年起加入 "and Evolution" 改称 **ICSME**。在 ICSME
> 20XX 颁发的 10 年 Most Influential Paper 表彰的是 ICSM 20(XX-10) 的论文。

## ICSME 与同类会议的区别

以下会议机制（按 2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 ACM 系会议、从 ICSE/FSE
或从技术优先会议转投作者最常犯的错误：

- **它是维护/演化会议。** ICSME 奖励扎根于**发布后生命周期**的贡献 —— 老化系统、变更影响、技术债、
  重构安全性、程序理解、软件如何演化 —— 而非维护收益只是附带的 greenfield 技术。
- **走 IEEE 路线，而非 ACM。** ICSME 使用 **IEEEtran 双栏**模板，发表于 **IEEE Xplore**，颁发
  **IEEE** artifact 徽章。2027 篇幅为**正文含图与附录 10 页 + 2 页纯参考文献**（与 2026 相同）。不要沿用 ACM
  `acmart` 单栏习惯。
- **单一 research 轮 —— 无 Major Revision。** research track 对每篇论文双盲评审一次，然后 accept 或
  reject。与 ESEC/FSE 的期刊式 revise-and-resubmit 不同，没有返修轮：证据必须在投稿时就完整。
- **Early-decision 分流 + author-response rebuttal。** 回复期开始时，最强与最弱的论文已直接收到
  Accept 或 Reject；其余收到 "Response Recommended"，在单次 rebuttal 中回答 PC 的具体问题。
- **EasyChair，先摘要后全文。** 通过 EasyChair 投稿，全文截止前约一周需完成摘要注册 —— 不是
  HotCRP、CMT 或 OpenReview。
- **丰富的备选 track。** 强势的 **Journal-First（J1C2）** track 让 TSE/EMSE 论文在会上报告；
  **Registered Reports**（与 EMSE 合作）先评审 protocol；新增 **Benchmark & Dataset Track** 接收数据
  与基准论文。**RENE**（复制与负结果）track 办到 2026 届，ICSME 2027 的 track 列表中已没有它；复制
  研究现投 research track（该 track 明确评估 replicability）。
- **默认 open science 与 ROSE。** **Joint Artifact Evaluation Track and ROSE Festival**（与同址
  SCAM、VISSOFT 共享）颁发 IEEE **Open Research Object** 与 **Research Object Reviewed** 徽章；
  open-science policy 把数据共享设为评审阶段的默认（不共享须在文中说明理由）。
- **AI 使用按 IEEE 规则披露。** 作者遵循 IEEE 的 AI 生成内容指南：注明所用 AI 系统及使用的章节。

## Skills

| Skill | 作用 |
| --- | --- |
| [`icsme-topic-selection`](skills/icsme-topic-selection/SKILL.md) | 在 ICSME 与同类会议（ICSE、FSE、SANER、MSR、ICPC、SCAM、TSE/EMSE）之间选路，用 lifecycle 与 re-label 测试，并选定 ICSME track（research / journal-first / registered report / RENE / NIER / tool-demo / industry）。 |
| [`icsme-workflow`](skills/icsme-workflow/SKILL.md) | 从摘要截止日倒排单轮年度计划，经 early-decision 分流、author-response rebuttal、IEEE Xplore camera-ready 与 ROSE-Festival artifact。 |
| [`icsme-writing-style`](skills/icsme-writing-style/SKILL.md) | 构建维护实证骨架：首页给出维护贡献、RQ 契约、会论证的 threats、10 页 IEEEtran 纪律。 |
| [`icsme-related-work`](skills/icsme-related-work/SKILL.md) | 覆盖维护/演化文献 lane，写 delta-first 定位，为 RENE 界定复制框架，并保持自引匿名。 |
| [`icsme-experiments`](skills/icsme-experiments/SKILL.md) | 让证据匹配论断形态：真实演化 subject、mining provenance、公平 baseline、SE 统计、survivorship 与变更历史混杂、防污染 LLM ablation。 |
| [`icsme-reproducibility`](skills/icsme-reproducibility/SKILL.md) | 构建 open-science 证据：诚实的 data-availability 声明、钉死的 mining/LLM provenance、投稿时即完整的匿名可运行 artifact。 |
| [`icsme-supplementary`](skills/icsme-supplementary/SKILL.md) | 按决策重要性划分 10 页正文与 artifact —— 决定录用的证据不得置于正文之外。 |
| [`icsme-submission`](skills/icsme-submission/SKILL.md) | EasyChair 终审：先摘要后全文两步、IEEEtran 篇幅、双盲清扫（含自有系统泄露）、open-science 项、desk-reject 分诊。 |
| [`icsme-review-process`](skills/icsme-review-process/SKILL.md) | 建模流程 —— 双盲、early-decision 分流、"Response Recommended"、单轮 accept/reject —— 及作者杠杆点。 |
| [`icsme-author-response`](skills/icsme-author-response/SKILL.md) | 撰写单轮 rebuttal：先看自己属于哪一档，用已有证据回答 PC 的具体问题，并保持匿名。 |
| [`icsme-artifact-evaluation`](skills/icsme-artifact-evaluation/SKILL.md) | 在与 SCAM/VISSOFT 共享的 artifact 截止日，将录用论文的包转化为 IEEE ROSE 徽章（Open Research Object / Research Object Reviewed）。 |
| [`icsme-camera-ready`](skills/icsme-camera-ready/SKILL.md) | 系统去匿名、补全 IEEE 元数据与 eCopyright、落实 response 承诺、把可用性链接永久化、通过 IEEE Xplore 检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十一个带 URL 与访问日期的来源；已核验 2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 ICSM/ICSME 论文，覆盖五种贡献形态（含 Most Influential Paper），附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构的依赖更新机器人研究，摘要与引言按 ICSME 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 ICSME 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./ICSME-Skills
claude plugin install icsme-skills
```

也可直接使用文件：每个 `skills/icsme-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- "这篇该投 ICSME 还是 MSR/SANER？" → `icsme-topic-selection`
- "按 ICSME research-track 规则审我的稿" → `icsme-submission`
- "拿到 'Response Recommended' —— 规划 rebuttal" → `icsme-author-response`
- "把 artifact 准备到 ROSE 徽章标准" → `icsme-artifact-evaluation`

## 目录结构

```text
ICSME-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面
├── skills/
│   └── icsme-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `icsme-topic-selection`；ICSME 与 ICSE/FSE 及演化同类会议重叠，且 track 众多，
   选对**会议与 track**都很重要。浏览 exemplars 看十年影响力的维护贡献长什么样。
2. **构建证据时** —— 让 `icsme-experiments` 与 `icsme-reproducibility` 贴着研究；采集期钉死的 mining
   provenance 无法事后补救，且没有返修轮可补。
3. **写作时** —— 用 `icsme-writing-style` 对照 worked example 打磨正文，用 `icsme-supplementary`
   划分正文/artifact，用 `icsme-related-work` 做 delta-first 定位。
4. **截止周** —— 先在较早的摘要截止日前完成注册，再用 `icsme-submission` 对终稿 PDF 与 artifact
   逐项过审。
5. **投稿后** —— 用 `icsme-review-process` 校准预期，若收到 "Response Recommended" 则用
   `icsme-author-response`，随后 `icsme-artifact-evaluation` 与 `icsme-camera-ready` —— 若结果不利，
   则用 `icsme-topic-selection` 的路由表改投。

## 2027 周期锚点事实（快照，非永久规则）

- ICSME 2027 为**第 43 届**：加拿大多伦多（York University），**2027 年 9 月 7-11 日**，SCAM、VISSOFT
  论文共用 artifact track。research 摘要 2027-02-19、全文 2027-02-26、early decisions 2027-04-26、
  author response 2027-04-27 至 04-30、通知 2027-05-25、camera-ready 2027-06-25（均 AoE）；经
  **EasyChair** 投稿（2026-11-23 时链接仍为 TBD）。General Co-Chairs：Gias Uddin、Song Wang；Program
  Co-Chairs：Shiva Nejati、Lei Ma。
- 上一届：ICSME 2026（第 42 届），意大利贝内文托，2026 年 9 月 14-18 日。
- 格式：**IEEEtran 双栏**，正文含图与附录 **10 页 + 2** 页参考文献。评审：**double-anonymous**、
  **单轮**，含 **early-decision 分流**与 **author-response** rebuttal —— **无 Major Revision**。
- Tracks（2027）：Research、**Journal-First（J1C2）**、**Registered Reports**、**Benchmark & Dataset**
  （新增）、NIER、Tool Demonstration and Data Showcase、Industry、Posters、Doctoral Symposium。RENE
  （复制与负结果）2026 届仍有，2027 列表中已无。
- Artifacts：**Joint Artifact Evaluation Track and ROSE Festival**，IEEE **Open Research Object** /
  **Research Object Reviewed** 徽章，录用后，与 SCAM/VISSOFT 共享。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 10+2 篇幅、单轮
   early-decision 模型、ROSE 的 IEEE 徽章）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如 research track 之外各 track 的确切截止日）。
3. **核验期不可确定项** —— 明确标为 待核实（如 ICSME 2027 EasyChair 链接、Journal-First 与
   Registered Reports 的 2027 截止日、注册费）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。ICSME 每届重定结构 —— 包括是否保留先摘要后全文两步与
  early-decision 分流 —— 每年先核验当届 Important Dates 页面。
- ICSME 无常任 editor-in-chief、无 APC；chairs 在 IEEE TCSE 下每届轮换。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的维护
  主题并不能证明该论文发表于 ICSM/ICSME（许多其实是 TSE、ICSE 或 MSR）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
