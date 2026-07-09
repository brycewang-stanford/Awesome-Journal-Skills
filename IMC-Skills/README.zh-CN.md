# ACM IMC Skills

面向 **IMC —— ACM Internet Measurement Conference（互联网测量会议）** 论文的 12 个 agent
skills。IMC 是 ACM SIGCOMM 主办、面向实证互联网与网络测量的旗舰会议。本包覆盖一次 IMC 投稿的
完整流程：判断项目是否 **测量优先**（属 IMC）还是应投 SIGCOMM、NSDI、CoNEXT 或 PAM；设计能经受
测量审稿人审视的 **观测点（vantage points）、数据集与方法**；跨越 IMC 的 **测量伦理与负责任披露**
门槛；准备 double-blind 的 `acmart` HotCRP 投稿及其 **artifact 可用性声明**；应对 **每年两个
截止日** 的周期与 **One-Shot-Revision** 返修轮；并在发布数据集/工具/平台时竞争 **Community
Contribution Award（社区贡献奖）**。

官方依据核验日期：**2026-07-09**。已核验 IMC 2026 的 call for papers、submission instructions 与
committees 页面；IMC 2025 的 call（篇幅）；IMC HotCRP 站点；SIGCOMM 的 IMC 事件页；以及 ACM
Digital Library 的 IMC proceedings。核验环境中直接抓取 `conferences.sigcomm.org` 与 `dl.acm.org`
返回 403，因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与 IMC HotCRP、ACM DL proceedings、
dblp 及 SIGCOMM 页面交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名冲突提醒：“IMC” 也指 Leeds 的 *International Medieval Congress*、*Indian Management
> Conclave*，以及一个 IEEE 服务计算的 “IMC” track —— 这些 **都不是** 本 IMC，本包事实均不来自
> 它们。

## IMC 与同类会议的区别

以下会议机制（按 2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 SIGCOMM、NSDI、安全会议
或 ML 会议转投作者最常犯的错误：

- **测量本身就是贡献。** IMC 更看重 **你对真实互联网学到了什么** 以及 **你如何测量** —— 观测点、
  数据集、ground truth 与方法 —— 而非新系统或新协议。系统出色而测量单薄的论文属 SIGCOMM/NSDI；
  技术朴素却揭示网络真实规律的论文才是 IMC 形态。
- **每年两个截止日，含 One-Shot-Revision 轮。** IMC 设两个投稿截止日（cycle 1 约 2025-11-20，
  cycle 2 约 2026-04-29）。首轮决定为 Accept、**One-Shot-Revision** 或 Reject。One-Shot-Revision
  是 **严格受限** 的返修：数条具体 action point、需一名审稿人 champion、由原审稿人在下一截止日
  复审 —— 不是开放式 major revision。
- **伦理是关卡，不是脚注。** 必须包含 **强制 Ethics 章节/附录**，缺失可被拒。涉及人类主体、用户
  数据或活体网络的测量按 **Belmont Report** 原则（尊重个人、行善、公正）评审，并有多数系统会议
  不严格执行的 **IRB** 审查与 **负责任披露** 要求。
- **数据集与 artifact 是一等公民。** 每篇投稿附 **artifact 可用性声明**（完整/部分/无）；录用论文
  被 **shepherd** 以兑现承诺的 artifact；**Community Contribution Award** 专门表彰发布的数据集、
  工具或平台（camera-ready 前公开）。
- **Replicability Track。** IMC 设专门 track（经 **Expression of Interest** 筛选），面向复现/再现
  既有测量结果的研究，优先 replicability。测量高度依赖不断变化的互联网，使这一 track 成为会议
  的标志性特征。
- **走 ACM 路线、double-blind、篇幅较宽。** IMC 使用 **ACM `acmart` 模板**、**double-blind** 评审，
  篇幅相对宽松（IMC 2025：正文含图 **≤13 页** + 无限参考文献/附录）。不要沿用 IEEE 双栏习惯。

## Skills

