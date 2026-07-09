> **Illustrative teaching example.** The paper, testbed, system, and every number below are
> **fictional** and exist only to demonstrate CoNEXT house style. No real-paper facts, deployments,
> or results are stated, and no policy is invented. Corresponding skills:
> [`conext-writing-style`](../../skills/conext-writing-style/SKILL.md),
> [`conext-topic-selection`](../../skills/conext-topic-selection/SKILL.md), and
> [`conext-experiments`](../../skills/conext-experiments/SKILL.md).

# Worked Example: A CoNEXT-Style Abstract + Introduction (before → after)

This demonstrates the **CoNEXT first-page arc** from `conext-writing-style`:
**networking problem in a real deployment → why the current state is inadequate → contribution
(system and/or measurement) → evidence on a real testbed or trace → what changes for operators or
protocols** — with the CoNEXT expectations that the contribution is a *networking* contribution,
evidence is **proportional to the claim** and drawn from the **real target platform**, and a
**limitations/threats** posture is visible from the start (not bolted on as a closing paragraph).

The framing also reflects `conext-topic-selection`: CoNEXT is strongest when the lesson is about
how networks are **built, measured, operated, or evolved** — here, whether a congestion-control
change helps under real bottlenecks — rather than a modeling result whose networking consequence is
incidental (which would route to a theory or ML venue), and when the study could not simply be
re-labeled as a SIGCOMM, NSDI, or IMC paper without loss.

**Illustrative paper (fictional):** *"Does It Actually Fill the Pipe? A Measurement Study and a
Bottleneck-Aware Pacing Filter for Short Flows."* Fictional artifact: a pacing filter that predicts
when a short flow will be throttled by a shallow-buffer bottleneck, evaluated on a real testbed and
a passive trace.

---

## Before (buries the networking contribution — typical first-draft abstract + intro)

> **Abstract.** Machine learning has transformed computer networking. We build a system that paces
> short flows using a state-of-the-art model and a novel feature pipeline. Our approach achieves
> high accuracy on a large dataset and outperforms baselines, showing the promise of AI for
> congestion control.
>
> **Introduction.** Congestion control is important. Many systems now pace flows in the network. In
> this paper we use an ML model with carefully engineered features to decide pacing, and we
> evaluate it on a dataset of flows, showing strong results. Section 2 covers related work,
> Section 3 our approach, Section 4 experiments, Section 5 limitations, and Section 6 concludes.

**What's wrong (against `conext-writing-style` / `conext-topic-selection` / `conext-experiments`):**

- **No networking problem on the first page** — it leads with "ML transformed networking" and an
  accuracy win, not with a problem an operator or protocol designer recognizes. CoNEXT wants the
  networking contribution up front.
- **Wrong claim shape.** "High accuracy" on an offline dataset is not evidence that anything
  changes on a real path; the paper never asks whether flows actually complete faster under a real
  bottleneck — the actual networking outcome.
- **Limitations are a Section 5 afterthought**, so the central threat (does the offline label
  reflect on-path behavior?) is never engaged where it matters.
- **Model-as-contribution.** If the model were swapped, no networking lesson would remain — the
  `conext-topic-selection` re-route signal that this is an ML paper wearing a networking title.
- **No testbed, no trace provenance, no artifact** — a double-anonymous CoNEXT reviewer will look
  for the real evaluation platform immediately.
- **Over-signposted roadmap** substituting for an argument.

---

## After (CoNEXT arc — problem → inadequacy → contribution → real-testbed evidence → what changes)

