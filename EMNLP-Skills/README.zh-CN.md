# EMNLP Skills（中文说明）

面向 **EMNLP（Conference on Empirical Methods in Natural Language Processing）** 投稿的
12 个 agent skills。EMNLP 是 ACL 系旗舰会议中"实证身份"最鲜明的一个：数据集、benchmark、
评测设计、error analysis、以及对语言系统真实行为的可测量论断，构成了这个会议的审稿文化。
本包覆盖完整投稿弧线：判断项目是否"EMNLP 形状"、构建经得起污染审查与显著性检验的证据、
走通 ACL Rolling Review、打好 commitment 这一步、并把录用结果（Main 或 Findings）转化为
正确的 ACL Anthology 记录。

官方依据核验日期：**2026-07-08**。已核验 EMNLP 2026 官网与主会 CFP、ACL Rolling Review
的 CFP / dates / authors 页面、Responsible NLP Research checklist、ARR May 2026 与
Industry Track 的 OpenReview group、以及 ACL Anthology 的 EMNLP 各卷。核验环境无法直接
抓取 `2026.emnlp.org` 与 `aclrollingreview.org`，官方页面内容通过精确 URL 的搜索引擎
渲染读取，并与 OpenReview、Anthology 交叉验证；完整来源链与全部 待核实 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## EMNLP 与兄弟会议的关键差异

以下机制均按 2026 周期核验，是本包大部分建议的出发点，也是从非 ARR 会议转来的作者最容易
踩的坑：

- **EMNLP 本身没有论文截稿日。** 论文投入 ARR May 2026 周期（截稿 2026-05-25），在 ARR
  完成评审，再于 **2026-08-02 前 commit 给 EMNLP**。ARR 负责评审，会议只负责决定。
- **一个周期喂两个会。** May 2026 周期同时服务 EMNLP 2026 与 AACL-IJCNLP 2026，投稿时
  就要声明意向会议。
- **Checklist 带牙齿。** Responsible NLP checklist 随投稿提交；自 2024 年 12 月起，
  填写错误、不完整或误导会被 desk reject；EMNLP 2025 还把完成的 checklist 作为论文附录
  发表。
- **两个录用出口。** Committed 论文进主会或 Findings of EMNLP——后者是 Anthology 独立
  卷收录的正式出版物，但历史上不保证报告或 poster 名额。
- **强制 Limitations 章节**，不计入 long 8 页 / short 4 页的正文上限，审稿人会拿它对照
  自己发现的弱点。
- **无匿名期，但仍双盲。** 预印本随时可发；提交的 PDF 必须匿名化。
- **诚信是成文政策。** 2026 CFP 点名 thinly sliced 投稿、幻觉引用、全 AI 生成论文
  （允许 AI 写作辅助）。
- **评测文化即会议本身。** 预算受控比较、NLP 统计功效等方法论批判正是在 EMNLP 发表的，
  其审稿人会用这些标准审你。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`emnlp-topic-selection`](skills/emnlp-topic-selection/SKILL.md) | 做实证身份测试，把论文对准 EMNLP 欢迎的类型（含负结果与复现），在 ACL 系兄弟会、CoNLL、LREC-COLING、TACL、ML 会议及 industry/demo 通道之间路由。 |
