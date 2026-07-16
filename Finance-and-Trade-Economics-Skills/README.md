# Finance-and-Trade-Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="《财贸经济》 journal cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-Finance%20%26%20Trade%20Economics-6b3f2a)](http://naes.org.cn/)
[![Index](https://img.shields.io/badge/index-CSSCI-1f6feb)](http://naes.org.cn/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《财贸经济》 (Finance & Trade Economics)** — a top CSSCI economics journal (monthly, founded 1980) hosted by the **National Academy of Economic Strategy (NAES), Chinese Academy of Social Sciences**. The journal covers public finance, taxation, monetary and financial economics, trade, circulation, and consumption, and favors empirical work that is tightly bound to major Chinese economic-policy realities and built on rigorous causal identification.

This repository is opinionated. It is **not** a generic Chinese-economics writing toolbox. It is a **Finance-and-Trade-Economics-specific** stack covering fiscal / tax / financial / trade topic selection, bilingual literature review, policy-shock quasi-experimental identification (DID / IV / RDD / DML), identifiable-channel mechanism and heterogeneity analysis, three-line-table house style, China-policy-anchored implications, and R&R rebuttals.

---

## Why a Separate Finance-and-Trade-Economics Skill Stack?

《财贸经济》 imposes constraints that differ materially from general economics journals:

| Constraint | Finance & Trade Economics | Implication |
|---|---|---|
| Discipline | Public finance / tax / money & finance / trade / consumption | Off-scene "generic" empirics are off-fit |
| Topic | Theory + a concrete Chinese fiscal/financial/trade policy reality | Must say "which finance problem, why now" |
| Institutional grounding | Anchored in China's fiscal/financial/trade institutions | Placeless, transplantable stories are desk-rejected |
| Contribution sentences | 3–5 explicit "边际贡献" bullets in the intro | Cannot be a single paragraph |
| Data | Firm / city / bank / household micro data, named to source | "public channels" wording reads as opaque data |
| Identification | Quasi-experimental; policy endogeneity handled | OLS / descriptive stats often desk-rejected |
| Mechanism | Near-mandatory, on an identifiable channel | A "policy black box" rarely gets accepted |
| Heterogeneity | Strongly preferred, on China-finance dimensions | "East / Central / West" only reads as lazy |
| Policy implications | Significance-level but anchored in concrete levers | The "加强完善推进" formula is punished |
| Length | ~15–25k Chinese characters incl. exhibits (verify on site) | Full structure expected |

Generic "scientific writing" or "economics writing" skill packs do not address these constraints.

> Accuracy note: exact word limits, reference caps, figure counts, the submission URL, and review specifics change year to year. This pack describes the durable norms — verify the current numbers on the journal's official 投稿须知 page.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/cte-skills
/plugin install cte-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/cte-skills.git
cd cte-skills

mkdir -p ~/.claude/skills && cp -R skills/cte-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cte-* ~/.codex/skills/
```

### First Prompt

```
Use cte-workflow to tell me which skill I should use next for my Finance-and-Trade-Economics manuscript.
```

---

## Default Workflow

```text
cte-topic-selection
        ▼
cte-literature-review
        ▼
cte-identification
        ▼
cte-mechanism
        ▼
cte-heterogeneity
        ▼
cte-tables-figures
        ▼
cte-policy-implication
        ▼
cte-abstract      (polish)
        ▼
cte-style         (polish)
        ▼
cte-submission
        ▼
cte-rebuttal
```

`cte-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill | Purpose |
|---|---|
| `cte-workflow` | Router — decides which sub-skill to invoke next |
| `cte-topic-selection` | Fiscal/financial/trade scope fit + theoretical grounding + contribution sentences |
| `cte-literature-review` | Bilingual, dialogic structure + canonical finance-theory checklist |
| `cte-identification` | Policy-shock quasi-experimental design (DID / IV / RDD / DML) + policy endogeneity |
| `cte-mechanism` | Identifiable-channel mechanism paths (opening the "policy black box") |
| `cte-heterogeneity` | China-finance-relevant heterogeneity cuts (beyond East/Central/West) |
| `cte-tables-figures` | Three-line tables, variable-definition table, transparent data sourcing, figures |
| `cte-policy-implication` | Significance-level framing anchored in concrete fiscal/financial levers |
| `cte-abstract` | Five-sentence abstract + blacklist-phrase removal |
| `cte-style` | Language polish: empty significance / "加强完善推进" → concrete |
| `cte-submission` | Pre-submission checklist + manuscript template (format, blind review) |
| `cte-rebuttal` | R&R response-letter structure |

### Resources

- [`skills/cte-submission/templates/manuscript_template.md`](skills/cte-submission/templates/manuscript_template.md) — Standard manuscript skeleton (abstract, variable table, references)
- [`skills/cte-submission/templates/checklist.md`](skills/cte-submission/templates/checklist.md) — 8-section pre-submission self-check
- [`resources/external_tools.md`](resources/external_tools.md) — Finance data sources (CNKI / CSMAR / WIND / CEIC / 工业企业 / 海关 / yearbooks) + Stata / R / Python packages
- [`resources/official-source-map.md`](resources/official-source-map.md) — Official facts (sponsor, editor, fees, blind review) with verification dates
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — Paradigm-calibrating classics by method × topic
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — Annotated before→after introduction in house style

---

## Differences vs. Neighboring Journals

| Dimension | Finance & Trade Economics | Neighboring venues |
|---|---|---|
| Pure asset pricing / corporate finance | Less central | 《金融研究》 |
| International trade / open-macro | Accepted but not core | 《世界经济》 |
| Specialized fiscal / tax policy | Accepted | 《财政研究》《税务研究》 |
| More general theory contribution | Off-scope | 《经济研究》《管理世界》 |
| Shared bar | China-policy grounding + credible identification + mechanism | — |

---

## What this repo does NOT do

- It will not write a submission-ready manuscript for you
- It does not simulate reviewer preferences
- It does not catalog 《财贸经济》's historical rejection rate, impact factor, or other metadata
- It does not judge whether your "theoretical contribution" is genuinely original — that is the researcher's own call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [China-Rural-Economy-Skills](https://github.com/brycewang-stanford/china-rural-economy-skills) — 《中国农村经济》

---

## License

MIT
