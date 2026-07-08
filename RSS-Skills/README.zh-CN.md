# RSS Skills

面向 **RSS —— Robotics: Science and Systems** 的 12 个 agent skills。RSS 是 RSS
Foundation 主办的 single-track、高选择性机器人旗舰会议。本包覆盖完整链路：判断项目
是否具备真正的 scientific claim（而不只是一套能跑的系统）、构建经得起科学审视的
真机证据、走通 OpenReview double-blind 流程与受邀的一页 rebuttal、直到把最终论文
发表进 roboticsproceedings.org 的免费开放获取论文集。

官方依据核验日期：**2026-07-08**。已核验 RSS 2026（悉尼）会议主页、Call for
Papers 与 review-process 页面、RSS 2026 OpenReview venue group、
roboticsproceedings.org 卷页、dblp RSS 索引，以及 RSS Foundation 奖项页面。核验
环境的网关对 `roboticsconference.org` 的直接抓取返回 HTTP 403，因此官方页面内容
通过精确 URL 的搜索引擎渲染读取，并与 roboticsproceedings.org、dblp、OpenReview
交叉核对。完整证据链（含所有 待核实 条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 当前周期状态（以核验日期为准）

RSS 2026（第 22 届）将于 **2026 年 7 月 13-17 日在澳大利亚悉尼**（UTS + 国际会展
中心）举行——距本包核验日期仅五天。2026 投稿漏斗已经关闭（摘要 1 月 23 日、正文
1 月 30 日、补充材料 2 月 6 日、受邀 rebuttal 4 月 3 日、录用通知 4 月 27 日，均
AoE）。因此本包服务两类现实用户：**处于报告与 artifact 发布阶段的录用作者**，以及
**规划 RSS 2027 的团队**——2027 的举办地、日期与截稿在核验时均未公布。

## RSS 之所以是 RSS

以下经核验的机制驱动了各 skill 中的建议：

- **一个会场，一个听众席。** 每篇录用论文都面向全体与会者报告。AC 会议上的真正
  问题不只是"这篇对不对"，而是"全领域是否必须听到它"——这就是本包反复强调单一
  可证伪 claim 的原因。
- **科学门槛，而非 demo 门槛。** 会议名称本身就是一份宣言。"我们把系统搭出来了、
  它能用"必须再提炼出可检验的洞见——隔离出的机制、测出的瓶颈、证明的性质——
  才算 RSS 形状。
- **rebuttal 要靠挣。** 2026 年采用两阶段评审：只有首轮过线的论文才被邀请提交一页
  rebuttal，且主要读者是 Area Chair。低于阈值的论文没有任何申辩机会——所以正文
  必须预先回答可预见的质疑。
- **上限即上限，简洁有奖。** 2026 年正文至多 8 页（参考文献除外），CFP 明确说这是
  ceiling 而非 floor，且审稿人偏爱不冗长的论文。（2021-2022 两届完全没有页数限制；
  格式规则在周期间确实会变。）
- **论文集免费，作者零费用。** 自 2005 年起每篇 RSS 论文都在
  roboticsproceedings.org 开放获取，DOI 形如 `10.15607/RSS.*`。没有 APC，成本模型
  是注册费。
- **链接等到 camera-ready。** 2026 CFP 只允许在最终版中放外部链接——匿名投稿必须
  完全依靠 PDF 与补充材料完成论证。
- **一月底截稿，全年档期拥挤。** RSS 位于 ICRA/IROS/RSS/CoRL 年度轮转的起点；选择
  RSS 既是 fit 决策也是日历决策，本包从 RSS 的视角教这份日历。

## Skills

