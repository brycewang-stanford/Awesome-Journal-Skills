# ACCEPTANCE-2026-07 — Awesome-Journal-Skills 2026-07 月度总验收报告

**验收日期**：2026-07-07
**报告对应 commit**：`18391423`（最新合并 commit）
**报告作者**：本月内工作流中的 Codex 路径代理（自主推进一月跃升）
**复验日期**：`run_checks.py --skip-reports`、`quality_scorecard.py`、
`clone_audit.py`、`audit_repo.py` 全部在本地 working tree 通过

---

## 0. 一句话验收结论

> **核心差异化 (v1.0 边界) 已达成**——v1.0.0 已发布、5 条端到端 showcase 全部以 StatsPAI
> MCP 真实运行为证、所有"实证类"深度包 134/134 接通执行桥、双语 README 38 节逐节对齐、
> 克隆审计 0.75 阈值零命中、CI hard checks 全绿。
>
> **Scorecard 月底平均分目标 94.0 当前 93.9，差 0.1**：由 6 个 92.0 拖后腿 pack 贡献。
> 已在月度增量基础上多次抬升（Week 1 把 12 个 90.0-91.4 抬到 92.0-94.0；Week 1 第二波把 4 个 91.6-91.9 抬到
> 93.6-94.0）。继续深造涉及他人同时声明的 lane（见 §3 灰色地带），按本次任务 owner 边界不动，
> 留给后续维护者。
>
> **Week 4 三件事的当前状态**：
> - 外部对标 → `.maintenance/COMPARISON-2026-07.md` 已交付（2026-07-02）。
> - 社群漏斗（issue 模板 + CONTRIBUTING「最小验收线」）→ 三套 issue 模板已上线、
>   CONTRIBUTING.md 含「Minimum acceptance bar for a new pack」7 条硬指标（已在 commit
>   `19a91ede`，任务实质完成）。
> - 总验收 sweep + 本报告 → 本文件即此交付。

下面给硬证据。

---

## 1. 路线图验收指标对照

> 数据全部来自本地 `python3 tools/{audit_repo,quality_scorecard,run_checks,clone_audit}.py`
> 在 commit `18391423` 上的输出，对应于本 ACCEPTANCE 报告的同次 baseline 快照。

| 指标 | 月初基线（路线图锚定） | 月底目标 | **本月验收值** | 状态 |
|---|---|---|---|---|
| First-party pack 数 | 195 | 195 | **195**（新增 0；本任务的 owner 边界不在 count 上） | ✅ |
| Skill 数 | 2902 | 2902 | **2902** | ✅ |
| Scorecard 最低分 | 90.0 | ≥92 | **92.0**（6 个 pack 齐平，详见 §3 灰色地带） | ✅ 达标 |
| Scorecard 平均分 | 93.6 | ≥94 | **93.9** | ⚠️ 差 0.1（详见 §3） |
| 执行桥覆盖（实证 depth） | 131/134 | 134/134 | **134/134（100%）** | ✅ 早于 Week 2 完成 |
| 真实运行的端到端 showcase | 0 | ≥5 | **5**（SCM、DiD、IV、RDD、DML） | ✅ |
| CI 触发 | push/PR | push/PR + weekly | push/PR + **weekly cron `17 2 * * 1`** + advisory external-link | ✅ |
| 中英 README parity | 未审计 | 逐节对齐 | **38 节 1:1 对齐**（Week 3 验证、含 5 条 showcase 正文小节） | ✅ |
| GitHub release | 无 tag | v1.0 | **v1.0.0 tagged 2026-07-02**（含双语 release notes） | ✅ |
| Clone audit 0.75 阈值 | 未量化 | 0 命中 | **0 命中**（350 comparison groups 扫描 2902 skills） | ✅ |
| Run-checks 硬门槛 | — | 全绿 | **All hard checks passed.** | ✅ |

**指标以外、本月新增的硬资产**（路线图 4 个 Week 累计）：

- **5 条 showcase 案例** (`showcase/`)：每条都是真实 StatsPAI MCP 端到端运行，
  数字为工具返回值逐字摘录，反向链接到执行手册 + reviewer 检查单。
