---
name: ndss-submission
description: Use when performing the final pre-upload audit of an NDSS submission — HotCRP fields, the AoE deadline, NDSS template and 13-page compliance, double-blind sweep, ethics readiness, the six-per-author cap, overlap rules, and desk-reject triage in the last week.
---

# NDSS Submission

This is the deadline-week skill: the paper exists, the cycle is chosen, and the job is to
get it into HotCRP without handing the PC a reason to discard it unread. NDSS 2027's summer
cycle ran through `ndss27-summer.hotcrp.com`; confirm the fall cycle's own site rather than
assuming the URL pattern (待核实 in this pack's source map).

## The clock

Deadlines are **11:59 PM Anywhere-on-Earth (UTC-12)** — the most forgiving timezone, which
is exactly why missing it is unforgivable. Fall 2027 cycle: papers due **August 19, 2026**.
Upload a complete candidate PDF a day early; HotCRP allows revision until the deadline, and
a placeholder in the system beats a perfect PDF stuck in a build error at 11:58.

## Hard-gate audit (any failure = fix before upload)

- **Template**: current NDSS template, unmodified — no geometry, spacing, or font surgery.
- **Length**: ≤13 pages of body; Ethics Considerations, references, and appendices sit
  outside the count and *behind* the body/ethics/references order the CFP prescribes.
- **Language**: English; PDF compiles on someone else's machine, fonts embedded.
- **Anonymity** (double-blind, per the 2027 CFP):
  - no author names/affiliations anywhere, including headers and the PDF's metadata
    (`pdfinfo`; check Author, Creator, and attached-file fields);
  - self-citations in third person; no "our earlier system [12]";
  - acknowledgments, grant numbers, and lab codenames removed;
  - artifact links point at anonymized hosting, not institutional GitLab;
  - figures and screenshots checked for usernames, hostnames, watermarks.
- **Ethics readiness**: if the work touches live systems, users, or vulnerabilities — the
  Ethics Considerations section exists, the disclosure state is described truthfully, and
  the paper can face the Ethics Review Board as-is. IRB paperwork alone is not the answer
  the venue accepts.
- **Cap and overlap**: every coauthor is on ≤6 submissions this cycle (12/year), and this
  paper does not majorly overlap a paper rejected in this symposium's earlier cycle, nor
  sit simultaneously under review elsewhere.

## Desk-reject triage

| Finding in final week | Severity | Move |
| --- | --- | --- |
| Body runs to page 14 | Fatal at deadline | Cut via the dependency test (`ndss-supplementary`), never via template hacks |
| Metadata shows an author name | Fatal if unseen | Rebuild PDF with scrubbed fields; re-check attachments |
| De-anonymizing repo link | Fatal if unseen | Re-host anonymously; re-grep the whole PDF for URLs |
| Undisclosed overlap with rejected summer paper | Fatal | Withdraw or rewrite scope honestly — reviewers overlap between cycles and remember |
| Ethics section missing for scanning study | Severe | Write it now from the method text; do not submit without it |
| HotCRP topics/conflicts incomplete | Recoverable | Complete before deadline; conflicts protect you |

## HotCRP field discipline

Abstract, title, topics, and conflicts steer reviewer assignment — treat them as targeting,
not paperwork. The abstract in the form must match the PDF verbatim (mismatches surface at
Round 1 and read as sloppiness). Declare conflicts by the CFP's definition, completely: a
missed conflict discovered later taints the review; an invented one to dodge a feared
reviewer is misconduct. List every coauthor with correct emails at submission — quiet
author-list edits after the deadline are a chairs-permission matter at security venues,
not an author right.

## Final 48 hours, in order

```text
T-48h  freeze content; branch the repo (submission tag)
T-36h  format pass: template diff, page count, reference/appendix order
T-30h  anonymity pass: metadata, links, figures, self-citations, acks
T-24h  ethics pass: section present, disclosure statements current TODAY
       (a vendor reply yesterday can invalidate a sentence written last week)
T-20h  upload candidate PDF to HotCRP; fill all fields; save
T-12h  cold read of the compiled-from-HotCRP download (not your local file)
T-2h   final re-upload if needed; screenshot the confirmation
```

## After the button

Nothing more is owed until the early-reject notification (fall: September 25, 2026). Use
the gap to pre-draft rebuttal scaffolding (`ndss-author-response`) and to keep the
disclosure process moving — the interactive discussion phase will ask what happened since
submission, and "the vendor patched in October" is a good answer only if you kept the
process alive.

## Output format

```text
[Upload state] candidate in HotCRP? fields complete?
[Hard gates] template / length / anonymity / ethics / cap+overlap — pass or blocker
[Triage] findings mapped to the table above, with owners
[Clock] hours to AoE deadline; next checkpoint
```
