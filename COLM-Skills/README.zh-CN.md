# COLM Skills

面向 **COLM（Conference on Language Modeling，语言建模会议）** 投稿的 12 个 agent
skills。COLM 是一个年轻的会议（2023 年 10 月公布，2024 年首届），专为"语言模型本身
就是研究对象"的工作而设：LM 的训练、数据、评测、推理、可解释性与安全。本包覆盖完整
周期——判断项目是否是 COLM 形状、构建抗污染且版本锁定的实验证据、打赢 OpenReview
rebuttal、把 7 月的录用变成 8 月的 camera-ready 和 10 月的现场报告。

官方依据核验日期：**2026-07-08**。已核验 COLM 2026 官网首页、key dates 页、Call for
Papers、submission instructions、author guide、FAQ、COLM 2026 OpenReview group、
2024/2025 两届 accepted papers 列表，以及 Outstanding Paper Awards 的独立机构报道。
核验环境无法直接抓取 `colmweb.org`（网关返回 403），因此官方页面内容通过搜索引擎对
准确 URL 的渲染读取，并与 OpenReview 和机构页面交叉核对；完整来源链与所有仍标注
**待核实** 的条目见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 2026 周期当前所处阶段（截至 2026-07-08）

本包构建于 **COLM 2026 放榜日当天**。3 月的两个截止（摘要 3 月 26 日、全文 3 月 31
日）与 rebuttal 窗口（5 月 22 日 - 6 月 8 日）均已结束；**录用通知 7 月 8 日发出**；
camera-ready 截止 **8 月 7 日**；会议 **10 月 6-9 日在旧金山 Hilton Union Square**
举行（主会 10 月 6-8 日，workshop 日 10 月 9 日）。据此：

- **今天收到录用？** 直接进入
  [`colm-camera-ready`](skills/colm-camera-ready/SKILL.md)——只有一个月，artifact
  公开发布应与终稿同批完成。
- **今天被拒？** 走 [`colm-review-process`](skills/colm-review-process/SKILL.md)
  的被拒分支：ICLR / NeurIPS / COLM 2027 的转投日历。
- **规划新工作？** 你面向的是 **COLM 2027**——日期未公布（待核实；合理工作假设是
  3 月下旬），规划类 skills 以已核验的 2026 日历为模板教学周期形状。

## COLM 与相邻会议的差别

- **LM 是研究对象，不是工具。** COLM 的立会理由是：语言模型技术带来的研究问题在
  ACL/EMNLP（以任务和语言为中心）、ICLR/NeurIPS/ICML（以通用性为中心）和系统类会议
  都放不顺。路由判据见 [`colm-topic-selection`](skills/colm-topic-selection/SKILL.md)。
- **奖项谱系偏爱"测量"。** 2024-2025 两届共 8 篇 Outstanding Paper 中 5 篇是分析、
  测量或评测批判类工作——这是关于审稿人价值观的强先验
  （[`resources/exemplars/library.md`](resources/exemplars/library.md)）。
- **LM 特有的严谨性就是审稿标准：** 污染（contamination）处理、预算对齐的
  baseline、checkpoint 哈希与 API 版本串+查询日期、解码参数披露、算力披露——
  [`colm-experiments`](skills/colm-experiments/SKILL.md) 与
  [`colm-reproducibility`](skills/colm-reproducibility/SKILL.md) 的核心。
- **紧凑的现代机制：** 全程 OpenReview，论文直接在 OpenReview 上公开出版（无 PMLR
  卷、不进 ACL Anthology）；正文**严格 9 页**、引用页数不限；双盲规则明确禁止致谢
  与任何暴露身份的链接；全体作者必须确认 Code of Ethics；LLM 使用政策（沿用 ICLR
  2026 版并放宽轻量辅助）；互惠审稿要求——4 篇及以上投稿的作者自动进入审稿人池。
- **年轻会议的波动性。** 三届办会（2024 费城、2025 蒙特利尔、2026 旧金山），规范与
  政策逐年变动——因此每个 skill 都区分"已核验的 2026 事实"与"待核实条目"。

## Skills 一览

