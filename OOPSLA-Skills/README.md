# OOPSLA Skills

Twelve agent skills for papers targeting **OOPSLA — the ACM SIGPLAN conference on
Object-Oriented Programming, Systems, Languages, and Applications**, which today
operates as the research-paper track of **SPLASH** and publishes its accepted
papers as journal articles in **PACMPL** (Proceedings of the ACM on Programming
Languages), in two issues per year: OOPSLA1 and OOPSLA2. The pack covers the
full campaign: deciding whether a project's center of mass belongs at OOPSLA
rather than POPL/PLDI/ICFP/Onward!, choosing between the two yearly submission
rounds, surviving multi-stage double-anonymous review with its four-way
outcomes, executing Minor and Major Revisions, earning artifact badges, and
presenting at the SPLASH conference.

Official basis checked on **2026-07-08**: the OOPSLA 2026 track pages on
`2026.splashcon.org` / `conf.researchr.org`, the `oopsla26.hotcrp.com` call and
deadlines pages, the OOPSLA 2026 Round 1 CFP as circulated on TYPES/announce,
the SPLASH 2026 site and dates pages, the SPLASH 2026 artifact-evaluation
track, the PACMPL journal and Vol. 10 Issue OOPSLA1 front matter on the ACM
Digital Library, SIGPLAN's SPLASH/OOPSLA series pages, and the SIGPLAN
Empirical Evaluation Guidelines. The verification environment's gateway
blocked direct fetches of those hosts (HTTP 403), so pages were read through
search-engine renderings of the exact URLs and cross-checked across
independent renderings, the ACM DL, and dblp; the full audit trail, including
every item still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes OOPSLA structurally different

Six verified mechanics shape all twelve skills — and distinguish OOPSLA from
its single-deadline SIGPLAN siblings:

- **Two doors per year into one journal volume.** OOPSLA 2026 took new papers
  in Round 1 (deadline October 10, 2025, AoE, firm) and Round 2 (March 17,
  2026, AoE, firm), both via HotCRP. Round 1 acceptances became PACMPL
  Vol. 10, Issue **OOPSLA1** (published from April 1, 2026 — 75 articles from
  227 submissions); Round 2 acceptances form Issue **OOPSLA2** (from
  October 1, 2026).
- **A four-way decision, not accept/reject.** Each round ends in Accept,
  Minor Revision (same-round completion; for 2026 this absorbed the previous
  "Conditional Accept" category), Major Revision, or Reject.
- **Round-hopping is designed in.** A Major Revision is an invitation to
  resubmit to the *next* round against an explicit expectation list, keeping
  the same reviewers where possible — so an October submission that draws a
  Major Revision can still publish in the same year's volume via the March
  round. This pack teaches that calendar arithmetic explicitly.
- **A journal format with a revision bonus.** Submissions use single-column
  `acmsmall` (`review,anonymous` options), at most **23 pages** excluding
  references, required statements, and appendices; invited revisions get
  **25 pages**. A **Data-Availability Statement** is required before the
  references and does not count against the cap.
- **A conference umbrella with its own geography.** Accepted papers present
  at SPLASH — in 2026: Oakland, California, October 4–9, with OOPSLA talks
  October 5–7, co-located with **ISSTA 2026** and alongside the **Onward!**
  Papers and Essays tracks. Artifact evaluation runs as a SPLASH-level track:
  two-phase (kick-the-tires, then full review), badges Functional, Reusable,
  and — via a Zenodo DOI deposit — Available.
- **An applied, breadth-first tradition.** PACMPL's scope line — "from design
  to implementation and from mathematical formalisms to empirical studies" —
  is OOPSLA's identity: experience reports, corpus studies, benchmark
  methodology, and human-aspects work all have verified precedent here, which
  is precisely where OOPSLA differs from theory-first POPL and
  implementation-performance PLDI.

Reviewing is double-anonymous and multi-stage; the Review Committee chairs
serve as PACMPL Associate Editors and rotate per volume (2026: Anders Møller
and Işıl Dillig). As of the check date, both 2026 rounds had closed and the
OOPSLA 2027 Round 1 call was **not yet posted** — its deadline is 待核实, not
"October 2026."

## The twelve skills

Campaign order, each linking to its neighbors:

- [`oopsla-topic-selection`](skills/oopsla-topic-selection/SKILL.md) — the
  center-of-mass test and SIGPLAN-family routing from OOPSLA's seat: POPL,
  PLDI, ICFP, Onward!, ECOOP, or an SE venue.
- [`oopsla-workflow`](skills/oopsla-workflow/SKILL.md) — the two-round clock:
  October-vs-March door choice, revision-path budgeting, the campaign state
  machine, and the rail to the SPLASH talk.
