# DAC 技能包

面向 **DAC——ACM/IEEE 设计自动化会议（Design Automation Conference，"The Chips to Systems
Conference"）** 投稿的十二个智能体技能。DAC 由 ACM 与 IEEE 主办、由 **ACM SIGDA** 与 **IEEE CEDA**
支持，是**电子设计自动化（EDA）**与芯片／系统设计领域的旗舰会议。本技能包覆盖 DAC 投稿的完整链条：
判断选题是否契合 DAC，以及应投**双盲、进入存档的 Research Manuscript（研究论文）赛道**还是面向工业界的
**Engineering Track（工程赛道）**；构建能经受 EDA 审稿人审视的 QoR 证据；在紧凑的 **6+1 页**双栏篇幅内（DAC 2027 用 IEEE
模板）完成两阶段、双盲的 Softconf 投稿；应对**单轮、由技术程序委员会（TPC）主导、接收／拒稿**的评审；
并交付收录于 IEEE Xplore 与 ACM 数字图书馆（ACM Digital Library）的最终版。

**官方依据复核于 2026-11-24**：`dac.com/2027` 上的 DAC 2027（第 64 届）主页、征稿启事、Research
Manuscript Submissions 页（格式、规则、AI 政策、时间表、FAQ）、Engineering Track 页与委员会页，以及
`softconf.com/dac27/research` 投稿系统，均为直接抓取。2026-07-09 的初版通过搜索引擎快照阅读 DAC 2026
页面，并与 ACM DL 的 DAC 会议录及 dblp 交叉核对；完整的溯源记录（含所有仍标注 **待核实** 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 同名警示：**ASP-DAC**（亚洲及南太平洋设计自动化会议）与 **DATE**（欧洲设计、自动化与测试会议）是
> *不同的* EDA 会议，各有自己的征稿——本包中任何事实均不源自它们。此外，电路论文里的 "DAC" 常指
> *数模转换器（digital-to-analog converter）*，那是一个在范围内的研究主题，而非本会议。

## DAC 与同类会议的不同之处

以下经 DAC 2027 周期核实的机制，驱动了各技能中的大部分建议，也是来自体系结构会议、机器学习会议或软件工程会议的
作者最常犯错之处：

- **两个同行评审论文赛道，评审模式不同。** DAC 同时设有双盲、进入存档的 **Research Manuscript** 赛道，
  以及面向工业界的 **Engineering Track**（后端／前端设计、IP、系统与软件），后者由独立的 Engineering Track
  委员会负责，不需要论文、也不出版。
  选对赛道是 DAC 特有、杠杆最高的决定——这在 ISCA/MICRO/HPCA 并不存在。
- **紧凑的 6+1 页篇幅。** 正文**不含参考文献不超过 6 页，另加 1 页仅放参考文献**，双栏、9–10 pt，
  DAC 2027 采用 **IEEE 模板**（DAC 2026 用 ACM 模板——模板一直与当届版权方一致）。第 7 页若出现任何非参考文献内容即构成**桌拒**理由。这比体系结构与软件工程会议的篇幅小得多。
- **Softconf 上的两阶段投稿。** **摘要阶段**（题目、约 100 词摘要、全部作者、TPC 利益冲突）比**论文阶段**早一周；错过摘要阶段
  就没有上传 PDF 的名额。
- **单轮、TPC 主导、接收／拒稿的评审。** 没有期刊式的 Major Revision，且 DAC 研究评审**没有作者
  rebuttal**（DAC 2027 时间表中没有）——杠杆几乎全部前置在基线与基准的选择上。
- **证据是 EDA 基准上的 QoR。** 审稿人看重在公认基准（ISPD、EPFL、ISCAS/ITC、TAU、CircuitNet）上、
  相对最强且经调优基线所测得的 **PPA（功耗／性能／面积）**、线长、时序裕量、覆盖率与运行时——而非某个代理
  指标上的准确率。
- **没有制品评审徽章赛道。** 与 FSE/ICSE 或 MICRO/ISCA 不同，DAC **不设**正式的制品评审／徽章赛道
  （DAC 2027 征稿中没有）；制品带来的是审稿可信度与社区复用，而非徽章。
