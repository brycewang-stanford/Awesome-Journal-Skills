# EDBT Skills

面向 **EDBT —— International Conference on Extending Database Technology（扩展数据库技术国际会议）**
论文的 12 个 agent skills。EDBT 是欧洲数据库系统旗舰会议，与 **ICDT**（其数据库理论姊妹会议）
联合举办，论文以 **open access 形式发表于 OpenProceedings.org**，并采用独特的
**多轮滚动投稿模型（multiple-cycle rolling submission）** 而非单一年度截止日。本包覆盖一次 EDBT
投稿的完整流程：判断项目属于 EDBT 还是应投 SIGMOD、VLDB、ICDE 或 ICDT；选择投稿 cycle 与论文类型
（Regular、Experiments & Analysis 或 Vision）；准备 Microsoft CMT 投稿；应对 cycle 内的
**revise-and-resubmit（返修重投）** 轮；直到完成 OpenProceedings camera-ready 与可复现 artifact。

官方依据核验日期：**2026-07-09**。已核验 EDBT/ICDT 2026（Tampere）research 与 industrial call、
`edbt.org` 的 EDBT Association 页面、EDBT 2027 的 cycle 截止日、OpenProceedings.org 卷页面及 dblp。
核验环境中直接抓取 `edbticdt2026.github.io`、`edbt.org` 与 `openproceedings.org` 均返回 403，
因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与 OpenProceedings 目录、dblp、WikiCFP 及
`databasetheory.org` 上的 ICDT call 交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 缩写冲突提醒：**EDBT 是数据库会议**，不是 EDTM（IEEE 电子器件技术与制造会议）或其他相似缩写的
> 会议。本包中的事实均不来自任何非数据库来源。

## EDBT 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 SIGMOD、VLDB、
ICDE 或 ICDT 理论侧转投作者最常犯的错误：

- **在 OpenProceedings.org 上开放获取，而非付费墙 DL。** EDBT 论文发表于 **OpenProceedings.org**
  —— 由 **ICDT 与 EDBT 共同创立** 的平台 —— 采用 **CC-BY-NC-ND 4.0** 许可、**版权归作者所有**、
  每卷有 **ISBN**，并被 DBLP/Scholar/SCOPUS 收录。**无 ACM/IEEE 付费墙、无 APC**。这是与
  SIGMOD/ICDE（ACM DL / IEEE Xplore）及 PVLDB 最鲜明的区别。
- **多轮滚动模型，而非单一年度截止。** 自 2022 起 EDBT 每年设 **三个投稿/发表 cycle**。作者按成熟度
  选择 cycle；较早 cycle 在当年会议报告，最后一个 cycle 顺延至下一届。
- **真实的 cycle 内 revise-and-resubmit。** 每个 cycle 流程为：投稿 → **author feedback phase** →
  **accept / revise / reject** → **revised submission** → 对返修稿的 **accept / reject**。revise
  是原审稿人在同一 cycle 内的真正复审 —— 更接近期刊 R&R 而非一次性 rebuttal。
- **论文类型是一等公民。** EDBT 区分 **Regular** 研究论文、**Experiments & Analysis** 论文
  （以基准测试/可重复性为独立贡献）与短篇 **Vision** 论文 —— 各有篇幅预算与评审预期。
- **欧洲数据库系统范畴，理论交给隔壁 ICDT。** EDBT 奖励“扩展”数据库技术：系统、应用数据管理与
  experiments-and-analysis 工作。姊妹会议 **ICDT** 承担理论；在两者间选路是实时决策，且不同于
  美国的 SIGMOD/PODS 配对。
- **Microsoft CMT 与 12 个月重投禁令。** 评审在 **Microsoft CMT** 中进行；被 EDBT 某 track 拒稿或
  撤稿的工作，在同一论文类型下 **12 个月内** 不得重投任何 EDBT track。
- **面向可复现的社区。** 数据库社区的可复现文化根植于 EDBT/SIGMOD；Experiments & Analysis 论文与
  可检验 artifact 受重视，而非可有可无的附加项。

## Skills

