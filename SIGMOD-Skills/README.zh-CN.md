# SIGMOD Skills（中文说明）

面向 ACM SIGMOD International Conference on Management of Data（数据库与数据管理
领域的 ACM 旗舰会议）研究论文的 12 个 agent skills。本包围绕 SIGMOD 在 CS 会议中
结构上最特殊的几点构建：研究论文实质上是投给期刊 **PACMMOD**（Proceedings of the
ACM on Management of Data）的**每年四轮**投稿，评审结果包含真正的 major/minor
**revision**；被拒后有 **12 个月禁投期**；并配有旗舰级 artifact 项目——
**Availability & Reproducibility Initiative（ARI）**，其徽章会嵌入 ACM DL 上的
正式 PDF。

官方依据核验日期：**2026-07-08**。已核验 SIGMOD 2027 研究轨 Call for Papers 与
important-dates 日历、PACMMOD 作者指南、`reproducibility.sigmod.org` 的 ARI 页面、
SIGMOD 2026 会议站点，以及用于 exemplar 验证的 sigmod.org 奖项页面。精确 URL、
已核验事实与"待核实"清单见
[`resources/official-source-map.md`](resources/official-source-map.md)。该文件同时
记录了访问方式说明：部分官方站点拒绝自动化抓取，事实通过对确切 URL 的搜索引擎
渲染读取，并在多个独立官方页面间交叉核对。

## 为什么 SIGMOD 需要单独一个包

- **"选轮次"取代了年度截稿。** SIGMOD 2027 的论文截稿为 2026 年 1 月 17 日 /
  4 月 17 日 / 7 月 17 日 / 10 月 17 日（摘要与利益冲突声明提前一周，均为
  11:59 PM AoE），每轮对应一期 PACMMOD。选哪一轮、以及输掉一轮的禁投代价，
  本身就是一项策略技能。
- **Revision 是一等公民。** major/minor revision 判定允许增加一页正文、给一个月
  时间，并要求提交最长四页、按审稿人分色标注修改的 revision letter——这一文体
  在其他 CS 会议几乎不存在。
- **双匿名贯穿数月**，覆盖 feedback 阶段与 revision，这改变了 artifact、预印本
  与代码仓库的处理方式。
- **可复现性被制度化。** PACMMOD 期望论文尽可能公开代码、数据、脚本与 notebook；
  ARI 在录用后按 Artifacts Available / Artifacts Evaluated / Results Reproduced
  三级徽章评估 artifact，并设 Best Artifact 奖。
- **邻居密集。** PVLDB 按月滚动收稿，PODS 收理论，ICDE 收更宽的数据工程，
  KDD 收挖掘，TODS 收期刊化扩展。在它们之间路由是本包显式教授的常规决策。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| `sigmod-submission` | 审核单轮投稿：摘要+COI 提前截止、CMT、12 页 ACM 模板、匿名、每人 10 篇上限、考虑禁投期的轮次选择。 |
| `sigmod-author-response` | 起草两类作者发言：轮中 feedback 回复，以及带分色标注的四页 revision letter。 |
| `sigmod-camera-ready` | 执行 PACMMOD 版式移植、去匿名、按轮次排期的 issue 发表、ACM DL 元数据与会议报告安排。 |
| `sigmod-artifact-evaluation` | 准备 ARI：HotCRP 注册、徽章阶梯、评估标准、硬件诚实披露、Best Artifact 定位。 |
| `sigmod-reproducibility` | 把溯源做进论文：代码/配置/数据/负载/硬件五层锁定、方差底线、baseline 公平、复现债务台账。 |
| `sigmod-supplementary` | 管理 12 页之外的材料：扩展技术报告、匿名冻结仓库、跨轮次托管卫生。 |
| `sigmod-review-process` | 建模轮次流水线：feedback 窗口、三值判定、一个月 revision、禁投期，以及"造系统的人"如何读稿。 |
| `sigmod-writing-style` | 落实第一页契约、running example 手法、有边界的系统性能声明与 12 页预算。 |
| `sigmod-related-work` | 覆盖五条文献线、防"重新发明"的深历史尽调、滚动venue的并发论文与重叠规则。 |
| `sigmod-experiments` | 设定评测门槛：负载真实性阶梯、调优过的 baseline、曲线优于单点、机制归因消融、败绩披露。 |
| `sigmod-workflow` | 把一轮当五幕来排期：倒排计划、revision 带宽、组合约束、预先商定的被拒预案。 |
| `sigmod-topic-selection` | 项目路由：research 轨 vs industrial 轨、SIGMOD vs PVLDB/PODS/ICDE/KDD/CIDR/TODS、"数据管理原语"测试。 |

## Resources

[`resources/`](resources/README.md) 之下包括：

- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  ——虚构存储引擎论文开头的 before → after 改写示范。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)——以奖项为锚的
  真实 SIGMOD 论文（Selinger 1979；Online Aggregation，ToT 2007；PrivBayes，
  ToT 2024；k-Shape，ToT 2025；PolarDB-MP，2024 工业轨最佳论文），并记录了若干
  "著名但不属于 SIGMOD"的论文以防误引。
