---
name: er-reproducibility
description: Use when organizing a reproducible research package (folder structure, master do-file, data availability statement) so empirical results survive 《经济研究》 referee scrutiny and录用后的扩展资料提交.
---

# 可复现研究包（er-reproducibility）

## 触发时机

- 实证做完了，准备把代码和数据整理成"别人能重跑"的形态
- 审稿人或编辑要求"提供代码核查"，而你的脚本现在是一坨乱麻
- 收到 R&R，要在干净环境里复现自己三个月前的结果，却跑不出来
- 录用后编辑部要求提交扩展资料（数据 + 代码）

## 为什么重要

- 《经济研究》审稿人 / 编辑会**核查代码与数据**：表格对不上、跑不出来，直接成为修改阶段的大坑，甚至撤稿。
- 可复现性差 → R&R 阶段每改一处都要从头手动重算，时间成本巨大。
- 现实是：**几个月后第一个跑不出你结果的人，就是你自己**。可复现包首先是给未来的自己用的。

## 标准目录结构

一个项目一个根目录，原始数据只读、代码分层、输出与代码分离：

```
project/
  ├── data/raw/        原始数据（只读，永不手改）
  ├── data/clean/      清洗后数据（由代码生成，可删可重建）
  ├── code/
  │   ├── 00_master.do     一键运行，顺序调用以下脚本
  │   ├── 01_clean.do      清洗：原始 → clean
  │   ├── 02_descriptive.do 描述性统计 / 平衡性
  │   ├── 03_baseline.do   基准回归
  │   ├── 04_mechanism.do  机制检验
  │   ├── 05_robustness.do 稳健性
  │   └── 06_figures.do    出图
  ├── output/tables/   表格（由代码生成）
  ├── output/figures/  图形（由代码生成）
  └── README.md        运行说明 + 数据可得性声明
```

原则：**output 里的任何文件都应能被 code 重新生成**。手工产物不进 output。

## master do-file 模板

只在 master 里定义一次根路径，全部用相对路径，固定版本与种子：

```stata
*============================================================
* 00_master.do —— 一键复现正文全部表与图
*============================================================
clear all
set more off
version 17                          // 声明 Stata 版本，便于他人对齐
set seed 20240101                  // 全局随机种子，bootstrap/安慰剂可复现

* 根路径：他人只需改这一行
global root "/Users/yourname/project"
global data  "$root/data"
global code  "$root/code"
global out   "$root/output"

* 按顺序运行，从原始数据到最终图表
do "$code/01_clean.do"
do "$code/02_descriptive.do"
do "$code/03_baseline.do"
do "$code/04_mechanism.do"
do "$code/05_robustness.do"
do "$code/06_figures.do"

display "复现完成：见 $out/tables 与 $out/figures"
```

## 脚本编写规范

- **一个脚本一个任务**：清洗、描述、回归、出图分开；不要把 8000 行塞进一个文件。
- **全链路可追溯**：从 `data/raw` 到 `output/tables` 的每一步都在代码里，无手工断点。
- **变量构造有注释**：每个生成变量注明**来源与公式**，例如：
  ```stata
  * 资产负债率 = 总负债 / 总资产（CSMAR 财务报表，FI_T1.B001000000 / FI_T1.A001000000）
  gen lev = total_debt / total_asset
  ```
- **缩尾、合并、样本筛选都在代码里留痕**：
  ```stata
  winsor2 lev roa, cuts(1 99) replace   // 上下 1% 缩尾
  drop if year < 2008 | year > 2022     // 样本期：2008–2022，注明理由
  ```
- 相对路径引用 `$data`/`$out`，**不写死绝对路径**（绝对路径只在 master 的 `global root` 出现一次）。

## 数据可得性说明

商业数据库（CSMAR / Wind / 税收调查等）**不能直接公开**，需在 README 写"数据可得性声明"，说清来源、获取方式、哪些可共享哪些受限：

```
## 数据可得性声明
本研究数据来自以下来源：
- 上市公司财务数据：CSMAR 数据库（订阅获取，受许可协议限制，不可公开再分发）。
- 城市层面控制变量：《中国城市统计年鉴》（公开出版物，已随包提供清洗后子集 data/clean/city_panel.dta）。
- 政策清单：作者手工整理自地方政府公开文件，随包提供 data/raw/policy_list.xlsx。
可共享：清洗代码（code/）、公开来源数据、变量构造说明。
受限：CSMAR 原始明细不可公开；复现者须自行订阅并按 01_clean.do 注明的字段重建。
联系方式：[作者邮箱]，可协助说明字段口径。
```

不要写"数据来源于公开渠道"这种含糊声明。

## 随机性与可复现

- 任何含随机性的步骤（bootstrap、安慰剂置换、ML 调参、随机抽样）**必须 `set seed`**，且种子在 master 里统一设定。
- 报告**软件版本与关键命令版本**：Stata 版本（`version 17`）、依赖的用户写命令及版本（如 `csdid` / `reghdfe` / `winsor2`），可在 README 列出 `which csdid` 的版本行。
- 涉及并行 / 多核时注意：核数变化可能改变随机数流，需在说明中标注运行环境。

## 必查清单

- [ ] 目录按 data/raw、data/clean、code、output 分层，raw 只读
- [ ] 存在 `00_master.do`，一键顺序运行全部脚本
- [ ] 所有路径相对化，绝对路径仅在 master 出现一次
- [ ] 每个生成变量有来源与公式注释；缩尾 / 合并 / 筛选在代码中留痕
- [ ] 所有随机步骤 `set seed`，种子在 master 统一设定
- [ ] README 含数据可得性声明，区分可共享 / 受限
- [ ] README 列出软件与关键命令版本
- [ ] 在**干净环境**从 `00_master.do` 一键重跑，能复现正文每一张表 / 图
- [ ] output 中表格 / 图形编号与正文引用完全一致
- [ ] 录用后按编辑部要求准备扩展资料（数据 + 代码），以投稿当期官网为准

> 注：《经济研究》录用后须按编辑部要求提交扩展资料——附录（Word）、与统计软件匹配的数据文件或 Excel、软件代码文件、（如有）权利人限制说明。是否提交完整复制包 / README 以投稿当期官网与编辑部通知为准，本技能不替代官方要求。

## 反模式

- 在 Excel 里手动改数 → 链路断裂，无法追溯
- 路径写死绝对路径，换台电脑全部报错
- 没有 master，靠"记得先跑哪个再跑哪个"
- 随机检验（bootstrap / 安慰剂）不设种子，每次结果都不一样
- 清洗与分析混在一个 8000 行脚本里，改一处全连坐
- 正文最终表格是从日志里**手抄**进 Word 的
- 数据可得性写"数据来源于公开渠道"，审稿人无法判断口径

## 输出格式

```
【目录结构】合规 / 待整理：[...]
【master】存在并一键可跑 / 缺失
【路径】全相对 / 发现写死绝对路径：[...]
【随机种子】全部已设 / 缺失：[...]
【数据声明】完整（区分可共享 / 受限）/ 含糊待改
【干净环境复现】通过 / 失败：[哪张表跑不出]
【版本记录】已列 Stata 与命令版本 / 缺失
【下一步】整理完成 → er-submission 做投稿前 preflight 与附件清单
```

## 参考

- 著录采用著者—出版年制；正文引用如（Gentzkow and Shapiro，2014），不使用 [1][2] 序号制。

## 附属资源

- [`../er-submission/SKILL.md`](../er-submission/SKILL.md) — 投稿前 preflight 与附件 / 扩展资料清单
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — CSMAR / Wind / CNRDS 等数据源与统计软件包速查
