---
name: usenixsec-submission
description: Use when finalizing a USENIX Security Symposium submission — the per-cycle HotCRP site, the registration deadline a week before the paper deadline, the 13-page body plus the mandatory Open Science appendix and the strongly encouraged Ethics appendix, double-blind sweeps, and the early-reject exposure of a weak upload.
---

# USENIX Security Submission

Final gate before a paper enters a USENIX Security cycle. The numbers below are the
USENIX Security '27 values, re-read directly from the live '27 Call for Papers on
2026-11-24 ('26 values kept for comparison). Reopen the live CFP before trusting any
date or cap.

## Two dates per cycle, and the first one bites

Every USENIX Security cycle opens with a **mandatory paper registration** one week
ahead of the submission deadline. In '27 registration fixes the title, the full author
list **with ORCIDs**, and the topics, plus a tentative non-blank abstract; a paper that
was never registered cannot be uploaded later, no matter how finished the PDF is. By
the submission deadline every author must also have an ORCID in their HotCRP profile
and confirm the submission terms, or the paper is not reviewed.

| Gate | Sec '26 Cycle 1 | Sec '26 Cycle 2 | Sec '27 Cycle 1 | Sec '27 Cycle 2 |
|---|---|---|---|---|
| Registration | Aug 19, 2025 | Jan 29, 2026 | Aug 18, 2026 | Jan 19, 2027 |
| Paper upload | Aug 26, 2025 | Feb 5, 2026 | Aug 25, 2026 | Jan 26, 2027 |
| Artifacts final (3-day grace) | — | — | Aug 28, 2026 | Jan 29, 2027 |
| Clock | AoE | AoE | AoE | AoE |

Each author may submit **at most seven papers per cycle** in '27; the check runs right
after submission and keeps the seven lowest submission numbers.

Each cycle runs its own HotCRP instance (the '27 Cycle 1 site is
`sec27cycle1.usenix.hotcrp.com`; the Cycle 2 link was not yet live on the call page on
2026-11-24). Registering on
the wrong cycle's site is a real failure mode when both are open in overlapping
windows — confirm the URL against the CFP, not against a browser bookmark.

## The page geometry is unusual — learn it before the deadline

The '27 CFP fixes a structure that trips authors arriving from ACM venues:

1. Main body: at most **13 pages**, excluding references and appendices, in the
   unaltered USENIX Security LaTeX template (US letter, two columns, 10-point Times on
   12-point leading, 7" x 9" text block).
2. A mandatory appendix titled **"Open Science"**, and — strongly encouraged but no
   longer mandatory in '27 — a well-labelled **"Ethics" / "Ethical Considerations"**
   appendix.
3. References and any optional appendices, with no length cap at submission; reviewers
   are not required to read appendices, so the paper must stand without them.
4. After acceptance the whole paper, appendices and bibliography included, must fit in
   **20 pages**.

The Open Science appendix is required content, not decoration. A submission whose Open
Science appendix does not state where the artifacts supporting the paper live (or
justify why they cannot be shared) is out of policy, and paper acceptance is later
made conditional on the availability actually checking out (see
`usenixsec-artifact-evaluation`). Squeezing whitespace or altering the template is
explicitly forbidden.

## Anonymity, in USENIX Security's own terms

The CFP names the leak vectors directly: author names, self-references phrased as
"we previously showed", funding acknowledgements, and artifact links or sites that
identify the group or track reviewers. Sweep for each of them plus the mechanical ones:

```bash
# Run on the exact PDF you intend to upload
pdftotext sub.pdf - | grep -nEi 'our (prior|previous) work|as we showed' | head
pdftotext sub.pdf - | grep -nEi 'github\.com/|gitlab\.|acknowledg|funded by' | head
pdfinfo sub.pdf | grep -Ei 'author|creator|producer'
grep -rEl 'institution|\\author' *.tex   # stray identity in source before rebuild
```

Artifacts referenced in the Open Science appendix must be reachable anonymously at
submission time — an anonymized mirror (the '27 CFP recommends
anonymous.4open.science with conference ID "SEC27") rather than the lab's named
organization. URLs are final at the paper deadline; the content may be uploaded during
the 3-day grace period and is frozen afterwards.

## Early reject makes sloppy uploads expensive

USENIX Security notifies a first wave of rejections mid-cycle (Oct 6, 2026 and
Mar 9, 2027 in the '27 cycles). A submission that reads as unfinished, violates
format, ducks the ethics discussion, or contains fabricated references can exit at
that gate — or be desk rejected — without reaching full committee discussion, and a
'27 Cycle 1 reject may not be resubmitted to '27 Cycle 2. The audit below is cheaper
than a lost cycle.

## Pre-upload audit order

1. Registration record complete and frozen: title, abstract (the real one — it
   drives reviewer bidding), all authors with ORCIDs, topics, conflicts.
2. Rebuild the PDF from clean sources; confirm the 13-page body, the Open Science
   appendix (and the Ethics appendix), and the PDF legible in grayscale.
3. Run the anonymity greps above; treat every hit as a blocker.
4. Open every artifact URL from a logged-out browser session.
5. Confirm no concurrent submission of the same work elsewhere, in writing from
   every coauthor.
6. Upload early enough to re-download the PDF from HotCRP and read it cold.

## Reverify each cycle

- Registration/upload dates (confirmed AoE for '27 on 2026-11-24).
- The 13-page cap, the 20-page camera-ready ceiling and which appendices are mandatory
  (the Ethics appendix became optional in '27).
- The per-cycle HotCRP hostnames (the '27 Cycle 2 site was not yet linked).
- The AI-use policy ('27: permitted, authors responsible, fabrication is misconduct) and
  the seven-papers-per-cycle cap.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue usenix-security-skills   # from a clone of the AJS repository
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
[Cycle] target cycle + HotCRP URL confirmed against CFP
[Registration] complete / missing fields: <list>
[Format] body pages, appendix order, template integrity
[Anonymity] clean / blockers: <grep hits, artifact URLs>
[Ethics + Open Science] both appendices substantive: yes / no
[Verdict] upload / hold — with the fix list
```
