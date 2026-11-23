---
name: jqte-submission
description: Use for the pre-submission preflight to 《数量经济技术经济研究》 (JQTE) — checking footnote conventions (脚式编排, renumbered per page), title/keyword/abstract format, the ≥1000-character (style sheet: ≥1200) policy section, abstract ≤500 字 / ≤5 keywords / 600–800-word English Summary / ≥2 JEL codes, the post-acceptance data-and-code release, the online submission system (jqte.net), and author-identification rules. Use right before submitting; verify every numeric rule against the journal's current 投稿须知.
---

# 投稿前 preflight（jqte-submission）

## 触发时机

- 方法、结果、含义都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿系统 / 官网：**https://www.jqte.net/**（编辑部官方网站，远程投稿系统，作者登录 author/login.aspx）
- 注释体例：**文中所需注释以脚式编排，每页重新编号**（页下注/脚注，逐页起编）
- **政策建议不少于 1000 字（纯方法类论文除外）**（《投稿须知》）；官网《体例（定稿）》写**不少于 1200 字、分条撰写**——两份官方文件不一致，按 1200 字准备
- 中文题目一般 ≤ 20 字（可加副标题）；英文题目与中文一致
- 题名下列作者（**≤ 4 位**）、单位、摘要（**≤ 500 字**）、关键词（**≤ 5 个**）、中图分类号（一个），并附英文 **Summary 600–800 词** + **JEL 至少两个**（官网《体例》，2026-11-24 复核）
- 数据与代码：录用后**一周内**把附录/数据/程序/案例材料发责任编辑，刊后公开（2022 年第 9 期起）
- 请在投稿系统内上传全本稿件
- 主办：中国社会科学院数量经济与技术经济研究所；月刊

> 摘要、关键词、英文 Summary、JEL、作者数已于 2026-11-24 由官网《体例（定稿）》坐实；查重阈值与全文总字数官网仍未列明（见 profile「待核实」）。**以官网最新《投稿须知》与投稿系统提示为准，不要凭记忆。**

## 体例 checklist

- [ ] 注释统一为**脚式编排、每页重新编号**（页下注，逐页起编）
- [ ] 中文题目 ≤ 20 字；英文题目与中文一致
- [ ] 题名下信息齐全：作者（≤4 位）、单位、摘要、关键词、中图分类号；英文 Summary（600–800 词）+ JEL（≥2 个）
- [ ] 摘要为完整短文，独立自含、不分段、不用图表公式
- [ ] 摘要 ≤ 500 字、关键词 ≤ 5 个（官网《体例》）
- [ ] 政策建议 ≥ 1200 字、分条撰写（《体例》；《投稿须知》为 1000 字；纯方法类除外）
- [ ] 图表有数据来源与方法注、编号连续
- [ ] 已在投稿系统上传全本稿件

## 可复现性 hygiene（本刊尤重）

- [ ] 方法/指标/参数构造透明，他人能复现
- [ ] 数据来源、口径、年份、平减/校准交代齐全
- [ ] CGE/IO 的弹性来源、闭合规则、情景设定可重建

## 匿名评审 hygiene

> 官网《投稿须知》要求在题目下注明作者姓名、单位，《体例》把作者信息、基金与致谢放在首页脚注——本刊是**审稿人匿名**（至少两位匿名评审专家），官网**未要求作者匿名化**（2026-11-24 复核）。以下各项仅在投稿系统另行提示上传匿名稿时执行。

- [ ] 正文/脚注/致谢/基金信息中去除可识别作者身份
- [ ] 自引改第三人称或匿名占位
- [ ] 文件属性（作者名）已清除

## 提交前内容复核（调用其它 skill）

- [ ] 贡献类型清楚、未硬凑因果（`jqte-fit-positioning`）
- [ ] 测度/模型/分解透明可复现（`jqte-measurement` / `jqte-io-cge`）
- [ ] 预测做了样本外评估（`jqte-forecasting`）
- [ ] 做了方法/参数敏感性（`jqte-sensitivity`）
- [ ] 表格有量化解读（`jqte-tables-figures`）

