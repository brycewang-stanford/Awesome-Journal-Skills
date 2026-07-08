---
name: colm-review-process
description: Use when reasoning about how COLM reviews a paper — the OpenReview pipeline from late-March submission through the May review release, the May-June rebuttal window, July decisions, reciprocal-reviewing obligations, the LLM-use rules for reviewers, and how a three-edition-old venue's norms differ from mature conferences.
---

# COLM Review Process

COLM runs a compact, single-cycle-per-year pipeline on OpenReview, and — because the
venue is three editions old — its reviewing culture is still visibly under
construction. Understanding both the posted mechanics and the young-venue dynamics
is what lets authors time their effort correctly.

## The 2026 pipeline (verified 2026-07-08)

| Phase | 2026 dates | Author-side reality |
|---|---|---|
| Abstract deadline | March 26 | Drives bidding and reviewer matching |
| Full paper deadline | March 31 | Submission freezes |
| Review writing | April - mid-May | Silence; nothing actionable |
| Reviews released | May 22 | Read-only day one; no same-day replies |
| Rebuttal | May 22 - June 8 | The 18-day window where effort pays |
| AC discussion + decisions | June - July 8 | Decisions posted July 8 |
| Camera-ready | August 7 | Accepted papers finalize |
| Conference | October 6-9, San Francisco | Main program Oct 6-8, workshops Oct 9 |

On this pack's access date — July 8, 2026 — the pipeline is at its decision moment:
rebuttals are closed and notifications land today. If you are triaging an outcome,
go directly to `colm-camera-ready` (accept) or the resubmission logic below
(reject).

## Who reviews you, and why it feels different

Three structural facts shape COLM reviews:

- **A self-selected LM reviewer pool.** Everyone opted into a language-modeling
  venue, so you will rarely justify why LMs matter — but you will face specialists
  on contamination, harness quirks, and prompt sensitivity (`colm-experiments`
  lists exactly what they check).
- **Reciprocal reviewing feeds the pool.** COLM has per-submission and per-reviewer
  requirements, and any author with 4+ submissions is drafted automatically. Your
  reviewers are substantially *this year's authors* — practically minded, current,
  and reading many similar papers in a short window.
- **Young-venue variance.** With only two prior editions of precedent, calibration
  across reviewers is wider than at older venues: score meanings, appendix-reading
  habits, and rebuttal responsiveness vary. The rational response is to make the
  paper robust to the *strictest* plausible reviewer rather than tuning to an
  imagined average.

## Rules that govern the conversation

- **Double-blind, both directions** — reviewers and ACs cannot see author names;
  authors cannot see reviewer names. Anything that de-anonymizes you mid-process is
  a self-inflicted wound.
- **Code of Ethics scope** — it explicitly covers reviewing and paper discussion,
  and reviewers are encouraged to raise potential violations they see in papers.
- **LLM use in reviewing must be disclosed, whatever its size** — the 2026 policy
  draws the reviewer line stricter than the author line. As an author, this cuts
  two ways: a review may lawfully have LLM assistance behind it, and a review that
  looks LLM-generated without engagement is a legitimate thing to flag to the AC
  in the rebuttal, factually and without accusation theater.

## Reading a COLM review packet

Sort reviewer claims into four bins before writing anything:

```text
bin A  misreading           -> point to the page/table; cheapest wins first
bin B  evidence gap         -> runnable inside the 18-day window? do it
                               (cache-based analyses are fastest: colm-artifact-evaluation)
bin C  scope disagreement   -> reviewer wants a different paper; answer once,
                               crisply, and let the AC arbitrate
bin D  correct hit          -> concede, state the fix, thank them briefly
```

The AC synthesizing the discussion is your real audience (`colm-author-response`
handles execution). Between June 8 and July 8 the process belongs to reviewers and
ACs; there is no author-visible discussion phase to work.

## What the AC actually reads

Area chairs at a compact venue synthesize under time pressure, and their reading
order shapes what survives:

1. The reviews' *summary and score* fields — first impressions form here.
2. The rebuttal's opening lines per reviewer — which is why conclusion-first
   responses matter (`colm-author-response`).
3. Whether reviewers *reacted* to the rebuttal — an unanswered strong response
   still counts, but an acknowledged one counts double; polite nudge-questions to
   silent reviewers are legitimate inside the window.
4. The paper itself, selectively, where reviewers disagree.

Score arithmetic is a poor predictor at a young venue: with wide reviewer
calibration variance and no published acceptance rate (待核实), a 5-5-8 with an
engaged champion routinely beats a flat 6-6-6. Optimize for giving one reviewer
the material to argue your case in the discussion you cannot see, rather than for
moving every score by one point.

## If the decision is a reject

- Mine the reviews for the bin-D items; they transfer to any venue.
- The calendar is forgiving: a July 8 COLM decision precedes the autumn ICLR
  deadline and the following spring's NeurIPS cycle, and COLM 2027's expected
  late-March deadline (待核实) is a natural 8-month runway for a genuine revision.
- Re-run `colm-topic-selection` honestly — a common COLM reject pattern is a paper
  whose contribution was a task result wearing LM-analysis framing.

## Volatile every edition

- All dates above; the phase structure itself (COLM has already adjusted process
  details in each of its three editions).
- Reviewer-form contents, score scales, and any acceptance-rate figures (none
  officially published; 待核实).
- Reciprocal-reviewing thresholds and enforcement.

## Output format

```text
[Phase today] <where the current cycle actually is — verify against colmweb.org/dates.html>
[Packet triage] A: <n> misreadings / B: <n> evidence gaps / C: <n> scope fights / D: <n> hits
[AC-facing issue] <the one point the meta-review will turn on>
[Deadline math] <days left in the relevant window>
[Plan] <respond / experiment / concede / escalate-to-AC items, in order>
```
