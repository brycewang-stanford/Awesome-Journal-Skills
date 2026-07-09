# AAMAS Skills

面向 **AAMAS**（International Conference on Autonomous Agents and Multiagent Systems，自主智能体
与多智能体系统国际会议）论文的 12 个 agent skills。AAMAS 是国际自主智能体与多智能体系统基金会
（IFAAMAS）的旗舰会议。本包聚焦 AAMAS 投稿中真正奖励 **交互（interaction）** 研究的环节：AAMAS
与 AI 会议之间的选会路由、OpenReview 投稿准备、8 页正文加不限页数参考文献的主赛道、double-blind
rebuttal、IFAAMAS 开放获取的 camera-ready、多智能体可复现性，以及 AAMAS 独特的赛道菜单
（main、AAAI、JAAMAS、Blue Sky Ideas、Demo、Competitions）。

官方依据核验日期：**2026-07-09**。已核验 AAMAS 2026 主赛道 Call for Papers、submission
instructions 与 important dates 页面；AAMAS 2026 与 AAMAS 2027 的 OpenReview conference group；
IFAAMAS 基金会与 proceedings；JAAMAS 期刊；以及 dblp `conf/atal` proceedings 索引。精确来源见
[`resources/official-source-map.md`](resources/official-source-map.md)，其中包含对屏蔽自动抓取的
主办页面的访问方式说明。

## AAMAS 有何不同

AAMAS 不是通用 AI 会议，也不是单智能体机器学习会议。它的审稿人关心的是贡献是否真正关于 **智能体之间
的交互**：博弈论推理、多智能体强化学习、机制设计与拍卖、协商与论辩、协调与团队合作、基于智能体的仿真、
社会选择。只有当结果 **因为存在多个自利或协作的智能体** 才成立时，才算契合；一个强的单智能体方法贴上
多智能体标签，是典型的需要改投的情形。本包把这种路由（AAMAS 与 AAAI / IJCAI / NeurIPS / ICML 的
取舍）作为一等决策来处理。

三个结构性事实贯穿全包，均按 2026 周期核验：

- **格式。** 主赛道论文正文至多 **8 页，外加不限页数的参考文献**，可作为 **full paper** 或 **2 页
  extended abstract** 提交。Blue Sky 论文含参考文献至多 4 页。
- **评审。** AAMAS 采用 **double-blind**，在 `ifaamas.org` 命名空间下的 **OpenReview** 上运行，
  并对初步评审设有 **rebuttal** 窗口。录用论文 *及其评审* 在 OpenReview 上公开，论文由 **IFAAMAS
  开放获取出版**。
- **赛道。** 除主赛道外，AAMAS 设有 **AAAI Track**（从 AAAI 快速转投，附对 AAAI 评审的回应）、
  **JAAMAS Track**（近期已发表 JAAMAS 期刊论文的口头报告）、**Blue Sky Ideas**、**Demo** 与
  **Competitions** 赛道，各自有独立的截止日期与规则。

## 赛道地图（AAMAS 2026，每周期需重新核验）

| 赛道 | 用途 | 格式信号 | 核验来源 |
| --- | --- | --- | --- |
| Main Technical Track | 原创智能体/多智能体研究 | 8 页 + 参考（full）或 2 页 + 参考（extended abstract） | CFP + submission instructions |
| AAAI Track | 承接强的 AAAI 投稿 | 主赛道格式 + ≤2 页对 AAAI 评审的回应，改动高亮 | AAAI Track CFP |
| JAAMAS Track | 展示近期 JAAMAS 期刊论文 | 期刊论文的 2 页 extended abstract | JAAMAS Track CFP |
| Blue Sky Ideas | 前瞻性、设定议程的观点 | 含参考文献 ≤4 页 | Blue Sky CFP |
| Demo Track | 现场/交互式智能体系统 | 短论文 + demo | Demo CFP |
| Competitions Track | 基准与智能体竞赛 | 竞赛提案 | Competitions CFP |

## Skills

- `aamas-topic-selection`：判断项目是否 AAMAS 型（智能体是研究对象），还是更适合 AAAI、IJCAI、
  NeurIPS、ICML、EC 或 JAAMAS 等期刊。
- `aamas-submission`：核查 OpenReview 准备、8 页加参考限制、full 与 extended-abstract 的选择、
  double-blind 匿名、supplement zip、赛道契合与 desk-reject 触发点。
- `aamas-author-response`：撰写聚焦、匿名的 rebuttal，回应初步评审，不放新结果、不泄露身份，也不
  依赖流程不允许的改稿上传。
- `aamas-camera-ready`：准备 IFAAMAS 开放获取的 camera-ready、去匿名、proceedings 元数据、注册
  与现场报告。
- `aamas-artifact-evaluation`：把多智能体代码、环境、对手/种群集合、随机种子与日志打包成匿名补充
  证据或录用后的公开发布。
- `aamas-reproducibility`：强化交互性主张的证据映射：证明、对手集合、种子、self-play 协议、算力，
  以及对策略性结果的不确定性。
- `aamas-supplementary`：组织证明、扩展的博弈定义、额外多智能体实验，以及在大小上限内的匿名
  artifact zip。
