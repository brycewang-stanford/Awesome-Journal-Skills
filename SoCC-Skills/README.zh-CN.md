# SoCC Skills

面向 **SoCC —— ACM Symposium on Cloud Computing（ACM 云计算研讨会）** 论文的 12 个 agent skills。
SoCC 是**唯一由 ACM SIGMOD 与 ACM SIGOPS 联合主办**的会议，这一联合主办身份正是本包的核心：SoCC
处于云计算研究的**系统与数据交叉点**，覆盖数据中心系统、存储、资源管理、serverless、大数据与
ML-systems 基础设施、边缘/雾计算，以及云经济学。本包覆盖一次 SoCC 投稿的完整流程：判断项目属于
SoCC 还是应投 OSDI/NSDI/EuroSys/ATC 或数据会议（SIGMOD/VLDB）；构建能同时满足两个主办社区的可测量
证据 —— 吞吐、**尾延迟**与**成本**；以 dual-anonymous 的 `acmart` 稿件通过 SoCC **每年两轮**评审；
应对 rebuttal；直到完成 ACM camera-ready 与可复现 artifact。

官方依据核验日期：**2026-07-09**。已核验 SoCC 2026（新加坡）与 SoCC 2025 research track 的 call 与
Important Dates、SoCC HotCRP 站点、ACM Artifact Review and Badging 政策，以及 ACM DL / dblp 的 SoCC
proceedings。核验环境中直接抓取 `acmsocc.org` 与 `dblp.org` 返回 403，因此通过搜索引擎对精确 URL 的
渲染阅读官方页面，并与 SoCC HotCRP deadlines 页、ACM Digital Library、dblp `conf/cloud` 流及截止日
镜像交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 命名冲突提醒：`ieee-socc.org` 是 **IEEE International System-on-Chip Conference**（硬件会议），
> **不是**本 SoCC。本包中的事实均不来自该会议。

## SoCC 与同类会议的区别

以下会议机制（按 2025/2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从纯系统旗舰、数据会议
或 ML 会议转投作者最常犯的错误：

- **SIGMOD 与 SIGOPS 联合主办。** SoCC 是唯一由数据与系统两大社区共同拥有的会议，因此论文会被**同时
  从两条轴**评审 —— 机制与工作负载、部署与测量。这正是 SoCC 区别于 OSDI/NSDI（系统旗舰）与
  SIGMOD/VLDB（数据旗舰）的身份。
- **每年两轮评审。** SoCC 设冬季轮与夏季轮，各有自己的摘要、投稿、rebuttal 与通知日期 —— 一年两次
  机会，但**第一轮被拒的论文当年不得再投第二轮**。
- **Dual-anonymous 评审 + rebuttal。** 审稿人与作者互相匿名；每轮设 author-response 窗口。**没有**
  期刊式 Major-Revision 轮 —— rebuttal 是 accept/reject 裁决前唯一的书面机会。
- **走 ACM `acmart` 路线。** SoCC 使用 ACM Primary Article Template，`sigconf`，9pt，正文含图
  **12 页**（short paper 6 页）+ **参考文献不限页** —— 不是 OSDI/NSDI/ATC 的 USENIX 模板。
- **系统构建与测量/经验论文并重。** clean-slate 系统、生产 trace 研究、benchmark、部署经验论文与
  云经济学工作在此都是原生的 —— 这一广度直接来自联合主办。
- **尾延迟与成本是一等公民。** 只报均值、或断言未经测量的成本节省，会被读作未经压力测试；p95/p99 与
  具体成本模型才是通货。

## Skills

