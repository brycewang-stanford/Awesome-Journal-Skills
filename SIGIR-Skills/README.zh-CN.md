# SIGIR Skills（中文说明）

面向 **SIGIR（International ACM SIGIR Conference on Research and Development in
Information Retrieval）** 投稿的 12 个 agent skills。SIGIR 是搜索、排序、推荐与检索
评价方向的旗舰会议，本包围绕四个使 SIGIR 策略不同于一般 ML 会议经验的结构性事实来组织：

1. **多轨道投稿体系，而非单一 CFP。** SIGIR 2026 设有 Full、Short、Perspectives、
   Resources、Reproducibility、Industry、Low Resource Environments 等轨道，规则分散在
   各轨道页面；Resources 轨道甚至采用**单盲**评审。把贡献路由到正确轨道是第一优先决策。
2. **没有附录逃生舱。** 长文 9 页、短文 4 页，仅参考文献不计页——附录计入正文页数，
   放不下的内容只能进论文引用的代码仓库，或者删掉。
3. **TREC 血统的评价文化。** 审稿人先审 protocol 再看创新性：测试集选择、baseline 调参
   对称性、指标 cutoff 纪律、逐 topic 配对显著性检验；"significantly" 在 IR 写作中是
   保留字，没有检验就不能用。
4. **ACM 出版管线。** 录用论文经 e-rights 与 TAPS 进入 ACM Digital Library
   （SIGIR 2025 卷：DOI 10.1145/3726302），CCS concepts 与元数据会伴随论文终身。

官方依据核验日期：**2026-07-08**。已核验：SIGIR 2026 官网（第 49 届，2026 年 7 月
20-24 日，澳大利亚墨尔本 | Naarm）、各轨道投稿页面与跨轨道政策页、SIGIR OpenReview
venue groups、ACM DL proceedings 记录、sigir.org，以及作为上一周期锚点的 SIGIR 2025
CFP。精确来源（含访问方式披露：部分官方域名只能通过搜索渲染核验）与全部 待核实 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 已核验的 2026 周期锚点

| 事实 | 2026 取值 | 变动性 |
|---|---|---|
| 届次 | 第 49 届，2026-07-20 至 24，墨尔本 \| Naarm | 每届 |
| 长文 | ≤ 9 页（参考文献除外；附录计入页数）；双盲 | 每周期 |
| 短文 | ≤ 4 页（参考文献除外）；独立 OpenReview group | 每周期 |
| Resources 轨道 | ≤ 6 页 + 参考文献；**单盲**；摘要 2/5 → 通知 4/2 → camera-ready 4/29 | 每周期 |
| Reproducibility | 2026 起独立成轨（从原合并轨道拆出） | 每周期 |
| 模板 | ACM Primary Article Template（LaTeX `sigconf` / Word Interim） | 每周期 |
| PC 义务 | 长文每篇需提名一位作者进入 PC | 每周期 |
| 平台 | OpenReview，按轨道分 group | 每周期 |
| 政策 | ACM 署名与 AI 使用披露；一稿多投直接拒；跨轨道重复投稿禁止 | 每周期 |
| 出版 | ACM DL，经 e-rights + TAPS | 每年 |

2026 长短文的精确截稿日（第三方 tracker 报告摘要 1/15、全文 1/22 AoE，与 2025 模式
一致）、rebuttal 机制、camera-ready 页数、主席名单与费用等均无法在线核实，已在来源图中
标注 待核实，不作断言。

## Skills 一览

选题与规划：

- [`sigir-topic-selection`](skills/sigir-topic-selection/SKILL.md)：两个判据——把检索
  组件换成 oracle 后贡献是否还成立（成立则不是 IR 论文）；最强诚实主张属于哪个轨道。
  并附 ECIR、CIKM、WSDM、CHIIR、ICTIR、RecSys、TheWebConf 与 NLP/ML 场馆的分流表。
- [`sigir-workflow`](skills/sigir-workflow/SKILL.md)：一月截稿的年度节奏、摘要/全文
  两段闸门的倒排计划、跨轨道禁令下的多线协调，以及 SIGIR→CIKM→SIGIR-AP→WSDM→ECIR
  的落选接力环。

写作与证据：

- [`sigir-writing-style`](skills/sigir-writing-style/SKILL.md)：IR 语域——先说任务与
  约束 regime、失败要说成机制、证据预告要带集合/指标/显著性、保留字纪律、以表格承载论证。
- [`sigir-related-work`](skills/sigir-related-work/SKILL.md)：从 Ponte & Croft 到
  ColBERT 的谱系素养、机制对比式 delta 句、场馆错标防护（DPR 在 EMNLP、ANCE 在 ICLR、
  NCF 在 WWW）、arXiv 时代同期工作处理。
- [`sigir-experiments`](skills/sigir-experiments/SKILL.md)：主张-测试集匹配、指标
  cutoff 纪律、配对检验加多重比较校正的社区惯例、baseline 调参对称、消融矩阵，以及
  LLM 时代新风险（数据污染、LLM 评审员校验、prompt 方差）。
