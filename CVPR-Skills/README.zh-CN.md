# CVPR Skills（中文说明）

面向 **CVPR（IEEE/CVF Conference on Computer Vision and Pattern Recognition）** 的 12 个
agent skills。CVPR 是计算机视觉的旗舰会议，也是按投稿量计全球最大的学术评审机器之一。
本包覆盖一次 CVPR 战役的完整弧线：判断项目能否经受 16,000 篇投稿规模的评审、构建
benchmark 级证据、通过 OpenReview 的 11 月三连 deadline、写好一页纸 rebuttal、履行
作者侧审稿义务，直至论文进入 CVF open access 与 IEEE Xplore。

官方依据**于 2026-11-24 复核**：直接抓取 CVPR 2027 Call for Papers、Author
Guidelines、Dates 页、Reviewer Guidelines 与 Organizers 页。2026-07-08 的初版经由
精确 URL 的搜索引擎渲染读取 CVPR 2026 各页、Compute Reporting Form 页面、
`cvpr-org/author-kit` 仓库、CVF open access 索引与官方规模/闭幕公告（当时直接抓取被
网关以 403 拦截）；完整来源链（含全部 待核实 项）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

**周期状态**：本包现描述 **CVPR 2027（西雅图，2027 年 6 月 20–24 日）**。投稿窗口已于
2026-11-16 关闭；评审 2027-01-25 发回，rebuttal 为 01-25 至 02-01，02-25 放榜。
CVPR 2026（丹佛，2026 年 6 月 3–7 日）保留为规模与程序的历史锚点。

## CVPR 与兄弟会议的关键差异（CVPR 2027 已核实）

- **图表计入页数上限**：正文 8 页*含图表*，仅参考文献与强制的 LLM Usage Statement
  可溢出。页数预算本质上是图的设计问题。
- **三个 deadline 相隔各一周**：论文注册 + 全体作者完整的 OpenReview profile 与
  enrollment（2026-11-10）→ 论文（11-16）→ 补充材料（11-23）。最容易出事的是第一个。
- **投稿即审稿契约**：全体作者纳入审稿人池；每位作者至多 25 篇投稿；2027 新增
  reciprocal-reviewer 配额——每位作者至多一篇"无合格审稿作者"的论文；高度不负责的
  审稿人，其署名的全部论文可被整体 desk reject。
- **强制 LLM Usage Statement**（2027 新设）：每篇论文须在正文之后说明 LLM/生成式 AI
  的使用情况（未使用也须声明），缺失即 desk reject；评审期间会议批准的 LLM 工具会处理
  投稿，不可退出。（2026 年的 Compute Reporting Form 未出现在 2027 指南中。）
- **一页纸、零附件的 rebuttal**：官方模板单页 PDF，超页或改版式直接不读；评审全程
  禁止外部链接。
- **arXiv 合法、链接违规**：挂 arXiv 预印本明确不算破坏匿名，但任何"扩展内容或绕过
  评审"的外链被禁止；论文在录用前处于媒体禁令之下。
- **规模即现实**：2026 年 16,092 篇完成评审、录用 4,090 篇（25.42%）、约 25,149 名
  审稿人、909 名 AC、约 12,200 名注册参会者。发表为双通道：CVF open access（免费、
  带水印的录用版）+ IEEE Xplore（record 版）。无 APC；无常设主编，各届主席轮换。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`cvpr-topic-selection`](skills/cvpr-topic-selection/SKILL.md) | 检验贡献是否是"关于视觉数据/视觉计算的主张"，并在 CVPR、ICCV/ECCV、WACV、3DV、NeurIPS、SIGGRAPH 与期刊之间路由。 |
