# CHI Skills

面向 **CHI —— ACM CHI Conference on Human Factors in Computing Systems**（ACM SIGCHI
旗舰会议）投稿的 12 个 agent skills，覆盖人机交互领域的交互技术、用户研究、无障碍
（accessibility）、社会计算、设计研究与人本 AI。本包贯穿一个完整 CHI 周期：判断项目
是否 CHI 形态、选择评审 subcommittee、构建能通过 rubric 筛查的研究证据、在单一截止
日打包论文与 video figure、走完两轮 revise-and-resubmit 评审，以及完成带强制无障碍
要求的 TAPS camera-ready。

官方依据核验日期：**2026-07-08**。已核验 CHI 2027 Papers call 与 review-process 页面、
CHI 2027 周期日历、CHI 2026 官网及其 Papers track 结果报告、CHI Steering Committee 的
assisted desk reject rubric、SIGCHI 的 accessibility 与 video 作者指南，以及 ACM 开放
获取政策页面。核验环境中对 `chi2027.acm.org` 与 `chi2026.acm.org` 的直接抓取返回
403，因此官方页面内容经由精确 URL 的搜索引擎渲染读取，并与 SIGCHI、`chi.acm.org` 和
ACM Digital Library 交叉核对；完整来源链（含所有 待核实 条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## CHI 与相邻会议的关键差异

以下机制均为 2026→2027 周期核验事实，也是从 ML 或系统会议转来的作者最常踩的坑：

- **用 PCS，不用 OpenReview/CMT。** 投稿与评审在 Precision Conference Solutions 上
  进行，9 月的一个截止日收齐*所有东西*——论文、video figure 与全部补充材料，之后没有
  单独的补充材料窗口。
- **按字数不按页数。** 没有固定页数上限：鼓励 5,000–8,000 词；5,000 词以下是按其体量
  评审的正当 short paper；超过 12,000 词且长度无正当理由会被 desk reject。评审被明确
  要求按"贡献相对长度"来衡量论文。
- **Subcommittee 就是你的陪审团。** 作者最多指定两个评审 subcommittee，该选择决定
  1AC、2AC 与审稿人池——是投稿表单里最具战略性的一栏。
- **筛查是动真格的。** 在格式类 desk reject 之外，还有 SC 与 AC 共同执行的 rubric 化
  *assisted* desk reject：文献情境化严重不足、贡献与篇幅不匹配、数据严重不足、方法
  透明度严重不足，都可能让论文在进入外审前出局。
- **是两轮评审，不是 rebuttal。** 第一轮不录用任何论文；1AC 或 2AC 给出 RR 及以上
  推荐的论文获得约五周窗口，提交带修订痕迹的修改稿加回复信，最终由 PC meeting 决定。
  CHI 2026 实况：6,730 篇完整投稿，38.7% 获邀修改，重投稿件 65.5% 录用，总录用率
  25.3%。
- **发表包含无障碍工作。** Camera-ready 走 ACM TAPS：作者必须为每张图提供 alt text，
  表格必须是真实标记而非截图，每个视频必须带隐藏字幕。自 2026 年 1 月 1 日起，ACM
  全部出版物开放获取。

## Skills 一览

