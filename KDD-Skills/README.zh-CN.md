# KDD Skills

面向 **KDD（ACM SIGKDD Conference on Knowledge Discovery and Data Mining）** 投稿的
12 个 agent skills。KDD 是数据挖掘、applied data science 与大规模知识发现的旗舰会议，
其投稿策略与单一截稿的 ML 会议有四个结构性差异，本包正是围绕它们构建：

1. **双 track、双证据标准。** Research Track 要求可命名的机制（mechanism）加消融与
   规模证据；Applied Data Science（ADS）Track 要求已部署系统并**量化 post-launch
   （上线后）表现**——2026 年 ADS CFP 明确规定缺少该量化直接 desk reject。
2. **每年两个投稿周期（cycle）。** 每个 cycle 的 abstract 截稿约早于正文一周，且
   决定选项中包含 **Resubmit**：论文可带着上一周期的审稿意见进入下一周期，但必须
   附上一页修改总结。
3. **Rebuttal 禁止超链接。** 作者回应阶段不能贴任何链接，因此在投稿 PDF 中引用的
   代码仓库是审稿人全程唯一可达的 artifact——artifact 工作必须在截稿**之前**完成。
4. **ACM 出版流水线。** 录用论文经 ACM e-rights 与 TAPS 进入 Digital Library，
   适用 ACM Open 模式；proceedings 统一 12 页预算（9 页正文，references + appendix
   合计不超过 3 页）。

官方依据核验日期：**2026-07-08**。已核验 KDD 2026 官网（第 32 届 SIGKDD 会议，
2026 年 8 月 9-13 日，韩国济州 ICC Jeju）、Research Track 与 ADS Track CFP、
Datasets & Benchmarks 与 AI for Sciences track CFP、各 track × cycle 的 OpenReview
group，以及 ACM Digital Library 的 proceedings 记录。完整来源与所有 待核实 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 已核验的 2026 周期锚点

| 事实 | 2026 年取值 | 波动性 |
|---|---|---|
| 届次 | 第 32 届 ACM SIGKDD 会议，2026-08-09 至 08-13，济州 ICC Jeju | 每届变化 |
| 投稿周期 | Cycle 1：abstract 2025-07-24、正文 2025-07-31；Cycle 2：abstract 2026-02-01、正文 2026-02-08（均 AoE） | 每周期 |
| 投稿格式 | ACM 双栏，`\documentclass[sigconf,anonymous,review]{acmart}`，8 页正文 + references + 可选 appendix，双盲 | 每周期 |
| Proceedings 预算 | 共 12 页：9 页正文 + references 与 appendix 合计 3 页以内 | 每周期 |
| ADS 门槛 | 必须量化 post-launch 表现，缺失即 desk reject | 每周期 |
| Rebuttal | 逐条回应每份审稿；**禁止超链接**；AC 给出建议，PC chairs 终审 | 每周期 |
| Resubmit 通道 | 声明上一次的 OpenReview forum id，并把一页修改总结放在 PDF 首页 | 每周期 |
| 平台 | OpenReview，全体作者 profile 须完整（近五年任职、DBLP、ORCID 等） | 每周期 |
| 出版 | ACM DL；非 ACM Open 参与机构作者可能需付 APC，ACM 已宣布 2026 年 65% 临时补贴 | 每年 |

通知与 camera-ready 日期、各类 chair 名单、费用金额等无法在线核实的条目，在来源
地图中一律标注 待核实，绝不臆测。

## Skills

选路与规划：

- [`kdd-topic-selection`](skills/kdd-topic-selection/SKILL.md)：两级选路——工作是否
  KDD 形状；再按"本周期能拿出的最强证据"选 track（Research / ADS / Datasets &
  Benchmarks / AI for Sciences），并处理 ICDM、SDM、WSDM、WWW、VLDB 与 ML 旗舰
  会议的分流。
- [`kdd-workflow`](skills/kdd-workflow/SKILL.md)：双周期流水线——选 cycle、里程碑
  倒排、rebuttal 人力预留、把 Resubmit 当作可追踪的"审稿契约"，以及 ACM 费用核查。

写作与证据：

- [`kdd-writing-style`](skills/kdd-writing-style/SKILL.md)：KDD 语域——以数据 regime
  开篇、每个效率形容词都挂到设计决策上、数据集必带规模、贡献条目陈述可证伪事实、
  ADS 的 lessons-learned 声部、8 页压缩战术。
- [`kdd-related-work`](skills/kdd-related-work/SKILL.md)：面向 KDD 自身谱系
  （DeepWalk → node2vec → metapath2vec 式的机制对比）定位，识别 venue 误标陷阱，
  以及跨周期重投与一稿多投的申报。
- [`kdd-experiments`](skills/kdd-experiments/SKILL.md)：四轴证据计划（质量、规模、
  效率、机制），时间序数据的防泄漏切分、调参对称性、消融矩阵，与 ADS 的
  post-launch 测量设计。