- [`resources/official-source-map.md`](resources/official-source-map.md)——每条事实
  的 URL 与核验日期、访问方式说明、待核实清单。
- [`resources/external_tools.md`](resources/external_tools.md)——官方入口与
  "禁止推断"规则。
- [`resources/code/README.md`](resources/code/README.md)——共享 artifact 冒烟检查
  工具包的数据系统语境适配。

## 快速上手场景

- **"系统已能跑，想投 7 月那一轮。"** 先用 `sigmod-workflow`（倒排计划、带宽
  检查），再用 `sigmod-experiments` 与 `sigmod-reproducibility` 清掉评测债务，
  最后两周进入 `sigmod-submission`。
- **"评审意见到了，有位审稿人读错了图 7。"** 用 `sigmod-author-response` 的
  feedback 模式——用精确指引纠正事实，不做承诺。
- **"拿到带六条要求的 major revision。"** 用 `sigmod-author-response` 的
  revision letter 模式，配合 `sigmod-experiments` 补做实验；先诚实评估一个月
  内能否全部落地。
- **"录用了，接下来？"** `sigmod-camera-ready` 做 PACMMOD 移植与去匿名，然后
  `sigmod-artifact-evaluation` 冲 ARI 徽章。
- **"这到底是不是一篇 SIGMOD 论文？"** 永远先跑 `sigmod-topic-selection`；
  评审阶段一半的痛苦源自路由错误。
- **"第 2 轮被拒了。"** 禁投期封锁研究轨约三轮：用 `sigmod-topic-selection`
  的venue对比表（PVLDB 月度入口、ICDE、TODS），配合 `sigmod-review-process`
  把评审意见转成返工计划。

## 核验快照（2026-07-08）

| 事实 | 数值 | 来源 |
| --- | --- | --- |
| 发表载体 | PACMMOD，每轮一期 | 2027 CFP、PACMMOD 页面 |
| SIGMOD 2027 各轮截稿 | 2026 年 1/17、4/17、7/17、10/17（AoE） | 2027 important dates |
| 页数预算 | 12 页正文 + 参考文献不限页，ACM 模板 | 2027 CFP |
| 平台 | Microsoft CMT | 2027 CFP |
| Revision 条款 | 加 1 页正文、letter ≤4 页、按审稿人分色 | 2027 CFP |
| 被拒禁投期 | 12 个月（逾期撤稿同罚） | 2027 CFP |
| 作者上限 | 每周期 10 篇研究轨投稿 | 2027 CFP |
| ARI 徽章 | Available / Evaluated / Results Reproduced | reproducibility.sigmod.org |
| SIGMOD 2026 | 班加罗尔，2026-05-31 至 06-05 | 2026.sigmod.org |
| SIGMOD 2027 | 亨廷顿海滩，2027-06-13 至 06-19 | 2027.sigmod.org |

## 安装

作为 Claude Code 插件（已含 marketplace 元数据）：

```bash
/plugin marketplace add brycewang-stanford/awesome-journal-skills
/plugin install sigmod-skills
```

或直接复制到项目：

```bash
cp -r SIGMOD-Skills/skills/* your-project/.claude/skills/
```

## 目录结构

```text
SIGMOD-Skills/
├── .claude-plugin/          # plugin.json 与 marketplace.json（注册 12 个 skills）
├── assets/cover.svg
├── resources/
│   ├── README.md
│   ├── official-source-map.md
│   ├── external_tools.md
│   ├── exemplars/library.md
│   ├── worked-examples/01-introduction.md
│   └── code/README.md
└── skills/
    └── sigmod-*/SKILL.md    # 12 个 skills
```

## 事实纪律

本包中每条截止日期、页数与政策陈述只允许两种状态之一：在 2026-07-08 对照具名
官方 URL 核验过，或明确标注"待核实"。构建时已知无法核验的事项——SIGMOD 2027
工业轨日历、当轮 CMT 站点 URL、ARI 2027 后勤安排、PACMMOD 费用机制、正文外
附录是否允许放入 PDF——均列入 source map 的待核实清单，而非猜测填充。

## 维护说明

- 全包引用的 SIGMOD 2027 轮次日历是带日期的观测值；后续周期会重新发布日期，
  只有"每季一轮"的模式可视为相对稳定。
- revision 机制（加页、letter 长度、分色标注规则）、作者投稿上限与禁投期措辞
  每周期重新声明——给出建议前必须重开当期 CFP。
- ARI 每届的注册站点、日期与硬件支持政策逐年变化。
- 官方页面互相矛盾时，以最新表述为准，记录矛盾，并以主席直接沟通为最终依据。
- 更新 exemplars 时遵循 library 的验证协议：奖项引文或 ACM DL 记录、双重独立
  确认，任何不一致即剔除。
