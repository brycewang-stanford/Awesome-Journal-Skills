> **Illustrative teaching example.** The paper, tool, benchmarks-as-used, and every number below
> are **fictional** and exist only to demonstrate DAC house style. No real-paper facts, tools, or
> QoR results are stated, and no policy is invented. Corresponding skills:
> [`dac-writing-style`](../../skills/dac-writing-style/SKILL.md),
> [`dac-topic-selection`](../../skills/dac-topic-selection/SKILL.md), and
> [`dac-experiments`](../../skills/dac-experiments/SKILL.md).

# Worked Example: A DAC-Style Abstract + Introduction (before → after)

This demonstrates the **DAC first-page arc** from `dac-writing-style`:
**design problem → why the current state is inadequate → contribution stated as a measured QoR
delta → evidence on standard benchmarks against the strongest baseline → why it generalizes** —
within a **six-page double-column budget** and **double-blind** (third-person self-citation).

The framing also reflects `dac-topic-selection`: DAC is strongest when the lesson is about how a
chip is **synthesized, placed, routed, timed, verified, or secured** — here, congestion-aware global
routing — measured in the field's own currency, and when the model-swap test passes (the
design-automation advantage would survive swapping the learner).

**Illustrative paper (fictional):** *"CongNet: Congestion-Aware Global Routing with a Learned Cost
Model."* Fictional tool: a global router that predicts routing congestion and steers wire ordering,
evaluated on standard placement/routing benchmarks against a strong prior router.

---

## Before (buries the contribution; no QoR framing — typical first-draft abstract + intro)

> **Abstract.** Machine learning is revolutionizing chip design. We propose a novel deep-learning
> approach for global routing that uses a state-of-the-art neural network and a new training
> pipeline. Our method achieves excellent results on our benchmarks and outperforms baselines,
> demonstrating the promise of AI for EDA.
>
> **Introduction.** Routing is an important step in physical design. Many routers have been proposed
> over the years. In our previous work [7] we studied congestion, and here we use a neural network to
> improve routing. We evaluate on several designs and show strong results. Section 2 covers related
> work, Section 3 our method, Section 4 experiments, Section 5 concludes.

**What's wrong (against `dac-writing-style` / `dac-topic-selection` / `dac-experiments`):**

- **No design problem or QoR claim on the first page** — it leads with "ML is revolutionizing chip
  design" instead of a routing problem stated in wirelength/overflow/runtime.
- **No named baseline and no standard benchmark** — "our benchmarks" and "baselines" are exactly what
  a DAC reviewer distrusts; the comparison *is* the paper.
- **First-person self-citation** ("in our previous work [7]") **de-anonymizes** under double-blind.
- **Model-as-contribution risk** — "a state-of-the-art neural network" with no EDA-specific lesson
  reads as an ML paper wearing an EDA title (a `dac-topic-selection` re-route signal).
- **Over-signposted roadmap** substituting for an argument, wasting scarce page budget.

---

## After (DAC arc — problem → inadequacy → QoR delta → benchmark evidence → generality)

> **Abstract.** Global routing must close on congestion without inflating wirelength or runtime, yet
> modern designs push analytic routers into repeated rip-up-and-reroute that scales poorly. We present
> **CongNet**, a global router with a learned congestion-cost model that reorders net ripping to
> avoid predicted hot-spots. On the standard ISPD routing benchmarks, CongNet reduces total overflow
> and keeps wirelength within a small margin of the best published router while completing in
> substantially less runtime on the largest circuits; per-benchmark results, seeds, and an ablation
> isolating the learned cost model are reported. The learned model generalizes to designs and a
> technology node unseen in training. *(design problem → inadequacy → QoR delta vs. a named baseline
> → generality — all on the first page.)*
>
> **Introduction.** *(¶1 — the design problem, first breath.)* In advanced-node physical design,
> routing congestion, not raw wirelength, is what stalls timing closure: a router that leaves
> overflow forces costly rip-up-and-reroute iterations that dominate turnaround. The engineering
> question is therefore not "can a model predict congestion?" but **"can a learned congestion model
> reduce real overflow at equal wirelength and lower runtime than the strongest existing router?"**
>
> *(¶2 — why the current state is inadequate.)* Analytic global routers order net ripping by static
> heuristics that ignore where congestion will actually concentrate, so on macro-dense designs they
> re-route the same regions repeatedly. Prior learning-based routers [refs, third person] predict
> congestion maps but do not *act* on the prediction inside the routing loop, leaving the QoR gain
> unrealized.
>
> *(¶3 — contribution, stated as EDA claims.)* We make two contributions. First, a **learned
> congestion-cost model** trained on routed designs that predicts per-region overflow risk. Second,
> **CongNet**, a global router that uses that model to reorder rip-up-and-reroute, realizing the
> prediction as measured QoR rather than a map.
>
> *(¶4 — evidence on standard benchmarks, each claim paired.)* We tie every claim to a number: total
> overflow and wirelength are reported **per benchmark on the full ISPD routing set** (Table 1)
> against the strongest published router tuned to equal effort; runtime and memory are reported on
> the same hardware, including the largest circuits (Table 2); an **ablation** replacing the learned
> cost model with the static heuristic isolates its contribution (Table 3); and generalization is
> shown on designs and a technology node **held out of training** (Table 4). Seeds and variance across
> runs are reported for the stochastic rip-up order.
>
> *(¶5 — generality and what changes for design.)* We state the central limit plainly: the learned
> model is trained on one node family, and we bound its transfer with the held-out-node experiment
> rather than claiming universality. The payoff for practice is concrete: fewer rip-up iterations
> means faster timing closure at equal quality. Section 2 details the cost model; Section 3 CongNet;
> Section 4 the evaluation. *(brief roadmap, no over-signposting; references on the seventh page
> only.)*

---

## Why the "after" meets the DAC bar

Mapped to the skill checklists:

- **QoR contribution on the first page** — the abstract and ¶1 pose a routing/congestion problem and
  state the delta in overflow/wirelength/runtime before any model detail (`dac-writing-style`: "state
  the contribution as a QoR claim").
- **Strongest baseline on a standard suite** — the evaluation commits to the full ISPD set against
  the best published router, tuned to equal effort, per benchmark (`dac-experiments`: the comparison
  is the paper; report the whole suite).
- **Ablation isolates the mechanism** — replacing the learned cost model with the static heuristic
  attributes the gain to the contribution, not to tuning (`dac-experiments`).
- **Model-swap test passes** — the lesson (acting on a congestion prediction inside the routing loop
  cuts overflow and runtime) survives swapping the learner, so it is an EDA contribution, not an ML
  re-route (`dac-topic-selection`).
- **Double-blind clean** — prior work and self-references are third person, and no acknowledgements
  or funding appear in the review version (`dac-writing-style`, `dac-submission`).
- **Budget-aware** — one contribution developed deeply, results in compact per-benchmark tables,
  references confined to the seventh page (`dac-writing-style`, `dac-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified DAC
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for DAC-specific submission policy, the
> 6+1 budget, and the Research-vs-Engineering track model.
