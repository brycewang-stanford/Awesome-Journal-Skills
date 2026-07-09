# IEEE VIS 技能包

面向 **IEEE VIS（IEEE 可视化会议）** 投稿的十二个智能体技能。IEEE VIS 是数据可视化领域的旗舰会议，自
**2021 年起**将原先分立的 SciVis、InfoVis、VAST 合并为一个统一会议，其完整论文（full papers）以
**期刊论文形式发表于 IEEE TVCG（可视化与计算机图形学汇刊）**。本技能包覆盖 VIS 投稿全流程：判断选题是否
适合 VIS（以及归属六大领域中的哪一个），还是应投向 EuroVis、CHI、SIGGRAPH 或 TVCG 期刊通道；构建以
**任务驱动**的设计与与贡献类型相匹配的证据；打包**作者可选双盲**的 PCS 投稿及其补充视频与开放材料；应对
带有**条件接收（conditional accept）第二轮**的**两阶段评审**；并完成 TVCG 终稿与图形可复现性印章
（Graphics Replicability Stamp）。

**核查日期 2026-07-09**：依据 IEEE VIS 2026 完整论文征稿、投稿格式指南、评审说明、领域模型（Area Model）
与开放实践页面；VIS 2026 评审流程变更博客；IEEE VGTC/TVCG 模板；以及图形可复现性印章计划。核查环境中直接
访问 `ieeevis.org`、`ieeexplore.ieee.org`、`precisionconference.com` 均返回 403，因此官方页面通过精确
URL 的搜索引擎快照阅读，并与官方 `@ieeevis` 公告、IEEE Xplore/TVCG、IEEE VIS 维基条目和 dblp 交叉核对；
完整追溯（含所有仍标注 **待核实** 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 范围混淆提醒：IEEE VIS **不是** IEEE VR，也**不是** ISMAR——它们是同属 PCS/VGTC 的姊妹会议但各自征稿。
> 本包无任何事实源自它们。

## VIS 与姊妹会议的关键差异

以下机制（依 2026 周期核实）驱动了各技能中的大部分建议，也是来自 CHI、视觉/机器学习会议或图形学会议的作者
最容易犯错之处：

- **论文即期刊文章。** VIS 完整论文发表于 **IEEE TVCG**（领域顶刊），以期刊标准评判并同时获得会议展示席位
  ——即“期刊一体化”模式。
- **两阶段评审含真实第二轮。** 首轮结果包含**条件接收**：入选论文进入完整的修订—再评审周期，只有真正完成
  “必需修改（required changes）”的论文才最终被接收——属期刊式 revise-and-review，而非一次性反驳。
- **通过 PCS（Precision Conference System）投稿，隶属 VGTC 学会。** 在 PCS 中依次选择学会 VGTC → 会议
  VIS 2026 → 通道 Full Papers，而非 HotCRP、OpenReview 或 CMT。
- **IEEE VGTC/TVCG 模板与 9+2 页预算。** 使用 VGTC 文档类：**正文最多 9 页，另加最多 2 页仅含参考文献与
  致谢**。既不是 `acmart`，也不是随手沿用的双栏 IEEEtran 习惯。
- **六大领域、按领域分派。** 自 2021 年统一以来，VIS 按**主领域**分派每篇论文——理论与实证、应用、系统与
  绘制、表示与交互、数据变换、分析与决策——由各领域论文主席（Area Paper Chairs）负责。
- **作者可选双盲。** 匿名化被推荐但非强制——在旗舰会议中较为少见，作者须每个周期自行慎重决定。
- **补充视频与开放实践文化。** 评审常观看视频；**图形可复现性印章**（GRSI / TVCG 印章）与开放实践计划奖励
  共享且可复现的代码与数据，研究类工作还看重预注册（preregistration）。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`vis-topic-selection`](skills/vis-topic-selection/SKILL.md) | 在 IEEE VIS 与姊妹会议（EuroVis、PacificVis、CHI、SIGGRAPH、TVCG 期刊通道）间选路，并按贡献类型与证据成熟度选定六大领域之一。 |