| Skill | 作用 |
| --- | --- |
| [`edbt-topic-selection`](skills/edbt-topic-selection/SKILL.md) | 在 EDBT 与同类会议（SIGMOD、VLDB、ICDE、ICDT 及数据管理期刊）间选路，用贡献形态、系统-理论取向及最近 cycle 判断。 |
| [`edbt-workflow`](skills/edbt-workflow/SKILL.md) | 运行滚动 cycle 日历：选 cycle，倒排 author-feedback 阶段与 revise-and-resubmit 窗口，处理 cycle 到会议的顺延。 |
| [`edbt-writing-style`](skills/edbt-writing-style/SKILL.md) | 构建系统论文骨架：首页给出数据管理问题、可复现设计、经得起数据库审稿人审视的评估、按类型的篇幅纪律。 |
| [`edbt-related-work`](skills/edbt-related-work/SKILL.md) | 覆盖数据管理文献 lane，写针对 SIGMOD/VLDB/ICDE/ICDT 的 delta-first 定位，处理 12 个月重投禁令与旧版本重叠。 |
| [`edbt-experiments`](skills/edbt-experiments/SKILL.md) | 让系统工作的证据匹配论断：真实 workload 与数据集、公平 baseline、诚实测量、Experiments & Analysis 论文标准。 |
| [`edbt-reproducibility`](skills/edbt-reproducibility/SKILL.md) | 构建可复现证据：可运行 artifact、钉死的环境与数据 provenance、论文与包的一致性，服务开放获取记录。 |
| [`edbt-supplementary`](skills/edbt-supplementary/SKILL.md) | 按决策重要性划分正文与 artifact，遵守按类型的篇幅预算与参考文献不计页数规则。 |
| [`edbt-submission`](skills/edbt-submission/SKILL.md) | CMT 终审：cycle 选择、论文类型、OpenProceedings/host 模板与篇幅、重投禁令检查、可复现项、desk-reject 分诊。 |
| [`edbt-review-process`](skills/edbt-review-process/SKILL.md) | 建模流程 —— CMT 评审、author-feedback 阶段、accept/revise/reject、cycle 内复审、cycle 到会议顺延 —— 及作者杠杆点。 |
| [`edbt-author-response`](skills/edbt-author-response/SKILL.md) | 撰写两轮：简短的 author-feedback 回复与把每条要求映射到具体修改的 revise-and-resubmit 变更信。 |
| [`edbt-artifact-evaluation`](skills/edbt-artifact-evaluation/SKILL.md) | 准备数据库系统 artifact 与可复现包：turnkey 运行、钉死 workload、面向开放获取记录的 DOI 存档。 |
| [`edbt-camera-ready`](skills/edbt-camera-ready/SKILL.md) | 完成 OpenProceedings camera-ready：host LaTeX 模板、CC-BY-NC-ND 许可与 ISBN 元数据、永久 artifact 链接、版权/e-rights 表单。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经核验的 EDBT 论文，覆盖多种贡献形态，附自检问题与对 SIGMOD/VLDB/ICDE/ICDT 的混淆防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构 query-optimization 研究的摘要与引言按 EDBT 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 EDBT 专用可复现检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./EDBT-Skills
claude plugin install edbt-skills
```

也可直接使用文件：每个 `skills/edbt-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 EDBT 还是 SIGMOD/VLDB/ICDT？” → `edbt-topic-selection`
- “该投哪个 EDBT cycle，日历长什么样？” → `edbt-workflow`
- “CMT 上传前按 EDBT research-track 规则审我的稿” → `edbt-submission`
- “拿到 revise —— 规划返修稿与变更信” → `edbt-author-response`

## 目录结构

```text
EDBT-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── edbt-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `edbt-topic-selection`；EDBT 与 SIGMOD/VLDB/ICDE 高度重叠，且 EDBT/ICDT
   之分很重要，按贡献形态与最近 cycle 选择是最高杠杆的一步。浏览 exemplars 看 EDBT 贡献长什么样。
2. **构建证据时** —— 让 `edbt-experiments` 与 `edbt-reproducibility` 贴着系统；workload、baseline
   与测量期钉死的 provenance 无法事后补救。
3. **写作时** —— 用 `edbt-writing-style` 对照 worked example 打磨正文，用 `edbt-supplementary`
   划分正文/artifact，用 `edbt-related-work` 对数据管理会议做 delta-first 定位。
4. **cycle 周** —— 用 `edbt-workflow` 选 cycle，再用 `edbt-submission` 对终稿 PDF 与 artifact
   逐项过审以便 Microsoft CMT 上传。
5. **投稿后** —— 用 `edbt-review-process` 校准预期，用 `edbt-author-response` 应对 author-feedback
   轮与任何 revise-and-resubmit 轮，随后 `edbt-artifact-evaluation` 与 `edbt-camera-ready` ——
   若结果不利，则用 `edbt-topic-selection` 的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- EDBT 2026 为**第 29 届**：**EDBT/ICDT 2026 联合会议**，芬兰 Tampere，**2026 年 3 月 24-27 日**，
  由 Tampere University 承办。截至 2026-07-09 已举办完毕。
- **EDBT 2027 cycle 截止日：** **2026-02-04**、**2026-06-10**、**2026-10-07**。截至 2026-07-09，
  cycle 1、2 已过，**cycle 3（2026-10-07）** 是下一个 live 截止日。
- 出版：**OpenProceedings.org**，open access，**CC-BY-NC-ND 4.0**，每卷 ISBN，无 APC。评审：
  **Microsoft CMT**，每年三个 cycle，cycle 内 **accept/revise/reject**。论文类型（EDBT 2022 CFP）：
  **Regular** 与 **Experiments & Analysis** ≤12 页 + 参考文献不限，**Vision** ≤6 页 + 参考文献不限
  （**待核实** 当前 cycle）。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 追溯到 source map 中的编号来源（如 OpenProceedings 的 CC-BY-NC-ND
   出版、三 cycle 模型、EDBT 2027 cycle 截止日、Tampere 届）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如各 cycle 的 author-feedback 与返修具体日期、
   发表月份聚集）。
3. **核验期不可确定项** —— 明确标为 待核实（如当前 cycle 单盲/双盲、精确篇幅预算、EDBT 可复现/
   徽章计划、EDBT 2027 地点、完整 chair 名单）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。EDBT 每届重定结构 —— 包括 cycle 数量与各 cycle 时间线 ——
  每年先在当届 host 站点核验 cadence。
- EDBT 无常任 editor-in-chief、无 APC；chairs 每届轮换，host 站点每年更换（Barcelona 2025、
  Tampere 2026）。将人与 URL 视为按届变化。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的工具名
  并不能证明该论文发表于 EDBT 而非 SIGMOD/VLDB/ICDE/ICDT。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
