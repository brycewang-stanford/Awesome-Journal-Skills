# ICDE 技能包

面向 **IEEE 国际数据工程会议（ICDE）** 研究论文的十二个智能体技能。ICDE 是 IEEE 计算机学会在数据工程
方向的旗舰会议，与 ACM SIGMOD、VLDB 共同构成数据库领域的顶级三角。本技能包围绕 ICDE 在这个三角中的
结构性差异展开：研究论文按 **每届两个固定轮次** 投稿（既不同于 SIGMOD 的一年四个季度轮次，也不同于
PVLDB 的一年十二个月度截止），采用 **单盲评审**，经由 **Microsoft CMT** 提交，由 **领域主席（area
chair）** 协调 **至少三位审稿人**，历史上设有 **Revise & Resubmit（修改重投）** 阶段和较短的修改窗口，
最终以经典会议论文集形式发表于 **IEEE Xplore**，而非会议自办的期刊。

官方依据核对于 **2026-07-09**：ICDE 2027 的研究论文征稿页、重要日期页与投稿指南；ICDE 2026 的研究征稿
与重要日期页（作为两轮两阶段机制的结构锚点）；ICDE 2026 会议站点；用于范例核验的 IEEE TCDE 影响力论文
奖记录；以及 IEEE TKDE 关系页面。确切网址、带日期的事实与「待核实」清单见
[`resources/official-source-map.md`](resources/official-source-map.md)。请注意其中记录的访问限制：
`icde2027.github.io`、`icde2026.github.io`、`ieee-icde.org` 与 IEEE Xplore 拒绝自动抓取，因此事实是
通过对确切网址的搜索渲染核验，并在多个独立的官方与机构页面之间交叉比对得到的。

## 为什么 ICDE 需要专属技能包

- **只有两轮，仅此两轮。** ICDE 2027 分第一轮（论文截止 2026 年 6 月 11 日）与第二轮（2026 年 11 月
  11 日截止，2027 年 2 月 10 日通知）。第一轮被拒的论文 **不能** 进入第二轮，需等待整整一届。因此选轮
  是一次真正的抉择，而非随手之举，本技能包会教你如何计算。
- **单盲，而非双盲。** 作者姓名保留在论文上。任何从双盲会议带来的匿名化反射动作——洗掉自引、匿名化
  代码仓库——在这里都是错的，甚至会让单盲审稿人困惑。
- **轮次内的修改重投。** ICDE 2026 模式在每轮内设两个评审阶段；第一阶段可返回 Revise & Resubmit，附
  约 4 周窗口，再做最终决定。预留修改带宽因而是一项一等的规划技能（当届的修改机制状态标注为「待核实」，
  请以最新征稿页为准）。
- **IEEE 机制，而非 ACM。** 终稿要经 IEEE eCopyright 与 PDF-eXpress 进入 IEEE Xplore；版式为 IEEE
  双栏模板，正文约 12 页加不限页数的参考文献。
- **邻里稠密。** SIGMOD 按季度收入 PACMMOD，PVLDB 按月滚动，EDBT 服务欧洲社区，IEEE TKDE 收录最佳
  ICDE 论文的期刊长版扩展。从 ICDE 的视角在它们之间做路由，是本技能包明确教授的常见决策。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| `icde-submission` | 审计单轮投稿：选轮资格、CMT 档案与利益冲突、IEEE 12 页版式、单盲要求、补充材料可得性。 |
