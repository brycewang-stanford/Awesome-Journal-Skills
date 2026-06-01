# AJS 全学科扩张蓝图 (10×100 = 1000 完整 skill 包)

> 目标（用户 /goal）：打造覆盖全学科的最强期刊 skills repo，帮全球用户快速发论文。
> 本文件是**顶层设计 + 可执行规范**。选刊明细见 `JOURNAL-MASTER-LIST.md`。
> 创建：2026-05-31 · 验收节点：≈2026-06-30（已设提醒）

---

## 0. 诚实的范围声明（必读）

- AJS 现状（2026-06-01）：**1564 skills / 92 包**（README 徽章）。其中
  `Computer-Science-Conference-Skills` 是 AI-first CS 会议**广度包**，`NeurIPS-Skills`
  `ICML-Skills`、`ICLR-Skills`、`AAAI-Skills`、`IJCAI-Skills` 和 `AISTATS-Skills` 是 category 8 的前六个完整会议深度包；并行
  W1 又补入 6 个英文经济学领域刊深度包，17 个英文计量/金融/理论/应用微观并行壳已补齐为完整深度包，W2 已补齐 18 个英文管理/运营/营销/会计/IS
  插件壳为完整深度包。广度包仍不是终态"一会/一刊一完整 12-skill
  深度包"的替代。
- 本计划终态：**1000 包 × ~12 skills ≈ 12,000 个 `SKILL.md`** — 约 14× 体量。
- 这是**分波、分会话**完成的工程，不是一次无人值守跑完的任务。每个包必须过
  仓库既有质量红线（官方源优先、`待核实` 标注、禁止 find-replace 克隆、clone 审计 < 0.90）。
- 因此本计划把工作拆成 **可验收的波次**；每波产出真实可审计的包，进度写入 `PROGRESS.md`。

---

## 1. 顶层学科骨架（10 大类，经济学与管理学已合并）

| # | 大类 | 英文配额 | 中文配额 | 小计 | 主排序锚点 |
|---|------|:---:|:---:|:---:|---|
| 0 | 综合·交叉 (Multidisciplinary) | 85 | 15 | 100 | Nature Index / JCR · 中国科学院期刊分区 |
| 1 | 经济学与管理学 (Econ & Management) | 70 | 30 | 100 | FT50 / UTD24 / ABS-AJG 4* · CSSCI 经管 |
| 2 | 社会科学 (Social Sciences) | 55 | 45 | 100 | SSCI 分区 · CSSCI / 南大核心 |
| 3 | 人文学科 (Humanities) | 45 | 55 | 100 | AHCI · CSSCI(含扩展) |
| 4 | 数学与物理科学 (Math & Physical) | 88 | 12 | 100 | JCR Q1 / Nature Index · 中科院分区 |
| 5 | 生命科学 (Life Sciences) | 90 | 10 | 100 | JCR Q1 / Nature Index · 中科院分区 |
| 6 | 医学与健康 (Medicine & Health) | 78 | 22 | 100 | JCR / JIF · 中华医学会系列 |
| 7 | 工程与技术 (Engineering & Tech) | 72 | 28 | 100 | JCR / EI · EI 收录中文刊 |
| 8 | 计算机科学与AI (CS & AI) | 90 | 10 | 100 | **CCF-A/B 顶会优先** · CCF 中文刊 |
| 9 | 农业与环境 (Agriculture & Env) | 75 | 25 | 100 | JCR Q1 · 中文权威农业刊 |
| | **合计** | **748** | **252** | **1000** | |

### 1.1 两个正交维度
- **学科维度**：上表 10 大类，每类含二级子领域（见 MASTER-LIST）。
- **语言维度**：`lang: en | zh` 标签，与学科正交，不进目录树层级。

### 1.2 归类红线（防止配额溢出 / 重复计数）
- **单一主学科归类 + 多标签**：一个刊只占一个大类的配额；跨界刊（如 JFE=金融）
  归主学科，其余关系用 `tags` 表达。
- 边界仲裁默认表：金融/会计/营销/IS/运营 → 大类 1；计量经济学 → 大类 1；
  统计学方法刊 → 大类 4；健康经济学 → 大类 1（非大类 6）；计算社科 → 大类 0(0b)。

### 1.3 大类 0「综合·交叉」内部二分
- `0a 综合性大刊`：Nature, Science, PNAS, Nat. Commun., Sci. Adv. 等（投稿范围=综合）。
- `0b 真·交叉学科`：计算社会科学、生物信息学、神经科学交叉、神经经济学、网络科学等。

---

## 2. 「完整 skill 包」的标准结构（生产模板）

