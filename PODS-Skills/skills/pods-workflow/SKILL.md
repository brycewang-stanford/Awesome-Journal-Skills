---
name: pods-workflow
description: Use when planning an ACM PODS project timeline across its multiple submission cycles per year, from venue fit through the EasyChair abstract-then-paper deadlines, the 48-hour rebuttal, the accept/reject/revision decision and shepherded revision round, PACMMOD-track publication, the arXiv full version, and presentation — with backward-planning offsets for a theory paper and honest handling of cycle choice.
---

# PODS Workflow

Use this as the project-management skill for a PODS submission. Replace every date with the current
official timetable and work backwards from the **abstract** deadline, which precedes the full-paper
deadline by about a week in each cycle. PODS runs **multiple submission cycles per year** and every
paper may hit a **revision** round with a shepherd, so plan for a two-round-per-cycle process, not a
single accept/reject.

PODS is a symposium whose papers are journal articles in the **PACMMOD PODS track**: it has **no
standing editor-in-chief** and no APC in the systems sense. Rotating leadership is the per-edition
PODS PC Chair (PODS 2026: Ke Yi, HKUST, verified 2026-07-09) appointed with ACM SIGMOD and SIGACT;
the cost model is registration and at least one author presents. Chairs rotate yearly — re-check the
organization page rather than carrying a name forward.

## Choosing a cycle

PODS's multi-cycle calendar is a planning lever, not just a constraint. As of 2026-07-09, PODS 2026
(Bengaluru) has already met, so the live target is **PODS 2027** (Huntington Beach): Cycle 1 closed
30 May 2026, and **Cycle 2 (abstract+COI 10 Oct 2026, paper 17 Oct 2026) is the next live deadline**.

- **Submit when the proof is complete, not when the cycle is nearest.** A rushed, gap-filled proof
  draws a reject that burns the cycle; PODS's next cycle is only a season away, so the cost of waiting
  one cycle is far smaller than at a once-a-year venue.
- **A reject cannot be immediately re-submitted.** Recent SIGMOD/PODS policy bars resubmitting
  rejected research-track work for roughly a year of cycles — so a premature submission can cost more
  than one cycle. Verify the exact wording before relying on the next cycle as a safety net.

## Milestones

- **Venue fit:** confirm PODS over SIGMOD/VLDB/ICDE and over ICDT (`pods-topic-selection`).
- **Result lock:** fix the model, the theorem statements, and complete every proof; the appendix is
  incorporated at submission, so proofs cannot be deferred to a later "full version."
- **Abstract + COI:** register the real title, abstract, authors, and declared conflicts of interest
  by the earlier abstract deadline of the chosen cycle.
- **Submission:** upload the anonymized `acmsmall` PDF (body + references + appendix) on EasyChair by
  the full-paper deadline.
- **Rebuttal:** use the ~48-hour window to correct factual misreadings only.
- **Decision:** accept / reject / **revision** (minor or major).
- **Revision (if invited):** implement the revision items within the given window; a shepherd judges
  whether the revision is satisfactory.
- **Acceptance:** prepare the PACMMOD camera-ready, post the **full version on arXiv**, register, and
  present at PODS.

## Backward plan from the paper deadline

| Weeks out (heuristic) | Theory-paper milestone |
|---|---|
| 10+ | Model and problem fixed; main theorem statements conjectured |
| 8 | Core proofs complete; lower-bound/upper-bound gap closed or scoped honestly |
| 6 | Full draft in `acmsmall`; every stated theorem has a complete proof in body or appendix |
| 4 | Appendix assembled and incorporated; anonymity sweep on paper and appendix |
| 3 | Internal read by a theory colleague who checks a proof end to end |
| 2 | Tighten definitions, related-work delta, page budget (15 pp excl. refs) |
| 1 | Final proof-read of the hardest proof; COI list prepared |
| 0 | Abstract by its earlier cutoff, then paper + appendix on EasyChair |

These offsets are planning heuristics only — anchor every one to the current Important Dates page,
never to a previous cycle's calendar.

## Failure modes by stage

- **A proof still open at week 6** forces a "sketch in the appendix" that the reviewers will not
  accept — the classic PODS reject in the making. Close the gap or scope the claim.
- **Leaving the appendix to the final week** produces incomplete proofs and identity leaks under
  double-anonymity (a named system, an acknowledgement).
- **Skipping the colleague read** forfeits the one chance to hear "your Lemma 4 is circular" from a
  friend instead of a reviewer.
- **Treating a revision as automatic** and under-budgeting the revision window turns a winnable
  minor revision into a reject when the shepherd is unsatisfied.

## Coordination notes

- Assign one author to own the proof appendix and its anonymity, and another to own the EasyChair
  fields and COI list; shared ownership is how both slip.
- Archive the exact submitted PDF and appendix — the revision round and the arXiv full version must
  correspond to them precisely.

## Output format

```text
[Current stage] idea / proofs / writing / abstract-registered / submitted / revision / accepted
[Chosen cycle] cycle 1 / cycle 2, with the next official deadline (date + source, or unknown)
[Critical path] <three tasks that determine readiness — usually a proof gap and the appendix>
[Risk register] <open proof / page budget / anonymity / revision window / arXiv full version>
[Owner map] <task -> person or role>
```
