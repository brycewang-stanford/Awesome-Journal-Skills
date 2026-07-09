# SIGGRAPH Skills

面向 **ACM SIGGRAPH Technical Papers（技术论文）项目** 论文的 12 个 agent skills。SIGGRAPH 是计算机
图形学旗舰会议，与姊妹会议 **SIGGRAPH Asia** 一起，其录用研究以特刊形式发表于 **ACM Transactions on
Graphics（TOG）** 期刊。本包覆盖一次 SIGGRAPH 投稿的完整流程：判断项目属于 SIGGRAPH 还是应投
Eurographics/EGSR、SGP、SCA 或视觉会议；构建能经受领域专家审稿人审视的**可见**图形学证据（teaser、
结果视频、与最强先前方法的正面对比、计时）；准备 **Linklings** 投稿及其“先建表、后上传”的两步截止日；
应对单轮评审中的 **1000 词 rebuttal**、Technical Papers Committee 会议与**条件录用后的第二阶段核验**；
直到完成 TOG camera-ready 并交付可运行、可申请 replicability stamp 的代码。

官方依据核验日期：**2026-07-09**。已核验 SIGGRAPH 2026 与 SIGGRAPH Asia 2026 技术论文的 call、
submissions FAQ 与 reviewer-instructions 页面、ACM SIGGRAPH 作者须知、ACM TOG 期刊与作者指南，以及
Graphics Replicability Stamp Initiative。核验环境中直接抓取 `s2026.siggraph.org`、
`asia.siggraph.org` 与 `dl.acm.org` 返回 403/405，因此通过搜索引擎对精确 URL 的渲染阅读官方页面，
并与 ACM Digital Library（TOG）、dblp 及 ACM SIGGRAPH 博客交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## SIGGRAPH 与同类会议的区别

以下会议机制（按 2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从视觉会议（CVPR/ICCV）、
可视化会议（VIS）或专门图形学 symposium 转投作者最常犯的错误：

- **论文即期刊文章。** SIGGRAPH 技术论文以特刊形式发表于 **ACM Transactions on Graphics（TOG）**——
  SIGGRAPH 2026 即 **TOG 第 45 卷第 4 期**。录用带来期刊 DOI 与卷期归属，而非仅会议 proceedings。
- **两条整合 track，一次评审。** 每篇投稿要么 **dual-track**（可作为 Journal 或 Conference 发表），
  要么 **Journal-only**，统一用**单一 6 级尺度**（Strong Reject … Strong Accept）评审。Technical
  Papers Committee 在录用时分配 track，对 **Conference track 的验证要求更宽松**，以容纳更冒险/早期
  的工作。
- **每年两个周期。** SIGGRAPH 北美（约 1 月截止，夏季办会）与 SIGGRAPH Asia（约 5 月截止，12 月办会）
  采用同一模型——被拒论文自然改投下一周期。
- **简短、纯文本 rebuttal。** 收到评审后，作者仅有**一轮 ≤1000 词、纯文本**（无图、无视频、无 URL）
  用于纠正事实错误——随后 **Technical Papers Committee 会议**决定，**条件录用**论文还须通过**第二
  阶段**委员核验。
- **走 ACM `acmart` 路线，期刊格式。** 要求 **`acmart` ≥ 2.16**（`acmtog` 谱系）；Conference track
  正文 **≤7 页**（不含参考文献与至多两页纯图页）。投稿系统为 **Linklings**。
- **结果视频是首要证据。** 运动、时序连贯性与渲染 artifact 无法以静图呈现；审稿人会观看结果视频，
  因此它是一等交付物（且提交时须持有每一帧的授权）。
- **社区自办 replicability，而非 ACM 徽章。** 图形学对 artifact evaluation 的对应物是 **Graphics
  Replicability Stamp（GRSI）** 与 **Code Replicability in Computer Graphics（CRCG）**——志愿者
  重建你的代码并复现结果，经 Software Heritage 存档——在录用后评定，独立于评审。

