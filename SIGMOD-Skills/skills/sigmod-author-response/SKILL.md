---
name: sigmod-author-response
description: Use when writing SIGMOD author feedback during a PACMMOD round or the revision letter after a major/minor-revision verdict, covering the mid-round feedback window, the four-page letter limit, per-reviewer change highlighting, the extra content page, and anonymity that must hold through resubmission.
---

# SIGMOD Author Response

SIGMOD gives authors two distinct speaking turns per round, and they play by
different rules. The mid-round **author feedback phase** (about a week, two
months after submission — e.g., Sep 10–17, 2026 for Round 3 of SIGMOD 2027) is
a short clarification exchange before first verdicts. The **revision letter**
accompanies a resubmission after a major or minor revision decision and is a
full engineering document. Confirm the current round's mechanics in the live
CFP before drafting either.

## Turn 1: the feedback phase

- Correct factual review errors first: a misread experiment, a baseline the
  reviewer missed, a theorem condition quoted wrong.
- Answer direct reviewer questions with pointers into the submitted PDF —
  section, table, and figure numbers, not paraphrase.
- Do not promise future experiments as if they were done; the revision phase
  exists precisely so that promised work can be delivered and re-checked.
- Preserve anonymity absolutely: no institutional context, no "in our
  production deployment at <company>" slips.
- Stay inside whatever length box CMT enforces this cycle; verify it live.

## Turn 2: the revision letter

A revision verdict at SIGMOD is an offer with a contract. For SIGMOD 2027:
the revised paper may add **one extra content page**, the letter runs up to
**four pages**, and every change must be highlighted in a **different color
per reviewer**, cross-referenced by section and page (line numbers when
possible).

| Letter component | What reviewers expect | Frequent failure |
|---|---|---|
| Change inventory | Requirement-by-requirement table, each mapped to an edit | Narrative essay with no map |
| Color key | One color per reviewer, stated up front | Uniform highlighting nobody can attribute |
| New evidence | Requested experiments actually run, numbers in the paper | Results only in the letter, not the paper |
| Declined requests | Explicit, reasoned, respectful refusal | Silent omission discovered on re-review |
| Locators | Section/page/line for every edit | "See revised Section 5" with no page |

## Revision triage order

1. Extract every sentence in the meta-review and reviews that states a
   requirement; number them R1.1, R2.1, and so on.
2. Classify each as: run new experiment / rewrite / clarify / decline.
3. Budget the single extra page before writing — decide which requirement
   owns it, because two half-answers waste it.
4. Draft edits in the paper first, the letter second; a letter written before
   the edits describes intentions, not changes.
5. Re-run the anonymity sweep on everything new: fresh plots, new repo
   snapshots, and added acknowledg— no, still none allowed.

## Skeleton letter

```text
Revision letter — Submission #NNN (Round k)
Color key: R1 = blue, R2 = orange, R3 = green.

R1.1 (required) "Compare against <baseline> on skewed workloads."
  Done. New Sec 6.4, Fig 9 (p. 11, blue). <Baseline> tuned per its
  authors' guidance; config in Appendix B.
R1.2 (suggested) "Discuss recovery cost."
  Added one paragraph, Sec 5.2 (p. 8, blue).
R2.1 (required) "Clarify the consistency guarantee under partition."
  Rewrote Sec 4.1 (p. 6, orange); the guarantee is unchanged, the prose
  overstated it. We now state exactly what is and is not guaranteed.
R3.1 (declined) "Port the engine to <other system>."
  We explain in Sec 7 (p. 12, green) why the design is engine-agnostic;
  a full port exceeds a revision cycle and does not test the claim.
```

## Deadline geometry

The revision window is one month (e.g., verdict Oct 19 → revised paper
Nov 19 for Round 3 of SIGMOD 2027), with the final accept/reject about three
weeks later. Reviewers evaluate only whether the stated requirements were
met — a revision is not an invitation to add a new contribution, and scope
creep reads as instability. Withdrawing instead of revising counts as a
rejection for the 12-month embargo, so price that before walking away.

## Feedback-phase micro-example

Reviewer question: "Figure 7 shows your system slower than Baseline B at low
thread counts — this seems to contradict the Section 3 claim."

Weak reply: "Thank you for the careful reading. Our system is designed for
high concurrency, and we believe the low-thread regime is less relevant in
practice."

Strong reply: "Sec 3's claim is scoped to contended workloads (p. 4, lines
12-14): under 8 threads there is no contention to remove, so we pay our
bookkeeping overhead (quantified at 4-7% in Tab 3) without benefit. Fig 7
is consistent with that scoping; we will make the boundary explicit in the
Fig 7 caption."

The strong version concedes the measured fact, cites its own scoping, and
prices the overhead — three moves in four sentences, no adjectives.

## Tone calibration for a systems audience

- Concede real bugs plainly and show the corrected numbers; database
  reviewers forgive errors faster than they forgive spin.
- Quantify every "we clarified" with what a reader can now compute or verify
  that they could not before.
- Never argue that a requirement is unreasonable in the feedback phase; argue
  it, if ever, in the letter with evidence.

## Output format

```text
[Phase] feedback window / revision letter
[Requirement ledger] Rk.n -> done / partial / declined, with locator
[Extra-page plan] which requirement owns the added page
[New-evidence risk] experiments promised vs. actually landed
[Anonymity re-check] pass or leak found in new material
[Send-readiness] ready / blocked on <item>
```
