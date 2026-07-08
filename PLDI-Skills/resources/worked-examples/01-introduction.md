> **Illustrative teaching example.** The system, language, benchmarks, and every
> number below are **fictional**, invented only to demonstrate PLDI house style. No
> real-paper results are reproduced and no venue policy is invented here — policy
> lives in [`../official-source-map.md`](../official-source-map.md). Companion
> skills: [`pldi-writing-style`](../../skills/pldi-writing-style/SKILL.md),
> [`pldi-experiments`](../../skills/pldi-experiments/SKILL.md), and
> [`pldi-topic-selection`](../../skills/pldi-topic-selection/SKILL.md).

# Worked Example: A PLDI-Style Abstract + Introduction (before → after)

PLDI's first page must convince an implementor-reviewer of three things at once:
the **design insight** (what new thing the language/compiler/analysis does and why
that was hard), the **implementation reality** (it exists, in a real toolchain, on
real programs), and the **evaluation honesty** (numbers with baselines, variance,
and stated limits — the SIGPLAN Empirical Evaluation Guidelines lens). A first page
that reads like a pure theory pitch drifts toward POPL; one that reads like a
product announcement gets audited to death.

**Fictional running paper:** *"Sift: Region-Aware Escape Analysis for Ahead-of-Time
Compiled Closures."* Fictional claim: a compositional escape analysis that lets an
AOT functional-language compiler stack-allocate most closures without whole-program
analysis.

---

## Before (product-announcement first draft)

> **Abstract.** Functional languages are increasingly popular but suffer from heap
> allocation overhead. We present Sift, a new escape analysis that is fast and
> precise. Sift is implemented in our compiler and achieves significant speedups on
> a wide range of benchmarks, outperforming existing approaches. We believe Sift
> will be useful to many compiler writers.
>
> **Introduction.** Memory management is a classic problem. Many analyses have been
> proposed, but they are either slow or imprecise. We designed Sift to be both fast
> and precise. Our contributions are: (1) the Sift analysis; (2) an implementation;
> (3) an evaluation showing Sift is better. The rest of this paper is organized as
> follows...

**What fails, in PLDI terms:**

- **No technical insight is stated.** "Fast and precise" is a wish, not a
  mechanism. The reviewer cannot tell what Sift *does* that prior escape analyses
  cannot, so novelty defaults to "unclear."
- **The hard case is hidden.** Closures capturing mutable environments across
  module boundaries — the actual difficulty — never appears on page one.
- **"Significant speedups on a wide range of benchmarks"** names no suite, no
  baseline compiler, no variance treatment — an immediate Empirical Evaluation
  Guidelines flag (unclear claim, no principled benchmark choice).
- **No compositionality story**, though that is the load-bearing design property.
- **"We believe it will be useful"** is advocacy; PLDI wants evidence.

---

## After (design insight → mechanism → measured claim)

> **Abstract.** Ahead-of-time compilers for functional languages heap-allocate
> closures conservatively because a closure's escape behavior depends on callers
> the compiler cannot see. We present **Sift**, a region-aware escape analysis that
> is **compositional**: each module is summarized by a polymorphic escape signature,
> so no whole-program pass is required and separate compilation is preserved. The
> key idea is to type closure environments with *region capabilities* that record
> the outermost frame a captured variable may outlive; signatures compose by
> capability subsumption. We implemented Sift in an AOT compiler for a
> Standard-ML-like language and evaluated it on a 14-program suite spanning
> parsers, provers, and web servers. Sift stack-allocates a majority of dynamic
> closure allocations on 11 of 14 programs, yielding geometric-mean end-to-end
> speedups of 1.17x (95% CI over 30 runs after warmup) against our baseline
> compiler with the prior flow-based analysis, at under 3% added compile time.
> Sift is unsound for programs using first-class continuations, which we detect
> and exclude conservatively.
>
> **Introduction.** *(¶1 — the hard case, concretely.)* A closure must be
> heap-allocated exactly when its environment outlives its allocating frame. For
> first-order locals this is a solved analysis problem; the difficulty is a
> closure that captures a mutable environment and is passed to *unknown* callers
> in separately compiled modules. Existing analyses either assume the whole
> program is visible — surrendering separate compilation — or degrade to
> allocating every escaping-typed closure on the heap.
>
> *(¶2 — the mechanism, one paragraph, no forward references.)* Sift types each
> captured variable with a region capability naming the outermost stack frame it
> may outlive. A module exports, per function, a polymorphic escape signature over
> these capabilities; call sites instantiate signatures, and composition is
> capability subsumption. The analysis therefore runs module-locally and its
> precision is limited only by signature polymorphism, not by call-graph
> visibility. *(the design insight is a sentence a compiler writer can act on)*
>
> *(¶3 — implementation reality.)* We implemented Sift as a middle-end pass in a
> real AOT toolchain, including the interactions that make escape analysis
> delicate in practice: exceptions, mutable references, and tail calls. The
> implementation, benchmark harness, and raw measurements are packaged as an
> artifact intended for the Functional, Reusable, and Available badges.
>
> *(¶4 — measured claims, each with its evidence address.)* On a 14-program suite
> chosen to cover allocation-heavy and control-heavy workloads (§6.1 justifies the
> suite), Sift converts a majority of dynamic closure allocations to stack
> allocation on 11 programs (Table 3), producing a 1.17x geometric-mean speedup
> over the flow-based baseline — reported as means over 30 post-warmup runs with
> 95% confidence intervals, on two microarchitectures (§6.3). Compile-time
> overhead stays under 3% (Table 5). Programs using first-class continuations are
> conservatively rejected by a check we prove sound (§5, Theorem 2).
>
> *(¶5 — contributions as falsifiable claims.)* We contribute: a region-capability
> type discipline for closure environments (§4); a compositional analysis with a
> soundness proof modulo the stated continuation restriction (§5); and an
> implementation plus evaluation showing the precision/compile-time trade-off
> (§6), with an artifact supporting independent replication.

---

## Why the "after" clears the PLDI bar

| First-page property | Where the "after" delivers it |
| --- | --- |
| Hard case stated before the solution | ¶1: unknown callers under separate compilation |
| Mechanism, not adjectives | ¶2: region capabilities + signature subsumption |
| Implementation reality | ¶3: real toolchain, exceptions/refs/tail calls handled |
| Benchmark rigor | ¶4: suite justification, warmup, 30 runs, CIs, two machines |
| Honest limits | Abstract + ¶4: continuation unsoundness stated, detected, proved excluded |
| Artifact culture | ¶3: badge-ready artifact planned at submission time |

Note what the rewrite did **not** do: it never claims generality beyond the suite,
never buries the continuation caveat in Section 7, and never cites wall-clock wins
without a variance treatment — the three most common PLDI evaluation objections.

> Next: study real first pages in [`../exemplars/library.md`](../exemplars/library.md)
> (all venue-verified), then check current-cycle mechanics in
> [`../official-source-map.md`](../official-source-map.md) before formatting.