## Skills

| Skill | 作用 |
| --- | --- |
| [`siggraph-topic-selection`](skills/siggraph-topic-selection/SKILL.md) | 在 SIGGRAPH、SIGGRAPH Asia、direct-to-TOG 与同类会议（CVPR/ICCV、CHI/UIST、Eurographics/EGSR/SGP/SCA/HPG/I3D）之间选路，并选择 dual-track 还是 Journal-only，用 visual-result、capability-axis 与 model-swap 测试判断。 |
| [`siggraph-workflow`](skills/siggraph-workflow/SKILL.md) | 从截止日倒排两个年度周期的计划，经 form/upload 两步、rebuttal、委员会决定、条件录用第二阶段、TOG camera-ready 与现场报告。 |
| [`siggraph-writing-style`](skills/siggraph-writing-style/SKILL.md) | 构建 SIGGRAPH 首页弧线：撑起全文的 teaser、位于可度量轴上的图形学贡献、可见的结果、acmart 7 页纪律。 |
| [`siggraph-related-work`](skills/siggraph-related-work/SKILL.md) | 覆盖图形学文献 lane（渲染、几何、动画、仿真、成像、learning-for-graphics），按能力差定位，并在 SIGGRAPH/SA/TOG/EG/EGSR/SGP/SCA 之间正确归属。 |
| [`siggraph-experiments`](skills/siggraph-experiments/SKILL.md) | 让可见证据匹配图形学论断：忠实的正面对比、带视觉的质量指标、ablation，以及在既定硬件上等质量的计时。 |
| [`siggraph-reproducibility`](skills/siggraph-reproducibility/SKILL.md) | 构建结果可复现性：确定性重生成、钉死场景/网格/权重与硬件、诚实的容差，以及可运行的代码+资产发布。 |
| [`siggraph-supplementary`](skills/siggraph-supplementary/SKILL.md) | 打磨补充材料——尤其是结果视频——并按决策重要性划分 7 页正文与补充材料的证据。 |
| [`siggraph-submission`](skills/siggraph-submission/SKILL.md) | Linklings 终审：form/upload 两步截止、acmart ≥2.16 与篇幅、dual-track 选择、代表图与结果视频、desk-reject 分诊。 |
| [`siggraph-review-process`](skills/siggraph-review-process/SKILL.md) | 建模流程——单一 6 级尺度、primary/secondary/tertiary 审稿人、rebuttal、委员会会议、条件录用+第二阶段、dual-track 分配——及作者杠杆点。 |
| [`siggraph-author-response`](skills/siggraph-author-response/SKILL.md) | 撰写 ≤1000 词纯文本 rebuttal，为关键审稿人纠正事实错误，并规划条件录用的修改清单。 |
| [`siggraph-artifact-evaluation`](skills/siggraph-artifact-evaluation/SKILL.md) | 申请 Graphics Replicability Stamp（GRSI/CRCG）：确定性结果复现、随附资产、Software Heritage 存档——而非 ACM 徽章方案。 |
| [`siggraph-camera-ready`](skills/siggraph-camera-ready/SKILL.md) | 清除条件、补全 ACM TOG 期刊元数据与 rights/DOI、定稿结果视频与代表图、将代码/数据链接永久化。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 SIGGRAPH 论文，覆盖五种贡献形态（1997-2022），附自检问题与同类会议护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构实时云渲染论文的 teaser、摘要与引言按 SIGGRAPH 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享可复现性工具，并给出通用套件无法完成的 SIGGRAPH 专用检查（结果视频、确定性重生成、资产、计时）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./SIGGRAPH-Skills
claude plugin install siggraph-skills
```

也可直接使用文件：每个 `skills/siggraph-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 SIGGRAPH 还是 Eurographics/CVPR？” → `siggraph-topic-selection`
- “按 SIGGRAPH 技术论文规则审我的稿” → `siggraph-submission`
- “拿到评审了——起草 1000 词 rebuttal” → `siggraph-author-response`
- “把代码准备到 Graphics Replicability Stamp 标准” → `siggraph-artifact-evaluation`

