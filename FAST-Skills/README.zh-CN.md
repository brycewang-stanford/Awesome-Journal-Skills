# USENIX FAST Skills

面向 **FAST —— USENIX Conference on File and Storage Technologies** 论文的 12 个 agent skills。FAST 是
USENIX 社区的存储系统旗舰会议，其身份完全围绕*存储*：文件系统、SSD/NVM 与闪存、键值与对象存储、缓存、
存储可靠性与耐久性、崩溃一致性，以及支撑这一切的真机测量。本包覆盖一次 FAST 投稿的完整流程：判断项目
属于 FAST 还是应投 OSDI、ATC、NSDI、EuroSys、HotStorage、MSST 或 ACM TOS；构建能经受存储审稿人审视的
存储证据（工作负载 trace、写放大、尾延迟、磨损/耐久、崩溃一致性测试、老化）；为 FAST 的**两个年度截止日**
之一准备 double-blind 的 HotCRP 投稿；应对 USENIX 评审、**author response**、shepherding 与 **one-shot
revision**；直到完成免费开放获取的 camera-ready 与获得 USENIX artifact 徽章。

官方依据核验日期：**2026-07-09**。已核验 FAST '26 与 FAST '27 的 Call for Papers 与 Important Dates、
FAST double-blind guidance、FAST '27 Call for Artifacts、USENIX Test-of-Time 与 Best-Paper 页面，以及
FAST HotCRP 站点。核验环境中直接抓取 `usenix.org` 与 `dl.acm.org` 返回 403，因此通过搜索引擎对精确 URL
的渲染阅读官方页面，并与 dblp（`conf/fast`）、ACM Digital Library 对 USENIX proceedings 的镜像及 FAST
HotCRP 交叉核对；完整记录（含所有 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

> 缩写冲突提醒：“FAST” 亦被其他社区复用（如某 IEEE/AST 软件测试研讨会及若干领域缩写）。本包仅指 **USENIX**
> File and Storage Technologies 会议（`usenix.org/conference/fastNN`，dblp `conf/fast`）。本包中的事实
> 均不来自同名活动。

## FAST 与同类会议的区别

以下会议机制（按 2026/2027 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 OS/系统会议、数据库会议
或体系结构会议转投作者最常犯的错误：

- **它是存储专门化的 USENIX 旗舰。** 审稿人都是存储人。论文的真实贡献必须落在*存储*语汇上 —— 文件系统、
  设备、键值、缓存或可靠性的教训 —— 而非只是碰到磁盘的通用系统结果。出色的调度或网络论文会被尊重，然后
  被路由到 OSDI/ATC/NSDI。
- **每年两个截止日。** FAST 设 **Spring** 与 **Fall** 两个截止日（FAST '27：2026-03-17 与 2026-09-15，
  AoE）。错过一个不等于损失一年 —— 另一个 on-ramp 就在数月之后 —— 这改变了相对单一年度截止日会议的日历策略。
- **USENIX double-blind，而非 ACM 的 “heavy” 匿名。** 匿名 PDF 与参考文献，并以第三人称写自己的先前工作；
  通知前有 **author-response** 期。这是 USENIX 模型，区别于仅 camera-ready 匿名的会议或期刊 R&R 回复信。
- **One-shot revision，而非开放式 R&R。** 除 accept/reject 外，FAST 还给 **accept-with-shepherding** 与
  **one-shot revision**。one-shot revision 的指令可要求*特定的新实验*；修订稿在下一个截止日重交，此后只能
  accept 或 reject。要把它当作第二个完整截止日来预算。
- **USENIX proceedings，免费开放，无 APC。** 论文由 USENIX 开放获取出版、无 article-processing charge；
  USENIX 双栏模板与**正文 12 页（long）/ 6 页（short）、参考文献不计入**界定篇幅 —— 不是 ACM `acmart`
  或 IEEE 10+2。
- **USENIX artifact 三徽章。** 录用后由 AEC 评定 **Artifacts Available / Artifacts Functional /
  Results Reproduced**，显示在首页 —— USENIX 三徽章方案，而非 ACM 四徽章。
- **存储证据文化。** 真机与固件、标准工作负载与 trace（SNIA IOTTA、YCSB、filebench、fio、block trace）、
  写放大、尾延迟、耐久与磨损、崩溃一致性测试、老化，是存储审稿人即便无明文也会执行的社区规范。

## Skills

