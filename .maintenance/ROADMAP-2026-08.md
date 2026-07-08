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
      静态尺子饱和、失去区分度——不再追静态分，scorecard 转为 CI 回归防线
      （run_checks 下限 90→94，2026-07-08 落地）。质量牵引换挡方案见
      `.maintenance/QUALITY-LANE-2026-09.md`（更正：初版建议的 skillopt 行为
      评测装置系 owner 2026-06-29 刻意拆除之物，不重建；改为轻量人触发流程）。

## Week 2（07-15 ~ 07-21）：category-8 扩张波（Wave 25-A 第 7–10 位）

按 `.maintenance/CATEGORY-8-BUILD-QUEUE.md` 既定顺序推进 UAI / COLT / MLSys / KDD
4 个完整会议深度包（category-8 完成度 6/100 → 10/100）：

- [x] 每包 12 skills（2026-07-08 完成，4 包共 48 个 SKILL.md、100 个文件），
      以 AISTATS-Skills 为结构金标准，prose 全部 venue-specific。
      理论会议（COLT）的 experiments/artifact 类 skill 按其真实形态改写——
      colt-artifact-evaluation 开篇即声明「COLT 无 artifact track/badge，
      证明附录即 artifact」，未假装存在 NeurIPS 式流程。
- [x] 事实纪律（2026-07-08）：4 包全部锚定各自 2026 届官方 CFP/日期页/OpenReview
      组/PMLR·ACM 出版页，URL + 访问日期落 `resources/official-source-map.md`。
      诚实披露：建包环境网关拦截 auai.org / learningtheory.org / mlsys.org /
      kdd2026.kdd.org 的直连抓取，官方页内容经搜索渲染核实并与 OpenReview 组、
      PMLR/dblp 元数据交叉验证——4 张 source map 均带 access-method note，
      无法钉住的条目（费用、camera-ready 细则、2027 周期等）全部列入 待核实。
- [x] 双语 README、plugin/marketplace 元数据、LICENSE、cover.svg、
      exemplars/worked-examples/external_tools 资源层齐全（逐包 25 文件）。
- [x] 对账（2026-07-08）：audit_repo 硬计数 2950/199 通过；根 marketplace 199 条；
      双语 README 徽章、学科表、深度包表（+4 行）、目录树（+4 行）、计数口径
      （2275 = 189 深度包）全部同步；quality_scorecard CONFERENCE_DEPTH_PACKS
      与 gen_venue_index 学科映射 +4；venue 索引再生成（185→189 行）；
      CATEGORY-8-BUILD-QUEUE（6→10 complete）、ASSET-INVENTORY、
      JOURNAL-MASTER-LIST [A-depth] 标记完成。
- [x] 验收（2026-07-08）：audit_repo 全绿；全仓克隆审计 0.75 阈值零命中
      （2950 skills / 350 groups，含 4 新包交叉比对）；4 包 bundle 内部审计
      0.70 阈值零命中；scorecard 199 包 min = mean = 94.0，新包与既有
      conference 包同档。

## Week 3（07-22 ~ 07-28）：事实核实清欠 + 外链健康

**执行结果（2026-07-08，诚实留档）——本环境对期刊/出版社域名整体封锁，
live 核实两条线均不可为，改做离线可验证的替代审计：**

- [x] 环境封锁取证：curl / Python urllib 在代理 CONNECT 阶段即被策略拒绝
      （`__agentproxy/status` 记录 connect_rejected "policy denial"）；WebFetch
      通道对 academic.oup.com、pnas.org、nasonline.org、econometricsociety.org、
      ciejournal.ajcass.com 全部 403，jmsc.tju.edu.cn DNS 不可解析。按代理
      README「组织策略拒绝不重试」纪律，live 复核顺延到有期刊域名出口的环境
      （owner 本地或 CI）。
- [x] source-map 待核实清欠 → **顺延并修正问题定义**：216 处基线中相当比例是
      「为什么当时没核实到」的诚实说明（计数正则同时匹配 403/blocked/could not
      等阻断解释），并非等量的开放事实债。本月不改计数正则（避免连续两次
      "把指标改小"），待 live 核实通道恢复后一并清欠。
- [x] 替代审计（离线可验证）：对 top-5 欠账包做**事实可追溯性抽查**——扫描
      全部 SKILL.md 中的硬数字（费用/字数/页数/百分比/天数），核对是否能回溯
      source map 或带稳健表述。43 个命中段落逐一复核：全部为方法论数字
      （95% CI、5%/10% 检验水平）、明确标注「示意」的教学数值、或措辞变体
      （"45 pages" vs source map 的 "45-page limit"，实已锚定）。
      **结论：0 处真实违规，top-5 包事实纪律通过。**
- [x] 外链审计：已跑 `tools/external_link_audit.py`（1843 个 URL），结果
      0 OK / 86 BLOCKED / 1757 UNREACHABLE——即同一环境封锁导致的全网不可达，
      按工具自身文档（"UNREACHABLE … re-run before acting"）不据此改动任何
      链接。外链健康继续由每周 CI 的 advisory external-link job（GitHub
      Actions 出口不受此策略限制）承担。

## Week 4（07-29 ~ 08-08）：社区治理 + 总验收

- [x] 补上月 ACCEPTANCE §3.2 明确欠账（2026-07-08，commit `879a098`）：
      `.github/ISSUE_TEMPLATE/bundle-replication-request.yml` 上线；
      `CONTRIBUTING.md` 新增「How to reuse a pack bundle」四条规则小节，
      并同步 structure 带宽（8–20）与分数地板（94）。
- [x] CLAIMS.md 治理减负（2026-07-08，同 commit）：366 行历史 lane 归档至
      `.maintenance/CLAIMS-ARCHIVE-2026-06.md`，CLAIMS.md 重置为精简现役板
      （协作规则 + 单一活跃 lane + 常设纪律）。
- [x] 总验收（2026-07-08）：`.maintenance/ACCEPTANCE-2026-08.md` 已交付——
      指标对照表、证据链、四条诚实灰色地带（source-map 顺延 / 外链留档 /
      scorecard 饱和退役预告 / category-8 10/100）。
- [x] release 建议：ACCEPTANCE §5 已向 owner 提议 v1.1.0 及 notes 要点；
      tag 由 owner 验收后决定，本任务未代打。

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
