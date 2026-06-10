---
name: ceq-abstract-english
description: Use when writing or polishing the English abstract and contribution statement for a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript — producing a tight English abstract (≤ ~100 words per the journal's guideline) that reads to a field economist and benchmarks the contribution against specific papers. Use at the polish stage, after identification and results are final.
---

# 英文摘要与贡献陈述（ceq-abstract-english）

## 触发时机

- 英文摘要质量差 / 中式英语 / 超长
- 贡献写成"This paper enriches the literature on…"
- 定稿前，主结果与识别已确定

## 为什么重要

CEQ 很多读者**只读英文摘要 + 图**（见 `ceq-figures`）。英文摘要 = 你的门面。它必须让 field 经济学家在 100 词内看懂：**问什么、怎么识别、发现什么、相对谁是新的**。CEQ 规范：英文摘要不超过约 100 个单词，三个中英文关键词，三个 JEL 号（详见 `resources/journal-profile.md`）。

## 五句法（控制在 ~100 词）

1. **问题**：研究的因果问题（一句，去本土包装）。
2. **设计**：识别来源（"Using the staggered rollout of …, we …"）。
3. **发现**：量化主结果 + 单位（"… raises Y by X%"）。
4. **机制**：一句话渠道。
5. **贡献/含义**：相对最近文献的差异，或一句政策/理论含义。

## 好坏对照

| 黑名单（中式/空话） | 白名单（field 可读） |
|---------------------|----------------------|
| "This paper enriches the literature." | "We provide the first credibly identified estimate of …" |
| "We use a series of robust methods." | "Using a regression discontinuity at the eligibility cutoff …" |
| "The results have important policy implications." | "A 10% increase in X reduces Y by 4%, implying …" |
| "Our study fills a gap in domestic research." | "Unlike Author (Year), who rely on OLS, we exploit …" |

## 英文写作规范

- 主动语态、现在时陈述发现；避免冗长从句。
- 量化结果带单位与符号方向，别只说"significant"。
- 术语用 field 标准词（identification, parallel trends, instrument），不要直译中文。
- 不堆方法名词；识别策略一句带过即可。
- 中英文摘要表意一致，但英文不必逐句直译中文。

## 自检清单

- [ ] 英文摘要 ≤ ~100 词（按官网规范复核）
- [ ] 五要素齐：问题/设计/发现/机制/贡献
- [ ] 主结果量化、带单位与方向
- [ ] 贡献对标具体文献，无 "enrich/fill the gap" 套话
- [ ] field 同行不读正文即可懂贡献
- [ ] 三个关键词、三个 JEL 号已备（见 `ceq-submission`）

## 反模式

- 英文摘要是中文摘要的机器直译
- 通篇 "significant" 不给数字
- 罗列方法却不说识别从哪来
- 用大词收尾（"profound implications"）替代具体含义

## CEQ 英文摘要的诊断—修法表

CEQ 不少读者只读英文摘要+图，摘要是国际索引里的门面。下表把常见症状映射到 field 可读的修法。词数与关键词/JEL 数量以编辑部最新稿约为准（现行约 ≤100 词、3 关键词、3 JEL）。

| 症状 | field 审稿人反应 | 修法 |
|------|------------------|------|
| 中文摘要机器直译 | 读着别扭、术语不对 | 按五句法重写，用 field 标准词 |
| 通篇 significant 无数字 | "效应多大？" | 量化主结果带单位与方向 |
| 罗列方法不说识别 | "因果凭什么？" | 一句点明外生变异来源 |
| 贡献=enrich/fill gap | "相对谁新？" | 对标具体文献写差异 |
| 超 ~100 词 | 超规、信息冗余 | 删机制以外的修饰，压回限额 |

## 微型走查：把中式直译改成 field 摘要

虚构稿件《社保征缴改归税务与企业用工》。初稿英文摘要是中文直译，超 130 词，满是 "significant"。按五句法重写（示意，词数仅演示）：

```
初稿（差）：This paper studies the significant impact of social
insurance collection reform on firms, using robust methods, and
finds significant effects with important policy implications. (≈130w，套话)

重写（五句法，≈92w）：
[问题] We ask how stricter enforcement of payroll-tax collection
affects firm employment.
[设计] Exploiting the staggered transfer of collection authority
to tax bureaus across provinces, we estimate effects with a
heterogeneity-robust DiD (Callaway–Sant'Anna).
[发现] Enforcement raises effective contribution rates and reduces
employment by about 2.1%.
[机制] The effect concentrates in labor-intensive, cash-constrained
firms, consistent with a labor-cost channel.
[贡献] Unlike prior work relying on OLS, we identify the causal
margin and the firms that bear it.
```

走查要点：重写后量化了 -2.1%、点明交错执法的外生来源、机制一句带过、贡献对标"prior work relying on OLS"。这正是 field 同行不读正文也能看懂的摘要。下一步过 `ceq-submission` 核词数与 JEL。

## 审稿人会怎么挑英文摘要

- "你说 significant，到底是多大？"——修法：把每个 significant 换成数值+单位+方向。
- "方法堆了一串，因果从哪来？"——修法：删方法名词，只留一句识别来源。
- "贡献写 enrich the literature，相对谁？"——修法：换成 "Unlike Author (Year)…we…" 的对标句（与 `ceq-literature-review` 一致）。

## 输出格式

```
【英文摘要词数】X / ≤100
【五要素】问题□ 设计□ 发现(量化)□ 机制□ 贡献□
【套话命中】X 处：[...]
【贡献对标】具体文献 □ / 仍套话（需改）
【关键词/JEL】3 关键词 □ 3 JEL □
【下一步】ceq-submission
```
