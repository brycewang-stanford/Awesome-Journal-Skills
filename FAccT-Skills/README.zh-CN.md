# ACM FAccT Skills

面向 **ACM FAccT —— Conference on Fairness, Accountability, and Transparency（公平、问责与透明性
会议）** 论文的 12 个 agent skills。FAccT 是**跨学科**负责任 AI 的旗舰会议。与纯 ML 会议
（NeurIPS/ICML）或 HCI 会议（CHI）不同，FAccT 独特地要求**公平、问责或透明性本身即为一等贡献**，
并汇聚一个真正混合的审稿群体 —— 计算机科学家、法学学者、社会科学家、人文学者与政策研究者。本包
覆盖一次 FAccT 投稿的完整流程：判断项目属于 FAccT 还是应投 ML/HCI/法律会议；构建能同时满足混合
评审组的证据（严谨的 CS 审计**与**批判性或定性研究都在范围内）；准备 mutually-anonymous 的
OpenReview 投稿及其必需的 endmatter 声明；应对 **Accept / Revise（major 或 minor）/ Reject** 返修再投周期；
直到完成 ACM `acmart` 存档 camera-ready 及其问责文档。

官方依据于 **2026-11-24 重新核验**，对应 **FAccT 2027**（第 10 届，**葡萄牙波尔图，2027 年
6 月 21-24 日**）：直接读取了 FAccT 2027 的 Call for Papers、Author Guide 与 Reviewer Guide，
facctconference.org 首页，FAccT Blog 关于 2027 时间线与流程变化的文章，以及 OpenReview FAccT 2027
group。FAccT 2026 页面（CFP、committees、CRAFT 与 Doctoral Colloquium call）作为历史一并复读；ACM DL
仍返回 403，故 FAccT '26 proceedings 的 DOI 经 Crossref 确认。完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 沿革提醒：本会议 2018-2020 年名为 **FAT\***（FAT\* 2018 收录于 **PMLR vol 81**；FAT\* 2019 为
> 首个 ACM DL proceedings），自 2021 年起更名为 **FAccT**。dblp 键仍为 `db/conf/fat`。不要将 FAccT
> 与会前 **FAT/ML workshop** 或姊妹会议 **AIES** 混淆。

## FAccT 与同类会议的区别

以下会议机制（按 2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从纯 ML、HCI 或法律背景
转投作者最常犯的错误：

- **公平/问责/透明性是贡献本身，而非一个段落。** 若删去 equity 框架后仍剩下一篇可发表的核心，那它
  应投该核心所属的 ML/HCI/法律会议。FAccT 要求 harm、问责或透明性问题**就是**这篇论文。
- **审稿群体是跨学科的。** 论文按你在注册时选择的 **focus areas** 匹配审稿人与 **Area Chairs**，
  且通常被跨学科阅读 —— 每个 lane 都要求**其领域**的严谨（审计要 disaggregation 与公平 baseline；
  定性研究要编码与 reflexivity；法律论文要法理精确）。
- **Accept / Revise（major 或 minor）/ Reject，且无独立 rebuttal。** **Revise**（2026 引入）是真正的
  revise-and-resubmit：按 Area Chair 归纳并排序的关切修改，**修改稿与 rebuttal 一并提交**，再被复审。
  FAccT 2027 取消了 2026 年首轮决定前的短 rebuttal，并新增 **Senior Area Chairs** 做校准。它不是软性拒稿。
- **OpenReview 与秋季截止。** 投稿与评审自 2026 起在 OpenReview 进行，并设有硬性的**摘要注册
  gate**（含 focus-area 选择），在论文截止前一周。自 2027 届起截止日提前到前一年 10 月底 / 11 月初。
- **所有作者都须报名审稿。** FAccT 2027 要求每篇论文的全部作者填写审稿人报名表；不履行可能导致
  （desk）reject。
- **Mutual anonymity，且 endmatter 规则特殊。** 作者与审稿人互相匿名。**Positionality**、
  Acknowledgements、Author Contributions 与 Competing Interests 声明在匿名投稿中**不得包含**，仅
  在录用后添加。
