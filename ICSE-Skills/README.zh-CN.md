# ICSE Skills（中文说明）

面向 **ICSE（IEEE/ACM International Conference on Software Engineering，国际
软件工程大会）** 投稿的 12 个 agent skills。ICSE 是软件工程研究社区的旗舰会议。
本包覆盖一次完整的 ICSE 投稿战役：判断项目属于 research track 还是应改投
co-located track 或兄弟会议、构建经得起 SE 实证审稿人审计的证据、按开放科学
要求组装 double-anonymous 的 HotCRP 投稿、应对 Accept / Major Revision /
Reject 三分决定模型，直至 camera-ready 与 ACM badge 认证的 artifact 交付。

官方依据核验日期：**2026-07-08**。已核验 ICSE 2027 Research Track call、
important dates、NIER 与 Journal-first call、ICSE 2026 artifact-evaluation
track、ICSE 2026 会议记录，以及 SIGSOFT/ICSE 奖项页面。核验环境直接抓取
`conf.researchr.org` 返回 403，故官方页面内容经由搜索引擎对原始 URL 的渲染
读取，并与 ICSE HotCRP 站点、ACM Digital Library、IEEE Xplore、dblp 交叉
验证；完整来源链与全部"待核实"条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## ICSE 与相邻投稿目标的关键差异

以下 2027 周期已核验的机制，决定了本包大部分建议的走向，也是从 ML 会议或
SE 期刊转投 ICSE 的作者最容易踩的坑：

- **一年只有一个周期。** ICSE 2027 只设单一投稿周期（强制 abstract 截止
  2026-06-23，正文截止 2026-06-30，均 AoE）——不同于 2025/2026 的双周期
  模式。错过六月就是错过一年。
- **Major Revision 是真实的决定类别。** 首轮决定（2026-10-20）分为 Accept、
  Major Revision、Reject；MR 论文有四周修改期（11-17 截止），12-18 出终局
  决定。ICSE 2026 的 321 篇录用中有 189 篇经由 Major Revision 通道。
- **四条公开评审标准，verifiability 在列。** Novelty、Rigor、Relevance、
  Verifiability & Transparency 被明确打分；复现包是评审材料，不是事后补丁。
- **硬性 10 页盒子。** 正文 ≤ 10 页（**含 appendix**、图表），另加 2 页仅限
  references；必须使用未经修改的 IEEE 会议模板，格式篡改被明文列为
  desk-reject 事由。不存在无限附录。
- **开放科学是默认值。** 共享是默认预期，*不*共享才需要在 Conclusion 之后的
  Data Availability 小节中说明理由。评审为 double-anonymous，评审期 artifact
  必须匿名化。
- **实证证据文化。** threats-to-validity 小节、research question 契约、效应
  量、真实 subject programs 都是审稿人群体强制执行的社区规范，即使没有条文。

## Skills 一览

| Skill | 作用 |
| --- | --- |
| [`icse-topic-selection`](skills/icse-topic-selection/SKILL.md) | 用双问题适配测试在 research track、NIER/SEIP/SEIS/Demos、FSE/ASE/ISSTA/MSR/ICSME 及 journal-first 通道之间路由。 |
| [`icse-workflow`](skills/icse-workflow/SKILL.md) | 从 6/30 倒排单周期年历：9 月 response、10 月决定、11 月冲刺、次年 4 月都柏林。 |
| [`icse-writing-style`](skills/icse-writing-style/SKILL.md) | 搭建实证 SE 论文骨架：RQ 契约、有实据的动机、非套话的 threats 小节、10 页压缩术。 |
| [`icse-related-work`](skills/icse-related-work/SKILL.md) | 横扫 ACM DL/IEEE Xplore/dblp 的五条文献线，写 delta 先行的定位段，保持自引双盲。 |
| [`icse-experiments`](skills/icse-experiments/SKILL.md) | 让证据匹配论断形状：真实 subjects、公平 baselines、SE 惯例的统计与效应量、定性研究严谨性、防污染的 LLM 消融。 |
| [`icse-reproducibility`](skills/icse-reproducibility/SKILL.md) | 构建 verifiability 叙事：availability statement、挖掘与 LLM 研究的溯源锚定、匿名但可运行的复现包。 |
| [`icse-supplementary`](skills/icse-supplementary/SKILL.md) | 按"评审地位"在 10 页正文与复现包之间分配内容——决定性内容不得只存在于包内。 |
| [`icse-submission`](skills/icse-submission/SKILL.md) | HotCRP 上传前的最终审计：强制 abstract、10+2 格式、机械化匿名检查、开放科学项、desk-reject 风险分级。 |
| [`icse-review-process`](skills/icse-review-process/SKILL.md) | 建模评审流水线——四标准、response、Major Revision、12 月终局——并指出作者真正有杠杆的位置。 |
| [`icse-author-response`](skills/icse-author-response/SKILL.md) | 写好两次发言：9 月按标准映射的 response，与 11 月经得起复审的修改台账。 |
| [`icse-artifact-evaluation`](skills/icse-artifact-evaluation/SKILL.md) | 把录用论文的复现包转化为 ACM badge：Available（DOI 存档）、Reusable（评审员友好文档），赶上 1 月窗口。 |
| [`icse-camera-ready`](skills/icse-camera-ready/SKILL.md) | 用好 camera-ready 多出的一页，系统化去匿名，把 availability 链接永久化，通过 IEEE 出版检查。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 12 条官方来源（URL + 访问日期）、已核验的 2027 周期事实、明确的"待核实"清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及五轮作者侧核验——第一轮就是"今年跑几个周期"。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经档案核验的真实 ICSE 论文，覆盖五种贡献形状，其中 3 篇为 Most Influential Paper 得主，附自检问题。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构 flaky-test 论文的摘要与引言，按四条评审标准逐步重写（before → after）。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向仓库级复现包工具的适配层，并列出通用工具查不出的 ICSE 专属检查项。 |

