# NAACL Skills（中文说明）

本包包含 12 个 agent skills，面向投稿 **NAACL —— 美洲各国计算语言学分会年会
（Annual Conference of the Nations of the Americas Chapter of the
Association for Computational Linguistics）** 的论文。该分会于 2024 年 9 月
经全体会员投票，将名称中的 "North American"（北美）改为 "Nations of the
Americas"（美洲各国），缩写 NAACL 保持不变。这次更名把其近年会议的实际面貌
写进了章程：一个覆盖从加拿大到阿根廷整个半球的 *ACL 旗舰会议，设有
"Languages of Latin America"（2024，墨西哥城）、"NLP in a Multicultural
World"（2025，阿尔伯克基）等主题赛道，并有 AmericasNLP（美洲原住民语言
NLP）等工作坊随会举办。

整个技能包围绕两个结构性事实展开：

1. **NAACL 自己不组织审稿。** 论文在 OpenReview 上的 ACL Rolling Review
   （ARR）周期内完成评审，作者随后把完整的评审包 **commit（提交承诺）**
   给某届 NAACL；该届的资深领域主席与程序主席据此决定录取进主会、
   **Findings of NAACL**，或拒稿。
2. **NAACL 不是每年都开。** 当 ACL 主会在美洲举办时，分会当年停办——
   没有 NAACL 2023，也没有 NAACL 2026（ACL 2026 在圣迭戈举行）。截至本包
   核验日期，下一届是 **NAACL 2027**，日期与地点均未公布。因此"投 NAACL"
   实质上是在为一个有时并不存在的会议规划 ARR 时间线，必须自带备选路线。

官方依据核验日期：**2026-07-08**。已核验 naacl.org、NAACL 2024/2025 届会
网站与征稿、更名投票公告、2027 届占位网站、ARR 的 CFP 与日期页，以及 ACL
Anthology 的 NAACL 与 Findings 卷目。核验时网络网关拦截了对官方域名的直接
抓取，因此所有事实均通过对精确官方 URL 的搜索引擎渲染结果确认，并与 ACL
Member Portal 公告交叉核对——完整来源链、访问日期与所有 **待核实** 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 本包的 NAACL 特色

- **先查日历，再查格式。** 所有涉及截止日期的技能，第一步都是"当前 ARR
  周期究竟通向哪一届 NAACL？"——年年开会的 venue 的作者从不需要问这个问题。
- **commit 是一个策略动作。** ARR 评审在 *ACL 家族内可携带；评审包是等
  NAACL、转投兄弟会议、还是带修改说明重进 ARR，被当作有决策树支撑的一级
  决策来处理。
- **美洲身份是可操作的约束，不是口号。** 技能里落实为：社区所有的语言数据
  及其发布限制；纳瓦特尔语、瓜拉尼语例句的三行注释（gloss）纪律；按语言
  变体（如 es-MX 与 es-AR）限定的结论表述；Anthology 元数据中重音符号的
  正确渲染；以及美洲主办城市的签证提前量。
- **把 Findings 讲成容量机制**：soundness 类质疑会同时封死两个层级，
  excitement 类质疑往往只决定进哪个层级——作者回应应据此分配精力。

## 12 个技能

| 技能 | 职责一句话 |
| --- | --- |
| [`naacl-topic-selection`](skills/naacl-topic-selection/SKILL.md) | 按时机、受众与主题赛道在 NAACL 与 ACL/EMNLP/EACL/AACL/LREC-COLING/TACL/ML 会议之间选路，不按想象中的档次排名。 |
| [`naacl-workflow`](skills/naacl-workflow/SKILL.md) | 管理"跳年"日历：临时倒排计划、里程碑负责人、commit/等待/改投的决策树。 |
| [`naacl-submission`](skills/naacl-submission/SKILL.md) | ARR 上传前审计：周期核对、格式/匿名/checklist 三道闸，以及静默决定命运的表单声明。 |
| [`naacl-writing-style`](skills/naacl-writing-style/SKILL.md) | 把每个结论限定到实测的语言与变体；让带注释的例句承担论证；写出能预判审稿意见的 Limitations。 |
| [`naacl-related-work`](skills/naacl-related-work/SKILL.md) | 覆盖五条文献谱系（含区域/社区谱系）；正确引用 Findings 与工作坊论文；以一句可证伪的 delta 句收束。 |
| [`naacl-experiments`](skills/naacl-experiments/SKILL.md) | 让实验设计匹配语言覆盖声明，保持预算公平的对比，防翻译腔测试集，经受审稿人五种探查。 |
| [`naacl-reproducibility`](skills/naacl-reproducibility/SKILL.md) | 把 Responsible NLP checklist 当合同答；钉死模型、prompt 与逐语言预处理；如实申报发布级别。 |
| [`naacl-artifact-evaluation`](skills/naacl-artifact-evaluation/SKILL.md) | 按 checklist 交叉盘问的标准打包数据/prompt/标注指南，妥善处理社区所有与原住民语言数据的约束。 |
| [`naacl-supplementary`](skills/naacl-supplementary/SKILL.md) | 在四个审阅层级间分配材料；为例句注释的三行成本做预算；不让任何结论只活在无义务层级。 |
| [`naacl-review-process`](skills/naacl-review-process/SKILL.md) | 建模"ARR 出评审、NAACL 出决定"的两段机器、主会与 Findings 的分流机制，以及停办年后异常深的 commit 池。 |
| [`naacl-author-response`](skills/naacl-author-response/SKILL.md) | 把短暂的窗口花在能改变"冻结记录"的地方——那份记录将在 commit 阶段被 NAACL SAC 重读。 |
| [`naacl-camera-ready`](skills/naacl-camera-ready/SKILL.md) | 把承诺清单与去匿名化合并进 Anthology 终版；恢复社区致谢；保住姓名中的重音符号。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 12 条来源（URL + 访问日期）、已核验事实清单、访问方式说明与待核实清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，及上传前按序执行的五轮作者侧核验。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经 Anthology 核验的 NAACL 论文（2013-2022）作为写作范本，附防误归 venue 的排除清单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构的语码转换 QA 论文开头，从"无范围界定"逐步重建为 NAACL 语域。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享 ML 会议可复现性工具包的适配器，外加 4 项通用工具查不出的 NLP 专项人工检查。 |

