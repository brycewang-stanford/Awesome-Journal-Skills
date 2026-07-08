# UAI Skills（中文说明）

面向 **UAI（Conference on Uncertainty in Artificial Intelligence，人工智能不确定性会议）**
投稿的 12 个 agent skills。UAI 由 AUAI（Association for Uncertainty in Artificial
Intelligence）主办，是 probabilistic reasoning、graphical models、causal inference、
Bayesian methods 与 decision making under uncertainty 方向的年度顶级会议。本包覆盖
一个完整 UAI 周期：判断"不确定性是否真的是论文贡献本身"、构建 inference 级别的实验
证据、组装单一 PDF 投稿、应对 OpenReview 评审与 author response，直至 PMLR
camera-ready 与 poster/spotlight 报告。

官方依据核验日期：**2026-07-08**。已核验 UAI 2026 Call for Papers、submission
instructions、important dates、reviewer/AC instructions、UAI 2026 OpenReview
group、AUAI code of conduct，以及 UAI 2020–2025 各届 PMLR proceedings。核验环境
无法直接抓取 `auai.org`，故官方页面内容经由搜索引擎对原始 URL 的渲染读取，并与
OpenReview、PMLR volume 页面及 GitHub 上的 `mlresearch` 元数据仓库交叉验证；完整
来源链与所有"待核实"条目见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## UAI 与相邻会议的关键差异

以下 2026 周期已核验的机制，决定了本包大部分建议的走向，也是从其他会议转投 UAI
的作者最容易踩的坑：

- **一个 PDF 承载全部评审内容。** 正文（main part）不超过 8 页，references 与
  appendices 不限页数、但必须放在**同一个 PDF** 内（≤ 15 MB）。没有单独的补充材料
  截止日；证明永远在评审记录之内。
- **ZIP 是"可选阅读"。** 可附带一个补充压缩包（≤ 50 MB，代码/数据），但规则明确
  写着 reviewers 没有义务查看——任何影响录用判断的证据都不能只放在 ZIP 里。
- **四条公开评审标准。** technical correctness、novelty、claims 是否有说服力的
  支撑（backing）、writing 的清晰度（clarity）。
- **审稿志愿条款。** 投稿即表示：若 Program Chairs 需要，至少一位作者同意为 UAI
  审稿。
- **所有录用论文均以 poster + spotlight 形式报告**（2026 年措辞为"physically or
  remotely"），部分论文获得更长报告时间；全部发表于 PMLR（开放获取，作者无需
  付费）。
- **不确定性必须是论文主题本身。** 评审池集中于概率推断、图模型、因果与贝叶斯
  统计；概率只作点缀的论文即使技术过硬也会被建议改投他处。

## Skills 一览

| Skill | 作用 |
| --- | --- |
| [`uai-topic-selection`](skills/uai-topic-selection/SKILL.md) | 用"删除测试"（删掉全部概率成分后还剩什么？）判断适配度，并在 UAI、AISTATS、NeurIPS/ICML、COLT、CLeaR 与期刊之间路由。 |
| [`uai-workflow`](skills/uai-workflow/SKILL.md) | 管理一年一投的节奏：2 月截稿、春季评审各阶段、6 月放榜、7 月 camera-ready、8 月开会，并为各类风险指定专人。 |
| [`uai-writing-style`](skills/uai-writing-style/SKILL.md) | 执行记号纪律（conditioning 与 `do(·)` 严格区分）、带编号的假设台账、8 页论证主干与克制的措辞。 |
| [`uai-related-work`](skills/uai-related-work/SKILL.md) | 覆盖 UAI 审稿人必查的五条文献线，核对 PMLR volume 与会议归属，保持自引的双盲纪律。 |
| [`uai-experiments`](skills/uai-experiments/SKILL.md) | 设计 exact-truth / stress / real-data 三级实验阶梯，让指标直接测量所声称的概率对象，并汇报多 seed 的离散度。 |
| [`uai-reproducibility`](skills/uai-reproducibility/SKILL.md) | 建立确定性台账、采样器诊断（R-hat/ESS）、ELBO 与 coverage 记录，以及诚实的代码可得性声明。 |
| [`uai-supplementary`](skills/uai-supplementary/SKILL.md) | 按"评审地位"而非方便程度，在 8 页正文、同一 PDF 的 appendix、可选 ZIP 三层之间分配内容。 |
| [`uai-artifact-evaluation`](skills/uai-artifact-evaluation/SKILL.md) | 为"只给你五分钟的怀疑者"打包代码与数据：每条结论一条命令，全程匿名，符合体积上限。 |
| [`uai-submission`](skills/uai-submission/SKILL.md) | 上传前的最终审计：各类上限、模板、机械化匿名检查、一稿多投与审稿志愿条款、desk-reject 风险分级。 |
| [`uai-review-process`](skills/uai-review-process/SKILL.md) | 建模评审流水线——bidding、评审撰写、author response、reviewer-AC 讨论、决定——并指出作者真正有杠杆的位置。 |
| [`uai-author-response`](skills/uai-author-response/SKILL.md) | 把每条评审意见映射到四条标准之一，用编号、有证据锚点、匿名的回复面向后续 AC 讨论写作。 |
| [`uai-camera-ready`](skills/uai-camera-ready/SKILL.md) | 把录用转化为规范的 PMLR 条目：去匿名、表单、公开 artifact、poster 与 spotlight 准备。 |

## Resources 一览

