# WACV Skills

面向 **WACV —— IEEE/CVF Winter Conference on Applications of Computer Vision（冬季计算机视觉
应用会议）** 论文的 12 个 agent skills。WACV 是 Computer Vision Foundation 四会日历中
以应用为先的冬季会议（夏季 CVPR、秋季 ICCV/ECCV 交替、冬季 WACV）。本包覆盖一次 WACV 投稿的
完整流程，且贴合它真实的运行方式：选择 **Applications 或 Algorithms track**、决定进入 **两轮投稿
中的哪一轮**、构建面向真实约束的证据、通过 OpenReview 的双盲检查、撰写可选的 **Round 1 一页
rebuttal**、把一篇 **Revise and Resubmit** 修改稿带入 **无 rebuttal 的 Round 2**，并最终发表在
CVF open access 与 IEEE Xplore。

官方依据交叉核验日期：**2026-07-09**。已核验 WACV 2027 Call for Papers、Author Guidelines、
Dates 页面；WACV 2027 Round 1 / Round 2 的 OpenReview groups；WACV 2026 Author/Reviewer
Guides 与会议页面；IEEE Computer Society 的 WACV 征稿；CVF open access 与 IEEE Xplore 记录；
dblp；以及官方 `@wacv_official` 账号发布的分轮统计。在核验环境中，`wacv.thecvf.com` 与
`openaccess.thecvf.com` 的直接抓取被拦截（HTTP 403），因此官方页面通过对精确 URL 的搜索渲染
读取，并与 OpenReview、dblp、IEEE Xplore、历年 WACV 站点存档交叉核对。完整链路（含所有仍标注
待核实 的条目）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

**周期状态：** WACV 2026（Tucson，2026 年 3 月 6-10 日）是最近一次完成的周期，提供了已核验的
格式锚点。**WACV 2027 周期正在进行中**：截至 2026-07-09，Round 1 论文截止（据报 2026 年 6 月
26 日）已过，我们正处在 Round 1 审稿窗口内，Round 2 截止（据报 2026 年 8 月 28 日）临近。
WACV 2027 确切会议日期与主办城市仍为 待核实。

## WACV 与它的 CVF 姐妹会有何不同

驱动本包每个 skill、且 CVPR / ICCV / ECCV **都没有** 的机制：

- **两轮、类期刊式审稿。** Round 1 论文至少获得三份评审，area chair 给出 **Accept**、
  **Revise and Resubmit** 或 **Reject** 之一。修改稿与新投稿在 Round 2 一起评审，Round 2 只给出
  **Accept** 或 **Reject**。没有其他 CVF 会议提供正式的修改路径。
- **修改环节才是主战场。** 在 WACV 2025 的 Round 1 中，1381 篇投稿里约 12% 直接录用、约 37%
  被拒、**约 51% 被邀请修改** —— 多数论文在 Revise-and-Resubmit 环节定生死，而非首轮。
- **rebuttal 只存在于 Round 1。** 作者可在 Round 1 评审后提交可选的一页 rebuttal；**Round 2
  没有 rebuttal**，因此仓促的修改事后无法再辩解。
- **两个 track、两套评审标准。** **Applications track**（考核系统级创新、领域新颖性、真实约束下的
  对比评估）与 **Algorithms track**（考核算法新颖性与匹配基线的评估）。作者选择一个主 track，
  这一选择会重塑首页写法。
- **应用为先的身份。** WACV 存在的意义是评审在真实约束下可用的计算机视觉 —— 低功耗推理、数据
  稀缺、真实场景鲁棒性 —— 而非为方法而方法。
- **熟悉的 CVF 管线。** 正文 8 页含图表（多余页仅放参考文献），OpenReview 双盲投稿且需有效
  profile 否则 desk reject，匿名补充材料，并双重发表于 CVF open access（免费、带水印）与
  IEEE Xplore（version of record）。无版面费；chairs 每届轮换，故无常任主编。

## Skills

| Skill | 作用 |
| --- | --- |
| [`wacv-topic-selection`](skills/wacv-topic-selection/SKILL.md) | 判断项目是否为“真实约束下的应用”贡献，在 WACV 与 CVPR/ICCV/ECCV/3DV/期刊间路由，并选择 Applications vs Algorithms track。 |
| [`wacv-workflow`](skills/wacv-workflow/SKILL.md) | 运行分叉的两轮日历：轮次/track 选择、Round 1 投稿与 rebuttal、Accept/Revise-and-Resubmit/Reject 分叉、Round 2 修改、camera-ready 与冬季会议。 |
| [`wacv-writing-style`](skills/wacv-writing-style/SKILL.md) | 针对所选 track 与两轮审稿人写首页，使显而易见的修改问题在被问之前就已回答。 |
| [`wacv-related-work`](skills/wacv-related-work/SKILL.md) | 覆盖 vision、姐妹会、并行工作与应用领域文献；自引保持双盲；核实所引“WACV 论文”确为 WACV。 |
| [`wacv-experiments`](skills/wacv-experiments/SKILL.md) | 构建切合 track 的证据 —— 面向约束的系统结果或匹配基线的新颖性 —— 含对比评估与诚实的不确定性。 |
| [`wacv-reproducibility`](skills/wacv-reproducibility/SKILL.md) | 维护 recipe ledger，复现的是部署约束而非仅精度，并在修改环节保持论文与 artifact 一致。 |
| [`wacv-supplementary`](skills/wacv-supplementary/SKILL.md) | 在 8 页正文与匿名补充材料间划分内容；把视频作为证据打包且不破坏双盲。 |
| [`wacv-artifact-evaluation`](skills/wacv-artifact-evaluation/SKILL.md) | 构建密封的匿名评审 artifact 与公开发布版，含约束复现与数据集许可。 |
| [`wacv-submission`](skills/wacv-submission/SKILL.md) | OpenReview 终审：轮次与 track 字段、profile、页数、匿名清扫、一稿多投、desk-reject 排查。 |
| [`wacv-review-process`](skills/wacv-review-process/SKILL.md) | 建模两轮流程、Round 1 的三种推荐、无 rebuttal 的 Round 2，以及作者杠杆真正在何处。 |
| [`wacv-author-response`](skills/wacv-author-response/SKILL.md) | 撰写 Round 1 一页 rebuttal，以及另行撰写把论文带入 Round 2 的 Revise-and-Resubmit 变更摘要。 |
| [`wacv-camera-ready`](skills/wacv-camera-ready/SKILL.md) | 交付 version of record：去匿名、真实链接、数据集发布、CVF/IEEE 双重发表与冬季报告。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 13 个官方来源及访问日期、已核验的两轮与格式事实、访问方式说明，以及明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口（两个 OpenReview 轮次 group）与五个作者侧核验流程。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 跨两个 track 的元数据核验 WACV 论文（GeoDiffuser、Re-Evaluating LiDAR Scene Flow），并附姐妹会误引防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构 applications-track 首页面向两轮审稿人的 before → after 重写。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 ML 会议可复现工具包的适配器，含 WACV 专属的轮次同步与约束复现说明。 |

