---
name: ceq-inference
description: Use when scrutinizing statistical inference for a 《经济学(季刊)》 (China Economic Quarterly, CEQ) manuscript — choosing and justifying the clustering level, handling weak instruments with robust inference, correcting for multiple hypothesis testing, and reporting standard errors that survive a technical reviewer. Default robust SEs are rarely enough at CEQ.
---

# 推断细节（ceq-inference）

## 触发时机

- 标准误用了默认稳健，但没说聚类层级理由
- 第一阶段 F 偏低 / 工具偏弱
- 跑了大量子样本/异质性，没做多重检验校正
- 审稿人会逐条挑推断的稿子

## CEQ 视角：推断是技术审稿的主战场

海外训练的审稿人会盯：**聚类层级、弱工具、多重检验、有限样本**。点估计漂亮但推断站不住，照样退。

## 1. 聚类层级（要给理由，不是默认）

- 聚类应与**处理/抽样的层级**一致：处理在省级，就省级聚类（即使样本在个体）。
- 簇数太少（< ~30–50）→ 用 wild cluster bootstrap（Cameron-Gelbach-Miller）。
- 面板同时考虑双向聚类（个体 + 时间）是否必要。
- [ ] 聚类层级与处理分配层级一致，且写明理由
- [ ] 少簇情形用 wild bootstrap

## 2. 弱工具（IV）

- 第一阶段 F 报告；多工具用 Kleibergen-Paap（非同方差稳健）而非简单 F。
- F 偏弱 → 用 **Anderson-Rubin** 等 weak-IV-robust 置信区间，别只靠 t 比。
- 报告 reduced form 与第一阶段，别只给 2SLS。
- [ ] F / KP 报告；弱则给 AR 区间
- [ ] reduced form 与第一阶段都展示

## 3. 多重假设检验

- 跑了多个结果变量 / 多个子组 → Romano-Wolf、List-Shaikh-Xu，或 BH/Bonferroni 校正。
- 异质性"找显著"要预警 p-hacking；最好预先登记或限制切分维度。
- [ ] 多结果/多子组已做 MHT 校正
- [ ] 异质性切分有理论依据，非数据挖掘

## 4. 标准误与有限样本

- DID 现代估计量用其配套（解析或 bootstrap）标准误，别套 TWFE 的。
- 小样本/少处理单位 → 随机化推断（permutation / placebo 分布）。
- [ ] 估计量与标准误匹配
- [ ] 必要时随机化推断

## 反模式

- "标准误聚类到个体层"但处理在省级——典型低估
- 只报 2SLS t 值，不管弱工具
- 报告 20 个异质性里挑出的 2 个显著，不做校正
- 现代 DID 估计量配 TWFE 标准误

## CEQ 技术审稿的推断扣分表

下表把本刊技术审稿最常打的推断漏洞，映射到"严重度"与第一时间的补救动作。严重度按本刊经验排序：聚类与弱工具几乎是硬伤，措辞类问题相对软。具体审稿尺度因稿件而异，以编辑部最新稿约与外审意见为准。

| 推断漏洞 | 严重度 | 第一补救 |
|----------|--------|----------|
| 聚类层级低于处理分配层级 | 高（多半要求重估） | 上提到处理层级；少簇配 wild bootstrap |
| 弱工具只报 t 值 | 高 | 报 KP F，给 Anderson-Rubin 区间 |
| 多结果/多子组不校正 | 中高 | Romano-Wolf 或 BH，标注族范围 |
| 现代 DID 套 TWFE 标准误 | 中高 | 改用估计量配套解析/bootstrap SE |
| 少处理单位不做随机化推断 | 中 | placebo 置换分布报精确 p |
| 只给点估计不给区间 | 低中 | 全表补 CI，正文报关键区间 |

## 微型走查：省级政策、个体面板的聚类陷阱

虚构稿件《自贸区扩围与企业全要素生产率》。处理在省（自贸区批次），数据在企业-年。作者初稿聚类到企业层，t 值都很漂亮。按本 skill 重做（示意数字，仅演示推断如何翻转）：

```
初稿：企业层聚类，β=0.061，SE=0.012，t=5.1（看似稳）
问题：处理在省级，企业层聚类低估了组内相关 → t 被夸大
重估：省级聚类后 SE=0.034，t=1.8（边缘显著）
省份数仅 14（簇数 < 30）→ 默认渐近不可靠
wild cluster bootstrap（Webb 权重，B=9999）：p=0.094
弱工具旁证：若用"距口岸距离×政策时点"作工具，
            KP F=6.7（弱）→ Anderson-Rubin 95% CI 含 0
结论：主效应在正确推断下不稳，需扩样本或换更强设计
```

走查要点：聚类层级一改，结论从"显著"变"边缘"——这正是 CEQ 审稿人第一刀的位置。诚实报告少簇 bootstrap 与 AR 区间，远胜硬撑 t 值。

## 审稿人追问模式与本刊语境修法

- "你为什么聚类到这一层？"——修法：写明聚类层级=处理/抽样层级，并报少簇 bootstrap，而非辩称"惯例如此"。
- "多个异质性结果里你挑了显著的，做了校正吗？"——修法：声明族范围、给 Romano-Wolf 校正后 p 值，并说明切分维度的理论先验（接 `ceq-mechanism`）。
- "弱工具下 t 检验失效，AR 区间是多少？"——修法：报 AR/CLR 区间，承认弱工具，必要时退回 reduced form 讨论。

## 输出格式

```
【聚类层级】... | 与处理层级一致 □ | 少簇 bootstrap □
【弱工具】F/KP=... | AR 区间 □ | reduced form □
【多重检验】结果数=.. 子组数=.. | 校正方法=..
【标准误-估计量匹配】是 / 否
【缺口】<待补>
【下一步】ceq-mechanism
```
