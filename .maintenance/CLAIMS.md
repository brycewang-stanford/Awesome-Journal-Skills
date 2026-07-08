# Maintenance Claims Board (multi-agent coordination)

> Claim a lane here before editing, and **check `git status` + this file before
> starting any pack.** Commit with targeted `git add <path>` (never `git add -A`)
> so concurrent work is preserved. Do not edit git submodules
> (AER-skills, nature-skills, nature-paper-skills, claude-scholar,
> codex-claude-academic-skills).

历史沿革：2026-06 多代理并发建设期的全部 lane 记录（Agent A/B/C/D/E、Codex、
Claude SkillOpt、W1/W2 workflow 波次）已完成并归档至
`.maintenance/CLAIMS-ARCHIVE-2026-06.md`。本板只保留当前活跃 lane。

## Active lanes

- **2026-08 月度路线图 owner**（started 2026-07-08）：执行
  `.maintenance/ROADMAP-2026-08.md` 四周工作流——scorecard structure 档位修正、
  category-8 扩张波（UAI / COLT / MLSys / KDD 4 个新深度包 + 计数对账）、
  source-map 待核实清欠（top-5 包）、外链修复、社区模板与本板归档、
  ACCEPTANCE-2026-08 总验收。触碰面：4 个新 pack 目录、`tools/quality_scorecard.py`
  structure 档位、`tools/audit_repo.py` 计数、根 README 徽章/表格、
  top-5 source map、`.github/ISSUE_TEMPLATE/`、`CONTRIBUTING.md`、`.maintenance/`。

## Claim log

| Lane / Pack | Agent | Status | Notes |
|------|-------|--------|-------|
| ROADMAP-2026-08 全量执行 | Claude (owner) | in progress | 见上方 Active lanes 触碰面清单 |

## 常设规则

- 质量门槛见 `CONTRIBUTING.md`（新 pack 最小验收线 + bundle 复用规则）。
- 一切 live facts 只来自各 pack `resources/official-source-map.md`，禁止编造。
- 新增 prose 必须 venue-specific：`python3 tools/clone_audit.py --threshold 0.75
  --fail-threshold 0.90` 零命中。
- 计数变更（skill/pack）必须与 `tools/audit_repo.py` 与两份根 README 同 commit 对账。
