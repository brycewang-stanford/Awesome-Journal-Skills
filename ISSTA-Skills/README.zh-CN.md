# ISSTA Skills

面向 **ISSTA —— ACM SIGSOFT 软件测试与分析国际研讨会（International Symposium on
Software Testing and Analysis）** 论文的 12 个 agent skills。ISSTA 的主题被明确限定在
软件的 *testing and analysis*：测试生成、fuzzing、符号执行、静态与动态分析、缺陷定位、
程序修复评估、sanitizer，以及对这些技术的实证研究。本包覆盖一次 ISSTA 冲刺的完整链条：
判断项目是否属于 testing-and-analysis、构建能经受 ISSTA 审稿人审视的 bug-finding 与
分析证据、打包 double-anonymous 的 HotCRP 投稿、处理 major-revision 流程，最后交付
camera-ready 以及带 ACM badge、Zenodo 存档的 artifact。

官方依据核验日期：**2026-07-09**。已核验 ISSTA 2026 Research Papers 征稿页、important
dates 页、artifact-evaluation track、SPLASH/ISSTA 2026 合办主页，以及 ACM Digital
Library proceedings 系列。`conf.researchr.org` 的直接抓取常被网关拦截，因此官方页面通过
搜索引擎对确切 URL 的渲染读取，并与 ISSTA HotCRP 站点、ACM DL proceedings 卷、dblp
交叉核对；完整的溯源链（含所有仍标记 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 本包适合谁

- 从**更宽泛的 SE 会议**（ICSE、FSE、ASE）转投 ISSTA 的作者，需要了解 testing/analysis
  专业化收紧了什么、又放下了什么。
- 从 **ML 会议**转来、习惯 leaderboard 证据的作者，需要重新学会以真实 subject、公平
  baseline 与非参数统计来评估。
- 从 **PL/verification**（PLDI、POPL、CAV）转来的作者，其分析需要一个实证 bug-finding
  故事才能契合 ISSTA，而非仅有 soundness 证明。
- 任何正在走 **Major-Revision** 路径的作者——第二阶段是真实的第二次机会，而非软拒。

## ISSTA 与兄弟会议的区别

以下会议机制按 2026 cycle 核验，驱动了本包大部分建议，也解释了从 ML 会议、SE 期刊或更宽泛
的 SE 会议转投过来的作者最常犯的错误：

- **Testing and analysis 是全部 scope，而非一个 track。** ISSTA 面向 *发现、刻画或推理*
  软件行为与缺陷的技术。若一篇论文的核心是新的需求流程或关于开发团队的人因研究，那它其实是
  披着 ISSTA 外衣的 ICSE/FSE 贡献——请尽早改投。
- **单一主 deadline，但有真实的第二阶段。** ISSTA 2026 只开一个 research-paper deadline
  （2026-01-29，AoE）；首轮结果为 Accept、**Major Revision** 或 Reject，Major-Revision
  论文需在固定的后续 deadline（2026-05-21）前修改，并得到终审结论（2026-06-25）。更早的
  cycle 曾采用两个 rolling deadline——此模型逐年变动，务必重新核验。
- **默认 double-anonymous。** LaTeX 投稿使用 ACM `sigconf` 模板加 `review`（行号）与
  `anonymous` 选项；正文、self-citation 措辞、仓库归属、PDF 元数据都不得泄露身份。
- **一个宽松的页数框，而非双栏挤压。** ISSTA 2026 规定除参考文献外一律 18 页（所有章节、
  图、appendix 都计入），这是相对旧的 10+2 模型的变化——超页或改格式的明示后果是 desk
  reject。
- **一流的 artifact 与可复现文化。** ISSTA 设有强 artifact evaluation，颁发 ACM badge：
  *Artifacts Available*（Zenodo 存档）、*Artifacts Evaluated — Functional* 与
  *— Reusable*，以及 *Results Reproduced*；审稿群体把可运行的工具和共享 benchmark 视为
  常态而非例外。
- **Bug-finding 证据有独立标准。** 主张需在真实 subject program 与成熟 benchmark
  （Defects4J、真实 CVE、fuzzing corpus）上、在公平的工具 baseline 下、以统计上站得住脚的
  比较（非参数检验与 effect size，而非单次幸运运行）来支撑。

## Skills

