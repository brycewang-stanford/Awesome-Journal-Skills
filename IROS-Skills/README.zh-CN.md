# IROS Skills

面向 **IROS —— IEEE/RSJ International Conference on Intelligent Robots and Systems**
（IEEE/RSJ 智能机器人与系统国际会议）论文的 12 个 agent skills。IROS 是秋季机器人旗舰会议，
由 IEEE Robotics and Automation Society（RAS）与日本机器人学会（RSJ, Robotics Society of
Japan）共同主办。本包覆盖完整链路：判断项目是否适合 IROS（相对 ICRA、RSS、CoRL 或 RA-L
期刊路线）、构建真实机器人证据、剪辑 60 秒视频附件、应对**没有 rebuttal** 的评审流程，以及在
IEEE Xplore 完成 camera-ready。

官方依据核验日期：**2026-07-09**。已核验 IROS 2026（Pittsburgh）的 call for papers 与
important dates 页面、IEEE RAS 联合主办会议页与 RA-L 页面，以及 PaperPlaza。核验环境直接抓取
`2026.ieee-iros.org` 返回 HTTP 403，故通过搜索引擎对精确 URL 的渲染阅读官方内容，并与 IEEE RAS
页面、PaperPlaza 及独立会议镜像交叉核对；完整证据链（含所有仍标注 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## IROS 与兄弟会议的区别

以下会议机制均按 2026 cycle 核验，驱动各 skill 的建议——也是从 ML 会议或 ICRA 转来的作者最常
踩的坑：

- **IEEE/RSJ 联合身份。** IROS 由 IEEE RAS **与**日本机器人学会共同主办，创办于 1988 年，是真正的
  双机构会议，主办地区逐年轮换。这正是名字里 "IEEE/RSJ" 的由来，也是每届委员会与规则都会重置的原因。
- **秋季档期。** IROS 是**秋季** IEEE-RAS 旗舰，与 ICRA 的春季档互为季节对应。从 IROS 的视角看机器人
  日历：春季投稿截止、夏季评审静默、六月中旬通知、七月 camera-ready、九月末/十月开会。
- **更紧的视频规格。** 2026 cycle 的可选视频附件为 **60 秒、10 MB**——只有 ICRA（180 秒 / 20 MB）的
  一半，且有**独立的截止日期**，在论文截止后几天。为 ICRA 剪的视频必须重剪，而非直接重传。
- **参考文献计入页数，且没有 supplementary PDF。** 所有关键内容都必须写进正文；需要 appendix 才能
  讲清的论证，对 IROS 而言就是篇幅错配。
- **2026 双盲。** IROS 长期是 single-blind 传统，但 2026 cycle 呈现为 double-anonymous——PDF 中不出现
  作者名，完整名单只放在 PaperPlaza metadata。"our prior rover [9]" 这类写法与带实验室标识的视频画面
  都会在评审阶段泄露身份。
- **没有 rebuttal。** 评审意见传统上**与决定一同**送达。所有可预见的异议都必须在论文与视频里预先回应；
  视频是评审能看到的唯一异步 "rebuttal"。
- **RA-L 路径已变。** IROS 2026 **不再提供 RA-L+IROS 联合投稿选项**；改为已发表的 RA-L（及 T-RO、
  T-ASE、RAM）论文经 transfer window 获得在 IROS presentation 的资格。这既不同于旧 cycle，也不同于
  常见的 ICRA 说法。
- **具身证据文化。** 评审者对硬件清单、试验次数、reset 流程、失败分类与 sim-to-real 差距高度敏感；
  缺了这些，再精致的 demo 也像广告。

## 当前 cycle 快照（2026-07-09）

截至核验日期，IROS 2026 **已过投稿、处于 cycle 中段**：3 月 2 日论文截止与 3 月 5 日视频截止均已
关闭，**通知已于 2026 年 6 月 16 日送达**，**当前义务是 camera-ready 与注册**——final paper 截止为
**2026 年 7 月 10 日**，即本包核验日期的次日。IROS 2027 据报道（非一手核验）为 2027 年 9 月末/
10 月初在意大利 Florence 举办。据此规划：若你为 2027 投稿而读本包，你面对的是**下一个**春季截止，
而非本次。

## Skills