| Skill | 作用 |
| --- | --- |
| [`colm-topic-selection`](skills/colm-topic-selection/SKILL.md) | 用"研究对象测试"在 COLM、ACL/EMNLP、ICLR、NeurIPS/ICML、系统会议与 workshop 之间路由，并权衡投年轻会议的利弊。 |
| [`colm-workflow`](skills/colm-workflow/SKILL.md) | 从 3 月截止倒排一年一次的战役：算力预订、claims 台账、互惠审稿分配表、决策树备忘录、多会议轮转。 |
| [`colm-writing-style`](skills/colm-writing-style/SKILL.md) | 用"关于 LM 的发现"开篇而非榜单差值；每条结论限定在被测模型与规模；正文 9 页自洽。 |
| [`colm-related-work`](skills/colm-related-work/SKILL.md) | 覆盖五条文献带，诚实处理 arXiv 为主与并行工作，核验每条参考文献真实存在，自引保持双盲。 |
| [`colm-experiments`](skills/colm-experiments/SKILL.md) | 顶住四类 LM 特有攻击：数据污染、baseline 不公平、版本漂移、解码敏感性；预算对齐、按真实噪声源报告不确定性。 |
| [`colm-reproducibility`](skills/colm-reproducibility/SKILL.md) | 分层可复现（精确/预算内/漂移中）、四个哈希锁定、缓存 API 原始响应、披露算力、写出逐项的可用性声明。 |
| [`colm-supplementary`](skills/colm-supplementary/SKILL.md) | 在严格 9 页正文与"审计线索"附录之间分配内容：逐字 prompt、调参台账、污染分析、匿名化材料包。 |
| [`colm-artifact-evaluation`](skills/colm-artifact-evaluation/SKILL.md) | 打包权重、数据、prompt 与缓存输出：许可证与 ToS 关卡、一条命令复现一张表、从缓存核验。 |
| [`colm-submission`](skills/colm-submission/SKILL.md) | 上传前终审：9 页上限、LM 特有的身份泄漏扫描、Ethics 确认、LLM 使用披露、互惠审稿人指派。 |
| [`colm-review-process`](skills/colm-review-process/SKILL.md) | 建模 3 月到 7 月的流水线、互惠审稿人池、年轻会议的评分方差、审稿人 LLM 使用规则与被拒分支。 |
| [`colm-author-response`](skills/colm-author-response/SKILL.md) | 规划约 18 天的 rebuttal：用缓存实验回应四类标准质疑、公开让步、写给 AC 看。 |
| [`colm-camera-ready`](skills/colm-camera-ready/SKILL.md) | 把录用变成 OpenReview 上的公开定稿：双向去匿名、兑现 rebuttal 承诺、同步发布 artifact、安排旧金山行程。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 12 条带日期的官方来源、访问方式说明、已核验 2026 事实、仅有二手报道的条目与明确的待核实清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | COLM 2024-2025 全部 8 篇 Outstanding Paper 的定位笔记、自检问题与"防止张冠李戴"守则。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的"刷榜式"首页如何重建为 COLM 形状：现象先行、污染上首页、模型锁定、结论限定。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口与上传前的五道作者侧核验。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 ML 会议可复现工具包，并列出通用工具查不出的五项 LM 特有检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./COLM-Skills
claude plugin install colm-skills
```

也可直接使用文件：每个 `skills/colm-*/SKILL.md` 都是独立说明文件，frontmatter 中的
`description` 决定触发时机。典型用法：

- "这篇该投 COLM 还是 EMNLP？" → `colm-topic-selection`
- "训练开跑前帮我红队一遍评测设计" → `colm-experiments`
- "5 月 22 日出审稿意见，先把 rebuttal 计划搭好" → `colm-author-response`
- "中了！8 月 7 日前要做完哪些事？" → `colm-camera-ready`

## 建议路线

1. **动笔之前**——先跑 `colm-topic-selection` 的"研究对象测试"；不通过就换会，这个
   包等于帮你省了一年。再对照
   [`resources/exemplars/library.md`](resources/exemplars/library.md) 的获奖谱系，
   看"被 COLM celebrated 的工作"长什么样。
2. **实验期间**——把 `colm-experiments` 的四类攻击清单和 `colm-reproducibility`
   的锁定纪律（哈希、版本串、查询日期、响应缓存）从第一天就装进代码库；事后补装的
   成本是十倍。
3. **写作期间**——`colm-writing-style` 管正文，`colm-supplementary` 管 9 页正文与
   附录的分工，`colm-related-work` 管定位；对照 worked example 的 before/after。
4. **截止周**——`colm-submission` 从头到尾过一遍，机械扫描跑在合成后的 PDF 上；
   合作者侧的政策项（Ethics 确认、LLM 披露、互惠审稿）提前两天完成。
5. **投稿之后**——`colm-review-process` 校准预期；5 月 22 日意见发布当天启动
   `colm-author-response` 的 18 天计划；7 月 8 日放榜后按分支进入
   `colm-camera-ready` 或转投规划。

## 2026 锚点事实（单周期快照，不是永久规则）

- COLM 2026 是**第三届**：旧金山 Hilton Union Square，**2026 年 10 月 6-9 日**
  （主会 10 月 6-8 日，workshop 10 月 9 日）。
- 时间线：摘要 **3 月 26 日** · 全文 **3 月 31 日** · 审稿意见 **5 月 22 日** ·
  rebuttal **5 月 22 日 - 6 月 8 日** · 放榜 **7 月 8 日** · camera-ready
  **8 月 7 日**。
- 格式：正文**严格 9 页**，引用页数不限；可选致谢 ≤ 1 页不计入页数（仅限终稿——
  投稿版双盲，禁止致谢与暴露身份的链接）。
- 平台：OpenReview（`colmweb.org/COLM/2026/Conference`），2026 年 2 月开放；论文在
  OpenReview 公开出版。
- 政策：全体作者确认 Code of Ethics；按 2026 政策披露 LLM 使用；互惠审稿含
  per-submission 与 per-reviewer 两层要求，4 篇及以上投稿自动入池。
- 历届：2024 费城（UPenn）· 2025 蒙特利尔 · 2026 旧金山；前两届各评出 4 篇
  Outstanding Paper。

## 事实纪律

全包贯穿三类陈述，刻意保持可区分：

1. **已核验的 2026 事实**——有日期、可追溯到来源表编号（9 页上限、3/26-3/31-5/22-
   6/8-7/8-8/7 日期链、LLM 政策）。
2. **仅有报道的事实**——只见于二手渲染并如实标注（2026 委员会名单、2025 会场建筑）。
3. **待核实条目**——终稿是否加页、注册与到场要求、录用率、是否有 artifact track、
   2027 全部日期——一律写成"待解决的问题"，绝不写成事实。

若发现任何 skill 把第 2、3 类当第 1 类陈述，视为 bug，对照官方页面修正。

## 维护说明

- COLM 年轻到**以上一切都逐年可变**——三届之内两次跨国换城市、政策每届微调。给出
  任何与截止相关的建议前，先重开 `colmweb.org` 与当届 OpenReview group。
- 构建时 dblp 无法直接访问；补充文献指引时请核对 `dblp.org/db/conf/colm/`。
- 新增范文请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——arXiv 页面上的 "Published at COLM" 横幅只是声明，不是证明。

## 许可证

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
