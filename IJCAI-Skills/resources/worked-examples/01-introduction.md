> **Illustrative teaching example.** The paper, method, and every number below are **fictional** and
> exist only to demonstrate IJCAI house style. No real-paper facts and no policy claims are stated here
> — for IJCAI-specific policy and deadlines see [`../official-source-map.md`](../official-source-map.md).
> Corresponding skills: [`ijcai-writing-style`](../../skills/ijcai-writing-style/SKILL.md),
> [`ijcai-topic-selection`](../../skills/ijcai-topic-selection/SKILL.md), and
> [`ijcai-experiments`](../../skills/ijcai-experiments/SKILL.md).

# Worked Example: An IJCAI-Style Abstract + Introduction (before → after)

This demonstrates the **IJCAI first-page arc** derived from `ijcai-writing-style` and
`ijcai-topic-selection`:
**problem → gap → core idea → evidence → why it matters beyond a narrow benchmark** — with the IJCAI
rules that the **AI contribution lands on the first page**, the body is **page-limited** (IJCAI-ECAI
2026 used a 7-page body), the submission is **self-contained and double-blind**, and every claim maps to
evidence a broad program committee can verify quickly.

**Illustrative paper (fictional):** *"Anytime Constraint-Guided Search for Combinatorial Optimization
under a Compute Budget."* Fictional method: a search algorithm that returns valid solutions at any
interruption point and tightens them as more compute is spent.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Combinatorial optimization is an important and widely studied problem in artificial
> intelligence. Many algorithms have been proposed over the years. In this paper, we apply a
> branch-and-bound search procedure with a learned heuristic and constraint propagation to a set of
> benchmark instances. We run experiments and report results. Our approach performs well on several
> datasets.
>
> **1 Introduction.** Combinatorial optimization has a long history in AI and operations research. It
> has been studied extensively by many researchers using many techniques. In this work, we use a
> branch-and-bound method together with constraint propagation and a heuristic. Section 2 reviews related
> work, Section 3 gives our method, Section 4 presents experiments, and Section 5 concludes.

**What's wrong (against `ijcai-writing-style` / `ijcai-topic-selection` / `ijcai-experiments`):**

- **Leads with method machinery** ("branch-and-bound with a learned heuristic") instead of the problem
  and the AI idea — the contribution is not on the first page (`ijcai-writing-style`: "put the AI
  contribution in the first page").
- **No stated gap.** A broad PC cannot tell what existing methods fail to do.
- **No verifiable headline evidence** — "performs well" names no metric, baseline, or magnitude
  (`ijcai-experiments`: map each claim to a table/figure/theorem).
- **Throat-clearing** ("important and widely studied," "long history") with no significance beyond the
  benchmark.
- **No broad-AI lesson** — nothing tells a planning, ML, or KR reviewer why this matters to them
  (`ijcai-topic-selection` breadth filter).
- **Over-signposted roadmap** standing in for an argument; wastes scarce body pages.

---

## After (IJCAI arc — problem + gap + core idea + evidence + broad significance, on page one)

> **Abstract.** Many real deployments of combinatorial optimization must return a usable solution **the
> moment they are interrupted**, yet the strongest exact solvers give nothing until they finish. *(problem,
> stated as a gap in current methods.)* We introduce an **anytime constraint-guided search** that maintains
> a feasible incumbent from its first node and provably tightens it as compute grows, using constraint
> propagation to prune without ever discarding feasibility. *(core idea, in one sentence.)* On three
> standard benchmark families it reaches within **2% of the optimal objective using 5x less compute** than
> the best anytime baseline, and matches the exact solver's final solution when run to completion. *(headline
> evidence with a metric and a magnitude.)* Because the method only assumes a propagatable constraint model,
> it applies across scheduling, routing, and configuration. *(why it matters beyond one benchmark.)*
>
> **1 Introduction.** Solvers for combinatorial optimization are usually evaluated on time-to-optimal, but a
> growing class of AI systems — online schedulers, planning-under-interruption, edge configuration — needs a
> **valid answer at any deadline**, not the best answer eventually. The dominant exact methods are
> all-or-nothing: interrupt them early and you get no feasible solution at all. *(problem + concrete gap, in
> the first paragraph, legible to a broad PC.)*
>
> Existing anytime heuristics fill this gap but **sacrifice the guarantees** that make exact solvers
> trustworthy: they can return infeasible incumbents or stall far from the optimum with no bound on how far.
> *(what current work fails to do — positioned against a specific prior approach, not a vague literature.)*
>
> We close this gap with **anytime constraint-guided search**, which keeps a feasible incumbent from the
> first node and uses constraint propagation both to prune and to certify a monotonically improving bound.
> The contribution is to show that **anytime behavior and exactness are not in tension**: the same
> propagation that prunes the search also supplies the feasibility guarantee an anytime solver normally
> gives up. *(core idea + contribution stated early, relative to a named tension in prior work.)*
>
> We evaluate against the strongest anytime and exact baselines on three benchmark families, report
> objective-vs-compute curves with repeated runs and confidence intervals, and ablate the propagation
> component to isolate its effect. *(claim → evidence map and an ablation, as `ijcai-experiments` requires —
> not "we run experiments.")* The method reaches within **2% of optimal at 5x less compute** than the best
> anytime baseline and recovers the exact optimum when uninterrupted. *(headline evidence restated.)*
>
> Beyond these benchmarks, the result implies that **any solver with a propagatable constraint model can be
> made anytime without weakening its guarantees**, which matters for planning, scheduling, and configuration
> across AI. *(broad-AI lesson that travels beyond the setting.)* Section 2 states the formal setup; Section 3
> presents the algorithm and its guarantee; Section 4 reports experiments and ablations. *(brief roadmap — no
> over-signposting, body pages spent on verifiable content.)*

---

## Why the "after" meets the IJCAI bar

Mapped to the skill checklists:

- **AI contribution on the first page** — the problem, the gap, the core idea, and a headline number with a
  metric appear in the abstract and first paragraphs (`ijcai-writing-style`: "problem, gap, core idea,
  evidence, and why it matters").
- **Broad-AI significance, not a single benchmark** — the closing claim generalizes to scheduling, routing,
  and configuration, so a planning, ML, or KR reviewer sees the stake (`ijcai-topic-selection` breadth
  filter; "broadly AI-facing").
- **Every claim maps to verifiable evidence** — baselines named, objective-vs-compute curves with repeated
  runs and confidence intervals, and an ablation isolating the core mechanism (`ijcai-experiments`:
  claim → evidence map; ablate the core mechanism; uncertainty estimates).
- **Page-limited discipline** — the roadmap is one line and the body pages are reserved for formal setup,
  algorithm, guarantee, and experiments (`ijcai-writing-style`: spend the body on claims reviewers can
  verify; IJCAI-ECAI 2026 7-page body).
- **Self-contained and double-blind-ready** — the argument stands without the supplement, and the draft
  carries no acknowledgements, contribution statement, or identifying phrasing (`ijcai-writing-style`,
  `ijcai-submission`).
- **Method demoted to a tool** — "branch-and-bound / propagation" appears only where the algorithm is
  described, never as the lead (avoids the "leading with the machinery" anti-pattern).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified IJCAI papers**
> whose framing executes this arc by topic × method, and confirm current page limits, anonymity, and LLM-use
> rules in [`../official-source-map.md`](../official-source-map.md) before submitting.
