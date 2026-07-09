# ICDT Skills

面向 **ICDT —— International Conference on Database Theory（国际数据库理论会议）** 论文的 12 个
agent skills。ICDT 是欧洲的数据管理基础理论会议，与 **EDBT** 联合举办（EDBT/ICDT 联合活动），论文以
**开放获取**方式发表于 **LIPIcs**（Schloss Dagstuhl）。本包覆盖一次 ICDT 投稿的完整流程：判断项目属于
ICDT 还是应投 **PODS**、同址的 EDBT 系统方向、纯理论会议（LICS/ICALP/STACS）或期刊；撰写带匹配上下界的
theorem-proof 论文；以 **匿名** 方式、按 **`lipics-v2021`** 15 页格式（附完整证明附录）打包投稿；应对
**每年两个提交轮次** 及其 **第一轮 revision** 机制；直至完成 LIPIcs camera-ready 与归档 full version。

官方依据核验日期：**2026-07-09**。已核验 ICDT 2026 与 ICDT 2027 在 databasetheory.org 的 call、
EDBT/ICDT 2026（Tampere）与 2027（Lille）活动站点、DROPS/LIPIcs 系列与 ICDT 2026 会议卷、
`lipics-v2021` 作者说明、Microsoft CMT 投稿系统，以及 ICDT 奖项页面。核验环境中直接抓取
`databasetheory.org`、`drops.dagstuhl.de` 及活动站点失败/返回 403，因此通过搜索引擎对精确 URL 的渲染
阅读官方页面，并与 dblp、DROPS 卷页、CMT/EasyChair 的 CfP 及邮件列表存档交叉核对；完整记录（含所有
待核实 项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名冲突提醒：SID 的 *International Conference on Display Technology*（`sidicdt.org`）与 IARIA 的
> *International Conference on Digital Telecommunications* 也缩写为 “ICDT”，**均不是**本会议。本包中的
> 事实均不来自它们。

## ICDT 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 PODS、系统会议或纯理论
会议转投作者最常犯的错误：

- **开放获取 LIPIcs，而非 ACM/IEEE。** ICDT 论文发表于 **LIPIcs（Leibniz International Proceedings in
  Informatics）**，Schloss Dagstuhl，采用 **CC-BY 4.0**，在 **DROPS** 上带 DOI，作者无 APC。
  camera-ready 是**纯 LaTeX 的 `lipics-v2021`** 文档 —— 这是与 **PODS**（research 论文现发表于 ACM
  **PACMMOD**）的实质出版差异。
- **与 EDBT 同址。** ICDT 在 **EDBT/ICDT** 联合活动内举办（2026 Tampere，2027 Lille），与 EDBT 系统方向
  共享同一周与场地 —— 同一楼、不同评审文化：ICDT 要证明，EDBT 要系统。
- **每年两个提交轮次。** ICDT 每年设 **两个截止日**（ICDT 2027：论文 2026-03-10 与 2026-09-10，AoE）。
  **第一轮带 revision 选项**；在第一轮被 **拒** 的论文 **不得** 投入第二轮，除非审稿人明确邀请。
- **自 2024 起匿名评审。** 常规 track 投稿不含作者姓名、单位或致谢。（简短的 **Database Theory in
  Action** track **不** 匿名。）
- **要求完整证明。** ICDT 是证明型会议：15 页正文（不含参考文献）给出结果与思路，**明确标注的附录**
  （由 PC 酌情阅读）放完整证明，**不允许在线附录**，并由 arXiv **full version** 在发表后承载全部证明。
- **紧界、精确模型的文化。** 匹配的上下界、明确的 data / combined / query 复杂度度量、固定的数据与查询
  模型，是数据库理论审稿群体即便无明文规定也会执行的社区规范。

## Skills

