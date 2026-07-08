# SODA 技能包（中文说明）

面向 **SODA——ACM-SIAM 离散算法研讨会（ACM-SIAM Symposium on Discrete
Algorithms）** 投稿的十二个智能体技能。SODA 由 SIAM 离散数学活动组（SIAG/DM）与
ACM 算法与计算理论特别兴趣组（SIGACT）联合主办，是算法社区推进"数量边界"的主
场：运行时间、近似比、数据结构界，以及支撑它们的离散数学。本技能包覆盖完整周
期：判断结果是否"SODA 形状"、为 HotCRP 构建不限页数的完整版投稿、通过轻量级双
盲评审与九月初为期三天的 rebuttal，再把十月的录用转化为 SIAM 会议论文集条目和
一月的现场报告。

官方依据核查日期：**2026-07-08**。核查对象包括 SIAM 的 SODA 2027 会议页与投稿
页、`soda27.hotcrp.com`、ALENEX 2027 与 SOSA 2027 页面、SIAM epubs 论文集卷
（2021–2026）、dblp 系列记录以及各机构的最佳论文公告。核查环境中 `siam.org`、
`hotcrp.com`、`dblp.org` 均拒绝直接抓取（HTTP 403），故通过搜索引擎渲染读取原始
URL 并跨源交叉验证；完整证据链与全部"待核实"条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## SODA 区别于兄弟会议的机制

以下 2027 周期已核实事实驱动了本包的大部分建议，也对应外来作者最常犯的错误：

- **不限页数，投稿即完整版。** CFP 鼓励提交论文完整版：标题页含 1–2 段摘要，
  之后是全部内容，证明一律在内。"细节见完整版"是别处的话术，在 SODA 是失误。
- **七月截稿、一月开会。** SODA 2027：2026 年 7 月 9 日（AoE）截稿，2027 年
  1 月 24–27 日在费城举行。SODA 占据理论年历的"夏季席位"，介于 STOC 的十一月
  截稿与 FOCS 的四月截稿之间。
- **轻量级双盲。** PDF 上不得出现姓名、单位、邮箱——但明确允许挂 arXiv、作报
  告；重要文献（包括自引）不得省略、不得匿名化。
- **存在简短 rebuttal。** 初审意见最迟 2026 年 9 月 1 日送达作者，回复截止
  9 月 4 日。只有三天——准备工作属于八月，不属于九月。
- **SIAM 出版机器。** 论文集进入 SIAM Publications Library，DOI 前缀
  `10.1137/1.978...`；终版要求随十月录用邮件下发。
- **各有使命的卫星会。** ALENEX（实验算法学，2026 年 7 月 20 日截稿，含正式
  制品评测）与 SOSA（算法简洁性，8 月 6 日截稿）与主会同址举行——它们正好接住
  SODA 评审会低估的那类论文。

## 技能一览

| 技能 | 作用 |
| --- | --- |
| [`soda-topic-selection`](skills/soda-topic-selection/SKILL.md) | 三问适配测试（有界可陈述？专家可读？离散技术？），并在 SODA、STOC/FOCS、ITCS、ESA/ICALP、SOSA、ALENEX、SoCG 与期刊之间路由。 |
| [`soda-workflow`](skills/soda-workflow/SKILL.md) | 运营七月到一月的全周期：倒排到 7 月 9 日、评审静默期任务、九月冲刺、十月分叉与卫星会编排。 |
| [`soda-writing-style`](skills/soda-writing-style/SKILL.md) | 打磨可引用的标题界、竞标面摘要、前十页综述契约与既有界对照表。 |
| [`soda-related-work`](skills/soda-related-work/SKILL.md) | 扫五条文献带，经 dblp 与期刊版核对界的沿革，处理 arXiv 优先权文化与双盲下的自引。 |
| [`soda-experiments`](skills/soda-experiments/SKILL.md) | 判断数值实验是否该出现、诚实标注其主张类别，并把以实现为主的工作路由到 ALENEX 或 SEA。 |
| [`soda-reproducibility`](skills/soda-reproducibility/SKILL.md) | 建立主张台账、执行"盲校对"证明检查、审计外部定理与概率预算、为机器验证步骤配证书。 |
| [`soda-supplementary`](skills/soda-supplementary/SKILL.md) | 架构那份唯一的不限页 PDF——前后件契约、按依赖排序的附录、定理重述——因为不存在补充材料通道。 |
| [`soda-artifact-evaluation`](skills/soda-artifact-evaluation/SKILL.md) | 打包计算机辅助证明证据与证书、保持存档匿名安全，制品为主时改走 ALENEX 的 AE 流水线。 |
| [`soda-submission`](skills/soda-submission/SKILL.md) | 终审：格式底线、轻量双盲清扫、完整性检查、HotCRP 记录卫生与"径直拒稿"触发条件。 |
| [`soda-review-process`](skills/soda-review-process/SKILL.md) | 建模评审流水线——竞标、子评审人、rebuttal、程序委员会合议、十月决定——以及什么真正能扳动边缘论文。 |
| [`soda-author-response`](skills/soda-author-response/SKILL.md) | 打好三天 rebuttal：八月备料、F/L/S/C 意见分诊、锚定定理的编号回复、干净的让步。 |
| [`soda-camera-ready`](skills/soda-camera-ready/SKILL.md) | 把完整版压缩为 SIAM 论文集版本、恢复署名、同步 arXiv、准备费城报告。 |

