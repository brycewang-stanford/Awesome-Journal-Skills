# USENIX Security Skills

面向 **USENIX Security Symposium（USENIX 安全研讨会）** 投稿的 12 个 agent skills。它是
计算机安全"四大"顶会之一；由于 USENIX ATC 在 2025 年后停办，USENIX Security 现已成为
USENIX 的旗舰夏季会议。本包覆盖一个 USENIX Security 周期的完整流程：判断工作是否属于
可审计的安全贡献、构建符合威胁模型的证据、组织"13 页正文 + 附录"的投稿、在双周期
HotCRP 评审与 shepherding 流程中存活，以及交付开放获取的 camera-ready 与两阶段
artifact evaluation。

官方依据核验日期：**2026-07-08**。已核验 USENIX Security '26 Call for Papers 与 Call for
Artifacts、各周期 HotCRP deadline 页面、社区 artifact-evaluation 说明、USENIX Security
ethics guidelines、'25 reviewing-model 页面（作为有据可查的历史），以及 '27 会议页面。
在核验环境中，直接抓取 `usenix.org`、`*.usenix.hotcrp.com` 与 `dblp.org` 均返回 HTTP 403，
因此官方页面通过搜索引擎对确切 URL 的渲染来阅读，并与多份渲染、USENIX 录用论文列表和
第二方 deadline 追踪站交叉核对；完整记录（含所有仍标注 待核实 的条目）见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## USENIX Security 与兄弟会议的不同

以下会议机制针对 '26 周期核验，决定了 skills 中的大部分建议，也是从其他会议转来的作者
最常犯错的地方：

- **每年两个投稿周期，各自是一条完整 HotCRP 流水线。** 每个周期都以一次强制的论文
  **registration** 开始，约在论文截止前一周；未注册的论文无法上传。"何时投稿"是一个
  策略选择，而非固定日期。
- **Major Revision 已取消。** 自 '26 起，本会取消 Invited-Major-Revision。现在的结果是
  Accept、**Accepted on Shepherd Approval**（最多两周 shepherding —— 只改文字，不加实验），
  或 reject。旧的"85% 完成度投稿再靠 revision 补救"的安全网不复存在。
- **Open Science 强制且与录用挂钩。** 每篇投稿都带一个 **Open Science 附录**，说明其
  artifacts 所在；论文录用以 finals 之前通过 **Phase-1 artifact 可用性检查** 为条件。
- **Ethics 是门槛，不是评分项。** 强制的 **Ethical Considerations 附录**、漏洞披露预期，
  以及针对 live-system 研究的 IRB/人类被试文档，可以单独让一篇技术过硬的论文被拒。
- **两阶段 artifact evaluation，三枚可独立授予的徽章** —— Artifacts Available（强制）、
  Artifacts Functional、Results Reproduced（两者可选，在 finals 之后）。
- **开放获取、作者不付费。** USENIX 在 usenix.org 上免费发布论文与报告录像；作者义务是
  在研讨会现场做报告。
- **可审计的证据是本会风格。** 评审群体看重可复现的攻击、标明观测点（vantage）的测量，
  以及对自适应攻击者做过评估的防御。

## Skills

