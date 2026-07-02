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

- [ ] 尾部提升：12 个 90.0–91.4 分 pack（Cancer-Cell、Annals-of-Mathematics、PRL、
      JACS、Cell、Economic-Research-Journal、Conservation-Biology、NEJM、
      Critical-Inquiry、Mind、PMLA、Games-and-Economic-Behavior）的最薄 skills
      深化到 ≥600 substance units/skill，目标全仓库最低分 ≥92。
- [ ] 执行桥补齐：Academy-of-Management-Annals / Annual-Review-of-Economics /
      Social-Sciences-in-China 三个实证 depth pack 接入
      `shared-resources/empirical-methods/execution-with-mcp.md`，达成 134/134 (100%)。
- [ ] CI 加固：`repo-audit.yml` 增加 weekly schedule 触发 + 外链审计 advisory job
      （非阻塞，产出报告），防止内容悄然过期。
- [ ] 验收：`run_checks.py --skip-reports` 全绿；scorecard min ≥92、mean ≥94。

## Week 2（07-08 ~ 07-14）：自动实证证据链（核心差异化）

- [ ] `showcase/` 目录：5 条端到端案例（DiD-Callaway–Sant'Anna、IV-弱工具稳健、
      RDD-rdrobust、SCM-加州禁烟、DML），每条从研究问题 → detect_design →
      preflight/recommend → 估计 → audit_result 稳健性 → 论文级表格，
      全部为**真实 StatsPAI MCP 运行输出**（含 result 数字与审计清单），非伪代码。
- [ ] 每条案例反向链接到使用它的 pack 与 `Research-Toolkit-Skills` 的
      `rt-execution-bridge`，README 首屏加「看得见的自动实证」入口。
- [ ] 把 showcase 纳入 `audit_repo.py` 清点（tripwire 更新）。

## Week 3（07-15 ~ 07-21）：可发现性 + 中英对齐

- [ ] README.en.md 与 README.md 逐节 parity 审计（结构、计数、新增 showcase 入口）。
- [ ] `gen_venue_index.py` 产出的 venue 索引挂到 README 首屏；GitHub topics、
      badges（CI 状态、pack 数、skill 数）补齐。
- [ ] gallery / 封面墙检查：所有 SVG 可渲染（rsvg-convert 渲染到真实文件验证）。
- [ ] 打 v1.0 release tag + release notes（中英双语）。

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
