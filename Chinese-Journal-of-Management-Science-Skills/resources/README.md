# 《中国管理科学》资源层（Resources）

**Chinese Journal of Management Science** 技能包的能力层。可运行代码为自包含而随包
提供；跨刊通用的实证方法指引集中在仓库共享方法库，下表给出链接。本刊三条主线
（优化建模 / 数据驱动预测 / 金融工程实证）中，共享库主要服务**实证/因果支线**；
优化与算法侧的把关逻辑内置在各 cjms-* 技能中。

## 内容一览

| 资源 | 给智能体的能力 |
|------|----------------|
| [`code/`](code/) | 可复现的 Stata + Python 因果推断骨架（清洗→描述→DiD/IV/RDD/DML→机制→稳健性→出表）。自已验证的 Economic-Research-Journal-Skills 代码库引入（Stata 18 MP，2026-06 实跑）。服务本包金融工程实证与政策冲击支线；复制后按需改造，勿盲目照跑。 |
| [审稿人异议清单](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | 按识别策略分类的审稿异议与预防动作——实证支线适用。 |
| [报告规范](../../shared-resources/empirical-methods/reporting-standards.md) | 现代推断与报告的底线（聚类、多重检验、DiD/RDD 报告、可复现性）。 |
| [`official-source-map.md`](official-source-map.md) | 本包全部已核实事实的官方来源 URL（核验 2026-07-16）与「待核实」清单——费用、主编、匿名模式等易变项的诚实登记。 |
| [`external_tools.md`](external_tools.md) | 三条主线的工具箱：求解器与标准测试集、分解-预测-集成软件栈、金融数据库、顺序编码制文献工具。 |
| [`worked-examples/`](worked-examples/) | 改写前 → 改写后的本刊式引言示范（虚构班轮联盟舱位互换论文），演示"情境冲突→双线缺口→可命名增量→带量级预告"的弧线。 |
| [`exemplars/library.md`](exemplars/library.md) | 经官网 URL 核实的代表作清单（主题×形态），含姊妹刊辨析与"待复核"纪律——只作定位参照，不复制其数字。 |

## 用法

1. **定题前** —— 用 `exemplars/library.md` 与 `cjms-topic-selection` 的三问先判对口；
   定理厚的稿子该去《管理科学学报》，案例/问卷稿该去《管理世界》系。
2. **建模求解时** —— 走 `cjms-model-formulation` → `cjms-solution-algorithm`；实证/预测
   支线改造 `code/` 骨架并过共享库的审稿异议清单。
3. **投稿前** —— 所有易变事实（费用、周期、模板、匿名）对照 `official-source-map.md`
   的待核实清单，以 www.zgglkx.com 当日页面为准。

> 共享方法库是跨刊通用底线；凡与本包技能或 `official-source-map.md` 的**本刊特定**
> 要求冲突处，以后者为准。
