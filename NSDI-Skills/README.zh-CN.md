# NSDI Skills

面向 **NSDI（USENIX Symposium on Networked Systems Design and Implementation）**
投稿的 12 个 agent skills。NSDI 是 networked/distributed systems 领域的旗舰会议，
要求论文围绕"真正搭建、并在真实流量下测量过的网络化系统"展开。这套包覆盖 NSDI
与所有单截止日期会议都不同的完整节奏：**每届两个投稿截止日期**（spring 与
fall）、跨截止日期的 **one-shot revise-and-resubmit** 机制、使投机性投稿代价高昂
的 resubmission ban、三条评审契约不同的 track、artifact badges，以及与公开代码/
数据挂钩的 Community Award。

官方依据核验日期：**2026-07-08**。已核验 NSDI '27 会议主页与 Call for Papers、
NSDI '26 主页、CFP、multiple-deadlines process 页面与 Call for Artifacts、按截止
日期划分的 HotCRP 站点、USENIX Test of Time awards 页面，以及用于 exemplar 核验的
dblp NSDI 条目。核验环境中直接抓取 `usenix.org` 与 `dblp.org` 均返回 HTTP 403，
因此所有事实均通过搜索引擎对官方 URL 的渲染读取，并经多个独立渲染交叉核对；完整
链路（含全部 待核实 事项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## NSDI 区别于兄弟会议的机制

以下机制均为 2026-27 周期核验结果，是本包大部分建议的出发点，也是从单截止日期
会议转来的作者最常踩的坑：

- **两个截止日期喂给同一届会议。** NSDI '27（2027 年 5 月 11-13 日，美国罗德岛
  Providence）设 spring gate（论文 2026-04-23）与 fall gate（摘要 2026-09-10、
  论文 2026-09-17，11:59 pm US EDT）。每个 gate 有独立的 HotCRP 站点、独立评审
  批次与独立的 accepted-papers 列表。
- **One-shot revision 就是作者答辩渠道。** 渲染出的 CFP 中没有 rebuttal 阶段；
  边界论文会收到审稿人写明的 required issues 清单，并获得在后续截止日期重投一次
  的机会——尽可能由同一批审稿人复审，必须附高亮差异版与修改说明，回避清单则被
  终局拒稿。
- **拒稿附带禁投。** 未获 revision 选项的拒稿论文不能投下一个截止日期：spring
  被拒即跳过同届 fall。"先投了看看"消耗的是两个截止日期。
- **三条 track、三种契约：** research（设计 + 实现 + practical evaluation）、
  operational systems（已部署系统的实战经验；系统名与公司名可保留，匿名规则放
  宽）、frontiers（大胆新想法，可不带完整评估）。
- **12 页上限含脚注、图与表**——投稿与最终版同一上限；references 与 appendices
  可超出该页数。
- **双盲但按 track 分叉**；每位作者跨截止日期最多 8 篇；引用同时在投的 NSDI
  论文须使用 CFP 规定的固定句式。
- **USENIX 开放获取**：历届 NSDI 论文全部免费下载，related work 覆盖不足或引用
  venue 张冠李戴都无从辩解。
- **Artifact 与开放性制度化**：录用后 badge 评测（'26 确认的名称为 Artifacts
  Available），并设 **Community Award**——授予在 final-papers 截止前公开代码/
  数据的最佳论文。

## Skills

| Skill | 作用 |
| --- | --- |
| [`nsdi-topic-selection`](skills/nsdi-topic-selection/SKILL.md) | 用 CFP 的显式 out-of-scope 清单检验 networking-stack 贡献，选定诚实的 track，并向 SIGCOMM、OSDI/SOSP、FAST、SIGMETRICS 分流。 |
| [`nsdi-workflow`](skills/nsdi-workflow/SKILL.md) | 跨 spring/fall 两个 gate 做排期：倒排计划、禁投窗口计算、revision 窗口管理与漫长评审静默期的利用。 |
| [`nsdi-writing-style`](skills/nsdi-writing-style/SKILL.md) | 在含图 12 页内搭建"运维痛点 → 设计原则 → 证据"的论证弧，用尾部百分位替换形容词。 |
| [`nsdi-related-work`](skills/nsdi-related-work/SKILL.md) | 扫全六条文献 lane（含本届 spring cohort），经 dblp/USENIX 证明 venue，处理双盲下的自引。 |
| [`nsdi-experiments`](skills/nsdi-experiments/SKILL.md) | 沿证据阶梯上行（micro → trace/testbed → deployment），选会还手的 baseline，报告尾部、方差与失效点。 |
| [`nsdi-reproducibility`](skills/nsdi-reproducibility/SKILL.md) | 维护拓扑、流量、配置、运行四本台账；刻画方差；尽早判定哪些数据能合法发布。 |
| [`nsdi-supplementary`](skills/nsdi-supplementary/SKILL.md) | 在正文、references、允许的 appendix 与 HotCRP auxiliary material 之间分配内容，含强制的 revision packet。 |
| [`nsdi-artifact-evaluation`](skills/nsdi-artifact-evaluation/SKILL.md) | 面向 AEC 打包：badge 选择即主张校准、降尺度拓扑、trace 替代物与 15 分钟冒烟路径。 |
| [`nsdi-submission`](skills/nsdi-submission/SKILL.md) | 上传前终审：认准本截止日期的 HotCRP 站点、美东时区、12 页核对、按 track 的匿名化、作者上限与禁投核查。 |
| [`nsdi-review-process`](skills/nsdi-review-process/SKILL.md) | 解读三分结局（accept / one-shot revision / reject 附禁投）与影响策略的审稿人连续性规则。 |
| [`nsdi-author-response`](skills/nsdi-author-response/SKILL.md) | 把 one-shot revision 当合同执行：issue 分诊、修改说明、高亮差异版，以及在原稿内预置回应。 |
| [`nsdi-camera-ready`](skills/nsdi-camera-ready/SKILL.md) | 在同样的 12 页内交付开放获取终稿，赶上 Community Award 的公开时钟，指定五月的报告人。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 11 个官方来源（URL + 核验日期）、已核验事实清单、访问方式说明与显式的 待核实 台账。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，外加上传前的五道作者侧核验（时钟、页数、匿名、状态、revision）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇 venue 已核验的 NSDI 论文（2007-2020，五类系统），各带自检问题，并附 Raft/B4/Chord/Spanner/Tor 张冠李戴防护表。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构 RPC-retry 系统论文的摘要与引言按 NSDI 运维证据弧重写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享可复现性工具包的适配器，并列出通用工具查不出的 NSDI 特有项（拓扑、trace、时序方差）。 |

