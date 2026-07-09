# 《软件学报》复现材料代码适配 (Journal of Software, JOS)

本目录把《软件学报》(Journal of Software, JOS) 作者引导到仓库级共享工具，保持"薄适配"：
本刊**政策**（中文同行评审、GB/T 7714 格式、代码/数据可用性现状）留在各技能与
[`../official-source-map.md`](../official-source-map.md)；可复用**工具**放在共享套件里，避免各
期刊包各存一份逐渐分叉的拷贝。

## 共享套件

- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
  ——可迁移到任何软件学科复现材料的可用性核查清单。
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  ——无依赖的复现包目录冒烟检查脚本。
- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  与 [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  ——通用投稿前核查与"答复审稿人"脚手架；后者请适配到
  [`../../skills/jos-author-response/SKILL.md`](../../skills/jos-author-response/SKILL.md) 的
  中文修回说明。

## 典型用法

```bash
# 在线投稿前，对复现材料目录做一次冒烟检查
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py \
  /path/to/jos-artifact-staging
```

脚本仅做目录结构冒烟检查。投稿政策仍以《软件学报》当前投稿指南与本包 experiments /
reproducibility / artifact-evaluation 技能为准。

## 通用工具无法替代的《软件学报》专属核查

- **中文写作与 GB/T 7714 著录**：复现包的 README 与论文正文都需中文规范表达，参考文献用
  GB/T 7714 著录，英文摘要术语与正文一致（见 `../../skills/jos-writing-style/SKILL.md`）。
- **代码/数据可用性是加分而非强制**：本刊尚无公开的强制 artifact 评审轨道（现状待核实），
  但提供可复现材料显著增强说服力；"可根据要求提供"是弱表述，应尽量给出可访问链接
  （见 `../../skills/jos-reproducibility/SKILL.md`）。
- **实验出处锁定**：挖掘类或大模型类研究需记录仓库 SHA、语料抽取日期、模型标识与日期、
  缓存原始输出——依赖在线 API 实时调用的包是重采样而非复现
  （见 `../../skills/jos-experiments/SKILL.md`）。
- **专刊材料要求**：若投 CCF ChinaSoft 联动专刊，材料与截稿口径以专刊征稿页与特约编辑要求
  为准（见 `../../skills/jos-artifact-evaluation/SKILL.md`）。

这不是经济学/Stata 计量套件，《软件学报》的证据也不是机器学习排行榜分数：请勿把 DiD
笔记本或纯 benchmark 打分框架搬进来。