| Skill | 作用 |
| --- | --- |
| [`usenixsec-topic-selection`](skills/usenixsec-topic-selection/SKILL.md) | 应用"移除攻击者"测试，按评审契合度在 USENIX Security、IEEE S&P、CCS、NDSS 与专门会议（PETS、SOUPS、WOOT）之间路由。 |
| [`usenixsec-workflow`](skills/usenixsec-workflow/SKILL.md) | 在两个年度周期间抉择，从 registration 硬墙倒排计划，并把会议特有风险分配到负责人。 |
| [`usenixsec-writing-style`](skills/usenixsec-writing-style/SKILL.md) | 把威胁模型前置，用总体量与离散度校准安全主张，并把披露叙事织入正文。 |
| [`usenixsec-related-work`](skills/usenixsec-related-work/SKILL.md) | 覆盖四大与专门会议的文献车道，处理多周期日历下的 concurrent work，并以双盲方式引用自己的工作。 |
| [`usenixsec-experiments`](skills/usenixsec-experiments/SKILL.md) | 把实验与主张类型对齐 —— 防御要自适应攻击者、检测要 base rate、测量要 vantage validity、live system 要 ethics。 |
| [`usenixsec-reproducibility`](skills/usenixsec-reproducibility/SKILL.md) | 撰写 Open Science 附录，决定哪些能公开哪些不能，并为受时间与环境耦合的安全实验做环境指纹。 |
| [`usenixsec-supplementary`](skills/usenixsec-supplementary/SKILL.md) | 按阅读保证在 13 页正文、两个强制附录、可选附录与外部 artifact 间分配材料。 |
| [`usenixsec-artifact-evaluation`](skills/usenixsec-artifact-evaluation/SKILL.md) | 通过强制的 Phase-1 可用性检查，并安全打包有危险性的安全 artifact 以争取可选的 Phase-2 徽章。 |
| [`usenixsec-submission`](skills/usenixsec-submission/SKILL.md) | 最终 HotCRP 审核：registration、13 页版式、两个命名附录、机械匿名检查、early-reject 风险。 |
| [`usenixsec-review-process`](skills/usenixsec-review-process/SKILL.md) | 建模双周期流程、已取消的 Major Revision、shepherd-approval，以及周期间的 resubmission 限制。 |
| [`usenixsec-author-response`](skills/usenixsec-author-response/SKILL.md) | 撰写能在线上讨论中存活的评审回应，处理被要求的 ethics 修订，并在录用后与 shepherd 协作。 |
| [`usenixsec-camera-ready`](skills/usenixsec-camera-ready/SKILL.md) | 把录用转化为正确的开放获取条目：去匿名、切换 artifact URL、Phase-1 签核、报告义务。 |

## Resources

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 十个官方来源（URL 与访问日期）、访问方式说明、已核验的 '26/'27 事实、明确的 待核实 清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方界面（HotCRP、CFP、Call for Artifacts、ethics、proceedings）与上传前的作者端核验步骤。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 五篇已核验的 USENIX Security '24 Distinguished Paper Award 论文，覆盖五个 主题 × 证据形态 车道，附自检问题与防误标指南。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构的证书 pinning 测量论文摘要与引言，按 USENIX Security 标准 before → after 重建。 |
| [`resources/code/README.md`](resources/code/README.md) | 通向共享会议可复现工具包的适配器，外加通用工具无法完成的 USENIX Security 专有检查（危险性、Open Science、双盲）。 |

## 安装与使用

作为 Claude Code 插件（本目录是自包含插件，带有自己的 marketplace 清单）：

```bash
# 在仓库克隆中执行
claude plugin marketplace add ./USENIX-Security-Skills
claude plugin install usenix-security-skills
```

或直接使用文件：每个 `skills/usenixsec-*/SKILL.md` 都是独立的指令文件，其 frontmatter 的
`description` 告诉 agent 何时触发。典型调用：

- "这篇测量研究该投 USENIX Security 还是 IMC？" → `usenixsec-topic-selection`
- "按 USENIX Security 投稿规则审核我的初稿" → `usenixsec-submission`
- "评审意见来了，帮我规划回应" → `usenixsec-author-response`
- "把我的扫描器打包送 artifact evaluation" → `usenixsec-artifact-evaluation`

## 包结构

```text
USENIX-Security-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json（声明 12 个 skill）
├── README.md                    # 英文说明
├── README.zh-CN.md              # 本文件
├── LICENSE                      # MIT
├── assets/cover.svg             # 封面
├── skills/
│   └── usenixsec-<topic>/SKILL.md   # 12 个 skill，各一目录
└── resources/
    ├── README.md                # 资源指南与建议路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md           # 通向共享可复现工具包的适配器
```

## 建议用法

1. **动笔前** —— 运行 `usenixsec-topic-selection`；若"移除攻击者"测试不通过，本包就替你
   省下了一个周期。浏览 exemplars 库，看看获奖形态的可审计安全贡献长什么样。
