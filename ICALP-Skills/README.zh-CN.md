# ICALP Skills

面向 **ICALP —— EATCS International Colloquium on Automata, Languages, and Programming** 论文的 12 个
agent skills。ICALP 是欧洲理论计算机科学的旗舰会议，也是欧洲理论计算机科学学会（EATCS）的年会。本包
覆盖一次 ICALP 投稿的完整流程：判断结果是否适合 ICALP，以及属于 **Track A**（算法、复杂性、博弈）还是
**Track B**（自动机、逻辑、语义）；把论文写成能经受领域专家审稿人*逐步核对*的定理论文；准备
lightweight double-blind 的 HotCRP 投稿（15 页正文 + full-version 附录）；应对 Track B 的 rebuttal；
直至完成 **LIPIcs** 开放获取的 camera-ready。

官方依据核验日期：**2026-07-09**。已核验 ICALP 2026（第 53 届，Royal Holloway）的 Call for Papers 与
Important Dates、Track A / Track B 的 HotCRP 站点、EATCS 系列与奖项页面，以及 LIPIcs/Dagstuhl 的作者
说明。核验环境中若干官方主机（Royal Holloway 站点、CFP PDF、邮件列表存档、WikiCFP）返回 403，因此通过
搜索引擎对精确 URL 的渲染阅读官方页面，并与 **dblp** 及 **DROPS/LIPIcs** 的 ICALP 卷交叉核对；完整记录
（含所有 待核实 项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> 同类会议提醒：ICALP **不是** STOC、FOCS 或 SODA（美国 ACM/SIAM 理论会议），也不是 LICS。它是 EATCS
> 的欧洲旗舰、LIPIcs 开放获取、单一截止日、双 track。本包中的事实均不来自那些会议。

## ICALP 与同类会议的区别

以下会议机制（按 2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从美国理论会议、系统/ML 会议或
期刊转投作者最常犯的错误：

- **两个 track、两个委员会、两个 HotCRP 服务器。** **Track A —— 算法、复杂性、博弈** 与 **Track B ——
  自动机、逻辑、语义与程序理论**。选 track 是有实质后果的真实决策（Track B 有 rebuttal，Track A 没有）。
- **每年单一截止日。** ICALP 每年设**一个二月截止日**（ICALP 2026：摘要 2 月 3 日，投稿 2 月 6 日，
  AoE）。错过就是一整年 —— 没有第二轮。
- **15 页 extended abstract + full version。** 正文 **≤15 页**（不含参考文献与**明确标注的附录**）；
  附录放省略的证明或 full version，由程序委员会自行决定是否阅读。camera-ready 用 **LIPIcs
  `lipics-v2021`**。
- **Lightweight double-blind。** 投稿匿名、自引用第三人称，但该机制刻意保持轻量 —— 目的是无偏的首轮
  阅读，而非让作者身份不可发现。（ICALP 历史上曾是 single-blind，近年改为 lightweight double-blind ——
  每届核验。）
- **作者互动不对称。** **Track B** 有 rebuttal 窗口（2026：3 月 21-24 日）；**Track A** 仅在**正确性**
  问题上联系作者。**没有返修轮** —— 投稿在截止日就必须正确。
- **没有 artifact evaluation。** ICALP 是纯理论：贡献是**定理**，“artifact” 的对应物是**含完整证明的
  full version**（外加可选的形式化）。本包因此把常规的 artifact/reproducibility skills 改造为**证明
  严谨性**。
- **LIPIcs 开放获取。** 论文集在 Schloss Dagstuhl 以 Creative Commons 发布，免费阅读、无读者付费墙 ——
  是 EATCS/欧洲的开放获取模型，而非 ACM/IEEE 模型。

## Skills

