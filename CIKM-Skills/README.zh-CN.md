# CIKM Skills

面向 **CIKM（ACM International Conference on Information and Knowledge Management）**
投稿的 12 个 agent skills。CIKM 是 information retrieval、data mining 与 knowledge
management/databases 三个社区共用一个会场的 ACM 会议。本包围绕四个结构性事实构建，
使 CIKM 策略成为独立学问，而不是 SIGIR 或 KDD 建议的复用：

1. **三社区混合审稿池。** CIKM 由 ACM SIGIR（1993 年起）与 SIGWEB（2006 年起）联合
   主办，一篇投稿通常同时被三个"车道"的审稿人阅读——IR 的评测文化、mining 的机制
   文化、KM/数据库的数据现实文化。本包的核心教学：什么时候这种宽度是优势（双车道、
   三车道论文），什么时候单一社区的专门会议更合适。
2. **五个 track，附录一律计入页数。** CIKM 2026 设 Full Research（≤10 页，**含**
   附录，另加 ≤2 页参考文献）、Short（≤4 页）、Applied Research（≤7 页，必须有部署
   证据）、Resource（≤4 页）、Demonstration（≤4 页）——"挪到附录"省不了任何空间，
   track 路由是第一级决策。
3. **有后果的 EasyChair 表单。** 每个 track 都要求提名一位作者担任审稿人（漏填即
   明文 desk reject）、要求申报任何公开的非匿名版本（arXiv 版本瞒报有 desk reject
   风险），并且 PDF 中必须包含 **GenAI Usage Disclosure** 一节，覆盖研究、代码、
   数据与写作全流程——会方保留自动合规检查的权利。
4. **信息家族日历里的秋季档。** 5 月摘要/全文关口、8 月 7 日通知、8 月 20 日
   camera-ready、11 月开会——这让 CIKM 成为 SIGIR 一月关口或 KDD 二月关口之后
   工作成熟时的自然下一站，也给录用作者留下 13 天的 ACM e-rights/TAPS 冲刺。

官方依据核验日期：**2026-07-08**。已核验：CIKM 2026 主站（第 35 届，2026 年 11 月
7-11 日，意大利罗马，站点位于罗马 Sapienza 大学域名下）、五个 track 的征稿页、
important-dates 与 submission-policies 页、CIKM '25 的 ACM DL 论文集记录（DOI
10.1145/3746252）、dblp 的 CIKM 索引，以及 SIGIR/SIGWEB 主办方页面。若干官方域名
只能通过搜索渲染读取（网关拦截了直接抓取）；访问方式说明、完整来源清单与所有
待核实条目见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 已核验的 2026 周期锚点

| 事实 | 2026 取值 | 波动性 |
|---|---|---|
| 届次 | 第 35 届 CIKM，2026-11-07 至 11，罗马 | 每届变化 |
| Full Research | ≤10 页（图表、**附录**计入）+ ≤2 页参考文献；双盲 | 每周期 |
| Short Research | ≤4 页（含附录） | 每周期 |
| Applied Research | ≤7 页；需要上线/数据发布等实证 | 每周期 |
| Resource / Demo | 各 ≤4 页；demo 论文进主论文集 | 每周期 |
| 日程 | Full：摘要 5-16、全文 5-23；short/resource/demo：5-30 / 6-6；通知 8-7；camera-ready 8-20（均 AoE） | 每周期 |
| 平台 | EasyChair，每篇选定对应 track | 每周期 |
| 表单义务 | 作者-审稿人提名（漏填 desk reject）；arXiv 版本申报 | 每周期 |
| GenAI 政策 | 必须含不计页的 "GenAI Usage Disclosure" 节；遵守 ACM AI 政策；禁止 AI 代写审稿 | 每周期 |
| 一稿多投 | 禁止与任何会议/期刊并行投稿；作者名单在摘要关口冻结 | 每周期 |
| 出版 | ACM Digital Library（e-rights + TAPS） | 每年 |

截至核验日，2026 所有投稿关口均已关闭——本包教的是**当前进行中的投稿后阶段**
（审稿等待、通知、13 天 camera-ready 窗口、罗马行程），以及 CIKM 2027 的规划。
2026 是否设 rebuttal、主席名单、camera-ready 页数放宽、注册费用与 2027 各项事实
均无法核验，一律标注待核实而非断言。

## Skills

选路与规划：

- [`cikm-topic-selection`](skills/cikm-topic-selection/SKILL.md)——车道计数测试
  （论文真正占据 IR/mining/KM 中的几条），对 SIGIR/KDD/WSDM/TheWebConf/SIGMOD/ISWC
  的诚实秋季档定位，以及五 track 分岔。
- [`cikm-workflow`](skills/cikm-workflow/SKILL.md)——5 月到 11 月的年度节奏、当前
  两种工作模式（审稿等待 vs 备战下一届）、摘要关口的作者名单冻结、多 track 协同
  与退路环。

写作构建：

- [`cikm-writing-style`](skills/cikm-writing-style/SKILL.md)——三车道首页
  （问题 → 边界为何难 → 有名字的机制 → 校准的证据预告）、跨车道词汇钉牢、
  附录计页下的压缩策略。
