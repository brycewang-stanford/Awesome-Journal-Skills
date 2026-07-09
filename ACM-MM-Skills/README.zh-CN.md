# ACM MM Skills

面向 **ACM MM（ACM International Conference on Multimedia，ACM 国际多媒体会议）** 论文的
12 个 agent skills。ACM MM 是 **ACM SIGMM** 的旗舰年会，也是多媒体领域的核心会场——它关注
的是*同时处理多种媒介*的工作：视觉与音频、语言、传感、交互的融合，以及承载、索引、渲染这些
内容的系统。本包覆盖 ACM MM 的完整流程：判断项目是否真正是多媒体贡献（而不是单模态的计算机
视觉或 NLP 结果）、在 16 个 thematic area 与多个 track 之间选择、走通 4 月的 OpenReview
截止链条、撰写匿名 rebuttal，并以 ACM `sigconf` 版式在 ACM Digital Library 中发表。

官方依据核验日期：**2026-07-09**。已核验 ACM MM 2026 官网（`2026.acmmm.org`）的 Calls &
Dates、Important Dates、Call for Technical Papers、Topics of Interest、Review Process
Guidelines，以及 Reproducibility / Open Source / Dataset / Brave New Ideas / Grand
Challenge 各 track 的 call；ACM MM 2026 的 OpenReview groups；ACM Digital Library 会议
论文集；dblp 的 `conf/mm` 索引；以及 `sigmm.org`（Test-of-Time 奖、主办邀请）。核验环境中
对 `2026.acmmm.org` 的直接抓取被拦截（HTTP 403），因此官方页面通过搜索引擎对精确 URL 的
渲染阅读，并与 OpenReview、ACM DL、dblp、SIGMM news 交叉核对；完整链路（含所有仍标注
待核实 的条目）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

**周期状态（2026-07-09）：** ACM MM 2026（里约热内卢，2026 年 11 月 10–14 日）是*当前进行中*
的周期。投稿链条已于 4 月结束（摘要 3 月 25 日、正文 4 月 1 日、补充材料 4 月 8 日），匿名
rebuttal 窗口在 6 月初，而**作者通知恰在 7 月初送达**——本包正是在 decision 与 camera-ready
的交界处撰写。录用作者进入 camera-ready 阶段（据报为 8 月 6 日）；被拒作者正在改投。MM 2027
计划落在亚洲/大洋洲（据报为香港），核验时其 CFP 与日期尚未公布。

## ACM MM 与兄弟会议的不同

驱动本包建议的、已核验的 2026 周期机制：

- **多媒体，而非单一模态。** 核心判据是*跨模态融合或媒体系统贡献*——视觉+音频+语言+传感、
  体验质量（QoE）、传输/分发、艺术与文化。纯目标检测应投 CVPR/ICCV，纯语言模型应投 ACL；
  ACM MM 要的是它们之间的接缝。
- **16 个 thematic area，一个主 track。** 投稿需选定一个 thematic area（Multimodal Fusion、
  Generative and Foundation Models、Search and Recommendation、情感/参与、艺术与文化、
  系统、Transport and Delivery、Responsible Multimedia 等），该领域决定哪些 reviewer 看到论文。
- **以 ACM 标准论属于短文。** 正文 6–8 页，使用 **ACM `sigconf` 模板**，参考文献可额外占用最多
  两页、且这两页只能放参考文献。超页论文不经评审直接 desk-reject。
- **双盲，但有明确例外。** 主 track 与多数 track 双盲；**Reproducibility、Open Source
  Software、Dataset** 三个 track 单盲，因为其 artifact 本身就是论文、无法匿名。
- **专门的 track 生态。** 主 track 之外还有 Brave New Ideas（愿景论文）、Multimedia Grand
  Challenge、Open Source Software Competition、带 ACM artifact badging 的 Reproducibility
  track、Interactive Art、Doctoral Symposium 与 workshops——各有独立 call 与规则。
- **用 OpenReview，但非 NeurIPS 式开放。** ACM MM 2026 在 OpenReview 上运行、含可选的匿名
  rebuttal；评审默认不公开，社区惯例是封闭的、带 ACM badge 的评审，而非公开论坛。
- **发表走 ACM，而非默认开放获取。** 录用论文进入 **ACM Digital Library**；无面向作者的 APC，
  但 ACM 的版权/OA 选项（含 ACM Open）与 sigconf 版权块在 camera-ready 时确定。无常设主编——
  轮换的对应角色是每届的 Program Chairs 与 General Chairs。

