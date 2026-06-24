# 《经济学（季刊）》 — 资源库

《经济学（季刊）》 技能包的能力层。可运行代码已就地引入以保证自包含；现代因果识别的横切方法规范
统一沉淀在共享的 empirical-methods 中枢，下方相对链接引用。

## 内容

| 资源 | 作用 |
|---|---|
| [`code/`](code/) | 可复现的 Stata + Python 因果识别脚本骨架（清洗 → 描述 → DID/IV/RDD/DML → 机制 → 稳健性 → 出表）。源自《经济研究》已实跑验证的代码库（Stata 18 MP，2026-06），复制即用，勿盲改命令。 |
| [审稿人异议清单](../../shared-resources/empirical-methods/reviewer-objection-checklist.md) | 顶刊审稿人按识别策略（DID/IV/RDD/DML/匹配/机制）真实提出的攻击点及预防答法。起表前自检设计。 |
| [报告规范](../../shared-resources/empirical-methods/reporting-standards.md) | 现代推断与报告的底线：聚类标准误、弱工具诊断、多重检验校正、DID/RDD 报告、可复现。 |
| [execution-with-mcp](../../shared-resources/empirical-methods/execution-with-mcp.md) | **从指导到“已拟合、已审计”的结果。** 把各设计族 / 审稿异议映射到本环境可调用的 StatsPAI / Stata MCP 工具，使本包实证 skill 真正*跑出*现代 DID / 弱工具稳健 CI / 多重检验校正并报告数字（解析/结构/定性工作在该工具链外）。 |
| [`official-source-map.md`](official-source-map.md) | 该刊的官方事实（费用、字数、盲审、数据政策、参考文献体例），区分 [官]/[经验值]。 |
| [`worked-examples/`](worked-examples/01-introduction.md) | 该刊房风格的引言 before→after 改写示例（示意性、虚构）。 |
| [`exemplars/library.md`](exemplars/library.md) | 该刊真实、经联网核实的代表作（按方法×主题），附姊妹刊辨析。 |

## 用法

1. **起表前**——用审稿人异议清单逐条压测设计；任何一条无法用一段话 + 一张表/图回应，即是漏洞。
2. **做结果时**——把 `code/` 套到你的数据上，保留现代估计量链（异质性稳健 DID、弱工具稳健 IV、偏差校正 RDD）。
3. **投稿前**——按报告规范走一遍推断自检，并对照本包 `official-source-map.md` 的该刊具体要求。

> 此处方法规范为期刊中性；该刊具体要求以本包各 skill 与 `official-source-map.md` 为准。
