---
name: mw-identification
description: Use when the empirical identification strategy is the bottleneck for a Management-World manuscript — quasi-experimental designs (DID, IV, RDD, DML, event study) with Chinese policy shocks. Stress-tests the design before drafting tables.
---

# 因果识别策略（mw-identification）

## 触发时机

- 实证主体仅有 OLS + 控制变量，担心被退稿
- DID 用了 TWFE 但没回应近年异质性处理批评（Goodman-Bacon, de Chaisemartin, Sun-Abraham, Callaway-Sant'Anna）
- IV 第一阶段 F 弱 / 工具变量内生性疑虑
- 准备用双重机器学习但不确定怎么报告

## 设计优先级

《管理世界》编委的偏好排序（强 → 弱）：

1. **政策冲击 + DID（含 staggered / continuous treatment）**
2. **断点回归（清晰的政策门槛）**
3. **工具变量（强工具 + 排他性论证）**
4. **倾向得分匹配 + DID**
5. **合成控制法**
6. **双重机器学习 / 因果森林**
7. OLS + 内生性讨论（容易退稿）

## 分支路径

### 分支 A：DID

- 是否 staggered？→ 必须用 Goodman-Bacon 分解 + Callaway-Sant'Anna 或 Sun-Abraham
- 平行趋势检验：事件研究图必须画
- 安慰剂：随机分配处理组 500–1000 次
- 是否汇报 Bacon 分解的"坏比较"权重？

### 分支 B：IV

- 第一阶段 F **必须 ≥ 10**（弱工具 → 用 Anderson-Rubin 或 weak-IV-robust CI）
- 排他性论证至少需要 3 段：理论 / 制度 / 安慰剂
- 是否报告了 reduced form？

### 分支 C：RDD

- 是否做了 McCrary 检验？
- 带宽：是否使用最优带宽（Calonico-Cattaneo-Titiunik）+ 至少 3 个带宽稳健性？
- 协变量平滑性检验

### 分支 D：DML

- 报告 sample-split 数 + cross-fitting
- 报告 nuisance 函数选择（lasso / random forest / xgboost）
- 至少给出 5 种不同 ML 学习器的稳健性

## 必查清单

- [ ] 平行趋势 / 平滑性 / 弱工具 检验都做了
- [ ] 安慰剂检验做了（处理时点随机 / 处理对象随机）
- [ ] 主回归的标准误聚类层次合理（个体 / 个体+时间 / 处理层级）
- [ ] 是否有"两阶段"识别（先确认外生性，再估处理效应）
- [ ] 是否回应了"被处理者预期"问题

## 反模式

- TWFE + staggered 但不讨论异质性处理偏误
- IV 用"外生事件 × 上一期内生变量"——审稿人会问"为何上一期不影响当期"
- "我们认为该政策外生于公司决策"但没给证据
- RDD 用了截断带宽但不汇报带宽敏感性

## 输出格式

```
【识别策略】DID / IV / RDD / DML / 其他
【已完成检验】[平行趋势, 安慰剂, 弱工具, ...]
【缺失检验】[...]
【聚类层次】...
【下一步】mw-mechanism-heterogeneity
```
