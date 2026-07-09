# ACM SIGMETRICS Skills

面向 **ACM SIGMETRICS —— ACM SIGMETRICS International Conference on Measurement and Modeling of
Computer Systems** 论文的 12 个 agent skills。SIGMETRICS 是计算机系统**性能测量、建模与评估**领域
的旗舰会议。本包覆盖一次 SIGMETRICS 投稿的完整流程：判断项目属于 SIGMETRICS 还是应投 IMC、
SIGCOMM/NSDI/OSDI、机器学习会议或性能期刊；构建把**性能上界证明**与**验证/测量**配对的证据；准备
double-anonymous 的 `acmsmall` 投稿并选择**三个滚动截止日**之一；应对 **POMACS** 的
**hybrid 会议-期刊评审**及其 **one-shot revision** 与强制 shepherding；直到完成 POMACS camera-ready
与获得 ACM artifact 徽章。

官方依据核验日期：**2026-07-09**。已核验 SIGMETRICS 2026 与 2027 的 call 与 Important Dates、POMACS
期刊页面、各截止日的 SIGMETRICS HotCRP 站点、ACM Artifact Review and Badging 政策，以及 SIGMETRICS
奖项页面。核验环境中直接抓取 `sigmetrics.org`、`dl.acm.org` 及 `*.hotcrp.com` 返回 403（对 2027
summer HotCRP 的 WebFetch 返回 403 Forbidden），因此通过搜索引擎对精确 URL 的渲染阅读官方页面，并与
ACM Digital Library（POMACS）、dblp、SIGARCH call-for-contributions 及 OpenAccept 统计交叉核对；完整
记录（含所有 待核实 项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> 缩写冲突提醒：SIGMETRICS **不是** IMC（ACM Internet Measurement Conference，纯网络测量），**不是**
> SIGCOMM/NSDI（网络系统），也**不是** SIGMOD（数据库）。本包中的事实均不来自这些会议。

## SIGMETRICS 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 IMC、系统会议或纯
学习会议转投作者最常犯的错误：

- **论文即期刊文章，且为滚动投稿。** SIGMETRICS research paper 发表在 **POMACS（Proceedings of the
  ACM on Measurement and Analysis of Computing Systems）**，一本 open-access 的 ACM 期刊，通过**每年
  三个截止日 —— summer、fall、winter** 投稿。没有单一年度截止日；按 POMACS 出版时间选择 cycle。
- **hybrid 会议-期刊评审，含 one-shot revision。** 首轮决定为 **Accept**（每篇录用论文都会
  **shepherding**）、**One-Shot Revision**（major revision：把修订稿重投到后两个截止日之一，针对一份
  明确的必改清单**仅复审一次**）或 **Reject**（12 个月内不得再投 SIGMETRICS）。该修订是真正的
  **单次机会**，而非期刊式无限返修。
- **严谨文化：性能上界证明。** SIGMETRICS 论文带**定理** —— 尾延迟上界、稳定性条件、regret 速率 ——
  并通过数值或实证验证。审稿人核查证明与假设，而不只看图。这与纯测量的 IMC 或系统建设型的
  SIGCOMM/NSDI 不同。
- **理论 + 测量 + 学习的融合。** track 包括 **Theory**、**Measurement & Applied Modeling**、
  **Learning** 以及新设的 **Operational Systems Track**，体现一个既看重随机建模、又看重真实测量的
  社区，二者常并存于一篇论文。
- **ACM `acmsmall` 期刊模板。** SIGMETRICS 2026 规定正文（单栏，含表与图）**至多 20 页 + 参考文献
  不限页数** —— 不是双栏会议框。
- **double-anonymous 评审，唯一例外。** 全程匿名，唯 **Operational Systems Track** 可披露部署机构
  或部署系统。
- **默认可复现。** 带种子的模拟器能重生成图并与分析吻合、钉死的测量 provenance，以及 ACM 徽章
  （Available / Functional / Reusable / Reproduced），是社区期望。

## Skills

