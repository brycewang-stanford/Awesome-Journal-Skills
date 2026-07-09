---
name: fast-submission
description: Use when auditing a USENIX FAST submission for HotCRP readiness, covering the choice between the Spring and Fall deadlines, abstract registration, the USENIX two-column template and 12-page (long) / 6-page (short) limit excluding references, double-blind anonymization, the artifact-availability story, and desk-reject triage before the AoE cutoff.
---

# FAST Submission

Run this audit before uploading to the FAST HotCRP site. FAST — the USENIX Conference on File and
Storage Technologies — publishes **open access via USENIX**, reviews **double-blind**, and runs
**two deadlines a year**. The first decision you make is not about the PDF but about *which
deadline* you are aiming at. Every number below was read from the FAST '26/'27 calls on 2026-07-09
via search renderings of the `usenix.org` URLs (see `resources/official-source-map.md`); treat them
as a one-cycle snapshot and reopen the live call first.

## Pick the deadline first

FAST '27 runs a **Spring** deadline (17 Mar 2026) and a **Fall** deadline (15 Sep 2026), each with
its own HotCRP instance, author-response window, and notification date. Consequences:

- Choose by readiness, not habit: a study that will be steady-state-solid in August targets **Fall**;
  do not rush it into a Spring slot it will fail.
- Register at the **right** HotCRP site — the Spring and Fall instances are different URLs; an
  abstract registered on the wrong one does not carry over.
- As of 2026-07-09 the live actionable target is the **FAST '27 Fall deadline, 15 Sep 2026**.

## Register the abstract early

FAST expects title, authors, abstract, and topics registered in HotCRP; some cycles require this a
few days before the full-paper cutoff. Register with the *real* title and abstract — they drive
reviewer bidding and PC match — not a placeholder you intend to swap.

## Format and page limit

- **USENIX two-column template** (LaTeX or Word), unmodified: 10-point on 12-point leading, a 7" x
  9" text block, 0.33" inter-column gap, US-letter. This is the USENIX path — not ACM `acmart`, not
  IEEE 10+2. Do not carry a two-column ACM/IEEE habit over.
- **Page limit (verify per cycle):** FAST '27 posts **≤12 pages for a long paper** and **≤6 pages
  for a short paper**, **excluding references** — the bibliography is uncapped and does not count.
  Camera-ready allowances are larger (reported 13 / 7 excluding references), so do not pad the
  submission toward the camera-ready size.
- Everything a reviewer must read to judge the paper lives in those pages; the artifact supports,
  it does not hold the argument.

## Double-blind sweep

FAST review is **double-blind**: anonymize the PDF and references and refer to your own prior work
in the **third person**. Storage papers leak identity through devices, tools, and traces, so the
surface is wide:

```bash
# Mechanical pass on the submission PDF and any anonymized artifact archive
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|zenodo\.org/record|our (system|lab|group)|acknowledg|grant' | head
unzip -l artifact.zip | grep -Ei '\.git/|\.DS_Store|/home/|/Users/|hostname' | head
grep -rni 'university\|@[a-z0-9.]*\.edu\|internal cluster\|<companyname>' artifact/ --include='*.md' | head
```

The storage-specific leaks: a system named after your lab or product, a cluster/hostname in a
config or SMART dump, a trace hosted on a personal or institutional URL, a datacenter name in a
field study, and commit metadata inside a zipped repository. Re-host artifacts and traces behind an
anonymizing location *before* upload.

## Availability story at submission time

USENIX values sharing. Concretely for the submission:

- State where the code, traces, and scripts will live and, where possible, provide an **anonymized**
  artifact or trace-replay bundle at review time.
- If something cannot be shared (proprietary drives under NDA, production traces with privacy
  limits), say so and why — a silent gap reads worse than a stated, justified exception.
- Pin device models, firmware, and trace identifiers now; they cannot be reconstructed later.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over the 12/6-page limit | Desk-reject-grade | Cut or move to the artifact; references don't absorb body text |
| Wrong template (ACM/IEEE, altered margins/font) | Named format-reject ground | Recompile in the USENIX template; recover space editorially |
| Identity leak in PDF, artifact, tool, or trace URL | Anonymity violation | Re-anonymize and re-host; scrub PDF and SMART/config metadata |
| Registered on the wrong deadline's HotCRP | No valid submission there | Re-register on the correct Spring/Fall instance before its cutoff |
| No device/firmware detail in the evaluation | Storage-soundness weakness | Add the testbed table before submission, not in rebuttal |
| Same work under review elsewhere | Concurrent-submission violation | Withdraw one venue; a one-shot revision also blocks parallel submission |

## Final-week order of operations

1. Confirm the target deadline (Spring/Fall) and its HotCRP URL and cutoff.
2. Freeze the body early; references can churn, the storage argument cannot.
3. Finalize the testbed table (devices, firmware, kernel, workloads/traces, device state).
4. Build the anonymized artifact/trace bundle and place its availability statement in the paper.
5. Run the mechanical double-blind checks on the *final* PDF and archive, not drafts.
6. Fill every HotCRP field — topics matching your evidence, conflicts for every coauthor's
   institution and recent collaborators — a day early.
7. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Both deadline dates and which HotCRP instance is live now.
- The page limit and which USENIX template revision is required.
- Artifact timing, one-shot-revision and shepherding wording, concurrent-submission rules, and any
  AI-disclosure policy — all cycle-volatile.

## Output format

```text
[FAST submission status] ready / blocked / needs work
[Target deadline] Spring / Fall <date + correct HotCRP URL>
[Registration] title/abstract/authors/topics/conflicts locked? yes/no
[Format] pages used (body/refs), USENIX template compliance
[Anonymity] clean / leaks: <where>
[Availability] artifact/trace bundle present? device+firmware provenance stated?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
