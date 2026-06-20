# Journal of Policy Analysis and Management Skills

<p align="center">
  <img src="assets/cover.svg" alt="Journal of Policy Analysis and Management cover" width="200">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Journal](https://img.shields.io/badge/journal-JPAM-8a5a12)](https://onlinelibrary.wiley.com/journal/15206688)
[![Field](https://img.shields.io/badge/field-Public%20Policy-1f6feb)](https://www.appam.org/news/jpam/)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

Agent skill stack for manuscripts targeted at the **Journal of Policy Analysis and Management (JPAM)** —
the **cross-disciplinary public-policy-analysis flagship** of the **Association for Public Policy Analysis
and Management (APPAM)**, founded in **1981** (from the merger of *Policy Analysis* and *Public Policy*)
and published by **Wiley**. JPAM bridges **economics, political science, and public management** to
publish **rigorous causal evaluation of policies and programs** across the policy fields — education,
health, labor & welfare, housing, crime & justice, environment, immigration, and social policy — with a
premium on **credible identification** and on **translating evidence into a clear policy implication**.

This repository is opinionated. It is **not** a generic social-science writing toolbox and it is **not**
an economics pack repurposed for policy. It is a **JPAM-specific** stack: a **credibly identified policy
or program effect** (RCT, DiD/event-study, RD, IV, synthetic control), **cost-benefit and distributional**
analysis, a **policy implication stated without overclaiming**, **double-blind** preparation, the **APPAM
membership-or-fee** requirement, and an **archived replication package** so results can be reproduced.

> **Official basis checked 2026-06-20** — facts are anchored to APPAM's JPAM pages, Wiley's journal /
> author routes, Wiley 2026 editor-note search renderings, and the RePEc `wly:jpamgt` record. Live
> submission prompts can change, so verify portal prompts and file metadata in Wiley Research Exchange.

---

## What Is JPAM, and Why a Dedicated Stack?

JPAM's constraints differ from a field economics journal or a public-management journal:

| Constraint            | JPAM                                                                          | Implication                                                       |
|-----------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------|
| Scope                 | **Cross-disciplinary policy analysis** (econ + political science + public mgmt) | The paper must inform a real policy decision across fields       |
| Premium on            | **Credible causal identification** of a policy/program effect                  | Selection-on-observables rarely clears the bar                   |
| Distinctive layer     | **Cost-benefit + distributional** analysis — who gains, who pays               | An estimate alone is not enough; "should we do it?" matters       |
| House voice           | A **clear policy implication, without overclaiming**                           | Calibrate the claim to the estimand; name the limits             |
| Publisher / owner     | **Wiley** / **APPAM**                                                          | Submitted through Wiley Authors / **Research Exchange**          |
| Review model          | **Double-blind / anonymized preflight**                                        | Anonymize the manuscript; keep a separate title page ready       |
| Submission gate       | **APPAM membership OR a submission fee** (waivers available)                   | Members free; non-members **USD 100 professional / USD 40 student** |
| Transparency          | **Archive data + code; data-availability statement**                          | Plan early for restricted administrative data                    |
| Distinctive forum     | **Point/Counterpoint** (invited, not peer-reviewed) + Policy Insights          | Choose the right article type up front                           |

Volatile specifics change. The source map separates confirmed APPAM/Wiley facts from live Research
Exchange prompts that must be checked at upload.

### Article types

- **Feature Research Articles** — full, credibly identified policy evaluations (the core format).
- **Methods for Policy Analysis** — methodological advances for policy analysts (peer-reviewed).
- **Policy Retrospectives** — reflective look-backs at a policy or literature.
- **Point/Counterpoint** — **invited, not peer-reviewed** scholarly debate on a timely policy question.
- **Policy Insights** — **invited, not peer-reviewed**, short (≤ 3,000 words) rapid takes.
- **Book Reviews** — invited/edited.

---

## Quick Start

### Option A — Claude Code Plugin (recommended)

```bash
/plugin marketplace add https://github.com/brycewang-stanford/jpam-skills
/plugin install jpam-skills
/reload-plugins
```

### Option B — Manual Copy

```bash
git clone https://github.com/brycewang-stanford/jpam-skills.git
cd jpam-skills

mkdir -p ~/.claude/skills && cp -R skills/jpam-* ~/.claude/skills/
# or
mkdir -p ~/.codex/skills && cp -R skills/jpam-* ~/.codex/skills/
```

### First Prompt

```
Use jpam-workflow to tell me which skill I should use next for my JPAM manuscript.
```

---

## Default Workflow

```text
jpam-topic-selection
        ▼
jpam-literature-positioning
        ▼
jpam-theory-building
        ▼
jpam-research-design
        ▼
jpam-data-analysis
        ▼
jpam-tables-figures
        ▼
jpam-writing-style          (polish)
        ▼
jpam-transparency-and-data
        ▼
jpam-review-process
        ▼
jpam-submission
        ▼
jpam-rebuttal
```

`jpam-workflow` is the router — it tells you which skill to use next based on where you are and which
**article type** fits. If you are pitching an invited type (Point/Counterpoint, Policy Insights), confirm
the invitation and length rules before drafting.

---

## Skills

| Skill                          | Purpose                                                                       |
|--------------------------------|-------------------------------------------------------------------------------|
| `jpam-workflow`                | Router — decides which sub-skill to invoke next                               |
| `jpam-topic-selection`         | Policy-relevant, credibly evaluable fit; pick the right article type           |
| `jpam-literature-positioning`  | Position across econ / political science / public-management literatures       |
| `jpam-theory-building`         | Build the theory of change / logic model, mechanism, and scope conditions     |
| `jpam-research-design`         | Credible identification — RCT, DiD/event-study, RD, IV, synthetic control      |
| `jpam-data-analysis`           | Estimation + cost-benefit + distributional analysis, robustness, uncertainty  |
| `jpam-tables-figures`          | Decision-legible exhibits: effect, uncertainty, design validity, distribution |
| `jpam-writing-style`           | A clear policy implication without overclaiming; cross-field legibility        |
| `jpam-transparency-and-data`   | Replication package + data-availability statement; restricted-data path        |
| `jpam-review-process`          | Double-blind review, desk screen, article types, decision categories           |
| `jpam-submission`              | Research Exchange preflight (anonymization, fee/membership, ORCID, data statement) |
| `jpam-rebuttal`                | R&R response across an identification reviewer and a policy reviewer           |

### Resources

- [`resources/external_tools.md`](resources/external_tools.md) — policy-evaluation data sources (CPS / SIPP / NCES / CMS / UCR / HUD / ACS) + R / Stata / Python and cost-benefit / MVPF tooling
- [`resources/official-source-map.md`](resources/official-source-map.md) — official Wiley / APPAM URLs behind every fact and live-check guardrail
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) — before→after JPAM-style introduction (fictional, illustrative)
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — real, web-verified JPAM papers by field × method, with a sibling-journal guardrail
- [`resources/code/`](resources/code/) — vendored Stata + Python causal-inference skeleton (DiD / IV / RD / DML)

---

## What This Repo Does Not Do

- It does not write a submittable manuscript for you
- It does not simulate any specific editor's or reviewer's taste
- It does not hard-code volatile metadata beyond sourced facts; verify live Research Exchange prompts before upload
- It does not decide whether your question is policy-relevant or your design credible — that is the researcher's call

---

## Differences vs. Sibling Journals

| Journal | What it is | How JPAM differs |
|---------|------------|------------------|
| **AEJ: Economic Policy** / **J. of Public Economics** | Economics **field** journals on policy | JPAM is cross-disciplinary and foregrounds the policy decision + cost-benefit + distribution, not just the economics |
| **Public Administration Review** / **JPART** | Public-management / administration journals | JPAM centers credibly identified **program effects**, not management theory |
| **APSR / AJPS** | Political-science generalist/field journals | JPAM's bar is policy evaluation and decision relevance, not disciplinary theory contribution |
| **JPAM** | **Cross-disciplinary policy-analysis flagship of APPAM** | Credible identification **plus** a calibrated policy implication for a mixed econ/PS/PA audience |

---

## Related

- [awesome-journal-skills](https://github.com/brycewang-stanford/awesome-journal-skills) — Index of journal-specific skill packs
- [JPAM on Wiley Online Library](https://onlinelibrary.wiley.com/journal/15206688) — publisher home
- [JPAM at APPAM](https://www.appam.org/news/jpam/) — owner, author guidelines, article types, fees

---

## License

MIT
