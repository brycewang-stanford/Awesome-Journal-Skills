---
name: jebo-workflow
description: Use when deciding which jebo-* sub-skill to invoke next, or when sequencing manuscript work from topic through rebuttal for a Journal of Economic Behavior & Organization (JEBO) submission. Routes by paper archetype — experiment, observational/behavioral empirics, behavioral theory, or agent-based simulation — but does not replace the specialized skills.
---

# JEBO Workflow Router (jebo-workflow)

## Overview

This is the router. It tells you **which jebo-* skill to use at the current stage** of a manuscript aimed at the *Journal of Economic Behavior & Organization* (JEBO) — Elsevier's broad outlet for **behavioral, experimental, and organizational economics**: bounded rationality, social preferences, lab and field experiments, behavioral game theory, organizational behavior and institutions, evolutionary/adaptive economics, and economic psychology. JEBO is deliberately **methodologically pluralist** — it publishes theory, experiments, observational empirics, and agent-based simulation side by side — so the binding constraint depends heavily on which of those four you are writing.

Operational tells that you are at JEBO and not a sibling: the paper leads with a **behavioral mechanism** (a deviation from frictionless rational-actor benchmarks), not with a clean causal-policy number for its own sake (that is AEJ: Applied / J. Public Econ) and not with a theorem about equilibrium existence (that is GEB). Process facts, verified 检索于 2026-06；以官网为准: Elsevier, hosted on ScienceDirect, ISSN 0167-2681, founded 1980, monthly; submission via **Elsevier Editorial Manager**; **single-anonymized** review (referees anonymous, authors named); abstract **≤250 words**, 1–7 keywords, JEL codes; author-date (Elsevier Harvard) references; data sharing **encouraged via the Research Data policy / Mendeley Data**, not a hard pre-acceptance gate. Editors (re-verified 2026-06-22 via Elsevier editorial board / IDEAS-RePEc): **Daniel Houser (George Mason) and Daniela Puzzello (Indiana)** — re-confirm on the live masthead before submission, as the roster rotates.

## When to trigger

- The user asks "what should I do next?" on a JEBO-bound paper
- A draft's current bottleneck needs diagnosing
- Work is ping-ponging between design, mechanism, exhibits, and the response letter
- A JEBO decision letter arrived and the user needs to switch into revision mode

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Is this behavioral enough for JEBO, or is it ExpEcon / GEB / J. Public Econ? | `jebo-topic-selection` |
| Contribution vs. the behavioral/experimental frontier is fuzzy | `jebo-literature-positioning` |
| Experimental design, treatment, or observational causal design is shaky | `jebo-identification` |
| The behavioral model / mechanism is loose or decorative | `jebo-theory-model` |
| Results may be specification-, demand-effect-, or inference-sensitive | `jebo-robustness` |
| Treatment-comparison exhibits are dense or hard to read | `jebo-tables-figures` |
| Prose buries the mechanism; abstract/intro do not land | `jebo-writing-style` |
| z-Tree/oTree code, instructions, and data deposit need packaging | `jebo-replication-package` |
| Want to anticipate referee objections before submitting | `jebo-referee-strategy` |
| Ready to submit via Editorial Manager; need a preflight | `jebo-submission` |
| Received an R&R; need a response-letter strategy | `jebo-rebuttal` |

## Default order

1. `jebo-topic-selection` — confirm the behavioral question fits JEBO, not a sibling
2. `jebo-literature-positioning` — stake the contribution vs. the behavioral frontier
3. `jebo-identification` — experimental design or observational causal credibility
4. `jebo-theory-model` — the behavioral model/mechanism that organizes the evidence
5. `jebo-robustness` — demand effects, MHT, specification, inference
6. `jebo-tables-figures` — treatment-comparison exhibits
7. `jebo-writing-style` — make the mechanism land (abstract + intro last)
8. `jebo-replication-package` — instructions + experiment code + data deposit
9. `jebo-referee-strategy` — anticipate the modal JEBO referee
10. `jebo-submission` — Editorial Manager preflight
11. `jebo-rebuttal` — after the R&R

> `jebo-writing-style` is late-stage polish; do not rewrite the intro before design and mechanism settle.

## Routing by paper archetype

JEBO spans four method families and the first bottleneck differs by family. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| Lab/field experiment (own data) | incentive compatibility, no-deception norm, pre-registration, comprehension checks | `jebo-identification` |
| Behavioral observational empirics | causal design (DID/IV/RD) + mapping estimate to a behavioral mechanism | `jebo-identification` → `jebo-theory-model` |
| Behavioral / bounded-rationality theory | a sharp testable prediction, not just a richer model | `jebo-theory-model` |
| Agent-based / evolutionary simulation | calibration discipline, parameter sweeps, reproducibility | `jebo-theory-model` → `jebo-robustness` |

## Worked routing example (illustrative)

A user says: "My lab experiment on overconfidence and team formation works, but a referee says the result could be a demand effect and the link to the behavioral model is hand-wavy." Two distinct JEBO pushbacks: *experimenter demand not ruled out* (owned by `jebo-robustness`, with the design defense in `jebo-identification`) and *mechanism not pinned to the model* (owned by `jebo-theory-model`). Route to `jebo-identification` to firm the design, `jebo-theory-model` to make the prediction sharp, then `jebo-robustness` for the demand-effect controls before returning to exhibits and the rebuttal.

## Anti-patterns

- Treating JEBO as interchangeable with **Experimental Economics** (ESA, method-focused) — JEBO wants the behavioral economics, not a pure design contribution
- Treating it as **Games and Economic Behavior** (formal game theory) or **J. of Economic Psychology** (psychology-first)
- Polishing prose before design, mechanism, and the evidence hierarchy are stable
- Letting the appendix carry a behavioral claim the main text must establish
- Quoting volatile process facts (editor, fees, limits) as permanent — mark them 待核实

## Output format

```text
【Target】Journal of Economic Behavior & Organization
【Archetype】experiment / observational / theory / simulation
【Current bottleneck】fit / contribution / design / mechanism / robustness / exhibits / style / package / submission / revision
【Next skill】<one jebo-* skill>
【Reason】why this is the binding constraint at JEBO
【Source check】official facts verified or marked 待核实
```