- **必需的 Generative AI Usage Statement。** 每篇投稿须披露是否及如何使用生成式 AI（未使用也要
  声明）。FAccT 2026 禁止由 LLM 生成正文；FAccT 2027 改为遵循 ACM 作者政策：披露（工具、模型版本、
  任务、人工核验）后可用 AI 生成内容，未披露即可 desk reject。投稿时应附 **Ethical Considerations**
  声明（含 adverse impacts）；endmatter 置于额外一页，不计入篇幅。
- **ACM `acmart`、存档，且现已 100% Open Access。** 论文发表于 ACM DL proceedings（存在
  **non-archival** 选项）；自 2026-01-01 起所有 ACM proceedings 经 ACM Open 或 APC 实现开放获取。
- **文档与影响的文化。** Datasheets、model cards、data statements 与 impact assessments 是 FAccT
  原生的 “artifact” —— 并无 SIGSOFT 式的 badging track。
- **同址 CRAFT 项目。** Critiquing and Rethinking Accountability, Fairness, and Transparency 在
  论文 track 之外运行参与式与 world-building 场次（workshop、fishbowl、unconference、艺术介入等）。

## Skills

| Skill | 作用 |
| --- | --- |
| [`facct-topic-selection`](skills/facct-topic-selection/SKILL.md) | 在 FAccT 与同类会议（NeurIPS/ICML、CHI/CSCW、AIES、法律/政策）之间选路，用 delete-the-equity 与 mixed-reviewer 测试，并区分 paper 与 CRAFT。 |
| [`facct-workflow`](skills/facct-workflow/SKILL.md) | 从摘要注册 gate 倒排单截止周期，经 OpenReview、Revise 轮（修改稿 + rebuttal 合并提交）、camera-ready 与报告。 |
| [`facct-writing-style`](skills/facct-writing-style/SKILL.md) | 让 FAccT 贡献对混合评审组清晰可读：首页点明谁受影响、论断限定到人群、harm 会论证而非罗列。 |
| [`facct-related-work`](skills/facct-related-work/SKILL.md) | 覆盖学科 lane（ML-公平、HCI、法律、STS），写跨 lane 的 delta-first 定位，并将借用概念追溯到出处。 |
| [`facct-experiments`](skills/facct-experiments/SKILL.md) | 让证据匹配论断：带公平 baseline 的 disaggregated 审计、定性严谨与 reflexivity、proxy 有效性、consent 与伦理。 |
| [`facct-reproducibility`](skills/facct-reproducibility/SKILL.md) | 构建透明性：发布代码/数据、datasheets/model cards/data statements，以及在不破坏保密的前提下可审计的定性工作。 |
| [`facct-supplementary`](skills/facct-supplementary/SKILL.md) | 在正文、endmatter 声明区与 artifact 之间划分内容，并各自处理好匿名规则。 |
| [`facct-submission`](skills/facct-submission/SKILL.md) | OpenReview 终审：摘要 gate + focus areas、acmart 匿名 PDF、mutual anonymity、必需/可选 endmatter、archival 选择。 |
| [`facct-review-process`](skills/facct-review-process/SKILL.md) | 建模流程 —— mutually anonymous、跨学科、Area Chairs 与 Senior Area Chairs、Accept/Revise/Reject、复审 —— 及作者杠杆点。 |
| [`facct-author-response`](skills/facct-author-response/SKILL.md) | 撰写随修改稿提交的 Revise 轮 rebuttal，把每条排序关切映射到修改（若某届恢复 2026 式短 rebuttal 亦适用）。 |
| [`facct-artifact-evaluation`](skills/facct-artifact-evaluation/SKILL.md) | 准备 FAccT 期望的问责文档（datasheets、model cards、impact assessments）与发布的代码/数据，而非徽章。 |
| [`facct-camera-ready`](skills/facct-camera-ready/SKILL.md) | 去匿名、补上此前隐去的 Positionality/Acks、按 ACM 格式重排、补全 ACM 元数据、处理 OA/APC 与 camera-ready 截止。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 FAccT/FAT\* 论文，覆盖五种贡献形态与学科，附自检问题与同类混淆防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构福利审计研究的摘要与引言按 FAccT 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 FAccT 专用文档与 disaggregation 检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./FAccT-Skills
claude plugin install facct-skills
```

也可直接使用文件：每个 `skills/facct-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 FAccT 还是 NeurIPS/CHI/AIES？” → `facct-topic-selection`
- “按 FAccT CFP 与 endmatter 规则审我的稿” → `facct-submission`
- “拿到 Revise —— 规划 revise-and-resubmit 回复” → `facct-author-response`
- “把 datasheet 与 model card 准备好” → `facct-artifact-evaluation`

