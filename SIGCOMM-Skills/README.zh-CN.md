# SIGCOMM Skills

面向 **ACM SIGCOMM** 论文的 12 个 agent skills。SIGCOMM 是 **ACM 数据通信专业组（ACM
Special Interest Group on Data Communication）的旗舰会议**，是计算机网络与通信系统设计、
测量、分析领域的顶级年度会场。本包围绕 SIGCOMM 投稿的真实节奏组织，而这一节奏与它的网络类
兄弟会场差别很大——从 USENIX 或 SIGMOBILE 转来的作者常常低估这一点：**每年只有一个正会
截稿**，喂给 **一场** 8 月的会议；评审流水线叠加了 **early-reject 早退**、**rebuttal**
与 **由 shepherd 主持的 one-shot revision**；录用后论文继续由 **shepherd** 陪跑到
camera-ready；采用 ACM 双栏排版并经 **TAPS** 出版；证据门槛用 **真实流量、真实拓扑、
尾延迟与可复现的“runnable”artifact** 的语言书写。

官方依据核验日期：**2026-07-09**。已核验 `conferences.sigcomm.org` 上的 ACM SIGCOMM 2026
会议页、Call for Papers、submission 与 camera-ready 页；`sigcomm26.hotcrp.com` 的截稿时
钟；SIGCOMM Call for Artifacts 与 `sigcomm.org` 的 Test-of-Time、Best-Paper 奖项页；以及
dblp / ACM Digital Library 用于范例核验。核验环境中直接抓取
`conferences.sigcomm.org`、`sigcomm.org`、`hotcrp.com`、`dblp.org` 均返回 **HTTP 403**，
因此以下每条事实都是通过搜索引擎对精确官方 URL 的渲染读取并交叉核对得到；完整轨迹（含所有
仍标注 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## SIGCOMM 与兄弟会场的不同

以下机制按 2026 版核验，驱动着 skills 中的大部分建议，也是双截稿会场作者最常踩的坑：

- **一个截稿、一场会议、一年一次机会。** SIGCOMM 2026（**第 40 届**，2026 年 8 月 17-21 日，
  Colorado Convention Center，丹佛）摘要注册 **2026-01-30**、全文 **2026-02-06**（AoE；
  HotCRP 页面渲染为次日 6:59:59 AM EST）。没有 fall 补投口——被拒的论文要等整整一年，
  这让单次投稿的赌注远高于 spring/fall 会场。
- **一个截稿、两条赛道。** 投稿在 **research** 与 **experience**（运营与部署经验）两条赛道
  中择一；experience 赛道看的是真实运营中可推广的经验教训，而非单纯的新颖性。
- **面向作者的三层评审流水线。** 共识拒稿会给 **early notification** 以便及早转投；进入
  discussion 阶段的论文会有 **rebuttal**；少数论文会拿到 **one-shot revision**——附带亮点
  小结与必须修改清单，约一个月后重投，**由 PC shepherd 主持**，尽量由原审稿人复审，最终
  只能是 **accept 或 reject**。
- **Shepherding 不止于录用。** PC shepherd 陪跑录用论文到 camera-ready，确认审稿意见已被
  回应，并 **必须批准任何 appendix 的必要性**，在 HotCRP 上签署最终版。
- **12 个单倍行距页、含图表。** 正文（references 之前的全部内容）上限为 **12 个单倍行距页，
  含图与表**；references 与可选 appendix 不计入上限；references 之前超过 12 页的稿件
  **不予评审**。
- **HotCRP 双盲、全程 ACM 模板。** 投稿在 `sigcomm26.hotcrp.com` 上匿名；摘要注册先于全文
  上传；投稿与终稿都用 ACM `acmart.cls`（或 ACM Word 模板）。
- **TAPS camera-ready。** 终稿把 **PDF 加源文件** 上传到 HotCRP，经 **ACM Publishing
  System（TAPS）** 处理，进入 ACM Digital Library 与 Computer Communication Review。
- **可复现文化，而不只是一个 badge。** SIGCOMM 是网络领域 artifact evaluation 的先行者；
  录用论文可通过独立委员会获得 **ACM badges**（Artifacts Available、Evaluated、Results
  Reproduced），“runnable papers”的传统对公开代码、trace、拓扑设了很高的门槛。
