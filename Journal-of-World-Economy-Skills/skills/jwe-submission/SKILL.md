---
name: jwe-submission
description: Use for the pre-submission preflight to 《世界经济》 (The Journal of World Economy) — checking footnote (页下注) conventions, reference list at the end, 内容提要 (no official length) + 3–5 keywords, title ≤ 26 characters, bilingual title, blind-review anonymity, and the official online submission site (www.jweonline.cn). Use right before submitting; verify every rule against the journal's current 投稿须知.
---

# 投稿前 preflight（jwe-submission）

## 触发时机

- 正文、识别、渠道、文风都定了，准备投稿
- 需要一份"投出去前最后核对"的清单

## 关键事实（详见 resources/journal-profile.md）

- 投稿系统：**www.jweonline.cn**（编辑部唯一官方投稿网址；编辑部邮箱 jwe@cass.org.cn，电话 (010)85195790）
- 注释体例：**脚注（页下注）**置当页下；**参考文献置文末**，文中与文末一一对应，中文在前外文在后（按拼音/字母排序）
- 篇幅：论文字数**最好不超过 2 万字**；标题（含副标题）**不超过 26 字**、用陈述句（编辑部《稿件体例调整规范》）
- 内容提要：简要阐述问题、意义、数据、方法、结论及政策启示，**官网未规定字数**；关键词 **3~5 个**；配中英文标题（官网《投稿须知》，2026-11-23 核实）
  - ⚠ 网上流传的「1.2 万—2.5 万字 / 提要 400—500 字 / 关键词 5—6 个」是**《世界经济与政治》**的要求，勿套用
- **正文不得出现作者姓名和任何可能透露身份的提示**（双向匿名外审）；作者、单位、基金、致谢放正文之外（封面/系统），封面具体格式官网未写明
- 数据与代码：**终审通过后一周内**按《数据与代码等可复现政策指南》提交，随文公开（可申请数据豁免，但代码、日志、输出仍须公开）；初投不要求提交
- 主办：中国世界经济学会 + 中国社会科学院世界经济与政治研究所（IWEP）；中国社会科学院主管；1978 年创刊，月刊；主编张斌；**本刊不向作者以任何形式收取任何费用**、按篇付稿费；双向匿名审稿（建议审稿 1 个月、作者返修 3 个月内，一般不超过三轮）（官网，2026-11-23 核实）
- **JEL / 中图分类号**：官网未核实到明文要求——**待核实**（投前对照最新《投稿须知》，勿凭记忆补写）

> 体例与字数以官网**最新《投稿须知》/《致作者》**为准。该刊投稿系统曾迁移、网上有 sjjj.magtech / manu30.magtech / sjjj.ndhx 等镜像与第三方代投站点——**只认 www.jweonline.cn**，不要凭记忆或第三方页面投稿。本刊与《世界经济与政治》《世界经济研究》是不同刊物，勿套用其要求。

## 体例 checklist

- [ ] 注释统一为**页下注（脚注）**；**参考文献置文末**且与文中一一对应
- [ ] 参考文献中文在前、外文在后，按拼音 / 字母排序；著录含刊名期号 / 出版年单位版次地点
- [ ] 引文准确可核查；直接引用标页码
- [ ] 中英文标题齐全，标题 ≤ 26 字、陈述句；内容提要覆盖问题/意义/数据/方法/结论/政策启示；关键词 3~5；全文最好 ≤ 2 万字
- [ ] 外国人名附原文或用原文；专业术语规范
- [ ] 图表规范、编号连续、有数据来源（PPML/GVC/shift-share 口径已注）
- [ ] 基金项目、作者信息放正文之外（封面/投稿系统），正文不出现

## 匿名评审 hygiene

- [ ] 正文 / 注释 / 致谢中**去除可识别作者身份**的信息
- [ ] 自引改为第三人称或匿名占位
- [ ] 投稿封面与正文分离，正文不出现作者姓名
- [ ] 文件属性（作者名）已清除

