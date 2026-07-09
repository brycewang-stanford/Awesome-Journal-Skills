# ASE Skills

面向 **ASE —— IEEE/ACM International Conference on Automated Software Engineering（自动化软件工程
国际会议）** 论文的 12 个 agent skills。ASE 是研究"如何**自动化**软件工程任务"的顶级会议：分析、
测试、综合、修复、理解，以及 AI4SE 与 SE4AI 的双向融合。本包覆盖一次 ASE 投稿的完整流程：判断项目
是否是 ASE 形态（一个"自动化"）还是应投 ICSE、FSE、ISSTA、PL 会议或 SE 期刊；构建能经受自动化 SE
审稿人审视的评估；准备 double-anonymous 的 HotCRP 投稿及其**强制 Data Availability 声明**；应对
**early-rejection 门槛**、rebuttal 与**准则约束的 Revision 轮**；直到完成 camera-ready 与获得 ACM
artifact 徽章，并被 IEEE Xplore 与 ACM Digital Library **双重收录**。

官方依据核验日期：**2026-07-09**。已核验 ASE 2026（慕尼黑）与 ASE 2025（首尔）research track 的 call
与 Important Dates 页面、ASE HotCRP 站点、ACM Artifact Review and Badging 政策，以及 ASE Most
Influential Paper 奖项页面。核验环境中直接抓取 `conf.researchr.org` 返回 403，因此通过搜索引擎对精确
URL 的渲染阅读官方页面，并与 dblp（ASE 论文集在历史系列键 `conf/kbse` 下）、ACM Digital Library、
IEEE Xplore 及 ASE HotCRP 交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 缩写冲突提醒："ASE" 也指 *Association for Science Education* 与 *Association for Surgical
> Education*，而 Springer 期刊 *Automated Software Engineering*（AUSE）是相关但不同的 venue。本包中
> 的事实均不来自这些。

## ASE 与同类会议的区别

以下会议机制（按 2025/2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 ICSE、FSE、ISSTA
或 ML 会议转投作者最常犯的错误：

- **贡献必须是一个"自动化"。** ASE 奖励在真实 subject 上评估的、自动化某个 SE 任务的技术或工具 ——
  而非宽泛的实证发现（偏 FSE）、测试理论结果（ISSTA）或模型进展（ML 会议）。model-swap 测试决定边界
  情形。
- **IEEE/ACM 双主办，双论文集。** ASE 由 IEEE 与 ACM SIGSOFT 共同主办，录用论文被 **IEEE Xplore 与
  ACM Digital Library 双重收录** —— 不同于仅 ACM 的 FSE/PACMSE。
- **模板随主办方而变。** 由于双主办，各届要求的格式有所不同（IEEE 双栏 vs. ACM `acmart`）。ASE 2026
  要求 ACM Primary Article Template —— `\documentclass[sigconf,review,anonymous]{acmart}`。每届先
  核验，不要沿用旧习惯。
- **10+2 篇幅与强制 Data Availability 声明。** 正文含图表 10 页 + 仅参考文献 2 页；Data Availability
  声明置于 Conclusions 之后并计入 10 页之内。录用论文加 1 页正文。
- **rebuttal 前的 early-rejection 门槛。** 初评分数一致为负的论文在 rebuttal 期前被拒 —— 快速回复，
  并把 rebuttal 精力集中到能改变结果的论文上。
- **准则约束的 Revision 轮。** 首轮结果为 Accept、**Revision** 或 Reject。Revision 会预先固定具体、
  可操作的准则；若满足，审稿人原则上接受，作者提交修订稿并附逐条 summary-of-changes。
- **同址 track：NIER、Tools-and-Datasets、Journal-First。** New Ideas and Emerging Results（4 页）、
  工具演示（≤4 页），以及面向 TSE/TOSEM/EMSE 工作的 Journal-First 通道。

## Skills

