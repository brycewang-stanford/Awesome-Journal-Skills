# ASPLOS Skills（中文说明）

面向 **ASPLOS — ACM International Conference on Architectural Support for
Programming Languages and Operating Systems** 的 12 个 agent skills。ASPLOS 由
ACM SIGARCH、SIGPLAN、SIGOPS 三个 SIG 联合主办，是横跨硬件与软件的多学科系统研究
顶会。本包覆盖一次完整 ASPLOS 战役的全弧线：证明工作真正落在
architecture-PL-OS 交叉点上、用 simulator / FPGA / 真实硅片构建硬件级证据、
通过只读前两页的 rapid review 筛选、驾驭一年两个 deadline 加 Major Revision
通道的投稿周期，以及把录用转化为带 ACM artifact badges 的正式出版物。

官方依据核验日期：**2026-07-08**。已核验 ASPLOS 2027 Call for Papers、载有 2027
时间线的会议主站、April cycle 的 HotCRP deadline 页、artifact evaluation 各页、
ACM DL 上第 30/31 届 proceedings，以及 SIGARCH/SIGPLAN/SIGOPS Influential Paper
Award 页面。核验环境无法直接抓取 `asplos-conference.org`、HotCRP 与 dblp（网关
返回 403），因此官方页面内容通过搜索引擎对精确 URL 的渲染读取，并与 ACM
Digital Library 和 SIGARCH 帖子交叉核对；完整证据链与所有 待核实 条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## ASPLOS 与相邻会议的关键差异

以下 2027 周期机制驱动了各 skill 中的大部分建议，也是从单一社区会议转投过来的
作者最容易踩的坑：

- **交叉点是入场券。** ASPLOS 征集 OS、PL、体系结构*及其交叉*的工作，且 rapid
  review 明确优先交叉点论文。干净的单社区论文应改投 ISCA/MICRO、PLDI/POPL 或
  SOSP/OSDI。
- **一届两个 deadline，不是一个也不再是三个。** ASPLOS 2027 在 2026 年 4 月 15
  日与 9 月 9 日（均 AoE，无摘要注册截止）收稿，取代了近年三轮制。截至本包核验
  日，April cycle 的 author response 窗口（2026-07-06 至 07-09）正在进行中。
- **只读两页的 rapid review。** 第一轮筛选只看每篇投稿的前两页（双盲），多数
  投稿可能止步于此。前两页是生存器官，需要单独工程化。
- **Major Revision 是真实结局。** 除 Accept / Reject 外，部分论文获得修改通道：
  在 notification 后六周的 camera-ready deadline 提交修改稿，且该修改稿本身
  计为一次投稿记录。
- **Rebuttal 有注意力预算。** 无硬性字数上限，但审稿人不被期望阅读超过 800
  词；CFP 将 rebuttal 的职责限定为纠正事实错误与回答审稿人问题。
- **参考文献规则带牙齿。** 参考文献不计入 11 页正文，但每条必须写出所有合作者
  完整的名与姓（禁止 "et al."），正文引用编号需超链接到条目，并附 DOI。
- **Artifact 文化与 ACM badges。** 录用后的 artifact evaluation 是 ASPLOS
  传统：`ae.tex` 模板的 Artifact Appendix、协作式评审委员会，以及 Available /
  Functional / Reproducible 三枚徽章（Available 要求公开的归档仓库）。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`asplos-topic-selection`](skills/asplos-topic-selection/SKILL.md) | 用跨层删除测试判定去留，在 ASPLOS 与 ISCA/MICRO/HPCA、PLDI/POPL、SOSP/OSDI/EuroSys、SC、MLSys 之间路由，并按证据成熟度选择 deadline。 |
