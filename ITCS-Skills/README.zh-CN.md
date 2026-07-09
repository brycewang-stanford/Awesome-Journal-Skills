# ITCS 技能包

面向投稿 **ITCS —— 理论计算机科学创新会议（Innovations in Theoretical Computer Science）** 的
十二个 agent 技能。ITCS 自 2010 年创立起，其定位就是奖励 **概念创新** 的理论会议：一个新模型、
一个新问题、一个出人意料的联系、一个领域此前未曾想到的方向。STOC、FOCS 奖励的是当年最深、最完善
的定理，而 ITCS 首先问的是另一个问题——*这是不是一个值得提出的新问题？* 整个技能包都围绕这一评审
气质来编写。它覆盖一次 ITCS 投稿的完整链条：判断一个想法是否"ITCS 型"，还是应投 STOC/FOCS/SODA
或期刊；把概念贡献写得让程序委员会在看到定理之前就先看到创新；准备轻量双盲的 LIPIcs 投稿并附
**完整证明**；理解 **无 rebuttal** 的评审；以及完成开放获取的 LIPIcs camera-ready。

官方依据核验于 **2026-07-09**：ITCS 2026（米兰 Bocconi）HotCRP 站点与截止日期页、`itcs-conf.org`
的历年 call for papers、LIPIcs/DROPS 会议录（第 362 卷 = ITCS 2026）、dblp 的 `conf/innovations`
数据流、Bocconi 计算科学系的 ITCS 2026 页面，以及维基百科的历史条目。在核验环境中直接抓取
`itcs2026.hotcrp.com`、`itcs-conf.org`、`cs.unibocconi.eu`、`drops.dagstuhl.de` 均返回 403，因此
官方页面通过对确切 URL 的搜索引擎渲染阅读，并至少在两个独立来源之间交叉核对；完整证据链（含所有仍
标注 待核实 的条目）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> 缩写撞名提醒：有若干无关会议也缩写为 "ITCS"（IEEE 智能交通系统会议实为 *ITSC*；WikiCFP 上还有各种
> "Information Technology and Computer Science / Convergence and Services" workshop）。**本包无一事实
> 源自它们**——每一条来源都对应 *Innovations in Theoretical Computer Science*。

## ITCS 与兄弟会议有何不同

以下 2026 周期已核验的会议机制，驱动了各技能中的大部分建议，也是从 STOC/FOCS、SODA 或期刊转投而来
的作者最常犯错之处：

- **概念创新是遴选标准，而非并列时的加分项。** ITCS 明确寻找引入新模型、提出新问题、建立意外联系的
  论文。一个技术上无懈可击但增量式的结果，即便凭深度足以进 STOC/FOCS，也可能因缺少*新想法*而被
  略过；而一个大胆但不完美的新方向反而可能被接收。先把创新写出来。
- **纯理论：思想与证明，没有代码。** 这里 **没有 artifact 评审、没有可复现性打包**。"可复现性"的对应
  物是一份**完整、可核验的证明**；"artifact"的对应物是让评审能验证每一条核心论断的**完整版附录或
  arXiv/ECCC 预印本**。
- **每年一次截稿，在九月初。** ITCS 2026 于 **2025 年 9 月 6 日** 截稿，十一月通知，次年一月开会
  （Bocconi，2026 年 1 月 27–30 日）。每年仅一次投稿截止——没有滚动轮次，没有第二周期。
- **轻量双盲。** 投稿隐去姓名、单位、邮箱，但**鼓励作者把完整版发到 arXiv / ECCC / Cryptology
  ePrint**，且重要参考文献**不**匿名。之所以"轻量"，是因为通过预印本去匿名被容忍而非查处。
- **无 rebuttal。** 遵循理论会议惯例，ITCS 在**没有作者答辩轮次**、没有 revise-and-resubmit 的情况下
  作出接收/拒稿决定。没有第二次申辩的机会——投稿必须在提交前就回应审稿人的可能异议。