## 安装与调用

作为 Claude Code 插件使用（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./ICSE-Skills
claude plugin install icse-skills
```

也可以直接把每个 `skills/icse-*/SKILL.md` 当作独立指令文件使用：frontmatter
中的 `description` 描述了触发场景。典型调用示例：

- "这篇该投 ICSE 还是 ISSTA？" → `icse-topic-selection`
- "按 ICSE research track 规则审计我的稿子" → `icse-submission`
- "拿到 Major Revision 了，帮我规划这四周" → `icse-author-response`
- "把 artifact 准备好去拿 badge" → `icse-artifact-evaluation`

## 目录结构

```text
ICSE-Skills/
├── .claude-plugin/           # plugin.json 与 marketplace.json（声明 12 个 skills）
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── LICENSE                   # MIT
├── assets/cover.svg          # 封面
├── skills/
│   └── icse-<主题>/SKILL.md  # 12 个 skill，一目录一文件
└── resources/
    ├── README.md             # 资源导览与推荐路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # 指向共享复现包工具
```

## 建议用法

1. **动笔之前**：先跑 `icse-topic-selection`；在单周期年历下，投错会场或
   证据早熟一档都要付出一整年的代价。同时翻一遍 exemplars library，看被
   十年后见之明认证过的 ICSE 贡献长什么样。
2. **设计研究期间**：把 `icse-experiments` 与 `icse-reproducibility` 放在
   代码库旁边；设计期点名的 threat 还来得及缓解，挖掘期锚定的溯源到六月就
   补不回来了。
3. **写作期间**：正文对照 worked example 用 `icse-writing-style`，正文/包
   分层用 `icse-supplementary`，定位用 `icse-related-work`。
4. **截稿周**：6/23 前注册 abstract，然后对最终 PDF 与复现包从头到尾执行
   `icse-submission`。
5. **投稿之后**：用 `icse-review-process` 校准预期；9 月与 11 月冲刺用
   `icse-author-response`；之后进入 `icse-artifact-evaluation` 与
   `icse-camera-ready`——若 12 月结果不利，则回到 `icse-topic-selection`
   的改投路由表。

## 2027 周期锚点事实（历史快照，非永久规则）

- ICSE 2027 为第 **49** 届：爱尔兰都柏林，**2027 年 4 月 25 日 – 5 月 1 日**
  （核心会期为周三至周五，4 月 28–30 日）。
- Research track：单一周期；abstract（强制）2026-06-23，正文 2026-06-30，
  均 23:59:59 AoE；投稿站点 `icse2027.hotcrp.com`。
- 流水线：author response 2026 年 9 月 · 放榜 2026-10-20 · Major Revision
  截止 2026-11-17 · MR 终局决定 2026-12-18。
- 格式：IEEE 会议模板 · 正文 ≤ 10 页（含图表与 appendix）· 另加 2 页仅限
  references · camera-ready 多给 1 页正文。
- 评审：double-anonymous；标准 = Novelty、Rigor、Relevance、Verifiability &
  Transparency；受 ICSE Open Science 政策约束。
- 背景：ICSE 2026（第 48 届，里约热内卢，2026-04-12 至 04-18）双周期共收
  1,469 篇、录用 321 篇（约 22%），其中 189 篇经由 Major Revision。

## 事实纪律

本包区分三类陈述，skills 的写法保证三类可辨：

1. **已核验的 2027 周期事实**——带日期/页数预算，且能在 source map 中追溯到
   编号来源（如 10+2 页模型、6/30 截稿、四条标准的完整定义）。
2. **转述事实**——仅经由二手渲染读取并明确标注（如 ICSE 2026 录用统计，
   仍待与 proceedings 卷首对照确认）。
3. **核验时无法确认的条目**——明确标注 **待核实**，以"待解决问题"而非事实的
   口吻表述（如 2027 artifact 截止日、response 格式上限、注册规则、AI 使用
   政策）。

若发现任何 skill 把第 2、3 类内容写成了第 1 类的口吻，请视为 bug，对照官方
页面修正。

## 维护说明

- 上述日期与预算均为 **2027 周期快照**。ICSE 每届重设自身结构——连投稿周期
  数都在 2026 与 2027 之间变过——所以每年第一件事是核验周期数。
- 2026-07-08 无法在线核验的条目已在 source map 中标注 **待核实**——尤其是
  2027 program chairs、artifact-evaluation 与 camera-ready 截止日、
  author-response 格式、注册与报告规则、LLM/AI 使用政策。确认之前不得当作
  事实陈述。
- ICSE 没有常任编辑部；chairs 每届轮换。不要把期刊包里"主编连续性"式的假设
  带到这里。
- 新增范文请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——companion volume 论文不能当作 research-track 范文。

## 许可证

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md).
