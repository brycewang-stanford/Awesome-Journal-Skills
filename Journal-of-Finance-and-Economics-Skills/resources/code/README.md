<!-- 自 Economic-Research-Journal-Skills/resources/code 引入（Stata 18 MP 已实跑验证，2026-06），用于 Journal-of-Finance-and-Economics-Skills 自包含。命令以规范源为准，勿在此处擅改。 -->
# 代码模板库（Stata + Python）

> ✅ **已验证**：核心命令链已在 Stata 18 MP 上用合成数据实跑通过——`reghdfe`(TWFE)、`bacondecomp`、`csdid`、`did_imputation`、事件研究 + 平行趋势联合检验、`esttab` 三线表导出、`ivreg2`+KP rk F、`weakivtest` 有效 F、`rdrobust`、`rddensity` 均正常运行（2026-06）。注意：Stata **do-file 模式**下循环体不能与 `{` 同行（须换行），本库已遵循此规则。

面向《经济研究》投稿实证研究的**可复现代码骨架**。既是各识别方法的"复制即用"模板，
也直接落地 `er-reproducibility` 的目录与一键复现规范。所有命令语法均已核对；版本敏感
之处（如 `did_multiplegt_dyn` 取代 `did_multiplegt`、Stata 19 内置弱工具稳健推断）请
以官方最新文档为准。

## 怎么用

1. 把项目按下列结构组织，`code/` 放本目录脚本：

```
project/
  ├── data/raw/         原始数据（只读）
  ├── data/clean/       清洗后数据
  ├── code/             ← 本目录脚本
  ├── output/tables/
  └── output/figures/
```

2. 打开 `stata/00_master.do`，改 `global root` 为你的项目根路径，首次运行取消依赖安装的注释。
3. `do code/00_master.do` 一键跑通：清洗 → 描述 → 识别 → 机制 → 稳健性 → 出表出图。

## Stata 脚本一览

| 文件 | 用途 | 对应技能 |
|------|------|----------|
| `00_master.do` | 一键复现主控、路径与依赖、固定随机种子 | er-reproducibility |
| `01_clean.do` | 原始→分析样本：合并、筛选留痕、变量构造、缩尾 | er-data-sample |
| `02_descriptive.do` | 描述统计三线表、处理组/控制组平衡性 | er-tables-figures |
| `03_did_modern.do` | TWFE 基准 → Bacon 分解 → CS/BJS/SA/dCDH → 事件研究 | er-identification |
| `04_iv.do` | IV：KP rk F + 有效 F (weakivtest) + AR 稳健推断 (weakiv) | er-identification |
| `05_rdd.do` | RDD：rdrobust 稳健偏差校正 CI + rddensity 操纵检验 | er-identification |
| `06_dml.do` | 双重机器学习：ddml + pystacked 多学习器 | er-identification |
| `07_mechanism.do` | 机制：只跑 D→M，M→Y 用理论论证（江艇 2022 口径） | er-mechanism |
| `08_robustness.do` | 稳健性体系：按识别威胁分类 + 安慰剂分布 + wild bootstrap | er-robustness |
| `09_tables.do` | 三线表（esttab）与事件研究图导出 | er-tables-figures |

## Python 脚本一览

| 文件 | 用途 |
|------|------|
| `python/clean_panel.py` | 大规模微观面板清洗（pandas），输出 analysis.dta |
| `python/dml_doubleml.py` | DoubleML PLR，多学习器稳健性对比 |
| `python/event_study_plot.py` | 发表级事件研究 / 平行趋势图（matplotlib，≥300 dpi） |

## 现代估计量与命令速查

| 方法 | 论文 | Stata | Python / R |
|------|------|-------|------------|
| 交叠 DID | Callaway & Sant'Anna (2021) | `csdid` | R `did::att_gt` |
| 交叠 DID | Sun & Abraham (2021) | `eventstudyinteract` | R `fixest::sunab` |
| 交叠 DID | Borusyak, Jaravel & Spiess (2024) | `did_imputation` | R `didimputation` |
| 交叠 DID | Gardner (2022) 两阶段 | `did2s` | R `did2s` |
| 交叠 DID | de Chaisemartin & D'Haultfœuille | `did_multiplegt_dyn` | R `DIDmultiplegtDYN` |
| 偏误诊断 | Goodman-Bacon (2021) | `bacondecomp` | — |
| IV 有效 F | Montiel Olea & Pflueger (2013) | `weakivtest` | — |
| IV 弱工具稳健 | Anderson-Rubin / CLR | `weakiv` | — |
| RDD | Calonico-Cattaneo-Titiunik (2014) | `rdrobust` `rddensity` | R/Python 同名包 |
| DML | Chernozhukov et al. (2018) | `ddml` `pdslasso` | Python `DoubleML` |
| 少聚类推断 | Roodman et al. (2019) | `boottest` | — |
| 选择偏误边界 | Oster (2019) | `psacalc` | — |

> 安装统一用 `ssc install <pkg>, replace`。各方法的报告口径与反模式见对应 `er-*` 技能。
>
> 命令的**出处、引文与"审稿一句话检查"**见姊妹文件 [共享报告规范](../../../shared-resources/empirical-methods/reporting-standards.md)：
> 本目录给可运行的端到端 `.do` 流程，`code-templates.md` 给每个命令的来源与权威引用。
