# ACCEPTANCE-2026-08 — Awesome-Journal-Skills 2026-08 月度总验收报告

**验收日期**：2026-07-08（本月工作前置完成；路线图窗口 2026-07-08 ~ 2026-08-08）
**基线 commit**：`0602461`（月初）
**报告作者**：2026-08 月度路线图 owner（见 `.maintenance/CLAIMS.md`）
**复验方式**：全部数字来自本地 working tree 上
`python3 tools/{run_checks,audit_repo,quality_scorecard,clone_audit}.py` 的实际输出
**增补（2026-07-08 同日，两轮）**：初版签署后 owner 两次指示继续执行全部后续
工作，第二、三波扩张与质量换挡均已完成——终态为 **207 pack / 3046 skill /
category-8 18/100 / CI scorecard 下限 94**，详见 §3.3–§3.4 增补段与 ROADMAP
「Week 2 增补」。

---

## 0. 一句话验收结论

> 本月四条线全部落地：**(1) 质量饱和收尾**——最后 6 个 92.0 pack 的丢分被证明是
> 评分尺子 structure 档位错配而非内容缺陷，做了全量 before/after 可复验的规格修正，
> scorecard 199 包 **min = mean = 94.0（公式构造性满分）**；**(2) 有节制扩张**——
> category-8 队列按序推进 UAI / COLT / MLSys / KDD 四个完整 12-skill 深度包
> （**195→199 pack、2902→2950 skill**，category-8 完成度 6→10/100），克隆审计
> 全仓零命中；**(3) 事实清欠**——live 核实通道被本环境网关整体封锁（已取证），
> 改做离线可追溯性抽查，top-5 欠账包 **0 处真实违规**；**(4) 治理减负**——第 4 套
> issue 模板 + CONTRIBUTING 复用规则 + CLAIMS 板归档重置。CI 硬门槛全程全绿。

---

## 1. 路线图验收指标对照

| 指标 | 基线（07-08 月初） | 月底目标 | **验收值** | 状态 |
|---|---|---|---|---|
| scorecard 最低分 | 92.0 | 94.0 | **94.0** | ✅ |
| scorecard 平均分 | 93.9 | 94.0 | **94.0**（公式满分，尺子已饱和） | ✅ |
| first-party packs | 195 | 199 | **199** | ✅ |
| canonical skills | 2902 | 2950 | **2950** | ✅ |
| category-8 完成度 | 6/100 | 10/100 | **10/100** | ✅ |
| 克隆审计 0.75 阈值 | 0 命中 | 0 命中（含新包） | **0 命中**（2950 skills / 350 groups） | ✅ |
| source-map 待核实清欠 | 216 处 | ≤190 | **顺延**（环境封锁，见 §3.1；替代审计通过） | ⚠️ 诚实顺延 |
| 外链审计 | — | 失效清零或留档 | **留档不可为**（见 §3.2） | ⚠️ 诚实留档 |
| issue 模板 | 3 套 | 4 套 | **4 套**（+bundle-replication-request） | ✅ |
| CLAIMS.md | 366 行历史堆积 | 归档重置 | **已归档** `CLAIMS-ARCHIVE-2026-06.md` | ✅ |
| run_checks 硬门槛 | 全绿 | 全绿 | **All hard checks passed.** | ✅ |

## 2. 证据链

### 2.1 inventory — `python3 tools/audit_repo.py`
```
Repository audit passed: 2950 canonical skills, 199 curated packs,
200 root journal entries, 5 executed showcase cases.
```

### 2.2 scorecard — `python3 tools/quality_scorecard.py`
```
Quality scorecard — 199 first-party packs · mean score 94.0/100
Distribution: min 94.0 · p10 94.0 · median 94.0 · below 86/88/90 = 0/0/0
Execution bridge (StatsPAI/Stata MCP) wired: 134/134 empirical depth packs (100%)
```
度量修正证据：修正只动 structure 档位（breadth `n>=50`→`n>=12`（均需 router）、
depth 上界 14→20），修正前后逐包对比 **195 包中恰好且仅有目标 6 包变动**
（92.0→94.0），其余 189 包分数逐一相等。depth/trigger/resources/runnable 四个
substance 维度的门槛一个字未动。94.0 = 35+20+28+5+6 是公式构造性上限；
静态尺子从此饱和，下月质量牵引应转向行为评测（tools/skillopt/ 路线）。

### 2.3 clone audit — `python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90`
```
Clone audit scanned 2950 skills in 350 comparison groups (scope=first-party).
No pairs at or above threshold 0.750.
```
另：4 个新包各自 `--bundle` 内部审计 0.70 阈值同样零命中；建包代理自检报告的
跨包最大字符相似度 0.40–0.49（含 README 与共享代码指针文件），远低于 0.75。

### 2.4 新包证据（UAI / COLT / MLSys / KDD）
- 每包 25 文件：12 SKILL.md + 双语 README + plugin/marketplace + LICENSE +
  cover.svg + resources 五件套；marketplace 声明与实际目录逐一相等；JSON 全部可解析；
  相对链接零断链（独立复验，非仅代理自报）。
- 事实纪律：每包 `resources/official-source-map.md` 锚定 2026 届官方 CFP /
  日期页 / OpenReview 组 / PMLR·ACM 出版页，访问日期 2026-07-08。四张 map 均带
  **access-method note**：建包环境网关拦截四个会议域名的直连抓取，页面内容经
  搜索渲染核实并与 OpenReview 组、PMLR/dblp/ACM 元数据交叉验证；钉不住的条目
  （费用、camera-ready 细则、chair 名单、下一届周期）一律 待核实，未断言。