| Skill | 作用 |
| --- | --- |
| [`iros-topic-selection`](skills/iros-topic-selection/SKILL.md) | 识别集成系统贡献及其具身约束；从 IROS 秋季视角在 ICRA、RSS、CoRL、RA-L、T-RO、HRI、CASE 之间选会。 |
| [`iros-workflow`](skills/iros-workflow/SKILL.md) | 从春季截止倒推：独立视频截止、夏季评审静默、六月通知、七月 camera-ready。 |
| [`iros-submission`](skills/iros-submission/SKILL.md) | PaperPlaza 终检：含参考文献的页数预算、IEEE 模板、双盲扫查、60 秒/10 MB 视频、一稿多投陷阱。 |
| [`iros-writing-style`](skills/iros-writing-style/SKILL.md) | 任务优先的开篇、以系统图为主图、把 demo 话术改写为数字、无 supplement 的正文纪律。 |
| [`iros-related-work`](skills/iros-related-work/SKILL.md) | 覆盖机器人系统各条脉络、处理并行 arXiv 工作、在双盲下保持自引匿名。 |
| [`iros-experiments`](skills/iros-experiments/SKILL.md) | 主张—证据阶梯：试验、reset、同硬件基线公平性、sim-to-real 差距、失败分类、小样本统计。 |
| [`iros-reproducibility`](skills/iros-reproducibility/SKILL.md) | 区分可重跑与仅可审计的主张；硬件清单、标定披露、日志记录、诚实的可得性声明。 |
| [`iros-supplementary`](skills/iros-supplementary/SKILL.md) | 把 60 秒视频当证据：分镜、未剪片段、标注失败、诚实倍速、10 MB 编码、画面匿名化。 |
| [`iros-artifact-evaluation`](skills/iros-artifact-evaluation/SKILL.md) | 为质疑者打包机器人 artifact 栈——硬件、日志、配置、代码、数据——含评审期与录用期两种状态。 |
| [`iros-review-process`](skills/iros-review-process/SKILL.md) | 建模 PaperPlaza 的 Associate Editor 流程、无 rebuttal 的后果、视频如何影响评审。 |
| [`iros-author-response`](skills/iros-author-response/SKILL.md) | 用现存渠道回应：论文内预先回应、camera-ready 修改、RA-L 回复信、被拒后转投备忘。 |
| [`iros-camera-ready`](skills/iros-camera-ready/SKILL.md) | 去匿名、整合 meta-review、IEEE eCF 版权、七月截止、注册与 IEEE Xplore 出版。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 8 个一手来源（URL + 访问日期）、二手来源标注、2026 cycle 已核验事实与显式 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口与五道作者侧核验（页数、匿名、视频、证据、时间）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经 DOI 核验的 IROS 论文（2012-2020），覆盖五条系统脉络，附自检问题与误归属防护。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的弹簧门移动操作摘要，从 demo 话术重写为 IROS 弧线，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 对接共享 ML 会议可复现套件，外加它无法完成的五项机器人专属检查。 |

## 安装与使用

作为 Claude Code 插件（本目录是带独立 marketplace manifest 的自包含插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./IROS-Skills
claude plugin install iros-skills
```

或直接使用文件：每个 `skills/iros-*/SKILL.md` 都是独立指令文件，其 frontmatter 的 `description`
告诉 agent 何时触发。常见调用：

- "这是 IROS 论文还是 CoRL 论文？" → `iros-topic-selection`
- "按 IROS 投稿规则审我的稿" → `iros-submission`
- "帮我给 60 秒视频做分镜" → `iros-supplementary`
- "被录用了——camera-ready 清单是什么？" → `iros-camera-ready`

## 目录结构

```text
IROS-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── iros-<topic>/SKILL.md # 12 个 skill，各一目录
└── resources/
    ├── README.md             # 资源导引与推荐路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 对接共享复现套件
```

## 推荐用法

1. **决定投哪一届之前** —— 先跑 `iros-topic-selection`；若系统没有具身约束，或季节更利于 ICRA，
   本包就已经帮你改进了计划。按系统脉络浏览 exemplars library。
2. **实验阶段** —— 把 `iros-experiments` 与 `iros-reproducibility` 放在机器人旁，并按
   `iros-supplementary` 从每次实验中积累视频素材，因为临近截止才补拍会同时损害证据与匿名。
3. **写作阶段** —— 正文用 `iros-writing-style`，定位用 `iros-related-work`，worked example 作为
   before/after 参照。
4. **截止前两周** —— 用 `iros-workflow` 排期，再做完整 `iros-submission` 终检，包含独立视频截止与
   含参考文献的页数预算。
5. **出结果之后** —— 用 `iros-review-process` 读评审包，按适用渠道用 `iros-author-response`
   （没有 rebuttal，通常就是 camera-ready），再走 `iros-camera-ready` 或转投 ICRA / CoRL / RA-L。

## 事实纪律

本包区分三类陈述：

1. **已核验的 2026 cycle 事实** —— 带日期/上限，且可追溯到 source map 中的编号行（如 60 秒/10 MB
   视频、7 月 10 日 camera-ready）。
2. **转述事实** —— 仅见于二手渲染或聚合站并如实标注（如 6 月 16 日通知、IROS 2027 Florence 会址）。
3. **核验时不可确证条目** —— 标 待核实 并以问句表述（如 2026 确切页数上限、双盲是否延续、是否存在
   rebuttal、general/program chair 名单、注册费）。

若某个 skill 把第 2、3 类当作第 1 类呈现，视为 bug，请对照当前官方页面修正。

## 维护说明

- 以上每个数字都是 **2026 cycle 快照**。IROS 规则确实会逐届变化——single-blind 转 double-anonymous
  的姿态与联合 RA-L 选项的取消即为明证；涉及 deadline 的建议前请重开 `<year>.ieee-iros.org`。
- IROS 没有常任 editor-in-chief；组委会与 PaperPlaza 的 Associate Editor/Editor 分派逐届轮换，
  联合主办地区交替。请勿把期刊包里的 editor 连续性假设搬过来。
- 不要把 IROS 与 ICRA 混同：二者共享 PaperPlaza 与 IEEE Xplore，但日历、视频规格与逐届政策各不相同。
- 新增 exemplar 时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——DOI 必须解析到 IROS proceedings 条目；`10.1109/ICRA.*` 的 DOI 不是 IROS。

## License

MIT —— 见 [`LICENSE`](LICENSE)。English README: [`README.md`](README.md)。
