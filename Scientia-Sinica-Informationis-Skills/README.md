# 《中国科学：信息科学》技能包 · Scientia Sinica Informationis (SSI) Skills

面向 **《中国科学：信息科学》(SCIENTIA SINICA Informationis, SSI)** 投稿的 12 个智能体技能。
本刊由**中国科学院**与**国家自然科学基金委员会**共同主办、**《中国科学》杂志社** (Science China Press)
出版，是**国家级、大信息学科综合中文旗舰**，覆盖**计算机科学与技术、控制科学与控制工程、
信息与通信工程、微电子与固体电子学**等领域，与英文姊妹刊 **Science China Information Sciences (SCIS)**
并行。本包覆盖从选题定位、中文科技写作、三审三校审稿、修回答复到录用定稿的全流程。

> English note: this is a **Chinese-language** journal pack for *Scientia Sinica Informationis*
> (SSI), the Chinese sister of *Science China Information Sciences*. 中文详细说明见
> [`README.zh-CN.md`](README.zh-CN.md)。

官方依据核对于 **2026-07-09**：SSI 官网 (scis.scichina.com) 首页与《投稿须知》、SciEngine 平台
SSI/SCIS 主页、以及 CNKI/万方/维普期刊主页。验证沙箱直接抓取官网返回 403，故官方页面经
搜索渲染读取并双源交叉核实，完整信源与全部 **待核实** 项见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 本刊与兄弟刊/姊妹刊有何不同

- **国家级大信息学科综合旗舰**：SSI 不是单一子学科刊，而是覆盖计算机、控制、通信、
  电子/微电子的综合刊，**定位高、以重大原创与综述（评述）为主**，强调**科学价值与创新高度**。
- **中英文相对独立的两刊**：中文版 SSI 与英文版 Science China Information Sciences (SCIS)
  主办、学科一致，但官方称为**相对独立的两个刊物**；应**择一投稿**，中英文互转/一稿两投政策
  **以编辑部当期说明为准（待核实）**，本包不臆断。
- **四个栏目各有定位**：**评述**（约 20 页，一般编委邀请）、**论文**（主体）、
  **快报**（≤4 页，优先发表）、**学术介绍**。
- **中文科技写作规范**：要求**中、英文双语摘要**、关键词，LaTeX 排版（官方模板），
  参考文献著录与中图分类号按当期须知（GB/T 7714 与否**待核实**）。
- **三审三校把关**：坚持公平公正客观的审稿原则；作者 90 天内未获意见、通知编辑部后可改投他刊。
- **版面费**：对录用稿件收取版面费，出版后免费提供样刊（**金额待核实**）。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`ssi-topic-selection`](skills/ssi-topic-selection/SKILL.md) | 判断该投 SSI（还是英文 SCIS 或计算机学报/自动化学报等兄弟刊），并定栏目（评述/论文/快报）。 |
| [`ssi-workflow`](skills/ssi-workflow/SKILL.md) | 从选题到录用的全流程编排：投稿、三审三校、修回轮次、校样定稿。 |
| [`ssi-writing-style`](skills/ssi-writing-style/SKILL.md) | 中文科技写作规范：首页弧线、中英文双语摘要、关键词、量与单位、参考文献、中图分类号。 |
| [`ssi-related-work`](skills/ssi-related-work/SKILL.md) | 相关工作与文献综述：讲清差异（delta）、覆盖国内外文献、避免自引泄露。 |
| [`ssi-experiments`](skills/ssi-experiments/SKILL.md) | 实验设计与呈现：证据与主张相称、公平对比、仿真/实测区分、统计与消融。 |
| [`ssi-reproducibility`](skills/ssi-reproducibility/SKILL.md) | 可复现性：数据/代码可用性声明、实验可重复、来源固定。 |
| [`ssi-supplementary`](skills/ssi-supplementary/SKILL.md) | 附录/补充材料/多媒体附件：正文与补充的划分原则。 |
| [`ssi-submission`](skills/ssi-submission/SKILL.md) | 投稿前审计：投稿系统、LaTeX 排版、栏目、双语摘要、版面费、伦理与学术规范。 |
| [`ssi-review-process`](skills/ssi-review-process/SKILL.md) | 审稿流程建模：初审→外审→复审→终审、三审三校、修回轮次与作者杠杆。 |
| [`ssi-author-response`](skills/ssi-author-response/SKILL.md) | 审稿意见答复与修回说明：逐条对应、标注修改位置、礼貌而有据。 |
| [`ssi-artifact-evaluation`](skills/ssi-artifact-evaluation/SKILL.md) | 代码与数据可用性：讲清本刊现状、如何提供可用材料（若有要求）。 |
| [`ssi-camera-ready`](skills/ssi-camera-ready/SKILL.md) | 录用后定稿/校样/清样：清样校对、元数据、版面费与样刊、发表信息。 |

## 资源

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 8 个信源、URL 与访问日期、已核实事实、访问方式说明、待核实清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | SSI 官网、投稿系统、SciEngine、LaTeX 模板等入口与交叉核实 surface。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 按栏目 × 贡献形状的写作范式坐标，避免与 SCIS 及兄弟刊混淆。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构信息科学论文"中英文摘要 + 引言"的改写前后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享可复现材料工具的适配，以及 SSI 专属检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 在仓库克隆中
claude plugin marketplace add ./Scientia-Sinica-Informationis-Skills
claude plugin install ssi-skills
```

或直接使用文件：每个 `skills/ssi-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 告诉智能体何时触发。典型调用：

- "这个成果该投《中国科学：信息科学》还是英文 SCIS / 计算机学报？" → `ssi-topic-selection`
- "按 SSI 的要求审一遍我的稿件与双语摘要" → `ssi-submission`
- "收到外审意见，帮我写修回说明" → `ssi-author-response`
- "录用了，帮我核对清样与发表信息" → `ssi-camera-ready`

## 包结构

```text
Scientia-Sinica-Informationis-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 技能）
├── README.md                 # 本文件（中文主页）
├── README.zh-CN.md           # 中文详细说明
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── ssi-<topic>/SKILL.md  # 12 个技能，每个一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 事实纪律

本包区分三类陈述：**已核实事实**（可双源追溯到信源地图，如主办单位、栏目、月刊、
90 天改投条款）、**报道级事实**（仅单一 surface 提及，如"三审三校"表述）、
**不可确认项**（标 **待核实**，如主编姓名、版面费金额、影响因子、录用率、中英文互转政策、
GB/T 7714 与中图分类号细则）。凡以"已核实"口吻陈述报道级/不可确认内容，均按 bug 处理，
以官网当期页面为准修正。绝不杜撰数字。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English readers: see the one-line note above;
中文详细说明见 [`README.zh-CN.md`](README.zh-CN.md)。
