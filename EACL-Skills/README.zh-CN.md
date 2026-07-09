# EACL Skills

面向 **European Chapter of the Association for Computational Linguistics 会议
（EACL）** 论文的 12 个 agent skills。EACL 是 *ACL 家族中承载欧洲身份的会议，
通常在每年年初春季于欧洲及地中海地区举办（2027 雅典、2026 拉巴特、2024
圣朱利安斯、2023 杜布罗夫尼克），是当年最早召开的 *ACL 会议。

与其兄弟会议一样，EACL 自身不设投稿系统。论文先在 OpenReview 上的
**ACL Rolling Review（ARR）** 中评审，再 **commit（提交承诺）** 到某一届 EACL，
由 senior area chairs 与 program chairs 把每篇 commitment 分入主会、
**Findings of ACL: EACL** 或拒稿。本包中所有与 deadline 相关的 skill 都按这一
两步节奏推理——先 ARR cycle，再 EACL commitment——而非某个单一“会议 deadline”。

官方依据核验日期：**2026-07-09**。已核验 EACL 2027 call for papers（第 20 届，
希腊雅典，2027-03-09 至 03-14）、aclrollingreview.org 的 ARR CFP、cycle 日历与
Responsible NLP checklist、ARR 的 OpenReview groups、ACL Anthology 的 EACL 与
Findings 卷，以及 ACL Member Portal 公告。核验网关屏蔽了对 `2027.eacl.org`、
`aclrollingreview.org` 与 `dblp.org` 的直接抓取，故这些页面通过搜索引擎对精确
官方 URL 的渲染读取，并与 ACL Anthology、ACL Member Portal 交叉核对。完整来源、
访问方式与全部 待核实 项见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## EACL 投稿的独特之处

- **欧洲分会，而非旗舰会。** EACL 是 ACL 的欧洲区域会议，与 NAACL（美洲）、
  AACL（亚太）以及旗舰 ACL 并列。它是欧洲及周边地区语言技术、多语言与低资源
  语言研究的天然归属地，评审社区也以欧洲为主——但学术范围是整个 CL/NLP，
  并非只收“欧洲主题”。
- **不规律的周期。** EACL 并非每年举办，档期也会移动；2021 年之前有间隔，
  随后 2023、2024、2026 各办一届，下一届为 2027。切勿默认 EACL 每年都有——
  规划前先确认该届是否存在。
- **只有一个可用 ARR cycle，没有退路。** 由于 EACL 2027 排在年初，组织方声明
  **2026-08-03 的 ARR cycle 是唯一可用 cycle**。不同于 ACL（可用两个 cycle），
  这里没有“顺延到下一 cycle”的安全网——错过即错过整届。时机是本包中最高杠杆的
  决策。
- **Limitations 章节必填**，且不计入长文 8 页 / 短文 4 页正文额度，与不限页数的
  references 和 appendices 并列。缺失即触发 desk reject。
- **Responsible NLP checklist 是评审的一部分。** 在 ARR 投稿时填写，误导性回答
  构成 desk reject 理由；而诚实的 Limitations 受到明确保护，不会因此被扣分。
- **两个存档层级。** Findings of ACL: EACL 是真实、进 Anthology 的录用结果，
  在 commitment 阶段决定，与主会同时通知。
- **开放获取、无费用。** 录用论文进入 ACL Anthology，2016 年后材料采用 CC BY 4.0，
  作者无需付费；成本模型是注册费，至少一位作者注册并到场报告。

## Skills

- `eacl-submission`：核查投向 EACL 的 ARR 上传件——正文页数额度、必填 Limitations、
  Responsible NLP checklist、匿名、preprint 与 resubmission 声明、一稿多投规则，
  以及单 cycle 时机陷阱。
- `eacl-author-response`：处理 cycle 内 rebuttal 窗口——分诊 reviews、面向 action
  editor、回应常见 NLP 审稿反对、标记不合格 review，并决定当下回应还是改投后续 venue。
- `eacl-camera-ready`：用好多出的一页正文、去匿名、披露 AI 协助、满足 meta-review，
  并为 EACL 或 Findings: EACL 记录准备干净的 ACL Anthology 元数据。
- `eacl-artifact-evaluation`：把代码、数据、prompt、模型输出与标注材料整理为匿名
  OpenReview 补充材料，对齐 checklist，并规划录用后的公开发布。
- `eacl-reproducibility`：把 Responsible NLP checklist 当作 claims 审计——超参数、
  算力、prompt 与解码披露、污染立场、方差报告与 checklist-论文一致性。
- `eacl-supplementary`：拆分正文、Limitations、appendix 与归档，确保决策关键内容
  不藏在 EACL 审稿人无义务阅读之处。
- `eacl-review-process`：解释 ARR-到-EACL 流程——reviewers、action editor、
  meta-review、commitment、venue 侧决定、伦理升级，以及何时改投兄弟会议。
- `eacl-writing-style`：为 task-first framing、首页示例、限定范围的 LLM 时代主张、
  量化 error analysis、匿名安全语气与 8/4 页压缩做修订。
- `eacl-related-work`：在快速变动的 NLP 文献中定位——Anthology 优先引用、Findings
  归属、并发 preprint，以及跨近期 *ACL 轮次与欧洲 venue 的时新性巡查。
- `eacl-experiments`：设计证据——调优过的 LLM baseline、与主张匹配的多语言广度、
  显著性与方差下限、human-eval 一致性、污染控制、ablation 与 error taxonomy。
