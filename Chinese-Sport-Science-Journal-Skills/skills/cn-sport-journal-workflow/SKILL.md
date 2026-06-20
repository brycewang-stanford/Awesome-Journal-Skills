---
name: cn-sport-journal-workflow
description: Use when deciding which Chinese sport-science (体育学) journal skill to invoke next, comparing fit across the 12 CSSCI sport-science source journals (《体育科学》《中国体育科技》, the Beijing/Shanghai/Chengdu/Wuhan/Xi'an/Shenyang/Tianjin sport-university journals, 《体育学刊》《体育学研究》《体育与科学》), or routing a sport-science manuscript before venue-specific rewriting. Also use to redirect manuscripts that only use sport as a case back to econ/management or clinical venues.
---

# 中文体育学期刊工作流（cn-sport-journal-workflow）

## 作用

这是体育学的路由 skill。它不替代单刊 skill，而是先判断稿件的**子学科、问题层级、方法形态（自然科学 vs 人文社科）和读者对象**，再转入对应期刊 skill。

## 需要时加载的资源

- 准备给出投稿前结论时，读 `../../resources/official-source-map.md` 并核验对应期刊的最新官方投稿须知。
- 不确定本学科边界（是否该投体育刊）时，读 `../../resources/source-basis.md`。

## 先问四件事

1. 子学科：运动人体科学（生理生化 / 生物力学 / 运动医学 / 体质健康）、运动训练与竞技体育、体育人文社会学（社会学 / 管理 / 经济 / 政策 / 史哲）、学校体育、民族传统体育？
2. 方法形态：实验 / 测试 / 干预（自然科学），还是问卷 / 计量 / 政策文本 / 田野 / 思辨（人文社科）？
3. 问题层级：学科理论命题，还是某项目、某人群、某政策的具体问题？
4. 投稿目标：冲学科顶刊，还是追求题刊匹配与审稿效率？

## 快速路由

| 稿件特征 | 优先 skill |
|---|---|
| 体育学本体的理论 / 机制贡献、综合性、分量足 | `china-sport-science` |
| 竞技体育、运动训练实战、运动表现与备战、应用性强 | `china-sport-science-and-technology` |
| 综合性体育学（运动人体科学 + 人文社科皆可），院校综合学报 | `journal-of-beijing-sport-university` / `journal-of-wuhan-sports-university` / `journal-of-xian-physical-education-university` / `journal-of-shenyang-sport-university` |
| 体育社会科学问题意识强、理论对话足 | `journal-of-shanghai-university-of-sport` / `journal-of-sports-research` |
| 运动人体科学（运动生理生化 / 生物力学 / 运动医学）偏重 | `journal-of-tianjin-university-of-sport` / `china-sport-science` |
| 体育史、体育文化、民族传统体育 | `journal-of-chengdu-sport-university` |
| 学校体育、体育教育、青少年体质与健康促进 | `journal-of-physical-education` |
| 思辨性、跨学科、理论批判与方法论反思 | `sports-and-science` |
| 体育只是案例，核心是经济 / 管理 / 临床 | 转出体育刊（见"防误投"） |

## 相近刊物区分

| 容易混淆 | 区分规则 |
|---|---|
| 《体育科学》 vs 《中国体育科技》 | 前者要求学科本体的理论 / 机制贡献、综合分量足；后者更适合竞技体育、运动训练实战、备战应用与运动人体科学的应用研究。 |
| 院校综合学报之间 | 看主办院校的传统强项与栏目：成体偏体育史 / 民族传统体育；天体运动人体科学偏强；上体社科偏强。题材贴近哪家的强项就优先哪家，不要只按地域或名气。 |
| 《体育学研究》 vs 《体育与科学》 | 两者都偏体育社会科学；前者更重规范的社会科学问题意识与理论对话，后者更接纳思辨性、跨学科与方法论反思的理论文章。 |
| 体育刊 vs 经管 / 临床刊 | 只有体育学本体问题（运动机制 / 训练规律 / 体育制度与社会过程）才投体育刊；体育只是案例的经济 / 管理实证回经管刊，纯医学临床研究回临床医学渠道。 |

## 决策规则

- 只有相关性、没有体育学本体问题：先补问题意识，不要急着选顶刊。
- 自然科学稿无对照 / 无伦理 / 样本与功效不足：先补设计与伦理，再谈选刊。
- 人文社科稿停在政策复述或故事复述：先补理论对话与概念提炼。
- 竞技实战与备战应用：优先《中国体育科技》，不是自动投《体育科学》。
- 体育只是研究场景、核心贡献在别学科：转出体育刊，回到对应学科渠道（中文经管见 `cn-journal-workflow`）。
- 投稿前必须进入单刊 skill 的"官方核验清单"，不要凭旧模板提交。

## 输出格式

```text
【首选期刊 skill】<skill-name>
【备选 1】<skill-name>（理由）
【备选 2】<skill-name>（理由）
【不建议投】<期刊>（一句话说明错位）
【路径】运动人体科学(实验/测试) / 体育人文社会学(定量/定性/政策/思辨) / 跨学科混合
【当前最大短板】选题 / 理论 / 设计与伦理 / 机制 / 格式 / 官方要求
【下一步】调用 <skill-name> 做单刊定位与改写
```
