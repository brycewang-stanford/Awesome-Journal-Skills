# Research-Toolkit-Skills（跨刊科研工作流工具包）

各**单刊深度包**回答"如何达到**这本**期刊的门槛";本包回答跨期刊的共性问题——**投哪本**、如何把分析**做实**、是否**就绪**、审稿人会**攻击什么**、怎么**回应**、以及如何交付**复现包**。

[English](README.md)

## 闭环

```
paper-profile.yml      先把稿子的五个信号写下来一次,下面每一步都读它
rt-journal-match       选刊(索引 744 本刊/会 → reach/match/safe + 改投阶梯)
  → rt-ladder-ev            给阶梯算账:预计月数、最终发出去的概率
  → rt-venue-integrity      索引之外的刊物,投之前逐项核验
  → rt-venue-reframe        改投时把稿子从原刊框架改写到新刊框架
  → rt-execution-bridge     用 StatsPAI / Stata MCP 真跑分析(拟合 + 审计)
  → rt-submission-readiness 在真实稿件文件上跑投稿前全流程:
                            预检 → 打分卡 → 审稿模拟 → 润色 → 投稿信 → 复检
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
| `rt-submission-readiness` | 投稿前全流程:按目标刊已核实规则做确定性预检、九维打分卡、审稿模拟、论断—证据润色、投稿信与声明、修改后复检 |
| `rt-desk-reject-risk` | 对照目标刊写明的拒稿触发条件输出分级风险报告 |
| `rt-simulated-referee` | 校准的 AE + 审稿人预演 |
| `rt-response-to-referees` | R&R → 逐条回应 + 修改计划 |
| `rt-replication-package` | 装配并校验 Data-Editor 复现包 |

## 投稿前打磨(rt-submission-readiness)

本包的旗舰流程。给出稿件文件和目标刊/会即可:

```bash
python3 resources/preflight/preflight.py paper.pdf --venue "Journal of Finance"   # 已安装本包
python3 tools/preflight.py paper.tex --venue icml --json                           # 仓库克隆内
python3 resources/preflight/preflight.py --list-venues                             # 已有机读规则的 venue
```

第 0 步是确定性检查:摘要/字数/页数上限,双盲匿名(作者信息、自我引用、致谢、非匿名代码链接、文件元数据),目标刊要求的全部声明,正文引用与参考文献一一对应(可选 Crossref 在线核验),图表编号、交叉引用与标准误注释,摘要数字能否在表格中找到,残留的 TODO 与修订痕迹。各刊上限来自每个 pack `official-source-map.md` 里的机读规则块——对照官方页面重新核实,并由 CI 保证与正文一致。之后依次做九维打分卡、按该刊审稿表格式的审稿模拟、论断—证据润色、按政策生成投稿信和声明,作者修改后再复检。效果用"植入缺陷"基准测量,见 [`showcase/presubmission-benchmark/`](https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/showcase/presubmission-benchmark/README.md)。

## 设计

- **不绑定单刊**:工具包负责选刊、跑分析、预演评审;**门槛与一切易变事实**(费用、字数、接收率、数据政策、体例)来自所选包的 skill 与 `resources/official-source-map.md`。
- **由 `shared-resources/` 的 canonical 能力文档支撑**(已同步复制到本包 [`resources/shared/`](resources/shared/),插件安装后链接仍有效)(`journal-selection/`、`empirical-methods/`、`submission-readiness/`):skill 是可触发入口,深度方法论与五大设计族(DiD/IV/RDD/合成控制/DML,全部真跑)的 worked-example 集中存放在那里。
- **测过才敢说**:选刊检索跑的是 `tools/match_venues.py`,**评测打的就是同一段代码**——gold set 切成调参一半、报数一半,在报数一半上只给标题时 R@10 = 65.7%,给对学科 77.7%(2026-11-23)([`eval/`](resources/shared/journal-selection/eval/README.md))。检索只给出"该读哪几本",推荐仍要打开每本刊自己的 pack。
- **画像写一次**:关于稿子的五个信号写成 [`paper-profile.yml`](resources/shared/journal-selection/paper-profile.md),不再由每个 skill 各自从正文重新推断、彼此打架。
- **跑了才报**:实证步骤经 StatsPAI / Stata MCP 工具执行并报真实数字;引用只走 `bibtex`。

## 安装

```bash
/plugin marketplace add https://github.com/brycewang-stanford/awesome-journal-skills
/plugin install research-toolkit-skills
/reload-plugins
```
