> **Illustrative teaching example.** The paper, tool, benchmarks, and every number below are
> **fictional** and exist only to demonstrate CAV house style. No real-paper facts, tools, or
> results are stated, and no policy is invented. Corresponding skills:
> [`cav-writing-style`](../../skills/cav-writing-style/SKILL.md),
> [`cav-topic-selection`](../../skills/cav-topic-selection/SKILL.md), and
> [`cav-experiments`](../../skills/cav-experiments/SKILL.md).

# Worked Example: A CAV-Style Abstract + Introduction (before → after)

This demonstrates the **CAV first-page arc** from `cav-writing-style`:
**verification problem → why current methods fall short → contribution (technique and/or tool) →
what is formally guaranteed → evidence on standard benchmarks → scope and limits** — with the CAV
expectations that the contribution is a *verification* contribution, soundness/completeness is
stated precisely, and the empirical comparison is fair (pinned tool versions, resource limits, the
right benchmark set).

The framing also reflects `cav-topic-selection`: CAV is strongest when the contribution advances
**how we prove properties of hardware, software, or systems** — here, a faster decision procedure
for a verification query — rather than a machine-learning result whose verification angle is
incidental (which would route elsewhere), and when the paper could not simply be re-labeled as a
TACAS tool paper or a VMCAI technique note without loss.

**Illustrative paper (fictional):** *"Lazy Lemma Sharing for Portfolio SMT Solving of Bit-Vector
Queries."* Fictional tool: a portfolio SMT engine that shares learned lemmas across solver
instances, evaluated on standard bit-vector benchmarks.

---

## Before (buries the verification contribution — typical first-draft abstract + intro)

> **Abstract.** SMT solvers are important for verification. We present a new portfolio solver that
> runs several engines in parallel and is faster than existing solvers. Our tool achieves great
> results on many benchmarks and shows the promise of parallel solving for verification.
>
> **Introduction.** Formal verification is widely used. SMT solvers are a key backend. Many solvers
> exist, but they can be slow. In this paper we build a portfolio solver that runs multiple engines
> and picks the fastest answer, and we evaluate it on benchmarks, showing strong results. Section 2
> covers background, Section 3 our tool, Section 4 experiments, and Section 5 concludes.

**What's wrong (against `cav-writing-style` / `cav-topic-selection` / `cav-experiments`):**

- **No precise verification claim on the first page** — it leads with "faster" and "great results,"
  not with *what problem is solved* or *what is guaranteed*. CAV wants the verification contribution
  and its formal content up front.
- **No soundness statement.** A portfolio solver that shares lemmas must argue the shared lemmas are
  sound across engines; the draft never says the answers stay correct.
- **Unfalsifiable evidence.** "Many benchmarks," "strong results" — no benchmark set revision, no
  baseline solver versions, no resource limits (timeout/memory), so no reviewer can trust or
  reproduce the comparison.
- **Tool-as-magic.** "Runs several engines and picks the fastest" describes plumbing, not a
  contribution; the actual idea (sound cross-engine lemma sharing) is hidden.
- **Category confusion.** Framed this way it reads like a thin TACAS-style tool note; the `re-label`
  test in `cav-topic-selection` is failing.
- **Over-signposted roadmap** substituting for an argument.

---

## After (CAV arc — problem → inadequacy → contribution → guarantee → benchmark evidence → scope)

