---
name: rss-submission
description: Use when auditing an RSS (Robotics: Science and Systems) submission for OpenReview readiness — the RSS 2027 two-stage cascade (5+1-page Extended Abstract, then an 8-page-excluding-references final paper), double-blind compliance, PDF self-containment, the no-links-until-camera-ready rule, the hallucinated-citation desk reject, and dual-submission exposure.
---

# RSS Submission

Final-gate audit for an RSS submission. Every rule below was verified for the RSS 2027
cycle (CFP, Author FAQ and Reviewer Guidelines, read directly on 2026-11-24); reopen
the live CFP before enforcing any of it on a later cycle.

## The two-stage cascade (RSS 2027)

RSS 2027 replaced the single deadline + rebuttal with a shepherding process. All
cutoffs are 11:59pm AoE:

| Gate | 2027-cycle date | What locks |
|---|---|---|
| Stage 1 Extended Abstract | December 4, 2026 | The reviewed 6-page PDF (5 content + 1 references), authors, OpenReview record |
| Stage 1 decision | February 5, 2027 | Reject, or invitation to rebuttal with a Metareview |
| Rebuttal | February 12, 2027 | Your response to the Metareview (`rss-author-response`) |
| Stage 2 decision | February 26, 2027 | Reject, or the finalized Extension Charter |
| Final paper | April 16, 2027 | 8 pages excluding references, executing the Charter |
| Supplementary | April 19, 2027 | Zip, 100MB max (`rss-supplementary`) |
| Notification / camera-ready | April 30 / May 14, 2027 | Acceptance; final version |

Treat December 4 as the real gate: there is no separate abstract registration, no
supplement at Stage 1, and the author list given at Stage 1 is generally final
(changes need Program Chair approval justified by the Charter).

## Format audit

- **Stage 1 is 5 + 1, strictly.** Up to 5 pages of content and exactly 1 page of
  references. An appendix in the Stage 1 PDF must fit inside the 5 content pages;
  nothing beyond the 6 pages — websites, videos, code — is reviewed. It is a
  semi-complete technical paper: problem, hypotheses and methodology complete,
  experiments allowed to be preliminary, related work limited to the directly
  relevant citations. It is not a position paper.
- **Stage 2 is a ceiling, not a target:** at most 8 pages excluding references. The
  final paper is judged on whether it executed the Extension Charter; a well-run
  negative result is acceptable, padding is not.
- **Self-containment rule:** the main PDF must carry everything needed to evaluate the
  core methodology and insights. At Stage 2, reviewers are not obliged to read the
  supplement.
- **No external links:** project pages, hosted videos, and repos — even anonymous ones
  — are discouraged in the blinded submission and welcome only in the camera-ready.
- **Template and PDF:** use the RSS LaTeX or Word template unmodified (font, margins,
  spacing changes risk desk rejection), no page numbers or "Draft" markings, PDF only,
  Type-1 / embedded fonts.
- **Citations:** every reference must be real — RSS 2027 runs automated checks and
  desk-rejects papers with hallucinated citations. LLM use is otherwise permitted, and
  disclosing it is encouraged but not mandatory.

## Double-blind sweep

RSS 2027 review is double-blind (and signed after acceptance: reviewer names are
published with accepted papers' reviews). Sweep in this order, because robotics leaks
differently from ML:

1. **Footage and figures** — lab walls, robot decals, institutional colors, staff in
   frame. Robotics papers de-anonymize through pixels more often than through prose.
2. **Platform genealogy** — "our previously published gripper [12]" narrows authorship
   to one lab; rewrite as third-person hardware description.
3. **Metadata** — PDF author fields, video container tags, archive paths containing
   usernames.
4. **Prose** — acknowledgements (not allowed in the submission at all), grant numbers,
   dataset names unique to one group.

## Eligibility and overlap

- RSS 2027 forbids any overlap with another venue's review, even for a few days: a
  paper under review elsewhere (ICLR, ICRA, IROS, CoRL, a journal) must be withdrawn
  there *before* the December 4 submission (Author FAQ).
- arXiv preprints are allowed without citing them; posting or advertising one during
  review is at the authors' own anonymity risk.
- Work presented at venues without published proceedings (or abstracts only) may be
  submitted.

## OpenReview record audit

The 2027 venue group is `roboticsfoundation.org/RSS/2027/Conference`. Field errors are
self-inflicted desk risks; check each against the PDF:

- Title and abstract match the PDF character-for-character (search indexing and AC
  assignment both read the form, not the file).
- Author list complete *in the form* even though the PDF is anonymous — conflicts
  and reviewer assignment run off form metadata, and it is frozen after Stage 1.
- Every author has an OpenReview account with current affiliation and conflict
  domains; new profiles without an institutional email take up to two weeks.
- Subject areas chosen for the AC you want: they route the paper to its jury.

## Severity ladder

| Finding | Severity | Window to repair |
|---|---|---|
| Missed December 4 Stage 1 gate | Fatal for the cycle | None |
| Stage 1 over 5 content pages or over 1 reference page | Desk risk | Until December 4 |
| Hallucinated or unverifiable reference | Desk reject | Until the gate |
| Paper still under review elsewhere on December 4 | Policy violation | Withdraw first |
| External link in submitted PDF | Anonymity/desk risk | Until the gate |
| Final paper ignores an Extension Charter item | Stage 2 rejection risk | Until April 16 |
| Lab-identifiable footage in the Stage 2 supplement | Anonymity breach | Until April 19 |

## Last-72-hours sequence (Stage 1)

1. Freeze the hypothesis sentence and re-derive the title/abstract from it.
2. Fit the method, hypotheses and key preliminary evidence into 5 pages; references
   into 1.
3. Rebuild the PDF from clean sources; check author metadata is empty.
4. Resolve every citation against a real record (DOI, proceedings page, arXiv ID).
5. Enter OpenReview fields; confirm the abstract text matches the PDF verbatim.
6. Submit with hours of margin; AoE is generous but the robot is not the thing to be
   finishing at 11pm on deadline day.

## Notes that save a cycle

- Stage 1 rewards a sharp, testable hypothesis more than a finished result table: the
  review form scores *Value of Hypothesis* and *Feasibility of Conclusion*.
- Plan Stage 2 capacity now: the Extension Charter can require new or different
  experiments between February 26 and April 16, 2027 — keep the robot, data pipeline
  and people available.
- Reference pages are excluded from the Stage 2 8-page count; at Stage 1 they get
  exactly one page, so trim the bibliography to direct citations.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue rss-skills   # from a clone of the AJS repository
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
[Submission verdict] ready / needs fixes / not ready
[Gate status] stage-1 abstract <done/pending> | rebuttal <n/a/done/pending> | final paper <done/pending> | supplement <done/pending>
[Format risks] <pages / self-containment / links / template>
[Anonymity findings] <footage / genealogy / metadata / prose>
[Overlap exposure] <none / declared / unresolved>
[Fix order] <ranked list before the next gate>
```
