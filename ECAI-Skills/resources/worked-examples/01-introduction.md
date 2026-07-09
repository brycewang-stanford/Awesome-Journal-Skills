> **Illustrative teaching example.** The paper, method, and every number below are **fictional**
> and exist only to demonstrate ECAI house style. No real-paper facts or results are stated, and no
> policy is invented. Corresponding skills:
> [`ecai-writing-style`](../../skills/ecai-writing-style/SKILL.md),
> [`ecai-topic-selection`](../../skills/ecai-topic-selection/SKILL.md), and
> [`ecai-experiments`](../../skills/ecai-experiments/SKILL.md).

# Worked Example: An ECAI-Style Abstract + Introduction (before → after)

This demonstrates the **ECAI first-page arc**: **a well-posed AI problem → why current methods are
inadequate → contribution (a mechanism, and where possible a guarantee) → evidence proportional to
the claim (theory and/or a fair empirical comparison) → what it means for AI** — all compressed
because ECAI reviews a **7-page body** (references are the only overflow: 1 page in a standalone
ECAI, 2 pages in the joint IJCAI-ECAI 2026). ECAI spans symbolic and applied AI, so the arc
rewards a contribution that a **general** AI audience recognizes as foundational, not a
narrow benchmark tweak.

The framing also reflects `ecai-topic-selection`: ECAI is strongest when the lesson is about how an
AI system **reasons, plans, learns, or decides** in a way that generalizes — here, making a learned
heuristic **safe to trust** inside a classical planner — rather than a leaderboard result that
could be relabeled for a pure-ML venue, and when the paper could not simply be resubmitted to a
dedicated sub-venue (AAMAS for MAS, KR for pure knowledge representation) without loss.

**Illustrative paper (fictional):** *"Bounded-Regret Heuristic Switching: Trusting a Learned
Heuristic in Classical Planning Without Losing Completeness."* Fictional method: a planner that
uses a learned heuristic when confident and provably falls back to an admissible baseline
otherwise, with a bound on lost solution quality.

---

## Before (buries the AI contribution — typical first-draft abstract + intro)

> **Abstract.** Deep learning has revolutionized planning. We train a neural network to predict
> good heuristic values and plug it into a planner. On a suite of benchmarks our method expands
> fewer nodes than a classical baseline and finds plans faster, demonstrating the power of learned
> heuristics for planning.
>
> **Introduction.** Planning is a central problem in AI. Classical heuristics are hand-designed and
> can be weak. Recently, machine learning has been used to learn heuristics. In this paper we train
> a model on solved instances and use it to guide search, and we show it works well on standard
> domains. Section 2 covers related work, Section 3 our method, Section 4 experiments, Section 5
> concludes.

**What's wrong (against `ecai-writing-style` / `ecai-topic-selection` / `ecai-experiments`):**

- **No AI problem stated as a problem.** It leads with "deep learning revolutionized planning" and
  a speed win, not with the *foundational* difficulty — a learned heuristic can be **inadmissible**
  and silently cost completeness or optimality. ECAI wants the general AI stake up front.
- **Wrong claim shape.** "Expands fewer nodes on benchmarks" is a benchmark delta; it says nothing
  about the property a planning researcher cares about — **guarantees**. If the model were swapped,
  no lasting AI lesson would remain (the `ecai-topic-selection` re-route signal to a pure-ML venue).
- **No theory where theory is cheap and expected.** A completeness/quality claim is provable; the
  draft asserts it empirically only.
- **Ignores the page budget.** A meandering intro wastes a scarce commodity: the body is 7 pages,
  so paragraph one must already carry the contribution.
- **No reproducibility posture** — no mention of domains, seeds, or a supplement, which a
  double-blind ECAI reviewer looks for immediately.

---

## After (ECAI arc — problem → inadequacy → contribution + guarantee → proportional evidence → meaning)

