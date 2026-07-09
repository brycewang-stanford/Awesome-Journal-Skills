# SSI 可复现材料 · 代码适配说明

本目录把《中国科学：信息科学》(Scientia Sinica Informationis, SSI) 作者引导至仓库级
共享工具，保持"薄适配"：SSI 特有的**政策**（栏目、三审三校、版面费、中英文姊妹刊关系、
数据/代码可用性现状）写在各技能与 [`../official-source-map.md`](../official-source-map.md)；
可复用的**工具**放在共享套件，避免各包各自维护分叉副本。

## 共享套件

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  —— 匿名评审与公开发布的通用检查，可迁移到任何信息科学可复现材料包。
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  —— 依赖无关的打包 smoke 检查（校验目录结构与说明文件是否齐备）。
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  与 [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  —— 通用投稿前自查与审稿答复脚手架；后者可适配到
  [`../../skills/ssi-author-response/SKILL.md`](../../skills/ssi-author-response/SKILL.md) 的中文修回说明。

## 典型用法

```bash
# 在准备补充材料/可复现包时做一次结构 smoke 检查
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/ssi-artifact-staging
```

把脚本当作**结构性 smoke 检查**即可；刊物政策仍以当期《投稿须知》与 SSI 各技能为准。

## 共享工具无法替代的 SSI 专属检查

- **中英文双语摘要与关键词齐备**：SSI 要求中、英文双语摘要，脚本无法判断英文摘要质量，
  须人工确保英文摘要可独立阅读（`../../skills/ssi-writing-style/SKILL.md`）。
- **数据/代码可用性以当期须知为准**：信息科学论文是否强制公开代码/数据**待核实**；
  可用性声明须与补充材料实际内容一致，"可向作者索取"是弱承诺
  （`../../skills/ssi-reproducibility/SKILL.md`、`../../skills/ssi-artifact-evaluation/SKILL.md`）。
- **实验/理论依据可追溯**：记录数据集版本、随机种子、硬件平台、工具链版本；
  仿真与硅后/实测结果分别标注（`../../skills/ssi-experiments/SKILL.md`）。
- **LaTeX 官方模板与排版**：SSI 稿件要求 LaTeX 排版，官方模板可能使用过时 CCT 中文支持，
  在现代 TeX 发行版需社区修订；打包时说明编译环境（`../../skills/ssi-submission/SKILL.md`）。

这里不是经济学计量/Stata 套件，SSI 证据也不是英文 ML 会议的排行榜证据：
不要在此引入 DiD 笔记本或 leaderboard 框架。