- `aamas-review-process`：理解 OpenReview 评审、rebuttal、area chair 讨论、公开评审，以及博弈论
  /MARL/系统混合的审稿人群体。
- `aamas-writing-style`：修订出交互优先的首页、命名清晰的 solution concept、8 页压缩与
  double-blind 措辞。
- `aamas-related-work`：在 AAMAS、AAAI、IJCAI、NeurIPS、ICML、EC 的多智能体、博弈论与 RL 文献中
  定位，并处理并行与先前版本。
- `aamas-experiments`：审查 self-play、基于种群与博弈论实验、对手选择、均衡/regret 指标、种子、
  ablation 与主张到证据的对应。
- `aamas-workflow`：从选会到摘要、正文、supplement、rebuttal、决定、camera-ready 与报告做项目
  管理，兼顾各赛道截止日期。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md)：核验过的事实锚点，含
  URL、访问日期、403 访问方式说明与 待核实 清单。
- [`resources/external_tools.md`](resources/external_tools.md)：官方 IFAAMAS/AAMAS CFP、投稿、
  OpenReview、JAAMAS 与 proceedings 链接。
- [`resources/exemplars/library.md`](resources/exemplars/library.md)：五篇 dblp 核验的 AAMAS
  论文，覆盖 MARL、security games、negotiation 与多智能体学习，并附姊妹会议的排除清单。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)：
  一个虚构的 AAMAS 摘要/引言 before-to-after 改写。
- [`resources/code/README.md`](resources/code/README.md)：面向多智能体实验的共享 ML 会议可复现性
  工具适配。

## 使用方式

1. **先路由。** 用 `aamas-topic-selection` 确认交互性主张成立，再用 `aamas-writing-style` 把它
   放到首页。
2. **建证据。** 用 `aamas-experiments` 与 `aamas-reproducibility` 配合共享代码工具，让 self-play
   与博弈论结果站得住。
3. **干净投稿。** 对照当年 CFP 用 `aamas-submission` 与 `aamas-supplementary`，然后在 rebuttal
   窗口用 `aamas-review-process` 与 `aamas-author-response`。
4. **收尾。** 用 `aamas-camera-ready` 出 IFAAMAS 开放获取版本，用 `aamas-workflow` 盯住每个赛道
   截止日期。

## 核验事实锚点（核验于 2026-07-09）

以下均为 AAMAS 2026 周期的历史锚点，不是永久规则。每一条都在
[`resources/official-source-map.md`](resources/official-source-map.md) 中标注来源；涉及 deadline
前请重新核验。

- AAMAS 2026 为 **第 25 届**，于 **2026 年 5 月 25-29 日** 在 **塞浦路斯帕福斯**（Coral Beach
  Hotel & Resort）举办，由 IFAAMAS 组织。
- 主赛道时间线：摘要 **2025 年 10 月 1 日**，论文 **2025 年 10 月 8 日**，rebuttal
  **2025 年 11 月 21-25 日**，camera-ready **2026 年 2 月 11 日**（均为 AoE）。
- 赛道截止不同：**AAAI Track 为 2025 年 11 月 17 日**；**JAAMAS Track 为 2026 年 1 月 6 日**。
- 主赛道论文：**正文至多 8 页加不限页数参考文献**；full paper 或 2 页 extended abstract；Blue Sky
  含参考文献至多 4 页。
- 评审为 **double-blind**，在 **OpenReview**（`ifaamas.org/AAMAS/2026/Conference`）上进行；评审
  与决定会公开；论文经 IFAAMAS 开放获取。
- 补充材料：单个 zip，**不超过 25 MB**。
- 下一周期 **AAMAS 2027（第 26 届）** 的 OpenReview group 已存在
  （`ifaamas.org/AAMAS/2027/Conference`）；但截至 2026-07-09，其主办城市、日期与截止日期尚无法干净
  确认（待核实）。

## 何时 AAMAS 不是合适的归宿

`aamas-topic-selection` skill 编码的最常见改投：

- 在多智能体环境中做基准测试的强 **单智能体** 方法 → NeurIPS 或 ICML。
- 中心不在交互的广义 **AI 推理、规划或知识表示** → AAAI 或 IJCAI。
- 以经济学为要点的 **市场设计、拍卖理论或均衡计算** → EC（Economics and Computation）。
- 需要 **期刊长度存档处理** 的工作 → JAAMAS 期刊（或其 AAMAS 报告赛道）。

用 frozen-agent 测试：若把其他智能体换成静态环境后结果仍然成立，则贡献是单智能体的，应投他处。

## 维护说明

- 涉及 deadline 的建议前，必须重新打开当年官方来源；AAMAS 每年轮换主办方，主办页面可能屏蔽自动抓取
  （用 IFAAMAS、OpenReview、ACM DL 与 dblp 交叉核对）。
- 把 AAMAS 2026 事实当作历史锚点。截至 2026-07-09，live 目标是 **AAMAS 2027**（第 26 届）；其
  OpenReview group 已存在，但主办城市、日期、截止日期与赛道清单尚无法干净确认——见来源图中的 待核实
  清单。
- 页数限制、extended-abstract 选项、rebuttal 机制、supplement 大小上限、赛道截止日期、proceedings
  模板、注册与报告义务都可能逐年变化。