## 安装与使用

作为 Claude Code 插件（本目录是自包含插件，带自己的 marketplace manifest）：

```bash
# 在仓库克隆中
claude plugin marketplace add ./WACV-Skills
claude plugin install wacv-skills
```

或直接使用文件：每个 `skills/wacv-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 告诉 agent 何时触发。典型调用：

- “这是 WACV 论文吗？该投哪个 track？” → `wacv-topic-selection`
- “该投 Round 1 还是 Round 2？” → `wacv-workflow` / `wacv-submission`
- “我拿到 Revise and Resubmit —— 接下来怎么办？” → `wacv-author-response` / `wacv-review-process`
- “按 WACV 的页数与匿名规则审我的稿” → `wacv-submission`
- “我该在 8 页正文与匿名补充材料间怎么分配内容？” → `wacv-supplementary`
- “camera-ready 该做哪些去匿名与发布步骤？” → `wacv-camera-ready`

## 目录结构

```text
WACV-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── wacv-<topic>/SKILL.md # 12 个 skill，每个一个目录
└── resources/
    ├── README.md             # 资源指南与建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 指向共享可复现工具包的适配器
```

## 与 CVPR/ICCV/ECCV 的关键区别（一句话）

WACV 的承重差异在于 **两轮 Revise-and-Resubmit 审稿**：多数论文在修改环节定生死，rebuttal
只在 Round 1 存在，Round 2 无 rebuttal；再叠加 **Applications / Algorithms 双轨** 与冬季日历。
其他 CVF 姐妹会都是单轮、无正式修改路径。若把 WACV 当作单截止会议来规划，就会白白丢掉它为
临界论文设计的安全网。

## 事实分级

全包始终区分三类陈述：

1. **已核验事实** —— 可追溯到 source map 中的编号来源（两轮模型及其三种 Round 1 结果、
   8 页含图表上限、双盲 OpenReview 规则、WACV 2025 Round 1 统计、CVF/IEEE 双重发表）。
2. **据报事实** —— 一致的二手或单一第一方来源，并标注为此类（据搜索渲染读取的 WACV 2027
   分轮日期、混合录用率区间、除已核验的 GeoDiffuser 外的最佳论文认定）。
3. **核验时不可确证条目** —— 明确标注 待核实（WACV 2027 确切会议日期与城市、补充材料大小上限、
   camera-ready 版面与表单、报告义务、任何 AI 披露要求）。

若某 skill 把第 2/3 类当作第 1 类陈述，应视为 bug，并对照官方页面修正。

## 维护说明

- 此处每个日期与规则都是**周期快照**。WACV 政策由轮换 chairs 每年重设 —— 在给出 deadline 敏感
  建议前，请重新打开 `wacv.thecvf.com` 当年页面，并记得它运行 **两个 OpenReview group**。
- 据报的 WACV 2027 分轮日期经搜索渲染读取；请在实时 Dates 页面重新确认，会议日期与城市按 待核实
  处理。
- 两轮模型、三种 Round 1 结果、以及 Applications/Algorithms 分轨是承重的差异点 —— 若未来周期改动
  它们，本包大部分内容需重新推演，而不仅是改日期。
- 新增 exemplar 时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程 —— `thecvf.com` 链接只有路径含 `WACV20XX` 时才是 WACV 引用。
- 补充材料大小上限、camera-ready 版面/表单、以及现场报告义务在核验时无法从渲染中确证，均按
  待核实 处理；给出交付级建议前，请对照当年官方 Author Guidelines 逐项确认。

## 核验环境说明

`wacv.thecvf.com` 与 `openaccess.thecvf.com` 在本次核验环境中被网关拦截（HTTP 403），因此
官方内容通过对精确 URL 的搜索渲染读取，并与 OpenReview、dblp、IEEE Xplore 及历年 WACV 站点
存档交叉核对；据报的 WACV 2027 分轮日期尤应在实时 Dates 页面重新确认。完整来源链路见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English README: [`README.md`](README.md)。
