# ATC Skills

面向 **ATC —— ACM SIGOPS Annual Technical Conference** 论文的 12 个 agent skills。该会议约五十年间
名为 **USENIX Annual Technical Conference（USENIX ATC）**，自 2026 届起转由 **ACM SIGOPS** 主办。
ATC 是系统社区**综合、务实**的会议：相比 OSDI/SOSP 这类更挑剔的旗舰会，它覆盖更宽的计算机系统面，
看重真实实现与实验结果，并设有专门的 **Deployed Systems（部署系统／经验）** 通道。本包覆盖一次 ATC
投稿的完整流程：判断项目属于 ATC 还是应投 OSDI、NSDI、EuroSys、FAST 或 workshop；应对**新的两轮
扩展摘要评审**；准备 double-blind 的 HotCRP 匿名投稿；处理**条件录用与 shepherding**；直到完成
camera-ready 与获得 USENIX 传承的 artifact 徽章。

官方依据核验日期：**2026-07-09**。已核验 ATC 2026 SIGOPS call 与主页、ATC 2026 HotCRP、USENIX
ATC '25 的 research 与 artifact call、USENIX 转 SIGOPS 的交接记录、ACM SIGOPS 会议列表及 dblp。
核验环境中直接抓取 `sigops.org`、`usenix.org` 与聚合站点返回 403，因此通过搜索引擎对精确 URL 的渲染
阅读官方页面，并与 USENIX ATC '25 页面、Wikipedia 历史条目及 dblp 交叉核对；完整记录（含所有 待核实
项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

> 缩写冲突提醒：**ATC** 也指 *American Transplant Congress* 与某 *Academic Tax Conference*，
> **都不是**本 ATC。本包事实均不来自它们。本 ATC 是计算机系统会议。

## ATC 与同类会议的区别

以下会议机制（按 2026 cycle 核验）驱动了 skills 中的大部分建议，也对应了从 OSDI/SOSP、NSDI 或旧版
USENIX ATC 转投作者最常犯的错误：

- **主办方、名称与日历刚刚同时改变。** ATC 2026 是约五十年 USENIX ATC 之后的**首届 ACM SIGOPS**
  版本。保留缩写，移至**香港沙田凯悦，2026 年 11 月 15-18 日**，改为**六月截止**（打破旧的冬季
  截止／夏季开会节奏），并转为 **ACM Open Access**。不要沿用 2026 前的 USENIX 假设。
- **两轮、扩展摘要评审。** 每篇投稿随全文上传**两页扩展摘要**。第一轮：两名有经验审稿人评判摘要，
  提前淘汰不达标论文。第二轮：3-4 名审稿人阅读全文。扩展摘要**仅供评审、不出版**，且须能独立成立。
- **“综合”正是要点。** ATC 覆盖 OS、存储、网络、虚拟化、分布式系统、性能、可靠性、能耗与故障排查，
  “从嵌入式设备到云的各种规模”，强调**实现与实验结果**。旗舰会可能视为增量的扎实有用工作在这里在范围内。
- **部署系统／经验论文是一等公民。** 专设通道接收关于真实部署系统的论文，**无需提出新想法** ——
  以实践洞见评判。（SIGOPS 下该通道是否延续为 待核实。）
- **先 double-blind，后 shepherd。** 评审 double-blind；录用论文为**条件录用**，须通过 **shepherd**
  方可最终录用。
- **USENIX 传承的 artifact 徽章。** artifact 由 Artifact Evaluation Committee 在录用后单独排期评定
  **Available / Functional / Reproduced** 徽章 —— 参与度很高的活跃文化（ATC '25：94% Functional，
  77% Reproduced）。
- **开放获取的新变化。** USENIX ATC 免费公开 proceedings、slides 与报告视频；SIGOPS 版本改为
  **ACM Open Access**，并有过渡期补贴 APC。

## Skills

