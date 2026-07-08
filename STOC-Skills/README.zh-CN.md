# STOC Skills（中文说明）

面向 **STOC — ACM Symposium on Theory of Computing**（ACM 计算理论研讨会）投稿的
12 个 agent skills。STOC 是 ACM SIGACT 的旗舰会议，覆盖算法、计算复杂性、密码学、
量子计算、学习理论等整个 theory of computation。本包覆盖一个 STOC 周期的完整弧线：
判断结果是否具有"旗舰级广度"、写出能在保证阅读窗口内说服跨方向委员会的 extended
abstract、通过 HotCRP 投稿审计、理解无 rebuttal 的评审流程，以及把录用转化为 ACM
proceedings 版本加社区真正阅读的 arXiv/ECCC 完整版。

官方依据核验日期：**2026-07-08**。已核验 `acm-stoc.org` 的 STOC 2026 Call for
Papers 与会议页面、STOC 2026 HotCRP 入口、SIGACT 奖项与政策页面、ACM Digital
Library proceedings 记录，以及范例论文的 dblp 条目。核验环境无法直接抓取官方域名
（网关 403），故所有页面均通过精确 URL 的搜索引擎渲染读取，并与 ACM DL、dblp、
SIGACT 社区博客交叉核对；完整来源链与全部 待核实 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## STOC 与相邻 venue 的结构性差异

以下机制均按 2026 周期核验，是本包全部建议的出发点：

- **阅读契约而非页数上限。** 投稿不限长度，但委员会只保证阅读 abstract、
  **table of contents** 与前十二页，其余自行裁量。ToC 是被评审的对象；所有定理
  必须在窗口内陈述。
- **完整版才是记录物。** CFP 要求录用作者在 camera-ready 前把含全部证明的完整版
  公开到 arXiv 或 ECCC；ACM proceedings 里的是 extended abstract——广告，不是
  记录。两份文档的一致性是一等工程问题。
- **新近转为双盲。** STOC 2026 采用双盲评审，告别了长期的非匿名传统；旧模板与
  旧习惯是最主要的身份泄露源。
- **没有 rebuttal。** 从 11 月截稿直达 2 月决定；所有可预期的异议必须在投稿内
  预先回答，因为没有第二次对话。
- **与 FOCS 构成双节拍年度。** STOC（11 月截稿、6 月开会）与 FOCS（4 月截稿、
  秋季开会）共享社区与范围；理论组围绕这对节拍排程，被拒论文通常改进后投向
  另一拍。
- **只看定理。** 没有实验维度、artifact track 或 checklist。计算的合法角色只有
  三种：带证书的证明步骤、构造发现工具、明确标注的示意图——从不是 benchmark。
- **TheoryFest。** STOC 2026 在盐湖城以五/六天扩展周形式举行（6 月 22–26 日，
  周六 6 月 27 日为 "Can AI do Theory?" workshop），全部录用论文有报告，PC 可
  评选至多四篇 Best Paper。

## Skills 一览

| Skill | 作用 |
| --- | --- |
| [`stoc-topic-selection`](skills/stoc-topic-selection/SKILL.md) | 运行广度三测试（走廊、谱系、技术），在 STOC/FOCS、SODA、CCC、ITCS、COLT、CRYPTO、PODC、SoCG、EC、QIP 或直接投期刊之间路由。 |
| [`stoc-workflow`](skills/stoc-workflow/SKILL.md) | 规划双节拍年度：向 11 月截稿倒排、FOCS 备选、勘误文件、camera-ready 双交付物。 |
| [`stoc-writing-style`](skills/stoc-writing-style/SKILL.md) | 定理先行的第一页、informal/formal 配对陈述、technical overview 章节、面向跨方向委员会的记号经济学。 |
| [`stoc-related-work`](skills/stoc-related-work/SKILL.md) | 覆盖理论审稿人必查的五条文献线——界的谱系、障碍文献、相邻模型、技术源流、并发预印本——并做版本感知的引用。 |
| [`stoc-supplementary`](skills/stoc-supplementary/SKILL.md) | 设计第十二页之后的一切：被评审的 ToC、内容放置矩阵、指针纪律、附录与完整版的分工。 |
| [`stoc-reproducibility`](skills/stoc-reproducibility/SKILL.md) | 让定理可独立核查：单一来源的陈述防止两版漂移、假设可见性、外部结果假设审计、承载证明的计算的确定性。 |
| [`stoc-experiments`](skills/stoc-experiments/SKILL.md) | 把任何计算归类为带证书的证明步骤、发现工具或示意图——并把 benchmark 形态的证据改道到奖励它的 venue。 |
| [`stoc-artifact-evaluation`](skills/stoc-artifact-evaluation/SKILL.md) | 管理无 artifact track 下的证据栈：完整版作为记录物、证书加独立 checker、诚实的形式化声明。 |
| [`stoc-submission`](skills/stoc-submission/SKILL.md) | HotCRP 终审：保证阅读规则、格式底线、双盲清扫、SIGACT 先发表/同时投稿政策、截稿周排序。 |
| [`stoc-review-process`](skills/stoc-review-process/SKILL.md) | 建模 SIGACT PC 加外部 subreviewer 的评审结构、委员会的评价轴、11 月至 2 月的时间线，以及各种结果的真实含义。 |
| [`stoc-author-response`](skills/stoc-author-response/SKILL.md) | 在无 rebuttal 的 venue 上经营三条真实渠道：预先消解异议、主席转达的技术澄清、面向 FOCS 的重投备忘录。 |
| [`stoc-camera-ready`](skills/stoc-camera-ready/SKILL.md) | 交付 3 月 31 日的两件产物——ACM proceedings 版与公开完整版——保持二者一致，并准备 TheoryFest 报告。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 12 个官方来源（URL + 核验日期）、已核验的 2026 周期事实、访问方式说明、明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口，以及与各 skill 对应的六个作者侧核验流程。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经 dblp/ACM 核验的 STOC 论文，横跨五十年与五种贡献类型，附 STOC/FOCS 误归属防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构的动态连通性论文开头：从期刊风格重建为 STOC 弧线（结果 → 谱系 → 障碍 → 技术 → 后果）。 |
| [`resources/code/README.md`](resources/code/README.md) | 在证明优先的 venue 上仍然适用的少量共享工具，加上 STOC 原生的匿名、漂移与打包检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace manifest，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./STOC-Skills
claude plugin install stoc-skills
```

也可直接使用文件：每个 `skills/stoc-*/SKILL.md` 都是独立的指令文件，frontmatter
中的 `description` 说明触发时机。典型用法：

- "这个结果该投 STOC 还是 SODA？" → `stoc-topic-selection`
- "上传前按 STOC 阅读规则审一遍稿" → `stoc-submission`
- "证明都在第 30 页之后，附录怎么组织？" → `stoc-supplementary`
- "录用了，3 月的两个截止要交什么？" → `stoc-camera-ready`

## 包结构

```text
STOC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                 # English version
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── stoc-<topic>/SKILL.md # 12 个 skills，每个一个目录
└── resources/
    ├── README.md             # 资源导览与推荐路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享工具适配（大部分谢绝引入）