> **Abstract.** Learned heuristics can speed up classical planning but are **not admissible**, so
> naively trusting them sacrifices the completeness and quality guarantees that make classical
> planning dependable. We ask a foundational question: **can a planner exploit a learned heuristic
> when it helps, yet provably never lose completeness and never exceed a stated suboptimality
> bound?** We present **bounded-regret heuristic switching**, which uses the learned heuristic
> under a confidence test and falls back to an admissible baseline otherwise. We prove the
> resulting search is **complete** and returns plans within a **factor (1+ε)** of optimal for a
> user-chosen ε, and we characterize when switching can only help. Empirically, on standard
> planning domains the method matches the learned heuristic's node savings on instances where it is
> reliable while **recovering the baseline's guarantees** on instances where it is not; domains,
> seeds, and code are in the anonymized supplement. *(problem → inadequacy → mechanism → guarantee
> → proportional evidence — all on the first page.)*
>
> **Introduction.** *(¶1 — the AI problem, first breath.)* Classical planning is trusted precisely
> because it comes with guarantees: a complete search will find a plan if one exists, and an
> admissible heuristic bounds solution quality. Learned heuristics threaten exactly this contract —
> they are often accurate but occasionally badly wrong, and a single inadmissible estimate can
> make search incomplete or return an arbitrarily poor plan. The engineering question is therefore
> not "can a network predict good heuristic values?" but **"how does a planner benefit from a
> learned heuristic while keeping the guarantees that justify using a planner at all?"**
>
> *(¶2 — why current approaches are inadequate.)* Prior work either plugs the learned heuristic in
> directly — buying speed at the cost of guarantees — or restricts it to admissible-by-construction
> forms that discard most of the model's signal. **Neither keeps both the speed and the contract.**
> No prior method lets a planner *decide, per state*, when the learned value is safe to trust.
>
> *(¶3 — contribution, stated as AI claims.)* We make two contributions. First, a **switching
> mechanism** with a per-state confidence test that consults the learned heuristic only inside a
> region where a fallback preserves correctness. Second, a **theoretical characterization**: we
> prove completeness, a (1+ε) suboptimality bound, and a condition under which switching dominates
> the admissible baseline in node expansions.
>
> *(¶4 — evidence proportional to the claim.)* Because the claims are about *guarantees and
> savings*, the evidence is a **proof plus a controlled comparison**: the guarantees are proved
> (full proofs in the supplement, sketched in §4), and the node-expansion and quality behavior is
> measured against both the classical baseline and the naive-learned planner on standard domains,
> reporting where switching helps and where it merely recovers the baseline (Table 1, Fig. 2).
>
> *(¶5 — what it means for AI, and the roadmap.)* The payoff is a way to **adopt learned guidance
> without abandoning the guarantees that define classical planning** — a template for trusting
> learned components inside symbolic systems generally. §2 sets up planning and admissibility; §3
> gives the mechanism; §4 the theory and experiments. *(brief roadmap, no over-signposting — the
> 7-page body cannot afford a full section-by-section preview.)*

---

## Why the "after" meets the ECAI bar

Mapped to the skill checklists:

- **A foundational AI problem on the first page** — the abstract and ¶1 pose a *guarantees*
  question a planning researcher recognizes before any network detail (`ecai-writing-style`: lead
  with the general-AI contribution, not the application of a model).
- **Evidence proportional to the claim** — the claim is about completeness and a suboptimality
  bound, so the evidence is a **proof** plus a controlled empirical comparison, not a benchmark
  delta (`ecai-experiments`: match the evidence to the claim shape; theory when the claim is
  provable).
- **Model-swap test passes** — the lesson (safely trust a learned component inside a symbolic
  system while preserving guarantees) survives swapping the underlying network, so it is an ECAI
  contribution, not a pure-ML re-route (`ecai-topic-selection`).
- **Page-budget discipline** — the contribution and guarantee are in paragraph one because the
  body is 7 pages; nothing decision-critical is deferred to the supplement
  (`ecai-writing-style`, `ecai-supplementary`).
- **Double-blind, open-science posture** — domains, seeds, code, and full proofs sit in an
  **anonymized** supplement, matching ECAI's double-blind review (`ecai-reproducibility`,
  `ecai-submission`).
- **Right track** — it is a foundational main-track contribution; a *deployed* environmental or
  industrial planning system would instead lead with real-world impact and route to **PAIS**
  (`ecai-topic-selection`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ECAI/PAIS
> papers** across contribution shapes, and [`../official-source-map.md`](../official-source-map.md)
> for ECAI-specific submission policy and the FAIA-vs-IJCAI-proceedings regime that governs the
> current cycle.
