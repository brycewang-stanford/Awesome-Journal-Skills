# FOCS Skills

面向 **FOCS（IEEE Symposium on Foundations of Computer Science，计算机科学基础
研讨会）** 投稿的 12 个 agent skills。FOCS 是理论计算机科学的秋季旗舰会议，由
IEEE Computer Society 的 TCMF（Technical Committee on Mathematical Foundations
of Computing）主办。本包覆盖以 4 月截稿为锚点的完整周期：基础层面重要性的
判断、以完整版（full version）投稿并让前十页承载全部论证、HotCRP 上传前的
审计、没有 rebuttal 的夏季评审等待，以及录用后把 IEEE Xplore 会议版和
arXiv/ECCC 上作为正确性记录的公开完整版同步交付。

官方依据核验日期：**2026-07-08**。核验对象包括 `focs.computer.org/2026/` 的
会议主页与 Call for Papers、FOCS 2026 HotCRP 投稿系统、workshop 征集页、IEEE
TCMF 奖项页面、IEEE Xplore 与 IEEE CS Digital Library 的会议录记录、dblp 条目，
以及近年 Machtey Award 的大学官方报道。核验环境无法直接抓取官方域名，因此
所有页面均通过精确 URL 的搜索引擎渲染读取，并与 TCMF、IEEE Xplore、dblp 及
社区博客交叉核对；完整链路（含全部 待核实 条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 2026 周期当前所处阶段（以核验日期为准）

FOCS 2026（第 67 届，纽约，2026 年 11 月 8–11 日）已于 **2026 年 4 月 1 日
17:00 EDT** 截稿。因此本包教的是当前周期的"进行时"阶段：夏季评审等待期、
7 月 31 日截止的 workshop 提案窗口、日期公布后的 camera-ready 准备，同时给出
面向 FOCS 2027（核验时 CFP 尚不存在）的倒排规划。所有 2026 事实均为周期
快照，不是永久规则。

## 驱动本包的会议机制

- **十页窗口，外加参考文献。** 投稿无长度上限，但委员会只保证阅读摘要、
  **参考文献**与正文前十页。FOCS 把文献列表明确列入必读集合——你的
  bibliography 是被评审的对象。
- **投的是论文本身，不是预告片。** CFP 鼓励直接提交含全部证明的完整版；
  该会议不存在任何独立的补充材料通道。
- **双盲评审的"老兵"。** FOCS 至少自 2023 周期起要求匿名投稿，比它的 ACM
  姊妹会议早数年；其目的措辞是保证初始判断无偏见，而非让作者身份不可发现。
- **IEEE 会议执行 SIGACT 政策。** 主办方是 IEEE TCMF，但先行发表/一稿多投
  政策沿用 SIGACT 规则，会议录发表在 IEEE Xplore——只读一个学会规则的作者
  常在这条接缝上摔跤。
- **没有 rebuttal。** 4 月上传与最终决定之间没有任何作者发言机会；投稿本身
  就是你在对话中的全部台词。
- **双旗舰之年中的春季一拍。** FOCS 四月收稿、秋季开会；STOC 十一月收稿、
  六月开会。两会构成理论界天然的再投稿回路，本包从 FOCS 的座位规划这个
  节奏。
- **以奖项谱系作为质量罗盘。** Machtey Award（最佳学生论文）与 TCMF 管理的
  Test of Time Award（10/20/30 年回望）用会议自己的声音定义了什么是耐久的
  FOCS 工作——exemplars 库即由此构建。

## Skills

