# 《系统工程学报》资源层

本目录为 `jse-tju-*` skills 提供可追溯事实、近年论文画像、写作示例与执行接口。
期刊动态要求不在 12 个 skill 中重复硬编码；先读
[`official-source-map.md`](official-source-map.md)，再引用已核实条目。

| 资源 | 作用 |
|---|---|
| [`official-source-map.md`](official-source-map.md) | 官网事实、访问日期、稳定性与待核实台账 |
| [`source-basis.md`](source-basis.md) | 30 篇近年样本的抽样方法和内容画像 |
| [`exemplars/library.md`](exemplars/library.md) | 六期、30 篇公开元数据的主题 × 方法 × 验证矩阵 |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | 按编辑部“背景—问题—内容—主要结论”规范改写引言 |
| [`external_tools.md`](external_tools.md) | 优化、网络、仿真、预测与实证支线的工具选择 |
| [`code/README.md`](code/README.md) | 最小复现接口；说明为何不复制不适配的大型代码模板 |

## 执行桥

本刊样本同时包含优化算法、复杂网络仿真、金融预测和空间计量，不能把单一因果推断
代码套在所有稿件上。涉及实证推断时，读取仓库共享的
[execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md)、
[reporting standards](../../shared-resources/empirical-methods/reporting-standards.md) 与
[reviewer objection checklist](../../shared-resources/empirical-methods/reviewer-objection-checklist.md)；
优化与仿真稿则按本包的 `algorithm-computation`、`validation` 和
`robustness-reproducibility` skills 建立问题专属实验。

> 共享资源只提供跨刊底线。与《系统工程学报》官网现行要求冲突时，以
> `official-source-map.md` 中核验日期最新的一手来源为准。