| Skill | 作用 |
| --- | --- |
| [`atc-topic-selection`](skills/atc-topic-selection/SKILL.md) | 在 ATC 与同类会议（OSDI、SOSP、NSDI、EuroSys、FAST、HotOS/workshop）间选路，用综合性 vs 挑剔性、部署系统测试与日历判断。 |
| [`atc-workflow`](skills/atc-workflow/SKILL.md) | 从六月截止倒排年度计划，经两轮评审、rebuttal、条件录用 shepherding、artifact 评审与 ACM camera-ready。 |
| [`atc-writing-style`](skills/atc-writing-style/SKILL.md) | 构建系统论文：可独立成立的两页扩展摘要、实现-测量叙事、两栏格式下的篇幅纪律。 |
| [`atc-related-work`](skills/atc-related-work/SKILL.md) | 覆盖系统文献 lane，对照 OSDI/NSDI/EuroSys/FAST 定位，并保持自引 double-blind。 |
| [`atc-experiments`](skills/atc-experiments/SKILL.md) | 让证据匹配论断：真实 testbed、诚实 baseline、端到端加 microbenchmark、尾延迟与方差、负载真实性。 |
| [`atc-reproducibility`](skills/atc-reproducibility/SKILL.md) | 构建 artifact 证据：钉死环境、通往关键数字的一键路径、匿名可运行的评审包。 |
| [`atc-supplementary`](skills/atc-supplementary/SKILL.md) | 按评审轮次与决策重要性划分扩展摘要、正文、附录与 artifact。 |
| [`atc-submission`](skills/atc-submission/SKILL.md) | HotCRP 终审：摘要+全文配对上传、两栏篇幅、double-blind 清扫、AoE 截止前的 desk-reject 分诊。 |
| [`atc-review-process`](skills/atc-review-process/SKILL.md) | 建模流程 —— 两轮、扩展摘要门槛、第二轮 3-4 审稿人、rebuttal、条件录用、shepherding —— 及作者杠杆点。 |
| [`atc-author-response`](skills/atc-author-response/SKILL.md) | 撰写 rebuttal 与 shepherd 会逐条核对的 description-of-changes。 |
| [`atc-artifact-evaluation`](skills/atc-artifact-evaluation/SKILL.md) | 在 AEC 自身截止日，将录用论文的包转化为 Available / Functional / Reproduced 徽章。 |
| [`atc-camera-ready`](skills/atc-camera-ready/SKILL.md) | 去匿名、完成 shepherd 要求的修改、补全 ACM Open Access 元数据、通过生产检查。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个带 URL 与访问日期的来源；已核验 2026 事实；访问方式说明；明确的 待核实 清单（含转型带来的不确定项）。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口（SIGOPS CFP、ATC HotCRP、USENIX 遗留页、ACM DL）与网关阻断时的交叉核对来源。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 经核验的 USENIX ATC 论文，覆盖多种贡献形态（含 Test-of-Time 与 Best Paper），附自检问题与同类会议护栏。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构存储缓存论文的扩展摘要+引言按 ATC 弧线重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享 replication-package 工具，并给出通用套件无法完成的 ATC 专用检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace manifest 的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./ATC-Skills
claude plugin install atc-skills
```

也可直接使用文件：每个 `skills/atc-*/SKILL.md` 都是独立指令文件，其 frontmatter `description`
告诉 agent 何时触发。典型调用：

- “这篇该投 ATC 还是 OSDI/NSDI？” → `atc-topic-selection`
- “按 ATC 2026 规则审我的稿” → `atc-submission`
- “把扩展摘要写到能过第一轮” → `atc-writing-style`
- “拿到条件录用 —— 规划 shepherd 修改” → `atc-author-response`
- “把 artifact 准备到 ATC 徽章标准” → `atc-artifact-evaluation`

## 目录结构

```text
ATC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── atc-<topic>/SKILL.md  # 12 个 skill，各一目录
└── resources/
    ├── README.md
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md
```

## 建议用法

1. **动笔前** —— 先跑 `atc-topic-selection`；ATC 与 OSDI/NSDI/EuroSys/FAST 重叠，综合性 vs 挑剔性
   的取舍与六月日历很重要。浏览 exemplars 看有持久影响力的 ATC 贡献长什么样。
2. **构建证据时** —— 让 `atc-experiments` 与 `atc-reproducibility` 贴着系统；testbed provenance
   与钉死的环境无法在投稿期补救。
3. **写作时** —— 用 `atc-writing-style` 打磨可独立成立的扩展摘要与正文，用 `atc-supplementary`
   划分摘要/正文/附录/artifact，用 `atc-related-work` 做同类会议感知的定位。
4. **截止周** —— 用 `atc-submission` 对摘要+全文配对上传与 double-blind 清扫逐项过审，赶在六月 AoE
   截止前完成。
5. **投稿后** —— 用 `atc-review-process` 校准两轮预期，用 `atc-author-response` 应对 rebuttal 与
   shepherd 的 description-of-changes，随后 `atc-artifact-evaluation` 与 `atc-camera-ready` ——
   若结果不利，则用 `atc-topic-selection` 的路由表改投。

## 2026 周期锚点事实（历史快照，非永久规则）

- ATC 2026 为**首届 ACM SIGOPS Annual Technical Conference**（前 USENIX ATC）：**中国香港（沙田
  凯悦），2026 年 11 月 15-18 日**。投稿截止**2026 年 6 月上旬**（AoE；6 月 1 日 vs 6 月 10 日
  在不同渲染间不一致 —— 待核实）。
- **两轮评审：**两页扩展摘要（仅评审、不出版）经两名审稿人把关，再由 3-4 名审稿人评全文。全文
  **≤12 页**、short **≤6 页**（不含参考文献/附录）；**两栏**，178×229 mm，10pt。**Double-blind。**
  **条件录用 + shepherding。** HotCRP：`atc26.hotcrp.com`。
- **Artifact：**Available / Functional / Reproduced 徽章，由 AEC 在录用后单独排期评定。
  **出版：**ACM Open Access（过渡期补贴 APC）。

## 事实纪律

本包区分三类陈述，skills 的写法保持其可区分：

1. **已核验 2026 事实** —— 带日期/篇幅并追溯到 source map 中的编号来源（如两轮模型、12/6 页篇幅、
   三个 artifact 徽章）。
2. **转述事实** —— 仅经二手渲染读到并如实标注（如投稿数量与具体 APC 数额）。
3. **核验期不可确定项** —— 明确标为 待核实（如六月的具体日期、强制模板文件、部署系统通道是否延续、
   chair 名单、任何 AI 披露政策）。

若任何陈述以第 1 类口吻呈现第 2/3 类内容，视为 bug，对照官方页面修正。

## 维护说明

- ATC 2026 是**转型届**；名称、主办方、出版方、日历与评审结构同时变动。每项都要对照当前 SIGOPS call
  重新核验 —— 尚无一项是稳定永久规则。
- ATC 无常任 editor-in-chief；chairs 每届在 SIGOPS 下轮换。USENIX 遗留的 ATC proceedings、slides
  与视频仍在 USENIX 站点；新版本在 ACM DL 以 Open Access 出版。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 —— 著名系统
  名并不能证明该论文发表于 ATC（许多里程碑系统论文在 OSDI/SOSP/NSDI，而非 ATC）。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
