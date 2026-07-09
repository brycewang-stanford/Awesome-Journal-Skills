# 《计算机研究与发展》代码与可复现材料适配器 (JCRD)

本目录把《计算机研究与发展》(Journal of Computer Research and Development, JCRD) 作者引向仓库级
共享工具，保持精简：JCRD 专用**政策**（双盲评审、只收中文稿、专题组稿、代码/数据可用性）落在
skills 与 [`../official-source-map.md`](../official-source-map.md)；可复用**工具**放在共享套件，
避免各包维护分叉副本。

## 共享套件

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  —— 匿名评审与公开发布检查，可迁移到任何计算机可复现材料包。
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  —— 无依赖的目录结构 smoke checker。
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  与 [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  —— 通用投稿前与答复脚手架；把后者适配为 JCRD 的**修回说明/审稿意见答复**，见
  [`../../skills/jcrd-author-response/SKILL.md`](../../skills/jcrd-author-response/SKILL.md)。

## JCRD 典型用法

```bash
# 上传前对匿名化的代码/数据材料做结构 smoke 检查
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/jcrd-artifact-staging
```

把脚本当作结构 smoke 测试；期刊政策仍以当期《投稿须知》与 JCRD 的实验、可复现、代码数据可用性
技能为准。

## 通用工具无法完成的 JCRD 专用检查

- **双盲延伸到材料层。** 本刊双盲评审：随稿提供的代码仓库、数据链接、README 与致谢不得泄露作者/
  单位/项目组身份；把仓库重托管到匿名服务后再放链接（见 `../../skills/jcrd-submission/SKILL.md`）。
- **数据/代码可用性说明诚实对应。** 说明须与实际提供的材料一致；「可向作者索取」是被计分的弱项，
  而非中性占位（见 `../../skills/jcrd-reproducibility/SKILL.md`）。
- **实验来源钉死。** 挖掘/大模型类研究记录数据集版本与抽取日期、模型标识与日期，并缓存原始输出；
  需实时 API 才能跑的材料只是重采样而非复现（见 `../../skills/jcrd-experiments/SKILL.md`）。
- **中文长文与材料一致。** 图表、算法伪码、符号表与正文中文表述一致；专题投稿另需符合专题的补充
  材料约定（见 `../../skills/jcrd-supplementary/SKILL.md`）。

这不是经济学包的 Stata/DiD 工具，JCRD 证据也不是纯排行榜分数：请勿在此引入计量 notebook 或
leaderboard 叙事。
