# ESEC/FSE Skills

面向 **ESEC/FSE —— ACM International Conference on the Foundations of Software Engineering**
论文的 12 个 agent skills。FSE 是 ACM SIGSOFT 旗舰会议，与 ICSE 并列为软件工程两大综合旗舰之一。
本包覆盖一次 FSE 投稿的完整流程：判断项目属于 FSE 还是应投 ICSE、ASE、ISSTA 或 SE 期刊；构建能
经受 SE 审稿人审视的实证证据；准备 double-anonymous 的 HotCRP 投稿及其 open-science 义务；应对
PACMSE 的 **journal-style Major Revision**；直到完成 PACMSE camera-ready 与获得 ACM artifact 徽章。

官方依据核验日期：**2026-07-09**。已核验 FSE 2026 与 FSE 2027 research track 的 call 与
Important Dates 页面、PACMSE 期刊页面、FSE HotCRP 站点、ACM Artifact Review and Badging 政策，以及
SIGSOFT/ESEC-FSE 奖项页面。核验环境中直接抓取 `conf.researchr.org` 与 `dl.acm.org` 返回 403，
因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与 ACM Digital Library（PACMSE）、dblp 及 FSE
HotCRP 交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名冲突提醒：`fse.iacr.org` 是密码学会议 *Fast Software Encryption*，**不是**本 FSE。本包中的
> 事实均不来自该会议。

## FSE 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 ICSE、PL/ML
会议或 SE 期刊转投作者最常犯的错误：

- **论文即期刊文章。** FSE research paper 发表在 **PACMSE（Proceedings of the ACM on Software
  Engineering）**，一本 open-access 的 ACM 期刊（Vol 1 = FSE 2024，Vol 2 = FSE 2025，
  Vol 3 = FSE 2026）。投稿按期刊稿件评审，同时获得会议报告席位。
- **Major Revision 是真实的期刊式返修轮。** 首轮决定为 Accept、**Major Revision** 或 Reject；
  Major Revision 是真正的 revise-and-resubmit，由原审稿人复审，需附匿名的逐条回复信 —— 更接近
  期刊 R&R 而非 rebuttal。
- **（当前）每年单一 research 截止日，但有前提。** FSE 2026 于 2025-09-11 截止；FSE 2027 于
  2026-10-02 截止。FSE 2024 曾试行双截止日模型；每年是一个还是两个截止日由当届决定 —— 先核验
  cadence。
- **Heavy double-anonymity。** 匿名贯穿所有评审与 discussion，甚至 Major Revision 回复信本身也
  必须匿名。
- **走 ACM 路线，而非 IEEE。** FSE 使用 **ACM Primary Article Template**，单栏、篇幅较宽松
  （FSE 2027：正文含图 ≤18 页 + 4 页参考文献）—— 不是 ICSE 的 IEEE 10+2。不要沿用 IEEEtran 习惯。
- **默认 open science 与 ACM badging。** 评审阶段即期望提供 Data Availability 声明与匿名可运行
  artifact；ACM 徽章（Available / Functional / Reusable / Reproduced）在录用后另设截止日评定。
- **实证 SE 的证据文化。** research-question 契约、真实 subject systems、公平 baseline、effect
  size 与 threats-to-validity 论证，是审稿群体即便无明文规定也会执行的社区规范。

## Skills

