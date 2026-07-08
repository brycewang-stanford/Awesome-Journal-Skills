# IEEE S&P Skills（中文说明）

面向 **IEEE S&P（IEEE Symposium on Security and Privacy，IEEE 安全与隐私研讨会）**
投稿的 12 个 agent skills。S&P 自 1980 年起举办，因最初在 Oakland 山区办会而在
安全领域被通称为"**Oakland**"，是安全与隐私方向的旗舰会议之一。本包覆盖一个完整
S&P 周期：判断"是否存在真实攻击者"、构建对抗级别的实验证据、组装带 ethics 记录的
匿名 HotCRP 投稿、应对带 early-reject 与短 rebuttal 的分轮评审、处理
**Accept / Revise / Reject** 三向决定，直至由 shepherd 把关的 IEEE camera-ready
与 artifact badges。

官方依据核验日期：**2026-07-08**。已核验 S&P 2027 Call for Papers 与各 cycle
deadline 页面、S&P 2026 CFP 与 artifact-evaluation 页面、IEEE Computer Society
安全与隐私技术委员会（TC）索引，以及 dblp 的 `conf/sp` proceedings 流。核验环境
无法直接抓取 `sp<年份>.ieee-security.org`，故官方页面内容经由搜索引擎对原始 URL
的渲染读取，并与 dblp、IEEE Xplore 交叉验证；完整来源链与所有"待核实"条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## S&P 与相邻会议的关键差异

以下 2026/2027 周期已核验的机制，决定了本包大部分建议的走向，也是从 USENIX
Security、CCS、NDSS——更不用说从 ML 或系统会议——转投 S&P 的作者最容易踩的坑：

- **每届 symposium 有多个投稿 cycle。** 每届 S&P 通过不止一个 cycle 收稿（2027
  届为 6 月与 11 月），每个 cycle 都是自成一体的小型会议，拥有独立的 HotCRP、
  具约束力的 registration 冻结、分轮评审与决定日。你要选的是 cycle，而非"截止
  日期"。
- **paper 截止前一周有具约束力的 registration。** 标题、完整摘要、含 **ORCID**
  的完整作者列表与 conflicts 在 registration 时冻结；ORCID 的姓名/邮箱必须与
  HotCRP 一致，否则 desk reject。
- **分轮评审，被淘汰者无 rebuttal。** 弱稿在第一轮直接被拒、没有申辩机会；
  存活论文看到评审并撰写约 5 天的 rebuttal。
- **三向决定，Revise 是标志性机制。** **Accept** 附带 draft meta-review 与
  **shepherd**；**Revise** 是针对一份书面 expectations summary 的结构化大修，
  需重新评审；**Reject** 触发一年 embargo（自原始投稿日起算），约 40% 重叠即
  视为 resubmission。
- **ethics 是结构性要求，不是点缀。** registration 时填写 Ethics
  Considerations 字段，Research Ethics Committee 可基于伦理理由拒稿，
  **Menlo Report** 为指定基线，需披露 IRB，涉及 PII 需说明 harm mitigation。
- **IEEE compsoc 模板下 13 + ≤5 页**、总计 18 页，且 **reviewers 无义务阅读
  appendix**——录用理由必须写在正文里。
- **SoK 是一等投稿类型**（`SoK:` 标题前缀加勾选框），**artifact evaluation**
  为录用后自愿参加，含 Available、Functional、Results Reproduced 三种 badge。

## Skills 一览

| Skill | 作用 |
| --- | --- |
| [`ieeesp-topic-selection`](skills/ieeesp-topic-selection/SKILL.md) | 用"真实攻击者测试"判断适配，决定 research 还是 SoK，并在 embargo 约束下于 USENIX Security、CCS、NDSS、PETS、CRYPTO 之间路由。 |
| [`ieeesp-workflow`](skills/ieeesp-workflow/SKILL.md) | 管理多 cycle 的一年：选 cycle、从 registration 周倒排，并为 Accept / Revise / Reject 各设专人。 |
| [`ieeesp-writing-style`](skills/ieeesp-writing-style/SKILL.md) | 通过第一轮存活测试——攻击者、有界主张、证据地图、why-now、ethics 信号——并压进 13 页 compsoc。 |
| [`ieeesp-related-work`](skills/ieeesp-related-work/SKILL.md) | 覆盖四大旗舰的文献窗口，写出 security-delta 句式，核验 dblp/Xplore 归属，保持自引匿名。 |
| [`ieeesp-experiments`](skills/ieeesp-experiments/SKILL.md) | 让评估匹配贡献类型，用 adaptive adversary 评估 defense，并以 trials 与离散度汇报攻击成功率。 |
| [`ieeesp-reproducibility`](skills/ieeesp-reproducibility/SKILL.md) | 冻结所测的"世界"——target 快照、硬件锁定、disclosure 时序——并在伦理限制下写诚实的可得性声明。 |
| [`ieeesp-supplementary`](skills/ieeesp-supplementary/SKILL.md) | 在 13 页正文与共享的 5 页 refs/appendix 之间分配内容，确保录用理由不落在 reviewers 可能不看的地方。 |
| [`ieeesp-artifact-evaluation`](skills/ieeesp-artifact-evaluation/SKILL.md) | 选择 Available / Functional / Reproduced badge，用 DOI 存档，并负责任地打包 exploit 与近似 malware 的代码。 |
| [`ieeesp-submission`](skills/ieeesp-submission/SKILL.md) | 最终 HotCRP 审计：registration 冻结、ORCID 匹配、compsoc 格式、含 disclosure 痕迹清扫的匿名化，以及 desk-reject 分级。 |
| [`ieeesp-review-process`](skills/ieeesp-review-process/SKILL.md) | 建模分轮、early reject、rebuttal、REC track、shepherd，以及作者真正有杠杆的位置。 |
| [`ieeesp-author-response`](skills/ieeesp-author-response/SKILL.md) | 为 5 天 rebuttal 分诊评审、回应 adaptive-attack 与 ethics 质疑，并把 Revise summary 当作合同。 |
| [`ieeesp-camera-ready`](skills/ieeesp-camera-ready/SKILL.md) | 处理 shepherd 的 concern ledger、加写 ethics section、去匿名并恢复 disclosure 细节，满足 IEEE compsoc/Xplore 要求。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 13 条官方来源（URL + 访问日期）、已核验的周期事实、明确的"待核实"清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及 registration 周、格式关、匿名、ethics 与录用后应执行的作者侧核验。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经元数据核验的真实 S&P 论文，覆盖 attack 与 SoK 车道，附自检问题与防误归属指南。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的 serverless 侧信道摘要与引言，重写为可通过第一轮无 rebuttal 评审（before → after）。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向共享可复现性工具包的适配层，并列出通用工具查不出的 S&P 专属检查（target 快照、disclosure 时序、危险材料处理）。 |

