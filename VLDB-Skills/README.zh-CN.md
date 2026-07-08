# VLDB Skills

面向 International Conference on Very Large Data Bases (VLDB) 及其出版载体 PVLDB
(Proceedings of the VLDB Endowment) 的 12 个 agent skills。VLDB 是数据库领域两大
旗舰会议之一，其结构与几乎所有 CS 会议都不同：**没有年度截稿日**。研究论文按
**每月滚动截稿**投给某一卷 PVLDB —— 每月 1 日一个 deadline，一年十二次机会 ——
采用期刊式的 **accept / revise / reject** 三值结果，revise 只有一次机会、最长三个
月修改期，论文先按月出版、数月后才在会议上报告。

官方依据核验日期：**2026-07-08**。已核验 PVLDB Volume 20 submission guidelines、
VLDB 2027 research-track call、PVLDB Volume 19 guidelines 与 VLDB 2026 research-track
call、VLDB 2026/2027 会议网站、pVLDB reproducibility 页面，以及用于 exemplar 验证的
VLDB Endowment 获奖记录。精确 URL、带日期的事实与 待核实 清单见
[`resources/official-source-map.md`](resources/official-source-map.md)。注意其中记录的
访问方式说明：`vldb.org`、`dl.acm.org`、`dblp.org` 拒绝自动化直接抓取，页面内容
通过对精确 URL 的搜索引擎渲染核验，并与多个独立官方/机构页面交叉比对。

## PVLDB 模型一段话讲清

每月 **25 日**前在 CMT 注册 abstract，下月 **1 日太平洋时间下午 5:00**（不是
AoE —— 务必换算时区）提交全文，再下月 **15 日**左右收到评审意见和结果。拿到
*revise* 意味着最多 **三个月**内完成**仅有的一次**修改，由同一批审稿人对照他们
明确列出的 required changes 重新评判。录用论文进入该卷的月度 issue 出版；在该卷
cutoff（Vol 19 为 2026 年 6 月 15 日）前录用的论文在对应会议上报告。构建日当前
开放的是 **Vol 20**（首个截稿 2026-04-01，最后截稿 2027-03-01），对应 **VLDB 2027
雅典，2027 年 8 月 23-27 日**；VLDB 2026 在**波士顿，2026 年 8 月 31 日 - 9 月
4 日**举行，收录 Vol 19 论文。

## 本包的深度投放在哪里

- **选月是算术题。** 一年十二个 deadline 时，策略能力体现在从会议 cutoff、评审
  时长、三个月修改期倒推出正确的投稿月份，而不是把手头的稿子丢给最近的 1 日。
  `vldb-workflow` 教这套倒推。
- **revision 就是 author response。** PVLDB 没有 rebuttal 阶段：评审与结果一起
  到达，与审稿人唯一的一次对话就是修改包。`vldb-author-response` 教 requirement
  ledger 和 change document 的写法。
- **单盲下的坦率。** 作者姓名保留在论文上，扩展版技术报告可以实名挂 arXiv，
  自引直接写 —— 与周边双盲会议正好相反（以现行 guidelines 原文为准，见待核实）。
- **有牙齿的可复现性。** 提供 artifact 可获 ACM badge；pVLDB Reproducibility
  Evaluation 会实际重跑实验；EA&B 类论文**必须**参加；设有 Best Reproducible
  Paper Award。两个 skill 分别覆盖工程侧与打包侧。
- **可扩展系统的证据文化。** 报告吞吐与尾延迟并声明方差、给曲线而非单点、
  认真调优对手系统、强制给出 loss map —— `vldb-experiments` 执行这条评审底线。

## Skills

- `vldb-submission`：审计一个月度周期 —— 25 日 abstract 关口、CMT 窗口、太平洋
  时间下午 5 点截稿、类别页数预算、单盲封面页、作者投稿上限。
- `vldb-author-response`：把 revise 结果变成 requirement ledger、三个月计划和
  能让同一批审稿人接受的 change document。
- `vldb-camera-ready`：制作 PVLDB issue 版本 —— 卷专属模板、PDF/A 与字体嵌入、
  availability 段落、命名/版权流程、会议报告安排。
- `vldb-artifact-evaluation`：按四个 artifact 层面为 pVLDB Reproducibility
  Evaluation 打包，冲击 badge 与奖项。
- `vldb-reproducibility`：把披露工程化写进论文 —— 硬件/软件/数据/负载底线、
  系统方差协议、对手公平性台账、图到原始数据的可追溯链。
- `vldb-supplementary`：管理页数预算之外的内容（appendix 占用正文限额）——
  扩展 TR、打 tag 的仓库、论文自足性检查。
