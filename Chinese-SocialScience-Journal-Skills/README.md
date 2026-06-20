# Chinese Social-Science Journal Skills

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

An opinionated agent skill stack for the **100 Chinese economics / management roadmap journals** in the parent repository, plus two broader social-science flagships: 《中国社会科学》 and 《社会学研究》.

Unlike the full lifecycle packs for 《经济研究》 and 《管理世界》, this pack ships **one self-contained fit-and-house-style skill per journal**, plus `cn-journal-workflow` for routing. Each journal skill helps answer: *is my manuscript on-target, how should it be framed, what methods and evidence does this journal expect, and what official submission details must be re-checked?*

## Coverage

| Group | Scope |
|---|---|
| 经济学 | 50 roadmap journals, including economic-research, CEQ, industrial economics, world economy, finance, rural/agri, fiscal/tax, open economy, labor, regional economics. |
| 管理学 / 战略 / 公共管理 | 30 roadmap journals, including management-world, management science, management review, systems engineering, public administration, soft science, S&T policy. |
| 会计 / 审计 / 交叉 | 20 roadmap journals, including accounting, audit, social security, e-government, tax, securities market, business economics, regional finance journals. |
| 额外社科旗舰 | social-sciences-in-china and sociological-studies, retained from the original ten-journal pack. |

