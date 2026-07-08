# SOSP Skills

[English](README.md) | **简体中文**

面向 ACM Symposium on Operating Systems Principles（SOSP）投稿的 12 个 agent
skills。SOSP 是 SIGOPS 的旗舰会议，接收"构建并实测"（built-and-measured）的计算机系统
软件研究：设计、实现、分析、评估与部署。本包覆盖完整投稿战役：判断项目是否具备
SOSP 形态、按春季 abstract 与全文两道 HotCRP 关口倒排日程、把论证压进"12 页正文 +
参考文献不计页"的版面、通过带 PC 主席审计 conflict 的 double-blind 评审、撰写职责
范围极窄的 author response、把 7 月的录用转化为 shepherd 把关的 13/14 页
camera-ready，并通过 sysartifacts 的 artifact evaluation 争取 ACM badges。

官方依据核验日期：2026-07-08。已核验 sigops.org 上的 SOSP 2026 Call for Papers 与
author guidelines、sosp26 HotCRP deadlines 页、sysartifacts 的 SOSP 2025/2026
artifact-evaluation 页面、SIGOPS 年度化公告、SIGOPS Hall of Fame、ACM Digital
Library 的 SOSP proceedings 以及 dblp。每条逐年变化的事实都能在
[`resources/official-source-map.md`](resources/official-source-map.md) 中追溯到
URL；无法当场钉死的条目一律标注 **待核实**，绝不臆测。构建期间对 sigops.org 的直接
抓取被网关拦截（403），source map 同时记录了"搜索引擎渲染 + ACM DL/dblp 交叉验证"的
替代核验方法。

## SOSP 的独特之处

本包围绕该会议自身的机制组织，而非泛泛的会议经验：

- **自 2024 年起每年举办。** SOSP 结束了与 OSDI 数十年的隔年交替（SIGOPS 2023 年
  公告）。第 30 届 2024 年 11 月在 Austin，第 31 届 2025 年 10 月在首尔，第 32 届
  2026 年 9 月 29 日 - 10 月 2 日在布拉格。投稿规划从两年一搏变成滚动巡回，多个
  skill 专门讲改投调度。
- **两道关口、一种页数结构。** Abstract registration 先于全文截止，且是硬关口：
  注册分配的 paper ID 会替换首页作者栏。投稿最多 **12 页 technical content，参考
  文献不计入** —— 这种预算形态奖励删正文、惩罚压缩参考文献。
- **Conflict 由主席审计。** PC 主席会复核申报的 conflict，可以增加也可以**删除**
  条目；把某位 PC 成员列为 conflict 以躲开严苛审稿人被明确点名为不当行为。本包把
  conflict 清单当作一份必须能当面辩护的文件来对待。
- **职责范围极窄的 response。** PC 会议前的 author response 只做两件事：纠正评审
  中的事实错误、回答审稿人明确提出的问题 —— 不得加新实验、不得承诺后续工作，强烈
  建议 500 词以内。
- **决定在会议室里做出。** 单轨 PC meeting 会现场辩论每篇候选论文；正文与 response
  都要写给"替你辩护的人"，而不是为了抬高平均分。
- **带 shepherd 的 camera-ready，页数扩容。** 终版 13 页 technical content，
  shepherd 可批准第 14 页 —— 多出的空间是留给评审意见的。
- **录用后的合作式 artifact evaluation。** sysartifacts 社区在决定之后运行 SOSP 的
  AE：single-blind，窗口期内允许作者修复问题，badge 目标（Available / Functional /
  Reusable，外加 Distinguished Artifact）由作者自选。
- **可引用的学术谱系。** SIGOPS Hall of Fame 与五十余年的 proceedings 意味着
  related work 会被一个熟知谱系的 PC 检验；exemplars library 收录了核验过的 SOSP
  经典，以及绝不能误归给 SOSP 的 OSDI/ATC 名作。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`sosp-submission`](skills/sosp-submission/SKILL.md) | 核查 HotCRP 就绪度：双截止、12 页 + 参考文献版式、paper-ID 匿名化、可辩护的 conflict、desk-reject 分诊。 |
| [`sosp-author-response`](skills/sosp-author-response/SKILL.md) | 撰写窄职责 response：只纠事实、只答提问，预算约 500 词，写给 PC meeting。 |
| [`sosp-camera-ready`](skills/sosp-camera-ready/SKILL.md) | 经营 shepherd 线程、把第 13/14 页花在评审关切上、安全去匿名、走通 ACM 版权流程。 |
| [`sosp-artifact-evaluation`](skills/sosp-artifact-evaluation/SKILL.md) | 通知后数日内在 sysartifacts 注册、按可运行性给 claim 分层、选定 badge、为交互窗口配人。 |
| [`sosp-reproducibility`](skills/sosp-reproducibility/SKILL.md) | 把平台钉死到用户态以下、机械化采集环境、让每张图一条命令即可从日志重建。 |
| [`sosp-supplementary`](skills/sosp-supplementary/SKILL.md) | 在正文与独立补充文档之间切分内容，绝不把评审关键证据流放到补充材料。 |
| [`sosp-review-process`](skills/sosp-review-process/SKILL.md) | 建模分轮评审、response 窗口与 PC meeting；按"还能改变什么"给评审意见分诊。 |
| [`sosp-writing-style`](skills/sosp-writing-style/SKILL.md) | 以可提取的 principle 开篇、搭建首页论证弧线、给 12 页做预算、让图自己说话。 |
| [`sosp-related-work`](skills/sosp-related-work/SKILL.md) | 沿 SOSP/OSDI 谱系按结构轴定位；处理第三人称自引与 concurrent work。 |
| [`sosp-experiments`](skills/sosp-experiments/SKILL.md) | 把 claim 映射到实验、公平调优 baseline、覆盖微基准/端到端/trace 三层、带分布报告尾延迟。 |
| [`sosp-workflow`](skills/sosp-workflow/SKILL.md) | 把项目放上年度日历、跑通 7-8 月三线并行冲刺、在巡回赛中改投被拒稿件。 |
| [`sosp-topic-selection`](skills/sosp-topic-selection/SKILL.md) | 运行 principle/embodiment/evidence 形态测试，不合适时改道 OSDI、ATC、NSDI、FAST、ASPLOS、VLDB、MLSys、EuroSys 或 HotOS。 |

