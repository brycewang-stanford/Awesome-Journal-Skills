# IEEE PerCom Skills

面向 **IEEE PerCom —— IEEE International Conference on Pervasive Computing and Communications**
论文的 12 个 agent skills。PerCom 是 IEEE 在**以人为中心的普适计算**方向的旗舰会议：活动识别、
上下文建模、移动与可穿戴感知、智能环境。本包覆盖一次 PerCom 投稿的完整流程：判断项目属于 PerCom
还是应投 ACM UbiComp/IMWUT、MobiCom、SenSys 或 IPSN；构建能经受普适计算审稿人审视的人体被试感知
证据；准备 **double-blind 的 HotCRP** 投稿及其 **IEEEtran 9+1** 篇幅；应对**单轮 rebuttal** 评审
及其 early-rejection 阶段；直到完成 IEEE Xplore camera-ready 与可复现的感知数据集。

官方依据核验日期：**2026-07-09**。已核验 PerCom 2027 的 Call for Papers 与 Important Dates 页面、
PerCom HotCRP 站点、Work-in-Progress 征稿、Mark Weiser Best Paper 与 Test of Time 奖项页面、
IEEE Xplore 及 dblp。核验环境中直接抓取 `percom.org` 返回 403，因此通过搜索引擎对精确 URL 的渲染
阅读官方页面，并与 PerCom HotCRP、IEEE Xplore / IEEE Computer Society Digital Library 及 dblp
交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 时间提示：截至 2026-07-09，**PerCom 2026（意大利 Pisa，2026-03-16 至 20）已结束**，因此 live
> 的下一个 research 目标是 **PerCom 2027（印度 Goa，2027-03-08 至 12）**。所有投稿周期建议均锚定
> PerCom 2027 的 call。

## PerCom 与相邻会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 ACM UbiComp/IMWUT、
网络化传感器会议（SenSys/IPSN）或 ML 会议转投作者最常犯的错误：

- **它是 IEEE，且以人为中心。** PerCom 是 IEEE Computer Society 的普适计算旗舰；重心是**人** ——
  活动识别、上下文感知、可穿戴、智能空间 —— 而非 SenSys/IPSN 那种纯网络化传感器系统。论文发表在
  **IEEE Xplore**，用 **IEEE 双栏 conference 模板**，而非 ACM `acmart`。
- **每年单一截止日，进入带 rebuttal 的单一评审轮。** PerCom 2027 注册 2026-09-04 截止，投稿
  2026-09-11（AoE）。没有期刊式 revise-and-resubmit，周期内也没有第二个截止日。
- **有界 rebuttal，前置 early-rejection。** 初审后，无任何正面评价的论文被 **early-reject**（约
  2026-11-20 通知）以便作者尽早改投；至少有一个 “weak accept” 的论文被**邀请提交 rebuttal**
  （约 2026-11-26），回答审稿人的明确问题。call 声明**不期望补充新实验** —— 投稿时证据必须已经到位。
- **Double-blind 评审。** 匿名 PDF、数据集/仓库链接、testbed/实验室名称，并以**第三人称**引用
  自己的既往工作，而非省略。
- **篇幅很紧。** **9 页**正文（10pt 双栏 `compsocconf` IEEEtran）**+ 1 页**仅参考文献 —— 只有
  单栏 ACM 篇幅的一小部分。靠编辑压缩，而非改模板，来塞下内容。
- **人体被试、跨被试的证据文化。** 真实被试、IRB/伦理处理、**leave-one-subject-out** 评估、
  以及在类别不平衡下用 **F1 而非 pooled accuracy**，是审稿群体即便无明文也会执行的社区规范。
- **独特的奖项文化。** **Mark Weiser Best Paper Award**（Elsevier 赞助）与较新的 **Test of Time
  Award**（PerCom 2026 首设）标记着会议的记忆；活跃的 **PerCom Workshops** 星系（WristSense、
  PerVehicle、CoMoRea、DIGITA……）与 **WiP**、**demo**、**industry** track 环绕主会。

## Skills