| Skill | 作用 |
| --- | --- |
| [`issta-topic-selection`](skills/issta-topic-selection/SKILL.md) | 判断项目适合 ISSTA，还是 ICSE、FSE、ASE、ICST、PLDI/CAV 或 SE 期刊，并说清其核心的 technique 与 property。 |
| [`issta-workflow`](skills/issta-workflow/SKILL.md) | 从一月 deadline 倒排全年：三月 response、四月决策、五月 Major-Revision 冲刺、六月终审、artifact evaluation，到十月的 Oakland。 |
| [`issta-writing-style`](skills/issta-writing-style/SKILL.md) | 搭建 testing/analysis 论文骨架：威胁模型、技术、评估契约、真正的 threats-to-validity，与 18 页纪律。 |
| [`issta-related-work`](skills/issta-related-work/SKILL.md) | 在 ISSTA、ICSE、FSE、ASE、ICST 与 PL/verification 各会议间做 delta-first 定位，并保持 self-citation 匿名。 |
| [`issta-experiments`](skills/issta-experiments/SKILL.md) | 按主张形态匹配证据：真实 subject、成熟 benchmark、公平等预算 baseline、非参数检验、effect size 与 bug-finding 指标。 |
| [`issta-reproducibility`](skills/issta-reproducibility/SKILL.md) | 构建可验证脊柱：固定 subject 与 benchmark 版本、seed 与预算、non-determinism 披露、claim-to-evidence 可追溯。 |
| [`issta-supplementary`](skills/issta-supplementary/SKILL.md) | 在 18 页正文与 artifact 之间切分内容，确保决定性内容不只存在于审稿人可能不看的位置。 |
| [`issta-submission`](skills/issta-submission/SKILL.md) | 核查 HotCRP 记录、18 页框、`sigconf`/`anonymous` 格式、double-anonymous 完整性与第一阶段 deadline 排序。 |
| [`issta-author-response`](skills/issta-author-response/SKILL.md) | 撰写 rebuttal；当结果为 Major Revision 时，把每条审稿意见转成可追踪的修改 ledger。 |
| [`issta-review-process`](skills/issta-review-process/SKILL.md) | 解释 double-anonymous 审稿、Major-Revision 阶段、评审标准及最终如何决策。 |
| [`issta-artifact-evaluation`](skills/issta-artifact-evaluation/SKILL.md) | 为 ACM badge（Available / Functional / Reusable / Results Reproduced）打包工具、benchmark 与结果，并做 Zenodo deposit。 |
| [`issta-camera-ready`](skills/issta-camera-ready/SKILL.md) | 去匿名、套用最终 `sigconf` 版式、完成 ACM 版权与 DOI、展示 artifact badge，准备 ACM DL 包。 |

## 2026 cycle 一览（每届都要重新核验日期）

| 里程碑 | ISSTA 2026 日期 | 说明 |
| --- | --- | --- |
| Research-paper 投稿 | 2026-01-29（AoE） | 单一主 deadline；HotCRP |
| Author response | 2026-03-24 至 03-26 | 窗口短；应尽早、精确回复 |
| 首轮通知 | 2026-04-16 | Accept / Major Revision / Reject |
| Major-Revision deadline | 2026-05-21 | 携审稿意见 ledger 重投 |
| 终审通知 | 2026-06-25 | 修改稿的最终结论 |
| 研讨会 | 2026-10-03 至 10-09 | Oakland, California；与 SPLASH 合办 |

## 12 个 skill 如何协同

先用 `issta-topic-selection` 与 `issta-workflow` 做选会与全年规划；再用 `issta-experiments`
与 `issta-reproducibility` 构建证据；然后用 `issta-writing-style`、`issta-related-work`、
`issta-supplementary` 打磨论文；用 `issta-submission` 与 `issta-artifact-evaluation` 打包投稿。
审稿到来后走 `issta-review-process` 与 `issta-author-response`；录用后走 `issta-camera-ready`。
[`resources/`](resources/README.md) 目录以核验来源、获奖 exemplar 与首页改写范例为这一切兜底。

## 维护说明

- 涉及 deadline 的建议前，必须重新打开当年官方页面；submission 模型是 ISSTA 最易变的部分。
- 本包中的 ISSTA 2026 事实是历史锚点，而非永久规则——deadline 数量、页数、badge 集合与
  评审标准都在各届之间变过。
- 每年核验当前 artifact-evaluation 征稿；badge 名称与 Zenodo 要求都是 cycle-specific。
- 确认当前 venue：ISSTA 2026 与 SPLASH 合办于 Oakland, California（2026-10-03 至 10-09）；
  ISSTA 2027 已宣布在 Singapore，日期仍 待核实。
