# OOPSLA Skills（中文说明）

面向 **OOPSLA**（ACM SIGPLAN Conference on Object-Oriented Programming,
Systems, Languages, and Applications）投稿的 12 个 agent skills。今天的
OOPSLA 是 **SPLASH** 大会框架下的研究论文轨道，录用论文以期刊文章形式发表在
**PACMPL**（Proceedings of the ACM on Programming Languages）上，每年分为
OOPSLA1 与 OOPSLA2 两期。本包覆盖完整投稿战役：判断项目的重心是否属于
OOPSLA（而非 POPL / PLDI / ICFP / Onward!）、在每年两个投稿轮次之间做选择、
应对多阶段 double-anonymous 评审的四种结果、执行 Minor / Major Revision、
拿 artifact 徽章，以及在 SPLASH 现场报告。

官方依据核验日期：**2026-07-08**。核验来源包括 `2026.splashcon.org` /
`conf.researchr.org` 上的 OOPSLA 2026 轨道页、`oopsla26.hotcrp.com` 的
call 与 deadlines 页、TYPES/announce 上流通的 OOPSLA 2026 Round 1 CFP、
SPLASH 2026 主站与日期页、SPLASH 2026 artifact-evaluation 轨道页、ACM
Digital Library 上的 PACMPL 期刊页与 Vol. 10 Issue OOPSLA1 卷首材料、
SIGPLAN 的 SPLASH/OOPSLA 系列页面，以及 SIGPLAN Empirical Evaluation
Guidelines。核验环境的网关对上述站点直接抓取返回 HTTP 403，因此所有页面
均通过搜索引擎对精确 URL 的渲染读取，并用相互独立的渲染、ACM DL 与 dblp
交叉核对；完整证据链（含所有仍标注 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## OOPSLA 的结构性特点

以下六条经核验的机制贯穿全部 12 个 skills，也是 OOPSLA 区别于
单一截稿日期的 SIGPLAN 兄弟会议之处：

- **每年两个入口，汇入同一期刊卷。** OOPSLA 2026 的 Round 1 截稿
  2025-10-10、Round 2 截稿 2026-03-17（均为 AoE、不延期），通过 HotCRP
  提交。Round 1 录用进入 PACMPL Vol. 10 Issue **OOPSLA1**（2026-04-01 起
  出版，227 篇投稿录 75 篇）；Round 2 录用进入 Issue **OOPSLA2**
  （2026-10-01 起出版）。
- **四种评审结果，而非二元录否。** 每轮结束时论文获得 Accept、Minor
  Revision（本轮内完成修改；2026 年起并入了旧的 "Conditional Accept"）、
  Major Revision 或 Reject 之一。
- **跨轮机制（round-hopping）是制度设计。** Major Revision 是受邀按明确
  修改清单在**下一轮**重投，并尽量保留原审稿人——十月投稿即使拿到 Major
  Revision，仍可经三月轮次在同一年度卷发表。本包把这套日历算术讲透。
- **期刊排版加修改稿加页。** 投稿使用单栏 `acmsmall`（`review,anonymous`
  选项），正文上限 **23 页**（参考文献、必需声明与附录不计入）；受邀修改稿
  上限 **25 页**。参考文献之前必须放置 **Data-Availability Statement**，
  不占页数。
- **SPLASH 保护伞与它的地理。** 录用论文在 SPLASH 现场报告——2026 年为
  美国加州奥克兰，10 月 4–9 日，OOPSLA 报告排在 10 月 5–7 日，与
  **ISSTA 2026** 同址联办，并与 **Onward!** Papers / Essays 轨道同场。
  Artifact evaluation 作为 SPLASH 级轨道运行：两阶段（先 kick-the-tires
  再全面评审），徽章为 Functional、Reusable，以及通过 Zenodo DOI 存档
  获得的 Available。
- **应用与广度并重的传统。** PACMPL 的范围表述——"from design to
  implementation and from mathematical formalisms to empirical studies"——
  就是 OOPSLA 的身份：经验报告、语料库研究、基准方法学、human-aspects
  工作在这里都有经核验的先例；这正是它与理论优先的 POPL、实现与性能
  优先的 PLDI 的分工所在。

评审为 double-anonymous、多阶段；Review Committee 两位主席兼任该卷的
PACMPL Associate Editors，逐卷轮换（2026 年为 Anders Møller 与 Işıl
Dillig）。截至核验日，2026 两轮均已截止，OOPSLA 2027 Round 1 的 CFP
**尚未发布**——其截稿日期属于 待核实，不能当作"2026 年 10 月"来引用。

## 12 个 Skills（按战役顺序）

- [`oopsla-topic-selection`](skills/oopsla-topic-selection/SKILL.md)：
  重心测试与 SIGPLAN 家族路由——POPL、PLDI、ICFP、Onward!、ECOOP 或 SE
  会议。
- [`oopsla-workflow`](skills/oopsla-workflow/SKILL.md)：两轮时钟——十月还是
  三月进场、修改路径的资源预留、战役状态机、直到 SPLASH 报告的全程轨道。
- [`oopsla-experiments`](skills/oopsla-experiments/SKILL.md)：把证据类型
  匹配到主张类型——基准、语料库研究、用户研究、案例研究、机械化证明；
  按轮次日历给实验排量。
