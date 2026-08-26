# ICLR Skills

这个包为 International Conference on Learning Representations (ICLR) 主会论文提供 12 个 agent
skills，覆盖 OpenReview 投稿检查、双盲公开评审、作者讨论、修订纪律、可复现性、代码/数据材料和
camera-ready 准备。

官方依据核验日期：2026-08-26，已锚定到 **ICLR 2027**（第 15 届，2027 年 4 月 26-30 日，加州；
摘要截稿 2026-09-18，全文 2026-09-25）。本届三项新规都会导致 desk reject：合著配额、
reciprocal reviewing、强制 AI 使用声明。主要来源包括 ICLR 2027 CFP、Author Guidelines、
Reviewer Guidelines、AI Policy for Authors、Dates、Code
of Ethics、Code of Conduct、LLM 使用政策更新、poster instructions 和 OpenReview 会议组。详见
`resources/official-source-map.md`。

## Skills

- `iclr-submission`：检查 OpenReview、匿名性、页数、reciprocal reviewing、LLM 披露、双投和补充材料。
- `iclr-author-response`：为 OpenReview 讨论期撰写回复、澄清和修订说明。
- `iclr-camera-ready`：处理录用后的 metadata、camera-ready 文件、poster、video 和 project page。
- `iclr-artifact-evaluation`：整理代码、数据、demo、checkpoint 和复现实验说明。
- `iclr-reproducibility`：加强随机性、计算资源、稳健性和证据链。
- `iclr-supplementary`：组织 appendix、supplementary files、代码链接和讨论期修订。
- `iclr-review-process`：理解 review 维度、AC/SAC、公开评论、受限评论和最终推荐。
- `iclr-writing-style`：把稿件改成 ICLR 读者容易评估的 learning-representation 贡献。
- `iclr-related-work`：处理 OpenReview / arXiv 并行工作和相邻 ICLR 论文。
- `iclr-experiments`：检查 baseline、ablation、scaling、统计、稳健性和 compute。
- `iclr-workflow`：管理从选题到 poster upload 的工作流。
- `iclr-topic-selection`：判断项目是否适合 ICLR，或是否应转投其他 venue。

## 维护原则

- 任何 deadline、模板、页数、discussion 规则和 camera-ready 细节，都要重新打开当年官方页面核验。
- 已结束届次的信息只作为已核验锚点，不当作永久规则；本包锚定在哪一届由
  `tools/cycle_audit.py` 报告。
- ICLR 的 OpenReview 公开性很强，回复、修订说明和录用后的讨论都会影响论文记录。

