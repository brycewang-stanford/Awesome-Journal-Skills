# RSS Skills

面向 **RSS —— Robotics: Science and Systems** 的 12 个 agent skills。RSS 是 RSS
Foundation 主办的 single-track、高选择性机器人旗舰会议。本包覆盖完整链路：判断项目
是否具备真正的 scientific claim（而不只是一套能跑的系统）、构建经得起科学审视的
真机证据、走通 RSS 2027 在 OpenReview 上的两阶段 shepherding 流程（Extended Abstract →
受邀 rebuttal → Extension Charter → 最终论文）、直到把最终论文
发表进 roboticsproceedings.org 的免费开放获取论文集。

官方依据首次核验于 **2026-07-08**（RSS 2026；因 `roboticsconference.org` 返回 HTTP 403，
当时通过搜索引擎渲染读取），并于 **2026-11-24 重新核验并迁移到 RSS 2027**：直接抓取了
RSS 2027 主页、Call for Papers、Author FAQ、Reviewer Guidelines 与委员会页面，以及存档的
RSS 2026 CFP；roboticsproceedings.org 卷页、dblp RSS 索引与 RSS Foundation 奖项页面构成其余
依据。完整证据链（含所有 待核实 条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 当前周期状态（截至 2026-11-24）

RSS 2027（第 23 届）将于 **2027 年 7 月 6–11 日在希腊雅典**（Megaron Athens International
Conference Centre）举行，CFP 已发布。**第一个截止日期很近：Stage 1 Extended Abstract 于
2026 年 12 月 4 日截止**（AoE 晚 11:59）。之后：Stage 1 决定（拒稿或邀请 rebuttal）2027 年
2 月 5 日；rebuttal 2 月 12 日；Stage 2 决定（拒稿或 Extension Charter）2 月 26 日；最终论文
4 月 16 日；补充材料 4 月 19 日；录用通知 4 月 30 日；camera-ready 5 月 14 日。RSS 2026（悉尼，
2026 年 7 月 13-17 日）已闭幕，作为标注清楚的历史保留。

## RSS 之所以是 RSS

以下经核验的机制驱动了各 skill 中的建议：

- **一个会场，一个听众席。** 每篇录用论文都面向全体与会者报告。AC 会议上的真正
  问题不只是"这篇对不对"，而是"全领域是否必须听到它"——这就是本包反复强调单一
  可证伪 claim 的原因。
- **科学门槛，而非 demo 门槛。** 会议名称本身就是一份宣言。"我们把系统搭出来了、
  它能用"必须再提炼出可检验的洞见——隔离出的机制、测出的瓶颈、证明的性质——
  才算 RSS 形状。
- **Shepherding，而非一次性把关（2027 新制）。** RSS 2027 以两阶段流程取代单一截稿 +
  rebuttal。Stage 1 是 **6 页 Extended Abstract（5 页正文 + 1 页参考文献）**——一篇半完成的
  论文：问题、假设与方法必须完整，实验可以是初步的；6 页之外的任何内容都不评审。受邀论文
  会收到 Metareview 并可 rebuttal，随后得到 **Extension Charter**，列出最终论文必须完成的
  实验或证明。Stage 2 提交**最终论文，至多 8 页（参考文献除外）**，评判标准是是否执行了
  Charter——有充分方法支撑的负面结果不会因此被拒。
- **以假设为中心的评分。** 审稿人给 *Value of Hypothesis* 与 *Feasibility of Conclusion*
  各打 1-4 分并提出 Charter 条目；录用论文的评审意见**连同审稿人与 chair 姓名**一起公开。
- **上限即上限，简洁有奖。** 页数上限是周期政策：2026 年正文至多 8 页（参考文献除外；
  此前 2021、2022、2025 年均无硬性上限），2027 年 Stage 1 为 5 + 1 页、Stage 2 为 8 页 +
  参考文献。
- **允许用 LLM，捏造引用即出局。** RSS 2027 允许作者与审稿人使用 LLM，鼓励（但不强制）
  披露，并在自动检查后对含"幻觉"参考文献的论文直接 desk-reject。
- **论文集免费，作者零费用。** 自 2005 年起每篇 RSS 论文都在
  roboticsproceedings.org 开放获取，DOI 形如 `10.15607/RSS.*`。没有 APC，成本模型
  是注册费。
