---
name: socc-submission
description: Use when auditing an ACM SoCC (Symposium on Cloud Computing) research-paper submission for HotCRP readiness, covering the two-round abstract+paper deadlines, the acmart/sigconf 12-page (full) or 6-page (short) budget with unlimited references, dual-anonymous review, the systems-and-data reproducibility posture, and desk-reject triage before the AoE cutoff.
---

# SoCC Submission

Run this audit before uploading to the SoCC HotCRP site (`socc26.hotcrp.com` for the 2026 cycle).
SoCC — the ACM Symposium on Cloud Computing — is the only venue **jointly sponsored by SIGMOD and
SIGOPS**, so your paper is read by both systems and data-management reviewers and must satisfy
both. Every number below was read from the SoCC 2026/2025 calls on 2026-07-09 via search
renderings of the `acmsocc.org` URLs (see `resources/official-source-map.md`); treat them as a
one-cycle snapshot and reopen the live call first.

## The two-round calendar (the distinctive SoCC deadline)

SoCC runs **two review rounds per year**, each with its own abstract, submission, author-response,
and notification dates. For SoCC 2026:

- **Round 1:** abstract 6 Feb 2026, paper 13 Feb 2026, response 12-14 Apr 2026, notify 29 Apr 2026.
- **Round 2:** abstract 7 Jul 2026, paper 14 Jul 2026 (AoE), response 10-12 Sep 2026, notify 26
  Sep 2026.

Two consequences to internalize:

- **Abstract registration precedes the paper by ~a week within the round.** Register the real
  title and abstract; the abstract drives reviewer bidding.
- **A Round-1 reject cannot be resubmitted to Round 2** of the same year. Choose the round you are
  genuinely ready for — a rushed Round-1 submission does not buy a cheap second attempt months
  later. Verify the exact dates and the no-resubmission rule on the live HotCRP deadlines page.

## Format and page budget

- **ACM Primary Article Template**, `sigconf` proceedings format, submitted anonymized:
  `\documentclass[sigconf, anonymous]{acmart}`, **9pt**. This is the ACM `acmart` path — not the
  USENIX template that OSDI/NSDI/ATC use. Do not carry a USENIX-format habit across.
- **Page budget (verify per cycle):** **full research papers 12 pages** for all text and figures,
  **plus unlimited references**; **short research papers 6 pages** plus unlimited references. The
  unlimited-reference allowance is generous — but everything a reviewer must read to judge the
  paper lives in the 12 (or 6) pages, not in an appendix.
- Single PDF, US-Letter, ≤10 MB. Margins, font, and spacing are fixed by `acmart`; recover space
  by editing, not by tampering with the template.

## Dual-anonymous sweep

SoCC review is **dual-anonymous**: reviewers do not see authors and authors do not see reviewers.
Because cloud-systems papers lean on deployments, traces, and named infrastructure, the leak
surface is wide:

```bash
# Mechanical pass on the submission PDF and any released artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|zenodo\.org/record|our (cluster|company|team|deployment)|acknowledg|grant' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/|internal' | head
```

The SoCC-specific leaks: a cluster or datacenter name, a cloud provider or product hint that only
your team runs, a trace named after your organization, a system named after your lab, and a
data-availability link pointing at a personal or corporate repository. Anonymize traces and
re-host artifacts behind an anonymizing service *before* upload.

## Reproducibility posture at submission time

SoCC is a systems-and-data venue; reviewers expect an inspectable evidence trail:

- Describe the **testbed / cluster**, the **workloads or traces**, and the **measurement scripts**
  that produce the paper's figures — enough that a reviewer believes the numbers are reproducible.
- Provide an **anonymized** artifact link or archived supplement where possible; released code,
  workload generators, and traces strengthen both the systems and the data reading of the paper.
- If a production trace or deployment cannot be shared (confidentiality), say so and why, and give
  what can be shared (a synthetic generator, aggregate statistics).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Main text over the 12/6-page budget | Desk-reject-grade | Cut or compress; unlimited references do not absorb body text |
| Wrong template (USENIX habit) or altered acmart | Named desk-reject ground | Recompile clean in `acmart` sigconf 9pt |
| Identity leak in PDF, trace name, cluster, or system name | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Abstract not registered by the round's earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| Round-1 reject reused in Round 2 | Policy violation | Not allowed same year; reroute or wait a full cycle |
| Same work under review elsewhere | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Freeze the system and the measurements early; text can churn, the numbers cannot.
2. Register title/abstract/authors/conflicts before the round's abstract cutoff.
3. Assemble the anonymized artifact (trace-replay harness, testbed scripts) and place its link in
   the paper.
4. Run the mechanical anonymity checks on the *final* PDF and the *final* archive, not drafts.
5. Fill every HotCRP field — subject tags matching both the systems and data facets, conflicts for
   every coauthor's institution and recent collaborators — a day early.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- The number of rounds, both rounds' dates, AoE cutoffs, and the no-cross-round-resubmission rule.
- The page budget and which acmart revision / font size is required.
- Rebuttal format, artifact-track existence and timing, dual-submission wording, and any
  AI-disclosure rule — all cycle-volatile; none should be assumed stable.

## Output format

```text
[SoCC submission status] ready / blocked / needs work
[Round] round 1 / round 2; abstract + paper registered by the round's cutoffs? yes/no
[Format] pages used (body only), acmart sigconf 9pt compliance
[Anonymity] clean / leaks: <where: trace/cluster/system/link>
[Reproducibility] testbed + workloads described? artifact link present?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
