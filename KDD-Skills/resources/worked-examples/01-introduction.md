> **Illustrative teaching example.** The system, datasets, numbers, and company below are all
> **fictional**; they exist only to show the KDD register. Nothing here states or invents any
> official policy — formatting and track rules live in
> [`../official-source-map.md`](../official-source-map.md). Corresponding skills:
> [`kdd-writing-style`](../../skills/kdd-writing-style/SKILL.md),
> [`kdd-topic-selection`](../../skills/kdd-topic-selection/SKILL.md), and
> [`kdd-experiments`](../../skills/kdd-experiments/SKILL.md).

# Worked Example: A KDD-Style Abstract + Introduction (before → after)

KDD's first page must answer a different question than a general-ML first page. Reviewers here ask:
**what data regime breaks existing methods, what mechanism fixes it, does it hold at realistic
scale, and could I rebuild it?** The arc this example teaches:
**data regime → failure of current methods → named mechanism → scale + ablation evidence →
availability**. Two register rules matter throughout: efficiency claims need a mechanism attached,
and every dataset mentioned needs its size stated the first time it appears.

**Illustrative paper (fictional, Research Track register):** *"StreamHive: Drift-Aware Anomaly
Detection over Evolving Event Streams with Bounded Memory."* Fictional method: a sketch-based
detector whose memory never grows with stream length and whose update cost is constant per event.

---

## Before (a general-ML draft misrouted into KDD)

> **Abstract.** Anomaly detection is a fundamental task with many applications. Recently, deep
> learning has shown great promise for anomaly detection. We propose StreamHive, a novel deep
> framework for detecting anomalies in streams. Extensive experiments demonstrate that StreamHive
> achieves state-of-the-art performance on multiple datasets, significantly outperforming strong
> baselines.
>
> **Introduction.** Anomaly detection has attracted much attention in recent years. Existing
> approaches can be divided into reconstruction-based, density-based, and classification-based
> methods. However, these approaches have limitations. To address them, we design a novel
> architecture combining a temporal encoder with an adaptive scoring head, trained end-to-end.
> Experiments on several benchmarks show the effectiveness of our approach. Our contributions are:
> (1) we propose StreamHive; (2) we conduct extensive experiments; (3) results show superiority.

**Why this fails the KDD read** (mapped to the skills):

- **No data regime.** Nothing says *streams that evolve, arrive fast, and never fit in memory* —
  the one fact that makes this a KDD paper instead of a generic detection paper
  (`kdd-topic-selection`: the venue signal is the data regime, not the model family).
- **"Extensive experiments" without scale.** No dataset sizes, no events/second, no memory
  footprint. A KDD reviewer cannot tell whether "streams" means 10^4 or 10^10 events
  (`kdd-experiments`).
- **Efficiency never claimed, mechanism never named.** The words "novel framework" do the work a
  mechanism should do (`kdd-writing-style`: attach every adjective to a design decision).
- **Contribution bullets are circular** — "we propose X; we evaluate X; X wins" describes every
  paper ever submitted.
- **No availability statement.** KDD rebuttals cannot carry links, so a paper that never mentions
  its artifact loses its only chance to point reviewers at code (`kdd-artifact-evaluation`).

---

## After (KDD arc: regime → failure → mechanism → scale evidence → availability)

