# Journal of the European Economic Association Skills

<p align="center"><img src="assets/cover.svg" width="200" alt="Journal of the European Economic Association Skills 封面"></p>

[English](README.md) | 简体中文

面向 **Journal of the European Economic Association（JEEA，欧洲经济学会会刊）** 投稿的 12 个 agent skills。
JEEA 是**欧洲经济学会（EEA）旗下的综合性期刊**，由**牛津大学出版社（OUP）**出版，发表覆盖经济学**所有
领域**的高质量研究——微观与宏观理论、应用计量、应用微观、金融、发展、公共——以强**理论 + 实证**的综合性
标准衡量，面向全球经济学读者。本技能包将稿件从期刊定位与犀利的问题出发，经可信识别（实证
**或**理论/结构）、理论模型打磨、稳健性、图表与写作，进入其 **DCAS 数据与代码政策**——即由 **JEEA 数据编辑
在正式接收前核验**、并发布于 JEEA Zenodo 社区的复现包——再到单盲投稿与 R&R 回复。

**官方依据核验日期：2026-06-20**：EEA 投稿、费用与数据编辑页；Oxford Academic 的 About、Author
Guidelines 与 Editorial Board 页；DCAS 背书；以及 JEEA Zenodo 社区。来源见
[`resources/official-source-map.md`](resources/official-source-map.md)。

## 为什么需要单独的技能栈？

| JEEA 约束 | 对稿件的要求 |
|-----------|--------------|
| 综合性、领域中立 | 结论须越出子领域；仅有子领域深度不符合定位 |
| 高标准的理论**与**实证 | 可信的实证设计**或**自洽的模型——执行水平决定能否被接收 |
| EEA 会员门槛 | 投稿作者须为 EEA 会员，方可投稿*及*再投修改稿 |
| 投稿费（€100，2026-02 起） | 通过 EEA 会员资料页支付；若投稿作者及全部合作者均位于中低收入国家则豁免 |
| 单盲评审、由 co-editor 主导 | 审稿人知晓作者；co-editor 以综合性契合度做 desk-reject |
| DCAS 数据与代码政策 | JEEA 数据编辑在**正式接收前**核验复现；复现包发布于 JEEA Zenodo 社区 |
| 排版规范 | 报告标准误 / 置信集；附线上附录；最终图件需 alt text |

## 快速开始

**作为 Claude Code 插件** —— 将 marketplace 指向本目录并启用插件：

```
/plugin marketplace add ./Journal-of-the-European-Economic-Association-Skills
/plugin install jeea-skills
```

**手动使用** —— 每个 skill 都是 `skills/` 下自洽的 `SKILL.md`。先打开 `skills/jeea-workflow/SKILL.md`，
它会把你路由到当前阶段对应的 skill。

## 默认工作流

```
jeea-topic-selection → jeea-literature-positioning → jeea-identification → jeea-theory-model
   → jeea-robustness → jeea-tables-figures → jeea-writing-style → jeea-replication-package
   → jeea-referee-strategy → jeea-submission → jeea-rebuttal
                         （jeea-workflow 在以上各项之间路由）
```

## 技能列表

| # | Skill | 作用 |
|---|-------|------|
| 1 | [`jeea-workflow`](skills/jeea-workflow/SKILL.md) | 路由器——诊断当前瓶颈并路由到合适的 skill |
| 2 | [`jeea-topic-selection`](skills/jeea-topic-selection/SKILL.md) | 判断投 JEEA 还是 The Economic Journal / EER / field journal / top-5；检验综合性契合度 |
| 3 | [`jeea-literature-positioning`](skills/jeea-literature-positioning/SKILL.md) | 面向综合性读者、相对前沿锚定边际贡献 |
| 4 | [`jeea-identification`](skills/jeea-identification/SKILL.md) | 压力测试识别——实证设计**或**理论/结构 |
| 5 | [`jeea-theory-model`](skills/jeea-theory-model/SKILL.md) | 规整模型；让假设、一般性与结论清晰可读 |
| 6 | [`jeea-robustness`](skills/jeea-robustness/SKILL.md) | 证明主结果对设定、样本、推断、假设稳健 |
| 7 | [`jeea-tables-figures`](skills/jeea-tables-figures/SKILL.md) | 以一张图表让主结果一目了然；不用显著性星号 |
| 8 | [`jeea-writing-style`](skills/jeea-writing-style/SKILL.md) | 让问题与带不确定性的结果在首段落地 |
| 9 | [`jeea-replication-package`](skills/jeea-replication-package/SKILL.md) | 为 JEEA 数据编辑核验构建 DCAS 复现包 |
| 10 | [`jeea-referee-strategy`](skills/jeea-referee-strategy/SKILL.md) | 预先化解稿件会招致的意见；越过 desk rejection |
| 11 | [`jeea-submission`](skills/jeea-submission/SKILL.md) | 投稿前终检：会员、费用、格式、数据政策、声明 |
| 12 | [`jeea-rebuttal`](skills/jeea-rebuttal/SKILL.md) | 撰写回复审稿人信与修改计划 |

## 资源

- [`resources/README.md`](resources/README.md) —— 能力层索引
- [`resources/official-source-map.md`](resources/official-source-map.md) —— 每条事实背后的官方 EEA / OUP 链接
- [`resources/external_tools.md`](resources/external_tools.md) —— 数据源、软件与工具包
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) —— JEEA 引言改写前后对照（虚构示例）
- [`resources/exemplars/library.md`](resources/exemplars/library.md) —— 经网络核实的真实 JEEA 论文，按方法 × 主题组织
- [`resources/code/`](resources/code/) —— 可复现的 Stata + Python 因果推断脚手架

## 与同门期刊的差异

| 期刊 | 定位 | 本技能包的取向 |
|------|------|----------------|
| **JEEA** | EEA 综合性理论 + 实证 | 本包的目标 |
| **The Economic Journal（RES）** | 广泛的欧洲综合性刊物 | JEEA 承载 EEA 学会期刊身份，理论+实证门槛较高 |
| **European Economic Review（EER）** | 广泛覆盖的欧洲期刊 | JEEA 对综合性新意的门槛更高 |
| **Top-5（AER / QJE / JPE / Ecma / REStud）** | 议程设定的综合性顶刊 | JEEA 是低于该门槛的强欧洲综合性归宿 |

## 相关链接

- 欧洲经济学会：https://eeassoc.org/
- JEEA（Oxford Academic）：https://academic.oup.com/jeea
- DCAS（数据与代码可得性标准）：https://datacodestandard.org/

## 许可

MIT © 2026 Bryce Wang。见 [LICENSE](LICENSE)。
