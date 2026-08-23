# QUALITY-LANE-2026-09 — 静态尺子饱和后的质量牵引方案

**背景（2026-07-08）**：`tools/quality_scorecard.py` 已全仓饱和——199 个 pack
min = mean = max = 94.0（公式构造性上限 35+20+28+5+6）。静态尺子从此失去
区分度，不能再作为"提升目标"；它的新角色是**回归防线**。

## 已落地（2026-07-08）

- `tools/run_checks.py` 硬门槛的 scorecard 下限由 90 提升到 **94**：任何
  pack 跌破公式满分即 CI 红灯。配套更新 `CONTRIBUTING.md` 最小验收线第 7 条
  （新 pack 必须建满 94.0 再开 PR）。

## 一个重要的更正（诚实纪律）

ROADMAP-2026-08 与 ACCEPTANCE-2026-08 §3.3 曾建议「下月转向 `tools/skillopt/`
的 rollout→judge→validation-gate 行为评测路线」。**该建议基于过时信息，予以
撤回**：查证 git 历史发现 owner 已于 2026-06-29（commit `b9c8fe75`）**刻意
拆除**了整套 SkillOpt / monthly-uplift 装置——原因是它长成了 7,400 行仪表盘 +
646KB worklog 的自引用循环，其 `--check-worklog/--check-only` 门把活动工作区
状态卷进硬检查，反复与人工提交竞态、在干净 checkout 上打破 CI。任何后续质量
方案都不得重建这类**自动提交、自我度量、常驻 CI 的评测装置**。

## 2026-09 质量牵引方案（轻量、人触发、不进 CI）

静态分饱和后，质量的真实敞口只剩两类，各配一个轻量流程：

### 1. 事实新鲜度（最大敞口）

skill 的价值随各 venue 换届/换政策而衰减。方案：**周期滚动复核**，人触发、
按批次、只动 source map 与受影响的 skill 段落。

- 触发点：各会议新一届 CFP 发布（CS/AI 包）、期刊年度换届（econ/管理包）。
  `.maintenance/` 不新增常驻看板；每次复核直接在 ROADMAP-当月 文件记一行。
- 通道纪律：官方页直连优先；本环境网关封锁时用「搜索渲染 + access-method
  note」的既有先例（见 UAI/COLT/MLSys/KDD source map），钉不住的落 待核实。
- 优先队列（按用户量与易变度）：CS/AI 会议包（一年一换全量过期）>
  英文旗舰 econ/finance（编辑与费用年度漂移）> 中文包（官网不可达，攒批处理）。

### 2. 行为质量（谨慎、人工、小样本）

不重建 harness。改为**人工触发的抽样行为评测**：维护者选 1-2 个 pack，把其
skill 装入真实 Claude Code 会话跑典型投稿任务，人工判断输出是否用上了 venue
事实、是否给出错误建议，把发现直接修进 SKILL.md（普通 PR，全套硬检查）。
不留脚本、不留 worklog、不进 CI——评测是手段，修复才是产出。

## 明确不做

- 不重建 `tools/skillopt*`、monthly-uplift 仪表盘或任何 auto-commit 循环。
- 不给静态 scorecard 加新维度来"制造提升空间"——防线角色不需要区分度。
- 不把行为评测接入 run_checks（网络依赖 + 模型不确定性 = CI 噪声源）。

## 修订（2026-08-23）：「不给静态 scorecard 加新维度」一条已被取代

上面「明确不做」的第二条——*不给静态 scorecard 加新维度来"制造提升空间"*
——本文件写下后不到一个月就已经被实践推翻了两次，现予以正式修订。记录经过，
以免下一个人把它当成仍然有效的约束、或者反过来以为可以随意加维度。

**它是怎么失效的。** 2026-08-09 的 `609eeb78` 给 scorecard 加了 evidence 维度
（source-map 新鲜度 + 待核实计数，0–6 分），代码注释写明理由：*"The previous
formula topped out at 94, causing every conforming pack to receive the same
nominal 94/100 and hiding the maintenance backlog."* 这正是本文件禁止的动作，
而且理由跟本文件自己认定的「最大敞口 = 事实新鲜度」是同一件事。到 2026-08-23，
新加的这一维也饱和了：299 个 pack 里 6 个维度有 5 个满分，分数在算术上等于
`94 + freshness(0-6)`，均值 99.2、最低 98.5，`--min-score 94` 成了一道永远不会
亮红灯的门。

**现在的形状。** 把两件事拆开，而不是继续往一个数里塞维度：

- **conformance（通过/不通过）** —— 这才是本文件想要的那道**回归防线**。它
  就是原来那 94 分的全部内容，只是不再伪装成分数：缺哪一项就说缺哪一项。
  `run_checks.py` 用 `--require-conformance` 硬门槛跑它，299/299 全过。
- **backlog score（0–100，只排序，不设标准）** —— 只用**还有区分度**的信号：
  source-map 时效、待核实负债、pack 里**最薄**那个 skill 的厚度、它与该 pack
  自身均值的落差、以及有 code library 的包的 execution-bridge 接线率。其中
  55 分落在 currency + verified 上，也就是本文件自己点名的第一敞口。

**保留下来的约束**（这几条没有被修订，仍然有效）：

- 不重建 `tools/skillopt*`、monthly-uplift 仪表盘或任何 **auto-commit 自度量**
  循环。scorecard 是只读的、离线的、确定性的，不写任何工作区状态。
- 不把行为评测接入 `run_checks`。
- backlog score **不是目标**。CI 里的 `--min-score 40` 远低于当前最低分
  （51.5），只是防止一个坏掉的新 pack 混进来的绊线，不是可以优化的指标；
  排序的用途是告诉维护者先修哪个包。

**下次别再手动发现这件事。** scorecard 现在会在表格末尾打印自己每个维度的
饱和度。某一行到 299/299 就说明它已经不再区分任何东西，应当移进 conformance。
写下这条的原因是：前两次饱和都是靠人偶然注意到均值很漂亮才发现的，中间各隔了
一个多月，而在那期间「质量分 99.2/100」这句话一直在对所有人说一切都很好。