- **链接等到 camera-ready。** 2027 CFP 禁止在匿名稿中放外部链接（匿名链接也不鼓励）；
  补充材料（zip，≤100MB）只在 Stage 2 接收。
- **十二月初就截稿，全年档期拥挤。** RSS 2027 把入口从一月底提前到 12 月 4 日，早于
  ICRA/IROS/CoRL 轮转；选择 RSS 既是 fit 决策也是日历决策，本包从 RSS 的视角教这份日历。

## Skills

| Skill | 作用 |
| --- | --- |
| [`rss-topic-selection`](skills/rss-topic-selection/SKILL.md) | 用 RSS 的那一个问题检验项目，跑 claim/听众/压缩三重探针，必要时改道 ICRA、IROS、CoRL、HRI、WAFR、T-RO 或 IJRR。 |
| [`rss-workflow`](skills/rss-workflow/SKILL.md) | 对着 2027 真实日历做计划：十二月 Extended Abstract、二月 rebuttal 与 Extension Charter、四月最终论文、七月会议周，以及兄弟会议轮转。 |
| [`rss-submission`](skills/rss-submission/SKILL.md) | 审计 Stage 1 Extended Abstract（5 + 1 页）与 Stage 2 最终论文（8 页 + 参考文献）、PDF 自包含、禁链接规则，以及机器人特有的双盲清查。 |
| [`rss-writing-style`](skills/rss-writing-style/SKILL.md) | 搭建 claim 先行的首页，把每句话的口径对齐证据，预答质疑，把简洁当作会被打分的特质。 |
| [`rss-related-work`](skills/rss-related-work/SKILL.md) | 覆盖五条文献带，用对比取代罗列，处理 arXiv 并发，拆除"平台链"匿名陷阱。 |
| [`rss-experiments`](skills/rss-experiments/SKILL.md) | 从 claim 的逻辑形式推导实验条件：试验协议、机制消融、sim/real 台账纪律、失败归因。 |
| [`rss-reproducibility`](skills/rss-reproducibility/SKILL.md) | 为每个 claim 声明可复现层级，撰写平台台账，交付日志支撑的试验数据，并规划开放发布。 |
| [`rss-supplementary`](skills/rss-supplementary/SKILL.md) | 用好晚一周的补充材料截稿：把视频剪成证据、素材匿名化、归档卫生、自包含试金石。 |
| [`rss-artifact-evaluation`](skills/rss-artifact-evaluation/SKILL.md) | 按六层 artifact 栈打包：匿名评审态与公开发布态，外加诚实的闭源声明。 |
| [`rss-review-process`](skills/rss-review-process/SKILL.md) | 建模两阶段流水线、阈值闸门、AC 会议决策，以及 single-track 选择性对审稿预期的影响。 |
| [`rss-author-response`](skills/rss-author-response/SKILL.md) | 把针对 Metareview 的受邀 rebuttal 写成给 Area Chair、塑造 Extension Charter 的备忘录——有预算、有坐标、有校准的让步；没收到邀请则向前分诊。 |
| [`rss-camera-ready`](skills/rss-camera-ready/SKILL.md) | 去匿名、恢复平台署名、加入新获许可的链接、核对 roboticsproceedings.org 元数据、准备 single-track 报告。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十三条一手来源（URL + 核验日期）、访问方式说明、已核验的 RSS 2027 事实、RSS 2026 历史、显式 待核实 清单与机器可读规则块。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，外加五道作者侧核验工序（届次、格式、匿名、评审机制、决定后）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经论文集核验的 RSS 论文（2005-2023），其中四篇为 Test of Time 得主，各配自检问题与误归属护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构双臂布料论文从 demo 报告改写为可证伪 claim 的 before → after，并映射到各 skill。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享 ML 会议可复现工具包的适配器，以及它无法完成的五项机器人专属检查。 |

## 安装与使用

