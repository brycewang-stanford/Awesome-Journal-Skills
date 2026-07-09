> **Illustrative teaching example.** The tool, benchmarks, and every number below are **fictional**
> and exist only to demonstrate TACAS house style. No real-paper facts, tools, or results are
> stated, and no policy is invented. Corresponding skills:
> [`tacas-writing-style`](../../skills/tacas-writing-style/SKILL.md),
> [`tacas-topic-selection`](../../skills/tacas-topic-selection/SKILL.md), and
> [`tacas-experiments`](../../skills/tacas-experiments/SKILL.md).

# Worked Example: A TACAS Tool-Paper Introduction (before → after)

This demonstrates the **TACAS regular-tool-paper first-page arc** from `tacas-writing-style`:
**problem in constructing or analysing a system → why existing tools fall short → what the tool
does and how it works → honest evidence on shared benchmarks → availability and reproducibility**.
Because tool papers are **single-blind** at TACAS and carry a **mandatory artifact** that is
evaluated with the PC, the introduction should name the tool, state where it can be obtained, and
promise exactly the evidence the artifact will let a reviewer reproduce.

The framing also reflects `tacas-topic-selection`: a **regular tool** paper (≤16 pages) is the
right category when the contribution is a usable, evaluated tool realizing a sound technique — as
opposed to a **tool-demonstration** paper (≤6 pages) for a mature tool shown in use, a **research**
paper for a new algorithm, or a **case-study** paper for applying existing methods to a substantial
real system. If the heart is a new decision procedure with a correctness proof and no tool, it is a
research paper; if it is a benchmark ranking of verifiers, it belongs in **SV-COMP**, not a tool
paper.

**Illustrative tool (fictional):** *"RelChk: A Bounded Refinement Checker for Concurrent Data
Structures."* Fictional artifact: a checker that, given a concurrent data-structure implementation
and a sequential specification, searches for a linearizability violation up to a bound, packaged as
a VM image with a benchmark harness.

---

## Before (buries the tool and the evidence — typical first-draft introduction)

> **Introduction.** Concurrency is hard and bugs are everywhere. Verifying concurrent software is
> an important and challenging problem that has received much attention. In this paper we propose a
> novel approach based on a new encoding and clever optimizations, and we show that it is very
> efficient and outperforms existing approaches on a range of benchmarks. Our results demonstrate
> the effectiveness of the approach. Section 2 gives preliminaries, Section 3 the approach,
> Section 4 the evaluation, and Section 5 concludes.

**What's wrong (against `tacas-writing-style` / `tacas-topic-selection` / `tacas-experiments`):**

- **No concrete problem and no tool on the first page** — it opens with "concurrency is hard," not
  with the specific analysis problem (bounded linearizability checking) or the named tool. A TACAS
  reader wants to know within a paragraph what the tool takes in, what it decides, and how.
- **"Novel," "clever," "very efficient" without content** — TACAS reviewers are verification
  experts; adjectives where an algorithm and a soundness statement belong read as hand-waving.
- **No availability or reproducibility posture** — a tool paper that never mentions an artifact,
  benchmarks, or a way to run it ignores that the **artifact is mandatory and gates acceptance**.
- **Unfair-comparison smell** — "outperforms existing approaches" with no named baselines, no
  common benchmark set, and no statement of what "outperforms" measures invites the reviewer's
  first objection.
- **Wrong-category risk** — if the real contribution is a new algorithm with a proof, this should
  be framed as a research paper; if it is a ranking of tools, it is SV-COMP. The draft hides which.

---

## After (TACAS tool-paper arc — problem → gap → tool + method → benchmark evidence → availability)

> **Introduction.** *(¶1 — the specific analysis problem, first breath.)* Linearizability is the
> standard correctness criterion for concurrent data structures, but checking it is expensive:
> exhaustive methods explore all interleavings and do not scale past small clients, while testing
> finds bugs only by luck. The practical question for a data-structure developer is concrete: given
> an implementation and a sequential specification, **can a tool automatically find a
> linearizability violation, up to a stated bound, fast enough to sit in a test loop?**
>
> *(¶2 — why existing tools fall short.)* Existing checkers either require a hand-written
> linearization-point annotation — which is exactly what a developer gets wrong — or enumerate
> histories with no reduction, so they time out on realistic client programs. Neither gives a
> **bounded, annotation-free** answer with a concrete counterexample a developer can replay.
>
> *(¶3 — the tool and how it works, stated as a mechanism.)* We present **RelChk**, a bounded
> refinement checker. RelChk encodes "some interleaving of the implementation has no matching
> sequential history up to bound *k*" as a set of SMT constraints, discharges them with an
> off-the-shelf solver, and reports a concrete violating history when one exists. The encoding is
> **sound and complete up to the bound** (Section 3), needs **no linearization-point annotations**,
> and returns a replayable counterexample, not just "unsafe."
>
> *(¶4 — honest evidence on shared benchmarks.)* We evaluate RelChk on a suite of concurrent
> data-structure benchmarks drawn from the literature and prior tool distributions (Section 4),
> against the strongest annotation-free checker we could configure, each given an **equal time
> budget on the same machine**. We report solved/unsolved counts, per-benchmark wall-clock time
> with the hardware stated, and the bound reached — not a single headline ratio. Where RelChk is
> slower, we say so and explain why.
>
> *(¶5 — availability and reproducibility.)* RelChk and every benchmark, script, and expected output
> are provided as the paper's **artifact**, packaged to run on the ETAPS evaluation VM without
> network access; we target the **Available**, **Functional**, and **Reusable** badges. Section 2
> gives the concurrency background; Section 3 the encoding and its bounded-soundness argument;
> Section 4 the evaluation; Section 5 related tools; Section 6 concludes. *(brief roadmap.)*

---

## Why the "after" meets the TACAS bar

Mapped to the skill checklists:

- **Problem and tool on the first page** — ¶1-¶3 name the analysis problem, the tool, and the
  mechanism (an SMT encoding with bounded soundness) before any adjective
  (`tacas-writing-style`: "lead with what the tool does and how").
- **Right category, made explicit** — it is framed as a **regular tool** paper: a runnable,
  evaluated tool realizing a technique, distinct from a research paper (algorithm+proof) or an
  SV-COMP ranking (`tacas-topic-selection`).
- **Soundness stated, not implied** — "sound and complete up to the bound" with a forward pointer
  to the argument is the claim shape TACAS reviewers check first (`tacas-writing-style`).
- **Fair, reproducible evaluation** — named baseline, shared benchmarks, equal time budget, stated
  hardware, honest reporting of where the tool loses (`tacas-experiments`: match evidence to the
  claim and never show an untuned baseline).
- **Availability and badges up front** — the artifact, its clean-VM packaging, and the target
  badges appear in the introduction, matching the **mandatory** tool-paper artifact that is
  evaluated with the PC (`tacas-artifact-evaluation`, `tacas-reproducibility`).
- **Single-blind, so named** — because a tool paper is single-blind, RelChk and its authors are
  named; contrast a **regular research** paper, which would be anonymized (`tacas-submission`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified TACAS
> tool and research papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for TACAS categories, page limits, the
> blind model, and the artifact/badge policy.
