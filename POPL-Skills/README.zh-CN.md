# POPL Skills

面向 **POPL（ACM SIGPLAN Symposium on Principles of Programming Languages）** 投稿的
12 个 agent skills。POPL 是 SIGPLAN 家族中偏理论的旗舰会议，核心是 semantics、type
systems、program logics、verification 原理及支撑它们的证明技术。本包覆盖一次完整的
POPL 战役：判断项目的决定性证据是否真的是定理而非 benchmark、搭建审稿人期待的
informal-to-formal 论证坡道、在 full double-blind 下通过每年唯一的 7 月 HotCRP
截稿、把 10 月的 *conditional acceptance* 转化为令 Review Committee 满意的修订版、
让机械化证明开发以零 `admit` 通过 artifact evaluation，最终以 **PACMPL Issue POPL**
期刊论文的形式发表并在 1 月的会议上报告。

官方依据核验日期：**2026-07-08**。已核验 POPL 2027 research-papers call 与
important-dates 页面（popl27.sigplan.org）、POPL 2027 与 POPL 2026 会议站点、
POPL 2025/2026 artifact-evaluation track、ACM Digital Library 上的 PACMPL 期刊与
各期页面，以及每个 exemplar 的 dblp 记录。核验环境中对 sigplan.org 与
conf.researchr.org 的直接抓取返回 HTTP 403，因此官方页面通过搜索引擎对精确 URL 的
渲染读取，并与 ACM DL、dblp 交叉核对。完整证据链（含所有 待核实 条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

**内置的时间警告：** POPL 2027 的投稿截止是 **2026 年 7 月 9 日 11:59 PM AoE ——
仅在上述核验日期之后一天**。任何在该日期附近使用本包的 agent，都必须先打开
live 页面确认窗口是否仍然开放，再向作者给出建议。

## POPL 的结构性特征

以下六条经核验的机制驱动了本包的绝大部分建议：

- **7 月截稿、1 月开会。** POPL 2027（第 54 届）：论文 2026 年 7 月 9 日经
  `popl27.hotcrp.com` 截稿，**没有 abstract deadline**；通知 2026 年 10 月 5 日；
  会议 2027 年 1 月 10-16 日在墨西哥城 Hilton Mexico City Reforma 举行。每年只有
  一个截稿；秋季属于修订、artifact 与差旅。
- **Full double-blind，且明确区别于自身历史。** 自 POPL 2023 起采用 *full*
  double-blind——作者身份只在 conditional-acceptance 决定之后、且仅对过线论文
  揭示——取代此前多年的 lightweight double-blind。
- **没有"录用"，只有"有条件录用"。** 每个正面决定都附带条件清单，CFP 原话直白：
  须在指定期限前向 Review Committee 提交令其满意的修订版，"否则有被拒风险"。
- **25 页正文预算与明示的处罚。** 正文（不含参考文献）至多 25 页，使用单栏
  acmart/`acmsmall` PACMPL 版式（10 pt 字号 / 12 pt 行距）；版式偏离是
  **summary rejection** 的直接依据，且不接受 Word。
- **证明 artifact 是本会的原生 artifact。** Artifact evaluation 面向有条件录用
  论文、按邀请进行；徽章为 Artifacts Evaluated - Functional、Artifacts Evaluated -
  Reusable、Artifacts Available（Zenodo/ACM DL 存档快照）。AE 页面以 Coq/Isabelle
  证明库作为 reusable artifact 的自有示例，并要求 reusable 证明必须完整——
  **Coq/Rocq 中不得有 `admit`，Lean/Isabelle 中不得有 `sorry`**。
- **一个出版期刊的会议。** 录用论文以 PACMPL（Proceedings of the ACM on
  Programming Languages）Issue POPL 形式发表：Vol 2 = 2018、Vol 7 = 2023、
  Vol 10 = 2026（2026 年 1 月 8 日出版，2675 页）。PACMPL 为 Gold Open Access；
  APC 为 400 美元，SIGPLAN 为无力支付的作者兜底，且 ACM 自 2026 年 1 月 1 日起
  全面开放获取。

同样经核验：至多 10% 的录用论文可评为 Distinguished Papers；POPL 2026（第 53 届）
于 2026 年 1 月 11-17 日在法国 Rennes 举行，CPP 共址（2027 年同样如此）；POPL 由
SIGPLAN 主办、SIGACT 与 SIGLOG 协办。POPL 2027 的 author-response 窗口、修订
截止与主席名单在核验时未能渲染，均记入 待核实。

## 十二个 skills

策略与定位：

- [`popl-topic-selection`](skills/popl-topic-selection/SKILL.md)——"principles"
  适配测试：决定性证据是否住在证明里？在 PACMPL 家族（PLDI、OOPSLA、ICFP）内部
  及向 LICS、CAV、CPP、ESOP、期刊的路由。
- [`popl-writing-style`](skills/popl-writing-style/SKILL.md)——informal-to-formal
  坡道、作为承重结构的记号系统、点名困难 case 的 proof sketch、可迁移性框架。
- [`popl-related-work`](skills/popl-related-work/SKILL.md)——定理级 delta 句、
  LICS/CAV/TOPLAS 邻域地图、PACMPL 期刊体引用格式、经 dblp 核验的经典归属。

证据：

- [`popl-reproducibility`](skills/popl-reproducibility/SKILL.md)——理论会议上
  "可复现"按主张类型的含义、机械化与手写证明的取舍、论文-证明对应表。
