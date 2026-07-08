---
name: stoc-topic-selection
description: Use when deciding whether a result belongs at STOC (ACM Symposium on Theory of Computing) — testing for broad theory-of-computation significance versus routing to FOCS, SODA, CCC, ITCS, COLT, CRYPTO, PODC, SoCG, EC, or a journal like JACM/SICOMP when the fit is specialized, conceptual, or empirical.
---

# STOC Topic Selection

STOC is ACM SIGACT's flagship for the theory of computation: algorithms and
data structures, computational complexity, cryptography, combinatorial and
continuous optimization, learning theory, quantum computing, algorithmic game
theory, coding theory, and the theory sides of adjacent fields (scope sentence
paraphrased from the STOC 2026 CFP, checked 2026-07-08; re-read the live topics
list before arguing fit). The question this skill answers is not "is this
theory?" but "is this *flagship-general* theory?" — because the venue's
distinguishing filter is breadth of interest across a cross-area committee.

## The breadth test

Ask three questions; STOC-shaped results pass at least two convincingly:

1. **The corridor test.** Could you explain to a theorist in a *different*
   sub-area, in three minutes, why this changes something they care about?
2. **The lineage test.** Does the result advance a problem the field at large
   has tracked (a named open problem, a long-standing bound, a barrier), rather
   than a parameterized variant introduced by the last three papers on it?
3. **The technique test.** Is there a transferable idea another sub-area could
   plausibly borrow?

Failing all three does not mean the work is weak — it means the reviewing lens
of a flagship will undervalue it, and a specialized committee will not.

## Routing map

| Signal in the work | Better-first venue | Why |
|---|---|---|
| Strong algorithmic result, interest mostly within algorithms | SODA | Deeper algorithms bench; specialized appreciation |
| Complexity-internal classification or oracle separation | CCC | The audience that can evaluate it fully |
| Bold model or conceptual reframing, proofs still modest | ITCS | Explicitly welcomes conceptual-first contributions |
| Learning-theoretic bounds, sample complexity, online learning | COLT (or ALT) | The statistical-learning reviewer pool lives there |
| Cryptographic construction with security-proof machinery | CRYPTO / EUROCRYPT / TCC | Protocol-level evaluation norms |
| Distributed/parallel model result | PODC / DISC / SPAA | Model-specific committee |
| Computational geometry core | SoCG | Ditto |
| Incentives, mechanism design, markets | EC | Ditto |
| Quantum result of quantum-internal interest | QIP | Route by the corridor test; quantum with broad consequences fits STOC/FOCS |
| Empirical algorithmics, implementation evidence central | ALENEX / ESA track B / systems venues | STOC has no experiments axis to reward it |
| Complete, mature treatment; no deadline pressure | JACM / SICOMP / TheoretiCS directly | Journals referee depth without page games |

STOC and **FOCS** are deliberately not differentiated by topic in this map: the
scope is near-identical, and the honest routing variable is *timing* (November
vs. April deadline) plus readiness (`stoc-workflow`'s two-beat table). Choosing
STOC over FOCS "for prestige" has no basis; the pair is treated as equals by
the community and by hiring committees.

## Aiming a result at STOC honestly

If the work is borderline, three legitimate moves raise flagship fit — and one
illegitimate move to refuse:

- **Generalize the frame:** if your technique proves the special case via a
  method that clearly extends, do the extension; breadth is often one lemma
  away.
- **Connect to a named question:** show the result's consequence for a problem
  outsiders track (a barrier, a conjecture, a well-known gap). This is
  positioning work (`stoc-related-work`), and it is honest when the connection
  is real.
- **Lead with the conceptual payoff:** a model clarification or an unexpected
  equivalence can carry a paper whose bounds are modest — STOC's history
  rewards ideas (Cook's STOC 1971 NP-completeness paper was exactly this).
- **Refuse:** inflating a variant into "the first result on X" by narrowing X
  until you are first. The lineage-checking reviewer (`stoc-related-work`,
  lane one) exists precisely for this.

## Anti-patterns in venue choice

- **Deadline-driven routing:** submitting to STOC because November is when the
  paper happened to be finished. The two-beat calendar (`stoc-workflow`) makes
  this unnecessary; readiness should pick the beat, fit should pick the tier.
- **Prestige laddering:** submitting a clearly SODA-shaped paper to STOC "to
  try," planning to cascade downward. It costs a review cycle, and theory's
  overlapping reviewer pools mean the second committee often knows.
- **Scope-sentence lawyering:** arguing fit from the CFP's topic list alone.
  The topics list is necessary, not sufficient; the breadth tests are the real
  filter.
- **Journal-phobia:** cycling a mature, complete result through conference
  deadlines for years when JACM or SICOMP would referee it once, properly.

## Prize-lineage calibration

For a sense of what "flagship-scale" has meant concretely, the SIGACT prize
record is the honest sample: STOC Best Papers (up to four per year), the Danny
Lewin student award, and the Test of Time awards for STOC papers whose
influence compounded over decades (`sigact.org/prizes`, checked 2026-07-08; see
`resources/exemplars/library.md` for dblp-verified cases). Calibrate against
what these papers *did* — opened a field, closed a known problem, moved a
famous bound — not against their fame today.

## Decision procedure

```text
1. Write the one-sentence contribution with its model and bound explicit.
2. Run the three breadth tests; record pass/fail with a sentence each.
3. If >= 2 pass: STOC or FOCS by calendar readiness (stoc-workflow).
4. If <= 1 passes: pick the specialized venue from the routing map and
   check ITS live CFP; specialized theory venues differ in format and
   review style more than in quality bar.
5. If the result is complete and timeless: consider the journal route
   directly; JACM/SICOMP acceptance does not require conference passage.
6. Re-run after any major strengthening — fit is a function of the result,
   and the result changed.
```

## Cycle-volatility warnings

- Topic lists in CFPs drift (quantum, fairness, and AI-theory items have been
  moving targets); the live CFP wording is the only citable scope (待核实).
- Deadline geometry among STOC/FOCS/SODA/CCC shifts by weeks year to year;
  verify each venue's current dates before committing the calendar.

## Output format

```text
[Fit] STOC-shaped / FOCS-timed / specialized (target: <venue>) / journal-direct
[Breadth tests] corridor <pass/fail> / lineage <pass/fail> / technique <pass/fail>
[One-sentence contribution] <model + bound + why outsiders care>
[Honest strengthening] <generalization or connection available, if any>
[Calendar] <next viable deadline with date from live CFP>
```
