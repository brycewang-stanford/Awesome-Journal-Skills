# MobiCom Skills（中文说明）

面向 **MobiCom —— ACM 移动计算与网络国际会议（ACM International Conference on Mobile
Computing and Networking）** 投稿的 12 个 agent skills。MobiCom 是 ACM SIGMOBILE 的旗舰
会议，是移动与无线网络系统被设计、实现并在真实无线电上测量的地方。本包围绕一次真实
MobiCom 投稿流程展开，而这套流程既不同于单一 deadline 的会议，也不同于 USENIX 风格的
系统会议：**每年两次的 rolling deadline**（每次 deadline 面向的是*下一届*会议）、**两轮
审稿 + early-reject 早拒 + rebuttal 窗口**、在此之上**保留的 one-shot major revision**、
ACM 双栏排版，以及一条用物理层语言写成的证据线——over-the-air 测量、信道与移动性条件、
真实硬件上的能耗。

官方依据于 **2026-11-24 重新核验**（直接抓取）：`sigmobile.org` 上的 MobiCom 2027 主页、
Call for Papers、Call for Artifacts 与委员会页，`mobicom27.hotcrp.com` 截止时钟，MobiCom
2026 主页与 CFP（历史），SIGMOBILE MobiCom 落地页，以及 SIGMOBILE Test-of-Time 奖页面。最初
2026-07-09 的核验（含用于 exemplar 核验的 dblp / ACM Digital Library）因 `sigmobile.org`、
`hotcrp.com`、`dblp.org` 当时返回 **HTTP 403**，是通过搜索引擎对官方 URL 的渲染读取的。完整
链路（含全部 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## MobiCom 与近邻会议的区别

- **每年两次 rolling deadline，每次面向下一届。** MobiCom 自第 25 届（2019）起采用
  multi-deadline 模式；每轮各开一次 PC meeting。**MobiCom 2027**（第 33 届，**2027 年
  10 月 18-22 日，希腊雅典**）的夏季轮已于 2026 年 8/9 月截稿（正文 2026-09-02 AoE，
  2026-11-19 出结果），冬季轮日期官方仍标为 **“TBD”**。
- **两轮审稿 + rebuttal，而非一锤定音。** 同一 deadline 内，第一轮未晋级的稿件会收到附带
  reviews 的早拒通知；晋级稿件进入第二轮，reviews 在固定 **rebuttal 窗口**前释放——rebuttal 可选、
  **不超过 500 词**，只能更正事实错误或回答问题，不得加入新实验、新数据或新图。这与
  完全没有 rebuttal 的 USENIX 会议是不同的响应面。
- **在 rebuttal 之上仍保留 one-shot revision。** 除 accept/reject 外，MobiCom 保留 major
  revision 通道（最多 **三** 项必改，在下一个 deadline 重投）；修改稿按拿到的 issue list 返回
  审稿人。录用先是 **有条件录用**，需经 4-6 周匿名 shepherding；普通拒稿 **11 个月** 内不得
  再投 MobiCom。
- **每篇投稿带来一位审稿人。** 2027 新增：每篇稿件指定一位资深作者，在同一轮审最多三篇稿件。
- **双栏、12 页且图表计入。** 正文上限为 12 页单倍行距编号页，**含图表**，采用 ACM 双栏
  几何；references（及其后从新页开始的可选 appendix）不计入上限；PDF 不得含嵌入超链接、
  小于 15 MB，使用 `acmart` `sigconf,10pt`。
- **HotCRP 上的 double-blind。** 稿件在每届 `mobicom<yy>.hotcrp.com` 站点匿名提交；
  abstract/registration 步骤（摘要至少 100 词，不得写 “TBD”）先于正文上传。
- **ACM artifact badges，而非 USENIX 方案。** 录用与有条件录用论文可申请三种 ACM 徽章：
  *Artifacts Available*、*Artifacts Evaluated — Functional*、*Results Reproduced*。
- **ACM 开放获取。** 所在机构未加入 ACM Open 的作者需付 APC（可申请减免；2027 补贴价：
  ACM/SIG 会员 500 美元、非会员 750 美元）；每篇录用论文须交 90 秒预告视频并由作者到场报告。
