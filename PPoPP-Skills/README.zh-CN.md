# PPoPP Skills

面向 **PPoPP —— ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming**
论文的 12 个 agent skills。PPoPP 是并行与并发编程的顶级论坛：面向并行的语言、编译器与运行时；
lock-free/wait-free 数据结构与并发正确性证明；GPU/加速器与 NUMA 性能工程；并行算法；以及大规模
可扩展性研究。本包覆盖一次 PPoPP 投稿的完整流程：判断项目属于 PPoPP 还是应投 PLDI、CGO、POPL、
ASPLOS 或 SC；构建 PPoPP 要求的**双重证据 —— 并发正确性 *与* 实测并行性能**；准备双栏 double-blind
的 HotCRP 投稿；应对 **author-response rebuttal**；直到完成 camera-ready 与获得与 CGO 共用的
ACM artifact 徽章。

官方依据核验日期：**2026-07-09**。已核验 PPoPP 2026（悉尼）与 PPoPP 2027（盐湖城）research track 的
call 与 Important Dates 页面、sigplan.org 的 PPoPP 公告、PPoPP HotCRP 站点、PPoPP/CGO 的 artifact
evaluation 页面、ACM Artifact Review and Badging 政策，以及 ACM Digital Library 会议录。核验环境中
直接抓取 `conf.researchr.org`、`sigplan.org` 与 `dl.acm.org` 返回 403，因此通过搜索引擎对精确 URL 的
渲染阅读官方页面，并与 ACM Digital Library、dblp 及 SIGARCH/SIGPLAN call 交叉核对；完整记录（含所有
待核实 项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## PPoPP 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 PLDI、POPL、CGO
或 HPC/systems 会议转投作者最常犯的错误：

- **它是关于并行性的 SIGPLAN 研讨会，而非编译器或语义会议。** PPoPP 奖励*核心就是*并发与并行性能的
  工作。巧妙的编译器 pass 属于 **CGO/PLDI**；并发新逻辑属于 **POPL**；机器/微架构结果属于
  **ASPLOS/HPCA**。PPoPP 要的是并行编程的教益。
- **双栏 ACM 格式，10 页紧凑。** 投稿使用**双栏 `acmart` `sigplan`** 会议模板
  （`ppopp-acmart-sigplanproc-template.tex`），**正文含图 10 页**，**参考文献不计且不限**。既不是
  PLDI 的单栏篇幅，也不是 IEEE 框 —— 两种习惯都不要带过来。
- **Double-blind，且有真实 rebuttal。** 评审为 **double-blind**；设有 **author-response** 阶段
  （rebuttal），reviewer 匹配可能用 **TPMS**，PC 之外另有 **External/Extended Review Committee
  (ERC)**。
- **四会同周。** PPoPP 在 **HPCA / CGO / PPoPP / CC** 联合周内举办（2026 悉尼；2027 盐湖城），因此
  其日历、artifact 流程乃至注册都与 CGO 交织 —— 作者可善用这一点。
- **独特的 artifact 徽章政策。** AE 委员会授予 **Functional *或* Reusable** 以及 **Results
  Reproduced**；PPoPP 有意**不授予 "Results Replicated"**，而绿色 **Artifacts Available** 徽章由
  出版方依据存放链接直接授予、**不做审计**。
- **被拒论文自动进入 poster。** 未获常规报告的论文自动进入 **poster track**，其**两页摘要收入会议
  录** —— 是真实的第二结果，而非安慰邮件。
- **双重证据门槛：正确性与可扩展性。** 并行结果同时被两方面评判：并发下正确（race、linearizability、
  内存模型）*且*确实可扩展（speedup 曲线、核数、NUMA 效应、GPU occupancy），并对真实 baseline。

## Skills

