> **Illustrative teaching example.** The paper, mechanism, workloads, and every
> number below are **fictional**, invented solely to demonstrate MICRO house style.
> No real results are reported and no venue policy is invented. Skills exercised:
> [`micro-writing-style`](../../skills/micro-writing-style/SKILL.md),
> [`micro-experiments`](../../skills/micro-experiments/SKILL.md), and
> [`micro-topic-selection`](../../skills/micro-topic-selection/SKILL.md).

# Worked Example: A MICRO-Style Abstract + Introduction (before → after)

The target is the **four-beat argument** from `micro-writing-style`:
**characterization → insight → mechanism → accounting** — with the venue's
expectations that motivation is *measured*, the mechanism is *sizeable in bits*,
and every speedup travels with its cost line.

**Fictional paper:** *"Ghostline: Demand-Triggered Dead-Block Reclamation for
Shared Last-Level Caches."* Fictional premise: many LLC lines die (are never
re-referenced) long before eviction, and their death is predictable from a burst
signature at fill time.

---

## Before (how first drafts actually read)

> **Abstract.** As the number of cores grows, the last-level cache becomes
> increasingly critical for performance. In this paper we propose Ghostline, a
> novel technique for improving cache efficiency. Ghostline uses a lightweight
> predictor to identify dead blocks and evict them early. Experiments show that
> Ghostline significantly outperforms LRU and state-of-the-art techniques on a
> wide range of benchmarks, while incurring negligible overhead.
>
> **Introduction.** Modern processors rely on deep cache hierarchies... [half a
> page of textbook background]. Prior work has studied dead-block prediction, but
> existing approaches have limitations. We propose a new approach that is more
> accurate and more efficient. Our contributions are: (1) we propose Ghostline;
> (2) we evaluate Ghostline extensively; (3) we show it outperforms prior work.

**Why this fails the MICRO read** (see the skill checklists):

- **No characterization.** Not one measured number motivates the problem — how
  much LLC capacity is dead, on what workloads, measured how? The first figure a
  MICRO reviewer wants is missing.
- **Mechanism un-sizeable.** "Lightweight predictor" carries no bits, no tables,
  no location in the pipeline. Nothing here could be re-implemented.
- **"Negligible overhead"** is the banned phrase — overhead at MICRO is a number
  with a unit, or it is unreported.
- **"Significantly outperforms ... wide range"** — no instrument named (simulated?
  which simulator?), no baseline named, no geomean, no regression admission.
- **Contribution list is circular** ("we propose it, we evaluate it") — it names
  activities, not findings.

---

## After (the four beats, in order)

> **Abstract.** In simulation of 8-core SPEC CPU2017 rate mixes on a 16MB shared
> LLC, we find that 31% (geomean) of resident lines receive their final hit within
> 40 accesses of fill yet occupy the cache for thousands more cycles before LRU
> reclaims them — dead capacity that re-references cannot use. *(characterization)*
> We observe that these early-dying lines announce themselves: 87% exhibit a
> distinctive fill-time burst signature — three or more hits inside a 16-access
> window, then silence. *(insight)* **Ghostline** detects this signature with a
> per-set sampling monitor and a 12-bit-per-region signature table (3.4KB per
> core), marking matching lines for demand-triggered reclamation: they are evicted
> only when a miss actually needs the space, so mispredictions cost re-fetches
> rather than latency. *(mechanism)* In cycle-level simulation (ChampSim,
> 8-wide OoO, detailed DRAM timing), Ghostline improves geomean IPC by 6.2% over
> an LRU baseline and 2.9% over the strongest prior dead-block scheme
> re-implemented under identical configs, with a worst-case single-workload
> regression of 1.1%; estimated overhead is 3.4KB storage per core and <0.4%
> LLC power (CACTI-class model, versioned in §5). *(accounting)*
>
> **Introduction, ¶1 (the measured problem).** A shared last-level cache earns its
> area only while its lines hold data that will be referenced again. Figure 1
> quantifies how often that fails: across 8-core SPEC CPU2017 mixes, roughly a
> third of LLC capacity is *dead-but-resident* — final hit already taken, eviction
> thousands of cycles away. This is measured headroom, not intuition: an oracle
> that reclaims lines at their true death time gains 11.8% geomean IPC (§6.5).
>
> **¶2 (why existing reclamation falls short, named).** Prior dead-block predictors
> commit to eviction at prediction time, so a false positive pays a full DRAM
> round-trip on the next touch — which is why published schemes throttle
> themselves conservatively and capture under half the oracle headroom in our
> re-implementation (§6.2). Reuse-distance approaches sidestep mispredictions but
> need per-line PC metadata whose storage grows with cache size.
>
> **¶3 (mechanism, sizeable).** Ghostline separates *detection* from *commitment*.
> A sampling monitor observes 32 sets per bank; a signature table (2048 entries ×
> 12 bits) learns which fill-time burst patterns precede death. Matching lines are
> *marked*, not evicted — reclamation happens on demand, when a miss needs a
> victim, making the misprediction penalty a re-fetch we already had to risk.
> Total state: 3.4KB per core; no critical-path logic (victim selection already
> tolerates a table lookup, §4.3).
>
> **¶4 (evidence contract).** We evaluate in cycle-level simulation with the
> methodology of §5 (simulator commit, configs, SimPoint recipe, and power-model
> versions all pinned), against an LRU baseline *and* the strongest prior scheme
> under identical configurations, plus an iso-storage variant giving the baseline
> our 3.4KB as extra associativity. We report per-workload results with geomean
> and name our regressions. *(claim–instrument match, per `micro-experiments`)*

---

## What changed, beat by beat

| Beat | Before | After |
|---|---|---|
| Characterization | absent | 31% dead-resident capacity, measured, Fig. 1 promised |
| Insight | "uses a predictor" | one sentence: burst-then-silence predicts death |
| Mechanism | "lightweight" | 2048 × 12-bit table, 3.4KB/core, demand-triggered commitment |
| Accounting | "negligible overhead" | 3.4KB + <0.4% power + 1.1% worst regression, model versioned |
| Instrument honesty | "experiments show" | "in cycle-level simulation (ChampSim, ...)" |
| Baseline dignity | "outperforms LRU" | prior scheme re-implemented + iso-storage control + oracle bound |

> Next: measure your draft against the real award-validated shapes in
> [`../exemplars/library.md`](../exemplars/library.md), and the current-cycle rules
> in [`../official-source-map.md`](../official-source-map.md).
