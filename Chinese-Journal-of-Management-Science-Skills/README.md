# Chinese Journal of Management Science (《中国管理科学》) Skills

<p align="center">
  <img src="assets/cover.svg" alt="Chinese Journal of Management Science cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-%E4%B8%AD%E5%9B%BD%E7%AE%A1%E7%90%86%E7%A7%91%E5%AD%A6-0d5c63)](https://www.zgglkx.com/)
[![Index](https://img.shields.io/badge/index-FMS%20T1%20%7C%20CSSCI-1f6feb)](https://www.zgglkx.com/CN/column/column1.shtml)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at **《中国管理科学》 (Chinese Journal of Management Science)** — the applied quantitative-management flagship founded by mathematician **Hua Luogeng in December 1984** (originally 《优选与管理科学》, renamed in 1993, monthly since 2014), supervised by the **Chinese Academy of Sciences** and co-sponsored by the Society of Optimization, Overall Planning and Economic Mathematics together with the CAS Institutes of Science and Development (ISSN 1003-207X, CN 11-2835/G3).

This repository is opinionated. It is **not** a generic "Chinese management journal" toolbox, and it is emphatically not a theorem-proving stack. CJMS descends from Hua Luogeng's mission of putting quantitative methods to work in the real economy: it publishes **applied modeling with computational and empirical validation** — a real management setting turned into a model, solved, computed, tested against benchmarks, and translated into managerial insight. The stack therefore routes by the journal's three live strands (optimization modeling / data-driven forecasting / financial-engineering empirics), enforces the 12-page limit and the equation-editor discipline the editorial office actually checks, and screens out the classic mismatch: theorem-heavy papers that belong at 《管理科学学报》 and regression-plus-policy narratives that belong at 《管理世界》.

> Durable norms only. Editors, fees, portal behavior and templates change — always verify on the official pages at **www.zgglkx.com** (facts in this pack checked 2026-07-16; see [`resources/official-source-map.md`](resources/official-source-map.md)).

---

## Why a Separate CJMS Skill Stack?

CJMS's constraints differ in kind from both its mathematical sibling and the empirical management journals:

| Constraint | 《中国管理科学》 (CJMS) | Implication |
|------------|--------------------------|-------------|
| Mission | Applied modeling in real management settings (Hua Luogeng tradition) | "Textbook model + Chinese background" fails; the setting must shape the model |
| Deliverable | Model + algorithm/method + calibrated computation or real-data test | Pure regressions and pure theorems are both off-strand |
| Strands | Optimization / forecasting / financial engineering side by side | Advice must branch by strand; validation bars differ |
| Length | Papers capped at ~12 pages (official guide) | Exhibit density is a design constraint, not an afterthought |
| Style | Prescribed section order, 100–200-char abstract, CLC number, equation-editor formulas | Form review rejects before content review begins |
| References | Sequential coding (顺序编码制), directly-read published sources only | Citation order must follow argument order |
| Portal | www.zgglkx.com only; editorial office warns against agent submission | No email or third-party submission |
| Fees/timeline | Conflicting public figures — flagged 待核实 in this pack | Re-check announcements at submission; never rely on cached numbers |
| Community | NSFC Management Science A-list journal; FMS T1; annual 中国管理科学学术年会 | Referees come from the Chinese OR/MS community — cite its recent work |

Generic "scientific writing" packs, and even the sibling 管理科学学报 pack, do not address these constraints.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/cjms-skills
/plugin install cjms-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/cjms-skills.git
cd cjms-skills

mkdir -p ~/.claude/skills && cp -R skills/cjms-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/cjms-* ~/.codex/skills/
```

### First Prompt

```
Use cjms-workflow to tell me which skill I should use next for my 《中国管理科学》 manuscript.
```

---

## Default Workflow

```text
cjms-topic-selection
        ▼
cjms-literature-review
        ▼
cjms-model-formulation
        ▼
cjms-solution-algorithm      (optimization strand)
        ▼
cjms-empirical-validation    (forecasting / finance strand)
        ▼
cjms-numerical-experiments
        ▼
cjms-managerial-insights
        ▼
cjms-tables-figures
        ▼
cjms-writing-style           (polish)
        ▼
cjms-submission
        ▼
cjms-rebuttal
```

`cjms-workflow` is the router — it names the next skill based on where you are, starting from which strand (optimization modeling / data-driven forecasting / financial-engineering empirics) your paper works in.

---

## Skills

| Skill | Purpose |
|-------|---------|
| `cjms-workflow` | Router — decides which sub-skill to invoke next, by strand |
| `cjms-topic-selection` | The three-question fit test, column mapping, sister-journal screening |
| `cjms-literature-review` | Two-lane (Chinese + international) review; nameable methodological increment |
| `cjms-model-formulation` | Setting-to-model mapping; variables/constraints/objective; numbered, defended assumptions |
| `cjms-solution-algorithm` | Solution-route decision table; pseudocode, property analysis, baselines |
| `cjms-empirical-validation` | Data provenance, rolling out-of-sample tests, benchmark batteries, DM/MCS |
| `cjms-numerical-experiments` | Grounded parameter calibration, experiment matrix, sensitivity and boundaries |
| `cjms-managerial-insights` | Condition–decision–effect rules; the slogan blacklist |
| `cjms-tables-figures` | Three-line tables, equation-editor formulas, algorithm boxes, 12-page density |
| `cjms-writing-style` | Prescribed section order, 100–200-char abstract, CLC number, 结语, sequential-coded references |
| `cjms-submission` | zgglkx.com preflight; fee/timeline caveats; checklist + manuscript template |
| `cjms-rebuttal` | Comment classification, revise-then-respond discipline, point-by-point 修改说明 |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — strand-by-strand toolkit (solvers and test libraries; decomposition-forecasting stack; financial databases; sequential-coding reference tools)
- [`resources/official-source-map.md`](resources/official-source-map.md) — official zgglkx.com / CAS URLs behind every verified fact (checked 2026-07-16), with an honest 待核实 ledger for fees, editorship and anonymity mode
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — URL-verified CJMS papers by topic × form, with sister-journal disambiguation
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — before → after CJMS-style introduction (fictional shipping-alliance optimization paper)
- [`resources/code/`](resources/code/) — vendored Stata + Python causal-inference skeleton for the empirical strand

---

## Differences vs. Sibling Chinese Venues

| Dimension | 中国管理科学 (CJMS) | 管理科学学报 (JMSC) | 系统工程理论与实践 | 管理世界 |
|-----------|--------------------|--------------------|--------------------|----------|
| Sponsor | CAS + SCOPE society | NSFC Management Science Dept. + Tianjin Univ. | Systems Engineering Society of China | Development Research Center of the State Council |
| Deliverable | Applied model + computation/empirics | Model + proofs + algorithm | Systems methodology + engineering application | Empirics, cases, policy |
| Yardstick | Does the method work on the real setting? | Mathematical rigor of the method | Systems-engineering contribution | Empirical/policy contribution |
| Fatal misfit | Pure regression, pure theorem | Application without provable properties | Single-firm business problem | Model without economic narrative |

If your paper's payoff is a theorem, go one door over to JMSC; if it is a regression coefficient with policy talk, go to 管理世界; if it is a working method that changes a real decision, CJMS is the target.

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — index of journal-specific skill packs
- [Journal-of-Management-Sciences-in-China-Skills](https://github.com/brycewang-stanford) — the theorem-heavy sibling's pack

---

## License

MIT