## 资源层

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个一手来源加奖项来源（URL 与访问日期）、已核实的 2027 周期事实、访问方式说明与完整"待核实"清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口与上传前的五道作者侧核验工序。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 四篇经归属核实、最佳论文级的 SODA 范文（2021–2025），覆盖四个问题带，各配自检问题与防误归属流程。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构动态数据结构论文的摘要与综述开头：从"限页venue习惯"重建为 SODA 双读者形态的前后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享打包冒烟检查器的适配说明，外加四项脚本查不出的 SODA 特有检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./SODA-Skills
claude plugin install soda-skills
```

也可直接使用文件：每个 `skills/soda-*/SKILL.md` 都是独立的指令文件，其
frontmatter `description` 说明触发时机。典型用法：

- "这个最小割改进投 SODA 还是等 STOC？" → `soda-topic-selection`
- "按 SODA 的格式和双盲规则审我的稿子" → `soda-submission`
- "9 月 1 日出意见——帮我排 rebuttal 计划" → `soda-author-response`
- "证明里有穷举搜索计算——怎么交付？" → `soda-artifact-evaluation`

## 建议路线

1. **动笔前**：先跑 `soda-topic-selection`，对照范文库确认"命名问题、卡住的边
   界、可量化推进"三要素齐备；不齐就换目标会议，省下一个周期。
2. **构建期**：`soda-reproducibility` 的主张台账与盲校对流程越早装配越便宜；
   `soda-writing-style` 与 `soda-supplementary` 分治前件与后件。
3. **截稿周**：按 [`resources/external_tools.md`](resources/external_tools.md)
   的五道工序核验，再走 `soda-submission` 全流程；AoE 截止不要心算时区。
4. **投稿后**：八月按 `soda-author-response` 备料，九月三天窗口全员在线；
   十月依结果走 `soda-camera-ready` 或 `soda-review-process` 的改道分支。

## SODA 在理论年历中的席位

理论组的排期单位不是单个截稿日，而是三个轮转的节拍；SODA 占据其中的夏季席位：

| 节拍 | 截稿季 | 开会季 | 2026–27 锚点 |
| --- | --- | --- | --- |
| SODA | 七月上中旬 | 一月 | 2026-07-09 截稿 → 2027-01-24/27 开会 |
| STOC | 十一月上旬 | 六月 | 模式性描述；2027 具体日期待核实 |
| FOCS | 四月上旬 | 秋季 | 模式性描述；2027 具体日期待核实 |

由此推出的排期逻辑：春季完工的结果自然投七月的 SODA；十月收到 SODA 拒稿距
STOC 截稿约一个月——够做表达层手术、不够做新数学；错过 7 月 9 日则等四个月
（STOC）、九个月（FOCS）或十二个月（下届 SODA）。理论文化从不惩罚晚一年的好
结果，永远惩罚按时交付的坏引理。详见
[`skills/soda-workflow`](skills/soda-workflow/SKILL.md)。

## 2027 周期锚点事实（历史快照，非永久规则）

- SODA 2027：**费城，2027 年 1 月 24–27 日**；按届数为第 38 届（2025 = 36 届、
  2026 = 37 届均已核实，2027 为推算）。
- 论文截稿 **2026 年 7 月 9 日（AoE）**，平台 `soda27.hotcrp.com`。
- 初审意见 **9 月 1 日前** 送达；回复截止 **9 月 4 日**；**10 月** 发决定与终
  版要求。
- 格式：**不限页数**（鼓励完整版）；标题页 1–2 段摘要；11 磅以上、单栏、1 英寸
  页边距、letter 纸型；违规有径直拒稿风险。
- 评审：**轻量级双盲**；arXiv 与报告自由；重要文献不得省略或匿名化。
- 同址卫星会：**ALENEX 2027**（1 月 24–25 日；7 月 20 日截稿；制品 9 月 11 日；
  AE 结果最迟 10 月 16 日）与 **SOSA 2027**（1 月 25–26 日；8 月 6 日截稿）。
  历史上的第三卫星会 ANALCO 在 dblp 的最后记录为 2019 年。
- 论文集 DOI 锚点（epubs.siam.org）：`10.1137/1.9781611976465`（2021）、
  `...977912`（2024）、`...978322`（2025）、`...978971`（2026）。

## 事实纪律

全包区分三类陈述并保持可辨识：

1. **已核实的 2027 周期事实**——带日期、可回溯到来源表编号（如 7 月 9 日截稿、
   格式底线、rebuttal 窗口）。
2. **转述事实**——仅见于可信二手来源并如实标注（如 2026 届程序委员会主席公布
   的投稿量创纪录消息）。
3. **核查时无法确认的条目**——一律标"待核实"并以问题形式表述（2027 程序委员会
   主席、终版机制、注册义务、论文集访问模式）。

若发现技能中把第 2、3 类当作第 1 类陈述，视为 bug，对照 SIAM 在线页面修正。

## 维护须知

- 上述所有日期都是 **2027 周期快照**。SODA 的程序委员会逐届重组，政策随之重
  设；给出任何截稿敏感建议前，先打开
  `siam.org/conferences-events/siam-conferences/soda<yy>/` 的当届页面。
- rebuttal 是近年才制度化的做法（至 2026 届成型），不是古老传统：每届都应重新
  确认其日期与机制，不要沿用假设。
- 终版页数、SIAM 宏包、注册规则随录用邮件下发，本包一律标"待核实"——绝不虚构。
- 新增范文请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程：dblp 加 epubs DOI 双重确认，因为 SODA/STOC/FOCS 的边界正是
  记忆最容易张冠李戴的地方。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
