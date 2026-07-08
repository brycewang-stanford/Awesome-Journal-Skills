# ECCV Skills（中文说明）

面向 **ECCV（European Conference on Computer Vision，欧洲计算机视觉会议）**
投稿的 12 个 agent skills。ECCV 是视觉领域的**偶数年旗舰会议**，由欧洲计算机
视觉协会（ECVA）主办，论文集走 **Springer LNCS，并由 ECVA 提供免费开放获取
镜像**——不是 CVF open access。这一出版机制差异，加上两年一届的节奏和
单栏 14 页的 LNCS 版式，是本包与 CVPR / ICCV 两个姊妹包在机制层面的真实
分界线，也是所有 skill 的组织主线：投 ECCV 是一笔以两年为单位的下注。

官方依据核验日期：**2026-07-08**。已核验 ECCV 2026 的 Dates、Call for
Papers、Submission Policies、What's New、FAQ、Reviewer Guide 页面，ECCV 2026
OpenReview group，SpringerLink 的 ECCV 论文集系列，以及 ECVA papers 门户。
核验环境直接访问 `eccv.ecva.net` 返回 HTTP 403，因此官方页面内容通过对精确
官方 URL 的搜索引擎渲染读取，并与 OpenReview、SpringerLink、ECVA、dblp
交叉核对。完整的来源链——URL、访问日期、"仅为转述"的事实与全部**待核实**
条目——见 [`resources/official-source-map.md`](resources/official-source-map.md)。

**周期状态（2026-07-08）：** ECCV 2026（瑞典马尔默，9 月 8–13 日，Malmö
Arena 与 Malmömässan）正处周期中段：3 月 5 日投稿截止、5 月 2–11 日
rebuttal 窗口、6 月 17 日录用通知均已过去，6 月 30 日 AoE 的 camera-ready
截止刚刚结束。因此本包重点教**当前进行时**的阶段——Springer camera-ready
收尾、6 月到 9 月的 artifact 发布跑道、会前约四周出现的 ECVA 开放获取副本、
以及被拒论文向 CVPR 11 月截止日的改投——并给出 **ECCV 2028** 的整周期
规划（2028 的一切细节均未公布，待核实）。

## 本包依据的核心事实

以下 2026 周期锚点均可在 source map 中溯源：

- **偶数年、两年一届。** ECCV 与 CVPR（每年）、ICCV（奇数年）构成互补三角；
  多个 skill 从 ECCV 视角教这张改投日历：6 月被拒，自然流向 CVPR 的
  11 月截止日。
- **三段式投稿链，走 CET 时钟。** 注册 2 月 26 日 → 正文 3 月 5 日晚
  11 点 **CET**（不是 AoE；聚合站因时区换算相差一天）→ 补充材料 3 月
  12 日。CVF 系姊妹会议已取消的"补充材料晚一周"结构在 ECCV 仍然保留。
- **Springer LNCS 版式。** 单栏 14 页，**图表计入页数**，超出部分只允许
  参考文献；模板自 2024 年后已更换。与任何双栏 CVF 版式的页面经济学
  完全不同。
- **五月的一页纸。** 5 月 2 日出评审；rebuttal 可选，5 月 11 日截止，
  一页双栏 PDF 且**参考文献计入页内**；5 月 12 日送达审稿人；6 月 17 日
  出结果。
- **面向作者的执法。** 全体作者都被要求在受邀时愿意审稿；迟交或"高度
  不负责任"的评审——包括违反与 CVPR 2026 对齐的 LLM 禁令——会使该审稿人
  **名下全部投稿**面临 desk rejection。
- **Springer + ECVA 出版。** Camera-ready 6 月 30 日 AoE（延期后）；出版
  以至少一位作者注册参会为前提；开放获取副本经 Springer 和/或 ECVA
  在会前不早于约四周上线；免费镜像在 ecva.net，而非 openaccess.thecvf.com。