| Skill | 作用 |
| --- | --- |
| [`rss-topic-selection`](skills/rss-topic-selection/SKILL.md) | 用 RSS 的那一个问题检验项目，跑 claim/听众/压缩三重探针，必要时改道 ICRA、IROS、CoRL、HRI、WAFR、T-RO 或 IJRR。 |
| [`rss-workflow`](skills/rss-workflow/SKILL.md) | 对着真实日历做计划：一月级联截稿、条件性四月 rebuttal、四月底决定、七月会议周，以及兄弟会议轮转。 |
| [`rss-submission`](skills/rss-submission/SKILL.md) | 审计三段截稿级联、8 页上限、PDF 自包含、禁链接规则，以及机器人特有的双盲清查。 |
| [`rss-writing-style`](skills/rss-writing-style/SKILL.md) | 搭建 claim 先行的首页，把每句话的口径对齐证据，预答质疑，把简洁当作会被打分的特质。 |
| [`rss-related-work`](skills/rss-related-work/SKILL.md) | 覆盖五条文献带，用对比取代罗列，处理 arXiv 并发，拆除"平台链"匿名陷阱。 |
| [`rss-experiments`](skills/rss-experiments/SKILL.md) | 从 claim 的逻辑形式推导实验条件：试验协议、机制消融、sim/real 台账纪律、失败归因。 |
| [`rss-reproducibility`](skills/rss-reproducibility/SKILL.md) | 为每个 claim 声明可复现层级，撰写平台台账，交付日志支撑的试验数据，并规划开放发布。 |
| [`rss-supplementary`](skills/rss-supplementary/SKILL.md) | 用好晚一周的补充材料截稿：把视频剪成证据、素材匿名化、归档卫生、自包含试金石。 |
| [`rss-artifact-evaluation`](skills/rss-artifact-evaluation/SKILL.md) | 按六层 artifact 栈打包：匿名评审态与公开发布态，外加诚实的闭源声明。 |
| [`rss-review-process`](skills/rss-review-process/SKILL.md) | 建模两阶段流水线、阈值闸门、AC 会议决策，以及 single-track 选择性对审稿预期的影响。 |
| [`rss-author-response`](skills/rss-author-response/SKILL.md) | 把受邀的一页 rebuttal 写成给 Area Chair 的备忘录——有预算、有坐标、有校准的让步；没收到邀请则向前分诊。 |
| [`rss-camera-ready`](skills/rss-camera-ready/SKILL.md) | 去匿名、恢复平台署名、加入新获许可的链接、核对 roboticsproceedings.org 元数据、准备 single-track 报告。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十条一手来源（URL + 核验日期）、403 访问方式说明、已核验的 2026 周期事实、显式 待核实 清单。 |
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
- "对照一月的截稿给我们做个审计" → `rss-submission`
- "我们收到了 rebuttal 邀请——一页，周五截止" → `rss-author-response`
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

## 2026 周期锚点事实（历史快照，不是永久规则）

- RSS 2026：第 22 届，**2026 年 7 月 13-17 日，澳大利亚悉尼**（UTS + 国际会展
  中心）；single-track 议程；早鸟注册截至 2026 年 5 月 11 日。
- 截稿（均 AoE）：摘要 **1 月 23 日**、正文 **1 月 30 日**、补充材料 **2 月 6 日**、
  受邀 rebuttal **4 月 3 日**、录用通知 **4 月 27 日**，均为 2026 年。camera-ready
  截稿从未公开出现——待核实，以录用邮件为准。
- 格式：**正文至多 8 页（参考文献除外）**（是 ceiling 不是 floor）；主文件仅限
  PDF；正文自包含；附录进补充材料；外部链接仅限 camera-ready；没有独立的 demo
  论文类别。
- 评审：**OpenReview 双盲**（`roboticsfoundation.org/RSS/2026/Conference` group）；
  两阶段、阈值闸门、一页 rebuttal 由 Area Chair 阅读；决定出自 AC 会议。2026
  Program Chair：Matei Ciocarlie（哥伦比亚大学）。
- 发表：**roboticsproceedings.org** 免费开放获取，DOI 形如
  `10.15607/RSS.<year>.<vol>.<paper>`；全流程无作者费用。
- 用于示例库的奖项脉络：Test of Time（Square Root SAM；SARSOP；RRT*/PRM* 最优性
  论文；深度学习抓取检测）与 Early Career Award / Spotlight 系列。
- RSS 2027：核验时无任何公告——地点、日期、截稿均 待核实。

## 事实纪律

全包始终区分三类陈述：

1. **已核验的 2026 周期事实**——带日期，可追溯到 source map 的编号行（截稿级联、
   页数上限、rebuttal 设计）。
2. **模式**——用于规划时明确标注为模式（为 2027 假设的"一月底截稿 / 七月开会"
   节奏）。
3. **未核验条目**——标注 待核实 并以问题形式表述（camera-ready 日期、到场要求、
   补充材料大小上限、录用率、AI 使用政策）。

任何 skill 若把第 2、3 类内容当作第 1 类呈现，应视为 bug，并对照官方页面修复。

## 维护说明

- 8 页上限是**周期政策而非传统**——RSS 2021 与 2022 完全没有页数限制。每个周期
  引用格式规则前必须重开 CFP。
- 两阶段 rebuttal 设计仅对 2026 核验过；在建议作者依赖（或放弃）申辩机会之前，
  先确认该设计仍然有效。
- `roboticsconference.org` 每个周期都会重绑定到最新届次：曾显示 2026 内容的 URL
  会悄悄变成 2027 内容。先看页眉横幅。
- 委员会在 RSS Foundation 下逐届轮换；不要把任何名字带入下一周期。
- 新增示例必须对照 roboticsproceedings.org 卷页（加 dblp）核验——arXiv 页面和
  项目主页不能证明一篇论文是 RSS 论文。

## License

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