- **Test-of-Time 与 Best-Paper 谱系锚定经典**——Chord、DCTCP、pFabric、VL2 等 SIGCOMM
  经典——也提醒作者：本领域最被引用的成果，也最常被误挂到 NSDI、MobiCom、CoNEXT、IMC。

## Skills

| Skill | 作用 |
| --- | --- |
| [`sigcomm-topic-selection`](skills/sigcomm-topic-selection/SKILL.md) | 检验网络栈贡献是否契合 SIGCOMM 的宽度，选 research 还是 experience 赛道，并把不合适的路由到 NSDI、MobiCom、CoNEXT、IMC 或 SIGMETRICS。 |
| [`sigcomm-workflow`](skills/sigcomm-workflow/SKILL.md) | 规划单截稿年度：倒排到 2 月的时间表、评审到 shepherd 的时间线、以及面向下一届的前向规划。 |
| [`sigcomm-writing-style`](skills/sigcomm-writing-style/SKILL.md) | 在 12 个含图页内构建 已测量的痛点 → 设计原则 → 尾部证据 的弧线，用百分位替代夸张形容词。 |
| [`sigcomm-related-work`](skills/sigcomm-related-work/SKILL.md) | 跨会场梳理网络文献，用 dblp/ACM DL 核实归属，区分正会与 CCR editorial，处理双盲安全的自引。 |
| [`sigcomm-experiments`](skills/sigcomm-experiments/SKILL.md) | 攀登证据阶梯（micro → testbed/trace → deployment），选会反击的 baseline，报告尾部、方差与失效点。 |
| [`sigcomm-reproducibility`](skills/sigcomm-reproducibility/SKILL.md) | 维护拓扑、流量、配置与运行台账；刻画方差；尽早决定哪些数据与代码可合法发布。 |
| [`sigcomm-supplementary`](skills/sigcomm-supplementary/SKILL.md) | 在正文、references 与经 shepherd 批准的 appendix 之间安排内容，在 12 页上限下保持正文自足。 |
| [`sigcomm-artifact-evaluation`](skills/sigcomm-artifact-evaluation/SKILL.md) | 为 AEC 打包：把 ACM badge 选择当作声明校准，缩比拓扑、trace 替身与快速 smoke 路径。 |
| [`sigcomm-submission`](skills/sigcomm-submission/SKILL.md) | 终审：正确的 HotCRP 注册、AoE 时钟、references 前 12 页检查、双盲扫查与赛道选择。 |
| [`sigcomm-review-process`](skills/sigcomm-review-process/SKILL.md) | 读懂结果空间（accept / one-shot revision / early 或 formal reject）以及塑造策略的 shepherd 与审稿连续性规则。 |
| [`sigcomm-author-response`](skills/sigcomm-author-response/SKILL.md) | 分别执行 rebuttal 与 one-shot revision（作为 shepherd 主持的契约）：问题分诊、change memo、标注 diff。 |
| [`sigcomm-camera-ready`](skills/sigcomm-camera-ready/SKILL.md) | 交付 TAPS 终稿于 12 页内，取得 shepherd 签署、去匿名，并在 badge 截止前发布公开 artifact。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 11 个官方来源（URL 与访问日期）、已核验事实清单、访问方法说明与显式的 待核实 登记。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方现场入口，加上五道作者侧核验（时钟、格式、双盲、赛道、状态）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 6 篇经会场核实的 SIGCOMM 论文（2001-2015），覆盖六个系统类别，每篇附自检，并有 OpenFlow-CCR / Hedera-NSDI / RED-期刊 / BBR-CACM 误挂防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的 flowlet-steering 系统的摘要与引言，按 SIGCOMM 已测量证据弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 对接共享可复现套件，并给出通用工具无法完成的 SIGCOMM 专属检查（拓扑、trace、尾部测量）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的自包含插件）：

```bash
# 从仓库克隆目录执行
claude plugin marketplace add ./SIGCOMM-Skills
claude plugin install sigcomm-skills
```