| [`emnlp-workflow`](skills/emnlp-workflow/SKILL.md) | 以 ARR 为锚排全年日历：标注与实验倒排到 5 月 25 日，给 7 月 response 窗口配人，提前起草 72 小时内要做的 commit-vs-revise 决定。 |
| [`emnlp-writing-style`](skills/emnlp-writing-style/SKILL.md) | 把论断收敛到实测语言与领域，例句必须挂着计数的错误类别，写有内容的 Limitations，校准 hedging。 |
| [`emnlp-related-work`](skills/emnlp-related-work/SKILL.md) | 覆盖五条谱系轴（任务、数据集祖先、方法、评测批判、邻域），正确引用 Findings / workshop / TACL，通过幻觉引用检查。 |
| [`emnlp-experiments`](skills/emnlp-experiments/SKILL.md) | 对着审稿人的五个探针设计实验：baseline 公平、覆盖-论断匹配、污染、方差、机制，外加 prompt 敏感性网格与有设计的 error analysis。 |
| [`emnlp-reproducibility`](skills/emnlp-reproducibility/SKILL.md) | 把 checklist 当合同来答，钉死模型版本与 API 查询日期，记录 decoding 与 prompt，诚实声明 release 等级。 |
| [`emnlp-supplementary`](skills/emnlp-supplementary/SKILL.md) | 按评审契约而非方便，把材料切分到四个层面：正文页、不计页的 Limitations、附录、可选上传。 |
| [`emnlp-artifact-evaluation`](skills/emnlp-artifact-evaluation/SKILL.md) | 按审稿人的真实检查顺序打包数据、prompt、评分代码与输出转储，配 data statement 与一次性 anonymize 发布方案。 |
| [`emnlp-submission`](skills/emnlp-submission/SKILL.md) | 上传前终审：模板与页限、匿名化扫描、checklist 一致性、引用可解析性、意向会议声明、互惠审稿义务。 |
| [`emnlp-review-process`](skills/emnlp-review-process/SKILL.md) | 建模两段式流水线——ARR 打分（soundness / excitement / overall）、meta-review、commitment、SAC 决定进 Main 或 Findings——找到作者真正的杠杆点。 |
| [`emnlp-author-response`](skills/emnlp-author-response/SKILL.md) | 按分数轴分诊审稿意见，只补窗口内可补的证据，面向 meta-review 与 commitment 后的档案来写。 |
| [`emnlp-camera-ready`](skills/emnlp-camera-ready/SKILL.md) | 执行三方合并（评审版 PDF + 承诺过的修改 + 去匿名化），守住 Anthology 元数据，公开恢复 artifact，处理 Findings 与布达佩斯行程。 |

## Resources

| 路径 | 放着什么 |
| :-- | :-- |
| `resources/official-source-map.md` | 11 个官方来源（URL + 核验日期）、已核验的 2026 周期事实、访问方式说明、明确的 待核实 清单。 |
| `resources/external_tools.md` | 会议侧与 ARR 侧的官方入口，加上传前要跑的五个作者侧核验环节。 |
| `resources/exemplars/library.md` | 6 篇经 Anthology 核验的真实 EMNLP 论文（从 GloVe 到统计功效方法论），按 topic × method 组织，附兄弟会议误归属防护清单。 |
| `resources/worked-examples/01-introduction.md` | 一个虚构的多语摘要论文首页，从"架构先行"重建为"现象先行"，before → after。 |
| `resources/code/README.md` | 共享 ML 会议可复现工具包的适配器，外加通用工具做不了的 NLP 专属检查（prompt、模型快照、decoding、标注材料）。 |

## 安装方式

本目录是一个带自有 marketplace 清单的完整 Claude Code 插件，两条命令即可装入：

```bash
claude plugin marketplace add ./EMNLP-Skills   # 在仓库克隆内执行
claude plugin install emnlp-skills
```

不装插件也能用：`skills/emnlp-*/SKILL.md` 每个都是自足的指令文件，agent 读 frontmatter
里的 `description` 即可判断触发时机。常见触发场景举例：

- "这个 benchmark 论文该投 EMNLP 还是 LREC-COLING？" → `emnlp-topic-selection`
- "帮我在 ARR 截稿前审一遍稿子" → `emnlp-submission`
- "评审意见出了——commit 还是转投下个周期？" → `emnlp-review-process` + `emnlp-author-response`
- "把语料和 prompt 打包发布" → `emnlp-artifact-evaluation`

## 文件布局