- **证据在空口上测量。** MobiCom 的审稿文化要求真实设备 testbed、RF/信道测量方法、移动性
  真实度与能耗核算；纯仿真或单次运行结果在这里会被视为评估不足。
- **SIGMOBILE Test-of-Time 奖** 锚定了本领域经典，并在 MobiCom 上颁发。

## Skills

| Skill | 作用 |
| --- | --- |
| [`mobicom-topic-selection`](skills/mobicom-topic-selection/SKILL.md) | 判断贡献是否为 MobiCom 认可的移动/无线网络机制，并把平台、传感、宽泛网络、安全类不匹配稿件路由到 MobiSys、SenSys、SIGCOMM/NSDI 或 WiSec。 |
| [`mobicom-workflow`](skills/mobicom-workflow/SKILL.md) | 针对夏/冬 rolling deadline 对做规划：某一轮面向哪一届、为空口实验留出时间的倒排表、早拒与 revision 如何改变计划。 |
| [`mobicom-writing-style`](skills/mobicom-writing-style/SKILL.md) | 在双栏 12 页内构建 无线痛点 → 机制 → 可测证据 的论证弧，用分位数与置信区间替代形容词。 |
| [`mobicom-related-work`](skills/mobicom-related-work/SKILL.md) | 梳理 SIGMOBILE 与网络文献分线，用 dblp/ACM DL 核验会议出处以避开 INFOCOM/SIGCOMM/NSDI 误标，并做 blind-safe 自引。 |
| [`mobicom-experiments`](skills/mobicom-experiments/SKILL.md) | 设计真实 testbed 评估：RF/信道测量方法、移动性条件、能耗剖析、在调优硬件上的 baseline 与诚实 ground-truth。 |
| [`mobicom-reproducibility`](skills/mobicom-reproducibility/SKILL.md) | 记录无线电、硬件、信道与移动性 provenance，使结果能在不同 testbed 上复现，并尽早决定哪些 trace 与固件可合法发布。 |
| [`mobicom-supplementary`](skills/mobicom-supplementary/SKILL.md) | 在 12 页正文、references、可选 appendix 与 HotCRP 字段之间分配内容，并把 rebuttal/revision 包排除在页数上限之外。 |
| [`mobicom-artifact-evaluation`](skills/mobicom-artifact-evaluation/SKILL.md) | 为 AEC 打包：申请哪几种 ACM 徽章、为没有无线电的评审提供硬件可选路径、以及证明 functional 的 smoke run。 |
| [`mobicom-submission`](skills/mobicom-submission/SKILL.md) | 终审：正确的 HotCRP 站点与轮次、AoE 截止、12 页双栏核查、含无线电 trace 泄露的匿名扫描、以及 abstract 先注册的前置条件。 |
| [`mobicom-review-process`](skills/mobicom-review-process/SKILL.md) | 读懂两轮流程的结果空间——早拒、rebuttal、accept、one-shot revision——以及影响 revision 策略的审稿人连续性。 |
| [`mobicom-author-response`](skills/mobicom-author-response/SKILL.md) | 在字数限制内完成 rebuttal，并单独把 one-shot revision 当作一份对 required-changes 清单的契约来执行。 |
| [`mobicom-camera-ready`](skills/mobicom-camera-ready/SKILL.md) | 交付去匿名的双栏终稿、完成 ACM 版权与元数据、协调 artifact 徽章并规划现场报告。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 官方来源 URL 与访问日期、已核验事实清单、access-method 说明（sigmobile.org / hotcrp.com / dblp.org 直接抓取均 403）、以及明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方页面入口，加上五道作者侧核验（clock、budget、blindness、status、revision/rebuttal）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经会议核验的 MobiCom 论文（2000-2013）覆盖五个子领域，各附 self-check，并含 RADAR/XORs/WiSee-demo 误标防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构 backscatter 链路论文的摘要与引言，改写成 MobiCom 可测证据弧，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享可复现工具包的适配器，并列出通用工具无法核验的 MobiCom 专有项（无线电 provenance、信道条件、能耗）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆内执行
claude plugin marketplace add ./MobiCom-Skills
claude plugin install mobicom-skills
```

也可直接使用文件：每个 `skills/mobicom-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 会告诉 agent 何时触发。典型调用：

