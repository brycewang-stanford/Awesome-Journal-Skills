---
name: colt-submission
description: Use when auditing a COLT (Conference on Learning Theory) submission for CMT readiness, the 12-page PMLR-format main body, single-PDF assembly with unlimited appendix, double-anonymous formatting, the parallel-submission ban covering journals and proceedings venues, and the ordered final-week checks before the AoE deadline.
---

# COLT Submission

Run this audit before uploading a learning-theory paper to COLT. Every number below was
checked against the COLT 2027 Call for Papers on 2026-11-23; reopen the current CFP at
learningtheory.org before trusting any of it in a later cycle, because COLT republishes
its rules from scratch each year.

## What the COLT 2027 call requires

- Platform: not yet announced — the COLT 2027 call says "Submission instructions coming
  soon" (2026-11-23). COLT 2025 and 2026 used Microsoft CMT, not OpenReview (2026:
  `https://cmt3.research.microsoft.com/COLT2026`, which the 2027 page still links as a
  leftover). COLT has used other systems in the past, so never assume the portal —
  follow the link in the live CFP once it is posted.
- Deadline: January 29, 2027, Anywhere on Earth, for COLT 2027, the 40th edition (June
  28 to July 2, 2027, Tokyo). One deadline for the whole manuscript; neither the 2026
  nor the 2027 call has a separate abstract-registration step, unlike NeurIPS-style
  venues. Confirm each year.
- Length: main body at most 12 PMLR-formatted pages excluding references and special
  sections such as an Ethics or AI statement, with no page limit on references and
  appendices, all submitted as one PDF.
- Anonymity: submissions must be suitable for double-anonymous review, refer to the
  authors' own prior work in the third person, and carry **no acknowledgments** (add
  them at camera-ready); the official LaTeX template's `anon` option suppresses author
  names.
- LLM use: the COLT 2027 LLM policy reads "Coming soon" (待核实). COLT 2026 allowed
  authors to use LLMs for writing, mathematics and research, encouraged mentioning
  unusual model contributions, and held authors responsible for correctness, including
  references.
- Attendance: at least one author of each accepted paper must attend in person.
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
2026 cycle; on 2026-11-23 the COLT 2027 call still linked the 2026 archive, so the 2027
package name is 待核实). Shape, not filename, is the stable part:

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

## Parallel-submission rules (verified for COLT 2027)

The COLT 2027 CFP, like the 2026 one, bars submissions substantially similar to papers previously
published, accepted for publication, or in parallel submission to other peer-reviewed
conferences with proceedings or to journals. It also bars sending a paper under COLT
review to a journal until decisions are released or the paper is withdrawn.

| Situation | COLT 2027 reading | Safe action |
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
5. Enter the portal early (CMT in 2025-2026; confirm for 2027) — create the submission
   record days before the January 29 AoE cutoff, since accounts, conflict entry, and
   subject areas take time on first use.
6. Upload, re-download, and open the PDF that the portal stores; confirm it is the intended
   compile and the appendix rendered.

## CMT logistics worth doing early (if 2027 stays on CMT)

- CMT accounts are per-email; make sure every coauthor's CMT identity uses their
  canonical email, since conflicts and the informed-AC anonymity model key off these
  records.
- Enter domain conflicts and coauthor conflicts completely — at a small venue an
  incomplete conflict list risks an actual conflicted reviewer, not a hypothetical.
- Subject-area selections steer reviewer assignment; pick the narrow area that names
  your subfield over the broad one that flatters the paper.

## Cycle-volatility warnings

- Deadline, portal, template name, page count, and anonymity mechanics are re-decided
  by each year's program chairs. The COLT 2027 facts above are read from the live call, not permanent rules.
- Whether COLT runs an Open Problems track in a given year, and its separate
  deadline and non-anonymous format, must be re-checked in the current CFP
  (2026: due May 25, 4 pages, non-anonymous; 待核实 for COLT 2027).

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue colt-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Output format

```text
[COLT readiness] Ready / Needs fixes / Not ready
[Blocking checks] <CMT record / 12-page body / single PDF / anonymity / parallel submission>
[Proof-integrity risk] <statement-proof drift, unverified lemma, external-result misuse>
[Desk-reject risk] <one issue>
[Fix order] <ordered actions before the AoE deadline>
```
