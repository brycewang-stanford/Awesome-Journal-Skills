> **Illustrative teaching example.** The system, mechanism, numbers, and citations
> below are **fictional**, invented only to demonstrate how an ASPLOS first-two-pages
> should be built. No real-paper facts are stated and no venue policy is invented.
> Companion skills: [`asplos-writing-style`](../../skills/asplos-writing-style/SKILL.md),
> [`asplos-topic-selection`](../../skills/asplos-topic-selection/SKILL.md), and
> [`asplos-experiments`](../../skills/asplos-experiments/SKILL.md).

# Worked Example: Surviving the Two-Page Rapid Review (before → after)

ASPLOS 2027 screens every submission with a **rapid review round that reads only the
first two pages** (CFP, checked 2026-07-08). That mechanic dictates the rewrite below:
by the end of page two, a screener must know (a) the cross-layer problem, (b) the
insight that couples hardware and software, (c) the mechanism, and (d) the headline
evidence with its methodology class (simulator, FPGA, or real silicon) named honestly.

**Fictional paper:** *"TidalPage: Contention-Steered Superpage Management for
CXL-Tiered Memory."* Fictional premise: an OS page-placement policy co-designed with
a small hardware hint register, evaluated on real two-tier hardware plus a simulator
sweep.

---

## Before (a first draft that dies in rapid review)

> **Abstract.** Memory is increasingly important in modern computing. CXL is an
> exciting new technology that enables memory tiering, but it introduces performance
> challenges. We present TidalPage, a novel system for managing superpages in tiered
> memory. TidalPage uses a hardware/software co-design approach and achieves
> significant speedups over Linux on a variety of workloads. Our results demonstrate
> the effectiveness of our approach.
>
> **Introduction (opening).** In recent years, memory technologies have advanced
> rapidly... [one page of CXL background follows]. The rest of this paper is
> organized as follows: Section 2 provides background on CXL, Section 3 discusses
> related work, Section 4 presents the design of TidalPage...

**Why the screener stops reading:**

- The **insight is absent**. "Hardware/software co-design approach" is a category,
  not an idea; the two-page round exists precisely to filter category-only pitches.
- **No mechanism is named.** What does the hardware provide? What does the OS decide?
  A rapid reviewer cannot tell whether this is architecture, OS, or vapor.
- **Evidence class is hidden.** "Significant speedups on a variety of workloads"
  names no platform, no baseline, no workload suite — uncheckable and therefore
  discounted.
- **Page-two real estate is spent on background and a roadmap**, the two lowest-value
  uses under a two-page screen.
- The framing never claims the **intersection** — and the CFP says the rapid round
  prioritizes work at the architecture-languages-OS intersection.

---

## After (built for the two-page screen)

> **Abstract.** Superpages cut TLB pressure but bind 2 MB of data to one memory tier,
> and on CXL-tiered systems that binding is wrong whenever hot and cold lines share a
> superpage: the OS can only migrate what it can see, and it cannot see sub-superpage
> contention. TidalPage restores that visibility with a **32-entry per-controller
> hint register** that samples line-granularity access skew and exposes it to the OS
> as an architectural register, plus a **placement policy that splits, migrates, or
> re-fuses superpages** on tier-pressure epochs. The hint register costs no visible
> die area at our scale point; the policy is 2.1 kLOC in Linux 6.9. On a two-socket
> host with a CXL memory expander (real hardware, 14 workloads from SPEC CPU 2017 and
> a graph suite), TidalPage improves end-to-end runtime by a geometric-mean 1.18×
> over Linux's tiering with superpages enabled, and never regresses past 2%; a gem5
> sweep varying expander latency from 150-400 ns locates where the benefit saturates.
> *(problem → invisible-information insight → mechanism at each layer → evidence with
> platform, baseline, and workload named → honest sensitivity method.)*
>
> **Introduction, ¶1 (the friction).** Two OS decisions collide on tiered memory:
> superpage promotion, which trades address-translation cost for placement
> granularity, and page migration, which needs fine granularity to track hot data.
> Today's kernels resolve the collision by demoting superpages under memory pressure —
> paying translation cost to regain visibility the hardware had all along and threw
> away.
>
> **¶2 (the insight, stated as one sentence).** The information the OS lacks —
> which cache-line regions inside a superpage are contended — already passes through
> the memory controller on every access; the fix is not a smarter heuristic but a
> **narrow architectural channel** that lets the controller tell the OS what it saw.
>
> **¶3 (the mechanism, one paragraph per layer).** Hardware: a sampling hint register
> file per controller, read as an architectural register, with an update rule that
> survives virtualization. OS: an epoch-driven policy consuming the hints to split,
> migrate, or re-fuse; policy decisions are exposed to userspace as advisory counters
> so runtimes can adapt. Interface: two instructions and one sysfs surface, specified
> in §3.4 so others can implement against it.
>
> **¶4 (the evidence contract).** Claims and where each is tested: end-to-end benefit
> on real silicon (§6.2); attribution via a no-hint ablation that isolates the
> register's contribution from the policy's (§6.4); generality via the gem5 latency
> sweep with simulator configuration and its cycle-accuracy limits stated (§6.5);
> overheads measured where the design does not help (§6.6).
>
> **¶5 (why this venue).** The contribution is the boundary itself: neither the
> register without the policy nor the policy without the register improves anything —
> an architecture-OS co-design in the sense the rapid review prioritizes.

---

## What moved, and why it maps to the skills

| Change | Skill rule it satisfies |
| --- | --- |
| Insight compressed to one sentence in ¶2 | `asplos-writing-style`: the idea must be quotable by a screener |
| Mechanism split into per-layer paragraphs | `asplos-writing-style`: each layer's contribution auditable separately |
| Platform, baseline, workloads named in the abstract | `asplos-experiments`: evidence class up front — real hardware vs simulator |
| Ablation promised where the credit is claimed | `asplos-experiments`: attribution before magnitude |
| gem5 sweep labeled with its accuracy limits | `asplos-reproducibility`: cycle-accuracy caveats are stated, not implied |
| "Never regresses past 2%" | `asplos-writing-style`: bounded honesty beats unbounded praise |
| Intersection claim made explicit in ¶5 | `asplos-topic-selection`: the deletion test passed in print |

> Next: study real award-validated first pages via
> [`../exemplars/library.md`](../exemplars/library.md), and confirm current-cycle
> mechanics in [`../official-source-map.md`](../official-source-map.md) before
> applying any date or cap mentioned here.