## 目录结构

```text
FAccT-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面
├── skills/
│   └── facct-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `facct-topic-selection`；delete-the-equity 与 mixed-reviewer 测试决定 FAccT
   （相对 NeurIPS/CHI/AIES/法律）是否合适。浏览 exemplars 看跨学科的一等 FAccT 贡献长什么样。
2. **构建证据时** —— 让 `facct-experiments` 与 `facct-reproducibility` 贴着研究；disaggregation、
   proxy 有效性、consent 与文档无法事后补救。
3. **写作时** —— 用 `facct-writing-style` 对照 worked example 打磨正文，用 `facct-supplementary`
   划分正文/endmatter/artifact，用 `facct-related-work` 做跨 lane 定位。
4. **截止周** —— 先在较早的 gate 前完成摘要与 focus-area 注册，再用 `facct-submission` 对终稿
   PDF、endmatter 与 artifact 逐项过审。
5. **投稿后** —— 用 `facct-review-process` 校准预期，用 `facct-author-response` 应对任何
   Revise 轮及其 rebuttal，随后 `facct-artifact-evaluation` 与 `facct-camera-ready` —— 若结果不利，则用
   `facct-topic-selection` 的路由表改投。

## FAccT 2027 锚点事实（周期快照，非永久规则）

- FAccT 2027 为**第 10 届**：**葡萄牙波尔图**，**2027 年 6 月 21-24 日**。摘要注册
  **2026-10-27**；论文 **2026-11-03**（截至 2026-11-24 均已过）；首轮决定（Accept / Revise major
  或 minor / Reject）**2026-12-22**；修改稿 + rebuttal **2027-01-28**；最终通知 **2027-03-23**；
  camera-ready **待定（TBD）**。CFP 所列 Program Chairs：Remi Denton、David Leslie、Aurelia
  Tamò-Larrieux、Isabel Valera（一篇博客署名为另外四人 —— 待核实）；General Chairs 尚未公布。
- 平台：**OpenReview**。评审：**mutually anonymous**、跨学科、按六个 focus area 匹配，通常三位审稿人
  + 一位 Area Chair，新增 **Senior Area Chairs**。模板：**ACM TAPS**（LaTeX `acmart` review/anonymous
  或 Word），单栏；**14 页 + 1 页 endmatter**，参考文献与附录不限；Revision/录用阶段 **15** 页。
- 必需 **Generative AI Usage Statement**（2027 为披露制）；投稿时附 **Ethical Considerations** 声明；
  Positionality、Acknowledgements、Author Contributions、Competing Interests 仅录用后添加。存档 ACM
  proceedings（含 non-archival 选项）；自 2026-01-01 起 **100% Open Access**（2026 APC 补贴价：会员
  $250 / 非会员 $350）。
- 历史：FAccT 2026（第 9 届，蒙特利尔，2026 年 6 月 25-28 日）截止 1 月 8 / 13 日，短 rebuttal
  截止 2026-02-24，首轮通知 03-02，返修 03-25，最终通知 2026-04-15。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 14+1 篇幅、mutual
   anonymity、Revise 轮、必需的 Generative AI Usage Statement）。
2. **转述事实** —— 仅经二手渠道读到并如实标注（如 FAccT '26 proceedings DOI：ACM DL 拒绝自动访问，
   经 Crossref 确认）。
3. **核验期不可确定项** —— 明确标为 待核实（如相互矛盾的 2027 Program Chairs 名单、2027
   camera-ready 日期、General Chairs、2027 CRAFT/Doctoral Colloquium call、2027 APC 补贴）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。FAccT 每届重定结构 —— 2026 引入 OpenReview、Revise 轮与
  Generative AI Usage Statement；2027 将截止提前到秋季、把 rebuttal 并入修改稿、新增 Senior Area
  Chairs、并把 AI 写作禁令改为披露制 —— 先核验各项是否延续。
- FAccT 无常任 editor-in-chief；General 与 PC Chairs 每届轮换。对**人**做连续性假设视为错误。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的
  负责任 AI 论文可能实为 workshop、期刊或 AIES 收录，而非 FAccT。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