```

## 推荐用法

1. **动笔之前**——先跑 `stoc-topic-selection` 的广度三测试；若不过，本包为你
   省下了一个投稿周期。再对照 `resources/exemplars/library.md` 校准什么才算
   "旗舰级"贡献。
2. **证明与写作期**——`stoc-writing-style` 管前十二页，`stoc-supplementary`
   管 ToC 与附录架构，`stoc-reproducibility` 管两版一致性；对照
   worked example 的 before/after 检查第一页弧线。
3. **截稿周**——`stoc-submission` 从头到尾过一遍：保证阅读审计、双盲清扫、
   SIGACT 政策核对、HotCRP 表单一致性；记住截止是美东时钟。
4. **投稿之后**——`stoc-review-process` 校准预期，`stoc-author-response`
   维护勘误文件并准备可能的主席转达问题。
5. **决定之后**——录用走 `stoc-camera-ready`（两件 3 月 31 日交付物）；被拒
   则按 `stoc-workflow` 的双节拍表评估 FOCS 重投。

## 2026 周期锚点事实（历史快照，非永久规则）

- STOC 2026 为第 **58** 届：美国犹他州盐湖城，**2026 年 6 月 22–26 日**，扩展
  TheoryFest 周（6 月 27 日周六："Can AI do Theory?" workshop）。
- 截稿：**2025 年 11 月 4 日 4:59pm EST**（美东时钟，非 AoE），HotCRP 提交，无
  单独摘要截止；通知 **2026 年 2 月 1 日前**；camera-ready **2026 年 3 月 31 日
  （AoE）**。
- 阅读规则：不限长度；保证阅读 abstract + ToC + 前**十二页**；11 磅以上字号、
  单栏、1 英寸页边距、letter 纸型。
- **双盲**评审；SIGACT 先发表/同时投稿政策（Science/Nature 例外）；arXiv/ECCC
  预印本不算先发表。
- 录用论文的含证明完整版须在 camera-ready 前公开于 **arXiv/ECCC**；proceedings
  收录于 ACM Digital Library（第 58 届 DOI：10.1145/3798129）。
- PC 主席：Artur Czumaj（Warwick）。实验性可选 **LLM 投稿前反馈**（基于
  Gemini；11 月 1 日前交全文；输出仅作者可见）。
- 姊妹节拍：FOCS 2026 截稿 2026 年 4 月 1 日（21:00 UTC），会议 2026 年
  11 月 8–11 日，纽约。

## 事实纪律

本包把三类陈述保持可区分：

1. **已核验的 2026 周期事实**——带日期并可追溯到来源表编号（十二页窗口、
   11 月 4 日截稿）。
2. **社区惯例**——只能从 venue 的实际行为中观察到的做法（主席转达澄清问题、
   subreviewer 代审），一律标注为惯例而非规则。
3. **核验时无法确认的条目**——标注 待核实 并写成待解决的问题（整个 STOC 2027
   周期、注册义务、camera-ready 格式细节、首个双盲年份）。

若发现任何第 2、3 类内容被写成第 1 类，按 bug 处理，对照官方页面修正。

## 维护说明

- 上述所有日期与规则均为 **2026 周期快照**。阅读窗口已在历史上变过大小
  （10 页 → 12 页），双盲是新政策；给出任何截稿敏感建议前，先打开当年的
  `acm-stoc.org/stoc<year>/`。
- **STOC 2027 在 2026-07-08 时整体 待核实**——找不到官方 CFP，聚合站列出的
  日期疑为 2026 数据的循环使用。历史规律（夏末发 CFP、11 月初截稿）只是规律，
  不是事实。
- PC 主席与委员会逐年轮换；本包中出现的所有人名均为单周期事实。
- 新增范例论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  dblp 核验流程——绝不凭记忆在 STOC 与 FOCS 之间归属论文。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
