---
name: cn-journal-workflow
description: Use when deciding which Chinese social-science/economics/management journal skill to invoke next, comparing fit across the 100-journal Chinese roadmap plus 中国社会科学 and 社会学研究, or routing a manuscript before venue-specific rewriting.
---

# 中文经管社科期刊工作流（cn-journal-workflow）

## 作用

这是路由 skill。它不替代单刊 skill，而是先判断稿件的**学科、问题层级、方法形态和读者对象**，再转入对应期刊 skill。

## 需要时加载的资源

- 路由不清或用户只说“经管/社科中文期刊”时，先读 `../../resources/worked-examples/venue-routing.md`。
- 相近刊物容易混淆时，读 `../../resources/exemplars/selection-patterns.md`。
- 准备给出投稿前结论时，读 `../../resources/official-source-map.md` 并核验对应期刊的最新官方投稿须知。

## 先问四件事

1. 问题层级：国家/制度/理论命题，还是某行业、某政策、某企业行为？
2. 方法形态：理论、准实验、结构模型、测度预测、数理优化、问卷/案例、政策评论？
3. 学科读者：经济学、金融、财政税收、国际经济、三农、管理科学、工商管理、公共管理、会计审计、社会政策？
4. 投稿目标：冲顶刊，还是追求题刊匹配和审稿效率？

## 快速路由

| 稿件特征 | 优先 skill |
|---|---|
| 中国经济理论贡献、完整实证生命周期 | `economic-research` 或完整 `er-workflow` |
| 管理实践、中国制度背景、可操作政策建议 | `management-world` 或完整 `mw-workflow` |
| 国际范式、识别/结构模型最强 | `china-economic-quarterly` |
| 产业、企业、创新、数字经济、厚稳健性 | `china-industrial-economics` |
| 国际贸易、开放经济、GVC、汇率/FDI | `journal-of-world-economy` / `journal-of-international-trade` |
| 金融、银行、货币政策、资本市场 | `journal-of-financial-research` / `studies-of-international-finance` |
| 三农、土地、乡村治理、农业政策 | `china-rural-economy` / `china-rural-survey` / `issues-in-agricultural-economy` |
| 财政、税收、预算、地方债 | `public-finance-research` / `tax-research` / `finance-and-trade-economics` |
| 测度、预测、IO/CGE、质量/效率 | `journal-of-quantitative-technological-economics` / `macroeconomics` / `journal-of-macro-quality-research` |
| 数理管理、优化、系统工程、算法 | `journal-of-management-sciences-china` / `systems-engineering-theory-and-practice` |
| 战略、组织、营销、问卷/案例理论 | `nankai-business-review` / `management-review` / `chinese-journal-of-management` |
| 公共管理、行政、数字政府、治理 | `journal-of-public-management` / `chinese-public-administration` / `e-government` |
| 科技政策、创新管理、科研评价 | `china-soft-science` / `studies-in-science-of-science` / `science-research-management` |
| 会计、审计、披露、内控 | `accounting-research` / `auditing-research` |
| 劳动、就业、社保、社会政策 | `studies-in-labor-economics` / `social-security-studies` |
| 跨学科最高平台、原创理论命题 | `social-sciences-in-china` |
| 社会学问题意识、定量/定性社会学 | `sociological-studies` |
| 体育学（运动训练、运动人体科学、体育人文社会学等） | 转中文体育学期刊合集 `Chinese-Sport-Science-Journal-Skills`（`cn-sport-journal-workflow`）；体育只是案例的经管稿仍回经管刊 |

## 相近刊物区分

| 容易混淆 | 区分规则 |
|---|---|
| 《经济研究》 vs 《中国工业经济》 | 前者要求能进入一般经济理论或重大政策机制；后者更适合产业、企业、创新、数字经济与厚实机制。 |
| 《金融研究》 vs 经管综合刊 | 金融渠道必须是核心问题；若金融变量只是机制或控制变量，转向产业、财政、区域或综合经管刊。 |
| 《管理世界》 vs 管理学专业刊 | 前者强调中国制度情境、管理实践和政策含义；纯构念/问卷/案例理论常先看南开管理评论、管理评论、管理学报。 |
| 《中国行政管理》 vs 《电子政务》 | 行政改革与治理理论优先前者；数字政府平台、数据治理和公共服务数字化优先后者。 |

## 决策规则

- 只有相关性、没有理论机制：先补问题意识，不要急着选顶刊。
- 有干净政策冲击但题目偏行业企业：优先《中国工业经济》，不是自动投《经济研究》。
- 金融变量只是控制变量：不要投《金融研究》；只有金融渠道是核心机制才对口。
- 问卷/SEM/案例理论建构：优先管理学刊，不要用经济学政策评估的口吻。
- 数理模型/算法是贡献：优先管理科学类；回归系数不是《管理科学学报》的核心产出。
- 投稿前必须进入单刊 skill 的“官方核验清单”，不要凭旧模板提交。

## 输出格式

```text
【首选期刊 skill】<skill-name>
【备选 1】<skill-name>（理由）
【备选 2】<skill-name>（理由）
【不建议投】<期刊>（一句话说明错位）
【当前最大短板】选题 / 理论 / 识别 / 机制 / 格式 / 官方要求
【下一步】调用 <skill-name> 做单刊定位与改写
```
