# Journal of Public Economics Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Public Economics cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JPubE-11486b)](https://www.sciencedirect.com/journal/journal-of-public-economics)
[![Field](https://img.shields.io/badge/field-Public%20Economics-1f6feb)](https://www.sciencedirect.com/journal/journal-of-public-economics)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Public Economics (JPubE)** — Elsevier's flagship field journal in **public economics / public finance**, founded in **1972 by Tony Atkinson** and edited by **Nathaniel Hendren (MIT)** and **Wojciech Kopczuk (Columbia University)**.

This repository is opinionated. It is **not** a generic economics-writing toolbox. It is a **JPubE-specific** stack for the economic role of government — taxation, public expenditure, social insurance, redistribution, externalities, public goods, and fiscal policy — answered with modern theory and quantitative methods, a credible policy-induced identification strategy (bunching, RKD, reform DID, IV, RDD), administrative/register data, sufficient-statistics or MVPF welfare mappings, figure-forward exhibits, and a reproducible package — for an international readership.

---

## Why a Separate JPubE Skill Stack?

JPubE imposes constraints that differ materially from a free generalist top-5 or a methods journal:

| Constraint | JPubE | Implication |
|------------|-------|-------------|
| Scope | The economic role of government (tax / transfer / insurance / public goods) | A labor/IO paper with a tax control may be off-fit |
| Premium on | A policy-relevant parameter + a welfare interpretation | A bare coefficient with no welfare payoff reads as thin |
| Identification bar | Bunching / RKD / RDD / reform DID / policy IV, design visible | OLS + controls is desk-vulnerable |
| Review model | **Single anonymized** (reviewers hidden; **authors known**), ≥ 2 reviewers | Do not strip your name expecting blind review |
| Submission fee | **US$165** (US$82.50 student; waived on Elsevier transfer) | Budget for it — unlike free generalist journals |
| Abstract | **250 words** maximum | A 300-word abstract is off-template |
| Short paper track | **≤ 6,000 words**, up to **five exhibits** | A focused result can use the expedited track |
| References | Author-date (name-and-year) | Numbered/footnote styles read as off-template |
| Source files | Editable Word (single-column) or LaTeX `.tex` (double-column LaTeX-only) | A PDF-only submission is non-compliant |
| Research data | Elsevier **Option C**: deposit/cite/link data or explain why data cannot be shared | Restricted public data need a precise access statement |
| Preprint | Optional **SSRN** posting at submission, no effect on outcome | A free dissemination option, not a strategic lever |
| Process | **Editorial Manager**; AI disclosure; **one appeal** per submission | Use the appeal only for a clear error |

Generic "scientific writing" or "econ writing" packs do not address these. The pack maps its venue facts to the official ScienceDirect / Elsevier pages in [`resources/official-source-map.md`](resources/official-source-map.md); live-check those pages before an actual upload because fees, required fields, and data-policy wording can change.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jpube-skills
/plugin install jpube-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jpube-skills.git
cd jpube-skills

mkdir -p ~/.claude/skills && cp -R skills/jpube-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jpube-* ~/.codex/skills/
```

### First Prompt

```
Use jpube-workflow to tell me which skill I should use next for my JPubE manuscript.
```

---

## Default Workflow

```text
jpube-topic-selection
        ▼
jpube-contribution-framing
        ▼
jpube-literature-positioning
        ▼
jpube-identification-strategy
        ▼
jpube-data-analysis
        ▼
jpube-tables-figures
        ▼
jpube-writing-style          (polish)
        ▼
jpube-replication-and-data-policy
        ▼
jpube-review-process
        ▼
jpube-submission
        ▼
jpube-rebuttal
```

`jpube-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill | Purpose |
|-------|---------|
| `jpube-workflow` | Router — decides which sub-skill to invoke next |
| `jpube-topic-selection` | Government-role fit + the policy-stakes bar |
| `jpube-contribution-framing` | Frame the contribution as a policy parameter / welfare verdict |
| `jpube-literature-positioning` | Stake the contribution on the public-finance frontier |
| `jpube-identification-strategy` | Credible policy-induced design (bunching / RKD / RDD / reform DID / IV) |
| `jpube-data-analysis` | Administrative/register data, elasticities, MVPF / sufficient stats |
| `jpube-tables-figures` | Figure-forward design exhibits, self-contained notes |
| `jpube-writing-style` | 250-word abstract, author-date, welfare translation |
| `jpube-replication-and-data-policy` | Elsevier research-data framework + reproducible package |
| `jpube-review-process` | Single-anonymized review, Editorial Manager, SSRN, appeals |
| `jpube-submission` | Editorial Manager preflight + US$165 fee |
| `jpube-rebuttal` | Revision response-letter and one-appeal strategy |

### Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — official JPubE/Elsevier URLs behind the pack's venue-specific facts
- [`resources/external_tools.md`](resources/external_tools.md) — data sources (IRS/SOI, LEHD, SSA, CMS, registers, TAXSIM) + Stata/R/Python packages for bunching, RKD, DID, IV

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or referee's taste
- It does not replace a live final check of operational metadata (fee, upload fields, APC options, current masthead, policy wording)
- It does not treat restricted administrative data as shareable; it routes those papers to a precise access statement plus code package

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [Journal of Public Economics (official)](https://www.sciencedirect.com/journal/journal-of-public-economics) — Elsevier / ScienceDirect

---

## License

MIT
