# ISCA Skills（中文说明）

面向 **ISCA —— ACM/IEEE International Symposium on Computer Architecture**（计算机
体系结构旗舰会议，由 ACM SIGARCH 与 IEEE-CS TCCA 联合主办）的 12 个 agent skills。
本包覆盖一次完整投稿战役：判断"机器本身是不是贡献"、以声明的 fidelity contract 构建
仿真级证据、通过 11 月的 abstract + paper 双关卡（HotCRP）、应对两轮评审与合并的
rebuttal/revision 窗口，以及把录用转化为带 ACM badge 的 artifact 论文并在六月底完成
现场报告。

官方依据核验日期：**2026-07-08**。已核验 ISCA 2026 会议站点（主页、Call for
Papers、submission guidelines、artifact evaluation）、SIGARCH 与 IEEE-TCCA 的
2026 征稿转发、ISCA 2026 HotCRP 入口、第 52 届（东京 2025）的 ACM DL / dblp
记录，以及 SIGARCH 的 Influential ISCA Paper Award 页面。核验环境的网关对
`iscaconf.org`、`sigarch.org`、`ieeetcca.org`、`dl.acm.org`、`dblp.org` 的直接
抓取返回 403，因此官方页面通过搜索引擎对精确 URL 的渲染读取，并互相交叉核对；
完整证据链（含全部 待核实 条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 当前周期状态（截至 2026-07-08）

ISCA 2026（第 53 届）已于 2026 年 7 月 1 日在美国北卡罗来纳州 Raleigh 闭幕。当前
活跃目标是 **ISCA 2027**——据 ACM DL 会议页渲染报道将于 2027 年 6 月 5-9 日在
Atlanta 举行，但核验时 2027 CFP 尚未发布。近几届的 abstract 截稿都落在前一年
11 月中旬（ISCA 2026 为 2025-11-10），因此规划假设是 **2026 年 11 月中下旬**的
关卡——在 `iscaconf.org/isca2027/` 上线前，此假设整体标注 待核实。

## ISCA 区别于兄弟会议的机制

以下为已核验的 2026 周期机制，也是各 skill 建议的出发点：

- **双主办、出版方轮换。** SIGARCH 与 TCCA 联合主办；第 52 届论文集由 ACM 出版，
  而 2026 届使用 IEEE 品牌与 IEEE 风格模板。文献检索要以 dblp 为脊柱，camera-ready
  时每届都要重新确认出版方流程。
- **体系结构年历中的六月旗舰席位。** 11 月截稿 → 6 月开会；改投路线为 MICRO
  （春季截稿 → 10 月）、HPCA（夏季 → 2 月）、ASPLOS（一届多关卡）。
- **相隔一周的两个截稿。** Abstract 2025-11-10、正文 2025-11-17：abstract 决定
  审稿人分配，是"决策截稿"而非形式。
- **正文 11 页、参考文献不限页。** 在一个有 50 年记忆的会议上，永远不要为省页数
  裁剪参考文献。
- **两轮评审 + rebuttal/revision 窗口。** 第一轮评审 12 月、第二轮 2 月，随后是
  2026-02-16 至 2026-03-06 的三周窗口——作者不仅可以申辩，还可以**修改论文**，
  必须像冲刺一样排班。
- **带特殊条款的双盲。** 表单之外不得出现作者名、PDF 元数据须清洗、artifact 链接
  须完全匿名——但参考文献**绝不**允许匿名或删除。
- **录用后自愿参加 artifact evaluation**，按 ACM Artifact Review and Badging
  政策评定，badge 印在论文上并写入 ACM DL 元数据。
- **仿真是默认测量仪器**，因此方法学严谨性（声明 fidelity 范围、锁定版本、采样
  区间政策、对真机的校准锚点）是评审胜负手。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`isca-topic-selection`](skills/isca-topic-selection/SKILL.md) | 判断新颖性的重心在哪一层（机器 / 软硬件契约 / 纯软件），在 ISCA/MICRO/HPCA/ASPLOS 年历中选席位，并权衡 industry track。 |