## Quick Start

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install chinese-socsci-journal-skills
/reload-plugins
```

Manual copy:

```bash
cp -R skills/* ~/.claude/skills/
# or for Codex
cp -R skills/* ~/.codex/skills/
```

## How to Use

Start with `cn-journal-workflow` when the venue is uncertain. If the target is already known, name the journal directly, for example: “Use `public-finance-research` to assess this财政论文 for《财政研究》.”

Every skill returns a fit verdict, method/evidence requirements, desk-reject risks, official-submission checks, and reroute suggestions.

## Skills

| Skill | Journal |
|---|---|
| `accounting-and-economics-research` | 《会计与经济研究》 |
| `accounting-research` | 《会计研究》 |
| `asia-pacific-economic-review` | 《亚太经济》 |
| `auditing-and-economics-research` | 《审计与经济研究》 |
| `auditing-research` | 《审计研究》 |
| `bulletin-of-chinese-academy-of-sciences` | 《中国科学院院刊》 |
| `business-management-journal` | 《经济管理》 |
| `china-accounting-review` | 《会计评论》 |
| `china-economic-quarterly` | 《经济学（季刊）》 |
| `china-economic-studies` | 《中国经济问题》 |
| `china-industrial-economics` | 《中国工业经济》 |
| `china-public-administration-review` | 《公共管理评论》 |
| `china-rural-economy` | 《中国农村经济》 |
| `china-rural-survey` | 《中国农村观察》 |
| `china-soft-science` | 《中国软科学》 |
| `chinese-journal-of-management` | 《管理学报》 |
| `chinese-journal-of-management-science` | 《中国管理科学》 |
| `chinese-public-administration` | 《中国行政管理》 |
| `chinese-review-of-financial-studies` | 《金融评论》 |
| `cn-journal-workflow` | Chinese journal routing workflow (not a journal) |
| `comparative-economic-and-social-systems` | 《经济社会体制比较》 |
| `contemporary-economy-of-japan` | 《现代日本经济》 |
| `contemporary-finance-and-economics` | 《当代财经》 |
| `e-government` | 《电子政务》 |
| `east-china-economic-management` | 《华东经济管理》 |
| `economic-aspects` | 《经济纵横》 |
| `economic-perspectives` | 《经济学动态》 |
| `economic-problems` | 《经济问题》 |
| `economic-research` | 《经济研究》 |
| `economic-review-cn` | 《经济评论》 |
| `economic-science` | 《经济科学》 |
| `economic-theory-and-business-management` | 《经济理论与经济管理》 |
| `economist-cn` | 《经济学家》 |
| `finance-and-economics` | 《财经科学》 |
| `finance-and-trade-economics` | 《财贸经济》 |
| `financial-regulation-research` | 《金融监管研究》 |
| `foreign-economics-and-management` | 《外国经济与管理》 |
| `forum-on-science-and-technology-in-china` | 《中国科技论坛》 |
| `frontiers-of-engineering-management-science-and-technology` | 《工程管理科技前沿》 |
| `governance-studies` | 《治理研究》 |
| `industrial-economics-research` | 《产业经济研究》 |
| `inquiry-into-economic-issues` | 《经济问题探索》 |
| `international-economic-review-cn` | 《国际经济评论》 |
| `international-economics-and-trade-research` | 《国际经贸探索》 |
| `issues-in-agricultural-economy` | 《农业经济问题》 |
| `journal-of-agrotechnical-economics` | 《农业技术经济》 |
| `journal-of-business-economics` | 《商业经济与管理》 |
| `journal-of-central-university-of-finance-and-economics` | 《中央财经大学学报》 |
| `journal-of-finance-and-economics` | 《财经研究》 |
| `journal-of-financial-research` | 《金融研究》 |
| `journal-of-guangdong-university-of-finance-and-economics` | 《广东财经大学学报》 |
| `journal-of-industrial-engineering-and-engineering-management` | 《管理工程学报》 |
| `journal-of-international-trade` | 《国际贸易问题》 |
| `journal-of-jiangxi-university-of-finance-and-economics` | 《江西财经大学学报》 |
| `journal-of-macro-quality-research` | 《宏观质量研究》 |
| `journal-of-management` | 《管理学刊》 |
| `journal-of-management-sciences-china` | 《管理科学学报》 |
| `journal-of-public-management` | 《公共管理学报》 |
| `journal-of-quantitative-technological-economics` | 《数量经济技术经济研究》 |
| `journal-of-shanghai-university-of-finance-and-economics` | 《上海财经大学学报》 |
| `journal-of-shanxi-university-of-finance-and-economics` | 《山西财经大学学报》 |
| `journal-of-world-economy` | 《世界经济》 |
| `journal-of-zhongnan-university-of-economics-and-law` | 《中南财经政法大学学报》 |
| `macroeconomics` | 《宏观经济研究》 |
| `management-review` | 《管理评论》 |
| `management-science-cn` | 《管理科学》 |
| `management-world` | 《管理世界》 |
| `modern-economic-research` | 《现代经济探讨》 |
| `modern-economic-science` | 《当代经济科学》 |
| `modern-finance-and-economics` | 《现代财经（天津财经大学学报）》 |
| `modern-financial-research` | 《现代金融研究》 |
| `nankai-business-review` | 《南开管理评论》 |
| `nankai-economic-studies` | 《南开经济研究》 |
| `organization-and-management` | 《组织与管理》 |
| `public-administration-and-policy-review` | 《公共管理与政策评论》 |
| `public-finance-research` | 《财政研究》 |
| `reform` | 《改革》 |
| `reform-of-economic-system` | 《经济体制改革》 |
| `research-and-development-management` | 《研究与发展管理》 |
| `research-on-economics-and-management` | 《经济与管理研究》 |
| `research-on-financial-and-economic-issues` | 《财经问题研究》 |
| `review-of-political-economy` | 《政治经济学评论》 |
| `rural-economy` | 《农村经济》 |
| `science-and-technology-progress-and-policy` | 《科技进步与对策》 |
| `science-of-science-and-management-of-st` | 《科学学与科学技术管理》 |
| `science-research-management` | 《科研管理》 |
| `scientific-decision-making` | 《科学决策》 |
| `scientific-management-research` | 《科学管理研究》 |
| `securities-market-herald` | 《证券市场导报》 |
| `shanghai-journal-of-economics` | 《上海经济研究》 |
| `social-sciences-in-china` | 《中国社会科学》 |
| `social-security-studies` | 《社会保障评论》 |
| `sociological-studies` | 《社会学研究》 |
| `soft-science` | 《软科学》 |
| `south-china-journal-of-economics` | 《南方经济》 |
| `studies-in-labor-economics` | 《劳动经济研究》 |
| `studies-in-science-of-science` | 《科学学研究》 |
| `studies-of-financial-economics` | 《金融经济学研究》 |
| `studies-of-international-finance` | 《国际金融研究》 |
| `systems-engineering-theory-and-practice` | 《系统工程理论与实践》 |
| `tax-research` | 《税务研究》 |
| `world-economic-papers` | 《世界经济文汇》 |
| `world-economic-studies` | 《世界经济研究》 |

## Source Discipline

Editorial rules change. The bundled [`resources/source-basis.md`](resources/source-basis.md) records the source policy used for this expansion, and [`resources/official-source-map.md`](resources/official-source-map.md) gives one official-source starting query per journal. Before final submission, always verify the live official 投稿须知 / 征稿简则 / 作者指南.
