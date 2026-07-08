---
name: osdi-review-process
description: Use when reasoning about how an OSDI paper is reviewed and decided — the double-blind HotCRP PC pipeline with no author-response period, the two tracks, conditional acceptance with heavyweight shepherding, co-chair recusal, notification timing, and the Jay Lepreau Best Paper lineage.
---

# OSDI Review Process

Model the pipeline the paper enters at the December deadline. The process facts below
are the OSDI '26 cycle (verified 2026-07-08); OSDI re-decides its process per edition —
'26 itself removed the response period — so read the current CFP's process section
before predicting anything.

## The pipeline, author's-eye view

```text
Dec 11  submission complete on HotCRP (osdi26.usenix.hotcrp.com)
   |    double-blind PC review, typically multi-round:
   |      early round -> low-scoring papers exit with fewer reviews
   |      later round(s) -> surviving papers gather more reviews
   |    online discussion + PC meeting
   |    (no author-response step existed in the '26 cycle)
Mar 26  notification: accept | conditional accept | reject
   |    conditional: shepherd assigned, mandated-change list issued
Jun 9   shepherd-approved final paper due (or the acceptance lapses)
Jul 13  open-access proceedings live as the event opens
```

Round structure and reviewer counts are PC-internal and vary; what is stable is the
consequence: **the first two or three pages decide whether the paper earns the later
rounds**, because early-round reviewers triage a large pile (capped at eight
submissions per author, but multiplied across a big community).

## What "no response period" changes about review

OSDI '26 eliminated the author response. Reading the decision process correctly
means internalizing three shifts:

- **Reviewer misunderstandings are terminal.** A reviewer who misreads the threat
  model or misses the baseline's tuning carries that reading into discussion
  unchallenged. The only defense is prose that cannot be misread
  (`osdi-writing-style`'s objection pass).
- **The PC discussion is where papers are saved or sunk** — by other reviewers, not
  by you. A paper survives when its champion can answer objections *from the paper's
  own text*; write so a champion is armed.
- **Conditional acceptance absorbs the dialogue.** The conversation that a rebuttal
  would have hosted moves after the decision, into shepherding, where it has teeth:
  mandated changes, verified by a named shepherd, on a deadline.

## Conditional acceptance and heavyweight shepherding

OSDI '26 stated the mechanism plainly: some papers are accepted conditionally, and
will be **rejected unless the authors make the changes the PC determined**, completed
by the final-paper deadline and approved by the shepherd. Treat it as:

| Property | Practical meaning |
|---|---|
| The change list is a contract | Scope it line by line; ambiguities are resolved with the shepherd, in writing, early |
| The shepherd is the gatekeeper | Their approval — not your opinion of completion — converts conditional to accepted |
| June 9 is the enforcement date | New experiments mandated in April need the frozen testbed from the review window (`osdi-reproducibility`) |
| It is not a negotiation to reopen | Relitigating the reviews with the shepherd burns the one relationship that can accept the paper |

`osdi-author-response` covers how to run the exchange itself.

## Structural facts worth knowing

- **Two tracks, one PC decision process:** Research and Operational Systems papers
  are reviewed against different evidence expectations (novel design vs deployed
  experience) — know which bar your reviewers were told to apply.
- **Co-chair recusal:** OSDI '26 pre-committed that a submitting co-chair's papers
  are handled exclusively by the other co-chair under the same double-blind
  procedure — an unusually explicit conflict rule worth citing if conflict questions
  arise.
- **Best-paper lineage:** the **Jay Lepreau Best Paper Award** (inaugurated at OSDI
  '08) is selected by the PC from the accepted program; strong artifacts and clean
  claims correlate with it, but it is not something authors apply for.
- **Openness after decision:** accepted papers become free PDFs the day the event
  opens (USENIX open access) — reviews themselves stay confidential; OSDI does not
  publish reviews or decisions OpenReview-style.

## Surviving the triage round

Multi-round PC review means the paper's first job is to not exit early. What
early-round reviewers can actually evaluate in a large pile:

- **Pages 1–2 carry the whole argument** — pain, gap, named idea, headline evidence
  with its cost. A reviewer who stops at page 3 should already be wrong to reject.
- **The evaluation's table of contents** — skimmers check that the strongest
  baseline appears and that a cost/limitations discussion exists before reading any
  numbers; their absence is a triage-round exit.
- **Figure captions as a parallel paper** — early readers walk the figures; captions
  that state takeaways ("recovery flat from 8 to 64 nodes; baselines linear") let
  the skim reach the right conclusion.
- **Formatting smells** — cramped spacing, page-13 spillover, or an appendix where
  none is allowed mark the paper as careless before content is weighed
  (`osdi-submission`).

None of this is gaming; it is writing for the process that actually exists — one
with early exits and no author response to recover from a bad first impression.

## Reading a rejection usefully

Without a response phase, OSDI reviews are the *only* signal you get, so mine them:
recurring phrases across reviewers ("unclear workload realism," "incremental over X")
are the PC-meeting summary leaking through. Sort objections into fixable-by-writing,
fixable-by-experiment, and fit-level; the first two feed a SOSP/NSDI retarget within
months (`osdi-workflow`), the third sends you to `osdi-topic-selection` before any
retarget.

## Decoding the decision letter

Three outcomes, three very different next moves: a **clean accept** still usually
assigns a shepherd for lighter-touch final-version guidance — treat their
suggestions seriously even when not framed as mandates; a **conditional accept** is
a contract with a June enforcement date, decoded in the section above; a **reject**
with substantive, convergent reviews is the system working — the reviews are the
retarget's requirements document — while a reject with thin, scattered reviews
usually means a triage-round exit, and the fix is the paper's first two pages, not
its technical core.

## Output format

```text
[Phase] pre-decision / conditional / accepted / rejected
[Process facts confirmed live] response period? tracks? shepherding wording? (待核实 if unread)
[If pre-decision] top 3 misreadings the text invites (terminal without rebuttal)
[If conditional] change-list scoped? shepherd contact opened? June feasibility
[If rejected] objection triage: writing / experiment / fit + retarget call
```