- **规模锚点（转述级）。** ECCV 2024（米兰，第 18 届）：LNCS 第 15059–15147
  卷，8,585 篇投稿录用 2,387 篇。
- **生态。** 2026 年列出 93 个 workshop（9 月 8–9 日）；ECVA 的 Koenderink
  Prize 每届授予十年前发表于 ECCV 的论文——本包将其用作"耐久性"品味
  信号，而非规则。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`eccv-topic-selection`](skills/eccv-topic-selection/SKILL.md) | 给两年期下注定价：ECCV 型选题判定，CVPR/ICCV/WACV/BMVC/ACCV/期刊分流，耐久性与"底座无关性"测试。 |
| [`eccv-workflow`](skills/eccv-workflow/SKILL.md) | 跑完偶数年战役：CET 截止链、从 ECCV 视角的改投三角、2026 周期当前位置、倒排 2028 年 3 月的计划。 |
| [`eccv-writing-style`](skills/eccv-writing-style/SKILL.md) | 为单栏 14 页 LNCS 经济学写作：页数台账、面向邻近方向审稿人的首页架构、数字引用文风、可被一页 rebuttal 守住的措辞。 |
| [`eccv-related-work`](skills/eccv-related-work/SKILL.md) | 覆盖间隔两年中的两届 CVPR 与一届 ICCV，处理 3 月截止日的 concurrent 惯例与"不得引用自家仓库"规则，核对 Springer/CVF 出处。 |
| [`eccv-experiments`](skills/eccv-experiments/SKILL.md) | 构造撑到 9 月的证据：六个月失效测试、底座对齐的公平对比表、机制隔离消融、"证伪实验先行"的排程。 |
| [`eccv-reproducibility`](skills/eccv-reproducibility/SKILL.md) | 满足两年可核查期：训练配方台账、基础模型 pinning 块、benchmark 增量的方差诚实度、正文/补充/代码归档的分层。 |
| [`eccv-supplementary`](skills/eccv-supplementary/SKILL.md) | 用好晚一周的补充截止：+7 天的正当用途、视频与定性结果打包、归档匿名清扫、正文自足性检查。 |
| [`eccv-artifact-evaluation`](skills/eccv-artifact-evaluation/SKILL.md) | 两阶段 artifact 生命周期：评审期的匿名封存归档，与 6→9 月十周公开发布跑道，对齐 ECVA/Springer 副本。 |
| [`eccv-submission`](skills/eccv-submission/SKILL.md) | 上传前终审：注册→正文→补充的 CET 链条、14 页门槛、一稿多投与社媒禁令、合作者审稿义务带来的连坐风险。 |
| [`eccv-review-process`](skills/eccv-review-process/SKILL.md) | 建模评审管线：OpenReview 各阶段到 6 月 17 日决定、2026 执法机制与 LLM 评审禁令、评审组构成、AC 讨论的杠杆点。 |
| [`eccv-author-response`](skills/eccv-author-response/SKILL.md) | 花好那一页：九天日程、按审稿人分配的页面预算（参考文献占页）、新实验的判断规则、可被 AC 直接引用的段落。 |
| [`eccv-camera-ready`](skills/eccv-camera-ready/SKILL.md) | 交付 Springer + ECVA 定稿：放宽后的页数预算、版权表与注册前提、rebuttal 承诺台账、arXiv 同步、马尔默行程。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十条来源及访问日期，"已核验/转述/待核实"三级分级，以及访问方式披露。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，加五个作者侧核验流程（时钟、模板、政策、审稿义务、出版记录）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经 Springer 溯源核验的 ECCV 范文（COCO、SSD、Perceptual Losses、NeRF、RAFT），附自检问题与三大会误归属防呆清单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构稀疏视角重建论文的首页，改写前 → 改写后，附迁移清单。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享 ML 会议可复现性工具包的适配层，外加五项 ECCV 专属检查。 |

## 安装与使用