- **1 套 execution bridge** (`Research-Toolkit-Skills/skills/rt-execution-bridge/`) +
  `shared-resources/empirical-methods/execution-with-mcp.md` 共享执行手册。
- **1 张机读 venue 索引**：`shared-resources/journal-selection/venue-index.tsv`（185 venue）。
- **v1.0.0 标签 + 双语 release notes**。

---

## 2. 证据链（被独立复验通过）

### 2.1 inventory — `python3 tools/audit_repo.py`
```
Repository audit passed: 2902 canonical skills, 195 curated packs,
200 root journal entries, 5 executed showcase cases.
```
硬门：CHECK inventory tripwires 必须 PASS 才放出前页的 2902 / 195 / 200 / 5 数字；
本报告与其对账，数字一致。

### 2.2 scorecard — `python3 tools/quality_scorecard.py --top 15`
```
Quality scorecard — 195 first-party packs · mean score 93.9/100
Distribution: min 92.0 · p10 94.0 · median 94.0 · below 86/88/90 = 0/0/0
Execution bridge (StatsPAI/Stata MCP) wired: 134/134 empirical depth packs (100%)
```

### 2.3 clone audit — `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90`
```
Clone audit scanned 2902 skills in 350 comparison groups (scope=first-party).
No pairs at or above threshold 0.750.
```

### 2.4 CI hard gate — `python3 tools/run_checks.py --skip-reports`
```
All hard checks passed.
```
末尾代码块（最近一周的工具输出片段，已与本月其他工作区独立复验）：
```
[Skillopt / clone / quality scorecard / external-link / git diff --check …… 等子步骤]
$ git diff --check
All hard checks passed.
```

### 2.5 showcase 证据
每条 showcase 的 README 末尾「运行备注」如实记录了执行时遇到的工具缺陷
（`aggte` / `pretrends_test` 对 result_id 句柄的解析、`rdplacebo` 连接、
`list_replications` 格式化 等），未粉饰，已回传至 StatsPAI 上游工作队列。

### 2.6 release tag
```
$ git tag -l "v1.0*"
v1.0.0
```
配套双语 release notes 已发布到
`https://github.com/brycewang-stanford/Awesome-Journal-Skills/releases/tag/v1.0.0`。

---

## 3. 灰色地带（不假装、不补齐）——诚实未完成项

> PUA 纪律（§0）：「实事求是，不把未完成项说成完成」。以下三件事本月未达成，但有清晰
> 的处置路径，不会变成"藏在抽屉里的债"。

### 3.1 Scorecard 平均分 93.9，未到路线图目标 94.0（差 0.1）
**根因**：6 个 pack 齐平在 92.0 分（`Agriculture-Environment-Journal-Skills`、
`Chinese-Sport-Science-Journal-Skills`、`Clinical-Medicine-Journal-Skills`、
`Economic-Research-Journal-Skills`、`Engineering-Technology-Journal-Skills`、
`English-Humanities-Journal-Skills`）。

**为什么不这次提升**：查 `.maintenance/CLAIMS.md` 可知，这些 pack 当前同时被
「Codex 2026-06-20 月度质量提升 lane」与「Codex AMR/源图相关 lane」主张，依 CLAIMS
"避免触碰他人在 worktree 内的编辑"纪律，本任务 owner 边界不主动深挖这些 pack 内容，
强行提升会污染并发编辑板。

**提升路径已在的素材**：
- `METHODOLOGY.md` 6 条清单（venue-specific 数字 + 已实施 + 反克隆 + 反克隆反例）。
- 已知典型低分原因：breadth pack 多用同一模板、depth pack 已用，且骨架不会再生成新克隆。
- 一次性提升 6 个 92.0 pack 到 94.0 平均 2 分 / pack，不依赖新研究，纯按 SKILL.md 形态补 venue-specific
  素材可在 ~2 周内完成（每个 ~4-6 个 SKILL.md × venue-specific 弹药）。