## 提交前内容复核（调用其它 skill）

- [ ] 开放维度立得住（`jwe-fit-positioning`）
- [ ] 识别（含 shift-share 推断）站得住（`jwe-identification`）
- [ ] 传导渠道讲清（`jwe-transmission-channel`）
- [ ] 政策落在开放政策层（`jwe-policy-implication`）

## 反模式

- 凭记忆套体例，不查最新《投稿须知》
- 用尾注 / 纯文中夹注替代页下注，或参考文献不与文中对应
- 经第三方"代投"站点投稿，未认准 www.jweonline.cn
- 忘清匿名信息 / 正文留作者名就投

## 《世界经济》投稿退回模式表

本刊（IWEP + 中国世界经济学会主办的 CSSCI 权威顶级期刊）形式审查与匿名 hygiene 出问题会直接退回。下表把常见退回触发点显性化。

| 退回触发点 | 后果 | 修法 |
|------------|------|------|
| 用尾注/文中夹注替代页下注 | 体例不合，退改 | 改页下注，参考文献置文末并与文中一一对应 |
| 正文留作者姓名/致谢/项目号 | 破坏双向匿名 | 封面分离，正文匿名占位，清文件属性 |
| 经第三方代投/旧镜像投稿 | 入口非官方 | 只认 www.jweonline.cn |
| 终审通过后未及时交数据/代码 | 耽误后续流程 | 终审后一周内按可复现政策指南提交；数据不能公开先提豁免申请 |

## 微型走查：投前 preflight（示意）

设一篇关税转嫁稿件准备投本刊。按本 skill 过最后一关：

```
preflight（示意）：
  体例 → 页下注□√ 文末参考文献□√ 中英标题□√ 中文在前外文在后□√
  字数 → 正文约 1.8 万字（最好 ≤ 2 万）√；标题 19 字（≤ 26）√；内容提要六要素齐√；关键词 4 个（3~5）√
  匿名 → 正文搜"致谢/基金/作者单位" = 0 命中；文件属性作者名已清
  图表 → 引力表注明 PPML□√；shift-share 报 exposure-robust SE□√；图表有数据来源√
  数据代码 → 海关清洗脚本+变量构造代码已备（受限微观说明获取渠道）
  待核实 → JEL/中图分类号官网未见明文 → 标"待核实"，投前对照最新《投稿须知》
  系统 → www.jweonline.cn 官方入口已确认，未走第三方
```

> 走查中的字数/关键词为示意占位，体例字数区间以编辑部最新《投稿须知》/《致作者》为准，勿凭记忆补写。

## 审稿人追问模式 + 本刊语境修法

- 退回"体例不符" → 对照官网最新《投稿须知》，勿套用《世界经济与政治》《世界经济研究》要求。
- 退回"匿名信息未清" → 复查正文/注释/致谢/文件属性，自引改第三人称。

## 校准锚点（本刊已刊论文形态）

本刊采用页下注、文末参考文献、中英文标题、双向匿名外审，终审通过后一周内须交数据与代码；JEL/中图分类号等是否要求以官网最新《投稿须知》为准，本卡片标注项均须投前核实。

## 输出格式

```
【体例】页下注□ 文末参考文献□ 中英标题□ 著录规范□
【字数】正文 X 字（最好 ≤ 2 万）/ 标题 X 字（≤ 26）/ 关键词 X 个（3~5）
【匿名】已清理 / 待清理 <点>（双向匿名）
【数据代码】已备 / 待备（终审通过后一周内提交）
【系统】www.jweonline.cn 官方入口已确认
【待核实项】JEL□ 中图分类号□（投前对照官网）
【内容复核】定位□ 识别□ 渠道□ 政策□
【结论】可投 / 待修 <清单>
```

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue journal-of-world-economy-skills   # from a clone of the AJS repository
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
