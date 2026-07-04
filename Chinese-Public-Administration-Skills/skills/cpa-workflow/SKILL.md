---
name: cpa-workflow
description: Use when deciding which cpa-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《中国行政管理》 (Chinese Public Administration). Routes — does not replace — the specialized skills.
---

# 中国行政管理工作流（cpa-workflow）

## 总览

这是路由器，它不替代任何专用 Skill。它告诉你**当前阶段应该用哪一个 cpa-* skill**。

默认假设：除非用户明确说明目标期刊不是《中国行政管理》，否则按中国行政管理学会主办、CSSCI 来源期刊《中国行政管理》的编委口味处理——**公共行政 / 公共管理学科，方法上定量与定性并重，须有公共管理理论框架**。

## 触发时机

- 用户问"我下一步该做什么？"
- 用户甩过来一份初稿，需要判断当前瓶颈
- 在研究设计、写作、政策含义、回复之间来回切，状态混乱
- 收到了《中国行政管理》的匿名评审意见，需要切换到 rebuttal 模式

## 路由表

| 当前症状                                          | 下一个 Skill                  |
|----------------------------------------------|---------------------------|
| 选题宏大空泛，缺公共管理理论定位 / 落不成可研究的问题   | `cpa-topic-selection`     |
| 综述缺公共管理理论文献 / 缺中国治理文献 / 罗列式      | `cpa-literature-review`   |
| 研究设计与问题不匹配 / 方法粗糙（仅描述性 + 主观判断） | `cpa-identification`      |
| 有结论但缺治理 / 政策过程机制                      | `cpa-mechanism`           |
| 没切跨地区 / 层级 / 治理情境差异                    | `cpa-heterogeneity`       |
| 表格列数过多 / 编码表缺失 / 机制图不规范             | `cpa-tables-figures`      |
| 文末是"强化 / 完善 / 健全 / 推进"四件套或空泛对策    | `cpa-policy-implication`  |
| 摘要写成套话 / 没说清问题方法发现 / 中英不对齐        | `cpa-abstract`            |
| 通篇对策套话、无理论支撑 / 命中黑名单短语            | `cpa-style`               |
| 准备投稿，需要 checklist                          | `cpa-submission`          |
| 收到外审意见，需要写回复信                          | `cpa-rebuttal`            |

## 默认顺序

1. `cpa-topic-selection` — 先把"理论框架 + 可研究的中国治理问题"定下来
2. `cpa-literature-review` — 公共管理理论与中国治理文献并重，对话式综述
3. `cpa-identification` — 研究设计：定量 / 定性 / 规范，方法与问题匹配
4. `cpa-mechanism` — 治理 / 政策过程机制
5. `cpa-heterogeneity` — 跨情境差异 / 条件性
6. `cpa-tables-figures` — 主表 / 编码表 / 机制图最终化
7. `cpa-policy-implication` — 政策含义（可操作但有据）
8. `cpa-abstract` — 摘要四段法 + 黑名单短语清除
9. `cpa-style` — 全文语言风格 polish
10. `cpa-submission` — 投稿前 preflight
11. `cpa-rebuttal` — 外审后

> `cpa-abstract` 与 `cpa-style` 是**后段 polish 阶段**触发，不要在研究设计未立住时去做。

## 路由诊断卡

不确定卡在哪一环时，逐题作答；**遇到第一个"否"就停**，右侧即下一个 skill：

```text
【《中国行政管理》路由诊断卡】
Q1  理论框架能用一句话说出（框架名=____）？        否 → cpa-topic-selection
Q2  综述在与公共管理理论"对话"而非罗列？          否 → cpa-literature-review
Q3  方法与问题匹配（定量/定性/规范，选=____）？    否 → cpa-identification
Q4  治理或政策过程的机制黑箱已打开？              否 → cpa-mechanism
Q5  跨地区/层级/治理情境的条件性已分析？          否 → cpa-heterogeneity
Q6  主表、资料编码表、机制图均已规范？            否 → cpa-tables-figures
Q7  政策建议有分析支撑且可操作？                  否 → cpa-policy-implication
Q8  摘要含"问题—方法—发现"三要素？               否 → cpa-abstract
Q9  全文黑名单短语命中 0 处？                     否 → cpa-style
Q10 投稿 checklist 全部通过？                     否 → cpa-submission
（已收到匿名评审意见 → 跳过 Q1–Q10，直接 cpa-rebuttal）
```

- "我有个大题目但不知怎么落地" → `cpa-topic-selection`
- "综述里没引治理 / 政策过程 / 街头官僚的经典" → `cpa-literature-review`
- "我做了问卷但只跑了描述统计 / 案例只是讲故事" → `cpa-identification`
- "我只能说'政策大概起了作用'，说不清怎么起作用" → `cpa-mechanism`
- "效应在哪些地区 / 层级更强我没分析" → `cpa-heterogeneity`
- "主表 8 列以上 / 案例没有资料编码表" → `cpa-tables-figures`
- "结尾全是'加强、完善、健全、推进'" → `cpa-policy-implication`
- "摘要里没有研究问题和方法" → `cpa-abstract`
- "全文'具有重要意义'命中 ≥ 3 处" → `cpa-style`
- "明天就要投了" → `cpa-submission`
- "收到匿名评审意见" → `cpa-rebuttal`

## 与经济学期刊 Skills 的差异

如果稿子本质是经济学（强调因果识别、经济理论、政策意义层启示），用 [Economic-Research-Journal-Skills](https://github.com/brycewang-stanford/economic-research-skills) 更合适。两者核心差异：

- 《中国行政管理》：公共管理理论框架优先；方法定量定性并重；政策含义面向政府实践、更可操作但须有据
- 《经济研究》：经济学理论 + 准实验识别优先；政策含义偏意义 / 制度层

## 反模式

- **不要**跳过 `cpa-topic-selection` 直接进研究设计——审稿人首先看理论定位与问题是否可研究
- **不要**把准实验方法硬套到本质是规范 / 案例的问题上——方法必须服务于问题
- **不要**让 `cpa-policy-implication` 在没有分析支撑时写"对策四件套"
- **不要**让 `cpa-rebuttal` 在你修订正文之前生成回复信
