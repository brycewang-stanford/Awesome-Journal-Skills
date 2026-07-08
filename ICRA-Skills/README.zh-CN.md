# ICRA Skills（中文说明）

面向 **ICRA（IEEE International Conference on Robotics and Automation，IEEE 机器人
与自动化国际会议）** 的 12 个 agent skills。ICRA 是 IEEE Robotics and Automation
Society（RAS）的旗舰会议，也是每年规模最大的机器人学投稿窗口。本包覆盖完整链路：
判断项目是否"ICRA 形状"（以及应当走直投会议、还是走 **RA-L 期刊 + 会议报告** 通道）、
构建真机实验证据、制作 video attachment、应对**没有 rebuttal** 的评审流程，直到
IEEE Xplore 的 camera-ready 落地。

官方依据核验日期：**2026-07-08**。核验对象包括 ICRA 2026（维也纳）的 call for papers
与 final submission 页面、已公布的 ICRA 2027（首尔）年度站点、IEEE RAS 系列页面与
RA-L 作者页面，以及 PaperPlaza。核验环境对 `ieee-icra.org` 年度站点的直接抓取返回
403，因此官方页面内容通过搜索引擎对精确 URL 的渲染读取，并与 IEEE RAS 页面、IEEE
Xplore 记录交叉核对；完整证据链（含所有仍标注 **待核实** 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## ICRA 与相邻 venue 的关键差异

以下机制均按 2026 周期核验，是本包 12 个 skills 的出发点，也是从 ML 会议转来的作者
最容易踩的坑：

- **通往同一个讲台的两条路。** 直投 ICRA（每年一次、9 月截稿）与 RA-L 期刊投稿后
  转会议报告（全年滚动、可修改重投、拿期刊发表）最终都站上 ICRA 的讲台。二者如何
  选择是本包显式教学的策略问题。
- **没有 rebuttal。** 经典 ICRA 流程中，评审意见与 1 月的录用决定一起送达。反驳
  必须提前写进论文里，video attachment 事实上承担了"异步 rebuttal"的角色。
- **视频是一等公民。** 最长 180 秒、最大 20 MB，只在固定窗口上传（其中第二个窗口
  在论文截稿**之后**关闭）；审稿人往往先看视频再读正文，评审表单里有专门栏目。
- **页面预算紧、没有附录。** 2026 周期投稿为 6 页正文 + 2 页纯参考文献；
  camera-ready 为**含参考文献在内总共 8 页**。没有补充 PDF，一切承重内容必须在
  正文里。
- **匿名规则刚刚翻转。** ICRA 2025 还是 single-blind；ICRA 2026 改为
  double-anonymous。"our previous platform [7]" 式写法和带实验室标识的视频画面
  一夜之间变成硬伤。
- **真机证据文化。** 审稿人默认要看 trial 数量、成功判据、失败分类和 sim-to-real
  差值；只有漂亮 demo 而无这些要素的论文会被当成广告。
- **截止时间是太平洋时区。** 2026 周期为 23:59 PT 而非 AoE——对按 ML 会议习惯
  计时的团队是整整五小时的陷阱。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`icra-topic-selection`](skills/icra-topic-selection/SKILL.md) | 做 embodiment test，在直投 ICRA 与 RA-L 通道之间权衡，并对照 IROS、RSS、CoRL、T-RO、HRI、CASE 分流。 |
| [`icra-workflow`](skills/icra-workflow/SKILL.md) | 从 9 月截稿倒排日历：视频窗口、冬季评审静默期、1 月通知、3 月 camera-ready、5/6 月会议。 |
| [`icra-submission`](skills/icra-submission/SKILL.md) | PaperPlaza 上传前终审：6+2 页面几何、模板合规、double-anonymous 清扫、视频规格与窗口、一稿多投红线。 |
| [`icra-writing-style`](skills/icra-writing-style/SKILL.md) | 任务先行的开篇、图优先的结构、把 demo 话术改写成测量数、跨栈符号纪律与 6 页预算。 |
| [`icra-related-work`](skills/icra-related-work/SKILL.md) | 覆盖机器人审稿人必查的五条文献带，处理 arXiv 并行工作，在匿名规则下引用自己的平台论文。 |
| [`icra-experiments`](skills/icra-experiments/SKILL.md) | 让论断高度与证据阶梯匹配：trial 与 reset、baseline 公平性、sim-to-real 差值、失败分类、小样本统计。 |
| [`icra-reproducibility`](skills/icra-reproducibility/SKILL.md) | 区分"可重跑"与"可审计"两类结果；硬件规格台账、rosbag 记录纪律、诚实的可用性声明。 |
| [`icra-supplementary`](skills/icra-supplementary/SKILL.md) | 把 180 秒视频当证据做：分镜、不剪辑的连续镜头、标注倍速、展示失败、20 MB 编码与画面匿名化。 |
| [`icra-artifact-evaluation`](skills/icra-artifact-evaluation/SKILL.md) | 按六层 artifact 栈打包（算法、集成、仿真、权重、硬件设计、证据日志），面向"五分钟怀疑者"。 |
| [`icra-review-process`](skills/icra-review-process/SKILL.md) | 建模 RAS Conference Editorial Board 流水线、无 rebuttal 的后果，以及与 RA-L 期刊评审的对照。 |
| [`icra-author-response`](skills/icra-author-response/SKILL.md) | 在真实存在的通道里回应审稿：camera-ready 修订、RA-L 回复信、被拒后转投 IROS/RA-L 的备忘录。 |
| [`icra-camera-ready`](skills/icra-camera-ready/SKILL.md) | 总共 8 页的终稿限制、去匿名化、IEEE 版权转让（eCF）、注册义务、终版视频与 IEEE Xplore。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十条一手来源（URL + 访问日期）、二手来源标注、已核验的 2026 周期事实、显式的待核实清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及上传前的五道作者侧核查（页面几何、匿名、视频、证据、时区）。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇经 DOI 核验的 ICRA 论文（2000-2018，五条主题带），附自检问题与"venue 张冠李戴"防误清单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 虚构的打滑再抓取论文摘要 + 引言，从 demo 话术重建为 ICRA 论证弧线（before → after）。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享 ML 会议可复现工具包的适配器，外加五项通用工具做不了的机器人学检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录中
claude plugin marketplace add ./ICRA-Skills
claude plugin install icra-skills
```

也可以直接使用文件：每个 `skills/icra-*/SKILL.md` 都是独立的说明文件，frontmatter
中的 `description` 定义了触发时机。典型问法：

- "这个工作 9 月投 ICRA 还是现在投 RA-L？" → `icra-topic-selection`
- "按 ICRA 规则审一遍我的稿子" → `icra-submission`
- "帮我给 attachment 视频写分镜" → `icra-supplementary`
- "1 月的评审意见到了，下一步怎么办？" → `icra-author-response`

## 目录结构

```text
ICRA-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── icra-<topic>/SKILL.md # 12 个 skill，各占一个目录
└── resources/
    ├── README.md             # 资源导览与推荐路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享可复现工具包适配器
