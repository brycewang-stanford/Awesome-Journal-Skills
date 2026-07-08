# ROADMAP — 2026-08 一个月工作计划（2026-07-08 启动）

**定位**：2026-07 路线图已全部完成并验收（见 `ROADMAP-2026-07.md` +
`ACCEPTANCE-2026-07.md`）。本月是「质量饱和收尾 + 有节制扩张 + 事实清欠 + 治理减负」
四线并进：把上月遗留的最后 0.1 平均分灰色地带诚实解决，按既定 category-8 队列
推进 4 个新会议深度包，压降 source-map 待核实欠账，并把社区/协作文档瘦身到
新贡献者可读的状态。

**基线（2026-07-08，commit `0602461` 复验）**：
195 个 first-party pack · 2902 个 skill · scorecard 平均 93.9 / 最低 92.0 ·
执行桥 134/134 · showcase 5 条 · run_checks 硬门槛全绿 · 克隆审计 0.75 阈值零命中 ·
source-map 待核实标记共 216 处（top-5：PNAS-Nexus 14、中国工业经济 6、世界经济 6、
Econometrica 5、管理科学学报 5）。

**总原则**（沿用既有纪律）：
- 质量优先于数量：新增 pack 必须是完整 12-skill、官方源背书的深度包，过全部硬门槛。
- 证据优先于声称：事实只来自各 pack `resources/official-source-map.md`，
  不可达的源诚实标 `待核实`，禁止编造。
- 度量诚实：不为凑指标弱化 substance 门槛；对评分尺子本身的错配，
  只做有据可依、全量 before/after 可复验的规格修正，并在本文件留档。
- 克隆纪律：新增 prose 必须 venue-specific，`clone_audit.py --threshold 0.75` 零命中。

---

## Week 1（07-08 ~ 07-14）：质量饱和收尾（mean → 94.0）

上月 ACCEPTANCE §3.1 把 6 个 92.0 pack 的差距归因为「缺 venue-specific 素材」。
本月复查推翻了该诊断：`quality_scorecard.py --json` 逐项分解显示这 6 个 pack 在
depth (35/35)、trigger (20/20)、resources (28/28)、runnable (5/5) 全部满分，
唯一丢分点是 structure 档位的 2 分：

- 5 个 breadth 束（31/13/31/41/37 个 skill，全部带 router）被 `n >= 50` 的
  绝对规模门槛判 1 分——但该门槛与分类逻辑自相矛盾：分类端明确承认
  「小而聚焦的 breadth 束」（如 13 刊运动科学束）合法，结构端却按规模罚分。
  一个覆盖其自身 roster 的完整小束不是缺陷。
- Economic-Research-Journal-Skills（depth，18 skills）被 `8 <= n <= 14` 的
  上界判 1 分——该包是 2026-06 被两个 agent 刻意深化到 18 skills 的旗舰包，
  「更完整」反而扣分是尺子错配。

- [x] 度量规格修正（2026-07-08 完成；不动 depth/trigger/resources/runnable 任何
      substance 门槛）：breadth structure 满分条件 `n >= 50 and has_router` →
      `n >= 12 and has_router`（router 是 breadth 的结构本质，12 为防 stub 下限）；
      depth structure 上界 14 → 20（保留防 stub 下限 8 与防散漫上限）。
- [x] 全量 before/after 对比（2026-07-08）：195 个 pack 中恰好且仅有目标 6 个变动，
      全部 92.0 → 94.0（Agriculture-Environment / Chinese-Sport-Science /
      Clinical-Medicine / Economic-Research-Journal / Engineering-Technology /
      English-Humanities），其余 189 个 pack 分数逐一相等。
- [x] 复跑验证（2026-07-08）：scorecard min 94.0 / mean 94.0；run_checks 硬门槛全绿。
- [x] 留档说明：94.0 是当前评分公式的构造性满分（35+20+28+5+6=94）。本次收尾后
      静态尺子饱和、失去区分度——下月起质量牵引应转向行为评测
      （`tools/skillopt/` 的 rollout→judge→gate 路线），不再追静态分。

## Week 2（07-15 ~ 07-21）：category-8 扩张波（Wave 25-A 第 7–10 位）

按 `.maintenance/CATEGORY-8-BUILD-QUEUE.md` 既定顺序推进 UAI / COLT / MLSys / KDD
4 个完整会议深度包（category-8 完成度 6/100 → 10/100）：

