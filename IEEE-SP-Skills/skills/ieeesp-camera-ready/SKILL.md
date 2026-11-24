---
name: ieeesp-camera-ready
description: Use when converting an IEEE S&P (Oakland) acceptance into a final paper, including working the shepherd against the draft meta-review's concern list, adding the ethics section, de-anonymizing and restoring disclosure specifics, IEEE compsoc and Xplore requirements, and coordinating artifact submission.
---

# IEEE S&P Camera-Ready

Use this after an Accept decision. S&P's camera-ready is not a formatting
pass: acceptance arrives with a **draft meta-review listing remaining
concerns and a shepherd who strikes each concern only when the revision
resolves it** (2027 CFP, re-verified 2026-11-24). The meta-review (< 500
words) is published in the final PDF, with an optional author response
(< 500 words). The camera-ready is due within one month of acceptance (2027:
shepherd submission Oct 2, 2026 / Mar 26, 2027; camera-ready Oct 16, 2026 /
Apr 8, 2027), must add the Ethics Considerations section and a
competing-interests disclosure, and is published open access in the Computer
Society Digital Library at once. Every accepted paper also presents a short
talk (5-7 minutes) and a poster at the symposium.

## Working the shepherding loop

1. Convert the draft meta-review into a numbered concern ledger on day one.
2. For each concern, agree internally on: the change, its location, and the
   one-line evidence the shepherd can check.
3. Ask the shepherd early about any concern you believe is out of scope or
   wrong — negotiation happens at the start, not at the deadline.
4. Submit the revision with a concern → change → location map; make the
   strike-through decision mechanical for the shepherd.
5. Nothing in the shepherding loop authorizes *new* claims: the accepted
   contribution is the contribution.

| Shepherd asks for | Right-sized response |
|---|---|
| Tone down claim X | Rewrite the claim to the evaluated boundary; show old/new text |
| Add limitation discussion | A titled paragraph, referenced from the intro |
| Clarify threat model edge | Amend §2 with the explicit assumption |
| Missing related system | Cite + one-line technical delta, not a new section |
| Ethics wording | Coordinate with the ethics section below |

## The ethics section is added now — and does not count

Accepted papers add a dedicated, well-marked ethics section **without it
counting against page limits** (2027 CFP wording, re-verified 2026-11-24). Write
it as a record, not a disclaimer:

- What could cause harm, to whom, and what you did about it.
- Responsible disclosure: who was notified, when, what they responded,
  current fix status — with the real names and dates now that anonymity has
  lifted.
- IRB approval or waiver, by institution and protocol ID, where applicable.
- Data handling: what PII existed, minimization, retention, who had access.

## De-anonymization with security-specific restorations

Beyond names, affiliations, acknowledgments, and first-person citations,
restore what anonymity forced you to blur:

- Vendor names and CVE identifiers in the disclosure narrative.
- Artifact URLs (repository, DOI deposit) replacing anonymized placeholders.
- Funding and infrastructure acknowledgments (measurement platforms often
  contractually require attribution).

```bash
# Residue sweep after de-anonymization
pdftotext final.pdf - | grep -inE 'anonym|redacted|omitted for (review|anonymity)|Vendor [A-Z]\b'
pdfinfo final.pdf | grep -iE 'title|author'   # metadata now correct, not blank
grep -rn 'REPLACE-AFTER-ACCEPT' . || true
```

## IEEE mechanics

The proceedings are published by IEEE; the compsoc template remains
mandatory. Confirmed in the 2027 CFP (re-verified 2026-11-24): the final paper
may be at most 18 pages, with extra pages only at the PC chairs' discretion;
accepted papers are published immediately, open access, in the Computer
Society Digital Library; one author is expected to register and present (a
short talk plus a poster). Still 待核实 on the author kit: the IEEE
copyright/eCF step and PDF-compliance checking.

## Sequence to the deadline

1. Concern ledger agreed with shepherd (week 1).
2. Content revisions + ethics section drafted (weeks 1–2).
3. De-anonymization and restoration sweep.
4. Artifact evaluation submission if opting in — its schedule runs off the
   acceptance date, in parallel (`ieeesp-artifact-evaluation`).
5. Final compsoc compile, IEEE PDF check, copyright form, upload.
6. Re-download and verify the archived PDF; Xplore keeps what you upload.

## Common failures at this stage

- Treating the meta-review as advisory — an unresolved concern is a
  shepherd-level blocker, not a style note.
- An ethics section written as legal boilerplate; reviewers approved a
  specific record and expect it stated.
- Disclosure narrative updated in the ethics section but not in the
  introduction, leaving contradictory timelines.
- Missing the artifact-evaluation registration window while polishing prose.

## Output format

```text
[Concern ledger] <n> total: resolved <n> · negotiating <n> · open <n>
[Ethics section] disclosure record ✓/✗ · IRB/waiver ✓/✗ · data handling ✓/✗
[De-anon sweep] names/CVEs/URLs restored ✓/✗ · residue found: <items>
[IEEE mechanics] deadline <date> · ≤18 pages · copyright/eCF 待核实 · talk + poster
[Artifact track] opted in? deadline <date>; badge targets <list>
```