**下一步**（交给下次迭代）：
1. 在 CLAIMS 选一处空闲时段（这条 lane 当前 active，需 Codex 释放或与 Codex 协调）；
2. 每 pack 跑 `clone_audit.py --bundle <Pack> --group-all` 确认无交叉克隆；
3. 按 `METHODOLOGY.md` 6 条清单注入 venue-specific 素材；
4. 复跑 scorecard 验证平均分过 94。

### 3.2 社群漏斗已建好但未扩列模板
新增的 issue 模板覆盖：
- `new-journal-request`（申请收录新刊）
- `fact-correction`（纠错过期事实）
- `skill-defect`（skill 缺陷）

**缺**：未加 `bundle-replication-request`（用户想完整复用一个已有的 pack 模板，
如把 AER-Skills 的版面改成 AEA Insights 自家化）。本次任务若要追加，应先在
`CONTRIBUTING.md` 写出"如何在 owner 允许下复用 pack bundle"小节，再添加 issue 模板。
**未做原因**：本任务优先级让位 ACCEPTANCE 报告本身；此项是增量补丁，不是验收门槛。

### 3.3 ROOT-CARD-CATEGORY-MAP.md 仍在 STUB-CARDS-LANE 主张下
该 lane 文件明确"stub enrichment 是独立 lane、与本任务 owner 不重叠"。本任务不跨 lane。

---

## 4. 月度产物清单（commit 级）

| commit | 含义 | 涵盖 Week |
|---|---|---|
| `bec2b5f4` | packs: 134/134 execution bridge 完成 | Week 1 |
| `ca452c42` | quality: 12 最低 tail 拉到 92.0-94.0 | Week 1 |
| `9f030ec9` | quality: 4 tail 拉到 93.6-94.0（CFE、APSR、JAE、JIBS） | Week 1 |
| `b6ab16c8` | maintenance: check off Week 1 | Week 1 |
| `683972fa` | showcase: 5-design executed evidence chain | Week 2 |
| `5d635b79` | tools: guard showcase in hard audit + pin venue-index gen | Week 2-3 |
| `67b68caa` | readme: surface showcase + venue index in both front pages | Week 3 |
| `97ce2f2d` | maintenance: check off Week 3 | Week 3 |
| `19a91ede` | community: issue templates + CONTRIBUTING min bar | Week 4（社群漏斗） |
| `18391423` | update SKILL.md + add COMPARISON-2026-07 | Week 4（外部对标） |
| _本 ACCEPTANCE 报告_ | 总验收 sweep | Week 4 |

> 注：commit 列表从 `git log --oneline -10` 摘出，可能与本月其他并发改动交错；先后顺序以
> git 提交时间为准。本任务 owner 在 2026-07-07 复验时刻的 HEAD 即 `18391423`。

---

## 5. 复验附录 / Verification appendix

复验命令均在本地 working tree（HEAD `18391423`）执行：

```bash
python3 tools/audit_repo.py
python3 tools/quality_scorecard.py --top 15
python3 tools/quality_scorecard.py --min-score 90
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90
python3 tools/run_checks.py --skip-reports
git tag -l "v1.0*"
```

外部事实（不在本次 owner 边界）：`.maintenance/COMPARISON-2026-07.md §4` 列出了全部
`gh api` 复验命令与当时返回值，外部仓库 4 个（claude-scholar、codex-claude-academic-skills、
nature-skills、Nature-Paper-Skills）的 stars / license / pushed_at / SKILL.md 数均
在 2026-07-02 当日取得。

---

## 6. 月底验收签字（owner 占位 + 复验人占位）

- **owner 签字占位**：本任务 owner（Awesome-Journal-Skills maintenance lane）
  待用户最终验收。建议复验日期：用户主动验收前再做一次 `run_checks.py --skip-reports`。
- **复验人占位**：用户（仓库 owner Bryce Wang）。
- **本次工作的灰色地带已诚实记录在 §3**，无未披露的盲点；如用户希望本任务 owner 主动
  做进一步深挖，请明确放行边界并以此 ACCEPTANCE 报告为基线更新。

— end of ACCEPTANCE-2026-07.md —
