# AEJ: Applied Economics Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="AEJ: Applied Economics Skills 封面"></p>

[English](README.md) | 简体中文

面向 **American Economic Journal: Applied Economics（AEJ: Applied）** 投稿的 12 个 agent skills。AEJ:
Applied 是美国经济学会（AEA）旗下的季刊，聚焦**具有可信因果识别的实证应用微观经济学**（劳动、发展、健康、
教育、公共、城市、环境、家庭金融）。本技能包以识别为驱动、实证优先：从期刊定位与干净的研究设计出发，经稳健性、
图表、AEA 风格写作，进入其标志性的 **AEA 数据与代码可得性政策**——即由 AEA 数据编辑在**发表前**核验可复现性的
openICPSR 复现包——再到单盲投稿与 R&R 回复。

**官方依据核验日期：2026-06-20**：AEA / AEJ: Applied 期刊页、编辑名单、编辑政策、审稿人指南、投稿页、体例页、披露政策与
AEA 数据与代码可得性政策。来源与投稿周 live-check 边界见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| AEJ: Applied 约束 | 对稿件的要求 |
|-------------------|--------------|
| 实证优先的应用微观 | 可信的因果设计即贡献；理论只用于解释/结构化，不主导 |
| 单盲评审 | 作者身份对审稿人可见；审稿人身份对作者匿名 |
| AEA 在线投稿 + JEL 代码 | 必须填写 JEL 代码；首页含标题、作者与机构；会员/非会员投稿费 |
| AEA 数据与代码可得性政策 | 数据 + 代码须存入 openICPSR 上的 AEA Data and Code Repository |
| 发表前可复现性核验（AEA 数据编辑 Lars Vilhuber） | 表与图须能从存放的复现包在发表前重新生成 |
| AEA 排版规范 | 摘要不超过 100 词；允许显著性星号，但要求报告标准误；图表注释须自洽；附线上附录 |

## 快速开始

**作为 Claude Code 插件** —— 将 marketplace 指向本目录并启用插件：

```
/plugin marketplace add ./AEJ-Applied-Economics-Skills
/plugin install aej-applied-economics-skills
```

**手动使用** —— 每个 skill 都是 `skills/` 下自洽的 `SKILL.md`。先打开 `skills/aeja-workflow/SKILL.md`，
它会把你路由到当前阶段对应的 skill。

## 默认工作流

```
aeja-topic-selection → aeja-literature-positioning → aeja-identification → aeja-theory-model
   → aeja-robustness → aeja-tables-figures → aeja-writing-style → aeja-replication-package
   → aeja-referee-strategy → aeja-submission → aeja-rebuttal
                         （aeja-workflow 在以上各项之间路由）
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`aeja-workflow`](skills/aeja-workflow/SKILL.md) | 路由器——诊断当前瓶颈并路由到合适的 skill |
| 2 | [`aeja-topic-selection`](skills/aeja-topic-selection/SKILL.md) | 判断投 AEJ: Applied 还是 AER / AEJ: Policy / field journal；打磨问题 |
| 3 | [`aeja-literature-positioning`](skills/aeja-literature-positioning/SKILL.md) | 相对最接近的既有工作锚定边际贡献 |
| 4 | [`aeja-identification`](skills/aeja-identification/SKILL.md) | 压力测试因果设计（RCT / DID / RD / IV / shift-share） |
| 5 | [`aeja-theory-model`](skills/aeja-theory-model/SKILL.md) | 把理论用量调到「解释/结构化」估计，而非主导 |
| 6 | [`aeja-robustness`](skills/aeja-robustness/SKILL.md) | 证明主结果对设定、样本、推断稳健 |
| 7 | [`aeja-tables-figures`](skills/aeja-tables-figures/SKILL.md) | 以 AEA 风格让主结果在一张图表中一目了然 |
| 8 | [`aeja-writing-style`](skills/aeja-writing-style/SKILL.md) | 让问题与估计在首段落地 |
| 9 | [`aeja-replication-package`](skills/aeja-replication-package/SKILL.md) | 为 AEA 数据编辑核验构建 openICPSR 复现包 |
| 10 | [`aeja-referee-strategy`](skills/aeja-referee-strategy/SKILL.md) | 预先化解该设计会招致的审稿意见 |
| 11 | [`aeja-submission`](skills/aeja-submission/SKILL.md) | 投稿前终检：首页信息、JEL、费用、格式、声明 |
| 12 | [`aeja-rebuttal`](skills/aeja-rebuttal/SKILL.md) | 撰写回复审稿人信与修改计划 |

## 资源

- [`resources/README.md`](resources/README.md) —— 能力层索引
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的官方 AEA 链接
- [`resources/external_tools.md`](resources/external_tools.md) —— 数据源、软件与工具包
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— AEJ: Applied 引言改写前后对照（虚构示例）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 经网络核实的真实 AEJ: Applied 论文，按方法 × 主题组织
- [`resources/code/`](resources/code/) —— 可复现的 Stata + Python 因果推断脚手架

## 与同门期刊的差异

| 期刊 | 定位 | 本技能包的取向 |
|------|------|----------------|
| **AEJ: Applied** | 识别驱动、具广泛兴趣的应用微观 | 本包的目标 |
| **American Economic Review（AER）** | 综合性、议程设定、篇幅更长 | AEJ: Applied 承接更专门的应用微观工作 |
| **AEJ: Economic Policy** | 政策问题框架、项目评估结论 | AEJ: Applied 以方法/识别驱动，而非政策性投资回报 |
| **领域期刊（JHE / JOLE / JDE）** | 子领域内部贡献 | AEJ: Applied 追求更广的应用微观读者 |

## 相关链接

- 美国经济学会期刊：https://www.aeaweb.org/journals
- AEA 数据与代码可得性政策：https://www.aeaweb.org/journals/policies/data-code

## 许可

MIT © 2026 Bryce Wang。见 [LICENSE](LICENSE)。
