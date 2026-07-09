---
name: aamas-supplementary
description: Use when preparing AAMAS supplementary material - proofs, extended game and mechanism definitions, extra multiagent experiments, opponent-set details, and the anonymized artifact zip - under the size cap, anonymity, and reviewer-discretion limits, including how to split a game-theory-plus-experiments paper across the 8-page body and the supplement.
---

# AAMAS Supplementary

Use this when assembling AAMAS supplementary material. The supplement can support the paper, but
the 8-page main submission must stand on its own; a body that is unintelligible without the
appendix reads as unreviewable within the page limit.

## Supplement structure

- Put full proofs, extended game and mechanism definitions, extra ablations, opponent-set
  documentation, and robustness tables in a clean appendix or supplementary document.
- Put executable assets - game code, environments, learning rules - in the anonymized zip when
  the current OpenReview form allows it.
- Respect the current supplement size cap (25 MB single zip in 2026) and the deadline.
- Keep every supplementary file double-blind: no authors, institutions, acknowledgements,
  private paths, repository owners, or identifying metadata.
- Do not hide essential motivation, the core game definition, the main theorem statements, or
  the primary interaction results in the supplement.
- Verify the archive opens on a clean machine and carries no credentials, caches, or OS
  metadata.

## Appendix architecture for proofs and games

- Order appendix sections to mirror the body: game and notation, main proofs, auxiliary lemmas,
  additional agents/opponents, then extended experiments.
- Restate each theorem and the relevant game before its proof so the appendix reads standalone
  without flipping back to the two-column body.
- Keep one proof sketch and the full game definition in the body itself; an AAMAS paper whose
  entire strategic argument lives in the appendix cannot be judged in eight pages.
- Cross-reference every appendix table, lemma, and opponent set from the body at least once;
  orphaned supplement material is invisible under reviewer discretion.

## What gets opened first

| Supplement item | Inspection likelihood | Practical implication |
|---|---|---|
| Proof of the headline equilibrium/mechanism result | High | Polish to main-text standard |
| Extended game or environment definition | High | Reviewers reconstruct the interaction from it |
| Extra opponent/population results | Medium | Reference each from the body |
| Code/environment archive | Variable, reviewer discretion | README must orient a reader in one minute |
| Raw episode logs | Low | Include for completeness, never rely on them |

## Vignette: splitting a mechanism-design paper

A submission proving a truthful decentralized mechanism plus a self-play study: the body keeps
the mechanism definition, the dominant-strategy theorem, one proof sketch, and the two
decision-critical figures (truthfulness under learning and the efficiency gap); the appendix
holds full proofs and sensitivity sweeps; the zip carries the game generator and the
strategic-deviation harness. Nothing decision-critical lives only in the zip, because archive
inspection is discretionary.

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Files] <appendix/proofs/game-defs/code/logs>
[Size/deadline] <current cap and deadline with source>
[Anonymity checks] <passed/issues>
[Main-paper dependency] <what breaks if supplement is ignored>
```
