# ACL Skills

面向 ACL（Annual Meeting of the Association for Computational Linguistics，
计算语言学协会年会）投稿的 12 个 agent skills。ACL 是 \*ACL 系列的旗舰会议，
覆盖计算语言学与自然语言处理全领域。

本包围绕 ACL 区别于传统"单一截稿日"会议的核心机制构建：**ACL Rolling Review
（ARR）**。论文先提交到 OpenReview 上按月份命名的 ARR cycle，在 cycle 内完成
审稿与 meta-review；随后作者再把带完整审稿包的论文 **commit** 给目标会议，由
会议的 Senior Area Chairs 与 Program Chairs 做出最终决定——主会、Findings of
ACL 或拒稿。因此本包中所有与时间相关的 skill（submission、author response、
review process、workflow）都按 cycle 与 commitment 窗口推理，而不是倒数一个
CFP 截止日。

官方依据核验日期：2026-07-08。已核验 ACL 2026 官方 calls（第 64 届年会，
San Diego，2026 年 7 月 2-7 日）、aclrollingreview.org 的 CFP、cycle 日历、
作者指南与 Responsible NLP checklist（域名被网关拦截时改读其公开 GitHub 源码
仓库）、OpenReview 的 ARR cycle groups、\*ACL camera-ready FAQ，以及 ACL
Anthology 政策页。完整来源清单、访问方式说明与仍标注 待核实 的条目见
`resources/official-source-map.md`。

## ACL 投稿的特殊之处

- **按 cycle 投稿，不是按截止日。** 2026 年 ARR 以 10 周为一个 cycle（提交日
  分别为 1 月 5 日、3 月 16 日、5 月 25 日、8 月 3 日、10 月 12 日）；每个会议
  自行公布接受哪些 cycle。ACL 2026 接受 2025 年 10 月与 2026 年 1 月两个
  cycle，commitment 截止 2026 年 3 月 14 日。
- **修改重投是制度设计的一部分。** 修改稿在后续 cycle 重投时必须链接前一次
  提交，并附修改摘要与逐条回应；隐瞒重投历史会被直接 desk reject。
- **Limitations 章节是硬性要求**，与不限页数的参考文献一样位于正文页数
  （长文 8 页 / 短文 4 页）之外；缺失即 desk reject。
- **Responsible NLP checklist 参与审稿。** 填写不实可导致 desk reject；
  诚实披露局限则受到明确保护，审稿人不得因此扣分。
- **2024 年 1 月 12 日起取消匿名期。** 可随时挂 preprint 但必须如实申报；
  选择不挂 preprint 可获奖项资格与临界录用优先权。投稿本身仍须完全匿名。
- **两级录用。** Findings of ACL 是正式的、进入 Anthology 的存档录用结果，
  在 commitment 阶段由会议决定。
- **永久开放获取。** 录用论文进入 ACL Anthology（2016 年后材料为 CC BY 4.0），
  不收作者费用；ACL 的成本模型是会议注册费。

## Skills

- `acl-submission`：审计 ARR 提交——页数预算、必需的 Limitations、Responsible
  NLP checklist、匿名化、preprint 与重投申报、一稿多投规则、desk-reject 触发点。
- `acl-author-response`：经营 cycle 内的 response 窗口——审稿分诊、影响
  meta-review、应对 NLP 审稿人常见质疑、举报失职审稿、决定当期回复还是
  下一 cycle 修改。
- `acl-camera-ready`：用好多出来的一页正文、去匿名化、披露 AI 辅助、落实
  meta-review 要求、交付干净的 Anthology 元数据（CC BY 4.0）。
- `acl-artifact-evaluation`：把代码、数据、prompt、模型输出与标注材料打包成
  匿名 .tgz/.zip 补充材料，对齐 checklist B 节，并规划录用后的公开发布阶梯。
- `acl-reproducibility`：把 Responsible NLP checklist 当作论断审计来跑——
  超参数、算力、prompt 与解码披露、数据污染立场、方差报告、checklist 与
  论文的一致性。
- `acl-supplementary`：切分正文、Limitations、附录与压缩包，确保关键证据
  不藏在审稿人没有义务阅读的位置。
- `acl-review-process`：建模 ARR 流水线——审稿人、AC meta-review、
  commitment、会议端决定、伦理升级路径，以及何时把审稿包转投兄弟会议。
- `acl-writing-style`：按任务优先的框架修改——首页给出真实语例、LLM 时代的
  论断限定、量化错误分析、匿名兼容的行文，以及 8/4 页压缩。
- `acl-related-work`：在快速演化的 NLP 文献中定位——优先引 Anthology 版本、
  正确署 Findings、处理同期 preprint、扫描最近几轮 \*ACL 的新基线。
- `acl-experiments`：设计证据——调优过的 LLM 基线、与论断匹配的多语言广度、
  显著性与方差底线、人评一致性、污染控制、消融与错误分类。
- `acl-workflow`：运转 cycle-and-commit 日历——选 cycle、倒排计划、重投循环、
  commitment 决策、camera-ready 直至 Anthology 发表。
- `acl-topic-selection`：在 ACL、EMNLP、NAACL/EACL/AACL、TACL、Computational
  Linguistics、COLM 与 ML 会议之间路由；选长文或短文；评估 theme track 与
  Findings 情形。

## Resources