## 安装与使用

作为 Claude Code plugin（本目录自带 marketplace manifest，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./NSDI-Skills
claude plugin install nsdi-skills
```

也可直接使用文件：每个 `skills/nsdi-*/SKILL.md` 都是独立指令文件，frontmatter 的
`description` 说明触发时机。典型用法：

- "这个拥塞控制系统该投 NSDI 还是 SIGCOMM？" → `nsdi-topic-selection`
- "选哪个截止日期？被拒的代价是什么？" → `nsdi-workflow`
- "收到 one-shot revision，帮我定计划" → `nsdi-author-response`
- "fall 上传前把 PDF 过一遍" → `nsdi-submission`

## 目录结构

```text
NSDI-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── nsdi-<topic>/SKILL.md # 12 个 skill，一目录一文件
└── resources/
    ├── README.md             # 资源导览与建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享可复现性工具包适配器
```

## 建议路线

1. **锁定截止日期之前**——先跑 `nsdi-topic-selection`（范围与 track）与
   `nsdi-workflow`（gate 计算）；对照 exemplars library 看已录用论文如何过线。
2. **系统构建期**——`nsdi-experiments` 与 `nsdi-reproducibility` 放在 testbed
   旁边；trace 来源与方差刻画无法事后补。
3. **写作期**——`nsdi-writing-style` 对照 worked example，`nsdi-supplementary`
   做正文/appendix 切分，`nsdi-related-work` 时打开本届 cohort 列表。
4. **截止周**——对最终上传文件完整执行 `nsdi-submission`。
5. **收到结果后**——先用 `nsdi-review-process` 定性，再走
   `nsdi-author-response`（revision）或 `nsdi-artifact-evaluation` +
   `nsdi-camera-ready`（录用）。

## 2026-27 锚点事实（带日期的快照，非长期规则）

- **NSDI '27** 为第 **24** 届：2027 年 5 月 11-13 日，美国罗德岛 Providence，
  Omni Providence Hotel。
- '27 spring gate：摘要 2026-04-16 / 论文 2026-04-23，通知 2026-07-23；
  fall gate：摘要 2026-09-10 / 论文 2026-09-17，通知 2026-12-08。均为
  11:59 pm **US EDT**（'26 用的是 PDT——时区约定本身会变）。
- Track：research、operational systems、frontiers。上限：每位作者跨截止日期
  8 篇。格式：12 页 + references + appendices，双盲。
- **NSDI '26**（第 23 届）已于 2026 年 5 月 4-6 日在华盛顿州 Renton 举行；其
  artifact 评测设三枚 badge，artifact 提交截止 2025-07-31。

## 事实纪律

全包始终区分三类陈述：

1. **已核验的周期事实**——日期、上限与规则均可追溯到 source map 中带编号的来源
   （如 4 月 23 日 spring 截止、12 页规则、one-shot revision 的要求）。
2. **转述事实**——仅见于二手渲染并如实标注（如经作者机构页面转述的 Test of
   Time 名单、Apache 项目转述的 Spark Best Paper）。
3. **待核实事项**——显式标记并以问题形式表述（如 '27 co-chairs、camera-ready
   日期、'26 badge 全称、是否存在 rebuttal 阶段）。

若 skills 中有第 2、3 类内容被当作第 1 类陈述，请视为 bug 并对照官方页面修正。

## 维护说明

- 上述所有日期都是 **2026-27 快照**。NSDI 按届、且按截止日期重设规则——给出
  deadline 相关建议前，务必重开当届 CFP 与对应 HotCRP `/deadlines` 页面。
- **frontiers track 出现在渲染的 '27 CFP 中**；不要假设其他届也有或条款不变。
- 截止时区在 **'26（PDT）与 '27（EDT）之间发生了变化**；不要沿用上一周期的
  时区换算表。
- 会议主席逐届轮换，'27 co-chairs 未能核验——引用任何人名前先查当届组织页。
- 新增 exemplar 必须走
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的
  venue 核验流程；系统领域最著名的论文恰恰最常被记错会议。

## License

MIT——见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
