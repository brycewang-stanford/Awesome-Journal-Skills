---
name: jqte-fit-positioning
description: Use to judge whether a manuscript fits 《数量经济技术经济研究》 (JQTE) and to decide how to frame its contribution — measurement, forecasting, or method-application versus clean causal inference — before investing in revision. The most common save: stopping a strong measurement paper from being dressed up as a weak causal study, and routing genuinely clean-causal work elsewhere.
---

# 匹配度与贡献定位（jqte-fit-positioning）

## 触发时机

- 还没动笔大改前，先问"这篇对不对口、贡献该怎么框"
- 有 TFP/效率/预测/分解结果，但不确定要不要包装成因果
- 识别其实很干净，纠结投本刊还是经济研究/季刊

## 第一步：判定贡献类型（决定全文骨架）

| 贡献类型 | 特征 | 本刊匹配度 |
|----------|------|-----------|
| 测度 | TFP/效率/指数/技术进步分解的"量得准" | 高 |
| 预测 | 宏观计量、景气、混频、政策模拟的"测得好" | 高 |
| 方法应用/改进 | 前沿计量用到中国数据并讲清适用条件 | 高 |
| 结构分解 | IO/CGE/SDA 的"分解清、可复现" | 高 |
| 干净因果 | 强识别 + 理论机制是核心卖点 | 中/低（多半改投） |

> 本刊隐性门槛：**测度透明、方法得当、可复现 > 因果叙事的干净度**。识别弱却硬包装因果，是高频拒因。

## 三道筛子（任一不过即高风险）

1. **核心可量化吗**：本文的贡献能落到一个"量/预测/分解得更好"的具体对象吗？还是只有一个泛泛的实证回归？
2. **方法节立得住吗**：构造/设定/参数是否透明、可复现，而非黑箱跑软件？
3. **是不是硬凑因果**：去掉勉强的因果话术后，测度/方法本身还成立且有价值吗？（若是，就老实做测度）

## 匹配度评级

| 评级 | 特征 | 处置 |
|------|------|------|
| 高 | 测度/预测/分解为核 + 方法透明可复现 | 进入 `jqte-topic-selection` 精修 |
| 中 | 方向对但方法节单薄 / 因果话术过重 | 先补 `jqte-measurement`/`jqte-io-cge`，并去掉硬凑因果 |
| 低 | 干净因果是真卖点 / 纯算法贡献 / 题目琐碎 | 改投对口期刊（见下） |

## 改投路由（fit 低时）

- 干净因果 + 理论：`economic-research` / `china-economic-quarterly`
- 产业/政策实证 + 厚稳健性：`china-industrial-economics`
- 数理模型/算法本身是贡献：`journal-of-management-sciences-china`

## 自检清单

- [ ] 能一句话说清贡献类型（测度/预测/方法/分解/因果）
- [ ] 贡献能落到"量/预测/分解得更好"的具体对象
- [ ] 方法节透明可复现，不是黑箱
- [ ] 没有为了"上档次"硬凑站不住的因果故事

## 反模式

- 给测度论文硬套 DID/IV 叙事——审稿人会问"识别站得住吗"，不如老实做测度
- 把"跑了个回归"当成够格——本刊看重方法与测度的扎实，不是回归本身
- 识别其实很干净却投本刊——清晰因果应去经济研究/季刊

## 输出格式

```
【匹配度】高 / 中 / 低（一句话理由）
【贡献类型】测度 / 预测 / 方法应用 / IO-CGE分解 / 因果
【方法节】透明可复现 / 单薄黑箱（需补）
【因果话术】无 / 适度 / 硬凑（需去掉）
【建议】精修本刊 / 先补方法 / 改投 <期刊>
【下一步】jqte-topic-selection
```