## 安装与调用

作为 Claude Code 插件使用（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./IEEE-SP-Skills
claude plugin install ieee-sp-skills
```

也可以直接把每个 `skills/ieeesp-*/SKILL.md` 当作独立指令文件使用：frontmatter
中的 `description` 描述了触发场景。典型调用示例：

- "这是真正的 S&P 论文，还是该投 USENIX Security？" → `ieeesp-topic-selection`
- "S&P 2027 我现实上能赶上哪个 cycle？" → `ieeesp-workflow`
- "按 S&P 投稿规则审计我的稿子" → `ieeesp-submission`
- "评审到了、我只有五天——规划 rebuttal" → `ieeesp-author-response`
- "我们拿到了 Revise，怎么处理？" → `ieeesp-review-process` + `ieeesp-author-response`

## 目录结构

```text
IEEE-SP-Skills/
├── .claude-plugin/            # plugin.json 与 marketplace.json（声明 12 个 skills）
├── README.md                  # 英文说明
├── README.zh-CN.md            # 本文件
├── LICENSE                    # MIT
├── assets/cover.svg           # 封面
├── skills/
│   └── ieeesp-<主题>/SKILL.md # 12 个 skill，一目录一文件
└── resources/
    ├── README.md              # 资源导览与推荐路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # 指向共享可复现性工具包
```

## 建议用法

1. **动笔之前**：先跑 `ieeesp-topic-selection`；若没有可辩护的攻击者，这一步就
   帮你省下一个 cycle 和一年 embargo。同时翻一遍 exemplars library，看"真实
   攻击者 + 端到端演示"在已录用论文里长什么样。
2. **规划 cycle**：用 `ieeesp-workflow` 从具体的 registration 周倒排；ethics
   latency（disclosure、IRB）是团队最容易放错位置的一项。
3. **做实验期间**：把 `ieeesp-experiments` 与 `ieeesp-reproducibility` 放在
   代码库旁边；adaptive-adversary 评估与 target 快照早装远比截稿周补装便宜。
4. **写作期间**：正文用 `ieeesp-writing-style`，正文/附录分层用
   `ieeesp-supplementary`，定位用 `ieeesp-related-work`，并对照 worked example
   的前后对比。
5. **截稿周**：从头到尾执行 `ieeesp-submission`，包括 ORCID 与 disclosure 痕迹
   的匿名检查，并把 registration 周当作独立的截止日。
6. **投稿之后**：用 `ieeesp-review-process` 校准预期；评审出来后用
   `ieeesp-author-response`；随后按决定进入 `ieeesp-camera-ready`（与 shepherd
   配合）或 Revise / rejection 分支。

## 事实纪律

本包区分三类陈述，skills 的写法保证三类可辨：

1. **已核验的周期事实**——带日期/上限，且能在 source map 中追溯到编号来源（如
   13 页正文上限、2026 年 11 月 17 日的 Cycle 2 截稿、Accept/Revise/Reject
   决定集）。
2. **转述事实**——只见于二手来源并明确标注（如 S&P 2025 的投稿/录用数量，来自
   机构获奖公告）。
3. **核验时无法确认的条目**——明确标注 **待核实**，以"待解决问题"而非事实的
   口吻表述（如 2027 Cycle 1 的评审时间表、Revise 的 resubmission 目标 cycle、
   2027 camera-ready 与 artifact 时间表）。

若发现任何 skill 把第 2、3 类内容写成了第 1 类的口吻，请视为 bug，对照官方页面
修正。

## 维护说明

- 上述日期与上限均为 **周期快照**；给出任何与截止日期相关的建议前，必须重新
  打开当年 `sp<年份>.ieee-security.org` CFP 与各 cycle deadline 页面。
- S&P 的截止时间以**固定时钟**（如 7:59:59 AM EDT）表述，而非 Anywhere-on-Earth
  ——请换算到你所在时区，不要默认 AoE。
- 2026-07-08 无法在线核验的条目已在 source map 中标注 **待核实**——尤其是 2027
  Cycle 1 的评审日期、Revise 的 resubmission 机制、2027 camera-ready 与
  artifact-evaluation 时间表、PC chairs 与 REC 名单，以及 generative-AI 政策的
  确切措辞。确认之前不得当作事实陈述。
- PC chairs 与 REC 每届轮换、政策逐年重设；不要把期刊包里"常任主编"式的连续性
  假设带到这里。
- 新增范文请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——仅凭一个"SP"字样不能证明论文属于主会 S&P（EuroS&P 与 SPW
  workshops 是不同 venue）。

## 许可证

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