## Skills

| Skill | 作用 |
| --- | --- |
| [`acmmm-topic-selection`](skills/acmmm-topic-selection/SKILL.md) | 判断是否真正是多媒体贡献、选 thematic area，并在 ACM MM、CVPR/ICCV、ACL、ICMR、MMSys、NeurIPS/ICLR、TOMM 间路由。 |
| [`acmmm-workflow`](skills/acmmm-workflow/SKILL.md) | 从 thematic-area 定位到 4 月 OpenReview 链条、6 月 rebuttal、7 月 decision、8 月 camera-ready、11 月现场报告的 SIGMM 日历。 |
| [`acmmm-writing-style`](skills/acmmm-writing-style/SKILL.md) | 写好多媒体首页：把跨模态贡献前置、把媒体证据当证据呈现、把论证压进 6–8 页 sigconf。 |
| [`acmmm-related-work`](skills/acmmm-related-work/SKILL.md) | 覆盖多媒体文献的分布——视觉、音频/语音、语言、HCI/QoE、系统——处理 arXiv 并发，并核实所引"ACM MM 论文"确属 ACM MM 而非 ICMR/CVPR。 |
| [`acmmm-experiments`](skills/acmmm-experiments/SKILL.md) | 设计跨模态证据：各模态的匹配 baseline、隔离融合作用的 ablation、主观质量为核心时的 user study/QoE，以及诚实的算力报告。 |
| [`acmmm-reproducibility`](skills/acmmm-reproducibility/SKILL.md) | 面向 ACM badging 流程做准备：环境捕获、数据/媒体获取、随机种子，以及 Reproducibility track 通往 Artifacts Evaluated / Results Reproduced 的路径。 |
| [`acmmm-supplementary`](skills/acmmm-supplementary/SKILL.md) | 组织正文后一周截止的补充材料：视频/音频演示、appendix，以及能在 reviewer 机器上正常渲染的匿名媒体。 |
| [`acmmm-artifact-evaluation`](skills/acmmm-artifact-evaluation/SKILL.md) | 构建匿名评审 artifact 与公开发布，并在 Open Source Software Competition、Dataset track 与主 track 补充证据间抉择。 |
| [`acmmm-submission`](skills/acmmm-submission/SKILL.md) | 最终 OpenReview 审查：thematic area、sigconf 页数预算、匿名 vs. 具名单盲 track、媒体/链接排查、一稿多投、desk-reject 分诊与末周排序。 |
| [`acmmm-review-process`](skills/acmmm-review-process/SKILL.md) | 建模 ACM MM 流程——thematic-area 路由、reviewer 与 AC、匿名 rebuttal、meta-review，以及 oral/poster 与奖项分层。 |
| [`acmmm-author-response`](skills/acmmm-author-response/SKILL.md) | 把多份评审整理成一份合规的匿名 rebuttal：先纠事实错误、补小型确认实验、有分寸地让步、不加新链接。 |
| [`acmmm-camera-ready`](skills/acmmm-camera-ready/SKILL.md) | 交付 ACM 定稿：去匿名、ACM 版权/CCS 元数据、sigconf 合规、artifact 发布、注册与里约现场报告准备。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | ACM MM 2026 官方来源及访问日期、已核验的 2026 周期事实、访问方式说明与明确的 待核实 列表。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 在用官方入口（官网、OpenReview groups、ACM DL、dblp、SIGMM）以及每个周期要跑的作者侧核验流程。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经元数据核验的 ACM MM 论文（Caffe、VLFeat、情感图像分类、对抗式与自编码器跨模态检索），附避免误标的护栏清单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构跨模态论文首页的改写：before → after，让首页先讲多媒体贡献。 |
| [`resources/code/README.md`](resources/code/README.md) | 通向共享 ML 会议可复现套件的适配器，加上 ACM MM 专属检查（媒体渲染、演示素材匿名、badging 就绪度）。 |

## 常见误投（用 `acmmm-topic-selection` 自查）

- **单模态穿上多媒体外衣**：音频/文本只是附加、从未被证明起作用。若 leave-one-modality-out
  ablation 后结果几乎不变，评审会判定其并非跨模态——纯视觉投 CVPR/ICCV，纯语言投 ACL。