- [`oopsla-reproducibility`](skills/oopsla-reproducibility/SKILL.md)：把
  SIGPLAN Empirical Evaluation Guidelines 变成可执行清单——warmup、方差、
  语料来源、可复现性台账、可兑现的 Data-Availability Statement。
- [`oopsla-writing-style`](skills/oopsla-writing-style/SKILL.md)：设计洞见
  先于工具名、可证伪的贡献句、能标出自身边界的运行示例、23 页内的期刊
  节奏。
- [`oopsla-related-work`](skills/oopsla-related-work/SKILL.md)：PACMPL 时代
  的引用格式（卷/期/文章号）、用 dblp 防兄弟会议误归属、逐条给出技术
  差异。
- [`oopsla-supplementary`](skills/oopsla-supplementary/SKILL.md)：正文/附录/
  artifact 三层分工、补充材料全字节匿名、把附录组织成修改轮可直接提升的
  单元。
- [`oopsla-submission`](skills/oopsla-submission/SKILL.md)：选轮、23 页
  匿名 `acmsmall` 格式契约、Data-Availability Statement、HotCRP 提交日
  流程。
- [`oopsla-review-process`](skills/oopsla-review-process/SKILL.md)：四结果
  流水线、审稿人连续性、跨轮重投机制，以 2026 卷为锚点讲解。
- [`oopsla-author-response`](skills/oopsla-author-response/SKILL.md)：把
  每轮的 response 窗口当成"归类之争"——把边缘论文推向修改类结果而非
  Reject。
- [`oopsla-camera-ready`](skills/oopsla-camera-ready/SKILL.md)：成为 PACMPL
  文章——审稿意见对账表、去匿名、开放获取流程、期次时点、SPLASH 报告。
- [`oopsla-artifact-evaluation`](skills/oopsla-artifact-evaluation/SKILL.md)：
  挺过 kick-the-tires、Functional/Reusable/Available 徽章阶梯、Zenodo
  DOI、主张到 artifact 的映射。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：
  每条事实的 URL、核验日期与 待核实 清单。
- [`resources/external_tools.md`](resources/external_tools.md)：在用系统
  （轨道页、HotCRP、artifact 轨道、ACM DL）及各自要检查的事项。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：6 篇
  经 dblp/ACM DL 核验的 OOPSLA 论文，覆盖本会的多种贡献形态，附误归属
  排除清单。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  一篇虚构 introduction 的前后改写——从工具广告改成设计论证。
- [`resources/code/README.md`](resources/code/README.md)：指向共享可复现性
  工具包，并给出 PL artifact 的概念对照表。

## 常见调用场景

- *"这篇部分验证工具的论文投 OOPSLA 还是 PLDI？"* →
  先用 `oopsla-topic-selection` 做重心测试，再用 `oopsla-workflow` 选轮。
- *"Round 1 拿到 Major Revision，接下来怎么办？"* →
  `oopsla-review-process` 讲跨轮机制；若 response 窗口未关，配合
  `oopsla-author-response`；用 `oopsla-experiments` 的需求矩阵估算
  修改工作量。
- *"十月截稿前帮我审一遍稿子。"* → `oopsla-submission`（格式/匿名/
  声明）、`oopsla-reproducibility`（四支柱清单）、`oopsla-supplementary`
  （分层检查）。
- *"论文进了 OOPSLA2，去奥克兰之前要做什么？"* →
  `oopsla-camera-ready`，然后 `oopsla-artifact-evaluation`。

## 与兄弟包的关系

本包只服务 OOPSLA，全程假定 PACMPL 两轮机制。单一截稿的 SIGPLAN 兄弟
会议有各自的深度包（如本仓库的 `PLDI-Skills`），日历、结果空间与证据
文化都不同；两者的交接点是 `oopsla-topic-selection` 里的路由表。若只
需要跨全 CS 的单文件会议画像，请用 `Computer-Science-Conference-Skills`，
其中的 OOPSLA 条目是本包深度内容的广度版本。

## 使用注意

- 本包不回答 Onward! Papers/Essays、poster、workshop 或同址 ISSTA 的
  投稿问题；这些轨道有独立的 call 与标准，请经
  [`resources/external_tools.md`](resources/external_tools.md) 去官方页面。
- 涉及金额（APC、注册费）与 2027 卷日期的问题，先查 source map 的
  待核实 清单，再打开官方页面确认，不要凭本包内容直接作答。
- 引用任何 OOPSLA 论文前，按 `oopsla-related-work` 的流程在 dblp 或
  ACM DL 上核对 venue 归属；本仓库的 exemplars 清单展示了误归属的典型。

## 维护说明

- 本包所有日期均为 **2026 卷锚点**，不是常设规则。结果类别在 2025→2026
  之间就发生过变动（Conditional Accept 并入 Minor Revision），应默认
  每卷都可能漂移。
- 给出任何截稿敏感建议之前：重新打开当前 OOPSLA 轨道页、HotCRP 实例与
  SPLASH 日期页；source map 里写明了构建时哪些可直接核验、哪些不可。
- 轮次截稿、页数上限、response 窗口机制、artifact 轨道排期、APC 金额与
  主席人选均逐卷轮换。官方页面一开放，最先要清零的就是 source map 里的
  待核实 登记表。