- `vldb-review-process`：建模滚动流水线 —— 约六周周转、三值结果空间、一次性
  revision 的胜率、常设 review board。
- `vldb-writing-style`：执行第一页契约、限定范围的性能声明、trade-off 坦率、
  12 页内的术语纪律。
- `vldb-related-work`：跨深层经典文献、现役 venue 圈与已上线系统做"重复发明"
  审计；处理滚动日历下的并行工作与版本重叠。
- `vldb-experiments`：完成四重证据义务 —— 问题存在、机制致效、增益可扩、
  代价已知。
- `vldb-workflow`：计算投稿月份、从 1 日倒排单个周期、为 revision 预留人力、
  管理团队投稿上限。
- `vldb-topic-selection`：应用 data-management primitive 测试，在 Regular /
  EA&B / Scalable Data Science / Vision 之间选类别，并对照 SIGMOD、PODS、ICDE、
  CIDR、EDBT、KDD、系统会议与 The VLDB Journal 做路由。

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) ——
  每条事实的 URL 与核验日期、访问方式说明、待核实清单。
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 四篇有
  奖项锚定的真实论文：Test-of-Time 2025 的查询优化器测量研究（Leis et al.,
  PVLDB 2015）、C-Store（VLDB 2005）、Hadoop-GIS（ToT 2024）、TiDB（PVLDB
  2020），以及"不是 VLDB 论文"的著名论文清单。
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  —— 一篇虚构 LSM 存储论文第一页的 before → after 重写。
- [`resources/external_tools.md`](resources/external_tools.md) —— 现行官方入口
  与"禁止推断"规则。
- [`resources/code/README.md`](resources/code/README.md) —— 共享 artifact 冒烟
  检查工具的系统视角用法。

## 常见入口

- **"我们哪个月投？"** → `vldb-workflow`。想带着 revision 保险走到雅典 2027，
  倒推起点大约在 cutoff 前六个月。
- **"这是 VLDB 论文还是 SIGMOD 论文？"** → `vldb-topic-selection`；两家 scope
  几乎完全重叠，答案通常取决于日历几何与类别匹配，而不是主题。
- **"拿到 revise，五条 required changes。"** → `vldb-author-response`，需要补
  实验再进 `vldb-experiments`。庆祝之前先算三个月是否够用。
- **"25 日 abstract 截稿前我们准备好了吗？"** → 提前两周跑 `vldb-submission`
  的审计序列。
- **"录用了 —— 现在哪里会出问题？"** → `vldb-camera-ready`（PDF/A 总在最后
  咬人），然后趁 artifact URL 冻结前进 `vldb-artifact-evaluation`。
- **"审稿人会问为什么不和 X 比。"** → 提前跑 `vldb-related-work` 的重复发明
  审计和 `vldb-experiments` 的 baseline 公平性协议。

## 安装

作为 Claude Code plugin（已含 marketplace 元数据）：

```bash
/plugin marketplace add brycewang-stanford/awesome-journal-skills
/plugin install vldb-skills
```

或直接把 skills 拷贝进项目：

```bash
cp -r VLDB-Skills/skills/* your-project/.claude/skills/
```

## 目录结构

```text
VLDB-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json（注册 12 个 skill）
├── assets/cover.svg
├── resources/
│   ├── README.md
│   ├── official-source-map.md
│   ├── external_tools.md
│   ├── exemplars/library.md
│   ├── worked-examples/01-introduction.md
│   └── code/README.md
└── skills/
    └── vldb-*/SKILL.md      # 12 个 skill
```

## 事实纪律

本包中每个日期、页数、上限与政策，要么绑定到 2026-07-08 核验过的具名 URL，
要么明确标注 待核实。刻意不猜的条目 —— 现行 Vol 20 页面上单盲政策的原文、
被拒后是否存在再投稿禁入期、Vol 20 camera-ready 流程、demo/tutorial 页数、
Vol 20 的会议 cutoff 日期、官方页面上的 EiC 名单 —— 都列在 source map 的
待核实一节。

## 维护说明

- PVLDB 每卷重新发布一切：截稿、上限、类别、页数、模板与官员每年重置。唯一
  可作先验的是滚动月度模式本身，且它也值得每年重读一次。
- 太平洋时间下午 5 点是这个 venue 对非美国作者最锋利的陷阱；凡引用日期处都
  保留时区换算提醒。
- VLDB 2027 结束后，将本包重新锚定到 Vol 21，并按 library 的双来源规则用最新
  Test-of-Time 获奖论文刷新 exemplars。
- 官方页面互相冲突时，以更新一卷的表述为准，记录冲突，并把 PVLDB
  Editors-in-Chief 的直接答复视为最终依据。