## 安装与使用

本目录是自带 marketplace 清单的独立 Claude Code 插件：

```bash
# 在仓库克隆内执行
claude plugin marketplace add ./NAACL-Skills
claude plugin install naacl-skills

# 或在 agent 配置中按路径直接引用某个技能：
#   NAACL-Skills/skills/<skill-name>/SKILL.md
```

安装后的典型用法：

- "这篇论文投 NAACL 2027 还是 EMNLP？" → `naacl-topic-selection` +
  `naacl-workflow`
- "周五 ARR 截止，帮我做投稿前审计" → `naacl-submission`
- "评审意见回来了，起草 response" → `naacl-author-response`，配合
  `naacl-review-process` 做分诊
- "论文进了 Findings，接下来怎么办？" → `naacl-review-process` +
  `naacl-camera-ready`

## 核心术语速查

| 术语 | 在本包中的含义 |
| --- | --- |
| **ARR 周期** | OpenReview 上按月份/年份标识的一轮 ACL Rolling Review，产出评审与 meta-review；本身不是录取。 |
| **Commitment** | 作者主动把完整评审包转交给某届 NAACL 请求决定的动作。 |
| **Findings of NAACL** | 面向"扎实但主会容量之外"论文的存档录取层级，收录于 ACL Anthology；报告形式随届次而变。 |
| **停办年** | ACL 主会在美洲举办、NAACL 当年不开的年份（2023、2026）；评审包只能等待、改投或修改重投。 |
| **Limitations 节** | 结论之后强制且不计页数的一节；缺失即构成 ARR CFP 明文的 desk-reject 理由。 |
| **Responsible NLP checklist** | 投稿时随附的问卷；误导性回答本身即是 desk-reject 理由——本包把它当合同对待。 |
| **AoE** | Anywhere on Earth（UTC-12），所有 ARR 截止时间使用的时钟。 |
| **待核实** | 本包的标记：截至访问日期未能在官方渲染结果中钉死的任何陈述。 |

## 与本仓库兄弟包的分工

[`ACL-Skills`](../ACL-Skills/)、[`EMNLP-Skills`](../EMNLP-Skills/) 与本包
覆盖共用同一套评审机器、但身份与日历不同的三个 venue。分工原则：各包只在
自己 venue 的决策需要的范围内叙述 ARR 通用机制；而本包独有的内容——停办年
规划、间隔年之后异常深的 commitment 池、美洲语言的数据治理与写作规范——
不会出现在其他包里。若论文尚未定 venue，请从
[`naacl-topic-selection`](skills/naacl-topic-selection/SKILL.md) 开始，它
按实际情况在整个家族内选路，而不是替 NAACL 拉客。

## 使用建议（配合中文工作流）

- 与导师或合作者用中文讨论投稿策略时，可直接引用各技能的 Output format
  段落作为讨论模板，字段名保留英文以对齐 OpenReview 界面。
- 涉及日期的一切结论，先查
  [`resources/official-source-map.md`](resources/official-source-map.md)
  的待核实清单，再打开官方页面确认；本包的 2024/2025 数据只是历史锚点。
- 面向美洲语言的项目，建议在立项阶段就阅读
  [`naacl-artifact-evaluation`](skills/naacl-artifact-evaluation/SKILL.md)
  中关于社区数据治理的部分——发布限制会反向约束实验与写作设计。
- 评审意见返回后，先用 [`naacl-review-process`](skills/naacl-review-process/SKILL.md)
  把每条意见分为 soundness 类与 excitement 类，再进入
  [`naacl-author-response`](skills/naacl-author-response/SKILL.md) 起草——
  分诊先于写作，是本包反复强调的顺序。
- 录取后若在停办年之外还有下一届可投的姊妹会议，不要把 camera-ready 与
  下一篇的 ARR 规划混在同一个日历里；两条时间线分开管理。

## 诚实性与维护规则

本包构建于 2026-07-08，正处于两届 NAACL 之间，并且明说这一点：

- NAACL 2024/2025 的日期与机制是**历史锚点**，用于展示流程形状，绝不冒充
  下一届的规则。
- 一切未钉死的事实——NAACL 2027 的日期、地点、对应 ARR 周期、commit
  截止、主题赛道、报告形式——都在来源图中标注**待核实**，各技能在每个
  涉及截止日期的步骤都把读者引回官方页面。
- ARR 机制（页数、checklist 执法、preprint 政策、周期节奏）随周期变化，
  以 CFP 与日期页为准；本包在结构上服从它们。
- NAACL 2027 征稿发布后需要更新：来源图的待核实节、workflow 技能的日历
  块、submission 技能的 check-zero 示例，以及本 README 的第二条结构性事实。

## 许可

MIT，见 [LICENSE](LICENSE)。本项目与 NAACL 分会、ACL、ACL Rolling Review、
OpenReview 均无隶属或背书关系；商标归各自所有者。
