---
name: usenixsec-submission
description: Use when finalizing a USENIX Security Symposium submission — the per-cycle HotCRP site, the registration deadline a week before the paper deadline, the 13-page body plus mandatory Ethical Considerations and Open Science appendices, double-blind sweeps, and the early-reject exposure of a weak upload.
---

# USENIX Security Submission

Final gate before a paper enters a USENIX Security cycle. The numbers below are the
'26 and '27 cycle values read from usenix.org pages on 2026-07-08 (direct fetches of
usenix.org returned 403 in the verification environment, so pages were read through
search-engine renderings and cross-checked against the per-cycle HotCRP deadline
pages). Reopen the live CFP before trusting any date or cap.

## Two dates per cycle, and the first one bites

Every USENIX Security cycle opens with a **mandatory paper registration** roughly one
week ahead of the submission deadline. Registration creates the HotCRP record —
title, abstract, authors, topics, conflicts — and a paper that was never registered
cannot be uploaded later, no matter how finished the PDF is.

| Gate | Sec '26 Cycle 1 | Sec '26 Cycle 2 | Sec '27 Cycle 1 | Sec '27 Cycle 2 |
|---|---|---|---|---|
| Registration | Aug 19, 2025 | Jan 29, 2026 | Aug 18, 2026 | Jan 19, 2027 |
| Paper upload | Aug 26, 2025 | Feb 5, 2026 | Aug 25, 2026 | Jan 26, 2027 |
| Clock | 11:59 pm AoE | 11:59 pm AoE | 待核实 (assume AoE) | 待核实 (assume AoE) |

Each cycle runs its own HotCRP instance (the '26 sites were
`sec26cycle1.usenix.hotcrp.com` and `sec26cycle2.usenix.hotcrp.com`). Registering on
the wrong cycle's site is a real failure mode when both are open in overlapping
windows — confirm the URL against the CFP, not against a browser bookmark.

## The page geometry is unusual — learn it before the deadline

The '26 CFP fixed a structure that trips authors arriving from ACM venues:

1. Main body: at most **13 pages** in the unaltered USENIX Security LaTeX template.
2. Immediately after the body, **before the references**: a mandatory appendix titled
   **"Ethical Considerations"** and a mandatory appendix titled **"Open Science"**,
   each allowed up to one page.
3. References, then any optional appendices, with no page cap.

Both named appendices are required content, not decoration. A submission whose Open
Science appendix does not state where the artifacts supporting the paper live (or
justify why they cannot be shared) is out of policy, and paper acceptance is later
made conditional on the availability actually checking out (see
`usenixsec-artifact-evaluation`). Squeezing whitespace or altering the template is
explicitly forbidden.

## Anonymity, in USENIX Security's own terms

The '26 CFP names the leak vectors directly: author names, self-references phrased as
"we previously showed", funding acknowledgements, and GitHub repositories that
identify the group. Sweep for each of them plus the mechanical ones:

```bash
# Run on the exact PDF you intend to upload
pdftotext sub.pdf - | grep -nEi 'our (prior|previous) work|as we showed' | head
pdftotext sub.pdf - | grep -nEi 'github\.com/|gitlab\.|acknowledg|funded by' | head
pdfinfo sub.pdf | grep -Ei 'author|creator|producer'
grep -rEl 'institution|\\author' *.tex   # stray identity in source before rebuild
```

Artifacts referenced in the Open Science appendix must be reachable anonymously at
submission time — an anonymized mirror (e.g., a stripped repository on an anonymous
hosting service) rather than the lab's named organization.

## Early reject makes sloppy uploads expensive

USENIX Security notifies a first wave of rejections mid-cycle (Oct 7, 2025 and
Mar 17, 2026 in the '26 cycles). A submission that reads as unfinished, violates
format, or ducks the ethics discussion can exit at that gate without ever reaching
full committee discussion, and second-cycle rejects face resubmission restrictions
set by the next year's chairs. The audit below is cheaper than a lost cycle.

## Pre-upload audit order

1. Registration record complete and frozen: title, abstract (the real one — it
   drives reviewer bidding), all authors, topics, conflicts.
2. Rebuild the PDF from clean sources; confirm 13-page body, the two named
   appendices in position, references after them.
3. Run the anonymity greps above; treat every hit as a blocker.
4. Open every artifact URL from a logged-out browser session.
5. Confirm no concurrent submission of the same work elsewhere, in writing from
   every coauthor.
6. Upload early enough to re-download the PDF from HotCRP and read it cold.

## Reverify each cycle

- Registration/upload dates and the AoE convention (待核实 for '27 until the final
  CFP text is fetched directly).
- The 13-page cap and the one-page allowances for the two named appendices.
- The per-cycle HotCRP hostnames.
- Any new AI-assistance disclosure or submission-count rule (none confirmed for '27
  as of 2026-07-08 — 待核实).

## Output format

```text
[Cycle] target cycle + HotCRP URL confirmed against CFP
[Registration] complete / missing fields: <list>
[Format] body pages, appendix order, template integrity
[Anonymity] clean / blockers: <grep hits, artifact URLs>
[Ethics + Open Science] both appendices substantive: yes / no
[Verdict] upload / hold — with the fix list
```