| Skill | 作用 |
| --- | --- |
| [`icdt-topic-selection`](skills/icdt-topic-selection/SKILL.md) | 在 ICDT 与同类（PODS、同址 EDBT、LICS/ICALP/STACS、TODS/LMCS/TheoretiCS 等期刊）之间选路，用贡献形态、日历以及 open-access LIPIcs vs PACMMOD 判断。 |
| [`icdt-workflow`](skills/icdt-workflow/SKILL.md) | 从所选截止日倒排两轮年度计划，经摘要注册、第一轮 revision、LIPIcs camera-ready 与 EDBT/ICDT 报告。 |
| [`icdt-writing-style`](skills/icdt-writing-style/SKILL.md) | 构建 theorem-proof 骨架：先固定数据与计算模型、尽早给出结果、正文放思路证明放附录，控制在 15 页内。 |
| [`icdt-related-work`](skills/icdt-related-work/SKILL.md) | 覆盖数据库理论各 lane，针对最近的先前界做 delta-first 定位，并保持自引匿名。 |
| [`icdt-experiments`](skills/icdt-experiments/SKILL.md) | 让证据匹配论断：以匹配界与构造为主要证据，仅在少见的算法型论文中做成比例的实验。 |
| [`icdt-reproducibility`](skills/icdt-reproducibility/SKILL.md) | 理论会议的“可复现”对应物：完整自洽的证明、钉死的模型、匹配的界，以及正文与 full version 的一致性。 |
| [`icdt-supplementary`](skills/icdt-supplementary/SKILL.md) | 在 15 页正文与标注附录间划分内容 —— 不允许在线附录，被评审的对象是单一 PDF。 |
| [`icdt-submission`](skills/icdt-submission/SKILL.md) | CMT 终审：选轮次、摘要+论文两步截止、`lipics-v2021` 与篇幅、匿名清扫、完整证明检查、desk-reject 分诊。 |
| [`icdt-review-process`](skills/icdt-review-process/SKILL.md) | 建模流程 —— 两轮、匿名评审、Accept/Revise/Reject、跨轮 carry 规则、证明正确性审查 —— 及作者杠杆点。 |
| [`icdt-author-response`](skills/icdt-author-response/SKILL.md) | 撰写第一轮 revision：逐条补上被指出的证明缺口、记录改动、保持修订稿匿名。 |
| [`icdt-artifact-evaluation`](skills/icdt-artifact-evaluation/SKILL.md) | 理解 ICDT 无代码 artifact track：把 proof-artifact（标注附录 + arXiv full version）做扎实，而非追 ACM 徽章。 |
| [`icdt-camera-ready`](skills/icdt-camera-ready/SKILL.md) | 去匿名、补全 LIPIcs 元数据（CCS、keywords、ORCID）、链接 full version、在 CC-BY 下通过 Dagstuhl/DROPS 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 四篇经存档核验的 ICDT Test-of-Time 论文，覆盖四种贡献形态，附自检问题与同类会议防混淆提示。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构一致性查询回答结果的摘要与引言按 ICDT 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 为何 ICDT 无代码 artifact，以及通用工具无法完成的 proof-artifact 检查清单。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./ICDT-Skills
claude plugin install icdt-skills
```

也可直接使用文件：每个 `skills/icdt-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 ICDT 还是 PODS/EDBT？” → `icdt-topic-selection`
- “按 ICDT 常规 track 规则审我的稿” → `icdt-submission`
- “拿到第一轮 revise —— 规划修订” → `icdt-author-response`
- “准备 LIPIcs camera-ready” → `icdt-camera-ready`

## 目录结构

```text
ICDT-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── icdt-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # proof-artifact 适配（无代码 track）
```

## 建议用法

1. **动笔前** —— 先跑 `icdt-topic-selection`；ICDT 与 PODS 几乎完全重叠，按日历与出版模式选择很重要。
   浏览 exemplars 看十年影响力的 ICDT 贡献长什么样。
2. **证明阶段** —— 让 `icdt-experiments` 与 `icdt-reproducibility` 贴着结果；匹配界与自洽证明无法在截止
   前补救。
3. **写作时** —— 用 `icdt-writing-style` 对照 worked example 打磨 theorem-proof 正文，用
   `icdt-supplementary` 划分正文/附录，用 `icdt-related-work` 做 delta-first 定位。
4. **截止周** —— 在所选轮次较早的摘要截止日前完成注册，再用 `icdt-submission` 对终稿 PDF 逐项过审。
5. **投稿后** —— 用 `icdt-review-process` 校准预期，用 `icdt-author-response` 应对第一轮 revision，随后
   `icdt-camera-ready` —— 若结果不利，则用 `icdt-topic-selection` 的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- ICDT 2026 为**第 29 届**，属 **EDBT/ICDT 2026**，芬兰 Tampere；会议录为 **LIPIcs 第 365 卷**。评审
  主席 **Balder ten Cate**（ILLC，阿姆斯特丹大学）。活动日期在不同渲染间有出入（3 月 24-27 vs 3 月
  9-14），标为 **待核实**。
- ICDT 2027 为**第 30 届**，属 **EDBT/ICDT 2027**，**法国 Lille，2027 年 4 月 6-9 日**；PC 主席
  **Stijn Vansummeren**（Hasselt 大学）。**两个轮次：** 论文 **2026-03-10**（第一轮，通知 2026-06-01）
  与 **2026-09-10**（第二轮，通知 2026-12-01），AoE。截至 2026-07-09，**第二轮是当前 live 目标**。
- 出版：**LIPIcs**，open access，**CC-BY 4.0**，DROPS 上带 DOI，作者无 APC。评审：**匿名**（常规
  track），**两轮**含 **第一轮 revision**。格式：**`lipics-v2021`，正文 15 页（不含参考文献）**，标注
  附录，不允许在线附录。系统：**Microsoft CMT**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 LIPIcs 出版、
   `lipics-v2021` 15 页格式、两轮日历、2024 起匿名评审）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如 EDBT/ICDT 活动内 ICDT 的确切会期）。
3. **核验期不可确定项** —— 明确标为 待核实（如 ICDT 2026 日期出入、完整 PC 名单、任何生成式 AI 披露
   政策、是否设简短 rebuttal 环节）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。ICDT 每届重定结构 —— 包括哪些轮次运行及其日期 —— 每年先核验 cadence。
- ICDT 无常任 editor-in-chief、作者无 APC；PC 主席每届轮换。对**人**做连续性假设视为错误。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾
  的核验流程 —— 熟悉的结果并不能证明该论文发表于 ICDT（许多是 PODS 或期刊论文）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
