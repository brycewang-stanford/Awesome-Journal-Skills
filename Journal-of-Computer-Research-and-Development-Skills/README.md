# 《计算机研究与发展》技能包 (JCRD Skills)

面向《计算机研究与发展》(Journal of Computer Research and Development, JCRD) 投稿的 **12 个 agent
技能**。JCRD 由**中国科学院计算技术研究所**与**中国计算机学会 (CCF)** 主办、**科学出版社**出版，
创刊于 1958 年（旧称《电子计算机动态》，为中国第一本计算机刊物），现为 **CCF A 类**中文旗舰
**月刊**（CCF「计算领域高质量科技期刊分级目录」T1 类）。本包覆盖一次 JCRD 投稿的完整弧线：判断
工作投本刊常规栏目还是**对口专题**、写好中文长文、构建能过外审的实验或综述证据、完成**双盲**投稿、
应对多轮同行评审与修回、直到录用定稿校样与代码/数据可用性。

> English: this is the Chinese-primary page. See [`README.zh-CN.md`](README.zh-CN.md) for the
> fuller Chinese edition. The venue is the **Journal of Computer Research and Development (JCRD)**,
> a CCF Class-A Chinese-language monthly.

官方依据核验日期：**2026-07-09**。已通过官网 `crad.ict.ac.cn`《投稿须知》与期刊简介、CNKI/万方/
维普期刊主页、CCF 推荐中文科技期刊目录与中科院计算所出版物页交叉核验。核验环境网关对官网直接抓取
返回 403，故官方页面经搜索渲染阅读并多 surface 交叉核对；完整来源与所有 **待核实** 项见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 本刊与姊妹刊的区别

以下机制驱动了各技能的大部分建议，也对应从姊妹刊转投作者最常犯的错误：

- **专题(special topic)组稿见长。** JCRD 每期常围绕前沿主题（体系结构、人工智能、大数据、信息
  安全、软件技术等）组织**专题**，由**客座编辑**发布征稿启事、设定主题与出版时间表；**综述与原创
  并重**。这是本刊区别于《计算机学报》(综合长文) 与《软件学报》(软件方向) 的核心。
- **双盲评审。** 外审专家只见稿件内容、不见作者身份；作者须在正文、致谢、基金号、自引与文件属性中
  隐去身份。这一点比部分姊妹刊的单盲更严。
- **只收中文稿。** 本刊不受理英文稿，须提供中英文题名、中英文摘要与关键词、中图分类号 (TP)。
- **稿件类型多元。** 学术论文、技术报告、综述、研究热点论文并行，综述与研究热点是本刊显著栏目。
- **多轮同行评审 + 修回。** 编辑初审→专家外审→复审→主编终审，可能多轮修回；作者以逐条**修回说明**
  回应意见。
- **GB/T 7714 与中文科技写作规范。** 参考文献按国标中英文对照著录，摘要/关键词/中图分类号齐备。

## 技能清单

| 技能 | 作用 |
| --- | --- |
| [`jcrd-topic-selection`](skills/jcrd-topic-selection/SKILL.md) | 在 JCRD 常规栏目与对口专题、以及姊妹刊之间选路，判断选题、栏目定位与专题时间表。 |
| [`jcrd-workflow`](skills/jcrd-workflow/SKILL.md) | 从投稿到录用倒排全流程：选题、写作、双盲投稿、外审、修回、终审、定稿。 |
| [`jcrd-writing-style`](skills/jcrd-writing-style/SKILL.md) | 中文科技写作规范：摘要五要素、关键词、中图分类号、GB/T 7714 参考文献、术语统一。 |
| [`jcrd-related-work`](skills/jcrd-related-work/SKILL.md) | 相关工作与文献综述：分类框架、delta 定位、双盲下的自引处理。 |
| [`jcrd-experiments`](skills/jcrd-experiments/SKILL.md) | 实验设计与呈现：数据集、基线、显著性、消融、真实系统度量与图表规范。 |
| [`jcrd-reproducibility`](skills/jcrd-reproducibility/SKILL.md) | 可复现性：环境固定、随机性控制、匿名可运行材料与诚实的可用性说明。 |
| [`jcrd-supplementary`](skills/jcrd-supplementary/SKILL.md) | 补充材料/附录：正文与附件的划分、专题补充约定、多媒体附件。 |
| [`jcrd-submission`](skills/jcrd-submission/SKILL.md) | 双盲投稿终审：投稿系统、格式、栏目/专题归属、匿名清扫、退稿风险分诊。 |
| [`jcrd-review-process`](skills/jcrd-review-process/SKILL.md) | 审稿流程建模：初审→外审→复审→终审、多轮修回与作者杠杆点。 |
| [`jcrd-author-response`](skills/jcrd-author-response/SKILL.md) | 审稿意见答复与修回说明：逐条回应、映射到修改、双盲下的措辞。 |
| [`jcrd-artifact-evaluation`](skills/jcrd-artifact-evaluation/SKILL.md) | 代码与数据可用性：现状说明、匿名托管、录用后永久化与许可。 |
| [`jcrd-camera-ready`](skills/jcrd-camera-ready/SKILL.md) | 录用后定稿/校样/清样：去匿名、补全元数据、校对与出版核对。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源、访问方式说明、已核验事实与 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官网与投稿入口、CCF/CNKI/万方交叉核对、GB/T 7714 与作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 按栏目/专题的贡献形态基准与姊妹刊边界辨析，附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 中文摘要与引言按 JCRD 弧线改写的 before→after（虚构示例）。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享可复现工具，并给出 JCRD 专用（双盲、可用性）检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./Journal-of-Computer-Research-and-Development-Skills
claude plugin install jcrd-skills
```

也可直接使用文件：每个 `skills/jcrd-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- 「这篇该投 JCRD 常规栏目还是某专题？还是投计算机学报/软件学报？」→ `jcrd-topic-selection`
- 「按《计算机研究与发展》双盲规则审我的稿」→ `jcrd-submission`
- 「收到外审意见，帮我写修回说明」→ `jcrd-author-response`
- 「把代码与数据整理到可用性标准」→ `jcrd-artifact-evaluation`

## 目录结构

```text
Journal-of-Computer-Research-and-Development-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个技能）
├── README.md                 # 本文件（中文主页）
├── README.zh-CN.md           # 中文（更详）
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── jcrd-<topic>/SKILL.md # 12 个技能，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 事实纪律

本包区分三类陈述：**已核验事实**（追溯到 source map 编号来源，如刊号 ISSN 1000-1239 / CN
11-1777/TP、月刊、只收中文稿、双盲评审、CCF A/T1）；**转述事实**（仅经二手渲染读到并标注，如
个别投稿人给出的审稿周期）；**核验期不可确定项**（明确标 **待核实**，如主编/编委名单、影响因子、
版面费、专题当期主题与截稿日）。若任何陈述以第一类口吻呈现第二/三类内容，视为 bug，对照官网修正。

## 维护说明

- 以上均为**周期快照**：专题主题、客座编辑、截稿日、影响因子逐期/逐年变动，用前先核当期页面。
- 影响因子、版面费、审稿周期不同 surface 数据不一，均标 **待核实**，勿在正文以确定口吻给出。
- 新增样例遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾核验流程。

## License

MIT —— 见 [`LICENSE`](LICENSE)。更详中文说明见 [`README.zh-CN.md`](README.zh-CN.md)。