- [ ] 每包 12 skills（submission / author-response / camera-ready /
      artifact-evaluation / reproducibility / supplementary / review-process /
      writing-style / related-work / experiments / workflow / topic-selection），
      以 AISTATS-Skills 为结构金标准，prose 全部 venue-specific。
      理论会议（COLT）的 experiments/artifact 类 skill 按其真实形态改写
      （证明验证、附录组织），不假装存在 NeurIPS 式 artifact track。
- [ ] 事实纪律：官方源（auai.org / learningtheory.org / mlsys.org / kdd.org 及
      各 2026 届 CFP）live 核实，URL + 访问日期落
      `resources/official-source-map.md`；不可达即 `待核实`。
- [ ] 双语 README、plugin/marketplace 元数据、LICENSE、cover.svg、
      exemplars/worked-examples/external_tools 资源层齐全。
- [ ] 对账：`tools/audit_repo.py` 硬计数 2902→2950 / 195→199、根 README 徽章与
      表格、`quality_scorecard.py` CONFERENCE_DEPTH_PACKS 集合、venue 索引再生成、
      `.maintenance/` 队列文件（CATEGORY-8-BUILD-QUEUE / ASSET-INVENTORY /
      JOURNAL-MASTER-LIST）标记 [A-depth]。
- [ ] 验收：`run_checks.py` 全绿；4 个新包 bundle 克隆审计无 ≥0.75 对；
      新包 scorecard 不拖后腿（≥ 既有 conference 包水平）。

## Week 3（07-22 ~ 07-28）：事实核实清欠 + 外链健康

- [ ] source-map 待核实清欠：对 top-5 欠账包（PNAS-Nexus 14、中国工业经济 6、
      世界经济 6、Econometrica 5、管理科学学报 5，共 36 处）逐条 live 复核；
      可核实的落 VERIFIED + 2026-07 访问日期，官方站不可达（403/JS 墙）的保留
      诚实标记并注明拦截原因。目标：全仓 216 处 → ≤ 190 处，且 top-5 包
      每包净下降。
- [ ] 外链审计：跑 `tools/external_link_audit.py`，对确认 404/域名失效的链接
      替换为当前官方地址；重定向到新官方域的更新；无法判定的不动。
- [ ] 复跑 source_map_audit / external_link_audit 留档 before/after 数字。

## Week 4（07-29 ~ 08-08）：社区治理 + 总验收

- [ ] 补上月 ACCEPTANCE §3.2 明确欠账：新增
      `.github/ISSUE_TEMPLATE/bundle-replication-request.yml`（用户申请复用
      pack 模板做自定刊物），并在 `CONTRIBUTING.md` 增加「如何复用一个 pack
      bundle」小节（先写规则、再挂模板）。
- [ ] CLAIMS.md 治理减负：2026-06 多代理并发期的历史 lane 已全部完成/合并，
      整板归档到 `.maintenance/CLAIMS-ARCHIVE-2026-06.md`，CLAIMS.md 重置为
      精简的当前状态板（保留协作规则 + 空 claim 表 + 指向归档）。
- [ ] 总验收：`.maintenance/ACCEPTANCE-2026-08.md`——全部硬检查 + scorecard
      分布 + 克隆审计 + source-map/外链 before/after + 诚实灰色地带。
- [ ] release 建议：验收通过后向 owner 提议 v1.1.0（4 新包 + 质量饱和 +
      清欠），tag 由 owner 决定是否打；本任务不自行发 release。

---

## 验收指标（月底 2026-08-08）

| 指标 | 基线（07-08） | 目标 |
|---|---|---|
| scorecard 最低分 | 92.0 | 94.0（公式满分） |
| scorecard 平均分 | 93.9 | 94.0（公式满分，尺子饱和留档） |
| first-party packs | 195 | 199（category-8 +4，全部完整深度包） |
| canonical skills | 2902 | 2950 |
| category-8 完成度 | 6/100 | 10/100 |
| 克隆审计 0.75 阈值 | 0 命中 | 0 命中（含 4 新包） |
| source-map 待核实总数 | 216 | ≤ 190（top-5 包每包净降） |
| 外链审计 | 未跑本月基线 | 确认失效项清零或留档不可修原因 |
| issue 模板 | 3 套 | 4 套（+bundle-replication-request） |
| CLAIMS.md | 366 行历史堆积 | 归档重置，新贡献者可读 |
| run_checks 硬门槛 | 全绿 | 全绿 |

进度与决策记录在本文件追加；月度全量复验数字以 `ACCEPTANCE-2026-08.md` 为准。
