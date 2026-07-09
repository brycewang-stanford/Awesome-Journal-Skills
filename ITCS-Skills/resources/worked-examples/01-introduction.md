> **Illustrative teaching example.** The paper, model, and every claim below are **fictional**
> and exist only to demonstrate ITCS house style. No real-paper facts are stated, and no policy
> is invented. Corresponding skills:
> [`itcs-writing-style`](../../skills/itcs-writing-style/SKILL.md),
> [`itcs-topic-selection`](../../skills/itcs-topic-selection/SKILL.md), and
> [`itcs-related-work`](../../skills/itcs-related-work/SKILL.md).

# Worked Example: An ITCS-Style Abstract + Introduction (before -> after)

This demonstrates the **ITCS first-page arc** from `itcs-writing-style`:
**a new question or model -> why the field lacked it -> what becomes possible (the conceptual
payoff) -> a crisp result that shows the model is alive -> what directions it opens** — with the
ITCS expectations that the **innovation is legible before any theorem**, the paper is honest
that its results are a *first foray* rather than the last word, and the scope-and-limitations
posture is visible from the start.

The framing also reflects `itcs-topic-selection`: ITCS is strongest when the contribution is a
**new lens on a problem** — a definition, a model, a connection — rather than the technically
deepest theorem on an existing question (which routes to STOC/FOCS on depth, or to SODA if it is
an algorithms result). The test is not "is this the hardest theorem this year?" but "**is this a
new question worth asking, and does the paper make me want to work on it?**"

**Illustrative paper (fictional):** *"Forgetful Certificates: A Model of Verification Under
Bounded Memory of the Prover."* Fictional model: an interactive-proof variant in which the
prover cannot remember its own past messages, and the question is what can still be proved.

---

## Before (buries the innovation under machinery — typical first-draft abstract + intro)

> **Abstract.** We study interactive proof systems with a memory-bounded prover. We prove that
> for a certain parameter regime, the class of languages provable is contained between two known
> classes, and we give a protocol achieving a round complexity of O(log n) using a new
> hashing-based amplification lemma. Our techniques combine algebraic encoding with a careful
> potential-function argument, improving the constants in prior work.
>
> **Introduction.** Interactive proofs are a central object in complexity theory. Much is known
> about them. In this paper we add a memory bound on the prover and analyze the resulting class.
> Section 2 has preliminaries, Section 3 our protocol, Section 4 the lower bound, Section 5 the
> amplification lemma, and Section 6 open problems.

**What's wrong (against `itcs-writing-style` / `itcs-topic-selection`):**

- **No new question on the first page.** It leads with a *containment result* and a *round
  complexity*, as if this were a STOC depth paper. An ITCS reader finishes the abstract without
  learning *why forgetful provers are an interesting thing to think about at all*.
- **The model is introduced as a technical tweak**, not as a lens. "We add a memory bound" hides
  the conceptual move (what does it *mean* for a proof to survive a prover that cannot remember
  its own claims?).
- **The payoff is missing.** ITCS wants to know what the model *lets us see or do* — a connection
  to streaming, to bounded rationality, to real verification settings — not a constant-factor
  improvement.
- **Depth-signalling in the wrong currency.** "Improving the constants in prior work" is a
  STOC/SODA virtue, not an ITCS one; here it reads as if the authors mistook the venue.
- **Over-signposted roadmap** substituting for an argument about why the reader should care.

---

## After (ITCS arc — new question -> gap -> payoff -> a result that shows the model is alive -> directions)

