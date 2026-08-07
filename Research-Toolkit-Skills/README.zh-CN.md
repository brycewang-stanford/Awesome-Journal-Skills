# Research-Toolkit-Skills（跨刊科研工作流工具包）

各**单刊深度包**回答"如何达到**这本**期刊的门槛";本包回答跨期刊的共性问题——**投哪本**、如何把分析**做实**、是否**就绪**、审稿人会**攻击什么**、怎么**回应**、以及如何交付**复现包**。

[English](README.md)

## 闭环

```
paper-profile.yml      先把稿子的五个信号写下来一次,下面每一步都读它
rt-journal-match       选刊(索引 743 本刊/会 → reach/match/safe + 改投阶梯)
  → rt-ladder-ev            给阶梯算账:预计月数、最终发出去的概率
  → rt-venue-integrity      索引之外的刊物,投之前逐项核验
  → rt-venue-reframe        改投时把稿子从原刊框架改写到新刊框架
  → rt-execution-bridge     用 StatsPAI / Stata MCP 真跑分析(拟合 + 审计)
  → rt-submission-readiness 对自己的稿件做过审 go/no-go 自检
  → rt-desk-reject-risk     按目标刊自己写明的拒稿触发条件给稿子打分
  → rt-simulated-referee    校准到刊的 AE + 审稿人 panel 预演
  → rt-response-to-referees R&R 后逐条回应信 + 修改计划
  → rt-replication-package  装配并校验 Data-Editor 复现包
rt-workflow            在以上各步之间路由
```

## 技能

| 技能 | 作用 |
|---|---|
| `rt-workflow` | 工具包路由 + 生命周期排序 |
| `rt-journal-match` | 摘要 → 候选刊排序 + 改投阶梯,底层跑 `tools/match_venues.py` |
| `rt-ladder-ev` | 给投稿顺序算账:预计月数、发出去的概率、阶梯走完仍没着落的概率 |
| `rt-venue-integrity` | 索引未覆盖的刊物,按收录、出版方、编委、费用逐项核验来源 |
| `rt-venue-reframe` | A 刊 → B 刊改写清单:贡献陈述、导论结构、证据门槛、体例、政策 |
| `rt-execution-bridge` | 经 MCP 真跑 DiD / IV / RDD / 合成控制 / DML 并审计 |
| `rt-submission-readiness` | 按目标刊门槛对稿件做 go/no-go |
| `rt-desk-reject-risk` | 对照目标刊写明的拒稿触发条件输出分级风险报告 |
| `rt-simulated-referee` | 校准的 AE + 审稿人预演 |
| `rt-response-to-referees` | R&R → 逐条回应 + 修改计划 |
| `rt-replication-package` | 装配并校验 Data-Editor 复现包 |

## 设计

- **不绑定单刊**:工具包负责选刊、跑分析、预演评审;**门槛与一切易变事实**(费用、字数、接收率、数据政策、体例)来自所选包的 skill 与 `resources/official-source-map.md`。
- **由 [`shared-resources/`](../shared-resources/) 的 canonical 能力文档支撑**(`journal-selection/`、`empirical-methods/`、`submission-readiness/`):skill 是可触发入口,深度方法论与五大设计族(DiD/IV/RDD/合成控制/DML,全部真跑)的 worked-example 集中存放在那里。
- **测过才敢说**:选刊检索跑的是 `tools/match_venues.py`,**评测打的就是同一段代码**——1738 篇论文的 gold set 切成调参一半、报数一半,只给标题时 R@10 = 40.5%,给对学科 51.3%([`eval/`](../shared-resources/journal-selection/eval/README.md))。检索只给出"该读哪几本",推荐仍要打开每本刊自己的 pack。
- **画像写一次**:关于稿子的五个信号写成 [`paper-profile.yml`](../shared-resources/journal-selection/paper-profile.md),不再由每个 skill 各自从正文重新推断、彼此打架。
- **跑了才报**:实证步骤经 StatsPAI / Stata MCP 工具执行并报真实数字;引用只走 `bibtex`。

## 安装

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install research-toolkit-skills
/reload-plugins
```
