---
name: podc-writing-style
description: Use when drafting or revising the body of an ACM PODC paper — building the distributed-theory skeleton (an explicit model box, the result stated as a theorem up front, a proof architecture the reader can navigate, and the 10-page-merits discipline) so the merits case lands within the first 10 pages a PODC committee is guaranteed to read.
---

# PODC Writing Style

Write for a reader who will check your proof. A PODC paper is a **mathematical argument** about a
**distributed model**, and the committee decides on the **first 10 pages after the title page** (the
merits budget). The house style is therefore front-loaded: fix the model, state the result, then
prove it — with the proof organized so a reviewer can find and verify each step.

## The first-page arc

Lead with the result inside its model, in this order (see the worked example in
`resources/worked-examples/01-introduction.md`):

1. **The problem inside a fixed model** — network (message-passing / shared memory), timing
   (synchronous / asynchronous / partial synchrony), fault model (crash / Byzantine /
   self-stabilizing), adversary (adaptive / oblivious), and the **cost measure** (rounds / messages /
   bits / space).
2. **Why the state of the art leaves a gap** — the best prior bound and exactly what it does not
   achieve in *this* model.
3. **The result, as a theorem** — an explicit bound and the resilience/assumptions it holds at, not
   "more efficient."
4. **Whether it is tight** — a matching lower bound elevates an algorithm to an optimality result,
   the venue's most valued shape.
5. **The proof idea in one breath** — name the technique (valency, indistinguishability, potential
   function, committee sampling, covering) so the reader knows how the argument goes.

## The model box is non-negotiable

Before the first theorem, state the model explicitly and completely. At PODC the model *is* the
theorem — an agreement result under synchrony and under asynchrony are different papers. A checklist
for the model box:

```text
[Network]     message-passing (point-to-point / broadcast) or shared memory (registers, objects)?
[Topology]    complete graph, arbitrary graph (LOCAL/CONGEST), dynamic network?
[Timing]      synchronous rounds / asynchronous / partial synchrony (GST)?
[Faults]      none / crash / omission / Byzantine / self-stabilizing; how many (t < n/3, etc.)?
[Adversary]   adaptive or oblivious; computational assumptions (if cryptographic)?
[Randomness]  deterministic / randomized (private / shared coins)?
[Cost measure] rounds, messages, bits, space, work — and worst-case vs. expected?
```

Every theorem must be true in exactly this model, and no proof may silently strengthen a synchrony
or weaken an adversary assumption mid-argument. Reviewers hunt for exactly this slippage.

## Proof architecture

The proof is the paper, so make it navigable:

- **State lemmas where the argument needs them**, each with a one-line role ("Lemma 3 bounds the
  number of rounds until a committee is honest-majority").
- **Separate the algorithm from its analysis.** Present the protocol cleanly (pseudocode in the
  process's local view), then prove safety, then liveness/complexity.
- **Name invariants.** Distributed proofs live on invariants preserved across rounds/steps; state
  them explicitly and prove they are maintained.
- **Route long proofs to the full version.** A proof sketch in the 10-page body with the full proof
  in the appendix is standard — but the sketch must convince a reviewer the full proof exists (see
  `podc-supplementary`).

## The 10-page-merits discipline

The committee is guaranteed to read only the abstract and the first 10 pages. So the first 10 pages
must, on their own, let a reviewer decide: they contain the model, the theorem, the delta over prior
work, and enough of the proof (in sketch or in full) to believe it. Do not defer the key idea to
page 14. Techniques for staying inside the budget:

- Put the **hardest, most novel** part of the proof in the body; route routine calculations and
  standard lemmas to the appendix/full version.
- Use a clean notation table once, not repeated definitions.
- Prefer a tight statement plus a proof idea over a verbose informal walk-through.

## Prose that helps a proof-checking reader

- **State theorems in the strongest true form** — with explicit constants/asymptotics and the exact
  assumptions, so a reviewer is not left guessing the regime.
- **Do not oversell.** "Optimal" requires a matching lower bound; "practical" requires more than a
  simulation and usually belongs at a systems venue. PODC readers penalize claims the proof does not
  support.
- **Distinguish `O`, `Θ`, `Ω`, and `o`** carefully; a distributed-theory reviewer reads asymptotics
  literally.
- **Keep an optional simulation clearly optional** — if you include a plot, say it *illustrates* a
  constant or a convergence rate and does not establish correctness (see `podc-experiments`).

## Anti-patterns (PODC-specific)

- **The missing model box** — "tolerates faults" without saying which faults, timing, or adversary.
- **Bound-free claims** — "more efficient" / "scales well" instead of a stated complexity.
- **Simulation-as-proof** — a scaling plot standing in for a correctness argument.
- **Proof gaps deferred past page 10** — the key lemma only in the appendix with no body sketch.
- **Sequential result in distributed clothing** — if removing distribution leaves the whole
  contribution, it is a STOC/SODA paper (`podc-topic-selection`).

## Output format

```text
[Model box] complete? (network/timing/faults/adversary/randomness/cost measure)
[Result placement] theorem stated on the first page? tightness (matching lower bound) addressed?
[Proof architecture] lemmas stated where used; invariants named; safety/liveness separated?
[10-page merits] model+result+delta+key proof idea all within the first 10 pages? yes/no
[Claim hygiene] "optimal"/"practical" claims backed? asymptotics precise?
[Fix queue] <ordered edits to land the merits case in 10 pages>
```