- [`popl-experiments`](skills/popl-experiments/SKILL.md)——支撑而非承载主张的
  实证：case study 纪律、证明工作量核算、诚实报告坏消息。
- [`popl-supplementary`](skills/popl-supplementary/SKILL.md)——正文 / 证明附录 /
  匿名 artifact 的三分、sketch 与完整证明的一致性、证明仓库的匿名清扫。

流程：

- [`popl-submission`](skills/popl-submission/SKILL.md)——HotCRP 机制、25 页上限
  与 summary-rejection 规则、理论论文特有的身份泄漏、最后 72 小时操作顺序。
- [`popl-review-process`](skills/popl-review-process/SKILL.md)——POPL 委员会如何
  用反例试探正确性、conditional acceptance 究竟决定什么、Distinguished Paper 机制。
- [`popl-author-response`](skills/popl-author-response/SKILL.md)——soundness 优先
  的四分类 triage、让步的技艺、符合 concise 要求的回复骨架。
- [`popl-workflow`](skills/popl-workflow/SKILL.md)——从 7 月倒排（"定理不可
  压缩"）、通知后的秋季三线并行、错过截稿时的 PACMPL 截稿轮盘。

决定之后：

- [`popl-camera-ready`](skills/popl-camera-ready/SKILL.md)——两道闸门：委员会
  修订与 PACMPL 出版；作为 diff 来审查的去匿名化；1 月签证时钟。
- [`popl-artifact-evaluation`](skills/popl-artifact-evaluation/SKILL.md)——证明
  视角下的徽章标准、公理审计、工具链锁定、Zenodo 存档。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)——12 条
  带日期的官方来源、已核验事实清单、待核实登记表，以及针对 403 封锁站点的
  访问方式说明。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)——6 篇经
  dblp/ACM DL 核验的里程碑论文，从 Cousot & Cousot 1977 到 PACMPL 2(POPL) 的
  RustBelt，外加 LICS/JCSS/FPCA/CGO 误归属陷阱。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  ——一篇虚构 gradual session types 论文的开篇按 POPL 论证弧重写的前后对照。
- [`resources/external_tools.md`](resources/external_tools.md)——HotCRP、PACMPL、
  dblp、Zenodo 与作者侧检查清单，附"不得推断"列表。
- [`resources/code/README.md`](resources/code/README.md)——共享 artifact kit 到
  证明开发的翻译表（seeds → 工具链锁定、experiment matrix → 对应表）。

## 一次 POPL 战役的建议路线

1. **截稿前十六周（冬/春）：** 诚实地跑 `popl-topic-selection`——如果主张必须靠
   benchmark 才成立，先做 PLDI/OOPSLA 的路线讨论，再决定是否投入元理论。把主
   定理精确地猜想出来。
2. **前十二至八周：** 证明困难引理，启动内核机械化，建立对应表
   （`popl-reproducibility`）。尽早冻结形式化核心——坏掉的引理不会被截稿肾上腺素
   修好。
3. **最后一个月：** 按 `popl-writing-style` 的坡道成稿，锁定 case studies
   （`popl-experiments`），按 `popl-supplementary` 组装附录与匿名 artifact 并做
   泄漏清扫，在 AoE 截止前清空 `popl-submission` 的严重性表。
4. **response 窗口：** 执行 `popl-author-response` 的四分类——soundness 在先、
   引用原始定义、不加新定理。
5. **有条件录用后（10 月初）：** 同一周开启三条线——条件清单
   （`popl-camera-ready`）、artifact 完整性与公理审计
   （`popl-artifact-evaluation`）、1 月签证与差旅。

## 本包纠正的常见误解

- **"POPL 是 lightweight double-blind。"** 2023 年起已不是——现行流程为 full
  double-blind，身份仅在 conditional-acceptance 决定后揭示。
- **"录用即完事。"** POPL 的录用是有条件的；修订闸门真实存在，CFP 把"拒稿"
  写成失败的代价。
- **"POPL 没有页数限制。"** 2027 年 CFP 规定正文至多 25 页（不含参考文献），
  并以 summary rejection 执行。
- **"admit 了的引理只要说明就行。"** 要拿 Reusable 徽章，AE 标准要求完整性——
  没有 `admit`、没有 `sorry`；披露属于公理审计，不能替代补完。
- **"POPL 2018 有会议论文集。"** PACMPL 时代的 POPL 论文是期刊文章——按卷号、
  Issue POPL、article number 引用。

## 与 PLDI/OOPSLA/ICFP 的分工

四个 SIGPLAN 旗舰同发 PACMPL，档案价值等同；差别在审稿人群与证据形态。一句话
判据：主张以"我们证明了"开头且删掉实现仍然成立，投 POPL；主张靠加速比或
benchmark 表撑起，投 PLDI；证据是用户研究或语料分析，投 OOPSLA；贡献是函数式
范式内的抽象与技术，投 ICFP。详见 `popl-topic-selection` 的路由表。

## 维护说明

- 以上所有带日期的事实都是 **2026-07-08 的单周期快照**，且多数经搜索渲染读取
  （直接抓取被封锁）。在依据任何截稿、页数或徽章规则行动前，先打开 live CFP。
- 2026 年 7 月 9 日是 POPL 2027 的截稿，不是自然规律；不要外推到后续周期，
  未渲染的 response 窗口与修订截止在直接打开 dates 页面之前一律视为未知。
- 主席名单、HotCRP 实例、徽章措辞与 double-blind 机制均为逐届决定；source map
  的易变项清单说明了每年需要复查什么。