## Resources 一览

| 资源 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 本包全部事实的官方 URL，核验日期 2026-07-08，含网关受阻时的核验方法与待核实清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 在线官方系统（CFP、HotCRP、sysartifacts、ACM DL、Hall of Fame）及作者侧检查清单与"禁止推断"规则。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 按"问题 × principle"组织的已核验 SOSP 经典，以及绝不能归到 SOSP 名下的 OSDI/ATC/EuroSys 名作。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构系统论文的摘要与引言按 SOSP 首页弧线逐步重写的前后对照。 |
| [`resources/code/README.md`](resources/code/README.md) | 把仓库级 ML 会议可复现性工具包适配到 OS 级 artifact 与 sysartifacts 打包的适配器。 |

## 2026 周期速览（历史锚点，不是永久规则）

| 里程碑 | 日期 |
| --- | --- |
| Abstract registration | 2026-03-27（AoE 为 03-26） |
| 全文截止 | 2026-04-02 7:59:59 AM EDT（AoE 为 04-01） |
| 录用通知 | 2026-07-03 |
| Camera-ready | 2026-08-28 |
| 会议（布拉格，捷克） | 2026-09-29 至 10-02 |

以本包核验日（2026-07-08）计，2026 届的决定刚刚公布：录用团队正处于
shepherding/AE/行程三线冲刺中，被拒团队正在年度化的 SOSP/OSDI 巡回上改投。
SOSP 2027 尚无任何公开日期（待核实）；永远不要对着"推断出来的截止日"倒排日程。

## 目录结构

```text
SOSP-Skills/
├── .claude-plugin/
│   ├── plugin.json           # 插件清单（sosp-skills，v0.1.0，MIT）
│   └── marketplace.json      # marketplace 条目，声明全部 12 个 skill 路径
├── assets/cover.svg          # 封面图
├── skills/                   # 12 个 skill，每目录一个 SKILL.md
│   └── sosp-*/SKILL.md
├── resources/
│   ├── official-source-map.md
│   ├── external_tools.md
│   ├── exemplars/library.md
│   ├── worked-examples/01-introduction.md
│   └── code/README.md        # 指向 ../shared-resources/ml-conference-methods 的适配器
├── README.md / README.zh-CN.md
└── LICENSE（MIT）
```

## Skills 之间如何联动

各 skill 之间靠交叉引用而非重复。证据三角 ——
[`sosp-experiments`](skills/sosp-experiments/SKILL.md) 设计证据、
[`sosp-reproducibility`](skills/sosp-reproducibility/SKILL.md) 让证据可追溯、
[`sosp-artifact-evaluation`](skills/sosp-artifact-evaluation/SKILL.md) 把证据打包换
badge —— 共用同一套 claims-map 纪律，只定义一次、两处引用。Response 链条同理：
[`sosp-review-process`](skills/sosp-review-process/SKILL.md) 分诊"还能改变什么"，
[`sosp-author-response`](skills/sosp-author-response/SKILL.md) 把不足 500 词的预算
精确花在这些点上。截止机制只写在
[`sosp-submission`](skills/sosp-submission/SKILL.md) 与
[`sosp-workflow`](skills/sosp-workflow/SKILL.md)；文风、文献定位与补充材料政策各自
只有一个权威出处。

## 建议入口

- **提前十二个月：** [`sosp-topic-selection`](skills/sosp-topic-selection/SKILL.md)
  → [`sosp-workflow`](skills/sosp-workflow/SKILL.md) →
  [`sosp-experiments`](skills/sosp-experiments/SKILL.md)，底层持续运行
  [`sosp-reproducibility`](skills/sosp-reproducibility/SKILL.md)。
- **截止月：** [`sosp-writing-style`](skills/sosp-writing-style/SKILL.md) →
  [`sosp-related-work`](skills/sosp-related-work/SKILL.md) →
  [`sosp-supplementary`](skills/sosp-supplementary/SKILL.md) →
  [`sosp-submission`](skills/sosp-submission/SKILL.md)。
- **评审到手：** [`sosp-review-process`](skills/sosp-review-process/SKILL.md) →
  [`sosp-author-response`](skills/sosp-author-response/SKILL.md)。
- **已录用：** [`sosp-camera-ready`](skills/sosp-camera-ready/SKILL.md) 与
  [`sosp-artifact-evaluation`](skills/sosp-artifact-evaluation/SKILL.md) 并行。

## 维护说明

- 任何涉及截止日期的建议之前，必须重开当年 CFP、authors 页与 HotCRP；SOSP 每年
  重发规则，主办城市也会变。
- 本包中的 2026 年日期、页数限制、response 机制与 AE 细节都是"单一已核验周期"的
  历史锚点。
- 官方页面互相矛盾时：截止时间以 HotCRP 为准，版式以最新 authors 页为准，并把冲突
  连同新的核验日期记入 source map。
- 直接访问 sigops.org 失败时，按
  [`resources/official-source-map.md`](resources/official-source-map.md) 中记录的
  三角核验法操作。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。由 Bryce Wang 维护，属于
[awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills)
项目的一部分。