| Skill | 作用 |
| --- | --- |
| [`percom-topic-selection`](skills/percom-topic-selection/SKILL.md) | 在 PerCom 与相邻会议（ACM UbiComp/IMWUT、MobiCom、SenSys、IPSN、MobiSys）之间选路，用贡献形态、以人为中心测试与 model-swap 测试判断。 |
| [`percom-workflow`](skills/percom-workflow/SKILL.md) | 从 9 月截止日倒排单周期年度计划，经注册、early-rejection 关卡、rebuttal、IEEE Xplore camera-ready 与线下报告。 |
| [`percom-writing-style`](skills/percom-writing-style/SKILL.md) | 构建普适计算骨架：首页给出 ubicomp 贡献、跨被试论断、会论证的 limitations、9 页篇幅纪律。 |
| [`percom-related-work`](skills/percom-related-work/SKILL.md) | 覆盖 ubicomp/移动/感知 lane，写 delta-first 定位，并保持自引 double-blind。 |
| [`percom-experiments`](skills/percom-experiments/SKILL.md) | 让证据匹配论断形态：真实人体被试、leave-one-subject-out 评估、不平衡类别的 F1、部署真实性、公平 baseline。 |
| [`percom-reproducibility`](skills/percom-reproducibility/SKILL.md) | 构建人体感知的 open-data 证据：去标识数据集、IRB/伦理处理、感知 provenance、跨被试可复现。 |
| [`percom-supplementary`](skills/percom-supplementary/SKILL.md) | 按决策重要性划分 9 页正文与数据集/artifact —— 决定录用的证据不得置于正文之外。 |
| [`percom-submission`](skills/percom-submission/SKILL.md) | HotCRP 终审：注册+投稿两步、IEEEtran 9+1 篇幅、double-blind 清扫、open-data 计划、desk-reject 分诊。 |
| [`percom-review-process`](skills/percom-review-process/SKILL.md) | 建模流程 —— double-blind、三名 TPC 审稿人、early-rejection 关卡、有界单轮 rebuttal —— 及作者杠杆点。 |
| [`percom-author-response`](skills/percom-author-response/SKILL.md) | 撰写有界 rebuttal：回答审稿人明确问题、纠正误读、不添加无支撑的新论断，并保持 double-blind。 |
| [`percom-artifact-evaluation`](skills/percom-artifact-evaluation/SKILL.md) | 打包可复用的感知 artifact 与数据集用于复现/徽章（IEEE DataPort / Zenodo，若提供则 IEEE Open Research Objects —— 逐年核验）。 |
| [`percom-camera-ready`](skills/percom-camera-ready/SKILL.md) | 去匿名、补全 IEEE Xplore 元数据（PDF eXpress、版权、ORCID）、把数据集链接永久化、通过 IEEE 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 PerCom 论文，覆盖五种贡献形态（含 Mark Weiser Best Paper 与 Test of Time），附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构的进食识别研究摘要与引言按 PerCom 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享复现工具，并给出通用套件无法完成的 PerCom 人体被试与跨被试检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./PerCom-Skills
claude plugin install percom-skills
```

也可直接使用文件：每个 `skills/percom-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 PerCom 还是 UbiComp/IMWUT 或 SenSys？” → `percom-topic-selection`
- “按 PerCom research-track 规则审我的稿” → `percom-submission`
- “我们被邀请 rebuttal —— 规划回复” → `percom-author-response`
- “把这个感知数据集准备到可发布” → `percom-reproducibility`

## 目录结构

```text
PerCom-Skills/
├── .claude-plugin/             # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                   # 英文说明
├── README.zh-CN.md             # 本文件
├── LICENSE                     # MIT
├── assets/cover.svg            # 封面
├── skills/
│   └── percom-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md          # 指向共享复现工具
```

## 建议用法

1. **动笔前** —— 先跑 `percom-topic-selection`；PerCom 与 UbiComp/IMWUT 主题高度重叠但模型与日历
   不同，刻意选择很重要。浏览 exemplars 看有影响力的 PerCom 贡献长什么样。
2. **构建证据时** —— 让 `percom-experiments` 与 `percom-reproducibility` 贴着研究；设计期定下的
   跨被试划分与采集期处理的 IRB/consent 无法事后补救。
3. **写作时** —— 用 `percom-writing-style` 对照 worked example 打磨正文，用 `percom-supplementary`
   划分正文/数据集，用 `percom-related-work` 做 delta-first 定位。
4. **截止周** —— 先在较早的注册截止日前完成注册，再用 `percom-submission` 对终稿 PDF 与数据集
   链接逐项过审。
5. **投稿后** —— 用 `percom-review-process` 校准预期，若通过 early-rejection 关卡则用
   `percom-author-response` 应对 rebuttal，随后 `percom-artifact-evaluation` 与
   `percom-camera-ready` —— 若结果不利，则用 `percom-topic-selection` 的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- PerCom 2026 为**第 24 届**：意大利 Pisa，**2026-03-16 至 20**；**Test of Time Award** 在此首设，
  表彰 “LANDMARC”（PerCom 2003）。
- PerCom 2027 为**第 25 届**：印度 Goa，**2027-03-08 至 12**；research 注册 **2026-09-04**，投稿
  **2026-09-11**（AoE）；early-reject / rebuttal 邀请 **2026-11-20**，rebuttal **2026-11-26**，
  通知 **2026-12-18**；篇幅 **9 页 + 1** 页参考文献；每篇 **3** 名 TPC 审稿人。这是 2026-07-09 时
  的下一个 live research 目标。
- 出版：**IEEE Xplore**。评审：**double-blind**，单轮带**有界 rebuttal** 与 **early-rejection**
  关卡。模板：**IEEEtran**（`compsocconf`，10pt，双栏）。门户：**HotCRP**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 9+1 IEEEtran
   篇幅、double-blind rebuttal 模型、2026-09-11 截止）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如完整组委名单，或约 14-15% 的历史录用率）。
3. **核验期不可确定项** —— 明确标为 待核实（如 PerCom 2027 TPC Chair 名单、camera-ready 日期、
   是否有正式复现徽章 track、任何 AI 披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。PerCom 每届重定结构 —— 包括 rebuttal 窗口与任何复现 track ——
  每年先核验 cadence。
- PerCom 无常任 editor-in-chief、无 APC；chairs 每届轮换。成本模型是 IEEE 注册，至少一位作者线下报告。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的系统名
  并不能证明该论文发表于 PerCom（大量 ubicomp 工作在 UbiComp/IMWUT、MobiCom、SenSys 或 IPSN）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