| Skill | 作用 |
| --- | --- |
| [`sigmetrics-topic-selection`](skills/sigmetrics-topic-selection/SKILL.md) | 在 SIGMETRICS 与同类（IMC、SIGCOMM/NSDI/OSDI、NeurIPS/ICML、Performance Evaluation/TON/QUESTA）之间选路，用 rigor 测试并选定 track。 |
| [`sigmetrics-workflow`](skills/sigmetrics-workflow/SKILL.md) | 跨三个滚动截止日排期，经注册、shepherding、one-shot revision、POMACS 出版与报告。 |
| [`sigmetrics-writing-style`](skills/sigmetrics-writing-style/SKILL.md) | 构建性能评估骨架：首页给出贡献、明示假设、定理配验证、20 页纪律。 |
| [`sigmetrics-related-work`](skills/sigmetrics-related-work/SKILL.md) | 覆盖性能评估 lane，写 delta-first 定位（更紧上界/更弱假设/更新数据），保持自引匿名。 |
| [`sigmetrics-experiments`](skills/sigmetrics-experiments/SKILL.md) | 让证据匹配论断：证明、分析与模拟吻合、真实 trace、公平 baseline、置信区间、学习保证、测量 provenance。 |
| [`sigmetrics-reproducibility`](skills/sigmetrics-reproducibility/SKILL.md) | 把证明与带种子模拟器当作 artifact：重生成图、匹配分析、钉死 trace provenance、诚实标注复现级别。 |
| [`sigmetrics-supplementary`](skills/sigmetrics-supplementary/SKILL.md) | 按决策重要性划分 —— 定理陈述、假设与主验证留在正文；完整证明入附录。 |
| [`sigmetrics-submission`](skills/sigmetrics-submission/SKILL.md) | HotCRP 终审：选截止日、注册 abstract + track、acmsmall 篇幅、匿名清扫、desk-reject 分诊。 |
| [`sigmetrics-review-process`](skills/sigmetrics-review-process/SKILL.md) | 建模流程 —— double-anonymous、三种结果、one-shot revision 重投后续截止日、12 个月禁投 —— 及作者杠杆点。 |
| [`sigmetrics-author-response`](skills/sigmetrics-author-response/SKILL.md) | 撰写 one-shot revision 回复信，在单次复审中关闭审稿人必改清单的每一项。 |
| [`sigmetrics-artifact-evaluation`](skills/sigmetrics-artifact-evaluation/SKILL.md) | 把包转化为 ACM 徽章（Available / Functional / Reusable / Reproduced）—— 图须能重生成并与分析吻合。 |
| [`sigmetrics-camera-ready`](skills/sigmetrics-camera-ready/SKILL.md) | 去匿名、纳入 shepherd 必改项、补全 POMACS 元数据、永久化 artifact、通过 ACM 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十一个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口（各截止日 HotCRP、POMACS、ACM badging）与网关阻断时的交叉核对来源。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 四篇经存档核验的 SIGMETRICS 论文，覆盖三种文化 —— 排队论、测量、带保证的学习，附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构调度研究的摘要与引言按 SIGMETRICS 弧线（定理 + 验证）重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 SIGMETRICS 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./SIGMETRICS-Skills
claude plugin install sigmetrics-skills
```

也可直接使用文件：每个 `skills/sigmetrics-*/SKILL.md` 都是独立指令文件，其 frontmatter
`description` 告诉 agent 何时触发。典型调用：

- “这篇该投 SIGMETRICS 还是 IMC/NSDI？” → `sigmetrics-topic-selection`
- “该投哪个滚动截止日，并审我的稿” → `sigmetrics-submission`
- “拿到 One-Shot Revision —— 规划回复信” → `sigmetrics-author-response`
- “把模拟器/artifact 准备到 ACM 徽章标准” → `sigmetrics-artifact-evaluation`

## 目录结构

```text
SIGMETRICS-Skills/
├── .claude-plugin/                  # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                        # 英文说明
├── README.zh-CN.md                  # 本文件
├── LICENSE                          # MIT
├── assets/cover.svg                 # 封面
├── skills/
│   └── sigmetrics-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `sigmetrics-topic-selection`；rigor 关卡（是否有定理、验证过的模型或有原则的
   测量？）与 track 选择决定审稿群体。浏览 exemplars 看有持久影响力的 SIGMETRICS 贡献长什么样。
2. **构建证据时** —— 让 `sigmetrics-experiments` 与 `sigmetrics-reproducibility` 贴着研究；设计期
   明示的假设与运行期记录的种子无法事后补救。
3. **写作时** —— 用 `sigmetrics-writing-style` 对照 worked example 打磨正文，用
   `sigmetrics-supplementary` 划分正文/附录/artifact，用 `sigmetrics-related-work` 做 delta-first
   定位。
4. **截止周** —— 先在较早的注册截止日前完成 abstract 与 track 注册，再用 `sigmetrics-submission`
   对终稿 PDF 与 artifact 逐项过审。
5. **投稿后** —— 用 `sigmetrics-review-process` 校准预期，用 `sigmetrics-author-response` 应对
   one-shot revision，随后 `sigmetrics-artifact-evaluation` 与 `sigmetrics-camera-ready` —— 若结果
   不利，则用 `sigmetrics-topic-selection` 的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- SIGMETRICS 2026 为**第 52 届**：美国密歇根大学安娜堡（Michigan Union），**2026 年 6 月 8-12 日**。
  三个截止日：Summer（投稿 2025-07-29）、Fall（投稿 2025-10-14）、Winter（投稿 2026-01-13），均
  23:59 AoE。
- SIGMETRICS 2027 在**美国佐治亚州亚特兰大，2027 年 6 月 7-11 日**；summer 轮 abstract 注册为
  **2026-07-03** —— 2026-07-09 时的下一个 live 目标（summer 投稿日 待核实；winter 转述为投稿
  2027-01-11 / 通知 2027-03-10）。
- 出版：**POMACS**，open access，无 APC。评审：**double-anonymous**，hybrid 会议-期刊。决定：
  Accept（shepherded）/ **One-Shot Revision** / Reject。模板：ACM **acmsmall**，正文 ≤20 页 +
  参考文献不限。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如三个滚动截止日、
   20 页 acmsmall 篇幅、one-shot-revision 规则）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如转述的 2027 winter 日期、历史录用率）。
3. **核验期不可确定项** —— 明确标为 待核实（如 2027 summer 投稿确切日、完整 track 数、本届是否设
   artifact track、奖项确切名称）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。SIGMETRICS 每届重定三个截止日、篇幅、track 列表与是否设 artifact
  track —— 每年先核验。
- SIGMETRICS 采**每届轮换的 General 与 Program Chairs**、**无 APC**；POMACS open access。即便
  **出版物**是期刊，也不要对**人**做期刊式连续性假设。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 熟悉的性能
  评估工具名并不能证明该论文发表于 SIGMETRICS（可能是 IMC、SIGCOMM、NSDI 或 NeurIPS）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