| Skill | 作用 |
| --- | --- |
| [`socc-topic-selection`](skills/socc-topic-selection/SKILL.md) | 用系统-数据交叉点测试、贡献形态与 model-swap / re-label 测试，在 SoCC 与同类会议（OSDI、NSDI、EuroSys、ATC、SOSP、SIGMOD/VLDB）间选路。 |
| [`socc-workflow`](skills/socc-workflow/SKILL.md) | 从某一轮摘要截止日倒排两轮年度计划，经投稿、rebuttal、通知、ACM camera-ready 与新加坡报告。 |
| [`socc-writing-style`](skills/socc-writing-style/SKILL.md) | 构建云系统骨架：首页给出运营者问题、系统+数据交叉的贡献、尾延迟与成本为一等公民、acmart 篇幅纪律。 |
| [`socc-related-work`](skills/socc-related-work/SKILL.md) | 同时覆盖系统与数据两条文献 lane，写 delta-first 定位，并保持自引匿名。 |
| [`socc-experiments`](skills/socc-experiments/SKILL.md) | 让可测量证据匹配论断形态：真实/近真实部署、生产工作负载、尾延迟与成本、公平且调优的 baseline、规模与多租户。 |
| [`socc-reproducibility`](skills/socc-reproducibility/SKILL.md) | 构建可复现故事：testbed 与工作负载描述、释放代码与 trace、provenance 钉死、复现尾延迟与成本。 |
| [`socc-supplementary`](skills/socc-supplementary/SKILL.md) | 按决策重要性划分正文与 artifact —— 决定录用的证据（尾延迟、成本、baseline）不得置于正文之外。 |
| [`socc-submission`](skills/socc-submission/SKILL.md) | HotCRP 终审：两轮摘要+投稿截止日、acmart 篇幅、dual-anonymous 清扫、可复现姿态、desk-reject 分诊。 |
| [`socc-review-process`](skills/socc-review-process/SKILL.md) | 建模流程 —— dual anonymity、两轮、SIGMOD+SIGOPS 联合审稿群、rebuttal、accept/reject —— 及作者杠杆点。 |
| [`socc-author-response`](skills/socc-author-response/SKILL.md) | 撰写唯一一轮 rebuttal：同时回应系统与数据审稿人并补上尾延迟/成本数字，且保持匿名。 |
| [`socc-artifact-evaluation`](skills/socc-artifact-evaluation/SKILL.md) | 在当届提供评审时，为 ACM 徽章（Available / Functional / Reusable / Reproduced）打包，在规模下复现尾延迟与成本。 |
| [`socc-camera-ready`](skills/socc-camera-ready/SKILL.md) | 系统去匿名、补全 ACM 元数据、把释放的代码与 trace 永久化、通过 ACM 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2025/2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 SoCC 论文，覆盖五种贡献形态（benchmark、trace 研究、存储 QoS、资源管理、serverless），附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构 serverless 自动扩缩研究的摘要与引言按 SoCC 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享可复现工具，并给出通用套件无法完成的 SoCC 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./SoCC-Skills
claude plugin install socc-skills
```

也可直接使用文件：每个 `skills/socc-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 SoCC 还是 OSDI/NSDI/SIGMOD？” → `socc-topic-selection`
- “按 SoCC research-track 规则审我的稿” → `socc-submission`
- “收到审稿意见 —— 帮我写 SoCC rebuttal” → `socc-author-response`
- “把 artifact 准备到 ACM 徽章标准” → `socc-artifact-evaluation`

## 目录结构

```text
SoCC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── socc-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `socc-topic-selection`；SoCC 与 OSDI/NSDI/EuroSys 及 SIGMOD/VLDB 均有重叠，
   按系统-数据交叉点选择很重要。浏览 exemplars 看 SoCC 贡献长什么样。
2. **构建证据时** —— 让 `socc-experiments` 与 `socc-reproducibility` 贴着系统；尾延迟/成本测量与
   钉死的 provenance 无法事后补救。
3. **写作时** —— 用 `socc-writing-style` 对照 worked example 打磨正文，用 `socc-supplementary`
   划分正文/artifact，用 `socc-related-work` 在两条 lane 上做 delta-first 定位。
4. **投稿轮周** —— 选你能做强的那一轮，在摘要截止日前完成注册，再用 `socc-submission` 对终稿 PDF
   与 artifact 逐项过审。
5. **投稿后** —— 用 `socc-review-process` 校准预期，用 `socc-author-response` 撰写 rebuttal，随后
   `socc-artifact-evaluation` 与 `socc-camera-ready` —— 若结果不利，则用 `socc-topic-selection`
   的路由表改投（记住第一轮被拒当年不得再投第二轮）。

## 2025/2026 周期锚点事实（历史快照，非永久规则）

- SoCC 2026 为**第 17 届**：**新加坡，2026 年 11 月 18-20 日**。第一轮：摘要 2 月 6 日，投稿 2 月
  13 日，response 4 月 12-14 日，通知 4 月 29 日。第二轮：摘要 7 月 7 日，投稿 7 月 14 日（AoE），
  response 9 月 10-12 日，通知 9 月 26 日。第一轮被拒当年不得再投第二轮。
- 格式：**ACM `acmart` sigconf，9pt，dual-anonymous**；full paper 正文含图 **12 页** + 参考文献
  不限页，short paper **6 页** + 参考文献不限页。HotCRP：`socc26.hotcrp.com`。
- 主办：**唯一**由 **ACM SIGMOD 与 SIGOPS** 联合主办的会议。评审：**dual-anonymous** + 每轮
  **rebuttal**；决定 **accept / reject**（无 Major Revision）。PC Co-Chairs 转述为 Eric Lo 与
  Ivan Beschastnikh（以官方页面为准）。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2025/2026 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如两轮日历、12 页
   acmart 篇幅、SIGMOD+SIGOPS 联合主办）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如 SoCC 2026 PC Co-Chair 姓名与完整组委名单）。
3. **核验期不可确定项** —— 明确标为 待核实（如某届 SoCC 是否设专门 artifact-evaluation track、
   General Chair 名单、任何 AI 使用披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。SoCC 每届重定结构 —— 包括轮次日期与跨轮再投规则 —— 每年先核验
  cadence。
- SoCC 无常任 editor-in-chief；chairs 每届在 SIGMOD 与 SIGOPS 下轮换。出版物是 ACM DL 会议
  proceedings，而非期刊。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的系统名
  并不能证明该论文发表于 SoCC（Mesos、Borg、Spark、TensorFlow 都是同类会议论文）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