| [`isca-workflow`](skills/isca-workflow/SKILL.md) | 从 11 月中旬倒排整年：证据冻结节点、冬季静默期、需排班的 2 月窗口，以及各种结果的分支预案。 |
| [`isca-writing-style`](skills/isca-writing-style/SKILL.md) | 围绕一句"机制-行为"洞察组织全文：用测量数据写 motivation、机制描述到可复算精度、数字带校准、为 revision 留余量。 |
| [`isca-related-work`](skills/isca-related-work/SKILL.md) | 跨 dblp/ACM/IEEE 检索五十年文献，写出带结构性差异的谱系段落；只匿名叙述口吻，绝不动参考文献。 |
| [`isca-experiments`](skills/isca-experiments/SKILL.md) | 声明方法学契约（工具、fidelity 范围、采样区间、校准锚点），让每类 claim 匹配能承载它的仪器，并诚实调优 baseline。 |
| [`isca-reproducibility`](skills/isca-reproducibility/SKILL.md) | 锁定结果链（模拟器 commit → 配置 → workload → 区间 → 统计），每张图一份 manifest，保证环境到 2 月还能复活。 |
| [`isca-supplementary`](skills/isca-supplementary/SKILL.md) | 在 ISCA 仅有的四个去处之间分流材料：11 页正文、匿名仓库、窗口备用架、录用后发布。 |
| [`isca-artifact-evaluation`](skills/isca-artifact-evaluation/SKILL.md) | 划分 Reproduce/Regenerate/Inspect 三层范围，把仿真重型工作流打包到评审员可冷启动，并争取 ACM badge。 |
| [`isca-submission`](skills/isca-submission/SKILL.md) | 截稿前终审：双关卡、11 页核查、模板、三条匿名规则加"参考文献不匿名"反规则、HotCRP 完整提交。 |
| [`isca-review-process`](skills/isca-review-process/SKILL.md) | 建模两轮评审管线、合并窗口的含义、PC 会议上的 champion 机制，以及如何解读每种结果。 |
| [`isca-author-response`](skills/isca-author-response/SKILL.md) | 按"三周能修好什么"分诊意见，最多补三个实验，为委员会而非审稿人写作，最小 diff 式修订。 |
| [`isca-camera-ready`](skills/isca-camera-ready/SKILL.md) | 先确认本届出版方流程，逐项反转匿名操作，整合 badge 与 DOI，并准备六月的报告。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 10 个官方来源（URL + 2026-07-08 访问日期）、已核验的 2026 周期事实、仅二手渲染报道的条目（ISCA 2027 Atlanta、主席名单）、明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及投稿前的五道作者侧核验（日历、格式、匿名、门户、录用后事项）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 六篇 Influential ISCA Paper Award（2020-2025 年度）获奖论文作为"贡献形状"，各配自查问题与双出版方归属校验指南。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构的内存调度论文摘要+引言按 ISCA 标准逐步重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享可复现工具包的适配器，并列出该工具包做不了的五项体系结构专属检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./ISCA-Skills
claude plugin install isca-skills
```

也可以直接使用文件：每个 `skills/isca-*/SKILL.md` 都是独立的说明文件，其
frontmatter `description` 告诉 agent 何时触发。典型调用：

- "这篇 prefetcher 论文投 ISCA 还是 MICRO？" → `isca-topic-selection`
- "截稿前帮我审一遍 methodology 一节" → `isca-experiments`
- "评审意见到了，revision 窗口周一开" → `isca-author-response`
- "把 gem5 artifact 打包送评" → `isca-artifact-evaluation`

## 包结构

```text
ISCA-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── isca-<topic>/SKILL.md # 12 个 skill，每个一个目录
└── resources/
    ├── README.md             # 资源导览 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享可复现工具包适配器
```

## 一次战役中的建议用法

1. **夏季（现在，面向 11 月关卡）：** 先跑 `isca-topic-selection` 并对照
   exemplars library；若判定合适，立刻按 `isca-experiments` 与
   `isca-reproducibility` 搭好基础设施，避免糟糕选择固化。
2. **秋季：** 用 `isca-writing-style` 对照 worked example 写正文；跑
   `isca-related-work` 的 dblp 检索；按 `isca-supplementary` 划分仓库与备用架。
3. **截稿两周内：** 对最终版执行 `isca-submission` 两次——abstract 关卡一次、
   paper 关卡一次。
4. **冬季：** 用 `isca-review-process` 校准预期；预建异议台账；2 月初做环境
   复活演练。
5. **窗口及之后：** 三周窗口执行 `isca-author-response`；录用则
   `isca-camera-ready` + `isca-artifact-evaluation`，被拒则走结果树的改投分支。

## 2026 周期锚点事实（历史快照，非永久规则）

- ISCA 2026 = **第 53 届**，Raleigh Convention Center（美国北卡州 Raleigh），
  **2026-06-27 至 07-01**；ISCA 2025 = 第 52 届，东京，2025-06-21 至 06-25
  （论文集由 ACM 出版）。
- 主 track：abstract **2025-11-10**、正文 **2025-11-17**；第一轮评审
  2025-12-19 截止、第二轮 2026-02-13 截止；**rebuttal/revision 窗口
  2026-02-16 至 2026-03-06**。Industry track：abstract 2025-12-05、正文
  2025-12-12。
- 格式：单倍行距双栏正文 **≤ 11 页**，参考文献不计页数且不限量；可打印
  PDF；建议使用 ISCA 2026 IEEE LaTeX 模板；经 **HotCRP**
  （`isca2026.hotcrp.com`）提交。
- 双盲：作者名只出现在表单；PDF 元数据清洗；artifact 链接完全匿名；参考文献
  永不匿名。
- Artifact evaluation：自愿、录用后进行、按 ACM badging 评定、badge 印在
  论文上；不影响录用决定。

## 事实纪律

本包区分三类陈述，并要求各 skill 保持可区分：

1. **已核验的 2026 周期事实**——带日期，可追溯到 source map 编号来源（11 页
   规则、11 月 10/17 截稿）。
2. **仅二手报道的事实**——只见于搜索渲染并如实标注（ISCA 2027 在 Atlanta、
   2026 届主席名单）。
3. **未核验条目**——标注 待核实，以待解决的问题形式表述（2027 CFP 的一切、
   通知日期、camera-ready 页数、参会义务、录用率）。

若发现任何 skill 把第 2、3 类当成第 1 类陈述，视为 bug，请对照官方页面修正。

## 维护说明

- 本包所有日期与上限都是 **2026 周期快照**；给出任何 deadline 敏感建议前，
  必须重开 `iscaconf.org/isca<year>/`。核验时 2027 CFP 尚不存在。
- ACM/IEEE 轮换使"沿用上届假设"（模板、出版方、版权表、camera-ready 页数）
  在 ISCA 比单一主办的会议更危险——每届重新核验。
- 主席与委员会逐届轮换；引用名单前必须重开 organization 页面。
- 新增 exemplar 时，按 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的流程操作：经 dblp 核验，而不是依赖单一出版方检索。

## 许可

MIT——见 [`LICENSE`](LICENSE)。英文版说明见 [`README.md`](README.md)。
