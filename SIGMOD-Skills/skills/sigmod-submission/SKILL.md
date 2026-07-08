---
name: sigmod-submission
description: Use when readying a SIGMOD research-track submission for a PACMMOD round, covering the abstract-plus-COI pre-deadline, Microsoft CMT mechanics, the 12-page ACM-template limit, double-anonymous rules, the 10-paper author cap, the 12-month rejection embargo, and desk-reject hazards.
---

# SIGMOD Submission

Run this audit before a round deadline. SIGMOD research papers are journal
submissions to PACMMOD (Proceedings of the ACM on Management of Data), reviewed
in year-round batches rather than one annual cutoff, so the first question is
always "which round," not "which year." Reopen the live CFP for the cycle you
target before trusting any number quoted here.

## What must be true a week early

SIGMOD front-loads part of the deadline: the abstract and the declaration of
conflicts of interest are due roughly one week before the paper itself
(SIGMOD 2027: the 10th vs. the 17th of the round month, 11:59 PM AoE). Missing
the abstract stage closes the round entirely — there is no PDF-only entry.

- Register the submission in Microsoft CMT with final title, abstract,
  topic areas, and the complete author list.
- Declare COIs honestly and completely; PC assignment happens off this data.
- Count your load: SIGMOD 2027 caps each author at ten research-track
  submissions across all four rounds combined.
- Decide now whether a weak draft should wait a round; a rejection triggers
  a 12-month embargo, and a late withdrawal is treated as a rejection too.

## Format and anonymity gate

| Check | SIGMOD 2027 rule (verify per cycle) | Failure mode |
|---|---|---|
| Length | 12 pages max, unlimited pages for references | Desk reject |
| Template | Current ACM template, fonts/margins untouched | Desk reject |
| PACMMOD format | Only for final publication, never for submission | Confused reviewers, chair flag |
| Author identity | No names, affiliations, or funding acknowledgements | Desk reject |
| Colleague thanks | No research-group or collaborator acknowledgements | Anonymity violation |
| Self-references | Third person, no "our prior system" giveaways | Reviewer discount or flag |
| Artifacts | Links must not expose authorship or institution | Anonymity violation |

Note the asymmetry with one-shot conferences: because reviewing is
double-anonymous across the full round — including any revision phase — the
anonymity discipline must survive months, not weeks. Plan artifact hosting
accordingly.

## Exclusivity and overlap

PACMMOD requires substantial novel content and exclusive consideration: once
submitted, the paper (or anything with substantial overlap in results) stays
out of every other venue until PACMMOD rejects it or you withdraw. Rolling
PVLDB submissions of a sibling paper are the classic accidental violation —
map the overlap between your group's pipelines before the abstract stage.

## Round-selection judgment

- Submit to the earliest round the evidence genuinely supports; a revision
  verdict already builds in one more month of runway.
- Do not burn a round on a draft whose experiments are still moving — the
  embargo prices failure at three skipped rounds, not one.
- If a companion paper is in PVLDB's monthly queue, stagger topics so neither
  submission poisons the other's novelty claim.
- Check whether the industrial track fits better before defaulting to
  research; its calendar and rules are separate and single-shot.

## Ten-day countdown

```text
D-10  Freeze contribution claims; stop adding experiments
D-9   Abstract, author list, topics, and COIs into CMT
D-7   Anonymity sweep: PDF metadata, repo URLs, funding lines, cluster names
D-5   Rebuild every plot from committed scripts; diff against paper numbers
D-3   Full ACM-template compliance pass; reference pages excluded from count
D-2   Fresh-eyes read of pages 1-2 by someone outside the project
D-1   Upload final PDF; confirm CMT shows the intended file version
D-0   Re-download from CMT and open the PDF you actually submitted
```

## Round calendar snapshot (SIGMOD 2027, verified 2026-07-08)

| Round | Abstract + COIs | Paper due | First verdict |
|---|---|---|---|
| 1 | Jan 10, 2026 | Jan 17, 2026 | Apr 19, 2026 |
| 2 | Apr 10, 2026 | Apr 17, 2026 | Jul 19, 2026 |
| 3 | Jul 10, 2026 | Jul 17, 2026 | Oct 19, 2026 |
| 4 | Oct 10, 2026 | Oct 17, 2026 | Jan 19, 2027 |

All cutoffs 11:59 PM AoE. Source:
`https://2027.sigmod.org/calls_papers_important_dates.shtml`. Future cycles
will shift these dates; treat the pattern (quarterly rounds, abstract a week
early) as the durable part and the dates as perishable.

## Common desk-reject and triage patterns

- Page 13 of content because an appendix crept ahead of the references.
- A GitHub link whose organization name is the authors' lab.
- Abstract registered under a placeholder title that never got updated.
- The same experimental core simultaneously sitting in a PVLDB revision.
- An acknowledgements section pasted in from a camera-ready of prior work.

None of these are recoverable after the round deadline; all of them are
findable in an afternoon before it.

## PODS co-location caution

SIGMOD ships with PODS, the theory symposium, under one registration and one
week — but they are separate venues with separate CFPs, PCs, deadlines, and
publication series. Concretely:

- A theory-leaning paper does not "fall through" to PODS if SIGMOD rejects
  it; it must be submitted to PODS on PODS's own calendar.
- Do not cite SIGMOD round dates when planning a PODS submission, and vice
  versa; the calendars are unrelated.
- The exclusivity rule still applies across the pair — the same results
  cannot sit in both queues at once.

## Final self-audit, one minute each

- Open the uploaded PDF from CMT and read the title, author-block area, and
  page count with fresh eyes.
- Search the PDF text for your surnames, institution, and grant numbers.
- Click every URL in the paper from an incognito window.
- Confirm the abstract in CMT matches the PDF abstract verbatim.
- Confirm the round you think you entered is the round CMT shows.

## Output format

```text
[Round verdict] submit this round / hold one round / reroute track
[CMT gate] abstract+COI status, author cap headroom
[Format gate] pages / template / reference handling
[Anonymity gate] pass or the specific leak found
[Overlap gate] PVLDB or other-venue conflicts, embargo exposure
[Ordered fixes] <what to repair before the abstract stage>
```
