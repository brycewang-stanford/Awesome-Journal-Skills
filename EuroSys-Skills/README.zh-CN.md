# EuroSys Skills（中文说明）

面向 **EuroSys —— European Conference on Computer Systems（欧洲计算机系统会议）** 投稿的
12 个 agent skills。EuroSys 是 ACM SIGOPS 欧洲分会（European Chapter of ACM SIGOPS）的
旗舰会议，属于顶级综合系统类会议。本包覆盖完整的 EuroSys 生命周期：判断项目是否
"EuroSys-shaped"、驾驭独特的**一届两轮投稿日历**（spring + fall 两个截稿、同一个四月
会议）、应对 HotCRP 双盲评审的三分支结果（**accept / revise-and-resubmit（即 one-shot revision）/ reject**），
以及把录用转化为 ACM camera-ready 与带 badge 的 **sysartifacts** artifact。

官方依据于 **2026-11-24 重新核验**（直接抓取）：EuroSys 2027 主页、Call for Papers 与
Organizing Committee 页，sysartifacts 上的 EuroSys 2027 artifact 页面，EuroSys 2026 主页，
以及 eurosys.org 的分会与 Test-of-Time 页面。最初 2026-07-08 的核验（另含 ACM DL 的 EuroSys
proceedings 与 dblp）因 `*.eurosys.org` 当时返回 HTTP 403，是通过搜索引擎渲染读取的；完整
证据链与全部 待核实 条目见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## EuroSys 与兄弟会议的关键差异

以下机制（均已核验）支撑了本包大部分建议，也是从 SOSP / OSDI / NSDI 习惯迁移过来的
作者最容易踩的坑：

- **两个评审轮次、一个四月会议。** 每届通过两轮独立投稿收稿（2027 届：spring 全文
  2026-05-14；fall 全文 2026-09-24），两批论文进入同一本 proceedings，同在 2027 年
  4 月 Rabat 报告。2027 两轮均已截稿；EuroSys 2028 的征稿尚未发布。
- **简短的作者回复。** 每轮在审稿意见发布几天后开放可选回复（2027 fall：2027-01-06 发布
  审稿意见、01-08 截止回复），只能更正事实错误、回答审稿人提问，不得加新实验，建议不超过
  500 词。
- **三分支结果。** 每篇投稿的结局是 accept（经 PC shepherd 批准修改稿前均为暂定录用）、
  reject，或带具体问题清单的 **revise-and-resubmit**——在下一轮提交修订版，不保证录用。
- **拒稿的代价是一年。** 某一轮被拒的论文，要到**下一届的同一轮**才能重投；仓促投稿
  的真实成本是一季加一年。
- **12 页技术内容，参考文献不限页。** CFP 推荐 SIGPLAN 模板（LaTeX 即
  `acmart[sigplan,twocolumn,review,anonymous]`），正文限于 178 x 229 mm 版心、字号 ≥10pt；
  可另交补充材料文件；每位作者每轮最多 3 篇投稿。
- **披露 AI 使用；ACM 开放获取。** 按 ACM 署名政策，任何 AI 工具的使用都须在投稿中完整披露；
  所在机构未加入 ACM Open 的作者需付 APC（2027 补贴价：会员 500 美元、非会员 750 美元）。
- **sysartifacts artifact evaluation。** 可选、录用通知后进行，三种 badge
  （Available / Functional / Reproduced，限三种组合），并设 Distinguished Artifact 奖
  （往届名为 Gilles Muller Best Artifact Award）。
- **有制度的社区。** 欧洲 SIGOPS 分会运营 Test-of-Time Award、Roger Needham PhD
  Award、Jochen Liedtke Young Researcher Award，还有培养未来审稿人的 Shadow PC。

## Skills 一览