| 路径 | 内容 |
| --- | --- |
| `resources/official-source-map.md` | 已核验来源（URL + 访问日期）、网关访问方式说明与 待核实 条目 |
| `resources/external_tools.md` | ARR / OpenReview / Anthology 官方入口与分阶段作者自查清单 |
| `resources/exemplars/library.md` | 按贡献类型组织的 6 篇已核验 ACL 主会范文，附兄弟会议误归属防护 |
| `resources/worked-examples/01-introduction.md` | 虚构论文的摘要与引言 before/after 改写，示范 ACL 行文 |
| `resources/code/README.md` | 指向仓库级共享 ML 会议可复现性工具包 |

## 使用建议

新项目的典型顺序：`acl-topic-selection` → `acl-experiments`（设计阶段）→
`acl-writing-style` + worked example → `acl-related-work` →
`acl-reproducibility` + `acl-artifact-evaluation` → `acl-supplementary` →
截稿前跑 `acl-submission` → response 窗口用 `acl-author-response` →
commitment 决策阶段用 `acl-review-process` + `acl-workflow` → 录用后
`acl-camera-ready`。

可以从本目录作为 Claude Code plugin 安装（manifest 位于 `.claude-plugin/`），
也可以按需单独加载 `skills/*/SKILL.md`。

## 已核验事实速览（访问日期 2026-07-08）

| 事实 | 内容 | 来源 |
| --- | --- | --- |
| 锚定届次 | ACL 2026，第 64 届年会 | 2026.aclweb.org |
| 时间 / 地点 | 2026 年 7 月 2-7 日，San Diego（hybrid） | 2026.aclweb.org |
| 审稿机制 | ARR（OpenReview）审稿，会议端做最终决定 | ACL 2026 CFP + aclrollingreview.org |
| ACL 2026 可用 cycle | ARR 2025 年 10 月、2026 年 1 月 | ACL 2026 CFP |
| 1 月 cycle 截稿 | 2026 年 1 月 5 日（AoE） | aclrollingreview.org/dates |
| Commitment / 通知 / camera-ready | 2026 年 3 月 14 日 / 4 月 4 日 / 4 月 19 日 | ACL 2026 CFP |
| 页数 | 长文 8 页、短文 4 页；camera-ready +1 页；参考文献不限 | ARR CFP + \*ACL camera-ready FAQ |
| 硬性章节 | Limitations（缺失即 desk reject） | ARR CFP |
| Checklist | Responsible NLP checklist（A-E 节） | aclrollingreview.org/responsibleNLPresearch |
| 匿名规则 | 投稿匿名；2024-01-12 起无匿名期 | ARR anonymity update |
| 录用层级 | 主会；Findings of ACL（存档） | Anthology venues/findings |
| 论文集 | ACL Anthology，开放获取，CC BY 4.0（2016 后） | aclanthology.org/faq/copyright |
| 2026 主题 | Explainability（可解释性），设 Thematic Paper Award | ACL 2026 CFP |

## 常见问题

**这个包能替代官方 call 吗？** 不能。它固化的是经核验的 2026 年状态与相对
稳定的机制；一切涉及截止时间的事实都必须重开 ARR 与会议官网核对，冲突时
以官方为准。

**为什么所有建议都按 cycle 表述？** 因为 ACL 的录用是两段式事件（ARR 审稿
+ 会议 commitment），任何"ACL 截稿日"式的说法在结构上就是错的。本包按
venue 自己的方式把两段分开处理。

**这个包适用于 EMNLP / NAACL 吗？** ARR 机制在 \*ACL 系列内共享，流水线
推理大多可迁移，但本包的校准、日期与届次政策都是 ACL 的。兄弟会议请使用
对应的包（若存在）。

**标注 待核实 的条目怎么处理？** 表示构建时网关无法直接打开官方页面加以
钉死。在你亲自打开官方页面之前把它当作未知；source map 精确列出了这些
条目。

## 维护说明

- ARR 的 cycle 结构已多次变动（每月 → 双月 → 10 周制），不要把 2026 年日历
  外推到未来；先重开 aclrollingreview.org/dates 与目标届会议官网。
- 本包中的 ACL 2026 事实（日期、theme、commitment 窗口）来自一场已于
  2026-07-07 闭幕的会议，是历史锚点而非长期规则。
- checklist 措辞、preprint 激励、页数政策、审稿表单与 Findings 的报告形式
  都按届变化；与本包冲突时一律以官方页面为准。
- 新增范文时务必确认 Anthology 页面的 venue 行写的是 ACL 年会主会论文集——
  Anthology 同时收录所有兄弟会议。

## 与本仓库其他包的关系

- 广度层：`Computer-Science-Conference-Skills` 中的 ACL 条目提供跨会议的
  选会与路由基线；本包是它的深度扩展，二者结论冲突时以本包更新的
  2026 核验事实为准（但仍以官方页面为最终权威）。
- 共享工具：可复现性冒烟检查复用仓库级 `shared-resources/
  ml-conference-methods` 工具包，入口见 `resources/code/README.md`。
- 兄弟会议：EMNLP、NAACL、EACL 等共享 ARR 机制但各有届次政策；不要把
  本包的日期与政策直接套用到兄弟会议上。

## 许可

MIT（见 `LICENSE`）。本包为社区文档，与 ACL 官方无隶属或背书关系。