```text
EMNLP-Skills/
├── .claude-plugin/                    ← 插件与 marketplace 清单（声明全部 12 个 skills）
├── README.md / README.zh-CN.md       ← 英文 / 中文说明
├── LICENSE（MIT）· assets/cover.svg  ← 许可证与封面
├── skills/emnlp-<topic>/SKILL.md     ← 12 个技能目录，每目录一个 SKILL.md
└── resources/                         ← 资源层
    ├── README.md（导览）· official-source-map.md（来源与待核实清单）
    ├── external_tools.md（官方入口）· exemplars/library.md（已核验范文）
    ├── worked-examples/01-introduction.md（首页改写示范）
    └── code/README.md（可复现工具包适配器）
```

## 建议路线

1. **动笔前** — 先跑 `emnlp-topic-selection`；实证身份测试不通过的项目，再怎么打磨也
   不是 EMNLP 论文。对照 exemplars library 看已录用论文的门槛长什么样。
2. **做实验时** — 把 `emnlp-experiments` 和 `emnlp-reproducibility` 放在代码库旁边；
   污染审查和多 seed 方差在早期便宜，在截稿周不可能。
3. **写作时** — `emnlp-writing-style` 管论断收敛与 Limitations，`emnlp-supplementary`
   管四层切分，`emnlp-related-work` 管谱系覆盖与引用可解析性。
4. **截稿周** — 从头到尾过一遍 `emnlp-submission`，包括机械化的匿名扫描与 checklist
   一致性检查。
5. **投稿后** — 用 `emnlp-review-process` 校准预期，7 月窗口用 `emnlp-author-response`，
   之后按 meta-review 走 `emnlp-camera-ready` 或转投下一周期。

## 2026 锚点事实（历史快照，不是永久规则）

- EMNLP 2026：**匈牙利布达佩斯，2026 年 10 月 24-29 日**，hybrid 形式。
- 流水线：ARR May 周期截稿 **5 月 25 日** · 作者注册表 5 月 27 日 · 审稿人交稿 7 月
  6 日 · 作者讨论 **7 月 7-13 日** · meta-review 发布 7 月 30 日 · **commitment 8 月
  2 日** · 录用通知 8 月 20 日 · camera-ready 9 月 20 日。
- 格式：只用 ACL 模板 · long ≤ 8 页 / short ≤ 4 页正文 · 参考文献不限 · 强制且不计页
  的 Limitations 章节。
- 录用层级：主会 + Findings of EMNLP（2025 年锚点：主会 1,810 篇、Findings 1,406 篇、
  industry 194 篇、demo 78 篇）。
- Industry Track：绕开 ARR 直投 OpenReview，截稿 2026-06-16 AoE。
- 出版：ACL Anthology，开放获取，作者零费用。

## 事实纪律

本包把三类陈述严格区分：

1. **已核验的 2026 周期事实** — 日期与页限均可追溯到 source map 中编号来源（如 5 月
   25 日截稿、8 月 2 日 commitment）。
2. **转述事实** — 来自页面渲染或组织者本人的公开发帖，并明确标注（如 2026 各 chair
   人选）。
3. **核验时不可确认项** — 标注 待核实，以问题而非事实的口吻表述（如 camera-ready 加页
   额度、Findings 报告形式、demo track 日期）。

任何把第 2、3 类当第 1 类陈述的文字都算 bug，请对照官方页面修正。

## 维护说明

- 上述每个日期都是**单一周期的快照**；ARR 每年重排周期与会议对应关系，会议侧的 track
  与行程也逐届重设。
- ARR 的评审政策（打分维度、checklist 执法、表单字段）会在年中更改并在
  `aclrollingreview.org` 公告——复述任何评审规则前先复核。
- 各 chair 逐届轮换；不要不加复核地沿用本包中的人名。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程——
  一个 Anthology 链接本身证明不了 venue。

## 许可证

本包以 MIT 许可发布（全文见 [`LICENSE`](LICENSE)）；英文完整说明请读 [`README.md`](README.md)。