| Skill | 作用 |
| --- | --- |
| [`eurosys-topic-selection`](skills/eurosys-topic-selection/SKILL.md) | 用四项实质门槛（built thing / 可迁移的 idea / 真实工作负载证据 / 可复述的 insight）检验项目，并在 EuroSys、SOSP、OSDI、NSDI、ASPLOS、ATC、FAST、SoCC 之间路由。 |
| [`eurosys-workflow`](skills/eurosys-workflow/SKILL.md) | 运营两闸门日历：按成熟度选 spring 或 fall，向 abstract 周倒排计划，在 accept / revision / reject 三分支间干净切换。 |
| [`eurosys-writing-style`](skills/eurosys-writing-style/SKILL.md) | 构建 "运维之痛 → 结构性缺口 → insight → 系统 → 有条件限定的数字" 叙事弧，分配 12 页预算，写出回答具名问题的 evaluation。 |
| [`eurosys-related-work`](skills/eurosys-related-work/SKILL.md) | 扫全系统会议圈（含 dblp 上 2006 年以来的 EuroSys 自身文献），陈述技术性 delta，处理 workshop / arXiv / 往轮投稿的谱系。 |
| [`eurosys-experiments`](skills/eurosys-experiments/SKILL.md) | 设计四层证据栈——end-to-end、分解、成本、边界——配合调优过的 baseline 与经得起 PC 默认怀疑的负载真实性。 |
| [`eurosys-reproducibility`](skills/eurosys-reproducibility/SKILL.md) | 为每个报告数字维护 provenance ledger，控制运行间方差，写出同时满足双盲评审与 AEC 的 availability 声明。 |
| [`eurosys-supplementary`](skills/eurosys-supplementary/SKILL.md) | 决定哪些内容离开 12 页正文——免费参考文献页、匿名 artifact 仓库、（若本轮允许的）附录——且不外移决定性证据。 |
| [`eurosys-artifact-evaluation`](skills/eurosys-artifact-evaluation/SKILL.md) | 选定 badge 组合，为陌生硬件上的评测者构建 artifact，铸造归档 DOI，以 Distinguished Artifact 奖（往届 Gilles Muller 奖）而非最低及格线为目标。 |
| [`eurosys-submission`](skills/eurosys-submission/SKILL.md) | 上传前的 HotCRP 终审：abstract 与全文两道闸门、页数预算、模板模式、身份泄露清扫、一稿多投与重投禁令检查。 |
| [`eurosys-review-process`](skills/eurosys-review-process/SKILL.md) | 建模两轮决策机器、三分支结果、重投禁令，以及真正能撬动系统类 PC 讨论的因素。 |
| [`eurosys-author-response`](skills/eurosys-author-response/SKILL.md) | 把评审意见按结果分箱，写出能改变分数的 rebuttal，把 revision 条件清单转成可执行计划。 |
| [`eurosys-camera-ready`](skills/eurosys-camera-ready/SKILL.md) | 模板退出匿名模式、走通 ACM eRights 与元数据流程、把 badge 挂到终版 PDF、规划 Rabat 现场报告。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十二个官方来源（URL + 核验日期）、已核验的 2027 周期事实、访问方式说明、显式 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及上传前必跑的五个作者侧检查 pass。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 从 Dryad（EuroSys '07）到 CacheBlend（EuroSys '25）的获奖级范文，各配定位要点与自检问题，另附系统领域经典论文的"防误归属"清单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构 LSM compaction 论文的摘要与引言 before → after 重写，示范 EuroSys 叙事弧。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享复现工具包的适配器，外加四项通用工具管不到的 EuroSys 专属检查（badge、硬件诚实性、匿名、溯源）。 |

## 安装与使用

作为 Claude Code plugin（本目录自带 marketplace manifest，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./EuroSys-Skills
claude plugin install eurosys-skills
```

也可以直接使用文件：每个 `skills/eurosys-*/SKILL.md` 都是独立指令文件，frontmatter 的
`description` 告诉 agent 何时触发。典型用法：

- "这篇调度器论文投 EuroSys 还是 SOSP？" → `eurosys-topic-selection`
- "目标是 fall 截稿，帮我排计划" → `eurosys-workflow`
- "注册 abstract 之前把 PDF 过一遍" → `eurosys-submission`
- "拿到 revise-and-resubmit 了，下一步？" → `eurosys-author-response`
- "把集群实验打包给 AEC" → `eurosys-artifact-evaluation`

## 目录结构

```text
EuroSys-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                    # 英文说明
├── README.zh-CN.md              # 本文件
├── LICENSE                      # MIT
├── assets/cover.svg             # 封面
├── skills/
│   └── eurosys-<topic>/SKILL.md # 12 个 skills，一目录一技能
└── resources/
    ├── README.md                # 资源导览与推荐路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md           # 共享复现工具包适配器