| Skill | 作用 |
| --- | --- |
| [`ase-topic-selection`](skills/ase-topic-selection/SKILL.md) | 在 ASE 与同类会议（ICSE、FSE、ISSTA、PL 会议、ML 会议、TSE/TOSEM/EMSE）之间选路，用自动化贡献形态与 model-swap、re-label 测试判断。 |
| [`ase-workflow`](skills/ase-workflow/SKILL.md) | 从截止日倒排年度计划，经 abstract 注册、early-rejection 门槛、rebuttal、Revision 轮、artifact 评审与双论文集 camera-ready。 |
| [`ase-writing-style`](skills/ase-writing-style/SKILL.md) | 构建"自动化优先"弧线：点明任务、保持工具可运行、通过 model-swap 测试、论证 threats、守住 10+2 篇幅。 |
| [`ase-related-work`](skills/ase-related-work/SKILL.md) | 覆盖自动化 SE 各 lane，对具名可运行工具做 delta-first 定位，写公平的 head-to-head，并保持自引匿名。 |
| [`ase-experiments`](skills/ase-experiments/SKILL.md) | 让证据匹配自动化论断：真实 subject、公平工具 baseline、隔离学习组件的 ablation、oracle、防污染 LLM 处理、provenance。 |
| [`ase-reproducibility`](skills/ase-reproducibility/SKILL.md) | 构建 open-science 证据：强制 Data Availability 声明、匿名可运行工具、钉死 provenance、缓存 LLM 输出。 |
| [`ase-supplementary`](skills/ase-supplementary/SKILL.md) | 按决策重要性划分 10 页正文与 artifact —— 决定录用的证据不得置于正文之外。 |
| [`ase-submission`](skills/ase-submission/SKILL.md) | HotCRP 终审：模板与 10+2 篇幅、double-anonymous 清扫（含工具名）、Data Availability 声明、desk-reject 分诊。 |
| [`ase-review-process`](skills/ase-review-process/SKILL.md) | 建模流程 —— double-anonymous 评审、early-rejection 门槛、Accept/Revision/Reject、准则约束的 Revision —— 及作者杠杆点。 |
| [`ase-author-response`](skills/ase-author-response/SKILL.md) | 撰写两轮：先要越过 early-rejection 门槛的 rebuttal，与把每条准则映射到修改的 revision summary-of-changes。 |
| [`ase-artifact-evaluation`](skills/ase-artifact-evaluation/SKILL.md) | 在 artifact track 自身截止日，把录用论文的工具转化为 ACM Artifacts Available / Reusable 徽章。 |
| [`ase-camera-ready`](skills/ase-camera-ready/SKILL.md) | 系统去匿名、用加页承载评审反馈、永久化 Data Availability 链接、通过 IEEE-Xplore/ACM-DL 双重生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2025/2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 ASE 论文，覆盖五种贡献形态（含 Most Influential Paper 得主），附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构 flaky-test 修复工具的摘要与引言按 ASE 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 ASE 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./ASE-Skills
claude plugin install ase-skills
```

也可直接使用文件：每个 `skills/ase-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- "这篇该投 ASE 还是 FSE/ISSTA？" → `ase-topic-selection`
- "按 ASE research-track 规则审我的稿" → `ase-submission`
- "拿到 Revision —— 规划 summary-of-changes" → `ase-author-response`
- "把工具准备到 ACM artifact 徽章标准" → `ase-artifact-evaluation`

## 目录结构

```text
ASE-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── ase-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `ase-topic-selection`；ASE 与 ICSE/FSE/ISSTA 重叠，自动化测试与日历都很重要。
   浏览 exemplars 看十年影响力的自动化 SE 贡献长什么样。
2. **构建证据时** —— 让 `ase-experiments` 与 `ase-reproducibility` 贴着工具；公平 baseline 与钉死的
   provenance 无法事后补救。
3. **写作时** —— 用 `ase-writing-style` 对照 worked example 打磨"自动化优先"弧线，用
   `ase-supplementary` 划分正文/artifact，用 `ase-related-work` 做 delta-first 定位。
4. **截止周** —— 先在较早的 abstract 截止日前完成注册，再用 `ase-submission` 对终稿 PDF 与 artifact
   逐项过审。
5. **投稿后** —— 用 `ase-review-process` 校准预期，用 `ase-author-response` 应对 rebuttal 与任何
   Revision 轮，随后 `ase-artifact-evaluation` 与 `ase-camera-ready` —— 若结果不利，则用
   `ase-topic-selection` 的路由表改投。

## 2025/2026 周期锚点事实（历史快照，非永久规则）

- ASE 2026 为**第 41 届**：德国慕尼黑，**2026 年 10 月 12-16 日**。research 投稿 **2026-03-26**；
  通知 **2026-05-25**；入口 `ase26.hotcrp.com`。截至 2026-07-09 通知已发出，故 ASE 2027 是下一个投稿
  目标（主办地/日期 待核实）。
- ASE 2025 为**第 40 届**：韩国首尔，**2025 年 11 月 16-20 日**。
- 格式：**ACM Primary Article Template**（2026 用 `\documentclass[sigconf,review,anonymous]{acmart}`）；
  正文 **10 页 + 2** 页参考文献；**强制 Data Availability 声明**置于 Conclusions 之后。评审：
  **double-anonymous**，rebuttal 前有 **early-rejection 门槛**，结果为 **Accept / Revision /
  Reject**。论文集：**IEEE Xplore 与 ACM Digital Library**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2025/2026 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 10+2 篇幅、ACM
   `acmart` 要求、early-rejection 门槛、Available/Reusable 徽章）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如社区 tracker 报告的 ASE 2025 录用率）。
3. **核验期不可确定项** —— 明确标为 待核实（如 ASE 2026 abstract 截止日、完整 Program Co-Chair 名单、
   ASE 2027 主办地/日期、是否提供 Functional/Reproduced 徽章、任何 AI 使用披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。ASE 每届重定结构 —— 包括所需模板（IEEE vs. ACM）、截止日数量与
  artifact 徽章 —— 每年先核验。
- ASE 无常任 editor-in-chief；chairs 每届在 IEEE 与 ACM SIGSOFT 下轮换。正是双主办（而非单一学会）使
  论文集同时进入 IEEE Xplore 与 ACM DL。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的工具名
  并不能证明该论文发表于 ASE（dblp 将 ASE 收在 `conf/kbse` 下）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
