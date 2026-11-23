# ICML Skills

这是 International Conference on Machine Learning (ICML) 的 first-party 深度包。

本包把 ICML main track 的 CFP、Author Instructions、Peer Review FAQ、Reviewer Instructions 和
LLM-review policy 拆成 12 个可调用 skill，覆盖选题定位、投稿审计、作者回复、
camera-ready、artifact、可复现性、补充材料、审稿流程、写作风格、相关工作、实验设计和全流程路由。

## Skills

| Skill | 用途 |
|---|---|
| `icml-topic-selection` | 判断论文适合哪种 ICML contribution type（含 2027 年并入 main track 的 Position Papers）或其它 venue。 |
| `icml-workflow` | 规划从 fit 诊断到 PMLR camera-ready 的全流程。 |
| `icml-submission` | 核验 OpenReview、LaTeX、8 页正文、匿名、supplement、impact statement、AI Disclosure Statement、投稿配额和政策风险。 |
| `icml-review-process` | 理解 reciprocal reviewing、reviewer/AC、ethics、LLM-review policy 和公开评审记录。 |
| `icml-author-response` | 写 rebuttal 和后续几轮 reviewer-author discussion 回复。 |
| `icml-camera-ready` | 准备录用后 PDF、PMLR agreement、lay summary、公开 artifact 和会后修订。 |
| `icml-artifact-evaluation` | 整理匿名代码/数据和公开发布 artifact。 |
| `icml-reproducibility` | 强化可复现实验、代码/数据声明和 impact statement 支撑。 |
| `icml-supplementary` | 决定哪些内容放论文 PDF、supplementary manuscript、code/data ZIP 或公开仓库。 |
| `icml-writing-style` | 按 ICML 的 soundness、originality、significance、clarity 和 impact 预期改写。 |
| `icml-related-work` | 处理 concurrent ICML submissions、近期论文和近邻 ML 文献定位。 |
| `icml-experiments` | 压测 baseline、消融、seed variance、算力和 claim-to-evidence fit。 |

## 来源纪律

本包已于 2026-11-23 切换到 ICML 2027（巴西里约热内卢，2027 年 7 月 31 日至 8 月 6 日；摘要截止 2027 年
1 月 14 日，全文截止 1 月 22 日，AoE），并据 ICML 2027 官方 CFP、Author Instructions、生成式 AI 政策和
Reviewer Instructions 核验。ICML 政策每年变化；任何投稿级建议都必须
重新打开当年 CFP、Author Instructions、Peer Review FAQ、OpenReview group 和 LLM-review policy。

