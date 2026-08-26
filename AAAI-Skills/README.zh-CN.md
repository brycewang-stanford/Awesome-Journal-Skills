# AAAI Skills

这个包为 AAAI Conference on Artificial Intelligence 主技术轨论文提供 12 个 agent skills，覆盖
OpenReview 投稿检查、两阶段审稿、AI-assisted review pilot、短 rebuttal、可复现性
checklist、补充材料和 camera-ready 出版准备。

官方依据核验日期：2026-08-26，已锚定到 **AAAI-27**（第 41 届，2027 年 2 月 16-23 日，蒙特利尔）。
主要来源包括 AAAI-27 conference page、Main Technical Track CFP、submission instructions、
review process、supplementary-material rules、author policies 和 publication/attendance rules。
其中 rebuttal FAQ 与 AI-assisted review pilot FAQ 两项仍取自 AAAI-26——AAAI-27 尚未发布对应页面，
source map 在对应行已注明。详见 `resources/official-source-map.md`。

## Skills

- `aaai-submission`：检查 OpenReview、匿名性、页数、reproducibility checklist、补充材料、作者上限、双投和 AI 使用政策。
- `aaai-author-response`：在 no URL、no new results 的约束下撰写 AAAI 短 rebuttal。
- `aaai-camera-ready`：处理录用后的 source files、proceedings metadata、extra pages、copyright、注册和报告安排。
- `aaai-artifact-evaluation`：整理代码、数据和 appendix，帮助审稿人核验可复现性。
- `aaai-reproducibility`：强化 checklist、证据地图、随机种子、compute 和数据细节。
- `aaai-supplementary`：组织 technical appendix、multimedia appendix 与 code/data ZIP。
- `aaai-review-process`：理解 Phase 1、Phase 2、AI-assisted review、SPC/AC 讨论和最终决定。
- `aaai-writing-style`：面向广义 AI 读者改写贡献、清晰度和政策相关表述。
- `aaai-related-work`：处理 archival work、arXiv/workshop papers 和 contemporaneous results。
- `aaai-experiments`：检查 baseline、ablation、统计、稳健性、AI 系统评估和 compute。
- `aaai-workflow`：管理从选题到 proceedings publication 的工作流。
- `aaai-topic-selection`：判断项目是否适合 AAAI，或应转向其他 AI venue。

## 维护原则

- deadline、模板、页数、rebuttal、supplement 和 camera-ready 细节必须重新打开当年官方页面核验。
- 已结束届次的信息只作为已核验锚点，不当作永久规则；本包锚定在哪一届由
  `tools/cycle_audit.py` 报告。
- 如果 AAAI 页面之间出现日期或规则冲突，以最新 Author Kit 或 chairs 直接通知为准，并记录冲突。