- **把兄弟会议当 ACM MM**：ICMR（检索）、MMSys（系统）、ACM Multimedia Asia、TOMM（期刊）
  各有不同门槛与引用串，务必在 dblp `conf/mm` 上核对版次行。
- **主观主张无 user study**："更自然/更具吸引力"须以主观评测支撑，而非断言。

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./ACM-MM-Skills
claude plugin install acm-mm-skills
```

也可直接使用文件：每个 `skills/acmmm-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 说明何时触发。典型调用：

- "这是 ACM MM 论文，还是该投 CVPR / ACL？" → `acmmm-topic-selection`
- "按 ACM MM 页数、sigconf 与匿名规则审查我的稿件" → `acmmm-submission`
- "评审出来了——规划匿名 rebuttal" → `acmmm-author-response`
- "拿 Reproducibility badge 和 camera-ready 需要交什么？" → `acmmm-camera-ready`

## 2026 周期锚点事实（历史快照，非永久规则）

- ACM MM 2026：2026 年 11 月 10–14 日，巴西里约热内卢；第 34 届；由 ACM SIGMM 组织。
- 截止日期（AoE）：摘要 3 月 25 日 · 正文 4 月 1 日 · 补充材料 4 月 8 日 · rebuttal 6 月 4 日 ·
  作者通知 7 月初（CFP 页写 7 月 7 日；Important Dates 与 Dataset 页写 7 月 9 日）· camera-ready
  据报 8 月 6 日。
- 版式：正文 6–8 页、ACM `sigconf` 模板，参考文献最多额外两页且只放参考文献；超页 desk-reject；
  经 OpenReview 投稿。
- Track：主 track（16 个 thematic area）、Dataset、Brave New Ideas、Multimedia Grand
  Challenge、Open Source Software Competition、Reproducibility（ACM badging）、Interactive
  Art、Doctoral Symposium、workshops、tutorials、panels、demos。
- 评审：主 track 双盲；Reproducibility、Open Source Software、Dataset 单盲；含可选匿名 rebuttal。
- 发表：ACM Digital Library；无作者侧 APC；ACM 版权/OA 在 camera-ready 确定；无常设主编——
  Program/General Chairs 每届轮换。

## 事实纪律

本包全程区分三类陈述：

1. **已核验的 2026 周期事实**——可追溯到 source map 中带编号的来源（如里约日期、4 月 1 日正文
   截止、6–8 页 sigconf 预算、具名单盲 track）。
2. **据报事实**——有一致的二手来源并如实标注（如来自 deadline 镜像的 8 月 6 日 camera-ready、
   MM 2027 的香港主办）。
3. **核验时无法确证的条目**——明确标注 待核实 并以问题形式表述（如 7 月 7 日 vs. 7 月 9 日的
   通知日期冲突、补充材料大小上限、ACM 版权/OA 表单细节、各 track 奖项结构，以及 2027 周期的
   一切）。

若某个 skill 把第 2/3 类材料当作第 1 类陈述，应视为 bug，并对照官方在线页面修正。

## 里约现场与投稿后

- 至少一位作者须注册并到场报告；尽早确认当前注册类别与报告要求，并及早办理里约（巴西）签证与
  行程——国际差旅是最常见的落地失败点。
- 报告要**播放媒体**：让听众*看到/听到*论文所利用的模态接缝，而不只是被描述。
- 被拒时用评审意见改投：偏检索的投 ICMR，偏系统的投 MMSys，区域性或早期结果投 ACM Multimedia
  Asia 或 workshop，成熟版本投 ACM TOMM 期刊或次年 ACM MM。

## 维护说明

- 本文所有日期、页数与 track 规则均为 **2026 周期快照**。ACM MM 政策每届由轮换 chairs 改写——
  在涉及 deadline 的建议前，请重开 `2026.acmmm.org`（及次年官网）核对当前周期。
- thematic-area 列表、活跃 track 集合、双盲例外会逐年变化；请核对当前 Topics of Interest 与各
  track 自己的 call。
- Reproducibility badging 遵循 ACM 不断演化的 artifact-review 术语；每周期核对当前
  Reproducibility-track call 与 ACM 的 badge 定义。
- 新增 exemplar 时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——著名多媒体论文常属于 ICMR、MMSys、CVPR 或 TOMM，而非 ACM MM 主会。

## License

MIT — 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
