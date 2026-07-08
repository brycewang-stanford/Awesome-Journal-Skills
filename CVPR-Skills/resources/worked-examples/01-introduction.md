> **Illustrative teaching example.** The paper, method, datasets-as-used, and every
> number below are **fictional**, invented solely to demonstrate CVPR first-page craft.
> No real results are quoted and no venue policy is invented. Companion skills:
> [`cvpr-writing-style`](../../skills/cvpr-writing-style/SKILL.md),
> [`cvpr-experiments`](../../skills/cvpr-experiments/SKILL.md), and
> [`cvpr-topic-selection`](../../skills/cvpr-topic-selection/SKILL.md).

# Worked Example: A CVPR-Style Abstract + Introduction (before → after)

CVPR's first page is read twice: once in a 90-second figure-and-abstract flip by an
overloaded reviewer from a 25,000-person pool, and once carefully if the flip goes
well. The rewrite below shows the moves that survive both reads — a nameable mechanism,
scoped numeric claims, matched-baseline honesty, a stated failure mode, and a teaser
figure treated as part of the argument.

**Fictional paper:** *"EchoTrack: Persistent Multi-Object Tracking by Re-Sounding
Dormant Tracks."* Fictional method: a tracker that keeps low-confidence "dormant"
tracks alive in a memory bank and re-activates them by appearance matching, targeting
long occlusions.

---

## Before (a first draft that dies in the flip)

> **Abstract.** Multi-object tracking is a fundamental problem in computer vision with
> many important applications such as autonomous driving and surveillance. Recently,
> deep learning has led to remarkable progress in this area. However, existing methods
> still struggle in complex scenarios. In this paper, we propose EchoTrack, a novel
> tracking framework that achieves state-of-the-art performance. Extensive experiments
> demonstrate the effectiveness of our approach.
>
> **Introduction.** Tracking has attracted increasing attention in recent years… (one
> paragraph of application boilerplate) … Many methods have been proposed, including
> tracking-by-detection and end-to-end paradigms… (a citation flood with no deltas) …
> Our contributions are: (1) we propose a novel framework; (2) we design an effective
> module; (3) extensive experiments show our method outperforms state-of-the-art
> methods on several benchmarks.

**Why the flip kills it** (mapped to the skills):

- **No mechanism anywhere.** "Novel framework," "effective module" — a reviewer cannot
  tell what was built (`cvpr-writing-style`: the table is the adjective; the mechanism
  is the contribution).
- **Unscoped superlatives.** "State-of-the-art" with no dataset, protocol, or backbone
  scope — precisely the claim shape `cvpr-writing-style` bans, and easy to falsify at
  a benchmark venue.
- **"Complex scenarios"** names no failure mode, so the paper promises nothing
  checkable (`cvpr-experiments`: when does it fail?).
- **Contribution bullets are content-free** — they would fit any tracking paper ever
  submitted; at 16k submissions, generic bullets are triage death.
- **No teaser thinking.** Nothing on page 1 tells the flip reader what image to hold
  in mind.

---

## After (built for the two-pass reader)

> **Abstract.** Multi-object trackers lose identity during long occlusions: when a
> pedestrian disappears behind a bus for 60 frames, association-by-motion decays and
> the track is terminated, splitting one identity into two. We present **EchoTrack**,
> which never hard-terminates: low-confidence tracks become **dormant memories** —
> appearance embeddings with an uncertainty-widened motion prior — and detections that
> match no active track are tested against dormant ones before spawning new
> identities. On the fictional LongOcc benchmark, EchoTrack improves IDF1 by 3.2 over
> the strongest memory-based baseline under **identical detections and backbone**, with
> the gain concentrated on occlusions longer than 40 frames (+7.9 IDF1) and a 4%
> runtime overhead (11.2 ms/frame, single A100). Under heavy appearance change
> (clothing swap, re-entry after minutes) dormant matching degrades toward the
> baseline, which we quantify. Code, configs, and the occlusion-length evaluation split
> will be released.
>
> **Introduction, ¶1 (problem as a picture).** Figure 1 shows a 90-frame sequence: a
> cyclist enters an underpass at frame 20 and exits at frame 81. The leading
> tracker-by-detection issues identity 7 at entry and identity 31 at exit; EchoTrack
> re-sounds identity 7. The failure is not detection — the cyclist is found in every
> visible frame — it is the **policy of terminating uncertain tracks**.
>
> **¶2 (why existing remedies fall short, each with a named reason).** Motion-only
> memories (Kalman-style) widen until they match everything, so persistent trackers cap
> memory at short horizons. Appearance re-identification banks help, but existing ones
> gate on high-confidence re-entry detections, which occlusion exits rarely provide.
> End-to-end query trackers carry identity implicitly, but their memory is
> temporally bounded by training-clip length. *(three lanes, three mechanisms, three
> deltas — the `cvpr-related-work` pattern compressed.)*
>
> **¶3 (the mechanism, stated so it can be ablated).** EchoTrack contributes one policy
> and two components: (i) dormancy instead of termination; (ii) an uncertainty-widened
> motion prior that *shrinks* the matching gate as dormancy ages, inverting the usual
> widening; (iii) a two-stage association that tries dormant matches only for
> detections orphaned by active association. Each maps to one ablation row in Table 3.
>
> **¶4 (evidence, scoped).** Under identical detections and backbone across all
> compared methods, EchoTrack improves IDF1 on three benchmarks, with gains growing
> monotonically in occlusion length; it adds 4% latency; and it fails predictably under
> appearance change, which Figure 6 shows and Section 5.3 measures. *(claims wear their
> scope; the failure mode is a section, not a secret — `cvpr-experiments`.)*

---

## The moves, itemized

| Draft symptom | Rewrite move | Skill |
| --- | --- | --- |
| "Novel framework" | Name the policy: dormancy instead of termination | `cvpr-writing-style` |
| "State-of-the-art" | "+3.2 IDF1, identical detections and backbone" | `cvpr-experiments` (matched-compute fairness) |
| "Complex scenarios" | "occlusions ≥ 40 frames: +7.9" — checkable scope | `cvpr-writing-style` claim calibration |
| Hidden costs | "4% overhead, 11.2 ms/frame, single A100" | CRF-aligned efficiency honesty |
| No failure story | Appearance-change degradation quantified up front | `cvpr-experiments` failure taxonomy |
| Citation flood | Three lanes with per-lane mechanism deltas | `cvpr-related-work` |
| Decorative Figure 1 | Teaser that states the problem and the win on one input | `cvpr-writing-style` flip test |

> Next: study how real CVPR first pages execute these moves in
> [`../exemplars/library.md`](../exemplars/library.md) (metadata-verified papers), and
> check every policy assumption against [`../official-source-map.md`](../official-source-map.md)
> before submission week.