| [`cvpr-workflow`](skills/cvpr-workflow/SKILL.md) | 管理从 9 月冻结 scope、11 月三连 deadline、1 月 rebuttal 周、2 月放榜到 6 月参会的整条日历，并规划被拒后的再投阶梯。 |
| [`cvpr-writing-style`](skills/cvpr-writing-style/SKILL.md) | 为"先翻图、后细读"的两遍式审稿人写作：teaser 图、自含 caption、8 页含图预算、有范围限定的主张、对 AI 辅助文本负全责。 |
| [`cvpr-related-work`](skills/cvpr-related-work/SKILL.md) | 覆盖五个文献货架，处理 arXiv 速度的 concurrent work，保持双盲自引，并核实"CVPR 论文"确实发表于 CVPR。 |
| [`cvpr-experiments`](skills/cvpr-experiments/SKILL.md) | 围绕四个隐含审稿问题设计证据——有效吗、为什么有效、何时失效、代价多大——含配平 baseline 与对齐 CRF 的效率报告。 |
| [`cvpr-reproducibility`](skills/cvpr-reproducibility/SKILL.md) | 维护 recipe 台账、benchmark/split 卫生、视觉算力规模下的 seed 诚实度，以及与 CRF 的一致性。 |
| [`cvpr-supplementary`](skills/cvpr-supplementary/SKILL.md) | 在 8 页正文与晚一周的补充材料之间分配内容；在禁链规则下把视频做成证据。 |
| [`cvpr-artifact-evaluation`](skills/cvpr-artifact-evaluation/SKILL.md) | 构建密封的匿名评审 artifact 与公开 release，含"数据集须在 camera-ready 前公开"义务与 license 决策。 |
| [`cvpr-submission`](skills/cvpr-submission/SKILL.md) | 上传前终审：profile、配额、页数上限、LLM Usage Statement、匿名/链接扫描、一稿多投声明、desk-reject 分级与最后 72 小时顺序。 |
| [`cvpr-review-process`](skills/cvpr-review-process/SKILL.md) | 建模 16k 规模的评审流水线——审稿义务执法、会议批准的 LLM 工具与外部 LLM 禁令、讨论期、oral/highlight/poster 分层——并定位作者杠杆点。 |
| [`cvpr-author-response`](skills/cvpr-author-response/SKILL.md) | 把多份评审分诊进一页纸：先杀事实性错误、用 mini-table 给数、有分寸地认错，为 AC 的可读性排版。 |
| [`cvpr-camera-ready`](skills/cvpr-camera-ready/SKILL.md) | 交付 record 版本：去匿名、恢复外链、数据集公开、CVF/IEEE 双通道发表、按分层准备报告与海报。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 14 条官方来源（含访问日期）、已核实的 2026 周期事实、访问方式披露与明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口链接 + 上传前的五道作者侧核验工序。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经元数据核实的 CVPR 论文（ResNet、YOLO、PointNet、ImageNet、Latent Diffusion），附"勿误归 CVPR"警示名单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构 tracking 论文的首页 before → after 重写，演示 flip-then-read 写法。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享 ML 会议可复现工具包的适配器，及通用工具查不了的 CVPR 专属检查。 |

## 安装与使用

作为 Claude Code 插件（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆内执行
claude plugin marketplace add ./CVPR-Skills
claude plugin install cvpr-skills
```

也可直接使用文件：每个 `skills/cvpr-*/SKILL.md` 都是独立的指令文件，frontmatter 的
`description` 说明触发时机。典型问法：

- "这篇适合投 CVPR 还是 WACV？" → `cvpr-topic-selection`
- "按 CVPR 页数与匿名规则审一遍我的稿子" → `cvpr-submission`
- "评审出来了，帮我规划一页纸 rebuttal" → `cvpr-author-response`
- "camera-ready 之前必须公开什么？" → `cvpr-camera-ready`

## 目录结构

```text
CVPR-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── cvpr-<topic>/SKILL.md # 12 个 skills，一目录一技能
└── resources/
    ├── README.md             # 资源导览 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 共享复现工具包适配器
