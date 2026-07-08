# NDSS Skills

面向 **NDSS（Network and Distributed System Security Symposium，网络与分布式系统安全研讨会）**
论文的 12 个 agent skills。NDSS 由 Internet Society 主办，与 IEEE S&P、USENIX Security、
ACM CCS 并称安全领域"四大"（big four）。本包覆盖一个 NDSS 周期的完整链路：判断攻击者模型
是否真实、构建具备部署真实性的证据、准备 double-blind 的 HotCRP 投稿及其 ethics 记录、
在带 early reject 与 interactive rebuttal 的**两轮评审**中生存、处理 **Accept / Minor
Revision / Major Revision** 决定，并完成 Internet Society 开放获取的 camera-ready 与可选的
artifact badges。

官方依据核验日期：**2026-07-08**。已核验 NDSS 2027 Call for Papers 与 Call for Artifacts、
`ndss27-summer.hotcrp.com` 现行周期站点、Internet Society 2026 年 6 月关于移师首尔的公告、
NDSS 2026 co-located events 与开放出版页面、Test of Time 奖页面，以及 dblp `conf/ndss`。在
核验环境中直接抓取 `ndss-symposium.org` 与 `dblp.org` 返回 HTTP 403，因此官方页面通过搜索
引擎对精确 URL 的渲染阅读，并与 HotCRP、Internet Society 页面、dblp 记录交叉核对；完整链路
（含所有 待核实 项）见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## NDSS 与同类会议的区别

以下机制按 2027 届核验，驱动了各 skill 的大部分建议，也是从其他安全会议或 ML／系统会议
转投作者最容易犯错之处：

- **一个刚刚改变的固定身份。** 数十年来 NDSS 就等于"二月的圣地亚哥"。2027 届刻意打破这一
  惯例：**韩国首尔，2027 年 3 月 22-26 日**，以扩大亚太参与。连举办城市都要当作逐届事实。
- **两个投稿周期汇入同一届会议。** summer 周期（2027 论文截止 2026-05-06）与
  **fall 周期（论文截止 2026-08-19）**，各自是完整流程。在同一届内某周期被拒的论文，不得
  以重大重叠再投另一周期——周期选择是策略问题，且 fall 截止可能就在眼前。
- **带 early reject 的两轮评审。** Round 1 以快读筛除末段且无 rebuttal；进入 Round 2 者可见
  评审意见、提交 rebuttal，并进入与评审的 **interactive discussion** 阶段。
- **偏重修订的决定集合。** 除 Accept 与 Reject 外，NDSS 还给出 **Minor Revision** 与
  **Major Revision**；后者附带评审撰写的 revision tasks 清单，按清单复审，每篇至多一次。
- **Ethics 是结构性的。** 可选的 **Ethics Considerations section**（不计入页数）、由 TPC 成员
  组成、可因伦理问题拒稿的 **Ethics Review Board**、作为基准的 **Menlo Report**，以及对高影响
  漏洞的披露要求——单有 IRB 批准并不被视为充分。
- **13 页，豁免宽松。** NDSS 模板 13 页正文，ethics 部分、参考文献与附录不计入——但评审无需
  阅读附录，因此录用理由必须落在正文内。
- **免费、开放获取的 proceedings。** Internet Society 向全世界免费发布论文与报告视频，无读者
  付费墙、无作者版面费，作者可自行存档 camera-ready。
- **自愿参加的 artifact evaluation。** 在有条件录用后，作者可争取首页的
  **Available / Functional / Reproduced** 徽章及 2 页 artifact 附录。

## Skills