| Skill | 用途 |
| --- | --- |
| [`chi-topic-selection`](skills/chi-topic-selection/SKILL.md) | 追问"谁会因这篇论文改变做法"，按 CHI 官方贡献类型分类，跑 subcommittee 匹配测试，并在 CHI、UIST、CSCW、DIS、IUI、ASSETS、IMWUT、TOCHI 之间诚实分流。 |
| [`chi-workflow`](skills/chi-workflow/SKILL.md) | 管理单截止日的一年：7 月开站、9 月全材料截止、12 月五周修改窗口、TAPS/publication-ready/注册链条、5 月会议，附责任人与风险清单。 |
| [`chi-writing-style`](skills/chi-writing-style/SKILL.md) | 写出分型的 contribution statement，面向混合方法陪审团行文，处理参与者引语，校准情境化 claim，保持可及性写作与可辩护的字数。 |
| [`chi-related-work`](skills/chi-related-work/SKILL.md) | 覆盖 CHI 检查的五条文献线（含馈源学科），按"战线"而非"清单"定位，化解最高频的 ADR-Context 筛查风险。 |
| [`chi-experiments`](skills/chi-experiments/SKILL.md) | 让证据形态匹配贡献类型：定量研究做功效分析、定性分析可审计、参与者与伦理信息按"结果页"标准报告。 |
| [`chi-reproducibility`](skills/chi-reproducibility/SKILL.md) | 在"以知情同意为边界尽量开放"原则下交付协议层、分析层、数据层透明度，并冷启动验证 availability statement。 |
| [`chi-supplementary`](skills/chi-supplementary/SKILL.md) | 为 9 月单一截止日产出带字幕的 video figure 与匿名补充材料包，并在 camera-ready 阶段制作 30 秒 video preview。 |
| [`chi-artifact-evaluation`](skills/chi-artifact-evaluation/SKILL.md) | 面向"只有五分钟的审稿人"与存档复用两类受众，打包原型、研究工具、codebook 与数据——这个会没有 badge 委员会替你把关。 |
| [`chi-submission`](skills/chi-submission/SKILL.md) | 上传 PCS 前的最终审计：字数制度、单栏模板、HCI 论文特有的匿名泄露渠道、desk-reject 分诊与截止周操作顺序。 |
| [`chi-review-process`](skills/chi-review-process/SKILL.md) | 建模评审管线：1AC/2AC 与外审、A/ARR/RR/RRX/X 量表、DR 与 rubric 化 ADR 筛查、revise-and-resubmit 门槛、PC meeting，并对照真实漏斗数据解读评审结果。 |
| [`chi-author-response`](skills/chi-author-response/SKILL.md) | 打好五周窗口：分诊评审意见、产出可审计的修订 diff、写出撑起第二轮的回复信。 |
| [`chi-camera-ready`](skills/chi-camera-ready/SKILL.md) | 把录用变成一篇发表且*无障碍*的论文：TAPS 源文件、全图 alt text、e-rights 与开放获取、video preview、注册截止日。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 12 条官方来源（URL + 访问日期）、已核验周期事实、明确的 待核实 清单，以及会议域名被拦截时的访问方式说明。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 在线官方入口（CHI 2027、SIGCHI 指南、PCS、TAPS、ACM DL）与每个里程碑前要跑的六个作者侧核验流程。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经 ACM DL 元数据核验的 CHI 论文（2009–2023），按贡献类型 × 方法分道，附自检问题与防误归属流程。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构智能音箱部署论文的摘要与引言，对照 CHI 筛查 rubric 逐步重写（before → after）。 |
| [`resources/code/README.md`](resources/code/README.md) | 共享可复现性工具包的适配器，外加通用工具无法覆盖的 5 项人类被试检查（同意范围、参与者去标识、研究工具完整性、视频字幕、AI 条件锁定）。 |

## 安装与使用

作为 Claude Code 插件使用（本目录是带 marketplace 清单的自包含插件）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./CHI-Skills
claude plugin install chi-skills
```

也可以直接使用文件：每个 `skills/chi-*/SKILL.md` 都是独立指令文件，frontmatter 中的
`description` 告诉 agent 何时触发。典型调用：

- "这个项目该投 CHI 还是 UIST？选哪个 subcommittee？" → `chi-topic-selection`
- "按 CHI 投稿规则审计我的稿件和补充材料" → `chi-submission`
- "收到 revise-and-resubmit 了，帮我规划这五周" → `chi-author-response`
- "带无障碍要求把 camera-ready 走完 TAPS" → `chi-camera-ready`

## 包结构

```text
CHI-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json（声明 12 个 skills）
├── README.md                # 英文说明
├── README.zh-CN.md          # 本文件
├── LICENSE                  # MIT
├── assets/cover.svg         # 封面
├── skills/
│   └── chi-<topic>/SKILL.md # 12 个 skills，一目录一技能
└── resources/
    ├── README.md            # 资源导览 + 建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # 共享可复现性工具包适配器