## 目录结构

```text
SIGGRAPH-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                     # 英文说明
├── README.zh-CN.md               # 本文件
├── LICENSE                       # MIT
├── assets/cover.svg              # 封面
├── skills/
│   └── siggraph-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md            # 指向共享可复现性工具
```

## 建议用法

1. **动笔前** —— 先跑 `siggraph-topic-selection`；SIGGRAPH 与视觉会议及图形学 symposium 高度重叠，
   选会议、周期与 track 很重要。浏览 exemplars 看十年影响力的 SIGGRAPH 贡献长什么样。
2. **构建结果时** —— 让 `siggraph-experiments`、`siggraph-supplementary` 与
   `siggraph-reproducibility` 贴着工作；结果视频与忠实的 baseline 对比无法在最后一周临时补做。
3. **写作时** —— 用 `siggraph-writing-style` 对照 worked example 打磨 teaser 与首页弧线，用
   `siggraph-related-work` 做能力差定位。
4. **截止周** —— 先在较早的 form 截止日前完成 submission form（作者锁定），再用 `siggraph-submission`
   对终稿 PDF、视频与代表图逐项过审。
5. **投稿后** —— 用 `siggraph-review-process` 校准预期，用 `siggraph-author-response` 应对 rebuttal
   与任何条件录用修改，随后 `siggraph-camera-ready` 与 `siggraph-artifact-evaluation` —— 若结果
   不利，则用 `siggraph-topic-selection` 的路由表改投下一周期。

## 2026 周期锚点事实（历史快照，非永久规则）

- SIGGRAPH 2026 为**第 53 届** ACM SIGGRAPH：**洛杉矶会议中心，2026 年 7 月 19-23 日**。技术论文
  submission form **2026-01-15**（22:00 UTC），完整投稿 **2026-01-23**（22:00 UTC）；rebuttal
  **2026-03-05 至 03-12**；**>1,120** 篇投稿；发表为 **TOG 第 45 卷第 4 期**。
- SIGGRAPH Asia 2026：**马来西亚吉隆坡，2026 年 12 月 1-4 日**；技术论文 Stage-2 全文
  **2026-05-12**（上传 05-13）；SIGGRAPH 2026 之后的下一个周期目标。
- 出版：**ACM Transactions on Graphics**，期刊整合。评审：单轮，历史上为 **single-blind**，用
  **6 级尺度**，含 **≤1000 词纯文本 rebuttal**、**Technical Papers Committee 会议**，以及**条件
  录用+第二阶段**核验。格式：**acmart ≥ 2.16**；Conference track **≤7 页** + 至多两页纯图页。
  投稿系统：**Linklings**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 TOG 第 45 卷第 4 期出版、
   Conference track 7 页篇幅、1000 词 rebuttal、acmart ≥ 2.16 要求）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如 >1,120 投稿数；SIGGRAPH 2025 录用数据）。
3. **核验期不可确定项** —— 明确标为 待核实（如 SIGGRAPH 2026 确切录用数、完整 Technical Papers
   Committee/Chair 名单、2026 精确的匿名与生成式 AI 披露措辞）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。SIGGRAPH **每年两届**并每届重定结构——每次先核验是哪个周期及其
  确切 **UTC** 截止时间。
- 会议由轮换的 **Technical Papers Chair** 与 **Technical Papers Committee** 主持，而非常任
  editor-in-chief——即便**产出**是 TOG 期刊文章。不要将会议路径与 ACM TOG 的 rolling 直投流
  （另有其 EiC）混为一谈。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的
  方法名并不能证明该论文发表于 SIGGRAPH（许多首发于 Eurographics、SGP、SCA 或 UIST）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
