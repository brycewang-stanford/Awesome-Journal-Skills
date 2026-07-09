# HPCA Skills

面向 **HPCA（IEEE International Symposium on High-Performance Computer
Architecture，IEEE 高性能计算机体系结构国际研讨会）** 论文的 12 个 agent skills。HPCA 是
计算机体系结构一年中的冬季旗舰会议，特点是**盛夏截稿、冬季（二月/三月）开会**。它由
**IEEE 计算机学会计算机体系结构技术委员会（TCCA）** 单独主办，属于 IEEE 单一主办方、
IEEE 出版的会议——这与它带 ACM 色彩的姊妹会（ISCA/MICRO/ASPLOS）在模板、徽章体系和
camera-ready 手续上都不同。本包覆盖完整链路：判断真正的贡献是一台机器、一个机制还是一次
测量；构建能通过体系结构 PC 的评测；在 HotCRP 上闯过七月的「先注册摘要、再交全文」两道门；
应对单一的 rebuttal/revision 窗口；并把录用转化为带 IEEE 徽章、在冬季档期宣讲的论文。

官方依据核验日期：**2026-07-09**。已核验 HPCA 2027 的 call-for-papers 与 important-dates
页面（`2027.hpca-conf.org`，镜像于 `conf.researchr.org/home/hpca-2027`）、HPCA 2026 主会、
artifact evaluation 与 camera-ready 页面（`2026.hpca-conf.org`）、HPCA 2025 call for papers
（`hpca-conf.org/2025/`，用于格式与匿名措辞）、HPCA 2026 HotCRP（`hpca2026.hotcrp.com`）、
IEEE-CS TCCA 站点与 HPCA Test of Time Award 页面（`ieeetcca.org`），以及 dblp 的 HPCA
系列索引。核验网关对 `hpca-conf.org`、`2026.hpca-conf.org`、`2027.hpca-conf.org`、
`conf.researchr.org`、`ieeetcca.org` 的直接抓取返回 HTTP 403，因此这些官方页面是通过对上述
精确 URL 的搜索引擎渲染读取并相互交叉核对的；完整证据链（含所有仍标注 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 当前周期状态（截至 2026-07-09）

**HPCA 2027 的截稿已迫在眉睫。** HPCA 2027 为第 33 届，据报道在美国犹他州盐湖城，2027 年
3 月举行；其全文截稿为 **2026 年 7 月 24 日（23:59 AoE）**，摘要与冲突（conflict）注册需
提前约**一周（约 7 月 17 日）**。如果你在 2026 年 7 月初读到这里，注册门槛只剩几天，而不是
几个月。HPCA 2026 为第 32 届，已于 **2026 年 1 月 31 日至 2 月 4 日在澳大利亚悉尼**举行——
因此核验时上一届刚结束，下一届截稿即为当前目标。HPCA 2027 报道的录用通知日期为
**2026 年 11 月 6 日**；从投稿到通知之间的 rebuttal/revision 窗口在核验时尚未公布（待核实）。

## HPCA 相对姊妹会的独特之处

驱动本包建议的、经核验的近周期机制：

- **单一 IEEE 主办、单一出版方。** TCCA 端到端主办 HPCA；论文由 IEEE 出版、用 IEEE 模板，
  artifact 采用 **IEEE reproducibility badging**，而非 ISCA/MICRO/ASPLOS 使用的 ACM
  Artifact Review and Badging。没有 ACM/IEEE 交替出版的问题——但任何 ACM 专属习惯（徽章名、
  版权表、DL 元数据）在这里都是**错的**习惯。
- **夏季截稿、冬季开会的档期。** HPCA 截稿在**七月下旬**，会议在**二月或三月**。在四会日历
  中，它是盛夏最后一个体系结构大截稿，也是来年第一个会议：ISCA（11 月截稿 → 6 月）、
  MICRO（春季 → 10 月）、ASPLOS（多档）、HPCA（7 月 → 2/3 月）铺满全年。
- **相隔一周的两道门。** 摘要与冲突注册早于全文约一周；较早那一步锁定 conflict list 并触发
  审稿分配，是硬性决策点，而非占位。
- **11 页正文、参考文献不限——但有一条参考文献规则。** 正文有页数上限（近周期为 11 页，
  不含参考文献），参考文献不计页数，且**每条参考文献必须列出全部作者**，否则论文可能被拒。
  绝不为省一行而缩写作者名单。
