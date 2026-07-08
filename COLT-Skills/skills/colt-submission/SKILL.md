---
name: colt-submission
description: Use when auditing a COLT (Conference on Learning Theory) submission for CMT readiness, the 12-page PMLR-format main body, single-PDF assembly with unlimited appendix, double-anonymous formatting, the parallel-submission ban covering journals and proceedings venues, and the ordered final-week checks before the AoE deadline.
---

# COLT Submission

Run this audit before uploading a learning-theory paper to COLT. Every number below was
checked against the COLT 2026 Call for Papers on 2026-07-08; reopen the current CFP at
learningtheory.org before trusting any of it in a later cycle, because COLT republishes
its rules from scratch each year.

## What the 2026 cycle actually required

- Platform: Microsoft CMT, not OpenReview. The COLT 2026 site pointed authors to
  `https://cmt3.research.microsoft.com/COLT2026`. COLT has used other systems in the
  past, so never assume the portal — follow the link in the live CFP.
- Deadline: February 4, 2026, Anywhere on Earth, for the 39th edition (June 29 to
  July 3, 2026, San Diego). One deadline for the whole manuscript; the 2026 CFP had no
  separate abstract-registration step, unlike NeurIPS-style venues. Confirm each year.
- Length: main body at most 12 PMLR-formatted pages excluding references, with no page
  limit on references and appendices, all submitted as one PDF.
- Anonymity: submissions must be suitable for double-anonymous review; the official
  LaTeX template's `anon` option suppresses author names.
- Scope: theoretical aspects of machine learning at the intersection of computer
  science, statistics, and applied mathematics, explicitly including theory that
  explains empirical phenomena.

## The single-PDF discipline

Because the appendix rides inside the same PDF as the body, COLT has no separate
supplement portal to forget — but also no second chance to patch a broken proof file.
Treat the appendix as reviewable text, not as an attachment:

- Compile body plus appendix together and check the PDF page count where the 12-page
  boundary falls; references must start after the body, appendices after references.
- Nothing decision-critical may exist only in the appendix. A reviewer who stops at
  page 12 should already believe the theorem statements and the proof strategy.
- Anonymize the appendix with the same care as the body: acknowledgements, grant
  numbers, code URLs pointing at personal repositories, and PDF author metadata all leak.

## Illustrative template skeleton

The exact style file name changes with the year (e.g., a `colt2026` package for the
2026 cycle). Shape, not filename, is the stable part:

```latex
\documentclass[12pt]{article}
\usepackage[anon]{colt2026}   % 'anon' hides authors for review; drop it at camera-ready
\usepackage{times}

\title[Short Title]{Tight Rates for a Learning Problem}
\coltauthor{\Name{Anonymous Author} \Email{anon@example.org}}

\begin{document}
\maketitle
\begin{abstract}%
One-paragraph statement of the problem, the main theorem, and the technique.
\end{abstract}
% <= 12 PMLR-formatted pages of body
% \bibliography{refs}  -- references excluded from the limit
% \appendix            -- full proofs; no page limit, same PDF
\end{document}
```

Download the real template from the current CFP; do not reuse a prior year's file, and
never alter margins, font size, or spacing — layout tampering is a desk-reject risk at
any PMLR venue.

## Parallel-submission rules (verified for 2026)

The COLT 2026 CFP barred submissions substantially similar to papers previously
published, accepted for publication, or in parallel submission to other peer-reviewed
conferences with proceedings or to journals. It also barred sending a paper under COLT
review to a journal until decisions are released or the paper is withdrawn.

| Situation | COLT 2026 reading | Safe action |
|---|---|---|
| Same results on arXiv | Preprints are standard in the theory community | Post freely; do not cite your arXiv version in a way that de-anonymizes |
| Under review at a journal | Forbidden overlap | Withdraw one venue before the COLT deadline |
| Extended abstract at a proceedings venue (e.g., STOC/FOCS/ALT) | Forbidden if substantially similar | Differentiate results substantially or pick one venue |
| Non-archival workshop talk | Generally tolerated in theory culture | Verify the workshop is truly non-archival, then declare if the form asks |
| Journal submission planned after COLT decision | Explicitly allowed once decisions are out | Calendar the journal submission after notification |

## Desk-reject and severity triage

| Trigger | Severity | Window to repair |
|---|---|---|
| Body beyond 12 PMLR pages | Desk reject | Only before the deadline |
| Author names or acknowledgements left in | Desk reject or chair flag | Only before the deadline |
| Parallel-submission violation | Rejection at any stage, discoverable late | Withdraw the other venue now |
| Main theorem provable only via a gap-ridden appendix | Review-stage rejection | Fix during the proof-verification pass |
| Missing formal problem setup in the body | Review-stage damage | Fixable in the writing pass |

## Final-week sequence for a COLT paper

1. Freeze theorem and lemma statements; every later edit must be proofread against the
   appendix, because statement-proof drift is the classic COLT correctness kill.
2. Run a full proof-verification pass with a coauthor who did not write the proofs,
   checking each inequality and each invocation of an external result.
3. Rebuild the single PDF and verify the body/references/appendix boundary pages.
4. Sweep for identity: author macros, `\thanks`, metadata, repository links, and
   self-citation phrasing ("in our earlier work [3]" must become third person).
5. Enter CMT early — create the submission record days before February-style AoE
   cutoffs, since CMT accounts, conflict entry, and subject areas take time on first use.
6. Upload, re-download, and open the PDF that CMT stores; confirm it is the intended
   compile and the appendix rendered.

## CMT logistics worth doing early

- CMT accounts are per-email; make sure every coauthor's CMT identity uses their
  canonical email, since conflicts and the informed-AC anonymity model key off these
  records.
- Enter domain conflicts and coauthor conflicts completely — at a small venue an
  incomplete conflict list risks an actual conflicted reviewer, not a hypothetical.
- Subject-area selections steer reviewer assignment; pick the narrow area that names
  your subfield over the broad one that flatters the paper.

## Cycle-volatility warnings

- Deadline, portal, template name, page count, and anonymity mechanics are re-decided
  by each year's program chairs. The 2026 facts above are anchors, not permanent rules.
- Whether COLT runs an Open Problems track in a given year, and its separate
  deadline and non-anonymous format, must be re-checked in the current CFP
  (待核实 for any cycle after 2026).

## Output format

```text
[COLT readiness] Ready / Needs fixes / Not ready
[Blocking checks] <CMT record / 12-page body / single PDF / anonymity / parallel submission>
[Proof-integrity risk] <statement-proof drift, unverified lemma, external-result misuse>
[Desk-reject risk] <one issue>
[Fix order] <ordered actions before the AoE deadline>
```
