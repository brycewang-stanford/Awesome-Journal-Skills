# 《经济动态评论》智能体技能包（`red-skills`）

面向 **Review of Economic Dynamics（RED，《经济动态评论》）** 投稿作者的、针对该期刊定制的十二个
Claude 智能体技能。RED 是 **经济动态学会（Society for Economic Dynamics, SED）** 的会刊，由
**爱思唯尔（Elsevier）** 出版（ISSN 1094-2025，季刊，自 1998 年起）。

RED 的范围由 **研究方法与视角而非子领域** 界定：动态、定量经济学——动态一般均衡模型、增长、经济周期、
劳动、货币与财政政策、国际宏观——并通过 **理论、计算或实证的动态模型** 加以研究。高度计算化的定量宏观
研究完全在收录范围之内。本技能包把 RED 的真实规范固化下来，帮助稿件通过编辑初筛，并尊重该刊以代码为先
的可复制文化。

## RED 的独特之处（也是本技能包存在的理由）

- **真实存在的逐篇投稿费。** 标准 **175 美元**；若投稿时全部合作者均为全日制学生则为 **100 美元**；
  **第二次及以后的重投免收**。在收到费用之前评审不会启动——这在多数顶级综合性经济学期刊中并不常见。
- **由学术共同体而非综合性编委挂名运营。** RED 归 SED（SED 年会背后的宏观/动态学术共同体）所有。
- **以代码为先的可复制要求。** 专门的《已发表论文数据与计算机代码可得性》政策同时覆盖
  **计算类与实证类** 论文；存档发布在 RED 网站上，并作为可被引用的 **RePEc “Computer Codes”** 系列编入索引。
  readme.txt 要求很具体（软件/操作系统、程序运行顺序、预计运行时间、随机种子）。
- **速度。** SED 宣传快速评审，目标是初筛通过后平均约 **两个月** 的周转时间。
- **单向匿名评审**（非双盲），编辑初筛后至少送 **两位** 审稿人。
- 协调主编（Coordinating Editor）：**Loukas Karabarbounis**（明尼苏达大学 / 明尼阿波利斯联储）。

## 十二个技能

| 技能 | 职责 |
| --- | --- |
| `red-workflow` | RED 稿件全生命周期总览 |
| `red-topic-selection` | 问题是否属于动态/定量且在 RED 范围内 |
| `red-literature-positioning` | 在动态经济学与 SED 文献中的定位 |
| `red-identification-strategy` | 按论文类型：模型假设/正则条件/因果设计 |
| `red-data-analysis` | 校准、矩匹配、估计、数值求解规范 |
| `red-contribution-framing` | 提炼定量/动态层面的边际贡献 |
| `red-tables-figures` | 脉冲响应、矩表、校准表、模型对数据的图表 |
| `red-writing-style` | RED 行文风格；作者-年份引用；约 250 词摘要 |
| `red-replication-and-data-policy` | 数据/代码存档、readme.txt、.zip/.gz 提交给代码编辑、RePEc 索引 |
| `red-review-process` | 初筛、单向匿名评审、约两个月目标 |
| `red-submission` | 投稿前预检：费用、ScienceDirect/Editorial Manager、关键词、AI 声明 |
| `red-rebuttal` | 收到修改重投（R&R）后的答复审稿人策略 |

## 安装 / 使用

本仓库是一个 Claude Code 插件。技能位于 `skills/red-<role>/SKILL.md`，并在
`.claude-plugin/marketplace.json` 与 `.claude-plugin/plugin.json` 中声明。将你的 Claude Code
marketplace 指向本目录并启用 `red-skills` 插件，即可按名称调用技能。

## 来源与诚信

每一条针对该期刊的事实都可在 [`resources/official-source-map.md`](resources/official-source-map.md)
（访问日期 2026-06-01）追溯到 SED/Elsevier 的官方页面。无法从可直接读取的官方页面确认的条目在该文件中
标注为 **待核实**，并且在技能中绝不作为事实陈述——尤其是：未确认的稿件长度上限、数据政策生效日期、
以及开放获取（OA/APC）费用金额。Guide for Authors 页面对直接抓取返回 HTTP 403，因此摘要字数上限、
评审模式、作者-年份引用与 1–6 个关键词等事实经由搜索抽取获得，并已相应标注。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。
