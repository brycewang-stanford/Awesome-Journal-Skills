---
name: icalp-topic-selection
description: Use when deciding whether a theoretical computer science result belongs at ICALP (EATCS) and, if so, whether it is a Track A (algorithms, complexity, games) or Track B (automata, logic, semantics, theory of programming) paper, and when distinguishing ICALP from the US theory venues STOC, FOCS, and SODA or from a TCS journal by contribution shape, community, and the LIPIcs open-access model.
---

# ICALP Topic Selection

Decide the venue **and the track** before drafting. ICALP — the EATCS International Colloquium on
Automata, Languages, and Programming — is **Europe's flagship theoretical-computer-science
conference** and the annual meeting of the European Association for Theoretical Computer Science. Its
contribution is a **theorem**: a precise statement in a clean model, proved completely. A paper whose
real deliverable is a system, a benchmark result, or an application with no new theorem is respected
and then rejected as out of scope.

## Two decisions, not one

Routing to ICALP is genuinely two questions:

1. **Is this an ICALP paper at all**, versus STOC/FOCS/SODA, a specialized venue (LICS, CCC, SoCG,
   CONCUR, ...), or a journal?
2. **Which track** — **Track A (Algorithms, Complexity and Games)** or **Track B (Automata, Logic,
   Semantics and Theory of Programming)**?

Both matter: the tracks have separate program committees and separate HotCRP servers, and Track B
carries a rebuttal while Track A does not.

## Track A vs Track B

| Signal in your result | Track |
|---|---|
| A faster algorithm, a better approximation ratio, a new data structure, a fine-grained bound | **A** |
| A complexity lower bound, hardness, or a completeness result about *computation* | **A** |
| Algorithmic game theory, mechanism design, equilibrium computation | **A** |
| Decidability/complexity of a **logic** or a **theory**, model theory of computation | **B** |
| Automata, formal languages, transducers, infinite-state systems (Petri nets/VASS, pushdown) | **B** |
| Semantics of programming languages, lambda calculi, type theory, verification foundations | **B** |
| Concurrency theory, process calculi, category-theoretic semantics | **B** |

Borderline cases exist (e.g. logic-flavored complexity). Resolve them by **which community should
referee the proof** — the one that will recognize the technique and the prior bound — and by which
track's recent programs contain your subarea.

## ICALP vs the US theory venues and journals

| Signal in your project | Better home | Why |
|---|---|---|
| Broad TCS result, ready now, and the February ICALP deadline is the nearest honest fit | **ICALP** | EATCS European flagship; LIPIcs open access; two tracks |
| Top-tier breakthrough aimed at the US theory community, STOC/FOCS timing fits | **STOC / FOCS** | ACM/IEEE flagships; different calendar, single-column ACM/IEEE style |
| Core is discrete algorithms / data structures with a SODA fit | **SODA** | SIAM algorithms venue; different community and calendar |
| Logic in computer science specifically (not general Track B breadth) | **LICS** | Dedicated logic venue; overlaps Track B, different community |
| Computational complexity specifically | **CCC** | Dedicated complexity venue |
| Computational geometry | **SoCG** | Dedicated geometry venue |
| Result too long, or wants a definitive journal version of record | **journal (JACM, TALG, TCS, LMCS, ...)** | No conference page ceiling; some ICALP papers later have journal versions |

ICALP's distinctive pull is **European TCS community + LIPIcs open access + a two-track single
February cycle**. It is not STOC/FOCS/SODA; do not carry their templates, blinding regimes, or
calendars across.

## Contribution shapes ICALP rewards

- **A better bound** — a faster algorithm, a smaller approximation ratio, a tighter complexity bound
  than the best known, with the improvement stated against a named prior result.
- **A lower bound / hardness / impossibility** — proving a limitation, conditionally or
  unconditionally, in a precisely defined model.
- **A decidability / complexity classification** — pinning the exact complexity of deciding a logic,
  language, or verification problem (a signature Track B move).
- **A dichotomy or complete characterization** — classifying an entire family rather than one
  instance.
- **A new model or a foundational result** — a clean model with a clear TCS payoff; "foundations" is
  in the name for both tracks.

## The re-route tests

- **Theorem test:** strip the implementation and the experiments — is there still a theorem worth
  proving? If not, the paper belongs at an experimental-algorithms, database, or systems venue, not
  ICALP.
- **Prior-bound test:** can you name the best previous bound your result beats? If you cannot, either
  the problem is not yet a recognized ICALP problem, or the contribution is not a bound (an
  `icalp-writing-style` framing fix, or a re-route).
- **Track-referee test:** who should check the proof — an algorithms/complexity person (A) or an
  automata/logic/semantics person (B)? If the honest answer is "a systems/ML/database person," ICALP
  is the wrong venue.

## Cheap reconnaissance before committing

```text
[Scope]    scan the last two ICALP programs (dblp db/conf/icalp) for your subarea and track
           -> present in Track A/B recently = a reviewer pool exists; absent = opening or mismatch
[Citations] is your bibliography majority TCS venues (ICALP/STOC/FOCS/SODA/LICS/CCC + TCS journals)?
           -> majority applied venues => reviewers read you as a visitor; reconsider the venue
[Calendar] ICALP has ONE annual February deadline; compare with STOC/FOCS/SODA/LICS dates
           -> route to the nearest honest fit rather than waiting a full year for a marginal preference
```

## Decision procedure

```text
[Is there a theorem?] strip code/experiments -> new theorem remains? no => not ICALP
[ICALP vs US/journal] European TCS breadth, Feb deadline nearest, open-access wanted? -> ICALP
[Track] bound/algorithm/complexity/games => A ; logic/automata/semantics/verification => B
[Specialized check] pure logic => LICS? pure complexity => CCC? geometry => SoCG?
[Verdict] ICALP Track A / ICALP Track B / sibling venue / journal, with a one-line reason
```

Run this before the writing skills; a wrong venue *or* track decision wastes every later step. When
the verdict is ICALP, continue with `icalp-workflow` for the calendar and `icalp-writing-style` for
the paper shape.
