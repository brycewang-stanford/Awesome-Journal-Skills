# 婚姻与家庭杂志（JMF）技能包

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Marriage and Family 封面" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JMF-8c3a5a)](https://onlinelibrary.wiley.com/journal/17413737)
[![Field](https://img.shields.io/badge/field-家庭科学-1f6feb)](https://www.ncfr.org/jmf)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

[English](README.md) | 简体中文

面向 **《婚姻与家庭杂志》（Journal of Marriage and Family, JMF）** 投稿的 Agent 技能栈。JMF 是
**家庭科学领域的旗舰跨学科期刊**，创刊于 **1939 年**，由 **Wiley** 出版、代表 **美国家庭关系理事会
（NCFR）**。它发表关于 **婚姻、亲密关系与家庭** 的研究、理论、解读与批判性讨论：家庭人口学、婚姻与
结合、离婚与关系解体、同居与生育、养育与儿童福祉、代际与亲密关系、性别，以及家庭政策——融合
**社会学、心理学、人口学与家庭研究**，定量、定性与混合方法兼收并蓄。

本仓库是**有主见的**。它**不是**通用社会科学写作工具箱，**也不是**把政治学或经济学包改个名字套用到
家庭研究。它是 **JMF 专属** 技能栈：一个真正的**家庭科学贡献**、一个取自家庭文献的概念框架、尊重
**分析单位**（个体、二元体/配偶、家庭、家户、队列）与共享关系者之间**非独立性**的研究设计、**双向匿名**
的稿件准备，以及为家庭研究常依赖的**受限使用（restricted-use）数据集**而构建的透明度方案。

---

## JMF 是什么，为何需要专属技能栈？

JMF 的约束不同于通用社会学、心理学或经济学期刊：

| 约束 | JMF | 含义 |
|------|------|------|
| 范围 | **家庭与亲密关系**——跨学科的家庭科学 | 家庭/配偶/亲子关系必须居于核心 |
| 看重 | 对**理解家庭**的贡献，兼具理论与意义 | 家庭只是顺带提及的泛化结果不合适 |
| 学科 | **社会学 + 心理学 + 人口学 + 家庭研究** | 跨学科回应家庭文献，而非只顾本学科 |
| 方法 | 定量/定性/混合方法——各按其标准评判 | 设计与分析单位要匹配；尊重非独立性 |
| 出版方 / 所有者 | **Wiley** / **NCFR** | 通过 **Wiley Research Exchange** 投稿（已从 ScholarOne 迁移） |
| 评审模式 | **双向匿名** | 彻底匿名化；去除姓名、单位、致谢 |
| 篇幅 | 稿件 **≤ 约 35 页**；**简报 ≤ 约 25 页**（含表/图） | 页数预算含图表；多用补充材料 |
| 摘要 | **结构化，约 200–225 词**（目的/背景/方法/结果等） | 非自由段落；评审人凭摘要受邀 |
| 体例 | **改良版 APA**；无偏见语言 | 非泛用 Chicago；精准描述家庭形态 |
| 透明度 | 可复现级别细节 + **数据可得性声明**（Wiley 政策） | 为受限数据规划：获取路径 + 合成数据 |

本包中的期刊事实已映射到
[`resources/official-source-map.md`](resources/official-source-map.md) 中的 NCFR / Wiley 来源。真正上传前，
仍需现场检查官方页面上的易变操作信息，例如投稿入口、费用、当前编辑名单、文件要求和期刊专属政策更新。

### 两种稿件形式

- **Article（论文）**——完整的原创研究，框架与分析充分展开；**≤ 约 35 页**，含摘要、正文、表格与图。
- **Brief Report（简报）**——一个精炼而完整的贡献；**≤ 约 25 页**。JMF 明确欢迎以简报形式提交
  **复现、创新设计与重要的零结果（null findings）**。

---

## 快速开始

### 方式 A — Claude Code 插件（推荐）

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jmf-skills
/plugin install jmf-skills
/reload-plugins
```

### 方式 B — 手动复制

```bash
git clone https://github.com/brycewang-stanford/jmf-skills.git
cd jmf-skills

mkdir -p ~/.claude/skills && cp -R skills/jmf-* ~/.claude/skills/
# 或
mkdir -p ~/.codex/skills && cp -R skills/jmf-* ~/.codex/skills/
```

### 第一条提示

```
用 jmf-workflow 告诉我，我的《婚姻与家庭杂志》稿件下一步该用哪个技能。
```

---

## 默认工作流

```text
jmf-topic-selection
        ▼
jmf-literature-positioning
        ▼
jmf-theory-and-conceptual-framework
        ▼
jmf-research-design
        ▼
jmf-data-analysis
        ▼
jmf-tables-figures
        ▼
jmf-writing-style          （润色）
        ▼
jmf-transparency-and-data-policy
        ▼
jmf-review-process
        ▼
jmf-submission
        ▼
jmf-rebuttal
```

`jmf-workflow` 是路由器——根据你所处阶段告诉你下一步用哪个技能。若设计是**前瞻性**的，尽早走
`jmf-research-design` 锁定预分析计划；若是重新评估已发表发现或报告重要零结果，考虑 **Brief Report** 形式。

---

## 技能列表

| 技能 | 用途 |
|------|------|
| `jmf-workflow` | 路由器——决定下一步调用哪个子技能 |
| `jmf-topic-selection` | 跨学科的家庭科学契合；论文 vs. 简报 |
| `jmf-literature-positioning` | 跨社会学/心理学/人口学回应家庭文献 |
| `jmf-theory-and-conceptual-framework` | 构建家庭科学框架（生命历程、家庭压力、交换……） |
| `jmf-research-design` | 纵向、二元、家庭层级与人口学设计；处理选择性 |
| `jmf-data-analysis` | 调查权重、非独立性、缺失数据、稳健性、效应量 |
| `jmf-tables-figures` | 改良 APA 下自洽、可读的图表；管理页数预算 |
| `jmf-writing-style` | 改良 APA；结构化摘要；无偏见语言；触达全领域 |
| `jmf-transparency-and-data-policy` | 可复现细节、数据可得性声明、受限数据路径 |
| `jmf-review-process` | 双向匿名评审、评审/编辑角色、R&R 流程 |
| `jmf-submission` | Wiley Research Exchange 投稿前检查（匿名、摘要、页数） |
| `jmf-rebuttal` | 面向多位匿名评审 + 编辑的 R&R 回应信策略 |

### 资源

- [`resources/external_tools.md`](resources/external_tools.md) — 家庭科学数据源（PSID / NLSY / Add Health / Fragile Families / NSFG / HRS / pairfam / IPUMS）+ R / Stata / Python 的二元、纵向、生存与调查工具
- [`resources/official-source-map.md`](resources/official-source-map.md) — 本包期刊专属事实背后的 NCFR / Wiley 官方 URL

---

## 本仓库不做什么

- 不替你写出可直接投稿的稿件
- 不模拟任何特定编辑或评审人的口味
- 不替代最终上传前对操作性元数据（投稿入口、费用、当前编辑名单、文件要求、政策措辞）的现场检查
- 不替你判断你的问题是否构成真正的家庭科学贡献——那是研究者的判断

---

## 相关

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — 期刊专属技能包索引
- [Journal of Marriage and Family（Wiley Online Library）](https://onlinelibrary.wiley.com/journal/17413737) — 出版方主页
- [NCFR 上的 JMF](https://www.ncfr.org/jmf) — 所有者、投稿指南、体例指南、评审政策

---

## 许可

MIT