| [`vis-workflow`](skills/vis-workflow/SKILL.md) | 从摘要截止日倒排年度周期：完整论文、两阶段评审、条件接收第二轮、TVCG 终稿与现场展示。 |
| [`vis-writing-style`](skills/vis-writing-style/SKILL.md) | 搭建可视化骨架：首页给出任务驱动的贡献、以任务论证每个编码、评估与贡献类型匹配、诚实陈述局限。 |
| [`vis-related-work`](skills/vis-related-work/SKILL.md) | 覆盖可视化各条脉络（VIS 各领域、EuroVis/CGF、PacificVis、邻近 HCI/图形学），写“差异优先”的定位，并保持自引双盲。 |
| [`vis-experiments`](skills/vis-experiments/SKILL.md) | 让证据匹配贡献类型：带功效分析与效应量的感知/受控研究、色盲安全编码、基准测试、设计研究验证。 |
| [`vis-reproducibility`](skills/vis-reproducibility/SKILL.md) | 构建开放实践叙事：诚实的开放材料声明、研究预注册、来源追溯、可运行归档。 |
| [`vis-supplementary`](skills/vis-supplementary/SKILL.md) | 按“决定性证据”原则在受评的 9 页正文与补充材料（含一等公民地位的视频）之间划分内容。 |
| [`vis-submission`](skills/vis-submission/SKILL.md) | PCS 终审：摘要—论文两段截止、VGTC 模板与 9+2 预算、可选双盲排查、开放材料、拒稿风险分诊。 |
| [`vis-review-process`](skills/vis-review-process/SKILL.md) | 建模评审流程——六领域分派、主审/副审/外审/学生审、两阶段条件接收第二轮——并指出作者可发力之处。 |
| [`vis-author-response`](skills/vis-author-response/SKILL.md) | 撰写两轮回应：首轮沟通，以及条件接收的“修改摘要”，将每项必需修改映射到具体改动。 |
| [`vis-artifact-evaluation`](skills/vis-artifact-evaluation/SKILL.md) | 通过独立志愿者复现，将已接收论文的材料包转化为图形可复现性印章，并完成开放实践披露。 |
| [`vis-camera-ready`](skills/vis-camera-ready/SKILL.md) | 去匿名、补全 TVCG 期刊元数据、将开放材料链接永久化、通过 IEEE 制作核查。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十一个来源（含 URL 与访问日期）、已核实的 2026 事实、访问方法说明、以及明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方页面与交叉核对来源（供网关阻断时使用），以及作者侧核查步骤。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核实、跨五种贡献类型的 IEEE VIS/TVCG 论文（含 Test-of-Time 获奖者）及自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的“不确定性编码”研究的摘要与引言，按 VIS 结构改写的前后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 通往仓库共享复现工具的适配器，以及通用工具无法完成的 VIS 专属核查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./VIS-Skills
claude plugin install vis-skills
```

或直接使用文件：每个 `skills/vis-*/SKILL.md` 都是独立指令文件，其 frontmatter 的 `description` 告诉
智能体何时触发。典型调用：

- “这是 VIS 论文还是该投 EuroVis/CHI？归哪个领域？” → `vis-topic-selection`
- “按 IEEE VIS 完整论文规则审我的稿” → `vis-submission`
- “拿到条件接收——规划第二轮修订” → `vis-author-response`
- “把材料包准备好去申请图形可复现性印章” → `vis-artifact-evaluation`

## 2026 周期锚定事实（历史快照，非永久规则）

- IEEE VIS 2026 于 **美国马萨诸塞州波士顿**、**2026 年 11 月**举行（多方记为 11 月 9–13 日；确切日期跨度
  待核实）。摘要截止 **2026-03-21**，完整论文 **2026-03-31**，补充材料 **2026-04-07**，首轮通知
  **2026-07-15**（均为 23:59 AoE）。
- 发表：**IEEE TVCG**，期刊一体化。投稿：**PCS**（VGTC 学会）。评审：**两阶段、作者可选双盲**，含
  **条件接收第二轮**。评审人：**主审 + 副审 + 外审**（2026 新增可选学生审）。模板：**IEEE VGTC/TVCG**，
  **9+2** 页。

## 事实纪律

本包区分三类陈述，并使各技能保持可辨：

1. **已核实的 2026 事实**——附带日期/预算并可追溯到来源表中的编号来源（如 TVCG 发表、9+2 预算、两阶段评审、
   六领域模型）。
2. **转述事实**——仅通过二手快照读到并如实标注（如确切会议日期跨度、完整领域主席名单）。
3. **核查时不可确证项**——明确标注 **待核实**（如 VIS 2026 确切日期跨度、短论文篇幅与周期、任何生成式 AI
   披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为缺陷，应对照官方页面修正。

## 维护说明

- 以上每个日期与预算都是**周期快照**。VIS 每届重新决定其结构——包括领域边界、评审人数规则、是否强制双盲——
  因此每年动手前先在当届征稿页核实。
- **会议**没有常设主编，主席逐届轮换。TVCG（**期刊**）有自己的编委会，但 VIS 论文经**会议征稿**进入，而非
  独立向 TVCG 投稿——切勿混淆两条入口。
- 新增示例论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程——熟悉的系统名并不
  能证明其为 IEEE VIS 论文（可能来自 EuroVis、CHI 或 SIGGRAPH）。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
