---
name: osdi-topic-selection
description: Use when deciding whether a systems project fits OSDI, choosing between its Research and Operational Systems tracks, or routing the work to SOSP, NSDI, FAST, EuroSys, or the post-USENIX ATC instead — applying the built-and-measured test before a December deadline is spent on a misfit.
---

# OSDI Topic Selection

Decide venue months before writing, not days. Everything below reflects the OSDI '27
pages as re-verified on 2026-11-24; the scope paragraph and track structure are re-issued in
every CFP, so reopen `usenix.org/conference/osdi<yy>/call-for-papers` before committing
a project to the December deadline.

## The built-and-measured test

OSDI's identity is in its name: design **and implementation**. Before anything else,
answer three questions honestly:

1. **Does the system exist?** Not a simulator of the idea — the artifact itself,
   runnable under load. A design argued only from simulation or analysis is fighting
   the venue's instincts.
2. **Has it been measured against something that fights back?** A mature baseline, a
   production-derived workload, a deployment. Microbenchmarks alone signal a workshop
   paper.
3. **Is there an idea that survives the implementation?** Name the abstraction,
   mechanism, or principle a different team could reuse. If the honest answer is
   "we engineered X to be faster," the contribution is engineering, and OSDI reviewers
   will say so.

Failing question 1 or 2 does not kill the project — it re-times it. Both OS flagships
now run annually (OSDI since 2021, SOSP since 2024), so waiting one build cycle costs
months, not the two years it cost under the old alternation.

## Is it in scope?

The OSDI '27 CFP takes a deliberately broad view of "systems": operating systems, file
and storage systems, distributed systems, cloud computing, mobile systems, secure and
reliable systems, formal verification of systems software, systems aspects of big data,
**systems for machine learning**, embedded systems, virtualization, networking as it
relates to operating systems, and management and troubleshooting of complex systems.
It also asks that submissions "offer insights that intrigue a substantial portion of
OSDI attendees," and that papers applying systems techniques to new domains (e.g., ML)
engage the relevant systems prior work, baseline against known techniques, and spell out
the new systems challenges. Two practical readings:

- ML-systems work is squarely welcome **as systems work** — scheduling, serving,
  memory, parallelism — not as model-accuracy work (see TensorFlow and Orca in
  [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md)).
- "Networking as it relates to operating systems" is the OSDI/NSDI border in one
  phrase: if the network is the object of study, it is NSDI's; if the host stack is,
  it can be OSDI's.

## Two tracks, one deadline

OSDI '27 (as '26) reviews two tracks side by side, registered and submitted on the same
December dates (December 1 / 8, 2026); Operational Systems titles end with
"(Operational Systems)":

| Track | The paper it wants | Choose it when |
|---|---|---|
| Research | New design + implementation + evaluation | The idea is the contribution and you built it to prove it |
| Operational Systems | Design, implementation, analysis, and **experience** of a deployed system | The system has run in production and the lessons are the contribution |

The Operational Systems track changes the evidence bar, not the quality bar: deployment
scale, incident history, and longitudinal behavior substitute for head-to-head novelty.
Do not put a research prototype in the operational track to dodge a novelty fight —
experience is exactly what it cannot show.

## Routing against the sibling venues

```text
Decision sketch (verify each venue's live CFP before acting):
built OS/storage/distributed system, idea-led  -> OSDI (Research)
same, but the story is production experience   -> OSDI (Operational Systems)
same community, ACM cadence fits better        -> SOSP (annual since 2024)
network is the object (protocols, fabrics)     -> NSDI
persistence/storage stack is the whole story   -> FAST
strong systems work, flagship bar uncertain    -> EuroSys / ACM SIGOPS ATC
                                                  (USENIX ATC ended after ATC '25)
position paper, no artifact yet                -> HotOS-style workshop first
```

Two cadence facts matter for routing. First, OSDI sits mid-year (OSDI '27: July 7–9,
2027, Baltimore) with a December submission — a December miss can retarget to SOSP or NSDI
within months. Second, USENIX ATC no longer exists as a USENIX venue; its successor is
stewarded by ACM SIGOPS, so pre-2026 advice that treats ATC as OSDI's co-located
little sibling is stale.

## Timing snapshot for the routing decision

Anchor the decision to real dates, then re-verify them live:

- **OSDI '26** (20th): July 13–15, 2026, Seattle; its submission gates were
  December 4/11, 2025 — history.
- **OSDI '27** (21st): July 7–9, 2027, Hyatt Regency Baltimore Inner Harbor; abstract
  registration **December 1, 2026**, complete papers **December 8, 2026** (5:59 pm EST);
  notification March 16, 2027 (CFP re-verified 2026-11-24). Tracks, the 12-page budget,
  the eight-paper cap and conditional acceptance carry over from '26.
- A project deciding venue in late November 2026 has one week to the OSDI '27
  registration gate; anything not near-final is really choosing between OSDI '28 and
  whatever SOSP/NSDI gates fall in between — pull the live pages before promising the
  team a date. Note the collision the '27 CFP calls out: a paper under NSDI '27 Fall
  review cannot go to OSDI '27.

## Signals you are about to misfire

- The evaluation section would be all microbenchmarks — no end-to-end workload exists
  yet. (Wait a cycle; see `osdi-experiments`.)
- The paper's strongest sentence is about the *model*, not the *system* — route to an
  ML venue, or reframe until the systems claim stands alone.
- The design is real but unbuilt — OSDI reviewers read "we expect" as "we have not."
- The contribution is a measurement study of others' systems with no design lesson —
  possible at OSDI, but the bar is a lesson that changes how people build, not a
  benchmark report.
- You cannot fit the idea into 12 reviewed pages without appendices — OSDI '27 allows a
  separate supplementary file but PC members need not read it, so a proof-heavy
  contribution may belong at a venue that reviews appendices.

## Output format

```text
[OSDI fit] strong / plausible / misfit (one-line reason)
[Built-and-measured] artifact exists? measured against a real opponent? idea survives?
[Track] Research / Operational Systems (why)
[Scope lane] which CFP topic phrase this sits under
[Re-route] best alternative venue + next live deadline to check
[Cycle math] months lost if we wait one build cycle vs risk of submitting now
```