## 反模式

- 凭记忆套体例与字数，不查最新《投稿须知》
- 用尾注/文中夹注替代脚式编排逐页注
- 政策建议不足 1000 字（非纯方法类）
- 方法节黑箱、无法复现就投

## 投稿前体例风险表（本刊特有项）

《数量经济技术经济研究》有几处与多数经济刊不同的体例硬约束,踩中即退回补正（数值类一律以官网最新《投稿须知》为准）。

| 体例项（本刊特有） | 达标线 | 常见踩雷 |
|--------------------|--------|----------|
| 注释体例 | 脚式编排、每页重新编号 | 用尾注/文中夹注替代 |
| 政策建议篇幅 | ≥1200 字分条（《体例》；《投稿须知》≥1000 字；纯方法类除外） | 不足篇幅或纯口号 |
| 中英题目 | 中文一般≤20 字；英文与中文一致 | 中文题目超长、中英题意不一致 |
| 题名下信息 | 作者≤4/单位/摘要≤500字/关键词≤5/中图分类号；英文 Summary 600–800 词 + JEL≥2 | 漏中图分类号、JEL 或英文 Summary |

## 微型走查：一篇 CGE 稿件的 preflight（示意）

承接碳税 CGE 稿件，投稿前逐项核对（示意）：

1. **体例**：注释改为脚式逐页编号（原为文末尾注）；中文题目 18 字；摘要 460 字、关键词 4 个、Summary 720 词、JEL 2 个。
2. **政策篇幅**：政策建议约 1200 字（达标），每条引模拟结果量级。
3. **可复现**：参数来源表、闭合说明、情景表、基准复制校验齐全；附录/数据/程序按《数据公开体例》命名，录用后一周内可交。
4. **系统**：在 jqte.net 作者端上传全本稿件。

```text
【体例】脚注逐页 □  题目 18字 □  摘要≤500/关键词≤5/Summary 600–800/JEL≥2 □  图表注 □
【字数】政策建议约 1200 字（≥1200 □，示意）
【可复现】参数表/闭合说明/情景表/基准复制 □｜附录/数据/程序已按数据公开体例命名 □
【系统】jqte.net 全本已上传 □｜【结论】可投（数值类以官网最新须知复核）
```

## 审稿/编辑追问模式 + 本刊语境修法

- **"注释为什么不是脚式逐页编号？"** → 这是本刊明确体例,统一改为页下注、每页重新起编,不可用尾注代替。
- **"政策建议不足 1000 字"**（《体例》要求 1200 字）→ 非纯方法类需补足并使每条由结果支撑（参 `jqte-implications`）；是否豁免**以编辑部最新稿约为准**。
- **"方法节无法复现"** → 投前先过 `jqte-measurement`/`jqte-io-cge` 补齐数据口径与参数来源。

## 校准锚点

- 投稿系统、官网入口与体例细则见 `resources/journal-profile.md`；摘要/关键词/Summary/JEL 数值出自官网《体例（定稿）》（2026-11-24 复核），查重阈值等仍未见官方数字,**一律以官网最新《投稿须知》与系统提示为准,不凭记忆**。
- 主办单位等基础事实稳定,但投稿流程偶有调整,投前再确认。

## 输出格式

```
【体例】脚注逐页□ 题目字数□ 题名下信息□ 图表注□
【字数】政策建议 X 字（≥1000 □ / 纯方法豁免 □）；摘要/关键词按系统核对
【可复现】方法透明□ 数据口径□ CGE/IO 可重建□
【匿名】已清理 / 待清理 <点>
【系统】jqte.net 投稿入口已确认
【结论】可投 / 待修 <清单>
```

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue journal-of-quantitative-and-technological-economics-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.