- **IEEE Xplore＋ACM DL 收录，每年单次截稿。** 被接收的 Research Manuscript 收录于 **IEEE Xplore 与
  ACM 数字图书馆**（DAC 2027 签署 IEEE 版权表），前提是完成全额 Speaker 注册并在海报环节现场报告；
  每年仅有一次存档截稿——在 11 月中旬，会议在次年 7 月举行。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`dac-topic-selection`](skills/dac-topic-selection/SKILL.md) | 在 DAC 与同类会议（ICCAD、DATE、ASP-DAC、ISCA/MICRO/HPCA）之间、并在 DAC 内部于 Research 与 Engineering 赛道之间路由，依据贡献形态、QoR-影响与 model-swap 测试，以及 11 月日历。 |
| [`dac-workflow`](skills/dac-workflow/SKILL.md) | 从 11 月论文截稿倒推整年：两阶段 Softconf 投稿、冬季评审、3 月通知、3 月底会议录稿件、4 月注册。 |
| [`dac-writing-style`](skills/dac-writing-style/SKILL.md) | 打造以 QoR 领起的首页，将贡献表述为可度量的增量，并在六页双栏内容纳完整论证，自引用一律用第三人称。 |
| [`dac-related-work`](skills/dac-related-work/SKILL.md) | 覆盖 EDA 文献脉络（DAC/ICCAD/DATE/ASP-DAC/TCAD/TODAES），以"增量优先"定位，并点名要超越的最强基线。 |
| [`dac-experiments`](skills/dac-experiments/SKILL.md) | 让证据匹配 QoR 论点：标准基准套件、公平且经调优的基线、完整 PPA＋运行时、消融，以及防污染的 ML-for-EDA 评测。 |
| [`dac-reproducibility`](skills/dac-reproducibility/SKILL.md) | 固定基准版本，披露流程／PDK／工具版本，报告随机种子与方差，并规划"先匿名后 DOI 存档"的仓库路径。 |
| [`dac-supplementary`](skills/dac-supplementary/SKILL.md) | 按"是否决定录用"切分内容——决定录用的一切都放进六页正文；第 7 页仅放参考文献。 |
| [`dac-submission`](skills/dac-submission/SKILL.md) | Softconf 终审：两阶段摘要＋论文截稿、6+1 IEEE 模板篇幅、双盲清扫、TPC 利益冲突申报、AI 内容披露与桌拒排查。 |
| [`dac-review-process`](skills/dac-review-process/SKILL.md) | 建模评审流程——双盲、TPC 主导、新颖性＋QoR、单轮接收／拒稿、约 20–25% 录取率——并指出（前置的）作者杠杆所在。 |
| [`dac-author-response`](skills/dac-author-response/SKILL.md) | 依 DAC 实况处理评审：DAC 2027 无回复期，因此做有的放矢的"修改并改投"ICCAD/DATE/ASP-DAC，或撰写期刊回复信（若将来某届设回复期，再写简明 rebuttal）。 |
| [`dac-artifact-evaluation`](skills/dac-artifact-evaluation/SKILL.md) | 在 DAC 无 ACM 徽章赛道的前提下，为审稿可信度与社区复用（DOI 存档、开源许可）打包工具／基准／流程。 |
| [`dac-camera-ready`](skills/dac-camera-ready/SKILL.md) | 系统性去匿名，完成 IEEE 版权表，在 3 月底会议录截稿前通过元数据检查，并满足 IEEE Xplore 与 ACM DL 收录所需的注册／报告条件。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十三个来源（含 URL 与访问日期）；经核实的 DAC 2027 事实（DAC 2026 作为历史）；访问方法说明；待核实清单；机器可读规则块。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方 DAC/IEEE-CEDA/ACM-DL/Softconf 界面、EDA 基准套件与开源流程，以及作者侧核验步骤。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 四篇经存档核实的 DAC 论文（Chaff、ABC 重写、逻辑混淆安全性、DREAMPlace），横跨四个 EDA 子领域，附自查问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的"拥塞感知布线"研究，其摘要与引言按 DAC 的 QoR 弧线重写，前后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 对接共享复现工具，并补充通用工具无法完成的 DAC 专属 QoR／流程／溯源检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是带有自身 marketplace 清单的自包含插件）：

```bash
# 在仓库克隆中执行
claude plugin marketplace add ./DAC-Skills
claude plugin install dac-skills
```

或直接使用文件：每个 `skills/dac-*/SKILL.md` 都是独立的指令文件，其 frontmatter 的 `description`
会告诉智能体何时触发。常见调用：