> **Abstract.** Event streams from large platforms evolve: feature distributions drift by hour, and
> anomalies must be flagged **before the stream can be stored, replayed, or labeled**. Detectors
> that retrain on windows either forget slow drifts or hold unbounded state; sketch methods bound
> memory but assume stationarity. We present **StreamHive**, which maintains a *drift-weighted
> family of count-min sketches* whose decay rates are set online from an estimate of drift speed,
> giving **O(1) update per event and memory independent of stream length** while tracking
> non-stationary normality. On three public streams (up to 2.1B events) and one synthetic drift
> suite, StreamHive matches window-retrained deep baselines on AUPRC while using a fixed 512 MB of
> memory and sustaining 1.4M events/second on one core; ablations show the drift-weighted decay,
> not the sketch ensemble, carries the gain. Code, data generators, and configs are in the
> anonymized repository referenced in Section 6. *(regime → failure → mechanism → scale numbers →
> ablation attribution → availability, all in one paragraph.)*
>
> **Introduction.** *(¶1 — the data regime, first.)* On a platform emitting tens of thousands of
> events per second, an anomaly detector faces three simultaneous constraints: it sees each event
> **once**, its memory must not grow with the stream, and the definition of "normal" **drifts**.
> Any two constraints are solved; the three together are not, and that triple is the problem this
> paper takes on.
>
> *(¶2 — why current methods fail, each for a named reason.)* Window-retrained deep detectors
> satisfy drift but not memory: state grows with window size, and slow drifts outlive any
> affordable window. Classical sketch detectors satisfy memory and single-pass but freeze their
> decay schedule, so under drift they either wash out true anomalies (fast decay) or alarm on stale
> normality (slow decay). Online ensembles adapt, but their per-event cost grows with model count.
> *(each family gets a mechanism-level failure, not "has limitations.")*
>
> *(¶3 — the mechanism, named and ablatable.)* StreamHive keeps a small family of count-min
> sketches with distinct decay rates and scores each event against a **drift-weighted mixture**,
> where weights are updated online from a lightweight drift estimator. The design has two
> separable choices — the sketch family and the drift weighting — and Section 5 ablates them
> independently, because the claim is that the *weighting* is what matters.
>
> *(¶4 — evidence scoped to the claim.)* We evaluate on three public event streams (up to 2.1B
> events; sources and preprocessing in Section 4.1) and a synthetic suite where drift speed is
> controlled. StreamHive holds memory fixed at 512 MB and 1.4M events/second on a single core
> while matching retrained baselines on AUPRC; under injected fast drift it degrades gracefully
> where fixed-decay sketches fail outright. We report medians over 5 seeds with interquartile
> ranges, and per-component runtime so the O(1)-update claim is checkable. *(scale numbers, seeds,
> and an auditably scoped "matches" — not "significantly outperforms.")*
>
> *(¶5 — contributions that assert facts, then availability.)* Contributions: (1) a formulation of
> bounded-memory detection under drift as decay-rate selection, (2) the drift-weighted sketch
> family with constant per-event cost, (3) an evaluation to 2.1B events with mechanism-isolating
> ablations, and (4) a released generator suite for controlled-drift benchmarking. All code and
> configurations are in the anonymized repository cited in Section 6, since review-phase
> discussion cannot carry links.

---

## Why the "after" version passes the KDD read

- **The regime is the hook** — single-pass, bounded memory, drift — so track fit is arguable in one
  sentence (`kdd-topic-selection`).
- **Failures are mechanism-level**, which sets up the related-work section as a set of contrasts
  rather than a taxonomy (`kdd-related-work`).
- **Every efficiency number has a mechanism** (O(1) update ← sketch family; fixed memory ← decay,
  not growth) and **every dataset has a size** (`kdd-writing-style`, `kdd-experiments`).
- **Ablations are promised where the claim is made** — the paper stakes itself on the weighting,
  and says where that is tested (`kdd-experiments`).
- **The artifact is referenced inside the paper**, the only reviewer-visible channel given the
  no-links rebuttal rule (`kdd-artifact-evaluation`).
- **ADS contrast:** if this system were *in production*, the same story would route to the ADS
  track and the evidence spine would change from ablations to **post-launch metrics** — see
  `kdd-topic-selection` for that fork.

> Next: [`../exemplars/library.md`](../exemplars/library.md) shows real, DOI-verified KDD papers
> whose first pages execute this arc; [`../official-source-map.md`](../official-source-map.md)
> holds the verified formatting and policy facts.