- [`sigir-reproducibility`](skills/sigir-reproducibility/SKILL.md)：IR 结果漂移的七大
  来源与逐项钉死方法；以及如何把 Reproducibility 轨道论文写成"分歧归因"型研究。

打包与投稿：

- [`sigir-artifact-evaluation`](skills/sigir-artifact-evaluation/SKILL.md)：run file +
  qrels + 索引配方的社区 artifact 标准、Resources 轨道与随文仓库的路由决策、标注文档
  规范、双盲/单盲两套打包。
- [`sigir-supplementary`](skills/sigir-supplementary/SKILL.md)：无附录规则下的三容器
  模型（预算页 / 免费参考文献 / 引用仓库），以及按"评审关键性"排序的取舍法。
- [`sigir-submission`](skills/sigir-submission/SKILL.md)：上传前审计——长短文格式对照、
  IR 特有的匿名风险（系统名、leaderboard、查询日志）、政策闸门、desk-reject 分级与
  最后一周操作序列。

评审期与录用后：

- [`sigir-review-process`](skills/sigir-review-process/SKILL.md)：按轨道分治的评审
  机器、IR 审稿人的打分序（评价效度先于创新性）、四种审稿人画像、决定包分诊。
- [`sigir-author-response`](skills/sigir-author-response/SKILL.md)：有窗口时如何精准
  回应、无窗口时如何在写作期预答、被拒后的路由方案（含 SIGIR-AP 公布过的 R&R 通道）。
- [`sigir-camera-ready`](skills/sigir-camera-ready/SKILL.md)：e-rights、TAPS、评审
  化名回解、CCS concepts 与 DL 元数据、artifact 公开，以及四月到七月的生产跑道。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：全部来源
  URL、访问日期、已核验事实与 待核实 清单。
- [`resources/external_tools.md`](resources/external_tools.md)：各轨道页面、OpenReview
  groups、ACM 写作管线与 IR 工具栈（trec_eval、ir_measures、ir_datasets、Anserini 等）。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：六篇经 DOI 核验的
  SIGIR 范文（1998-2020）与错标防护清单。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  虚构论文的首页弧线改写示范（before → after）。
- [`resources/code/README.md`](resources/code/README.md)：共享 ML 会议可复现工具包的
  IR 适配层。

## 建议使用顺序

1. **路由**：`sigir-topic-selection`（轨道分叉），再 `sigir-workflow`（日历倒排）。
2. **构建**：`sigir-experiments` + `sigir-reproducibility` 打证据，同时用
   `sigir-writing-style` 与 `sigir-related-work` 成稿。
3. **打包**：截稿周之前完成 `sigir-artifact-evaluation` 与 `sigir-supplementary`，
   然后跑 `sigir-submission` 审计。
4. **评审期**：用 `sigir-review-process` 读懂机器，用 `sigir-author-response` 应答
   （或在写作期预答）。
5. **出版**：录用后 `sigir-camera-ready`；被拒则回到 `sigir-workflow` 的接力环。

## SIGIR 投稿者最常踩的坑（速查）

1. **把压缩版长文当短文投**：短文是"一个聚焦发现的完整论证"，不是删减版长文；证据
   残缺在 4 页里更显眼。
2. **指望附录**：SIGIR 附录计入页数，别人的"细节见附录"策略在这里不成立，出口是
   论文引用的仓库。
3. **裸用 "significantly"**：没有配对检验与多重比较校正就使用该词，是这个社区
   最容易识别的信誉漏洞。
4. **baseline 调参不对称**：SIGIR 最常见的致命审稿意见；调参预算要对称并写进论文。
5. **数据集与方法论文跨轨道双投**：2026 政策明令禁止，投稿前先分配好每个贡献的归属。
6. **忘记 PC 提名义务**：长文每篇需提名一位作者进 PC，临截稿再找人选是自造危机。

## 安装

```bash
claude plugin marketplace add ./SIGIR-Skills
claude plugin install sigir-skills
```

也可以直接让 agent 读取单个 `skills/sigir-*/SKILL.md`——每个 skill 自含范围声明与
结构化输出块，可彼此组合。

## 范围与免责声明

- 本包提供投稿策略、结构与证据建议，不是 CFP 本身：任何与当届轨道页面冲突之处，
  以官方页面为准。
- 所有具体事实核验于 2026-07-08，且按"周期锚点"措辞。SIGIR 在 2025→2026 之间就重组过
  轨道（Resource & Reproducibility 拆分），未来同样可能变化。
- 标注 待核实 的条目（截稿日、rebuttal、费用、主席、camera-ready 页数）在向作者陈述
  之前必须在线核实。
- 包内文字不应粘贴进论文；worked example 是刻意虚构的，exemplar library 记录的是
  定位模式而非可复用文句。

## 维护说明

- 给出任何 deadline 敏感建议前，重开**对应轨道**页面而非记忆中的"SIGIR CFP"。
- 每届会后更新：届次/城市、轨道阵容、页数预算、各轨道匿名制度、OpenReview group id、
  ACM Open 状态说明。
- SIGIR 2027 是第 50 届、按轮换规则在美洲举办——周年届往往有额外变动，逐项重验。