- **LIPIcs 开放获取，无 APC。** 论文以 `lipics-v2021` 文类发表于 **LIPIcs**（Schloss Dagstuhl），
  开放获取、CC 许可、**无版面费**。这是 Dagstuhl 路线，不是 ACM `acmart`、也不是 IEEE `IEEEtran`。
- **版面宽松但需完整证明，并有前 10 页"亮点窗口"。** 投稿单栏、字号 >= 11pt，**无硬性页数上限**；
  惯例是前 10 页呈现论文的亮点与意义，随后附**完整证明**（可置于附录）。
- **Graduating Bits 文化。** 一个由临近毕业（前后皆可）的研究者作简短报告的固定环节，赋予 ITCS 一种
  更小圈子、定方向、以人为先的氛围，也塑造了会场所奖励的东西。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`itcs-topic-selection`](skills/itcs-topic-selection/SKILL.md) | 用概念创新测试、"值得提出的新问题"筛选和单一截稿日历，在 ITCS 与兄弟会议（STOC、FOCS、SODA、CCC、ICALP、期刊）之间选路。 |
| [`itcs-workflow`](skills/itcs-workflow/SKILL.md) | 从九月初截稿倒推整年：无 rebuttal 评审、十一月通知、LIPIcs camera-ready、一月报告。 |
| [`itcs-writing-style`](skills/itcs-writing-style/SKILL.md) | 打磨 ITCS 首页：在定理之前先讲概念贡献与*问题为何是新的*，诚实的范围与局限姿态，完整证明干净地后置。 |
| [`itcs-related-work`](skills/itcs-related-work/SKILL.md) | 在理论文献中定位，写清"该模型/问题为何是新的"差异，并在轻量匿名下保持诚实（参考文献不匿名）。 |
| [`itcs-experiments`](skills/itcs-experiments/SKILL.md) | 把证据匹配到*理论*论断：证明为主要证据，配以举例与分离结果，以及罕见且界定清晰的示例性实验或模拟。 |
| [`itcs-reproducibility`](skills/itcs-reproducibility/SKILL.md) | 让数学可核验：完整证明、自足定义、arXiv/ECCC 上的完整版，以及对所依赖前人结果的追溯。 |
| [`itcs-supplementary`](skills/itcs-supplementary/SKILL.md) | 按"审稿人必须核验什么"在正文与附录/完整版之间切分——任何核心证明都不得只存在于 PC 无需阅读的预印本里。 |
| [`itcs-submission`](skills/itcs-submission/SKILL.md) | 最终 HotCRP 审查：单栏 >= 11pt 格式、前 10 页亮点窗口、轻量双盲清查、证明完整性、以及归档式先前发表检查。 |
| [`itcs-review-process`](skills/itcs-review-process/SKILL.md) | 建模评审流程——PC 加外审、概念创新权重、轻量双盲、**无 rebuttal**、接收/拒稿——以及作者（有限的）着力点。 |
| [`itcs-author-response`](skills/itcs-author-response/SKILL.md) | 应对 ITCS **没有 rebuttal** 的现实：在投稿中预先化解异议，并处理决定后的通信、改投选路与 camera-ready 窗口。 |
| [`itcs-artifact-evaluation`](skills/itcs-artifact-evaluation/SKILL.md) | 把"artifact"适配到纯理论：完整证明附录与 arXiv/ECCC 完整版*就是* artifact——如何在无代码轨道下让论断可独立核验。 |
| [`itcs-camera-ready`](skills/itcs-camera-ready/SKILL.md) | 去匿名、切换 `lipics-v2021` 文类、补齐 LIPIcs 元数据（ACM CCS、关键词、资助），通过 Dagstuhl 开放获取出版的生产检查。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验的 2026 事实；访问方法说明；显式的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方站点与网关受阻时的交叉核对来源，以及作者侧核验环节。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 跨概念贡献类型、已核验的 ITCS 论文，附自检问题与兄弟会议防混淆护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构新模型论文的摘要与引言，按 ITCS"创新先行"结构重写，前 -> 后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 为何这一纯理论包不附带代码工具集，以及取而代之的证明可核验性检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是带有自身 marketplace 清单的自包含插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./ITCS-Skills
claude plugin install itcs-skills
```

或直接使用文件：每个 `skills/itcs-*/SKILL.md` 都是独立指令文件，其 frontmatter 的 `description`
告诉 agent 何时触发。典型调用：

- "这是 ITCS 论文，还是该投 STOC/FOCS/SODA？" -> `itcs-topic-selection`
- "把我的新模型写得让创新在第一页就落地" -> `itcs-writing-style`
- "按 ITCS 投稿规则审查我的草稿" -> `itcs-submission`
- "ITCS 没有 rebuttal——拿到评审后我还能做什么？" -> `itcs-author-response`

## 建议流程

1. **动笔前** —— 先跑 `itcs-topic-selection`；ITCS 与 STOC/FOCS/SODA 在范围上重叠，但按不同的轴
   （问题的新颖性）遴选，因此选对会议是收益最高的一步。翻看范例库，看看这里的"创新"长什么样。
2. **构思时** —— 让 `itcs-writing-style` 与 `itcs-related-work` 常伴草稿；概念贡献及其新颖性差异
   必须在首页可读，而不是要到第 4 节才挖出来。
3. **证明时** —— 用 `itcs-reproducibility` 与 `itcs-supplementary` 做到完整可核验的证明与正文/附录
   切分；仅当示例性模拟确实有助于某个论断时才用 `itcs-experiments`。
4. **截稿周** —— 用 `itcs-submission` 对最终 PDF 全流程走查：格式、前 10 页亮点窗口、轻量双盲清查、
   证明完整性。
5. **投稿后** —— 用 `itcs-review-process` 校准预期，用 `itcs-author-response` 面对无 rebuttal 的现实
   与决定后改投；随后用 `itcs-camera-ready` 完成 LIPIcs 生产环节——若结果相反，则回到
   `itcs-topic-selection` 的选路表。

## 2026 周期锚点事实（历史快照，非永久规则）

- ITCS 2026 是第 **17** 届：**意大利米兰 Bocconi 大学，2026 年 1 月 27–30 日**；摘要/注册
  2025 年 9 月 4 日，投稿 9 月 6 日（美东时间 19:59:59），通知约 11 月 10 日；经
  `itcs2026.hotcrp.com`。会议录：**LIPIcs 第 362 卷**。
- 出版：**LIPIcs**（Schloss Dagstuhl），开放获取，无 APC，`lipics-v2021` 文类。评审：
  **轻量双盲**、**无 rebuttal**、接收/拒稿。
- 格式：单栏、字号 >= 11pt、**无硬性页数上限**；前 10 页亮点窗口；须附**所有核心论断的完整证明**
  （允许放附录）。
- ITCS 2027 的主办地/日期/截稿在 2026-07-09 时点仍为 **待核实**——请重开当期 call。

## 事实纪律

本包区分三类陈述，各技能均力求保持其可辨：

1. **已核验的 2026 事实** —— 带日期/格式并可溯源到源图中的编号来源（如 LIPIcs 第 362 卷、九月初
   截稿、轻量双盲规则、无 rebuttal 惯例）。
2. **转述事实** —— 仅经单一二手渲染读到并如实标注（如 ITCS 2026 程序主席姓名与本地组织者名单）。
3. **核验时不可确认项** —— 显式标 待核实（如 ITCS 2027 主办地/日期、camera-ready 页数上限、2026
   接收率与论文数）。

若任何陈述以第一类口吻呈现第二、三类材料，视为 bug，须对照官方现行页面修正。

## 维护说明

- 上文每个日期都是**周期快照**。ITCS 每届轮换主办地与主席，且每年单一截稿；每年动手前先核验当期 call。
- ITCS 无常设主编、无 APC；程序主席与 PC 每届轮换。
- 新增范例论文时，请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  核验流程——著名作者或熟悉的定理并不能证明它发在 ITCS（可能是 STOC、FOCS、SODA 或期刊）。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