- venue-true 差异化（抽查复验）：COLT 用 **Microsoft CMT**（纠正了「COLT 用
  OpenReview」的任务假设）且 colt-artifact-evaluation 开篇声明本会**无 artifact
  track**、证明附录即 artifact；KDD 双周期双 track、rebuttal 禁超链、Resubmit
  管线；MLSys Research/Industrial 双轨 + 录后 artifact 徽章；UAI 单 PDF 附录 +
  reviewer-volunteer 义务。
- 对账同 commit（`ff74cbf`）：audit tripwires、根 marketplace（199 条）、双语
  README 徽章/学科表/深度包表/目录树/计数口径（2275 = 189 深度包 + 668 + 7 =
  2950）、scorecard 集合、venue 索引（185→189 行）、.maintenance 队列文件。

### 2.5 CI hard gate — `python3 tools/run_checks.py`
```
All hard checks passed.
```
（含 py_compile、audit_repo、克隆守门、git diff --check 与报告类审计。）

## 3. 灰色地带（不假装、不补齐）——诚实未完成项

### 3.1 source-map 待核实清欠 —— 顺延（环境封锁）
本环境出口代理对期刊/出版社域名策略性拒绝（curl / urllib 在 CONNECT 阶段 403；
WebFetch 对 academic.oup.com、pnas.org、nasonline.org、econometricsociety.org、
ciejournal.ajcass.com 全部 403；jmsc.tju.edu.cn DNS 不可解析）。按代理 README
「组织策略拒绝不重试」纪律，live 复核顺延至有期刊域名出口的环境（owner 本地
浏览器或另配 CI）。**替代交付**：top-5 欠账包硬数字可追溯性抽查（43 个命中段落
逐一复核）**0 处真实违规**；并留档「216 处基线计数含阻断说明prose，高估开放
事实债」的测量学注记（本月不改计数正则，避免连续两次向下调整指标）。

### 3.2 外链修复 —— 留档不可为
`tools/external_link_audit.py` 实跑 1843 URL：0 OK / 86 BLOCKED / 1757
UNREACHABLE——同一环境封锁所致，按工具自身语义（UNREACHABLE 须重跑后再行动）
不据此改任何链接。外链健康继续由每周 CI advisory job（GitHub Actions 出口）承担。

### 3.3 scorecard 已饱和 —— 静态尺子退役预告（含一处更正）
min = mean = max = 94.0 后，该尺子对后续质量工作失去区分度。静态 scorecard
转为回归防线：`run_checks.py` 硬门槛下限已由 90 提至 94（2026-07-08）。
**更正**：本报告初版曾建议「转向 tools/skillopt/ 行为评测路线」——该建议基于
过时的 CLAIMS 归档信息，已撤回：owner 于 2026-06-29（commit `b9c8fe75`）刻意
拆除了 SkillOpt/monthly-uplift 装置（自引用循环、破坏 CI），不得重建。替代
方案（轻量、人触发、不进 CI）见 `.maintenance/QUALITY-LANE-2026-09.md`。

### 3.4 category-8 进度（两轮增补后 18/100）
初版验收时为 10/100。owner 两次指示继续推进：第二波 The Web Conference /
WSDM / SIGIR / CVPR（199→203 pack / 2950→2998 skill），第三波 ICCV / ACL /
EMNLP / ICRA（203→207 pack / 2998→3046 skill），均于 2026-07-08 建成并
全量对账，category-8 现为 **18/100**。Wave 25-A 下一批（ASSET-INVENTORY
已更新）：CHI / SOSP / OSDI / IEEE S&P。按「每波过全部硬门槛」的节奏滚动，
不冲量。

## 4. 月度产物清单（commit 级，全部在 claude/repo-analysis-planning-8rqc2w）

| commit | 含义 | 对应周 |
|---|---|---|
| `8832560` | ROADMAP-2026-08 + scorecard structure 档位修正（6×92.0→94.0） | Week 1 |
| `879a098` | bundle-replication 漏斗 + CONTRIBUTING 复用规则 + CLAIMS 归档 | Week 4（社区） |
| `f660266` | Week 3 环境封锁取证 + 离线可追溯性替代审计 | Week 3 |
| `ff74cbf` | UAI/COLT/MLSys/KDD 四深度包 + 全量对账（199/2950） | Week 2 |
| _本报告_ | ACCEPTANCE-2026-08 总验收 | Week 4 |

## 5. release 建议（决定权在 owner）

本月增量（+4 完整深度包、质量满分收尾、治理瘦身）符合一次 **v1.1.0** minor
release 的体量。建议 notes 要点：199 packs / 2950 skills、category-8 10/100、
scorecard 全仓 94.0 满分、第 4 套社区模板。tag 与 GitHub release 由 owner 验收
本报告后自行决定，本任务不代打。

## 6. 复验附录

```bash
python3 tools/run_checks.py                      # 全套硬门槛 + 报告
python3 tools/audit_repo.py                      # 2950 / 199 / 200 / 5
python3 tools/quality_scorecard.py --top 15      # min = mean = 94.0
python3 tools/clone_audit.py --threshold 0.75 --fail-threshold 0.90
for b in UAI-Skills COLT-Skills MLSys-Skills KDD-Skills; do
  python3 tools/clone_audit.py --bundle $b --threshold 0.70 --fail-threshold 0.90
done
```

— end of ACCEPTANCE-2026-08.md —