| [`asplos-workflow`](skills/asplos-workflow/SKILL.md) | 运营两闸门的 2027 日历：9 月 9 日倒计时、按风险分派 owner、为录用/修改/两类拒稿分别准备分支预案。 |
| [`asplos-writing-style`](skills/asplos-writing-style/SKILL.md) | 为 rapid review 工程化第 1-2 页，提炼一句话跨层洞见，分层组织机制章节，在含图表脚注的 11 页内做图预算。 |
| [`asplos-related-work`](skills/asplos-related-work/SKILL.md) | 同时覆盖三个社区的五条文献线，用边界位置而非组件差异做区分，按 2027 双盲规则处理自引与 arXiv。 |
| [`asplos-experiments`](skills/asplos-experiments/SKILL.md) | 让每条 claim 匹配其证据仪器——真实硅片、FPGA、simulator——并声明 cycle-accuracy 局限、调优过的强 baseline、分层 ablation 与诚实的失利结果。 |
| [`asplos-reproducibility`](skills/asplos-reproducibility/SKILL.md) | 按结果捕获机器/模拟器/固件状态，脚本化采集，为评审者可能没有的硬件写三档可获得性声明。 |
| [`asplos-supplementary`](skills/asplos-supplementary/SKILL.md) | 在"自包含的 11 页"与"审稿人不被要求阅读的附录"之间切分内容；用匿名补充材料处理无法引用的自有工作。 |
| [`asplos-artifact-evaluation`](skills/asplos-artifact-evaluation/SKILL.md) | 撰写 `ae.tex` Artifact Appendix，瞄准三枚徽章，搭建评审者可盲走的包结构，为硬件依赖的 claim 准备替代路径。 |
| [`asplos-submission`](skills/asplos-submission/SKILL.md) | 上传前终审：11 页几何、强制模板、全名+DOI 引用格式、匿名清扫、GenAI 披露、AoE 截止前确认 HotCRP 状态为 complete。 |
| [`asplos-review-process`](skills/asplos-review-process/SKILL.md) | 建模分阶段流水线——rapid 筛选、正式评审、author response、Accept/Major Revision/Reject——并定位每阶段作者的真实杠杆。 |
| [`asplos-author-response`](skills/asplos-author-response/SKILL.md) | 把评审意见分入 CFP 认可的类别，按 800 词阅读预算行文，只用已提交证据作答，并主动开出修改条款。 |
| [`asplos-camera-ready`](skills/asplos-camera-ready/SKILL.md) | 六周内把 decision 变成可出版的 ACM 论文：去匿名 diff、版权表格、修改稿的 change note、徽章与 artifact 集成。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个官方来源（URL + 2026-07-08 访问日期）、已核验的 2027 周期事实、显式 待核实 清单、网关访问方式说明。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，外加上传前的五个作者侧核验流程（几何、引用、匿名、两页、HotCRP 状态）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经 Influential Paper Award 验证的 ASPLOS 论文，按贡献"形状"组织，各配自检问题与场馆归属防误配指南。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构 CXL 分层内存论文的摘要+引言改写（before → after），目标是通过两页 rapid review。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享复现工具包的适配器，外加通用工具做不了的四项硬件检查（模拟器钉版、硬件依赖、固件状态、徽章映射）。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace manifest，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./ASPLOS-Skills
claude plugin install asplos-skills
```

也可以直接使用文件：每个 `skills/asplos-*/SKILL.md` 都是独立指令文件，其
frontmatter `description` 告诉 agent 何时触发。典型问法：

- "这篇加速器论文投 ASPLOS 还是 ISCA？" → `asplos-topic-selection`
- "9 月截止前帮我红队审一遍前两页" → `asplos-writing-style`
- "拿到 Major Revision 了，怎么规划这六周？" → `asplos-review-process` + `asplos-camera-ready`
- "把 gem5 实验打包送 artifact evaluation" → `asplos-artifact-evaluation`

## 包结构

```text
ASPLOS-Skills/
├── .claude-plugin/             # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                   # 英文说明
├── README.zh-CN.md             # 本文件
├── LICENSE                     # MIT
├── assets/cover.svg            # 封面
├── skills/
│   └── asplos-<topic>/SKILL.md # 12 个 skill，一目录一文件
└── resources/
    ├── README.md               # 资源导览 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md          # 共享复现工具包适配器
```

## 2027 锚点事实（单周期快照，非永久规则）

- ASPLOS 2027：**希腊克里特岛伊拉克利翁，2027 年 4 月 11-15 日**。ASPLOS 2026
  为第 31 届（ACM DL），2026 年 3 月 22-26 日于匹兹堡举行；2025 年第 30 届
  （鹿特丹）是首次 ASPLOS-EuroSys 联合会议。
- 投稿截止：**2026-04-15** 与 **2026-09-09**，均 11:59 PM AoE，HotCRP 提交
  （每周期一个站点），无摘要截止。
- April cycle：response 2026-07-06 至 07-09；notification 2026-07-27。
  September cycle：response 2026-12-01 至 12-04；notification 2026-12-21。
- 格式：正文（含全部文字、图、表、脚注）≤ **11 页**、单倍行距双栏；参考文献
  不计页且不限量；模板强制；附录允许但审稿人不被要求也不被鼓励阅读。
- 评审：双盲；先经**两页 rapid review**；rebuttal 阅读预期约 **800 词**；
  结局为 Accept / **Major Revision**（notification 后六周提交，计为一次投稿）
  / Reject。
- Artifact：录用后评审；徽章 **Available / Functional / Reproducible**；
  Artifact Appendix 用 `ae.tex`。

## 事实纪律

本包始终区分三类陈述：

1. **已核验的 2027 周期事实**——带日期/上限，可追溯到 source map 的编号来源
   （如 11 页规则、9 月 9 日截止）。
2. **推导或二手事实**——明确标注（如"第 32 届"系由 ACM DL 第 31 届标题推算，
   非官方抓取的届数）。
3. **核验时不可得的条目**——标 待核实 并写成待解决的问题（如 camera-ready
   页数、2027 届主席、参会要求、AE 日程）。

若发现任何 skill 把第 2、3 类内容写成第 1 类，请视为 bug 并对照官方页面修正。

## 维护说明

- 上文所有日期与上限均为 **2027 周期快照**。deadline 结构本身在 2026 与 2027
  之间已经变过一次（三轮 → 两轮）；不重开 `asplos-conference.org` 就不要对
  2028 做任何假设。
- 2026-07-08 无法在线核验的条目集中列在 source map 的 待核实 小节——尤其是
  2027 届主席、September cycle 的 HotCRP 地址、camera-ready 页数、注册与参会
  规则、AE 日历、以及是否存在单作者投稿上限。确认前不得当作事实陈述。
- 程序委员会领导层每届轮换；不存在常设主编，也没有跨年度可援引的政策记忆。
- 新增范例论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  核验流程——奖项页面只给标题，书目权威以 ACM DL 条目为准。

## 许可

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
