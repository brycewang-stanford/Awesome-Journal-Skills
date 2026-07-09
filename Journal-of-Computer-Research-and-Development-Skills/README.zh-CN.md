# 《计算机研究与发展》技能包（中文详版）(JCRD Skills)

本文件是《计算机研究与发展》(Journal of Computer Research and Development, JCRD) 技能包的**中文
详版**，与 [`README.md`](README.md) 互补。JCRD 由中国科学院计算技术研究所与中国计算机学会 (CCF)
主办、科学出版社出版，创刊于 1958 年，现为 **CCF A 类**中文旗舰**月刊**，以**专题(special topic)
组稿**见长、综述与原创并重、实行**双盲评审**。刊号 ISSN 1000-1239、CN 11-1777/TP。

官方依据核验日期 **2026-07-09**：官网 `crad.ict.ac.cn`《投稿须知》与期刊简介、CNKI/万方/维普、
CCF 推荐中文科技期刊目录、中科院计算所出版物页。核验环境网关对官网直接抓取返回 403，故经搜索渲染
阅读并多 surface 交叉核对；完整来源与 **待核实** 项见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 一、为何要专门为 JCRD 建包

《计算机研究与发展》是**综合性**中文计算机期刊，但它区别于姊妹刊的关键在于**组织方式**与**评审
方式**：

- **专题组稿。** 本刊每期常围绕前沿主题组织**专题**，由**客座编辑**牵头征稿，专题内**综述**与
  **原创研究**并重。作者可投常规栏目，也可投**对口专题**（受专题主题与截稿时间表约束）。这与
  《计算机学报》(Chinese Journal of Computers) 的综合长文、《软件学报》(Journal of Software) 的
  软件方向形成明确区分。
- **双盲评审。** 外审专家只见内容、不见身份；作者须全稿匿名。这比部分姊妹刊的单盲更严，直接影响
  写作（自引第三人称）、投稿（匿名清扫）与修回（措辞不泄露身份）。
- **只收中文稿。** 须中英文题名/摘要/关键词、中图分类号 (TP)、GB/T 7714 参考文献。
- **稿件类型。** 学术论文、技术报告、综述、研究热点论文并行。

英文刊名中的 Journal / Computer / Research / Development 四词与本包目录名一致，各技能正文均自然
复现，确保线索匹配。

## 二、12 个技能怎么配合

| 阶段 | 技能 | 关键动作 |
|---|---|---|
| 选题定位 | `jcrd-topic-selection` | 判断投常规栏目还是对口专题；与姊妹刊选路；核对专题截稿。 |
| 全流程 | `jcrd-workflow` | 从投稿到录用倒排：写作→双盲投稿→外审→修回→终审→定稿。 |
| 写作 | `jcrd-writing-style` | 摘要五要素、关键词、中图分类号、GB/T 7714、术语统一。 |
| 综述 | `jcrd-related-work` | 分类框架、delta 定位、双盲自引。 |
| 实验 | `jcrd-experiments` | 数据集、基线、显著性、消融、真实系统度量、图表规范。 |
| 可复现 | `jcrd-reproducibility` | 环境固定、随机性控制、匿名可运行材料、诚实可用性说明。 |
| 补充材料 | `jcrd-supplementary` | 正文/附件划分、专题补充约定、多媒体附件。 |
| 投稿 | `jcrd-submission` | 双盲终审：系统、格式、栏目/专题归属、匿名清扫、退稿分诊。 |
| 审稿流程 | `jcrd-review-process` | 初审→外审→复审→终审、多轮修回、作者杠杆点。 |
| 答复修回 | `jcrd-author-response` | 逐条回应、映射修改、双盲措辞、修回说明格式。 |
| 代码数据 | `jcrd-artifact-evaluation` | 可用性现状、匿名托管、录用后永久化与许可。 |
| 定稿校样 | `jcrd-camera-ready` | 去匿名、补全元数据、校对、出版核对。 |

## 三、事实纪律与三类陈述

1. **已核验事实**：刊号、月刊、主办与出版方、只收中文稿、双盲评审、CCF A/T1、征稿范围与稿件类型
   —— 均可追溯到 source map 编号来源。
2. **转述事实**：如个别投稿人给出的「约 4 个月」审稿周期、部分专题历史主题 —— 标注为二手转述。
3. **待核实**：主编/编委名单、影响因子（各 surface 数据不一）、版面费、专题当期主题与截稿日、
   摘要精确字数与篇幅上限、模板版本 —— 一律以官网当期页面为准，不杜撰。

## 四、安装与使用

```bash
claude plugin marketplace add ./Journal-of-Computer-Research-and-Development-Skills
claude plugin install jcrd-skills
```

典型调用：

- 「这篇投 JCRD 哪个专题？还是投计算机学报？」→ `jcrd-topic-selection`
- 「按《计算机研究与发展》双盲规则审稿」→ `jcrd-submission`
- 「写外审意见的修回说明」→ `jcrd-author-response`
- 「整理代码与数据到可用性标准」→ `jcrd-artifact-evaluation`

## 五、维护说明

- 专题主题、客座编辑、截稿日逐期变动；影响因子、版面费、审稿周期逐年变动。用前先核官网当期页面。
- 若多 surface 冲突，以官网当期《投稿须知》/当期目次为准，并记录冲突。
- 新增样例遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾核验流程。

## License

MIT —— 见 [`LICENSE`](LICENSE)。中文主页见 [`README.md`](README.md)。