本目录本身就是一个带 marketplace 清单的 Claude Code 插件。在仓库克隆内
先执行 `claude plugin marketplace add ./ECCV-Skills`，再执行
`claude plugin install eccv-skills` 即完成安装。

不装插件也可以：每个 `skills/eccv-*/SKILL.md` 的 frontmatter 已声明触发
时机，可直接作为指令文件加载。几个典型场景：

| 你的问题 | 对应 skill |
| --- | --- |
| 这篇重建论文等 ECCV 2028，还是 11 月投 CVPR？ | `eccv-topic-selection` + `eccv-workflow` |
| 冻结前按 LNCS 规则过一遍 PDF | `eccv-submission` + `eccv-writing-style` |
| 三份评审、一页纸、九天 | `eccv-author-response` |
| 中了——从录用到马尔默之间要做什么？ | `eccv-camera-ready` + `eccv-artifact-evaluation` |

## 目录结构

顶层为 `.claude-plugin/`（plugin.json 与 marketplace.json，声明全部 12 个
skill 路径）、双语 README、MIT `LICENSE`，以及 `assets/cover.svg`
（偶数年桥形主题封面）。`skills/` 下是 12 个 `eccv-<topic>/SKILL.md`
目录；`resources/` 下是 `README.md`、`official-source-map.md`、
`external_tools.md`、`exemplars/library.md`、
`worked-examples/01-introduction.md` 与 `code/README.md` 六个支撑文件，
共 25 个文件。

## 事实纪律

本包的陈述分三级，且在所有文件中保持可区分：

1. **已核验的 2026 周期事实**——可追溯到 source map 的编号条目（CET 截止
   链、含图表的 14 页规则、参考文献占页的一页 rebuttal、审稿义务执法、
   Springer/ECVA 出版路径）。
2. **转述级事实**——多个二手渲染一致但未在原始页面重验（2024 录用数据、
   camera-ready 15 页限额及其计页口径、93 个 workshop）。
3. **待核实条目**——以开放问题的形式表述（2026 届的正式届数、rebuttal
   新结果规则的原文、补充材料大小上限、参会报告义务，以及 2028 的
   全部流程）。

任何 skill 把第 2/3 级材料当第 1 级陈述都是 bug，应对照在线页面修正。

## 与 CVPR / ICCV 姊妹包的边界

三个视觉旗舰各有独立深度包，请按机制而不是按声望选包：

- **出版管道不同。** ECCV 的定稿走 Springer LNCS 图书系列，免费副本在
  ecva.net；CVPR/ICCV 走 CVF open access 加 IEEE Xplore。引用格式、
  版权表、开放获取时点因此完全不同。
- **版式不同。** ECCV 是单栏 LNCS、14 页含图表；CVF 系是双栏、页数
  上限更紧。同一篇稿子换会必须重排版并重算页数预算，本包的
  `eccv-writing-style` 只教单栏经济学。
- **节奏互补。** ECCV 只在偶数年 9 月前后开会；错过 3 月截止意味着在
  本会等两年，所以 `eccv-workflow` 教的是把 CVPR 的 11 月截止与
  ICCV 的奇数年 3 月截止当作显式退路的改投三角。
- **补充材料机制不同。** 2026 年 ECCV 保留了"正文冻结后一周再交补充
  材料"的结构，而 CVF 姊妹会议已改为同日提交——两边的打包节奏不能
  互相套用。

## 维护说明

- 下一个真正的更新时点是 eccv.ecva.net 上 ECCV 2028 页面上线：主办地、
  截止链及其时钟、页数规则与计页口径、rebuttal 版式、执法措辞与平台都
  需要重验。
- 优先看每届的 "What's New" 页——2026 年该页的政策密度最高（审稿义务
  执法、LLM 禁令、camera-ready 延期）。
- CET 与 AoE 之分在 2026 年造成过聚合站的真实分歧；引用任何截止日都
  必须带时区与来源。
- 新增范文必须通过 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的 SpringerLink 核验流程；LNCS 排版本身不能证明论文属于 ECCV。

## 许可证

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
