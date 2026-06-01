# IJCAI Skills

面向 IJCAI / IJCAI-ECAI 主会论文的 12 个 agent skills。这个包覆盖 Chairing Tool
投稿、摘要与作者信息截止、两阶段审稿、作者回复、可复现性证据、补充材料、重投信息、
LLM 使用政策与 camera-ready。

官方依据核验日期：2026-06-01。已核验 IJCAI-ECAI 2026 Main Track CFP、Submissions
FAQ、Author's Response FAQ、Reproducibility、Author Kit、Important Dates、Peer Review
Principles 与 IJCAI COI policy。精确来源见 `resources/official-source-map.md`。

## Skills

- `ijcai-submission`：核查 Chairing Tool、作者信息、ORCID、页数、匿名、补充材料、
  重投信息、作者上限、一稿多投与 LLM 使用政策。
- `ijcai-author-response`：按 1 页模板处理 reviewer pressing questions、事实错误与
  unethical review escalation，不加入新结果。
- `ijcai-camera-ready`：处理去匿名、最终格式、元数据、版权、注册、现场报告与 artifact
  发布节奏。
- `ijcai-artifact-evaluation`：在没有独立 artifact badge 的前提下，把代码、数据、证明
  与日志整理成可复现证据。
- `ijcai-reproducibility`：按 convincing / credible / irreproducible 口径补强理论、
  算法、数据集与计算实验。
- `ijcai-supplementary`：整理 Technical Appendix、ZIP 与 Resubmission File，控制截止、
  格式、大小与匿名风险。
- `ijcai-review-process`：解释 Phase 1 summary reject、完整评审、PC/SPC/AC/SAC 角色、
  ethics、保密与 COI。
- `ijcai-writing-style`：压缩 7 页正文，强化 broad AI significance、自洽表述、匿名写法、
  ethics 与 reproducibility。
- `ijcai-related-work`：处理 archival work、arXiv、workshop、近 12 个月被拒版本与
  shortened prior version。
- `ijcai-experiments`：审查 baseline、ablation、统计证据、超参数、算力、数据集、伦理与
  可复现性。
- `ijcai-workflow`：从选题到摘要注册、作者信息、全文上传、回复、录用、camera-ready 与
  现场报告做项目管理。
- `ijcai-topic-selection`：判断项目适合 IJCAI 主轨、special track、survey track，还是更
  适合 NeurIPS / ICML / ICLR / AAAI 等其它 AI venue。

## 维护说明

- 涉及 deadline、页数、模板、费用、LLM 政策、回复格式、补充材料与 camera-ready 时，必须
  重新打开当年官方页面。
- 本包中的 IJCAI-ECAI 2026 事实是历史锚点，不应当被当成永久规则。