> **Abstract.** Every model of interactive proof assumes a prover that perfectly remembers what
> it has already said. But many real verifiers — a streaming service, a low-power sensor, a
> human — interact with parties whose memory of the exchange is itself bounded. We introduce
> **forgetful certificates**: interactive proofs in which the prover's memory of its own past
> messages is bounded by a parameter *m*. The model exposes a question invisible in the standard
> setting: *how much of a proof's power comes from the prover's ability to stay consistent with
> its own history?* We show the model is neither trivial nor all-powerful — with *m* logarithmic
> in the input, forgetful provers already capture a natural and previously unstudied class, and
> we exhibit a language that separates forgetful from standard provers. These first results
> suggest forgetfulness is a new axis along which the power of verification can be measured, with
> apparent links to streaming lower bounds and to bounded-rationality models of delegation.
> *(new question -> gap -> model -> a separation showing it is alive -> directions — all on the
> first page.)*
>
> **Introduction.** *(¶1 — the new question, first breath.)* Interactive proofs give a
> computationally weak verifier confidence in a powerful prover's claim. The entire theory rests
> on a silent assumption: the prover **remembers everything it has said** and can keep its later
> messages consistent with its earlier ones. Strip that assumption away — as reality does whenever
> the "prover" is a device, a service, or a person with bounded memory — and a question appears
> that the standard model cannot even phrase: *what part of a proof's soundness was doing the work
> of forcing the prover to be consistent with itself?*
>
> *(¶2 — why the field lacked the question.)* Prior work on resource-bounded provers bounds the
> prover's *computation* or *advice*, never its *memory of the interaction itself*. Because the
> classical prover is stateless-by-omnipotence — it can recompute its whole history for free —
> the consistency assumption was never isolated as a resource. No existing model lets us ask what
> it is worth.
>
> *(¶3 — the conceptual contribution.)* We introduce **forgetful certificates**, interactive
> proofs with an *m*-bit bound on the prover's memory of its own transcript. The definition is
> the contribution: it turns "self-consistency" into a measurable quantity and places standard
> interactive proofs at one end (m unbounded) of a new spectrum.
>
> *(¶4 — a crisp result that shows the model is alive.)* A model is only interesting if it is
> neither empty nor everything. We prove two anchoring results: (i) with *m = O(log n)*,
> forgetful provers already decide a natural class strictly containing the trivially-verifiable
> languages; and (ii) there is an explicit language provable by a standard prover but **not** by
> any forgetful prover with sublinear *m* — a separation witnessing that forgetfulness genuinely
> costs power. Proofs of both are complete in Appendices A-B.
>
> *(¶5 — honest scope and the directions it opens.)* We are explicit about what this is: a **first
> map** of a new axis, not its final geography. We do not resolve the exact class boundary for
> intermediate *m*, and we conjecture but do not prove a connection to multi-pass streaming lower
> bounds. What we claim is that "how much must a prover remember?" is a question worth the
> community's attention, with visible bridges to streaming, to delegation under bounded
> rationality, and to the study of stateless cryptographic devices. Section 2 fixes the model;
> Sections 3-4 prove the anchoring results; Section 5 collects open problems, which are the point.
> *(brief roadmap, framed as an invitation.)*

---

## Why the "after" meets the ITCS bar

Mapped to the skill checklists:

- **Innovation before theorem** — the abstract and ¶1 pose a *new question* and name the *new
  model* before any bound (`itcs-writing-style`: "lead with the conceptual contribution; the
  reader should want the theorem before they see it").
- **Right venue, novelty-first** — the contribution is a lens that reorganizes an existing area,
  not a constant-factor improvement, so it is ITCS-shaped rather than a STOC depth paper or a
  SODA algorithms paper (`itcs-topic-selection`: the "new question worth asking" test).
- **A result that shows the model is alive** — the separation and the capture result pre-empt the
  reviewer's first objection ("is this model empty or trivial?") the way ITCS PCs probe every new
  model (`itcs-writing-style` / exemplars: model first, one crisp result as evidence).
- **Honest first-foray posture** — ¶5 states plainly what is unresolved and frames the open
  problems as the deliverable, matching the ITCS norm that a bold, incomplete direction can beat
  a polished increment (`itcs-writing-style`: scope and limitations are a feature, not an
  apology).
- **Full proofs present** — both anchoring results carry complete proofs in appendices, meeting
  the ITCS submission requirement that every central claim be checkable
  (`itcs-reproducibility`, `itcs-supplementary`).
- **Positioned by delta, not volume** — ¶2 isolates exactly what prior resource-bounded-prover
  work did *not* ask, rather than listing citations (`itcs-related-work`: delta-first
  positioning).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ITCS
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for ITCS-specific submission policy and
> the conceptual-novelty ethos.
