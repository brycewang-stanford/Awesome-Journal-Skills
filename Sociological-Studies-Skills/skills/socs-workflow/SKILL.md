---
name: socs-workflow
description: Use when deciding which socs-* sub-skill to invoke next, or when sequencing manuscript work from problematic framing through rebuttal for 《社会学研究》 (Sociological Studies). Routes — does not replace — the specialized skills, and re-routes off-discipline drafts to other journal packs.
---

# 《社会学研究》工作流（socs-workflow）

## 总览

这是路由器，不替代任何专用 skill。它告诉你**当前阶段该用哪个 socs-* skill**。

默认假设：目标是国内社会学第一刊《社会学研究》（中国社会科学院社会学研究所主办，双月刊）。该刊**定量与定性双传统并重**，共同门槛是**社会学问题意识 + 与社会学理论的实质对话**，而非干净因果识别。基础事实见 `resources/journal-profile.md`。

## 触发时机

- 用户问"这篇能不能投《社会学研究》/ 下一步做什么"
- 手头有 CGSS/CFPS/CLDS 回归结果，或田野/访谈材料，但讲不出社会学问题意识
- 稿子读起来像"经济学实证 + 政策建议"，担心问题意识缺位
- 不确定定量稿与定性稿分别怎么写到位
- 收到外审意见需要回复

## 路由表

| 当前症状 | 下一个 Skill |
|----------|-------------|
| 不确定对不对口、像不像社会学 | `socs-fit-positioning` |
| 只有"X 影响 Y"，立不住社会学问题 | `socs-problematic` |
| 文献只堆近年实证、没进社会学理论脉络 | `socs-theory-dialogue` |
| 定量：有系数没社会学解读，陷入识别军备竞赛 | `socs-quantitative` |
| 定性：田野/访谈材料，编码与可信度没规范 | `socs-qualitative` |
| 系数/材料没翻译成"社会过程" | `socs-mechanism-social-process` |
| 材料丰富但没提炼出概念/机制 | `socs-concept-building` |
| 通篇政策汇报腔 / 纯技术腔 | `socs-style` |
| 摘要写成套话 / 超 200 字 / 关键词不对 | `socs-abstract-keywords` |
| 准备投稿，需要体例与系统 checklist | `socs-submission` |
| 收到外审意见，需要写回复 | `socs-rebuttal` |

## 默认顺序

1. `socs-fit-positioning` — 先判断是不是社会学问题，别把政策评估硬投
2. `socs-problematic` — 立住社会学问题意识
3. `socs-theory-dialogue` — 进入经典与当代社会学理论脉络
4. `socs-quantitative` **或** `socs-qualitative` — 按路径做规范（可混合）
5. `socs-mechanism-social-process` — 把证据翻译成社会过程
6. `socs-concept-building` — 定性稿尤其要从材料提炼概念
7. `socs-style` — 学理文风，去政策腔与技术腔
8. `socs-abstract-keywords` — 摘要 ≤ 200 字 + 3–5 关键词
9. `socs-submission` — 投稿前 preflight（文中夹注、文末参考文献、唯一投稿系统）
10. `socs-rebuttal` — 外审后

## 决策口诀

- "我有系数但没社会学故事" → `socs-problematic` + `socs-mechanism-social-process`
- "田野材料一大堆但没概念" → `socs-concept-building`
- "文献全是近五年回归，没社会学经典" → `socs-theory-dialogue`
- "读起来像政策文件" → `socs-style`

## 路由走查示例（两种典型稿件，数字为示意）

把路由表用在两份具体稿件上，演示如何按症状逐站派发：

```
稿件 A（定量·CFPS 流动人口子女教育）：
  症状：有事件史回归结果，辍学风险约 1.8 倍（示意），但落点写成政策建议。
  路由：
    1) socs-fit-positioning  → 删政策测试：问题塌掉 → 先改造为社会学问题
    2) socs-problematic      → 立"户籍墙的制度筛选"问题意识
    3) socs-theory-dialogue  → 进入分层/机会结构脉络，修正"资源补偿论"
    4) socs-quantitative     → 异质性按制度位置切，操作化户籍为制度身份
    5) socs-mechanism-...    → 翻译成"筛选—固化—再生产"社会过程
    6) socs-style            → 删政策腔结论
    7) socs-abstract-keywords→ 命题前置摘要 ≤200 字
    8) socs-submission       → 夹注/脚注/匿名 preflight

稿件 B（定性·基层治理田野）：
  症状：蹲点 11 个月（示意），故事生动但"没概念、没抓手"。
  路由：
    1) socs-fit-positioning  → 确认是社会学问题（治理实践，非政策评估）
    2) socs-problematic      → 立"指标压力下的执行变形"问题
    3) socs-qualitative      → 补编码透明、反身性、负面案例
    4) socs-concept-building → 提炼「悬置式执行」概念（核心贡献）
    5) socs-theory-dialogue  → 与街头官僚理论对话（修正/扩展）
    6) socs-mechanism-...    → 写出"形式吸纳—实质延迟"机制
    7) socs-style / abstract / submission → 收尾
```

二者共享同一骨架，但定量稿重"机制翻译 + 异质性"，定性稿重"概念提炼 + 可信度"。

## 与本仓库其它期刊包的差异（关键再路由）

- **跨学科大命题**（制度/文明/治理层面的原创理论）→ 转 social-sciences-in-china（《中国社会科学》）
- **经济因果 + 政策评估**（干净识别、政策含义为落点）→ 转 economic-research（《经济研究》）或 china-industrial-economics（《中国工业经济》）
- 《社会学研究》要的是**社会学问题意识 + 理论对话**，定量/定性都是证据手段，方法不是贡献本身

## 反模式

- **不要**跳过 `socs-fit-positioning` 就动笔——它最常救稿（避免把政策评估投错门）
- **不要**在没有社会学问题意识时去抠摘要和文风
- **不要**让 `socs-rebuttal` 在正文未修订前生成回复