```

## 推荐用法

1. **立项前**：先跑 `icra-topic-selection`；如果 embodiment test 不通过，或时间
   窗口更适合 RA-L，这个包就已经帮你省下一个投稿周期。按主题带翻阅 exemplars。
2. **实验阶段**：把 `icra-experiments` 与 `icra-reproducibility` 放在机器人旁边；
   每次实验都按 `icra-supplementary` 的要求积累原始视频素材——截稿周补拍的视频
   既不可信也难匿名。
3. **写作阶段**：正文用 `icra-writing-style`，定位用 `icra-related-work`，对照
   worked example 的 before/after。
4. **截稿两周**：用 `icra-workflow` 排程，然后走完整的 `icra-submission` 审计，
   包括视频窗口日期和太平洋时区换算。
5. **决定之后**：用 `icra-review-process` 读懂决定包，按适用通道走
   `icra-author-response`，再进入 `icra-camera-ready` 或 IROS/RA-L 转投路线。

## 2026 周期锚点事实（历史快照，不是永久规则）

- ICRA 2026：**2026 年 6 月 1-5 日，奥地利维也纳 Messe Wien**，主题 "Robots for
  all"，8,000+ 参会者。
- 当前目标：**ICRA 2027，2027 年 5 月 24-28 日，韩国首尔 COEX**；注册约 2027 年
  2 月初开放；**论文截稿日期尚未公布**（近年规律为前一年 9 月中旬）。
- 2026 投稿：PaperPlaza，截稿 2025 年 9 月 15 日 23:59（太平洋时间）；6 页正文 +
  2 页纯参考文献；double-anonymous。
- 视频附件：≤ 180 秒、≤ 20 MB、mpeg/mp4/mpg，窗口为 2025-08-05 至 09-09 与
  2025-09-17 至 09-22。
- 录用通知 2026-01-31、camera-ready 2026-03-06（二手来源，需复核）；终稿含参考
  文献共 8 页；完成 eCF 版权转让后发表于 IEEE Xplore。
- RA-L 通道：全年投稿，6 页含参考文献（超页每页 175 美元、至多 2 页），首轮决定
  约 3 个月，录用后 270 天内转入 RAS 会议做报告。

## 事实纪律

本包把三类陈述分开维护：

1. **已核验的 2026 周期事实**——带日期/上限，可追溯到 source map 的编号来源
   （如 6+2 页面拆分、视频规格）。
2. **二手转述事实**——仅见于聚合站或渲染快照，均已标注（如 1 月 31 日通知日期）。
3. **核验时不可得的条目**——标注 **待核实**，以问题而非结论的形式出现（如 ICRA
   2027 截稿日、double-anonymous 是否延续、注册费、AI 使用政策）。

若发现任何 skill 把第 2、3 类内容写成了第 1 类，请视为 bug，对照官方页面修正。

## 维护说明

- 上文所有数字都是 **2026 周期快照**。2025→2026 从 single-blind 到
  double-anonymous 的翻转证明 ICRA 规则确实逐年变化；给出任何 deadline 级建议前
  必须重开 `<year>.ieee-icra.org`。
- ICRA 没有常设主编；组织委员会与 RAS Conference Editorial Board 的分工按届轮换，
  不要把期刊包里的"主编连续性"假设搬过来。
- 不要把会议规则与 RA-L 规则混用：两者共享 PaperPlaza，但政策各自独立。
- 新增 exemplar 时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——DOI 必须解析到 ICRA 论文集条目；"大家都说这篇是 ICRA"不算核验。

## 许可

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