- [`kdd-reproducibility`](skills/kdd-reproducibility/SKILL.md)：可复现性是 AC 的
  评分维度——rerunnable / rebuildable / attested 三档诚实模型、流水线各环节钉死、
  config-as-artifact manifest、生产数字的测量协议。

打包与投稿：

- [`kdd-artifact-evaluation`](skills/kdd-artifact-evaluation/SKILL.md)：构建必须在
  PDF 内引用的匿名仓库（rebuttal 禁链使其成为唯一通道）、规模断言的 benchmark
  harness、不泄露生产数据的 ADS 证据打包。
- [`kdd-supplementary`](skills/kdd-supplementary/SKILL.md)：三容器分配（8 页正文 /
  references 之后的 appendix / 引用的仓库）、camera-ready 3 页上限陷阱、重投的
  一页修改总结。
- [`kdd-submission`](skills/kdd-submission/SKILL.md)：截稿前审计——track 与 cycle
  申报、全体作者 OpenReview profile 完整性、sigconf 格式、匿名、ADS desk-check
  暴露面、最后一周操作序列。

审稿阶段与之后：

- [`kdd-review-process`](skills/kdd-review-process/SKILL.md)：决策机器（审稿人 →
  AC 建议 → PC chairs 终审）、Accept / Resubmit / Reject 三元博弈、学界-业界混合
  审稿池的阅读习惯、生成式 AI 审稿规则。
- [`kdd-author-response`](skills/kdd-author-response/SKILL.md)：禁链条件下的
  rebuttal——用章节/表格/行号坐标锚定证据、按审稿人分箱作答、把注定不中的周期打成
  高质量 Resubmit。
- [`kdd-camera-ready`](skills/kdd-camera-ready/SKILL.md)：页数算术（12 页内 9+3）、
  e-rights、TAPS 源码处理、去匿名、ACM Open APC 状态与 DL 元数据。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：全部官方
  URL 与访问日期、已核验事实清单、待核实登记表。
- [`resources/external_tools.md`](resources/external_tools.md)：各 track CFP、
  OpenReview group、ACM DL 入口与逐周期作者核查清单。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：经 DOI 核验的
  KDD 范文（XGBoost、node2vec、DeepWalk、metapath2vec、Ad Click Prediction），
  外加 ICDM / NeurIPS / RecSys 误标防护清单。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  虚构论文的 before/after 重写，示范 KDD 首页弧线：数据 regime → 机制 → 规模证据
  → 可获得性。
- [`resources/code/README.md`](resources/code/README.md)：共享 ML 会议可复现性工具
  包的适配说明，附 KDD 特有的打包注意点。

## 建议顺序

1. **选路**：先 `kdd-topic-selection`（track 分叉优先），再 `kdd-workflow`（选 cycle）。
2. **构建**：`kdd-experiments` + `kdd-reproducibility` 出证据，同步用
   `kdd-writing-style` 与 `kdd-related-work` 成稿。
3. **打包**：`kdd-artifact-evaluation` 与 `kdd-supplementary` 必须早于截稿周完成，
   然后跑 `kdd-submission` 审计。
4. **应答**：`kdd-review-process` 读懂审稿包，`kdd-author-response` 逐条作答。
5. **出版或循环**：录用走 `kdd-camera-ready`；拿到 Resubmit 则带着审稿契约回到
   `kdd-workflow`。

## 安装

本包以 Claude Code plugin 形式发布。在本仓库根目录：

```bash
# 添加以本目录为根的 marketplace，然后安装插件
claude plugin marketplace add ./KDD-Skills
claude plugin install kdd-skills
```

也可以让 agent 直接读取 `skills/kdd-*/SKILL.md`：每个 skill 自成一体，frontmatter
描述界定触发范围，结尾的结构化输出格式便于多个 skill 串联使用。

## 范围与免责

- 本包提供的是 KDD 投稿的**策略、结构与证据**建议，不是 CFP 本身：任何内容与当前
  周期官方说明冲突时，一律以官方为准。
- 所有事实带日期。具体条目均于 2026-07-08 对照来源地图核验；不稳定项（截稿、费用、
  chair 名单）刻意写成周期波动提示或标注 待核实，绝不硬编码。
- 请勿把本包任何文字直接粘进论文：worked example 是刻意虚构的教学材料，范文库记录
  的是定位模式而非可复用的语句。

## 维护说明

- 上表所有带日期的事实都是 **2026 周期锚点，不是规则**。KDD 的周期数、页数预算、
  track 阵容（2026 年就新增了两个 track）、rebuttal 机制与 ACM Open 条款都会随
  周期调整。
- 给出任何与截稿相关的建议前，必须重开**指定 cycle 的指定 track** 的 CFP——在这个
  会议上，"KDD 的 CFP"这个说法天然歧义。
- 来源地图中标注 待核实 的条目（通知日期、chair 名单、费用），在向作者陈述前必须
  在线核实。
- 若 CFP 页面与 OpenReview 公告冲突，以较新的 OpenReview 指示或 chair 直接沟通为准，
  并记录该冲突。
- 英文版详见 [`README.md`](README.md)；两份 README 应同步更新，避免中英事实漂移。