以 `Academy-of-Management-Review-Skills/` 为黄金样板，每个包必须含：

```
<Journal>-Skills/
├── LICENSE
├── README.md                         # 英文
├── README.zh-CN.md                   # 中文
├── .gitignore
├── .claude-plugin/
│   ├── plugin.json                    # name, version, description
│   └── marketplace.json               # 声明全部 skills（须与实际一致）
├── assets/
│   └── cover.svg                      # 统一封面卡（真实封面可后补）
├── resources/
│   ├── official-source-map.md         # 官方源 + URL + 访问日期（硬性审计）
│   └── external_tools.md
└── skills/                            # ~12 个 venue-specific skill
    ├── <slug>-submission/SKILL.md  (+ templates/)
    ├── <slug>-rebuttal/SKILL.md
    ├── <slug>-review-process/SKILL.md
    ├── <slug>-writing-style/SKILL.md
    ├── <slug>-workflow/SKILL.md
    ├── <slug>-topic-selection/SKILL.md
    ├── <slug>-data-analysis/SKILL.md
    ├── <slug>-tables-figures/SKILL.md
    ├── <slug>-contribution-framing/SKILL.md
    ├── <slug>-methods/SKILL.md
    ├── <slug>-literature-positioning/SKILL.md
    └── <slug>-theory-development/SKILL.md
```

### 2.1 学科自适应的 skill 集（不是所有学科都套用经管 12 件套）
- **CS/AI 顶会**：用 `submission / rebuttal(author-response) / camera-ready /
  artifact-evaluation / supplementary / reproducibility / review-process /
  writing-style / related-work / experiments / workflow / topic-selection`。
- **实验科学（生命/医学/化学）**：增 `reporting-guidelines（CONSORT/ARRIVE 等）/
  ethics-IRB / data-availability / cover-letter`，弱化 `theory-development`。
- **数学/理论**：增 `proof-exposition / notation`，弱化 `data-analysis`。
- 模板差异在 MASTER-LIST 的每个大类头部声明。

---

## 3. 排序锚点（让「top 70/30」可证伪）

每个大类的入选必须能追溯到公开榜单，禁止凭感觉：

| 维度 | 英文榜单 | 中文榜单 |
|---|---|---|
| 经管 | FT50, UTD24, ABS-AJG 4*/4, RePEc | CSSCI 经管来源刊, 国家自科委/社科委认定 |
| 社科人文 | SSCI/AHCI JCR 分区 | CSSCI(含扩展版), 南大核心 |
| 理工医农 | JCR (JIF/分区), Nature Index, 中科院分区 | 北大中文核心, 中国科技核心, 中华医学会 |
| CS/AI | **CCF 推荐会议/期刊 A/B 类**, CSRankings | CCF 中文刊推荐 |

入选条目在 MASTER-LIST 标注 `[anchor: 榜单名]`，无法核实的标 `待核实`。

---

## 4. 分波执行计划（每波 = 可独立验收）

> 单波规模按"一次会话能高质量产出"控制，避免克隆化。

- **Wave 0（本轮）**：蓝图 + 选刊总表（本文件 + MASTER-LIST）+ 提醒。✅
- **Wave 1**：去重盘点 — 把现有 92 包 / 200 根卡映射进 10 大类，标出"已有/需补"。
- **Wave 2+**：按大类滚动建包。优先级：
  1. 大类 1 经管（已有最多内容，补齐到 100）
  2. 大类 8 CS/AI（**AI 顶会排最前**，全新高价值）
  3. 大类 0 综合·交叉
  4. 其余 6 类滚动推进
- 每波：建包 → `python3 tools/run_checks.py` → clone 审计 → 写 PROGRESS.md → 留待验收。

### 4.1 可选加速：并行 workflow
选刊与建包可用多 agent 并行（每个 agent 负责一个大类/一批刊的源核验 + 建包）。
**需用户显式说 "workflow" 才会启动**（成本可观）。

---

## 5. Definition of Done（验收标准）

一个包算"完成"当且仅当：
1. 结构完整（§2 全部文件齐全，marketplace 声明 == 实际 skills 数）。
2. 每个 SKILL.md venue-specific，**clone 审计 < 0.90**（理想 < 0.75）。
3. `official-source-map.md` 含 ≥1 官方 URL + 可见访问日期；不可核实项标 `待核实`。
4. `python3 tools/run_checks.py` 通过。
5. 根级 `AJS-ROOT-JOURNAL-ENTRY` 导航卡指向真实 canonical SKILL.md。
6. README 双语 + 计数方法学已同步更新。

整体验收（1 个月节点）：按大类报告"完成包数 / 在建 / 未启动"，给出真实进度而非空壳数。
