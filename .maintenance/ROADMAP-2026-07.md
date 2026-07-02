# ROADMAP — 2026-07 一个月整体跃升计划

**目标**：把 Awesome-Journal-Skills 打造成全网第一的「自动实证研究」skill 仓库——
不仅是最全的期刊投稿 skill 集合，而且是唯一一个**能真正把实证分析跑出来、
用真实工具运行结果做证据**的仓库。

**基线（2026-07-01）**：195 个 first-party pack · 2902 个 skill · 平均分 93.6 ·
最低分 90.0 · 执行桥接通 131/134 实证 depth pack (98%) · CI 硬门槛全绿。

**总原则**（沿用既有纪律）：
- 质量优先于数量：不为凑数新增 pack；每一分提升都要过 `tools/run_checks.py` 硬门槛。
- 证据优先于声称：实证能力必须以真实工具运行结果（StatsPAI / Stata MCP）为证。
- 事实纪律：一切 live facts（费用、字数限制、政策）只来自各 pack 的
  `resources/official-source-map.md`，禁止编造。
- 克隆纪律：新增 prose 必须 venue-specific，`clone_audit.py --threshold 0.75` 零命中。

---

## Week 1（07-01 ~ 07-07）：质量尾部清零 + 门槛加固

- [x] 尾部提升（2026-07-01 完成，共两波 16 个 pack）：第一波 12 个 90.0–91.4 分
      pack（Cancer-Cell、Annals-of-Mathematics、PRL、JACS、Cell、
      Economic-Research-Journal、Conservation-Biology、NEJM、Critical-Inquiry、
      Mind、PMLA、Games-and-Economic-Behavior）→ 92.0–94.0；第二波 4 个新暴露
      尾部（财经研究、APSR、JAE、JIBS 91.6–91.9）→ 93.6–94.0。
- [x] 执行桥补齐（2026-07-01）：AOM-Annals / Annual-Review-of-Economics /
      Social-Sciences-in-China 接入执行手册，达成 134/134 (100%)。
- [x] CI 加固（2026-07-01）：weekly cron 触发 + 外链审计 advisory job 已上线。
- [x] 验收（2026-07-01）：`run_checks.py --skip-reports` 全绿；
      scorecard min 92.0、mean 93.8（mean ≥94 留待 Week 2-3 随 showcase 与
      次尾部深化自然达成）；克隆审计 0.75 阈值零命中。
- 附注：Week 2 的 showcase 已提前开种——首条 SCM 案例（加州 Prop 99）已用真实
  StatsPAI 运行落库（`showcase/scm-california-prop99/`），中英 README 首屏已挂入口。

## Week 2（07-08 ~ 07-14）：自动实证证据链（核心差异化）

- [x] `showcase/` 目录（2026-07-02 完成）：5 条端到端案例全部为真实 StatsPAI MCP
      运行——SCM 加州禁烟（−18.19，三估计量一致）、交错 DiD Castle Doctrine
      （+0.110，Honest DiD 过关）、IV Card 大学距离（0.132，AR/CLR/tF 弱 IV 面板）、
      RDD 差额胜选（43.85，密度检验+安慰剂断点）、DML 教育回报（0.074，
      含「函数形式 vs 内生性」方法边界示范）。数据全部为公开基准
      （Abadie 面板 + Mixtape 复现数据）。
- [x] 每条案例反向链接执行手册与 reviewer checklist；中英 README 首屏入口已挂
      （2026-07-01）。
- [x] 把 showcase 纳入 `audit_repo.py` 清点（2026-07-02 完成）：
      `EXPECTED_SHOWCASE_CASES=5` 硬门槛，检查索引链接、逐案例 README、
      运行日期与运行备注证据标记。
- 附注：运行中累计发现 7 处 StatsPAI 上游缺陷（synth_time_placebo/synth_loo
  年份类型强转、aggte/pretrends_test/dml_sensitivity 句柄不解析、
  anderson_rubin_test 空载荷、rdplacebo 连接崩溃、list_replications 格式化错误），
  已在各案例「运行备注」如实记录——回传修复排入 StatsPAI 仓库的工作队列。

## Week 3（07-15 ~ 07-21）：可发现性 + 中英对齐

- [x] README.en.md 与 README.md 逐节 parity 审计（2026-07-02 完成）：38 个标题
      1:1 对应；双语新增 showcase 正文小节（五案例 + 数字表）；修复两处陈旧
      193→195 计数。
- [x] venue 索引挂双语首屏导航（185 刊机读表）；生成器修复为确定性输出
      （排除 Toolkit pack）；GitHub topics 换入 causal-inference /
      empirical-research / econometrics / replication（20 上限内置换）。
- [x] gallery / 封面墙检查（2026-07-02）：README 引用的 406 个本地图片全部存在
      （git 索引大小写精确校验），13 个 SVG rsvg-convert 渲染到真实文件全部通过，
      393 个 PNG/JPG 文件头正常，零修复。
- [x] v1.0.0 已发布（2026-07-02）：annotated tag + 双语 release notes，
      https://github.com/brycewang-stanford/Awesome-Journal-Skills/releases/tag/v1.0.0

## Week 4（07-22 ~ 07-31）：外部对标 + 社区漏斗 + 总验收

- [ ] 对标文档：与 claude-scholar、codex-claude-academic-skills 等同类仓库的
      能力矩阵对比（覆盖面、执行能力、质检体系、双语），只写可验证事实。
- [ ] 社区漏斗：issue 模板（新期刊申请 / 事实纠错 / skill 缺陷）、
      CONTRIBUTING 增补「一个新 pack 的最小验收线」。
- [ ] 总验收 sweep：全部硬检查 + scorecard 分布 + 外链审计 + 中英 parity，
      结果记入 `.maintenance/ACCEPTANCE-2026-07.md`。

---

## 验收指标（月底）

| 指标 | 基线 | 目标 |
|---|---|---|
| scorecard 最低分 | 90.0 | ≥ 92 |
| scorecard 平均分 | 93.6 | ≥ 94 |
| 执行桥覆盖（实证 depth） | 131/134 | 134/134 |
| 真实运行的端到端 showcase | 0 条独立入口 | ≥ 5 条 |
| CI 触发 | push/PR | push/PR + weekly |
| 中英 README parity | 未审计 | 逐节对齐 |
| release | 无 tag | v1.0 |

进度与决策记录在本文件追加，不另开 worklog。
