---
name: imc-submission
description: Use when auditing an ACM IMC submission for HotCRP readiness, covering the paper-registration step, the acmart template with BBL upload, the full/short page limits, double-blind anonymity including vantage-point details, the mandatory Ethics section, the artifact-availability declaration, cycle choice, and desk-reject triage before the AoE cutoff.
---

# IMC Submission

Run this audit before uploading to the IMC HotCRP site. IMC — the ACM Internet Measurement
Conference, sponsored by ACM SIGCOMM — judges a submission on **what it measured about the real
Internet and how**, so the mechanics below are where good measurement work is needlessly lost.
Every number was read from the IMC 2027 call and submission instructions, re-verified 2026-11-23
by direct page load (see `resources/official-source-map.md`); treat them as a one-cycle snapshot
and reopen the live pages first.

## Pick the cycle first

IMC runs **two deadlines a year** (IMC 2027: cycle 1 17 Nov 2026, cycle 2 7 Apr 2027, both
11:59PM AoE, hard deadlines with no extensions). This is a real choice, not a formality:

- The **One-Shot-Revision** path resubmits to the *next* deadline with the *same* reviewers, so a
  cycle-1 submission that earns a revision lands back in cycle 2. If your data collection finishes
  late, cycle 2 may be the honest target rather than rushing cycle 1.
- Registration precedes submission by a week (IMC 2027: register by 10 Nov 2026 for cycle 1,
  by 31 Mar 2027 for cycle 2). Miss registration and no PDF slot exists.
- A paper **rejected** at one deadline cannot come back at the next: roughly 12 months must pass
  since the last IMC deadline it was submitted to (a paper rejected in IMC 2026 cycle 2 can go to
  IMC 2027 cycle 2, not cycle 1). Format desk rejects are exempt.
- Each cycle has its own HotCRP instance (`imc2027-cycle1.hotcrp.com`, `imc2027-cycle2.hotcrp.com`).

## Format and page budget

- **ACM `acmart` template**, in the required review format, unmodified — the submission
  instructions give `\documentclass[10pt,sigconf,letterpaper,anonymous,nonacm]{acmart}`; Letter
  paper, 10-point font, numbered pages, PDF under 15 MB, abstract recommended at no more than
  200 words. This is the ACM path — do
  not carry an IEEE two-column habit across from a sibling networking venue.
- Upload the **BBL file** of your references on the reviewing system, as the submission
  instructions require — a missing BBL is a preventable processing failure.
- **Page budget (IMC 2027):** full papers **up to 13 pages** of technical content **+
  unlimited** references and appendices; short papers **up to 6 pages** of technical content +
  unlimited references and appendices. Any paper with **more than 6 pages of technical content is reviewed as a full paper**.
- The appendix is unlimited but **may not be used to dodge the body limit** — the page-limited
  body must be self-contained and decision-complete.

## Double-blind sweep (including infrastructure)

IMC uses **double-blind** review: no author names or affiliations, no identifying grant numbers,
and third-person references to your own prior work. Measurement papers leak identity in ways a
generic checklist misses:

```bash
# Mechanical pass on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|zenodo\.org/record|acknowledg|grant|@[a-z0-9.]*\.edu' | head
```

The measurement-specific leaks: a **vantage point** or testbed that only your group operates, an
AS number or probe hostname that names your institution, a RIPE Atlas measurement ID tied to your
account, a released-dataset URL on a personal or lab domain, and acknowledgements to the operators
who gave you access. Anonymize the *infrastructure description*, not just the byline. IMC's
anonymity guidelines do allow a narrow exception: naming a well-known but non-public capability
(a network telescope, an established measurement app) when blinding it would gut the paper — use
it rarely and only for that text; public platforms and datasets (RIPE Atlas, RouteViews) should
simply be named.

## The Ethics section is a gate

IMC requires a **clearly marked appendix section titled "Ethics"**; a paper without one **may be
rejected**. IMC 2027 makes it one of **three mandatory appendix sections** — **Ethics**, **Open
Science** (what artifacts will be released, or why not), and **Generative AI** (if, where, and how
generative AI was used; a footnote for small AI-generated text spans). These are the only
appendix sections reviewers are expected to read. The Ethics section is not boilerplate:

- **Human subjects / user data** (traffic, DNS queries, social data, credentials): document
  **IRB** approval or exemption, and attach the anonymized determination form if required. Reason
  explicitly against **Belmont Report** principles — respect for persons (consent), beneficence
  (risk vs. benefit), justice (who bears risk vs. who benefits).
- **Active measurement**: argue that probing does not harm targets or intermediary networks, name
  opt-out/blocklist handling, and rate-limit disclosure.
- **Vulnerability or exposure findings**: state a **responsible-disclosure** plan and its timeline.

Write this section early (see `imc-experiments`); ethics approvals cannot be retrofitted at the
deadline.

## Artifact-availability declaration

Every submission carries a declaration: **full**, **partial**, or **no** availability.

- Prefer **full**: an anonymized dataset/tool link the reviewers can inspect.
- **No availability** is acceptable *only* with a stated legitimate reason (proprietary data,
  privacy, legal) in a specific section — a silent "none" reads as a weakness.
- Accepted papers are **shepherded** to deliver what was promised, so do not over-declare.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over the page limit / appendix smuggling decision-critical content | Desk-reject-grade | Cut or restructure; the body must be self-contained |
| Template altered or wrong `acmart` format | Named desk-reject ground | Recompile clean; recover space editorially |
| Missing BBL upload | Processing failure | Generate and upload the BBL |
| Identity leak in PDF, dataset link, or vantage-point description | Anonymity violation | Re-anonymize infrastructure and links; scrub PDF metadata |
| **No Ethics section** | Named rejection ground | Add a real Ethics section; document IRB/disclosure |
| Missing Open Science or Generative AI appendix section (IMC 2027) | Mandatory-section gap | Add both sections, even if the answer is "none" |
| Human-subjects work without IRB documentation | Ethics failure | Obtain/attach the IRB determination |
| Not registered by the cycle's registration date | No submission slot | Nothing fixes this post-cutoff — calendar it now |

## Final-week order of operations

1. Freeze the measurement narrative early; the finding and its vantage points cannot churn.
2. Register title/abstract/authors/conflicts before the registration cutoff.
3. Write the Ethics, Open Science, and Generative AI appendix sections and confirm IRB/disclosure
   documentation is ready.
4. Build the anonymized dataset/tool link and set the availability declaration honestly.
5. Run the mechanical anonymity checks — including infrastructure — on the *final* PDF.
6. Upload the PDF **and the BBL**, fill every HotCRP field (topics, conflicts for every coauthor's
   institution and recent collaborators) a day early, then re-download and read the PDF cold.

## Reverify each cycle

- Exact deadline/registration dates and which cycle you are targeting.
- The page limits and `acmart` variant.
- Ethics-statement wording and the IRB-form requirement.
- Artifact-declaration options and any responsible-disclosure or AI-use rule — all cycle-volatile.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue imc-skills   # from a clone of the AJS repository
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
[IMC submission status] ready / blocked / needs work
[Cycle] deadline 1 / deadline 2, registered by the cutoff? yes/no
[Format] pages used (body/refs), acmart compliance, BBL uploaded?
[Anonymity] clean / leaks: <where, incl. vantage points>
[Ethics] section present? IRB/disclosure documented? yes/no
[Appendix] Open Science + Generative AI sections present? yes/no
[Availability] declaration full/partial/none + justification if none
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