| Skill | 作用 |
| --- | --- |
| [`ndss-topic-selection`](skills/ndss-topic-selection/SKILL.md) | 应用 wire / deployment-envelope / adversary-ownership 三项测试，并在 IEEE S&P、USENIX Security、CCS、PETS、IMC、ACSAC 间按贡献形态分流。 |
| [`ndss-workflow`](skills/ndss-workflow/SKILL.md) | 运行双周期年度：选 summer 或 fall，从 AoE 截止倒排至 disclosure clock，并按决定分支——从 NDSS 视角讲述四大日历。 |
| [`ndss-writing-style`](skills/ndss-writing-style/SKILL.md) | 构建首页 contract——能力受限的攻击者、与证据匹配的主张、编织式 ethics——并压入 13 页应对两轮阅读。 |
| [`ndss-related-work`](skills/ndss-related-work/SKILL.md) | 覆盖 flagship、专门会议与 advisory/RFC 文献，写机制级 delta，对开放 proceedings 与 dblp 核验，并保持自引匿名。 |
| [`ndss-experiments`](skills/ndss-experiments/SKILL.md) | 按贡献类型在 live、testbed、emulation 之间匹配证据，对 adaptive adversary 评估防御，并保持测量诚实。 |
| [`ndss-reproducibility`](skills/ndss-reproducibility/SKILL.md) | 冻结被测互联网、清洗携带身份的 traces、维护 claims ledger，并撰写经得起开放获取审视的可得性声明。 |
| [`ndss-supplementary`](skills/ndss-supplementary/SKILL.md) | 在 13 页正文、不计页数的 ethics 部分与附录间按评审状态分配内容，并补充 camera-ready 的 artifact 附录。 |
| [`ndss-submission`](skills/ndss-submission/SKILL.md) | HotCRP 终审：AoE 时钟、模板与页数、double-blind 排查、ethics 就绪、每作者六篇上限与重叠规则、desk-reject 分诊。 |
| [`ndss-review-process`](skills/ndss-review-process/SKILL.md) | 建模两轮评审、early reject、rebuttal 与 interactive discussion、Accept/Minor/Major 决定集合与 Ethics Review Board。 |
| [`ndss-author-response`](skills/ndss-author-response/SKILL.md) | 分诊 Round-2 意见，以可定位证据回应 adaptive-attack 与 ethics 质疑，并向 Accept 或有界修订推进。 |
| [`ndss-artifact-evaluation`](skills/ndss-artifact-evaluation/SKILL.md) | 瞄准 Available/Functional/Reproduced 徽章，负责任地打包 exploit 与 traces，撰写 2 页 artifact 附录。 |
| [`ndss-camera-ready`](skills/ndss-camera-ready/SKILL.md) | 完成修订条件、去匿名、恢复披露细节、放置已获徽章，并满足 Internet Society 开放获取要求。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 11 个官方来源（URL 与访问日期）、访问方式说明、已核验 2027 周期事实、reported facts 与 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方入口，以及 cycle／format／anonymity／ethics／cap／post-acceptance 六项作者自查。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经元数据核验的 NDSS 论文（含 2 篇 Test of Time），附自检问题与已核验误标清单。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一篇虚构的 stale-delegation DNS 论文摘要与引言，围绕攻击者模型、测量纪律与披露改写，before → after。 |
| [`resources/code/README.md`](resources/code/README.md) | 通往共享可复现工具的适配层，以及通用工具无法做的 NDSS 专项检查（trace 清洗、live-Internet 快照、exploit 门控）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自带 marketplace 清单的独立插件）：

```bash
# 从仓库克隆处
claude plugin marketplace add ./NDSS-Skills
claude plugin install ndss-skills
```

或直接使用文件：每个 `skills/ndss-*/SKILL.md` 都是独立指令文件，其 frontmatter 的
`description` 告知 agent 何时触发。典型调用：

- "这是 NDSS 论文，还是该投 USENIX Security？" → `ndss-topic-selection`
- "我还赶得上 NDSS fall 周期吗？" → `ndss-workflow`
- "按 NDSS 投稿规则审我的草稿" → `ndss-submission`
- "进入 Round 2，帮我规划 rebuttal" → `ndss-author-response`
- "我们拿到了 Major Revision，怎么办？" → `ndss-review-process` + `ndss-author-response`

## 事实纪律

各 skill 区分三类陈述：

1. **已核验周期事实**——带日期／上限并追溯到 source map 中编号来源（2026-08-19 fall 截止、
   13 页限制、Accept/Minor/Major 决定集合、移师首尔）。
2. **Reported facts**——仅见于二手来源并如实标注（如个人页面上出现的某 Publication Chair）。
3. **核验时不可确证项**——标 待核实、以待解问题呈现，绝不当作事实（fall HotCRP 网址、Major
   Revision 重投窗口、2027 chairs、任何生成式 AI 政策、2027 co-located 工作坊清单、2027
   artifact 截止）。

若发现某 skill 将第 2、3 类当作第 1 类，请视为 bug 并对照官方页面修正。

## 维护说明

- 上述每个日期、上限与城市都是**周期快照**——给出 deadline 敏感建议前，重开当年
  `ndss-symposium.org` CFP 与现行 HotCRP 站点。
- NDSS 截止采用 **Anywhere-on-Earth（UTC-12）**；请刻意换算。
- 2027 移师首尔证明连 NDSS 最固定的属性（二月的圣地亚哥）都是逐届的。不要把任何单一事实
  当作永久规则前推。
- Chairs、ERB、模板版本、HotCRP 网址与徽章定义均逐届轮换或重设；把期刊式的连续性假设当作
  错误。
- 新增 exemplar 论文时，遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  中的流程——网络安全类标题不等于 NDSS，USENIX Security、S&P、CCS、IMC 共享同一题材。

## License

MIT，见 [`LICENSE`](LICENSE)。English README: [`README.md`](README.md)。