| Skill | 用途 |
| --- | --- |
| [`focs-topic-selection`](skills/focs-topic-selection/SKILL.md) | 执行"后果/障碍/耐久性"三问重要性测试，安全使用 broaden-the-reach 通道，在 FOCS、STOC、SODA、CCC、ITCS、CRYPTO、QIP、COLT 与期刊之间路由。 |
| [`focs-workflow`](skills/focs-workflow/SKILL.md) | 管理 2026 周期投稿后的进行时阶段，并按四月节奏为 2027 做倒排规划，含责任人矩阵与 STOC 节拍协调。 |
| [`focs-writing-style`](skills/focs-writing-style/SKILL.md) | 为保证阅读的页数做预算，用 `thm-restate` 绑定非正式/正式定理陈述，写好"障碍段落"，保持双盲安全的行文。 |
| [`focs-related-work`](skills/focs-related-work/SKILL.md) | 构建结果谱系表，钉住 arXiv/ECCC 版本号，核对 `conf/focs/` 与 `conf/stoc/` 归属，宽厚地处理并行工作。 |
| [`focs-experiments`](skills/focs-experiments/SKILL.md) | 按"审稿人会问什么"给计算定位——承担证明的枚举验证、被发现的构造、诚实的示意图——并把 benchmark 证据改道到合适的会议。 |
| [`focs-reproducibility`](skills/focs-reproducibility/SKILL.md) | 工程化可查证性：假设台账、跨版本哈希锁定的定理陈述冻结、外部定理引用审计、计算步骤的证书。 |
| [`focs-supplementary`](skills/focs-supplementary/SKILL.md) | 在没有补充材料通道的会议上设计第十一页之后的一切——双读者契约、正文组织、指针纪律、篇幅判断。 |
| [`focs-artifact-evaluation`](skills/focs-artifact-evaluation/SKILL.md) | 在没有 artifact track 的前提下管理证据清单：作为记录载体的公开完整版、证书打包、版本台账、克制的形式化声明。 |
| [`focs-submission`](skills/focs-submission/SKILL.md) | HotCRP 上传前的最终审计：EDT 截稿时钟、十页窗口、排版底线、PDF 加密禁令、匿名清扫、IEEE/SIGACT 政策接缝。 |
| [`focs-review-process`](skills/focs-review-process/SKILL.md) | 建模 TCMF 体系下的 PC、子审稿人委派、委员会的三个核心问题、FOCS 的双盲历史，以及每种结果的真实含义。 |
| [`focs-author-response`](skills/focs-author-response/SKILL.md) | 在无 rebuttal 的会议上运作：投稿前的预先答辩、联系 PC 主席的少数正当情形、纪律化的秋季再投稿备忘录。 |
| [`focs-camera-ready`](skills/focs-camera-ready/SKILL.md) | 同步交付 IEEE 会议版与公开完整版，彻底逆转匿名化，准备纽约报告与奖项资格材料。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 13 个来源的 URL 与访问日期、已核验的 2026 周期事实清单、访问方式说明、待核实 台账。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及与各 skill 对应的六项作者侧自查。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 以奖项为锚的范文库（Test of Time 与 Machtey 两条谱系），附自检问题与 FOCS/STOC 归属误配防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构的 expander decomposition 论文开篇，从期刊节奏重排为十页窗口结构。 |
| [`resources/code/README.md`](resources/code/README.md) | 在定理型会议上仍然适用的少量共享工具，加上 FOCS 原生的 PDF、陈述冻结与证书检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./FOCS-Skills
claude plugin install focs-skills
```

也可直接使用文件：每个 `skills/focs-*/SKILL.md` 都是独立的指令文件，其
frontmatter `description` 告诉 agent 何时触发。典型问法：

- "这个 hardness 结果够 FOCS 吗，还是该投 CCC？" → `focs-topic-selection`
- "我们 4 月 1 日投完了——现在该做什么？" → `focs-workflow`
- "上传 HotCRP 前帮我审一遍 PDF" → `focs-submission`
- "有个引理依赖穷举搜索，怎样让它可被引用地成立？" → `focs-experiments`
- "录用了：IEEE 版和 arXiv 版怎么保持一致？" → `focs-camera-ready`

## 包结构

```text
FOCS-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── focs-<topic>/SKILL.md # 12 个 skill，每个一个目录
└── resources/
    ├── README.md             # 资源导览与建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 可查证性工具说明
```

## 2026 锚点事实（周期快照，非永久规则）

- FOCS 2026 为**第 67 届**：美国纽约，**2026 年 11 月 8–11 日**，IEEE
  Computer Society TCMF 主办。
- 截稿：**2026 年 4 月 1 日 17:00 EDT（21:00 UTC）**，HotCRP
  （`focs26.hotcrp.com`）；notification 与 camera-ready 日期在核验时尚未
  公布（待核实）。
- 格式：无长度上限；鼓励提交完整版；保证阅读范围为摘要 + 参考文献 +
  前**十页**；11 磅以上单栏、1 英寸页边距、letter 纸型；PDF 不得带有
  复制/打印安全限制。
- **双盲评审**（FOCS 至少自 2023 年起实行）；SIGACT 先行发表/一稿多投政策；
  预期在 camera-ready 前把含全部证明的完整版公开（arXiv/ECCC）。
- PC 主席：Sanjeev Khanna（单周期事实）。Workshop 定于 11 月 8 日周日；
  提案 2026 年 7 月 31 日 AoE 前发给 workshop 主席 Dakshita Khurana 与
  Sam Hopkins；8 月 14 日出结果。
- 姊妹节拍：STOC 2026 于 2025 年 11 月 4 日截稿、2026 年 6 月 22–26 日举行。

## 事实纪律

本包把三类陈述保持可区分：

1. **已核验的周期事实**——带日期，可追溯到 source map 的编号来源（4 月 1 日
   截稿、十页窗口）。
2. **社区惯例**——从会议实际运作观察到的做法（子审稿人委派、arXiv 先行
   文化），以惯例身份标注。
3. **待核实条目**——在 source map 中显式列出，在 skill 中以问题而非事实的
   口吻出现（notification 日期、camera-ready 格式、参会义务、FOCS 2027 的
   一切）。

任何把第 2、3 类当作第 1 类陈述的文字都是 bug，应对照官方页面修正。

## 维护说明

- 上述所有数字均为 **2026 周期快照**。截稿日、窗口页数、匿名措辞与奖项
  机制都可能变化；给出临期建议前务必重开 `focs.computer.org/<year>/`。
- **FOCS 2027 在 2026-07-08 时完全待核实**：无 CFP、无地点、无日期。
  "四月截稿、秋季开会"是历史规律，不是承诺。
- PC 主席与委员会按届任命；本包中出现的人名随其周期过期。
- 新增范文时使用 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的奖项锚定配方，切勿凭记忆在 FOCS 与 STOC 之间归属论文。

## License

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