| `icde-author-response` | 起草两类回复：反驳，以及按约 4 周窗口裁剪的修改重投变更文档，并按审稿人建立需求台账。 |
| `icde-camera-ready` | 完成 IEEE eCopyright/PDF-eXpress 进 Xplore 的流程、整合必改项、终版工件发布、注册，以及 TKDE 扩展路径。 |
| `icde-artifact-evaluation` | 将代码、生成器与日志打包为「可得性计分」的补充材料，让偏工程的委员会几分钟内即可复跑。 |
| `icde-reproducibility` | 把可复现性写进论文：硬件/设备/版本固定、带种子的生成器、方差规程、基线调优公平性、图到日志的可追溯。 |
| `icde-supplementary` | 管理 12 页之外的内容：可运行工件包、扩展扫描实验，以及保持正文自足的单盲打包。 |
| `icde-review-process` | 建模两轮两阶段流水线：领域主席协调、R&R 阶段、单盲动态，以及工程型审稿人如何读评测。 |
| `icde-writing-style` | 落实首页数据工程契约、可重建的机制、贯穿的运行示例，以及 12 页 IEEE 双栏压缩。 |
| `icde-related-work` | 在深厚的数据库经典、会议环（SIGMOD/VLDB/EDBT）、期刊与在产系统上做「重复发明」审计；处理两轮并发。 |
| `icde-experiments` | 设定评测标准：负载真实性、调优基线、曲线优于单点、吞吐与尾延迟并报方差、隔离机制的消融、代价披露。 |
| `icde-workflow` | 把一届当作两轮单元来规划：选轮、逆向排期、修改带宽储备，以及第一轮被拒的代价。 |
| `icde-topic-selection` | 为项目做路由：数据管理原语测试、研究轨 vs 工业轨，以及从 ICDE 视角比对 SIGMOD/PVLDB/EDBT/TKDE。 |

## 资源

这些技能给出判断，资源目录则提供原材料：一个可对照改写的 ICDE 开篇、可用于定位的有奖项背书论文、
面向 CMT 补充材料的可运行工件参照，以及让每条陈述都可追溯的带日期事实台账。除技能外，
[`resources/`](resources/README.md) 还提供：

- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) ——
  一个虚构的写优化索引开篇，按本包规则做前后对照改写。
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 有奖项背书的真实 ICDE 论文
  （SpatialHadoop，2025 年十年影响力奖；Bw-Tree，2023 年十年影响力奖；阿里 PolarDB，2024 工业最佳
  论文），并附一份「并非 ICDE 论文」的著名论文清单。
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条已核验事实连同网址与
  访问日期、访问方式说明与「待核实」清单。
- [`resources/external_tools.md`](resources/external_tools.md) —— 官方在用页面与「不得臆测」规则。
- [`resources/code/README.md`](resources/code/README.md) —— 共享工件冒烟检查套件，翻译成数据系统语境。

## 快速上手场景

- **「我们错过了六月那轮——还赶得上 ICDE 2027 吗？」** 先用 `icde-workflow`：第一轮已关闭，第二轮
  （2026 年 11 月 11 日）是当前目标，据此逆向规划评测。
- **「这是 ICDE 论文还是 SIGMOD/VLDB 论文？」** 永远先用 `icde-topic-selection`；三者范围几乎完全
  重叠，答案通常取决于日历几何与会议文化，而非主题。
- **「评审返回 Revise & Resubmit 外加五项必改。」** 用 `icde-author-response` 变更文档模式，配合
  `icde-experiments` 完成被要求的实验——先核对约 4 周窗口的可行性再承诺。
- **「审稿人说我们的基线没调优。」** 用 `icde-experiments` 的基线公平协议，再用 `icde-author-response`
  报告调优预算或重跑结果。
- **「录用了——接下来呢？」** 用 `icde-camera-ready` 完成 IEEE eCopyright/PDF-eXpress 与 Xplore 检查，
  再在工件 URL 冻结前用 `icde-artifact-evaluation`。
- **「我们第一轮被拒了。」** 这会关闭本届：用 `icde-topic-selection` 的会场表（SIGMOD 的下一个季度轮、
  PVLDB 的月度关口），配合 `icde-review-process` 把评审意见转成面向 ICDE 2028 第一轮的返工计划。

## 核验快照（2026-07-09）

