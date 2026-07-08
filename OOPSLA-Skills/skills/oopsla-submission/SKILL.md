---
name: oopsla-submission
description: Use when preparing or auditing an OOPSLA submission — picking between the two yearly PACMPL rounds, meeting the 23-page acmsmall anonymous format, writing the required Data-Availability Statement, clearing double-anonymous and concurrent-submission checks, and filing correctly on HotCRP before a firm AoE deadline.
---

# OOPSLA Submission

OOPSLA accepts new papers into either of two yearly rounds feeding the PACMPL
OOPSLA volume; for the 2026 volume the rounds closed October 10, 2025 and
March 17, 2026, both 11:59:59 PM AoE and explicitly firm, via
`oopsla26.hotcrp.com`. Before running this audit, confirm which round is
actually open on the current SPLASH track page — as of 2026-07-08 both 2026
rounds had closed and the 2027 Round 1 call was not yet posted (待核实).

## The three questions that precede any checklist

1. **Which round?** A round is a strategic choice, not just a date. Filing in
   the earlier round leaves the later round of the *same volume* available for
   a Major-Revision resubmission; filing in the later round pushes any Major
   Revision into next year's volume. See `oopsla-workflow` for the calendar
   math.
2. **New paper or invited revision?** A Major-Revision invitation must come
   back as a revision in the designated round, answering the reviewers'
   expectation list — never re-filed as a fresh submission. Mixing these up
   forfeits reviewer continuity.
3. **Is the evidence finished?** The two-round model gives reviewers a
   revision lever; an evaluation you plan to "complete during review" invites
   exactly that lever to be pulled against you.

## Format contract (2026 volume)

| Rule | Value | Consequence of violating |
| --- | --- | --- |
| Class options | `acmsmall,screen,review,anonymous` on `acmart` | Wrong template reads as non-compliant at triage |
| Initial submission cap | 23 pages, excluding references, required statements, appendices | Over-cap papers risk rejection without review |
| Invited-revision cap | 25 pages, same exclusions | Extra two pages exist to *answer reviewers* |
| Data-Availability Statement | Required, placed before the references, not counted | Missing statement is an avoidable flag |
| Anonymity | Double-anonymous, multi-stage | Identity leaks void the review contract |

## Anonymity sweep beyond the obvious

- Tool and prototype names that are already public: rename or cite in the
  third person, and scrub GitHub organization strings from listings.
- The Data-Availability Statement itself must stay anonymous — point to an
  anonymized archive, not a lab server whose hostname names your group.
- PDF metadata (`pdfinfo` shows author fields LaTeX quietly embeds), embedded
  figure paths, and acknowledgment stubs left from a prior journal draft.
- Self-citation grammar: "we extended X [12]" de-anonymizes; "this work builds
  on X [12]" does not.

## Concurrent-submission and prior-work posture

Declare any overlapping manuscript honestly. The dangerous case at OOPSLA is
the *sibling-venue loop*: a rejected PLDI or POPL version resubmitted with the
same evaluation weaknesses — reviewer pools overlap, and the two-round model
means the same people may see the paper twice within one year. Fix what the
last venue's reviews established before re-entering the family.

## Filing-day sequence

```text
T-3 days   Freeze claims; regenerate all numbers from the artifact
T-2 days   Anonymity sweep (text, metadata, statement, supplement)
T-1 day    HotCRP record: title/abstract match PDF, topics, conflicts,
           all authors listed with institutions in the form only
T-0        Upload PDF + supplement; re-download and open both;
           confirm timestamp shows AoE margin, not local-time optimism
```

Deadlines being firm means the plan needs no heroics on the final night; if
the paper is not assembled at T-3, target the next round instead — with two
rounds a year, the cost of waiting is months, not a year.

## Output format

```text
[Round] <target round + deadline, from the live track page>
[Filing type] new submission / invited revision
[Format] pass / fail per contract row above
[Anonymity] clean / leaks found: <list>
[Statement] Data-Availability Statement present and anonymous: yes/no
[Verdict] file now / fix list / wait for next round
```