- **双盲评审 + 单一 rebuttal/revision 窗口。** 姓名只出现在表单里；与 ISCA 的两轮评审不同，
  近周期的 HPCA 采用一个合并窗口，作者在其中答复、论文可被修订。
- **自愿的、录用后的 artifact evaluation**，在单独的 HotCRP 上进行，赢得印在论文上的
  **IEEE reproducibility 徽章**——体系结构社区的可信度信号，走 IEEE 而非 ACM 流程。
- **Industry track**（工业赛道）与主赛道并行，面向以已部署系统证据、而非研究原型为贡献的工作。
- **仿真与真实硅片都是一等公民**，因此明确的 fidelity contract（工具、配置、workload、采样、
  验证）正是 HPCA 评审胜负所在。

## Skills

| Skill | 作用 |
| --- | --- |
| [`hpca-topic-selection`](skills/hpca-topic-selection/SKILL.md) | 判断贡献究竟是机器、机制还是测量，从冬季席位在 HPCA/ISCA/MICRO/ASPLOS 全年中选路，并权衡 Industry track。 |
| [`hpca-workflow`](skills/hpca-workflow/SKILL.md) | 从七月下旬的截稿倒排全年：证据冻结、两步注册、秋季等待、rebuttal/revision 冲刺，以及各结果的分支计划。 |
| [`hpca-writing-style`](skills/hpca-writing-style/SKILL.md) | 围绕一个「机制→行为」主张搭建论文：可测的动机、可核查的机制、经校准的数字，以及为修订窗口留出余量。 |
| [`hpca-related-work`](skills/hpca-related-work/SKILL.md) | 在 dblp 与 IEEE Xplore 上扫 HPCA/ISCA/MICRO/ASPLOS 记录，写出带结构性差异的谱系，匿名化行文，且绝不从参考文献里删作者。 |
| [`hpca-experiments`](skills/hpca-experiments/SKILL.md) | 声明 fidelity contract——工具、配置、workload、采样、验证——把每个主张对应到其仪器，并诚实调校 baseline。 |
| [`hpca-reproducibility`](skills/hpca-reproducibility/SKILL.md) | 钉住结果链（simulator commit → 配置 → workload → 采样区间 → 统计），每张图一份 manifest，并让环境在徽章轮次里可复活。 |
| [`hpca-supplementary`](skills/hpca-supplementary/SKILL.md) | 在 HPCA 的四个去处间分流材料：11 页正文、匿名 artifact 镜像、窗口期的暂存架、录用后的公开发布。 |
| [`hpca-artifact-evaluation`](skills/hpca-artifact-evaluation/SKILL.md) | 划定可复现层级，为冷启动评审打包仿真/硅片工作流，在单独的 AE HotCRP 上赢得 IEEE 徽章。 |
| [`hpca-submission`](skills/hpca-submission/SKILL.md) | 终审：七月两步门、11 页检查、IEEE 模板、匿名规则加「全作者」参考文献反规则、AI 使用披露、HotCRP 完成。 |
| [`hpca-review-process`](skills/hpca-review-process/SKILL.md) | 建模双盲流程，理解单一 rebuttal/revision 窗口的含义、PC 会上的 champion 动态，以及如何读懂每种结果。 |
| [`hpca-author-response`](skills/hpca-author-response/SKILL.md) | 按窗口能修什么来分流异议，跑少量新实验，为委员会会议写作，并做最小 diff 的修订。 |
| [`hpca-camera-ready`](skills/hpca-camera-ready/SKILL.md) | 反转每一步匿名化，套用 IEEE 模板与版权表，整合徽章与 DOI，并准备冬季报告。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个官方来源，带 URL 与 2026-07-09 访问日期；已核验的周期事实；仅为报道的条目（2027 具体日期、chair 名单）；明确的 待核实 清单；访问方式说明。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 现行官方入口与五道作者自查（日历、格式、匿名、门户、录用后）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 六篇 HPCA Test of Time Award 获奖论文作为贡献形态，每篇附一个自查问题与经 dblp 核对的署名护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构 prefetcher 的摘要与引言，按会议标准逐步重建，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 通向共享可复现工具包的适配器，外加工具包无法完成的五项体系结构专属检查（simulator pinning、图表可溯、workload 授权、机器状态、评审预算）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的自包含插件）：

