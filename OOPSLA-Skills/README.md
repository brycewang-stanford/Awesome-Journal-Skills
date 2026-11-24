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

Official basis: the pack now targets the **OOPSLA 2027** volume. Its call on
`2027.splashcon.org`, the SPLASH 2027 home, dates and organizing-committee
pages, the SPLASH 2027 artifact-evaluation call, and the `oopsla27.hotcrp.com`
front and deadlines pages were **re-verified on 2026-11-24** by direct fetch.
The 2026-volume sources (OOPSLA 2026 track page, `oopsla26.hotcrp.com`, the
TYPES/announce CFP, SPLASH 2026 pages, PACMPL Vol. 10 Issue OOPSLA1 front
matter, SIGPLAN series pages and Empirical Evaluation Guidelines) were checked
on 2026-07-08 through search-engine renderings, because the gateway then
returned HTTP 403; the full audit trail, including every item still marked
待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes OOPSLA structurally different

Six verified mechanics shape all twelve skills — and distinguish OOPSLA from
its single-deadline SIGPLAN siblings:

- **Two doors per year into one journal volume.** OOPSLA 2027 takes new
  papers in Round 1 (deadline October 14, 2026, AoE, firm — now closed) and
  Round 2 (April 7, 2027, AoE, firm), both via `oopsla27.hotcrp.com`. Round 1
  acceptances form Issue **OOPSLA1** (published no earlier than April 1,
  2027); Round 2 acceptances form Issue **OOPSLA2** (no earlier than
  October 1, 2027). For scale, the 2026 volume's OOPSLA1 issue held 75
  articles from 227 October-2025 submissions.
- **A four-way decision, not accept/reject.** Each round ends in Accept,
  Minor Revision (revise by the round's revision deadline or wait for the next
  round; absorbs the old "Conditional Accept", as in 2026), Major Revision, or
  Reject. New for 2027: a paper may be rejected after two clearly negative
  reviews without an author response, the chairs may desk-reject clearly
  below-bar papers, and no author may be on more than **5** submissions per
  round (at most 2 with no senior author).
- **Round-hopping is designed in.** A Major Revision is an invitation to
  resubmit to the *next* round against an explicit expectation list, keeping
  the same reviewers where possible — so an October submission that draws a
  Major Revision can still publish in the same year's volume via the April
  round. A Round 1 reject may not come back in Round 2. This pack teaches that
  calendar arithmetic explicitly.
- **A journal format with a revision bonus.** Submissions use single-column
  `acmsmall` (`review,anonymous` options), at most **23 pages** excluding
  references, required statements, and appendices; invited revisions get
  **25 pages**. A **Data-Availability Statement** is required before the
  references and does not count against the cap. Every paper also needs a
  senior author registered as a **reserve reviewer** (with exemptions).
- **A conference umbrella with its own geography.** Accepted papers present
  in person at SPLASH — in 2027: Prague, Czechia, October 10–15, co-located
  with MPLR and SAS (remote presentation not possible). SPLASH 2026 was in
  Oakland, October 4–9, 2026, alongside ISSTA 2026 and Onward!. Artifact
  evaluation runs as a SPLASH-level track for Accepted and Minor Revision
  papers: kick-the-tires, then full review; badges Available (DOI),
  Functional or Reusable, and Results Reproduced.
- **An applied, breadth-first tradition.** PACMPL's scope line — "from design
  to implementation and from mathematical formalisms to empirical studies" —
  is OOPSLA's identity: experience reports, corpus studies, benchmark
  methodology, and human-aspects work all have verified precedent here, which
  is precisely where OOPSLA differs from theory-first POPL and
  implementation-performance PLDI.

Reviewing is double-anonymous and multi-stage; the Review Committee chairs
serve as PACMPL Associate Editors and rotate per volume (2027: Nadia
Polikarpova and Ilya Sergey; 2026: Anders Møller and Işıl Dillig). As of
2026-11-24, OOPSLA 2027 Round 1 has closed (author response December 1–5,
2026) and **Round 2 (April 7, 2027) is the next open door**.

## The twelve skills

Campaign order, each linking to its neighbors:

- [`oopsla-topic-selection`](skills/oopsla-topic-selection/SKILL.md) — the
  center-of-mass test and SIGPLAN-family routing from OOPSLA's seat: POPL,
  PLDI, ICFP, Onward!, ECOOP, or an SE venue.
- [`oopsla-workflow`](skills/oopsla-workflow/SKILL.md) — the two-round clock:
  October-vs-April door choice, revision-path budgeting, the campaign state
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
  taught from the 2027 anchors.
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
- *"Audit this draft before the April deadline."* → `oopsla-submission`
  (format/anonymity/statement), `oopsla-reproducibility` (the four pillars),
  `oopsla-supplementary` (layering).
- *"We were accepted into OOPSLA2 — what happens before Prague?"* →
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

- Everything dated here is a **2027-volume anchor**, not a standing rule.
  Outcome categories moved between 2025 and 2026 (Conditional Accept merged
  into Minor Revision), and 2027 added submission limits and early/desk
  rejection; assume similar drift every volume.
- Before any deadline-sensitive advice: reopen the current OOPSLA track page,
  the HotCRP instance, and the SPLASH dates page; the source map lists what
  was and was not directly verifiable at build time.
- Round deadlines, page caps, response-window mechanics, artifact-track
  scheduling, APC amounts, and chair names all rotate per volume. The 待核实
  register in the source map is the first thing to retire as pages open.
