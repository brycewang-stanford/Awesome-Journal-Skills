# CoRL Skills（中文说明）

面向 **CoRL（Conference on Robot Learning，机器人学习会议）** 投稿的 12 个
agent skills。CoRL 创办于 2017 年（首届在 Mountain View，论文集为 PMLR v78），
由 Robot Learning Foundation 运营，是"machine learning 驱动机器人能力"这一交叉
方向的核心年会：imitation learning 与 RL 上真机、sim-to-real 迁移、以及
vision-language-action（VLA）基础模型浪潮的大本营。与机器人领域的巨型会议相比，
它规模小、录用严，社区就是 robot-learning 研究者本身。

官方依据核验日期：**2026-07-08**。已核验 CoRL 2026 年度站点（Austin）、Call for
Papers、Instruction for Authors、rebuttal 与 reviewer 指南、CoRL 2026 OpenReview
group，以及 PMLR v78–v305 各卷页面。核验环境中直接抓取 `corl.org` 返回 403，
因此官方页面通过搜索引擎对确切 URL 的渲染读取，并与 OpenReview、PMLR 卷页面、
组织者公开声明交叉核对；完整证据链与全部 待核实 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 2026 周期当前所处的阶段

本包按 2026-07-08 的真实日历状态编写：

- CoRL 2026 投稿截止**已过**（摘要 5 月 26 日、正文 5 月 29 日）。
- 已投稿件正处于**审稿期**；评审意见预计 8 月初释出，**一页 PDF rebuttal**
  截止 **2026 年 8 月 11 日（AoE）**，reviewer–AC 讨论期为 **8 月 12–19 日**。
- 录用决定预计 9 月（确切日期 待核实），camera-ready 截止 **10 月 12 日**，
  会议 **11 月 9–12 日**在德州 Austin 的 JW Marriott 举行（9 日为 workshop 日），
  是该系列的第 10 届。
- 新项目应面向 **CoRL 2027** 规划（年度站点尚未核验到）；选会与流程两个 skill
  对这条分支有明确覆盖。

## CoRL 与相邻 venue 的关键差异

- **交叉点即身份。** 论文必须同时过两道门槛：learning 是贡献本身，且主张
  必须依赖具身实验。缺第一条应去 ICRA/IROS/RSS，缺第二条应去
  NeurIPS/ICLR/ICML。选会 skill 把这变成可执行的判定。
- **强制且计页的 Limitations 章节。** 2026 规则要求它写进 8 页正文之内——
  失败模式是被评审的论证的一部分，不是附录里的客套。
- **一页 PDF rebuttal，且前面有一道闸门。** 没有任何 reviewer 或 AC 给出
  weak accept 及以上分数的论文，可能在第一轮**无 rebuttal**直接被拒；过了
  闸门的论文，作者的全部话语权就是评审后数天内的那一页。
- **录用论文的评审公开。** rebuttal 往来会成为论文永久公开记录的一部分。
- **视频是证据，但 PMLR 不收。** 审稿期强烈鼓励提交总览视频（≤ 250 MB、
  约 3 分钟）；而 PMLR 论文集不接受视频，录用后必须在外部站点承载视频与
  artifact，并在正文给出链接。
- **evaluation-episode 文化。** seeds × episodes × 任务广度、量化的
  sim-to-real 差距、BC/RL/VLA 各家族基线的公平比较，是这批 reviewer 的
  条件反射式检查。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`corl-topic-selection`](skills/corl-topic-selection/SKILL.md) | 双轴判定（learning 是否为贡献 / 主张是否需要具身），在 CoRL、ICRA/IROS、RSS 与 ML 会议之间选路。 |
| [`corl-workflow`](skills/corl-workflow/SKILL.md) | 管理一年一次的周期：5 月截稿、把暑期安静期用于 rebuttal 备弹、8 月硬仗、秋季决定、11 月 Austin。 |
| [`corl-submission`](skills/corl-submission/SKILL.md) | OpenReview 投稿终审：corl_2026 模板、含 Limitations 的 8 页、视频上限、项目页与真机画面的匿名清查、GenAI 政策核对。 |
| [`corl-review-process`](skills/corl-review-process/SKILL.md) | 建模 reviewer → AC → SAC → PC 会议的层级、以 weak accept 为录用门槛的 rubric、第一轮拒稿闸门与录用后评审公开。 |
| [`corl-author-response`](skills/corl-author-response/SKILL.md) | 写好那一页 PDF：先找"辩护人"的分诊、按预期分数收益分配版面、紧凑的新证据表格、面向公开记录的语气。 |
| [`corl-camera-ready`](skills/corl-camera-ready/SKILL.md) | 把第 9 页花在兑现评审承诺上，切换 final 模板、合并附录，并搭好 PMLR 无法承载的外部视频/代码门面。 |
| [`corl-artifact-evaluation`](skills/corl-artifact-evaluation/SKILL.md) | 按声明的 release 层级打包代码、数据、checkpoint 与 benchmark：审稿期匿名，录用后可长期存续。 |
| [`corl-reproducibility`](skills/corl-reproducibility/SKILL.md) | 把可重跑的一半（仿真/训练）与可稽核的一半（硬件）分开：版本锁定、manifest、逐 episode 日志、诚实的可用性声明。 |
| [`corl-supplementary`](skills/corl-supplementary/SKILL.md) | 在附录 / 补充上传 / 外部托管三个通道间放置内容；让视频成为证据——不剪辑的完整执行、标注倍速、展示失败。 |
| [`corl-writing-style`](skills/corl-writing-style/SKILL.md) | 同时服务 ML 与 robotics 两类读者：第一页契约、带规模标注的克制表述、把 Limitations 写成加分项。 |
| [`corl-related-work`](skills/corl-related-work/SKILL.md) | 覆盖三条文献带加上 VLA 浪潮与 concurrent arXiv；PMLR 引用卫生，包括会议年份与出版年份错位的陷阱。 |
| [`corl-experiments`](skills/corl-experiments/SKILL.md) | 设计双层随机性协议（训练 seeds × 评测 episodes）、泛化划分、跨家族公平基线与量化迁移差距。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 10 个官方来源（URL + 访问日期）、访问方式说明、已核验/转述事实分级与 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及每个周期都要跑的五道作者侧核验。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 6 篇经 PMLR 核验的范文（Chen 手内重定向、SayCan、RT-2、OpenVLA、VideoMimic、AnyPlace），附防误归属指南与核验流程。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构的力感知模仿学习论文摘要/引言的前后对照改写，逐条映射到本包标准。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向仓库级 ML 会议可复现工具包，并列出通用工具做不了的机器人特有检查。 |

