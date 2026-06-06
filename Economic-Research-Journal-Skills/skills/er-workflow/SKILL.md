---
name: er-workflow
description: Use when deciding which er-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for 《经济研究》 (Economic Research Journal). Routes — does not replace — the specialized skills.
---

# 经济研究工作流（er-workflow）

## 总览

这是路由器，它不替代任何专用 Skill。它告诉你**当前阶段应该用哪一个 er-* skill**。

默认假设：除非用户明确说明目标期刊不是《经济研究》，否则按 CSSCI《经济研究》的编委口味处理。

工具定位为**「生成 + 诊断」双模**：既能诊断当前稿件的瓶颈、给出可填模板，也能直接产出引言、机制段、摘要、回复信等初稿段落供你修改。

## 触发时机

- 用户问"我下一步该做什么？"
- 用户甩过来一份初稿，需要判断当前瓶颈
- 实证、写作、回复来回切，状态混乱
- 收到了《经济研究》的外审意见，需要切换到 rebuttal 模式

## 路由表

| 当前症状                                          | 下一个 Skill                  |
|----------------------------------------------|---------------------------|
| 选题想法模糊，担心理论贡献不够                       | `er-topic-selection`      |
| 引言从遥远背景写起 / 没剧透结论 / 贡献写成"丰富研究"   | `er-introduction`         |
| 文献综述缺中文经典 / 缺理论文献                       | `er-literature-review`    |
| 缺理论分析与假设推导 / 假设无方向、不可证伪            | `er-theory-hypotheses`    |
| 数据来源含糊 / 变量定义用描述不给公式 / 样本筛选不透明  | `er-data-sample`          |
| 实证只有 OLS / 交叠 DID 只用 TWFE / 弱工具          | `er-identification`       |
| 主结果有了，但没机制分析（或还在跑中介三步法）          | `er-mechanism`            |
| 没切异质性 / 切分维度无理论指引                       | `er-heterogeneity`        |
| 缺稳健性 / 换度量或样本结论就翻                       | `er-robustness`           |
| 表格列数过多 / 注释不规范 / 手抄表格                  | `er-tables-figures`       |
| 文末没有政策含义，或写得太"操作化"                    | `er-policy-implication`   |
| 摘要写成套话 / 英文梗概不合五要素 / 中英不对齐         | `er-abstract`             |
| 通篇空话套话 / 政策建议是"加强完善推进"四件套         | `er-style`                |
| 投稿前想先过一遍高频审稿质疑、堵漏洞                  | `er-reviewer-lens`        |
| 数据代码乱、无法一键复现、扩展资料没准备好            | `er-reproducibility`      |
| 准备投稿，需要 checklist                            | `er-submission`           |
| 收到 R&R，需要写回复信                              | `er-rebuttal`             |

## 默认顺序

1. `er-topic-selection` — 先把"理论贡献 + 中国问题"定下来
2. `er-introduction` — 搭引言漏斗框架（后期 polish 再回炉）
3. `er-literature-review` — 中英文献并重，理论文献必引
4. `er-theory-hypotheses` — 理论分析与可检验假设
5. `er-data-sample` — 数据说明、变量定义表、描述统计
6. `er-identification` — 准实验识别（现代估计量）
7. `er-mechanism` — 机制路径（D→M + 理论论证 M→Y）
8. `er-heterogeneity` — 异质性切分
9. `er-robustness` — 稳健性检验体系
10. `er-tables-figures` — 主表 / 主图最终化（代码导出）
11. `er-policy-implication` — 政策含义（意义层）
12. `er-abstract` — 中文提要 + 英文梗概五要素（polish）
13. `er-style` — 全文语言风格 polish
14. `er-reviewer-lens` — 投稿前高频质疑自检
15. `er-reproducibility` — 整理一键复现包与扩展资料
16. `er-submission` — 投稿前 preflight
17. `er-rebuttal` — 外审后

> `er-introduction` / `er-abstract` / `er-style` 含**后段 polish**性质：识别策略未立住前，不必反复打磨措辞。

## 决策口诀

- "我有数据但没理论故事" → `er-topic-selection`
- "引言第一段还在写'随着……的发展'" → `er-introduction`
- "综述里没引 North / Acemoglu / 林毅夫" → `er-literature-review`
- "有现象但讲不清为什么会有这个效应（事前）" → `er-theory-hypotheses`
- "变量定义写的是'反映 XX'而不是公式" → `er-data-sample`
- "DID 用了 TWFE 但没回应异质性处理偏误" → `er-identification`
- "我还在跑中介三步法 / Sobel" → `er-mechanism`（已被弃用，改 D→M）
- "异质性只切了东中西" → `er-heterogeneity`
- "审稿人会说'换个度量结论还在吗'" → `er-robustness`
- "主表 8 列以上 / 表是手抄的" → `er-tables-figures`
- "我建议政府重视该问题" → `er-policy-implication`
- "摘要里没有量化结果 / 英文摘要是中文逐句翻译" → `er-abstract`
- "全文'具有重要意义'命中 ≥ 3 处" → `er-style`
- "明天就要投了，先自检一遍" → `er-reviewer-lens` → `er-submission`
- "收到 3 份审稿意见" → `er-rebuttal`

## 与《管理世界》Skills 的差异

如果稿子偏管理学 / 案例 / 实务，使用 [management-world-skills](https://github.com/brycewang-stanford/management-world-skills) 更合适：

- 《经济研究》：理论贡献优先，政策含义偏意义层
- 《管理世界》：实践契合优先，政策建议偏可操作

## 反模式

- **不要**跳过 `er-theory-hypotheses` / `er-literature-review` 直接进识别——审稿人首先看理论定位
- **不要**让 `er-tables-figures` 在识别策略未立住时就美化表格
- **不要**让 `er-rebuttal` 在你修订正文之前生成回复信
- **不要**把 `er-reviewer-lens` 当成投稿后才看的东西——它是投稿前的镜子
