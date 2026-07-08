---
name: isca-submission
description: Use when running the final pre-deadline audit of an ISCA submission — the two-step abstract-then-paper gate a week apart, the 11-page text limit with unlimited references, the template check, the double-blind sweep including PDF metadata and anonymized artifact links, and HotCRP form completion before AoE.
---

# ISCA Submission

This audit assumes the deadline is days away and the PDF nearly final. Every hard
rule cited below is the verified ISCA 2026 record (checked 2026-07-08); the 2027
guidelines were not yet posted at check time, so confirm each line against the
live `iscaconf.org` pages before trusting it (待核实).

## The two-step gate

ISCA 2026 collected **abstracts November 10** and **full papers November 17,
2025** — a seven-day gap with different stakes at each step:

- The abstract step registers title, abstract text, authors, topics, and
  conflicts in HotCRP. It is what reviewer assignment works from. Submitting a
  throwaway abstract and rewriting it at the paper step defeats its purpose and
  can misroute the paper to the wrong reviewers.
- The paper step uploads the reviewed PDF. New submissions cannot appear at this
  step — no abstract, no paper.
- Industry-track submissions ran on their own later pair (December 5 / December
  12, 2025); confirm which track's dates govern you.

Treat the abstract deadline as the real deadline for *decisions* (title, claim,
topic areas, author list, conflicts) and the paper deadline as the real deadline
for *evidence and prose*.

## Hard-format checklist, 2026 rules

| Item | 2026 rule | Check |
|---|---|---|
| Body length | ≤ 11 pages of single-spaced two-column text, references NOT counted | Count pages up to the bibliography start |
| References | Any number of pages | Never cut citations for space |
| Template | ISCA 2026 IEEE LaTeX template suggested for LaTeX users | Build from the official class, unmodified |
| File | Printable PDF | Fonts embedded; prints without errors |
| Portal | HotCRP (`isca2026.hotcrp.com` pattern) | Account, form, and upload confirmed — not just saved |

Page-limit recovery should come from cutting content, not squeezing geometry:
committees can and do check formatting mechanically, and a paper that reads as
crammed invites the question of what a revision could even absorb.

## Double-blind sweep — the three 2026-specific rules

The verified guidelines make three demands that trip authors coming from other
venues:

1. **No author names on any submitted document** — they exist only in the HotCRP
   form fields.
2. **PDF metadata must not give away authors.** LaTeX toolchains embed usernames
   and file paths; scrub and verify.
3. **Artifact links must be fully anonymized** (an anonymized repository service,
   not your lab's GitHub) — while **references must not be anonymized or
   omitted**. Blind the voice and the links, never the bibliography (details in
   `isca-related-work`).

```bash
# Mechanical anonymity + format pass on the final PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'     # metadata fields
pdftotext paper.pdf - | grep -nEi \
  'github\.com/(?!anonymous)|gitlab|acknowledg|funded by|grant' | head
pdftotext -f 1 -l 1 paper.pdf - | head -5                  # no names under title
pdffonts paper.pdf | awk '$5=="no"'                        # non-embedded fonts
# body-page count: note the page where references begin, compare to 11
pdftotext paper.pdf - | grep -n 'REFERENCES\|References' | head -1
```

Also sweep content-level identity: named internal clusters, institution-specific
trace names, acknowledgment stubs, and "as we showed in [7]" phrasing.

## The HotCRP form is a second document

Draft every field at the abstract step and re-verify at the paper step:

- **Title/abstract** — must match the PDF exactly; mismatches confuse bidding
  and look careless at the PC meeting.
- **Topics** — choose for the reviewer pool you want; a memory-hierarchy paper
  tagged only "accelerators" gets accelerator reviewers.
- **Authors and conflicts** — complete conflict declaration for *every* author:
  advisors, recent coauthors, institutional conflicts. Missing conflicts
  discovered later are an integrity problem, not a typo. Over-declaring to dodge
  specific reviewers is likewise detectable and sanctionable.
- **Declared coverage** — any dual-submission, prior-workshop, or extended-abstract
  history the current cycle's form asks about, answered literally.

## Final-72-hours run order

1. Freeze experiments; tag the repo at the commit producing every number in the
   PDF (`isca-reproducibility`).
2. Full read-through by a coauthor against the self-check lists in
   `isca-writing-style` and `isca-experiments`.
3. Run the mechanical pass above on the *final* build, not a near-final one —
   metadata regenerates on every compile.
4. Complete every HotCRP field; upload; confirm status shows submitted.
5. Download the PDF back from HotCRP and open it cold on another machine. The
   uploaded artifact, not your local file, is the submission.
6. Calendar the rebuttal/revision window now (mid-February to early March in the
   2026 cycle) so the team is staffed when reviews land (`isca-author-response`).

## Common last-week failures, ranked by frequency

- Abstract step missed entirely — authors tracking only the paper date.
- Metadata leak from a coauthor's build environment (fixed by one designated
  build machine).
- Un-anonymized artifact URL in a footnote added late.
- Topics chosen in five seconds, misrouting review assignment.
- HotCRP "draft saved" mistaken for "submitted" at 11:58 PM AoE.

## Audit output template

Fill this in and circulate to all coauthors before each of the two deadlines:

```text
[Gate] abstract step / paper step         [Deadline] <date, AoE-converted>
[Format] body pages: __ /11 · refs pages: __ (uncounted) · template: official
[Blinding] names=form-only · metadata=clean · artifact-links=anonymized ·
           references=INTACT
[HotCRP] title/abstract match PDF · topics deliberate · conflicts complete ·
         status=SUBMITTED
[Freeze] repo tagged at figure-producing commit · env image stored
[Open risks] <anything unresolved, with owner and hour-of-day plan>
```

Every rule above is one edition's snapshot from
`../../resources/official-source-map.md`. If the live 2027 pages disagree with
this file, the live pages win.