| 事实 | 取值 | 来源 |
| --- | --- | --- |
| 发表载体 | IEEE Xplore 会议论文集 | ICDE 2027 征稿 |
| 每届轮次 | 两个研究轮次 | ICDE 2027 重要日期 |
| ICDE 2027 第一轮截止 | 2026 年 6 月 11 日（已关闭） | ICDE 2027 重要日期 |
| ICDE 2027 第二轮截止 | 2026 年 11 月 11 日；2027 年 2 月 10 日通知 | ICDE 2027 重要日期 |
| 第一轮被拒 → 第二轮 | 不合资格；等下一届 | ICDE 2027 征稿 |
| 评审模式 | 单盲，领域主席 + 至少 3 位审稿人 | ICDE 2027 征稿 |
| 修改机制（2026 模式） | 两阶段；Revise & Resubmit，约 4 周窗口 | ICDE 2026 征稿/日期 |
| 篇幅预算 | 约 12 页 + 不限参考文献，IEEE 版式 | ICDE 2026 征稿 |
| 投稿平台 | Microsoft CMT（利益冲突由作者申报） | ICDE 投稿指南 |
| TKDE 关系 | 最佳论文扩展邀请 + TKDE 海报轨 | ICDE 2026 TKDE 页面 |
| ICDE 2026 | 加拿大蒙特利尔，2026 年 5 月 4-8 日 | icde2026.github.io |
| ICDE 2027 | 丹麦哥本哈根，2027 年 5 月 17-21 日 | icde2027.github.io |

## 安装

作为 Claude Code 插件（已包含 marketplace 元数据）：

```bash
/plugin marketplace add brycewang-stanford/awesome-journal-skills
/plugin install icde-skills
```

或直接把技能包复制进你的项目：

```bash
cp -r ICDE-Skills/skills/* your-project/.claude/skills/
```

## 目录结构

```text
ICDE-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json（注册 12 个技能）
├── assets/cover.svg
├── resources/
│   ├── README.md
│   ├── official-source-map.md
│   ├── external_tools.md
│   ├── exemplars/library.md
│   ├── worked-examples/01-introduction.md
│   └── code/README.md
└── skills/
    └── icde-*/SKILL.md      # 12 个技能
```

## 事实纪律

本包中的每个截止日期、页数与政策陈述都带有两种标签之一：于 2026-07-09 对照具名官方网址核验，或明确标注
「待核实」。建包时已知不确定的条目——ICDE 2027 是否保留 2026 的 Revise & Resubmit 模式还是改为二元
接收/拒稿、第一轮通知与终稿的确切日期、当前 CMT 网址、ICDE 2027 页数的再确认，以及任何按届的作者投稿
上限——都列入 source map 的「待核实」区，而非臆测填写。

## 维护提示

- ICDE 每届都会新建 `icdeYYYY.github.io` 站点并重新宣布其轮次日历、版式与评审模式；只有「每届两轮」
  这一模式、单盲默认、CMT 平台、IEEE-Xplore 发表模式与 TKDE 关系可作为安全先验——即便这些也值得每年
  重读。
- 修改重投机制（阶段结构、窗口长度）恰是各届之间最易漂移的细节；在就修改胜算给建议前，请重开最新征稿页。
  ICDE 2027 是否保留 ICDE 2026 的两阶段 Revise & Resubmit，抑或改为二元接收/拒稿，属「待核实」。
- 更新范例时，需以 IEEE TCDE 奖项引用或 IEEE Xplore 记录为准，切勿仅凭 DBLP 的主题匹配把论文归入 ICDE。
- 第一轮/第二轮的不对称——错过第一轮损失五个月，第一轮被拒损失一整届——是最尖锐的常见陷阱；凡讨论选轮
  处务必保留此提醒。
- 若征稿、重要日期与指南三页冲突，以最新陈述为准，记录冲突，并以程序主席的沟通为最终依据。
- 更换新一届时，仅将「每届两轮」「单盲默认」「CMT 平台」「IEEE Xplore 发表」与「TKDE 关系」作为先验
  向前携带，其余一切（日期、页数、修改机制、匿名政策）都需在新站点重新核验后再给出可提交建议。
- 更新范例时遵循库内协议：需 IEEE TCDE 奖项引用或 IEEE Xplore 记录、第二处独立确认，任一处不一致即
  剔除。