| Skill | 作用 |
| --- | --- |
| [`imc-topic-selection`](skills/imc-topic-selection/SKILL.md) | 在 IMC 与同类会议（SIGCOMM、NSDI、CoNEXT、PAM、USENIX Security、WWW、期刊）间选路，用测量优先测试、数据集/观测点视角与双截止日日历判断。 |
| [`imc-workflow`](skills/imc-workflow/SKILL.md) | 从你瞄准的那个截止日倒排年度计划，经注册、One-Shot-Revision 轮、shepherding 与 camera-ready。 |
| [`imc-writing-style`](skills/imc-writing-style/SKILL.md) | 构建测量论文骨架：首页给出发现、方法与观测点可审计、论证局限、尽早写 Ethics 章节。 |
| [`imc-related-work`](skills/imc-related-work/SKILL.md) | 覆盖测量文献 lane，对照既有数据集与观测点定位，保持 delta 与自引匿名。 |
| [`imc-experiments`](skills/imc-experiments/SKILL.md) | 让证据匹配论断：有代表性的观测点、ground truth、纵向稳定性、合乎伦理的主动测量、面向变化互联网的诚实混杂控制。 |
| [`imc-reproducibility`](skills/imc-reproducibility/SKILL.md) | 构建可用性证据：artifact 可用性声明、带 provenance 的数据集发布、无法原样重跑之测量的可复现性。 |
| [`imc-supplementary`](skills/imc-supplementary/SKILL.md) | 划分正文与附录/artifact，把决策关键证据与 Ethics 讨论留在评审正文内。 |
| [`imc-submission`](skills/imc-submission/SKILL.md) | HotCRP 终审：注册、`acmart` + BBL、double-blind 清扫、Ethics 章节、artifact 声明、周期选择、desk-reject 分诊。 |
| [`imc-review-process`](skills/imc-review-process/SKILL.md) | 建模流程 —— double-blind、多轮评审、Accept/One-Shot-Revision/Reject、champion 规则、early reject、shepherding —— 及作者杠杆点。 |
| [`imc-author-response`](skills/imc-author-response/SKILL.md) | 撰写 rebuttal，以及标志性的 One-Shot-Revision 再投：面向同一批审稿人处理受限的 action point 集合。 |
| [`imc-artifact-evaluation`](skills/imc-artifact-evaluation/SKILL.md) | 把录用论文的数据与代码转为发布、可用的 artifact —— 可用性 shepherding、DOI 存档、Community Contribution Award 资格。 |
| [`imc-camera-ready`](skills/imc-camera-ready/SKILL.md) | 去匿名、定稿 Ethics 与可用性声明、永久化数据集/代码链接，通过 IMC proceedings 的 ACM 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经网络核验的 IMC 论文，覆盖多种测量贡献形态，附自检问题与同类会议防混淆。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构审查测量研究的摘要与引言按 IMC 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 IMC 专用检查（可用性声明、数据集 provenance、伦理）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./IMC-Skills
claude plugin install imc-skills
```

也可直接使用文件：每个 `skills/imc-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 IMC 还是 SIGCOMM/NSDI？” → `imc-topic-selection`
- “按 IMC 投稿规则审我的稿” → `imc-submission`
- “拿到 One-Shot-Revision —— 规划再投” → `imc-author-response`
- “把数据集准备到发布与社区贡献奖标准” → `imc-artifact-evaluation`

## 目录结构

```text
IMC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── imc-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动手测量前** —— 先跑 `imc-topic-selection`；IMC 与 SIGCOMM/NSDI 重叠，靠测量优先测试与双截止日
   日历决定目标。浏览 exemplars 看有影响力的测量贡献长什么样。
2. **采集数据时** —— 让 `imc-experiments` 与 `imc-reproducibility` 贴着研究；观测点选择、伦理审批与
   数据集 provenance 无法事后补救。
3. **写作时** —— 用 `imc-writing-style` 对照 worked example 打磨正文，用 `imc-supplementary` 划分
   正文/附录，用 `imc-related-work` 做数据集感知的定位，并尽早写 Ethics 章节。
4. **截止周** —— 在该 cycle 注册截止日前完成注册，再用 `imc-submission` 对终稿 PDF、BBL 与 artifact
   声明逐项过审。
5. **投稿后** —— 用 `imc-review-process` 校准预期，用 `imc-author-response` 应对 rebuttal 与任何
   One-Shot-Revision，随后 `imc-artifact-evaluation` 与 `imc-camera-ready` —— 若结果不利，则用
   `imc-topic-selection` 的路由表改投。

## 2026 周期锚点事实（历史快照，非永久规则）

- IMC 2026：**德国卡尔斯鲁厄，2026 年 10 月 12-16 日。** General Chairs：Christian Wressnegger
  （KIT）与 Nurullah Demir（Stanford）；Program Chairs：Alan Mislove（Northeastern）与 Italo
  Cunha（UFMG）。
- **两个截止日：** cycle 1 投稿约 2025-11-20（注册约 2025-11-13）；cycle 2 投稿约 2026-04-29。
  One-Shot-Revision 在下一截止日再投，由同一批审稿人复审。
- 格式：**`acmart`、double-blind、上传 BBL**；full paper 正文含图 **≤13 页** + 无限参考文献/附录
  （IMC 2025 依据，2026 待确认）。**Ethics** 章节强制。
- 数据集/artifact：投稿时 **可用性声明**，录用后 **shepherding**，公开发布可竞争 **Community
  Contribution Award**；并设经 EoI 筛选的 **Replicability Track**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如双截止日、One-Shot-Revision、
   强制 Ethics 章节、artifact 声明、Community Contribution Award）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如 cycle 1 精确注册日与 camera-ready 日期）。
3. **核验期不可确定项** —— 明确标为 待核实（如 2026 精确正文页数、是否颁发正式 ACM 复现徽章、
   public-review 传统当前状态、录用率、完整 PC 名单）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是 **周期快照**。IMC 每届重定结构 —— 包括精确截止日、页数与 One-Shot-Revision
  机制 —— 每年先在当前 call 与 submission instructions 上核验。
- IMC 无常任 editor-in-chief；chairs 在 ACM SIGCOMM 下每届轮换。对人做连续性假设视为错误。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程 —— 熟悉的数据集或工具名并不能证明该论文发表于 IMC（大量测量工作发表在 SIGCOMM、
  NSDI 或 PAM）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