- [`oopsla-experiments`](skills/oopsla-experiments/SKILL.md) — matching
  evidence type to claim type across benchmarks, corpus studies, user
  studies, case studies, and mechanizations; sizing experiments to the round
  calendar.
- [`oopsla-reproducibility`](skills/oopsla-reproducibility/SKILL.md) — the
  SIGPLAN Empirical Evaluation Guidelines as an operational checklist:
  warmup, variance, corpus provenance, the reproducibility ledger, and a
  redeemable Data-Availability Statement.
- [`oopsla-writing-style`](skills/oopsla-writing-style/SKILL.md) — design
  insight before artifact, falsifiable claims, running examples that mark
  their own boundaries, journal pacing in 23 pages.
- [`oopsla-related-work`](skills/oopsla-related-work/SKILL.md) — PACMPL-era
  citation form (volume/issue/article), dblp verification against
  sibling-venue misattribution, per-line technical deltas.
- [`oopsla-supplementary`](skills/oopsla-supplementary/SKILL.md) — the
  body/appendix/artifact layering rule, anonymity for every byte, and
  appendices structured as promotable units for revision rounds.
- [`oopsla-submission`](skills/oopsla-submission/SKILL.md) — round selection,
  the 23-page anonymous `acmsmall` contract, the Data-Availability Statement,
  and the filing-day sequence on HotCRP.
- [`oopsla-review-process`](skills/oopsla-review-process/SKILL.md) — the
  four-outcome pipeline, reviewer continuity, and round-hopping mechanics,
  taught from the 2026 anchors.
- [`oopsla-author-response`](skills/oopsla-author-response/SKILL.md) — the
  per-round response window as a bucket argument: steering borderline papers
  toward revision outcomes instead of rejection.
- [`oopsla-camera-ready`](skills/oopsla-camera-ready/SKILL.md) — becoming a
  PACMPL article: reconciliation tables, de-anonymization, open-access steps,
  issue timing, and the SPLASH talk.
- [`oopsla-artifact-evaluation`](skills/oopsla-artifact-evaluation/SKILL.md)
  — kick-the-tires survival, the Functional/Reusable/Available ladder, Zenodo
  DOIs, and claim-to-artifact mapping.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) —
  every fact, its URL, its access date, and the 待核实 register.
- [`resources/external_tools.md`](resources/external_tools.md) — the live
  systems (track page, HotCRP, artifact track, ACM DL) and what to check in
  each.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — six
  dblp/ACM-DL-verified OOPSLA papers spanning the venue's contribution
  shapes, plus the misattribution cut list (WebAssembly→PLDI, gradual-typing
  →POPL, TypeScript→ECOOP...).
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional before/after rewrite from tool advertisement to design
  argument.
- [`resources/code/README.md`](resources/code/README.md) — pointer to the
  shared reproducibility kit with a PL-artifact translation table.

## Typical invocations

- *"Is this partial-verification tool paper OOPSLA or PLDI?"* →
  `oopsla-topic-selection`, then `oopsla-workflow` to pick a round.
- *"We got Major Revision in Round 1 — what now?"* → `oopsla-review-process`
  for the hop mechanics, `oopsla-author-response` if the window is still
  open, `oopsla-experiments` for the demand matrix.
- *"Audit this draft before the October deadline."* → `oopsla-submission`
  (format/anonymity/statement), `oopsla-reproducibility` (the four pillars),
  `oopsla-supplementary` (layering).
- *"We were accepted into OOPSLA2 — what happens before Oakland?"* →
  `oopsla-camera-ready` then `oopsla-artifact-evaluation`.

## Relationship to sibling packs

This pack is OOPSLA-specific and assumes the PACMPL two-round machinery
throughout. The single-deadline SIGPLAN siblings have their own packs (e.g.
`PLDI-Skills` in this repository) with different calendars, outcome spaces,
and evidence cultures; the venue-fit table in `oopsla-topic-selection` is the
hand-off point between them. For quick single-file venue profiles across all
of CS, see `Computer-Science-Conference-Skills`, whose OOPSLA entry is the
breadth version of what this pack covers in depth.

## Maintenance notes

- Everything dated here is a **2026-volume anchor**, not a standing rule.
  Outcome categories moved between 2025 and 2026 (Conditional Accept merged
  into Minor Revision); assume similar drift every volume.
- Before any deadline-sensitive advice: reopen the current OOPSLA track page,
  the HotCRP instance, and the SPLASH dates page; the source map lists what
  was and was not directly verifiable at build time.
- Round deadlines, page caps, response-window mechanics, artifact-track
  scheduling, APC amounts, and chair names all rotate per volume. The 待核实
  register in the source map is the first thing to retire as pages open.