| Skill | 作用 |
| --- | --- |
| [`fse-topic-selection`](skills/fse-topic-selection/SKILL.md) | 在 ESEC/FSE 与同类会议（ICSE、ASE、ISSTA、MSR、ICSME、EMSE/TSE/TOSEM）之间选路，用贡献形态、model-swap 与 re-label 测试及日历判断。 |
| [`fse-workflow`](skills/fse-workflow/SKILL.md) | 从截止日倒排单周期年度计划，经注册、Major Revision 轮、artifact 评审、PACMSE camera-ready 与报告。 |
| [`fse-writing-style`](skills/fse-writing-style/SKILL.md) | 构建实证 SE 骨架：首页给出 SE 贡献、RQ 契约、会论证的 threats、篇幅纪律。 |
| [`fse-related-work`](skills/fse-related-work/SKILL.md) | 覆盖 SE 文献 lane，写 delta-first 定位，并保持自引匿名。 |
| [`fse-experiments`](skills/fse-experiments/SKILL.md) | 让证据匹配论断形态：真实 subject、公平 baseline、SE 统计与 effect size、定性严谨、防污染 LLM ablation、mining provenance。 |
| [`fse-reproducibility`](skills/fse-reproducibility/SKILL.md) | 构建 open-science 证据：诚实的 Data Availability 声明、provenance pinning、匿名可运行 artifact。 |
| [`fse-supplementary`](skills/fse-supplementary/SKILL.md) | 按决策重要性划分正文与 artifact —— 决定录用的证据不得置于正文之外。 |
| [`fse-submission`](skills/fse-submission/SKILL.md) | HotCRP 终审：两步注册+投稿、ACM 模板与篇幅、heavy 匿名清扫、open-science 项、desk-reject 分诊。 |
| [`fse-review-process`](skills/fse-review-process/SKILL.md) | 建模流程 —— heavy double-anonymity、≥3 审稿人、Accept/Major Revision/Reject、期刊式复审 —— 及作者的杠杆点。 |
| [`fse-author-response`](skills/fse-author-response/SKILL.md) | 撰写两轮：初审 rebuttal 与把每条要求映射到 tracked change 的匿名 Major Revision 回复信。 |
| [`fse-artifact-evaluation`](skills/fse-artifact-evaluation/SKILL.md) | 在 artifact track 自身截止日，将录用论文的包转化为 ACM 徽章（Available / Functional / Reusable / Reproduced）。 |
| [`fse-camera-ready`](skills/fse-camera-ready/SKILL.md) | 系统去匿名、补全 PACMSE 期刊元数据、把可用性链接永久化、通过 ACM 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 FSE 论文，覆盖五种贡献形态（含 Test-of-Time 与 Distinguished Paper），附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构 review-bot 研究的摘要与引言按 FSE 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 FSE 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./FSE-Skills
claude plugin install fse-skills
```

也可直接使用文件：每个 `skills/fse-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 FSE 还是 ICSE/ISSTA？” → `fse-topic-selection`
- “按 FSE research-track 规则审我的稿” → `fse-submission`
- “拿到 Major Revision —— 规划回复信” → `fse-author-response`
- “把 artifact 准备到 ACM 徽章标准” → `fse-artifact-evaluation`

## 目录结构

```text
FSE-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── fse-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `fse-topic-selection`；FSE 与 ICSE 高度重叠，按日历与社区取向选择很重要。
   浏览 exemplars 看十年影响力的 FSE 贡献长什么样。
2. **构建证据时** —— 让 `fse-experiments` 与 `fse-reproducibility` 贴着研究；设计期命名的 threats
   与采集期钉死的 provenance 无法事后补救。
3. **写作时** —— 用 `fse-writing-style` 对照 worked example 打磨正文，用 `fse-supplementary` 划分
   正文/artifact，用 `fse-related-work` 做 delta-first 定位。
4. **截止周** —— 先在较早的注册截止日前完成注册，再用 `fse-submission` 对终稿 PDF 与 artifact
   逐项过审。
5. **投稿后** —— 用 `fse-review-process` 校准预期，用 `fse-author-response` 应对 rebuttal 与任何
   Major Revision 轮，随后 `fse-artifact-evaluation` 与 `fse-camera-ready` —— 若结果不利，则用
   `fse-topic-selection` 的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- FSE 2026 为**第 34 届**：加拿大蒙特利尔（Concordia SGW 校区），**2026 年 7 月 5-9 日**。research
  注册 2025-09-04，投稿 2025-09-11（AoE）。General Chairs：Shin Hwei Tan 与 Foutse Khomh。
- FSE 2027 为**第 35 届**：中国深圳，**2027 年 7 月 12-16 日**；research 截止 **2026-10-02**（AoE）；
  篇幅 **≤18 页**正文含图 **+ 4** 页参考文献；每篇 **≥3** 名 PC 审稿人。这是 2026-07-09 时的下一个
  live research 目标。
- 出版：**PACMSE**，open access，无 APC。评审：**double-anonymous “heavy”**。决定：Accept /
  **Major Revision** / Reject。模板：**ACM Primary Article Template**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 PACMSE 出版、
   FSE 2027 的 18+4 篇幅、heavy 匿名规则）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如超出已具名 General Chairs 的完整组委名单）。
3. **核验期不可确定项** —— 明确标为 待核实（如 FSE 2026/2027 完整 Program Co-Chair 名单、artifact
   track 截止日、任何 AI 使用披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。FSE 每届重定结构 —— 包括截止日数量（FSE 2024 与后续年份不同）——
  每年先核验 cadence。
- FSE 无常任 editor-in-chief、无 APC；chairs 每届轮换。即便**出版物**是期刊，也不要对**人**做
  期刊式连续性假设。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的工具名
  并不能证明该论文发表于 FSE。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
