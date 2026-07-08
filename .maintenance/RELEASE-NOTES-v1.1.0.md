# v1.1.0 Release Notes（草案 · owner 验收后可直接用于 GitHub Release）

> Tag 建议：`v1.1.0`，基于 2026-07-08 的 `claude/repo-analysis-planning-8rqc2w`
> 合并后的 main。本文件为双语草案；发布时可整段复制。发布动作由 owner 执行，
> 本草案不代打 tag。

---

## 中文

### Awesome Journal Skills v1.1.0 — 十二个 CS/AI 会议深度包 + 全仓质量满分

自 v1.0.0（2026-07-02）以来的主要变化：

**新增 12 个会议深度包（category-8 完成度 6/100 → 18/100）**
- 第一波：UAI · COLT · MLSys · KDD
- 第二波：The Web Conference · WSDM · SIGIR · CVPR
- 第三波：ICCV · ACL · EMNLP · ICRA
- 每包 12 个 skill、双语 README、官方源图（URL + 访问日期 + 访问方式披露）、
  exemplars / worked-examples / external-tools 资源层
- venue-true 差异化：COLT 如实按「无 artifact track、证明附录即 artifact」的
  理论会议形态编写并采用 CMT（非 OpenReview）口径；KDD 覆盖双投稿周期、
  Research/ADS 双轨与 Resubmit 管线；MLSys 覆盖 Research/Industrial 双轨与
  录后 artifact 徽章；CVPR 覆盖超大规模评审与 reviewer 注册义务
- 仓库总量：**195 pack / 2902 skill → 207 pack / 3046 skill**

**质量：全仓评分满分收尾**
- 修正评分器 structure 档位的规格错配（对完整小型广度束与深化旗舰包的
  错误罚分），修正前后逐包对比：195 包中仅目标 6 包变动，其余全部不变
- 全仓 195→207 个 pack 全部达到公式满分 **94.0**；CI 回归防线由
  `--min-score 90` 提升至 **94**
- 克隆审计 0.75 阈值全仓零命中（3046 skills）

**事实纪律**
- top-5 欠账 source map 完成一轮搜索渲染核实（8 项升级、其余债务精确化，
  全部带访问方式披露）；top-5 包硬数字可追溯性抽查零违规

**社区与治理**
- 新增第 4 套 issue 模板 `bundle-replication-request` + CONTRIBUTING
  「如何复用一个 pack bundle」规则
- CLAIMS 协作板归档重置；新增 QUALITY-LANE-2026-09（静态尺子饱和后的
  轻量质量方案）

---

## English

### Awesome Journal Skills v1.1.0 — twelve CS/AI conference depth packs + repo-wide perfect scores

Highlights since v1.0.0 (2026-07-02):

**12 new conference depth packs (category-8 progress 6/100 → 18/100)**
- Wave 1: UAI · COLT · MLSys · KDD; Wave 2: The Web Conference · WSDM · SIGIR · CVPR;
  Wave 3: ICCV · ACL · EMNLP · ICRA
- Each pack ships 12 skills, bilingual READMEs, an official source map
  (URL + access date + access-method disclosure), and an exemplars /
  worked-examples / external-tools resource layer
- Venue-true adaptations: COLT is written as the proof-first venue it is
  (no artifact track — the appendix is the artifact; CMT, not OpenReview);
  KDD covers the dual submission cycles, Research/ADS exclusivity and the
  Resubmit pipeline; MLSys covers the Research/Industrial dual track and
  post-acceptance artifact badges; CVPR covers review at 10k+ scale and
  author-reviewer registration duties
- Repo totals: **195 packs / 2902 skills → 207 packs / 3046 skills**

**Quality: the whole repo at the scorecard ceiling**
- Fixed a structure-band mis-specification in the scorecard (it penalised
  legitimate small breadth bundles and a deliberately deepened flagship);
  the before/after diff shows exactly the six target packs moving and
  every other score unchanged
- All 207 packs now score the formula ceiling **94.0**; the CI regression
  floor was raised from `--min-score 90` to **94**
- Clone audit: zero pairs at the 0.75 threshold across 3046 skills

**Fact discipline**
- A search-rendering verification pass over the five highest-debt source
  maps (8 items upgraded, remaining flags converted to precise dated debt,
  all with access-method disclosures); a hard-number traceability sweep
  over the same packs found zero violations

**Community & governance**
- Fourth issue template `bundle-replication-request` plus a CONTRIBUTING
  "How to reuse a pack bundle" section
- Claims board archived and reset; QUALITY-LANE-2026-09 documents the
  post-saturation quality regime