```

## CVPR 2027 周期事实（2026-11-24 复核）

- CVPR 2027：2027 年 6 月 20–24 日，西雅图（6 月 20–21 日 workshops/tutorials，
  6 月 22–24 日主会）。
- 时间线：论文注册 + profile/enrollment 2026-11-10 · 论文 11-16（AoE，不延期）·
  补充材料 11-23 · 评审发回 2027-01-25 · rebuttal 01-25 至 02-01 · 放榜 02-25。
- 格式：8 页含图表 + 参考文献与 LLM Usage Statement 可溢出；CVPR 2027 author kit
  内含单页 rebuttal 模板。
- 主席：General Chairs Deva Ramanan、Arun Ross；Program Chairs Alexander Berg、
  Liangliang Cao、Vicky Kalogeiton、Nicu Sebe、Humphrey Shi、Angela Yao。

## 2026 周期锚点事实（历史快照，不是永久规则）

- CVPR 2026：2026 年 6 月 3–7 日，丹佛 Colorado Convention Center（6 月 3–4 日
  workshops/tutorials，6 月 5–7 日主会 + 展览）。
- 时间线：摘要 + profile 2025-11-06 · 论文 + CRF 11-13（AoE，官方声明不改期）·
  补充材料 11-20 · 评审发回 2026-01-22 · rebuttal 截至 01-29 · 讨论期 01-30 至
  02-05 · 放榜 02-20。
- 格式：8 页含图表 + 仅参考文献可溢出；官方 author kit 位于
  `github.com/cvpr-org/author-kit`，内含单页 rebuttal 模板。
- 规模：16,092 篇完成评审；录用 4,090 篇（25.42%）；约 25,149 名审稿人（97 个国家/
  地区）；909 名 AC；44,011 名作者；约 12,200 人注册参会。程序追踪方报道 141 篇
  oral、578 篇 highlight（分层数字按"报道"级别对待）。
- 发表：CVF open access + IEEE Xplore，作者侧零费用。

## 事实纪律

本包把三类陈述严格分开：

1. **已核实事实**——可追溯到 source map 编号来源（如 8 页含图上限、2026-11-16
   deadline、LLM Usage Statement；2026 年的 CRF 必填节）。
2. **报道级事实**——仅见于二手来源并如实标注（如 2026 年 oral/highlight 数量、
   2026 年主席人名）。
3. **核验时不可得项**——明确标注 待核实 并写成待解决的问题（如补充材料体积上限、
   camera-ready 表单与截止、2027 年是否仍有算力表单、Findings Track 细则）。

若发现任何 skill 把第 2、3 类当作第 1 类陈述，请视为 bug 并对照官方现页修正。

## 建议使用路线

1. **动笔之前**：先跑 `cvpr-topic-selection` —— 如果贡献经不起"这是不是一个关于视觉
   计算的主张"的检验，本包为你省下的是一整个投稿周期；再对照 exemplars 库看录用形态。
2. **做实验时**：把 `cvpr-experiments` 与 `cvpr-reproducibility` 放在代码旁边；
   recipe 台账在第一次出数前建立，比 deadline 周补记便宜得多。
3. **写作时**：正文用 `cvpr-writing-style`（先过 90 秒翻图测试），定位用
   `cvpr-related-work`，正文/补充材料的分配用 `cvpr-supplementary`。
4. **Deadline 双周**：`cvpr-submission` 从头到尾执行一遍，含对合并 PDF 的机械式匿名
   与格式检查，以及 LLM Usage Statement。
5. **投稿之后**：用 `cvpr-review-process` 校准预期；评审落地后走
   `cvpr-author-response` 的分诊流程；2 月放榜后进入 `cvpr-camera-ready` 或
   `cvpr-workflow` 的再投阶梯。

## 维护说明

- 本包所有日期、上限与执法规则均为 **CVPR 2027 快照**（2026 数值标为历史）；CVPR
  政策由轮换的 Program Chairs 每年重写，给出任何 deadline 敏感建议前必须重开
  `cvpr.thecvf.com` 当前页。
- Compute Reporting Form 是 2026 年新生事物，2027 指南已不再提及；LLM Usage
  Statement 与 reciprocal-reviewer 配额是 2027 年的新规，均应假设会继续演化。
- 审稿义务执法、LLM 政策与媒体禁令近年持续收紧，且可能继续收紧；每个周期同时核对
  Author 与 Reviewer Guidelines。
- 新增 exemplar 时遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——大量著名视觉论文实际发表于 ICCV/ECCV/ICLR 而非 CVPR。

## 许可

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
