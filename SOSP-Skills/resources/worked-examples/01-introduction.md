> **Illustrative teaching example.** The system, mechanism, workloads, and every number below are
> **fictional**, invented solely to demonstrate SOSP house style. No real-paper facts are stated
> and no venue policy is invented. Corresponding skills:
> [`sosp-writing-style`](../../skills/sosp-writing-style/SKILL.md),
> [`sosp-topic-selection`](../../skills/sosp-topic-selection/SKILL.md), and
> [`sosp-experiments`](../../skills/sosp-experiments/SKILL.md).

# Worked Example: A SOSP-Style Abstract + Introduction (before → after)

This demonstrates the **SOSP first-page arc** from `sosp-writing-style`:
**concrete problem → why existing systems fail structurally → the extractable principle → the
system embodying it → headline measured evidence with named baselines → honest scope** — written
so a PC member can restate the principle at the meeting without the paper open, and so every
claim already points at the experiment that will defend it.

The framing also reflects `sosp-topic-selection`: the contribution below is a *principle about
where a responsibility belongs in the stack*, embodied in a built system — not a 10% speedup,
not an unbuilt design, not a scale flex.

**Illustrative paper (fictional):** *"Ledger: Crash-Consistent Storage by Delegating Ordering to
the Allocator."* Fictional idea: file systems reconstruct write-ordering constraints that the
block allocator already knows; exposing allocation intents downward makes crash consistency a
property of allocation, shrinking the ordering points on the write path.

---

## Before (feature-list intro — typical systems first draft)

> **Abstract.** Storage performance is increasingly critical in modern datacenters. We present
> Ledger, a new storage system that supports crash consistency, high throughput, and low tail
> latency. Ledger uses a novel journaling design, an efficient allocation strategy, and a
> carefully engineered write path. Extensive experiments show that Ledger significantly
> outperforms existing systems on a wide range of workloads.
>
> **Introduction.** Crash consistency has been studied for decades. Many systems use journaling,
> copy-on-write, or soft updates. However, these approaches have various limitations. In this
> paper we present Ledger, which combines the best of these approaches with several
> optimizations. Ledger supports standard POSIX semantics, integrates with existing kernels, and
> is highly configurable. We describe Ledger's architecture, including its journaling module,
> allocator, and recovery module, and evaluate it extensively. Section 2 discusses background,
> Section 3 presents the design, ...

**What's wrong (against `sosp-writing-style` / `sosp-experiments`):**

- **No extractable principle.** "Novel journaling design + efficient allocation + careful
  engineering" is a feature list; nothing survives extraction to one repeatable sentence.
- **No structural gap.** "Various limitations" never says why journaling, CoW, and soft updates
  *cannot* be fixed in place — so the paper reads as one more point in a crowded space.
- **Unanchored superlatives.** "Significantly outperforms," "extensive experiments," "wide range
  of workloads" — every phrase is a target at the PC meeting, and none names a baseline, a
  workload, or a number (`sosp-experiments` would fail the claim map on page one).
- **The market-size opening.** "Increasingly critical in modern datacenters" spends the most
  valuable sentence in the paper saying nothing falsifiable.
- **Roadmap instead of argument**, and no owned limitation anywhere — the meeting will find one
  for you.

---

## After (SOSP arc — problem → structural gap → principle → system → evidence → scope)

> **Abstract.** File systems make crash consistency expensive because they enforce write
> ordering at the journal, after allocation has already fixed *where* data lands: on our traces,
> 61% of ordering stalls serialize writes whose blocks the allocator had already made
> order-independent. We show that crash consistency can be **delegated to the allocation layer**:
> if the allocator exposes *allocation intents* — promises about which blocks become reachable
> together — the file system can drop per-write ordering and recover by replaying intents.
> Ledger embodies this principle as a drop-in volume layer under two file systems. On
> write-heavy fileserver and key-value workloads, Ledger improves throughput by 1.8-2.4x over
> ordered journaling and cuts p99 write latency by 3.1x, while recovering in time proportional
> to unresolved intents rather than journal length. Ledger currently assumes single-volume
> deployments; cross-volume transactions fall back to ordered mode.
>
> **Introduction.** Every crash-consistent file system answers one question: which writes must
> be ordered so that a crash never exposes a state the file system cannot interpret? Journaling,
> copy-on-write, and soft updates answer it in the same place — at the write path — and pay the
> same cost: ordering points that serialize otherwise-independent I/O. The stall is structural,
> not an engineering artifact: by the time the write path sees a block, the allocator has
> already decided its placement and its reachability relations, and the write path must
> conservatively re-derive what the allocator knew. ...
>
> This paper's principle: **move crash consistency to the layer that creates the constraints.**
> The allocator, not the write path, knows which blocks become reachable together; exposing that
> knowledge as durable *allocation intents* lets ordering be enforced once, at allocation, and
> merely replayed at recovery. ... We built Ledger, a volume layer implementing intent
> delegation beneath unmodified ext4 and beneath our port of a log-structured file system
> (§4). ... Against ordered journaling and CoW baselines on the same kernel and hardware,
> Ledger sustains 1.8-2.4x higher throughput on write-heavy workloads (§6.2), holds p99 write
> latency 3.1x lower at equal offered load (§6.3), and bounds recovery by outstanding intents,
> not journal length (§6.5). Intent delegation is not free: cross-volume rename spans two
> allocators, and Ledger serializes it through the slower ordered path (§7 measures the cost).

**Why this works (the arc, move by move):**

| Arc move | Where it lands | The craft point |
| --- | --- | --- |
| Concrete problem | "61% of ordering stalls serialize writes..." | Opens with a *measured* motivating fact, not a market claim |
| Structural gap | "the write path must conservatively re-derive what the allocator knew" | Explains why existing designs cannot be patched — the gap is a property of layering |
| Principle | "move crash consistency to the layer that creates the constraints" | One sentence, no system name, repeatable at the PC meeting |
| Embodiment | Ledger under two file systems | Generality of the principle demonstrated by two hosts, not asserted |
| Evidence | 1.8-2.4x, p99 3.1x, recovery bound — each with a section pointer | Claims arrive pre-wired to the experiments that defend them (`sosp-experiments` claim map) |
| Honest scope | cross-volume falls back to ordered mode, cost measured in §7 | The limitation is volunteered *and* quantified — a footnote at the meeting, not its topic |

**Transfer checklist** (apply to your own draft): extract your principle with the system name
banned from the sentence; find your "61%" — the measured fact that makes the problem concrete;
make every headline number carry a baseline and a section pointer; and write the limitation
sentence yourself, with a measurement, before a reviewer writes it for you.
