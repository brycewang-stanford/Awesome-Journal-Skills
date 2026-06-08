> **Illustrative teaching example.** The paper, system, datasets, and every number below are
> **fictional** and exist only to demonstrate AAAI house style. No real-paper facts and no AAAI policy
> are stated here — for policy see [`../official-source-map.md`](../official-source-map.md). Corresponding
> skills: [`aaai-writing-style`](../../skills/aaai-writing-style/SKILL.md) and
> [`aaai-topic-selection`](../../skills/aaai-topic-selection/SKILL.md).

# Worked Example: An AAAI-Style Abstract + Introduction (before → after)

This demonstrates the **AAAI first-page arc** from `aaai-writing-style`:
**AI problem → why it is hard / why a broad AI audience should care → contribution type (method /
theory / system / benchmark / dataset / evaluation / social impact / alignment) → evidence → scope and
limitation** — under the AAAI constraints that the **problem, the new capability or insight, and the
evidence appear on the first page**, that the work reads to a broad AI program committee (not only one
benchmark community), and that claims stay aligned with reproducibility and supplementary evidence and
avoid unsupported "human-level" / "general" / "safe" wording.

The AAAI proceedings are page-limited (AAAI-26: 7 pages of technical content; see
[`../official-source-map.md`](../official-source-map.md)), so the abstract and intro must carry the
contribution **compactly** — no long literature catalogue, no method name as the lead.

**Illustrative paper (fictional):** *"Budgeted Self-Consistency: Calibrated Early-Exit Sampling for
Reliable LLM Reasoning."* Fictional setting: an inference-time decoding method that decides how many
reasoning samples to draw per question based on a calibrated confidence signal.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Large language models have attracted enormous attention in recent years and are now
> used across many tasks. Self-consistency is a popular technique. In this paper, we propose a new
> method based on sampling multiple chains of thought and aggregating them. We use a confidence
> estimator and an early-exit rule. We run experiments on several datasets and show that our method
> works well. We hope this work is useful to the community.
>
> **Introduction.** Reasoning with large language models has been studied extensively. Many methods
> have been proposed, including chain-of-thought prompting, self-consistency, and various decoding
> strategies. In this paper, we use a calibrated early-exit sampler to improve LLM reasoning. We
> describe our approach, run experiments, and report results. Section 2 reviews related work, Section 3
> describes the method, Section 4 presents experiments, and Section 5 concludes.

**What's wrong (against `aaai-writing-style` / `aaai-topic-selection` / `aaai-experiments`):**

