# OSDI Skills（中文说明）

面向 **OSDI — USENIX Symposium on Operating Systems Design and Implementation** 的
12 个 agent skills。OSDI 是 USENIX 的系统研究旗舰会议，覆盖操作系统、存储、分布式系统、
云基础设施与机器学习系统。本包覆盖一个完整 OSDI 周期：判断贡献是否是"已构建、已测量"
的系统，设计评测，把故事压进 12 页受审正文，通过（2026 年**没有 rebuttal** 的）双盲评审，
完成 conditional accept 的 shepherding，最终发表为 USENIX 开放获取论文并申请
sysartifacts artifact badge。

官方依据核验日期：**2026-07-08**。已核验 OSDI '26 会议主页、Call for Papers（HTML 与
PDF 两版）、Requirements for Authors、Call for Artifacts、`osdi26.usenix.hotcrp.com`
的 deadlines 页、USENIX 关于 OSDI 年度化与 USENIX ATC 停办的官方博客，以及 OSDI '27
会议占位页。核验环境中直接抓取 `usenix.org` 返回 HTTP 403，因此官方页面通过搜索引擎对
精确官方 URL 的渲染读取，并与 dblp 和 HotCRP 站点交叉核对；完整来源链与所有 待核实 条目
见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## OSDI 与其他会议的关键差异

以下机制均按 2026 周期核验，是本包大部分建议的出发点，也是从 ACM 或 ML 会议转来的
作者最容易踩的坑：

- **USENIX 会议，不是 ACM 会议。** 论文集**从会议开幕当天起开放获取** ——
  `usenix.org` 上历届 OSDI 论文全部免费下载。没有付费墙，没有 ACM DL 费用，
  也没有作者出版费。
- **投稿走 HotCRP**（不是 OpenReview 或 CMT），且 USENIX 用本地时间：OSDI '26 的
  截止是 **2:59 pm PST**，不是 AoE 午夜。
- **12 页受审正文，参考文献不限页，投稿禁止附录。** '26 CFP 明确：参考文献页数不限，
  但投稿 PDF 中不得包含补充性附录材料——评审依据必须全部装进 12 页。录用后终稿放宽到
  14 页正文另加参考文献**和**附录。
- **2026 年没有 rebuttal。** OSDI '26 取消了 author-response 阶段。作者的杠杆前移到
  投稿前（写清楚），后移到通知后（**conditional acceptance + 重量级 shepherding**：
  PC 指定修改清单，由 shepherd 验收）。
- **两条评审 track**：传统 Research track 和面向已部署系统经验论文的
  **Operational Systems track**。
- **Artifact evaluation 由 sysartifacts 社区承担**，在 conditional accept 之后进行。
  2026 年只评 **Artifacts Available** 一枚 badge——相比早年 Available / Functional /
  Reproduced 三枚是刻意收窄。
- **两大 OS 旗舰现在都是年会。** OSDI 自 2021 年、SOSP 自 2024 年起每年举办，
  12 月投 OSDI 未中，几个月内即可转投，不必再等两年。
- **最佳论文传统**：**Jay Lepreau Best Paper Award**，自 OSDI '08 设立。

## Skills 一览

| Skill | 作用 |
| --- | --- |
| [`osdi-topic-selection`](skills/osdi-topic-selection/SKILL.md) | 做"已构建且已测量"检验，选 Research 或 Operational Systems track，并在 OSDI、SOSP、NSDI、FAST、EuroSys、ATC 之间路由。 |
| [`osdi-workflow`](skills/osdi-workflow/SKILL.md) | 管理 12 月到 7 月的整年：题目注册、投稿、静默评审期、artifact 截止、shepherding 终稿、西雅图会期。 |
| [`osdi-writing-style`](skills/osdi-writing-style/SKILL.md) | 在评审被明确要求对注水论文降档的前提下，用 12 页写出痛点 → 抽象 → 机制 → 测量的系统叙事。 |
| [`osdi-related-work`](skills/osdi-related-work/SKILL.md) | 覆盖六条系统文献线，利用 USENIX 免费论文集做核对，并按"系统改名"规则匿名处理自己的前作。 |
| [`osdi-experiments`](skills/osdi-experiments/SKILL.md) | 设计回答研究问题的评测：成熟 baseline、真实负载、可扩展性、尾延迟与组件分解。 |
| [`osdi-reproducibility`](skills/osdi-reproducibility/SKILL.md) | 在实验运行时同步记录硬件、配置、负载与测量出处，保证论文与 artifact 不漂移。 |
| [`osdi-supplementary`](skills/osdi-supplementary/SKILL.md) | 在"投稿无附录"规则下分流内容：哪些进 12 页，哪些等 14 页终稿，哪些成为 artifact。 |
| [`osdi-artifact-evaluation`](skills/osdi-artifact-evaluation/SKILL.md) | 面向 sysartifacts 评审打包 artifact：2026 年的 Artifacts Available badge、Zenodo 归档、5 月截止。 |
| [`osdi-submission`](skills/osdi-submission/SKILL.md) | HotCRP 终审：12 月双截止、PST 时刻、12 页核查、机构级匿名、系统改名规则、单作者 8 篇上限。 |
| [`osdi-review-process`](skills/osdi-review-process/SKILL.md) | 建模无 rebuttal 的双盲 PC 流程：评审看什么、conditional acceptance 与 shepherding 如何运作、作者杠杆在哪。 |
| [`osdi-author-response`](skills/osdi-author-response/SKILL.md) | 在无 rebuttal 体制下工作：投稿时预答异议，把 shepherd 的修改函当作真正的 author response 来回。 |
| [`osdi-camera-ready`](skills/osdi-camera-ready/SKILL.md) | 交付 6 月终稿：14 页加附录、两页 artifact appendix、去匿名、USENIX 开放获取发表与报告义务。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 11 个官方来源（URL + 核验日期）、已核验的 2026 周期事实、访问方式说明与明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口（USENIX 页面、HotCRP、sysartifacts）与投稿前的作者侧自检清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经 dblp/USENIX 核验的 OSDI 论文，横跨二十年与五类系统，附自检问题与兄弟会议误归防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构存储系统论文的摘要与引言，按 OSDI 设计叙事弧线做 before → after 重写。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向仓库共享的 ML 会议可复现性工具包，并列出通用工具做不了的 OSDI 专项检查。 |

