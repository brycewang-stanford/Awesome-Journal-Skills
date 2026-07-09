---
name: conext-submission
description: Use when auditing an ACM CoNEXT submission for HotCRP readiness, covering the choice between the December and June cycles, the mandatory paper-registration step, the ACM acmart page budget (long ≤16 + ≤4 appendix; short ≤10 + ≤2 appendix), double-anonymous review, the reproducibility badge opt-in due at submission, PACMNET publication, and desk-reject triage before the cutoff.
---

# CoNEXT Submission

Run this audit before uploading to the CoNEXT HotCRP site. CoNEXT research papers are published as
**journal articles in PACMNET** (Proceedings of the ACM on Networking), so the submission is judged
like a journal manuscript that also earns a conference slot. Every number below was read from the
CoNEXT 2026 call and the CoNEXT 2025 CFP on 2026-07-09 via search renderings (see
[`../../resources/official-source-map.md`](../../resources/official-source-map.md)); treat them as a
one-cycle snapshot and reopen the live call first.

## Pick the cycle first

CoNEXT runs **two submission cycles a year**, and choosing the wrong one costs months:

- The **December cycle** (for CoNEXT 2026: registration 5 Dec 2025, submission 12 Dec 2025) gives
  an earlier notification (31 Mar 2026) and, if you earn a major revision, a spring resubmission
  path.
- The **June cycle** (submission 5 Jun 2026) is the later entry point into the *same* annual program
  and the same rolling PACMNET volume.

Both feed one conference and one journal volume, so the decision is about *readiness and calendar*,
not prestige — submit to the nearer honest deadline your evidence is actually ready for. See
[`conext-workflow`](../conext-workflow/SKILL.md) for the full backward plan from each cutoff.

## The two-step deadline within a cycle

CoNEXT separates **paper registration** from **paper submission**:

- **Registration** locks in title, abstract, authors, and conflicts a week early (December cycle:
  5 December 2025). Miss it and the system will not accept the PDF later.
- **Submission** uploads the anonymized PDF (December cycle: 12 December 2025).

Register with the *real* title and abstract, not a placeholder — the abstract drives reviewer
bidding, and a registered abstract that diverges from the final paper quietly worsens your TPC
match.

## Format and page budget

- **ACM `acmart` template**, unmodified. This is the ACM path — do not carry an IEEE two-column
  habit over from a sibling venue's kit.
- **Page budget (verify per cycle; 2025 numbers, 待核实 for 2026):**
  - **Long papers:** ≤ **16 pages** of text and figures, **unlimited references**, up to **4 pages
    of appendices**.
  - **Short papers:** ≤ **10 pages** of text and figures, **unlimited references**, up to **2 pages
    of appendices**.
- Appendices are for material that supports but does not decide the paper; nothing a reviewer must
  read to accept the paper should live only in an appendix or the artifact (see
  [`conext-supplementary`](../conext-supplementary/SKILL.md)).

## Double-anonymous sweep

CoNEXT runs **double-anonymous** review: authors and reviewers are mutually hidden. Because
networking papers lean on testbeds, deployments, traces, and operator relationships, the leak
surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant|our (testbed|deployment|university)' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/' | head
grep -rniE 'university|@[a-z0-9.]+\.edu|internal hostname|AS[0-9]+ .*our' artifact/ --include='*.md' | head
```

The networking-specific leaks: a testbed or deployment named after your lab, a topology figure
showing internal hostnames or an AS you operate, a trace whose capture point identifies your
institution, a data-availability link pointing at a personal GitHub, and commit metadata inside a
zipped repository. Re-host artifacts behind an anonymizing service *before* upload.

## Reproducibility opt-in at submission time

The optional ACM reproducibility badges are administered by CoNEXT's **reproducibility committee**,
and the critical timing trap is here:

- You must **opt in for ACM badging before the paper submission deadline** — it cannot be added
  later.
- Within a week of acceptance you send a **one-page** artifact description with pointers to code and
  other artifacts.
- Even if you skip badging, include a data-availability posture: pinned traces/configs and a
  runnable artifact strengthen the review (see [`conext-reproducibility`](../conext-reproducibility/SKILL.md)).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Main text over the page budget | Desk-reject-grade | Cut or move to the appendix; references are unlimited but do not absorb body text |
| Template altered (margins, shrunk font, wrong `acmart` option) | Named desk-reject ground | Recompile clean, recover space editorially |
| Identity leak in PDF, artifact, topology figure, or testbed name | Anonymity violation | Re-anonymize and re-host; scrub PDF metadata |
| Abstract/paper not registered by the earlier date | No submission slot exists | Nothing fixes this post-deadline — calendar it now |
| Wanted a badge but did not opt in before submission | Ineligible for badging | Opt in *now*, before the cutoff |
| Same study under review at SIGCOMM/NSDI/IMC | Dual-submission exposure | Withdraw one venue; verify the current concurrent-submission wording |

## Final-week order of operations

1. Confirm which cycle (December/June) you are targeting and its exact cutoff and time zone.
2. Freeze the body early; references can churn, the argument cannot.
3. Register title/abstract/authors/conflicts well before the registration cutoff.
4. Decide badging and **opt in before submission** if you want it.
5. Build the anonymized artifact and place its (anonymized) link in the paper.
6. Run the mechanical anonymity checks on the *final* PDF and the *final* archive, not drafts.
7. Fill every HotCRP field — topics that match your evidence, conflicts for every coauthor's
   institution and recent collaborators — a day early; late conflicts are the classic midnight
   failure.
8. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Both cycles' exact dates and time zones, and which cycle you are entering.
- The page budget and which `acmart` variant is required.
- Appendix handling, the reproducibility badge set and opt-in deadline, dual-submission wording, and
  any AI-disclosure rule — all cycle-volatile; none should be assumed stable.

## Output format

```text
[CoNEXT submission status] ready / blocked / needs work
[Cycle] December / June, cutoff date + time zone
[Registration] title/abstract/authors/conflicts locked by the earlier deadline? yes/no
[Format] pages used (body/appendix/refs), acmart compliance
[Anonymity] clean / leaks: <where>
[Reproducibility] badge opt-in done before submission? artifact link present?
[Fix queue] <ordered, with owners and dates before the cutoff>
```
