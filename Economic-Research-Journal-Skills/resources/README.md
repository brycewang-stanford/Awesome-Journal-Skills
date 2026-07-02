# resources/ 目录索引

本目录是 Economic-Research（《经济研究》）技能包的共享资产层，供 18 个 `er-*` skill 交叉引用。

| 资产 | 内容 | 主要服务的 skill |
|---|---|---|
| [`official-source-map.md`](official-source-map.md) | 该刊官方事实核查表：VERIFIED 事实（著者-出版年体例、五要素英文梗概、署名限制等）与"需复核 / Live-check"清单的分栏管理，附范文归属避坑表 | 全部（事实口径的唯一来源） |
| [`code/`](code/) | 可一键运行的 Stata（`00`–`09` 分步 `.do`）+ Python 实证骨架：清洗 → 描述统计 → 现代 DID → IV → RDD → DML → 机制 → 稳健性 → 制表 | `er-identification` `er-robustness` `er-mechanism` `er-tables-figures` `er-reproducibility` |
| [`code-templates.md`](code-templates.md) | 命令出处与引文速查（与 `code/` 互补：脚本给流程，本文件给每条命令的来源与"审稿一句话检查"） | `er-identification` `er-robustness` |
| [`worked-examples/`](worked-examples/) | "金税三期与企业 TFP"单案例贯穿 12 个章节段落的整套范文（数字自洽、系数为示意值） | 各写作类 skill 的"配套与范例"小节 |
| [`exemplars/`](exemplars/) | 已核实确属《经济研究》的范文清单（王永钦·董雯 2020 IV；张勋等 2019 机制；刘生龙等 2016 RDD 等） | `er-topic-selection` `er-literature-review` 等 |
| [`external_tools.md`](external_tools.md) | 外部工具与检索入口备忘 | `er-submission` `er-reproducibility` |

## 使用口径

1. 涉及期刊硬性规定（字数、图表、费用、周期）时，一律以 `official-source-map.md` 的 VERIFIED / 需复核分栏为准，不得在 skill 正文另行断言。
2. 范文引用仅限 `exemplars/` 已核实清单，防止把《管理世界》《中国工业经济》名篇误标为《经济研究》。
3. `worked-examples/` 中的系数均为示意，不得当作真实文献数字引用。