## 安装与使用

作为 Claude Code plugin（本目录自带 marketplace manifest，可独立安装）：

```bash
# 在仓库克隆内执行
claude plugin marketplace add ./OSDI-Skills
claude plugin install osdi-skills
```

也可以直接使用文件：每个 `skills/osdi-*/SKILL.md` 都是独立的指令文件，frontmatter 的
`description` 告诉 agent 何时触发。典型用法：

- "这个调度器该投 OSDI 还是 NSDI？" → `osdi-topic-selection`
- "按 OSDI 投稿规则审一遍我的稿子" → `osdi-submission`
- "拿到 conditional accept，下一步？" → `osdi-author-response`、`osdi-camera-ready`
- "为 badge 准备 artifact" → `osdi-artifact-evaluation`

## 目录结构

```text
OSDI-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── osdi-<topic>/SKILL.md # 12 个 skills，每个一个目录
└── resources/
    ├── README.md             # 资源指南与建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享可复现性工具包适配器
```

## 建议路线

1. **距截止还有几个月** —— 先跑 `osdi-topic-selection`；如果系统还没构建、没测量，
   这个检验能省下一整个周期。对照 exemplars library 看录用论文如何把可运行系统放在
   论文中心。
2. **构建阶段** —— 把 `osdi-experiments` 和 `osdi-reproducibility` 放在测试集群旁边；
   负载真实性和测量出处无法在截止周补做。
3. **写作阶段** —— 用 `osdi-writing-style` 组织 12 页叙事，用 `osdi-supplementary`
   做无附录分流，用 `osdi-related-work` 对照可免费下载的 OSDI/SOSP/NSDI 文献定位。
4. **12 月** —— 完整过一遍 `osdi-submission`：提前一周注册题目，盯 PST 截止时刻，
   匿名做到机构与系统名层面。
5. **通知之后** —— 用 `osdi-review-process` 解读决定，用 `osdi-author-response`
   处理 shepherding 往来，用 `osdi-artifact-evaluation` 和 `osdi-camera-ready`
   完成 5–6 月交付。

## 2026 周期锚点事实（历史快照，非永久规则）

- OSDI '26 为**第 20 届**：2026 年 **7 月 13–15 日**，美国华盛顿州西雅图
  The Westin Seattle。Program Co-Chairs：Eddie Kohler（Harvard University）与
  Amar Phanishayee（NVIDIA）。
- 2026 流水线：题目/摘要注册 **2025-12-04** · 全文投稿 **2025-12-11**（均为
  2:59 pm PST，HotCRP）· 通知 **2026-03-26** · artifact 提交 **2026-05-08**
  （8:59 pm PDT）· 终稿 **2026-06-09**。
- 版式：投稿正文 **12 页**（含图表），参考文献不限页，投稿 PDF **不得含附录**；
  终稿 **14 页** 另加参考文献与附录；通过 artifact evaluation 的论文可再加
  **2 页** artifact appendix。
- 政策：双盲评审，机构也须匿名，arXiv 预印本须使用不同系统名，单作者至多
  **8 篇**投稿，无 author-response 阶段，conditional acceptance + shepherding。
- 出版：USENIX **开放获取**论文集，开幕即全网免费；无作者费用；会议靠注册费运转，
  设 hardship 折扣。

## 事实纪律

本包把陈述分为三类，且 skills 的写法保证三类可区分：

1. **已核验的 2026 周期事实** —— 带日期/上限，可追溯到 source map 中的编号来源
   （如 12 页正文、12 月 11 日截止、单枚 Artifacts Available badge）。
2. **转述事实** —— 仅见于二手渲染并如实标注（如 OSDI '27 的巴尔的摩日期，
   目前只有活动聚合站给出，待官方页面确认）。
3. **核验时无法确认的条目** —— 明确标注 待核实，写成待解决的问题而非事实
   （如 OSDI '27 CFP 截止、注册费、AI 使用政策）。

若发现任何 skill 把第 2、3 类当第 1 类陈述，请视为 bug，对照官方在线页面修正。

## 维护说明

- 上述所有日期与上限都是 **2026 周期快照**；给出与截止相关的建议前，务必重开当年的
  `usenix.org/conference/osdi<yy>` 页面。
- author-response 与 artifact badge 政策**在 OSDI '26 发生过变化**（取消 response；
  badge 收窄为仅 Available）。它们可能再变——以当年 CFP 与 Call for Artifacts 为准，
  不要假设任一方向。
- USENIX ATC 已于 ATC '25 后停办，后继会议由 ACM SIGOPS 运营；不要沿用 2026 年前
  OSDI 页面上的"co-located ATC"信息。
- OSDI 主席按届轮换，没有常设主编；引用任何人名前先查当年 organizers 页面。
- 新增 exemplar 论文时，按 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程操作——著名系统论文分散在 OSDI、SOSP、NSDI、ATC 各处，
  venue 必须核实，不能凭记忆。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