> **Abstract.** Short flows dominate modern application traffic, yet they routinely finish before
> congestion control can find the right rate, and shallow-buffer bottlenecks silently throttle them
> — a loss operators cannot see with flow-level counters. We study **1.4 billion short flows across
> three vantage points** and find that a large fraction are throttled at a bottleneck the sender
> never detects, with the throttled fraction varying sharply by path and buffer depth (measurements
> reported with confidence intervals; the trace-extraction methodology and vantage points are in
> the artifact). Building on the study, we present **PaceGuard**, a bottleneck-aware pacing filter
> that predicts throttling from the first RTTs and adjusts pacing before the flow completes. On a
> **hardware testbed with real switch buffers** it shortens completion time for throttled short
> flows while leaving unaffected flows unchanged; we report effect sizes, a per-path breakdown, and
> a contamination-aware ablation isolating the learned component from the pacing mechanism.
> *(problem → inadequacy → finding → system → real-testbed evidence → limitations posture — all on
> the first page.)*
>
> **Introduction.** *(¶1 — the networking problem, first breath.)* An application's tail latency is
> often set by its shortest flows, and those flows are the ones congestion control serves worst:
> they complete before the control loop converges. When a shallow-buffer bottleneck throttles them,
> flow-level counters show nothing wrong. The engineering question is therefore not "can a model
> predict throughput?" but **"which short flows are being throttled at a bottleneck, and can a
> sender act before the flow ends?"**
>
> *(¶2 — why the current state is inadequate.)* Existing pacing schemes react to signals that
> arrive too late for short flows, and offline throughput predictors are evaluated against
> dataset labels rather than on-path completion. Both are **proxies for what an operator cares
> about, not the outcome itself**: a predictor can score well offline and still miss the throttling
> that matters. No prior study measures the throttled fraction of short flows on real paths at
> scale and ties it to a deployable sender-side action.
>
> *(¶3 — contribution, stated as networking claims.)* We make two contributions. First, a
> **measurement study** of how often, and on which paths, short flows are throttled at shallow
> bottlenecks, across three vantage points with an openly documented trace-extraction protocol.
> Second, **PaceGuard**, a sender-side filter that predicts throttling from early RTT and adjusts
> pacing, evaluated for whether it shortens completion without harming other traffic.
>
> *(¶4 — evidence on the real target, each claim paired.)* We tie every claim to evidence: the
> throttled-fraction estimates carry bootstrap confidence intervals (Table 1); per-path differences
> are tested with corrected comparisons (Fig. 2); PaceGuard's completion-time and fairness effects
> are reported with effect sizes on a **hardware testbed with real switch buffers and on
> trace-driven replay** (Table 3); and an ablation replacing the learned predictor with a threshold
> heuristic isolates its marginal value (Table 4). Traces, configs, testbed topology, and code are
> in the anonymized artifact.
>
> *(¶5 — limitations posture and what changes for networking.)* We state the central threat plainly:
> "throttled at a bottleneck" is **inferred** from path signals, not ground-truth switch telemetry,
> and we bound it with a subset where switch counters were available. The payoff for practice is
> concrete: operators gain visibility into a loss they could not see, and senders gain an action
> they can deploy without network support. Section 2 details the measurement design; Section 3
> PaceGuard; Section 4 the evaluation; limitations are argued alongside each result, not deferred.
> *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the CoNEXT bar

Mapped to the skill checklists:

- **Networking contribution on the first page** — the abstract and ¶1 pose an operational
  short-flow problem and an outcome-level question before any model detail
  (`conext-writing-style`: "lead with the networking contribution").
- **Evidence proportional to the claim** — the claim is about *on-path completion*, so the evidence
  is testbed and trace-driven replay with intervals and effect sizes, not offline accuracy
  (`conext-experiments`: match the evidence to the claim shape and use the real target platform).
- **Limitations engaged where they live** — the inference threat (proxy for ground-truth
  throttling) is named in ¶5 and bounded with a telemetry subset, reported *with* results rather
  than quarantined (`conext-writing-style`: the limitations section is an argument, not
  boilerplate).
- **Right venue, model-swap test passes** — the lesson (a large fraction of short flows are
  invisibly throttled; a sender can act early) survives swapping the predictor, so it is a
  networking contribution, not an ML re-route (`conext-topic-selection`).
- **Reproducible by default** — traces, configs, testbed topology, and code are in an anonymized
  artifact, matching CoNEXT's double-anonymous, reproducibility-committee expectations and the
  badge **opt-in due at submission** (`conext-reproducibility`, `conext-artifact-evaluation`).
- **Fair, contamination-aware evaluation** — a real-buffer testbed, per-path breakdown, and an
  ablation isolating the learned component pre-empt the reviewer's first three objections
  (`conext-experiments`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified CoNEXT
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for CoNEXT-specific submission policy and
> the two-cycle PACMNET journal-style model.