也可直接使用文件：每个 `skills/sigcomm-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 告诉 agent 何时触发。典型调用：

- “这个拥塞控制结果是 SIGCOMM 还是 NSDI 的料？” → `sigcomm-topic-selection`
- “我们 2 月只有一个截稿——给出倒排计划” → `sigcomm-workflow`
- “我们拿到了带 shepherd 的 one-shot revision——制定方案” → `sigcomm-author-response`
- “在摘要注册关闭前审一遍 PDF” → `sigcomm-submission`

## 目录结构

```text
SIGCOMM-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                    # 英文说明
├── README.zh-CN.md              # 本文件
├── LICENSE                      # MIT
├── assets/cover.svg             # 封面图
├── skills/
│   └── sigcomm-<topic>/SKILL.md # 12 个 skill，每个一个目录
└── resources/
    ├── README.md                # 资源指南 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md           # 对接共享可复现套件
```

## 建议用法

1. **决定投这一年之前** —— `sigcomm-topic-selection` 定范围与赛道，`sigcomm-workflow` 算
   单截稿的时间；范例库展示了以录用形态越过门槛的样子。
2. **搭建阶段** —— `sigcomm-experiments` 与 `sigcomm-reproducibility` 贴着 testbed 用；
   trace 出处与尾部方差刻画无法事后补齐。
3. **写作阶段** —— 对照 worked example 用 `sigcomm-writing-style`，用
   `sigcomm-supplementary` 划分正文/appendix，用 `sigcomm-related-work` 并打开网络经典、
   核实会场归属。
4. **截稿周** —— 对确切的上传候选稿端到端跑一遍 `sigcomm-submission`。
5. **收到结果后** —— 用 `sigcomm-review-process` 判定结果类型，然后
   `sigcomm-author-response`（rebuttal 或 revision），或
   `sigcomm-artifact-evaluation` + `sigcomm-camera-ready`（录用）。

## 2026 锚点事实（带日期的快照，不是永久规则）

- **SIGCOMM 2026** 为 **第 40 届**：**2026 年 8 月 17-21 日，Colorado Convention
  Center，丹佛，美国**。
- 单一正会截稿：摘要 **2026-01-30**、全文 **2026-02-06**（AoE）。Camera-ready
  **2026-07-03 23:59 UTC** 经 ACM TAPS。截至 2026-07-09，截稿已过、结果已发，当前活跃阶段
  是 camera-ready 定稿、shepherd 签署、artifact evaluation 与 8 月现场汇报——同时下一届的
  前向规划已经可以启动。
- 赛道：research 与 experience。格式：references 前 12 个单倍行距页（含图表），references
  与可选 appendix 另计，双盲，ACM `acmart.cls`。
- 评审流水线：early reject、rebuttal、以及 shepherd 主持的 one-shot revision（只 accept 或
  reject）；录用论文由 shepherd 陪跑到 camera-ready。

## 事实纪律

全包中三类陈述始终可区分：

1. **已核验的周期事实** —— 追溯到 source map 编号来源的日期、上限与规则（如 2 月 6 日截稿、
   references 前 12 页规则、one-shot revision 机制）。
2. **转述事实** —— 仅由二手渲染承载并如实标注（如经奖项页与作者机构确认的 Test-of-Time 选择）。
3. **待核实 条目** —— 显式标注并以开放形式陈述（如 2026 年 chairs、确切 notification 日期、
   2026 完整 artifact-badge 集合）。

任何在 skills 中把第 2、3 类当作第 1 类陈述的地方都是 bug，须对照官方现场页修正。

## 维护说明

- 上面每个日期都是 **2026 快照**。SIGCOMM 每届重发规则——涉及截稿敏感建议时先打开当年 CFP 与
  HotCRP 截稿页。
- **单截稿** 模型是本会场的核心约束；不要把 NSDI 或 MobiCom 的双截稿/滚动截稿推理搬进来。
- Chairs 每届轮换、2026 名单未能取回——命名任何人前先查 organization 页。
- 新范例必须通过 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  会场核验流程；网络经典中最有名的论文最常被误挂，且 CCR editorial note 不是正会论文。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English README: [`README.md`](README.md)。
