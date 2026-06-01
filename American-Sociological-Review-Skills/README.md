# American Sociological Review Skills

<p align="center">
  <img src="assets/cover.svg" alt="American Sociological Review cover" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-ASR-6b2737)](https://journals.sagepub.com/home/asr)
[![Field](https://img.shields.io/badge/field-Sociology-1f6feb)](https://www.asanet.org/publications/journals/american-sociological-review/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **American Sociological Review (ASR)** — the
**flagship general journal of the American Sociological Association (ASA)**, founded in **1936** and
published by **SAGE**. ASR publishes work from across sociology: stratification and mobility,
demography, comparative-historical sociology, ethnography and interviews, social networks,
political and economic sociology, and computational sociology.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is
**not** a political-science or economics pack relabeled. It is an **ASR-specific** stack: a question
of broad sociological significance, theory that travels, a design defended on its own methodological
terms, a properly **masked** manuscript, and submission through **Sage Track** with the journal's
**$25 processing fee** and the **ASA data-sharing** norm.

---

## What Is ASR, and Why a Dedicated Stack?

ASR's constraints differ from a subfield journal or a methods journal:

| Constraint            | ASR                                                                           | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **All of sociology**                                                          | The paper must matter beyond its subfield                        |
| Premium on            | Broad significance + a theoretical payoff that travels                        | A narrow, descriptive result is off-fit                          |
| Methods               | Quantitative, demographic, comparative-historical, ethnographic, network, computational — judged on own terms | Don't force one template onto every paper |
| Publisher / owner     | **SAGE** / **ASA**                                                            | Submitted via **Sage Track** (ScholarOne), not Editorial Manager |
| Review model          | **Masked (anonymous)** — anon manuscript + separate title page                | You *may* self-cite, just not identifyingly                      |
| Fee                   | **$25 non-refundable** processing fee (waived for ASA student members)        | Budget it unless you're an ASA student                           |
| Length                | **Articles ≤ 15,000 words** incl. text + references + footnotes; **Comments/Replies ≤ 3,000** | References count toward the limit |
| Abstract              | **150-200 words**, non-identifying                                            | Different from journals that cap at 150                          |
| Format                | Double-spaced, **Times New Roman 12 pt**, ≥1-inch margins, **ASA Style Guide** | Specific manuscript formatting                                   |
| Transparency          | **ASA data-sharing policy** (availability after publication)                  | A norm, not a verified editor-run replication check              |

Volatile specifics (editors and term, fee, exact caps, data policy) change — items not directly
confirmed are marked **待核实** in [`resources/official-source-map.md`](resources/official-source-map.md).
**Verify on the official journal page.**

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/asr-skills
/plugin install asr-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/asr-skills.git
cd asr-skills

mkdir -p ~/.claude/skills && cp -R skills/asr-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/asr-* ~/.codex/skills/
```

### First Prompt

```
Use asr-workflow to tell me which skill I should use next for my ASR manuscript.
```

---

## Default Workflow

```text
asr-topic-selection
        ▼
asr-literature-positioning
        ▼
asr-theory-building
        ▼
asr-research-design
        ▼
asr-data-analysis
        ▼
asr-tables-figures
        ▼
asr-writing-style          (polish)
        ▼
asr-data-and-transparency
        ▼
asr-review-process
        ▼
asr-submission
        ▼
asr-rebuttal
```

`asr-workflow` is the router — it tells you which skill to use next based on where you are.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `asr-workflow`                 | Router — decides which sub-skill to invoke next                               |
| `asr-topic-selection`          | Broad sociological significance; Article vs. Comment/Reply                     |
| `asr-literature-positioning`   | Place the contribution in a sociological debate that travels                  |
| `asr-theory-building`          | Build a portable theoretical argument (not just a finding)                    |
| `asr-research-design`          | Defend the design — quant, demographic, comparative-historical, ethnographic, network |
| `asr-data-analysis`            | Analysis norms, uncertainty, robustness across sociological methods           |
| `asr-tables-figures`           | Clear, self-contained exhibits (excluded from the word count)                 |
| `asr-writing-style`            | ASA Style Guide; reach the discipline within 15,000 words                     |
| `asr-data-and-transparency`    | ASA data-sharing policy; confidentiality; documentation                       |
| `asr-review-process`           | Masked review, decisions, what reviewers weigh                                |
| `asr-submission`               | Sage Track preflight (masking, $25 fee, abstract 150-200, 15,000 words)       |
| `asr-rebuttal`                 | R&R response-letter strategy for multiple reviewers + editor                  |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — sociology data sources (GSS / PSID / IPUMS / LIS) + R / Stata / Python and CAQDAS/QCA tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official SAGE / ASA URLs behind every fact, with 待核实 markers

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not assert volatile metadata (current editors and term, fee, exact caps, data policy) — verify on the official page; unverified items are marked 待核实
- It does not decide whether your question is of broad sociological significance — that is the researcher's call

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [American Sociological Review (SAGE)](https://journals.sagepub.com/home/asr) — publisher home
- [ASR at ASA](https://www.asanet.org/publications/journals/american-sociological-review/) — owner, submission information, policies

---

## License

MIT