| Skill | 作用 |
| --- | --- |
| [`icalp-topic-selection`](skills/icalp-topic-selection/SKILL.md) | 判断 ICALP vs STOC/FOCS/SODA/LICS 或期刊，以及 Track A vs Track B，依据贡献形态、审稿社区与单一二月日历。 |
| [`icalp-workflow`](skills/icalp-workflow/SKILL.md) | 从二月截止日倒排单周期年度计划，经摘要注册、Track B rebuttal、四月通知与 LIPIcs camera-ready。 |
| [`icalp-writing-style`](skills/icalp-writing-style/SKILL.md) | 构建理论骨架：先给模型再给定理、首页写清陈述与相对已有界的改进、在 15 页内让审稿人能核对证明。 |
| [`icalp-related-work`](skills/icalp-related-work/SKILL.md) | 对照已知最优界定位，正确归功 TCS 会议与期刊版本，并在 double-blind 下保持自引第三人称。 |
| [`icalp-experiments`](skills/icalp-experiments/SKILL.md) | 让证明策略匹配论断形态，并处理合理支撑定理的计算（SAT/SMT 证书、穷举基例），而不使论文沦为实验论文。 |
| [`icalp-reproducibility`](skills/icalp-reproducibility/SKILL.md) | 让结果可核对：完整自足的证明、full version、可复现证书，及可选的 Coq/Lean/Isabelle 形式化。 |
| [`icalp-supplementary`](skills/icalp-supplementary/SKILL.md) | 按决策重要性划分：正文赢得信任、附录供核验，决定录用的内容不得藏在无人读的附录里。 |
| [`icalp-submission`](skills/icalp-submission/SKILL.md) | HotCRP 终审：正确 track 服务器、摘要注册、15 页预算、double-blind 清扫、禁止一稿多投、格式拒稿分诊。 |
| [`icalp-review-process`](skills/icalp-review-process/SKILL.md) | 建模流程 —— 两个委员会、以正确性为中心的评审、Track B rebuttal vs Track A 正确性联系、单一 accept/reject —— 及作者杠杆点。 |
| [`icalp-author-response`](skills/icalp-author-response/SKILL.md) | 撰写 Track B rebuttal（或回应 Track A 正确性询问）：纠正误读、指向确切引理、诚实承认真实缺口、保持匿名。 |
| [`icalp-artifact-evaluation`](skills/icalp-artifact-evaluation/SKILL.md) | 理解 ICALP 为何无 artifact track 及其替代物 —— 避免从系统/ML 会议来的作者构建无人评审的包。 |
| [`icalp-camera-ready`](skills/icalp-camera-ready/SKILL.md) | 转为 `lipics-v2021`、去匿名、补全 LIPIcs 元数据（ORCID/CCS/funding/related-version）、与 full version 对齐、通过 Dagstuhl 生产。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口（ICALP、EATCS、HotCRP、LIPIcs/DROPS）与网关阻断时的交叉核对来源，以及作者端核查。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 七篇经网络核验的 ICALP 论文，覆盖两个 track、七种贡献形态（Best Paper 与 Best Student Paper），附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构动态图结果的摘要与引言按 ICALP 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 submission-readiness 工具，并给出通用套件无法完成的 ICALP 证明与匿名检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./ICALP-Skills
claude plugin install icalp-skills
```

也可直接使用文件：每个 `skills/icalp-*/SKILL.md` 都是独立指令文件，其 frontmatter `description` 告诉
agent 何时触发。典型调用：

- “这篇是 ICALP Track A 还是 Track B —— 或该投 STOC/SODA？” → `icalp-topic-selection`
- “按 ICALP 规则审我的稿” → `icalp-submission`
- “拿到 Track B 审稿意见 —— 帮我写 rebuttal” → `icalp-author-response`
- “把录用论文准备成 LIPIcs camera-ready” → `icalp-camera-ready`

## 目录结构

```text
ICALP-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面
├── skills/
│   └── icalp-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `icalp-topic-selection`；ICALP-vs-同类 *和* Track A-vs-B 两个决策都重要。浏览
   exemplars 看两个 track 里十年影响力的 ICALP 贡献长什么样。
2. **证明时** —— 让 `icalp-experiments` 与 `icalp-reproducibility` 贴着工作；只“相信”而未写出的证明
   无法录用，证明中用到的计算必须可核对。
3. **写作时** —— 用 `icalp-writing-style` 对照 worked example 打磨正文，用 `icalp-supplementary`
   划分正文/附录，用 `icalp-related-work` 做 delta-first 定位。
4. **截止周** —— 先在较早的二月注册截止日前完成摘要注册，再用 `icalp-submission` 在正确 track 服务器上
   对终稿逐项过审。
5. **投稿后** —— 用 `icalp-review-process` 校准预期，用 `icalp-author-response` 应对 Track B rebuttal
   （或 Track A 正确性询问），随后 `icalp-camera-ready` —— 若结果不利，则用 `icalp-topic-selection` 的
   路由表改投。

## 2026 周期锚点事实（历史快照，非永久规则）

- ICALP 2026 为**第 53 届**：**Royal Holloway, University of London**（英国 Egham），会议
  **2026 年 7 月 7-10 日**（workshops 7 月 6 日），与 **PODC**、**SPAA** 同地举办。
- **日历（AoE）：** 摘要注册 **2026-02-03**，投稿 **2026-02-06**；**Track B rebuttal 2026-03-21 至 24**；
  通知 **2026-04-20**。
- **格式：** extended abstract **≤15 页**（不含参考文献 + 明确标注的附录，附录放省略证明或 full
  version）；camera-ready 用 **LIPIcs `lipics-v2021`**。
- **评审：** lightweight **double-blind**；**Track A** 算法/复杂性/博弈，**Track B** 自动机/逻辑/语义；
  单一 **accept/reject**。出版：**LIPIcs**，开放获取。
- **奖项：** 每个 track 的 best paper 与 best student paper；会议还颁发 **EATCS Award**、**Presburger
  Award**、**EATCS Distinguished Dissertation Award** 与 **Gödel Prize**（EATCS/ACM SIGACT，偶数年在
  ICALP 颁发）。PC chairs（转述）：Track A **Sayan Bhattacharya**、**Danupon Nanongkai**；Track B
  **Michael Benedikt**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（双 track 结构、15 页格式、
   二月日期、LIPIcs 出版）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如完整 PC-chair 名单、Gabriele Puppis 在 Track B 的
   确切角色）。
3. **核验期不可确定项** —— 明确标为 待核实（如 2026 录用率与录用篇数、camera-ready 截止日、ICALP 2027
   主办地、任何 AI 披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。ICALP 每届重定细节 —— 每年先在当届 call 上核验日期、篇幅规则与匿名
  机制。
- ICALP 无常任 editor-in-chief、无读者付费墙；PC chairs 与本地组委每届在 EATCS 与 ICALP steering
  committee 下轮换。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程 —— 熟悉的定理名并不能证明该论文发表于 ICALP（PCP 定理在 FOCS；AKS 在期刊）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
