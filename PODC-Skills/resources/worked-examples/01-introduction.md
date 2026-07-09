> **Illustrative teaching example.** The paper, model, theorem, and every bound below are
> **fictional** and exist only to demonstrate PODC house style. No real-paper facts, results, or
> constants are stated, and no policy is invented. Corresponding skills:
> [`podc-writing-style`](../../skills/podc-writing-style/SKILL.md),
> [`podc-topic-selection`](../../skills/podc-topic-selection/SKILL.md), and
> [`podc-experiments`](../../skills/podc-experiments/SKILL.md).

# Worked Example: A PODC-Style Abstract + Introduction (before → after)

This demonstrates the **PODC first-page arc** from `podc-writing-style`:
**problem in a precisely stated model → why the state of the art leaves a gap → the result
(algorithm and/or bound) stated up front → the cost measure and matching lower bound → the proof
idea in one breath** — with the PODC expectations that the **model box** (network, timing, faults,
adversary, cost measure) is fixed before any theorem, the result is stated as a **theorem with a
tight bound**, and the **proof technique** is named rather than deferred.

The framing also reflects `podc-topic-selection`: PODC is strongest when the contribution is a
**provable guarantee in a distributed model** — round/message/space complexity, an impossibility, or
a matching bound — rather than a measured system (which routes to a systems venue) or a sequential
algorithm (which routes to STOC/SODA), and when the result could not simply be re-labeled as a DISC,
SPAA, or PODS paper without loss.

**Illustrative paper (fictional):** *"Sublinear-Message Byzantine Agreement under Partial Synchrony
with an Adaptive Adversary."* Fictional result: a randomized agreement protocol whose message
complexity beats the prior bound, plus a matching lower bound showing it is optimal.

---

## Before (buries the model and the bound — typical first-draft abstract + intro)

> **Abstract.** Byzantine agreement is a central problem in distributed computing and blockchains.
> We propose a new, efficient protocol that tolerates faults and uses fewer messages than previous
> approaches. Experiments on a simulator show our protocol scales well and outperforms baselines,
> demonstrating its practicality for large-scale systems.
>
> **Introduction.** Distributed systems must agree despite failures. Many protocols exist, but they
> are expensive. In this paper we present a new protocol that is more efficient, and we evaluate it
> in simulation, showing strong results. Section 2 covers related work, Section 3 our protocol,
> Section 4 experiments, and Section 5 concludes.

**What's wrong (against `podc-writing-style` / `podc-topic-selection` / `podc-experiments`):**

- **No model box.** "Tolerates faults" hides the questions that decide correctness: crash or
  Byzantine? synchronous, asynchronous, or partial synchrony? adaptive or oblivious adversary? What
  fraction of faults? At PODC these are not details — they *are* the theorem.
- **No stated bound.** "Fewer messages" is not a result; PODC wants a **theorem** with an explicit
  message-complexity expression and the resilience it holds at.
- **Simulation stands in for a proof.** A PODC agreement claim is established by a **proof of
  agreement, validity, and termination**, not by a scaling plot. The plot is at best optional.
- **No optimality claim.** The paper never asks whether its bound is *tight* — the matching lower
  bound that would make it a PODC-grade result is absent from the first page.
- **Wrong-venue smell.** "Practicality for large-scale systems" with a simulator reads as an
  ICDCS/DSN framing; the PODC contribution (a bound and its optimality) is buried.
- **Over-signposted roadmap** substituting for a result statement.

---

## After (PODC arc — model → gap → result → tight bound → proof idea)

