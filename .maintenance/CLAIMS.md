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

- **主题词表 lane**（2026-08-27）：给检索加第二套词表。`scope-postings.tsv` 是从各 pack
  的**流程散文**里抽的（怎么投稿、怎么评审、格式规定），而 query 是论文标题，说的是
  **主题**——两者不在同一个语域上，结果是 dev 半集里每七篇有一篇的真实 venue **在任何
  深度上都检索不到**。新增 `tools/fetch_venue_topics.py`：按 venue 类型走免费源
  （期刊 → Crossref，会议 → DBLP），抓各 venue 自己发表过的文章标题，产出
  `venue-sources.tsv`（可人工复核的解析映射）与 `topic-postings.tsv`（第二套倒排词表），
  由 `match_lib` 合并检索。**解析规则一律是归一化后的精确匹配**：模糊匹配不会让排序变差
  一点，而是把别人的主题装进这个 venue——中文刊用译名匹配已经错过三次（《金融研究》→
  Southern Finance Association 的同名刊等），所以加了 ISSN 否决规则。触碰面：`tools/`
  （新增 `fetch_venue_topics.py`、两个新测试文件、`match_lib` 双词表加载、
  `match_venues` 的 `°` 标记、`eval_journal_match` 的 scope-only 对照行、`run_checks`
  新增 offline `--check`）、`shared-resources/journal-selection/`（两个新生成物 + README
  + `journal-match.md`）、`CONTRIBUTING.md`、`CHANGELOG.md`。**不触碰任何 pack 内容。**

- **计数护栏 lane**（2026-08-27）：`audit_repo.check_documented_counts` —— 把 capability
  文档里写死的数字钉到它所描述的生成物上。发现时 `journal-match.md` 与
  `journal-selection/README.md` 里五个数字全是旧的（743 venue / 289 深度包 / 300 层
  检索深度 / 1,725 与 1,507 两个互相矛盾的 ladder 边数），而每一句话都和推翻它的那个
  文件放在同一个目录里。触碰面：`tools/audit_repo.py`、`tools/tests/test_documented_counts.py`、
  两份 journal-selection 文档、`tools/README.md`。

- **会议届次锚定修正 lane**（2026-08-27）：`cycle_audit.edition_years` 没有左边界，
  "EACL 2027" 里含有 "ACL 2027"，于是 `ACL-Skills` 被判为锚定在一个它一条事实都没有的
  届次上——恰好是这个检查本身要防止的那种误读。同批按修正后的结果实地复核了
  ACL / PODC / ICML / AISTATS 四个包（此前 403 的网关已开放）。触碰面：
  `tools/cycle_audit.py`、`tools/tests/test_cycle_audit.py`、上述四个包的 source map、
  `ACL-Skills/skills/acl-workflow`、`.maintenance/` 两份看板。

- **会议届次锚定 lane**（2026-08-26）：新增 `tools/cycle_audit.py` 与
  `.maintenance/CYCLE-CURRENCY.md`——freshness 只回答"什么时候重读的"，对会议还要回答
  "重读的是哪一届"，issue #3 报的就是这个缺口。同批修正 scorecard 的 wiring 维度作用域
  （把 102 个 CS 包移出分母，并把真正该接的两个包接上），并按新工具的结果把
  `AAAI-Skills` 重锚到 AAAI-27、`ICLR-Skills` 重锚到 ICLR 2027（该届摘要截稿
  2026-09-18，是全库唯一仍在进行中的 deadline），另有 CAV/DAC/COLT/AISTATS/ICML/PODC/
  NeurIPS 七个包补记 edition status。触碰面：`tools/`（新增 `cycle_audit.py`、
  `venue_lib.CONFERENCE_DEPTH_PACKS`/`CONFERENCE_ALIASES`/`uses_econometric_execution`、
  两个新测试文件）、`AAAI-Skills`、`ICLR-Skills`、上述七个会议包的 source map、
  `Chinese-Journal-of-Management-Science-Skills` 与 `Language-Linguistic-Society-Skills`
  各三个 skill、两份根 README 的召回数字、`CHANGELOG.md`、`.maintenance/`。

- **外链体检 lane**（2026-08-26）：修 `external_link_audit.py` 把「站点对陌生
  UA 返回 404」误判为死链的问题（SciEngine 两页 + CNKI 一页本来就活着），并处理
  重定向表里两个已被抢注的会议域名。触碰面：`tools/external_link_audit.py`、
  `tools/tests/test_external_link_audit.py`、`.maintenance/DEAD-LINKS.md`、
  `CHANGELOG.md`，以及**两处 pack 内容**——`ECAI-Skills/resources/`（FAIA 索引改指
  IOS Press）与 `Computer-Science-Conference-Skills/`（COLING 官方锚点改指 ACL
  Anthology venue 页），连带重新生成 `shared-resources/journal-selection/` 生成物。

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