2. **构建时** —— 让 `usenixsec-experiments` 与 `usenixsec-reproducibility` 常开在代码旁；
   自适应攻击者实验与披露时钟，早开始比在截止周补救便宜得多。
3. **写作时** —— 正文用 `usenixsec-writing-style`，正文/附录/artifact 拆分用
   `usenixsec-supplementary`，定位用 `usenixsec-related-work`；对照 worked example 的
   before/after。
4. **截止周** —— 完整走 `usenixsec-submission`，含 registration 与机械匿名检查；注意
   registration 硬墙在论文截止前一周。
5. **投稿后** —— 用 `usenixsec-review-process` 校准预期，评审意见到来时用
   `usenixsec-author-response`，随后按 notification 邮件走 `usenixsec-camera-ready`
   （含 Phase-1 artifact 时钟）或拒稿分诊。

## 2026/2027 锚点事实（历史快照，非永久规则）

- **USENIX Security '26** 为第 35 届：**Baltimore Marriott Waterfront，2026 年 8 月 12–14 日**。
  Program co-chairs：Elissa Redmiles（Georgetown）与 Ben Stock（CISPA）。
- **Sec '26 Cycle 1**：registration 2025-08-19 · submission 2025-08-26 · early reject
  2025-10-07 · notification 2025-12-04 · finals 2026-01-15。
- **Sec '26 Cycle 2**：registration 2026-01-29 · submission 2026-02-05 · early reject
  2026-03-17 · notification 2026-05-14 · finals 2026-06-11。所有截止均为 11:59 pm AoE。
- **版式**：未改动的 USENIX Security LaTeX 模板 · 正文 ≤ 13 页 · references 前有强制的
  "Ethical Considerations" 与 "Open Science" 附录（各 ≤ 1 页）。
- **USENIX Security '27** 为第 36 届：**Denver，2027 年 8 月 11–13 日**，chairs 为
  Adam Doupé（Arizona State）与 Andrei Sabelfeld（Chalmers）；Cycle 1 registration
  2026-08-18 / submission 2026-08-25；Cycle 2 registration 2027-01-19 / submission
  2027-01-26。
- **Proceedings**：USENIX 开放获取，作者不付费。

## 事实纪律

本包区分三类陈述，skills 的写法保持它们可区分：

1. **已核验的 2026/2027 周期事实** —— 带日期/上限，可追溯到 source map 中编号来源
   （如 13 页正文、Cycle 2 的 2 月 5 日截止）。
2. **转述事实** —— 仅见于第二方来源并如实标注（如 '27 program co-chairs，来自会议追踪站
   渲染）。
3. **核验时无法确证的条目** —— 明确标注 待核实，以待解决的问题形式呈现，绝不当作事实
   （如 '27 notification 日期、resubmission 限制、任何 AI 使用政策）。

若发现 skills 中把第 2 或第 3 类材料当作第 1 类呈现，视为 bug，对照官方页面修正。

## 维护说明

- 上述每个日期与上限都是 **周期快照**；涉及 deadline 的建议前，请重开当年的
  `usenix.org/conference/usenixsecurity<NN>` 页面与当周期 HotCRP 站点。
- 2026-07-08 无法在线核验的条目在 source map 中标为 待核实 —— 尤其是 '27 的
  early-reject/notification/finals 日期、'27 的 AoE 约定、周期间 resubmission 限制，以及
  任何 AI 辅助政策。确证前不要当作事实陈述。
- USENIX Security 的 chairs 每届轮换、政策逐年重置；把期刊包里带来的"主编连续性"假设
  用在这里都是错误。
- **Major Revision 已在 '26 取消** —— 若某个 skill 或记忆有相反说法，即为过时。当前的
  中间结果是 shepherd approval。
- 新增 exemplar 论文时，遵循
  [`resources/exemplars/library.md`](resources/exemplars/library.md) 末尾的核验流程 ——
  CVE 或某场演讲中出现同名，并不能证明学术论文或其发表会议。

## 许可

MIT —— 见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md)。