```

## 建议用法

1. **研究开始前** —— 先跑 `chi-topic-selection`：贡献类型决定证据方案，subcommittee
   决定受众。对照 exemplars library 看每种贡献类型的录用形态。
2. **构建证据时** —— 把 `chi-experiments` 与 `chi-reproducibility` 放在研究旁边：
   4 月就把知情同意的存档共享范围谈好、随手归档研究工具，到 8 月再补几乎不可能。
3. **写作时** —— 正文用 `chi-writing-style`，定位用 `chi-related-work`（它现在是
   筛查级问题），video figure 用 `chi-supplementary`；开头对照 worked example 重写。
4. **截止周** —— 对即将上传 PCS 的最终文件从头到尾跑一遍 `chi-submission`，包括对
   PDF、压缩包、外链与音轨的机械化匿名清查。
5. **投稿之后** —— 用 `chi-review-process` 解读第一轮结果，12 月窗口用
   `chi-author-response`，然后视 12 月 17 日的结果进入 `chi-camera-ready` 或回到
   `chi-topic-selection` 做改投分流。

## 周期锚点事实（历史快照，不是永久规则）

- CHI 2026：2026 年 4 月 13–17 日，西班牙巴塞罗那。CHI 2027：2027 年 5 月 10–14 日，
  美国宾夕法尼亚州匹兹堡。
- CHI 2027 Papers：PCS 于 2026-07-30 开放；**2026-09-10 全部材料截止**；修改稿
  2026-12-03；最终通知 2026-12-17；TAPS 源文件 2027-01-14；publication-ready
  2027-02-18；注册与报告视频 2027-03-04。
- 长度制度：鼓励 5,000–8,000 词；<5,000 为 short paper；>12,000 有 desk-reject
  风险；评审阶段用 ACM 单栏模板。
- CHI 2026 漏斗：6,730 篇完整投稿 → 2,603 篇获邀修改（38.7%）→ 1,705 篇有条件录用
  （总录用率 25.3%；重投稿件录用率 65.5%）。
- 筛查：格式类 desk reject + rubric 化 assisted desk reject（ADR-Context /
  ADR-Contribution / ADR-Data / ADR-Method），2026 年最高频依据是 ADR-Context。
- 出版：ACM TAPS；作者必须提供 alt text；2026-01-01 起 ACM 出版物全面开放获取。

## 事实纪律

本包区分三类陈述，skills 的行文保持三者可辨：

1. **已核验周期事实** —— 带日期/阈值，可追溯到 source map 中的编号来源（如 9 月 10
   日截止、A/ARR/RR/RRX/X 量表）。
2. **转述事实** —— 仅经二手渲染读取或由已发布日期推断，并如实标注（如第一轮结果的
   大致通知时间）。
3. **核验时不可确认项** —— 明确标注 待核实，写成待解决的问题而非事实（如 CHI 2027
   subcommittee 名单、PCS 上传上限、注册规则）。

若发现任何 skill 把第 2、3 类内容写成了第 1 类，请视为 bug，对照在线官方页面修正。

## 维护说明

- 上述所有日期与阈值都是 **2026→2027 周期快照**；给出任何 deadline 敏感建议前，先
  重新打开当年的 `chi<year>.acm.org` 页面。
- 2026-07-08 无法在线核验的条目已在 source map 中标注 待核实 —— 尤其是 CHI 2027
  subcommittee 名单、PCS 文件大小限制、注册与远程报告规则、AI 使用政策措辞，以及
  2027 作者适用的开放获取安排。确认前不得当作事实陈述。
- CHI 改评审流程的频率高于多数会议（ADR rubric 是 2026 周期引入的；字数措辞近几个
  周期反复调整）；任何"流程延续性"假设在这里都应当作错误处理。
- 新增范例论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程 —— CHI 没有 PMLR 式捷径，ACM DL 记录是唯一的 venue 证明。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md).