> **Abstract.** Portfolio SMT solvers gain speed by running independent engines in parallel, but
> they discard the search knowledge each engine learns, so the parallel instances re-derive the
> same lemmas. We present **lazy lemma sharing**, a method that exchanges learned bit-vector lemmas
> across portfolio engines **without compromising soundness**: shared lemmas are replayed only when
> an engine can re-derive them under its own theory reasoning, which we prove preserves
> equisatisfiability (Thm. 1). We implement the method in a portfolio engine and evaluate it on the
> standard bit-vector benchmark division (fixed revision, stated in the artifact) against the latest
> released versions of two widely used solvers, under a uniform 20-minute / 8-GB per-instance limit
> on identical hardware. On this set the method solves a nontrivial number of previously timed-out
> instances and reduces mean solving time on commonly solved instances; every run, including the
> full per-instance table and the sharing logs, is in the artifact. *(problem → inadequacy →
> technique → guarantee → fair benchmark evidence → reproducibility — all on the first page.)*
>
> **Introduction.** *(¶1 — the verification problem, first breath.)* Bit-vector reasoning is the
> backend of hardware and low-level software verification, and portfolio solving is the standard way
> to buy wall-clock speed on hard queries. Yet each engine in a portfolio learns lemmas — clauses
> that prune its search — and throws them away at the process boundary, so an N-engine portfolio
> often does close to N times the redundant learning. The question is whether that learning can be
> **shared soundly**, given that engines use different internal theory reasoning.
>
> *(¶2 — why the current state is inadequate.)* Existing portfolios parallelize at the query level
> (fastest engine wins) or share only propositional clauses, which are unsound to import directly
> when engines disagree on theory lemmas. Neither exploits theory-level lemmas, and ad hoc sharing
> risks importing a lemma that is valid in one engine's encoding but not another's — an **unsoundness
> bug**, the one failure a verification tool cannot have.
>
> *(¶3 — contribution, stated as verification claims.)* We contribute (i) **lazy lemma sharing**, a
> protocol in which a shared bit-vector lemma is admitted by a receiving engine only after it
> re-derives the lemma under its own theory solver, and (ii) a proof that the protocol preserves
> equisatisfiability, so the portfolio's verdict is exactly the verdict of any single sound engine
> (Thm. 1). The contribution is a technique with a guarantee, not a scheduling heuristic.
>
> *(¶4 — evidence on standard benchmarks, each claim paired.)* We tie every claim to evidence: the
> soundness claim to Theorem 1 and to a differential check against a trusted solver on all SAT/UNSAT
> verdicts (no disagreements); the speed claim to the fixed-revision bit-vector benchmark division,
> run against pinned baseline versions under a uniform resource limit on stated hardware, with the
> full per-instance results, seeds, and sharing logs in the artifact.
>
> *(¶5 — scope and limits, and what changes for verification.)* We state the limits plainly: the
> method targets bit-vector logic and shows no benefit on theories where lemma re-derivation is as
> expensive as the original solve; the gain also shrinks past eight engines as sharing overhead
> grows. The payoff is concrete: portfolio solvers can convert redundant parallel learning into
> shared progress **without a soundness risk**. Section 2 gives background on portfolio SMT and
> bit-vector lemmas; Section 3 the protocol and proof; Section 4 the evaluation; limits are argued
> alongside each result, not deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the CAV bar

Mapped to the skill checklists:

- **Verification contribution on the first page** — the abstract and ¶1 pose a solving problem and
  name the guarantee (equisatisfiability) before any engineering detail (`cav-writing-style`: "lead
  with the verification contribution and its formal content").
- **Soundness stated and checked** — the central claim is a preserved-correctness theorem, backed by
  a differential check, not a benchmark score alone (`cav-experiments`: a soundness claim ships a
  proof and/or a checkable witness).
- **Fair, reproducible benchmark evidence** — fixed benchmark revision, pinned baseline versions,
  uniform time/memory limits, stated hardware, and per-instance data in the artifact pre-empt the
  reviewer's first objection (`cav-experiments`, `cav-reproducibility`).
- **Right venue and category, re-label test passes** — a technique *with a proof* implemented in a
  tool is a CAV Regular Paper; stripped of the theorem it would be a thin tool note, so the
  `cav-topic-selection` re-label test is satisfied.
- **Scope and limits explicit** — the logic restriction and the eight-engine ceiling are stated as
  the paper's own boundaries, the CAV norm of not over-claiming generality (`cav-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified CAV
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for CAV-specific submission policy and the
> LNCS / two-stage-review / AEC cycle.
