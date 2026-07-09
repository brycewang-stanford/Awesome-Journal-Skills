---
name: icdt-submission
description: Use when auditing an ICDT (International Conference on Database Theory) regular-paper submission for Microsoft CMT readiness, covering the two-step abstract-then-paper deadline in the correct submission cycle, the lipics-v2021 15-page limit excluding references, the clearly-marked appendix read at the PC's discretion, anonymous submission since 2024, the complete-proofs / full-version expectation, and which submission problems are unfixable after the AoE cutoff.
---

# ICDT Submission

Run this audit before uploading to **Microsoft CMT** for the International Conference on Database
Theory. ICDT is a **pure database-theory** venue: reviewers read for a precise theorem, a correct
proof, and a genuine advance in the foundations of data management, and they publish the result
**open access in LIPIcs** (Schloss Dagstuhl). Every number below was read on 2026-07-09 from the
ICDT 2026/2027 calls at `databasetheory.org` via search renderings (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call
first.

## Pick the right cycle first

ICDT runs **two submission cycles per year**, and choosing the cycle is the first decision, not a
detail:

- **Cycle 1** closes in the (northern) spring and **offers a revision option** — a first decision
  can be Accept, **Revise-and-resubmit**, or Reject.
- **Cycle 2** closes in the (northern) autumn; a paper **rejected in Cycle 1 may not be resubmitted
  to Cycle 2 unless the reviewers explicitly invited it.** Do not treat the two cycles as a free
  second attempt.

For ICDT 2027 (Lille), Cycle 1 papers were due **10 March 2026** and Cycle 2 papers **10 September
2026** (AoE); confirm the live dates. If your proof might still move, the earlier cycle's revision
round is worth more than a later raw submission.

## The two-step deadline

Each cycle separates an **abstract deadline** from the **paper deadline**, both AoE and about a
week apart (ICDT 2027 Cycle 1: abstracts 3 March 2026, papers 10 March 2026):

- Register the abstract with the real title and abstract — it drives PC bidding and conflict
  handling. A placeholder abstract worsens your reviewer match.
- Miss the abstract deadline and CMT will not accept the PDF later.

## Format and page budget

- **`lipics-v2021` LIPIcs document class, unmodified.** This is the Dagstuhl LaTeX style, not
  `acmart` and not `IEEEtran` — do not carry a PODS/SIGMOD `acmart` habit across.
- **At most 15 pages excluding references.** References do not count against the 15; nothing else
  escapes it except the appendix below.
- **A clearly marked appendix is allowed but read at the PC's discretion.** The main 15 pages must
  contain everything needed to *assess* the contribution; the appendix holds the full proofs a
  referee may check. **Online/external appendices are not allowed** — everything reviewed lives in
  the single submitted PDF.

## Complete proofs and the full version

ICDT expects **complete, checkable proofs**. A theorem stated without a proof a referee can verify
is the classic desk-level weakness at a theory venue:

- Put proof sketches and the main argument in the body; put the full details in the marked
  appendix so the paper is self-contained within one PDF.
- Maintain a **full version** (typically on arXiv) that will carry the complete proofs after
  review; reference it in the camera-ready, not in an anonymized submission if the link deanonymizes
  you.

## Anonymous-submission sweep (since 2024)

ICDT regular papers are **anonymous**: the PDF must not reveal authorship.

```bash
# Mechanical pass on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'acknowledg|grant|funded by|our (previous|earlier) (work|paper)|\bwe .* in \[[0-9]+\]' | head
```

- Remove author names, affiliations, and **acknowledgments to funding sources and collaborators**.
- Cite your own prior work in the third person ("Building on the construction of [17]…"), not "our
  earlier paper [17]."
- If you post a full version, do not let an arXiv link or an identifying system name reintroduce
  your identity into the anonymous PDF.
- Note the exception: the **Database Theory in Action** short-paper track is **not** anonymous —
  the anonymity rule is for the regular research track.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over 15 pages (excl. refs) | Format-reject-grade | Move detail to the marked appendix; tighten the body — refs do not absorb it |
| Class altered (margins, font, `\vspace` hacks) | Named format ground | Recompile clean `lipics-v2021`; recover space by editing, not by shrinking |
| A theorem with no verifiable proof anywhere in the PDF | Fatal at a theory venue | Add the full proof to the appendix before upload |
| Author identity leaks (names, acks, "our tool") | Anonymity violation | Re-anonymize; scrub PDF metadata; neutralize self-citations |
| Abstract not registered by the earlier deadline | No paper slot exists | Nothing fixes this post-AoE — calendar it now |
| Resubmitting a Cycle-1 reject into Cycle 2 uninvited | Against the cross-cycle rule | Do not; only resubmit if reviewers invited it |
| Same result under review at PODS/a journal | Concurrent-submission exposure | Withdraw one; check the current dual-submission wording |

## Final-week order of operations

1. Freeze the theorem statements early; the exposition can churn, the results cannot.
2. Register the abstract in the correct cycle before the earlier deadline.
3. Confirm every claimed theorem has a complete proof in the body or the marked appendix.
4. Run the anonymity sweep on the *final* PDF, including self-citation phrasing.
5. Fill every CMT field — subject areas that match your result, conflicts for each coauthor's
   institution and recent collaborators — a day early.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The cycle dates, which cycle you are targeting, and the revision-window length.
- The page limit and the required LIPIcs class revision.
- The anonymous-submission wording and any generative-AI disclosure rule (**待核实**).
- Whether the Database Theory in Action track runs and its separate rules.

## Output format

```text
[ICDT submission status] ready / blocked / needs work
[Cycle] 1 (revision-eligible) / 2 (no uninvited carry), abstract+paper registered? yes/no
[Format] pages used (body/refs), lipics-v2021 compliance, appendix marked?
[Proofs] every theorem has a checkable proof in-PDF? yes/no
[Anonymity] clean / leaks: <where>
[Fix queue] <ordered, with dates before the AoE cutoff>
```