```

## 2027 周期锚点事实（历史快照，非永久规则）

- EuroSys 2027：**摩洛哥 Rabat，2027 年 4 月**（官网同时写有 4 月 19—22 日与 4 月 19 至 23 日，
  结束日期 待核实）；EuroSys 2026 为第 21 届，英国爱丁堡，2026-04-27 至 04-30。EuroSys 2028：
  2026-11-24 尚无征稿。
- Spring 轮（已结束）：abstract **2026-05-07**、全文 **2026-05-14**，回复截止 07-31，通知
  **2026-08-21**，camera-ready **2026-09-25**。
- Fall 轮（评审中）：abstract **2026-09-17**、全文 **2026-09-24**（AoE），审稿意见
  2027-01-06，回复截止 01-08，通知 **2027-01-29**，camera-ready **2027-03-05**。
- 排版：**12 页技术内容 + 参考文献不限页**；SIGPLAN 模板（`acmart[sigplan,twocolumn,review,anonymous]`）；
  178 x 229 mm 版心，双栏间距 ≥ 8 mm；双盲；每位作者每轮最多 3 篇。
- 结果：accept（shepherd）/ **revise-and-resubmit**（问题清单、下一轮）/ reject（不得投紧接着的下一轮）。
- 主席：General Chairs Rachid Guerraoui、Rafael Pires；PC Chairs Pramod Bhatotia、Lydia Chen、
  Andreas Haeberlen。
- 投稿入口：`eurosys27-spring.hotcrp.com` / `eurosys27-fall.hotcrp.com`；proceedings 进
  ACM DL（开放获取）；artifact 走 sysartifacts，badge 为 Available / Functional / Reproduced。

## 推荐路线

1. **动笔之前**：先跑 `eurosys-topic-selection` 做实质门槛与路由判断——EuroSys 拒稿
   附带一年同轮禁投，选错闸门的成本是真实的；再用 `eurosys-workflow` 锁定 spring 或
   fall 目标并倒排计划。
2. **搭系统、跑实验期间**：`eurosys-experiments` 的四层证据栈与
   `eurosys-reproducibility` 的 provenance ledger 越早装上越便宜；评测矩阵入库管理。
3. **写作期间**：正文用 `eurosys-writing-style`，定位用 `eurosys-related-work`，
   超页分流用 `eurosys-supplementary`，并对照 worked example 的 before → after。
4. **截稿周**：`eurosys-submission` 从 abstract 闸门到身份清扫全程走一遍，再按
   `resources/external_tools.md` 的五个 pass 收尾。
5. **通知之后**：按 `eurosys-review-process` 分箱，rebuttal 或 revision 走
   `eurosys-author-response`，录用后 `eurosys-camera-ready` 与
   `eurosys-artifact-evaluation` 双线并行、各设 owner。

## 事实纪律

本包把三类陈述明确区分：

1. **已核验的周期事实**——能追溯到 source map 的编号来源（截稿、页数、结果政策）。
2. **转述事实**——仅见于二手渲染并明确标注（录用数量）。
3. **待核实条目**——一律写成待解决的问题而非事实（2027 结束日期、fall 轮 artifact 日期、
   camera-ready 页数、EuroSys 2028 的一切信息）。

若发现任何 skill 把第 2、3 类当第 1 类陈述，请视为 bug，并对照官方页面修正。

## 维护说明

- 上述所有日期都是 **2027 周期快照**：给出任何截稿敏感建议前，先重开
  `202N.eurosys.org` 与当轮 HotCRP 实例。
- EuroSys 的政策按届、按轮设定；rebuttal、附录、camera-ready 的假设不可跨轮沿用。
- 会议主席逐届轮换；稳定的是分会（eurosys.org），多变的是各届会议站点。
- 新增范文请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾
  的双来源核验流程；系统领域的经典论文极易被归错会议。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