> **Abstract.** We study **Byzantine agreement in the partially synchronous message-passing model**
> with an **adaptive** adversary controlling up to *t < n/3* parties. The best prior protocols in
> this setting use a superlinear number of messages per party in the worst case. We present a
> randomized protocol that reaches agreement with **O(f(n)) messages** in expectation (for the
> explicit f stated in Theorem 1), tolerating the optimal *t < n/3* Byzantine faults and terminating
> with probability 1. We complement it with a **matching Ω(f(n)) lower bound** (Theorem 2) showing no
> protocol in this model does asymptotically better, so our message complexity is **optimal**. The
> upper bound uses a committee-sampling argument robust to adaptive corruption; the lower bound uses
> an indistinguishability argument over adversary strategies. *(model → gap → upper bound → matching
> lower bound → proof technique — all on the first page.)*
>
> **Introduction.** *(¶1 — the problem inside a fixed model, first breath.)* We work in the
> **partially synchronous** model: messages are eventually delivered within an unknown bound after an
> unknown global stabilization time. *n* parties communicate by point-to-point messages; up to *t* of
> them are **Byzantine**, chosen **adaptively** by an adversary that observes the execution. We
> measure **message complexity**: the expected total number of messages sent. The question is how few
> messages suffice for Byzantine agreement in this model, and whether the answer is tight.
>
> *(¶2 — why the state of the art leaves a gap.)* Protocols optimized for the synchronous model do
> not preserve their message bounds under partial synchrony, and protocols hardened against an
> adaptive adversary have paid for it in messages. No prior protocol simultaneously (i) tolerates the
> optimal *t < n/3*, (ii) withstands an *adaptive* adversary, and (iii) achieves a message complexity
> that is known to be optimal — leaving open whether the adaptive-adversary penalty is fundamental.
>
> *(¶3 — the result, stated as theorems.)* We resolve this. **Theorem 1 (upper bound):** a randomized
> protocol achieving agreement, validity, and almost-sure termination with the stated expected
> message complexity at *t < n/3* against an adaptive adversary. **Theorem 2 (lower bound):** every
> such protocol must send Ω(f(n)) messages in expectation, so Theorem 1 is optimal up to constants.
>
> *(¶4 — the cost measure and why the bound is tight.)* The two theorems meet: the upper bound's
> committee sampling sends few messages precisely because committees are small, and the lower bound
> shows any protocol sending fewer cannot distinguish an agreeing execution from a disagreeing one
> under adaptive corruption. We state the model assumptions the lower bound needs explicitly, so the
> optimality claim is auditable rather than asymptotic hand-waving.
>
> *(¶5 — proof idea and what it buys the field.)* The upper bound's technical core is a
> committee-election subprotocol whose committees stay honest-majority even as the adversary corrupts
> reactively; the lower bound is a valency/indistinguishability argument over the adversary's
> corruption schedule. The payoff is a **fundamental limit**: the adaptive-adversary penalty for
> partially synchronous agreement is now pinned down. Section 2 fixes notation and the model;
> Section 3 gives the protocol and its proof; Section 4 the lower bound; full proofs are in the
> appendix of the full version. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the PODC bar

Mapped to the skill checklists:

- **Model box before any theorem** — the abstract and ¶1 fix network, timing, fault type, adversary,
  and cost measure before stating a bound, so "tolerates faults" can never be ambiguous
  (`podc-writing-style`: state the model first).
- **Result as a theorem with a tight bound** — an explicit expected message complexity *and* a
  matching lower bound, not "fewer messages" (`podc-experiments`: the theory analogue of strong
  evidence is a *matching* bound, not a plot).
- **Proof is the evidence** — agreement/validity/termination are proved; the committee-sampling and
  indistinguishability techniques are named up front (`podc-writing-style`: name the technique).
- **Right venue, re-label test passes** — the contribution is a bound and its optimality in a
  distributed model, so it is a PODC result, not an ICDCS system or a STOC sequential algorithm
  (`podc-topic-selection`).
- **Optional simulation stays optional** — no scaling plot masquerades as the result; if included at
  all, it would illustrate the constant, not establish agreement (`podc-experiments`,
  `podc-reproducibility`).
- **10-page discipline anticipated** — the first-page arc makes the merits case reviewers must see
  within the first 10 pages, and full proofs are routed to the appendix/full version
  (`podc-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified PODC
> papers** whose first pages execute this arc, and [`../official-source-map.md`](../official-source-map.md)
> for PODC-specific submission policy and the proofs-venue cycle.
