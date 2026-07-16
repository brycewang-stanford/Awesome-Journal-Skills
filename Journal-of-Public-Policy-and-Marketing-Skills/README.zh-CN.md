# Journal of Public Policy & Marketing Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of Public Policy & Marketing Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of Public Policy & Marketing（JPP&M）** 投稿的 12 个 agent skills。JPP&M 是 AMA 旗下、由 SAGE 出版的期刊，定位于营销、公共政策与消费者/社会福祉的交叉点。本包围绕其独有的"政策相关性硬门槛"设计：每篇论文都必须切入一个正在进行的政策议题（消费者保护、警示与标签、隐私与数据政策、公共健康营销、可持续性、金融福祉、弱势消费者、市场公平），并给出监管机构（FTC、FDA、CFPB）、NGO 或受监管营销者可以真正落地的政策含义。

**官方依据核验日期：2026-07-16**（投稿前需复核易变细节）：见 [`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JPP&M 约束 | 对稿件的要求 |
|------------|--------------|
| Policy Contribution Statement（≤300 词，必交，供桌面初筛） | 动笔前必须说清政策议题、超越现有文献之处、可采取行动的利益相关者 |
| 方法多元但有反事实门槛 | 实验须使用"可被强制推行"的刺激材料；政策评估须有可信的 DiD/RDD/合成控制对照 |
| 双重读者（营销学者 + 政策读者） | 效应以决策单位（百分点、美元、卡路里）报告；图表要让机构分析师读得懂 |
| 50 页全含上限、双向匿名、SageTrack 投稿 | 图表精简、两文件拆分、彻底的匿名化清查 |
| "证据而非倡导"规范 | 建议强度与识别强度匹配；权衡与代价必须写明 |

## 快速开始

```text
/plugin marketplace add ./Journal-of-Public-Policy-and-Marketing-Skills
/plugin install jppm-skills
```

手动使用：先打开 [`skills/jppm-workflow/SKILL.md`](skills/jppm-workflow/SKILL.md)。

## 默认工作流

```text
jppm-workflow → jppm-topic-selection → jppm-theory-development → jppm-literature-positioning → jppm-methods → jppm-data-analysis → jppm-contribution-framing → jppm-tables-figures → jppm-writing-style → jppm-submission → jppm-review-process → jppm-rebuttal
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jppm-workflow`](skills/jppm-workflow/SKILL.md) | 按稿件症状与论文类型路由到正确的技能 |
| 2 | [`jppm-topic-selection`](skills/jppm-topic-selection/SKILL.md) | 检验问题是否"政策优先"，并选定投稿去向 |
| 3 | [`jppm-theory-development`](skills/jppm-theory-development/SKILL.md) | 围绕消费者、企业、监管者三方构建"政策杠杆理论" |
| 4 | [`jppm-literature-positioning`](skills/jppm-literature-positioning/SKILL.md) | 对照 JPP&M 学术脉络与监管记录进行定位 |
| 5 | [`jppm-methods`](skills/jppm-methods/SKILL.md) | 设计政策情境真实的实验与有反事实的评估 |
| 6 | [`jppm-data-analysis`](skills/jppm-data-analysis/SKILL.md) | 以决策单位估计 DiD/RDD/实验效应，并做全套诊断 |
| 7 | [`jppm-contribution-framing`](skills/jppm-contribution-framing/SKILL.md) | 撰写 Policy Contribution Statement 与监管者可落地的含义 |
| 8 | [`jppm-tables-figures`](skills/jppm-tables-figures/SKILL.md) | 在 50 页上限内制作双重读者都能用的图表 |
| 9 | [`jppm-writing-style`](skills/jppm-writing-style/SKILL.md) | 以政策问题开篇的行文、200 词摘要、证据而非倡导的语气 |
| 10 | [`jppm-submission`](skills/jppm-submission/SKILL.md) | SageTrack 投稿预检：文件、匿名化、声明、页数 |
| 11 | [`jppm-review-process`](skills/jppm-review-process/SKILL.md) | 解读桌面初筛、混合审稿人构成与决定信 |
| 12 | [`jppm-rebuttal`](skills/jppm-rebuttal/SKILL.md) | 把 R&R 要求转化为实际工作并撰写回复信 |

## 资源

- [`resources/README.md`](resources/README.md) — 资源索引
- [`resources/official-source-map.md`](resources/official-source-map.md) — 官方 URL 与易变信息（核验于 2026-07-16）
- [`resources/external_tools.md`](resources/external_tools.md) — 监管记录、评估数据与软件工具
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — 营销与政策经典文献及引用护栏
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — 带批注的 JPP&M 风格引言示例
- [`resources/code/`](resources/code/) — 内置实证代码工具箱（DiD/IV/RDD 流水线）

## 与同门技能包的差异

| 对比 | 关键差异 |
|------|----------|
| JCP / JCR 包 | 标题主张是政策决定，而非心理机制 |
| JM / JMR 包 | 利益相关者是监管者与消费者福祉，而非企业绩效 |
| Marketing Science 包 | 证据服务于规则制定，而非建模贡献 |
| 经济学期刊包 | 交换关系中的营销侧（说服、企业反应、消费者推断）是分析核心 |

## 相关链接

- https://www.ama.org/journal-of-public-policy-and-marketing/
- https://journals.sagepub.com/home/ppo
- https://www.ama.org/submission-guidelines-american-marketing-association-journals/
- https://mc.manuscriptcentral.com/ama_jppm

## 许可

MIT (c) 2026 Bryce Wang。见 [LICENSE](LICENSE)。