```bash
# 在仓库克隆内执行
claude plugin marketplace add ./HPCA-Skills
claude plugin install hpca-skills
```

或直接使用文件：每个 `skills/hpca-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 告诉 agent 何时触发。典型触发：

- 「这篇 cache-coherence 论文该投 HPCA 还是 MICRO？」→ `hpca-topic-selection`
- 「七月截稿前审一遍我的 methodology」→ `hpca-experiments`
- 「审稿到了，rebuttal/revision 窗口周一开」→ `hpca-author-response`
- 「把 gem5 artifact 打包送 IEEE 徽章轮次」→ `hpca-artifact-evaluation`

## 目录结构

```text
HPCA-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── hpca-<topic>/SKILL.md # 12 个 skill，每个一个目录
└── resources/
    ├── README.md             # 资源指南与建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享可复现工具包适配器
```

## 一次投稿的建议用法

1. **初夏（现在，为七月门）：** 打开 exemplars library 用 `hpca-topic-selection`；若适配成立，
   在基础设施定型前接入 `hpca-experiments` 与 `hpca-reproducibility`。
2. **截稿两周内：** 对照 worked example 用 `hpca-writing-style`；跑 `hpca-related-work` 的
   dblp/Xplore 扫描；用 `hpca-supplementary` 做仓库/暂存分流；再从头到尾跑 `hpca-submission`
   两次——注册步一次、全文步一次。
3. **秋季等待：** 用 `hpca-review-process` 设定预期；预建异议台账；在审稿到来前做环境复活演练。
4. **窗口期：** 用 `hpca-author-response` 打完合并的 rebuttal/revision 冲刺，做最小 diff 修订。
5. **之后：** 录用则 `hpca-camera-ready` + `hpca-artifact-evaluation`；被拒则走结果树的
   retargeting 分支（MICRO、ISCA、ASPLOS）。

## 周期锚点事实（历史快照，非永久规则）

- HPCA 2026＝**第 32 届**，澳大利亚悉尼，**2026 年 1 月 31 日至 2 月 4 日**（注册 2025-07-25，
  全文 2025-08-01；HotCRP `hpca2026.hotcrp.com`，AE 在 `hpca2026ae.hotcrp.com`）。
- HPCA 2027＝**第 33 届**，据报道在犹他州盐湖城，2027 年 3 月；全文 **2026-07-24（AoE）**，
  注册约提前一周；报道通知日期 2026-11-06。
- 格式（2025 周期）：**≤ 11 页**正文，最小 10pt 字体，参考文献不计且不限，**每条参考文献须
  列全作者**；IEEE 模板；HotCRP 投稿。
- 双盲：姓名只在表单；**单一 rebuttal/revision 窗口**；AI 生成内容需在 acknowledgments 披露。
- Artifact evaluation：自愿、录用后、单独 HotCRP，赢得 **IEEE reproducibility 徽章**。

## 事实纪律

全包始终区分三类陈述：

1. **已核验周期事实**——带日期、可溯至 source map 的编号来源（11 页规则、7 月 24 日截稿）。
2. **报道事实**——仅见于二手渲染并如此标注（HPCA 2027 的 3 月具体日期、2027 chair 名单）。
3. **未核实条目**——标 待核实 并写成待解决的问题（2027 rebuttal 窗口、2027 页数上限、AE
   日历、录用率）。

若 skills 中把第 2、3 类当作第 1 类呈现，即为 bug；请对照现行官方页面修正。

## 维护说明

- 这里的每个日期与上限都是**周期快照**；涉及 deadline 前请重新打开当年的 `20XX.hpca-conf.org`。
- HPCA 单一 IEEE 主办消除了 ISCA 的出版方交替陷阱，但不要照搬 ACM 徽章名、版权表或 DL 惯例——
  IEEE 流程在 camera-ready 与 artifact evaluation 处不同。
- Chair 与委员会每届轮换；未重开组织页面前不要引用任何名单。
- 新增 exemplar 时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的 Test-of-Time 配方——通过 dblp 与 TCCA 奖项页面核验，而非某一个库的搜索。

## License

MIT——见 [`LICENSE`](LICENSE)。English README: [`README.md`](README.md)。
