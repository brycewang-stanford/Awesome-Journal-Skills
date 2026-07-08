---
name: focs-topic-selection
description: Use when deciding whether a theoretical-computer-science result belongs at FOCS (IEEE Symposium on Foundations of Computer Science) — testing foundations-level significance, weighing the April deadline against sibling theory venues like STOC, SODA, CCC, ITCS, or CRYPTO, and applying the CFP's broaden-the-reach clause.
---

# FOCS Topic Selection

FOCS asks for "new and original research on theory of computation" and explicitly
welcomes papers that broaden the reach of the theory of computing or raise
important problems that can benefit from theoretical investigation (FOCS 2026
CFP, checked 2026-07-08 via `focs.computer.org/2026/call-for-papers-2/`). The
selection question is therefore two-dimensional: is this a theorems paper whose
significance survives a committee drawn from every corner of TCS, and is the
April-anchored IEEE cycle the right launch window for it?

## The significance test a FOCS PC applies

A foundations flagship rewards results that change what other theoreticians can
prove, not results that only optimize inside one subcommunity's parameter chart.
Before committing to the April deadline, answer three questions in writing:

1. **Consequence:** name a problem *outside* your immediate subarea that becomes
   easier, or a belief that must be revised, if your theorem holds.
2. **Obstacle:** state what stood in the way — a known barrier, a stuck
   parameter regime, a missing structural insight — and how your technique gets
   past it.
3. **Durability:** would the result still be cited if the constant factors were
   worse? If the paper's value evaporates without its best constants, it is
   likely a specialized-venue paper.

A "yes" on two of three is competitive; a "yes" driven only by technical
difficulty, with no consequence statement, is the classic strong-reject-with-
respect outcome.

## Routing across the theory ecosystem

| Signal in your result | Better home | Why |
|---|---|---|
| General TCS interest, mature proofs, ready by April 1 | **FOCS** | The fall flagship; full-version submissions welcome |
| Same profile, but ready in autumn | **STOC** (ACM SIGACT) | The spring flagship; the other beat of the same community |
| Algorithms with heavy implementation or fine-grained constants | **SODA / ESA** | Committees calibrated for algorithmic depth over breadth |
| Complexity-internal progress (e.g., inside a known hierarchy) | **CCC** | Specialist referees who value the regime you improved |
| Conceptual model or provocative definition, proofs still thin | **ITCS** | Explicitly rewards vision over completeness |
| Cryptographic construction with security-proof machinery | **CRYPTO / EUROCRYPT / TCC** | IACR reviewing conventions fit the proof style |
| Quantum result addressed mainly to quantum insiders | **QIP** | Talk-driven venue; pair with an arXiv record |
| Learning-theoretic core with sample-complexity focus | **COLT / ALT** | Statistical-learning referees |
| Geometry- or distributed-computing-native contribution | **SoCG / PODC / DISC** | Community-specific evaluation depth |

FOCS and STOC differ in sponsor (IEEE Computer Society TCMF vs. ACM SIGACT),
calendar seat, and program committee — not in scope or prestige. Never argue
"FOCS because it is stronger than X"; argue from audience and timing.

## Timing logic from the FOCS seat

The FOCS deadline (April 1 for the 2026 cycle) sits roughly five months after
STOC's early-November deadline and about seven months before the conference
itself. Consequences worth planning around:

- A February STOC rejection leaves about eight weeks to strengthen a paper for
  FOCS — enough for new lemmas, not for a new main theorem.
- A summer FOCS rejection lands close to STOC's autumn deadline, making the
  two venues a natural resubmission loop for borderline-flagship work.
- The CFP applies SIGACT's prior/simultaneous-publication policy even though
  FOCS is an IEEE event: work published, or scheduled to be published, before
  the conference month elsewhere is ineligible, and simultaneous submission to
  another proceedings venue or journal is barred.

## The broaden-the-reach lane

The CFP sentence inviting papers that widen theory's reach is a real lane, not
decoration: FOCS regularly accepts work importing TCS rigor into new territory
(economic mechanisms, learning pipelines, quantum experiments, fairness,
verification). To use the lane safely:

- The imported problem must be formalized well enough that a theorem about the
  formalization says something about the original phenomenon — reviewers reject
  "we define X and prove trivia about X" imports quickly.
- At least one proof should require an idea that specialists in the source
  domain do not already have; otherwise the paper reads as a survey with
  notation.
- Cite the domain's own literature accurately; a cross-over paper that
  misstates the state of the neighboring field loses the committee's trust on
  the theory too.

## Common misroutes seen from the FOCS seat

- **The constants paper.** An improvement from 2.371 to 2.368 in a famous
  exponent can absolutely be FOCS material — but only when the write-up
  explains the structural reason the previous approach was stuck. Without that,
  SODA's referees will value the engineering more.
- **The kitchen-sink crypto paper.** Ten related constructions with security
  proofs is an IACR paper; FOCS wants the one construction whose existence
  changes the map.
- **The premature model.** A new complexity model with only easy separations
  belongs at ITCS this year and at FOCS in two years, once someone proves
  something hard in it — possibly you.
- **The disguised benchmark paper.** If the strongest section is an evaluation,
  no theory framing will save it here; see `focs-experiments` for what
  computation can and cannot do in this venue.

## Quick self-diagnosis

```text
[Claimed contribution] <one sentence, no adjectives>
[Consequence outside subarea] <named problem or belief revised — or NONE>
[Barrier bypassed] <named obstacle — or NONE>
[Deletion test] remove best constants: still citable? yes/no
[Cycle fit] proofs complete by April 1? yes/no
[Verdict] FOCS / STOC (autumn) / specialized venue: ____
```

Two NONE answers or a "no" on proof completeness means route elsewhere or wait
a beat. FOCS grants no rebuttal in which to repair a shaky significance case
(see `focs-review-process`), so the routing decision must be honest before the
formatting work begins. If the contribution is a new model or problem rather
than a theorem, re-read the CFP's broaden-the-reach sentence and consider
whether ITCS's explicitly conceptual charter serves the paper better — an
important-problems paper at FOCS still needs nontrivial technical evidence
that the problem is tractable and rich.

Finally, calibrate against the venue's own memory: the exemplars library in
`resources/exemplars/library.md` maps recent Test of Time and Machtey Award
citations to durability patterns (field-opener, technique transplant,
barrier map, subfield founder). If your draft cannot honestly claim kinship
with any pattern there, that is not disqualifying — but it predicts which
committee question (`focs-review-process`) will decide your fate, and it
should shape where the writing effort goes.