| Skill | 作用 |
| --- | --- |
| [`fast-topic-selection`](skills/fast-topic-selection/SKILL.md) | 在 FAST 与同类会议（OSDI、ATC、NSDI、EuroSys、HotStorage、MSST、SYSTOR、ACM TOS）之间选路，用存储贡献形态、storage-lesson 测试与两截止日日历判断。 |
| [`fast-workflow`](skills/fast-workflow/SKILL.md) | 从选定的 Spring/Fall 截止日倒排两截止日年度计划，经 double-blind 投稿、author response、shepherding 或 one-shot revision、artifact 评审与开放获取 camera-ready。 |
| [`fast-writing-style`](skills/fast-writing-style/SKILL.md) | 构建存储系统骨架：首页给出存储问题、设计/机制叙事、回答“真机上代价几何”的评估、USENIX 篇幅纪律。 |
| [`fast-related-work`](skills/fast-related-work/SKILL.md) | 覆盖存储文献 lane（FAST/OSDI/ATC/EuroSys/HotStorage/MSST/TOS），写 delta-first 定位，并保持自引 double-blind。 |
| [`fast-experiments`](skills/fast-experiments/SKILL.md) | 存储评估核心：真机与固件、标准 trace 与工作负载、写放大、尾延迟、耐久/磨损、崩溃一致性测试、老化、公平 baseline。 |
| [`fast-reproducibility`](skills/fast-reproducibility/SKILL.md) | 构建存储可复现性：钉死设备型号、固件与 trace 出处；说明读者在会老化且个体差异的硬件上重建结果所需之物。 |
| [`fast-supplementary`](skills/fast-supplementary/SKILL.md) | 按决策重要性划分正文与 artifact，使用“参考文献不计入”的篇幅与 USENIX double-blind 规则。 |
| [`fast-submission`](skills/fast-submission/SKILL.md) | HotCRP 终审：选 Spring/Fall、注册摘要、满足 USENIX 模板与 12/6 页、清扫 double-blind 泄漏、给出 artifact 可用性叙事、desk-risk 分诊。 |
| [`fast-review-process`](skills/fast-review-process/SKILL.md) | 建模流程 —— double-blind PC 评审、外部 referee、author response、shepherding、one-shot revision —— 及作者杠杆点。 |
| [`fast-author-response`](skills/fast-author-response/SKILL.md) | 撰写两轮：通知前短 rebuttal，与把每条必需修改（含新实验）映射到具体结果的 one-shot-revision 变更清单。 |
| [`fast-artifact-evaluation`](skills/fast-artifact-evaluation/SKILL.md) | 将录用论文的包转化为 USENIX 徽章（Available / Functional / Reproduced），处理需特定硬件、大 trace 或长耐久运行的存储 artifact。 |
| [`fast-camera-ready`](skills/fast-camera-ready/SKILL.md) | 去匿名、套用较大的 camera-ready 篇幅与 USENIX 模板、永久化 trace/代码可用性、加 artifact appendix 与徽章、赶 final-files 截止日。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026/2027 事实；访问方式说明；明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与网关阻断时的交叉核对来源，以及作者端核查清单。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经存档核验的 FAST 论文，覆盖五种存储贡献形态（含 Test-of-Time 与 Best Paper），附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构 SSD 键值研究的摘要与引言按 FAST 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的存储专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./FAST-Skills
claude plugin install fast-skills
```

也可直接使用文件：每个 `skills/fast-*/SKILL.md` 都是独立指令文件，其 frontmatter `description` 告诉
agent 何时触发。典型调用：

- “这篇该投 FAST 还是 OSDI/ATC？” → `fast-topic-selection`
- “按 FAST CFP 在 Fall 截止日前审我的稿” → `fast-submission`
- “拿到 one-shot revision —— 规划重交” → `fast-author-response`
- “把存储 artifact 准备到 USENIX 徽章标准” → `fast-artifact-evaluation`

## 目录结构

```text
FAST-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面
├── skills/
│   └── fast-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `fast-topic-selection`；FAST 与 OSDI/ATC/EuroSys 高度重叠，按存储社区取向与更近的
   那个截止日选择很重要。浏览 exemplars 看十年影响力的 FAST 贡献长什么样。
2. **构建证据时** —— 让 `fast-experiments` 与 `fast-reproducibility` 贴着 testbed；测量期钉死的设备型号、
   固件与 trace 出处无法事后补救。
3. **写作时** —— 用 `fast-writing-style` 对照 worked example 打磨正文，用 `fast-supplementary` 划分
   正文/artifact，用 `fast-related-work` 做 delta-first 定位。
4. **截止周** —— 选 Spring 或 Fall，尽早注册摘要，再用 `fast-submission` 对终稿 PDF 逐项过审。
5. **投稿后** —— 用 `fast-review-process` 校准预期，用 `fast-author-response` 应对 rebuttal 与任何
   one-shot revision，随后 `fast-artifact-evaluation` 与 `fast-camera-ready` —— 若结果不利，则用
   `fast-topic-selection` 的路由表改投。

## 2026/2027 周期锚点事实（历史快照，非永久规则）

- FAST '26 为**第 24 届**：美国 Santa Clara（Hyatt Regency Santa Clara），**2026 年 2 月 24-26 日**。
  设两个截止日（Spring 2025-03-18，Fall 2025-09-16），并引入 one-shot revision。
- FAST '27 为**第 25 届**：美国 Santa Clara，**2027 年 2 月 23-25 日**；两个截止日 —— **Spring
  2026-03-17** 与 **Fall 2026-09-15**（AoE）。投稿篇幅 **正文 12 页（long）/ 6 页（short），参考文献
  不计入**。2026-07-09 时的 live 可行目标是 **Fall 截止日，2026-09-15**。
- 出版：**USENIX 开放获取**，免费，无 APC。评审：**double-blind** 且有 author response。决定：Accept /
  Accept-with-shepherding / **One-shot Revision** / Reject。模板：**USENIX 双栏**。Artifact：**Available
  / Functional / Reproduced**。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026/2027 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如两截止日、12/6 页篇幅、
   one-shot-revision 规则、三 USENIX 徽章）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如具体酒店与 CFP 未具名的组委名单）。
3. **核验期不可确定项** —— 明确标为 待核实（如 FAST '27 Program Co-Chair 与 AEC 名单、AEC 匿名模型、
   任何 AI 使用披露政策、确切举办城市）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- 以上日期与篇幅都是**周期快照**。FAST 每届重定结构 —— 包括截止日数量与 revision 机制 —— 每年先核验
  cadence。
- FAST 无常任 editor-in-chief、无 APC；chairs 与 AEC 每届轮换。对**人**做连续性假设视为错误。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  核验流程 —— 熟悉的存储工具名并不能证明该论文发表于 FAST（许多其实在 OSDI、ATC、EuroSys 或 SOSP）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