- "这是 DAC 论文吗？投 Research 还是 Engineering 赛道？" → `dac-topic-selection`
- "按 DAC 研究论文规则审查我的稿件" → `dac-submission`
- "我的基线／基准评测在 DAC 够强吗？" → `dac-experiments`
- "被拒且无 rebuttal——改投 ICCAD/DATE" → `dac-author-response`

## 目录结构

```text
DAC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个技能）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── dac-<topic>/SKILL.md  # 12 个技能，各占一个目录
└── resources/
    ├── README.md             # 资源指南与建议路径
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 对接共享工具
```

## 建议用法

1. **动笔前** —— 先跑 `dac-topic-selection`；DAC-vs-同类会议 与 Research-vs-Engineering 这两个决定
   支配后续一切。浏览范例库，看看具十年影响力的 DAC 贡献长什么样。
2. **构建证据时** —— 让 `dac-experiments` 与 `dac-reproducibility` 常伴左右；基线、基准套件与溯源在
   设计阶段确定，一旦过了截稿便无法补救（且没有 rebuttal 可以挽回）。
3. **写作时** —— 用 `dac-writing-style` 对照范例打磨六页正文，用 `dac-supplementary` 切分正文／仓库，
   用 `dac-related-work` 做增量优先的定位。
4. **截稿周** —— 在摘要阶段截止前完成摘要提交，随后用 `dac-submission` 对最终匿名 PDF 从头到尾核验。
5. **决定之后** —— 用 `dac-review-process` 校准预期，用 `dac-author-response` 处理
   "修改并改投"，再进入 `dac-camera-ready`——若结果相反，则回到 `dac-topic-selection` 的路由表。

## DAC 2027 锚定事实（周期快照，非永久规则）

- DAC 2027 是**第 64 届**设计自动化会议：**加州圣何塞**（San Jose Convention Center），
  **2027 年 7 月 11–14 日**。研究论文摘要截止 **2026 年 11 月 11 日**、论文截止 **11 月 18 日**（美国太平洋
  时间下午 5 点；均已截止）；录用编号公布 2027 年 2 月 22 日；接收／拒稿 3 月 8 日；会议录稿件 3 月 31 日；
  作者注册 4 月 10 日。Engineering Track 截稿 2027 年 1 月 11 日。
- 格式：**正文 6 页 + 1 页仅参考文献**，**双栏**，9–10 pt，单一 PDF，**IEEE 模板**；签署 IEEE 版权表；
  收录于 **IEEE Xplore 与 ACM 数字图书馆**。
- 评审：**双盲、TPC 主导、单轮接收／拒稿**，未录用者可能受邀参加 WIP 海报；**无 rebuttal**、**无制品
  徽章赛道**；录取率 **20–25%**。若使用 LLM 生成内容，须设 "Content Generated by AI" 一节披露。
- 主席：大会主席 David Pan；TPC 主席 Ambar Sarkar；TPC 联合主席 Jiang Hu、Rajiv Joshi。
- 由 **ACM 与 IEEE** 主办，**ACM SIGDA** 与 **IEEE CEDA** 支持。
- 历史：DAC 2026（第 63 届）于 2026 年 7 月 26–29 日在长滩举行，使用 ACM 模板、ACM 为版权方。

## 事实纪律

本包区分三类陈述，各技能的写法都力求让它们可辨：

1. **已核实的 DAC 2027 事实** —— 带有日期／篇幅，并可溯源到源图中的编号来源（如 6+1 篇幅、IEEE 模板、
   双盲评审、11 月论文截稿）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如经搜索引擎快照读到的 DAC 2026 历史信息）。
3. **核对时无法确证的条目** —— 显式标注 **待核实**（如 DAC 2027 完整 TPC 名单、最终版 IEEE 版权声明
   措辞、2027 年是否另发 LBR 征稿）。

若任何陈述以第 1 类口吻呈现第 2、3 类内容，应视为缺陷，并对照官方最新页面修正。

## 维护说明

- 上述每个日期与篇幅都是**周期快照**。DAC 每届都会重新决定其结构——包括截稿、是否设回复期、主题领域清单
  ——因此每年动手前先核验当届征稿启事。
- DAC 无常设主编；其轮值对应物是各届的大会主席、技术程序主席与赛道主席，隶属 ACM SIGDA 与 IEEE CEDA。
- 新增范例论文时，请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  核验流程——熟悉的工具名并不能证明它出自 DAC（ABC 的工具论文在 CAV；EPIC 在 DATE；IC 指纹在 S&P）。

## 许可证

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