作为 Claude Code plugin（本目录自带 marketplace manifest，是自包含插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./RSS-Skills
claude plugin install rss-skills
```

也可直接使用文件：每个 `skills/rss-*/SKILL.md` 都是独立指令文件，frontmatter 的
`description` 告诉 agent 何时触发。典型用法：

- "这个项目到底是 RSS 论文还是 ICRA 论文？" → `rss-topic-selection`
- "对照 12 月 4 日截稿审计我们的 Extended Abstract" → `rss-submission`
- "我们被邀请回应 Metareview——2 月 12 日截止" → `rss-author-response`
- "剪补充材料视频" → `rss-supplementary`
- "录用了——最终版要改什么？" → `rss-camera-ready`

## 包结构

```text
RSS-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                # 英文说明
├── README.zh-CN.md          # 本文件
├── LICENSE                  # MIT
├── assets/cover.svg         # 封面
├── skills/
│   └── rss-<topic>/SKILL.md # 12 个 skill，一目录一文件
└── resources/
    ├── README.md            # 资源指南 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # 共享复现工具包适配器
```

## RSS 2027 锚点事实（届次快照，不是永久规则）

- RSS 2027：第 23 届，**2027 年 7 月 6–11 日，希腊雅典**（Megaron Athens International
  Conference Centre）；single-track 议程。
- 截稿（均 AoE 晚 11:59）：Extended Abstract **2026 年 12 月 4 日** · Stage 1 决定
  **2027 年 2 月 5 日** · rebuttal **2 月 12 日** · Stage 2 决定 / Extension Charter
  **2 月 26 日** · 最终论文 **4 月 16 日** · 补充材料 **4 月 19 日** · 录用通知 **4 月 30 日** ·
  camera-ready **5 月 14 日**。
- 格式：Stage 1 **6 页 = 5 页正文 + 1 页参考文献**，附录须在 5 页之内，不收补充材料；
  Stage 2 **8 页（参考文献除外）**；补充材料 zip ≤ 100MB，仅限 Stage 2；仅限 PDF、模板不得
  修改、不加页码；匿名稿不得含外部链接。
- 评审：**OpenReview 双盲**（`roboticsfoundation.org/RSS/2027/Conference`）；两阶段
  shepherding，含 Metareview、rebuttal 与 Extension Charter；录用论文的评审署名公开。2027
  Program Chair：Amanda Prorok（剑桥大学）；General Chair：Matei Ciocarlie（哥伦比亚大学，
  2026 年任 Program Chair）。
- AI：允许使用 LLM，鼓励披露，捏造引用即 desk-reject。
- 历史：RSS 2026（悉尼，2026 年 7 月 13-17 日）采用一月单一截稿（摘要 1 月 23 日、正文
  1 月 30 日）、正文 8 页（参考文献除外），以及 4 月 27 日决定前的阈值闸门式一页 rebuttal
  （4 月 3 日）。
- 发表：**roboticsproceedings.org** 免费开放获取，DOI 形如
  `10.15607/RSS.<year>.<vol>.<paper>`；全流程无作者费用。
- 用于示例库的奖项脉络：Test of Time（Square Root SAM；SARSOP；RRT*/PRM* 最优性
  论文；深度学习抓取检测）与 Early Career Award / Spotlight 系列。
- RSS 2028：截至 2026-11-24 无任何公告。

## 事实纪律

全包始终区分三类陈述：

1. **已核验的 RSS 2027 事实**——带日期，可追溯到 source map 的编号行（两阶段日历、
   5 + 1 与 8 页上限、Extension Charter、署名评审、LLM 政策）。
2. **模式**——用于规划时明确标注为模式（如为 2028 假设的"七月开会"节奏）。
3. **未核验条目**——标注 待核实 并以问题形式表述（rebuttal 格式、到场要求、注册费、
   录用率）。

任何 skill 若把第 2、3 类内容当作第 1 类呈现，应视为 bug，并对照官方页面修复。

## 维护说明

- 页数上限是**周期政策而非传统**——RSS 2021、2022 与 2025 均无硬性页数限制。每个周期
  引用格式规则前必须重开 CFP。
- 两阶段 shepherding 设计是 2027 年新制（2026 年为阈值闸门式一页 rebuttal）；为 2028
  提供建议之前，先确认该设计仍然有效。
- `roboticsconference.org` 每个周期都会重绑定到最新届次：2026 年 7 月到 11 月之间已从
  2026 切换为 2027 内容，2026 页面移到 `/2026/` 下。先看页眉横幅。
- 委员会在 RSS Foundation 下逐届轮换；不要把任何名字带入下一周期。
- 新增示例必须对照 roboticsproceedings.org 卷页（加 dblp）核验——arXiv 页面和
  项目主页不能证明一篇论文是 RSS 论文。

## License

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