- `eacl-workflow`：运行单 cycle-并-commit 日历——锁定 cycle、倒排计划、rebuttal
  窗口、commitment 决策，以及 camera-ready 到 Anthology 发布。
- `eacl-topic-selection`：在 EACL、ACL、EMNLP、NAACL、AACL、TACL、Computational
  Linguistics、LREC-COLING、COLM 与 ML venue 之间选路；选长文还是短文；权衡
  Findings 情景与单 cycle 约束。

## Resources

| 路径 | 内容 |
| --- | --- |
| `resources/official-source-map.md` | 已核验来源，含 URL、访问日期、网关访问方式说明与 待核实 项 |
| `resources/external_tools.md` | 官方 ARR/OpenReview/EACL/Anthology 入口，以及分阶段作者自查 |
| `resources/exemplars/library.md` | 五篇已核验的 EACL 主会/Findings 范例，按贡献类型分类，附兄弟 venue 防混淆 |
| `resources/worked-examples/01-introduction.md` | EACL 风格的虚构前后对照 abstract + introduction |
| `resources/code/README.md` | 指向共享 ML-conference 可复现性工具包 |

## 使用方式

新项目的典型顺序：`eacl-topic-selection` → `eacl-experiments`（设计阶段）→
`eacl-writing-style` + worked example → `eacl-related-work` →
`eacl-reproducibility` + `eacl-artifact-evaluation` → `eacl-supplementary` →
在唯一 ARR deadline 前 `eacl-submission` → rebuttal 窗口内 `eacl-author-response`
→ commitment 决策时 `eacl-review-process` + `eacl-workflow` → 录用后
`eacl-camera-ready`。

可从本目录作为 Claude Code 插件安装（marketplace 清单在 `.claude-plugin/`），
或按需单独加载 `skills/*/SKILL.md`。

## 已核验事实快照（访问日期 2026-07-09）

| 事实 | 取值 | 来源 |
| --- | --- | --- |
| 下一届 | EACL 2027，第 20 届欧洲分会会议 | 2027.eacl.org |
| 日期 / 地点 | 2027-03-09 至 03-14，希腊雅典（hybrid） | 2027.eacl.org |
| 评审 | OpenReview 上的 ACL Rolling Review；EACL 做 commit | EACL 2027 CFP + aclrollingreview.org |
| 可用 ARR cycle | 仅 2026-08-03（无退路） | EACL 2027 CFP + @eaclmeeting 日期更正 |
| commitment 截止 | 2026-10-11 | EACL 2027 CFP |
| 通知 / camera-ready | 2026-11-12 / 2026-11-26 | EACL 2027 CFP |
| 页数额度 | 长文 8、短文 4；camera-ready +1；references/appendices 不限 | ARR CFP + EACL 2027 CFP |
| 必填章节 | Limitations（不计页数；缺失即 desk reject） | ARR CFP |
| Checklist | Responsible NLP checklist | aclrollingreview.org/responsibleNLPresearch |
| 匿名 | 匿名投稿；自 2024-01-12 起无 anonymity period | ARR anonymity policy |
| 录用层级 | 主会；Findings of ACL: EACL（存档） | ACL Anthology |
| 论文集 | ACL Anthology，开放获取，CC BY 4.0（2016 年后） | aclanthology.org |
| 上一届 | EACL 2026，第 19 届，摩洛哥拉巴特，2026-03-24 至 03-29 | aclanthology.org/2026.eacl-long |

## 常见问题

**这个包能替代官方 call 吗？** 不能。它编码了已核验的 2027 年状态与稳定的 ARR
机制；任何与 deadline 相关的事实都必须对照最新的 ARR 与 EACL 官方页面重新核对，
官方页面在冲突时优先。

**为什么反复强调“唯一 cycle”？** 因为 EACL 2027 只接受 2026 年 8 月的 ARR cycle，
常见的 *ACL“下一 cycle 再投”退路对这一届并不存在。本包把这个单一 cycle 视为一次性、
不可重复的硬性关口，而非多次尝试之一。

**这个包涵盖 ACL、EMNLP 或 NAACL 吗？** ARR 机制在 *ACL 家族中共享，许多流程推理可
迁移，但这里的校准、日期、cadence 与区域身份属于 EACL。兄弟 venue 请用对应的兄弟包。

**EACL 只收欧洲语言的工作吗？** 不是。EACL 欢迎整个 CL/NLP。其欧洲身份塑造的是社区
与举办地，也使它成为多语言与低资源语言研究的天然归属地，但主题范围并不按地域限制。

**标注为 待核实 的事实怎么办？** 表示在构建时无法通过网络网关确认。在你亲自打开官方
页面之前，请当作未知处理；source map 明确列出了这些事实。

## 维护说明

- EACL 的 cadence 与档期在各届之间移动；切勿把 2027 时机向前推。做任何 deadline
  敏感建议前，重新打开目标届网站与 aclrollingreview.org/dates。
- 本包中的 EACL 2027 事实（日期、唯一可用 cycle、commitment 窗口）是当年锚点，
  不是永久规则；官方页面在任何冲突中优先。
- checklist 措辞、preprint 激励、页数政策、review 表单与 Findings 报告方式都随
  cycle 变化。
- 新增范例时，务必确认 Anthology 的 venue 行明确写明是某一届 EACL——Anthology
  同时托管所有兄弟会议，共享的 `E`/`eacl` 标识极易混淆。

## License

MIT（见 `LICENSE`）。本包为社区文档，与 ACL 或其欧洲分会无隶属或背书关系。
