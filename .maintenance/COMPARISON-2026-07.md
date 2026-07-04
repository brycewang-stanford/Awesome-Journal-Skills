# COMPARISON-2026-07 — 与同类学术 Skills 仓库的能力对比

> 检索日期（retrieval date）：**2026-07-02**。所有外部事实均在当日通过 `gh api`（GitHub REST API）
> 取得；本仓库事实来自本地 working tree（HEAD `19a91ede`）与既有审计工具输出。
> 每个单元格都可复验（复验命令见文末附录）；无法确认的写 **未验证 / not verified**，不做推断。
> 对比对象取自本仓库 README.md「第三方收录（外链）」区块（L386、L1180–L1188）：
> [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)、
> [codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills)、
> Nature 系两个仓库 [nature-skills](https://github.com/Yuan1z0825/nature-skills) 与
> [Nature-Paper-Skills](https://github.com/Boom5426/Nature-Paper-Skills)。

---

## 1. 一句话定位 / One-line positioning

| 仓库 | 一句话定位 |
|------|-----------|
| **Awesome-Journal-Skills**（本仓库） | 按刊建包：519 本期刊 + 155 个 CS/AI venue，每个重点期刊一个 12 技能深度包，配执行桥与已执行证据。<br>*Per-venue packs: 519 journals + 155 CS/AI venues, one 12-skill depth pack per flagship, with execution bridges and committed run evidence.* |
| **claude-scholar** | 跨期刊的半自动科研助手插件：从选题、写代码、跑实验到写作发表的通用工作流，支持 Claude Code / Codex / Kimi / OpenCode。<br>*Venue-agnostic research-assistant plugin: ideation-to-publication workflow across four CLI agents.* |
| **codex-claude-academic-skills** | 面向中文科研用户的 3 个大颗粒 skill：Office 学术文档、论文写作润色、MATLAB/Python 科学计算工具箱。<br>*Three coarse-grained skills for Chinese researchers: academic Office docs, paper writing, scientific computing toolkit.* |
| **nature-skills** | Nature 风格学术表达与科研绘图的通用 skill 集（15 个 nature-\* 技能 + 自带学术检索 MCP server）。<br>*Nature-style academic-expression and figure skills (15 nature-\* skills plus a bundled academic-search MCP server).* |
| **Nature-Paper-Skills** | Nature 系手稿全周期 skill 包：起草、修改、审计、rebuttal、重投，claim-driven 工作流。<br>*Nature-series manuscript lifecycle skills: draft, revise, audit, rebuttal, resubmit.* |

---

## 2. 能力矩阵 / Capability matrix

所有外部数字为 2026-07-02 `gh api` 快照；四个对方仓库的 git tree 均 `truncated: false`（SKILL.md 计数完整，无截断）。

| 维度 | **Awesome-Journal-Skills** | claude-scholar<br>(Galaxy-Dawn) | codex-claude-academic-skills<br>(zLanqing) | nature-skills<br>(Yuan1z0825) | Nature-Paper-Skills<br>(Boom5426) |
|------|---------------------------|--------------------------------|--------------------------------------------|-------------------------------|-----------------------------------|
| **Venue 覆盖** | 519 本期刊 + 155 个 CS/AI venue（README 收录范围声明 + `tools/audit_repo.py` inventory 校验） | 仅 Nature 系：4 个 nature-\* 技能（writing / polishing / response / data）；无按刊目录 | 0 个 venue 专属技能（三个 skill 均跨期刊通用） | Nature 系单一风格；15 个技能全部 nature-\* 前缀，为通用科研流程而非按刊区分 | 1 个 venue 技能（`skills/venue/nature-portfolio-playbook`）+ venue-routing 文档 |
| **SKILL.md 数** | 2,902（`tools/audit_repo.py` 口径） | 45 | 24（顶层 3 个；其余 21 个为 `scientific-toolkit-skill/references/` 下 vendored 的科学计算子技能） | 15 | 18 |
| **按刊深度** | 195 packs；重点刊每刊约 12 技能深度包（投稿流程、审稿文化、方法规范等） | 无按刊深度包 | 无 | 无（Nature 作为整体风格，非逐刊） | Nature portfolio 作为单一 playbook；无逐刊包 |
| **执行能力（可运行分析）** | 134/134 实证深度包内置 execution bridge（对接 StatsPAI MCP 等可运行分析） | 有 `mcp-integration` 技能 + 三语 `MCP_SETUP` 文档（教配置 MCP，非内置分析执行）；技能附示例 Python 脚本 | 无 MCP 引用；`scientific-toolkit-skill` 提供 MATLAB/Python 计算脚本（本地运行，非 MCP） | **自带 MCP server**（`nature-academic-search/mcp-server/`：arXiv / Crossref / PubMed / Scopus / ScienceDirect 检索源）；各技能附安装与辅助脚本 | 无 MCP 引用（tree 路径无 mcp；code search 1 次命中但抽取文件内容 grep 未复现）；技能附 Python 辅助脚本（`scan_citations.py` 等） |
| **已执行证据（committed run outputs）** | `showcase/` 5 个公开基准数据实证案例（DiD / IV / RDD / SCM / DML），含真实工具运行输出 | 未发现（`examples/` 为模板与配置示例） | 有少量：vendored `timesfm-forecasting/examples/anomaly-detection/output/anomaly_detection.json`（随上游参考内容带入） | 提交了示例图 PNG（`nature-figure/assets/figures4papers/`）——为成品图资产，非可复验的基准运行记录 | `examples/*.md` 为手写示例；`tests/` 含 1 个 pytest 文件；未发现真实运行输出 |
| **质量门 / CI** | `.github/workflows/repo-audit.yml`：push/PR 硬门（inventory tripwires、local-link audit、prose clone audit、showcase evidence markers）+ 每周日程运行（cron `17 2 * * 1`，外链 liveness 为 advisory） | 2 个 workflow：`installer_smoke.yml`（安装/卸载冒烟 + 文档存在性）、`repo_sanity.yml`（机器路径泄漏、junk 文件检查）——仓库卫生层面，不校验技能内容 | 无 `.github/workflows` | 无 `.github/workflows` | 无 `.github/workflows`（有 `tests/test_check_figure_refs.py`，但无 CI 执行它） |
| **双语** | ZH-EN 双首页（README.md / README.en.md），38 个 section 1:1 对齐 | **三语**：README 与 CLAUDE / MCP_SETUP / OBSIDIAN_SETUP 均有 en / zh-CN / ja-JP 版，且 CI 强制三语文档存在 | 仅中文 README（自我定位 Chinese-first） | 仅中文 README | 双语：README.md（中文）+ README.en.md |
| **质量评分体系** | `tools/quality_scorecard.py`：floor 92.0、mean 93.8，趋势 enforced | 未发现 | 未发现 | 未发现 | 未发现 |
| **机器可读索引** | `shared-resources/journal-selection/venue-index.tsv`：185 venue（186 行含表头，本地实测） | 未发现 | 未发现 | 未发现 | 未发现 |
| **License** | MIT（本地 LICENSE；GitHub API 亦返回 MIT） | MIT | MIT | Apache-2.0 | MIT |
| **Stars（2026-07-02）** | 584 | 4,474 | 1,345 | **25,214** | 339 |
| **最近 push（2026-07-02 快照）** | 2026-07-02（本地 HEAD `19a91ede` 2026-07-02） | 2026-07-02 | 2026-05-14 | 2026-07-01 | 2026-05-08 |
| **版本发布** | v1.0.0（本地 git tag 实测） | 未验证 | 未验证 | 未验证 | 未验证 |

口径说明：
- 「SKILL.md 数」按 git tree 中以 `SKILL.md` 结尾的路径计，包含 vendored/参考内容（对 codex-claude-academic-skills 影响最大，已单独注明拆分）。
- 「未发现」= 在完整 tree 路径列表中按关键词（workflow / scorecard / mcp / venue-index 等）检索无命中；「未验证」= 本次未检索该项。
- Stars 为快照值，随时间变化；对比时只应读趋势量级，不应读精确差值。

---

## 3. 诚实的对方优势（steelman）

不摆免责声明，逐仓库说对方确实做得比本仓库好的地方：

**claude-scholar**
1. **多 agent 平台适配是真的做了工程**：官方声明支持 Claude Code / Codex CLI / Kimi Code CLI / OpenCode，且 CI 有分支感知（`main` / `codex` / `opencode` 三分支触发）与安装/卸载冒烟测试。本仓库的插件形态目前以 Claude Code marketplace 为主，没有做等价的跨平台安装验证。
2. **三语文档且被 CI 强制**：en / zh-CN / ja-JP 三语 README + 配置文档，缺一即 CI 失败。本仓库是双语且 1:1 对齐，但没有把「语言版本存在性」做成硬门。
3. **覆盖科研的"写代码/做实验"侧**：bug-detective、architecture-design、webapp-testing、verification-loop 等把研究软件工程也纳入工作流。本仓库刻意不做这一层（交给外链），但对"科研 = 也要写代码"的用户，claude-scholar 一个插件解决的面更宽。
4. **社区规模**：4,474 stars，约为本仓库的 7.7 倍，issue/PR 反馈盘子更大。

**codex-claude-academic-skills**
1. **Office 产出链是本仓库完全没有的能力**：`office-academic-skill` 带完整 OOXML 参考实现（docx/pptx 的 pack/unpack/validate/redlining 脚本），能直接生成学术 Word/PPT（组会、开题、答辩场景）。本仓库不产 Office 工件。
2. **大颗粒、低认知负担**：只有 3 个入口 skill，中文用户"一键调用"心智成本远低于在 2,902 个技能里定位。对不关心具体期刊的用户，这是更好的默认体验。
3. **科学计算参考库成体系**：vendored 的 21 个计算子技能（sympy / qutip / pymatgen / pymoo / timesfm 等）覆盖物理、材料、优化、时序预测等本仓库执行桥未触及的学科计算生态。

**nature-skills**
1. **自带可运行的 MCP server**：`nature-academic-search` 是仓库内实现的多源学术检索 MCP server（arXiv / Crossref / PubMed / Scopus / ScienceDirect，含 live tests）。本仓库的执行桥是"对接外部 MCP"，而它是"自己发货一个 MCP"，分发上更自洽。
2. **社区影响力量级不同**：25,214 stars，是本组对比中的绝对头部（约为本仓库 43 倍），且配套视频教程与付费社群，用户教育做得最重。
3. **工作流覆盖到论文之外**：paper-to-patent（专利）、proposal-writer（基金）、experiment-log（实验记录）、paper2ppt——科研生命周期上比本仓库"面向发表"的定位铺得更宽。

**Nature-Paper-Skills**
1. **claim-driven 手稿工作流有明确的方法论**：claim-evidence map、paper-handoff、submission-audit 的 checklist 化设计，围绕"论证链"组织写作过程；本仓库深度包按投稿环节切分，没有等价的 claim→evidence 追踪结构。
2. **带脚本的引用审计工具链**：`citation-verifier/scripts/scan_citations.py`、`reference-audit-guide/` 的 API 客户端 + 格式检查器，且有 pytest 测试文件——单点上比本仓库多数技能的纯 prose 引用指引更"可执行"。
3. **会议模板即拿即用**：`conference-paper-writing/templates/icml2026/` 含完整 LaTeX 模板 + 示例 PDF；本仓库 CS venue 深度包不 vendored 官方 LaTeX 模板。

共同的结构性差异（非单方优势）：四个对方仓库都选择"少而通用"，本仓库选择"多而按刊"。前者安装轻、维护面小；后者的代价是必须靠 inventory/clone/scorecard 这套审计工具压住规模化的质量风险——这正是本目录其他文档存在的原因。

---

## 4. 复验附录 / Verification appendix

检索日期：**2026-07-02**。外部事实一律 `gh api`；`<R>` ∈ {`Galaxy-Dawn/claude-scholar`, `zLanqing/codex-claude-academic-skills`, `Yuan1z0825/nature-skills`, `Boom5426/Nature-Paper-Skills`}。

**A. 对方仓库元数据（stars / license / pushed_at / 默认分支 / 描述）**
```bash
gh api repos/<R> --jq '{full_name, stargazers_count, license: .license.spdx_id, pushed_at, default_branch, description}'
```
2026-07-02 返回值：
| repo | stars | license | pushed_at |
|------|------:|---------|-----------|
| Galaxy-Dawn/claude-scholar | 4474 | MIT | 2026-07-02T04:28:47Z |
| zLanqing/codex-claude-academic-skills | 1345 | MIT | 2026-05-14T09:08:48Z |
| Yuan1z0825/nature-skills | 25214 | Apache-2.0 | 2026-07-01T22:43:59Z |
| Boom5426/Nature-Paper-Skills | 339 | MIT | 2026-05-08T08:53:50Z |

**B. SKILL.md 计数（含截断标志）**
```bash
gh api "repos/<R>/git/trees/HEAD?recursive=1" \
  --jq '{truncated, skillmd_count: ([.tree[].path | select(endswith("SKILL.md"))] | length)}'
```
2026-07-02 返回：claude-scholar 45、codex-claude-academic-skills 24、nature-skills 15、Nature-Paper-Skills 18；四者均 `truncated: false`。

**C. Venue 覆盖 / CI / MCP / 脚本 / 输出证据（tree 路径检视）**
```bash
gh api "repos/<R>/git/trees/HEAD?recursive=1" --jq '.tree[].path' > <R>.txt
grep "SKILL.md" <R>.txt                 # 逐技能路径，判 venue 专属目录
grep -i "^\.github/workflows" <R>.txt   # CI 存在性
grep -iE "mcp" <R>.txt                  # MCP 集成
grep -iE "output|result|example" <R>.txt  # committed 输出证据
grep -i "readme" <R>.txt                # README 语言版本
```
关键命中（2026-07-02）：
- claude-scholar：`.github/workflows/installer_smoke.yml`、`repo_sanity.yml`；`MCP_SETUP.{md,zh-CN.md,ja-JP.md}`；`skills/mcp-integration/`；nature-\* 技能 4 个；`README.{md,zh-CN.md,ja-JP.md}`。
- codex-claude-academic-skills：无 workflows；无 mcp 路径；21/24 个 SKILL.md 位于 `scientific-toolkit-skill/references/scientific-skills/`；`timesfm-forecasting/examples/anomaly-detection/output/anomaly_detection.json`。
- nature-skills：无 workflows；`skills/nature-academic-search/mcp-server/`（arxiv/crossref/pubmed/scopus/sciencedirect 源 + live tests）；`nature-figure/assets/figures4papers/**/*.png`；单一 `README.md`。
- Nature-Paper-Skills：无 workflows；无 mcp 路径；`skills/venue/nature-portfolio-playbook/SKILL.md`；`tests/test_check_figure_refs.py`；`README.md` + `README.en.md`。

**D. CI 内容与 README 语言（内容级抽查）**
```bash
gh api repos/Galaxy-Dawn/claude-scholar/contents/.github/workflows/repo_sanity.yml --jq '.content' | base64 -d
gh api repos/Galaxy-Dawn/claude-scholar/contents/.github/workflows/installer_smoke.yml --jq '.content' | base64 -d
gh api repos/<R>/readme --jq '.content' | base64 -d | head
```
确认：repo_sanity 检查机器路径泄漏 + junk 文件；installer_smoke 跑安装/卸载冒烟并强制三语文档存在；nature-skills 与 codex 仓库 README 为中文单语；Nature-Paper-Skills README 首屏即「简体中文 | `English (README.en.md)`」。

**E. MCP code-search 交叉核对**
```bash
gh api "search/code?q=repo:Boom5426/Nature-Paper-Skills+mcp" --jq '.total_count'    # → 1
gh api "search/code?q=repo:zLanqing/codex-claude-academic-skills+mcp" --jq '.total_count'  # → 3
```
逐一核验：codex 仓库 3 次命中全部为 OOXML schema 文件（`shared-math.xsd`），非 MCP 集成；Nature-Paper-Skills 命中文件 `skills/optional/conference-paper-writing/SKILL.md` 抽取后 `grep -i mcp` 无命中（GitHub 索引分词伪命中），故矩阵记为「无 MCP 引用」。

**F. 对比对象来源（本仓库 README 外链区块）**
```bash
grep -n "github.com" README.md | grep -v "brycewang-stanford\|anthropics"
```
命中 L386（第三方收录说明）与 L1180–L1188（upstream 表：nature-skills / Nature-Paper-Skills / claude-scholar / codex-claude-academic-skills）。L1929–L1953 的「更多第三方」列表为通用写作/综述工具，无按刊结构，不纳入矩阵。

**G. 本仓库事实**
- 2,902 skills / 195 packs / 519 journals + 155 CS-AI venues；scorecard floor 92.0 / mean 93.8；execution bridge 134/134；双语 38 sections 1:1 —— 既有审计口径，复验：`python3 tools/audit_repo.py`、`python3 tools/quality_scorecard.py`、`python3 tools/run_checks.py`。
- CI：`cat .github/workflows/repo-audit.yml` —— push/PR 硬门 + `cron: "17 2 * * 1"` 周程；外链 liveness 为 advisory job（`if: schedule || workflow_dispatch`）。
- showcase 5 案例：`ls showcase/` → did-castle-doctrine / dml-returns-to-schooling / iv-card-college-proximity / rdd-close-elections / scm-california-prop99。
- 185-venue 索引：`wc -l shared-resources/journal-selection/venue-index.tsv` → 186 行（1 表头 + 185 venue），2026-07-02 本地实测。
- v1.0.0：`git tag | tail -1` → v1.0.0。License：`head -1 LICENSE` → MIT。
- Stars/pushed_at（本仓库）：`gh api repos/brycewang-stanford/awesome-journal-skills --jq '{stargazers_count, license: .license.spdx_id, pushed_at}'` → 584 / MIT / 2026-07-02T11:04:09Z。
- 本地 HEAD：`git log -1 --format='%h %cI'` → `19a91ede 2026-07-02T04:04:08-07:00`。

---
*本文档为快照式对比：stars、pushed_at、SKILL.md 数随对方仓库演化会过期；复验请重跑附录命令并更新检索日期。*