| Skill | 作用 |
| --- | --- |
| [`ppopp-topic-selection`](skills/ppopp-topic-selection/SKILL.md) | 在 PPoPP 与同类会议（PLDI、CGO、POPL、ASPLOS、HPCA、SC、SPAA、OOPSLA）间选路，用“并行性是不是贡献本身？”测试与联合周日历判断。 |
| [`ppopp-workflow`](skills/ppopp-workflow/SKILL.md) | 从夏季截止日倒排年度计划，经 rebuttal、通知、录用后 AE 轮、camera-ready 与联合周报告。 |
| [`ppopp-writing-style`](skills/ppopp-writing-style/SKILL.md) | 用双栏构建并行编程骨架：首页给出并发+性能论断、可扩展性叙事、10 页纪律。 |
| [`ppopp-related-work`](skills/ppopp-related-work/SKILL.md) | 覆盖并行编程各 lane（运行时、lock-free 结构、内存模型、GPU），写 delta-first 定位并保持自引匿名。 |
| [`ppopp-experiments`](skills/ppopp-experiments/SKILL.md) | 让证据匹配论断：并发正确性与实测可扩展性 —— speedup 曲线、核数扫描、NUMA/GPU、方差与诚实 baseline。 |
| [`ppopp-reproducibility`](skills/ppopp-reproducibility/SKILL.md) | 让并行结果可复现：钉死硬件/拓扑、thread pinning、seed、warm-up，以及评审者复跑的环境描述。 |
| [`ppopp-supplementary`](skills/ppopp-supplementary/SKILL.md) | 按决策重要性划分 10 页正文与 artifact/附录 —— 决定录用的证明与完整扫描须保持可读。 |
| [`ppopp-submission`](skills/ppopp-submission/SKILL.md) | HotCRP 终审：双栏模板与 10 页篇幅、double-blind 清扫、摘要、对 PC+ERC 的 conflict、desk-reject 分诊。 |
| [`ppopp-review-process`](skills/ppopp-review-process/SKILL.md) | 建模流程 —— double-blind、PC+ERC、TPMS 匹配、rebuttal、决定与自动 poster 考量 —— 及作者杠杆点。 |
| [`ppopp-author-response`](skills/ppopp-author-response/SKILL.md) | 为性能/并发论文写 rebuttal：在字数上限内用数字而非形容词回答缺 baseline 与能否扩展之问。 |
| [`ppopp-artifact-evaluation`](skills/ppopp-artifact-evaluation/SKILL.md) | 在与 CGO 共用的录用后 AE track，用可复现并行测量赢得 PPoPP 徽章（Functional/Reusable + Reproduced；Available 经出版方）。 |
| [`ppopp-camera-ready`](skills/ppopp-camera-ready/SKILL.md) | 去匿名、补全 ACM 版权/元数据、把 artifact DOI 永久化、通过双栏会议录的 ACM 生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经存档核验的 PPoPP 论文，覆盖并行编程多种贡献形态，附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构 lock-free 索引研究的摘要与引言按 PPoPP 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的并行测量检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./PPoPP-Skills
claude plugin install ppopp-skills
```

也可直接使用文件：每个 `skills/ppopp-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 PPoPP 还是 CGO/PLDI/ASPLOS？” → `ppopp-topic-selection`
- “按 PPoPP research-track 规则审我的稿” → `ppopp-submission`
- “审稿人说不 scale —— 规划 rebuttal” → `ppopp-author-response`
- “把 artifact 准备到 PPoPP/CGO 徽章标准” → `ppopp-artifact-evaluation`

## 目录结构

```text
PPoPP-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面
├── skills/
│   └── ppopp-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `ppopp-topic-selection`；PPoPP 在边缘与 CGO/PLDI/ASPLOS 重叠，先确认并行性
   就是贡献。浏览 exemplars 看有持久影响的 PPoPP 结果长什么样。
2. **构建证据时** —— 让 `ppopp-experiments` 与 `ppopp-reproducibility` 贴着研究；可扩展性曲线与
   race-freedom 论证在机器不在后无法补做，硬件/拓扑须在运行时钉死记录。
3. **写作时** —— 用 `ppopp-writing-style` 对照 worked example 打磨双栏正文，用 `ppopp-supplementary`
   划分 10 页正文/artifact，用 `ppopp-related-work` 做 delta-first 定位。
4. **截止周** —— 先注册摘要，再用 `ppopp-submission` 对终稿 PDF 与 double-blind 逐项过审。
5. **投稿后** —— 用 `ppopp-review-process` 校准预期，用 `ppopp-author-response` 应对 rebuttal，随后
   `ppopp-artifact-evaluation` 与 `ppopp-camera-ready` —— 若结果不利，则用 `ppopp-topic-selection`
   的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- PPoPP 2026 为**第 31 届**：澳大利亚悉尼，**2026 年 1 月 31 日 – 2 月 4 日**，与 **HPCA/CGO/CC 2026**
  同周。全文投稿 **2025-09-01**；author response **2025-10-27 至 29**；通知 **2025-11-10**；artifact
  提交 **2025-11-17**；artifact 通知 **2026-01-05**；终稿 **2026-01-09**。
- PPoPP 2027 为**第 32 届**：美国盐湖城，**2027 年 3 月 20–24 日**，与 **HPCA/CGO/CC 2027** 同周；
  **夏季轮**投稿 **2026-08-03**（`ppopp27-summer.hotcrp.com`），author response **2026-10-06 至 08**，
  通知 **2026-10-26**。是否另有**秋季轮**为 待核实。这是 2026-07-09 时的下一个 live 目标。
- 格式：**双栏 `acmart` `sigplan`**，**10 页**正文含图，**参考文献不限**，摘要 **100–400 词**。
  评审：**double-blind** 加 **author-response rebuttal**。Artifact：**Functional/Reusable +
  Reproduced**（无 "Replicated"）；**Available** 经出版方授予。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如 10 页双栏篇幅、
   double-blind rebuttal、artifact 徽章政策）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如超出已具名 chairs 的完整组委名单、TPMS 使用）。
3. **核验期不可确定项** —— 明确标为 待核实（如 PPoPP 2027 秋季轮截止日、是否存在明确的 "Revision"
   决定类别、任何 AI 使用披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。PPoPP 每届重定结构 —— 包括一年是一轮还是两轮投稿（2027 的
  “summer” HotCRP 暗示分轮）—— 每年先在当前 Important Dates 页面核验 cadence。
- PPoPP 无常任 editor-in-chief；chairs 每届由 ACM SIGPLAN 任命轮换。
- 由于 PPoPP 与 CGO 共享同周与 artifact 文化，每个 cycle 需确认 AE track、截止日与徽章集是否联合
  运行、由哪个委员会负责。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
