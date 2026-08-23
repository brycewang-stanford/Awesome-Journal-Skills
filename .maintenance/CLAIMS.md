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

- **工具层可靠性 lane**（2026-08-23）：给 `tools/` 补上单元测试（此前只有
  `py_compile`），并修掉测试过程中暴露的四个缺陷——被 bot 验证页覆盖的
  `assets/banner-en.png`、把 API 拒答当成"该论文没有摘要"的
  `fetch_abstracts.py`、饱和到只剩 freshness 的 `quality_scorecard.py`、
  以及 `venue_lib.DISC` 里七条永远不会命中的学科规则。另有一处纯度量改进：
  检索索引深度 300→900（held-out R@10 41.5%→46.7%）；补齐摘要语料后 `title+abstract` 配置首次可报（729 条 term bag，R@10 54.9%）。触碰面：`tools/`（新增
  `tools/tests/`）、`shared-resources/journal-selection/` 生成物、
  `CONTRIBUTING.md`、`CHANGELOG.md`、两份根 README 的召回数字、
  `.maintenance/QUALITY-LANE-2026-09.md`。**不触碰任何 pack 内容。**

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
| 《系统工程学报》depth pack | Codex | done (2026-07-30) | 12-skill depth pack + root entry；合并进 main 时计数重算为 4166 skills / 300 packs / 201 root entries / 744 venues；质量分 94.0 |
| 工具层可靠性 + 检索深度 | Claude | done (2026-08-23) | 242 个离线单测接入 `run_checks` 首位；scorecard 拆成 conformance 硬门槛 + backlog 排序；`KEYWORD_DEPTH` 300→900；8 个 venue 学科重分类。全套硬检查通过。 |
| ROADMAP-2026-08 全量执行 | Claude (owner) | done (2026-07-08) | 四周工作流 + 多轮增补全部完成：质量满分收尾、Wave 25-A 24/24 + 两个 EN core-61 梯队（共 40 会议深度包）、清欠、治理、banner、PR #6/#7 合并；终态 229 pack / 3310 skill |

## 常设规则

- 质量门槛见 `CONTRIBUTING.md`（新 pack 最小验收线 + bundle 复用规则）。
- 一切 live facts 只来自各 pack `resources/official-source-map.md`，禁止编造。
- 新增 prose 必须 venue-specific：`python3 tools/clone_audit.py --threshold 0.75
  --fail-threshold 0.90` 零命中。
- 计数变更（skill/pack）必须与 `tools/audit_repo.py` 与两份根 README 同 commit 对账。