## 安装与使用

本目录是一个自带 marketplace 清单的 Claude Code 插件：

```bash
# 在仓库克隆内执行
claude plugin marketplace add ./CoRL-Skills
claude plugin install corl-skills
```

也可以直接使用文件：每个 `skills/corl-*/SKILL.md` 都是独立的指令文件，
frontmatter 中的 `description` 描述触发时机。典型用法：

- "这个 VLA 微调项目该投 CoRL 还是 ICLR？" → `corl-topic-selection`
- "下个月出评审意见，现在该干什么？" → `corl-workflow`
- "评审到了，两个 borderline 一个 weak accept" → `corl-author-response`
- "seeds 和 episodes 到底要多少才够？" → `corl-experiments`
- "中了——camera-ready 有什么不一样？" → `corl-camera-ready`

## 2026 锚点事实（单周期快照，不是永久规则）

- CoRL 2026：第 10 届，JW Marriott，德州 Austin，**2026 年 11 月 9–12 日**。
- 截稿：摘要 **5 月 26 日**、正文 **5 月 29 日**，OpenReview
  （`robot-learning.org/CoRL/2026/Conference`），双匿名。
- 版式：8 页正文**含强制的 Limitations 章节**；致谢/参考文献/附录不计页；
  补充视频 ≤ 250 MB。
- 流程：可能第一轮无 rebuttal 直接拒稿；一页 PDF rebuttal 截止 **8 月 11 日**；
  讨论期 **8 月 12–19 日**；决定 9 月（待核实）；录用论文评审公开。
- Camera-ready：9 页正文，`\usepackage[final]{corl_2026}`，截止
  **10 月 12 日 23:59 AoE**；视频外部托管（PMLR 不收）。
- 论文集：PMLR，开放获取。已核验卷号锚点：v78 = 2017、v164 = 2021、
  v205 = 2022、v229 = 2023、v270 = 2024、v305 = 2025。
- 2026 组织者（转述）：General Chairs 为 Yuke Zhu 与 Peter Stone；Program
  Chairs 为 Ani Majumdar、Dieter Fox、Georgia Chalvatzaki。职位逐年轮换。

## 建议路线

1. **动笔之前**——先跑 `corl-topic-selection`：双轴判定不过，本包就替你省下
   一整年；再用范文库校准"learning 即贡献"的录用形态长什么样。
2. **搭实验时**——把 `corl-experiments` 与 `corl-reproducibility` 摆在代码库
   旁边：双层随机性协议与版本 manifest 越早装上越便宜，deadline 周再补装
   几乎不可能。
3. **写作阶段**——正文用 `corl-writing-style`，三通道内容分配用
   `corl-supplementary`，文献定位用 `corl-related-work`，随手对照 worked
   example 的前后改写。
4. **截稿周**——`corl-submission` 从头到尾过一遍，含对 PDF、视频帧与链接的
   机械化匿名检查。
5. **投稿之后**——用 `corl-review-process` 校准预期，安静期按 `corl-workflow`
   备好 rebuttal 弹药；意见一到切换 `corl-author-response`，之后按结果走
   `corl-camera-ready` 或转投分支。

## 事实纪律

本包刻意区分三类陈述：

1. **已核验的 2026 周期事实**——带日期或上限，可追溯到 source map 中的编号
   来源（如 5 月 29 日截稿、250 MB 视频上限）。
2. **转述事实**——仅有二手或渲染级证据，并已标注（如分数刻度的数值形式、
   主席名单）。
3. **待核实条目**——核验时无法落实，以问题而非事实的口吻出现（决定日期、
   GenAI 政策原文、2026 卷号、注册规则）。

若发现任何 skill 把第 2、3 类内容写成第 1 类，请视为 bug，对照在线页面修复。

## 维护说明

- 所有日期与上限均为 **2026 快照**；CoRL 主席逐年轮换、规则逐年重发，给出
  截止日期相关建议前必须重开当年站点。
- 页数口径（8 页里含什么）与 rebuttal 形式在 CoRL 短短的历史中都变过，
  切勿跨年沿用。
- 预期 corl.org 会拦截自动抓取；按 source map 记录的"搜索渲染 + 交叉核对"
  方法读取，并记下访问日期。
- 新增范文请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——仅有 PMLR 链接不能证明 venue，RSS/CoRL 误归属非常常见。

## 许可

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