- “这是 MobiCom 论文还是 MobiSys 论文？” → `mobicom-topic-selection`
- “我们在为哪一轮写作，它面向哪一届？” → `mobicom-workflow`
- “reviews 出来了——起草 rebuttal”或“我们拿到 major revision” → `mobicom-author-response`
- “上传 HotCRP 前审一遍 PDF” → `mobicom-submission`

## 目录结构

```text
MobiCom-Skills/
├── .claude-plugin/               # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                     # 英文说明
├── README.zh-CN.md               # 本文件
├── LICENSE                       # MIT
├── assets/cover.svg              # 封面
├── skills/
│   └── mobicom-<topic>/SKILL.md  # 12 个 skill，每个一个目录
└── resources/
    ├── README.md                 # 资源导引 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md            # 指向共享可复现工具包的适配器
```

## 建议路线

1. **先定位**——`mobicom-topic-selection` 判定范围与兄弟会议路由，`mobicom-workflow`
   判定这一轮面向哪一届、无线电实验能否赶上；exemplars library 展示什么能过线。
2. **搭建证据**——`mobicom-experiments` 与 `mobicom-reproducibility` 就在 testbed 旁；
   信道日志、移动性条件与能耗 trace 事后无法重建。
3. **写作**——`mobicom-writing-style` 对照 worked example，`mobicom-supplementary`
   处理正文/附录切分，`mobicom-related-work` 打开当轮 cohort 与会议核验流程。
4. **deadline 周**——`mobicom-submission` 对确切上传候选逐项过一遍。
5. **通知之后**——`mobicom-review-process` 分类结果，随后 `mobicom-author-response`
   （rebuttal 或 revision），或 `mobicom-artifact-evaluation` + `mobicom-camera-ready`
   （录用）。

## 事实纪律

全包始终区分三类陈述：

1. **已核验的周期事实**——日期、上限与规则，均可溯源到 source map 中的编号来源（例如 12 页
   双栏规则、两轮 + 500 词 rebuttal 流程、2026-09-02 夏季轮 deadline）。
2. **据报事实**——仅由二手渲染承载并如实标注（例如经作者机构转述的 Best-Paper 结果）。
3. **待核实 项**——明确标出并以问句表述（例如 2027 冬季轮日期、2027 camera-ready
   截止、注册费）。

任何把第 2 类或第 3 类当作第 1 类陈述的地方都是 bug；请对照实时页面修正。

## MobiCom 2027 锚点事实（带日期的快照，非永久规则）

- **MobiCom 2027** 为第 **33** 届：**2027 年 10 月 18-22 日，希腊雅典**。General Co-Chairs
  Dimitrios Koutsonikolas、Symeon Papavassiliou；TPC Co-Chairs Joerg Widmer、Nirupam Roy。
- **夏季轮**（已出结果）：摘要 **2026-08-26**、正文 **2026-09-02**（23:59 AoE），早拒
  2026-10-23，rebuttal 2026-11-03 至 11-06，录用通知 2026-11-19。**冬季轮：TBD**（2026-11-24）。
- Artifact：夏季轮截止 2027-01-17（通知 2027-02-17）；冬季轮截止 2027-07-24（通知 2027-08-24）。
- 格式：**12 页双栏、含图表**，references 与可选 appendix 不计入；HotCRP 上 **double-blind**；
  rebuttal 不超过 500 词。
- 历史：**MobiCom 2026**（第 32 届）于 2026 年 10 月 26-30 日在美国德州 Austin 举行；其冬季轮
  摘要 2026-03-06、正文 2026-03-13（AoE）。

## 维护说明

- 以上每个日期都是 **MobiCom 2027 快照**（2026-11-24 重新核验）。MobiCom 每届重发规则、且每年两次 deadline——涉及
  deadline 时，务必重新打开当年 CFP 与对应的 HotCRP `/deadlines` 页。
- deadline 是 **AoE** 截止，即便页面印的是美东时钟时间；切勿沿用上一周期的本地换算。
- **某一轮面向哪一届** 每个周期都会移动——在实时 CFP 上确认你瞄准的轮次确实是你以为的那届。
- Chairs 每届轮换——引用前请查委员会页（上面 2027 名单读取于 2026-11-24）。
- 新增 exemplar 必须通过 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的会议核验流程；无线领域最著名的论文恰恰最常被在 INFOCOM/SIGCOMM/NSDI 之间误标。

## License

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
