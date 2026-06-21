# Journal of Corporate Finance Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Corporate Finance cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JCF-0b3d6b)](https://www.sciencedirect.com/journal/journal-of-corporate-finance)
[![Publisher](https://img.shields.io/badge/publisher-Elsevier-eb6500)](https://www.sciencedirect.com/journal/journal-of-corporate-finance)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Corporate Finance (JCF)** — an **Elsevier** journal publishing **empirical and theoretical corporate finance**: financial structure, governance, payout, financial contracting, risk management, innovation, M&A, and international corporate finance, including work at the intersection of corporate finance and macroeconomics, asset pricing, household/behavioral finance, fintech/blockchain, law, financial intermediation, and market microstructure.

This repository is opinionated. It is **not** a generic finance-writing toolbox. It is a **JCF-specific** stack: a credible corporate-finance question, a defensible identification strategy on firm-level data, careful robustness, self-contained exhibits, an Elsevier Option C data-availability statement, and a process tuned to JCF's up-front fee and active desk-rejection screen.

---

## Why a Separate JCF Skill Stack?

JCF imposes constraints that differ materially from a top-5 general-interest journal or a methods journal:

| Constraint              | JCF                                                                       | Implication                                                       |
|-------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                   | Empirical **and** theoretical **corporate finance**                       | A pure asset-pricing or accounting paper is off-fit              |
| Format                  | Full-length **or** "shorter format" papers; **no fixed length** (待核实)  | A clean single result can go as a shorter paper                  |
| Submission system       | **Editorial Manager** via ScienceDirect                                   | Not Editorial Express or ScholarOne                              |
| Fee                     | **US$340 non-refundable**, paid up front; no refund on desk reject        | Budget it; clearing the desk screen matters                      |
| Review model            | **Single anonymized (single-blind)**; min. two reviewers                  | Do **not** anonymize the manuscript                             |
| Desk policy             | **Active desk rejection** without full review                             | Contribution + identification must be legible on page one        |
| Abstract                | **≤ 250 words**, no references; 1–7 keywords                              | A long or citation-heavy abstract reads as off-template          |
| References              | **Author-date**; "your paper, your way" at first submission               | Any consistent style with full elements + DOIs; styled at revision |
| Data policy             | **Elsevier Option C** (data-availability statement)                       | No JFE-Data-Archive-style mandatory archive (待核实)             |
| Perks                   | Free integrated **SSRN** preprint posting at submission                   | Optional immediate public preprint with DOI                      |

Generic "scientific writing" or "econ writing" packs do not address these constraints. Volatile specifics (current editors, exact fee, abstract cap, data policy) change — **verify them on the official Guide for Authors**.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jcf-skills
/plugin install jcf-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jcf-skills.git
cd jcf-skills

mkdir -p ~/.claude/skills && cp -R skills/jcf-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jcf-* ~/.codex/skills/
```

---

## The 12 Skills

| Skill | Role |
|-------|------|
| `jcf-workflow` | Orchestrates the full JCF lifecycle and routes to the others |
| `jcf-topic-selection` | Scope fit; full-length vs. shorter format |
| `jcf-literature-positioning` | Locating the corporate-finance strand and marginal contribution |
| `jcf-identification-strategy` | Causal design for endogenous firm decisions (DID/IV/RDD/event study/matching) |
| `jcf-data-analysis` | WRDS-era panels, fixed effects, clustering, robustness |
| `jcf-tables-figures` | Self-contained tables and event-study/CAR figures |
| `jcf-contribution-framing` | A crisp "what's new and why it matters" that clears the desk screen |
| `jcf-writing-style` | ≤250-word abstract, keywords, author-date references |
| `jcf-replication-and-data-policy` | Elsevier Option C data-availability statement and archive |
| `jcf-review-process` | Single-anonymized model, two+ reviewers, declarations |
| `jcf-submission` | Editorial Manager preflight, US$340 fee, declarations |
| `jcf-rebuttal` | Point-by-point R&R response across divergent reviewers |

---

## Key JCF Facts (verified 2026-06-01; re-confirm on the official guide)

- **Publisher**: Elsevier. **Submission**: Editorial Manager, via the ScienceDirect "Submit your article" link.
- **Fee**: US$340.00 non-refundable submission fee, paid during submission; not refunded on desk rejection.
- **Review**: single anonymized (single-blind); minimum two reviewers; active desk-rejection policy.
- **Abstract**: ≤ 250 words; 1–7 keywords; no references in the abstract.
- **References**: author-date (Harvard); "your paper, your way" (consistent style) at first submission, full Elsevier styling at revision.
- **Data**: Elsevier "Research Data" Option C — state availability; deposit/cite code and data or explain why not.
- **Co-Editors-in-Chief**: Kristine Hankins (University of Kentucky) and Heitor Almeida (University of Illinois at Urbana-Champaign); Co-Editors include Morten Bennedsen, Simi Kedia, Evgeny Lyandres, Xuan Tian, and Tracy Wang (re-verify the live roster — see source map).
- **Perk**: free integrated SSRN preprint posting at submission.

Items that could not be fully verified (e.g., a hard length limit, a separate revision fee, the current APC) are marked **待核实** in [`resources/official-source-map.md`](resources/official-source-map.md) and are not treated as load-bearing.

---

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every used fact, its official URL, and an accessed date (2026-06-01); unverified items marked 待核实.
- [`resources/external_tools.md`](resources/external_tools.md) — data sources (Compustat/CRSP/SDC/DealScan), Stata/R/Python packages, and the design toolkit for empirical corporate finance.

---

## Disclaimer

This is an unofficial, community skill pack. It is not affiliated with or endorsed by Elsevier or the Journal of Corporate Finance. Always confirm current requirements on the official Guide for Authors before submitting.

## License

MIT — see [LICENSE](LICENSE).