- [`cikm-related-work`](skills/cikm-related-work/SKILL.md)——三条战线的文献覆盖、
  boundary-work 段落、CIKM 自家里程碑的引用，以及误归属防线
  （DeepWalk/SASRec/NGCF/Conv-KNRM/TransE 都**不是** CIKM 论文）。
- [`cikm-experiments`](skills/cikm-experiments/SKILL.md)——claim-车道-证据契约、
  让混合评审团都认可的数据集选择、隔离机制的 ablation，以及 Applied track 的
  部署证据门槛。
- [`cikm-reproducibility`](skills/cikm-reproducibility/SKILL.md)——链式流水线
  （索引/KG/模型/评测）的漂移地图、不可发布数据的诚实模式、把 GenAI 披露当作
  方法记录。

投稿：

- [`cikm-submission`](skills/cikm-submission/SKILL.md)——分 track 页数卡、EasyChair
  三道表单关口、GenAI 披露节、匿名清扫与 desk-reject 台账。
- [`cikm-supplementary`](skills/cikm-supplementary/SKILL.md)——三容器拆分（计页
  附录 vs 匿名 artifact vs 删除），以及不计页部分不许装什么。
- [`cikm-artifact-evaluation`](skills/cikm-artifact-evaluation/SKILL.md)——各 track
  的 artifact 角色、Resource track 的可采纳门槛、KG 快照打包、demo 生存包与
  匿名到公开的分阶段发布。

审稿到出版：

- [`cikm-review-process`](skills/cikm-review-process/SKILL.md)——混合审稿池效应、
  各 track 的评价标准差异、什么能推动 borderline，以及当前周期的时间线现实。
- [`cikm-author-response`](skills/cikm-author-response/SKILL.md)——四种作者侧写作
  情形（有无窗口 × 录用与否）、三车道回复结构与 concern → edit 台账。
- [`cikm-camera-ready`](skills/cikm-camera-ready/SKILL.md)——穿过 e-rights 与 TAPS
  的 13 天序列、超越"加名字"的去匿名化、CCS/dblp 元数据、GenAI 节保留与并行的
  罗马行程线。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)——每条
  已核验事实附 URL 与访问日期；所有缺口标注待核实。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)——六篇经 dblp
  核验的 CIKM 里程碑（TAGME 2010 → BERT4Rec 2019），覆盖全部车道组合，并列出
  已查证的邻会误归属陷阱。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  ——虚构论文开头的 before → after 三车道改写示范。
- [`resources/external_tools.md`](resources/external_tools.md)——官方在线入口及
  各入口需复查的内容。
- [`resources/code/README.md`](resources/code/README.md)——仓库共享的 ML 会议
  可复现工具包，附工具包覆盖不到的 CIKM 专项检查。

## 使用方式

按场景的典型入口：

| 你的处境 | 先用 | 再用 |
|---|---|---|
| 判断一篇边界论文投哪里 | `cikm-topic-selection` | `cikm-workflow` 算日历账 |
| 手上有 CIKM 2026 在审稿件（当前周期） | `cikm-workflow` 模式 A | `cikm-camera-ready` 预备 + `cikm-author-response` 台账 |
| 为下一届起草 | `cikm-writing-style` + worked example | `cikm-experiments`、`cikm-related-work` |
| 距离 deadline 一周 | `cikm-submission` | `cikm-supplementary` 做拆分决策 |
| 做 resource 或 demo | `cikm-artifact-evaluation` | `cikm-submission` 查该 track 页数卡 |
| 刚被拒 | `cikm-author-response`（重投简报） | `cikm-workflow` 退路环 |

每个 skill 末尾都有 output format 块，让 agent 的输出成为可比对、可决策的摘要，
而不是散文。

## 目录结构

```text
CIKM-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（12 条 skill 路径）
├── assets/cover.svg
├── resources/
│   ├── official-source-map.md    # 已核验事实 + 待核实清单
│   ├── external_tools.md         # 官方在线入口
│   ├── exemplars/library.md      # 六篇 dblp 核验的 CIKM 里程碑
│   ├── worked-examples/01-introduction.md
│   └── code/README.md            # 共享可复现工具包指针
└── skills/cikm-*/SKILL.md        # 十二个 skills
```

## 与邻会包的关系

本仓库另有 SIGIR、KDD、WSDM 等专门会议包。分工原则：单一社区的深度问题
（IR 评测协议、KDD 双周期机制、WSDM 匿名实验传统）在各自的包里；CIKM 包
专注三社区混合场景——车道计数、边界论文写法、appendix 计页预算、EasyChair
表单义务与 GenAI 披露。一篇论文在 CIKM 与邻会之间摇摆时，从本包的
`cikm-topic-selection` 开始，它会诚实地把不适合 CIKM 的论文送去邻会。

## 维护说明

- CIKM 每年换一个主办方域名；不要沿用去年的 URL 或规则，从系列页或对当届的
  新搜索出发。
- 锚点表里的每一项都可能被下一届主办委员会改写：track 阵容、页数、平台
  （当前是 EasyChair）、披露措辞与提名规则。
- 本包中的 2026 事实是带日期的推理锚点，不是常设政策。官方页面与本包冲突时，
  以页面为准，并用新的访问日期更新 source map。