| 路径 | 内容 |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | 10 条官方来源（URL + 访问日期）、已核验的 2026 周期事实、明确的"待核实"清单。 |
| [`resources/external_tools.md`](resources/external_tools.md) | 官方在线入口，以及上传前应执行的五轮作者侧核验。 |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | 5 篇经元数据核验的真实 UAI 论文（PMLR v161/v216/v244），覆盖五个 topic × method 车道，附自检问题与防误归属指南。 |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | 一个虚构因果发现论文的摘要与引言，按四条评审标准逐步重写（before → after）。 |
| [`resources/code/README.md`](resources/code/README.md) | 指向仓库级 ML 会议可复现性工具包的适配层，并列出通用工具查不出的 UAI 专属检查项。 |

## 安装与调用

作为 Claude Code 插件使用（本目录自带 marketplace 清单，可独立安装）：

```bash
# 在仓库克隆目录下
claude plugin marketplace add ./UAI-Skills
claude plugin install uai-skills
```

也可以直接把每个 `skills/uai-*/SKILL.md` 当作独立指令文件使用：frontmatter 中的
`description` 描述了触发场景。典型调用示例：

- "这个可识别性结果该投 UAI 还是 AISTATS？" → `uai-topic-selection`
- "按 UAI 投稿规则审计我的稿子" → `uai-submission`
- "评审意见到了，帮我规划 rebuttal" → `uai-author-response`
- "把采样器实验打包成补充材料" → `uai-artifact-evaluation`

## 目录结构

```text
UAI-Skills/
├── .claude-plugin/          # plugin.json 与 marketplace.json（声明 12 个 skills）
├── README.md                # 英文说明
├── README.zh-CN.md          # 本文件
├── LICENSE                  # MIT
├── assets/cover.svg         # 封面
├── skills/
│   └── uai-<主题>/SKILL.md  # 12 个 skill，一目录一文件
└── resources/
    ├── README.md            # 资源导览与推荐路线
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # 指向共享可复现性工具包
```

## 建议用法

1. **动笔之前**：先跑 `uai-topic-selection`；删除测试不通过就换会——这是本包最省
   时间的一步。同时翻一遍 exemplars library，看"不确定性作为贡献本身"在已录用
   论文里长什么样。
2. **做实验期间**：把 `uai-experiments` 与 `uai-reproducibility` 放在代码库旁边；
   三级实验阶梯和确定性台账在早期安装远比截稿周补装便宜。
3. **写作期间**：正文用 `uai-writing-style`，正文/附录/ZIP 分层用
   `uai-supplementary`，定位用 `uai-related-work`，并对照 worked example 的
   前后对比。
4. **截稿周**：从头到尾执行 `uai-submission`，包括对合并后 PDF 的机械化匿名与
   体积检查。
5. **投稿之后**：用 `uai-review-process` 校准预期；评审出来后用
   `uai-author-response`；6 月放榜后进入 `uai-camera-ready` 或 rejection 分诊。

## 2026 周期锚点事实（历史快照，非永久规则）

- UAI 2026 为第 **42** 届：荷兰阿姆斯特丹，**2026 年 8 月 17–21 日**（周一
  tutorials，周二至周四正会，周五 workshops）。
- 投稿窗口：**2026-01-25 至 2026-02-25，23:59 AoE**，OpenReview 提交。
- 2026 流水线：bidding 3/2–3/9 · 评审撰写 3/21–4/11 · author response
  4/23–5/2 · reviewer-AC 讨论 5/2–5/8 · 放榜 6/1 · camera-ready 7/27。
- 格式：UAI LaTeX 模板 · 正文 ≤ 8 页 · references/appendices 不限页且在同一
  PDF · PDF ≤ 15 MB · 可选 ZIP ≤ 50 MB。
- 出版：PMLR（开放获取，作者免费）。卷号锚点：v124 = 2020、v161 = 2021、
  v180 = 2022、v216 = 2023、v244 = 2024、v286 = 2025。

## 事实纪律

本包区分三类陈述，skills 的写法保证三类可辨：

1. **已核验的 2026 周期事实**——带日期/上限，且能在 source map 中追溯到编号来源
   （如正文 8 页上限、2 月 25 日截稿）。
2. **转述事实**——只见于二手来源并明确标注（如 2026 general chairs 名单，来自
   组织者个人主页）。
3. **核验时无法确认的条目**——明确标注 **待核实**，以"待解决问题"而非事实的口吻
   表述（如注册规则、LLM 政策）。

若发现任何 skill 把第 2、3 类内容写成了第 1 类的口吻，请视为 bug，对照官方页面
修正。

## 维护说明

- 上述日期与上限均为 **2026 周期快照**；给出任何与截止日期相关的建议前，必须
  重新打开当年 `auai.org/uai<年份>/` 官方页面。
- 2026-07-08 无法在线核验的条目已在 source map 中标注 **待核实**——尤其是 2026
  Program Chairs 名单、camera-ready 页数额度、注册费与远程报告细则、LLM/AI 使用
  政策、UAI 2026 的 PMLR 卷号。确认之前不得当作事实陈述。
- UAI 的主席每届轮换、政策逐年重设；不要把期刊包里"常任主编"式的连续性假设带到
  这里。
- 新增范文请遵循 [`resources/exemplars/library.md`](resources/exemplars/library.md)
  末尾的核验流程——仅凭 PMLR 卷号不能证明论文属于 UAI。

## 许可证

MIT，见 [`LICENSE`](LICENSE)。English version: [`README.md`](README.md).