- **No AI problem stated on page one.** A broad AAAI reviewer cannot tell what capability is new or why
  it matters beyond one benchmark (`aaai-writing-style`: "state the AI problem, the new capability or
  insight, and the evidence in the first page").
- **Contribution type is unnamed** — is this a method, a system, an evaluation? (`aaai-writing-style`:
  "make clear whether the contribution is method, theory, system, benchmark, ...").
- **No quantitative evidence in the abstract** ("works well", "useful").
- **Throat-clearing** ("enormous attention", "studied extensively") burns page-limited space.
- **Related-work catalogue** instead of a compact contrast (`aaai-writing-style`: "compact related-work
  contrasts instead of long literature catalogues").
- **Leads with the technique**, not the problem; **no limitation / scope**; **no link to
  reproducibility or compute** that Phase 1 reviewers need (`aaai-experiments`).

---

## After (AAAI arc — problem + contribution type + evidence on page one, compact)

> **Abstract.** Self-consistency improves large-language-model (LLM) reasoning by sampling many
> reasoning chains and voting, but it spends the *same* large sample budget on easy and hard questions
> alike, making it costly and wasteful. **We present Budgeted Self-Consistency (BSC), an inference-time
> *method* that calibrates a per-question confidence signal and exits early once the answer is
> confidently determined, reallocating compute to the questions that actually need it.** Across five
> reasoning benchmarks and three open-weight model families, BSC matches the accuracy of fixed
> 40-sample self-consistency while using **2.7x fewer samples on average**, and its calibrated
> confidence is well-behaved (expected calibration error below 0.03). The gains are *mechanistic*, not
> dataset-specific: they hold across model families and grow with question-difficulty dispersion. We
> release code, prompts, and per-seed logs; the method adds no training and a single interpretable
> threshold. *(Problem → contribution type "method" → evidence with numbers → scope → reproducibility,
> all in the abstract.)*
>
> **Introduction.** **Can an LLM decide *how much* to think per question, instead of paying a fixed,
> worst-case reasoning budget on every input?** Self-consistency raises reasoning accuracy by drawing
> many chains of thought and majority-voting, but it draws the same large number of samples for a
> trivial arithmetic step and for a multi-hop proof — so most of its compute is wasted on questions the
> model already answers confidently after a few samples. *(AI problem stated first, legible to a broad
> AI reviewer; why it is hard / why it matters: a compute-reliability tradeoff, not a single
> leaderboard.)*
>
> The difficulty is that "confidently determined" must be estimated *online, mid-decoding,* from the
> samples drawn so far, and a naive vote-margin estimate is badly miscalibrated — it stops too early on
> hard questions and too late on easy ones. *(Names the technical obstacle before the method.)*
>
> **Our contribution is a method**: Budgeted Self-Consistency couples a lightweight calibrated
> confidence estimator with an early-exit rule, so the sample budget is spent where it changes the
> answer. We make three claims, each tied to an experiment: (i) BSC matches fixed-budget
> self-consistency accuracy at **2.7x fewer samples** (cost experiment); (ii) its confidence is
> calibrated across model families (calibration experiment, ECE < 0.03); and (iii) the savings come
> from difficulty-adaptive allocation, not from a single dataset, shown by an ablation that removes
> calibration and by a controlled difficulty-dispersion study. *(Contribution type named; every claim
> maps to evidence — the `aaai-experiments` rule.)*
>
> BSC is **training-free** and exposes a **single interpretable threshold**, so it drops into existing
> decoding stacks. We state its scope plainly: it assumes a usable confidence signal and helps most when
> question difficulty varies; on uniformly hard sets the budget cannot be cut. *(Scope + limitation on
> page one; no "general" or "human-level" overclaim.)* Code, prompts, seeds, and per-question sample
> counts are released, and all results report mean and variance over five seeds with matched compute.
> *(Reproducibility / compute hook the Phase 1 reviewer needs.)*
>
> The paper proceeds as follows. Section 2 contrasts BSC with self-consistency and adaptive-compute
> decoding; Section 3 defines the calibrated early-exit rule; Section 4 reports the cost, calibration,
> and ablation experiments. *(Compact roadmap — no over-signposting.)*

---

## Why the "after" meets the AAAI bar

Mapped to the skill checklists:

- **First page states the AI problem, the new capability, and the evidence** — the question, the method,
  and the headline numbers (2.7x fewer samples; ECE < 0.03) all appear in the abstract and first
  paragraph (`aaai-writing-style`).
- **Contribution type is explicit** — "Our contribution is a *method*" — so a broad PC can classify the
  paper instantly (`aaai-writing-style` / `aaai-topic-selection`).
- **Broad-AI framing, not one benchmark** — the result is a compute-reliability mechanism that "holds
  across model families," which a reasoning, efficiency, *or* evaluation reviewer can each value
  (`aaai-topic-selection` strong-signal: "evidence that supports a general AI claim, not only a local
  application result").
- **Every claim maps to an experiment** — three numbered claims, each with its experiment and an
  ablation that isolates the mechanism (`aaai-experiments`: "map every experimental block to a claim",
  "ablations that isolate mechanisms").
- **Scope and limitation stated up front**, and **no unsupported "general / human-level / safe"
  language** (`aaai-writing-style` overclaim guard).
- **Reproducibility-aware** — code/prompts/seeds and mean±variance over matched compute are promised on
  page one, easing checklist scrutiny and the Phase 1 trust decision (`aaai-experiments`,
  `aaai-reproducibility`).
- **Page-limit discipline** — the related-work catalogue and throat-clearing are gone; the contrast is
  compressed to one roadmap sentence, conserving the 7-page technical budget.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified AAAI
> main-conference papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for the AAAI page-limit, reproducibility, and
> AI-use policy this example is written to respect.
